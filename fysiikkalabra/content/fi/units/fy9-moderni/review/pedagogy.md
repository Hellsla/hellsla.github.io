VERDICT: PASS
CONTENT-HASH: 876c08f6ee47b4ec
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8 and -s9; older tasks untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (ei mitään)

## Polish
- s8 Yleisiä virheitä, a: esimerkki "$\mu = 16 / 20\,\text{cm} = 0{,}80$" on jäänyt vanhoista lukuarvoista. Nykyisillä pisteillä $(0;\,80)$ ja $(10;\,20)$ osamäärä on $80/20 = 4$ ja virheellinen tulos $4/10\,\text{cm} = 0{,}40\,\text{1/cm}$. Korjaa luvut, ettei oppija näe lukua 16, jota aineistossa ei ole.
- s9 a: ruudukon piste on enää vain ratkaisussa ja kriteerissä, ei tehtävätekstissä; toinen piste on silti origo. Hyväksyttävä.
- s8 antaa mallin valmiina (tietoinen valinta).

## Checked
- Avasin fi-paketin: s8 ja s9 tasks.json, solutions.md ja tarkistusosio (practice.py check OK); hash alussa ja lopussa 876c08f6ee47b4ec.
- Round 1:n polish-kohdat: s9 a:n teksti ei enää anna pistettä $(250;\,18\,000)$, joten $H_0$ luetaan kuvaajalta ja `graph_read` mittaa jotain. s8 a: toinen luettava piste $(10\,\text{cm};\,20\,\mu\text{Sv/h})$ ja ratkaisun luvut ($\ln 4/10 = 0{,}14$) täsmäävät.
- s8 d: oletus kysytään nyt tekstissä ("Mainitse myös yksi mallin oletus ... ja sen vaikutus"), kriteeri vastaa kysymystä; ei paljasta ratkaisun rakennetta (oletuksen sisältö jää oppijalle).
- s9 c: uudelleenmuotoilu ("etäisyydet olivat nollia ... samalla nopeudella") ei paljasta ketjua $t = 1/H_0$ eikä yksikkömuunnosta.
- Pyöristys kahteen numeroon (0,14; 6,6; 2,2; 24; 72; 120; $1{,}4\cdot10^{10}$) vastaa lähtötietoja; tarkempi $\mu$ selitetty. Laskuketjut tasattuina riveinä; yksikkökentät (1/cm, µSv/h, mSv, cm, km/s/Mpc, a) kielineutraaleja.
- Pisteet 3+3+3+4 ja 3+3+4+3 täsmäävät kriteereihin; 360 px: check_layout ja shots.md, ei avattu.
