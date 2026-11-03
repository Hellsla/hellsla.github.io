/* Local store of the students' own solutions (teacher 2026-11-01, phase 2 of the solution editor, lesson.js part 6).
   Everything stays in this browser on this device (IndexedDB): no login, no cloud, nothing is sent anywhere.
   One record per task, keyed by the task's stable id (the exercise's <li id>, e.g. "fy3-3-L1-01", or a Sovella task's
   section id, e.g. "fy3-s1"): { id, html, page, updated }. `html` is the editor's own answer HTML, so text, line
   breaks, formulas (images with their LaTeX in alt) and pasted pictures come back as they were.
   Backup file: { format: "ruukkilabra-ratkaisut", version: 1, exported, solutions: [record, ...] }.
   Every call returns a promise; a failure rejects with an Error whose `code` is "unavailable", "quota", "corrupt",
   "format" or "failed", so the page can say what went wrong instead of claiming success. */
(() => {
  const DB = 'ruukkilabra-ratkaisut', STORE = 'solutions', FORMAT = 'ruukkilabra-ratkaisut', VERSION = 1;
  const fail = (code, cause) => { const e = new Error(code + (cause && cause.message ? ': ' + cause.message : '')); e.code = code; e.cause = cause; return e; };
  const codeOf = (e) => (e && (e.name === 'QuotaExceededError' || e.code === 22 || /quota/i.test(e.message || '')) ? 'quota' : 'failed');
  let dbp = null;
  const open = () => dbp || (dbp = new Promise((ok, no) => {
    let req;
    try { req = window.indexedDB.open(DB, 1); } catch (e) { no(fail('unavailable', e)); return; }
    req.onupgradeneeded = () => { if (!req.result.objectStoreNames.contains(STORE)) req.result.createObjectStore(STORE, { keyPath: 'id' }); };
    req.onsuccess = () => { const db = req.result; db.onversionchange = () => { db.close(); dbp = null; }; ok(db); };
    req.onerror = () => no(fail('unavailable', req.error));
    req.onblocked = () => no(fail('unavailable', new Error('blocked')));
  }).catch((e) => { dbp = null; throw e; }));
  // one transaction; resolves with the request's result when the transaction has committed (so "saved" is true)
  const run = (mode, work) => open().then((db) => new Promise((ok, no) => {
    let tx, req;
    try { tx = db.transaction(STORE, mode); req = work(tx.objectStore(STORE)); } catch (e) { no(fail(codeOf(e), e)); return; }
    tx.oncomplete = () => ok(req && req.result);
    tx.onabort = tx.onerror = () => no(fail(codeOf(tx.error || (req && req.error)), tx.error || (req && req.error)));
  }));
  const valid = (r) => r && typeof r === 'object' && typeof r.id === 'string' && r.id && typeof r.html === 'string';
  const clean = (r) => ({ id: r.id, html: r.html, page: typeof r.page === 'string' ? r.page : '', updated: typeof r.updated === 'string' ? r.updated : '' });

  const api = {
    // the saved html of one task, '' when there is none; a damaged record rejects with code "corrupt"
    get: (id) => run('readonly', (s) => s.get(id)).then((r) => {
      if (r === undefined) return '';
      if (!valid(r)) throw fail('corrupt');
      return r.html;
    }),
    // an empty answer removes the record, so "delete everything" and an emptied editor leave nothing behind
    put: (id, html, page) => (html ? run('readwrite', (s) => s.put({ id, html, page: page || '', updated: new Date().toISOString() }))
                                   : run('readwrite', (s) => s.delete(id))),
    remove: (id) => run('readwrite', (s) => s.delete(id)),
    clear: () => run('readwrite', (s) => s.clear()),
    // every intact record; damaged ones are counted, not returned
    all: () => run('readonly', (s) => s.getAll()).then((rs) => ({ solutions: rs.filter(valid).map(clean), damaged: rs.filter((r) => !valid(r)).length })),
    backup: () => api.all().then(({ solutions }) => JSON.stringify({ format: FORMAT, version: VERSION, exported: new Date().toISOString(), solutions }, null, 1)),
    // a backup file's text -> the records it holds, checked before anything is written; then all are written in one
    // transaction (all or nothing). A newer version than this page knows is refused rather than half read.
    restore: (text) => {
      let data;
      try { data = JSON.parse(text); } catch (e) { return Promise.reject(fail('format', e)); }
      if (!data || data.format !== FORMAT || typeof data.version !== 'number' || data.version > VERSION || !Array.isArray(data.solutions)) return Promise.reject(fail('format'));
      const rs = data.solutions.filter(valid).map(clean);
      return run('readwrite', (s) => { rs.forEach((r) => s.put(r)); return null; }).then(() => ({ restored: rs, skipped: data.solutions.length - rs.length }));
    },
    FORMAT, VERSION,
  };
  window.flPadStore = api;
})();
