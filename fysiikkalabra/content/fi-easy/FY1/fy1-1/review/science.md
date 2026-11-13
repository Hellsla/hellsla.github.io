VERDICT: PASS
CONTENT-HASH: c47f1ae7e8ee25d5

## Blocking

## Polish
- lesson.md:94 — the new rule says "Jos kerroin on alle noin 3 …", but line 46 introduces $a$ in $a\cdot10^{n}$ without the name *kerroin*. The physics is right: the true boundary is $\sqrt{10}\approx3{,}16$, and "noin 3" covers it. The S2 reader may still not link "kerroin" to $a$. Fix: "Jos kerroin $a$ on alle noin 3 …", or name $a$ the *kerroin* at line 46.
- lesson.md, figure after "Kohdetyyppejä, ei portaita" (line 266 onward) — the generic label "musta aukko" sits at about $10^{10}\,\text{m}$, which is Sgr A*. A stellar black hole would sit near $10^{4}\,\text{m}$. The caption says the icons are not to scale, and the text names "tämä musta aukko", so this is C. Optional fix: label it "Sgr A*" or "Linnunradan keskustan musta aukko".

## Checked
- The Suuruusluokka change agrees with the glossary and with check-1's feedback ("kerroinosa yli noin 3"). Every example follows the $\sqrt{10}$ rule: $170\to10^{2}$, $1{,}7\,\text{m}\to10^{0}$, $8{,}8\cdot10^{3}\to10^{4}$, $4{,}0\cdot10^{16}\to10^{17}$, $1{,}27\cdot10^{7}\to10^{7}$, $1{,}39\cdot10^{9}\to10^{9}$.
- Recomputed in one script: the example gives $k=6{,}47\cdot10^{4}$ and $\Delta n=5$; exp-1 gives 5, exp-2 gives 8 and exp-3 gives $-4$. Siirto gives $12\,732\,\text{km}$, and its mistakes are $40\,000$, $6366$ and $111$. Check-2 gives $57\,917$, and its inverted mistake is $1{,}73\cdot10^{-5}$. The reflect counts are 42 and 62. All agree with inquiry.json and lesson-answers.py.
- Magnitudes: the Sgr A* horizon diameter is $4GM/c^{2}=2{,}5\cdot10^{10}\,\text{m}$ for $4{,}3\cdot10^{6}M_\odot$. The observable universe is $8{,}8\cdot10^{26}\,\text{m}=93$ billion light-years. One light-year is $9{,}46\cdot10^{15}\,\text{m}$, and Proxima is $4{,}0\cdot10^{16}\,\text{m}$ away. The ratio of the proton's electric repulsion to gravity is $1{,}2\cdot10^{36}$. The Oort cloud is 17–830 times the heliopause distance. $(109)^{3}\approx10^{6}$ Earths fit in the Sun.
- Sim: `mainObj` and `kohdeExp` give water at $L=-9$, Earth at 7,7 and the universe at 27,5, as each intro says. Jump targets and $n$ values: atom $-10$, proton $-15$, Neptune's orbit radius 13, Milky Way 21, Planck $-35$, hair $-4$. The calc box's $62$ px is right.
- The OBJ sizes are sound rounded values. The model box says orbits are labelled by radius and drawn by diameter, which matches `ext`.
- Every figure's numbers check out: the power-of-ten axis (minor tick = $10^{5}$), the five steps from proton to atom, the nested-structure scales $10^{9}$–$10^{27}\,\text{m}$, and the force arrows of the four interactions.
- Each prediction and choice has exactly one correct option, and every distractor's feedback is correct (neutron star vs black hole, the interactions, Etsi virhe).
- The four interactions, beta-minus decay, the residual strong force and EM vs gravity at large scales are stated correctly and within the brief's scope.
- The exit ticket and check-3's model answer agree with the theory.
- The hash was the same at the start and at the end.
