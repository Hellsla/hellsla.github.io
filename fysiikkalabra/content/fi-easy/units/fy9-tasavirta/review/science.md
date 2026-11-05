VERDICT: PASS
CONTENT-HASH: e8bf91a0dde33d19

Tämä on Selkeä suomi -käännöksen tieteellinen katselmus. Lähde on content/fi/units/fy9-tasavirta/, joka on jo hyväksytty.

Tarkistukset: `check_i18n.py` antaa fi-easy-kielelle 0 virhettä (vastaukset, toleranssit, oikeat vaihtoehdot, kaavat, osiot, kuvat). `practice.py check` on OK (6 tehtävää, 95 pistettä). `units.py figures fy9-tasavirta --lang fi-easy --check` kertoo, että kuvat ovat ajan tasalla. Kaikkien tekstien (unit.md, inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json, sovella/solutions.md) lukujen multijoukko on täsmälleen sama kuin lähteessä: yhtään lukua ei ole lisätty, poistettu tai muutettu. Kaikki kaavalohkot ja Sijoitus-rivit ovat sanatarkasti lähteen mukaisia. Luin jokaisen muutetun lauseen lähdettä vasten (Periaate, Vastaus, Järkevyys, palaute, kriteerit, mallivastaukset).

## Blocking
Ei yhtään.

## Polish
1. unit.json `key_concepts`, *sisäinen resistanssi*: lause "osa jännitteestä häviää pariston sisällä" on fysiikaltaan väljä, koska jännite ei "häviä". Korjaus: "Kun virta kulkee sen läpi, napajännite on jännitehäviön $R_\text{s} I$ verran pienempi kuin lähdejännite."
2. sovella/tasks.json s2 c, kriteeri 1: jännitelain kuvaus on jaettu kolmeen lauseeseen ("Se laskee … Lisäksi se laskee akun lähdejännitteen verran"). Sisältö vastaa lähdettä. Jos silmukka kuvattaisiin yhdellä lauseella, lukija näkisi sen kokonaisuutena. Muutos ei ole pakollinen.
3. inquiry.json activities[13].solution, Järkevyys: muotoilu "noin neljä kertaa suurempi" korvaa lähteen sanan "noin nelinkertainen". Merkitys on sama ja oikea (68/16 ≈ 4,3). Ei toimenpidettä.

Fysiikka on lähteen mukainen: mallien ehdot (Ohmin laki vakiolämpötilassa, Joulen lain muodot vain vastukselle, $E$ ja $R_\text{s}$ vakioita), pyöristysperustelut ja yksiköt. Lisätyt selitykset ovat oikein eivätkä tuo uusia lukuja. Selitetyt käsitteet ovat kapasiteetti (= varaus), haaraton piiri (= yksi reitti), kääntäen verrannollinen, ekstrapolaatio, termostaatti, resoluutio ja oikosulku.
