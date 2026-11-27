/* Koetila, the FY9 exam mode (work queue 11b PR 6; docs/FY9_ADAPTIVE_PLAN.md 6.4, scripts/koetila.py).
   One script for two kinds of page: a minikoe page (fy9-minikoe-<id>.html, cards cut out of the unit pages) and the practice exam
   (fy9-harjoituskoe), whose page works as before until the student starts the exam mode. The page carries <div id="koetila"
   data-t="texts" data-spec="{id, minutes, pts, tasks:[{id (the card), key, min, pts, group, kind}], groups:[{id, choose}]}">.
   Three states, kept on this device only in the key ruukkilabra:fy9-koetila (the name has fy9-, so the whole-work file carries it):
     idle   nothing started: a minikoe page shows only its Aloita button; the practice exam page is as it was, with one panel
     run    the clock runs (wall-clock time, so a reload or a closed tab does not stop it; Tauko stops it); a task in a group of choices
            is chosen before it is answered; the time of each task is kept; answers are kept as they are typed
     ended  the student ended it or the time ran out: every answer is put back, the page checks the numbers and choices once (the first answer is
            the answer), the points of the tasks written out are the student's own, and the result with the time table is shown
   Until it has ended, the hints, the feedback ("Lähellä", the mistake and the right option), the model answers, the solutions and the
   answers a check compares to are taken out of the page itself (the page is rebuilt from its source when it ends: a reload), so
   there is nothing to open. The clock tells and blocks nothing: its text is no live region; a polite status says only that 10, 5 and
   1 minute are left. Nothing is sent anywhere; one summary row per exam goes to the "exams" field of the coach's key (plan 4.4), and the
   attempts made while the exam is checked are logged by valmentaja.js with the mode "k" (window.flKoetila.key / mode). */
