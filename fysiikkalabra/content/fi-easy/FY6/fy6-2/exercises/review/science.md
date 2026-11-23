VERDICT: PASS
CONTENT-HASH: e0d944a8c7421a99
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from f3c6399e3049def6 base e238aa9

## Blocking

## Polish
- exercises/solutions.md:85, 187 (L2-04, L3-04 Kaava) — the labels $\Sigma U = 0$ and $\Sigma I = 0$ are Kirchhoff notation, taught only in a later chapter; the equations themselves ($U_\text{paristo} = U_\text{m} + U_\text{lamppu}$, $I_1 = I_2 + I_\text{m}$) are right and were already used — drop the labels or say in words "jännitteet samassa silmukassa" / "haarautumiskohtaan tuleva virta".
- exercises/solutions.md:175, 187 (L2-07, L3-04) — the symbol $s$ is used for the half-range scatter estimate (looks like a standard deviation) and, in another task, for the relative decrease $\dfrac{U_\text{ilman} - U}{U_\text{ilman}}$; $q$ on line 252 is likewise undefined — name each in words in the line, or use e.g. $\dfrac{\Delta U_\text{m}}{U_\text{ilman}}$.

## Checked
- Delta: Kaava steps rewritten as aligned blocks starting from $\Delta x = p \cdot x + n \cdot r$, $R = \dfrac{U}{I}$ and the loop/junction relations; every rearrangement is algebraically right and ends in the form the Sijoitus uses. L3-04 derivation moved from Sijoitus into Kaava intact.
- Recomputed in one script: 10,6 %, 3,20, 2,17 %, 0,1522 V, 0,08245 V, 4,76 %, ΔR 2,90 Ω, q 2,98: all agree with answers.py; no number changed.
- L2-04: $U_\text{lamppu} = R_\text{lamppu} I \approx 0$ because $I \approx 0$ is the right mechanism (voltmeter in series), stated condition present.
- Model answers L1-06, L1-07, L2-05/06, L2-07, L3-04, L3-05 only split into paragraphs; physics and numbers identical.
- exercises.json: only "esimerkkiaineisto" removed from captions (teacher-approved); multimeter-task figure teacher-approved and unchanged (1,37 V, 20 V range).
- Hash identical at start and end.
