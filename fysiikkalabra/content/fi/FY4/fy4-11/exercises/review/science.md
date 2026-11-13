VERDICT: FAIL
CONTENT-HASH: 3139ddc5959cc19b

## Blocking
- exercises.json fy4-11-L1-09 (tolerance 0.03) ja solutions.md fy4-11-L1-09 Vastaus — (A, arviointi ja pyöristys) MAFY-arvo $\mu = 0{,}8$ on yhden merkitsevän numeron arvo, mutta ratkaisu perustelee "kaksi merkitsevää numeroa kuten … kitkakertoimessa $0{,}8$". Opiskelija, joka pyöristää aineiston mukaan, saa $30\,\text{m}$, joka on 4,6 % vastauksesta $31{,}46\,\text{m}$ ja jää toleranssin ulkopuolelle ("Lähellä"). — Korjaa pyöristysperuste: $\mu = 0{,}8$ on taulukon välin yläpää ja vain yhden numeron tarkkuudella, joten tulos on noin $30\,\text{m}$, ilmoitettuna $31\,\text{m}$. Nosta `tolerance` arvoon 0.05.
- solutions.md fy4-11-L1-09 Periaate — (A, määritelmä) "pysähtymismatka saadaan kaavasta $v_0^2 = 2as$": luvussa pysähtymismatka on $s_\text{r} + s_\text{j}$, ja tässä lasketaan jarrutusmatka. — Kirjoita "jarrutusmatka".
- exercises.json fy4-11-L3-06 (tolerance 0.02) ja solutions.md fy4-11-L3-06 Vastaus — (A, arviointi ja pyöristys) massa $70\,\text{kg}$ ja nopeus $15\,\text{m/s}$ ovat kahden merkitsevän numeron arvoja, mutta ratkaisu ilmoittaa kolme numeroa "aikojen mukaan". Kahteen numeroon pyöristävä opiskelija saa $11\,\text{kN}$, joka on 4,8 % vastauksesta $10{,}5\,\text{kN}$, eli toleranssin ulkopuolella. — Kirjoita massaksi $70{,}0\,\text{kg}$ (kuvaajan $15\,\text{m/s}$ on ruutuviivalla) tai nosta `tolerance` arvoon 0.05. Korjaa myös perustelu.

## Polish
- exercises.json fy4-11-L1-09 — tehtäväteksti antaa jarrutusmatkan symbolina $s$, mutta luku käyttää symbolia $s_\text{j}$. — Kirjoita $s_\text{j} = \dfrac{v_0^2}{2a}$ (myös ratkaisuun).
- figures.py ex_tv_tyyny (L3-06) — B:n suora osuu akseliin $0{,}02\,\text{s}$:n ruudun keskelle ($0{,}150\,\text{s}$). Jos lukema on $\pm 0{,}005\,\text{s}$ pielessä, erotus muuttuu yli 2 %. Lukema on kohtuullinen, mutta B:n aika $0{,}140$ tai $0{,}160\,\text{s}$ (ruutuviivalla) olisi varmempi.

## Checked
- MAFY-rivi: docs/mafy-arvot.tsv rivi 57, kumi–asfaltti liukukitkakerroin 0,5–0,8, VERIFIED. Tehtävä käyttää välin yläpäätä kuten teksti sanoo. Vihje on pelkkä taulukon nimi *Kitkakertoimia*, ja `lookup: MAFY` on asetettu.
- L1-09 laskettu uudelleen: $a = 7{,}85\,\text{m/s}^2$ ja $s_\text{j} = 31{,}46\,\text{m}$; välin toinen pää $\mu = 0{,}5$ antaa $50{,}3\,\text{m}$, kuten ratkaisu sanoo. ABS-vertailu ($\mu \approx 0{,}9$) vastaa taulukon lepokitkaa.
- L2-09 laskettu uudelleen: $20\,\text{m} + 25\,\text{m} = 45\,\text{m}$. Kuvan arvot ($20\,\text{m/s}$; $1{,}0\,\text{s}$ ja $3{,}5\,\text{s}$) ovat ruutuviivoilla, joten ne luetaan ±2 %:n sisään. Hidastuvuus $8{,}0\,\text{m/s}^2$ on realistinen.
- L3-06 laskettu uudelleen: $17{,}5 - 7{,}0 = 10{,}5\,\text{kN}$, ja voimien suhde 2,5 vastaa aikojen käänteistä suhdetta.
- Toistoa ei ole: kuvat ovat uusia, eikä mikään aiempi tehtävä käytä niitä. L2-01 (kaava) ja L2-06 / L3-05 (taulukot) ratkaistaan eri tavalla.
- Merkinnät $s_\text{r}$, $s_\text{j}$, $t_\text{r}$, $F_\text{ka}$ ja $\Delta v$ ovat L2-09:ssä ja L3-06:ssa samat kuin luvussa.
- Mallin ehdot (vaakasuora tie, ilmanvastus jätetty huomiotta, $N = mg$) on kerrottu. Sisältö pysyy FY4:n keskeisissä sisällöissä.
