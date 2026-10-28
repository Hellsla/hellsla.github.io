VERDICT: FAIL
CONTENT-HASH: fdfbc1a91389a62a

## Blocking
1. solutions.md:99 (fy2-5-L3-01, Järkevyys) — "erotus $8{,}0\,\text{kg} - 2{,}79\,\text{kg}$ on yli kaksi kertaa öljyn massa" on väärin: $5{,}21 : 2{,}79 \approx 1{,}87$, eli alle kaksi kertaa; väärä tarkistus opettaa vääränlaista järkevyysarviota — korjaa: "ja erotus on $2{,}87 - 1 = 1{,}87$ kertaa öljyn massa: $1{,}87 \cdot 2{,}79\,\text{kg} \approx 5{,}2\,\text{kg}$, kuten pitää."

## Polish
1. exercises.json fy2-5-L3-02 — yksikkö "päivän annosta" on kömpelö — "annosta" tai kysy "kuinka monta päivää ruoka riittää, desimaalilukuna" ja pidä yksikkö "päivää".
2. solutions.md L3-01 Vastaus — "kaksi merkitsevää numeroa kuten tiedoissa $120\,\text{MJ}$" — $120$ voi olla kolmen numeron luku; mainitse pelkästään lämpöarvot $15$ ja $43$.
3. exercises.json L3-01 — "Selitä myös" ei tarkisteta vastauskentässä (vain kg); pidä mallivastauksessa selitys näkyvänä (on jo Vastaus-rivillä).

## Checked
- Edellisen kierroksen huomautukset korjattu: L1-03 ja L1-05 ovat nyt yhden kaavan tehtäviä ilman muunnoksia, L3-01 ei enää toista ennusteen 2,9:ää, L3-03:n Periaate perustelee jakamisen ajalla.
- Maakaasun $48\,\text{MJ/kg}$ vastaa oppitunnin taulukkoa; vastaus $96\,\text{MJ}$ oikein ja answers.py yhdenmukainen.
- L1-03 $310\,000\,\text{MJ}$ ($312\,000$ sisällä toleranssin) ja L1-05 $0{,}96\,\text{MJ}$ oikein, yksikkö sopii kysymykseen.
- L3-01 $5{,}2\,\text{kg}$ ($8{,}0 - 2{,}79$) laskettu oikein, pyöristys tehtävän tarkkuudella.
- L3-02 uusi muotoilu poistaa "3 täyttä päivää" -epäselvyyden.
- Yksiköt ja luvut LaTeXina, kertominen pisteellä, jakaminen kaksoispisteellä; muunnoksessa $1200 \cdot (1 : 1000)$.
