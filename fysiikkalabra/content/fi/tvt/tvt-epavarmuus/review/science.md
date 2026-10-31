VERDICT: PASS
CONTENT-HASH: fd34db779eea2d90

## Blocking
- None.

## Polish
- Tapa 2, step 2: "Ohjelma laskee epävarmuuden siitä, kuinka paljon pisteet poikkeavat sovitetusta suorasta. Se ei tiedä mitään epävarmuusjanoista, joita et ole antanut ohjelmalle." ga-facts.md says not to claim which statistic is shown. The physics is that of any unweighted least-squares fit and the lesson (few points can give an unrealistically small value; compare with method 1) is sound, but "joita et ole antanut ohjelmalle" implies that entering error bars would change the value, which is not verified. Suggest: "Luku perustuu pisteiden hajontaan suoran ympärillä, ei epävarmuusjanoihin."
- Propagation: "tulon ja osamäärän suhteellinen epävarmuus on enintään suureiden suhteellisten epävarmuuksien summa" — add that a squared quantity counts twice (e.g. $T^2$), or "kun suureet ovat ensimmäisessä potenssissa" (guardrails B).
- Tapa 1 needs error bars, whose location is unverified (Pro, ask the teacher) — fine; optionally say the steepest/shallowest lines can also be judged against the scatter of the points when no error bars are shown.

## Checked
- Steepest/shallowest lines through (almost) all error bars; Δk = (k_max − k_min)/2; "rajaavat arvioidun vaihteluvälin, eivät varmoja rajoja" (guardrails wording).
- Numbers recomputed: Δk = 0,16 s^2/m; 0,16 : 4,05 = 0,0395 ≈ 4 %; g = 9,748 m/s^2; Δg ≈ 0,39 m/s^2; reported (9,7 ± 0,4) m/s^2 — rounding rule correct; k = 4,05 is the midpoint of 4,21 and 3,89; data labelled "keksitty esimerkkiaineisto".
- Δg/g = Δk/k for g = 4π^2/k correct; unit check of Δk vs Δg; systematic error (video scale) not caught by the fit; overlap ≠ equality wording.
- UI: Graph Options (lower left) > Add Manual Fit (Pro), handles, slope/intercept update, max three lines; Apply Curve Fit; "Show uncertainty of curve fit parameters" (Pro) with the prescribed hedge — all in ga-facts.md.
- Figure matches figures.py: extreme lines found by search really pass through every bar; best fit between them; labels LaTeX, leader lines, no overlaps.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Sarakkeen ominaisuudet**, **Näytä virhepalkit** (ga-sarakkeen-ominaisuudet.png), **Käyrän sovitus**, **Lineaarinen** (ga-kuvaajatyokalut.png, ga-kayran-sovitus.png). English: Add Manual Fit, Show uncertainty of curve fit parameters (both in ga-facts, both hedged with "kysy opettajalta").
- Method 2 wording is correct: the parameter uncertainty comes from the scatter about the line, not from the error bars, and can be unrealistically small for few points. The phrase "m:n vieressä" asserts a display position that ga-facts marks as unverified; harmless, but "tulosruudussa näkyy myös kulmakertoimen (ohjelman m) epävarmuus" would be safer (polish).
- Worked example unchanged and still right: 4π²/4,05 = 9,748; Δk/k = 0,0395; Δg ≈ 0,39 → (9,7 ± 0,4) m/s².
