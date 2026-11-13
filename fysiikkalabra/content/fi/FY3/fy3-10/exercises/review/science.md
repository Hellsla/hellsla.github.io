VERDICT: PASS
CONTENT-HASH: aacdb2b4ad9b71db
SCOPE: delta added-exercise from 8c50fb38cfdcf2c1 base 89bcb63b7431

## Blocking
(none)

## Polish
- L2-09 — its answer $n_B = 0{,}0361$ mol is the intermediate step of L2-04 on the same figure (`n_B` in answers.py); a student doing both repeats the step. Consider asking for A, or for the ratio $n_A/n_B$ from the slopes, or ordering L2-09 before L2-04 as its warm-up.
- answers.py — the comment "# Added exercises (teacher 2026-11-12 …)" appears twice in a row; one is enough.

## Checked
- Only L1-09 and L2-09 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $n = 500/39{,}95 = 12{,}52$ mol, $p = nRT/V = 12{,}52 \cdot 8{,}31 \cdot 293 / 0{,}0100 = 3{,}047$ MPa → 3,05 MPa; answers.py agrees. MAFY value 39,95 g/mol matches docs/mafy-arvot.tsv (VERIFIED).
- L1-09 conditions: ideal-gas behaviour stated as an assumption in the task (needed at about 30 bar: real argon deviates by a few per cent, inside the model the task sets); $R$ given; MPa conversion shown; three figures justified by 0,500 kg (T, R also three).
- L1-09 check is a real one (molar volume 24 l/mol → about 30 × atmospheric ≈ 3 MPa).
- L2-09 recomputed: from B's points $p/T = 0{,}15$ kPa/K; $n = pV/(RT) = 60\,000 \cdot 0{,}00200 / (8{,}31 \cdot 400) = 0{,}03610$ mol; same from (200 K; 30 kPa).
- figures.py pt-suorat: B line $p = 0{,}15\,T$ kPa through gridline crossings (200; 30) and (400; 60); axes to scale from 0; the description lists the same points; neither gives $n$.
- L2-09 conditions: closed rigid vessel (fixed $n$, $V$) stated; temperature already in K; the line through the origin is consistent with $p \propto T$ at constant $V$ for a thin gas.
- Both solutions complete: given/asked, principle with reason, symbolic form first, conversions, substitution with units, rounding reason, real reasonableness check. Notation as in the brief ($pV = nRT$, $R = 8{,}31$, \textsf{l}).
- Units (MPa, mol) and relative tolerances (0,04, 0,03) fit the data; within FY3 central content (ideaalikaasun tilanyhtälö).
- Hash identical at start and end.
