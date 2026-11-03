/* Lesson page behaviour. Everything runs in the browser and nothing is sent anywhere; only the student's own
   solutions in the solution editor are kept on this device (part 6, padstore.js).
   1. Answer check: compares the typed number with data-answer within the relative data-tol.
   2. Section nav: marks the section currently on screen.
   3. Worked example in stages: reveals the solution one stage at a time.
   4. Print: opens every collapsed block and every hidden stage while printing.
   5. A link to something inside a closed box (the Ennusta box, a hint) opens the box, so the target shows.
   5b. Exercise head: Vastaus and Näytä ratkaisu as buttons beside the Ydintehtävä tag (the boxes open in place).
   6. Solution editor: "Kirjoita ratkaisu" under every exercise opens Abitti's own editor (Digabi rich-text-editor) and
      "Kopioi ratkaisu" copies the solution for L'Math or Abitti. The editor is loaded on the first click only.
   7. Enlarge a figure (teacher 2026-11-03): a click on a figure or a photo, or its "Suurenna kuva" button, shows it
      larger in a dialog, never over the image's own pixels nor about 90 % of the window (sim-embed.js enlarges a simulation).
   Its messages come from the page's #fl-strings block (lang/<lang>.json "js", written in by build.py). */
(() => {
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent); } catch (e) { return {}; } })();
  const msg = (k, v) => { const s = (L10N.js || {})[k]; return typeof s === 'string' ? s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m)) : k; };   // lang/<lang>.json "js"
  const parse = (s) => {
    const t = s.trim().replace(/\s+/g, '').replace(/−/g, '-').replace(',', '.').replace(/[^\d.eE+-]/g, '');
    return t === '' ? NaN : Number(t);
  };
  document.querySelectorAll('form.check').forEach((form) => {
    const input = form.querySelector('input'), out = form.querySelector('output');
    const ans = Number(form.dataset.answer), tol = Number(form.dataset.tol);
    let tries = 0;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const v = parse(input.value);
      if (Number.isNaN(v)) { out.textContent = msg('check_number'); out.dataset.state = 'hint'; return; }
      tries += 1;
      const limit = ans === 0 ? tol : tol * Math.abs(ans);
      const diff = Math.abs(v - ans);
      if (diff <= limit) {
        out.textContent = msg('correct'); out.dataset.state = 'ok'; form.classList.add('is-ok'); input.setAttribute('aria-invalid', 'false');
      } else {
        input.setAttribute('aria-invalid', 'true');
        if (diff <= 3 * limit) out.textContent = msg('check_close');
        else if (Math.abs(v) > 0 && (Math.abs(v / ans) > 900 || Math.abs(ans / v) > 900)) out.textContent = msg('check_magnitude');
        else out.textContent = tries >= 2 ? msg('check_give_up') : msg('check_retry');
        out.dataset.state = 'no';
      }
    });
  });

  const toc = document.querySelector('nav.toc');
  if (toc) {
    const links = [...toc.querySelectorAll('a')];
    const targets = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    let pinned = null;
    const mark = (id) => links.forEach((a) => {
      const on = a.getAttribute('href') === '#' + id;
      a.toggleAttribute('aria-current', on);
      if (on && toc.scrollWidth > toc.clientWidth) a.scrollIntoView({ inline: 'nearest', block: 'nearest' });
    });
    // the active section is the last one whose top has passed 35 % of the viewport; a tap pins its target
    // until the reader scrolls on, so a short last section can still be marked
    const update = () => {
      if (pinned) { mark(pinned); return; }
      const line = window.innerHeight * 0.35;
      let current = targets[0];
      targets.forEach((t) => { if (t.getBoundingClientRect().top <= line) current = t; });
      if (current) mark(current.id);
    };
    links.forEach((a) => a.addEventListener('click', () => { pinned = a.getAttribute('href').slice(1); mark(pinned); setTimeout(() => { pinned = null; }, 900); }));
    let ticking = false;
    window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { ticking = false; update(); }); } }, { passive: true });
    window.addEventListener('resize', update);
    update();
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
    ['#exercises li[id]', (t) => t.querySelector(':scope > .task') && t, (box) => box.querySelector(':scope > form.check, :scope > details.answer')],   // write first, then check (teacher 2026-11-01)
    ['section.practice-task[id]', (t) => t.querySelector(':scope > .task-card'), (box) => box.querySelector(':scope > details.reveal')],
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
