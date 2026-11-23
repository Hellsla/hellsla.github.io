VERDICT: PASS
CONTENT-HASH: 4d32277ff3d6470a
SCOPE: delta kaava-steps (work queue 8g) from 914daee64065bfde

## Blocking

## Polish
- content/fi-easy/FY8/fy8-1/exercises/solutions.md:408 and :431 — the earlier note stands: "muutaman nanometrin" and "noin ±10 nm" disagree — give one figure.

## Checked
- Every changed Kaava step (L1-01, L1-04, L1-07, L1-09/L1-10, L2-01…L2-07, L3-01…L3-05): each starts from E = hf, c = fλ, hf = W + E_k,max, P = NE, I = Ne, E_k = ½mv² and solves symbolically to the form the Sijoitus row uses; every rearrangement checked by hand (λ0 = hc/W, N = Pλ/(hc), W = hc/λ − E_k,max, U_s = (h/e)f − W/e, f0 = f1 − E1/k, t = W/(IA), I = eηPλ/(hc), U_s = (E_f,max − W)/e). No sign or factor error.
- The slope steps now name k = h/e (eV/Hz) and W = hf0 = kf0: consistent with the Sijoitus rows.
- On disk the Kaava steps are aligned display blocks (the packet diff shows them flattened); the rows read correctly.
- Paragraph splits in L1-06, L1-08, L3-04, L3-05 only: joined text identical to the passed version.
- exercises.json, answers.py, numbers and tolerances unchanged.
- Hash 4d32277ff3d6470a at the start and the end.
