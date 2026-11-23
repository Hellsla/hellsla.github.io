/* Local store of the students' own solutions (teacher 2026-11-01, phase 2 of the solution editor, lesson.js part 6).
   Everything stays in this browser on this device (IndexedDB): no login, no cloud, nothing is sent anywhere.
   One record per task, keyed by the task's stable id (the exercise's <li id>, e.g. "fy3-3-L1-01", or a Sovella task's
   section id, e.g. "fy3-s1"): { id, html, page, updated }. `html` is the editor's own answer HTML, so text, line
   breaks, formulas (images with their LaTeX in alt) and pasted pictures come back as they were.
   Backup file: { format: "ruukkilabra-ratkaisut", version: 1, exported, solutions: [record, ...], progress? }.
   `progress` (teacher 2026-11-07) is the "Tehty" ticks of the assigned tasks (tehty.js, localStorage ruukkilabra:tehty,
   { v: 1, done: { id: ISO time }, log: [[id, ISO time, 1 | 0], ...] }); a restore merges it with this browser's.
   A record removed (an emptied editor, Poista ratkaisu, Poista kaikki) or restored dispatches "fl:pad-change" on
   document, { id, html? } or { all: true }, so tehty.js takes the tick off a task whose solution is gone.
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
  // the site's data kept as persistent (teacher 2026-11-08): the browser does not clear it by itself when the disk runs
  // low; asked once a page, after the first saved solution. Safari's 7-day rule may still apply there.
  let kept = false;
  const keep = () => { if (kept) return; kept = true; try { if (navigator.storage && navigator.storage.persist) navigator.storage.persisted().then((p) => p || navigator.storage.persist()).catch(() => {}); } catch (e) { /* not offered */ } };
  const valid = (r) => r && typeof r === 'object' && typeof r.id === 'string' && r.id && typeof r.html === 'string';
  const changed = (detail) => { try { document.dispatchEvent(new CustomEvent('fl:pad-change', { detail })); } catch (e) { /* no listener */ } };
  const DONE = 'ruukkilabra:tehty';
  const doneOf = (v) => (v && v.v === 1 && v.done && typeof v.done === 'object' && !Array.isArray(v.done) ? v : null);
  const readDone = () => { try { return doneOf(JSON.parse(localStorage.getItem(DONE))); } catch (e) { return null; } };
  // a backup's ticks into this browser's: a tick kept where this browser has none, the log merged by time
  // (replace: the backup's ticks win where both have one, teacher's work file "OK: korvaa")
  const mergeDone = (p, replace) => {
    const inp = doneOf(p);
    if (!inp) return;
    const own = readDone() || { v: 1, done: {}, log: [] };
    const iso = (t) => typeof t === 'string' && !isNaN(Date.parse(t));
    Object.keys(inp.done).forEach((id) => { if (typeof id === 'string' && iso(inp.done[id]) && (replace || !(id in own.done))) own.done[id] = inp.done[id]; });
    const seen = new Set((own.log || []).map((x) => x.join('|')));
    (Array.isArray(inp.log) ? inp.log : []).forEach((x) => { if (Array.isArray(x) && x.length === 3 && iso(x[1]) && !seen.has(x.join('|'))) { own.log.push([String(x[0]), x[1], x[2] ? 1 : 0]); seen.add(x.join('|')); } });
    own.log.sort((a, b) => (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0));
    try { localStorage.setItem(DONE, JSON.stringify(own)); } catch (e) { /* ticks stay as they were */ }
  };
  const clean = (r) => ({ id: r.id, html: r.html, page: typeof r.page === 'string' ? r.page : '', updated: typeof r.updated === 'string' ? r.updated : '' });

  // the time of each solution's first save (teacher 2026-11-07: the module page's graph, tehty.js): set once, gone with the solution
  const FIRST = 'ruukkilabra:ratkaistu';
  const first = (id, on) => {
    try {
      const m = id === null ? {} : JSON.parse(localStorage.getItem(FIRST) || '{}') || {};
      if (on && !m[id]) m[id] = new Date().toISOString(); else if (!on && id !== null) delete m[id]; else if (on) return;
      localStorage.setItem(FIRST, JSON.stringify(m));
    } catch (e) { /* the graph then uses the last save */ }
  };
  // One module's work in this browser (work queue 17b PR 1: moved here unchanged from palautus.js courseWork, so the
  // module's work file "ruukkilabra-tyo" v1 and the whole-site file "ruukkilabra-kaikki" v1, kaikki.js, read and write
  // it with the same code): which keys and solutions are the module's (CODE, "FY3"), reading them, and adding a file's
  // to this browser in two steps, plan (what differs) then apply (nothing is written before the caller has asked).
  // The module page's counter keeps two maps, one for every module: the file carries this module's part.
  const MAPS = ['ruukkilabra:ratkaistu', 'ruukkilabra:tarkistettu'];
  const work = (CODE) => {
    const PRE = CODE.toLowerCase() + '-';
    const KEY_RE = new RegExp('(^|[:/])' + CODE.toLowerCase() + '-[a-z0-9]', 'i');
    const plain = (k) => /^(fl:|ruukkilabra:)/.test(k) && k !== 'ruukkilabra:tehty' && !k.startsWith('ruukkilabra:palautus:') && KEY_RE.test(k);
    const ownKey = (k) => MAPS.includes(k) || plain(k);
    const readMap = (k) => { try { const v = JSON.parse(localStorage.getItem(k) || '{}'); return v && typeof v === 'object' && !Array.isArray(v) ? v : {}; } catch (e) { return {}; } };
    const ownRec = (r) => r && typeof r.id === 'string' && r.id.toLowerCase().startsWith(PRE);
    const readLocal = () => {
      const out = {};
      try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (plain(k)) out[k] = localStorage.getItem(k); } } catch (e) { /* no storage */ }
      MAPS.forEach((k) => { const m = readMap(k), ids = Object.keys(m).filter((id) => id.toLowerCase().startsWith(PRE)).sort();
        if (ids.length) out[k] = JSON.stringify(Object.fromEntries(ids.map((id) => [id, m[id]]))); });
      const sorted = {}; Object.keys(out).sort().forEach((k) => { sorted[k] = out[k]; });
      return sorted;
    };
    // what a checked file (sols: records, local: { key: text }, only the module's own) would change; rejects with code "open" when this browser cannot be read
    const plan = async (sols, local) => {   // local: { key: text }
      let mine, have = {};
      try { mine = new Map((await api.all(PRE)).solutions.map((r) => [r.id, r])); } catch (e) { throw fail('open', e); }
      try { localStorage.length; have = readLocal(); } catch (e) { throw fail('open', e); }
      const diffS = sols.filter((r) => mine.has(r.id) && mine.get(r.id).html !== r.html);
      const diffL = Object.keys(local).filter((k) => !MAPS.includes(k) && k in have && have[k] !== local[k]);
      const newer = diffS.filter((r) => (mine.get(r.id).updated || '') > (r.updated || '')).length;
      return { sols, local, mine, have, diffS, diffL, newer, differs: diffS.length + diffL.length };
    };
    // replace: the file's records win where both differ (OK in the question), else only what this browser lacks is added
    const apply = async (pl, replace) => {
      const { sols, local, mine, have } = pl;
      const putS = sols.filter((r) => !mine.has(r.id) || (replace && mine.get(r.id).html !== r.html));
      const putL = Object.keys(local).filter((k) => !MAPS.includes(k) && (!(k in have) || (replace && have[k] !== local[k])));
      try { if (putS.length) await api.putAll(putS); } catch (e) { throw fail('open', e); }
      try { putL.forEach((k) => localStorage.setItem(k, local[k])); } catch (e) { throw fail('open', e); }
      Object.keys(local).filter((k) => MAPS.includes(k)).forEach((k) => {   // added to this browser's map; an entry it has stays
        let add = {}; try { add = JSON.parse(local[k]) || {}; } catch (e) { /* nothing to add */ }
        const m = readMap(k); let n = 0;
        Object.keys(add).forEach((id) => { if (id.toLowerCase().startsWith(PRE) && !(id in m)) { m[id] = add[id]; n++; } });
        if (n) try { localStorage.setItem(k, JSON.stringify(m)); } catch (e) { /* the count misses them here */ }
      });
      return { n: putS.length, m: putL.length };
    };
    return { PRE, ownKey, ownRec, readMap, readLocal, plan, apply };
  };
  const api = {
    // the saved html of one task, '' when there is none; a damaged record rejects with code "corrupt"
    get: (id) => run('readonly', (s) => s.get(id)).then((r) => {
      if (r === undefined) return '';
      if (!valid(r)) throw fail('corrupt');
      return r.html;
    }),
    // an empty answer removes the record, so "delete everything" and an emptied editor leave nothing behind
    put: (id, html, page) => (html ? run('readwrite', (s) => s.put({ id, html, page: page || '', updated: new Date().toISOString() }))
                                   : run('readwrite', (s) => s.delete(id))).then((r) => { first(id, !!html); if (html) keep(); changed({ id, html: html || '' }); return r; }),
    remove: (id) => run('readwrite', (s) => s.delete(id)).then((r) => { first(id, false); changed({ id }); return r; }),
    clear: () => run('readwrite', (s) => s.clear()).then((r) => { first(null, false); changed({ all: true }); return r; }),
    // every intact record; damaged ones are counted, not returned
    // all(prefix): only the records whose id starts with it (a module, "fy3-"), read by key range so a module page
    // does not load every module's solutions and pictures (teacher 2026-11-08: FY1-FY8 in one browser)
    all: (prefix) => run('readonly', (s) => (prefix ? s.getAll(IDBKeyRange.bound(prefix, prefix + '\uffff')) : s.getAll())).then((rs) => ({ solutions: rs.filter(valid).map(clean), damaged: rs.filter((r) => !valid(r)).length })),
    backup: () => api.all().then(({ solutions }) => JSON.stringify(Object.assign({ format: FORMAT, version: VERSION, exported: new Date().toISOString(), solutions }, readDone() ? { progress: readDone() } : {}), null, 1)),
    // a backup file's text -> the records it holds, checked before anything is written; then all are written in one
    // transaction (all or nothing). A newer version than this page knows is refused rather than half read.
    restore: (text) => {
      let data;
      try { data = JSON.parse(text); } catch (e) { return Promise.reject(fail('format', e)); }
      if (!data || data.format !== FORMAT || typeof data.version !== 'number' || data.version > VERSION || !Array.isArray(data.solutions)) return Promise.reject(fail('format'));
      const rs = data.solutions.filter(valid).map(clean);
      return run('readwrite', (s) => { rs.forEach((r) => s.put(r)); return null; }).then(() => { mergeDone(data.progress); changed({ all: true }); return { restored: rs, skipped: data.solutions.length - rs.length }; });
    },
    // records written in one transaction, all or nothing (the work file, palautus.js)
    putAll: (rs) => { const ok = rs.filter(valid).map(clean); return run('readwrite', (s) => { ok.forEach((r) => s.put(r)); return null; }).then(() => { if (ok.length) keep(); changed({ all: true }); return ok.length; }); },
    mergeDone, readDone, work,
    FORMAT, VERSION,
  };
  window.flPadStore = api;
})();
