VERDICT: PASS
CONTENT-HASH: 092d5e13ddc54fbc
SCOPE: delta added-exercise from a6b9feb8d21605fb base 8f23aa7ae3bd

## Blocking

## Polish
- exercises.json (L2-09) — L2-09 on L1-01 käänteisenä samoilla luvuilla (v = 20 m/s, a_n = 5,0 m/s², r = 80 m). Fysiikka on oikein, mutta L1-01:n tehnyt tietää säteen valmiiksi. — Kuvaajan pisteeksi tai käyrän säteeksi kannattaa valita eri arvot, esimerkiksi r = 60 m ja piste (15 m/s; 3,75 m/s²), jolloin vastaukseksi tulee 60 m.
- lessons/FY5/fy5-4/figures.py (kuvaaja_b) — käyrä 1,2v²/60 nousee arvoon 12,5 kN, kun v = 25 m/s, joten se menee noin 10 px y-akselin ylärajan 12 kN yli, eikä sitä leikata. — Nosta y-akseli 13 kN:iin tai lopeta käyrä 24 m/s:iin. (Visuaalinen asia, ei vaikuta lukemaan.)

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L2-09 ja L3-06.
- Laskin uudelleen figures.py:n käyristä. Kuvan a käyrä on v²/80 ja merkitty piste (20; 5,0), joten r = v²/a_n = 80 m. Kuvan b käyrä on 1,2v²/60 kN, joten F(20 m/s) = 8,0 kN ja μ0 = 8000/(1200·9,81) = 0,6796 ≈ 0,68. Tulokset ovat samat kuin answers.py:ssä ja exercises.json:ssa.
- Malli on oikea: kitka on ainoa vaakasuora voima, N = mg ja rajatapaus F = μ0·N. Tehtävä kertoo oletukset, ja merkinnät ovat samat kuin luvussa.
- Merkitsevät numerot: kummassakin luettu arvo on kahden numeron tarkkuudella (5,0 ja 8,0), vastaukset ovat 80 m ja 0,68, ja toleranssi 2 % sopii niihin.
- Kuvat ovat uusia tehtäväkuvia, joita käytetään vain exercises.json:ssa (figure catalog `used_in`). Kumpikaan ei kerro sädettä, eikä kumpikaan toista Tarkista osaamisesi -tehtävää. Alt-teksteissä on samat pisteet.
- Järkevyystarkistukset ovat oikeat: L2-09:ssä 1,25 m/s² nopeudella 10 m/s, L3-06:ssa kuivan ja märän asfaltin vertailu.
