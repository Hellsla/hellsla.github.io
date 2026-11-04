VERDICT: PASS
CONTENT-HASH: 321eee9838d818f2

Round 2 (delta review of round 1 fixes; round 1 hash c908c7c1c4a5b48e)

## Blocking
(none in round 1, none now)

## Round 1 polish — verified
1. melting-curve label size: shared catalog figure, left under Shared issues (developer.md). Accepted.
2. Flat sub-heading hierarchy: template CSS, under Shared issues. Accepted.
3. Plain units: fixed; preview text has no plain "(K)", "(kg)", "(°C)", "(1/K)".
4. Desktop column: house layout.
5. kayra labels 14 px: at the brief's minimum, accepted.

## Changed text checked in the preview
s5 b Vastaus (mug estimate, 1890 J : 25,7 K ≈ 70 J/K renders correctly at 390), s1 water-layer wording, "vakiopaineessa", Miksi question, exit ticket item 2, aineisto solution. Finnish is fine.

## Checked
python3 scripts/build.py fy9-lampo; Playwright at 390 and 1280 with all details open: scrollWidth 390/1280 (no horizontal overflow), 0 .katex-error, no raw $, no console errors.

## Shared issues
- fy3-7/melting-curve labels ≈ 13 px at 390 px.
- Template: ### under ## Kaava should be visibly smaller.
