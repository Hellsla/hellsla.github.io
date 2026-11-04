VERDICT: FAIL
CONTENT-HASH: 8a5d8df9ec7942ef

Full review of the 8 new tasks and set coherence.

## Blocking
- exercises.json:76, :95, :99 (L1-07) — **B/causality**: the task and feedback make density the reason oil and water form layers. Option C feedback ("Tässä öljy on tiheydeltään pienempää, joten se asettuu veden päälle omaksi kerrokseksi") answers "they mix" with density, and option D feedback says "pienempi tiheys tarkoittaa aina ylempää kerrosta". Both hold only for liquids that do not mix: ethanol (790 kg/m³, in the lesson table) and water have different densities and mix completely. — Fix: add "Öljy ei sekoitu veteen." to the stem. Rewrite C feedback to "Öljy ja vesi eivät sekoitu toisiinsa, joten ne jäävät eri kerroksiksi; tiheys ratkaisee, kumpi kerros on päällä." and D to "...pienempi tiheys tarkoittaa ylempää kerrosta, kun nesteet eivät sekoitu." Same in solutions.md:133.

## Polish
- solutions.md:153 (L2-05) — says "noin 2,6–2,8 g/cm³ on hyvä vastaus", but tolerance 0,03 accepts only 2,62–2,78, so 2,6 is marked wrong — write "noin 2,62–2,78" or widen the tolerance to 0,04.
- solutions.md:133 — "öljy on noin 0,92-kertaisesti vettä" is not a sentence, and "kuutiometri öljyä painaa 920 kg" uses painaa with kg (the glossary keeps mass and weight apart) — "öljyn tiheys on 0,92 kertaa veden tiheys; kuutiometrin massa on 920 kg". Same fix for "11-kertaisesti vettä" at solutions.md:143.
- solutions.md:189 (L3-05) — "kolme merkitsevää numeroa kuten massassa 520 g": 520 g and 100 cm³ are ambiguous (2–3 figures) — rest the 3 figures on the table densities, or say that the data are read as three figures.
- exercises.json:104 (L1-08) — same type as L1-03 (V = m/ρ in g and g/cm³); the plan's level-1 item is "lasku massasta" (m = ρV) — consider asking for the mass instead.
- L3-04 stem already says the reading rises too much, giving away half the reasoning (pedagogy's call).

## Checked
- Recomputed (one script): L1-08 5,00 cm³; L2-05 slope 2,705 (origin) / 2,706 (free) → aluminium; L2-06 slope 0,9205 g/cm³ = 920 kg/m³, intercept 85,0 g; L2-07 107/12 = 8,92 g/cm³, range 7,6–10,7; L3-05 250/6,26 = 39,94 cm³. All match answers.py.
- L2-06 model m_yht = ρV + m0 as in the lesson; L2-05 origin line has a physical reason; slopes from line points.
- L1-06, L3-04: one correct option each, distractor feedback right; bubble → V too large → ρ too small (10/11 ≈ 0,91).
- No duplicates (L2-07/L2-03, L2-06/L2-04, L3-05/L3-02 differ in type); notation is the lesson's.
