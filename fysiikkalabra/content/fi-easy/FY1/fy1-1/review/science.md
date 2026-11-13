VERDICT: PASS
CONTENT-HASH: 52e40c11931c671e

## Blocking

## Polish
- inquiry.json `check-1` feedback (both the $10^{16}$ and the $10^{17}$ option) — the feedback gives the rule "kun kerroinosa on yli noin 3, lähin kymmenpotenssi on seuraava". After the teacher's edit the theory no longer states this cut-off. It only says "kymmenpotenssien akselilla lähimpänä". The feedback is still correct, because $\log_{10}4 = 0{,}60 > 0{,}5$ and its second sentence explains it on the axis. But a student meets the "noin 3" rule only here. Optionally lead with the axis sentence ("akselilla $4{,}0\cdot10^{16}$ on lähempänä kohtaa $10^{17}$") and give "noin 3" as a rule of thumb. This is not an error.
- inquiry.json `simulaatio.howto` (carried from the earlier round) — "Lähennä/Loitonna muuttavat näkymän leveyden kymmenesosaksi tai kymmenkertaiseksi". In fact the buttons jump to the next whole power of ten.

## Checked
- Diff (commit 9e7b1d7): the Suuruusluokka paragraph lost its $\sqrt{10}\approx3{,}16$ sentences. What is left is correct. "The power of ten nearest the number on the power-of-ten axis" is well defined, because the figure just above it is an evenly spaced (logarithmic) axis drawn to scale. All three examples are right under either reading: $170 \to 10^{2}$, $1{,}7\,\text{m}\to10^{0}\,\text{m}$ and $8{,}8\cdot10^{3}\,\text{m}\to10^{4}\,\text{m}$. This is a fair level-C simplification and leaves no wrong picture.
- The edited paragraph agrees with the Tiivistelmä ("lähin kymmenpotenssi"), with the glossary (cut-off about 3) and with the sim's `kohdeExp = round(log10 m)`. That rule gives $-10$, $-15$, $-35$, $27$, $-4$ (hair, $7{,}0\cdot10^{-5}$), $13$ (Neptune, $4{,}5\cdot10^{12}$) and $21$ (Milky Way). These are the values the experiments' answers use.
- One script recomputed the lesson and inquiry numbers next to lesson-answers.py. Example: $k = 6{,}47\cdot10^{4}$, 5 steps. Exp-1: 5. Exp-2: 8. Exp-3: $-4$. Siirto: $12\,732\,\text{km}$; its distractors $40\,000$, $6366$ and $111$ are also right. Check-2: $57\,917$, with the distractor $1{,}73\cdot10^{-5}$. Virhe: $109$. Observable universe: $8{,}8\cdot10^{26}\,\text{m} = 93$ billion light-years. Everything agrees.
- Check-1: exactly one option is correct, $10^{17}\,\text{m}$, and every distractor's feedback is right.
- Rest of the lesson, re-read in full mode: structure of matter, nucleus/atom ratio, heliopause and Oort cloud, neutron star and Sgr A* horizon, the four interactions (Coulomb/gravity ratio $\sim10^{36}$ for two protons), Tunnista, Vuorovaikutukset, exit ticket and check-3 model answer. No error or unstated condition found. Scope stays within the FY1 brief.
- Hash $52e40c11931c671e$ was the same at the start and at the end.
