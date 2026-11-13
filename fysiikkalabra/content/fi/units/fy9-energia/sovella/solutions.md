## fy9-energia-s1

### a)
**Annettu:** jääkaapin keskiteho $P_1 = 45\,\text{W}$ koko vuorokauden $t_1 = 24\,\text{h}$; kuusi ledilamppua, kukin $7{,}0\,\text{W}$, aika $t_2 = 5{,}0\,\text{h}$; kahvinkeitin $P_3 = 1{,}0\,\text{kW}$, aika $t_3 = 15\,\text{min}$
**Kysytty:** laitteiden sähköenergia vuorokaudessa $E_\text{tarve}$ kilowattitunteina
**Periaate:** Jokainen laite muuntaa energiaa omalla tehollaan, joten sen energia on teho kertaa käyttöaika (luku *Teho*). Jääkaapin teho on keskiteho, joten sekin kerrotaan koko vuorokaudella. Energiat lasketaan yhteen samassa yksikössä.
**Kaava:** $E = P\,t$ jokaiselle laitteelle, joten $E_\text{tarve} = P_1 t_1 + 6\,P_2 t_2 + P_3 t_3$
**Muunnokset:** Kilowattitunteja varten tehot kilowateiksi ja ajat tunneiksi: $45\,\text{W} = 45 \cdot 0{,}001\,\text{kW} = 0{,}045\,\text{kW}$, $7{,}0\,\text{W} = 0{,}0070\,\text{kW}$ ja $15\,\text{min} = 15 \cdot \tfrac{1}{60}\,\text{h} = 0{,}25\,\text{h}$.
**Sijoitus:** $E_\text{tarve} = 0{,}045\,\text{kW} \cdot 24\,\text{h} + 6 \cdot 0{,}0070\,\text{kW} \cdot 5{,}0\,\text{h} + 1{,}0\,\text{kW} \cdot 0{,}25\,\text{h} = 1{,}08\,\text{kWh} + 0{,}21\,\text{kWh} + 0{,}25\,\text{kWh} = 1{,}54\,\text{kWh}$
**Vastaus:** $E_\text{tarve} \approx 1{,}5\,\text{kWh}$ eli $1{,}54 \cdot 3{,}6\,\text{MJ} \approx 5{,}5\,\text{MJ}$, kaksi merkitsevää numeroa kuten jääkaapin teho $45\,\text{W}$ ja kahvinkeittimen teho $1{,}0\,\text{kW}$.
**Järkevyys:** Jääkaappi käyttää lähes kaksi kolmasosaa energiasta, vaikka sen teho on laitteista toiseksi pienin: se on päällä koko ajan. Kahvinkeittimen suuri teho vaikuttaa vähän, koska se on päällä vain neljännestunnin. Puolitoista kilowattituntia vuorokaudessa on pienen kesämökin tavallinen kulutus.

### b)
**Annettu:** a-kohdasta $E_\text{tarve} = 1{,}54\,\text{kWh}$; akun hyötysuhde $\eta_\text{akku} = 90\,\%$, vaihtosuuntaajan $\eta_\text{v} = 93\,\%$; pilvisen päivän tuotanto $1{,}5\,\text{kWh}$
**Kysytty:** paneelien tarvittava tuotanto $E_\text{paneelit}$ vuorokaudessa ja riittääkö pilvisen päivän tuotanto
**Periaate:** Energia kulkee paneeleista akun ja vaihtosuuntaajan kautta laitteisiin. Vaiheet ovat peräkkäin: akun antama energia on vaihtosuuntaajan ottama energia. Siksi ketjun hyötysuhde on vaiheiden hyötysuhteiden tulo, ja paneelien on tuotettava enemmän kuin laitteet käyttävät (luku *Energiantuotanto ja voimalaitosten hyötysuhde*).
**Kaava:** $\eta = \eta_\text{akku}\,\eta_\text{v} = \dfrac{E_\text{tarve}}{E_\text{paneelit}}$, joten $E_\text{paneelit} = \dfrac{E_\text{tarve}}{\eta_\text{akku}\,\eta_\text{v}}$
**Muunnokset:** $90\,\% = 0{,}90$ ja $93\,\% = 0{,}93$. Energiat pysyvät kilowattitunteina.
**Sijoitus:** $E_\text{paneelit} = \dfrac{1{,}54\,\text{kWh}}{0{,}90 \cdot 0{,}93} = \dfrac{1{,}54\,\text{kWh}}{0{,}837} = 1{,}84\,\text{kWh}$. Pilvisenä päivänä laitteisiin asti tulee $0{,}837 \cdot 1{,}5\,\text{kWh} = 1{,}26\,\text{kWh}$.
**Vastaus:** Paneelien on tuotettava noin $1{,}8\,\text{kWh}$ vuorokaudessa (kaksi merkitsevää numeroa kuten a-kohdan tarve). Pilvisen päivän $1{,}5\,\text{kWh}$ ei riitä: siitä tulee laitteisiin vain noin $1{,}3\,\text{kWh}$, joten puuttuva osa otetaan akusta, jos siellä on aurinkoisen päivän ylijäämää.
**Järkevyys:** Ketjun hyötysuhde $0{,}84$ on pienempi kuin kummankaan vaiheen, kuten kertolaskussa pitää, ja tarve kasvaa noin viidenneksen. Aurinkoisena päivänä laitteisiin tulee $0{,}837 \cdot 5{,}4\,\text{kWh} \approx 4{,}5\,\text{kWh}$, mikä riittää lähes kolmeksi päiväksi.

### c)
**Kysytty:** onko naapurin päätelmä paneelien vuorokauden energiasta oikea
**Periaate:** Teho kertoo, kuinka nopeasti energiaa muuntuu, ja energia on teho kertaa aika (luku *Teho*). Paneelin nimellisteho on suurin teho, jonka se antaa kirkkaassa auringonpaisteessa.
**Mallivastaus:** Väite on väärä, koska siinä teho ja energia sekoitetaan. Kilowatti on tehon yksikkö ja kilowattitunti energian: $1{,}2\,\text{kW}$ tarkoittaa, että paneelit voivat tuottaa enintään $1{,}2\,\text{kWh}$ *tunnissa*. Vuorokauden energia on keskiteho kertaa aika, ja se riippuu siitä, kuinka kauan ja kuinka voimakkaasti aurinko paistaa. Aineiston mukaan aurinkoisena päivänä paneelit tuottivat $5{,}4\,\text{kWh}$, mikä vastaa $5{,}4\,\text{kWh} : 1{,}2\,\text{kW} = 4{,}5$ tuntia täydellä teholla. Pilvisenä päivänä tuotanto $1{,}5\,\text{kWh}$ vastasi vain noin tuntia. Naapurin luku osuu sattumalta lähelle pilvistä päivää, mutta päättely on väärä.

