VERDICT: PASS
CONTENT-HASH: be5a20d4c273629f
Mode: full
Round: 1

## Blocking

## Polish
- [Minor] Taulukon sarakeotsikot (Rata, Kaartuu, Kohta) ovat lyhyitä; ei muutettavaa.

## Checked
- Avattu fi-easy-kuvakaappaus open-exercises-L3-1280-6 (L3-04 ratkaisu): kaavat, desimaalipilkku, yksiköt pystyssä, ei leikkautumista, ei vaakasuuntaista ylivuotoa.
- Uusien tehtävien tekstit, taulukot ja kuvatekstit luettu käännöksestä; selitykset sulkeissa (liike-energia, klassinen käsittely) näkyvät luettavasti.
- Ei englantia tai muuta vierasta kieltä sivulla.
- check_i18n.py fi-easy: 0 errors.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4

## Follow-up (be5a20d4c273629f: four solutions.md edits on top of the hash above)
- After `python scripts/build.py fy7-2 --exercises`, Playwright on the preview page with every exercise level and solution open, at 360 and 390 px: every inline `.katex` of L1-02 Annettu and Kaava (and L2-03, L3-02) has `getClientRects().length == 1`. The grouped ${|q| = e = …\,\text{C}}$ is 213 px in a 274 px (360) / 304 px (390) column; $|q|vB = \dfrac{mv^2}{r}$ 118 px, $r = \dfrac{mv}{|q|B}$ 80 px. No horizontal overflow.
- Absolute-value bars, upright units and the decimal comma render cleanly; the chapter titles stay italic.
- No blocking issue.
