VERDICT: PASS
CONTENT-HASH: 8d5dcc7a85927ad4

## Blocking

## Polish
- lessons/FY6/fy6-12/lesson-answers.py:5 — "Gravity ... in the sim's weakest field it is at least about 10^-10 of the electric force" has the bound the wrong way round. The weakest case (alpha, 1000 V/m) gives weight : electric force ≈ 2·10⁻¹⁰, so gravity is *at most* about 2·10⁻¹⁰ of the electric force. Comment only. — fix: "at most about 2·10^-10".

## Checked
- Round 2. I reviewed the diff from commit f3bb2adf and re-checked the full packet.
- Round-1 blocker resolved: inquiry.json simulaatio.model now says "vähintään miljardeja kertoja pienempi". The lowest ratio is the alpha in 1000 V/m: 4,9·10⁹, which is "miljardeja" and true. lesson-answers.py now computes the alpha case and asserts > 10⁹; I ran it.
- siirto Järkevyys: "vaikka energiat ovat samaa suuruusluokkaa" (1,2 keV vs 3,0 keV) is correct.
- Yleinen virhekäsitys: "suuremmalla levyjen välimatkalla ... E = U : d" is unchanged in substance.
- Stale retrieval block removed; the comment now matches the qualitative kertaus item.
- Every round-1 number re-verified unchanged: example 3,248·10⁷ m/s; 500 eV proton 309 km/s and electron 13 262 km/s; ion 42,0 km/s; tarkistus-2 300 eV; virhe −4,8·10⁻¹⁷ J; exit −50 eV and 4,8·10⁻¹⁶ J.
- No new physics errors in the changed lines. Colours, symbols (E_p, E_k) and constants follow the FY6 rules.
