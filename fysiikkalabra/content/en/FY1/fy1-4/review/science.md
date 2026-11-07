VERDICT: PASS
CONTENT-HASH: cefe1060a1ac8c88
Mode: light (teacher 2026-11-07, "kevyt katselmointi": style-suggestion diff since origin/main only)

## Blocking
- none

## Polish
- Koe 2 / Ennuste 2 feedback for the 78,5 g option: the one-point extrapolation 78,5 g − 16 g ≈ 63 g (62,5 g) differs slightly from the ~61 g best constant term stated in the correct option's feedback (with k locked at 0,80 g/ml the best b is 117,3 − 56 = 61,3 g). Not introduced by this change (previously 63 g as well) and the feedback's point stands; optional: "noin 62–63 g, lähellä parhaan suoran arvoa 61 g".

## Checked
- inquiry.json: slope 0,80 g/ml now matches the locked k of Koe 2 (LSQ slope of the data is 0,787, so 0,79 and 0,80 are both fair); 20 ml · 0,80 g/ml = 16 g, 78,5 − 16 ≈ 63 g recomputed
- "kuvaa kärryn tasaista liikettä" matches data set 1 (kärry radalla); "sovitetaan suora eikä yhdistetä murtoviivaksi" correct
- one-point s : t feedback ("each value is off by its own point's error") correct; units now upright ($\text{km/h}$, $\text{s/m}$), solution notation $s\ (\text{km})$
- lesson.md: "poikkeamat suunnilleen kumoavat toisensa", "kauempana suorasta": both improve accuracy; table headers $t\ (\text{min})$, $T\ (^\circ\text{C})$ fine
- lang sims.fy1-4: no change; no figures.py or sim change
- en: same changes as fi, meaning preserved
