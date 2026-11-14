VERDICT: PASS
CONTENT-HASH: 7c46ff42f3980942
SCOPE: delta added-exercise from 12247bcf797a5c2e base 81db4a6fd727

## Blocking

## Polish
- solutions.md (L2-09, Vastaus) — pyöristysperuste "kuten nopeudessa 1540 m/s" ei nimeä rajoittavaa tietoa. Rajoittava tieto on kuvasta luettu aika 90 µs, jonka lukematarkkuus on noin ±1 µs. — Perustele kolme numeroa lukematarkkuudella.
- exercises.json (L2-09 ja L1-01) — lasku on lähes sama: L1-01:ssä kaiun aika on 91,0 µs, ja L2-09 lukee kuvasta 90 µs. L2-09:ssä on lisänä kuvaajan lukeminen, joten tehtävä ei ole toisto.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 5: arvioin muutetun tehtävän L2-09.
- L2-09: d = vt/2 = 1540·90·10⁻⁶/2 m = 6,93 cm, kuten answers.py:ssä ja suomenkielisessä versiossa. Toleranssi 2 % kattaa ±1 µs:n lukemat (6,85–7,01 cm).
- Selkokielinen lisäys "A-kuvaus näyttää kaiut ajan funktiona" on oikein. Periaate "kaksi kertaa syvyys" ja järkevyystarkistus (13,9 cm/2) ovat oikein.
- Kuva, sen kuvaus ja ratkaisu sijoittavat kaiun C kohtaan 90 µs. Kuva ei kerro syvyyttä.
- Toisto: inquiry-tarkistus kysyy kerrosta B–C (3,08 cm) ja L2-05 käyttää taulukkoa, joten luun syvyyttä ei kysytä muualla.
- Kaikkien tehtävien answer, unit ja tolerance ovat samat kuin suomenkielisessä versiossa. L1-09:n (14,0 m) ja L2-09:n luvut ovat samat.
