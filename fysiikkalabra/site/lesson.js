/* Lesson page behaviour. Everything runs in the browser; nothing is stored or sent anywhere.
   1. Answer check: compares the typed number with data-answer within the relative data-tol.
   2. Section nav: marks the section currently on screen.
   3. Worked example in stages: reveals the solution one stage at a time.
   4. Print: opens every collapsed block and every hidden stage while printing.
   5. A link to something inside a closed box (the Ennusta box, a hint) opens the box, so the target shows.
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
