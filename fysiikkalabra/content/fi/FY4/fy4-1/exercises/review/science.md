VERDICT: PASS
CONTENT-HASH: 9e3f1aafd212641a
SCOPE: delta added-exercise from 6532dd8778633a6f base 7db0992d648a
## Blocking

## Polish
- content/fi/FY4/fy4-1/exercises/solutions.md (L2-09 Vastaus) — "nopeudet $2{,}0\,\text{m/s}$ ja aika $6{,}0\,\text{s}$ on luettu kuvaajasta": aika $6{,}0\,\text{s}$ annetaan tehtävätekstissä, sitä ei lueta kuvaajasta. Parempi: "nopeudet on laskettu kuvaajan ruudukon risteyksistä, ja aika $6{,}0\,\text{s}$ on annettu kahdella numerolla".
- solutions.md (L2-08 Järkevyys) — "Nopeus $2{,}0\,\text{m/s}$ on kävelyvauhtia": kyse on keskivauhdista, joten "Keskivauhti $2{,}0\,\text{m/s}$" pitäisi suureet erillään, kuten ratkaisun muu osa tekee.

## Checked
- Kierroksen 3 polish-huomiot on korjattu. L2-08:n keskivauhdilla on oma tunnus $v_\text{kv}$, joten se ei enää sekoitu luvun keskinopeuteen $v_\text{k}$. L2-09:n Vastaus sanoo, että nopeudet on luettu kuvaajasta.
- Laskin vastaukset uudelleen yhdessä skriptissä, omat kaavani `python -I answers.py`:n rinnalla. L2-08: $s = 12 + 0 + 8 = 20\,\text{m}$ ja $20\,\text{m} : 10\,\text{s} = 2{,}0\,\text{m/s}$. L2-09: $x_\text{A} = 16\,\text{m}$, $x_\text{B} = 8\,\text{m}$ ja $d = 8\,\text{m}$. Sekä answers.py että exercises.json antavat samat arvot.
- Fysiikka: keskivauhti on matka jaettuna ajalla, ja tehtävä määrittelee sen. Matka saadaan osasiirtymien itseisarvoista, ja vertailu keskinopeuteen $0{,}4\,\text{m/s}$ pitää paikkansa. L2-09 käyttää yhtälöä $x = x_0 + vt$ ja välimatkaa $|x_\text{A} - x_\text{B}|$. Suorat leikkaavat pisteessä $(4\,\text{s};\, 12\,\text{m})$. Ohjeen sanamuoto "ylempänä oleva viiva" on käytössä.
- Kuvien kulmapisteet ovat ruudukon risteyksissä, joten toleranssit (2 % ja 4 %) riittävät.
- Hash 9e3f1aafd212641a sekä alussa että lopussa.
