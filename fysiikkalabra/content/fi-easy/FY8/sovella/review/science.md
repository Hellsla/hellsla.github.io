VERDICT: PASS
CONTENT-HASH: cf73b6eb91e31ba3

## Blocking
None.

## Polish
- fy8-s2 d: $1790\,\text{W}$ has three figures, while b) says the power has two and $t = 14\,\text{a}$ has two. Justify three or give $1800\,\text{W}$ (inside the tolerance).
- fy8-s2 b, Vastaus: the figures are justified by the fuel mass, which is not used for $m$; the limiting datum is the power.
- fy8-s3 d: the "valmistajan mukaan" dose rate $3{,}0\,\mu\text{Sv/h}$ is not covered by the source note (only the pulse counts are). Realistic magnitude (about 0,4 MBq Cs-137); name it an example value in the note.
- fy8-s3 a, criterion `conclusion`: "Todennäköisin syy on …" asks more than the task; the solution says "Esimerkiksi". Accept any justified cause.
- fy8-s5 text: "loput $99{,}274\,\%$": the shares sum to 99,994 % (U-234).
- fy8-s4 text states "suhde muuttui vain, kun vapaat neutronit hajosivat" as fact; d) expects it named as an assumption.

## Checked
- Hash identical at start and end. Every number recomputed from the task data in my own script: all agree with solutions.md, answers.py, rubric details and tasks.json answers within tolerance.
- s1: 2,223 and 1,968 eV match level differences; third line 295,9 nm (UV); 1193 excitations; Si limit 1107 nm; 1500 nm is 0,827 eV. Collisional quenching against lifetimes is the real mechanism; intensity versus photon energy correct.
- s2: Δm 0,006005 u, Q 5,594 MeV; A 2,232·10^15 Bq, m 3,52 kg, share 83 %; Po-210 0,160; U-238 ratio 5,1·10^7; 1791 W, 98,5 W; dose chain to 0,566 mSv, alternative 0,56 mSv.
- s3: background 22,4 1/min, all net rates, $Rr^2$, $R^{-1/2}$; least-squares d 1,31 cm, read line k 5,63·10^-3, K 3,15·10^4; uncertainties 14 %, 1,8 %, 6 %; r 36,2 cm, 0,23 µSv/h (dose rightly uses r; alternative 0,27). Figures' data and marked points agree; data declared model-made.
- s4: 0,782 MeV; decay equation, d → u, weak interaction; p/n 7,16; 135 s + 1 s; 1 : 5 gives 271 s; T½ 608,9 s from 878,4 s.
- s5: factors 7,165 and 1,364, share 3,67 %; moderator and void feedback correct; 3,49 a; 4,73·10^17 J, 5,8 t; 82 988 half-lives; Pu-239 → U-235.
- Scope inside FY8 central contents, no later-course physics. Points add up (15, 20, 17, 16, 16); criteria match tasks and solutions; "Hyväksytään myös" lists valid alternatives; level figure to scale.
