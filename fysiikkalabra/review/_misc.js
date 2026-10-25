const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_CHROMIUM });
  for (const W of [360, 390, 1280]) {
    const pg = await b.newPage({ viewport: { width: W, height: 800 } });
    await pg.goto('file://' + path.resolve('preview/fy3-4.html')); await pg.waitForSelector('#sim-root canvas'); await pg.waitForTimeout(400);
    const r = await pg.evaluate(() => {
      const c = document.querySelector('#sim-root canvas').getBoundingClientRect();
      const ctl = [...document.querySelectorAll('#sim-root label, #sim-root input')].map(e => { const q = e.getBoundingClientRect(); return [e.tagName, Math.round(q.height), q.top >= c.bottom - 0.5]; });
      const par = document.querySelector('main p, article p'); const cs = getComputedStyle(par);
      const cv = document.createElement('canvas').getContext('2d'); cv.font = cs.fontSize + ' ' + cs.fontFamily;
      const ch = cv.measureText('abcdefghijklmnopqrstuvwxyzäö ').width / 29;
      const sr = document.querySelector('#sim-root input[type=range]').getBoundingClientRect();
      return { sw: document.documentElement.scrollWidth, iw: innerWidth, canvasW: Math.round(c.width), ctl, charsPerLine: Math.round(par.getBoundingClientRect().width / ch), fs: cs.fontSize, k: window.simDebug.k, ts11: 11 * (600 / c.width) / (600 / c.width) , sliderH: Math.round(sr.height) };
    });
    console.log(W, JSON.stringify(r));
    await pg.close();
  }
  await b.close();
})();
