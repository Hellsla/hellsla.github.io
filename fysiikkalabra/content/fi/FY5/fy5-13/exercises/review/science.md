VERDICT: PASS
CONTENT-HASH: 3fca34ecee93e95f

## Blocking

## Polish
- solutions.md fy5-13-L1-03 Järkevyys — "matalimmat äänet, joita ihminen juuri ja juuri kuulee (noin 20–40 Hz)": 32,7 Hz is clearly audible at organ levels. Consider "lähellä kuulon alarajaa (noin 20 Hz)".

## Checked
- All 12 answers recomputed in one script with my own formulas (f1 = v/2L, v/4L, λ = 2d, f4 = 4f1, Δf = Δv/2L, v = 4Lf, L = 3v/2f3, v = 2Lf/n, f1/2, f_b − f_a, (f_b − f_a)/2 → v/4f1). All agree with answers.py and exercises.json.
- L2-04 figure (figures.py task_string): sin(4πu) over the 0–1,20 m ruler gives four loops and five nodes; the description gives the same data; the answer is not shown.
- L3-02 and L3-03: the successive-resonance reasoning is right (string differs by f1, closed pipe by 2f1; 510 = 3·170 and 850 = 5·170 confirm odd harmonics).
- L2-02: closed end at the water = displacement node; the end-correction remark (shortest column slightly shorter than λ/4) is physically right; 3 significant figures justified.
- Significant figures and tolerances fit the data (L2-01: 2 sf from Δv = 7,0 m/s, tolerance 0,03).
- Speed of sound 340 m/s used consistently, as in the lesson brief; notation (f_n, λ_n, L, n odd) matches the brief.
- Every solution has Annettu, Kysytty, Periaate, Kaava (symbolic first), Muunnokset, Sijoitus, Vastaus, Järkevyys with a real check.
