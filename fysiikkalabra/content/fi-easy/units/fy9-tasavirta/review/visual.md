VERDICT: PASS
CONTENT-HASH: e8bf91a0dde33d19

Tämä on Selkeä suomi -käännöksen visuaalinen ja kielellinen katselmus. Esikatselu tehtiin komennolla `python3 scripts/build.py fy9-tasavirta`, ja tulos on preview/fi-easy/fy9-tasavirta.html. Sivu tarkistettiin Playwrightilla leveyksillä 390 px ja 1280 px. Kaikki details-elementit olivat auki (vihjeet, ratkaisut, mallivastaukset, pisteytykset).

Tulokset:
- Vaakavieritystä ei ole (scrollWidth = 390 / 1280). KaTeX-virheitä, renderöimätöntä LaTeXia ja konsolivirheitä ei ole.
- Kaikki 7 kuvaa piirtyvät: hero, käsitekartta, mökin kytkentä, $(I, U)$-kaavakuva ja ratkaisujen kaksi kuvaajaa. Leveydellä 390 px kuvat ovat 298–358 px leveitä, ja kuvakaappausten perusteella tekstit ovat luettavia.
- Kuvien tekstit ja kuvaukset ovat selkosuomea. figures.json sisältää 26 avainta, ja kaikki on täytetty. Niistä 20 on lyhyitä nimiöitä, jotka on tarkoituksella pidetty samoina.
- Kuvissa on desimaalipilkku (4,63 V; 0,50 A; 6,3 A).
- Taulukot (langan mittaukset, paristokotelo, virherajat) mahtuvat 390 px:n leveyteen.
- Virtanuolet ovat violetteja kuten lähteessä. Voimia tai nopeuksia ei ole.
- LaTeX: suureet, yksiköt (`\text{}`), ohuet välit ja desimaalipilkku `{,}` ovat kunnossa kaikkialla. Luvut ja kaavat ovat samat kuin lähteessä.
- *Luvun tärkeät käsitteet* -komponentissa on kiinteä johdanto ja termit lihavoituina. Muistiinpanokenttiä ei ole.

## Blocking
Ei yhtään.

## Polish
1. unit.json `description` näkyy kurssisivulla, ja se on edelleen 40 sanan luettelo. Jaa se kahdeksi lyhyeksi lauseeksi (ks. pedagogy.md kohta 2).
2. figures.json, hero-kuvan kuvaus: ilmaus "lämpimän oranssi" on peräisin lähteestä. S2-lukijalle riittäisi "taivaanranta on oranssi".

## Shared issues
- Leveydellä 390 px sisällysluettelon viimeinen linkki (`toc-end`) jatkuu näkymän oikean reunan yli vaakavieritettävän navigaation sisällä. Sama näkyy lähdeversiossa, ja se tulee yhteisestä templatesta, ei tästä käännöksestä.
