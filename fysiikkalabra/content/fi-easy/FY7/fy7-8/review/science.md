VERDICT: PASS
CONTENT-HASH: 02ed5717f19b13fa
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the FY7 editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- Two-wire model (P = UI, $P_\text{h} = RI^2$, R = both conductors, current out and back) is now explicitly a simplification; real grid three-phase, 400 kV = line voltage, $P = \sqrt{3}\,UI\cos\varphi$ for a balanced load, power factor 1 when in phase — correct. Low-voltage network ≈400 V phase–phase / ≈230 V phase–neutral ($400/\sqrt3 \approx 231$) correct. "Teho on jännitteen ja virran tulo" limited to a resistive load: correct. Loss-graph aria (200 MW, 6,0 Ω): 100 kV → 12 %, 200 kV → 3,0 %, 400 kV → 0,75 % recomputed. Inquiry virhe: $I = 500\,\text{A}$, $P_\text{h} = 1{,}5\,\text{MW}$; siirto: $I = 300\,\text{A}$, $P_\text{h} = 720\,\text{kW}$ — both now state the two-wire model, answers unchanged and right. Grid single-line aria, figures.py and figures.json match the lesson. Summary consistent with theory. fi, en, fi-easy agree. Hash identical at start and end.
- Round 2: "Samalla jännitteellä, virralla ja tehokertoimella … noin $1{,}73$-kertaisen tehon" (en "At the same voltage, current and power factor") is now exact (Minor resolved). en paragraph split otherwise only.
