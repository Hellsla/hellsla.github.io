VERDICT: PASS
CONTENT-HASH: 3636de61f06855aa

Delta review, round 2 (work queue 11c): only the `hints` of `sovella/tasks.json`, all 105 hints of the 35 written parts (s1–s9) read and compared with the Finnish hints, each part's rubric, `sovella/solutions.md` and answer. Diff `git diff origin/main -- content/fi-easy/units/fy9-moderni` (review/ ignored). Changes since round 1 re-checked, including the new glosses.

## Blocking
None.

## Polish
1. s9 a, hint 3 (fi-easy): the Finnish hint's last sentence is missing, so the advice not to use a measured point off the line is lost. Replacement: "Valitse suoralta piste, jonka arvot voi lukea tarkasti ja joka on kaukana origosta. Lue sekä $v$ että $d$. Älä käytä mittauspistettä, joka ei ole suoralla."
2. s1 c, hint 3 (fi-easy): "Vertaa sitä vuosiannokseen $5{,}9\,\text{mSv}$" drops "keskimääräiseen" and "osuutena" of the Finnish hint. Replacement: "Vertaa sitä keskimääräiseen vuosiannokseen $5{,}9\,\text{mSv}$: kuinka suuri osa siitä annos on?"

## Checked
1. Same models, symbols and conditions as the Finnish hints and the solutions (s1 $E = hc/\lambda$, half-life law, $H = A_m m k_\text{annos}$, $A = \lambda N$; s2 $E_3 - E_2$, $v = cz$ for small $z$, $v = H_0 d$, $1+z$; s3 $eU = hf - W$, $hf_0 = W$; s5 background subtraction and $\ln N$ line; s6 $P_\text{l} = nE_\text{f}$, $E = \Delta m c^2$, $P_\text{l} - P_\text{s} = Q/t$; s7 $Q = c_\text{v} m \Delta T$; s8 $\dot{H} = \dot{H}_0 e^{-\mu d}$, $\dot{H}_\text{max} = H_\text{max}/t$; s9 $t = 1/H_0$).
2. The glosses are physically right: hajoamisvakio, punasiirtymä (aallonpituuden venyminen), irrotustyö (energia, joka irrottaa elektronin metallista), kulmakerroin (jyrkkyys), ionisoida (irrottaa elektroneja atomeista), radioaktiivisuus (epävakaiden ytimien ominaisuus), lauhdutin, painotuskerroin, vaimennuskerroin, eksponentti.
3. Every stated number recomputed in the same script as the Finnish report and matches the task data ($30{,}1 \cdot 3{,}156 \cdot 10^{7}\,\text{s}$, $2{,}00 \cdot 10^{8}\,\text{eV}$, $235 \cdot 1{,}661 \cdot 10^{-27}\,\text{kg}$, $\Delta T = 80\,\text{K}$, $1{,}5\,\text{h} \cdot 220$, $1\,\text{Mpc} = 3{,}086 \cdot 10^{19}\,\text{km}$, and the rest). No hint gives a final answer. LaTeX and decimal comma throughout.
