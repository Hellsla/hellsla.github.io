VERDICT: FAIL
CONTENT-HASH: 76b9b8b3e6ff81b1

## Blocking
- lesson.md:134 and :262 (Tiivistelmä) — "Virhe-arvio pyöristetään yhteen merkitsevään numeroon, tai kahteen, jos ensimmäinen numero on 1" contradicts the teacher's rule that an error estimate has one significant figure. Fix: drop the exception in both places. In the example on :134, use a one-figure estimate, e.g. $3{,}2\,\text{s} \pm 0{,}1\,\text{s}$ rather than $3{,}18\,\text{s} \pm 0{,}1\,\text{s}$.
- lesson.md:237–251 (Esimerkki: Sijoitus, Tulos, Järkevyys) and figure fy13-ex (lessons/FY1/fy1-3/figures.py:105–115) — the example gives $\Delta t = 0{,}12\,\text{s}$ with two figures, $t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}$ and $\varepsilon = 3{,}8\,\%$. Fix, either way:
  - (a) Apply the rule: $\Delta t \approx 0{,}1\,\text{s}$ and $t = 3{,}2\,\text{s} \pm 0{,}1\,\text{s}$. Then $\varepsilon = 0{,}12\,\text{s} : 3{,}18\,\text{s} \cdot 100\,\% \approx 4\,\%$, one figure as in check-2 and the exit ticket. Rewrite Järkevyys for the band $3{,}1$–$3{,}3\,\text{s}$, which holds four of the six results.
  - (b) Change the data so that the half-range's first digit is 2–9.
  
  Update the figure and lesson-answers.py to match.

## Polish
- inquiry.json exp-3 hint 3 and solution — "$0{,}0850\,\text{s}$", but the readout shows $0{,}085\,\text{s}$ (open since round 2).
- inquiry.json contribution — names only random and systematic error. Add karkea virhe (open since round 2).
- lessons/FY1/fy1-3/lesson-answers.py — inq-ice-corrected is unused (open since round 2).
- Spelling — the round-3 edits write "virhearvio" while the rest of the lesson writes "virhe-arvio". Pick one.

## Checked
- Round-2 blocker fixed. Check-2's Vastaus is "$2\,\%$, one figure as in $0{,}05\,\text{s}$ (laskimen arvo $2{,}08\,\%$)". The exit ticket gives "$\approx 2\,\%$". Answer 2.1 with tolerance 0.05 accepts 2 (4,8 % off).
- Round-2 polish fixed: karkea virhe now says "kerran vahingossa". One sentence explains Δx as both the error and the always-positive estimate.
- No ×, \times or ÷; \cdot for products; ":" in the divisions written as operations; error symbols Δx, Δt, Δt_sys.
- One script recomputed check-2 (2,08 %), the exit ticket (1,99 % and 19,9 g), the worked example (3,1817 s, 0,12 s, 3,77 %) and siirto (5,44 g with its mistakes). The other values match round 2.
- The formulas and the sim model are unchanged since round 2 and correct. Experiments lock the parameters they do not vary.
- Content hash is identical at the start and the end.
