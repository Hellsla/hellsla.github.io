VERDICT: PASS
CONTENT-HASH: 0b078ca45bfb00c4

## Blocking

## Polish
- lesson.md:587 (Worked example, Result) — "three significant figures like the intensity 840 W/m²" names only the intensity; the angle 35° has two significant figures (carried over from the passed fi; same polish as the fi review). — Fix: add "the angle 35° is taken as exact".

## Checked
- Translation fidelity against the passed fi version: inquiry.json, exit-ticket.json and lesson.md have the same structure, the same correct flags, the same experiment initial/locked/vary/measure keys, and the same numbers in every string (decimal point only). All eight inline figures are geometrically identical to fi; only the label text differs.
- One script recomputed every number from the task text: Malus 0.75/0.50/0.25; Brewster 53.1°/36.9°/56.3°; worked example 281.8 → 282 W/m² (a third of 840); ennuste values 46.7/37.5/12.5 % and the linear 33.3 %; koe-1 37.5 % with mistakes 75/43.3/33.3; koe-2 12.5 %; virhe 25 W/m²; siirto 2.128 m with mistakes 1.203/1.279; tarkistus-2 2.066 mW with mistakes 3.214/1.033/2.934; exit ticket 56.3°.
- mittaus: least-squares fit A = 360.72 lx, B = 14.64 lx, ΔA = 2.37 lx, matching the text (360.7, 14.6, 2.4); the fig-5 capture shows the points and the line to scale; badged `example`.
- English physics wording correct: direction of polarisation = E-field direction; the film's chains absorb the component along them; unpolarised light halved by the even split; I ∝ amplitude²; reflected glare polarised parallel to the surface and perpendicular to the plane of incidence; n₁ is the medium of incidence and reflection; Malus's conditions (ideal polariser, polarised light) stated.
- Each choice item has exactly one correct option; every distractor's English feedback names the real error.
- Sim strings (lang/en.json sims.fy7-15) translate the readout faithfully; the koe-1 capture shows English labels, I₁ = 50.0 %, cos² = 1.000 at 0°, and the model box states ideal polarisers and model values.
- No Finnish words visible: experiment names, values, measure labels and figure labels are English.
