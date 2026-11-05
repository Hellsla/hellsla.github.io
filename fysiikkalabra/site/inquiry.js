/* Inquiry lesson behaviour (pages built from inquiry.json; see docs/inquiry.md). Runs after lesson.js, which
   already handles every form.check (numeric answers), the section nav and the staged example.
   Everything stays in the browser. Answers are kept in memory, and copied to localStorage only so that a
   reload on the same device does not lose a prediction; every access is wrapped, and the page works without it.
   1. Predictions (fieldset.choice with data-reveal): the student commits before any feedback; the feedback
      appears only after the linked experiment has recorded data-reveal-min measurements, or, for a prediction
      the simulation cannot test (an explanation), once the linked theory section has been on screen.
   2. Plain choices: feedback for the selected option after "Vastaa" (why it is wrong); one change of answer, then the
      correct option is shown with its reasoning (teacher 2026-11-03). 2b–2c: true-or-false lists and ordering tasks
      (teacher 2026-11-05) answered at once, the wrong items marked, one change, then the right answers.
   3. Experiments (.experiment): drive window.simAdapter — set the initial conditions, lock the controlled
      parameters, record the varied parameter and the measured quantities into a table, reset. The table is kept in
      localStorage (ruukkilabra:<page>:koe<n>) until Nollaa, and copied with Kopioi taulukko (TSV)
      with a decimal comma and the headings' data-plain text (teacher 2026-11-03).
   4. Numeric tasks: common-mistake feedback (data-mistakes) on top of lesson.js; every hint in view and open.
   5. Explanations: model answer and self-assessment criteria once the student has ticked "Olen tehnyt ratkaisun", then
      the unticked criteria as the reasoning to add and where to practise it; a
      conclusion (data-after) also waits for the measurements of its experiments and copies tables and text for notes.
   6. Reflection: shows the student's own predictions next to the evidence and asks whether to revise.
   7. The Ennusta box (details.fold, closed at first): its summary counts the answers; closing it keeps them.
   Its messages come from the page's #fl-strings block (lang/<lang>.json "js", written in by build.py). */
