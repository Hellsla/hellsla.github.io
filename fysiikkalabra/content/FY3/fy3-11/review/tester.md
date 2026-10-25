VERDICT: PASS
CONTENT-HASH: a1174ac0ea0906c7

## Blocking
None.

## Polish
- tests/sims/fy3-11.json — no assertion ties the drawn arrow widths or colours to simState; they agree (see Checked), but a regression would go unnoticed. Add, e.g., a pixel test: `{"expr":"(()=>{const c=document.querySelector('#sim-root canvas'),f=c.width/600,d=c.getContext('2d').getImageData(Math.round(146*f),0,1,c.height).data;let a=-1,b=-1;for(let y=0;y<c.height;y++){const i=y*4;if(Math.abs(d[i]-200)<25&&Math.abs(d[i+1]-60)<25&&Math.abs(d[i+2]-35)<25){if(a<0)a=y;b=y}}return (b-a+1)/f/window.simState.bandTotal})()","expected":1,"tol":0.02,"note":"fuel arrow is bandTotal px tall"}`.
- sim.js:~49 — the note under the canvas ("Yhteistuotannossa sähkön ja kaukolämmön osuus ... 95 %") is shown in every mode, including the heat pump; show it only when mode is yhteistuotanto.
- sim.js:12 — waste heat blue [110,160,205] and outdoor-air blue [80,170,230] are close; fine because they never share a diagram, but the fuel red [200,60,35] and "heat inside" red [220,75,50] are also near-identical. Optional: make heat-inside a warmer orange-red.
- Coverage of the 79 assertions is otherwise good (every slider, every simState field, ranges, visibility, CHP cap both ways, readout text, 3 overlap sweeps). Overlap sweeps cover only 3 slider corners; my full sweep (below) found no problem.

## Checked
- `PASS preview/fy3-11  [] []` (test_sims.py fy3-11, 79 assertions, no console or page errors); lint: 0 errors, 0 warnings.
- Energy conservation: swept 4 modes x 3 values (min, mid, max) of every visible slider = 54 combinations at 360, 390 and 1280 px: Puse+Pheat+Pwaste = Pin, Pel+Pambient = Pout = cop·Pel, sumIn = sumOut, Pwaste >= 0, etaTotal = (Puse+Pheat)/Pin, no NaN, no decimal point in readout. 0 flagged.
- CHP cap via real input events: 60 % + 65 % gives 30 % + 65 % (eta yields as the slider moved last) and etaTotal 95, Pwaste 50 MW; then eta 50 gives heat 45 (heat yields); etaTotal never above 95 anywhere in the sweep.
- Colours and widths vs simState: sampled canvas pixels in 11 slider settings (all modes, extremes): every arrow's height equals P·simState.scale within 1-2 px (outline); colours match the legend (fuel red, el yellow, district heat orange, waste/outdoor blue, heat inside red); fuel/Pout always fill bandTotal = 210 px; the zero district-heat flow is a dashed line.
- No canvas text box overlaps another or leaves the 600x400 canvas in any of the 54 combinations at 360 (k=2,04), 390 (k=1,85) and 1280 px (k=1).
- Controls: 1 select + 4 sliders only (power, eta, district heat share, cop), no buttons; matches sim-spec, none added. Ranges and presets match the spec; DOM order canvas, controls, readout.
- Formulas: sim.js η = Puse/Pin, Pwaste = Pin − Puse − Pheat, cop = Pout/Pel agree with lesson.md (W = Q₁ − Q₂, η = W/Q₁, lämpökerroin as heat/electric power); CHP cap 95 % is consistent with the lesson's 85–90 %.
- Visual detail (human rule): boiler flames, turbine, generator, condenser, pistons, flywheel, outdoor fan unit, house wall, moving chevrons; screenshots at 360 and 1280 px look correct, no horizontal overflow (scrollWidth = innerWidth).
- Hash a1174ac0ea0906c7 identical before and after the review.
