VERDICT: FAIL
CONTENT-HASH: 54a069e1f891626c

## Blocking
- exercises.json:334 (L2-09) — A, arviointi: tehtäväteksti kysyy yhä kerrosta B–C ("Lue kuvasta kaikujen B ja C hetket. Kuinka paksu on kudoskerros, jota rajaavat kaikuja B ja C vastaavat rajapinnat?"). Vastaus 2,31 cm, answers.py ja ratkaisu laskevat kuitenkin kerroksen A–B. Kysytyn kerroksen paksuus on 1540·40 µs/2 = 3,08 cm, joten sivu hylkäisi oikean vastauksen. Teksti kysyy lisäksi samaa kuin inquiry-tarkistus `ascan-BC-cm`. — Korjaus: vaihda tekstiin "Lue kuvasta kaikujen A ja B hetket. Kuinka paksu on kudoskerros, jota rajaavat kaikuja A ja B vastaavat rajapinnat?"

## Polish
- solutions.md (L1-09, Vastaus) — ilmaus "Aika 20 ms on sovittu tarkaksi" ei ole kurssin käytäntö. — Anna vastaus 14 m, koska ajassa 20 ms on kaksi merkitsevää numeroa. Toleranssi 4 % hyväksyy sekä 14 että 14,0.
- exercises.json (L1-09) — pohjan lähellä vesi on noin 4-asteista, ja pulssi kulkee myös jään läpi. Kumpikin vaikutus mahtuu toleranssiin, mutta lisäys "oletetaan koko vesi 0-asteiseksi" estäisi väärän mielikuvan.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09 (kierros 3).
- L2-09:n ratkaisu ja answers.py: Δd = 1540·(50 − 20) µs/2 = 2,31 cm. Lasku on oikein kerrokselle A–B, ja A–B ei toista inquiryä. Ainoa virhe on tehtäväteksti.
- Piikit ovat 5 µs:n apuviivoilla (20, 50 ja 90 µs), joten kolme merkitsevää numeroa ja toleranssi 2 % sopivat.
- L1-09: 1402,4·0,020/2 = 14,02 m. Arvo 1402,4 m/s on mafy-arvot.tsv:n VERIFIED-riviltä (vesi 0 °C).
- Järkevyystarkistukset ovat oikein: d_A = 1,54 cm ja d_B = 3,85 cm. L1-09:ssä kudoksen arvolla saataisiin 15,4 m, eli noin 10 % liikaa.
