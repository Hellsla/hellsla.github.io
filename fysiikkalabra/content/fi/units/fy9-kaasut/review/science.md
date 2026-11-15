VERDICT: PASS
CONTENT-HASH: 9723f5bee22920e2
Round 2 (fix round after queue 9c round 1): delta against the version round 1 reviewed (9d91dfe6c6c1bab9).

## Blocking
(none)

## Polish
- C: the 1st-law row still writes W without naming it the work done on the gas; the work row now says "työn suuruus" (magnitude) as the Kaava does, so the pair no longer contradicts the Kaava. "→ 1. pääsääntö, W kaasuun" would make the sign explicit.
- C: "syvyys nesteessä → p = ρgh" is the hydrostatic part (round 1, stands).

## Checked
- Round-1 Blocking fixed (fi: missing constant-pressure condition): row 7 is now "paine vakio, tilavuus muuttuu → työn suuruus, W = pΔV" (en "constant pressure, volume changes → magnitude of the work"), which is exactly the Kaava row (constant pressure, ΔV a magnitude, ΔU = Q + W with W done on the gas; on expansion W = −pΔV).
- aria-label: "työn suuruus on paine kertaa tilavuuden muutoksen suuruus" states the same physics as the pill.
- Rendered chart (360 px) shows the new row; other rows unchanged and correct as in round 1.
- teacher.md: "haara"/"branch" -> "rivi"/"row" only; no formula, number or physics changed.
- Hash taken at the start and the end (9723f5bee22920e2).
