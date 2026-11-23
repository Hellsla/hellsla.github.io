VERDICT: PASS
CONTENT-HASH: 5f393ded3780a5f2
SCOPE: delta answers,md-paragraphs,numbers,reflow,structure,teacher-figure,typography,wording from 33edaea9b5ea3767 base c7f5e91

## Blocking

## Polish
- solutions.md:322 (fy2-6-L3-02), Järkevyys: the check now gives "$4{,}7 : 1{,}7 \approx 2{,}8$". This is right for the rounded values, but it no longer lands on the answer 2,7, so a check meant to confirm the answer seems to contradict it. Fix: "$4{,}73\,\text{TWh}$ ja $1{,}73\,\text{TWh}$, ja $4{,}73 : 1{,}73 \approx 2{,}7$".
- solutions.md:406 (fy2-6-L2-08), Järkevyys: "noin $1400$:aa voimalaa … Se on tuhansien voimaloiden suuruusluokkaa". 1400 is about a thousand, not "thousands". Fix: "noin tuhannen voimalan suuruusluokkaa".

## Checked
- fy2-6-L1-10 (new): $m = Pt/H = 2{,}0\,\text{MJ/s} \cdot 3600\,\text{s} / 10\,\text{MJ/kg} = 720\,\text{kg}$, which agrees with answers.py. The fuel power $P$ is the rate at which energy is released in burning, so $E = Pt = Hm$ is the right model and needs no efficiency. MAFY's LHV for milled peat, 10 MJ/kg, matches the lesson's table. ±4 % accepts 691–749 kg. "12 kg minuutissa" checks out.
- fy2-6-L2-08 (new): 2024 was a leap year, so 8784 h is right. $20\,200\,\text{GWh} / 8784\,\text{h} = 2{,}30\,\text{GW}$, which agrees with answers.py; ±2 % accepts 2,25–2,35. `fy2-6/fi-bars` prints 20,2 TWh at the wind bar and does not give the answer away. The source, Tilastokeskus 2024, is named.
- The rewritten Kaava lines start from the basic relations and combine them symbolically:
  - $E = Pt$
  - $P_\text{ka} = o\,P_\text{nim}$
  - share = part/whole
  - $m = kE$
  - the power balance $P_\text{kulutus} = P_\text{ydin} + P_\text{tuuli} + P_\text{muut}$
  - $E = N E_\text{koti}$
- In the energy ratio and the solar-park tasks, $P_\text{nim}$ and $t$ cancel correctly: $0{,}90/0{,}33 = 2{,}727$ and $0{,}90 \cdot 1600/0{,}11 = 13\,091\,\text{MW}$.
- Recomputed and unchanged: $70{,}08\,\text{GWh}$; $2\,803\,200$ households; $1{,}616 \cdot 10^{6}\,\text{t}$; $7{,}14\,\text{GW}$; $489{,}6\,\text{GWh}$ and 32 %; $16{,}6$ and $10{,}6\,\text{euroa/MWh}$.
- The paragraph splits (L1-06, L1-07, L1-08, the wind-share task, L3-01, L3-03 to L3-05) keep every claim and number.
- answers.py matches every numeric answer in exercises.json within its tolerance.
- Hash 5f393ded3780a5f2 at the start and at the end.
