VERDICT: PASS
CONTENT-HASH: c693c9ed74c26cf5

## Blocking

## Polish
- content/fi-easy/FY8/sovella/tasks.json (fy8-s5 b, third concept criterion) — "fissioiden lämpö kiehutti veden pois": the solution says the fission energy became the ore's internal energy (P1 guardrail); say "fissioiden energia kuumensi malmin, ja vesi kiehui pois".
- content/fi-easy/FY8/sovella/solutions.md:441 (fy8-s5 c) — "uraani-235:tä, Tämä": comma for a full stop.
- fy8-s3 (task text and a) — a school Cs-137 source also emits beta particles, which a GM tube counts; the model speaks only of photons. Harmless for the invented data, but one clause ("oletetaan, että putki laskee lähteen fotonit") would close it.

## Checked
- One script recomputed every number: s1 2,22 / 1,97 eV, λ3 = 295,9 nm, n = 1193, λ_max(Si) = 1107 nm, 0,83 eV; s2 Δm = 0,006005 u, Q = 5,594 MeV, A = 2,232e15 Bq, m = 3,52 kg, 238/270 → 4,23 kg, 83 %, 0,57 W/g, Po 0,160, U-238 ratio 5,1e7 (≈1,8e8 kg), 1791 W, 98,5 W, H_E = 0,566 mSv; s3 net rates, Rr², 1/√R, slope 5,63e-3, intercept −1,30 cm, K = 3,15e4, ±10 /min (14 %), ±55 (1,8 %), 6 %, r = 36,2 cm, 0,23 (0,27) µSv/h, 2,25 µSv, 16 µSv/d; s4 0,782 MeV, 7,16, N_n = 0,858, 135 s, 0,735, 271 s, 14 % / 26 %; s5 7,17, 1,364, 3,67 %, 1 : 26, 3,49 a, 4,7e17 J, 1,5e28 fissions, 5,8 t, 83 000 half-lives. All agree with answers.py and the solutions.
- Physics: atomic masses cancel electrons in α decay; quenching vs lifetimes (0,7 s, 110 s) and altitudes; single-photon threshold in Si; w_R and w_T chain D → H_T → H_E; 1/(r+d)² linearised as 1/√R vs r; Poisson √N with background; n → p e⁻ ν̄ via the weak interaction (udd → uud); Y = 2N_n/(N_n+N_p); Oklo moderator feedback and negative void effect; Pu-239 → U-235 as the tracer.
- Fixed during this review (hash 9092f186… → c693c9ed…): s3 d's Vastaus and rubric had said the tube cannot tell the source from background at 36 cm; at net = background a 1-min count is about 3σ above it. Both now say the source is hidden by background fluctuation "sen kauempana": correct.
- Rubrics: every criterion asks only what its part gives and asks; points add up (15, 20, 17, 16, 16); answer tolerances accept the stated alternatives (1190–1200, 135–140 s, 1,0–1,6 cm, 0,56 mSv).
- Scope: all inside FY8 central contents; data sources named (NIST, NASA, AME2020, NNDC, PDG 2024, IUPAC, STUK, Oklo literature); s3's counts are marked as invented.
- Significant figures and their reasons fit the data (two for s2 b, e, s4 c, s5 a, c).
- Hash c693c9ed74c26cf5 at the end (packet's 9092f186a00eeba9 at the start; the diff between them is the s3 d fix only).
