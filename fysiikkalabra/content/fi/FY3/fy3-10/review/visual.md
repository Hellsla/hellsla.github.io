VERDICT: FAIL
CONTENT-HASH: 6835af91860ab87d

## Blocking
- [Major] lesson.md Ydinajatus, Kaava, Järkevyys (captures theory-1280-1/2, example-390-2) — numbers with units in prose are half plain text, half KaTeX, sometimes inside one expression: "1 Pa · m³ = 1 N/m² · m³ = 1 N · m = 1 J" (sans digits and "m³" with serif "1 J"), "0,2073 mol · 29 g/mol ≈ 6,0 g", "5,0/24 ≈ 0,21 mol", "0,207 mol" beside "0,83 g". Also plain "5,00 litran", "101 kPa:n", "24 litraa", "273,15". NOTES §1 (2026-10-28) puts every number with its unit in maths, and a written division takes a colon. Two typefaces in one chain read as sloppy and the chain breaks at "·" mid-line — fix: set each such chain and value as inline `$...$` (`$1\,\text{Pa} \cdot \text{m}^3 = 1\,\tfrac{\text{N}}{\text{m}^2} \cdot \text{m}^3 = 1\,\text{N} \cdot \text{m} = 1\,\text{J}$`, `$5{,}0\,\textsf{l} : 24\,\textsf{l/mol} \approx 0{,}21\,\text{mol}$`, `$0{,}207\,\text{mol}$` and so on).
- [Major] lesson.md Ydinajatus, "$N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}$" (capture theory-1280-1) — the Avogadro constant, the lesson's key number, splits across two lines after "·". Inline maths must stay on one line — fix: keep the constant unbreakable, e.g. `{6{,}022 \cdot 10^{23}}\,\text{1/mol}` inside one `\mbox`-free group, or reword so it does not fall at a line end.

## Polish
- [Minor] lesson.md Esimerkki, tulos paragraph — "Ainemäärän rajoittaa tilavuus 5,0 l ja massan lisäksi moolimassa 4,0 g/mol" is garbled; write "Ainemäärän tarkkuutta rajoittaa tilavuus $5{,}0\,\textsf{l}$, ja massan tarkkuutta rajoittaa lisäksi moolimassa $4{,}0\,\text{g/mol}$; kumpikin on annettu kahdella numerolla, joten tulokset annetaan kahdella merkitsevällä numerolla."
- [Minor] lesson.md Ydinajatus first paragraph — the 55-word opening sentence ("Kun 5,00 litran pallo täytetään … hyvin erilaiset: …") carries setup, caveat and four values; split after "vuorotellen" into situation and result.
- [Minor] figure 5 (scene, hot-air balloon) — nothing in the Tiivistelmä refers to it, so it decorates rather than teaches; add one summary line or an `aria-label` link to the idea (warm air, fewer particles per volume).
- [Minor] stage-tutki-390-1 — "noin ± / 0,02 g" breaks between ± and the number; bind with `\pm 0{,}02\,\text{g}` in one maths span.
- [Minor] sim-390 — canvas labels ("osumia/s", "osuma seinään", V = 100 %) are small (about 9 px) on a phone; the readout below carries the same values, so use only if cheap.

## Checked
- contact sheets skimmed; fig-1…fig-5 at 390 (hero, helium-ilma, mole-masses, paine-ja-tekijat, scene); particle counts equal in figs 2 and 3 verified in source
- top-390, intro-1280, theory-1280-1/2, example-390-1/2, sim-390, sim-1280
- stage-tutki-390-1/3/5, selita-390-2, sovella-390-1, exp-exp-1-390-1, stage-exercises-390, open-tarkista-1280-1
- not opened: theory-1280-3, other tutki/tarkista parts, exp-2

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
