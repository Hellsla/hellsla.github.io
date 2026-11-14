VERDICT: PASS
CONTENT-HASH: b12c411f043ca675
SCOPE: delta added-exercise from 19c4b1112a3292c3 base 81db4a6fd727

## Blocking

## Polish
- solutions.md (L2-09, Järkevyys) — virke "vesiaallolla, jonka aallonpituus on 8,0 cm, taajuus ei voi ylittää noin 4,5 Hz" pitää paikkansa (syvän veden gravitaatio–kapillaariaalto antaa 4,52 Hz), mutta väite ei perustu mihinkään, mitä kurssissa on opetettu. Sen voi poistaa tai lyhentää muotoon "kuten aaltoaltaissa tavallisesti".
- exercises.json (L2-10) — päättely on sama kuin L1-07:ssä (taajuus kaksinkertaistuu, aallonpituus puolittuu, b/λ kaksinkertaistuu). Uutta on vain kuvan lukeminen. Tämä on hyväksyttävää.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L2-09 ja L2-10.
- Kierroksen 1 korjaukset on tehty. L2-09:n taajuus on nyt 4,0 Hz, joten v = 4,0 Hz · 8,0 cm = 32 cm/s. Tämä on fysikaalisesti mahdollinen: dispersiorelaatiosta tulee syvyydeksi noin 1,3 cm. L2-10 esittää nyt vakionopeuden oletuksena ja mainitsee, että todellisessa altaassa nopeus riippuu aallonpituudesta.
- Laskin figures.py:stä uudelleen. Aaltorintamat ovat pystyviivoilla 1 ja 5, joten λ = 8,0 cm. Rako on vaakaviivojen 1 ja 7 välissä, joten b = 12 cm, λ' = 4,0 cm ja b/λ' = 3,0. Tulokset vastaavat answers.py:tä ja exercises.json:ia.
- Merkitsevät numerot: molemmissa vastauksissa on kaksi, ja toleranssi 2 % sopii.
- Kuvaa rako-ruudukko käytetään vain tehtävissä, ei inquiry.json:ssa. Alt-tekstissä on samat ruudukon paikat, eikä siinä ole merkitty λ:aa eikä b:tä.
