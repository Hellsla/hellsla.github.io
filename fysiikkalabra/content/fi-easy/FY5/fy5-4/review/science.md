VERDICT: PASS
CONTENT-HASH: 3a034727967b1659

## Blocking

## Polish
- inquiry.json simulaatio `text`/`calc`, exp-1 measure label — "lähtökitka" is used as a quantity in Tutki before it is named; the full name "täysin kehittynyt lepokitka eli lähtökitka" appears only in the feedback of the optional pred-3 (friction guardrail P8: name it so where it is introduced) — write "Lähtökitka eli täysin kehittynyt lepokitka on $\mu_0 N = \mu_0 mg$" in the `calc` box (and/or the lead).
- inquiry.json pred-2 correct feedback — "Kitka osoittaa yhä kohti keskipistettä" is true only at the instant the grip fails; in the model the friction stays perpendicular to the velocity and points to the centre of the car's own, wider turn — "Kitka osoittaa yhä kohtisuoraan nopeutta vastaan, kaarroksen sisäpuolelle".
- lessons/FY5/fy5-4/lesson-answers.py `siirto-v-1` comment says "N taken as 2G"; the mistake fed back is "ΣF = mg" — align the comment (no student-visible effect).

## Checked
- One script recomputed every number from the task texts with my own formulas and matched lesson-answers.py: example $F_\mu = 6000\,\text{N}$, $\mu_0 \ge 0{,}5097 \to 0{,}51$ (rounded up, a "vähintään" value); Koe 1 $750/3000/6750/12\,000\,\text{N}$ against $11\,772\,\text{N}$, $v_\text{max} = 19{,}81\,\text{m/s}$ (rounded down to $19{,}8$), mistakes $22{,}15$ and $392{,}4$; Koe 2 ratio $0{,}920$ for every mass; siirto $15{,}34\,\text{m/s}$ (mistakes $18{,}79$, $10{,}85$, feedback right); check-2 $148\,\text{N}$ ($47{,}12$, $294{,}3$); check-3 $T = 0{,}765\,\text{N}$, $N = 1{,}67\,\text{N}$; exit ticket factor 9.
- Graph: pixel positions give $a_\text{n} = 2, 8, 18$ (r = 50 m) and 9 (r = 100 m) at 10/20/30 m/s; the text and aria-label agree.
- Δv figure: velocities tangent, equal length; Δv points from the arc's midpoint to the centre, as the text says. Kaarre, nyppylä/notko and example force diagrams: N = G where a is horizontal, N < G on the crest and N > G in the dip, $F_\mu/G \approx 0{,}51$ in the example.
- Task figures (figures.py): virhe N + F_kp = G with F_kp up; valitse-a N > G; b N = G; c N < G; d N > G plus an invented downward F_kp. Each wrong option has one error, and its feedback names it. The kiekko model figure shows only G, N, T and a_n drawn apart.
- sim.js: $a_\text{n} = v^2/r$, $N = mg$, grip test $mv^2/r \le \mu_0 mg$; a skid turns at $\mu_0 g / v$ (radius $v^2/(\mu_0 g)$: 51 m at 20 m/s, 80 m and 115 m at 25 and 30 m/s), so the car leaves the asphalt only well over the limit, as the spec and pred-2 say. The model box states the static-friction skid simplification.
- Koe 1 and Koe 2 lock r, m, the surface (and v) and vary one parameter. simState carries an, Ftarve, Fmax, pito. Slider steps reach every initial value.
- Exactly one correct option in kertaus, pred-1–3, virhe, valitse and check-1. The distractors' feedback is right physics.
- Scope: no angular quantities. Centrifugal force is treated as a misconception, with the rotating-frame fictitious force correctly limited.
- Hash at start and end: 3a034727967b1659.
