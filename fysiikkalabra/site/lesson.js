/* Lesson page behaviour. Everything runs in the browser; nothing is stored or sent anywhere.
   1. Answer check: compares the typed number with data-answer within the relative data-tol.
   2. Section nav: marks the section currently on screen.
   3. Print: opens every collapsed block while printing. */
(() => {
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
      if (Number.isNaN(v)) { out.textContent = 'Kirjoita luku, esimerkiksi 9,81.'; out.dataset.state = 'hint'; return; }
      tries += 1;
      const limit = ans === 0 ? tol : tol * Math.abs(ans);
      const diff = Math.abs(v - ans);
      if (diff <= limit) {
        out.textContent = 'Oikein.'; out.dataset.state = 'ok'; form.classList.add('is-ok'); input.setAttribute('aria-invalid', 'false');
      } else {
        input.setAttribute('aria-invalid', 'true');
        if (diff <= 3 * limit) out.textContent = 'Lähellä. Tarkista pyöristys ja yksikkö.';
        else if (Math.abs(v) > 0 && (Math.abs(v / ans) > 900 || Math.abs(ans / v) > 900)) out.textContent = 'Suuruusluokka on väärä. Tarkista yksikkö.';
        else out.textContent = tries >= 2 ? 'Ei vielä. Vastaus ja ratkaisu löytyvät alta.' : 'Ei aivan. Yritä uudelleen.';
        out.dataset.state = 'no';
      }
    });
  });

  const toc = document.querySelector('nav.toc');
  if (toc && 'IntersectionObserver' in window) {
    const links = [...toc.querySelectorAll('a')];
    const targets = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const mark = (id) => links.forEach((a) => a.toggleAttribute('aria-current', a.getAttribute('href') === '#' + id));
    const io = new IntersectionObserver((entries) => {
      entries.filter((en) => en.isIntersecting).forEach((en) => mark(en.target.id));
    }, { rootMargin: '-40% 0px -55% 0px' });
    targets.forEach((t) => io.observe(t));
  }

  let opened = [];
  window.addEventListener('beforeprint', () => {
    opened = [...document.querySelectorAll('details:not([open])')];
    opened.forEach((d) => { d.open = true; });
  });
  window.addEventListener('afterprint', () => { opened.forEach((d) => { d.open = false; }); opened = []; });
})();
