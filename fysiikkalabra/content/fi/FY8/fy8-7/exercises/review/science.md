VERDICT: PASS
CONTENT-HASH: 550d4a2308e6dc21
Round: 1

## Blocking

## Polish
- exercises.json:136 (fy8-7-L1-09 statement 3) — the heating statement needs the idea that thermal equilibrium always keeps N₁ > N₂; the brief's Tiivistelmä teaches inversion by pumping but not why heating cannot do it. Fine as a reasoning statement if the lesson says it; otherwise add "lämmittäminen ei riitä" to the lesson or reword to "Populaatioinversio syntyy, kun ainetta lämmitetään" (still false, needs no Boltzmann reasoning).
- exercises.json:148 vs solutions.md (statement 5) — feedback says "satoja kertoja", solution "monta kertaa"; true for a He–Ne laser, not for every laser. Use "monta kertaa" in both.

## Checked
- Recomputed in one script: hc = 1,9865·10⁻²⁵ J m, 650 nm photon 3,056·10⁻¹⁹ J = 1,91 eV for laser and LED alike; key "1 epätosi, 2 tosi, 3 epätosi, 4 epätosi, 5 tosi" correct.
- Statement 4: smaller dot (3 nm) → larger gap → shorter λ, so "A longer λ" is false; consistent with the Tiivistelmä.
- Statements 2 and 5 true as the lesson states them (stimulated photon copies energy, direction and phase; axial light amplified between mirrors).
- Distractors catch the chapter's own warned mistake (laser photons "more energetic", statement 1); every feedback's physics right; no de Broglie anywhere.
- Notation (hf, λ, E₂ − E₁, N₂ > N₁) as in the brief; answers.py only gained a comment and still runs.
- 3–6 statements with at least one true and one false (exercise-types type 8).
- Text only: the inline chain "hc = 6,626·10⁻³⁴ J s · 2,998·10⁸ m/s = …" in solutions.md:149 is long (~380 px estimated); KaTeX can break at = and ·, but the visual reviewer should measure it at 390 px.
- Hash identical at start and end.
