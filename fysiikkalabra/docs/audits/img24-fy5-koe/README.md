# Työjono 24: FY5 koe ja Sovella, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla. Tiedosto
`<omistaja>_<nimi>_<kieli>_<leveys>.webp`: leveydet 360 px (2× tarkkuus) ja 1280 px; sticky-palkki ja valikko piilotettu.
5 kuvaa: koe (vain `fi`, kokeella ei ole käännöksiä) `fy5-k2-board`, `fy5-k2-fbd`, `fy5-k3-fbd`, `fy5-k5-modes`;
Sovella (`fi`, `en`, `fi-easy`) `fy5-s1-crane`. Yhteensä 4 × 2 + 3 × 2 = 14 kuvaa. WebP:t `assets/pics/fy5/` (pisin sivu enintään 1600 px),
rivit `lessons/FY5/ASETTELU.tsv`; merkinnät ovat edelleen `figures.py`:n LaTeX-`foreignObject`eja, piirroksia ei muutettu.

Esikatselukaappauksissa kuvat kopioitiin käsin `preview/pics/fy5/`-kansioon: `build.py` ei kopioi koe- eikä Sovella-sivun
kuvatiedostoja (jaettu korjaus, kerrottu koordinaattorille).

ASETTELU.tsv:n rivit ylittävät viewBoxin (yksikköä; 1 yksikkö ≈ 1 px 1280 px:n näkymässä). Kaikissa ylittävä kaista on tyhjää taustaa (0 % ei-taustaa):
| kuva | viewBox | rivi (x y l k) | ylitys |
|---|---|---|---|
| fy5-k2-board | 600 × 340 | 0 0 600 347,5 | ala 7,5 |
| fy5-k2-fbd | 600 × 440 | 1,2 1,2 597 441,5 | ala 2,7 |
| fy5-k3-fbd | 600 × 340 | 2,5 0 594,1 344,1 | ala 4,1 |
| fy5-k5-modes | 600 × 400 | −1,3 −1,3 603 407 | vasen 1,3, ylä 1,3, oikea 1,7, ala 5,7 |
| fy5-s1-crane | 600 × 350 | 0 0 597 354,5 | ala 4,5 |

Huomiot (`PAATOS.txt`):
- `fy5-k2-board`: vesi on uudessa kuvassa selvästi suurempi alue; mitat 4,0 m ja 1,2 m paikoillaan.
- `fy5-k2-fbd`: Codexin oma raportti: voimanuolten tarkat pituussuhteet eivät säilyneet. Kuvan `aria-label` ja mallivastaus sanovat "nuolten pituudet ovat mittakaavassa": opettajan katsottava.
- `fy5-k5-modes`: solmu-S-merkinnät osuvat pidikkeiden ja solmupisteiden päälle (alkup. kuvassa alapuolella); ei siirretty, opettajan katsottava.
