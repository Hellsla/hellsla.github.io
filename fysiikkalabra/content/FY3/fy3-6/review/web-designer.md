VERDICT: FAIL
CONTENT-HASH: 3243e1e380d9c9a9

## Blocking
- lesson.md:92-97 (misconception, aligned) — row 1 `3,0 kg·(T − 20 °C) = 1,0 kg·(80 °C − T)` is wider than the display box: it scrolls sideways and the right-hand side is cut off at 390 px (scrollWidth 383 vs 356) and 360 px (383 vs 326, 57 px hidden). The key line of the argument cannot be read without a swipe. — Fix: break it as `3{,}0\,\text{kg}\cdot(T-20\,{}^\circ\text{C}) \\ &= 1{,}0\,\text{kg}\cdot(80\,{}^\circ\text{C}-T)` (or drop the kg and say in the text that kg cancels).
- lesson.md:33-36 (Kaava, aligned solving for T) — row 1 `c₁m₁T₁ − c₁m₁T = c₂m₂T − c₂m₂T₂` is cut off at 360 px (345 vs 326, 19 px hidden; fits at 390 and 1280). — Fix: put the right-hand side on its own row (`&= c_2 m_2 T - c_2 m_2 T_2` after a `\\`) and recheck at 360.
- lesson.md:81, 85 (worked example, single-line displays) — scroll sideways at 390 px (449 and 461 vs 356) and 360 px (449, 461 vs 326); the units fractions make them about 100-135 px too wide. Also lesson.md:15 at 360 only (343 vs 326). — Fix: split each into an `aligned` with `&=` at the line start so the right side drops to row 2, or write units inline (`J/(kg·K)`), as the solutions already do.

## Polish
None.

## Checked
- Hash 3243e1e380d9c9a9 at start and end; lint 0 errors, 0 warnings; build ok; 0 console errors at 1280, 390, 360; page overflow 0 at all widths.
- Upota: first control, directly below the canvas, 92x40 px; button bottom is 475 px (1280), 291 px (390x844) and 244 px (360x640) from the canvas top, so canvas + button fit one screen; gap canvas to button 35, 35, 8 px.
- DOM order is canvas, controls, readout, note. All sliders, select and button are 40 px tall; all five labels one line (27 px), no wrapping at any width.
- Scroll-away test at 390 and 360: Upota pressed, scrolled away 3,5 s, simState.t 0,77-0,78 s; 0,6 s after return 1,44-1,49 s, so no jump (step clamp works).
- Full 10 s runs at 1280, 390 and 360 for five settings: cold iron 1 kg into 60 °C water, 0 °C Al in 0,10 kg of 5 °C water, hot Cu 1 kg in 0,10 kg water (T 50,5), tiny hot water body, equal temperatures. End state t = 10, TW = TB = Teq, no clipping or label collisions; the T label moves below the line near the top (checked in screenshots); no string through "kappale".
- Canvas text about 11-13 px at 390 and 360; readout is DOM text, 6 lines at most.
- At 1280 every display fits (606 px box); at narrow widths overflow scrolls inside `.katex-display`, the page itself never overflows.
- Screenshots: review/fy3-6-wd2-*.png (git-ignored).
