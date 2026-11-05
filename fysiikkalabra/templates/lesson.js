/* Lesson page behaviour. Everything runs in the browser and nothing is sent anywhere; only the student's own
   solutions in the solution editor are kept on this device (part 6, padstore.js).
   1. Answer check: compares the typed number with data-answer (±2 %, one unit in the last digit data-step, or the
      wider data-tol; 2–5 % away is "Lähellä") and tells other parts of the attempt (event fl:attempt).
   2. Progress bar: the stage navigation marks the stage on screen and the stages whose answers are all given.
   3. Worked example in stages: reveals the solution one stage at a time.
   4. Print: opens every collapsed block and every hidden stage while printing.
   5. A link to something inside a closed box (the Ennusta box, a hint) opens the box, so the target shows.
   5b. Exercise head: Vastaus and Näytä ratkaisu as buttons beside the Ydintehtävä tag (the boxes open in place).
   6. Solution editor: "Kirjoita ratkaisu" under every exercise opens Abitti's own editor (Digabi rich-text-editor) and
      "Kopioi ratkaisu" copies the solution for L'Math or Abitti. The editor is loaded on the first click only.
   7. Enlarge a figure (teacher 2026-11-03): a click on a figure or a photo, or its "Suurenna kuva" button, shows it
      larger in a dialog, never over the image's own pixels nor about 90 % of the window (sim-embed.js enlarges a simulation).
   8. Try first (teacher 2026-11-03): Vastaus, Näytä ratkaisu and a model answer open only after the student's own
      attempt (one Tarkista, or the tick "Olen tehnyt ratkaisun"); ?ratkaisut=1 opens them all for the teacher.
   Its messages come from the page's #fl-strings block (lang/<lang>.json "js", written in by build.py). */
