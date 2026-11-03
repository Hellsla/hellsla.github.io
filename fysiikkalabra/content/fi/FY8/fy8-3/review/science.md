VERDICT: FAIL
CONTENT-HASH: d9efd22fd0ba624e

## Blocking
- inquiry.json:147 (`simulaatio.model`) — **A**: "Bohrin kuvan ratojen säteet ovat kaavamaisia: todellisuudessa säde kasvaa kuten $n^2$" says real orbits exist, which contradicts lesson.md "Yleinen virhekäsitys" and the Bohr section (an electron has no orbit) — write "Bohrin mallissa säde kasvaa kuten $n^2$".
- inquiry.json:124 (`ennuste-3`, option "absorboituu … $0{,}8\,\text{eV}$ jää liike-energiaksi") — **A**: the feedback says "vain $10{,}20\,\text{eV}$ absorboituu", but the correct option's feedback, koe-3 and the conclusion all have $12{,}10\,\text{eV}$ absorbed too — write "ja $10{,}20\,\text{eV}$:n ja $12{,}10\,\text{eV}$:n fotonit absorboituvat".
- lesson.md:111 ("tuottavat vedyn neljä näkyvää viivaa"), with lesson.md:3 and inquiry.json:304 (`pohdi`: "miksi … näkyy juuri neljä viivaa?") — **B**: by the lesson's own visible band, $1{,}7$–$3{,}3\,\text{eV}$, the transitions $7 \to 2$ ($397\,\text{nm}$, $3{,}12\,\text{eV}$), $8 \to 2$ ($389\,\text{nm}$) and $9 \to 2$ ($384\,\text{nm}$) are also visible light. The text implies only four transitions to $n = 2$ fall in the visible, which its own numbers refute. The real reason the eye sees four lines is not stated: the higher lines are faint and lie at the violet edge, where the eye is barely sensitive — add half a sentence: "neljä kirkasta viivaa; seuraavat ($397\,\text{nm}$, $389\,\text{nm}$, …) ovat himmeitä ja näkyvän valon reunalla".

## Polish
- lesson.md `absorption` figure (caption: energy scale to scale) — the freed electron for $14{,}0\,\text{eV}$ is drawn about $1{,}4\,\text{eV}$ above zero; at this scale $E_\text{k} = 0{,}4\,\text{eV}$ is about 7 px — put the dot at y ≈ 39.
- sim.js `model()` — with TOL $0{,}03\,\text{eV}$ and levels up to $n = 30$, every slider step from $13{,}20$ to $13{,}55\,\text{eV}$ is absorbed from $n = 1$. This is physically fair (the levels crowd together), but a student may wonder why; the model box could say that near $13{,}6\,\text{eV}$ the levels are so dense that almost every photon matches one.
- lessons/FY8/fy8-3/lesson-answers.py — the comment says "slider value 12,09 eV", but the slider step is $0{,}05$ and the tasks use $12{,}10\,\text{eV}$ (still within tolerance).

## Checked
- One script recomputed every lesson and inquiry number with my own formulas: example $656{,}5\,\text{nm}$, misconception $1459\,\text{nm}$, the Balmer lines and their differences ($170 / 52 / 24\,\text{nm}$), the series ranges $91{,}2$–$122$, $365$–$656$ and $821$–$1876\,\text{nm}$, kertaus $1{,}89 / 3{,}02\,\text{eV}$, siirto $364{,}7\,\text{nm}$, tarkistus-2 $1282\,\text{nm}$ with mistakes $2279$ and $821$, exit ticket $12{,}09\,\text{eV}$. All agree.
- Every choice item has exactly one correct option. The distractors' feedback is right, apart from the ennuste-3 item above.
- `levels`, `absorption` and `spectrum` figures checked pixel by pixel against $E_n$ and λ; the Bohr figure's radii are $1 : 4 : 9$; $a_0 = 0{,}053\,\text{nm}$.
- sim.js: $E_n$, $hc/\Delta E$, the absorption, ionisation and $E_\text{k}$ logic, and the zone ranges cover every selectable line. simState has dE, lambda, nEnd and Ek, and koe-1, koe-2 and koe-3 isolate the varied parameter.
- The Bohr model's successes and limits, the energy zero, the negative levels and ionisation are correct and stay in FY8 scope (no Schrödinger equation, $E_n$ given as data).
