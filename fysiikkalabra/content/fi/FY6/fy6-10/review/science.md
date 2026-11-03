VERDICT: FAIL
CONTENT-HASH: 77512beb804a33e4

## Blocking
- lesson.md:395, :523; inquiry.json:149, :299, :344, :403; assets/sims/fy6/fy6-10/sim.js:11; lessons/FY6/fy6-10/lesson-answers.py:8, figures.py:12, sim-spec.md — (A, course constant) Coulomb's constant is $8{,}99 \cdot 10^{9}$ everywhere, but the FY6 rule is $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N} \cdot \text{m}^2}{\text{C}^2}$ — use 8,988 in the text, the sim, the scripts and the figure generator (and the glossary entry for Coulombin laki). Then re-quote the model readings: with 8,988 the sim shows $3{,}99\,\text{mN}$ at 3,0 cm (not 4,00) and $2{,}00\,\text{mN}$ at $q_2 = +40\,\text{nC}$ (not 1,998); fix ennuste-1/-2 feedback, koe-1 hint and solution, and the johtopäätös model to match. The rounded answers (0,24 mN, 0,92 mN, 30 nC) do not change.
- lesson.md:327 — (A, definition consistency) "pieneen positiiviseen koevaraukseen"; the next chapter (fy6-11) and the glossary name the same concept *testivaraus* — write "testivaraukseen" so the student meets one term.

## Polish
- lesson.md:3, inquiry.json:19 — "seinään, jossa ei ole sähkövarausta" suggests a neutral wall holds no charges, which the polarisation paragraph then relies on — "seinään, jolla ei ole nettovarausta / joka on sähköisesti neutraali".
- lessons/FY6/fy6-10/lesson-answers.py "virhe-ilman-nelio" computes $1{,}1 \cdot 10^{-5}\,\text{N}$ (r = 0,020 m), but the option in inquiry.json:299 states $1{,}1 \cdot 10^{-7}\,\text{N}$ (r = 2,0 unsquared, as the student wrote) — compute the displayed value.
- lesson.md (Kappaleiden varautuminen, influenssi + maadoitus) — optionally name the sign: the grounded conductor keeps a charge opposite to the rod's when the ground is broken before the rod is removed.

## Checked
- Every number recomputed independently with k = 8,99 and 8,988: 12 exercises, Esimerkki (2,397·10⁻⁴ N, 24 mg), graph F(r) 4,0/1,0/0,44/0,25 mN, siirto 0,923 mN, tarkistus-2 30 nC, koe-1 ratio 16, kertaus, exit ticket — all agree with answers.py/lesson-answers.py.
- check-graph screenshot: points (3; 8,99), (9; 1,0) mN lie on k q²/r² with q = 30 nC.
- Sim: F = k|q1q2|/r², equal and opposite F21/F12, sign → direction, no induction stated in the model box; field lines green, forces red; simState keys F, F12, F21 give the measured quantities with the locked parameters isolating r and q2.
- Predictions: exactly one correct option each; distractor feedback correct; ennuste-3 polarisation model physically right.
- Influence/polarisation mechanism (closer opposite charge, force falls with distance) consistent across theory, ennuste-3, tarkistus-3 and summary.
- Coulomb's law conditions (point charges, uniformly charged spheres, vacuum ≈ air) stated; third-law pair notation F12/F21 consistent between text, figure and sim.