(() => {
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent); } catch (e) { return {}; } })();
  const msg = (k, v) => { const s = (L10N.js || {})[k]; return typeof s === 'string' ? s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m)) : k; };   // lang/<lang>.json "js"
  const key = (id) => 'fl:' + location.pathname.split('/').pop() + ':' + id;
  const store = { get(id) { try { return JSON.parse(localStorage.getItem(key(id))); } catch (e) { return null; } },
                  set(id, v) { try { localStorage.setItem(key(id), JSON.stringify(v)); } catch (e) { /* private mode, blocked storage */ } } };
  const fi = (x) => {
    if (typeof x !== 'number' || !Number.isFinite(x)) return String(x);
    const a = Math.abs(x), s = a >= 100 ? x.toFixed(0) : a >= 10 ? x.toFixed(1) : a >= 1 ? x.toFixed(2) : x.toPrecision(3);
    return s.replace('.', (L10N.format || {}).decimal || ',').replace('-', '−');
  };
  // a value with its unit as maths (teacher 2026-10-28, "kaikki LaTeXilla"): 1,0 s -> $1{,}0\,\text{s}$
  const fiTex = (x, u) => {
    if (typeof x !== 'number' || !Number.isFinite(x)) return String(x);
    const n = fi(x).replace(/,/g, '{,}').replace('−', '-');
    const unitTex = u ? '\\,' + (u === '%' ? '\\%' : '\\text{' + u + '}') : '';
    return '$' + n + unitTex + '$';
  };
  const typeset = (el) => { if (window.renderMathInElement) window.renderMathInElement(el, { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false }); if (window.flGlueMath) window.flGlueMath(el); };
  // an element's content without its form controls, as HTML: rendered formulas stay formulas (textContent would read
  // KaTeX's hidden MathML copy as well and repeat every formula as plain letters)
  const asHtml = (n) => { const c = n.cloneNode(true); c.querySelectorAll('input, .feedback').forEach((x) => x.remove()); c.querySelectorAll('.scenario').forEach((x) => x.after(' ')); return c.innerHTML.trim(); };
  const measured = {};              // experiment id -> number of recorded measurements
  // 3b. the exported table (teacher 2026-11-03): headings without LaTeX (th[data-plain]), numbers with a decimal comma in
  // every language (a Finnish spreadsheet reads them as numbers), TSV for the clipboard (Lataa CSV dropped, teacher 2026-11-04).
  const pageId = (location.pathname.split('/').pop() || 'index').replace(/\.html?$/, '');
  const attr = (t) => String(t).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  const cell = (raw, shownAs) => {     // a measured value as a spreadsheet takes it: 1,25 and -0,500, a word as a word
    if (raw == null && shownAs == null) return '';
    if (typeof raw === 'number') return fi(raw).replace('.', ',').replace('−', '-');
    if (/^-?\d+(?:\.\d+)?$/.test(String(raw))) return String(raw).replace('.', ',');   // a select's number ("0.5")
    return String(shownAs).replace(/\\text\{([^{}]*)\}/g, '$1').replace(/\{,\}/g, ',').replace(/\\[,;: ]/g, ' ').replace(/[${}]/g, '').trim();   // a name in words, maths unwrapped
  };
  const tableRows = (tb) => {
    if (!tb) return [];
    const head = [...tb.querySelectorAll('thead th')].map((th) => (th.dataset.plain || th.textContent).trim());
    const body = [...tb.querySelectorAll('tbody tr')].map((tr) => [...tr.children].map((td) => (td.dataset.value ?? td.dataset.plain ?? td.textContent).trim()));
    return body.length ? [head, ...body] : [];
  };
  const asTsv = (rows) => rows.map((r) => r.map((c) => c.replace(/[\t\r\n]+/g, ' ')).join('\t')).join('\n');
  const copyText = (text, done) => {   // the clipboard API, then a hidden textarea and execCommand('copy')
    const fallback = () => { const t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select(); let ok = false; try { ok = document.execCommand('copy'); } catch (e) { ok = false; } t.remove(); done(ok); };
    try { navigator.clipboard.writeText(text).then(() => done(true), fallback); } catch (e) { fallback(); }
  };
  const showText = (after, text) => {  // neither worked: the text in a field of its own, selected, to copy by hand
    let t = after.nextElementSibling;
    if (!t || !t.classList.contains('exp-export-text')) {
      t = document.createElement('textarea'); t.className = 'exp-export-text'; t.readOnly = true; t.setAttribute('aria-label', msg('exp_copy_text')); after.after(t);
    }
    t.value = text; t.rows = Math.min(12, text.split('\n').length + 1); t.hidden = false; t.focus(); t.select();
  };
  const bus = new EventTarget();

  // 1. a prediction linked to a theory section is revealed once that section has been on screen
  const seen = new Set();
  document.querySelectorAll('fieldset.choice[data-reveal]').forEach((fs) => {
    const t = document.getElementById(fs.dataset.reveal);
    if (!t || t.dataset.type !== 'theory') return;
    const pending = fs.querySelector('.pending');
    if (pending) pending.textContent = pending.dataset.theory;   // the language's 'read the theory section' text
    if (!('IntersectionObserver' in window)) { measured[t.id] = Infinity; return; }
    if (seen.has(t.id)) return;
    seen.add(t.id);
    const io = new IntersectionObserver((es) => { if (es.some((e) => e.isIntersecting)) {
      io.disconnect(); measured[t.id] = Infinity; bus.dispatchEvent(new CustomEvent('fl:measured', { detail: { id: t.id, count: Infinity } })); } },
      { rootMargin: '0px 0px -40% 0px' });   // read, not glimpsed: the section must reach the upper 60 % of the window
    io.observe(t);
  });

  // 1–2. choices
  document.querySelectorAll('fieldset.choice').forEach((fs) => {
    const id = fs.closest('.activity')?.id || fs.querySelector('input')?.name || '';
    const radios = [...fs.querySelectorAll('input[type=radio]')], out = fs.querySelector('output');
    const btn = fs.querySelector('button.commit'), pending = fs.querySelector('.pending'), justify = fs.querySelector('.justify textarea');
    const reveal = fs.dataset.reveal, min = Number(fs.dataset.revealMin || 1);
    const feedbacks = [...fs.querySelectorAll('.feedback')];
    const show = (i) => {
      feedbacks.forEach((f) => { f.hidden = f.dataset.for !== String(i); });
      const ok = radios[i].dataset.correct === '1';
      out.textContent = ok ? msg('correct') : msg('not_quite'); out.dataset.state = ok ? 'ok' : 'no';
      fs.dataset.state = ok ? 'ok' : 'no';
    };
    const commit = (i, silent) => {
      fs.dataset.committed = '1';
      store.set(id, { choice: i, text: radios[i].parentElement.textContent.trim(), html: asHtml(radios[i].parentElement), why: justify ? justify.value : '' });
      if (reveal) {
        radios.forEach((r) => { r.disabled = true; });
        btn.hidden = true;
        if ((measured[reveal] || 0) >= min) { show(i); if (pending) pending.hidden = true; }
        else if (pending) { pending.hidden = false; if (!silent) pending.focus?.(); }
      } else show(i);
      if (!silent) bus.dispatchEvent(new CustomEvent('fl:answered', { detail: { id } }));
    };
    // a plain choice (teacher 2026-11-03): the feedback says why the chosen option is wrong; the answer may be changed
    // once, and after the second try the correct option is shown with its reasoning. A prediction is committed once.
    let tries = 0;
    const finish = () => { radios.forEach((r) => { r.disabled = true; }); btn.hidden = true; };
    btn.addEventListener('click', () => {
      const i = radios.findIndex((r) => r.checked);
      if (i < 0) { out.textContent = msg('choose_first'); out.dataset.state = 'hint'; return; }
      commit(i, false);
      if (window.flAttempt) window.flAttempt(fs, 'choice', radios[i].dataset.correct === '1' ? 'ok' : 'no');
      if (reveal) return;
      tries += 1;
      if (radios[i].dataset.correct === '1') { finish(); return; }
      if (tries < 2) { out.textContent = msg('not_quite') + ' ' + msg('choice_one_more'); return; }
      const c = radios.findIndex((r) => r.dataset.correct === '1');
      if (c >= 0) {
        const li = radios[c].closest('li'); li.classList.add('is-answer');
        const mark = document.createElement('strong'); mark.className = 'answer-mark'; mark.textContent = msg('choice_correct_mark') + ': ';
        const fb = feedbacks.find((f) => f.dataset.for === String(c));
        if (fb) { fb.hidden = false; fb.classList.add('is-answer');
          const first = fb.firstElementChild || fb, t = first.firstChild, ok = msg('correct');   // "Oikein. …" would read oddly after "Oikea vastaus:"
          if (t && t.nodeType === 3 && t.textContent.trimStart().startsWith(ok)) t.textContent = t.textContent.trimStart().slice(ok.length).trimStart();
          first.prepend(mark); }
      }
      out.textContent = msg('choice_reveal'); finish();
    });
    radios.forEach((r) => r.addEventListener('change', () => { if (!reveal) { feedbacks.forEach((f) => { f.hidden = true; }); out.textContent = ''; delete out.dataset.state; delete fs.dataset.state; } }));
    if (justify) justify.addEventListener('input', () => { const s = store.get(id); if (s) { s.why = justify.value; store.set(id, s); } });
    if (reveal) bus.addEventListener('fl:measured', (e) => {
      if (e.detail.id !== reveal || e.detail.count < min) return;
      const i = radios.findIndex((r) => r.checked);
      if (fs.dataset.committed && i >= 0) { show(i); if (pending) pending.hidden = true; }
    });
    const saved = store.get(id);
    if (saved && radios[saved.choice]) { radios[saved.choice].checked = true; if (justify && saved.why) justify.value = saved.why; if (reveal) commit(saved.choice, true); }
  });

  // 2b–2c. A list answered at once (teacher 2026-11-05): true-or-false statements (fieldset.tf) and putting items in
  // order (fieldset.order). "Vastaa" needs every item; the first answer marks the wrong items, they may be changed
  // once, and then every item shows its right answer and (a statement) its reasoning. Not stored: a page reload starts over.
  document.querySelectorAll('fieldset.tf, fieldset.order').forEach((fs) => {
    const tf = fs.classList.contains('tf'), rows = [...fs.querySelectorAll(tf ? '.tf-list > li' : '.order-list > li')];
    const out = fs.querySelector('output'), btn = fs.querySelector('button.commit');
    const given = (li) => tf ? li.querySelector('input:checked')?.value : li.querySelector('select').value;
    const right = (li) => given(li) === (tf ? li.dataset.true : li.dataset.rank);
    const say = (text, state) => { out.textContent = text; out.dataset.state = state; fs.dataset.state = state === 'hint' ? '' : state; };
    let tries = 0;
    const finish = () => { fs.querySelectorAll('input, select').forEach((x) => { x.disabled = true; }); btn.hidden = true; };
    const reveal = () => rows.forEach((li) => {
      li.dataset.state = right(li) ? 'ok' : 'no';
      if (tf) { const fb = li.querySelector('.feedback'); if (fb) { fb.hidden = false;
          const mark = document.createElement('strong'); mark.className = 'answer-mark';
          mark.textContent = msg(li.dataset.true === '1' ? 'tf_is_true' : 'tf_is_false') + '. ';
          (fb.firstElementChild || fb).prepend(mark); } }
      else { const r = li.querySelector('.ord-right'); r.textContent = msg('order_right_place', { n: li.dataset.rank }); r.hidden = false; }
    });
    btn.addEventListener('click', () => {
      if (rows.some((li) => !given(li))) { say(msg(tf ? 'tf_all_first' : 'order_all_first'), 'hint'); return; }
      if (!tf && new Set(rows.map(given)).size !== rows.length) { say(msg('order_distinct'), 'hint'); return; }
      tries += 1;
      const wrong = rows.filter((li) => !right(li));
      if (window.flAttempt) window.flAttempt(fs, 'choice', wrong.length ? 'no' : 'ok');
      bus.dispatchEvent(new CustomEvent('fl:answered', { detail: { id: fs.dataset.id } }));
      rows.forEach((li) => { delete li.dataset.state; });
      if (!wrong.length) { say(msg('list_all_right'), 'ok'); reveal(); finish(); return; }
      if (tries < 2) { wrong.forEach((li) => { li.dataset.state = 'no'; }); say(msg('list_wrong', { n: wrong.length, total: rows.length }), 'no'); return; }
      say(msg('list_reveal'), 'no'); reveal(); finish();
    });
    fs.addEventListener('change', (ev) => { const li = ev.target.closest('li'); if (li && tries < 2) delete li.dataset.state; });
  });

  // 7. the Ennusta box: "2 kysymystä", then "vastattu 1/2", then "vastattu 2/2 · palaute 2/2"
  document.querySelectorAll('details.fold').forEach((fold) => {
    const status = fold.querySelector('.fold-status'), sets = [...fold.querySelectorAll('fieldset.choice')], n = sets.length;
    if (!status || !n) return;
    const update = () => {
      const done = sets.filter((f) => f.dataset.committed).length, shown = sets.filter((f) => f.dataset.state).length;
      status.textContent = done ? msg('fold_answered', { done, n }) + (shown ? msg('fold_feedback', { shown, n }) : '') : msg(n === 1 ? 'fold_question_one' : 'fold_question_many', { n });
    };
    bus.addEventListener('fl:answered', update); bus.addEventListener('fl:measured', update); update();
  });

  // 3. experiments: the physics stays in the simulation; this only sets, locks, reads and resets it.
  // p5 runs the sketch's setup (which defines the adapter) after the window load event, so bind lazily.
  const whenAdapter = (cb) => {
    const t0 = Date.now();
    const tick = () => { if (window.simAdapter) cb(window.simAdapter); else if (Date.now() - t0 < 4000) setTimeout(tick, 100); else cb(null); };
    tick();
  };
  // The page has one simulation. On a wide screen it stays in its column beside the experiments (.lab, site.css), which
  // sticks in view while the student works down through them. On a phone and a tablet an experiment that starts brings
  // it next to its own buttons and table, so the picture, the control being varied and "Kirjaa mittaus" fit one screen;
  // its first place keeps a link. A resize puts it right again. Either way the experiment that drives the simulation is
  // marked (.is-active), and the simulation card names it (.sim-context), so the picture and its task stay linked.
  const simEl = document.getElementById('sim');
  const simHome = simEl ? document.createElement('p') : null;
  if (simHome) { simHome.className = 'sim-moved'; simHome.hidden = true; simEl.before(simHome); }
  const simContext = simEl && simEl.querySelector('.sim-context');
  let activeExp = null;
  const besideLab = () => { const lab = simHome && simHome.closest('.lab'); return !!lab && getComputedStyle(lab).getPropertyValue('--wide').trim() === '1'; };
  const markActive = () => {
    document.querySelectorAll('.activity.is-active').forEach((a) => a.classList.remove('is-active'));
    if (!activeExp) { if (simContext) simContext.textContent = ''; return; }
    const act = activeExp.ex.closest('.activity'); act.classList.add('is-active');
    if (simContext) {
      const sum = act.parentElement.closest('details')?.querySelector(':scope > summary');   // an optional experiment's title is its box's summary
      const shown = (n) => { if (n.nodeType !== 1) return n.textContent; const c = n.cloneNode(true); c.querySelectorAll('.katex-mathml').forEach((m) => m.remove()); return c.textContent; };   // visible text only: KaTeX also carries hidden MathML
      const h3 = act.querySelector('h3');
      const title = (h3 ? shown(h3).trim() : '') || (sum ? [...sum.childNodes].filter((n) => !n.classList?.contains('opt-tag')).map(shown).join('').trim() : '');
      simContext.innerHTML = msg('sim_in_use'); const a = simContext.querySelector('a'); a.href = '#' + activeExp.id; a.textContent = title;
    }
  };
  const placeSim = () => {
    if (!simEl) return;
    simEl.style.marginTop = '';
    if (!activeExp || besideLab()) {
      if (simHome.nextElementSibling !== simEl) simHome.after(simEl);
      simHome.hidden = true;
      return;
    }
    const { ex, id } = activeExp;
    if (!ex.contains(simEl)) ex.querySelector('.exp-controls').before(simEl);
    const title = ex.closest('.activity').querySelector('h3')?.textContent || msg('sim_moved_default');
    simHome.innerHTML = msg('sim_moved');
    const link = simHome.querySelector('a'); link.href = '#' + id; link.textContent = title;
    simHome.hidden = false;
  };
  // The sticky column (.lab-side) never scrolls inside itself (Lauri 2026-11-04). When it is taller than the window it
  // moves with the page until its far edge is in view and sticks there: scrolling down shows its lower part (the
  // controls), scrolling back up brings the picture back, so the page scroll alone reaches all of it.
  const labSide = simEl && simEl.closest('.lab-side');
  if (labSide) {
    let lastY = window.scrollY, lastTop = null, frame = 0;
    const fit = () => {
      frame = 0;
      const dy = window.scrollY - lastY; lastY = window.scrollY;
      labSide.style.top = '';
      const cs = getComputedStyle(labSide);
      if (cs.position !== 'sticky') { lastTop = null; return; }
      const maxTop = parseFloat(cs.top) || 0, minTop = Math.min(maxTop, window.innerHeight - 12 - labSide.offsetHeight);
      if (minTop === maxTop) { lastTop = maxTop; return; }
      const t = Math.max(minTop, Math.min(maxTop, (lastTop === null ? maxTop : lastTop - dy)));
      labSide.style.top = Math.round(t) + 'px';
      lastTop = Math.max(t, labSide.getBoundingClientRect().top);   // where it really is (not stuck yet: its own place)
      lastTop = Math.min(lastTop, maxTop);
    };
    const queue = () => { if (!frame) frame = requestAnimationFrame(fit); };
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue);
    if (window.ResizeObserver) new ResizeObserver(queue).observe(labSide);
    fit();
  }
  const bringSim = (ex, id) => { activeExp = { ex, id }; markActive(); placeSim(); };
  let resizing = false;
  window.addEventListener('resize', () => { if (!resizing) { resizing = true; requestAnimationFrame(() => { resizing = false; placeSim(); }); } });
  document.querySelectorAll('.experiment').forEach((ex) => {
    const id = ex.closest('.activity').id;
    const initial = JSON.parse(ex.dataset.initial), locked = JSON.parse(ex.dataset.locked), vary = ex.dataset.vary, measure = JSON.parse(ex.dataset.measure), min = Number(ex.dataset.min || 2);
    const varyName = ex.dataset.varyName || vary, lockedNames = ex.dataset.lockedNames ? JSON.parse(ex.dataset.lockedNames) : locked;
    const start = ex.querySelector('.exp-start'), rec = ex.querySelector('.exp-record'), reset = ex.querySelector('.exp-reset');
    const tbody = ex.querySelector('tbody'), status = ex.querySelector('.exp-status'), question = ex.querySelector('.exp-question');
    const copyBtn = ex.querySelector('.exp-copy'), expStatus = ex.querySelector('.exp-export-status');
    const n = [...document.querySelectorAll('.experiment')].indexOf(ex) + 1;   // Koe 1, Koe 2, … in page order
    const skey = 'ruukkilabra:' + pageId + ':koe' + n;
    let savedText = null; try { savedText = localStorage.getItem(skey); } catch (e) { savedText = null; }
    const saved = (() => { try { const v = JSON.parse(savedText); return v && v.vary === vary && JSON.stringify(v.measure) === JSON.stringify(measure) && Array.isArray(v.rows) ? v.rows : null; } catch (e) { return null; } })();
    // the table is written at once after every change (a closed tab keeps the last measurement), but only when it changed:
    // a restored table is not written back (2026-11-05)
    let kept;
    const keep = (rs) => {
      const text = rs.length ? JSON.stringify({ vary, measure, rows: rs }) : null;
      if (text !== null && text === kept) return;
      try { if (text) localStorage.setItem(skey, text); else localStorage.removeItem(skey); kept = text; } catch (e) { kept = undefined; /* private mode, blocked storage */ }
    };
    let rows = [], armed = false;
    let words = {}; try { words = JSON.parse(ex.dataset.words || '{}'); } catch (e) { words = {}; }
    const say = (t) => { status.textContent = t; if (t.includes('$')) typeset(status); };
    [start, rec].forEach((b) => { b.disabled = true; });
    if (question) question.hidden = true;
    const announce = () => {
      measured[id] = rows.length;
      bus.dispatchEvent(new CustomEvent('fl:measured', { detail: { id, count: rows.length } }));
      if (question) question.hidden = rows.length < min;
    };
    whenAdapter((A) => {
      const unit = (k) => (A && A.params && A.params[k] && A.params[k].unit ? A.params[k].unit : '');
      const td = (x, u, k, raw) => (words[k] && String(x) in words[k] ? `<td data-plain="${attr(cell('', words[k][String(x)]))}" data-value="${attr(cell(x, words[k][String(x)]))}">${words[k][String(x)]}</td>`   // a select's value or a switch in words ("values" of the experiment)
        : `<td data-plain="${fi(x)}${u ? ' ' + u : ''}" data-value="${attr(cell(raw === undefined ? x : raw, x))}">${fiTex(x, u)}</td>`);   // plain text for the notes, the bare number for the export
      const shown = (x) => (typeof x === 'string' && !(words[vary] && x in words[vary]) && typeof window.__v === 'function' ? window.__v(x) : x);   // a body or material named in the page's language (sim "values")
      const rowEl = (r) => { const tr = document.createElement('tr'); tr.innerHTML = td(shown(r.vary), unit(vary), vary, r.vary) + measure.map((k) => td(r[k], unit(k), k)).join(''); return tr; };
      const changed = () => {
        if (copyBtn) copyBtn.disabled = !rows.length;
        if (expStatus) expStatus.textContent = '';
        keep(rows);
      };
      // the whole table (a restored visit, Nollaa); a new measurement adds and typesets its own row only (2026-11-05:
      // the table used to be rebuilt and every formula in it typeset again after each measurement)
      const render = () => {
        tbody.textContent = '';
        const all = document.createDocumentFragment();
        rows.forEach((r) => all.appendChild(rowEl(r)));
        tbody.appendChild(all);
        typeset(tbody);
        changed();
      };
      const append = (r) => { const tr = rowEl(r); tbody.appendChild(tr); typeset(tr); changed(); };
      if (saved && saved.length) { rows = saved; kept = savedText; render(); announce(); }   // the measurements of an earlier visit, already stored as they are
      if (copyBtn) copyBtn.addEventListener('click', () => {
        const text = asTsv(tableRows(ex.querySelector('table.exp-table')));
        if (!text) return;
        copyText(text, (ok) => { if (ok) { expStatus.textContent = msg('exp_copied'); setTimeout(() => { if (expStatus.textContent === msg('exp_copied')) expStatus.textContent = ''; }, 4000); }
          else { expStatus.textContent = msg('exp_copy_failed'); showText(ex.querySelector('.exp-controls'), text); } });
      });
      if (!A) {
        say(msg('exp_no_sim'));
        if (question) question.hidden = false;
        measured[id] = Infinity; bus.dispatchEvent(new CustomEvent('fl:measured', { detail: { id, count: Infinity } }));   // nothing to wait for
        return;
      }
      const missing = Object.keys(initial).concat(locked, [vary]).filter((k) => !A.params || !A.params[k]);
      if (missing.length) { say(msg('exp_unsupported', { params: missing.join(', ') })); return; }
      start.disabled = false;
      start.addEventListener('click', () => {
        A.set(initial); locked.forEach((k) => A.lock(k, true)); A.lock(vary, false);
        armed = true; rec.disabled = false;
        say(msg('exp_started', { locked: lockedNames.length ? msg('exp_started_locked', { names: lockedNames.join(', ') }) : '', vary: varyName }));
        bringSim(ex, id);
        if (besideLab()) ex.closest('.activity').scrollIntoView({ behavior: 'smooth', block: 'start' });   // the sim is level with it
        else rec.scrollIntoView({ behavior: 'smooth', block: 'end' });
      });
      rec.addEventListener('click', () => {
        if (!armed) { say(msg('exp_start_first')); return; }
        const S = A.get() || {};
        if (!(vary in S) || measure.some((k) => !(k in S))) { say(msg('exp_no_value')); return; }
        const row = { vary: S[vary] };
        measure.forEach((k) => { row[k] = S[k]; });
        if (rows.length && rows[rows.length - 1].vary === row.vary) { say(msg('exp_same_value', { vary: varyName })); return; }
        rows.push(row); append(row); announce();
        say(rows.length < min ? msg('exp_recorded_more', { n: rows.length, vary: varyName, left: min - rows.length }) : msg('exp_recorded_enough', { n: rows.length }));
      });
      reset.addEventListener('click', () => {
        locked.forEach((k) => A.lock(k, false)); A.reset(); rows = []; armed = false; rec.disabled = true; render(); announce();   // render() also clears the stored table
        const t = ex.querySelector('.exp-export-text'); if (t) t.hidden = true;
        say(msg('exp_reset'));
      });
    });
  });

  // 4. numeric tasks: common-mistake feedback
  document.querySelectorAll('.act-numeric form.check, .exp-question form.check, .interpret form.check').forEach((form) => {
    let mistakes = [];
    try { mistakes = JSON.parse(form.dataset.mistakes || '[]'); } catch (e) { mistakes = []; }
    if (!mistakes.length) return;
    const input = form.querySelector('input'), out = form.querySelector('output'), tol = Number(form.dataset.tol);
    form.addEventListener('submit', () => {
      const v = Number(input.value.trim().replace(/\s+/g, '').replace(/−/g, '-').replace(',', '.').replace(/[^\d.eE+-]/g, ''));
      if (!Number.isFinite(v) || out.dataset.state === 'ok' || out.dataset.state === 'close') return;
      const m = mistakes.find((x) => Math.abs(v - x.value) <= (x.value === 0 ? tol : tol * Math.abs(x.value)));
      if (m) { if (m.html) out.innerHTML = m.html; else out.textContent = m.feedback; out.dataset.state = 'no'; if (m.feedback.includes('$')) typeset(out); }
    });
  });
  // hints (teacher 2026-11-04): every hint is in view and opens freely, no lock between them

  // 5. explanations
  const expMin = (eid) => Number(document.querySelector(`#${CSS.escape(eid)} .experiment`)?.dataset.min || 2);
  const tableText = (eid) => {        // an experiment's table as in its own export (TSV), under its title
    const act = document.getElementById(eid), tb = act && act.querySelector('table.exp-table');
    if (!tb) return '';
    const sum = act.parentElement.closest('details')?.querySelector(':scope > summary');   // an optional experiment's title is its box's summary
    const title = act.querySelector('h3')?.textContent.trim() || [...(sum?.childNodes || [])].filter((x) => !x.classList?.contains('opt-tag')).map((x) => x.textContent).join('').trim() || eid;
    const rows = tableRows(tb);
    return [title, rows.length ? asTsv(rows) : [...tb.querySelectorAll('thead th')].map((th) => (th.dataset.plain || th.textContent).trim()).join('\t') + '\n' + msg('copy_no_rows')].join('\n');
  };
  const allExperiments = [...document.querySelectorAll('.experiment')].map((x) => x.closest('.activity')?.id).filter(Boolean);
  document.querySelectorAll('.explain').forEach((ex) => {
    const btn = ex.querySelector('.show-model'), model = ex.querySelector('.model'), ta = ex.querySelector('textarea');
    const copy = ex.querySelector('.copy-notes'), status = ex.querySelector('.explain-status');
    const id = ex.closest('.activity')?.id || '';
    let after = []; try { after = JSON.parse(ex.dataset.after || '[]'); } catch (e) { after = []; }
    const saved = store.get(id); if (saved && saved.text) ta.value = saved.text;
    const say = (t) => { if (status) status.textContent = t; };
    const missing = () => after.filter((eid) => (measured[eid] || 0) < expMin(eid));
    // the model answer (or model diagram) and the criteria open after the tick "Olen tehnyt ratkaisun" (a drawing task:
    // "Olen piirtänyt voimakuvion paperille"); the tick alone is enough, the text field is the student's own (teacher
    // 2026-11-03). The button stays in view, marked unavailable until then; a conclusion still waits for its measurements.
    const tick = ex.querySelector('.drew input'), draw = ex.classList.contains('draw');
    const OPEN = !!window.flSolutionsOpen;
    const ready = () => OPEN || !tick || tick.checked;
    const lockText = msg(draw ? 'locked_drawn' : 'locked_done');
    const lockNote = window.flLockNote ? window.flLockNote(lockText) : Object.assign(document.createElement('span'), { className: 'lock-note', textContent: lockText });
    const mark = () => {
      if (ready()) { btn.removeAttribute('aria-disabled'); lockNote.remove(); }
      else { btn.setAttribute('aria-disabled', 'true'); btn.after(lockNote); }
    };
    if (OPEN && tick) tick.checked = true;
    mark();
    ta.addEventListener('input', () => store.set(id, { text: ta.value }));
    if (tick) tick.addEventListener('change', () => { mark(); if (tick.checked) { if (status && status.textContent && !missing().length) say(''); if (window.flAttempt) window.flAttempt(ex, 'done', 'done'); } });
    btn.addEventListener('click', () => {
      const m = OPEN ? [] : missing();
      if (m.length) { say(msg('explain_measure_first', { experiments: m.map((eid) => document.getElementById(eid)?.querySelector('h3')?.textContent.trim() || eid).join(', ') })); return; }
      if (!ready()) { say(msg(draw ? 'explain_draw_first' : 'explain_tick_first')); tick.focus(); return; }
      say(''); model.hidden = false; btn.hidden = true; model.querySelector('h4')?.focus?.();
    });
    // own answer → model answer → observable criteria → what is missing → where to practise (teacher 2026-10-28)
    const critBtn = ex.querySelector('.check-criteria'), result = ex.querySelector('.crit-result');
    if (critBtn && result) critBtn.addEventListener('click', () => {
      const boxes = [...ex.querySelectorAll('ul.criteria input[type=checkbox]')];
      const missingCrit = boxes.filter((b) => !b.checked).map((b) => b.closest('label').querySelector('span').innerHTML);
      result.querySelector('.crit-msg').textContent = msg(missingCrit.length ? 'criteria_missing' : 'criteria_all');
      result.querySelector('.crit-missing').innerHTML = missingCrit.map((h) => '<li>' + h + '</li>').join('');
      result.querySelector('.crit-practice').hidden = !missingCrit.length;
      result.hidden = false;
      if (missingCrit.length) ta.focus();
    });
    if (copy) copy.addEventListener('click', () => {
      const title = ex.closest('.activity')?.querySelector('h3')?.textContent.trim() || msg('copy_conclusion');
      const text = [document.title, '', ...allExperiments.map(tableText).filter(Boolean).flatMap((t) => [t, '']), title + ':', ta.value.trim() || msg('copy_not_written')].join('\n');   // every experiment's table (teacher 2026-11-03)
      copyText(text, (ok) => { say(ok ? msg('copy_done') : msg('copy_failed')); if (!ok) showText(copy.parentElement, text); });
    });
  });

  // 6. reflection: the student's own predictions beside the evidence
  document.querySelectorAll('.reflect').forEach((r) => {
    const ids = JSON.parse(r.dataset.predictions), list = r.querySelector('.my-predictions');
    const fill = () => {
      list.innerHTML = '';
      ids.forEach((pid) => {
        const act = document.getElementById(pid), fs = act && act.querySelector('fieldset.choice');
        const legend = fs ? asHtml(fs.querySelector('legend')) : pid;
        const saved = store.get(pid);
        const li = document.createElement('li');
        const q = document.createElement('p'); q.className = 'rq'; q.innerHTML = legend; li.appendChild(q);
        const a = document.createElement('p');
        if (saved && fs) {
          const ok = fs.querySelectorAll('input[type=radio]')[saved.choice]?.dataset.correct === '1';
          const revealed = fs.dataset.state !== undefined;
          a.innerHTML = msg('reflect_you_predicted', { text: saved.html || saved.text }) + (saved.why ? ` <em>(${saved.why})</em>` : '') +
            (revealed ? ` — ${ok ? msg('reflect_supported') : msg('reflect_not_supported')}` : msg('reflect_measure_first'));
        } else { a.innerHTML = msg('reflect_not_answered', { href: '#' + pid }); }
        li.appendChild(a); list.appendChild(li);
      });
    };
    fill(); bus.addEventListener('fl:answered', fill); bus.addEventListener('fl:measured', fill);
    const ta = r.querySelector('textarea'), id = r.closest('.activity').id;
    const saved = store.get(id); if (saved && saved.text) ta.value = saved.text;
    ta.addEventListener('input', () => store.set(id, { text: ta.value }));
  });
})();
