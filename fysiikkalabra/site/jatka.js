/* Jatka (design audit 2026-11-10, P0-3; teacher: "Suunta B toteutettuna A:n askelin"): the next thing to do, in view.
   - A module page (and every page with chapter tiles, ol.ch-cards): each tile whose chapter has been started says
     "3/7 vaihetta" (with a tick at 7/7), from the chapter's done stages (lesson.js part 2, localStorage ruukkilabra:<page>
     { done: [stage ids], of: number of stages }). Over the tiles one row, "Jatka: Luku 4 · <title>, vaihe 4/7 Teoria",
     for the chapter opened last if it is one of the page's and not finished, else the first unfinished chapter after
     a started one. Nothing shows before the reader has started a chapter. The row reads: the Jatka button on the left,
     the chapter and stage, and a quiet Poista on the right that hides the row (progress kept) until the target changes.
   - The front page: the same row for the chapter opened last in this language (ruukkilabra:viimeisin, lesson.js).
   Read from this browser only; nothing is sent, and the page is the same without storage or this script. */
(() => {
  const box = document.getElementById('jatka');
  if (!box) return;
  const T = (() => { try { return JSON.parse(box.dataset.t || '{}'); } catch (e) { return {}; } })();
  const fmt = (s, v) => String(s || '').replace(/%(\w+)/g, (m, k) => (v && k in v ? String(v[k]) : m));
  const PRE = (location.pathname.match(/(?:^|\/)((?:en|fi-easy|fr|sv)\/)[^/]*$/) || [])[1] || '';
  const read = (k) => { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } };
  const state = (file) => {
    const v = read('ruukkilabra:' + PRE + file.replace(/\.html$/, ''));
    const done = v && Array.isArray(v.done) ? v.done.length : 0, of = v && v.of > 0 ? v.of : 0;
    return { done, of, finished: of > 0 && done >= of, started: done > 0 };   // opened but nothing done: not started
  };
  const last = (() => { const v = read('ruukkilabra:viimeisin'); return v && typeof v.file === 'string' && /^[\w.-]+\.html$/.test(v.file) && (v.pre || '') === PRE ? v : null; })();
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const show = (href, num, title, stage) => {
    const text = el('p', 'resume-text');
    text.append(el('strong', '', (num ? num + ' · ' : '') + title));   // the button on the left says Jatka
    if (stage) text.append(el('span', 'resume-stage', stage));
    const go = el('a', 'resume-go', T.go || 'Jatka'); go.href = href;
    // Poista (teacher 2026-11-13): hides the row until the reader opens another chapter or another stage; the progress
    // itself stays (ruukkilabra:jatka-pois keeps only what was hidden)
    const key = PRE + href + '|' + (stage || '');
    if (read('ruukkilabra:jatka-pois') === key) return;
    const hide = el('button', 'resume-hide', T.hide || 'Poista'); hide.type = 'button';
    if (T.hide_label) { hide.title = T.hide_label; hide.setAttribute('aria-label', T.hide_label); }
    hide.addEventListener('click', () => {
      try { localStorage.setItem('ruukkilabra:jatka-pois', JSON.stringify(key)); } catch (e) { /* the row goes for this visit */ }
      box.hidden = true; box.replaceChildren();
    });
    box.replaceChildren(go, text, hide); box.hidden = false;
  };
  const stageText = (v) => (v && v.n && v.of ? fmt(T.stage, { n: v.n, of: v.of }) + (v.label ? ' ' + v.label : '') : '');

  const tiles = [...document.querySelectorAll('ol.ch-cards li.live:not(.me-tile) .ch-box > a[href]')   /* the module's end tiles (exam, challenge tasks) are not chapters */].map((a) => ({ a, file: a.getAttribute('href'), box: a.closest('.ch-box') }))
    .filter((t) => /^[\w.-]+\.html$/.test(t.file));
  if (!tiles.length) {                       // the front page
    if (last && last.title) show(last.file, last.num || '', last.title, stageText(last));
    return;
  }
  let pick = null, any = false;
  tiles.forEach((t, i) => {
    const s = state(t.file); t.s = s;
    if (!s.started) return;
    any = true;
    const num = t.box.querySelector('.l-num'); t.num = num ? num.textContent.trim() : '';
    // what the mark says is the count of worked stages, never "learned": a stage counts once its required answers are
    // given (lesson.js), a visit alone marks nothing; a record from before 2026-11-10 has no stage count: "Aloitettu"
    const mark = el('span', 'ch-state' + (s.finished ? ' is-done' : ''), s.of ? fmt(T.stages || '%n/%of', { n: Math.min(s.done, s.of), of: s.of }) : (T.started || 'Aloitettu'));
    if (num) num.append(' · ', mark); else t.box.append(mark);
    t.box.closest('li').dataset.state = s.finished ? 'done' : 'doing';
  });
  const mine = last && tiles.find((t) => t.file === last.file);
  if (!any && !mine) return;
  if (mine && !mine.s.finished) pick = { t: mine, stage: stageText(last) };
  else {
    const from = tiles.reduce((k, t, i) => (t.s.started ? i : k), -1);                 // the last chapter that was opened
    const next = tiles.slice(0, from + 1).find((t) => t.s.started && !t.s.finished) || tiles[from + 1];
    if (next) pick = { t: next, stage: next.s.of ? fmt(T.stage, { n: Math.min(next.s.done + 1, next.s.of), of: next.s.of }) : '' };
  }
  if (pick) show(pick.t.file, pick.t.num != null ? pick.t.num : ((pick.t.box.querySelector('.l-num') || {}).textContent || '').trim(), pick.t.a.textContent.trim(), pick.stage);
})();
