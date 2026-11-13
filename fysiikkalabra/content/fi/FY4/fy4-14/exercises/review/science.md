VERDICT: PASS
CONTENT-HASH: 2ec9267f358ff7ed
SCOPE: delta added-exercise from 5ffc229e2dbf46e5 base 81db4a6fd727

## Blocking

## Polish
- solutions.md fy4-14-L2-08 Vastaus — "kolme merkitsevää numeroa kuten massassa $75{,}0\,\text{kg}$" ei ota huomioon, mikä tulosta oikeasti rajaa. Kuvaajasta luettu $\Delta v = 6{,}0\,\text{m/s}$ on kahden numeron tarkkuudella ja $5\,\text{m/s}$:n ruudukossa noin $\pm 1\,\text{m/s}$:n luentaa. — Ilmoita $F_\text{v} \approx 6{,}2 \cdot 10^2\,\text{N}$ ja perustele luentatarkkuudella. Toleranssi 5 % riittää jo nyt.

## Checked
- L2-08 laskettu uudelleen: $a = (46{,}4 - 40{,}4)/4{,}0 = 1{,}50\,\text{m/s}^2$, $F_\text{v} = m(g - a) = 623\,\text{N}$, $G = 735{,}75\,\text{N}$ ja suhde $0{,}847$ eli noin $85\,\%$; täsmää answers.py:n kanssa.
- Luettavuus: luentaa herkkä on vain $\Delta v$; $1\,\text{m/s}$:n virhe muuttaa tulosta 3 %. Tyypilliset lukemat (40 ja 45 tai 46,5) antavat $613$–$642\,\text{N}$, joten ne pysyvät ±5 %:n toleranssin sisällä. Kuvan kuvaus antaa samat pisteet eikä massaa, kiihtyvyyttä eikä voimaa.
- Aineiston fysiikka: pisteet sopivat neliölliseen ilmanvastukseen ($v = v_\text{t}\tanh(gt/v_\text{t})$, $v_\text{t} \approx 48\,\text{m/s}$ toistaa pisteet $\pm 0{,}3\,\text{m/s}$:n tarkkuudella). Vatsa alaspäin putoavan hyppääjän rajanopeus on realistinen. Alun kulmakerroin on lähes $g$ ja b-kohdan raja $F_\text{v} = G$, kuten luvussa.
- Keskeisdifferenssi välin 6–10 s yli on perusteltu arvio hetken 8 s kiihtyvyydelle, ja tehtävä nimeää pisteet, joten malli on kerrottu.
- Voimakuvio: $\overline{G}$ alas keskipisteestä ja $\overline{F}_\text{v}$ ylös, painoa lyhyempänä, kun hyppääjä vielä kiihtyy; kuvio vastaa liikettä. Liikeyhtälö $mg - F_\text{v} = ma$ luetaan kuviosta positiivisen suunnan ollessa alas, kuten luvun kaavaosiossa.
- Merkinnät $\overline{G}$, $\overline{F}_\text{v}$ ja $F_\text{v} = G$ rajanopeudella ovat samat kuin luvussa.
- Toistoa ei ole: kuvaa käyttää vain tämä tehtävä. L2-05 (vaahtomuovipallon taulukko) sekä L2-07 ja L3-04 (varjon auettua) ovat eri tilanteita.
- Sisältö pysyy FY4:n keskeisissä sisällöissä (liikeyhtälö ja voimakuvio); ilmanvastusta ei lasketa nopeudesta.