### Yleisiä virheitä
- Jääkaapin keskiteho kerrotaan vain muutamalla tunnilla, koska kompressori ei käy koko ajan; keskiteho ottaa tämän jo huomioon.
- $15\,\text{min}$ kirjoitetaan $0{,}15\,\text{h}$:ksi; oikein $15 \cdot \tfrac{1}{60}\,\text{h} = 0{,}25\,\text{h}$.
- b-kohdassa tarve kerrotaan hyötysuhteilla, jolloin paneelien tuotannoksi tulee tarvetta pienempi luku.
- Hyötysuhteiden häviöt lasketaan yhteen ($10\,\% + 7\,\% = 17\,\%$); tulos on tässä lähellä oikeaa, mutta periaate on väärä.

### Hyväksytään myös
- a-kohdan energia jouleina: $E_\text{tarve} = 1{,}54 \cdot 3{,}6\,\text{MJ} \approx 5{,}5\,\text{MJ}$.

## fy9-energia-s2

### a)
**Annettu:** tunnissa poltettavan hakkeen massa $m = 42\,\text{t}$, aika $t = 1\,\text{h}$, lämpöarvo $H = 9{,}5\,\text{MJ/kg}$
**Kysytty:** polttoaineteho $P_0$ megawatteina
**Periaate:** Hakkeesta vapautuva energia on lämpöarvo kertaa palanut massa, koska lämpöarvo on energia kilogrammaa kohti (luku *Polttoaineet ja lämpöarvo*). Polttoaineteho on tämä energia jaettuna ajalla, jossa se vapautuu (luku *Teho*).
**Kaava:** $E = Hm$ ja $P_0 = \dfrac{E}{t}$, joten $P_0 = \dfrac{Hm}{t}$
**Muunnokset:** $42\,\text{t} = 42 \cdot 1000\,\text{kg} = 42\,000\,\text{kg}$, $9{,}5\,\text{MJ/kg} = 9{,}5 \cdot 10^{6}\,\text{J/kg}$ ja $1\,\text{h} = 3600\,\text{s}$; lopuksi $1\,\text{W} = 10^{-6}\,\text{MW}$.
**Sijoitus:** $P_0 = \dfrac{9{,}5 \cdot 10^{6}\,\text{J}/\text{kg} \cdot 42\,000\,\text{kg}}{3600\,\text{s}} = \dfrac{3{,}99 \cdot 10^{11}\,\text{J}}{3600\,\text{s}} = 1{,}108 \cdot 10^{8}\,\text{W} = 110{,}8\,\text{MW}$
**Vastaus:** $P_0 \approx 1{,}1 \cdot 10^{2}\,\text{MW}$, kaksi merkitsevää numeroa kuten lämpöarvo $9{,}5\,\text{MJ/kg}$ ja massa $42\,\text{t}$. Jatkokohdissa käytetään pyöristämätöntä arvoa $110{,}8\,\text{MW}$.
**Järkevyys:** Polttoaineteho on vähän suurempi kuin sähkö- ja kaukolämpötehojen summa $100\,\text{MW}$, kuten energian säilymisen mukaan pitää: loput noin $11\,\text{MW}$ ovat häviöitä. Pyöreillä luvuilla $10\,\text{MJ/kg} \cdot 40\,000\,\text{kg} : 3600\,\text{s} \approx 110\,\text{MW}$.

### b)
**Annettu:** a-kohdasta $P_0 = 110{,}8\,\text{MW}$; sähköteho $P_\text{s} = 30\,\text{MW}$, kaukolämpöteho $P_\text{k} = 70\,\text{MW}$
**Kysytty:** sähköhyötysuhde $\eta_\text{s}$ ja kokonaishyötysuhde $\eta_\text{kok}$ prosentteina
**Periaate:** Hyötysuhde on hyödyksi saadun tehon osuus otetusta tehosta. Sähköhyötysuhteessa hyötyä on vain sähkö, kokonaishyötysuhteessa sähkö ja kaukolämpö yhdessä (luku *Energiantuotanto ja voimalaitosten hyötysuhde*).
**Kaava:** $\eta_\text{s} = \dfrac{P_\text{s}}{P_0}$ ja $\eta_\text{kok} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Muunnokset:** Kaikki tehot ovat megawatteina, joten yksikkö supistuu. Suhdeluku muutetaan prosenteiksi kertomalla luvulla $100\,\%$.
**Sijoitus:** $\eta_\text{s} = \dfrac{30\,\text{MW}}{110{,}8\,\text{MW}} = 0{,}271 = 27{,}1\,\%$ ja $\eta_\text{kok} = \dfrac{30\,\text{MW} + 70\,\text{MW}}{110{,}8\,\text{MW}} = 0{,}902 = 90{,}2\,\%$
**Vastaus:** $\eta_\text{s} \approx 27\,\%$ ja $\eta_\text{kok} \approx 90\,\%$, kaksi merkitsevää numeroa kuten tehot $30\,\text{MW}$ ja $70\,\text{MW}$.
**Järkevyys:** Molemmat ovat alle $100\,\%$. Sähköhyötysuhde on pienempi kuin tavallisen lauhdevoimalan noin $40\,\%$, koska yhteistuotannossa höyry lauhdutetaan kaukolämpöä varten korkeammassa lämpötilassa. Kokonaishyötysuhde $90\,\%$ on yhteistuotannolle tyypillinen.