(() => {
  const root = document.getElementById('koetila');
  if (!root) return;
  const parse = (s) => { try { return JSON.parse(s); } catch (e) { return null; } };
  const T = parse(root.dataset.t) || {}, spec = parse(root.dataset.spec);
  if (!spec || !Array.isArray(spec.tasks)) return;
  const KEY = 'ruukkilabra:fy9-koetila', LIMIT = spec.minutes * 60000, MINI = root.dataset.page === 'mini';
  const fmt = (s, v) => String(s || '').replace(/\{(\w+)\}/g, (m, k) => (v && k in v ? v[k] : m));
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const num = (x) => String(Math.round(x * 10) / 10).replace('.', ',');
  const cards = spec.tasks.map((t) => Object.assign({}, t, { el: document.getElementById(t.id) })).filter((c) => c.el);
  const byId = Object.fromEntries(cards.map((c) => [c.id, c]));

  // ---- storage (this device only; the exam mode is not offered where nothing can be stored: it is rebuilt from the page by a reload) ----
  let canStore = true;
  const readAll = () => {
    try { const o = JSON.parse(localStorage.getItem(KEY)); if (o && o.v === 1 && o.exams && typeof o.exams === 'object') return o; } catch (e) { /* none or damaged */ }
    return { v: 1, exams: {} };
  };
  const load = () => { try { localStorage.getItem(KEY); } catch (e) { canStore = false; } return canStore ? readAll().exams[spec.id] || null : null; };
  let rec = load();
  const save = () => {
    if (!rec || !canStore) return;
    try { const all = readAll(); all.exams[spec.id] = rec; localStorage.setItem(KEY, JSON.stringify(all)); } catch (e) { canStore = false; }
  };
  const drop = () => { try { const all = readAll(); delete all.exams[spec.id]; localStorage.setItem(KEY, JSON.stringify(all)); } catch (e) { /* nothing stored */ } rec = null; };

  const now = () => Date.now();
  let state = !rec ? 'idle' : rec.state === 'ended' ? 'ended' : 'run';
  let grading = false;

  // ---- what other scripts may ask (valmentaja.js: the task key of a card and the mode of a row) ----
  const counted = (c) => !c.group || (rec && (rec.chosen || []).includes(c.id));
  window.flKoetila = {
    state: () => state,
    key: (id) => (byId[id] ? byId[id].key : null),
    mode: (id, kind) => (byId[id] && (state === 'run' || (state === 'ended' && counted(byId[id]) && (grading || kind === 'rubric'))) ? 'k' : 'p'),
  };

  // ---- the controls whose values are kept ----
  const controls = (card) => [...card.querySelectorAll('input[type=text], input[type=radio], textarea')].filter((x) => !x.closest('.sa-rate, .pad, [class^="pad-"], [class*=" pad-"], .kt-row'));
  const answers = (card) => { const o = {}; controls(card).forEach((x, i) => { const v = x.type === 'radio' ? (x.checked ? 1 : 0) : x.value; if (v) o[i] = v; }); return o; };
  const restore = (card, a) => controls(card).forEach((x, i) => { if (!a || !(i in a)) return; if (x.type === 'radio') x.checked = !!a[i]; else x.value = a[i]; });
  const answered = (c) => Object.keys(answers(c.el)).length > 0 || !!(rec && rec.wrote && rec.wrote[c.id]);
  const title = (c) => { const h = c.el.querySelector('h3'); if (!h) return c.key; const k = h.cloneNode(true); k.querySelectorAll('.pts, .kt-tag').forEach((n) => n.remove()); return k.textContent.replace(/\s+/g, ' ').trim().replace(/^\d+\.\s*/, ''); };

  // ---- the lock: what helps or tells is taken out of a card ----
  const DROP = '.hints, details.solution, details.reveal, details.answer, .feedback, .model, .solution-text, .pending, .practice-hint, .mc-score, .crit-result, .explain-status, .show-model, .commit, .copy-notes, .lock-note, .ex-foot, .task-skills, fieldset.choice output';
  const lock = (card) => {
    card.querySelectorAll(DROP).forEach((n) => n.remove());
    card.querySelectorAll('form.check').forEach((f) => {   // the number field stays; what it is compared with, the mistakes and the button go
      const box = el('div', 'kt-num'), input = f.querySelector('input'), unit = f.querySelector('.unit');
      if (input) box.append(input);
      if (unit) box.append(unit);
      f.replaceWith(box);
    });
    card.querySelectorAll('[data-correct], [data-points], [data-answer], [data-mistakes], [data-tol], [data-exact], [data-reveal]').forEach((n) => ['data-correct', 'data-points', 'data-answer', 'data-mistakes', 'data-tol', 'data-exact', 'data-reveal'].forEach((a) => n.removeAttribute(a)));
    card.querySelectorAll('.numeric output, .interpret output').forEach((n) => n.remove());
  };

  // ---- the clock ----
  const spentOf = () => rec.spent + (rec.paused ? 0 : Math.max(0, now() - rec.tick));
  const advance = () => {
    const t = now(), d = rec.paused ? 0 : Math.max(0, t - rec.tick);
    rec.tick = t;
    if (d) { rec.spent += d; if (rec.cur && rec.times) rec.times[rec.cur] = (rec.times[rec.cur] || 0) + d; }
  };
  const clock = (ms) => { const s = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), r = s % 60; return (h ? h + ':' + String(m).padStart(2, '0') : m) + ':' + String(r).padStart(2, '0'); };

  // ---- ending ----
  const summaryRow = () => {
    const iso = (t) => new Date(t).toISOString().slice(0, 16) + 'Z', times = {};
    cards.forEach((c) => { if (rec.times && rec.times[c.id]) times[c.key] = Math.round(rec.times[c.id] / 1000); });
    const chosen = cards.filter(counted).map((c) => c.key);
    return { id: spec.id, start: iso(rec.start), end: iso(rec.end), chosen, times };
  };
  const logExam = () => {   // one summary row in the coach's key (plan 4.4 "exams"); the rest of the key is kept as it is
    const V = window.flValmentaja; if (!V || !V.read) return;
    const d = V.read(); if (!d) return;
    d.exams = (Array.isArray(d.exams) ? d.exams : []).concat([summaryRow()]).slice(-50);
    V.write(d);
  };
  const finish = (reason) => {
    if (state !== 'run') return;
    advance(); rec.state = 'ended'; rec.end = now(); rec.reason = reason; rec.paused = false;
    cards.forEach((c) => { rec.ans[c.id] = answers(c.el); });
    state = 'ended';
    logExam();
    save();
    location.reload();
  };

  // ---- the page by state ----
  const tasksBox = document.getElementById('kt-tasks');
  const pageStart = (label) => {
    const b = el('button', 'kt-go', label); b.type = 'button';
    b.addEventListener('click', () => {
      rec = { state: 'run', start: now(), tick: now(), spent: 0, paused: false, cur: null, times: {}, chosen: [], wrote: {}, ans: {}, res: {} };
      state = 'run'; save(); location.reload();
    });
    return b;
  };

  if (state === 'idle') {
    if (MINI) { cards.forEach((c) => lock(c.el)); if (tasksBox) tasksBox.hidden = true; }
    root.hidden = false;
    root.append(canStore ? pageStart(T.start) : el('p', 'notice', T.nostore));
    return;
  }

  if (state === 'run') {
    advance();
    if (spentOf() >= LIMIT) {   // the time ran out while the page was closed
      rec.spent = LIMIT; rec.state = 'ended'; rec.end = now(); rec.reason = 'time'; state = 'ended';
      cards.forEach((c) => { if (!rec.ans[c.id]) rec.ans[c.id] = {}; });
      logExam(); save();
    }
  }

  if (state === 'run') {
    root.hidden = false;
    cards.forEach((c) => { lock(c.el); restore(c.el, (rec.ans || {})[c.id]); });
    const live = el('div', 'visually-hidden kt-live'); live.setAttribute('role', 'status'); live.setAttribute('aria-live', 'polite');
    const bar = el('div', 'kt-bar'), time = el('span', 'kt-time'), pause = el('button', 'kt-pause'), end = el('button', 'kt-end', T.end);
    bar.setAttribute('role', 'group'); bar.setAttribute('aria-label', T.time_h);
    time.setAttribute('role', 'timer'); time.setAttribute('aria-live', 'off');
    pause.type = 'button'; end.type = 'button';
    bar.append(time, pause, end); document.body.append(bar, live); document.documentElement.classList.add('kt-on');

    const paintPause = () => { pause.textContent = rec.paused ? T.resume : T.pause; pause.setAttribute('aria-pressed', rec.paused ? 'true' : 'false'); };
    pause.addEventListener('click', () => { advance(); rec.paused = !rec.paused; rec.tick = now(); paintPause(); save(); });
    end.addEventListener('click', () => { if (window.confirm(T.end_confirm)) finish('user'); });

    // the groups of choices: chosen before answering, taken back only while the task has no answer; the clock of each task
    const mine = (c) => (rec.chosen || []).includes(c.id);
    const groupCards = (g) => cards.filter((c) => c.group === g.id);
    cards.forEach((c) => {
      const head = c.el.querySelector('h3'), row = el('div', 'kt-row');
      c.row = row;
      if (c.group) {
        c.pick = el('button', 'kt-pick', T.choose); c.pick.type = 'button';
        c.pick.addEventListener('click', () => {
          const on = mine(c);
          if (on && answered(c)) return;
          rec.chosen = on ? rec.chosen.filter((x) => x !== c.id) : (rec.chosen || []).concat([c.id]);
          if (!on) rec.cur = c.id;
          save(); paint();
        });
        row.append(c.pick);
        const body = el('div', 'kt-body');
        [...c.el.childNodes].forEach((n) => { if (n !== head) body.append(n); });
        c.el.append(body); c.body = body;
      }
      c.go = el('button', 'kt-task-start', T.start_task); c.go.type = 'button';
      c.go.addEventListener('click', () => { advance(); rec.cur = rec.cur === c.id ? null : c.id; save(); paint(); });
      row.append(c.go);
      (head || c.el).after(row);
      c.el.addEventListener('focusin', () => { if (rec.cur !== c.id && (!c.group || mine(c))) { advance(); rec.cur = c.id; save(); paint(); } });
      c.el.addEventListener('input', () => { clearTimeout(c.t); c.t = setTimeout(() => { rec.ans[c.id] = answers(c.el); save(); paint(); }, 400); });
      c.el.addEventListener('change', () => { rec.ans[c.id] = answers(c.el); save(); paint(); });
      c.el.addEventListener('fl:written', () => { rec.wrote[c.id] = 1; save(); paint(); });
    });
    const paint = () => {
      const groups = {};
      (spec.groups || []).forEach((g) => { groups[g.id] = groupCards(g).filter(mine).length; });
      cards.forEach((c) => {
        const on = !c.group || mine(c), g = c.group && (spec.groups || []).find((x) => x.id === c.group);
        c.el.classList.toggle('kt-current', rec.cur === c.id);
        if (c.pick) {
          const full = !on && groups[c.group] >= g.choose, locked = on && answered(c);
          c.pick.textContent = on ? T.chosen : T.choose; c.pick.setAttribute('aria-pressed', on ? 'true' : 'false');
          c.pick.disabled = full || locked;
          c.body.inert = !on; c.el.classList.toggle('kt-off', !on);
        }
        c.go.disabled = !on; c.go.setAttribute('aria-pressed', rec.cur === c.id ? 'true' : 'false');
      });
    };
    const tick = () => {
      advance();
      const left = LIMIT - rec.spent;
      time.textContent = fmt(T.left, { t: clock(left) });
      for (const m of [10, 5, 1]) if (LIMIT > m * 60000 * 1.5 && left <= m * 60000 && !(rec.warned || []).includes(m)) { rec.warned = (rec.warned || []).concat([m]); live.textContent = fmt(T.warn, { n: m }); }
      if (left <= 0) { finish('time'); return; }
      save();
    };
    paintPause(); paint(); tick();
    setInterval(tick, 1000);
    window.addEventListener('pagehide', () => { if (state === 'run') { advance(); save(); } });
    return;
  }

  // ---- ended: the page as it was built, the answers back in, the checks done once, the result ----
  root.hidden = false; root.replaceChildren();
  if (tasksBox) tasksBox.hidden = false;
  if (!rec.res) rec.res = {};
  cards.forEach((c) => { restore(c.el, (rec.ans || {})[c.id]); });
  cards.forEach((c) => {
    if (counted(c)) return;
    c.el.classList.add('kt-off');
    c.el.querySelectorAll('.rubric input').forEach((i) => { i.disabled = true; });
    const h = c.el.querySelector('h3'); if (h) h.append(' ', el('span', 'kt-tag', T.unchosen));
  });
  const cardOf = (e) => { const d = e.detail || {}, t = e.target && e.target.closest ? e.target.closest('.activity[id]') : null; return byId[(t && t.id) || d.id]; };
  document.addEventListener('fl:attempt', (e) => {
    const c = cardOf(e); if (!c || !grading || !counted(c)) return;
    const d = e.detail || {};
    if (d.state === 'ok' || d.state === 'close' || d.state === 'no') { rec.res[c.id] = d.state; save(); paint(); }
  });
  document.addEventListener('fl:rubric', (e) => {
    const c = cardOf(e), d = e.detail || {}; if (!c || c.kind !== 'short' || !counted(c) || !(d.max > 0)) return;
    rec.res[c.id] = { self: Math.max(0, Math.min(1, d.got / d.max)) }; save(); paint();
  });
  document.addEventListener('change', (e) => { if (e.target.closest && e.target.closest('.rubric')) paint(); });

  const got = (c) => {
    if (!counted(c)) return 0;
    if (c.kind === 'long') { let s = 0; c.el.querySelectorAll('.rubric input:checked').forEach((i) => { s += Number(i.value) || 0; }); return Math.min(c.pts, s); }
    const r = rec.res[c.id];
    return r === 'ok' ? c.pts : r === 'close' ? c.pts / 2 : r && r.self != null ? Math.round(c.pts * r.self * 2) / 2 : 0;
  };
  const resultText = (c) => {
    if (!counted(c)) return T.unchosen;
    const r = rec.res[c.id];
    if (c.kind === 'long') return c.el.querySelector('.rubric input:checked') ? T.res_self : T.not_answered;
    return r === 'ok' ? T.res_ok : r === 'close' ? T.res_close : r === 'no' ? T.res_no : r && r.self != null ? T.res_self : T.not_answered;
  };
  const panel = el('section', 'kt-result'); panel.setAttribute('aria-labelledby', 'kt-result-h');
  const h = el('h2', '', T.result_h); h.id = 'kt-result-h';
  const line = el('p', 'kt-line', rec.reason === 'time' ? T.ended_time : T.ended_user), pts = el('p', 'kt-points'), table = el('table', 'kt-table'), again = el('button', 'kt-again', T.again);
  again.type = 'button';
  again.addEventListener('click', () => { if (window.confirm(T.again_confirm)) { drop(); location.reload(); } });
  const paint = () => {
    // the total counts only what the rules allow: the required tasks and, of a group, at most "choose" tasks (the best ones if more were somehow marked)
    let total = 0;
    const free = cards.filter((c) => !c.group).reduce((s, c) => s + got(c), 0); total += free;
    (spec.groups || []).forEach((g) => { total += cards.filter((c) => c.group === g.id).map(got).sort((a, b) => b - a).slice(0, g.choose).reduce((s, x) => s + x, 0); });
    total = Math.min(total, spec.pts);
    pts.textContent = fmt(T.points, { got: num(total), max: spec.pts });
    const head = document.createElement('thead'), hr = el('tr');   // three narrow columns so that the table fits a phone: the task and its result, the points, planned / used minutes
    [['', 'kt-c-task'], [T.points.replace(/\{got\} \/ \{max\}/, '').trim(), 'kt-c-pts'], [T.planned + ' / ' + T.used, 'kt-c-time']].forEach(([t, c]) => { const th = el('th', c, t); th.scope = 'col'; hr.append(th); });
    head.append(hr);
    const body = document.createElement('tbody');
    cards.forEach((c) => {
      const tr = el('tr', counted(c) ? '' : 'kt-skip'), th = el('th'), a = el('a', '', title(c));
      th.scope = 'row'; a.href = '#' + c.id;
      th.append(a, el('span', 'kt-sub', ' · ' + resultText(c)));
      const used = counted(c) && rec.times && rec.times[c.id] ? fmt(T.min, { n: Math.max(1, Math.round(rec.times[c.id] / 60000)) }) : '–';
      tr.append(th, el('td', '', counted(c) ? num(got(c)) + ' / ' + c.pts : '–'), el('td', '', c.min + ' / ' + used));
      body.append(tr);
    });
    table.replaceChildren(head, body);
  };
  panel.append(h, line, pts, table, again);
  root.append(panel);
  paint();

  // the checks, once: a number in its field is Tarkista'd, a picked option Vastaa'd, by the page's own code, so the feedback, the hints and the locks
  // are the practice page's; the attempts are logged as exam attempts (mode k)
  if (!rec.graded) {
    const grade = () => {
      grading = true;
      cards.filter((c) => c.kind === 'short' && counted(c)).forEach((c) => {
        const f = c.el.querySelector('form.check'), picked = c.el.querySelector('fieldset.choice input:checked');
        if (f) { const i = f.querySelector('input'); if (i && i.value.trim()) f.requestSubmit(); else rec.res[c.id] = 'none'; }
        else if (picked) { const b = c.el.querySelector('fieldset.choice .commit'); if (b) b.click(); }
        else if (c.el.querySelector('fieldset.choice')) rec.res[c.id] = 'none';
      });
      setTimeout(() => { grading = false; rec.graded = true; save(); paint(); }, 1500);
    };
    if (document.readyState === 'complete') setTimeout(grade, 700); else window.addEventListener('load', () => setTimeout(grade, 700));
  }
})();
