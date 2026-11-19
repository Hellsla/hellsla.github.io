VERDICT: PASS
CONTENT-HASH: db97051f5614558d

## Blocking

## Polish
- lesson.md:47 — "tämän luvun laskutehtävissä ajanotto alkaa aina niin" is now true (every calculation in the lesson, inquiry and exercises starts at an upward pass through equilibrium; L3-05 starts at a pass with the distance growing, which is the positive direction there). The optional "vaihe" choice is about interpreting $C$, not a calculation, so the round-1 contradiction is gone. If you want, "laskutehtävissä ja esimerkeissä" would also cover the worked example by name; this is optional.
- inquiry.json tarkistus-3 model — $C = 0{,}01$ is called $C \approx 0$. You could say it is about $0{,}2\,\%$ of a cycle ($0{,}01/2\pi$), so a reader sees why it counts as zero. This is optional.

## Checked
- Round-1 item: I read every exercise text that sets a start time (L1-09, L3-01, L3-05) and every inquiry calculation. All start at an upward equilibrium pass; "vaihe" ($C = \pi/2$ at release, ääriasema, a quarter cycle) is right and has exactly one correct option.
- I recomputed all the sim numbers from sim.js's generator. Aineisto 1 with $T = 1{,}60\,\text{s}$: $d$ = 1,849 / 0,126 / 3,705 cm for $A$ = 3, 6, 12 cm. Koe 2: $N$ = 6 and 3, $f$ = 1,25 and 0,625 Hz. Koe 3 best fit on the slider grid: $A = 8{,}5\,\text{cm}$, $T = 2{,}20\,\text{s}$, $d = 0{,}127\,\text{cm}$, falling sharply at 2,20 s. Max noise is 0,2500 cm, as stated.
- The setups isolate the varied parameter: koe-1 locks $T$, koe-2 locks $A$, koe-3 leaves both free on purpose. `simState` gives d, N, f and A.
- Worked example: $T = 0{,}60\,\text{s}$, argument 2,618 rad, $x = 2{,}0\,\text{cm}$; the degree-mode value 0,183 cm is right; the T/4 and T/2 check is a real check.
- siirto: 3,804 cm. The mistakes are right: degree mode 0,0877; $f$ used as $T$ gives −3,80; $2A$ = 8,0.
- Etsi virhe: 1,11 vs 2,22 Hz. tarkistus-1: 0,80 m and 3,0 s, one correct option. tarkistus-2: 0,556 Hz; the distractors 1,8, 1,11 and 0,185 are right; a 0,8 m pendulum gives 1,79 s ✓.
- tarkistus-3: $T = 0{,}800\,\text{s}$, $f = 1{,}25\,\text{Hz}$, range 0,378–0,482 m. "Poispäin tunnistimesta" fits $C \approx 0$ with $A > 0$.
- Figures from figures.py: kuvaaja ($A = 4$, $T = 0{,}80$, peaks 0,2 and 1,0 s, upward passes 0,8 and 1,6 s); sovitus (3T = 3,6 s, A = 3 cm); task graph $T = 1{,}8\,\text{s}$ crossing every 0,9 s. All consistent with their texts.
- Conditions are stated: no damping; sine only for spring and small-swing pendulum; radians; "yleensä" in the fit sentence; sim values are called model values.
- Definitions (jaksonaika: same place and same direction; amplitudi; vaihe; hertsi) match the glossary. The circle derivation and the karusellin lapsi example are correct. The scope is FY5, with no ω.
- Exit ticket, summary and kertaus agree with the theory.
