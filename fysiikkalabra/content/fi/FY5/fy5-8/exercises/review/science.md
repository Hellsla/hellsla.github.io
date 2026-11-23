VERDICT: PASS
CONTENT-HASH: 50ffe8c82ceb5c83

## Blocking

## Polish
- content/fi/FY5/fy5-8/exercises/solutions.md:192 (L2-07) — the Kaava stops at $\Delta E = E_1 - E_2$, and Sijoitus then substitutes three times. Simplified to the end, it would be $\Delta E = \tfrac{1}{2}F_\text{v}^2\left(\tfrac{1}{k_1} - \tfrac{1}{k_2}\right)$, which gives $0{,}60\,\text{J}$. The task asks for parts a–c separately, so the current form is acceptable.
- solutions.md:107 (L3-02) — the row $E_\text{alku} = E_\text{loppu}$ is right. Naming the energies once in words would help the reader: the spring's potential energy at the start, the gravitational potential energy at the top.

## Checked
- The hash was the same at the start and the end. I judged the diff and read the changed Kaava blocks on disk; the packet's diff joins their rows. The Sijoitus rows, answers, units and tolerances are unchanged.
- The previous Blocking item is fixed. L3-02 now starts from conservation of mechanical energy, $E_\text{alku} = E_\text{loppu}$, then $\tfrac{1}{2}kx^2 = mgh$ and $h = \dfrac{kx^2}{2mg}$. The symbol $E_\text{p}$ is no longer used for two different energies.
- Every block starts from the basic law ($F_\text{v} = kx$, $E_\text{p} = \tfrac{1}{2}kx^2$, $\Sigma F = F_1 + F_2$ or $4\Delta F = \Delta m\,g$) and ends in the form that Sijoitus uses.
- L2-03 starts from $\Delta E_\text{p} = E_\text{p2} - E_\text{p1}$, using energies measured from the rest length, as the Periaate says.
- L3-01 uses $\Delta F = k\,\Delta x$, which follows from linearity and is stated in the Periaate.
- L2-06 uses $x = L - L_0$, the extension, not the length. This is right.
- L3-03: $F_1 = -k_1x$ and $F_2 = -k_2x$ are the force components, and $|\Sigma F| = (k_1+k_2)x$.
- The paragraph splits in L1-07, L2-05 and L3-04 change no wording or physics.
- I recomputed every changed task in one script, and all of them match:
  - L1: 9000 N/m; 0,15 m
  - L2: 75 N/m and 0,24 J; 500 N/m; 0,54 J; 24,525 N/m; 0,60 J
  - L3: 24,5 kN/m; 0,1835 m; 3,2 N; 302 N/m
