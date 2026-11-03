VERDICT: PASS
CONTENT-HASH: c06e4f191eafe729

## Blocking

## Polish
- exit-ticket.json:8 — "neljän pienimmän ($1{,}89$–$3{,}02\,\text{eV}$) fotonit ovat näkyvää valoa" is true, but $7 \to 2$ ($3{,}12\,\text{eV}$, $397\,\text{nm}$) is also inside the lesson's own $1{,}7$–$3{,}3\,\text{eV}$ band. Matching lesson.md ("seuraavat … himmeitä ja näkyvän valon violetilla reunalla") with half a sentence would keep the two consistent (C, optional).
- lesson.md:66 — "noin $10^{-8}\,\text{s}$" is the usual textbook order of magnitude ($2p$ of hydrogen is about $1{,}6\,\text{ns}$). It is fine as an order of magnitude; "suuruusluokaltaan" would make that explicit (C).

## Checked
- All three round-1 blockers are fixed. The `simulaatio.model` box now says "Bohrin mallissa säde kasvaa kuten $n^2$". The `ennuste-3` distractor feedback names both the $10{,}20$ and the $12{,}10\,\text{eV}$ absorptions. lesson.md has "neljä kirkasta näkyvää viivaa; seuraavat ($397$, $389\,\text{nm}$, …) ovat himmeitä …". The round-1 polish was also applied: the absorption figure's freed electron sits at $0{,}4\,\text{eV}$, the model box explains the crowding from $13{,}20$ to $13{,}55\,\text{eV}$, and the lesson-answers comment is corrected.
- One script recomputed every number from my own formulas, and all agree with the text, lesson-answers.py and answers.py: the example ($656{,}5\,\text{nm}$), the misconception ($1459\,\text{nm}$), Balmer 3–8 → 2, the series limits ($91{,}2$, $364{,}7$, $820{,}6$, $1875{,}6\,\text{nm}$), kertaus, siirto ($1{,}04\,\text{eV}$; mistakes $1{,}89$ and $2{,}74$), tarkistus-2 ($1282\,\text{nm}$; mistakes $2279$ and $821$), the exit ticket ($12{,}09\,\text{eV}$) and $4 \to 1$ ($97\,\text{nm}$).
- The sim's absorption logic, run over the slider grid from $n = 1$, hits exactly $10{,}2$, $12{,}1$, $12{,}75$, $13{,}05$ and every value from $13{,}20$ to $13{,}55\,\text{eV}$. That matches the model box. koe-3 gives $10{,}20$ and $12{,}10$ absorbed, $11{,}00$ passing through and $14{,}00$ ionising ($E_\text{k} = 0{,}40\,\text{eV}$).
- In `levels`, `absorption` and `spectrum`, the pixel positions match $E_n$ and λ to within 1 px. The Bohr figure's radii are $1 : 4 : 9$ and its electron sits on the rings. In the hero, red is diffracted the most, which is the right grating order. The spectral colours are as intended.
- sim.js implements $E_n$, $hc/\Delta E$, $E_\text{k} = hf + E_\text{a}$ and the zone scales; every selectable line lands in its zone. The simState keys (dE, lambda, nEnd, Ek) match koe-1, koe-2 and koe-3, and each experiment locks mode and $n_\text{a}$ and varies one parameter.
- Every choice item has exactly one correct option, and each distractor's feedback is physically right.
- The energy zero, the negative levels, the ionisation condition, absorption only at a level difference, and the Bohr model's successes and limits all agree across theory, summary, glossary, inquiry and exit ticket. Scope: FY8, with $E_n$ given as data and no Schrödinger equation.
