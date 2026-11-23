VERDICT: PASS
CONTENT-HASH: 870b888366bc5011
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography from fb8bc2ae3ac4c6db base b5600a6
Delta review of the Kaava steps rewritten to start from the basic equations (queue 8g) and of the model answers split into paragraphs. Categories and base come from `reviews.py` scope for science.

## Blocking

## Polish

## Checked
- The hash was 870b888366bc5011 at the start and at the end. The packet's diff shows the aligned blocks flattened, so I read the Kaava lines on disk (solutions.md:46–116, :189, :226, :252). They are proper `aligned` blocks.
- Energy chains: $\Delta E_\text{k} + \Delta E_\text{p} = 0$ with $\Delta E_\text{p} = e(V_2 - V_1)$ for the proton moving from 4,0 cm to 1,0 cm has the right sign and gives +150 eV. $E_{\text{k},A} + E_{\text{p},A} = E_{\text{k},B} + E_{\text{p},B}$ with $E_\text{p} = -eV$ is right for the electron.
- $E_\text{k} = W = qU$ is used only for particles starting from rest, which each task and principle states. It agrees with the brief's $\tfrac12 mv^2 = \lvert q \rvert U$.
- Turning point: $E_{\text{k},0} = eV = eUx : d$ with $V = Ex$ measured from the negative plate, then $d - x$. The physics and algebra are right.
- Deflection: $a = eU_\text{p} : (md)$ and $t = L : v$ with $v^2 = 2eU_\text{k} : m$ give $y = U_\text{p}L^2 : (4dU_\text{k})$. The derivation is right and the mass cancels.
- $V_P = Ex$ with $E = U : d$, and $E_\text{p} = -eV_P$: the notation follows the brief ($V$, $E_\text{p}$, $W_{AB}$, $U = Ed$).
- The paragraph splits (L2 model answers, L3 parts a–c) keep every sentence and number unchanged.
- I recomputed in one script: 150 eV; −75 eV; −120 eV; 4,39·10⁵ m/s; 284 V; 6,80·10⁶ m/s; 42,9; 4,34 mm; m₁ = 6,77·10⁻²⁷ kg; 2,52·10⁷ m/s; 2,78 mm; 8,39·10⁶ m/s. All agree with the solutions.
- No answer, tolerance or task text changed apart from the caption marker (caption-label).
