VERDICT: DONE

Round 1 fix.
- lesson.md: measurement error symbol is now $e$ (Δx stays the half-range estimate); summary adds the "two figures if first digit is 1" exception.
- solutions.md: L1-02 uses $e$ and calls 3 mm on 20 cm large for a tape (systematic cause); L1-03 notes 0,35 s exact, 0,4 s as stated estimate; L3-02 "250-osaan".
- inquiry.json: exp-2 solution uses $e$; sim `model` explains δ_sat vs half-range; exp-1 key says half-range settles at about 0,25 s (n = 1 gives 0 with one reading); column label "ero oikeaan (s)"; second `prior` item removed (comprehensive-school knowledge, mean is in the lesson).
- exercises.json: L3-01 adds "viiveet ovat joka kerralla samat".
- sim.js: dots drawn at exact reading x (bins kept for stacking only).
- Not fixable here: sticky-sim legend crop (.lab-side in templates/site.css, max-height + overflow scroll) and sideways table scroll (shared components).
