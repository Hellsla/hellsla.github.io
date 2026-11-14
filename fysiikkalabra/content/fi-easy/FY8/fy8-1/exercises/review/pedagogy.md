VERDICT: PASS
CONTENT-HASH: 660f444084d55575
SCOPE: delta added-exercise from 5e7e04fa3110d92d base 5a45b28682e8

## Blocking
(none)

## Polish
(none new; round-1 polish on L2-08 level and "Kaava" wording unchanged and optional)

## Checked
- L2-08 solution diff: Muunnokset now states frequencies are used in units of 10^14 Hz so the slope 0.4136 eV gives eV directly; the old line mixed units (eV per 10^14 Hz times a unitless-looking factor) and is repaired.
- Sijoitus 0.4136 * (12 - 5.56) = 2.66 eV is correct and consistent with the stated unit convention.
- Järkevyys no longer uses the work function (not readable in the task); compares the graph reading 2.7 eV to hf = 4.96 eV and notes 2.66 agrees: clearer, reading stays the primary route.
- Reading step, answer (2.7 eV, tolerance) and L1-10, L2-09 untouched; earlier PASS stands.
- Method: text diff only.
