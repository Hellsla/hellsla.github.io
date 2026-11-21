VERDICT: PASS
CONTENT-HASH: 21fd7ab556f66cbc

## Blocking

## Polish
- lesson.md:161 — the question says "lähes levossa" and then asks "Miksi vesi ei liiku?"; "Miksi vesi liikkuu niin vähän?" or "Miksi vesi on lähes paikallaan?" would match the corrected claim exactly. Not blocking: the answer gives the condition and the "lähes".
- lesson.md:161 — the block's answer is still the same as check tarkistus-1's ("harja kohtaa aina pohjan"); the paragraph just before gives it already, so nothing new is given away.

## Checked
- Round-1 Blocking fixed: the nodal-line block (l. 160–164) now says "lähes levossa" and "Kun aallot ovat yhtä suuret, poikkeamien summa on koko ajan lähes nolla". This agrees with l. 137, the summary (l. 327), the glossary (solmuviiva) and tarkistus-1. The residual is real: circular waves weaken with distance, e.g. about 16 % at r = 3,00 m vs 4,25 m with A ∝ 1/√r (computed).
- Block l. 126: y = 3,0 cm + (−2,0 cm) = 1,0 cm ylöspäin (recomputed); the reason given ("eivät ole yhtä suuret") is right.
- Block l. 233: energy redistributed, not destroyed; agrees with the sentence before it and the guardrails.
- Worked-example stage split (l. 182–184): numbers unchanged; λ = v/f = 0,500 m, Δs = 1,25 m, Δs/λ = 2,5 → heikentävä (recomputed).
- inquiry.json `learn`: Fourier goal marked "(valinnainen)", matching the slot's täsmennys ("valinnaisena").
- New model picture (teacher-approved figure, not a pysahdy block): source spacing ≈ 3 ring spacings, three nodal lines each side, as d = 3λ gives (Δs = 0,5λ, 1,5λ, 2,5λ). Caption agrees.
- Placement: each block follows the paragraph it draws on.
- Hash at start and end: 21fd7ab556f66cbc.

## Vanhan sisällön löydökset
- lesson.md:137 — "Vesi on levossa kokonaisina viivoina" right after "lähes levossa" (inconsistent; the sim's howto "vesi pysyy levossa" is the same).
- lesson.md:199 — "piste pysyy levossa" for equal amplitudes (summary says "lähes levossa").
- Deterministic checks: `inquiry` FAIL (not caused by the new blocks; not investigated).
