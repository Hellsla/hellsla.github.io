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


  // One source of truth for objectives and sequential lesson links.
  // Unreviewed lessons cannot appear in the published site's catalogue.
  const filename = window.location.pathname.split('/').pop();
  if (/^fy[1-8]-\d+\.html$/i.test(filename)) {
    const id = filename.replace(/\.html$/i, '');
    fetch('catalogue.json').then((r) => {
      if (!r.ok) throw Error('Catalogue unavailable');
      return r.json();
    }).then((entries) => {
      const current = entries.find((e) => e.id === id && e.published);
      if (!current) return;
      const article = document.getElementById('teoria');
      const h1 = article?.querySelector('h1');
      if (h1 && current.goals?.length) {
        const aside = document.createElement('aside');
        const header = document.createElement('strong');
        aside.className = 'lesson-goals';
        aside.setAttribute('aria-label', 'Oppimistavoitteet');
        header.textContent = 'Oppimistavoitteet';
        const list = document.createElement('ul');
        for (const goal of current.goals) {
          const li = document.createElement('li');
          li.textContent = goal.replace(/^(?:LOPS \w+:|Täsmennys:|Taidot:|Temaattinen tarkastelu:)\s*/, '');
          list.appendChild(li);
        }
        aside.append(header, list);
        h1.after(aside);
      }
      const peers = entries.filter((e) => e.course === current.course && e.published);
      const at = peers.findIndex((e) => e.id === id);
      const nav = document.createElement('nav');
      nav.className = 'lesson-pagination';
      nav.setAttribute('aria-label', 'Oppituntien selaus');
      const add = (entry, title, cls) => {
        const a = document.createElement('a');
        const small = document.createElement('span');
        const strong = document.createElement('strong');
        a.href = entry.id + '.html'; a.className = cls;
        small.textContent = title; strong.textContent = entry.title;
        a.append(small, strong); nav.appendChild(a);
      };
      if (at > 0) add(peers[at - 1], '← Edellinen oppitunti', 'previous');
      if (at >= 0 && at < peers.length - 1) add(peers[at + 1], 'Seuraava oppitunti →', 'next');
      if (nav.childElementCount) document.querySelector('main.reading')?.appendChild(nav);
    }).catch(() => {}); // Existing course links work without this enhancement.
  }

  let opened = [];
  window.addEventListener('beforeprint', () => {
    opened = [...document.querySelectorAll('details:not([open])')];
    opened.forEach((d) => { d.open = true; });
  });
  window.addEventListener('afterprint', () => { opened.forEach((d) => { d.open = false; }); opened = []; });
})();
