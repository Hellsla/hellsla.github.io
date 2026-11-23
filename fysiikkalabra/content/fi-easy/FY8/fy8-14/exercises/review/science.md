VERDICT: PASS
CONTENT-HASH: 6cc9799097272169

## Blocking

## Polish

## Checked
- Hash 6cc9799097272169 (`reviews.py hash fy8-14 --exercises --lang fi-easy`) at the start and the end.
- `git diff origin/main`: only solutions.md changed, and every removed line is a `**Kaava:**` line. Answers, answers.py, tolerances and the Sijoitus steps are unchanged.
- Inverse-square dose: "kääntäen verrannollinen etäisyyden neliöön" is stated. The chain $\dot H_2 = \dot H_1(r_1/r_2)^2$ and $H = \dot H_2 t$ is correct.
- Radiotherapy entrance dose: $D = N k D_\text{kerta}/n$ with $n = 5$, $k = 1{,}3$, $N = 30$ is the same as the old $30\cdot1{,}3\cdot D_\text{kerta}/5$.
- Bone versus tissue contrast: the same $I_0$ in front of the layer and the other layers cancelling out are stated as the reason. $I_\text{A}/I_\text{B} = 2^{d/d_{1/2}^\text{luu}-d/d_{1/2}^\text{kudos}}$ is correct; I checked it numerically.
- Thickness from the attenuation law: $I_0/I = 2^{d/d_{1/2}}$, then $\ln$, then $d = d_{1/2}\ln(I_0:I)/\ln 2$. This is right and uses the lesson's notation. The same holds for the count-rate calibration: $d_{1/2} = d_{20}\ln2/\ln(R_0:R_{20})$, then $d_x$.
- PET dose: $A_0 = am/(\tfrac12)^{t/T_{1/2}}$ and $H = kA_0 + H_\text{TT}$. The combined form $kam/(\tfrac12)^{t/T_{1/2}} + H_\text{TT}$ is correct.
