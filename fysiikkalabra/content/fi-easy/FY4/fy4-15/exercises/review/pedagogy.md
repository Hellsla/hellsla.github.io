VERDICT: PASS
CONTENT-HASH: 775b15e10f821e0e
SCOPE: delta numbers from a6c04be5fc42821b base cabadc3e6179

## Blocking
None.

## Polish
1. exercises/solutions.md (all hydro Kaava) — $P_\text{o}$ is used without a name; add once "missä $P_\text{o}$ on veden luovuttama teho ja $P$ sähköteho" so the symbol is explained where it first appears.
2. exercises/solutions.md (all wind Kaava) — "$m = \rho A v t$" is the key step but gets no reason; add "Aika $t$ kuluessa ilmaa kulkee matkan $vt$ pinta-alan $A$ läpi, joten tilavuus on $Avt$ ja massa $\rho A v t$."
3. exercises/solutions.md (L3 power-ratio tasks) — the long repeated chain buries the one new step ("joten $x = ...$"); start the new step on its own sentence: "Kun $\eta$, $\rho$ ja $A$ pysyvät samoina, tehojen suhde on …".

## Checked
- Rewrite only: every Kaava now starts from E_p = mgh or E_k = ½mv², the mass per time (ρQt or ρAvt), the power as energy per time, and η = P/P_o, simplifies symbolically (ρQgh, ½ρAv³), then gives the asked formula; no number, answer or id changed.
- Efficiency step is explicit: P = ηP_o, so students see where η enters instead of being handed P = ηρQgh.
- Simplification to the end before substitution holds (t cancels in the chain), consistent with the house rule.
- Opened fy4-15-open-exercises-1280-1.png: the Kaava chain renders as aligned rows, nothing clipped; the capture predates this edit, so the longer chains were not seen at 360 px (the packet lists no 360 px capture; the developer's open-solution layout check covers it).
- Paragraph splits in Mallivastaus items and the multiple-choice explanation are line breaks only; the four alternatives now each have their own paragraph, easier to read.
- Caption marker esimerkkiaineisto removal is an approved wording change.
- Hash the same at start and end.
