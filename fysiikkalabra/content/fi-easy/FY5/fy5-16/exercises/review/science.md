VERDICT: PASS
CONTENT-HASH: a138b3319b58764e

## Blocking

## Polish
- exercises.json (fy5-16-L2-10 text) — "Energia-annos tarkoittaa korvaan tulleen äänen energian määrää" is strictly energy per unit area (I·t), as the solution's Periaate says; a fair simplification (C), optional "pinta-alaa kohti".

## Checked
- Hash same at start and end. Delta, round 1 (fi-easy): four captions lost "(esimerkkiaineisto)" (teacher's no-badge rule; data unchanged), added fy5-16-L2-10 (TTL Melu, source task).
- Script comparison with content/fi/FY5/fy5-16: same ids, answer, unit, tolerance, level, kind; every number in the L2-10 text and solution identical in fi and fi-easy.
- Source claims match sources.md: 80/85/87 dB(A) as 8-hour levels; 85 dB: noise-control programme, compulsory protectors, marked areas; limit assessed inside the protector; impulsive-noise quotation; no 3 dB rule attributed to TTL.
- Recomputed: 10^0,3 = 1,995; 10^1 = 10; 10^0,9 = 7,943; t2 = 8 h/7,943 = 1,007 h -> 1,0 h (tol 3 %); rule of thumb 8 h/2³ = 1 h.
- 94 dB all day: 7 dB above 87 dB(A); 1 h of 94 dB with a quiet rest of day: 94 + 10 lg(1/8) = 84,97 ≈ 85 dB(A), below 87, as stated.
- 1 dB changes I by +26 %/−21 %, "noin neljänneksen" fine; reference values span 80–87 = 7 dB.
- Model limits right: computed reference time, not a safe time; impulsive noise not covered.
- answers.py lines for L2-10 compute the right physics.
- No SCOPE line printed in the packet's instructions, so none written.
