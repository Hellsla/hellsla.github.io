VERDICT: PASS
CONTENT-HASH: 9c30fcda079726fd
SCOPE: delta added-exercise from efb48162357b8d03 base 7db0992d648a
## Blocking

## Polish
- L2-08 — voimilla ei ole nimettyjä aiheuttajia (esimerkiksi kaksi narua), vaikka luvun sääntö on, että jokaisella voimalla on aiheuttaja. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- Kierroksen 4 polish-huomio on korjattu. Kuvan `ruutu-vinot` kuvaus (aria-teksti ja figcat) sanoo nyt "Kappale … Kappale on … kappaleen", kuten tehtäväteksti. Muutos koskee vain tekstiä: diffin mukaan ruudukko, kappaleen koko, voimat $(10;\, 12)\,\text{N}$ ja $(-4;\, -4)\,\text{N}$, `a_dir` ja mittajana ovat ennallaan.
- Suunta "$53^\circ$ $x$-akselista kohti $+y$-suuntaa" pitää paikkansa: $\arctan(8{,}0/6{,}0) = 53{,}13^\circ$. Voimakuvion `a 53,13` on samassa suunnassa.
- Laskin vastauksen uudelleen `python -I answers.py`:n rinnalla. $|\Sigma F| = \sqrt{6{,}0^2 + 8{,}0^2}\,\text{N} = 10\,\text{N}$ ja $a = 10\,\text{N} : 2{,}5\,\text{kg} = 4{,}0\,\text{m/s}^2$. Arvo täsmää answers.py:n ja exercises.json:n kanssa (toleranssi 0,02).
- Fysiikka: jää on kitkaton ja vaakasuora, joten paino ja tukivoima kumoavat toisensa. Komponenttiyhtälöt ovat oikein. Järkevyystarkistus pitää paikkansa, sillä $10\,\text{N} < 21{,}3\,\text{N}$ ja voimat muodostavat 6–8–10-kolmion.
- Voimakuvion tarkistuslista: kaksi voimaa, jotka eivät ole kolmannen lain pari. Kiihtyvyyttä ei ole piirretty voimaksi, eikä komponentteja ole laskettu kahteen kertaan.
- Hash 9c30fcda079726fd sekä alussa että lopussa.
