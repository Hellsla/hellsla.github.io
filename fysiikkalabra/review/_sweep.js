const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_CHROMIUM });
  const url = 'file://' + path.resolve('preview/fy3-4.html');
  const out = {};
  for (const W of (process.argv[2]||"360,390,1280").split(",").map(Number)) {
    const pg = await b.newPage({ viewport: { width: W, height: 800 } });
    const errs = []; pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await pg.goto(url); await pg.waitForSelector('#sim-root canvas');
    await pg.evaluate(() => document.querySelector('#sim-root').scrollIntoView());
    await pg.waitForTimeout(500);
    const res = await pg.evaluate(async () => {
      const sl = document.querySelectorAll('#sim-root input[type=range]'), cb = document.querySelector('#sim-root input[type=checkbox]');
      const wait = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
      const set = (el, v) => { el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); };
      const problems = []; let n = 0, minFont = 99, minGap = 99; const usedRd = {};
      const gap = (a, c) => Math.max(a[0] - c[1], c[0] - a[1], a[2] - c[3], c[2] - a[3]);
      for (const over of [false, true]) for (const rho of [700, 1000, 1300]) for (let h = 0; h <= 20; h += 0.5) {
        cb.checked = over; set(sl[1], rho); set(sl[0], h); await wait(); n++;
        const d = window.simDebug, s = window.simState, B = d.boxes, tag = `W${innerWidth} over=${over} rho=${rho} h=${h}`;
        const names = Object.keys(B);
        for (let i = 0; i < names.length; i++) {
          const a = B[names[i]];
          if (a[0] < 0 || a[1] > 600 || a[2] < 0 || a[3] > 400) problems.push(tag + ' outside ' + names[i]);
          for (let j = i + 1; j < names.length; j++) { const g = gap(a, B[names[j]]); if (g < 0) problems.push(tag + ` overlap ${names[i]}/${names[j]}`); }
        }
        for (const [on, o] of Object.entries(d.obstacles)) for (const nm of names) { if (on==='dot'||true) { const g = gap(B[nm], o); if (g < 0) problems.push(tag + ` ${nm} touches ${on}`); else if (nm==='reading'||nm==='p0'||nm==='hTitle') minGap = Math.min(minGap, g);} }
        if (!d.readingPlaced) problems.push(tag + ' reading fallback');
        if (!over && !B.p0) problems.push(tag + ' no p0 label');
        // blue line vs boxes (sampled)
        const [x1,y1,x2,y2] = d.line;
        for (const nm of names) { const a = B[nm]; for (let t = 0; t <= 1; t += 0.002) { const x = x1 + (x2-x1)*t, y = y1+(y2-y1)*t; if (x > a[0] && x < a[1] && y > a[2] && y < a[3]) { problems.push(tag + ` ${nm} on blue line`); break; } } }
        usedRd[d.used.reading] = (usedRd[d.used.reading]||0)+1;
      }
      return { n, problems, minGap, usedRd, k: window.simDebug.k, cw: document.querySelector('#sim-root canvas').getBoundingClientRect().width };
    });
    res.errs = errs; out[W] = res;
    console.log(W, 'states', res.n, 'problems', res.problems.length, 'minGap', res.minGap, 'reading cand use', JSON.stringify(res.usedRd), 'canvasW', res.cw, 'k', res.k, 'errs', errs.length);
    res.problems.slice(0, 15).forEach(p => console.log('  ', p));
    await pg.close();
  }
  await b.close();
})();
