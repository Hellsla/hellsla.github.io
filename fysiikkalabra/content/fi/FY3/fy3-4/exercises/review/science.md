VERDICT: PASS
CONTENT-HASH: 7aab3f782db93840

## Blocking

## Polish
- exercises/solutions.md:217 and exercises.json:137 (L1-09) — inline chains render at 406 px and 362 px on one line at 390 px width (Playwright on preview, solution and feedback opened; column 330 px), past the ~300 px limit. Not physics: split, e.g. "$\Delta p = \rho g h$" then "$\Delta p = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 1000\,\text{m}$" then "$\Delta p = 9{,}81 \cdot 10^{6}\,\text{Pa}$"; feedback: "$\rho g h \approx 9{,}8 \cdot 10^{6}\,\text{Pa}$". For the visual reviewer.
- exercises.json (L1-09, 10⁶ feedback) — "kilometri on muunnettu metreiksi kymmenen kertaa liian pieneksi" is a contrived route to 10⁶ Pa; physics right, optional.

## Checked
- L1-09 recomputed: $\rho g h = 1000 \cdot 9{,}81 \cdot 1000 = 9{,}81 \cdot 10^{6}\,\text{Pa}$; $\log_{10} = 6{,}99$, so 10⁷ Pa is nearest linearly and logarithmically; 100 m → 9,8·10⁵, 10 km → 9,8·10⁷ (feedback right). Sea water 1025 kg/m³ would still give 10⁷; the task states ρ = 1000 kg/m³ as an assumption.
- Asks the hydrostatic (over)pressure, so adding $p_0$ does not change the order; 10⁵ distractor links to the lesson's air-pressure point.
- Exactly one correct option; options are bare powers of ten, form-neutral.
- $\Delta p = \rho g h$ notation as in the brief; in scope.
- Rest of the set unchanged since PASS; hash same at start and end.
