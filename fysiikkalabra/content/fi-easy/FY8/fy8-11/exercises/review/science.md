VERDICT: PASS
CONTENT-HASH: f10e9d39ee6a7796

## Blocking

## Polish
- content/fi-easy/FY8/fy8-11/exercises/solutions.md (fy8-11-L2-09 Kuvaajan lukeminen) — the solution says the curve is "ruudukon viivalla 8,7" at A = 100, but the plotted curve is at 8,68. Fix: say "noin 8,7". The answer 160 MeV and the 15 % tolerance are fine: the exact curve gives 153,6 MeV, and readings 8,6–8,7 and 7,9–8,0 give 140–180 MeV.
- content/fi-easy/FY8/fy8-11/exercises/solutions.md (fy8-11-L3-06 Kaava) — $\log_2$ is not in the decay-law chapter, which uses $t = T_{1/2}\ln(A_0/A)/\ln 2$. L3-03 already uses $\log_2$. Fix: optionally add "eli $\ln(A_0/A)/\ln 2$".

## Checked
- 8g Kaava steps: L1-01, L1-04, L2-02 and L2-03 start from $Q = \Delta m\,c^2$ with $\Delta m = m_\text{alku} - m_\text{loppu}$. The neutrons are counted correctly, including the 2 that are left in L2-03. L3-01 uses $E = Pt = NQ$ and $m = Nm_\text{U}$. L3-02 uses $\Delta m = 4m_\text{H} - m_\text{He}$. All are correct.
- New L2-09: $Q = E_\text{B,loppu} - E_\text{B,alku} = 200(\varepsilon_{100} - \varepsilon_{200})$. The nucleon number is conserved and there are no free neutrons in the model. The task asks the student to assume the curve fits; that assumption is stated. The comparison with U-235 ($0{,}9 \cdot 236 \approx 210$ MeV) is right.
- New L3-06: the figure fy8-9/aktiivisuus has $A_0 = 720$ kBq and $T_{1/2} = 5{,}0$ h. 360 kBq is reached at 5,0 h and 180 kBq at 10 h. $t = 5{,}0 \cdot \log_2 1000 = 49{,}8$ h, so the answer is 50 h. Readings of 4,9–5,1 h stay inside 5 %. At 20 h the activity is 45 kBq. The task states the extrapolation and the safety threshold as assumptions. The Pu-239 comparison (about 240 000 a) is the same as in L3-03.
- answers.py: the new lines compute the same physics from the readings (160; 49,83).
- The captions lost "esimerkkiaineisto", but the task texts of L2-05 and L3-04 still say it, so the data are not presented as measured.
- The remaining changes only split paragraphs.
- One script checked the answers: all 19 stored answers agree with answers.py within tolerance.
- The hash was the same at the start and at the end.
