VERDICT: FAIL
CONTENT-HASH: 945476e5b7ef9fb3

## Blocking
- content/fi/FY5/fy5-8/exercises/solutions.md:107 (L3-02), A, definition and consistency — The new Kaava uses one unsubscripted symbol for two different energies: $E_\text{p} = \tfrac{1}{2}kx^2$ and then $E_\text{p} = mgh$. In this lesson (glossary, theory) $E_\text{p}$ is the spring's potential energy, so the second row says the spring energy equals $mgh$ as a definition. The basic equation, conservation of mechanical energy, is no longer written. The old row $\tfrac{1}{2}kx^2 = mgh$ at least showed the equality. — Fix: start from the principle and keep the two energies apart, for example `E_\text{alku} = E_\text{loppu} \\ \tfrac{1}{2}kx^2 = mgh \\ h = \dfrac{kx^2}{2mg}`, or use subscripted symbols ($E_\text{p,jousi} = E_\text{p,pv}$). The Sijoitus and the answer stay unchanged.

## Polish
- solutions.md:192 (L2-07) — The Kaava stops at $\Delta E = E_1 - E_2$ and then substitutes three times. "Simplify to the end" would give $\Delta E = \tfrac{1}{2}F_\text{v}^2\left(\tfrac{1}{k_1} - \tfrac{1}{k_2}\right)$ (= 0,60 J). The task asks for parts a–c separately, so the current form is acceptable.

## Checked
- Delta: the Kaava steps of L1-02, L1-05, L2-01, L2-02, L2-03, L3-01, L3-02, L3-03, L2-06, L2-07 and L3-05 are now aligned blocks that start from $F_\text{v} = kx$, $E_\text{p} = \tfrac{1}{2}kx^2$, $4\Delta F = \Delta m g$ and $\Sigma F = F_1 + F_2$. Every rearrangement except L3-02's symbol is right. The packet's diff collapsed the line breaks; I read the file on disk.
- L2-01 gives $\tfrac{1}{2}F_\text{v}x = \tfrac{1}{2}kx^2$ for a linear spring. That matches the lesson's triangle area.
- L3-01: $\Delta F = k\Delta x$ follows from linearity, and the Periaate says so.
- L3-03: $F_1 = -k_1x$ and $F_2 = -k_2x$ both point towards equilibrium, which agrees with the force diagram (both forces to the left).
- One script recomputed every changed task. L1-02 9000 N/m, L1-05 0,15 m, L2-01 75 N/m and 0,24 J, L2-02 500 N/m, L2-03 0,54 J, L3-01 24,5 kN/m, L3-02 0,1835 m, L3-03 3,2 N, L2-06 24,5 N/m, L2-07 0,60 J, L3-05 302 N/m, 37,75 J, 27,6 J and 73,1 %. All match the Sijoitus lines and answers.py, which are unchanged.
- Paragraph splits in L2-04, L2-05 and L3-04's conclusion change no wording.
- Hash 945476e5b7ef9fb3 at the start and at the end.
