// node scripts/ahjo_tab_icons.js assets/shared/brand/ahjo-makerspace-merkki.svg assets/shared/brand
// renders the Ahjo mark to the 32 px favicon and the 180 px touch icon of the Ahjo pages (scripts/ahjo.py tab_icons)
const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const [src, dir] = process.argv.slice(2); const svg = fs.readFileSync(src, 'utf8');
 const b = await chromium.launch();
 for (const [n, full] of [[32, false], [180, true]]) {
  const p = await b.newPage({ viewport: { width: n, height: n } });
  // the touch icon fills its square (the phone rounds the corners itself); the favicon keeps the rounded square
  const s = full ? svg.replace(/<rect [^>]*\/>/, '<rect width="48" height="48" fill="#fffdf8"/>') : svg;
  await p.setContent(`<style>html,body{margin:0;background:transparent}svg{display:block;width:${n}px;height:${n}px}</style>${s}`);
  await p.screenshot({ path: `${dir}/ahjo-${n}.png`, omitBackground: true });
 }
 await b.close(); })();
