const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.PW_CHROMIUM });
  const url = 'file://' + path.resolve('preview/fy3-4.html');
  for (const W of [360, 390, 1280]) {
    const pg = await b.newPage({ viewport: { width: W, height: 800 }, deviceScaleFactor: 2 });
    await pg.goto(url); await pg.waitForSelector('#sim-root canvas'); await pg.evaluate(() => document.querySelector('#sim-root').scrollIntoView()); await pg.addStyleTag({content:'nav,header,.sticky,[class*=nav]{visibility:hidden!important}'}); await pg.waitForTimeout(400);
    const cases = W === 1280 ? [[1000,5,false],[1000,20,false],[1300,18,true],[700,6,false]] : [[1000,5,false],[1300,6,false],[1000,18,false],[1000,20,false],[1300,20,true],[700,18,true],[1300,5,true],[700,6,true]];
    for (const [rho,h,over] of cases) {
      await pg.evaluate(([rho,h,over]) => { const sl = document.querySelectorAll('#sim-root input[type=range]'), cb = document.querySelector('#sim-root input[type=checkbox]');
        const set=(e,v)=>{e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}; cb.checked=over; set(sl[1],rho); set(sl[0],h); }, [rho,h,over]);
      await pg.waitForTimeout(150);
      await pg.locator('#sim-root canvas').screenshot({ path: `review/fy3-4-r3-${W}-h${h}-r${rho}-${over?'over':'full'}.png` });
    }
    await pg.close();
  }
  await b.close();
})();
