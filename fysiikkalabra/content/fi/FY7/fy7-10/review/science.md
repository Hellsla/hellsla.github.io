VERDICT: FAIL
CONTENT-HASH: 6dd11c845cfa9c6d

## Blocking
- inquiry.json:18 (hook) with lesson.md:128 (Näennäinen syvyys, last sentence) — **B**, causality/consistency. The hook says "katso lasia sivulta … siirtyneen sivuun", and the hero shows a sideways shift. The lesson explains it by refraction at the water *surface*, with the submerged part looking *raised*. That holds only when the glass is viewed obliquely from above through the surface. Straight from the side, the light leaves through the glass wall, and the sideways shift comes from the curved wall (the round glass of water acts as a lens). tarkistus-3 already states the right condition ("sivulta vinosti ylhäältä"). Fix: hook "katso lasia vinosti ylhäältä"; at lesson.md:128 add "kun lasia katsotaan vinosti ylhäältä vedenpinnan läpi".

## Polish
- lesson.md:168 (and the glossary) — "aineessa se on aina suurempi kuin 1": add "näkyvälle valolle läpinäkyvissä aineissa" (C if left).
- lesson.md:122 — "Mitä suurempi on taitekertoimien ero, sitä enemmän säde taittuu": add "samalla tulokulmalla".

## Checked
- Every number recomputed in one script: example 38,02° / 2,256·10⁸ m/s; misconception 22,1°/40,6°; ennuste-1 28,9°; ennuste-2 1,84×; koe-1 angle ratios 1,36/1,48; koe-2 35,2/30,9/30,3/18,5°; virhe 40,6°; siirto 41,68° (25,94° in the glass, mistakes right); tarkistus-2 1,4703 (mistakes right); nopeus 2,013; exit ticket.
- The mittaus least-squares fit reproduces A = 1,4895, B = −0,0041, ΔA = 0,0162. The data match n = 1,49 rounded to 1°.
- Partial reflection 4,3 %/2,0 %. Unpolarised Fresnel R increases monotonically with angle for every sim pair, so "loivemmassa kulmassa suurempi osa" is true.
- Figures to scale: interface 50° → 35,2°; wavefronts λ₁ : λ₂ = 1,33 and continuous; depth rays obey Snell within 0,2°; graph end points 48,8°/24,4°.
- sim.js: β = α₁, Snell, TIR condition, Fresnel rs/rp, T = 1 − R. The simState keys cover every measure. Each experiment's locks isolate its varied parameter. The model box states the limits.
- Every choice item has exactly one correct option and correct distractor feedback. The wavefront causality and the unchanged frequency are right.
- The CRC source and year are named. The scope fits LOPS FY7.