### c)
**Annettu:** sähköteho $P_\text{s} = 30\,\text{MW}$ ja kaukolämpöteho $P_\text{k} = 70\,\text{MW}$; lauhdevoimalan hyötysuhde $\eta_\text{l} = 38\,\%$, lämpökattilan $\eta_\text{lk} = 90\,\%$; $H = 9{,}5\,\text{MJ/kg}$; aika $t = 1\,\text{h}$
**Kysytty:** erillistuotannossa tunnissa tarvittavan hakkeen massa $m$ tonneina
**Periaate:** Kumpikin laitos tarvitsee polttoainetehon, joka on sen hyötyteho jaettuna sen hyötysuhteella. Laitosten polttoainetehot lasketaan yhteen, ja tunnin energiasta saadaan massa lämpöarvon avulla kuten a-kohdassa.
**Kaava:** $P_0 = \dfrac{P_\text{s}}{\eta_\text{l}} + \dfrac{P_\text{k}}{\eta_\text{lk}}$ ja $P_0\,t = Hm$, joten $m = \dfrac{P_0\,t}{H}$
**Muunnokset:** $38\,\% = 0{,}38$, $90\,\% = 0{,}90$, $1\,\text{MW} = 10^{6}\,\text{W}$, $1\,\text{h} = 3600\,\text{s}$, $9{,}5\,\text{MJ/kg} = 9{,}5 \cdot 10^{6}\,\text{J/kg}$ ja lopuksi $1\,\text{kg} = 0{,}001\,\text{t}$.
**Sijoitus:** $P_0 = \dfrac{30\,\text{MW}}{0{,}38} + \dfrac{70\,\text{MW}}{0{,}90} = 78{,}9\,\text{MW} + 77{,}8\,\text{MW} = 156{,}7\,\text{MW}$ ja $m = \dfrac{156{,}7 \cdot 10^{6}\,\text{W} \cdot 3600\,\text{s}}{9{,}5 \cdot 10^{6}\,\text{J}/\text{kg}} = 59\,390\,\text{kg} = 59{,}4\,\text{t}$
**Vastaus:** noin $59\,\text{t}$ haketta tunnissa, kaksi merkitsevää numeroa kuten tehot ja lämpöarvo. Se on noin $17\,\text{t}$ enemmän kuin yhteistuotannon $42\,\text{t}$.
**Järkevyys:** Erillistuotanto tarvitsee enemmän polttoainetta, koska lauhdevoimalan lauhduttimen lämpö menee hukkaan. Yhteistuotanto säästää $1 - 42 : 59{,}4 \approx 0{,}29$ eli noin kolmanneksen polttoaineesta, mikä on yhteistuotannolle tyypillinen suuruusluokka.

### d)
**Kysytty:** miksi kokonaishyötysuhde laskee kesällä, kun kaukolämpöä tarvitaan vähän
**Periaate:** Hyötysuhde riippuu siitä, mikä lasketaan hyödyksi (luku *Hyötysuhde*). Lämpövoimakone ei voi muuttaa kaikkea lämpöä sähköksi, vaan osa on luovutettava kylmempään ympäristöön (luku *Energiantuotanto ja voimalaitosten hyötysuhde*).
**Mallivastaus:** Höyrykierrosta on joka tapauksessa poistettava lauhduttimessa lämpöä, kun voimala tuottaa sähköä. Talvella tämä lämpö lämmittää kaukolämpövettä ja lasketaan hyödyksi, joten kokonaishyötysuhde on noin $90\,\%$. Kesällä kaukolämpöä tarvitaan vain käyttöveteen, joten suurin osa lauhduttimen lämmöstä on luovutettava ympäristöön, esimerkiksi jäähdytysveteen, hukkalämpönä. Jos sähköteho pysyy $30\,\text{MW}$:ssa, polttoainetta kuluu yhä noin saman verran, mutta hyötyä on vähemmän, ja kokonaishyötysuhde laskee kohti sähköhyötysuhdetta. Siksi yhteistuotantovoimalaa ajetaan lämmön tarpeen mukaan: kesällä pienemmällä teholla tai ei ollenkaan, ja sähkö tuotetaan muualla.

### Yleisiä virheitä
- Tonnit tunnissa jaetaan suoraan tunnilla ilman muunnoksia, jolloin teho saadaan yksikössä $\text{MJ/h}$ ja verrataan megawatteihin.
- Kokonaishyötysuhteeseen lasketaan vain sähkö tai hyötysuhde lasketaan sähkötehosta ($70 : 30$).
- c-kohdassa sähkö- ja lämpöteho lasketaan yhteen ja jaetaan yhdellä hyötysuhteella, vaikka laitoksia on kaksi.
- c-kohdassa hyötysuhteet kerrotaan keskenään, vaikka laitokset eivät ole peräkkäin vaan rinnakkain.

### Hyväksytään myös
- a-kohdassa $P_0 \approx 111\,\text{MW}$ ja jatkokohdat sillä laskettuina: $\eta_\text{s} \approx 27\,\%$ ja $\eta_\text{kok} \approx 90\,\%$.

## fy9-energia-s3

### a)
**Kysytty:** vuorokauden sähkönkulutus $E$ ulkolämpötilan $T$ funktiona kuvaajana ja siihen sovitettu malli
**Kuvaaja:** Vaaka-akselilla on ulkolämpötila $T\ ({}^\circ\text{C})$ ja pystyakselilla vuorokauden kulutus $E\ (\text{kWh})$. Vaaka-akselille tarvitaan negatiivisia lämpötiloja, ja asteikko jatkuu c- ja d-kohtia varten $-30\,{}^\circ\text{C}$:sta $+20\,{}^\circ\text{C}$:seen.

<svg data-fig="fy9-energia-s3-graph" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: talon sähkönkulutus vuorokaudessa E ulkolämpötilan T funktiona. Kahdeksan mustaa pistettä lämpötiloissa −19…2 °C. Pisteisiin on sovitettu laskeva suora, jota on jatkettu katkoviivana molempiin suuntiin. Suora kulkee pisteiden (−20 °C; 191 kWh) ja (0 °C; 93 kWh) kautta; nämä kaksi suoran pistettä on ympyröity, ja niistä luetaan kulmakerroin noin −4,9 kWh asteelta. Lämpötilassa −28 °C suoralta luetaan noin 230 kWh. Suora laskee muun kulutuksen tasolle 12 kWh noin lämpötilassa 17 °C." style="max-width:100%;font-size:24px">
  <line x1="125.5" y1="390" x2="125.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="167" y1="390" x2="167" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="209" y1="390" x2="209" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250.5" y1="390" x2="250.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="292" y1="390" x2="292" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="333.5" y1="390" x2="333.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="390" x2="375" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="417" y1="390" x2="417" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458.5" y1="390" x2="458.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="390" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="326" x2="500" y2="326" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="262" x2="500" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="198" x2="500" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="134" x2="500" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="390" x2="514" y2="390" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,390 L513,396 L513,384 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="391" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="125.5" y1="390" x2="125.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="167" y1="390" x2="167" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144.5" y="399.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="209" y1="390" x2="209" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250.5" y1="390" x2="250.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="228" y="399.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-10$</div></foreignObject>
  <line x1="292" y1="390" x2="292" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="333.5" y1="390" x2="333.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="323.5" y="399.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="375" y1="390" x2="375" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="417" y1="390" x2="417" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="400.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="458.5" y1="390" x2="458.5" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="390" x2="500" y2="397" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="77" y1="326" x2="84" y2="326" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="77" y1="262" x2="84" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="77" y1="198" x2="84" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="183.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="77" y1="134" x2="84" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="119.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="77" y1="70" x2="84" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="532" y="375.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{kWh})$</div></foreignObject>
  <line x1="333.5" y1="390" x2="333.5" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <polyline points="175.5,152 350,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92.5,89.5 175.5,152" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="350,284 483.5,384" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="300.5" cy="246.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250.5" cy="212" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200.5" cy="167.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="175.5" cy="152" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="225.5" cy="191.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="228.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="325.5" cy="262" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350" cy="284" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="167" cy="145.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="333.5" cy="271" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="100.5" y1="96" x2="100.5" y2="390" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="96" x2="100.5" y2="96" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="471" y1="374.5" x2="471" y2="390" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="84" y1="374.5" x2="471" y2="374.5" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="134" y="68.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$230\,\text{kWh}$</div></foreignObject>
  <foreignObject x="125.5" y="341" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$12\,\text{kWh}$</div></foreignObject>
  <foreignObject x="283.5" y="119.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k \approx -4{,}9\,\text{kWh}/{}^\circ\text{C}$</div></foreignObject>
