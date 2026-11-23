VERDICT: PASS
CONTENT-HASH: fb46aec0512cf1e0
SCOPE: delta numbers,reflow,typography from 15261a26498e83ce base 4b05399

## Blocking

## Polish
- exercises/solutions.md:76 (L1-05) — "$E = hf$, josta:" is followed by $f = c/\lambda$, which does not follow from $E = hf$: it is the wave equation, a second basic law. The chain is right. Fix: "$E = hf$ ja $f = c/\lambda$, joten $E = hc/\lambda$ ja $\lambda = hc/E$".
- exercises/solutions.md:143 (L2-02) and :472 (L3-05) — the same "josta" problem. $I_2 = I_1(\tfrac12)^{\dots}$ and $T = (\tfrac12)^{d/d_{1/2}}$, $R = AT\eta$ are further relations, not consequences of the first row. Fix: write "ja" or "sekä" for the added laws.
- exercises/solutions.md:249 (L3-02) — the required net rate ($30\,\text{min}^{-1}$) is written as $R_\text{t}$ in $(\tfrac12)^{d/d_{1/2}} = R_\text{t}/(R_0 - R_\text{t})$. This is only correct because the requirement happens to equal the background. The text before 8g had the same issue. Fix: a symbol of its own, e.g. $R_\text{s}$.

## Checked
- The hash was fb46aec0512cf1e0 at the start and the end. Scope: delta on solutions.md only.
- The packet's diff view flattens the aligned blocks, so I read the Kaava blocks on disk. Each is a proper `aligned` block with one equation per row.
- A script compared the file with the pre-8g commit e16119cde8. Every changed line lies inside a Kaava step. No Annettu, Muunnokset, Sijoitus, Vastaus or Järkevyys line changed, and exercises.json and answers.py are unchanged.
- I checked each new derivation step. The ratio form $\tfrac{N_0 - N_\text{t}}{N - N_\text{t}} = 2^{d/d_{1/2}}$, its logarithm and $d_{1/2} = \tfrac{d \ln 2}{\ln(\dots)}$ are correct (L2-03, L2-06, L3-04). So are the equal-attenuation rearrangement (L2-04), the net rate (L2-01, L1-07), the two-shield product (L2-02), the activity $A = R/(T\eta)$ (L3-05) and $d = d_{1/2}\ln(R_0/R)/\ln 2$ (L3-07).
- Every Kaava now starts from the basic law and ends in the symbolic form that is substituted.
- I recomputed L1-05: $\lambda = hc/E = 98{,}4\,\text{nm}$ for $12{,}6\,\text{eV}$. L3-02 gives $d_{1/2} = 5{,}55\,\text{mm}$ and $d = 34{,}99\,\text{mm}$. Both are unchanged and agree with the solutions.
