VERDICT: PASS
CONTENT-HASH: c55461f4fa2a8ea8
SCOPE: delta added-exercise from 08a5298251fe93cc base 415cbc7c6bc3

## Blocking

## Polish
- exercises/solutions.md:431 — Vastaus gives the reading accuracy as "noin $\pm 10\,\text{nm}$", but Annettu (line 408) says "muutaman nanometrin" and the example brackets the limit within $2\,\text{nm}$ (538/540). Use one figure in both places.
- exercises/solutions.md:432 — "natriumin raja-aallonpituus $544\,\text{nm}$ teoriassa" does not say where 544 comes from. It is $hc/W$ with $W = 2{,}28\,\text{eV}$: name that value.
- exercises/solutions.md:424 — $6{,}626 \cdot 10^{-34} \cdot 5{,}562 \cdot 10^{14} = 3{,}685 \cdot 10^{-19}\,\text{J}$, not $3{,}686$. The final $2{,}30\,\text{eV}$ is unchanged.
- lessons/FY8/fy8-1/answers.py:238 — the comment "3,7e-19..." is garbled. Write $3{,}685 \cdot 10^{-19}\,\text{J}$.

## Checked
- Hash c55461f4fa2a8ea8 at the start and the end. Only fy8-1-L2-10 was judged.
- Recomputed: $f_0 = c/539\,\text{nm} = 5{,}562 \cdot 10^{14}\,\text{Hz}$ and $hf_0 = 2{,}3006\,\text{eV}$. answers.py also gives 2,30055. The box value 2,3 eV is correct, and $hc/W = 539{,}1\,\text{nm}$ for $W = 2{,}3\,\text{eV}$.
- Tolerance 0,05 (relative) accepts 2,185–2,415 eV. Readings of 530–550 nm give 2,254–2,340 eV, so they are all accepted, as the solution says.
- Attribution matches the verified lines: the metal list, sodium 2,3 eV, zinc 4,3 eV and platinum 6,3 eV in the sim's model, the wavelength and intensity sliders, no frequency control, the energy graph, and that it runs in the browser. Nothing beyond those lines is attributed to PhET.
- Physics: $hf_0 = W$ at the threshold. Intensity changes the current but not $E_\text{k,max}$, and $E_\text{k,max} = hf - W$ grows with frequency. The d) model answer contrasts the wave model with the photon model correctly. Scope is FY8 fy8-1.
- Vastaus's first paragraph holds 2,3 eV. Two significant figures are justified by the slider reading.
