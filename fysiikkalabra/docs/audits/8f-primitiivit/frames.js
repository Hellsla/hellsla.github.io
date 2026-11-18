const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const b = await chromium.launch(), pg = await b.newPage({ viewport: { width: 700, height: 260 } });
  await pg.goto('file://' + path.join(__dirname, 'demo.html'));
  fs.mkdirSync(path.join(__dirname, 'frames'), { recursive: true });
  for (let i = 0; i < 20; i++) {
    await pg.evaluate((t) => document.getAnimations().forEach((a) => { a.pause(); a.currentTime = t; }), 5000 * i / 20 + 0.001);
    await pg.locator('svg.fig-anim').screenshot({ path: path.join(__dirname, 'frames', String(i).padStart(2, '0') + '.png') });
  }
  await b.close();
})();
