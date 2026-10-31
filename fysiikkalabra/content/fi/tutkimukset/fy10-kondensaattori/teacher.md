**Valmistelu.** Valitse kondensaattori, jonka merkinnöistä näkyvät kapasitanssi, suurin sallittu jännite ja napaisuus, ja kirjaa nämä opiskelijoille, jos merkinnät ovat vaikeita lukea. Ilmoita jännitelähteen enimmäisjännite niin, että se jää selvästi kondensaattorin jänniterajan ja anturin mittausalueen alapuolelle. Valitse vastukset niin, että aikavakio $\tau = RC$ sopii käytettävään mittaustapaan: anturilla riittää lyhyempi aikavakio, käsin luettaessa tarvitaan pidempi. Selvitä jännitemittarin tai anturin sisäinen resistanssi laitteen ohjeesta, jotta voit kertoa sen opiskelijoille, ja suosi vastuksia, joiden resistanssi on siihen verrattuna pieni. Laajennusta varten varaa noin viisi eri resistanssia; perusmittauksen kaksi vastusta voivat olla niistä kaksi. Tarkista kytkennät ennen kuin jännitelähde kytketään päälle, ja pura kondensaattorit työn lopuksi.

**Tavallisia virhekäsityksiä ja ongelmia.**

- Elektrolyyttikondensaattori kytketään väärin päin tai napaisuuden merkintää ei tunnisteta.
- Etuliitteet sekoittuvat: mikrofaradit, kiloohmit ja niiden tulo sekunteina lasketaan väärin.
- Aikavakio luetaan kuvaajasta jännitteen puolittumisaikana. Puoliintumisaika ja aikavakio ovat eri suureita.
- Aikavakio määritetään yhdestä pisteestä, vaikka alkuhetki tai alkujännite on epätarkka; sovitus koko käyrään on luotettavampi.
- Varautumisen mittauksessa linearisoidaan jännite $u$ eikä erotusta $U_0 - u$, jolloin kuvaaja ei suoristu.
- Logaritmia otetaan hyvin pienistä jännitteistä, joissa mittarin lukematarkkuus on suuri osa lukemasta.
- Mallin oletusten rikkoutumista ei pohdita. Virhelähteiden suunnat:
  - Mittarin tai anturin sisäinen resistanssi $R_\text{V}$ on kondensaattorin rinnalla, joten purkautumisessa $\tau = C\cdot\dfrac{R R_\text{V}}{R + R_\text{V}}$. Kapasitanssista $C = \dfrac{\tau}{R}$ tulee liian pieni, eniten suurilla resistansseilla.
  - Kondensaattorin vuotovirta purkaa kondensaattoria vastuksen ohi samaan tapaan, joten kapasitanssista tulee liian pieni, eniten suurilla resistansseilla.
  - Johtimien ja jännitelähteen sarjaresistanssi $r$ antaa $\tau = (R + r)\cdot C$, joten kapasitanssista tulee liian suuri, eniten pienillä resistansseilla. Laajennuksen kuvaajassa se näkyy vakioterminä.
- Merkittyä kapasitanssia pidetään tarkkana arvona, vaikka elektrolyyttikondensaattorin toleranssi voi olla suuri; toleranssi luetaan merkinnöistä tai valmistajan tiedoista.

**Eriyttäminen.** Ohjatussa työtavassa sivu kiinnittää purkautumismittauksen, kaksi vastusta ja kaksi toistoa kummallekin sekä mallin sovitustavan. Osittain ohjatussa opiskelija valitsee purkautumisen tai varautumisen, vastukset ja mittaustavan sekä perustelee mallin sovituksen. Itsenäisessä työtavassa annetaan vain tutkimuskysymys ja välineet, ja laajennus kuuluu työhön. Ohjattu työtapa saa eksponenttimallin teoriaosassa, osittain ohjattu etsii mallin ensin mittaustuloksista ja tarkistaa sen sitten sivulta. Kaikki perustelevat, mikä mallin parametri vastaa aikavakiota; itsenäisessä työtavassa perustelu rakennetaan teoriaosan muutosnopeudesta. Sähköopin moduuli FY6 ei ole vielä julkaistu, joten sivun teoriaosa on kirjoitettu niin, että työn voi tehdä ennen sitä.

**Turvallisuus.** Työn tärkeimmät riskit ovat elektrolyyttikondensaattorin väärä napaisuus ja jänniterajan ylittäminen, jotka voivat kuumentaa ja rikkoa kondensaattorin, sekä varatun kondensaattorin oikosulkeminen. Jännitteen raja tulee aina kondensaattorin merkinnöistä tai opettajalta, ei arviosta. Kondensaattori puretaan vastuksen kautta ennen kytkennän muuttamista. Vain pienjännitteinen tasajännitelähde; verkkojännite ei kuulu oppilaiden piireihin.
