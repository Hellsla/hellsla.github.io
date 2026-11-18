VERDICT: PASS
CONTENT-HASH: 4465c40cddfece9f
SCOPE: delta: new tasks s8 (Betoniseinä) and s9 (Galaksien etääntyminen) and the intro; older tasks untouched

## Blocking
- (none)

## Polish
- s9 a: tehtävän teksti antaa suoran pisteen ($250\,\text{Mpc}$; $18\,000\,\text{km/s}$), ja kuvan kuvaus toistaa sen. Kuvaajaa ei tarvitse lukea, joten `graph_read` ei mittaa mitään. Parempi: poista piste tekstistä ja kuvauksesta, jolloin $H_0$ luetaan ruudukosta (s8:ssa näin jo on).
- s9 a: toinen "kaukana oleva piste" on origo, joka on annettu.
- s8 antaa mallin $\dot{H}=\dot{H}_0 e^{-\mu d}$ valmiina; sopii tavoitteeseen, mutta mallin tunnistaminen jää harjoittelematta.
- Helppo kieli: "Se on esitetty seinän paksuuden funktiona" ja "Niihin on sovitettu suora" ovat selkeitä lyhyitä lauseita, mutta s9 c:n ketju "Muuntaa $H_0$:n yksikköön" jättää subjektin pois; "$\dot{H}$ käytävän puolella. Se on esitetty..." on hyvä. Muuten kieli on kevyttä ja termit (annosnopeus, vaimennuskerroin, Hubblen vakio) säilyvät.

## Checked
- Avasin fi-easy-paketin: tarkistukset (practice.py check OK), s8 ja s9 tasks.json omana tekstinään, solutions.md ja kuvien kuvaukset.
- Uskollisuus: samat luvut, pisteet (3+3+3+4, 3+3+4+3), toleranssit ja kriteerit kuin fi-versiossa; lauseet lyhennetty ilman sisällön muutosta, esim. d-kohdan oletus ("Nimeää oletuksen ja kertoo...") ja yläpyöristys säilyvät. Ei lisättyjä tai poistettuja vihjeitä.
- Laskin luvut uudelleen: $\mu=0{,}1386$, $6{,}6\,\mu\text{Sv/h}$, $2{,}18\,\text{mSv}$, $23{,}6\,\text{cm}$, $H_0=72$, $116{,}7\,\text{Mpc}$, $1{,}36\cdot10^{10}\,\text{a}$; toleranssit hyväksyvät kahden numeron pyöristykset.
- Taso ja vaihtelu: s8 lukeminen, malli, päättely, mitoitus; s9 lukeminen, käänteinen lasku, yksikkömuunnos, selitys. Yleiset virheet todellisia.
- Alt-nimet ($\dot{H}$, $d$, $v$) vastaavat tekstiä; yksikkökentät kielineutraaleja.
- Intro: "Yhdeksän" = 9 tehtävää (136 p); tehtävät 7, 8, 9 oikein. 360 px: luotin check_layoutiin ja shots.md:hen, en avannut kuvia.
- Hash alussa ja lopussa sama.
