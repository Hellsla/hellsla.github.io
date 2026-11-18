VERDICT: PASS
CONTENT-HASH: 115941f6cb5f4383
SCOPE: delta: new tasks s8 (Betoniseinä) and s9 (Galaksien etääntyminen) and the intro; older tasks untouched

## Blocking
- (none)

## Polish
- s9 a: tehtävän teksti antaa suoran pisteen ($250\,\text{Mpc}$; $18\,000\,\text{km/s}$), ja kuvan kuvaus toistaa sen. Kuvaajaa ei tarvitse lukea, joten kriteeri `graph_read` ei mittaa mitään ja yhdeksän mittauspistettä ovat koristetta. Parempi: poista piste tekstistä ja kuvauksesta, jolloin $H_0$ luetaan ruudukosta; s8:ssa näin jo on (kuvaus kertoo vain arvon $80$ kohdassa $d=0$).
- s9 a: toinen "kaukana oleva piste" on origo, joka on annettu. Lukeminen on silti oppimisen kohde vasta, kun piste pitää löytää itse.
- s8 teksti antaa mallin $\dot{H}=\dot{H}_0 e^{-\mu d}$ valmiina. Se sopii tehtävän tavoitteeseen (kuvaajan lukeminen ja malli), mutta "tunnista eksponentiaalinen vaimeneminen" jää harjoittelematta; sanottakoon tämä tietoisena valintana.
- s9 c: teksti kertoo vakionopeusoletuksen, mutta ei ketjua $t=1/H_0$. Hyvä; rakenne ei paljastu.
- Pyöristys: kuvaaja, s8 ja s9 antavat lähtötiedot kahdella numerolla, ja vastaukset ovat kahdella (6,6; 24; 120; 1,4·10^10). Täsmällinen $\mu$ jatkolaskuissa on selitetty ratkaisussa.

## Checked
- Avasin fi-paketin: tarkistusosio (practice.py check OK), s8 ja s9 tasks.json, solutions.md ja answers.py-laskennat sekä kuvien figures.py (alt-tekstit).
- Laskin luvut uudelleen: $\mu=\ln16/20=0{,}1386\,1/\text{cm}$; $6{,}6\,\mu\text{Sv/h}$; $330\,\text{h}$, $2{,}18\,\text{mSv}$; $3{,}03\,\mu\text{Sv/h}$, $23{,}6\,\text{cm}$; $H_0=72$; $116{,}7\,\text{Mpc}$; $1/H_0=1{,}36\cdot10^{10}\,\text{a}$. Toleranssit hyväksyvät kahden numeron pyöristykset.
- Taso: s8 nousee lukemisesta mallin käyttöön, päättelyyn (raja ylittyy) ja mitoitukseen ja oletuksen arviointiin; s9 lukemisesta käänteiseen laskuun, yksikkömuunnokseen ja käsitteelliseen selitykseen (ei keskipistettä). Sopii FY8:n tasolle, vaihtelua kahden kuvaajatehtävän välillä on.
- Pisteytys: osien pisteet = kriteerien summa (3+3+3+4, 3+3+4+3); kriteerit kysyvät vain sen, mitä osa; yleiset virheet ovat todellisia (ln vs osamäärä, mSv/$\mu$Sv, $1/72$ ilman muunnosta, "räjähdyksen sirpaleet"). Ratkaisut: laskuketjut tasattuina riveinä, järkevyysarviot mukana.
- Kuvien alt-nimet ($\dot{H}$, $d$, $v$) vastaavat tehtävätekstiä; s8:n alt ei paljasta arvoa $5{,}0$. Yksikkökentät ($1/\text{cm}$, $\mu$Sv/h, $\text{a}$) kielineutraaleja.
- Intro: "Yhdeksän" vastaa 9 tehtävää (136 p); viittaus tehtäviin 7, 8, 9 oikein. 360 px: luotin check_layoutiin ja shots.md:hen (hash sama), en avannut kuvia.
- Hash alussa ja lopussa sama.
