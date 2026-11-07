VERDICT: PASS
CONTENT-HASH: cb620fb4093e4a26

## Blocking
- none

## Polish
- lesson.md (Kaava, lopputilanteet 3–4): case 3's condition $Q_\text{v} < Q_\text{j,läm}$ also holds in case 4, and case 4 omits the water's own $Q_\text{v}$ (only implied by "edes"). A clean split would be case 3: $Q_\text{v} < Q_\text{j,läm} \le Q_\text{v} + s m_\text{v}$, case 4: $Q_\text{v} + s m_\text{v} < Q_\text{j,läm}$. Not an error ("voi jäätyä"); teacher's wording, so optional.

## Checked
- delta review 2026-11-07 round 2 (follow-up consistency edits): inquiry: every Q_v = c_v m_v ΔT_v; threshold step defines ΔT_v = T_v − 0 °C, ΔT_v = 33 400 J / 1257 J/K = 26,57 K, T_v = 0 °C + 26,57 K = 26,57 °C recomputed; 40 °C → 10,1 °C, Etsi virhe 25 140 J, 100 200 J, 2933 J/K, tea 58 660 J recomputed; ΔT_v = 70 K. Agrees with the teacher's Kaava. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): new Kaava (Q_v = c_v m_v ΔT_v, Q_j,läm, Q_j = Q_j,läm + s m_j, ΔT_v defined), the four end states (≥/≤ boundaries per guardrail, all-water-freezes case kept), the case 3/4 references and the Δ added in worked example and summary; worked example 25 140 J, 17 540 J, 6,0 °C recomputed; consistent with the unchanged balance and summary.
batch delta review (round 1, 2026-10-28): the hashed content on this branch is identical to the version passed on main after the physics audit (same hash e561d782886c645f; git diff against origin/main touches only review/usage.tsv), so the diff is empty. The sim LaTeX pass (KaTeX labels and readouts in lang/fi.json, window.simText tests, howto/model/calc boxes) is already part of that passed version; spot-read its sim strings for physics, symbols and units against the guardrails: no new or changed claim.
