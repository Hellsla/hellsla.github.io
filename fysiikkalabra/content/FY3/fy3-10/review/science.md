VERDICT: PASS
CONTENT-HASH: 69ae26d6b93fc889

## Blocking

## Polish
- lesson.md:14 (Ydinajatus SVG): helium/air arrow length ratio is 2,0, but √(29/4) ≈ 2,7. The direction is right. Optional: shorten the air arrows to about 10 px.
- (Reused; file unchanged) solutions.md L1-03 Järkevyys: "18 g … tavallisen patruunan koko". Typical cartridges hold 24–38 g; use "pienen".
- (Reused) solutions.md L2-01 Järkevyys: optionally add that attraction dominates at 288 K and 180 bar (Z < 1).

## Checked
- The hash was 69ae26d6b93fc889 at both the start and the end.
- Ydinajatus SVG (new): 12 particles in each balloon (equal n). The labels n, m = 0,83 g and 6,0 g match the worked example. The aria-label claim is correct: same T, same mean kinetic energy, so v ∝ 1/√m.
- Kaava SVG (new): 2N has 12 particles and the same arrow length; 2T has 6 particles with arrows √2 longer (1,42); V/2 has gas height 74 of 148 px. The labels p, 2p, 2p, 2p agree with pV = nRT, and the LaTeX symbols are correct.
- sim.js speed (new): each frame advances deltaTime·speed of simulated time; tAvg and pMeasured use simulated time.
- Playwright, 4 s real time per speed: 0,25× gives tAvg 1,0 s and ratio 0,975; 0,5× gives 2,0 s and 1,000; 1× gives 2,03 s and 0,988. The default is 0,5. The change event sets simState.speed.
- Playwright at 0,25× with N = 20: the 2 s window filled in 8,0 s of real time. Twelve readings had sd 3,8 %. In 200 independent windows the sd was 5,0 % at N = 20 and 2,5 % at N = 100. So "±10 %" (≈ 2σ) holds.
- Lisätietoja (new): measured/predicted = (p/p_ref)/[(N/100)(T/300)/V_rel] = (pV/NT)/(p_ref V_ref/N_ref T_ref), which is correct. "Nopeus muuttaa vain tahtia" is confirmed above.
- Reused (all unchanged): 12 answers within 0,5 %, solutions, exit ticket, worked example, formulas and FY3 scope.
- Reused: the sim physics p = NkT/A, the isothermal volume change and the reference state (lesson.md:196).
