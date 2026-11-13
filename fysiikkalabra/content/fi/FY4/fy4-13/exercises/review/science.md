VERDICT: FAIL
CONTENT-HASH: 491be6e952e2e9c5

## Blocking
- exercises.json fy4-13-L3-06 (punnus $0{,}20\,\text{kg}$), suhteessa tehtävään fy4-13-L2-09 (kärry $0{,}80\,\text{kg}$) — (7, arviointi) molemmat uudet tehtävät käyttävät samaa kuvaa `karry-vt-points`, ja ne kuvaavat samaa koetta. L2-09:n mukaan kärryn massa on $0{,}80\,\text{kg}$, ja kuvan kiihtyvyydellä sen punnukseksi tulisi $0{,}198 \approx 0{,}20\,\text{kg}$. L3-06 antaa punnukseksi $0{,}20\,\text{kg}$ ja kysyy kärryn massaa, jonka vastaus on $0{,}81\,\text{kg}$. Sivulla aiemmin oleva tehtävä kertoo siis L3-06:n vastauksen, ja L3-06:n b-kohdan jännitysvoima ($1{,}57\,\text{N}$) on L2-09:n vastaus. — Erota tilanteet. Anna L3-06:ssa punnukselle eri massa, esim. $0{,}30\,\text{kg}$, jolloin $m_1 = 0{,}30 \cdot (9{,}81/1{,}95 - 1) = 1{,}21\,\text{kg}$ (lukuvälillä $a = 1{,}9$–$2{,}0\,\text{m/s}^2$ tulos on $1{,}17$–$1{,}25\,\text{kg}$, eli ±4 % riittää). Päivitä vastaus, ratkaisu, voimakuvion luvut ja answers.py. Toinen vaihtoehto on vaihtaa L2-09:n kärryn massa.

## Polish
- solutions.md fy4-13-L2-09 ja fy4-13-L3-06 Kuvaajan lukeminen — kulmakerroin lasketaan raakapisteestä $(2{,}0;\,3{,}9)$ ja origosta. Guardrailien mukaan kulmakerroin luetaan sovitetulta suoralta. — Lisää: "piirretään pisteiden kautta origon kautta kulkeva suora ja luetaan siltä piste $(2{,}0\,\text{s};\,3{,}9\,\text{m/s})$". Sovitus antaa saman tuloksen, $1{,}95\,\text{m/s}^2$.

## Checked
- L2-09 laskettu uudelleen: $a = 1{,}95\,\text{m/s}^2$ (pienimmän neliösumman suora origon kautta antaa $1{,}953$) ja $T = m_1 a = 1{,}56\,\text{N}$; täsmää answers.py:n kanssa.
- L3-06 laskettu uudelleen: $m_1 = m_2(g/a - 1) = 0{,}806\,\text{kg}$. b) $T = 1{,}57\,\text{N} < m_2 g = 1{,}96\,\text{N}$, ja perustelu ($m_2 g - T = m_2 a > 0$) on oikein ja sama kuin luvun virhekäsitysosiossa.
- Luettavuus: $2{,}9$ ja $3{,}9$ ovat $0{,}5\,\text{m/s}$:n ruutujen välissä. Lukema $3{,}8$–$4{,}0$ antaa L2-09:lle $1{,}52$–$1{,}60\,\text{N}$ ja L3-06:lle $0{,}78$–$0{,}83\,\text{kg}$, eli molemmat pysyvät ±4 %:n toleranssin sisällä. Kuvan kuvaus antaa samat pisteet eikä massaa eikä kiihtyvyyttä.
- Voimakuviot: kärryllä $\overline{G}_1$, $\overline{N}$ ja $\overline{T}_1$ oikealle; punnuksella $\overline{G}_2$ alas ja $\overline{T}_2$ ylös, lyhyempänä. Kuviot vastaavat liikettä, nopeutta tai kiihtyvyyttä ei ole piirretty voimana, ja liikeyhtälöt luetaan kuviosta.
- Merkinnät $m_1$, $m_2$, $T$, $a$, $\overline{T}_1$ ja $\overline{T}_2$ ovat samat kuin luvussa. Mallin ehdot (kevyt ja venymätön lanka, kevyt ja kitkaton väkipyörä, kitkaton rata) on kerrottu.
- Mikään aiempi tehtävä ei käytä tätä kuvaa; vain nämä kaksi uutta tehtävää käyttävät sitä.
