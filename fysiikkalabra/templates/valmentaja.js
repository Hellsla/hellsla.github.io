/* FY9-valmentaja (docs/FY9_ADAPTIVE_PLAN.md sections 3, 4.4, 5, 6, 7.1). Part (a), the evidence log (work queue 11b PR 3), is invisible; parts (b) to (d), the competence model,
   the recommendations and the coach page with its row on FY9.html (PR 4), are at the end of this file.
   (a) Invisible: it adds nothing to a page. On a FY9 unit page it listens to what the page already says and writes one row per
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
    if (!unit) return;
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
    if (!unit) return;
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
    if (!unit) return;
    const det = e.detail || {}; if (!det.id || !det.complete || !(det.max > 0)) return;
    const k = taskKey(det.id), d = read();
    const result = Math.round(100 * Math.max(0, Math.min(1, det.got / det.max))) / 100;
    log([now(), k, 's', result, firstOf(d, k, 's') ? 1 : 0, opened(det.id), null, 'p'], true);   // changing the points revises the same assessment
  });
  // "Mikä vaihe oli vaikein?" (PR 5, plan 6.3): once a number task's solution or a long task's model answer is open, an optional row of chips from a fixed
  // list; a chip pressed again is taken back. Kept in the same key as steps { "<task key>": ["sijoitus", ...] }, on this device only, never
  // in the teacher's view (palautus_tasks.py takes every details out of a task). The row is made when the solution first opens, so the page is as
  // before until then; where nothing can be stored (read gives null) there is no row.
  const SCRIPT = document.currentScript;
  const STEPS = ['tulkinta', 'annettu', 'periaate', 'kaava', 'muunnokset', 'sijoitus', 'vastaus', 'jarkevyys', 'kuvaaja'];
  const stepsOf = (d, k) => (d && d.steps && typeof d.steps === 'object' && Array.isArray(d.steps[k]) ? d.steps[k].filter((x) => STEPS.includes(x)) : []);
  const setStep = (k, id, on) => {
    const d = read(); if (!d) return false;
    const steps = d.steps && typeof d.steps === 'object' && !Array.isArray(d.steps) ? d.steps : {};
    const mine = new Set(stepsOf({ steps }, k)); on ? mine.add(id) : mine.delete(id);
    if (mine.size) steps[k] = STEPS.filter((x) => mine.has(x)); else delete steps[k];
    if (Object.keys(steps).length) d.steps = steps; else delete d.steps;
    return write(d);
  };
  let UI = null; try { UI = JSON.parse(SCRIPT && SCRIPT.dataset.t || 'null'); } catch (e) { UI = null; }
  if (UI && UI.steps) document.addEventListener('toggle', (e) => {
    const box = e.target;
    if (!unit || !box || !box.matches || !box.open || box.querySelector('.hardstep')) return;
    if (!box.matches('details.solution') && !box.matches('.practice-task > details.reveal')) return;
    const task = box.closest(TASK); if (!task || !task.id || !read()) return;
    const k = taskKey(task.id), row = document.createElement('div'), q = document.createElement('p'), chips = document.createElement('div');
    row.className = 'hardstep'; row.setAttribute('role', 'group'); q.className = 'hardstep-q'; q.id = 'hs-' + task.id; q.textContent = UI.q;
    row.setAttribute('aria-labelledby', q.id); chips.className = 'hardstep-chips';
    for (const id of STEPS) {
      const b = document.createElement('button'), on = stepsOf(read(), k).includes(id);
      b.type = 'button'; b.className = 'hardstep-chip'; b.dataset.step = id; b.textContent = UI.steps[id] || id; b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.addEventListener('click', () => {
        const want = b.getAttribute('aria-pressed') !== 'true';
        if (setStep(k, id, want)) b.setAttribute('aria-pressed', want ? 'true' : 'false');
      });
      chips.append(b);
    }
    row.append(q, chips);
    const into = box.querySelector(':scope > .reveal-body') || box, rub = into.querySelector(':scope > .rubric');   // a long task: before the points the student gives, after the solution
    rub ? into.insertBefore(row, rub) : into.append(row);
  }, true);
  window.flValmentaja = { KEY, unit, read, write, canStore: () => canStore, stepsOf, STEPS };
})();

/* (e) the goal and the courses taken (work queue 11b PR 4b, P13): the student's own two settings under the key ruukkilabra:fy9-tavoite
   { v: 1, goal: "LE" | "MC" | "BA" | null, courses: [1..8] }, this device only, carried by the whole-work file (the key names fy9-) and removed by
   Tyhjennä. The goal changes what is recommended, never a state word, and locks nothing; no grade is shown or predicted (R10). Courses: when any
   is ticked, a unit whose home course (index unit.course; the exam units have none) is not ticked is left out of the recommendations and the table.
   (b) the competence model, (c) the recommendations, (d) the views (work queue 11b PR 4; plan sections 5 and 6).
   The model and the recommendations are pure functions of the log, the task index and a day: window.flCoach.cells(log, index, today, summary)
   and window.flCoach.recommend(index, d, today, opts); the tests run them on fixed logs (scripts/test_valmentaja_coach.py). No
   randomness (a tie goes by the order of the course), no model at run time, nothing sent. The index is in the page itself
   (<script type="application/json" id="fy9-index">, the FY9 task index of this language), so the page works offline.
   Only the first attempt at a task is evidence (plan 5.1); later attempts are practice. A day is the student's own local day. */
