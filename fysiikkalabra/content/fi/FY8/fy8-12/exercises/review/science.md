VERDICT: PASS
CONTENT-HASH: c8f7f77d685ed452

## Blocking

## Polish
- exercises.json:6 (L1-01) — Co-60 emits two gamma lines, $1{,}17$ and $1{,}33\,\text{MeV}$. The $10{,}4\,\text{mm}$ is the narrow-beam lead value at their mean, $1{,}25\,\text{MeV}$ (XCOM: 9,9 mm at 1,17 MeV and 10,8 mm at 1,33 MeV). The value is right as given data. — If wanted, write "keskimääräiselle energialle $1{,}25\,\text{MeV}$" in the task and the solution.
- solutions.md L2-03 — the answer is given as $5{,}3\,\text{mm}$ but exercises.json has 5.34. Both are within tolerance. — Consider 5.3 in the JSON to match the stated rounding.

## Checked
- Recomputed all 12 answers in one script with my own formulas, and every one agrees with answers.py and exercises.json: 18,9 %; 1,61 · 10⁵; 6,0 mm; 7,67 %; 98,4 nm; 6,60 1/s; 0,811 %; 5,34 mm; 70,9 mm; 482; 34,99 mm; 1,243 · 10⁶.
- Data are realistic: Pb d½ for Co-60 is 10,4 mm (XCOM 1,25 MeV); concrete 39 mm and Pb 5,5 mm (Cs-137); water 8,1 cm (Cs-137, 80,9 mm); W = 34 eV; Am-241 5,49 MeV with a 4,1 cm range in air; a 1,0 MeV electron's CSDA path in air is about 3,6 m, which matches the stated winding path; water ionisation energy 12,6 eV.
- Background subtracted before using the attenuation law (L1-03, L2-01, L2-03, L3-02). L3-02 uses 2400 − 30 for the net rate correctly.
- L3-01: ion pairs per cm with W cancelling. The uniform-ionisation assumption is stated in the task.
- L3-03: the photon picture (one photon, one ionisation) and the heating explanation are correct. The reasonableness check (ratio of 2 · 10⁵) is a real check.
- Every solution states the principle, gives the symbolic solution before substitution, shows the conversions, and justifies its rounding by the limiting datum.
- Narrow beam is stated wherever the attenuation law is applied to a shield.
- Notation follows the lesson ($d_{1/2}$, $n_\text{i}$, $I : I_0$). Decimal comma, \cdot and LaTeX number + unit are used throughout. No de Broglie wavelength.
