/* Jatka (design audit 2026-11-10, P0-3; teacher: "Suunta B toteutettuna A:n askelin"): the next thing to do, in view.
   - A module page (and every page with chapter tiles, ol.ch-cards): each tile whose chapter has been started says
     "3/7 vaihetta" (with a tick at 7/7), from the chapter's done stages (lesson.js part 2, localStorage ruukkilabra:<page>
     { done: [stage ids], of: number of stages }). Over the tiles one row, "Jatka: Luku 4 · <title>, vaihe 4/7 Teoria",
     for the chapter opened last if it is one of the page's and not finished, else the first unfinished chapter after
     a started one. Nothing shows before the reader has started a chapter.
   - The front page: the same row for the chapter opened last in this language (ruukkilabra:viimeisin, lesson.js).
   - The row (teacher 2026-11-13): the Jatka button first, then the chapter and its stage, and Tyhjennä at the other end,
     which clears the progress of this language after a confirmation.
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
  // A title is text with its formulas as $TeX$. A record written before 2026-11-13 holds KaTeX's whole text, the formula
  // three times ("Q=cmΔTQ = cm\Delta TQ=cmΔT"): read as P + X + TeX + X it is mended to P + $TeX$ (never rewritten).
  const mend = (t) => {
    t = String(t || '');
    if (t.includes('$') || !t.includes('\\')) return t;
    for (let k = Math.floor(t.length / 2); k >= 1; k--) {
      const x = t.slice(-k), head = t.slice(0, -k), i = head.indexOf(x);
      if (i < 0) continue;
      const tex = head.slice(i + k);
      if (tex.includes('\\') && tex.trim()) return head.slice(0, i) + '$' + tex.trim() + '$';
    }
    const c = t.indexOf(':'); return c > 0 ? t.slice(0, c).trim() : t;
  };
  const GREEK = { Delta: 'Δ', delta: 'δ', rho: 'ρ', lambda: 'λ', mu: 'μ', alpha: 'α', beta: 'β', omega: 'ω', Omega: 'Ω', pi: 'π', theta: 'θ', varphi: 'φ', sigma: 'σ', eta: 'η', tau: 'τ', cdot: '·', times: '×' };
  const plain = (t) => t.replace(/\$([^$]*)\$/g, (m, x) => x.replace(/\\([A-Za-z]+)/g, (q, n) => GREEK[n] || n).replace(/(Δ|δ|ρ|λ|μ|α|β|ω|Ω|π|θ|φ|σ|η|τ) (?=[A-Za-z])/g, '$1').replace(/\\[,;: ]/g, ' ').replace(/[{}]/g, '').replace(/[_^]/g, '')).replace(/\s+/g, ' ');
  // the formulas set in KaTeX where the page has it (module pages), plain text where it has not (the front page)
  // (jatka.js runs before the KaTeX scripts at the end of a module page, which then set the $TeX$ in <main>; the front page has none)
  const setTitle = (node) => {
    const tex = () => { try { window.renderMathInElement(node, { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false }); } catch (e) { /* the $TeX$ stays */ } };
    if (window.renderMathInElement) return tex();
    if (!document.querySelector('ol.ch-cards')) { node.textContent = plain(node.textContent); return; }
    const late = () => { if (!node.textContent.includes('$')) return; if (window.renderMathInElement) tex(); else node.textContent = plain(node.textContent); };
    if (document.readyState === 'complete') late(); else window.addEventListener('load', late);
  };
  // a tile's title as $TeX$: its rendered formulas back to their TeX
  const tileTitle = (a) => { const c = a.cloneNode(true); c.querySelectorAll('.katex').forEach((k) => { const n = k.querySelector('annotation'); k.replaceWith(n ? '$' + n.textContent.trim() + '$' : (k.querySelector('.katex-html') || k).textContent); }); return c.textContent.replace(/\s+/g, ' ').trim(); };
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  // Tyhjennä (teacher 2026-11-13): clears this language's progress from this browser after a confirmation: the
  // chapters' stage records (ruukkilabra:<page>, { done, of }) and the chapter opened last (ruukkilabra:viimeisin).
  // The reader's answers, solutions, self-assessment and cards (their own keys) are kept.
  const clear = () => {
    if (!window.confirm(T.clear_confirm || 'Tyhjennä eteneminen?')) return;
    try {
      const keys = [];
      for (let i = 0; i < localStorage.length; i++) keys.push(localStorage.key(i));
      keys.forEach((k) => {
        if (!k || !k.startsWith('ruukkilabra:' + PRE)) return;
        const rest = k.slice(('ruukkilabra:' + PRE).length);
        if (!/^[\w.-]+$/.test(rest) || /^(en|fi-easy|fr|sv)$/.test(rest)) return;   // a page's own record, never a key with ':'
        const v = read(k);
        if (v && typeof v === 'object' && Array.isArray(v.done)) localStorage.removeItem(k);
      });
      if (last) localStorage.removeItem('ruukkilabra:viimeisin');
    } catch (e) { /* no storage */ }
    location.reload();
  };
  // the row: the Jatka button where the label was, the chapter and its stage, Tyhjennä at the other end
  const show = (href, num, title, stage) => {
    const go = el('a', 'resume-go', T.resume || 'Jatka'); go.href = href;
    if (T.go) go.setAttribute('aria-label', T.go + ': ' + (num ? num + ' · ' : '') + plain(title));
    const text = el('p', 'resume-text');
    const strong = el('strong', '', (num ? num + ' · ' : '') + title); text.append(strong); setTitle(strong);
    if (stage) text.append(el('span', 'resume-stage', stage));
    const del = el('button', 'resume-clear', T.clear || 'Tyhjennä'); del.type = 'button';
    if (T.clear_label) del.title = T.clear_label;
    del.addEventListener('click', clear);
    box.replaceChildren(go, text, del); box.hidden = false;
  };
  const stageText = (v) => (v && v.n && v.of ? fmt(T.stage, { n: v.n, of: v.of }) + (v.label ? ' ' + v.label : '') : '');

  const tiles = [...document.querySelectorAll('ol.ch-cards li.live:not(.me-tile) .ch-box > a[href]')   /* the module's end tiles (exam, challenge tasks) are not chapters */].map((a) => ({ a, file: a.getAttribute('href'), box: a.closest('.ch-box') }))
    .filter((t) => /^[\w.-]+\.html$/.test(t.file));
  if (!tiles.length) {                       // the front page
    if (last && last.title) show(last.file, last.num || '', mend(last.title), stageText(last));
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
  if (pick) show(pick.t.file, pick.t.num != null ? pick.t.num : ((pick.t.box.querySelector('.l-num') || {}).textContent || '').trim(), tileTitle(pick.t.a), pick.stage);
})();
