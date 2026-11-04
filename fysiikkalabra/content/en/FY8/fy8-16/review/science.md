VERDICT: PASS
CONTENT-HASH: a75034a4c97a5dae

## Blocking

## Polish
- content/en/FY8/fy8-16/inquiry.json:40 — "An ionising photon can have any energy" is true only above the ionisation threshold (same wording as the passed Finnish source) — "can have any energy above 13.6 eV".
- lessons/FY8/fy8-16/lesson-answers.py:29 — the comment says the least-squares fit is 69,7, but the code gives 69,83, and koe-1 and sim-spec say 69,8 (shared file, not part of the translation) — change the comment to 69,8.

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json, exercises.json and solutions.md matches content/fi (compared by script, decimal separators normalised): nothing was lost or changed in translation.
- Recomputed in one script: the galaxy table (v, z, Δλ), the least-squares H0 = 69.83 with odd galaxies above the line and even ones below, 1/H0 = 13.97, 14.00, 13.58 and 19.56 Gyr, hook 669.4/495.8 nm, figure 689.1 nm, worked example z = 0.035045, v = 10 506 km/s, H0 = 70.04.
- CMB: Wien 1.063 mm, 3000/2.725 ≈ 1100, 3000 K peak 966 nm (near-IR, as tarkistus-1 says), 13.6 eV ↔ 91.2 nm.
- Transfer item 86.0 Mpc, and its mistakes 84.3, 8.6·10⁴ and 6020; virhe 4.4·10²⁰ s ≈ 1.4·10¹³ a (×1000); recall option 0.0143.
- BBN 2/8 = 25 %, Planck fractions 4.9/26.2/68.9 %, triple alpha 7.274 MeV, 1 Mpc = 3.26 Mly, timeline 13.8 − 4.6 = 9.2 Gyr.
- The conditions are stated where the laws are used: v = cz for z < 0.1; 1/H0 assumes constant expansion, and the text says why it differs from 13.8 Gyr; own motion explains the scatter.
- Causality: expansion of space (not Doppler from a centre), transparency through recombination, fusion up to the Fe-56 peak, r-process in supernovae and mergers.
- Assessment: exactly one correct option in each choice item; every distractor's feedback is physically right; the explain model answers and the exit ticket agree with the theory.
- The sim implements v = 70·d + own motion, z = v/c, λ = λ0(1+z) and 1/H0, as the model box states (the 8× exaggeration is said).