</svg>

Kuvaajassa ympyröidyt kohdat ovat ne kaksi suoran pistettä, joista b-kohdan kulmakerroin luetaan. Katkoviiva on suoran jatke mitatun alueen ulkopuolelle (c- ja d-kohta).

**Mallivastaus:** Pisteet ovat lähes suoralla: kulutus kasvaa tasaisesti, kun ulkolämpötila laskee. Pisteisiin sovitetaan yksi laskeva suora, joka kulkee pisteiden lomitse, eikä pisteitä yhdistetä murtoviivaksi päivien järjestyksessä. Pisteiden pieni heilunta suoran molemmin puolin johtuu esimerkiksi tuulesta, auringosta ja saunomisesta, joita lämpötila ei kerro. Suoraa on kuvassa jatkettu katkoviivana mitatun alueen ulkopuolelle c- ja d-kohtia varten.

### b)
**Annettu:** a-kohdan kuvaaja ja suoralta luetut pisteet; vuorokausi $t = 24\,\text{h}$
**Kysytty:** suoran kulmakerroin $k$ ja lämmitystehon kasvu kelviniä kohti $\dfrac{\Delta P}{\Delta T}$ yksikössä $\text{W/K}$
**Periaate:** Suora kertoo, että vuorokauden energia kasvaa yhtä paljon jokaista lämpötila-asteen laskua kohti. Kulmakerroin on energian muutos asteelta. Koska vuorokauden energia on keskiteho kertaa vuorokauden pituus, tehon muutos saadaan jakamalla energian muutos ajalla (luku *Teho*). Lämpötilaeron muutos on sama celsiusasteina ja kelvineinä.
**Kuvaajan lukeminen:** Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä, ei mittauspisteitä: $(-20\,{}^\circ\text{C};\ 191\,\text{kWh})$ ja $(0\,{}^\circ\text{C};\ 93\,\text{kWh})$.
**Kaava:** $k = \dfrac{\Delta E}{\Delta T}$ ja $P = \dfrac{E}{t}$, joten $\dfrac{\Delta P}{\Delta T} = \dfrac{|k|}{t}$
**Muunnokset:** $1\,\text{kWh} : 1\,\text{h} = 1\,\text{kW} = 1000\,\text{W}$, joten $\text{kWh}$ jaettuna tunneilla antaa kilowatteja. $1\,{}^\circ\text{C}$:n muutos on $1\,\text{K}$.
**Sijoitus:** $k = \dfrac{93\,\text{kWh} - 191\,\text{kWh}}{0\,{}^\circ\text{C} - (-20\,{}^\circ\text{C})} = \dfrac{-98\,\text{kWh}}{20\,{}^\circ\text{C}} = -4{,}9\,\text{kWh}/{}^\circ\text{C}$ ja $\dfrac{\Delta P}{\Delta T} = \dfrac{4{,}9\,\text{kWh}}{24\,\text{h} \cdot 1\,\text{K}} = 0{,}204\,\text{kW}/\text{K} = 204\,\text{W}/\text{K}$
**Vastaus:** Kulmakerroin on noin $-4{,}9\,\text{kWh}$ asteelta vuorokaudessa, eli lämmitysteho kasvaa noin $200\,\text{W}$ jokaista kelviniä kohti, jonka ulkolämpötila laskee. Kaksi merkitsevää numeroa, koska kuvaajalta luettu kulmakerroin on noin $\pm 0{,}2\,\text{kWh}$ asteelta tarkka.
**Järkevyys:** Mallin mukaan lämmitystä tarvitaan alle noin $17\,{}^\circ\text{C}$:n ulkolämpötilassa (d-kohta). Kun ulkona on $-20\,{}^\circ\text{C}$, lämmitysteho on noin $36{,}5\,\text{K} \cdot 0{,}204\,\text{kW}/\text{K} \approx 7{,}5\,\text{kW}$, sama kuin $(191 - 12)\,\text{kWh} : 24\,\text{h} \approx 7{,}5\,\text{kW}$, mikä sopii omakotitalon sähkölämmitykseen. Pienimmän neliösumman suora antaa saman: $-4{,}89\,\text{kWh}$ asteelta eli $204\,\text{W/K}$.

### c)
**Annettu:** a-kohdan suora, b-kohdan kulmakerroin $k = -4{,}9\,\text{kWh}$ asteelta ja suoran piste $(T_0;\ E_0) = (0\,{}^\circ\text{C};\ 93\,\text{kWh})$; arvioitava lämpötila $T = -28\,{}^\circ\text{C}$
**Kysytty:** vuorokauden kulutus $E$ kilowattitunteina ja arvion luotettavuus
**Periaate:** Suora on malli kulutuksesta. Mitatun alueen ulkopuolinen arvo saadaan jatkamalla suoraa eli ekstrapoloimalla, mikä on perusteltua vain, jos sama malli pätee myös siellä.
**Kuvaajan lukeminen:** Katkoviivana jatketulta suoralta luetaan lämpötilan $-28\,{}^\circ\text{C}$ kohdalta noin $230\,\text{kWh}$.
**Kaava:** $E = E_0 + k\,(T - T_0)$, missä $(T_0;\ E_0)$ on suoran tunnettu piste ja $k$ sen kulmakerroin
**Muunnokset:** Ei tarvita: lämpötila ja kulmakerroin ovat samoissa yksiköissä kuin kuvaajassa.
**Sijoitus:** $E = 93\,\text{kWh} + (-4{,}9\,\text{kWh}/{}^\circ\text{C}) \cdot (-28\,{}^\circ\text{C} - 0\,{}^\circ\text{C}) = 93\,\text{kWh} + 137{,}2\,\text{kWh} = 230{,}2\,\text{kWh}$
**Vastaus:** noin $230\,\text{kWh}$ vuorokaudessa, kaksi merkitsevää numeroa kuten kulmakerroin. Arvio on ekstrapolointi $9\,\text{K}$ kylmimmän mittauksen $-19\,{}^\circ\text{C}$ ulkopuolelle. Se pätee, jos lämpöhäviöt kasvavat edelleen suoraan lämpötilaeron mukana; kova tuuli suurentaa kulutusta, ja jos lämmittimien yhteenlaskettu teho on alle noin $9\,\text{kW}$, ne eivät riitä ja sisälämpötila laskee.
**Järkevyys:** Kulutus on suunnilleen kaksi ja puoli kertaa nollan asteen kulutus, ja keskiteho $230\,\text{kWh} : 24\,\text{h} \approx 9{,}6\,\text{kW}$ on omakotitalon sähkölämmityksen yläpäässä. Esimerkkihinnalla $0{,}20\,\text{€/kWh}$ päivä maksaisi noin $46\,\text{€}$.

