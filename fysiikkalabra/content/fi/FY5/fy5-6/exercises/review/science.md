VERDICT: PASS
CONTENT-HASH: 0d489920ee94599b
SCOPE: delta added-exercise from 1ae57cce87a7a6fc base 81db4a6fd727

## Blocking

## Polish
- solutions.md:224 (L1-11) — "kolme merkitsevää numeroa kuten taulukon massassa" ei ole oikea perustelu, koska taulukon massassa 7,346·10²² kg on neljä merkitsevää numeroa. Rajoittava tieto on korkeus 300 km. — Nimeä se perusteluksi.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-10, L1-11 ja L2-08.
- Kierroksen 1 korjaus on tehty. L2-08:n vastaus on nyt 7,7. Rajoittavana tietona mainitaan 88 milj. km (kaksi merkitsevää numeroa), ja ratkaisussa näkyy myös pyöristämätön 7,724. Answer 7.7 vastaa answers.py:tä.
- Laskin uudelleen. L1-10: √(γ·1,99·10³⁰/1,496·10¹¹) = 29,80 km/s. L1-11: √(γ·7,346·10²²/2,037·10⁶) = 1,551 km/s. L2-08: √(5250/88) = 7,724.
- L2-08 kertoo, että ympyräradat ovat hypoteettisia ja että Halleyn komeetan todellinen rata on ellipsi. Mallia ei siis sovelleta väärin.
- L1-11 laskee säteen kaavalla r = R + h. MAFY-arvot ja ±4 %:n toleranssi sopivat yhteen.
- Kuva radat on käytössä vain lesson.md:ssä (Milloin ympyrämalli pätee) ja tehtävissä, ei inquiry.json:ssa. Tehtävät lukevat kuvan eri puoliskoja. L1-10 laskee saman nopeuden kuin L1-08, mutta eri menetelmällä, ja ratkaisu mainitsee tämän.
- Merkinnät ovat luvun: γ, M, r ja v = √(γM/r).
