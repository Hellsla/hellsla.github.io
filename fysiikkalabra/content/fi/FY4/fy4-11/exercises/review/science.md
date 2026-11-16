VERDICT: PASS
CONTENT-HASH: a1d86531e0f61248

## Blocking

## Polish
- solutions.md (fy4-11-L2-10, Kaava) — the final form $v = \sqrt{v_0^2 - 2a\,(d - v_0\,t_\text{r})}$ still stands after the part d sentence about $\mu$ — move it right after $v^2 = v_0^2 - 2as$.
- solutions.md (L2-10, Periaate and Järkevyys "Mallin rajat") — "ainoa vaakasuora voima on kitka" holds only when air resistance is neglected; neither the task nor the limits say so — add "kun ilmanvastus jätetään huomiotta" (the calculator's constant deceleration implies it; level C, not blocking).
- exercises.json (L2-10) — the answer box ($69{,}4\,\text{km/h} \pm 3\,\%$) follows the calculator's parameters read on 16.11.2026; if Liikenneturva changes them, the box and answers.py must follow.

## Checked
- Diff since the passed version (bab8736584): only solutions.md of L2-10, Vastaus split into paragraphs before "Lisäksi: a)", "b)", "d)", "e)"; whitespace-normalised text identical to the passed version; exercises.json and answers.py unchanged.
- All 22 numeric answers recomputed in one script with my own formulas (own origin fits for L2-05 $a = 7{,}85$, L2-06 $60{,}0\,\text{km/h}$; own linear fit for L3-04 $t_\text{r} = 1{,}21\,\text{s}$, $a = 5{,}10\,\text{m/s}^2$, $v_\text{max} = 65{,}9\,\text{km/h}$): all inside tolerance and equal to answers.py.
- L2-10 against the coordinator's source record: 1 s, 9 and $1{,}5\,\text{m/s}^2$, rounding to a metre; model gives 11/7/18, 17/15/32, 22/27/50, 28/43/71 m and ice 165/187 m, exactly the calculator's values.
- L2-10 c: $49{,}66\,\text{m} < 50\,\text{m}$, margin $0{,}34\,\text{m}$ called unreliable (safe side); $100\,\text{km/h}$: $v = 19{,}28\,\text{m/s} = 69{,}4\,\text{km/h}$, with the rounded 28 m $69{,}8\,\text{km/h}$; two figures justified.
- L2-10 d: six-fold braking distance, $\mu = 0{,}92$ and $0{,}15$ from $\mu mg = ma$; e: ABS cannot raise $\mu$, $1{,}25^2 = 1{,}56$, calculator 27 → 43 m. No "muuttuu lämmöksi".
- L2-08: one correct option ($2 : 4 = 0{,}50$); L1-06, L1-07: one correct option each, distractor feedback names the real error.
- L3-05: $0{,}79\,\text{m}$, $10\,\text{kN}$, $18\,\text{kN}$ (two figures from $4{,}5\,\text{m/s}$); L3-06 $10{,}5 \to 11\,\text{kN}$ inside tolerance 0.05; L3-04 c 80 km/h: $75\,\text{m}$, impact $51{,}5\,\text{km/h}$, 60 km/h $47\,\text{m}$.
- Figures ex-tv-jarrutus (20 + 25 = 45 m) and ex-tv-tyyny (17,5 − 7,0 = 10,5 kN) give the values at grid crossings.
- Hash the same at the start and the end.
