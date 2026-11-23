VERDICT: PASS
CONTENT-HASH: 23cf1121d1015995

## Blocking

## Polish
- content/fi/FY5/fy5-9/exercises/solutions.md (L3-05 Kaava) — The block opens with $t = \tfrac{T}{4}$ before $T = 2\pi\sqrt{l/g}$, which defines $T$. Putting the basic law first would read more naturally.

## Checked
- Delta: the Kaava steps of L1-03, L2-01…L2-04, L3-01…L3-05, L2-05, L2-06 and L2-09 are now aligned blocks. They start from $T = 2\pi\sqrt{m/k}$, $T = 2\pi\sqrt{l/g}$, $f = 1/T$, energy conservation ($E = \tfrac{1}{2}mv^2 + \tfrac{1}{2}kx^2 = \tfrac{1}{2}kA^2$), the equilibrium $m_\text{p}g = k\Delta x$ and the linearised model $T^2 = \tfrac{4\pi^2}{k}(m + m_0) = am + b$. Each ends at the form the Sijoitus uses. Every rearrangement is algebraically right. The packet's diff collapsed the line breaks; I read the file on disk.
- L3-03: $N = t/T'$ and $\Delta t = t - NT = t(1 - T/T')$ is the right counting model for the clock.
- L2-09: $\sqrt{k/m} = 2\pi/T$ is right, so $v_{\max} = 2\pi A/T$.
- One script recomputed every changed task. L1-03 3,183 Hz, L2-01 0,5591 m, L2-02 0,90 kg, L2-03 0,6325 m/s, L2-04 3,252 s, L3-01 1,732 m/s, L3-02 26 160 N/m and 1,390 s, L3-03 21,72 s, L2-05 9,772 m/s², L2-06 20,14 N/m, L3-04 1,570 s²/kg, 25,15 N/m, 21,0 g and 17,69 N/m, L3-05 0,549 s, 0,5981 and 0,5988 m/s, L2-09 0,471 m/s. All match the Sijoitus lines and answers.py, which are unchanged.
- New sentence in L3-05's Järkevyys: I computed the exact large-amplitude factor through the AGM. At 10° it is 1,0019 (0,2 %, as the text says), and at 60° it is 1,0732, which agrees with L2-07's 1,073. Calling it "sama suuruusluokka" as the 0,13 % speed difference is fair.
- L3-05's paragraph split changes no other wording.
- Hash 23cf1121d1015995 at the start and at the end.
