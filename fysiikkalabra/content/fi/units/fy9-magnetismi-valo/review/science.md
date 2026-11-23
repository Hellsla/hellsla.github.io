VERDICT: PASS
CONTENT-HASH: e8fc07600488a929
SCOPE: full: the unit (unit.md, inquiry.json, exit ticket, teacher.md) with its Sovella task set; the three new ```pysahdy boxes judged first.

## Blocking
None.

## Polish
- teacher.md "Arviointi" and the 65–75 min row are out of date. They say "muut viisi" tasks, a total of $95$ points, and "Kaikki aineistot ovat keksittyjä esimerkkejä". The set now has 9 tasks and $137$ points (`practice.py check`). s7 uses real CERN data (`source: statistics`). This is teacher-facing text, not physics, and it was not changed in this round, but it should be corrected.
- unit.md, Induktio ja vaihtovirta: "Kentässä liikkuvan tangon jännite on $e = vBl$" does not say it holds when $v$, $\overline{B}$ and the rod are mutually perpendicular. Every other formula in that section states its condition. This is a one-line reminder that passed earlier, so it is not blocking.
- Box 3 (taittuminen): its answer repeats the sentence just above it word for word ("taitekulma on tulokulmaa suurempi"). The physics is right; whether the box is placed well is for the pedagogy reviewer.

## Checked
- `units.py hash` gave e8fc07600488a929 at the start and at the end. `practice.py check` passes in fi, en and fi-easy (9 tasks, 137 points, criteria points = part points).
- **Pysähdy boxes:**
  - Box 1: induced voltage needs a changing flux; with constant flux there is none. This is correct and matches lt-2, the Virheet list and s9 c.
  - Box 2: the magnetic force is always perpendicular to $\overline{v}$, so it changes only the direction. This is correct with no hidden condition, and it matches the Kaava text, the johda box and lt-1.
  - Box 3: from $n_1 > n_2$, the ray bends away from the normal. This is correct and matches the rajakulma figure and lt-5.
- **Other changes since f56ae412:**
  - The hero, ympyra and rajakulma drawings became webp images (carried as `teacher-figure`), and two labels moved slightly. The ympyra $\overline{F}_\text{M}$ still points to the centre and $\overline{B}$ still points into the page.
  - The inquiry change and the solutions.md changes only split paragraphs (`md-paragraphs`); I diffed them word by word.
- **Recomputed with my own formulas in one script, side by side with answers.py; all agree:**
  - hook: $174\,\text{A}$, $15{,}1\,\text{kW}$ ($37{,}8\,\%$); $2{,}0\,\text{A}$, $2{,}0\,\text{W}$
  - Tutki: $18{,}69\,\text{mW}$, $34{,}6\,\text{mW}$, $0{,}452\,\text{s}$, $0{,}15\,\text{mJ}$
  - siipi: $0{,}391\,\text{V}$; Sirius: $9925\,\text{K}$ (mistake value $9652 = 9925 - 273$)
  - ikkuna: $48{,}75^\circ$, $3{,}42\,\text{m}$; öljy: $1740$, $580$, $348\,\text{nm}$
  - virhe-siirto: $455\,\text{A}$, $826\,\text{kW}$, $1{,}65\,\%$, $3{,}0\,\text{GW}$; lt-5: $41{,}1^\circ$, $1{,}164$; muuntaja: $0{,}24\,\text{A}$
  - exit ticket: $2{,}42$
  - s1: $565{,}5$ and $399{,}9\,\text{V}$, $375$ and $7{,}5\,\text{A}$, $0{,}225\,\%$
  - s2: $81{,}81^\circ$ and $8{,}19^\circ$, $68{,}6\,\mu\text{s}$, $+0{,}707\,\mu\text{s}$, $0{,}897\,\text{mW}$
  - s5: $533{,}0$ and $532{,}2\,\text{nm}$
  - s6: $18{,}29\,\text{MHz}$, $3{,}914 \cdot 10^7\,\text{m/s}$, $0{,}341\,\text{m}$, $80$ turns, $4{,}37\,\mu\text{s}$, $4{,}50 \cdot 10^{15}\,\text{m/s}^2$
  - s7: $2{,}9978 \cdot 10^8\,\text{m/s}$, $1{,}089\,\mu\text{J}$, $436\,\text{MJ}$, $0{,}579\,\text{MJ}$, $753$ cars
  - s8: $1{,}5$, $2{,}0 \cdot 10^8\,\text{m/s}$, $0{,}75\,\text{ns}$, $41{,}8^\circ$
  - s9: $2{,}4$ and $1{,}8\,\text{V}$, $0{,}369\,\text{J}$
- **Choice items:** every one (lt-1…6, virhe-siirto, lue-kuvaaja, rata, aurinkolasit, tarkistus-1) has exactly one correct option, and each distractor's feedback is right. The tarkistus-3 model answer and criteria agree. No later-course physics: s6 and s7 state where classical mechanics stops holding.
