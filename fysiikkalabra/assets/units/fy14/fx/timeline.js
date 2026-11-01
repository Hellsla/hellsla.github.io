/* The course timeline (data-fx="timeline"): events from the data file named by the element's data-src
   (units/fy14/data/timeline.json), apart from this code. Above the list a year strip (an SVG axis from the first to
   the last year shown) with one tick per event, coloured and shaped by theme (the legend names them in words); a tick
   is a link to its event card. Filters: era (buttons), theme, a search over titles, text, people and places. Each
   card shows the year and place, the text, the people (a short biography behind a disclosure), the sources and,
   when the event is about a device on the course map, "Show on the map" (the map unit's page with #f-<id>).
   Data on the element: {eras?: [era ids shown, default all], themes?: [theme ids], map?: "<map page>.html",
   intro?: text, start_era?: era id selected first}. */
window.FX.timeline = (el, d, A) => {
  const { h, md } = A;
  const src = el.getAttribute('data-src');
  const TH = { science: ['#1d4ed8', 'circle'], device: ['#c2410c', 'square'], politics: ['#7e22ce', 'diamond'], people: ['#0f766e', 'triangle'] };
  const root = h('div', { class: 'fx-tl' }); el.append(root);
  A.data(src).then(build).catch((e) => root.append(h('p', { class: 'fx-note' }, 'The timeline data could not be loaded (' + e + ').')));

  const yr = (x) => String(x == null ? '' : x).slice(0, 4);   // a biography's ISO date shown as its year
  function build(data) {
    const eras = data.eras.filter((e) => !d.eras || d.eras.includes(e.id));
    const all = data.events.filter((e) => eras.some((x) => x.id === e.era) && (!d.themes || d.themes.includes(e.theme))).sort((a, b) => a.year - b.year || String(a.date).localeCompare(String(b.date)));
    let era = d.start_era || '', theme = '', text = '';
    const idp = el.id + '-';
    const eraBar = h('div', { class: 'fx-steps', role: 'group', 'aria-label': 'Era' },
      [['', 'All eras']].concat(eras.map((e) => [e.id, `${e.title} (${e.from}–${e.to})`])).map(([id, t]) => {
        const b = h('button', { type: 'button', class: 'fx-step', 'aria-pressed': String(id === era) }, t);
        b.addEventListener('click', () => { era = id; eraBar.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b))); draw(); });
        return b;
      }));
    const themeSel = h('select', { id: idp + 'theme' }, h('option', { value: '' }, 'All themes'), ...Object.entries(data.themes).filter(([k]) => !d.themes || d.themes.includes(k)).map(([k, t]) => h('option', { value: k }, t)));
    const q = h('input', { id: idp + 'q', type: 'search', autocomplete: 'off', placeholder: 'a name, a place, a word' });
    themeSel.addEventListener('change', () => { theme = themeSel.value; draw(); });
    q.addEventListener('input', () => { text = q.value.trim().toLowerCase(); draw(); });
    const strip = h('div', { class: 'fx-tl-strip' });
    const count = h('p', { class: 'fx-msg', 'aria-live': 'polite' });
    const list = h('ol', { class: 'fx-tl-list' });
    const legend = h('ul', { class: 'fx-legend', 'aria-label': 'Themes' }, Object.entries(data.themes).filter(([k]) => TH[k]).map(([k, t]) => h('li', {}, h('span', { class: 'fx-sym', 'aria-hidden': 'true', style: `color:${TH[k][0]}` }, { circle: '●', square: '■', diamond: '◆', triangle: '▲' }[TH[k][1]]), t)));
    root.append(...(d.intro ? [h('p', { class: 'fx-prompt', html: md(d.intro) })] : []), eraBar,
      h('div', { class: 'fx-tl-filters' }, h('div', { class: 'fx-field' }, h('label', { for: idp + 'theme' }, 'Theme'), themeSel), h('div', { class: 'fx-field fx-field-wide' }, h('label', { for: idp + 'q' }, 'Search'), q)),
      strip, legend, count, list, h('p', { class: 'fx-note' }, `Events checked ${A.date(data.checked)}. Sources are listed with every event.`));

    const mark = (shape, x, y, c) => {
      const s = 6;
      if (shape === 'square') return `<rect x="${x - s}" y="${y - s}" width="${2 * s}" height="${2 * s}" fill="${c}"/>`;
      if (shape === 'diamond') return `<path d="M${x},${y - s - 1} L${x + s + 1},${y} L${x},${y + s + 1} L${x - s - 1},${y} Z" fill="${c}"/>`;
      if (shape === 'triangle') return `<path d="M${x},${y - s - 1} L${x + s + 1},${y + s} L${x - s - 1},${y + s} Z" fill="${c}"/>`;
      return `<circle cx="${x}" cy="${y}" r="${s}" fill="${c}"/>`;
    };
    function draw() {
      const shown = all.filter((e) => (!era || e.era === era) && (!theme || e.theme === theme)
        && (!text || [e.title, e.text, (e.people || []).join(' '), e.place, e.country].join(' ').toLowerCase().includes(text)));
      count.textContent = `${shown.length} event${shown.length === 1 ? '' : 's'} shown.`;
      // the strip: the years of the selected era (or all), ticks stacked when they share a year
      const er = eras.find((x) => x.id === era), a = er ? er.from : Math.min(...all.map((e) => e.year)), b = er ? er.to : Math.max(...all.map((e) => e.year));
      // the strip is drawn at its real width (1 unit = 1 px), so labels keep their size on a phone; fewer year labels there
      const W = Math.max(300, Math.min(1000, Math.round(strip.clientWidth || 1000) - 16)), X = (y) => 30 + (W - 60) * (y - a) / Math.max(1, b - a), seen = {};
      const step = [5, 10, 20, 25, 50].find((st) => (W - 60) * st / Math.max(1, b - a) >= 56) || 50;   // labels at least 56 px apart
      const level = shown.map((e) => { const k = Math.round(X(e.year) / 10); seen[k] = (seen[k] || 0) + 1; return seen[k]; });
      const H = 60 + 15 * Math.max(2, ...level), base = H - 30;   // as tall as the highest stack of marks
      let svg = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Year strip from ${a} to ${b}: one mark per event shown; the list below has the same events."><line x1="20" y1="${base}" x2="${W - 20}" y2="${base}" stroke="#6b7480" stroke-width="2"/>`;
      for (let y = Math.ceil(a / step) * step; y <= b; y += step) svg += `<line x1="${X(y)}" y1="${base - 4}" x2="${X(y)}" y2="${base + 6}" stroke="#6b7480" stroke-width="2"/><text x="${X(y)}" y="${base + 24}" font-size="15" text-anchor="middle" fill="#474c5b">${y}</text>`;
      shown.forEach((e, i) => {
        const [c, sh] = TH[e.theme] || ['#555', 'circle'];
        svg += `<a href="#${idp}ev-${e.id}" aria-label="${e.year}: ${e.title.replace(/"/g, '&quot;')}">${mark(sh, X(e.year), base - 8 - 15 * (level[i] - 1), c)}<title>${e.year}: ${e.title.replace(/</g, '&lt;')}</title></a>`;
      });
      strip.innerHTML = svg + '</svg>';
      list.replaceChildren(...shown.map((e) => {
        const [c] = TH[e.theme] || ['#555'];
        const bio = e.biography ? h('details', { class: 'fx-tl-bio' }, h('summary', {}, `Who was ${e.biography.name}?`),
          h('p', {}, h('strong', {}, `${e.biography.name} (${yr(e.biography.born)}–${e.biography.died ? yr(e.biography.died) : ''})`)), h('p', { html: md(e.biography.text) })) : null;
        const mapLink = e.facility && d.map ? h('a', { class: 'fx-link', href: `${d.map}#f-${e.facility}` }, 'Show on the map →') : null;
        return h('li', { class: 'fx-tl-card', id: idp + 'ev-' + e.id, style: `border-left-color:${c}`, tabindex: '-1' },
          h('p', { class: 'fx-tl-year' }, h('span', { class: 'fx-tl-y' }, e.date ? new Date(e.date + 'T12:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : String(e.year)),
            ' · ' + [e.place, e.country].filter(Boolean).join(', ') + ' · ' + (data.themes[e.theme] || e.theme)),
          h('h4', {}, e.title), h('p', { html: md(e.text) }),
          ...(e.people && e.people.length ? [h('p', { class: 'fx-tl-people' }, 'People: ' + e.people.join(', '))] : []),
          ...(bio ? [bio] : []),
          h('p', { class: 'fx-tl-src' }, 'Sources: ', ...e.sources.flatMap((s, i) => [i ? ', ' : '', h('a', { href: s.url }, s.title)]), ...(mapLink ? [' · ', mapLink] : [])));
      }));
      A.typeset(list);
    }
    draw();
    let lastW = strip.clientWidth;
    if ('ResizeObserver' in window) new ResizeObserver(() => { if (Math.abs(strip.clientWidth - lastW) > 20) { lastW = strip.clientWidth; draw(); } }).observe(strip);
    strip.addEventListener('click', (ev) => { const a = ev.target.closest('a'); if (!a) return; ev.preventDefault(); const t = document.getElementById(a.getAttribute('href').slice(1)); if (t) { t.scrollIntoView({ block: 'center' }); t.focus({ preventScroll: true }); } });
  }
};