### d)
**Kysytty:** ulkolämpötila, jossa lämmitystä ei mallin mukaan tarvita, ja miksi se ei ole $21\,{}^\circ\text{C}$
**Periaate:** Kun lämmitystä ei tarvita, kulutus on pelkkä muu sähkönkulutus $E_\text{muu} = 12\,\text{kWh}$, joten suoralta $E = E_0 + kT$ ratkaistaan $T = \dfrac{E_\text{muu} - E_0}{k}$. Energia säilyy: kaikki sisällä käytetty sähköenergia muuttuu lopulta lämmöksi, ja myös ihmiset ja auringonsäteily tuovat taloon energiaa (luku *Energialajit ja energian säilyminen*).
**Mallivastaus:** Jatketulta suoralta luetaan, että kulutus laskee muun kulutuksen tasolle $12\,\text{kWh}$ noin lämpötilassa $16$–$17\,{}^\circ\text{C}$ (suoran yhtälöstä $T = \dfrac{E_\text{muu} - E_0}{k} = \dfrac{12\,\text{kWh} - 93\,\text{kWh}}{-4{,}9\,\text{kWh}/{}^\circ\text{C}} = 16{,}5\,{}^\circ\text{C}$). Talo tarvitsee lämmitystä siis vasta, kun ulkona on kylmempää. Lämpötila on noin $4\,\text{K}$ sisälämpötilaa $21\,{}^\circ\text{C}$ alempi, koska valaistuksen, ruoanlaiton ja laitteiden sähköenergia muuttuu sisällä lämmöksi. Lisäksi asukkaat lämmittävät taloa, ja ikkunoista tuleva auringonsäteily lisää energiaa. Nämä korvaavat pienen lämpötilaeron lämpöhäviöt, joten lämmittimiä tarvitaan vain lopun kattamiseen. Tulos on suuntaa antava: se perustuu talvipäivien suoraan, jota jatketaan pitkälle mitatun alueen ulkopuolelle, eikä aineisto erottele aurinkoa ja tuulta.

### Yleisiä virheitä
- Pisteet yhdistetään murtoviivaksi päivämäärän järjestyksessä, jolloin kuvaaja ei näytä riippuvuutta lämpötilasta.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- b-kohdassa kilowattitunnit tulkitaan suoraan kilowateiksi jakamatta vuorokauden tunneilla, jolloin tulokseksi tulee $4900\,\text{W/K}$.
- c-kohdassa ekstrapolointia ei mainita lainkaan tai tulosta pidetään varmana.
- d-kohdassa vastataan, että lämmitys loppuu $21\,{}^\circ\text{C}$:ssa, koska sisällä on silloin sama lämpötila.

### Hyväksytään myös
- Kulmakerroin $-4{,}7$…$-5{,}1\,\text{kWh}$ asteelta, kun suora on sovitettu silmämääräisesti pisteiden lomitse, ja sen mukaiset tulokset: b-kohdassa $192$–$216\,\text{W/K}$, c-kohdassa $220$–$240\,\text{kWh}$ ja d-kohdassa $15$–$18\,{}^\circ\text{C}$.

## fy9-energia-s4

### a)
**Kysytty:** riittävätkö kaksi tuulivoimalaa ja akku korvaamaan dieselvoimalan
**Periaate:** Vuoden energia on keskiteho kertaa vuoden tunnit (luku *Energiantuotantotavat ja niiden vertailu*). Sähköverkossa tuotannon on kuitenkin vastattava kulutusta joka hetki, joten energian lisäksi on tarkasteltava tehoa ja varastoa.
**Mallivastaus:** Tuulivoimaloiden keskiteho on $P_\text{ka} = k\,N\,P_\text{nim}$ ja vuoden energia $E = P_\text{ka}\,t$, missä keskiteho on osuus $k = 0{,}30$ nimellistehosta, voimaloita on $N = 2$ ja nimellisteho on $P_\text{nim} = 1{,}0\,\text{MW}$. Keskiteho on $0{,}30 \cdot 2 \cdot 1{,}0\,\text{MW} = 0{,}60\,\text{MW}$, joten vuodessa ne tuottavat $0{,}60\,\text{MW} \cdot 8760\,\text{h} \approx 5{,}3\,\text{GWh}$. Se on enemmän kuin saaren kulutus $3{,}0\,\text{GWh}$, joten väitteen ensimmäinen osa pitää vuoden energian osalta. Sähköä ei kuitenkaan voi käyttää silloin, kun sitä tuotetaan vuoden aikana keskimäärin: tyynellä tuulivoimalat eivät tuota mitään. Täysi akku kattaa talven huippukulutuksen vain $2{,}0\,\text{MWh} : 1{,}2\,\text{MW} \approx 1{,}7$ tuntia, ja tyyni pakkasjakso voi kestää päiviä. Dieseliä ei siksi voi purkaa, ellei saarelle saada muuta säätövoimaa tai yhteyttä mantereen verkkoon.

### b)
**Kysytty:** vaihtoehtojen vertailu ainakin kolmella perusteella ja perusteltu suositus
**Periaate:** Tuotantotapoja verrataan samoilla perusteilla: säädettävyys ja toimitusvarmuus, päästöt, polttoaineen kuljetus ja varastointi sekä hinta (luvut *Energiantuotantotavat ja niiden vertailu* ja *Energiantuotanto, ympäristö ja ilmastonmuutos*).
**Mallivastaus:**
- *Säädettävyys ja toimitusvarmuus.* Dieselvoimala on säädettävä ja riittää huippuun ($1{,}5\,\text{MW} > 1{,}2\,\text{MW}$). Tuulivoima on sääriippuvaista, eikä akku kata pitkää tyyntä. Kaapeli tuo saarelle koko mantereen verkon säätövoiman, ja sen $5\,\text{MW}$ riittää huippuun.
- *Päästöt.* Diesel tuottaa noin $2100\,\text{t}$ hiilidioksidia vuodessa (c-kohta). Tuulivoiman elinkaaren päästöt ovat siitä vain pieni osa, ja kaapelin sähkön päästöt riippuvat mantereen tuotantotavoista.
- *Kuljetus ja häviöt.* Diesel on tuotava laivalla, mikä on kallista ja altis jäätalvelle. Kaapelin siirtohäviö on vain noin $3\,\%$: saaren $3{,}0\,\text{GWh}$:a varten mantereelta lähetetään noin $3{,}1\,\text{GWh}$.
- *Hinta.* Kaapeli ja tuulivoimalat ovat suuria investointeja, mutta niissä ei ole polttoainekuluja.

