VERDICT: PASS
CONTENT-HASH: fd34db779eea2d90

## Blocking

None.

## Polish

- Tapa 1 step 1 depends on error bars, whose GA Pro path is unverified ("kysy opettajalta"). Acceptable now; add the path once Lauri confirms it (same as tvt-kuvaaja step 5). Until then the student can still drag the manual lines through the points' plausible range.
- Tapa 1 step 2: "Valitse kuvaajan vasemman alakulman valikosta **Graph Options** kohta **Add Manual Fit**" is a little heavy; e.g. "Avaa kuvaajan vasemmasta alakulmasta valikko **Graph Options** ja valitse **Add Manual Fit** kahdesti."
- Note for the student that GA Pro's **Graph Tools** (fits, Tangent) and the lower-left **Graph Options** menu are different menus; the names are close and the guides use both.
- Checklist line 1 "Tiedät, kummalla tavalla…" is weak; "Kulmakertoimen epävarmuus $\Delta k$ on arvioitu, ja tapa on kirjattu raporttiin" checks goal 1 directly.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Menu names (Graph Options, Add Manual Fit, Apply Curve Fit, Show uncertainty of curve fit parameters) used as the verified facts allow; the parameter-uncertainty wording stays within "parametrin epävarmuus" and says to ask the teacher if the setting is not found.
- Two methods are clearly separated, each with what to click and why; Tapa 2 explains what the program's number does not know (error bars, systematic errors).
- Goals (estimate Δk; propagate; report rounded) match the three blocks; checklist covers each.
- Worked example labelled "Keksityssä esimerkkiaineistossa"; numbers consistent with tvt-kulmakerroin (k = 4,05 s²/m, g ≈ 9,748 → (9,7 ± 0,4) m/s²), unrounded intermediates, units throughout.
- Mistakes are real ones (lines missing the bars, too many digits, mismatched rounding, Δk reported as Δg, small uncertainty mistaken for correctness). Figure shows steepest/shallowest lines through the bars, no numbers.
- Cross-links to suoran-sovitus, kulmakerroin, kuvaaja sensible. No spreadsheet/Excel/Tracker leftovers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- No screenshot in this guide (not needed); guides.py check: ok. Rendered preview checked: no leftover markdown or {{ga:}} markers.
- Method 1 step 1 now gives the real path (••• → Sarakkeen ominaisuudet → Näytä virhepalkit). Polish: after ticking the box the student still has to enter the size of Δy; one clause ("ja anna epävarmuuden suuruus") would close the step. Not verified where it is typed, so keep it generic.
- Add Manual Fit step is honestly hedged ("voi löytyä…, vieritä…, kysy opettajalta"); the menu in the screenshot does scroll, so the hint is plausible. No screenshot in this guide; none needed.
