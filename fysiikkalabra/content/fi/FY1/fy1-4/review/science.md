VERDICT: PASS
CONTENT-HASH: f5b4bdd7b0b1cd9b

## Blocking

## Polish
- Outlier answer: 'ennen kuin pistettä jätetään pois' reads as if exclusion follows; the guardrail wording adds that exclusion is justified and documented.
- Interpolation prompt: 'Jännitettä mitattiin välillä x = 2…10' mixes the measured quantity and the horizontal variable; e.g. 'Mittaukset tehtiin välillä x = 2…10'.

## Checked
batch delta review: three new pysahdy blocks (outlier not removed automatically; x = 6 interpolation vs x = 30 extrapolation; slope (2,0 s; 3,0 m)-(6,0 s; 11,0 m) = 2,0 m/s recomputed, read from the fitted line) and the knowns/question split.