(() => {
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent); } catch (e) { return {}; } })();
  const msg = (k, v) => { const s = (L10N.js || {})[k]; return typeof s === 'string' ? s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m)) : k; };   // lang/<lang>.json "js"
  const parse = (s) => {
    const t = s.trim().replace(/\s+/g, '').replace(/−/g, '-').replace(',', '.').replace(/[^\d.eE+-]/g, '');
    return t === '' ? NaN : Number(t);
  };
  // A real attempt (teacher 2026-11-03, "opiskelija yrittää ensin itse"): Tarkista with a number, Vastaa with a choice,
  // or the tick "Olen tehnyt ratkaisun". It opens what part 8 keeps locked; other scripts may listen too (the progress bar).
  // detail: id (the task: exercise li, activity or Sovella task), kind check | choice | done, state ok | close | no | done.
  const taskId = (el) => (el.closest('#exercises li[id], section.practice-task[id], .activity[id]') || {}).id || '';
  const attempt = (el, kind, state) => el.dispatchEvent(new CustomEvent('fl:attempt', { bubbles: true, detail: { id: taskId(el), kind, state } }));
  window.flAttempt = attempt;
  // Accepted (teacher 2026-11-03): within 2 % of the model answer or one unit in its shown last significant digit
  // (data-step), whichever is larger, or the task's own wider tolerance; 2–5 % away is "Lähellä", not a rejection.
  document.querySelectorAll('form.check').forEach((form) => {
    const input = form.querySelector('input'), out = form.querySelector('output');
    const ans = Number(form.dataset.answer), tol = Number(form.dataset.tol), step = Number(form.dataset.step) || 0;
    let tries = 0;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = parse(input.value);
      if (!Number.isFinite(v)) { out.textContent = msg('check_number'); out.dataset.state = 'hint'; return; }
      tries += 1;
      const a = Math.abs(ans);
      const accept = ans === 0 ? Math.max(tol, step) : Math.max(0.02 * a, tol * a, step);
      const near = ans === 0 ? 2.5 * accept : Math.max(0.05 * a, 1.25 * accept);
      const diff = Math.abs(v - ans);
      let state;
      if (diff <= accept * (1 + 1e-9)) {
        out.textContent = msg('correct'); state = 'ok'; form.classList.add('is-ok'); input.setAttribute('aria-invalid', 'false');
      } else if (diff <= near * (1 + 1e-9)) {
        out.textContent = msg('check_near'); state = 'close'; input.setAttribute('aria-invalid', 'false');
      } else {
        input.setAttribute('aria-invalid', 'true');
        if (Math.abs(v) > 0 && ans !== 0 && (Math.abs(v / ans) > 900 || Math.abs(ans / v) > 900)) out.textContent = msg('check_magnitude');
        else out.textContent = tries >= 2 ? msg('check_give_up') : msg('check_retry');
        state = 'no';
      }
      out.dataset.state = state;
      attempt(form, 'check', state);
    });
  });

  /* 2. The progress bar (teacher 2026-11-03): the stage navigation sticks under the top edge at every width.
     - The stage on screen is marked (aria-current), seen with an IntersectionObserver on a line at 35 % of the window;
       a tap pins its target until the reader scrolls on, so a short last section can still be marked. While the page
       is read aloud (readaloud.js, event fl:reading) the stage being read is marked instead.
     - A stage is marked done once every required answer in it is given: each choice committed with Vastaa, each number
       checked with Tarkista, each written explanation compared with the model answer. Optional tasks (details.opt) and
       the exercises that are not core tasks do not count. A stage with no required answer (Pohdinta,
       Teoriatiivistelmä) is done once the reader has scrolled to its end. The done stages are kept on this device in localStorage
       (key ruukkilabra:<page>), every access wrapped, and the page works without it.
     - On a narrow window the bar scrolls sideways inside itself and keeps the current stage in view.
     Without JavaScript the bar is a plain list of links. */
  const toc = document.querySelector('nav.toc');
  if (toc) {
    const links = [...toc.querySelectorAll('a[href^="#"]')];
    const pairs = links.map((a) => [a, document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)))]).filter((p) => p[1]);
    const targets = pairs.map((p) => p[1]);
    let pinned = null, reading = null, current = null;
    const keepInView = (a) => {
      if (toc.scrollWidth <= toc.clientWidth + 1 || getComputedStyle(toc).flexDirection === 'column') return;
      const tools = toc.querySelector('.toc-tools'), right = toc.clientWidth - (tools ? tools.offsetWidth : 0);
      const l = a.offsetLeft - toc.scrollLeft, r = l + a.offsetWidth;
      if (l < 8) toc.scrollTo({ left: Math.max(0, a.offsetLeft - 16) });
      else if (r > right - 8) toc.scrollTo({ left: a.offsetLeft + a.offsetWidth - right + 16 });
    };
    const mark = (id) => {
      if (!id || id === current) return;
      current = id;
      links.forEach((a) => {
        const on = a.getAttribute('href') === '#' + id;
        if (on) { a.setAttribute('aria-current', 'step'); keepInView(a); } else a.removeAttribute('aria-current');
      });
    };
    const inView = new Set();
    const update = () => {
      if (reading) return mark(reading);
      if (pinned) return mark(pinned);
      let last = null;
      if (inView.size) targets.forEach((t) => { if (inView.has(t)) last = t; });    // a sub-section (Exit ticket) wins over its stage
      else {
        const line = window.innerHeight * 0.35;
        targets.forEach((t) => { if (t.getBoundingClientRect().top <= line) last = t; });
        if (!last) last = targets[0];
      }
      if (last) mark(last.id);
    };
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((es) => { es.forEach((e) => { if (e.isIntersecting) inView.add(e.target); else inView.delete(e.target); }); update(); },
        { rootMargin: '-35% 0px -64% 0px' });
      targets.forEach((t) => io.observe(t));
    }
    let ticking = false;     // the gaps between sections and old browsers: the last section whose top passed the line
    window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { ticking = false; if (!inView.size) update(); }); } }, { passive: true });
    const reView = () => { const a = links.find((x) => x.hasAttribute('aria-current')); if (a) keepInView(a); };
    window.addEventListener('resize', reView);
    // the Kuuntele tools (readaloud.js) appear in the bar only once a voice is found, after the stage may be marked
    if ('MutationObserver' in window) new MutationObserver(reView).observe(toc, { childList: true, subtree: true, attributes: true, attributeFilter: ['hidden'] });
    links.forEach((a) => a.addEventListener('click', () => { pinned = a.getAttribute('href').slice(1); mark(pinned); setTimeout(() => { pinned = null; }, 900); }));
    document.addEventListener('fl:reading', (e) => { reading = (e.detail && e.detail.id) || null; if (reading) mark(reading); else update(); });
    window.flStageOf = (el) => { let id = null; pairs.forEach(([, t]) => { if (t.contains(el)) id = t.id; }); return id; };
    update();

    // done stages
    const page = (location.pathname.match(/(?:^|\/)((?:en|fi-easy|fr|sv)\/)?([^/]+?)(?:\.html)?$/) || []).slice(1).join('').replace(/\/$/, '') || 'index';
    const KEY = 'ruukkilabra:' + page;
    let saved = { done: [], answered: [] };
    try { const v = JSON.parse(localStorage.getItem(KEY)); if (v && Array.isArray(v.done)) saved = { done: v.done, answered: Array.isArray(v.answered) ? v.answered : [] }; } catch (e) { /* no storage */ }
    const save = () => { try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) { /* private mode, blocked storage */ } };
    const REQUIRED = 'fieldset.choice, form.check, .explain .show-model';
    const required = (sec) => [...sec.querySelectorAll(REQUIRED)].filter((u) => !u.closest('details.opt, #exercises li:not(.core), [hidden]:not(.show-model)'));
    const answered = (u) => (u.dataset.flTried ? true : u.matches('fieldset') ? !!u.dataset.committed
      : u.matches('form') ? /^(ok|no|close)$/.test((u.querySelector('output') || {}).dataset?.state || '') : u.hidden);
    const unitKey = (u) => { const host = u.closest('[id]'); const all = [...host.querySelectorAll(REQUIRED)]; return host.id + ':' + all.indexOf(u); };
    const stages = pairs.filter(([, t]) => t.matches('section.stage')).map(([a, t]) => ({ a, t, units: required(t) }));
    const DONE = msg('stage_done');
    const show = (s) => {
      if (s.a.classList.contains('is-done')) return;
      s.a.classList.add('is-done');
      const sr = document.createElement('span'); sr.className = 'visually-hidden'; sr.textContent = ' (' + DONE + ')'; s.a.append(sr);
    };
    const inside = (r) => r.height > 0 && r.bottom >= 0 && r.bottom <= window.innerHeight;   // its end is on screen
    const check = (scrolled) => {
      let changed = false;
      stages.forEach((s) => {
        s.units.forEach((u) => { const k = unitKey(u); if (answered(u) && !saved.answered.includes(k)) { saved.answered.push(k); changed = true; } });
        const done = s.units.length ? s.units.every((u) => saved.answered.includes(unitKey(u)))
          : scrolled === true && inside(s.t.getBoundingClientRect());
        if (done && !saved.done.includes(s.t.id)) { saved.done.push(s.t.id); changed = true; }
        if (saved.done.includes(s.t.id)) show(s);
      });
      if (changed) save();
    };
    if (stages.length) {
      const later = () => setTimeout(check, 0);       // after the page's own handlers (inquiry.js) have run
      document.addEventListener('click', later); document.addEventListener('submit', later);
      document.addEventListener('fl:attempt', (e) => {   // a real attempt reported by the page's scripts ({id, kind, state})
        const el = e.detail && e.detail.id ? document.getElementById(e.detail.id) : null;
        if (el) (el.matches(REQUIRED) ? [el] : [...el.querySelectorAll(REQUIRED)]).forEach((u) => { u.dataset.flTried = '1'; });
        later();
      });
      let read = 0;
      window.addEventListener('scroll', () => { if (!read) read = setTimeout(() => { read = 0; check(true); }, 250); }, { passive: true });
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', later); else later();
    }
  }

  // Worked example in stages: stage 1 is shown, "Näytä seuraava vaihe" reveals one more, "Näytä kaikki" the rest.
  document.querySelectorAll('.worked').forEach((w) => {
    const steps = [...w.querySelectorAll('.step')];
    const next = w.querySelector('.next-step'), all = w.querySelector('.all-steps');
    let shown = 1;
    const show = () => {
      steps.forEach((s, i) => { s.hidden = i >= shown; });
      const done = shown >= steps.length;
      next.hidden = done; all.hidden = done;
    };
    w.classList.add('js');
    next.addEventListener('click', () => { shown += 1; show(); steps[shown - 1].focus?.(); });
    all.addEventListener('click', () => { shown = steps.length; show(); });
    steps.forEach((s) => s.setAttribute('tabindex', '-1'));
    show();
  });

  const openTo = (id) => {
    const t = id && document.getElementById(id);
    for (let d = t && t.closest('details:not([open])'); d; d = d.parentElement && d.parentElement.closest('details:not([open])')) d.open = true;
  };
  const hashId = (h) => { try { return decodeURIComponent(h.slice(1)); } catch (e) { return ''; } };
  document.addEventListener('click', (e) => { const a = e.target.closest && e.target.closest('a[href^="#"]'); if (a) openTo(hashId(a.getAttribute('href'))); });
  window.addEventListener('hashchange', () => openTo(hashId(location.hash)));
  if (location.hash) openTo(hashId(location.hash));

  // 5b. Exercise head row (teacher 2026-11-01): "Vastaus" and "Näytä ratkaisu" sit beside the Ydintehtävä tag at the
  // top of the exercise, as buttons; what they open stays where it is, after the answer box and the editor. Without
  // scripts the boxes keep their own summaries (site.css hides them only under li.ex-js).
  document.querySelectorAll('#exercises li[id]').forEach((li) => {
    const boxes = [...li.querySelectorAll(':scope > details.answer, :scope > details.solution')];
    if (!boxes.length || !li.querySelector(':scope > .task')) return;
    const head = document.createElement('div'); head.className = 'ex-head';
    const num = li.querySelector(':scope > .ex-num'); if (num) head.append(num);   // the running number "6-3" first (build.py number_label)
    const tag = li.querySelector(':scope > .ex-core'); if (tag) head.append(tag);
    boxes.forEach((d, i) => {
      d.id = d.id || `${li.id}-${d.classList.contains('answer') ? 'answer' : 'solution'}`;
      const b = document.createElement('button'); b.type = 'button'; b.className = 'ex-toggle';
      b.textContent = d.querySelector(':scope > summary').textContent; b.setAttribute('aria-controls', d.id);
      const sync = () => b.setAttribute('aria-expanded', String(d.open));
      b.addEventListener('click', () => { d.open = !d.open; });
      d.addEventListener('toggle', sync); sync();
      head.append(b);
    });
    li.prepend(head); li.classList.add('ex-js');
  });

  // 6. Solution editor (teacher 2026-11-01). Every exercise the build writes (build.py exercise_html: an <li id> with a
  // p.task, in #exercises) and every Sovella itsenäisesti task (practice.py: section.practice-task > .task-card) gets
  // the button, so every page, now and later, has it without a change to a lesson or task. The answer box, the
  // check, the answer, the model solution and the rubric are left as they are; the editor goes before them (in an
  // exercise before the answer box too: the student writes the solution first, then checks the number).
  // Phase 2 (teacher 2026-11-01): each solution is kept in this browser on this device, keyed by the task's id
  // (padstore.js, IndexedDB, loaded with the editor): saved a moment after each change, restored when the editor
  // opens, with export/import of a backup file and deletion. Nothing is sent anywhere.
  const PAD_TASKS = [   // [the task, its part the editor goes in, what it goes before]
    ['#exercises li[id]', (t) => t.querySelector(':scope > .task') && t, (box) => box.querySelector(':scope > form.check, :scope > label.solved, :scope > details.answer')],   // write first, then check (teacher 2026-11-01)
    ['section.practice-task[id]', (t) => t.querySelector(':scope > .task-card'), (box) => box.querySelector(':scope > label.solved, :scope > details.reveal')],
  ];
  const HERE = document.currentScript ? document.currentScript.src : location.href;
  const VENDOR = new URL('vendor/digabi/', HERE).href;
  let padLib = null;
  const load = (src, base = VENDOR) => new Promise((ok, fail) => { const s = document.createElement('script'); s.src = new URL(src, base).href; s.onload = ok; s.onerror = fail; document.head.appendChild(s); });
  const loadPad = () => padLib || (padLib = (() => {
    const css = document.createElement('link'); css.rel = 'stylesheet'; css.href = VENDOR + 'mathquill.css'; document.head.appendChild(css);
    window.MathJax = { startup: { typeset: false }, options: { enableMenu: false }, svg: { fontCache: 'none' } };   // never touches the KaTeX page
    return Promise.all([load('tex-svg.js'), load('rich-text-editor-bundle.js'), load('padstore.js', HERE)]).then(() => window.MathJax.startup.promise);
  })().catch((e) => { padLib = null; throw e; }));
  // Abitti draws a formula on its server; here MathJax draws it into a self-contained SVG with the LaTeX in alt,
  // which the editor (and Abitti, on paste) reads back as an editable formula.
  const drawLatex = (img, latex) => {
    const svg = window.MathJax.tex2svg(latex, { display: false }).querySelector('svg');
    svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    img.setAttribute('src', 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svg.outerHTML))));
    img.setAttribute('alt', latex);
  };
  // The clipboard gets the editor's own HTML (text, line breaks, formulas as images with LaTeX in alt, pictures) and
  // a plain-text copy with each formula as \( LaTeX \), for a program that only takes text.
  const plainOf = (html) => {
    const d = document.createElement('div'); d.innerHTML = html;
    d.querySelectorAll('img').forEach((i) => i.replaceWith(i.alt && !/^data:image\/(png|jpe?g)/.test(i.src) ? `\\(${i.alt}\\)` : ''));
    d.querySelectorAll('br').forEach((b) => b.replaceWith('\n'));
    d.querySelectorAll('div,p').forEach((b) => b.prepend('\n'));
    return d.textContent.replace(/ /g, ' ').replace(/^\n+/, '').replace(/\n{3,}/g, '\n\n').trim();
  };
  const copyHtml = (html) => {
    const text = plainOf(html);
    const viaEvent = () => {   // the older route, for a browser without navigator.clipboard.write
      let done = false;
      const on = (e) => { e.preventDefault(); e.clipboardData.setData('text/html', html); e.clipboardData.setData('text/plain', text); done = true; };
      document.addEventListener('copy', on, { once: true });
      try { document.execCommand('copy'); } catch (e) { /* done stays false */ }
      document.removeEventListener('copy', on);
      return done ? Promise.resolve() : Promise.reject(new Error('copy'));
    };
    if (navigator.clipboard && window.ClipboardItem) {
      return navigator.clipboard.write([new ClipboardItem({ 'text/html': new Blob([html], { type: 'text/html' }), 'text/plain': new Blob([text], { type: 'text/plain' }) })]).catch(viaEvent);
    }
    return viaEvent();
  };
  // The open editors by task id (to refresh them after an import or "Poista kaikki") and their pending saves.
  const editors = new Map();
  const saveError = (e) => msg({ quota: 'pad_save_quota', unavailable: 'pad_save_unavailable', corrupt: 'pad_save_corrupt' }[e && e.code] || 'pad_save_failed');
  const say = (el, text, state) => { el.textContent = text; if (state) el.dataset.state = state; else delete el.dataset.state; };
  const flushAll = () => Promise.all([...editors.values()].map((ed) => ed.flush()));
  const unsaved = () => [...editors.values()].some((ed) => ed.busy());
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') flushAll(); });
  window.addEventListener('pagehide', flushAll);
  window.addEventListener('beforeunload', (e) => { if (unsaved()) { flushAll(); e.preventDefault(); e.returnValue = ''; } });   // a change still on its way asks before leaving
  // "Tallennetut ratkaisut": a backup file of every saved solution, bringing one back, and deleting all (one panel
  // per open editor; all act on the whole store of this device).
  const backupPanel = (status) => {
    const d = document.createElement('details'); d.className = 'pad-saved';
    const sum = document.createElement('summary'); sum.textContent = msg('pad_saved_title');
    const row = document.createElement('div'); row.className = 'pad-tools';
    const mk = (key) => { const b = document.createElement('button'); b.type = 'button'; b.className = 'pad-btn'; b.textContent = msg(key); row.append(b); return b; };
    const exp = mk('pad_export'), imp = mk('pad_import'), del = mk('pad_delete_all');
    const file = document.createElement('input'); file.type = 'file'; file.accept = 'application/json,.json'; file.hidden = true;
    const note = document.createElement('p'); note.className = 'pad-note'; note.textContent = msg('pad_backup_note');
    d.append(sum, note, row, file);
    exp.addEventListener('click', () => flushAll().then(() => window.flPadStore.backup()).then((text) => {
      const n = JSON.parse(text).solutions.length;
      const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
      a.download = `ruukkilabra-ratkaisut-${new Date().toISOString().slice(0, 10)}.json`; document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 1000);
      say(status, msg('pad_exported', { n }), 'ok');
    }, (e) => say(status, saveError(e), 'no')));
    imp.addEventListener('click', () => file.click());
    file.addEventListener('change', () => {
      const f = file.files && file.files[0]; file.value = '';
      if (!f) return;
      f.text().then((text) => window.flPadStore.restore(text)).then(({ restored }) => {
        restored.forEach((r) => { const ed = editors.get(r.id); if (ed) ed.set(r.html); });
        say(status, msg('pad_imported', { n: restored.length }), 'ok');
      }, (e) => say(status, e && e.code === 'format' ? msg('pad_import_failed') : saveError(e), 'no'));
    });
    del.addEventListener('click', () => {
      if (!window.confirm(msg('pad_delete_all_confirm'))) return;
      editors.forEach((ed) => ed.cancel());
      window.flPadStore.clear().then(() => { editors.forEach((ed) => ed.set('', true)); say(status, msg('pad_deleted_all'), 'ok'); },
        (e) => say(status, saveError(e), 'no'));
    });
    return d;
  };
  PAD_TASKS.forEach(([sel, partOf, beforeOf]) => document.querySelectorAll(sel).forEach((task) => {
    const li = partOf(task);
    if (!li) return;
    const id = task.id + '-pad';
    const open = document.createElement('button');
    open.type = 'button'; open.className = 'pad-open'; open.textContent = msg('pad_write');
    open.setAttribute('aria-expanded', 'false'); open.setAttribute('aria-controls', id);
    const box = document.createElement('div'); box.className = 'pad'; box.id = id; box.hidden = true;
    li.insertBefore(open, beforeOf(li));
    open.after(box);
    let answer = { answerHtml: '' }, made = false;
    const status = document.createElement('p'); status.className = 'pad-status'; status.setAttribute('aria-live', 'polite');
    open.addEventListener('click', () => {
      const show = box.hidden;
      box.hidden = !show; open.setAttribute('aria-expanded', String(show)); open.textContent = msg(show ? 'pad_hide' : 'pad_write');
      if (!show || made) { if (show) box.querySelector('.rich-text-editor')?.focus(); return; }
      made = true;
      box.append(status); status.textContent = msg('pad_loading');
      loadPad().then(() => window.flPadStore.get(task.id).then((html) => ({ html }), (e) => ({ html: '', error: e }))).then((saved) => {
        const label = document.createElement('span'); label.id = id + '-label'; label.hidden = true; label.textContent = msg('pad_label');
        const root = document.createElement('div'); root.className = 'pad-editor';
        const tools = document.createElement('div'); tools.className = 'pad-tools';
        const copy = document.createElement('button'); copy.type = 'button'; copy.className = 'pad-copy'; copy.textContent = msg('pad_copy');
        const note = document.createElement('p'); note.className = 'pad-note'; note.textContent = msg('pad_note');
        const del = document.createElement('button'); del.type = 'button'; del.className = 'pad-btn pad-delete'; del.textContent = msg('pad_delete');
        const saveState = document.createElement('p'); saveState.className = 'pad-save'; saveState.setAttribute('aria-live', 'polite');
        tools.append(copy, del, status);
        box.replaceChildren(label, root, saveState, tools, note, backupPanel(status));
        status.textContent = '';
        // autosave: a change marks the solution dirty and is written 0,8 s after the last keystroke; leaving the page
        // writes at once (flushAll). "Tallennettu" is shown only after the write has committed.
        let timer = 0, dirty = false, writing = null, last = saved.html, quiet = false;
        const flush = () => {
          clearTimeout(timer);
          if (!dirty) return writing || Promise.resolve();
          dirty = false; const html = answer.answerHtml || '';
          const w = (writing || Promise.resolve()).catch(() => {}).then(() => window.flPadStore.put(task.id, html, location.pathname.split('/').pop()))
            .then(() => { last = html; if (!dirty) say(saveState, msg('pad_saved'), 'ok'); },
              (e) => { dirty = true; say(saveState, saveError(e), 'no'); })
            .finally(() => { if (writing === w) writing = null; });
          return (writing = w);
        };
        const changed = (a) => {
          answer = a;
          if (quiet || (a.answerHtml || '') === last && !dirty) return;   // the editor reporting the value it was given
          dirty = true; say(saveState, msg('pad_saving'));
          clearTimeout(timer); timer = setTimeout(flush, 800);
        };
        answer = { answerHtml: saved.html };
        const ref = window.makeRichText({ container: root, language: 'FI', onLatexUpdate: drawLatex, onValueChange: changed, initialValue: saved.html,
          textAreaProps: { ariaLabelledBy: label.id, lang: document.documentElement.lang } });
        if (saved.error) say(saveState, saveError(saved.error), 'no');
        else if (saved.html) say(saveState, msg('pad_restored'), 'ok');
        editors.set(task.id, {
          flush, busy: () => dirty || !!writing,
          cancel: () => { clearTimeout(timer); dirty = false; },
          // set the editor's content from outside (import, delete): stored already, so it is not saved again
          set: (html, gone) => { quiet = true; last = html; answer = { answerHtml: html }; try { ref.current && ref.current.setValue(html); } finally { setTimeout(() => { quiet = false; }, 0); }
            say(saveState, gone ? '' : msg('pad_restored'), gone ? null : 'ok'); },
        });
        del.addEventListener('click', () => {
          if (!window.confirm(msg('pad_delete_confirm'))) return;
          editors.get(task.id).cancel();
          window.flPadStore.remove(task.id).then(() => { editors.get(task.id).set('', true); say(status, msg('pad_deleted'), 'ok'); },
            (e) => say(status, saveError(e), 'no'));
        });
        copy.addEventListener('click', () => {
          if (!answer.answerHtml) { status.textContent = msg('pad_empty'); status.dataset.state = 'hint'; return; }
          copyHtml(answer.answerHtml).then(() => { status.textContent = msg('pad_copied'); status.dataset.state = 'ok'; },
            () => { status.textContent = msg('pad_copy_failed'); status.dataset.state = 'no'; });
        });
        setTimeout(() => root.querySelector('.rich-text-editor')?.focus(), 0);
      }, () => { made = false; status.textContent = msg('pad_failed'); status.dataset.state = 'no'; });
    });
  }));

  // 7. Enlarge a figure (teacher 2026-11-03, "kuvat aukeaa klikkaamalla isoksi, ei kuitenkaan liian isoksi"). Every
  // figure (svg role="img") and every photo or screenshot (figure > img) in the page opens larger in a modal dialog:
  // as large as fits in about 92 % of the window, but a photo never over its own pixels and a drawing never over
  // 1,6 times its drawn size (at most 1200 px). On a phone, where the window is no wider than the figure already is,
  // it opens 1,6 times larger in a box that scrolls. A button (shown on hover and keyboard focus) gives the same to
  // the keyboard; Esc, the close button or a click closes it, and the focus returns to where it was. Figures inside
  // controls, the simulation and the interactive course components are left as they are.
  const ZOOM_SKIP = '#sim, .fx, button, a, label, summary, [contenteditable], .pad, .zoom-dlg, [data-nozoom]';
  const zoomable = (el) => el && el.matches('main svg[role="img"], main figure > img') && !el.parentElement.closest(ZOOM_SKIP + ', svg');
  const ZOOM_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  let zdlg = null, zstage = null, zcap = null, zfrom = null;
  const zoomDialog = () => {
    if (zdlg) return zdlg;
    zdlg = document.createElement('dialog'); zdlg.className = 'zoom-dlg'; zdlg.setAttribute('aria-label', msg('zoom_dialog'));
    zdlg.innerHTML = '<button type="button" class="zoom-close"><span aria-hidden="true">×</span> </button><div class="zoom-stage"></div><div class="zoom-cap"></div>';
    const close = zdlg.querySelector('.zoom-close'); close.append(msg('zoom_close'));
    zstage = zdlg.querySelector('.zoom-stage'); zcap = zdlg.querySelector('.zoom-cap');
    close.addEventListener('click', () => zdlg.close());
    zdlg.addEventListener('click', (e) => { if (!zcap.contains(e.target) && !close.contains(e.target)) zdlg.close(); });   // a click on the picture or around it closes
    zdlg.addEventListener('close', () => {
      zstage.textContent = ''; zcap.textContent = ''; document.documentElement.classList.remove('zoom-open');
      if (zfrom && zfrom.isConnected) zfrom.focus({ preventScroll: true }); zfrom = null;
    });
    document.body.appendChild(zdlg);
    return zdlg;
  };
  const openZoom = (el, from) => {
    const d = zoomDialog(), r = el.getBoundingClientRect();
    let node, w0, h0, cap;
    if (el.tagName === 'IMG') {
      node = new Image(); node.src = el.currentSrc || el.src; node.alt = el.alt; node.decoding = 'async';
      w0 = el.naturalWidth || r.width; h0 = el.naturalHeight || r.height; cap = w0;
    } else {
      node = el.cloneNode(true);
      [node, ...node.querySelectorAll('[id]')].forEach((n) => n.removeAttribute('id'));   // its markers and gradients still resolve to the figure on the page
      const vb = el.viewBox && el.viewBox.baseVal;
      w0 = vb && vb.width ? vb.width : r.width; h0 = vb && vb.height ? vb.height : r.height;
      cap = Math.min(1200, Math.max(720, r.width * 1.6));
      node.removeAttribute('width'); node.removeAttribute('height'); node.classList.remove('zoomable');
    }
    const fig = el.closest('figure'), fc = fig && fig.querySelector(':scope > figcaption');
    if (fc) zcap.innerHTML = fc.innerHTML;
    zstage.textContent = ''; zstage.appendChild(node);
    document.documentElement.classList.add('zoom-open');
    zfrom = from || document.activeElement;
    d.showModal();
    const ar = h0 / w0 || 0.6;
    const roomW = Math.min(window.innerWidth * 0.92, 1200), roomH = window.innerHeight * 0.92 - zcap.offsetHeight - d.querySelector('.zoom-close').offsetHeight - 24;
    let w = Math.min(roomW, roomH / ar, cap);
    if (w < r.width * 1.1) w = Math.min(cap, Math.max(w, r.width * 1.6));   // a phone: larger than the window, the box scrolls
    node.style.width = Math.round(w) + 'px'; node.style.height = Math.round(w * ar) + 'px'; node.style.maxWidth = 'none';
    zstage.classList.toggle('zoom-pan', w > roomW + 1 || w * ar > roomH + 1);
    zstage.scrollLeft = 0; zstage.scrollTop = 0;
    d.querySelector('.zoom-close').focus({ preventScroll: true });
  };
  const wire = (el) => {
    if (el.classList.contains('zoomable')) return;
    el.classList.add('zoomable');
    const host = el.parentElement; host.classList.add('zoom-host');
    const b = document.createElement('button'); b.type = 'button'; b.className = 'zoom-btn';
    b.setAttribute('aria-label', msg('zoom_open')); b.title = msg('zoom_open'); b.innerHTML = ZOOM_ICON;
    b.addEventListener('click', (e) => { e.stopPropagation(); openZoom(el, b); });
    el.after(b);
  };
  document.querySelectorAll('main svg[role="img"], main figure > img').forEach((el) => {
    if (!zoomable(el)) return;
    if (el.tagName !== 'IMG') { wire(el); return; }
    // a photo only when it has more pixels than the page shows (a screenshot at its own size would not grow)
    const check = () => { const w = el.getBoundingClientRect().width; if (el.naturalWidth > (w || el.width || 0) * 1.15) wire(el); };
    if (el.complete && el.naturalWidth) check(); else el.addEventListener('load', check, { once: true });
  });
  document.addEventListener('click', (e) => {
    const el = e.target.closest && e.target.closest('svg.zoomable, img.zoomable');
    if (!el || !zoomable(el) || e.defaultPrevented || (window.getSelection && String(window.getSelection()).length)) return;
    openZoom(el, el.parentElement.querySelector(':scope > .zoom-btn'));
  });

  // 8. Try first (teacher 2026-11-03, "opiskelija yrittää ensin itse, ja ratkaisu avautuu vasta sen jälkeen"). A numeric
  // task's Vastaus and Näytä ratkaisu open after one Tarkista with a number (part 1); a written task's answer, an
  // exercise drawn on paper and a Sovella itsenäisesti task's model answer and rubric after the tick "Olen tehnyt
  // ratkaisun" (label.solved; an inquiry explanation's own tick is in inquiry.js). A locked control stays in view,
  // dimmed, with a lock symbol beside it (the reason as hover and screen-reader text), so the student knows the solution is there. Nothing is kept: a reload locks
  // again. ?ratkaisut=1 (the teacher) opens every lock on the page.
  const OPEN_ALL = (() => { try { return new URLSearchParams(location.search).get('ratkaisut') === '1'; } catch (e) { return false; } })();
  window.flSolutionsOpen = OPEN_ALL;
  if (OPEN_ALL) {
    const main = document.querySelector('main');
    if (main) { const p = document.createElement('p'); p.className = 'teacher-note'; p.setAttribute('role', 'note'); p.textContent = msg('teacher_mode'); main.prepend(p); }
  }
  // a locked box's summary does not open it (a click, Enter or Space all arrive as a click); a script may still open it
  document.addEventListener('click', (e) => {
    const sum = e.target.closest && e.target.closest('summary');
    if (sum && sum.parentElement.dataset.locked && sum.parentElement.firstElementChild === sum) e.preventDefault();
  }, true);
  // Only the lock symbol shows; the reason stays as hover text (title) and as hidden text for screen readers (teacher 2026-11-04).
  const lockNote = window.flLockNote = (text, n) => {
    n = n || document.createElement('span'); n.className = 'lock-note'; n.title = text;
    const t = document.createElement('span'); t.className = 'visually-hidden'; t.textContent = text; n.replaceChildren(t);
    return n;
  };
  const lockBoxes = (boxes, why) => {
    if (OPEN_ALL || !boxes.length) return () => {};
    const notes = [], buttons = [];
    const note = () => { const n = lockNote(msg(why)); notes.push(n); return n; };
    const head = boxes[0].parentElement.querySelector(':scope > .ex-head');
    boxes.forEach((d) => {
      d.open = false; d.dataset.locked = '1';
      const sum = d.querySelector(':scope > summary'); sum.setAttribute('aria-disabled', 'true');
      const b = head && d.id ? head.querySelector(`button.ex-toggle[aria-controls="${CSS.escape(d.id)}"]`) : null;
      if (b) { b.disabled = true; b.setAttribute('aria-disabled', 'true'); buttons.push(b); }
      else sum.append(note());
    });
    if (buttons.length) { const n = note(); n.id = boxes[0].parentElement.id + '-lock'; head.append(n); buttons.forEach((b) => b.setAttribute('aria-describedby', n.id)); }
    let open = false;
    return () => {
      if (open) return; open = true;
      boxes.forEach((d) => { delete d.dataset.locked; d.querySelector(':scope > summary').removeAttribute('aria-disabled'); });
      buttons.forEach((b) => { b.disabled = false; b.removeAttribute('aria-disabled'); b.removeAttribute('aria-describedby'); });
      notes.forEach((n) => n.remove());
    };
  };
  const boxesIn = (el) => [...el.querySelectorAll(':scope > details.answer, :scope > details.solution, :scope > details.reveal')];
  document.querySelectorAll('form.check').forEach((form) => {
    const box = form.closest('#exercises li[id]') || form.closest('.numeric');
    if (!box) return;
    const unlock = lockBoxes(boxesIn(box), 'locked_try');
    form.addEventListener('fl:attempt', unlock);
  });
  document.querySelectorAll('label.solved').forEach((label) => {
    const tick = label.querySelector('input'), unlock = lockBoxes(boxesIn(label.parentElement), 'locked_done');
    if (OPEN_ALL) tick.checked = true;
    tick.addEventListener('change', () => { if (tick.checked) { unlock(); attempt(label, 'done', 'done'); } });
  });

  let opened = [];
  window.addEventListener('beforeprint', () => {
    opened = [...document.querySelectorAll('details:not([open])')];
    opened.forEach((d) => { d.open = true; });
    document.querySelectorAll('.worked .step[hidden]').forEach((s) => { s.hidden = false; s.dataset.printOpened = '1'; });
  });
  window.addEventListener('afterprint', () => {
    opened.forEach((d) => { d.open = false; }); opened = [];
    document.querySelectorAll('.worked .step[data-print-opened]').forEach((s) => { s.hidden = true; delete s.dataset.printOpened; });
  });
})();

