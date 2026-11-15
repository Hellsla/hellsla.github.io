VERDICT: PASS
CONTENT-HASH: 21e37c420884aec3

## Blocking

## Polish
- fy6-k7 a, rubric `units_precision` detail still says "$W \approx 10\,\text{kWh}$". The solution now says "noin $10{,}2\,\text{kWh}$", which is right for the data's three significant figures, and the answer check (10,24, tolerance 2 %) would reject 10. Make the detail say $10{,}2\,\text{kWh}$ (category 6, consistency).
- fy6-k7 d, Vastaus: "Sisäenergiaksi muuttuu satoja kilowatteja, joten jakoavain ja navat kuumenevat". With the wrench's resistance taken as ≈ 0, almost all of the $EI_\text{k} \approx 330\,\text{kW}$ goes into the cells' internal resistance. The wrench and the contacts heat because even their small resistance at kiloampere currents takes kilowatts. The hazards listed are right; only the "joten" link is loose.
- fy6-k1 b, Perustelu: says that only the battery's internal resistance and the wires limit the current, but the intro sets internal resistance as negligible. Name the ammeter's own small resistance too.

## Checked
- Full review, round 1. Hash 21e37c420884aec3 at the start and the end.
- One script recomputed every number from the task data with my own formulas, beside answers.py; all agree. Spot values:
  - k2: 17,99 Ω; 188,6 mA and 2,61 V.
  - k3: ΔI 0,84 mA; 40 / 80 %.
  - k4: 4,02·10⁴ m/s; 0,207 kg per day; 1936 W.
  - k5: 255 / 411 / 542 s.
  - k6: 25,0 nC; 12 % short at 3 cm.
  - k7: 10,24 kWh; 114 W; 6400 A; 391 A, 610 W, 76 W.
- Osa 1: exactly one option is correct in each item, and each distractor and its reasoning is right.
- Causality is right throughout: the hot filament, the grid spacing dropping out (Fd = eU), constant-power discharge (ΔU/Δt = I/C), charge redistribution on the conducting spheres.
- The 2026-11-15 wording changes are physically correct.
- Scope is within FY6.
- The figures' numbers match the data.
- practice.py check OK.
