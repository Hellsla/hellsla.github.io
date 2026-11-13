VERDICT: PASS
CONTENT-HASH: 14555a0377ff79b2
## Blocking

## Polish

## Checked
- Muutos koskee vain L1-09:n Vastaus-riviä, ja luvut, tunnukset ja kaavat ovat ennallaan. Uusi perustelu pitää paikkansa. Taulukon arvossa $24{,}79\,\text{m/s}^2$ on neljä merkitsevää numeroa. Korkeus $20\,\text{m}$ tulkitaan tarkaksi. Tulos $1{,}27\,\text{s}$ annetaan kolmella numerolla, koska eri taulukoiden arvot poikkeavat jo neljännessä numerossa. Rivi ei enää väitä taulukon arvossa olevan kolmea numeroa.
- Laskin vastauksen uudelleen samassa skriptissä kuin muut: $t = \sqrt{2 \cdot 20\,\text{m} / 24{,}79\,\text{m/s}^2} = 1{,}2703\,\text{s}$. Arvo on sama answers.py:ssä ja exercises.json:ssa (1.2703, toleranssi 0,04). Sekä $1{,}27\,\text{s}$ että $1{,}3\,\text{s}$ mahtuvat toleranssiin. Toleranssi $\pm 4\,\%$ on mainittu oikein.
- Fysiikka on ennallaan: vapaa pudotus levosta ilman ilmanvastusta, ja ratkaisu $t = \sqrt{2h/g}$ johdetaan ensin symbolein. Järkevyystarkistus Maan arvoon $2{,}02\,\text{s}$ on yhä aito.
- Hash 14555a0377ff79b2 sekä alussa että lopussa.
