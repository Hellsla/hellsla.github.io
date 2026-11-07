/* Oma itsearvio on the module page (teacher 2026-11-07), beside Oma eteneminen: how many of the module's verbal
   self-assessment statements (each chapter's Itsearvio tavoite-1, -2, …; not the tasks' own ratings) the student has
   assessed, and the skills fingerprint: one column per chapter in teaching order, one row per statement, each cell in
   the colour of the chosen level (the Itsearvio scale's colours; grey when not assessed). The statements come from
   #fl-course (build.py self_goals), the levels from this browser (localStorage ruukkilabra:itsearvio:<chapter>, written
   by inquiry.js). Nothing is sent; the levels go to the teacher only in the work file the student returns. */
(() => {
  const box = document.getElementById('oma-itsearvio');
  const C = (() => { try { return JSON.parse(document.getElementById('fl-course').textContent); } catch (e) { return null; } })();
  if (!box || !C || !Array.isArray(C.chapters)) return;
  const chs = C.chapters.filter((c) => Array.isArray(c.goals) && c.goals.length);
  if (!chs.length) return;
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).js || {}; } catch (e) { return {}; } })();
  const FI = { selfmap_count: '{{n}}/{{total}} väitettä arvioitu', selfmap_col: 'Luku {{n}}', selfmap_cell: 'Luku {{ch}}, väite {{k}}: {{text}} ({{level}})', selfmap_none: 'ei arvioitu',
    selfmap_aria: 'Osaamisen sormenjälki', sa_a: 'Osaan tämän niin hyvin, että voisin opettaa sen kaverillenikin', sa_b: 'Koen oivaltaneeni tämän asian',
    sa_c: 'Osaan osittain, mutta epävarmuutta on vielä', sa_d: 'Tarvitsen vielä harjoitusta ja aikaa tämän ymmärtämiseen', sa_x: 'En ole vielä harjoitellut tätä' };
  const S = (k, v) => (typeof L10N[k] === 'string' ? L10N[k] : FI[k] || '').replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m));
  const LEVELS = ['a', 'b', 'c', 'd', 'x'];
  const level = (ch, k) => {
    try { const v = JSON.parse(localStorage.getItem('ruukkilabra:itsearvio:' + ch) || 'null'); const it = v && v.items && v.items['tavoite-' + k];
      return it && LEVELS.includes(it.level) ? it.level : ''; } catch (e) { return ''; }
  };
  const rows = Math.max(...chs.map((c) => c.goals.length));
  // the module's themes above their chapters' columns (curriculum.json "themes", as on the chapter cards)
  const themes = (() => { try { return JSON.parse(box.dataset.themes || '[]'); } catch (e) { return []; } })();
  const spans = [];
  chs.forEach((c) => { const th = themes.find((t) => t.first === c.id); if (th || !spans.length) spans.push({ t: th ? th.t : '', n: 0 }); spans[spans.length - 1].n++; });
  const draw = () => {
    let n = 0, total = 0;
    const grid = document.createElement('div');
    grid.className = 'sm-grid'; grid.setAttribute('role', 'img'); grid.setAttribute('aria-label', S('selfmap_aria'));
    grid.style.setProperty('--cols', chs.length); grid.style.setProperty('--rows', rows);
    if (themes.length) {
      grid.append(Object.assign(document.createElement('span'), { className: 'sm-corner' }));
      spans.forEach((sp) => { const t = document.createElement('span'); t.className = 'sm-theme'; t.textContent = sp.t; t.style.gridColumn = 'span ' + sp.n; grid.append(t); });
    }
    const head = document.createElement('span'); head.className = 'sm-corner'; grid.append(head);
    chs.forEach((c) => { const h = document.createElement('span'); h.className = 'sm-col'; h.textContent = c.n; h.title = S('selfmap_col', { n: c.n }); grid.append(h); });
    for (let k = 1; k <= rows; k++) {
      const r = document.createElement('span'); r.className = 'sm-row'; r.textContent = k; grid.append(r);
      chs.forEach((c) => {
        const cell = document.createElement('span'), text = c.goals[k - 1];
        if (!text) { cell.className = 'sm-cell sm-gap'; grid.append(cell); return; }
        const lv = level(c.id, k); total++; if (lv) n++;
        cell.className = 'sm-cell'; if (lv) cell.dataset.level = lv;
        cell.title = S('selfmap_cell', { ch: c.n, k, text, level: lv ? S('sa_' + lv) : S('selfmap_none') });
        grid.append(cell);
      });
    }
    box.querySelector('.sm-count').textContent = S('selfmap_count', { n, total });
    box.querySelector('.sm-map').replaceChildren(grid);
    const legend = box.querySelector('.sm-legend');
    if (!legend.children.length) LEVELS.forEach((lv) => { const li = document.createElement('li'), sw = document.createElement('span');
      sw.className = 'sm-cell'; sw.dataset.level = lv; li.append(sw, ' ' + S('sa_' + lv)); legend.append(li); });
    box.hidden = false;
    const wrap = box.closest('details'); if (wrap) wrap.hidden = false;
  };
  draw();
  window.addEventListener('storage', (e) => { if (!e.key || e.key.startsWith('ruukkilabra:itsearvio:')) draw(); });
  window.addEventListener('pageshow', (e) => { if (e.persisted) draw(); });
})();
