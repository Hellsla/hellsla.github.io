VERDICT: PASS
CONTENT-HASH: d42131f792a90753

## Blocking
- none

## Polish
- none

## Checked
Delta review of commit 79af52c4 vs the passed version. Only inquiry.json exp-1 and exp-2 changed: an identity `values` map (isoterminen->isoterminen, isobaarinen->isobaarinen). Initial values, locked parameters, varied parameter, measured keys and min are untouched, so each experiment still isolates its varied parameter (exp-1 locks mode and Tc, varies Vml; exp-2 locks mode, varies Tc at constant p). Only the display of the Initial-state line changes (tilanmuutos: isoterminen). No number, formula, answer or physics claim changed.
