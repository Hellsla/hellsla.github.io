VERDICT: FAIL
CONTENT-HASH: 014855b802fc608b

## Blocking
- lesson.md:420 (Esimerkki, Tulos) — **A** (guardrail "Values and significant figures", P7). The question asks how much the joint must give way *at least* ("kuinka paljon liikuntasauman on vähintään annettava periksi"), so the answer is a limit value. It must be rounded to the safe side, up: $86{,}4\,\text{mm}$ → $87\,\text{mm}$ with two figures. The text rounds it down to "noin $86\,\text{mm}$". — Fix: state the change as $\Delta l \approx 86\,\text{mm}$ and the joint's minimum as $87\,\text{mm}$, giving the reason (a "vähintään" value is rounded up). Alternatively, drop "vähintään" from the question so it asks only for the change in length.

## Polish
- inquiry.json johtopaatos.model — "$\Delta l = 6{,}0\,\text{mm}$" next to "$12{,}0\,\text{mm}$". The sim and the predictions say $6{,}00\,\text{mm}$. — Write $6{,}00\,\text{mm}$.
- inquiry.json pred-3 (Bea feedback) and simulaatio.model say "Teoriatiivistelmä". The stage is now Teoria. — Write "Teoria" (the build renames it only in headings).
- lesson.md:286, inquiry.json olomuodot/check-3 — The gas's larger expansion is put down only to weak interactions ("lähes vapaita"). The actual mechanism is that faster particles push harder on the surroundings, so at constant outside pressure the volume grows; that gives γ ≈ 1/T. The level makes this acceptable (C). — Consider half a sentence on pressure in the theory paragraph.
- lesson.md:427 — "jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta": the order of freezing comes from the 4 °C density maximum, as line 288 says. Ice expanding explains only why the ice stays on top. — Separate the two causes.

## Checked
- One script recomputed every number from the task data with my own formulas: example $86{,}4\,\text{mm}$, $0{,}072\,\%$; pred-1/pred-2 $6{,}00$/$12{,}0\,\text{mm}$, $0{,}0600\,\%$; olomuodot $0{,}36$, $2{,}1$, $11$, $34\,\text{cm}^3$; virhe $28$ vs $1{,}8\,\text{mm}$ (×15, 0,7 %); siirto $44\,\text{mm}$, mistakes $0{,}044$ and $110$, glass ratio 41, $43\,\text{mm}$ with glass; check-2 $23 \cdot 10^{-6}$, mistakes 46 and 15,3; exit ticket $21\,\text{mm}$; air/steel ≈ 94 ("noin sata"). All agree.
- Micro-model: anharmonic asymmetry correct; the misconception about particles growing is corrected in theory, pred-3, olomuodot and check-3.
- γ ≈ 3α derivation; validity limits (about 100 K for solids, a liquid's γ near 20 °C) stated where the formulas are used.
- Water anomaly, holes growing, shrink fit, bimetal strip, sagging power lines: physically right.
- Each prediction has exactly one correct option, and every distractor's feedback is correct.
- sim.js implements ΔL = αL₀ΔT with ΔT from 20 °C. The ×100 exaggeration is labelled, and the "under 0,3 %" claim holds (max 0,23 %). The model box says honestly that the spacing is set from the formula and the vibration is drawn symmetric.
- exp-1/exp-2: material and L0 (or T) locked, one variable varied; simState gives dT, dL and rel.
- Figures: particles (d > d₀, same size), rod and flask are marked exaggerated, and their labels are consistent.
- Units, $1/\text{K}$ = $1/{}^\circ\text{C}$ reasoning, and ΔT in K throughout.