/* Inline formulas never break onto two lines (Lauri 2026-11-04; site.css .katex nowrap). An inline formula wider
   than its text column (a long calculation on a 360 px phone) is moved onto its own line and scrolls sideways,
   like display maths, instead of overflowing the page. Re-checked on resize and when a <details> opens. */
(function () {
  const SKIP = '.katex-display,.eq-chain,svg,.sim-tex-layer,.fig-tex,#sim-root';
  // The punctuation glued after a formula (lesson.html flGlueMath: "⁠." or inside a .math-glue span) cannot start
  // a line, so it counts in the formula's width; when the formula goes onto its own line, the mark goes with it.
  const host = k => { const h = k.parentNode; return h && h.nodeName === 'SPAN' && !h.className && h.childNodes.length === 1 ? h : k; };
  const PUNCT = /^⁠?[,.;:!?)\]]+/;
  function fit(root) {
    const ks = [...(root || document).querySelectorAll('.katex')].filter(k => !k.closest(SKIP));
    ks.forEach(k => {
      k.classList.remove('kx-wide');
      const m = k.querySelector(':scope>.kx-punct');
      if (m) { const h = host(k), n = h.nextSibling; if (n && n.nodeType === 3) n.data = m.dataset.text + n.data; else h.after(m.dataset.text); m.remove(); }
    });
    const W = document.documentElement.clientWidth;
    ks.forEach(k => {
      if (!k.offsetParent) return;
      let box = k.parentElement.closest('p,li,td,th,dd,dt,div,summary,figcaption,blockquote,label,.steps,.stage');
      while (box && box.parentElement && getComputedStyle(box).display === 'inline-block') box = box.parentElement;   // an inline-block box grows with the formula (fy5-15 answer)
      const r = k.getBoundingClientRect();
      const n = host(k).nextSibling, p = n && n.nodeType === 3 && n.data.match(PUNCT);
      let end = r.right;
      if (p) { const g = document.createRange(); g.setStart(n, 0); g.setEnd(n, p[0].length); end = Math.max(end, g.getBoundingClientRect().right); }
      const right = Math.min(W, box ? box.getBoundingClientRect().right : W);
      if (end > right + 1 || (box && r.width > box.clientWidth + 1)) {
        k.classList.add('kx-wide');
        if (p) { const s = document.createElement('span'); s.className = 'kx-punct'; s.dataset.text = p[0]; s.textContent = p[0].replace('⁠', ''); k.append(s); n.data = n.data.slice(p[0].length); }
      }
    });
  }
  let t; const later = () => { clearTimeout(t); t = setTimeout(() => fit(), 150); };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => fit()); else fit();
  window.addEventListener('load', () => fit()); window.addEventListener('resize', later);
  document.addEventListener('toggle', e => { fit(e.target); later(); }, true);   // later: maths auto-rendered on open
  new MutationObserver(later).observe(document.body, {subtree: true, attributes: true, attributeFilter: ['hidden']});   // a solution unlocked (try-first) or revealed
  window.flFitMath = fit;
})();
