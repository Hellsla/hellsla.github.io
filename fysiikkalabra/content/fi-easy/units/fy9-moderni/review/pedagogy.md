VERDICT: PASS
CONTENT-HASH: 43cb3edae017c63d
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8 and -s9; older tasks untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (ei mitään)

## Polish
- s8 Yleisiä virheitä, a: esimerkki "$\mu = 16 / 20\,\text{cm} = 0{,}80$" on jäänyt vanhoista luvuista. Nykyisillä pisteillä $(0;\,80)$ ja $(10;\,20)$ osamäärä on $80/20 = 4$ ja väärä tulos $0{,}40\,\text{1/cm}$. Korjaa luvut.
- s8 d, kriteeri: "Kertoo, miten oletus vaikuttaa" on lauseena vajaa (subjekti puuttuu); kuitenkin ymmärrettävä.
- s9 a: ruudukon piste on enää vain ratkaisussa ja kriteerissä; toinen piste on origo. Hyväksyttävä.

## Checked
- Avasin fi-easy-paketin: s8 ja s9 tasks.json omana tekstinään, solutions.md ja tarkistusosio (practice.py check OK); hash alussa ja lopussa 43cb3edae017c63d.
- Round 1:n kohdat: s9 a:n teksti ei anna pistettä $(250;\,18\,000)$, joten $H_0$ luetaan kuvaajalta. s8 a:n toinen piste $(10\,\text{cm};\,20\,\mu\text{Sv/h})$ vastaa ratkaisua ($\ln 4/10 = 0{,}14$).
- s8 d: oletus kysytään tekstissä ("Mainitse myös yksi mallin oletus ... ja kerro sen vaikutus"); kriteeri vastaa kysymystä eikä paljasta sisältöä.
- s9 c: kysymys ei paljasta ketjua $t = 1/H_0$ eikä yksikkömuunnosta.
- Uskollisuus: samat luvut, pisteet (3+3+3+4, 3+3+4+3), toleranssit ja kriteerit kuin fi:ssä; lauseet lyhyitä ja termit (annosnopeus, vaimennuskerroin, Hubblen vakio) säilyvät. Pyöristys kahteen numeroon kuten lähtötiedoissa; laskuketjut tasattuina riveinä; yksikkökentät kielineutraaleja.
- 360 px: check_layout ja shots.md, ei avattu.
