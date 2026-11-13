VERDICT: PASS
CONTENT-HASH: c4bc3eda5ca95d13
## Blocking

## Polish
- content/fi/FY4/fy4-9/exercises/solutions.md (L3-02 Kaava) — "$F\,\Delta t = mv_0 - 0$" kirjoittaa liikemäärän muutoksen väärinpäin (alku miinus loppu). Luku painottaa etumerkkejä, joten $-F\,\Delta t = 0 - mv_0$ ("vyön voima osoittaa liikettä vastaan") olisi johdonmukainen L2-01:n kanssa.
- solutions.md (L2-07 Vastaus) — "kuten massassa $0{,}50\,\text{kg}$ ja nopeudessa $1{,}50\,\text{m/s}$ pyöristettynä": nopeudessa $1{,}50\,\text{m/s}$ on kolme numeroa, eikä se rajoita tulosta $\Delta v$. Tarkkuuden rajaa massa $0{,}50\,\text{kg}$, joten sen mainitseminen yksin riittää.

## Checked
- Muuttunut rivi (L2-08:n Vastaus) pitää paikkansa. Tulos on $450\,\text{N} = 4{,}5 \cdot 10^2\,\text{N}$, jossa on kaksi merkitsevää numeroa. Huippuarvo $900\,\text{N}$ ja kesto $12\,\text{ms}$ luetaan $100\,\text{N}$:n ja $2\,\text{ms}$:n ruudukolta, ja kolmion keskiarvo on $F_\text{max}/2$.
- Laskin kaikki 18 numeerista vastausta uudelleen yhdessä skriptissä omilla kaavoillani `python -I answers.py`:n rinnalla. Kaikki täsmäävät exercises.json:n kanssa, ja pyöristetyt vastaukset mahtuvat toleransseihin.
- Puolisuunnikassummat on laskettu itse: L2-07 antaa $1{,}44\,\text{N}\cdot\text{s}$ ja kärryn loppunopeudeksi $+1{,}38\,\text{m/s}$, L3-04 antaa $981\,\text{N}\cdot\text{s}$ ja $50{,}45\,\text{km/h}$. L3-04 c on $39\,\text{kN}$, joka on yli kaksi kertaa huippuarvo $17{,}4\,\text{kN}$, ja keskiarvo on $9{,}81\,\text{kN}$. L3-01:n puolisuunnikas on $48\,\text{N}\cdot\text{s}$.
- L3-05: $v_1 = -4{,}905\,\text{m/s}$ ja $v_2 = +3{,}924\,\text{m/s}$. Paino otetaan mukaan, jolloin $N_\text{ka} = 447\,\text{N}$, ja savipallolle $251\,\text{N}$. Korkeudet $1{,}23\,\text{m}$ ja $0{,}78\,\text{m}$ ovat oikein.
- Etumerkit ovat kimpoamisissa oikein: L2-03 antaa $-1{,}5\,\text{N}\cdot\text{s}$ ja L3-03 voimat $80$ ja $140\,\text{N}$. Kolmannen lain käyttö on perusteltu.
- Monivalinnoissa on täsmälleen yksi oikea vaihtoehto. L1-09:n väärät vaihtoehdot ja niiden palautteet pitävät paikkansa: $0{,}4\,\text{N}$ on noin $2 \cdot 0{,}196\,\text{N}$, $4000$ syntyy liike-energiasta ($\text{W}$, ei $\text{N}$) ja $400\,000$ grammoista. L1-06:n neljä vaihtoehtoa ja palautteet ovat oikein.
- Ehdot on kerrottu tehtävissä: paino jätetään huomiotta iskun aikana, ja kitka tai ilmanvastus jätetään huomiotta. Esimerkkiaineisto on merkitty taulukoihin. Kuvien kuvaukset antavat samat luvut kuin kuvat eivätkä paljasta vastauksia.
- Merkinnät ($p$, $I$, $F_\text{ka}$, etumerkit) ovat samat kuin luvussa, ja sisältö pysyy FY4:n alueella.
- Hash c4bc3eda5ca95d13 sekä alussa että lopussa.
