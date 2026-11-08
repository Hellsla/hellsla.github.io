/* Annetut tehtävät and the student's own progress (teacher 2026-11-07, FY3 first). The teacher's assigned tasks of the
   module are the page's #fl-course (build.py course_block, from annetut.json): { course, chapters, assigned: [id, ...] }.
   - A chapter page: every assigned exercise (li.assigned, "Annettu" beside its number, a green left edge) gets a small
     "Tehty" box at the right end of its head row, before "Avaa isoksi". It can be ticked only when the task's own
     solution editor has a saved solution (padstore.js) with text, a formula or a picture: the open editors are written
     first, then the saved record is read back. A number in Tarkista, a hint or the model solution is not enough. The tick
     can be taken off; it goes by itself when the saved solution is deleted or emptied (padstore.js "fl:pad-change"),
     also when the page opens and the solution is no longer there. Tehtävät opens with "3/5 annettua tehtävää tehty".
   - The module page: Oma eteneminen (build.py progress_section): "43/72 tehtävää tehty", a bar and the graph of the
     done tasks by date (cumulative), drawn again whenever a tick changes (also in another tab).
   Kept in this browser only, localStorage ruukkilabra:tehty = { v: 1, done: { id: ISO time }, log: [[id, ISO time, 1 | 0]] }:
   a new tick gets a new time, a task counts once, the log keeps each tick and untick (no other activity, keystrokes or
   time on the page). The module's work file (palautus.js) carries the ticks and their log, so Avaa tallennettu työ brings
   the graph back on another computer. The graph is drawn from the ticks as they are,
   so an untick corrects it. */
