VERDICT: PASS
CONTENT-HASH: 90ffa68a637fc5ce

## Blocking
(none)

## Polish
- inquiry.json `reaktiot` — puhelimella (stage-tutki-390-2) reaktiotaulukon yhtälöt katkeavat keskeltä riviä ($n \to p +$ / $e^- + \bar{\nu}_e$), ja opiskelijan pitää laskea seitsemän reaktiota kolmella luvulla päässä. Fix: anna reaktiot omina riveinään (numeroituna) ja sano tehtävässä, että tarkistetaan kolme lukua jokaisesta; ennen kysymystä voi pyytää täyttämään yhden esimerkkirivin.
- inquiry.json `reaktiot` / `johtopaatos` — taulukossa on valmiina reaktio $\bar{\nu}_e + p \to n + e^+$ ja sen laskettu tarkistus mallivastauksessa; tason 3 tehtävä fy8-15-L3-03 kysyy täsmälleen saman hiukkasen $X$. Fix: tehtävässä käytä toista reaktiota (esim. $\nu_e + n \to p + X$) tai ota $\bar{\nu}_e + p$ pois taulukosta.
- lesson.md Higgsin bosoni ja CERN — kappale (LHC:n pituus, energia, Suomen jäsenyysvuosi) ylittää paikan tavoitteet (perushiukkaset ja perusvuorovaikutukset, fotoni välittäjänä); ei häiritse oppimista, mutta lisää lukumäärää. Fix: lyhennä LHC-kappale kahteen virkkeeseen.
- lesson.md Ydinajatus — seitsemän alalukua, kuusi kuvaa ja taulukko ennen ensimmäistäkään laskua; teoriaosa on tuntiin suuri, vaikka jokainen kappale on lyhyt. Fix: harkitse Higgs/CERNin ja antihiukkasten merkitsemistä lisäluettavaksi.
- inquiry.json `siirto` (myonin hajoaminen) — rakenne $Q = (m - m)c^2$ on sama kuin esimerkissä, joten siirto on pieni: vaihtelua saisi pyytämällä ensin tarkistamaan säilymislait.

## Checked
- Paketti: tavoitteet, esitiedot (fy8-14, kaksi pohjatietoa), lesson.md, inquiry.json kokonaan, tehtävät ja ratkaisut (myös uusi L3-01 Ω⁻ -hajoaminen), poistumislipuke.
- Kuvat: contact-1 (hero, skaalat, taulukko, hadronit, annihilaatio, välittäjä), fig-13 (beeta), stage-tutki-390-2.
- Polku: pohdinta → ennusteet (kvarkkien varaukset, miksi protoni ei hajoa; väärien vaihtoehtojen palaute korjaa virhekäsityksen) → kaksi taulukkotutkimusta → teoria → esimerkki; alun kysymys saa vastauksen (baryoniluku, protoni kevyin baryoni).
- Ennuste 2: vaihtoehdot ovat uskottavia, oikea ei ole aina ensimmäinen; palaute avautuu vasta teorian jälkeen.
- Ei simulaatiota, eikä sellaista tarvita; tutkimus tehdään datataulukoista.
- Hash alussa ja lopussa sama.
