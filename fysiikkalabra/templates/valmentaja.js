/* FY9-valmentaja, part (a): the evidence log (work queue 11b PR 3; docs/FY9_ADAPTIVE_PLAN.md sections 3, 4.4, 7.1).
   Invisible: it adds nothing to a page. On a FY9 unit page it listens to what the page already says and writes one row per
   attempt into one key of this browser, ruukkilabra:fy9-valmentaja:
     - fl:attempt (lesson.js, inquiry.js): a checked number or a choice (automatic), a written solution (done)
     - fl:rubric (selfassess.js, inquiry.js): the points the student gave their own answer (self-assessed)
     - the opening of a hint (details.hint): counted, so an attempt after hints is told apart from one without
   The log is { v: 1, log: [[time, task, way, result, first, hints, mistake, mode], ...] }:
     time     "2026-11-20T18:04Z" (UTC, minutes)
     task     "<unit>#<activity id>" for a short task (the ids lt-1, tarkistus-2 repeat in every unit, so never bare), the task's own id
              "fy9-voimat-s1" for a long one
     way      "a" the page checked it · "s" the student's own assessment (or a written solution marked done: result null)
     result   "ok" | "close" | "no" for "a"; points got / max, 0 to 1, for "s"
     first    1 the first attempt at the task (the only one that counts as evidence, plan 5.1), 0 a later one
     hints    how many hints of the task had been opened on this page when the attempt was made
     mistake  the number of the option picked (a wrong choice) or of the common mistake matched (a number), else null
     mode     "p" practice ("k", exam mode, comes with its own pull request)
   No name, no device id, no text the student wrote, nothing sent anywhere: this file has no network call (scripts/test_valmentaja_log.py
   checks it). Other keys of this log (cells, steps, plan, exams) belong to later pull requests and are kept as they are.
   Keeping it works without storage (a private window, a full or blocked store): the page is as before. The key name matches the
   module's work file (padstore.js work(): "…:fy9-…"), so Tallenna työ tiedostoon and Avaa tallennettu työ carry it. */
(() => {
  const KEY = 'ruukkilabra:fy9-valmentaja', MAX_LOG = 3000, MAX_CHARS = 1500000;
  const unit = (location.pathname.match(/(?:^|\/)(fy9-[a-z0-9]+(?:-[a-z0-9]+)*?)(?:\.html)?$/) || [])[1];
  if (!unit) return;
  const TASK = '#exercises li[id], section.practice-task[id], .activity[id]';
  const LONG = /^fy9-[a-z0-9-]+-s\d+$/;
  const isRow = (r) => Array.isArray(r) && r.length === 8 && typeof r[0] === 'string' && typeof r[1] === 'string' && (r[2] === 'a' || r[2] === 's')
    && (r[3] === null || typeof r[3] === 'string' || (typeof r[3] === 'number' && r[3] >= 0 && r[3] <= 1)) && (r[4] === 0 || r[4] === 1)
    && Number.isInteger(r[5]) && r[5] >= 0 && (r[6] === null || Number.isInteger(r[6])) && (r[7] === 'p' || r[7] === 'k');
  // what this browser holds, checked against the format; null where it cannot be used and must not be overwritten (damaged, or a newer version)
  const read = () => {
    let raw = null;
    try { raw = localStorage.getItem(KEY); } catch (e) { return null; }
    if (raw === null) return { v: 1, log: [] };
    if (raw.length > MAX_CHARS) return null;
    let d; try { d = JSON.parse(raw); } catch (e) { return null; }
    if (!d || typeof d !== 'object' || Array.isArray(d) || d.v !== 1 || !Array.isArray(d.log)) return null;
    d.log = d.log.filter(isRow);
    return d;
  };
  let canStore = true;
  const write = (d) => {
    if (d.log.length > MAX_LOG) d.log = d.log.slice(d.log.length - MAX_LOG);   // the oldest go first (summarising them into cells comes with the coach's model)
    for (let tries = 0; tries < 2; tries++) {
      try { localStorage.setItem(KEY, JSON.stringify(d)); canStore = true; return true; }
      catch (e) { d.log = d.log.slice(Math.ceil(d.log.length / 10)); }   // a full store: drop the oldest tenth once and try again
    }
    canStore = false; return false;
  };
  const taskKey = (id) => (LONG.test(id) ? id : unit + '#' + id);
  const now = () => new Date().toISOString().slice(0, 16) + 'Z';
  // hints opened on this page, per task (a toggle does not bubble, so it is heard in the capture phase)
  const hints = new Map();
  document.addEventListener('toggle', (e) => {
    const h = e.target;
    if (!h || !h.matches || !h.matches('details.hint') || !h.open) return;
    const t = h.closest(TASK); if (!t || !t.id) return;
    const s = hints.get(t.id) || new Set(); s.add(h.dataset.n || String(s.size + 1)); hints.set(t.id, s);
  }, true);
  const opened = (id) => (hints.get(id) || new Set()).size;
  const log = (row, replace) => {
    const d = read(); if (!d) { canStore = false; return; }
    const k = row[1];
    if (replace) { for (let i = d.log.length - 1; i >= 0; i--) if (d.log[i][1] === k && d.log[i][2] === 's' && d.log[i][3] !== null) { row[0] = d.log[i][0]; row[4] = d.log[i][4]; d.log[i] = row; write(d); return; } }
    d.log.push(row); write(d);
  };
  const firstOf = (d, k, way) => (d ? !d.log.some((r) => r[1] === k && r[2] === way && (way === 'a' || r[3] !== null)) : true);
  document.addEventListener('fl:attempt', (e) => {
    const det = e.detail || {}; if (!det.id) return;
    setTimeout(() => {   // a moment later: inquiry.js has then said which common mistake the number was (detail.mistake)
      const k = taskKey(det.id), d = read();
      if (det.kind === 'done') {   // a written solution, done: no result, only that it was made (once)
        if (d && !d.log.some((r) => r[1] === k && r[2] === 's' && r[3] === null)) log([now(), k, 's', null, firstOf(d, k, 's') ? 1 : 0, opened(det.id), null, 'p']);
        return;
      }
      if (det.state !== 'ok' && det.state !== 'close' && det.state !== 'no') return;
      const miss = det.kind === 'choice' ? (det.state === 'no' && Number.isInteger(det.choice) ? det.choice : null) : (Number.isInteger(det.mistake) ? det.mistake : null);
      log([now(), k, 'a', det.state, firstOf(d, k, 'a') ? 1 : 0, opened(det.id), miss, 'p']);
    }, 0);
  });
  document.addEventListener('fl:rubric', (e) => {
    const det = e.detail || {}; if (!det.id || !det.complete || !(det.max > 0)) return;
    const k = taskKey(det.id), d = read();
    const result = Math.round(100 * Math.max(0, Math.min(1, det.got / det.max))) / 100;
    log([now(), k, 's', result, firstOf(d, k, 's') ? 1 : 0, opened(det.id), null, 'p'], true);   // changing the points revises the same assessment
  });
  window.flValmentaja = { KEY, unit, read, canStore: () => canStore };
})();
