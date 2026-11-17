VERDICT: PASS
CONTENT-HASH: ec86a73cd1b31a70

## Blocking

## Polish
- solutions.md:303 (L2-09): the solution says the curve at $A = 100$ "is on the grid line 8.7 MeV". The plotted curve (`semf(100)`) is at 8.684 MeV, just under the line, and at $A = 200$ it is at 7.916 MeV. The readings 8.7 and 7.9 are right to the 0.1 MeV grid. Write "at about 8.7 MeV" so that a student who reads 8.6 or 8.7 is not told the curve sits exactly on a line.
- L2-09: reading from the curve itself gives $Q = 200(8.684 - 7.916)\,\text{MeV} = 154\,\text{MeV}$. Readings one grid step apart give 140–180 MeV. The stored value 160 with a 15 % tolerance (136–184) covers this, and the solution already gives an uncertainty of $\pm 20\,\text{MeV}$. No change is needed.

## Checked
- Hash at start and end: ec86a73cd1b31a70.
- All 19 stored answers compared with the output of answers.py. Each is within its tolerance; the largest difference is 0.57 % (L3-01). The two new entries are L2-09 (160 vs 160.0) and L3-06 (50 vs 49.83).
- L2-09 physics: nucleon number is conserved, and the energy released is the increase in total binding energy, $Q = A(\varepsilon_{100} - \varepsilon_{200})$. Solved symbolically before substitution. The sign and magnitude are right, and the task says the graph should be assumed to describe the hypothetical nuclei.
- L2-09 reasonableness check, recomputed from the curve: from $A = 236$ to $A = 118$ the increase is $8.560 - 7.638 = 0.92\,\text{MeV}$, and $\times 236 \approx 217\,\text{MeV}$. "About 0.9 MeV, ≈210 MeV" is right, and so is "a lighter nucleus releases a little less".
- L2-09 figure: the y range 7.0–9.0 on a 0.1 MeV grid and vertical lines every 10 give every reading the task needs. The description gives the grid without giving the answer away.
- L3-06 figure (fy8-9/aktiivisuus): $A_0 = 720$ kBq (point marked), $T = 5.0$ h, so 360 kBq at 5 h and 180 kBq at 10 h, as the solution's check says. At 20 h the activity is $720/16 = 45$ kBq, which is right.
- L3-06: $t = T\log_2(A_0/A) = 5.0\,\text{h}\cdot 9.966 = 49.83\,\text{h}$, which rounds to 50 h with two significant figures (justified by the half-life read as 5.0 h). The extrapolation beyond the figure is stated in the task and justified in the solution, as the guardrail on fits requires. The 0.1 % safety threshold is stated as an assumption, and the values are labelled as example values.
- L3-06 comparison with Pu-239: $24\,100\,\text{a}\cdot 9.966 = 240\,000\,\text{a}$, which matches L3-03.
- answers.py: the new lines compute the same model from the readings the task asks for, and the units (MeV, h) and tolerances fit the reading precision.
- The removal of "example data" from the L2-05 and L3-04 captions changes no number.
- Scope: binding energy per nucleon and the decay law are within the FY8 central contents and scope notes.