Suositus: merikaapeli ja tuulivoimalat yhdessä. Kaapeli takaa sähkön tyynellä ja vie ylijäämän mantereelle, tuulivoima vähentää päästöjä, ja nykyinen dieselvoimala jää varavoimaksi kaapelivian varalle.

### c)
**Kysytty:** dieselvoimalan vuotuinen hiilidioksidipäästö ja arvio väitteestä ”tuulivoima on täysin päästötöntä”
**Periaate:** Päästö on energia kertaa päästökerroin, $m = e \cdot E$. Tuotantotapoja verrataan elinkaaren päästöillä, joihin kuuluvat myös rakentaminen, kuljetukset ja purku (luku *Energiantuotanto, ympäristö ja ilmastonmuutos*).
**Mallivastaus:** Kulutus kilowattitunteina on $3{,}0\,\text{GWh} = 3{,}0 \cdot 10^{6}\,\text{kWh}$, joten dieselvoimalan päästö on $m = e \cdot E = 700\,\text{g}/\text{kWh} \cdot 3{,}0 \cdot 10^{6}\,\text{kWh} = 2{,}1 \cdot 10^{9}\,\text{g}$. Sijoitetaan $1\,\text{g} = 10^{-6}\,\text{t}$: päästö on noin $2100\,\text{t}$ hiilidioksidia vuodessa. Tuulivoimala ei käytössä polta mitään, mutta sen teräksen ja betonin valmistus, kuljetus, rakentaminen ja purku aiheuttavat päästöjä. Elinkaaren päästökerroin on siksi muutamia kymmeniä grammoja kilowattituntia kohti tai vähemmän, ei nolla. Väite on siis epätarkka: tuulivoima on vähäpäästöistä, ja sen päästöt ovat vain murto-osa dieselin päästöistä, mutta täysin päästötöntä se ei ole.

### Yleisiä virheitä
- a-kohdassa tuulivoimaloiden vuoden energia lasketaan nimellisteholla ($2{,}0\,\text{MW} \cdot 8760\,\text{h} = 17{,}5\,\text{GWh}$), jolloin keskitehoa ei oteta huomioon.
- Akun kapasiteettia ($\text{MWh}$) verrataan suoraan kulutushuippuun ($\text{MW}$), vaikka toinen on energia ja toinen teho.
- b-kohdassa luetellaan vaihtoehtojen ominaisuuksia vertaamatta niitä toisiinsa tai tekemättä suositusta.
- c-kohdassa gigawattitunnit kerrotaan suoraan päästökertoimella ilman muunnosta kilowattitunneiksi.

## fy9-energia-s5

### a)
**Annettu:** raportista vesi $m = 1{,}0\,\text{kg}$, alkulämpötila $T_1 = 15\,{}^\circ\text{C}$, loppulämpötila $T_2 = 96\,{}^\circ\text{C}$, aika $t = 3\,\text{min}\ 5\,\text{s}$, arvokilven teho $P = 2200\,\text{W}$; $c = 4190\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** keittimen hyötysuhde $\eta$ raportin tiedoista
**Periaate:** Hyötysuhde on veteen siirtyneen energian osuus keittimen ottamasta sähköenergiasta (luku *Hyötysuhde*). Veteen siirtynyt energia on vedelle siirtynyt lämpömäärä $Q = cm\Delta T$, koska vesi lämpenee eikä raportin mukaan kiehu pois (luku *Aineen lämpeneminen ja jäähtyminen*). Sähköenergia on teho kertaa aika.
**Kaava:** $\eta = \dfrac{Q}{E}$, missä $Q = cm\,(T_2 - T_1)$ ja $E = P\,t$, joten $\eta = \dfrac{cm\,(T_2 - T_1)}{P\,t}$
**Muunnokset:** $3\,\text{min}\ 5\,\text{s} = 3 \cdot 60\,\text{s} + 5\,\text{s} = 185\,\text{s}$. Lämpötilaero on sama celsiusasteina ja kelvineinä: $96\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 81\,\text{K}$.
**Sijoitus:** $\eta = \dfrac{4190\,\text{J}/(\text{kg} \cdot \text{K}) \cdot 1{,}0\,\text{kg} \cdot 81\,\text{K}}{2200\,\text{W} \cdot 185\,\text{s}} = \dfrac{339\,390\,\text{J}}{407\,000\,\text{J}} = 0{,}834 = 83{,}4\,\%$
**Vastaus:** $\eta \approx 83\,\%$, kaksi merkitsevää numeroa kuten vesimäärä $1{,}0\,\text{kg}$ ja lämpötilaero $81\,\text{K}$. Ryhmän luku on laskettu oikein.
**Järkevyys:** Hyötysuhde on alle $100\,\%$ ja vedenkeittimelle tavallista suuruusluokkaa: lämmityselementti on veden sisällä, joten suurin osa energiasta päätyy veteen. Häviöiksi jää $407\,\text{kJ} - 339\,\text{kJ} \approx 68\,\text{kJ}$, joka lämmittää kannua ja ilmaa.

### b)
**Kysytty:** onko johtopäätös perusteltu, mittauksen tärkeimmät virhelähteet ja niiden vaikutuksen suunta
**Periaate:** Johtopäätös on perusteltu vain, jos ero väitettyyn arvoon on suurempi kuin tuloksen epävarmuus (luku *Mittaaminen ja mittauksen luotettavuus*). Virhelähteen vaikutus arvioidaan laskemalla tulos uudelleen muutetulla arvolla.
**Mallivastaus:** Ryhmän johtopäätös ei ole perusteltu, koska tuloksen epävarmuus on useita prosenttiyksiköitä ja mittaus tehtiin vain kerran.
- *Teho arvokilvestä.* Arvokilven teho on nimellisarvo, ei mitattu, ja todellinen teho riippuu verkkojännitteestä. Jos se olisi $2100\,\text{W}$, hyötysuhteeksi tulisi $87\,\%$; jos yli $2200\,\text{W}$, tulos olisi alle $83\,\%$. Sähköenergia pitäisi mitata energiamittarilla.
- *Loppulämpötila.* Vesi kiehui eli oli noin $100\,{}^\circ\text{C}$, kun keitin sammui, mutta lämpötila mitattiin vasta kannen avaamisen jälkeen. Mittaus antaa liian pienen lämpötilaeron ja siksi liian pienen hyötysuhteen; $100\,{}^\circ\text{C}$:lla tulos olisi $88\,\%$.
- *Vesimäärä.* Kannun asteikko on epätarkka. Jos vettä oli $1{,}05\,\text{kg}$, tulos olisi $88\,\%$; jos $0{,}95\,\text{kg}$, se olisi $79\,\%$. Vesi pitäisi punnita.
- *Kannun lämpeneminen ja höyrystyminen.* Osa energiasta lämmittää kannua ja osa höyrystää vettä kiehumisen aikana. Ne ovat todellisia häviöitä, mutta riippuvat siitä, mitä valmistaja laskee hyödyksi.