(() => {
  const ME = document.currentScript;
  const HERE = ME ? ME.src : location.href;
  const KEY = 'ruukkilabra:tehty', LOG_MAX = 3000;
  const C = (() => { try { return JSON.parse(document.getElementById('fl-course').textContent); } catch (e) { return null; } })();
  if (!C) return;
  // A module without assigned tasks (teacher 2026-11-07: FY1-FY9 but FY3): only its page's Oma eteneminen, over every
  // task of the module; a task counts as done when it has a saved solution, dated by its first save (padstore.js
  // ruukkilabra:ratkaistu, else the record's last save), or when every Tarkista and Vastaa of the task has been checked
  // (ruukkilabra:tarkistettu, lesson.js). No marks or Tehty boxes on the tasks themselves.
  const EVERY = !(Array.isArray(C.assigned) && C.assigned.length);
  if (EVERY && !document.getElementById('oma-eteneminen')) return;
  const A = { course: C.course, tasks: EVERY ? (C.chapters || []).flatMap((c) => c.tasks || []) : C.assigned };
  let solved = {};
  const ALL = new Set(A.tasks);
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).js || {}; } catch (e) { return {}; } })();
  const FI = { done_label: 'Tehty', done_aria: 'Tehtävä {{num}} tehty', done_need: 'Kirjoita ensin oma ratkaisu Kirjoita ratkaisu -editoriin. Tehdyksi voi merkitä, kun ratkaisu on tallennettu.',
    done_checking: 'Tarkistetaan tallennettua ratkaisua…', done_store: 'Tallennettua ratkaisua ei voitu tarkistaa, joten tehtävää ei merkitty tehdyksi.',
    done_unsaved: 'Ratkaisua ei saatu tallennettua, joten tehtävää ei merkitty tehdyksi.', done_nosave: 'Selain ei salli tallentamista, joten Tehty-merkintä ei säily.',
    done_removed: 'Tallennettu ratkaisu poistettiin, joten Tehty-merkintä poistui.', done_lesson: '{{n}}/{{total}} annettua tehtävää tehty',
    progress_count: '{{n}}/{{total}} tehtävää tehty', progress_empty: '', progress_axis_y: 'tehtyjä', progress_chart: '{{n}}/{{total}}' };
  const S = (k, v) => (typeof L10N[k] === 'string' ? L10N[k] : FI[k] || '').replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m));
  const LANG = document.documentElement.lang || 'fi';
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const say = (node, text, state) => { if (!node) return; node.textContent = text || ''; node.hidden = !text; if (state) node.dataset.state = state; else delete node.dataset.state; };

  // ---- the ticks ----
  const read = () => {
    if (EVERY) return { v: 1, done: solved, log: [] };
    try {
      const v = JSON.parse(localStorage.getItem(KEY));
      if (v && v.v === 1 && v.done && typeof v.done === 'object' && !Array.isArray(v.done)) return { v: 1, done: v.done, log: Array.isArray(v.log) ? v.log : [] };
    } catch (e) { /* none or unreadable: no ticks */ }
    return { v: 1, done: {}, log: [] };
  };
  const save = (id, on) => {
    const st = read(), t = new Date().toISOString();
    if (!on && !(id in st.done)) return true;
    if (on) st.done[id] = t; else delete st.done[id];
    st.log.push([id, t, on ? 1 : 0]);
    if (st.log.length > LOG_MAX) st.log = st.log.slice(-LOG_MAX);
    try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { return false; }
    render();
    return true;
  };
  // the module's ticks and log for the submission file (palautus.js)
  if (!EVERY) window.flDone = {
    course: A.course, assigned: A.tasks.slice(),
    progress: () => {
      const st = read();
      return { course: A.course, assigned: A.tasks.slice(), done: A.tasks.filter((id) => typeof st.done[id] === 'string').map((id) => [id, st.done[id]]),
        history: st.log.filter((x) => Array.isArray(x) && ALL.has(x[0])).slice(-LOG_MAX).map((x) => [x[0], x[1], x[2] ? 1 : 0]) };
    },
  };

  // ---- the saved solutions (padstore.js) ----
  const loadStore = () => (window.flPadStore ? Promise.resolve() : new Promise((ok, no) => {
    const s = document.createElement('script'); s.src = new URL('padstore.js', HERE).href; s.onload = ok; s.onerror = no; document.head.append(s);
  }));
  // a solution: some text, a formula or a picture the student added (a formula and a picture are images in the editor's HTML)
  const isSolution = (html) => {
    if (!html) return false;
    const d = new DOMParser().parseFromString('<div>' + html + '</div>', 'text/html');
    return !!d.querySelector('img') || d.body.textContent.replace(/[\s ​⁠]/g, '') !== '';
  };
  const msgs = new Map();   // task id -> its message line (a chapter page)
  const drop = (id) => { if (save(id, false)) say(msgs.get(id), S('done_removed'), 'hint'); };
  // every tick of the module whose saved solution is gone (the page opens, "Poista kaikki", a backup brought back)
  const FIRST = 'ruukkilabra:ratkaistu';
  const reconcile = () => {
    if (EVERY) {
      loadStore().then(() => window.flPadStore.all()).then(({ solutions }) => {
        let first = {}; try { first = JSON.parse(localStorage.getItem(FIRST) || '{}') || {}; } catch (e) { /* none */ }
        const now = new Date().toISOString(), out = {};
        solutions.forEach((r) => { if (ALL.has(r.id) && isSolution(r.html)) out[r.id] = typeof first[r.id] === 'string' ? first[r.id] : r.updated || now; });
        let checked = {}; try { checked = JSON.parse(localStorage.getItem('ruukkilabra:tarkistettu') || '{}') || {}; } catch (e) { /* none */ }
        Object.keys(checked).forEach((id) => { const t = checked[id] && checked[id].done;   // every answer part checked (lesson.js)
          if (ALL.has(id) && typeof t === 'string' && (!out[id] || t < out[id])) out[id] = t; });
        solved = out; render();
      }, () => { /* the store cannot be read now */ });
      return;
    }
    const st = read(), mine = Object.keys(st.done).filter((id) => ALL.has(id));
    if (!mine.length) return;
    loadStore().then(() => window.flPadStore.all()).then(({ solutions }) => {
      const has = new Set(solutions.filter((r) => isSolution(r.html)).map((r) => r.id));
      mine.filter((id) => !has.has(id)).forEach(drop);
      render();
    }, () => { /* the store cannot be read now: the ticks stay */ });
  };
  document.addEventListener('fl:pad-change', (e) => {
    const d = e.detail || {};
    if (d.all || EVERY) { reconcile(); render(); return; }
    if (!d.id || !ALL.has(d.id) || !(d.id in read().done)) return;
    if ('html' in d) { if (!isSolution(d.html)) drop(d.id); }
    else loadStore().then(() => window.flPadStore.get(d.id)).then((html) => { if (!isSolution(html)) drop(d.id); }, () => {});
  });
  window.addEventListener('storage', (e) => { if (EVERY) reconcile(); else if (e.key === KEY || e.key === null) render(); });
  window.addEventListener('pageshow', (e) => { if (e.persisted) reconcile(); });

  // ---- a chapter page ----
  const sec = document.getElementById('exercises');
  const items = sec ? [...sec.querySelectorAll('li.assigned[id]')].filter((li) => ALL.has(li.id)) : [];
  const boxes = new Map();
  let lessonCount = null;
  items.forEach((li) => {
    const head = li.querySelector(':scope > .ex-head');
    const lab = el('label', 'ex-done'), box = el('input'), txt = el('span', null, S('done_label'));
    box.type = 'checkbox';
    box.setAttribute('aria-label', S('done_aria', { num: li.dataset.num || '' }).trim());
    lab.append(box, txt);
    const msg = el('p', 'ex-done-msg'); msg.hidden = true; msg.setAttribute('aria-live', 'polite');
    if (head) { const big = head.querySelector(':scope > .ex-big'); if (big) head.insertBefore(lab, big); else head.append(lab); head.after(msg); }
    else { li.prepend(lab); lab.after(msg); }
    boxes.set(li.id, box); msgs.set(li.id, msg);
    box.addEventListener('change', async () => {
      if (!box.checked) { if (!save(li.id, false)) say(msg, S('done_nosave'), 'no'); else say(msg, ''); render(); return; }
      box.checked = false; box.disabled = true; say(msg, S('done_checking'));
      try {
        if (window.flPads) { try { await window.flPads.flush(); } catch (e) { say(msg, S('done_unsaved'), 'no'); return; } }
        await loadStore();
        const html = await window.flPadStore.get(li.id);
        if (!isSolution(html)) { say(msg, S('done_need'), 'hint'); return; }
        if (!save(li.id, true)) { say(msg, S('done_nosave'), 'no'); return; }
        say(msg, '');
      } catch (e) { say(msg, S('done_store'), 'no'); } finally { box.disabled = false; render(); }
    });
  });
  if (items.length) {
    lessonCount = el('p', 'done-count'); lessonCount.setAttribute('aria-live', 'polite');
    const head = sec.querySelector(':scope > .split-head') || sec.querySelector(':scope > h2');   // lesson.js part 9 wraps the heading
    if (head) head.after(lessonCount); else sec.prepend(lessonCount);
  }

  // ---- the module page ----
  const mod = document.getElementById('oma-eteneminen');
  if (mod) { mod.hidden = false; const wrap = mod.closest('details'); if (wrap) wrap.hidden = false; }
  const graph = mod && mod.querySelector('details.pm-graph');
  if (graph) graph.addEventListener('toggle', () => { if (graph.open) render(); });
  let lastW = 0;
  window.addEventListener('resize', () => { const c = graph && graph.open && graph.querySelector('.pm-chart'); if (c && Math.abs(c.clientWidth - lastW) > 8) render(); });

  // The graph (the student's own; the teacher's view shows only the Tehty marks, never the times or a graph): the date across, the done tasks
  // up to the module's total, a step for each day with ticks, from the first tick's day to today.
  const SVGNS = 'http://www.w3.org/2000/svg';
  const sv = (tag, attrs, text) => { const e = document.createElementNS(SVGNS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (text != null) e.textContent = text; return e; };
  const dayKey = (d) => d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
  const DAY = 864e5;
  // the goal line (teacher 2026-11-07): 90 tasks in a 2 op module, 45 in a 1 op one (#fl-course goal); the axis still
  // runs up to every task of the module, so the student sees there are more
  const GOAL = EVERY && Number(C.goal) > 0 && Number(C.goal) < A.tasks.length ? Number(C.goal) : 0;
  const chart = (host, times, total) => {
    host.textContent = '';
    if (!times.length) { host.append(el('p', 'pm-empty', S(EVERY ? 'progress_empty_all' : 'progress_empty'))); return; }
    const per = new Map();
    times.map((t) => new Date(t)).sort((a, b) => a - b).forEach((d) => { const k = dayKey(d); per.set(k, (per.get(k) || 0) + 1); });
    const days = [...per.keys()].map((k) => new Date(k + 'T00:00:00'));
    const today = new Date(dayKey(new Date()) + 'T00:00:00');
    let d0 = days[0], d1 = new Date(Math.max(today, days[days.length - 1]));
    if (d1 - d0 < DAY) d0 = new Date(d1 - DAY);
    const W = Math.max(280, Math.round(host.clientWidth || 600)), H = 230, L = 40, R = 14, T = 14, B = 30;
    lastW = W;
    const x = (d) => L + (W - L - R) * (d - d0) / (d1 - d0), y = (n) => T + (H - T - B) * (1 - n / total);
    const svg = sv('svg', { width: W, height: H, viewBox: `0 0 ${W} ${H}`, role: 'img', class: 'pm-svg', 'aria-label': GOAL ? S('progress_chart_all', { n: times.length, total, goal: GOAL }) : S('progress_chart', { n: times.length, total }) });
    const px = (H - T - B) / total, step = [1, 2, 5, 10, 20, 25, 50, 100, 200].find((k) => k * px >= 22) || 500;   // labels at least 22 px apart
    const near = (a, b) => Math.abs(a - b) * px < 16;
    for (let v = 0; v <= total; v += step) {
      if (v && ((v !== total && near(v, total)) || (GOAL && near(v, GOAL)))) continue;
      svg.append(sv('line', { x1: L, x2: W - R, y1: y(v), y2: y(v), class: 'pm-grid' }), sv('text', { x: L - 6, y: y(v) + 4, 'text-anchor': 'end', class: 'pm-tick' }, String(v)));
    }
    svg.append(sv('line', { x1: L, x2: W - R, y1: y(total), y2: y(total), class: 'pm-total' }), sv('text', { x: L - 6, y: y(total) + 4, 'text-anchor': 'end', class: 'pm-tick pm-tick-total' }, String(total)));
    if (GOAL) svg.append(sv('line', { x1: L, x2: W - R, y1: y(GOAL), y2: y(GOAL), class: 'pm-goal' }), sv('text', { x: L - 6, y: y(GOAL) + 4, 'text-anchor': 'end', class: 'pm-tick pm-tick-goal' }, String(GOAL)),
      sv('text', { x: W - R - 4, y: y(GOAL) + 17, 'text-anchor': 'end', class: 'pm-tick pm-tick-goal' }, S('progress_goal', { goal: GOAL })));
    const span = Math.round((d1 - d0) / DAY), every = Math.max(1, Math.ceil(span / Math.max(1, Math.floor((W - L - R) / 64))));
    const fmt = (d) => d.toLocaleDateString(LANG, { day: 'numeric', month: 'numeric' });
    for (let i = 0; i <= span; i += every) { const d = new Date(d0.getTime() + i * DAY); svg.append(sv('text', { x: x(d), y: H - 10, 'text-anchor': 'middle', class: 'pm-tick' }, fmt(d))); }
    svg.append(sv('line', { x1: L, x2: W - R, y1: y(0), y2: y(0), class: 'pm-axis' }), sv('line', { x1: L, x2: L, y1: T, y2: y(0), class: 'pm-axis' }));
    let n = 0, path = `M${x(d0)} ${y(0)}`;
    const dots = [];
    [...per.entries()].forEach(([k, c]) => { const d = new Date(k + 'T00:00:00'); path += ` H${x(d)} V${y(n + c)}`; n += c; dots.push([x(d), y(n)]); });
    path += ` H${x(d1)}`;
    svg.append(sv('path', { d: path, class: 'pm-line' }));
    dots.forEach(([cx, cy]) => svg.append(sv('circle', { cx, cy, r: 3.5, class: 'pm-dot' })));
    host.append(svg);
  };

  const render = () => {
    const st = read();
    boxes.forEach((box, id) => { box.checked = id in st.done; box.closest('li').classList.toggle('is-done', box.checked); });
    if (lessonCount) lessonCount.textContent = S('done_lesson', { n: items.filter((li) => li.id in st.done).length, total: items.length });
    if (mod) {
      const done = A.tasks.filter((id) => typeof st.done[id] === 'string'), total = A.tasks.length;
      mod.querySelector('.pm-count').textContent = GOAL ? S('progress_count_goal', { n: done.length, total, goal: GOAL }) : S('progress_count', { n: done.length, total });
      const bar = mod.querySelector('.pm-bar');
      bar.setAttribute('aria-valuemax', String(total)); bar.setAttribute('aria-valuenow', String(done.length));
      bar.setAttribute('aria-label', S('progress_count', { n: done.length, total }));
      bar.firstElementChild.style.width = (total ? 100 * done.length / total : 0) + '%';
      if (graph && graph.open) chart(graph.querySelector('.pm-chart'), done.map((id) => st.done[id]), total);
    }
  };
  window.flProgressChart = chart;
  render();
  reconcile();
})();
