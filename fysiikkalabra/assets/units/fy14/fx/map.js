/* Global Fusion Explorer (data-fx="map"): fusion research facilities on a world map (Leaflet 1.9.4 from vendor/,
   OpenStreetMap tiles loaded by the student's browser, © OpenStreetMap contributors). The facts live in the data file
   named by the element's data-src (units/fy14/data/facilities.json), apart from this presentation code.
   - One marker per site; a site with several devices (Culham, Princeton, Naka, Cadarache …) lists them all.
   - Filters: search (name, country then and now, site), country, device type, status and a year ("operating in …" or any year);
     the list under the map shows exactly the facilities the filters leave, as buttons, so the whole explorer works
     with a keyboard and a screen reader without touching the map.
   - Selecting a facility (marker, list or #f-<id> in the address, as the timeline links) shows its panel: type,
     status, place, years, achievements, why it matters, sources and the date they were checked.
   - "Operating in" a year: start ≤ year ≤ end. A retired machine with end null (no source gives its end year) counts
     only up to its last_seen year (the latest year a source shows it running) or else start + 10, never to today.
   - Without scripts or tiles the list still works; the map is an extra, never the only way to the facts.
   Data on the element: {map_height?: px, year?: default year filter, intro?: text}. */
window.FX.map = (el, d, A) => {
  const { h, md, base } = A;
  const src = el.getAttribute('data-src');
  const COL = { tokamak: '#c2410c', 'spherical-tokamak': '#a16207', stellarator: '#1d4ed8', pinch: '#7e22ce', inertial: '#be123c', other: '#0f766e' };
  const SHAPE = { operating: '●', construction: '◐', planned: '○', retired: '◆' };
  const root = h('div', { class: 'fx-map' });
  el.append(root);
  const css = h('link', { rel: 'stylesheet', href: base + 'vendor/leaflet/leaflet.css' }); document.head.append(css);
  const loadLeaflet = () => (window.L ? Promise.resolve() : new Promise((res, rej) => { const s = h('script', { src: base + 'vendor/leaflet/leaflet.js' }); s.onload = res; s.onerror = rej; document.head.append(s); }));
  Promise.all([A.data(src), loadLeaflet().catch(() => null)]).then(([data]) => build(data)).catch((e) => {
    root.append(h('p', { class: 'fx-note' }, 'The facility data could not be loaded (' + e + '). Open the page from the web site, not from a file.'));
  });

  function build(data) {
    const F = data.facilities.filter((f) => f.lat != null && f.lon != null);
    const cats = data.categories, stats = data.statuses;
    const countries = [...new Set(F.map((f) => f.country))].sort();
    const starts = F.map((f) => f.start).filter(Boolean);
    const y0 = Math.min(...starts), y1 = new Date().getFullYear();
    const sel = (id, label, opts) => h('div', { class: 'fx-field' }, h('label', { for: id }, label),
      h('select', { id }, h('option', { value: '' }, 'All'), ...opts.map(([v, t]) => h('option', { value: v }, t))));
    const idp = el.id + '-';
    const q = h('input', { id: idp + 'q', type: 'search', autocomplete: 'off', placeholder: 'e.g. JET, Japan, Culham' });
    const yr = h('input', { id: idp + 'year', type: 'range', min: y0, max: y1, step: 1, value: y1 });
    const anyYear = h('input', { id: idp + 'any', type: 'checkbox', checked: d.year == null });
    const yrOut = h('output', { for: idp + 'year', class: 'fx-year-out' });
    const form = h('form', { class: 'fx-map-filters', role: 'search', 'aria-label': 'Filter the facilities', onsubmit: (e) => e.preventDefault() },
      h('div', { class: 'fx-field fx-field-wide' }, h('label', { for: idp + 'q' }, 'Search'), q),
      sel(idp + 'country', 'Country', countries.map((c) => [c, c])),
      sel(idp + 'cat', 'Device type', Object.entries(cats)),
      sel(idp + 'status', 'Status', Object.entries(stats)),
      h('div', { class: 'fx-field fx-field-wide fx-year' }, h('label', { for: idp + 'year' }, 'Operating in the year'), h('div', { class: 'fx-year-row' }, yr, yrOut),
        h('label', { class: 'fx-check' }, anyYear, ' any year (show every facility)')),
      h('button', { type: 'reset', class: 'fx-btn fx-quiet' }, 'Clear filters'));
    if (d.year != null) yr.value = d.year;
    const count = h('p', { class: 'fx-msg', 'aria-live': 'polite' });
    const mapBox = h('div', { class: 'fx-map-canvas', style: `height:${d.map_height || 460}px`, role: 'region', 'aria-label': 'World map of fusion facilities (the list below has the same facilities)' });
    const panel = h('div', { class: 'fx-map-panel', id: idp + 'panel', tabindex: '-1', 'aria-live': 'polite' },
      h('p', { class: 'fx-note' }, 'Select a marker or a facility in the list to see its story.'));
    const legend = h('ul', { class: 'fx-legend', 'aria-label': 'Legend' },
      ...Object.entries(cats).map(([k, t]) => h('li', {}, h('span', { class: 'fx-swatch', style: `background:${COL[k] || '#555'}` }), t)),
      ...Object.entries(stats).map(([k, t]) => h('li', {}, h('span', { class: 'fx-sym', 'aria-hidden': 'true' }, SHAPE[k] || '●'), t)));
    const list = h('ul', { class: 'fx-map-list' });
    root.append(...(d.intro ? [h('p', { class: 'fx-prompt', html: md(d.intro) })] : []), form, count, h('div', { class: 'fx-map-main' }, mapBox, panel), legend,
      h('h4', { class: 'fx-map-list-h' }, 'Facilities shown'), list,
      h('p', { class: 'fx-note' }, `Data checked ${A.date(data.checked)}. Not an exhaustive list of fusion experiments. Map tiles © OpenStreetMap contributors.`));

    let map = null; const markers = {};
    if (window.L) {
      map = window.L.map(mapBox, { worldCopyJump: true, scrollWheelZoom: false, minZoom: 1 }).setView([35, 20], 2);
      window.L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 12, attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);
      mapBox.addEventListener('focus', () => map.scrollWheelZoom.enable()); mapBox.addEventListener('blur', () => map.scrollWheelZoom.disable());
    } else mapBox.replaceChildren(h('p', { class: 'fx-note' }, 'The map could not be loaded. Use the list below.'));

    const where = (f) => (f.country_then ? `${f.country_then} (today ${f.country})` : f.country);
    const site = (f) => f.lat.toFixed(2) + ',' + f.lon.toFixed(2);
    const years = (f) => (f.start ? f.start : '?') + '–' + (f.end ? f.end : f.status === 'operating' ? 'today' : f.status === 'retired' ? '?' : '');
    const UNKNOWN_SPAN = 10; // a retired machine whose end year no source gives: counted only to last_seen or start + 10
    const live = (f, y) => f.start != null && f.start <= y && (f.end != null ? f.end >= y
      : f.status === 'retired' ? y <= (f.last_seen || f.start + UNKNOWN_SPAN) : f.status !== 'planned' && f.status !== 'construction');
    const show = (f, focusPanel) => {
      panel.replaceChildren(
        h('p', { class: 'fx-map-kicker' }, h('span', { class: 'fx-swatch', style: `background:${COL[f.category] || '#555'}` }), `${cats[f.category] || f.category} · ${stats[f.status] || f.status}`),
        h('h4', {}, !f.full_name || f.full_name === f.name ? f.name : f.full_name.toLowerCase().startsWith(f.name.toLowerCase()) ? f.full_name : f.name + ' — ' + f.full_name),
        h('p', { class: 'fx-map-where' }, `${f.site}, ${where(f)} · ${years(f)}` + (f.operator ? ' · ' + f.operator : '')),
        ...(f.photo ? [h('figure', { class: 'fx-map-photo' }, h('img', { src: f.photo.src, alt: f.photo.alt || '', loading: 'lazy' }), h('figcaption', { html: md(f.photo.credit || '') }))] : []),
        h('p', { html: md(f.importance) }),
        ...(f.achievements && f.achievements.length ? [h('ul', {}, f.achievements.map((a) => h('li', { html: md(a) })))] : []),
        ...(f.note ? [h('p', { class: 'fx-note', html: md(f.note) })] : []),
        h('p', { class: 'fx-map-src' }, 'Sources: ', ...f.sources.flatMap((s, i) => [i ? ', ' : '', h('a', { href: s.url }, s.title)])));
      list.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.id === f.id)));
      if (map) { map.setView([f.lat, f.lon], Math.max(map.getZoom(), 5)); const m = markers[site(f)]; if (m) m.openTooltip(); }
      if (focusPanel) panel.focus({ preventScroll: false });
      try { history.replaceState(null, '', '#f-' + f.id); } catch (e) { /* file: pages */ }
    };
    const draw = () => {
      const s = q.value.trim().toLowerCase(), c = form.querySelector('#' + idp + 'country').value, k = form.querySelector('#' + idp + 'cat').value, st = form.querySelector('#' + idp + 'status').value;
      const y = Number(yr.value); yrOut.textContent = anyYear.checked ? 'any' : String(y); yr.disabled = anyYear.checked;
      const shown = F.filter((f) => (!s || [f.name, f.full_name, f.country, f.country_then, f.site, f.operator].join(' ').toLowerCase().includes(s))
        && (!c || f.country === c) && (!k || f.category === k) && (!st || f.status === st) && (anyYear.checked || live(f, y)));
      count.textContent = `${shown.length} of ${F.length} facilities shown` + (anyYear.checked ? '.' : ` (operating in ${y}).`);
      list.replaceChildren(...shown.sort((a, b) => (a.start || 9999) - (b.start || 9999)).map((f) => h('li', {}, h('button', { type: 'button', 'data-id': f.id, 'aria-pressed': 'false', onclick: () => show(f, true) },
        h('span', { class: 'fx-swatch', style: `background:${COL[f.category] || '#555'}` }), h('strong', {}, f.name), ` ${where(f)}, ${years(f)} · ${cats[f.category] || f.category} · ${stats[f.status] || f.status}`))));
      if (!map) return;
      Object.values(markers).forEach((m) => m.remove());
      const groups = {}; shown.forEach((f) => (groups[site(f)] = groups[site(f)] || []).push(f));
      Object.entries(groups).forEach(([key, fs]) => {
        const f0 = fs[0], col = COL[f0.category] || '#555';
        const icon = window.L.divIcon({ className: 'fx-pin', html: `<span style="background:${col}">${fs.length > 1 ? fs.length : SHAPE[f0.status] || ''}</span>`, iconSize: [28, 28], iconAnchor: [14, 14] });
        const m = window.L.marker([f0.lat, f0.lon], { icon, keyboard: true, title: fs.map((f) => f.name).join(', '), alt: fs.map((f) => f.name).join(', ') }).addTo(map);
        m.bindTooltip(fs.map((f) => f.name).join(', '));
        if (fs.length === 1) m.on('click', () => show(f0, false));
        else {
          const box = h('div', { class: 'fx-pop' }, h('p', {}, h('strong', {}, f0.site)), h('ul', {}, fs.map((f) => h('li', {}, h('button', { type: 'button', class: 'fx-linkbtn', onclick: () => { map.closePopup(); show(f, false); } }, `${f.name} (${years(f)})`)))));
          m.bindPopup(box);
        }
        markers[key] = m;
      });
    };
    form.addEventListener('input', draw);   // 'change' only for controls without 'input': a search box's change on blur would
    form.addEventListener('change', (e) => { if (e.target.type !== 'search' && e.target.type !== 'text') draw(); });   // rebuild the list under a tap
    form.addEventListener('reset', () => setTimeout(() => { anyYear.checked = true; draw(); }, 0));
    draw();
    const want = (location.hash.match(/^#f-([\w-]+)$/) || [])[1];
    const f = want && F.find((x) => x.id === want);
    if (f) { anyYear.checked = true; draw(); show(f, false); requestAnimationFrame(() => panel.scrollIntoView({ block: 'start' })); }
    if (map) setTimeout(() => map.invalidateSize(), 200);
  }
};
