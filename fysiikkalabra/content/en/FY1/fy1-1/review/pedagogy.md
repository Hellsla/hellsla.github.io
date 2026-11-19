VERDICT: PASS
CONTENT-HASH: 9b532fe015859d89

## Blocking
(none)

## Polish
1. lesson.md Summary / inquiry.json `reflect` — the opening question ("Why can physics study both a proton and the whole universe?") is never answered in words. The reflect returns only to the "42 orders" count. Fix: add one sentence to the reflect or the Summary: the same method (model, prediction, measurement) and the same four interactions work at every scale, so one science covers both ends.
2. inquiry.json `menetelmat` (optional) — the slot goal "physics is based on experiments" is carried on the required path only by the Key idea paragraph and exit-ticket question 2. The investigation reads model values off a menu, so the student never sees a measurement become a size. Fix: make `menetelmat` required (it is short), or move its proton question into Tutki.
3. inquiry.json `exp-2` question — the choice ("Which statement correctly describes how they are related?") can be answered from the theory text and does not use the recorded rows. Fix: ask for a number the rows give (for example the orders between Neptune's orbit and the Milky Way, or between the Milky Way and the universe), and keep the nesting statement for the check.
4. Repetition of atom vs proton: pred-1, exp-1, the Formula section, the ladder figure and the worked example all use $1.1\cdot10^{-10}$ vs $1.7\cdot10^{-15}\,\text{m}$ with the same answer. Fix: give the worked example a different pair (for example the Milky Way and the Solar System's planetary region, or a person and a hair).
5. inquiry.json `tunnista`, black-hole option — the lesson never says how large a stellar-mass black hole is. A student can only exclude it by scaling Sgr A* down, which is not hinted. Fix: add to the feedback or the text: "$2.5\cdot10^{10}\,\text{m}$ for $4.3\cdot10^{6}$ solar masses means about $8\,\text{km}$ for $1.4$ solar masses, so the horizon would be smaller than $20\,\text{km}$". Also, the Planck-length sentence (quantum gravity) goes beyond the course scope; shorten it to "a size calculated from constants of nature, far below anything measured".

## Checked
- Learning path: prerequisites (powers, units of length) are enough. The order is model, powers of ten, order of magnitude, ratio, light-year, matter, universe, interactions, and each step builds on the last.
- Scope matches the teacher's briefs of 2026-10-27 and 2026-10-28 (no quantum mechanics, no stellar evolution beyond the object types). Workload is at the upper limit for one lesson, but optional items (kertaus, exp-3, menetelmat, virhe, siirto, check-3) are marked.
- The predictions come before the evidence (pred-1 and pred-2 are gated by `reveal` on exp-1 and exp-2). Wrong-option feedback repairs the misconceptions (a nucleus drawn large, an exponent difference read as a ratio, adding exponents).
- Numbers checked: 42 and 62 orders, 8 orders from Neptune to the Milky Way, 6 from the Milky Way to the universe, the $10^{36}$ ratio, the Eratosthenes answer 12 732 km, the Sun to neutron-star ratio $5.8\cdot10^{4}$, and the order-of-magnitude rule on $4.0\cdot10^{16}\,\text{m}$ → $10^{17}$.
- The worked example has seven stages, one step each, symbolic before numeric, with a reasonableness check. Solutions in Tutki, Sovella and Tarkista follow the seven-part form.
- Option feedback does not refer to letters or positions. The speakers' roles are not skewed (only one named speaker, Veera, in the error item).
- Exit ticket: question 1 tests interactions and range, question 2 tests model testing. Neither asks about orders of magnitude, but check-1, check-c2 and check-2 cover them.
- English reading level and terms fit 16–19-year-olds. The glossary terms are used consistently, and "observable universe" is flagged by the packet as not yet in glossary.json (developer task).
- Not verified from captures (not opened; the packet's text and the deterministic checks were relied on): phone clipping and the simulation's behaviour. I found nothing in the text that would break at 360 px.
