VERDICT: PASS
CONTENT-HASH: ad20b72d0247f55a

## Blocking

## Polish
- lesson.md:125 (Partial reflection) — "the surface of a lake mirrors the trees on the shore in the evening" carries over the Finnish "iltaisin": the cause is the grazing view across the lake (large angle of incidence) with the bright shore against the dark water, not the time of day. Fix: "when you look at it at a grazing angle far across the lake" (C if left; same polish as the fi review).

## Checked
- Translation fidelity: every string of inquiry.json, exit-ticket.json and lesson.md checked against the passed fi version. Same structure, same correct flags, same experiment initial/locked/vary/measure keys, and the same numbers in every string (decimal point only). The six figures differ from fi only in the label text and label box widths.
- One script recomputed everything from the task text: the example 38.02° and 2.256·10⁸ m/s; ennuste-1 28.9°; ennuste-2 22.1° → 40.6° (×1.84, not 44.2°), maximum 48.8°/24.4°; angle ratios 1.36/1.48; koe-2 35.2/30.9/30.3/18.5° with n₂ sin α₂ = 0.766; virhe 0.651 → 40.6°; siirto 41.68° (25.94°, mistakes 22.08 and 39.9); tarkistus-2 1.470 (0.680; 1.592); nopeus 2.013 (4.47); exit ticket 25°/50° and 1.33; R at normal incidence 2.0 %/4.3 %.
- mittaus: least-squares fit gives A = 1.4895, ΔA = 0.0162, B = −0.0041; the line passes (0.60; 0.89); mistakes 0.671 = 1 : A and 1.79 = 70 : 39; single-row ratios 1.42 and 1.49.
- English physics wording correct: angles from the normal, "optically denser/less dense", frequency set by the source and unchanged, λ 1.33 times shorter, wavefront turning as the cause, reversibility, apparent depth with the oblique view and sideways shift, n > 1 for transparent materials in visible light.
- Each choice item has exactly one correct option; every distractor's English feedback names the real error.
- Sim strings (lang/en.json sims.fy7-10) translate the readout faithfully, including the total-reflection line; the koe-1 capture shows English labels, α₂ = 0.0° at 0° and R = 2.0 %; the graph capture shows the 48.8°/24.4° end points.
- Model box states yellow light, flat smooth boundary, no absorption, unpolarised Fresnel R, and calls the readings model values.