Myöhään luettu loppulämpötila pienentää tulosta varmasti. Arvokilven teho ja kannun asteikko voivat muuttaa sitä kumpaan suuntaan tahansa: todellinen teho riippuu verkkojännitteestä ja voi olla yli tai alle $2200\,\text{W}$. Todellinen hyötysuhde voi siis hyvin olla lähellä $90\,\%$. Väitteen kumoamiseen tarvitaan mitattu sähköenergia, punnittu vesi ja useita toistoja.

### c)
**Kysytty:** koesuunnitelma, jolla selvitetään, riippuuko hyötysuhde vesimäärästä
**Periaate:** Kokeessa muutetaan vain yhtä muuttujaa, vesimäärää, ja pidetään muut vakioina. Suureet mitataan mahdollisimman suoraan, ja mittaukset toistetaan, jotta satunnaisen vaihtelun suuruus nähdään (luku *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:**
- *Muuttujat.* Muutettava suure on veden massa, esimerkiksi $0{,}50\,\text{kg}$, $0{,}75\,\text{kg}$, $1{,}0\,\text{kg}$, $1{,}25\,\text{kg}$ ja $1{,}5\,\text{kg}$. Vakiona pidetään sama keitin, sama alkulämpötila (vesi samasta astiasta), kansi kiinni ja keittimen alkulämpötila: kannun annetaan jäähtyä huoneenlämpöiseksi tai se huuhdellaan kylmällä vedellä mittausten välissä.
- *Mittaukset.* Vesi punnitaan vaa'alla. Keitin kytketään energiamittarin kautta, joka näyttää sähköenergian suoraan. Lämmitys lopetetaan ennen kiehumista, esimerkiksi kun sekoitetun veden lämpötila on $80\,{}^\circ\text{C}$, jotta höyrystyminen ei vääristä tulosta; lämpötila mitataan heti katkaisun jälkeen sekoittaen.
- *Toistot ja tulokset.* Jokainen vesimäärä mitataan kolme kertaa. Hyötysuhde lasketaan kaavalla $\eta = \tfrac{cm\Delta T}{E}$, ja tulokset esitetään kuvaajana hyötysuhde vesimäärän funktiona toistojen hajonnan kanssa.

Jos hyötysuhde kasvaa vesimäärän kasvaessa, syy on todennäköisesti kannun lämpeneminen: se vie lähes saman energian joka kerta, joten se on suurempi osa pienen vesimäärän energiasta.

### Yleisiä virheitä
- a-kohdassa lämpötilaero muutetaan kelvineiksi lisäämällä $273$ kumpaankin lämpötilaan eri tavalla tai käytetään loppulämpötilaa $96\,{}^\circ\text{C}$ lämpötilaerona.
- Aika kirjoitetaan $3{,}5\,\text{min}$:ksi; $3\,\text{min}\ 5\,\text{s}$ on $185\,\text{s}$.
- b-kohdassa todetaan vain ”mittausvirheitä oli”, nimeämättä virhelähdettä tai sen vaikutuksen suuntaa.
- c-kohdassa muutetaan samaan aikaan vesimäärää ja keitintä tai lämmitetään eri lämpötiloihin, jolloin vaikutuksia ei voi erottaa.

### Hyväksytään myös
- c-kohdassa lämmityksen voi lopettaa myös keittimen sammumiseen, jos loppulämpötila mitataan heti ja kannen ollessa kiinni, ja suunnitelma toteaa höyrystymisen vaikutuksen.

## fy9-energia-s6

### a)
**Annettu:** yläaltaan tilavuus $V = 7{,}50 \cdot 10^{4}\,\text{m}^3$, veden tiheys $\rho = 1000\,\text{kg/m}^3$, korkeusero $h = 1{,}20\,\text{km}$, $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** veden potentiaalienergia $E_\text{p}$ ala-altaaseen verrattuna megawattitunteina
**Periaate:** Kun ala-allas valitaan nollatasoksi, korkeudella $h$ olevan veden potentiaalienergia on yhtä suuri kuin työ, joka tarvitaan sen nostamiseen tasaisesti ylös, $mgh$ (luvut *Työ ja energia* ja *Liike-energia, potentiaalienergia ja mekaaninen energia*). Altaan korkeus on pieni korkeuseroon verrattuna, joten kaikki vesi on noin korkeudella $h$.
**Kaava:** $m = \rho V$ ja $E_\text{p} = mgh$, joten $E_\text{p} = \rho V g h$
**Muunnokset:** $1{,}20\,\text{km} = 1{,}20 \cdot 1000\,\text{m} = 1200\,\text{m}$. Megawattitunti sijoittamalla: $1\,\text{MWh} = 10^{6}\,\text{W} \cdot 3600\,\text{s} = 3{,}6 \cdot 10^{9}\,\text{J}$.
**Sijoitus:** $E_\text{p} = 1000\,\text{kg}/\text{m}^3 \cdot 7{,}50 \cdot 10^{4}\,\text{m}^3 \cdot 9{,}81\,\text{m}/\text{s}^2 \cdot 1200\,\text{m} = 8{,}829 \cdot 10^{11}\,\text{J} = \dfrac{8{,}829 \cdot 10^{11}}{3{,}6 \cdot 10^{9}}\,\text{MWh} = 245{,}3\,\text{MWh}$
**Vastaus:** $E_\text{p} \approx 245\,\text{MWh}$, kolme merkitsevää numeroa kuten tilavuus $7{,}50 \cdot 10^{4}\,\text{m}^3$ ja korkeusero $1{,}20\,\text{km}$.
**Järkevyys:** Kilogramma vettä saa $1200\,\text{m}$:n pudotuksesta noin $12\,\text{kJ}$, eli yksi kuutio noin $12\,\text{MJ} \approx 3{,}3\,\text{kWh}$. $75\,000$ kuutiota antaa siis noin $250\,\text{MWh}$, sama suuruusluokka.

### b)
**Annettu:** a-kohdasta $E_\text{p} = 245{,}3\,\text{MWh}$; turbiinin ja generaattorin hyötysuhde $\eta_\text{t} = 88\,\%$; tyhjennysaika $t = 6{,}0\,\text{h}$
**Kysytty:** voimalan sähköteho $P$ megawatteina
**Periaate:** Turbiini ja generaattori muuttavat virtaavan veden energian sähköksi, ja hyötysuhde kertoo sähköksi tulevan osuuden. Allas tyhjennetään tasaisesti, joten teho on sähköenergia jaettuna ajalla (luku *Teho*).
**Kaava:** $E_\text{s} = \eta_\text{t}\,E_\text{p}$ ja $P = \dfrac{E_\text{s}}{t}$, joten $P = \dfrac{\eta_\text{t}\,E_\text{p}}{t}$
**Muunnokset:** $88\,\% = 0{,}88$. Megawattitunnit jaettuna tunneilla antaa suoraan megawatteja: $\text{MWh} : \text{h} = \text{MW}$.
**Sijoitus:** $P = \dfrac{0{,}88 \cdot 245{,}3\,\text{MWh}}{6{,}0\,\text{h}} = \dfrac{215{,}8\,\text{MWh}}{6{,}0\,\text{h}} = 35{,}97\,\text{MW}$
**Vastaus:** $P \approx 36\,\text{MW}$, kaksi merkitsevää numeroa kuten tyhjennysaika $6{,}0\,\text{h}$ ja hyötysuhde $88\,\%$.
**Järkevyys:** Teho vastaa noin kymmentä suurta tuulivoimalaa tai noin $16\,000$ vedenkeitintä. Sähköenergia $216\,\text{MWh}$ on pienempi kuin potentiaalienergia $245\,\text{MWh}$, kuten energian säilymisen ja häviöiden mukaan pitää.

### c)
**Annettu:** $E_\text{p} = 245{,}3\,\text{MWh}$; pumpun ja moottorin hyötysuhde $\eta_\text{p} = 85\,\%$; b-kohdasta $\eta_\text{t} = 88\,\%$ ja sähköenergia $E_\text{s} = 215{,}8\,\text{MWh}$
**Kysytty:** pumppaukseen verkosta otettava sähköenergia $E_\text{verkko}$ ja varaston kokonaishyötysuhde $\eta$
**Periaate:** Pumppauksessa sähköenergia muuttuu veden potentiaalienergiaksi, ja vain osa $\eta_\text{p}$ siitä tulee hyödyksi, joten verkosta on otettava enemmän kuin vedelle tulee potentiaalienergiaa. Täyttö ja tyhjennys ovat peräkkäiset vaiheet, joten kokonaishyötysuhde on niiden tulo (luku *Energiantuotanto ja voimalaitosten hyötysuhde*).
**Kaava:** $\eta_\text{p} = \dfrac{E_\text{p}}{E_\text{verkko}}$, joten $E_\text{verkko} = \dfrac{E_\text{p}}{\eta_\text{p}}$, ja $\eta = \eta_\text{p}\,\eta_\text{t}$
**Muunnokset:** $85\,\% = 0{,}85$ ja $88\,\% = 0{,}88$; energiat pysyvät megawattitunteina.
**Sijoitus:** $E_\text{verkko} = \dfrac{245{,}3\,\text{MWh}}{0{,}85} = 288{,}5\,\text{MWh}$ ja $\eta = 0{,}85 \cdot 0{,}88 = 0{,}748 = 74{,}8\,\%$
**Vastaus:** Verkosta otetaan noin $290\,\text{MWh}$ (kaksi merkitsevää numeroa kuten hyötysuhde $85\,\%$; tarkemmin $289\,\text{MWh}$), ja kokonaishyötysuhde on noin $75\,\%$.
**Järkevyys:** Tarkistus energioista: $E_\text{s} : E_\text{verkko} = 215{,}8\,\text{MWh} : 288{,}5\,\text{MWh} = 0{,}748$, sama kuin hyötysuhteiden tulo. Noin neljännes energiasta muuttuu putkissa, pumpussa, turbiinissa ja generaattoreissa lämmöksi, mikä on pumppuvoimaloille tyypillistä.

### d)
**Kysytty:** pitääkö väite ”voimala tuottaa joka päivä $216\,\text{MWh}$ sähköä”, ja miksi voimala silti voi olla hyödyllinen
**Periaate:** Energia säilyy: voimala voi antaa sähkönä enintään sen energian, joka siihen on pumppaamalla varastoitu, ja häviöiden takia vähemmän (luku *Energialajit ja energian säilyminen*). Varasto siirtää energiaa ajassa (luku *Energian siirtäminen: sähkö ja lämpö*).
**Mallivastaus:** Väite on harhaanjohtava. Pumppuvoimala ei tuota energiaa vaan varastoi sitä: jokaisella täytöllä ja tyhjennyksellä se ottaa verkosta noin $289\,\text{MWh}$ ja antaa takaisin noin $216\,\text{MWh}$, joten noin $73\,\text{MWh}$ muuttuu lämmöksi. Voimala on silti hyödyllinen, koska se siirtää energiaa ajassa. Se täytetään, kun sähköä on tarjolla paljon ja halvalla, esimerkiksi tuulisena yönä, ja se tyhjennetään kulutushuipun aikaan tai tyynellä, kun sähköä on niukasti. Vesivoimana se on myös nopeasti säädettävää tehoa, jota sääriippuvainen tuulivoima tarvitsee rinnalleen. Oikea muotoilu olisi: ”Voimala antaa verkkoon $216\,\text{MWh}$ ottamaansa $289\,\text{MWh}$:a myöhemmin, silloin kun sähköä tarvitaan.”

### Yleisiä virheitä
- a-kohdassa massa lasketaan suoraan tilavuudesta ilman tiheyttä tai kilometrit unohdetaan muuntaa metreiksi.
- Joulet muunnetaan megawattitunneiksi jakamalla luvulla $3600$ tai $10^{6}$, mutta ei molemmilla.
- c-kohdassa potentiaalienergia kerrotaan pumpun hyötysuhteella, jolloin verkosta otettu energia olisi pienempi kuin vedelle varastoitunut.
- Kokonaishyötysuhde lasketaan keskiarvona $(85\,\% + 88\,\%) : 2$ tai yhteenlaskuna eikä tulona.

### Hyväksytään myös
- c-kohdan energia kolmella merkitsevällä numerolla $289\,\text{MWh}$ ja kokonaishyötysuhde $74{,}8\,\%$.