(() => {
  const V = window.flValmentaja;
  if (!V) return;
  const DAY = 86400000, STEPS = [1, 2, 5, 10, 20], LAST = 6, FADE = 0.8;
  const pad = (n) => String(n).padStart(2, '0');
  const ymd = (d) => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
  const num = (s) => { const [y, m, d] = s.split('-').map(Number); return Math.round(Date.UTC(y, m - 1, d) / DAY); };
  const str = (n) => new Date(n * DAY).toISOString().slice(0, 10);
  const dayOf = (iso) => { const d = new Date(iso); return isNaN(d) ? null : ymd(d); };
  const today = () => ymd(new Date());
  const COMPS = ['concept', 'math', 'graph', 'experiment', 'communication', 'transfer'];
  const compsOf = (t) => (Array.isArray(t.comp) ? t.comp : Object.keys(t.comp || {})).filter((c) => COMPS.includes(c));

  // the weight of one attempt (plan 5.1): its result r and how far it can be trusted w. A choice can be guessed (0.7), an opened hint
  // lowers a right answer (0.6), a self-assessed rubric counts 0.6 and an explanation's own ticks 0.4, an exam-mode result 1.2 times
  const attempt = (row, task) => {
    let r, w;
    if (row[2] === 'a') {
      r = row[3] === 'ok' ? (row[5] > 0 ? 0.6 : 1) : row[3] === 'close' ? 0.5 : row[3] === 'no' ? 0 : null;
      w = task.kind === 'numeric' ? 1 : 0.7;
    } else {
      r = typeof row[3] === 'number' ? row[3] : null;
      w = task.kind === 'explain' ? 0.4 : 0.6;
    }
    if (r === null) return null;
    return { r, w: row[7] === 'k' ? w * 1.2 : w, auto: row[2] === 'a' || row[7] === 'k' };
  };

  // [{cell: "<unit>|<competency>", task, t, day, r, w, auto}] in time order: the first attempts of the tasks this index knows
  const evidence = (log, index) => {
    const by = new Map(index.tasks.map((t) => [t.id, t]));
    const out = [];
    log.forEach((row, i) => {
      if (row[4] !== 1) return;
      const task = by.get(row[1]), day = dayOf(row[0]);
      if (!task || !day) return;
      const a = attempt(row, task); if (!a) return;
      for (const c of compsOf(task)) out.push({ cell: task.unit + '|' + c, task: task.id, t: row[0], i, day, ...a });
    });
    return out.sort((x, y) => (x.t < y.t ? -1 : x.t > y.t ? 1 : x.i - y.i));
  };

  // the revisit schedule of one cell (plan 5.3): a day's result is its weighted mean; a result of 0.8 or more moves the interval up
  // 1 -> 2 -> 5 -> 10 -> 20 days, under 0.5 it is 1 day again, else it stays; next = that day + the interval
  const schedule = (days, from) => {
    let k = from && Number.isInteger(from.step) ? Math.max(0, Math.min(STEPS.length - 1, from.step)) : 0, next = from && from.next || null;
    for (const [day, r] of days) {
      k = r >= 0.8 ? Math.min(k + 1, STEPS.length - 1) : r < 0.5 ? 0 : k;
      next = str(num(day) + STEPS[k]);
    }
    return { step: k, next };
  };
  const perDay = (evs) => {
    const m = new Map();
    for (const e of evs) { const a = m.get(e.day) || [0, 0]; a[0] += e.r * e.w; a[1] += e.w; m.set(e.day, a); }
    return [...m].map(([d, [s, w]]) => [d, s / w]).sort((x, y) => (x[0] < y[0] ? -1 : 1));
  };
  // a cell summary kept when old log rows are folded away: { next, step, ev: [[day, r, w, auto], ...] } (the last six attempts)
  const fromSummary = (c) => (c && Array.isArray(c.ev) ? c.ev.filter((e) => Array.isArray(e) && typeof e[0] === 'string' && e[1] >= 0 && e[1] <= 1 && e[2] > 0).map((e) => ({ day: e[0], r: e[1], w: e[2], auto: !!e[3], task: '' })) : []);

  // the state of every cell that has a task: { "<unit>|<comp>": { state, M, W, n, days, own, next, due, last } }
  const cells = (log, index, todayStr, summary) => {
    const evs = evidence(log, index), mine = {};
    for (const e of evs) (mine[e.cell] = mine[e.cell] || []).push(e);
    const out = {};
    for (const t of index.tasks) for (const c of compsOf(t)) {
      const k = t.unit + '|' + c; if (out[k]) continue;
      const sum = summary && summary[k], old = fromSummary(sum), all = old.concat(mine[k] || []), last = all.slice(-LAST);
      let W = 0, S = 0, R = 0;
      last.forEach((e, j) => { const rec = Math.pow(FADE, last.length - 1 - j); W += e.w; S += rec * e.w * e.r; R += rec * e.w; });
      const M = R ? S / R : 0, days = new Set(last.map((e) => e.day)).size, auto = last.some((e) => e.auto);
      const sch = schedule(perDay(mine[k] || []), old.length ? sum : null);   // a summary already holds its own days' steps
      const due = !!(sch.next && num(sch.next) <= num(todayStr));
      let state = W === 0 ? 'none' : W < 2 ? 'few' : M < 0.5 ? 'practise' : M < 0.8 ? 'growing' : (W >= 3 && days >= 2 && auto) ? (due ? 'strongdue' : 'strong') : 'growing';
      out[k] = { state, M, W, n: new Set(last.map((e) => e.task || e.day)).size, days, own: all.length > 0 && !auto, next: sch.next, step: sch.step, due, last: all.length ? all[all.length - 1] : null };
    }
    return out;
  };

  // the three tasks to do next (plan 5.4). Candidates: tasks not touched in the last 7 days that fit the minutes left (opts.budget, none = any).
  // score = 3 need + 2 due + 2 follow-up + 1 new (the day's path, 1.5, comes with the revisit path); at most one task per cell, two per unit, and one
  // the page checks when some cell needs work (need 0.5 or more); a tie goes by the order of the course, then of the page.
  const recommend = (index, d, todayStr, opts) => {
    opts = opts || {};
    const log = d.log || [], goal = GOALS.includes(opts.goal) ? opts.goal : null, t0 = num(todayStr);
    const have = evidence(log, index);   // the diagnostic is offered on the evidence of the whole index, whatever the courses
    index = within(index, opts.courses);
    const cs = cells(log, index, todayStr, d.cells);
    if (!have.length && !Object.keys(d.cells || {}).length) return { diag: true, recs: [], cells: cs };
    const touched = new Map();
    for (const r of log) { const day = dayOf(r[0]); if (day && (!touched.has(r[1]) || touched.get(r[1]) < day)) touched.set(r[1], day); }
    const wrong = new Set();
    for (const e of have) if (e.r < 0.5 && t0 - num(e.day) <= 3) wrong.add(e.task);
    const follow = new Set(index.tasks.filter((t) => wrong.has(t.id)).flatMap((t) => t.followups || []));
    const order = new Map(index.units.map((u, i) => [u.id, i]));
    const cand = [];
    index.tasks.forEach((t, i) => {
      const seen = touched.get(t.id);
      if (seen && t0 - num(seen) < 7) return;
      if (opts.budget != null && t.min > opts.budget) return;
      let best = null;
      for (const c of compsOf(t)) {
        const cell = cs[t.unit + '|' + c], need = cell.W === 0 ? 0.6 : goal && sufficient(goal, c) && cell.W >= 2 && cell.M >= 0.5 ? 0 : 1 - cell.M, pull = 3 * need + (cell.due ? 2 : 0);   // the cell that needs the task most: of a task of several competencies
        if (!best || pull > best.pull) best = { key: t.unit + '|' + c, cell, need, pull };
      }
      if (!best) return;
      const terms = { need: 3 * best.need, due: best.cell.due ? 2 : 0, wrong: follow.has(t.id) ? 2 : 0, fresh: seen ? 0.3 : 1 };
      const score = terms.need + terms.due + terms.wrong + terms.fresh + (goal && fits(goal, t) ? 1.5 : 0);
      cand.push({ task: t, i, score, key: best.key, cell: best.cell, need: best.need, terms });
    });
    cand.sort((a, b) => b.score - a.score || (order.get(a.task.unit) - order.get(b.task.unit)) || a.i - b.i);
    const ok = (set, c) => !set.some((x) => x.key === c.key) && set.filter((x) => x.task.unit === c.task.unit).length < 2;
    let pick = [];
    const lim = goal ? LIMIT_OF[goal] : {}, within_ = (set, c) => Object.keys(lim).every((k) => set.filter((x) => klass(x.task).includes(k)).length + (klass(c.task).includes(k) ? 1 : 0) <= lim[k]);
    for (const c of cand) { if (pick.length >= 3) break; if (ok(pick, c) && within_(pick, c)) pick.push(c); }
    for (const c of cand) { if (pick.length >= 3) break; if (!pick.includes(c) && ok(pick, c)) pick.push(c); }   // the mix is a wish: a short list is filled
    pick.sort((a, b) => cand.indexOf(a) - cand.indexOf(b));
    if (pick.some((c) => c.need >= 0.5) && !pick.some((c) => c.task.check === 'auto')) {
      const rest = pick.slice(0, -1), a = cand.find((c) => c.task.check === 'auto' && ok(rest, c));
      if (a) pick = rest.concat(a);
    }
    const recs = pick.map((c) => {
      const t = c.terms; let key = 'more', days = 0;
      if (t.wrong && t.wrong >= t.due && t.wrong >= t.need) key = 'wrong';
      else if (t.due && t.due >= t.need) { key = 'stale'; days = c.cell.last ? Math.max(1, t0 - num(c.cell.last.day)) : 1; }
      else if (c.cell.W === 0) key = 'new';
      return { id: c.task.id, task: c.task, cell: c.key, reason: { key, days }, score: Math.round(c.score * 100) / 100 };
    });
    return { diag: false, recs, cells: cs };
  };

  // old log rows folded into the cells' summaries (the page that holds the index does it: a unit page has none): the oldest rows go, what the
  // model needs of them stays (the last six attempts of each cell and its revisit schedule, plan 4.4)
  const LIMIT = 2000, KEEP = 1500;
  const compact = (d, index) => {
    if (d.log.length <= LIMIT) return false;
    const gone = d.log.slice(0, d.log.length - KEEP), by = {};
    d.cells = d.cells && typeof d.cells === 'object' && !Array.isArray(d.cells) ? d.cells : {};
    for (const e of evidence(gone, index)) (by[e.cell] = by[e.cell] || []).push(e);
    for (const k of Object.keys(by)) {
      const old = d.cells[k], all = fromSummary(old).concat(by[k]), sch = schedule(perDay(by[k]), old);
      d.cells[k] = { next: sch.next, step: sch.step, ev: all.slice(-LAST).map((e) => [e.day, Math.round(e.r * 100) / 100, Math.round(e.w * 100) / 100, e.auto ? 1 : 0]) };
    }
    d.log = d.log.slice(d.log.length - KEEP);
    return true;
  };
  // the settings (PR 4b): read leniently, written only by the student's own choice
  const SET_KEY = 'ruukkilabra:fy9-tavoite', GOALS = ['LE', 'MC', 'BA'], CORE = ['concept', 'math', 'graph'];
  const readSet = () => {
    try {
      const o = JSON.parse(localStorage.getItem(SET_KEY));
      if (o && o.v === 1) return { goal: GOALS.includes(o.goal) ? o.goal : null, courses: [...new Set((Array.isArray(o.courses) ? o.courses : []).filter((c) => Number.isInteger(c) && c >= 1 && c <= 8))].sort((a, b) => a - b) };
    } catch (e) { /* none or damaged: no settings */ }
    return { goal: null, courses: [] };
  };
  const writeSet = (st) => {
    try {
      if (!st.goal && !st.courses.length) localStorage.removeItem(SET_KEY); else localStorage.setItem(SET_KEY, JSON.stringify({ v: 1, goal: st.goal || null, courses: st.courses }));
      return true;
    } catch (e) { return false; }
  };
  // the index of the courses taken: no courses ticked is the whole index
  const within = (index, courses) => {
    if (!courses || !courses.length) return index;
    const units = index.units.filter((u) => !u.course || courses.includes(u.course)), ids = new Set(units.map((u) => u.id));
    return Object.assign({}, index, { units, tasks: index.tasks.filter((t) => ids.has(t.unit)) });
  };
  // what each goal asks of a cell and of the three (plan PR 4b): a state that is enough for the goal stops pulling, a task kind that fits adds
  // 1.5, and a limit keeps the mix (B-A no long task while short ones are left, M-C at most two long and two short, L-E at most one task the page checks by itself)
  const sufficient = (goal, comp) => goal === 'BA' || (goal === 'MC' && !CORE.includes(comp));
  const fits = (goal, t) => (goal === 'BA' ? t.check === 'auto' && t.kind !== 'long' : goal === 'LE' ? ['long', 'explain', 'interpret'].includes(t.kind) : false);
  const LIMIT_OF = { BA: { long: 0 }, MC: { long: 2, short: 2 }, LE: { plain: 1 } };
  const klass = (t) => [t.kind === 'long' ? 'long' : 'short', t.kind === 'choice' || t.kind === 'numeric' ? 'plain' : ''];
  // the mistakes that came back (PR 5, plan 6.2.3): a wrong option or a common mistake counts when the same one was hit at least twice, in any attempt;
  // options that the side file groups as one misconception (index.misconceptions, "<task>/<number>") count together. [{task, n, mistake, grp}] most
  // often first, a tie by the latest hit; the page shows the existing feedback of that option, nothing new
  const repeated = (log, index) => {
    const by = new Map(index.tasks.map((t) => [t.id, t])), grp = new Map();
    for (const [name, g] of Object.entries(index.misconceptions || {})) for (const it of (g && g.items) || []) grp.set(it, name);
    const hit = new Map();
    log.forEach((r, i) => {
      if (!Number.isInteger(r[6]) || !by.has(r[1])) return;
      const pair = r[1] + '/' + r[6], key = grp.get(pair) || pair, h = hit.get(key) || { n: 0 };
      h.n++; h.last = i; h.task = r[1]; h.mistake = r[6]; hit.set(key, h);
    });
    return [...hit.values()].filter((h) => h.n >= 2).sort((a, b) => b.n - a.n || b.last - a.last);
  };
  // the steps the student marked as the hardest, in the order of the list: [[step, [task id, ...]], ...] (a task the index no longer knows is left out)
  const hardSteps = (d, index) => {
    const known = new Set(index.tasks.map((t) => t.id)), s = d && d.steps && typeof d.steps === 'object' ? d.steps : {};
    return V.STEPS.map((id) => [id, Object.keys(s).filter((k) => known.has(k) && Array.isArray(s[k]) && s[k].includes(id))]).filter((x) => x[1].length);
  };
  window.flCoach = { cells, recommend, compact, evidence, today, COMPS, readSet, writeSet, within, SET_KEY, GOALS, repeated, hardSteps };

  // ---- (d) the views ----
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const fmt = (s, v) => String(s || '').replace(/\{(\w+)\}/g, (m, k) => (v && k in v ? v[k] : m));
  const json = (id) => { const e = document.getElementById(id); try { return e ? JSON.parse(e.textContent) : null; } catch (x) { return null; } };
  const index = json('fy9-index');
  const page = document.getElementById('fy9-coach'), row = document.getElementById('fy9-coach-row');
  if (!index || !Array.isArray(index.tasks) || !(page || row)) return;
  const host = page || row, T = (() => { try { return JSON.parse(host.dataset.t || '{}'); } catch (e) { return {}; } })();
  const data = () => V.read() || { v: 1, log: [] };
  const rank = (d) => { const e = evidence(d.log, index); return e.length || Object.keys(d.cells || {}).length; };
  const minutes = (recs) => recs.reduce((s, r) => s + (r.task.min || 0), 0);
  const where = (t) => { const u = index.units.find((x) => x.id === t.unit); return u ? (u.n ? fmt(T.chapter, { n: u.n }) + ' ' : '') + u.title : ''; };
  const reason = (r) => (r.key === 'stale' ? fmt(T.why_stale, { n: r.days }) : T['why_' + r.key] || '');
  const SYMBOL = { none: '○', few: '◔', practise: '▲', growing: '◑', strong: '●', strongdue: '●' };

  if (row) {
    const st = readSet(), d = data(), res = recommend(index, d, today(), { goal: st.goal, courses: st.courses });
    if (res.diag || !res.recs.length) return;
    const n = res.recs.length, go = el('a', 'resume-go', T.go); go.href = row.dataset.href || 'FY9-valmentaja.html';
    row.replaceChildren(go, el('p', 'resume-text', fmt(n === 1 ? T.row_one : T.row_n, { n, m: Math.round(minutes(res.recs) / 5) * 5 || minutes(res.recs) })));
    row.hidden = false;
    return;
  }

  // the coach page
  const d = data(), t = today();
  if (compact(d, index)) V.write(d);   // (a damaged or newer log is not compacted: data() is then empty and is never written)
  let st = readSet();
  const next = document.getElementById('coach-recs'), areas = document.getElementById('coach-areas');
  const render = () => {
    const res = recommend(index, d, t, { goal: st.goal, courses: st.courses });
    if (next) {
      if (res.diag) {
        const a = el('a', 'coach-go', T.diag); a.href = page.dataset.diag || 'fy9-koe.html'; next.replaceChildren(a);
      } else {
        const ol = el('ol', 'coach-recs');
        for (const r of res.recs) {
          const li = el('li', 'coach-rec'), a = el('a', 'coach-task', r.task.title); a.href = r.task.href;
          li.append(a, el('span', 'coach-where', where(r.task)), el('span', 'coach-min', fmt(T.min, { n: r.task.min })), el('span', 'coach-why', reason(r.reason)));
          ol.append(li);
        }
        next.replaceChildren(ol);
      }
    }
    if (areas && !res.diag) {
      const names = T.comp || {}, unitName = (id) => { const u = index.units.find((x) => x.id === id); return u ? (u.n ? u.n + ' ' : '') + u.title : id; };
      const box = document.createDocumentFragment(), shown = within(index, st.courses).units;
      for (const c of COMPS) {
        const mine = shown.map((u) => [u.id, res.cells[u.id + '|' + c]]).filter((x) => x[1]);
        if (!mine.length) continue;
        const count = {}; mine.forEach(([, s]) => { count[s.state] = (count[s.state] || 0) + 1; });
        const det = el('details', 'coach-comp'), sum = el('summary'), tab = el('table', 'coach-table');
        sum.append(el('span', 'coach-comp-name', names[c] || c));
        const strong = (count.strong || 0) + (count.strongdue || 0);
        sum.append(el('span', 'coach-comp-sum', [strong && T.state_strong + ' ' + strong, count.growing && T.state_growing + ' ' + count.growing, count.practise && T.state_practise + ' ' + count.practise].filter(Boolean).join(' · ') || T.state_none));
        const body = el('tbody');
        for (const [id, s] of mine) {
          const tr = el('tr'), th = el('th', '', unitName(id)); th.scope = 'row';
          const td = el('td', 'coach-state s-' + s.state), word = el('span', 'coach-word', T['state_' + s.state]);
          td.append(el('span', 'coach-mark', SYMBOL[s.state]), word);
          if (s.W > 0) td.append(el('span', 'coach-basis', fmt(T.basis, { n: s.n, d: s.days }) + (s.own ? ' · ' + T.own : '')));
          td.querySelector('.coach-mark').setAttribute('aria-hidden', 'true');
          tr.append(th, td); body.append(tr);
        }
        tab.append(body); det.append(sum, tab); box.append(det);
      }
      const holder = areas.querySelector('.coach-areas-body');
      holder.replaceChildren(box, el('p', 'coach-note', T.note));
      areas.hidden = false;
    }
  };
  render();

  // the two settings (PR 4b): saved the moment they change, on this device only
  const set = document.getElementById('coach-set');
  if (set) {
    const save = () => { const ok = writeSet(st); if (!ok) note.hidden = false; render(); showClear(); };
    const goals = el('fieldset', 'coach-opts'), gl = el('legend', '', T.goal_lead);
    goals.append(gl);
    for (const g of [''].concat(GOALS)) {
      const lab = el('label', 'coach-opt'), r = el('input'); r.type = 'radio'; r.name = 'coach-goal'; r.value = g; r.checked = (st.goal || '') === g;
      r.addEventListener('change', () => { st.goal = g || null; save(); });
      lab.append(r, el('span', '', g ? T['goal_' + g] : T.goal_none)); goals.append(lab);
    }
    const cs = el('fieldset', 'coach-opts coach-courses'), cl = el('legend', '', T.courses_h);
    cs.append(cl, el('p', 'coach-set-lead', T.courses_lead + ' ' + T.courses_none));
    const grid = el('div', 'coach-course-grid');
    for (let n = 1; n <= 8; n++) {
      const lab = el('label', 'coach-opt'), c = el('input'); c.type = 'checkbox'; c.value = String(n); c.checked = st.courses.includes(n);
      c.addEventListener('change', () => { st.courses = [...grid.querySelectorAll('input:checked')].map((x) => Number(x.value)); save(); });
      lab.append(c, el('span', '', 'FY' + n)); grid.append(lab);
    }
    cs.append(grid);
    const note = el('p', 'notice', T.nostore); note.hidden = true;
    set.querySelector('.coach-set-body').replaceChildren(goals, cs, el('p', 'coach-note', T.set_note), note);
    set.hidden = false;
  }

  // the hard steps and the repeated mistakes: shown only when there is something, and only what the student did or chose; the feedback is the page's own
  const taskOf = (id) => index.tasks.find((x) => x.id === id);
  const stepBox = document.getElementById('coach-steps');
  if (stepBox) {
    const hs = hardSteps(d, index);
    if (hs.length) {
      const ul = el('ul', 'coach-steplist');
      for (const [id, ids] of hs) {
        const li = el('li'), names = el('span', 'coach-step', (T.steps || {})[id] || id);
        li.append(names, document.createTextNode(': '));
        ids.forEach((tid, i) => { const t = taskOf(tid), a = el('a', '', t.title); a.href = t.href; if (i) li.append(document.createTextNode(', ')); li.append(a); });
        ul.append(li);
      }
      stepBox.querySelector('.coach-steps-body').replaceChildren(ul);
      stepBox.hidden = false;
    }
  }
  const missBox = document.getElementById('coach-mistakes');
  if (missBox) {
    const feedback = json('fy9-mistakes') || {}, plain = (x) => String(x).replace(/\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/\*/g, '');
    const list = repeated(d.log, index).filter((h) => feedback[h.task] && feedback[h.task][h.mistake]);
    if (list.length) {
      const ul = el('ul', 'coach-misslist');
      for (const h of list) {
        const t = taskOf(h.task), li = el('li'), a = el('a', 'coach-task', t.title); a.href = t.href;
        li.append(a, el('span', 'coach-where', where(t)), el('span', 'coach-min', fmt(T.mistakes_n, { n: h.n })), el('p', 'coach-feedback', plain(feedback[h.task][h.mistake])));
        ul.append(li);
      }
      missBox.querySelector('.coach-mistakes-body').replaceChildren(ul);
      missBox.hidden = false;
    }
  }

  const keep = document.getElementById('coach-data');
  let showClear = () => {};
  if (keep) {
    let store = true;
    try { localStorage.getItem(V.KEY); } catch (e) { store = false; }   // anything under our keys, a damaged log too, can be cleared; no storage at all is said
    if (!store) keep.append(el('p', 'notice', T.nostore));
    const has = () => { try { return localStorage.getItem(V.KEY) !== null || localStorage.getItem(SET_KEY) !== null; } catch (e) { return false; } };
    let b = null;
    showClear = () => {
      if (!b && has()) {
        b = el('button', 'coach-clear', T.clear); b.type = 'button';
        b.addEventListener('click', () => {
          if (!window.confirm(T.clear_confirm)) return;
          try { localStorage.removeItem(V.KEY); localStorage.removeItem(SET_KEY); } catch (e) { /* no storage */ }
          location.reload();
        });
        keep.append(b);
      }
    };
    showClear();
  }
})();
