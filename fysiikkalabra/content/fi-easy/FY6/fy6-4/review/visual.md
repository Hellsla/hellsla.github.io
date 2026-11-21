VERDICT: PASS
CONTENT-HASH: 5dd76c8d5bd2d97a

## Blocking
(none)

## Polish
- [Minor] Vastaus, rinnankytkennän laskuesimerkki: \tfrac-murtoluvun yksiköt ovat pieniä 360 px:llä, mutta luettavissa.

## Checked
batch delta review (round 2, scope: Pysähdy ja mieti -laatikot): pakettikaappaukset eivät sisällä laatikoita, joten renderöin sivun (build.py → preview/fi-easy/fy6-4.html) Chromiumilla 360 px:llä, avasin kaikki aside.stop-think-vastaukset ja mittasin: 3 laatikkoa, ei leikkautumista, ei vaakavieritystä, ei KaTeX-virheitä; avasin kuvakaappaukset laatikoista (yksiköt, desimaalipilkku {,}, \cdot, kaksoispisteet kunnossa). Sisältö hash-vaihto vain fy6-10 ja fy6-13 (yksi vastauslause muutettu kesken, ulkoasuun vaikuttamaton).
