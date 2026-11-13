VERDICT: PASS
CONTENT-HASH: 5cfb2fa70736df06
SCOPE: delta added-exercise from efb48162357b8d03 base 7db0992d648a
## Blocking

## Polish
- lessons/FY4/fy4-5/figures.py:379 (ruutu-vinot) — tehtävä puhuu nyt kappaleesta, mutta kuvan kuvaus (aria-teksti ja figcat) sanoo yhä "Jääkiekko … Kiekko". Ruudunlukijan käyttäjä kuulee siis $2{,}5\,\text{kg}$:n jääkiekosta. Vaihda kuvaukseen "Kappale", kun kuva hyväksytään seuraavan kerran.
- L2-08 — voimilla ei ole nimettyjä aiheuttajia (esimerkiksi kaksi narua), vaikka luvun sääntö on, että jokaisella voimalla on aiheuttaja. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- Kiekko on vaihdettu kappaleeksi. Massa $2{,}5\,\text{kg}$ sopii nyt tilanteeseen, eikä fysiikka muuttunut.
- Suunta "$53^\circ$ $x$-akselista kohti $+y$-suuntaa" pitää paikkansa: $\arctan(8{,}0/6{,}0) = 53{,}13^\circ$. Vektori $\Sigma\overline{F} = (6{,}0;\, 8{,}0)\,\text{N}$ on ensimmäisessä neljänneksessä. Voimakuvion `a 53,13` on samassa suunnassa.
- Laskin vastauksen uudelleen samassa skriptissä `python -I answers.py`:n rinnalla. Komponentit ovat $F_1 = (10;\, 12)\,\text{N}$ ja $F_2 = (-4;\, -4)\,\text{N}$, joten $|\Sigma F| = 10\,\text{N}$ ja $a = 4{,}0\,\text{m/s}^2$. Arvo täsmää answers.py:n ja exercises.json:n kanssa.
- Fysiikka: jää on kitkaton ja vaakasuora, joten paino ja tukivoima kumoavat toisensa. Komponenttiyhtälöt ovat oikein. Järkevyystarkistus pitää paikkansa, sillä $10\,\text{N} < 21{,}3\,\text{N}$ ja voimat muodostavat 6–8–10-kolmion.
- Voimakuvion tarkistuslista: kaksi vaakasuoraa voimaa, jotka eivät ole kolmannen lain pari. Kiihtyvyyttä ei ole piirretty voimaksi, eikä komponentteja ole laskettu kahteen kertaan.
- Hash 5cfb2fa70736df06 sekä alussa että lopussa.
