## fy9-lampo-s1

### a)
**Annettu:** ala $A = 1800\,\text{m}^2$, vesikerroksen paksuus $d = 3{,}00\,\text{cm}$, veden tiheys $\rho = 1000\,\text{kg/m}^3$; vesi $15{,}0\,{}^\circ\text{C}$, valmis jää $-4{,}0\,{}^\circ\text{C}$; $c_\text{v} = 4190\,\text{J/(kg}\cdot\text{K)}$, $c_\text{j} = 2100\,\text{J/(kg}\cdot\text{K)}$, $s = 334\,\text{kJ/kg}$
**Kysytty:** lämpömäärä $Q$, joka on poistettava, gigajouleina
**Periaate:** Energia säilyy. Vesi muuttuu $15{,}0\,{}^\circ\text{C}$:n vedestä $-4{,}0\,{}^\circ\text{C}$:n jääksi, ja samalla se luovuttaa energiaa. Kylmäkoneen on poistettava kaikki tämä energia. Muutoksessa on kolme vaihetta. Ensin vesi jäähtyy $0\,{}^\circ\text{C}$:seen ($Q = cm\Delta T$). Sitten vesi jäätyy, ja lämpötila pysyy samana. Silloin vesi luovuttaa sulamislämmön ($Q = sm$). Lopuksi jää jäähtyy $-4{,}0\,{}^\circ\text{C}$:seen ($Q = cm\Delta T$). Sana vähintään tarkoittaa, että halliin johtuvaa lämpöä ei lasketa mukaan.
**Kaava:** $m = \rho A d$ ja $Q = c_\text{v} m\,\Delta T_\text{v} + s m + c_\text{j} m\,\Delta T_\text{j}$, joten $Q = \rho A d\,(c_\text{v}\,\Delta T_\text{v} + s + c_\text{j}\,\Delta T_\text{j})$
**Muunnokset:** $3{,}00\,\text{cm} = 3{,}00 \cdot 0{,}01\,\text{m} = 0{,}0300\,\text{m}$ ja $334\,\text{kJ/kg} = 334\,000\,\text{J/kg}$. Lämpötilan muutokset ovat samat kelvineinä: $\Delta T_\text{v} = 15{,}0\,\text{K}$ ja $\Delta T_\text{j} = 4{,}0\,\text{K}$. Lopuksi $1\,\text{GJ} = 10^{9}\,\text{J}$.
**Sijoitus:** $m = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1800\,\text{m}^2 \cdot 0{,}0300\,\text{m} = 54\,000\,\text{kg}$ ja $Q = 54\,000\,\text{kg} \cdot (4190 \cdot 15{,}0 + 334\,000 + 2100 \cdot 4{,}0)\,\tfrac{\text{J}}{\text{kg}} = 54\,000\,\text{kg} \cdot 405\,250\,\tfrac{\text{J}}{\text{kg}} = 2{,}188 \cdot 10^{10}\,\text{J} = 21{,}9\,\text{GJ}$
**Vastaus:** $21{,}9\,\text{GJ}$. Vastauksessa on kolme merkitsevää numeroa, kuten kerroksen paksuudessa $3{,}00\,\text{cm}$ ja veden lämpötilassa $15{,}0\,{}^\circ\text{C}$. Jään jäähtymisessä $4{,}0\,\text{K}$ on vain kaksi numeroa, mutta se koskee vain pientä termiä.
**Järkevyys:** Vaiheittain $Q_\text{v} = 3{,}39\,\text{GJ}$, $Q_\text{s} = 18{,}0\,\text{GJ}$ ja $Q_\text{j} = 0{,}454\,\text{GJ}$. Niiden summa on sama $21{,}9\,\text{GJ}$. Pyöristetyillä luvuilla $54\,\text{t} \cdot 400\,\text{kJ/kg} \approx 22\,\text{GJ}$. Kilowattitunteina se on noin $6100\,\text{kWh}$. Se on suunnilleen sama kuin omakotitalon sähkönkulutus vuodessa. Tämä sopii suureen jääalaan.

### b)
**Annettu:** a-kohdan $Q = 2{,}188 \cdot 10^{10}\,\text{J}$, kylmäkoneen teho $P = 350\,\text{kW}$
**Kysytty:** kuinka kauan jäädyttäminen kestää, $t$ tunteina
**Periaate:** Kylmäkone poistaa energiaa tasaisella teholla. Siksi aika saadaan, kun poistettava energia jaetaan teholla (luku *Teho*). Tulos on alaraja eli pienin mahdollinen aika. Syy on se, että kone poistaa samalla myös lämpöä, joka johtuu halliin ja betoniin.
**Kaava:** $P = \dfrac{Q}{t}$, joten $t = \dfrac{Q}{P}$
**Muunnokset:** $350\,\text{kW} = 350 \cdot 1000\,\text{W} = 350\,000\,\text{W}$ ja lopuksi $1\,\text{h} = 3600\,\text{s}$.
**Sijoitus:** $t = \dfrac{2{,}188 \cdot 10^{10}\,\text{J}}{350\,000\,\text{W}} = 62\,500\,\text{s} = 62\,500 \cdot \tfrac{1}{3600}\,\text{h} = 17{,}4\,\text{h}$
**Vastaus:** vähintään $17{,}4\,\text{h}$. Vastauksessa on kolme merkitsevää numeroa, kuten tehossa $350\,\text{kW}$ ja a-kohdan tuloksessa.
**Järkevyys:** On uskottavaa, että uuden jään tekeminen kestää noin vuorokauden. Todellisuudessa aikaa kuluu enemmän, koska kerrokset ruiskutetaan vähitellen ja hallin ilma lämmittää jäätä. Tarkistus: $350\,\text{kW} \cdot 17{,}4\,\text{h} \approx 6100\,\text{kWh} \approx 21{,}9\,\text{GJ}$.

### c)
**Kysytty:** onko jäätyminen nopea vaihe, kun vesi on jo $0\,{}^\circ\text{C}$:ssa
**Periaate:** Kun vesi jäätyy, se luovuttaa sulamislämmön, vaikka lämpötila pysyy $0\,{}^\circ\text{C}$:ssa. Hiukkaset asettuvat säännölliseen järjestykseen, ja niiden välinen vuorovaikutusenergia pienenee. Kylmäkoneen on poistettava tämä energia samalla teholla kuin muunkin energian (luku *Olomuodon muutokset*).
**Mallivastaus:** Väite on väärä. Katsotaan a-kohdan vaiheita. Jäätyminen vaatii $18{,}0\,\text{GJ}$ eli noin $82\,\%$ kokonaislämmöstä. Veden jäähtyminen $15{,}0\,{}^\circ\text{C}$:sta $0\,{}^\circ\text{C}$:seen vaatii vain noin $16\,\%$ ja jään jäähtyminen noin $2\,\%$. Teholla $350\,\text{kW}$ veden jäähdyttäminen kestää noin $2{,}7\,\text{h}$, mutta jäätyminen noin $14\,\text{h}$. Lämpötila ei muutu jäätymisen aikana, mutta energiaa on silti poistettava. Jäätyminen vapauttaa jokaisesta kilogrammasta $334\,\text{kJ}$. Se on yhtä paljon kuin vesi luovuttaa, kun se jäähtyy lähes $80\,\text{K}$. Jäätyminen on siis jäädytyksen hitain vaihe. Jäämestarin ei kannata odottaa, että se käy hetkessä.

### Yleisiä virheitä
- Jäätymisen sulamislämpö unohdetaan, koska lämpötila ei muutu. Silloin tulokseksi tulee vain noin $3{,}8\,\text{GJ}$.
- Paksuutta ei muunneta metreiksi. Silloin massa on sata kertaa liian suuri.
- Jään jäähtymisessä käytetään veden ominaislämpökapasiteettia.
- b-kohdassa tulos jätetään sekunneiksi tai teho jätetään kilowateiksi. Silloin vastauksen yksikkö on väärä.
- c-kohdassa väitettä arvioidaan ilman lukuja.

### Hyväksytään myös
- a-kohdassa vaiheet voi laskea erikseen ja laskea ne yhteen. Vastaus $22\,\text{GJ}$ kahden merkitsevän numeron tarkkuudella hyväksytään, kun perusteluna on jään lämpötila $-4{,}0\,{}^\circ\text{C}$.

## fy9-lampo-s2

### a)
**Annettu:** koivuklapien massa $m_\text{p} = 12{,}0\,\text{kg}$, lämpöarvo $H = 15\,\text{MJ/kg}$, kiveen siirtyvä osuus $\eta = 80\,\%$; kivimassa $m_\text{k} = 1800\,\text{kg}$, $c = 980\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** kuinka paljon kivimassan keskimääräinen lämpötila nousee, $\Delta T$
**Periaate:** Kun puu palaa, se vapauttaa energian $Hm$ (luku *Polttoaineet ja lämpöarvo*). Tästä energiasta $80\,\%$ siirtyy kiveen. Loput lähtee savukaasujen mukana piippuun. Kivi pysyy kiinteänä. Siksi kiven vastaanottama lämpö nostaa sen lämpötilaa kaavan $Q = cm\Delta T$ mukaan (luku *Aineen lämpeneminen ja jäähtyminen*). Lämmityksen aikana kivestä johtuu jo vähän lämpöä huoneeseen. Sitä ei oteta huomioon.
**Kaava:** $Q = \eta H m_\text{p}$ ja $Q = c\,m_\text{k}\,\Delta T$, joten $\Delta T = \dfrac{\eta H m_\text{p}}{c\,m_\text{k}}$
**Muunnokset:** $15\,\text{MJ/kg} = 15 \cdot 10^{6}\,\text{J/kg}$ ja $80\,\% = 0{,}80$.
**Sijoitus:** $\Delta T = \dfrac{0{,}80 \cdot 15 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} \cdot 12{,}0\,\text{kg}}{980\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 1800\,\text{kg}} = \dfrac{1{,}44 \cdot 10^{8}\,\text{J}}{1{,}764 \cdot 10^{6}\,\tfrac{\text{J}}{\text{K}}} = 81{,}6\,\text{K}$
**Vastaus:** noin $82\,\text{K}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lämpöarvossa $15\,\text{MJ/kg}$ ja osuudessa $80\,\%$. Tulos on keskiarvo. Kivimassan sisäosat lämpenevät enemmän kuin pinta.
**Järkevyys:** Jos kivi on aamulla $25\,{}^\circ\text{C}$:ista, sen keskilämpötila nousee noin $105\,{}^\circ\text{C}$:seen. Takan pinta tuntuu silloin kuumalta, mutta se ei polta. Syy on se, että pinta on kylmempi kuin sisäosat. Kivimassan lämpökapasiteetti $1{,}76\,\text{MJ/K}$ on suuri. Siksi $144\,\text{MJ}$ ei nosta lämpötilaa satoja asteita.

### b)
**Annettu:** a-kohdan $Q = 144\,\text{MJ}$, aika $t = 24\,\text{h}$
**Kysytty:** keskimääräinen lämmitysteho $P$ kilowatteina
**Periaate:** Vuorokauden aikana kivi jäähtyy takaisin alkulämpötilaansa. Siksi se luovuttaa huoneisiin saman energian, jonka se sai. Keskiteho on energia jaettuna ajalla (luku *Teho*).
**Kaava:** $P = \dfrac{Q}{t}$
**Muunnokset:** $144\,\text{MJ} = 144 \cdot 10^{6}\,\text{J}$ ja $24\,\text{h} = 24 \cdot 3600\,\text{s} = 86\,400\,\text{s}$; lopuksi $1\,\text{W} = 0{,}001\,\text{kW}$.
**Sijoitus:** $P = \dfrac{144 \cdot 10^{6}\,\text{J}}{86\,400\,\text{s}} = 1667\,\text{W} = 1{,}67\,\text{kW}$
**Vastaus:** noin $1{,}7\,\text{kW}$. Vastauksessa on kaksi merkitsevää numeroa, kuten a-kohdan lähtötiedoissa.
**Järkevyys:** Teho on sama kuin yhden tai kahden sähköpatterin teho. Se on tavallinen tulisijan keskiteho. Teho ei ole vakio. Heti lämmityksen jälkeen kivi on kuumimmillaan, ja silloin se luovuttaa enemmän.

### c)
**Annettu:** lämpöhäviö $k_\text{h} = 150\,\text{W/K}$ eli $150\,\text{W}$ kelviniä kohti, sisällä $21\,{}^\circ\text{C}$, ulkona $-10\,{}^\circ\text{C}$; b-kohdan $P = 1667\,\text{W}$
**Kysytty:** kuinka suuren osan lämmöntarpeesta takka kattaa, prosentteina
**Periaate:** Sisälämpötila pysyy samana, kun lämmitys antaa yhtä suuren tehon kuin talosta lähtee. Lähtevä teho on verrannollinen sisälämpötilan ja ulkolämpötilan eroon samalla tavalla kuin kaavassa $P = UA\Delta T$ (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kaava:** $P_\text{h} = k_\text{h}\,(T_\text{sisä} - T_\text{ulko})$ ja osuus $= \dfrac{P}{P_\text{h}} = \dfrac{P}{k_\text{h}\,(T_\text{sisä} - T_\text{ulko})}$
**Muunnokset:** Lämpötilaero on sama kelvineinä: $21\,{}^\circ\text{C} - (-10\,{}^\circ\text{C}) = 31\,\text{K}$. Suhdeluku muutetaan prosenteiksi kertomalla se luvulla $100\,\%$.
**Sijoitus:** $P_\text{h} = 150\,\tfrac{\text{W}}{\text{K}} \cdot 31\,\text{K} = 4650\,\text{W}$ ja osuus $= \dfrac{1667\,\text{W}}{4650\,\text{W}} = 0{,}358 = 35{,}8\,\%$
**Vastaus:** noin $36\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten takan tehossa.
**Järkevyys:** Jos takka kattaisi koko tarpeen, siinä pitäisi polttaa vuorokaudessa $4650\,\text{W} \cdot 86\,400\,\text{s} : (0{,}80 \cdot 15\,\text{MJ/kg}) \approx 33\,\text{kg}$ puuta. Se on lähes kolme kertaa niin paljon kuin yksi iltapesällinen. Takka on siis lisälämmitys. Varaavat takat ovat yleensä lisälämmityksiä.

### d)
**Kysytty:** miksi peltikamiinan lämmitys loppuu nopeasti ja varaavan takan lämmitys ei
**Periaate:** Kappaleen lämpökapasiteetti $C = cm$ kertoo, kuinka paljon energiaa tarvitaan, kun lämpötila muuttuu yhden kelvinin. Lämpö siirtyy pinnalta huoneeseen sitä suuremmalla teholla, mitä suurempi lämpötilaero on (luvut *Aineen lämpeneminen ja jäähtyminen* ja *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Mallivastaus:** Ohuen peltikamiinan massa on pieni, ja siksi sen lämpökapasiteetti on pieni. Tuli kuumentaa kamiinan pinnan nopeasti hyvin kuumaksi. Lämpötilaero huoneeseen on suuri, joten energiaa siirtyy suurella teholla. Huone lämpenee nopeasti. Pelti ei kuitenkaan varastoi juuri yhtään energiaa. Kun tuli sammuu, kamiina jäähtyy pian, ja lämmitys loppuu. Varaavan takan kivimassa on $1800\,\text{kg}$. Se varastoi saman energian, vaikka sen lämpötila nousee vain noin $80\,\text{K}$. Takan pinta on vain vähän lämmin. Siksi energiaa siirtyy huoneeseen pienemmällä teholla, mutta koko vuorokauden ajan. Takka siis tasaa lämmitystä ajassa. Energia ei katoa kummassakaan, mutta se vapautuu eri tahtiin eli eri nopeudella.

### Yleisiä virheitä
- a-kohdassa unohdetaan, että vain $80\,\%$ puun energiasta siirtyy kiveen.
- Lämpöarvon megajouleja ei muunneta jouleiksi. Silloin lämpötilan nousuksi tulee alle kelvin.
- b-kohdassa jaetaan tunneilla, mutta tulos ilmoitetaan watteina.
- c-kohdassa lämpötilaeroksi otetaan $21\,\text{K} - 10\,\text{K} = 11\,\text{K}$, vaikka oikea ero on $31\,\text{K}$.
- d-kohdassa sanotaan, että kivi ”sisältää lämpöä”. Kivi varastoi sisäenergiaa. Lämpö on energiaa, joka siirtyy.

## fy9-lampo-s3

### a)
**Kysytty:** kuvaaja, jossa höyrystyneen veden massa $\Delta m$ on kuumentimen tehon $P$ funktiona, ja kuvaajaan sovitettu malli
**Kuvaaja:** Vaaka-akselilla on teho $P\ (\text{W})$ ja pystyakselilla massa $\Delta m\ (\text{g})$. Asteikot alkavat nollasta. Silloin näkyy kohta, jossa suora leikkaa vaaka-akselin. Sitä tarvitaan c-kohdassa.

<svg data-fig="fy9-lampo-s3-graph" viewBox="0 0 480 420" role="img" aria-label="Kuvaaja: höyrystyneen veden massa Δm viidessä minuutissa uppokuumentimen tehon P funktiona. Kuvaajassa on viisi mustaa pistettä tehoilla 200–1000 W. Pisteisiin on sovitettu nouseva suora. Suoraa on jatkettu katkoviivana vaaka-akselille ja tehoon 1100 W asti. Suora kulkee pisteiden (100 W; 4 g) ja (1100 W; 137 g) kautta. Nämä kaksi suoran pistettä on ympyröity, ja niistä luetaan kulmakerroin noin 0,133 g/W. Suora leikkaa vaaka-akselin noin teholla 70 W. Suora ei kulje origon kautta." style="max-width:100%;font-size:26px">
  <line x1="107.5" y1="370" x2="107.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130.5" y1="370" x2="130.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="154" y1="370" x2="154" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="177.5" y1="370" x2="177.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200.5" y1="370" x2="200.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="370" x2="224" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247.5" y1="370" x2="247.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270.5" y1="370" x2="270.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="370" x2="294" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="370" x2="317.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340.5" y1="370" x2="340.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="370" x2="364" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="349.5" x2="364" y2="349.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="328.5" x2="364" y2="328.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="308" x2="364" y2="308" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="287.5" x2="364" y2="287.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="266.5" x2="364" y2="266.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="246" x2="364" y2="246" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="225.5" x2="364" y2="225.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="204.5" x2="364" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="184" x2="364" y2="184" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="163.5" x2="364" y2="163.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="142.5" x2="364" y2="142.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="122" x2="364" y2="122" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="101.5" x2="364" y2="101.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="80.5" x2="364" y2="80.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="60" x2="364" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="370" x2="378" y2="370" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M390,370 L377,376 L377,364 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="371" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="107.5" y1="370" x2="107.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="130.5" y1="370" x2="130.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="154" y1="370" x2="154" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="177.5" y1="370" x2="177.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153" y="378.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$400$</div></foreignObject>
  <line x1="200.5" y1="370" x2="200.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="224" y1="370" x2="224" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="247.5" y1="370" x2="247.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="270.5" y1="370" x2="270.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="378.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$800$</div></foreignObject>
  <line x1="294" y1="370" x2="294" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="317.5" y1="370" x2="317.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="340.5" y1="370" x2="340.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="364" y1="370" x2="364" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333" y="378.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$1200$</div></foreignObject>
  <line x1="77" y1="349.5" x2="84" y2="349.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="328.5" x2="84" y2="328.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="308" x2="84" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="287.5" x2="84" y2="287.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="266.5" x2="84" y2="266.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37" y="251" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$50$</div></foreignObject>
  <line x1="77" y1="246" x2="84" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="225.5" x2="84" y2="225.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="204.5" x2="84" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="184" x2="84" y2="184" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="163.5" x2="84" y2="163.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="148" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$100$</div></foreignObject>
  <line x1="77" y1="142.5" x2="84" y2="142.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="122" x2="84" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="101.5" x2="84" y2="101.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="80.5" x2="84" y2="80.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="60" x2="84" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="44.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$150$</div></foreignObject>
  <foreignObject x="52" y="374.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="396" y="354.5" width="66" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$P\ (\text{W})$</div></foreignObject>
  <foreignObject x="74" y="2.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\Delta m\ (\text{g})$</div></foreignObject>
  <polyline points="130.5,334 317.5,115" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="100,370 130.5,334" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="317.5,115 340.5,87.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="130.5" cy="333" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="177.5" cy="281" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="224" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="270.5" cy="171" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="317.5" cy="114" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="107.5" cy="361.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="340.5" cy="87" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="100.1" cy="370" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="106.1" y1="364" x2="144.7" y2="351.4" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="148.5" y="336" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$P_\text{h} \approx 70\,\text{W}$</span></div></foreignObject>
  <foreignObject x="81" y="110.5" width="157" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$k \approx 0{,}133\,\text{g/W}$</span></div></foreignObject>
</svg>

Kuvaajassa on ympyröity kaksi suoran pistettä. Niistä luetaan b-kohdan kulmakerroin. Oranssi piste on kohta, jossa suora leikkaa vaaka-akselin (c-kohta).

**Mallivastaus:** Pisteet ovat lähes suoralla. Höyrystyneen veden massa kasvaa tasaisesti, kun teho kasvaa. Pisteisiin sovitetaan yksi nouseva suora, joka kulkee pisteiden välistä. Suoraa ei pakoteta kulkemaan origon kautta, koska mikään fysikaalinen syy ei vaadi sitä. Osa tehosta voi kulua muuhun kuin höyrystämiseen. Suoraa jatketaan katkoviivana vaaka-akselille asti. Suora leikkaa akselin selvästi nollan oikealla puolella.

### b)
**Annettu:** a-kohdan suora ja siltä luetut pisteet; mittausaika $t = 300\,\text{s}$
**Kysytty:** veden ominaishöyrystymislämpö $r$ yksikössä $\text{MJ/kg}$
**Periaate:** Vesi kiehuu koko ajan, joten sen lämpötila ei nouse. Osa kuumentimen tehosta johtuu ympäristöön. Loput tehosta höyrystää vettä. Energia säilyy: $(P - P_\text{h})\,t = r\,\Delta m$. Tässä $P_\text{h}$ on häviöteho eli teho, joka johtuu ympäristöön. Yhtälöstä saadaan $\Delta m = \dfrac{t}{r}\,P - \dfrac{t}{r}\,P_\text{h}$. Suoran kulmakerroin on siis $\dfrac{t}{r}$ (luvut *Olomuodon muutokset* ja *Graafinen esitys ja suoran sovittaminen*).
**Kuvaajan lukeminen:** Suoralta luetaan kaksi pistettä, jotka ovat kaukana toisistaan. Mittauspisteitä ei käytetä. Pisteet ovat $(100\,\text{W};\ 4{,}0\,\text{g})$ ja $(1100\,\text{W};\ 137{,}0\,\text{g})$.
**Kaava:** $k = \dfrac{\Delta(\Delta m)}{\Delta P} = \dfrac{t}{r}$, joten $r = \dfrac{t}{k}$
**Muunnokset:** Kulmakertoimen grammat muutetaan kilogrammoiksi: $1\,\text{g} = 10^{-3}\,\text{kg}$. Yksikkö on $\tfrac{\text{s}}{\text{kg/W}} = \tfrac{\text{W}\cdot\text{s}}{\text{kg}} = \tfrac{\text{J}}{\text{kg}}$, ja lopuksi $1\,\text{MJ} = 10^{6}\,\text{J}$.
**Sijoitus:** $k = \dfrac{137{,}0\,\text{g} - 4{,}0\,\text{g}}{1100\,\text{W} - 100\,\text{W}} = \dfrac{133{,}0\,\text{g}}{1000\,\text{W}} = 0{,}133\,\tfrac{\text{g}}{\text{W}}$ ja $r = \dfrac{300\,\text{s}}{0{,}133 \cdot 10^{-3}\,\tfrac{\text{kg}}{\text{W}}} = 2{,}26 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} = 2{,}26\,\text{MJ/kg}$
**Vastaus:** $r \approx 2{,}26\,\text{MJ/kg}$. Kolme merkitsevää numeroa on yläraja eli suurin järkevä tarkkuus. Syy on se, että silmällä sovitetun suoran kulmakerroin on noin $\pm 2\,\%$:n tarkkuinen. Vastaus $2{,}3\,\text{MJ/kg}$ on yhtä hyvä.
**Järkevyys:** Taulukkoarvo on $2{,}26\,\text{MJ/kg}$. Myös pienimmän neliösumman suora antaa $2{,}26\,\text{MJ/kg}$. Tarkistetaan yhdellä pisteellä: teholla $600\,\text{W}$ höyrystämiseen jää noin $530\,\text{W}$. Silloin $530\,\text{W} \cdot 300\,\text{s} : 2{,}26\,\tfrac{\text{MJ}}{\text{kg}} \approx 70\,\text{g}$, kuten taulukossa.

### c)
**Annettu:** a-kohdan suora, joka leikkaa vaaka-akselin; b-kohdan kulmakerroin $k = 0{,}133\,\text{g/W}$ ja suoran piste $(P_1;\ \Delta m_1) = (100\,\text{W};\ 4{,}0\,\text{g})$
**Kysytty:** teho $P_\text{h}$, jolla vesi ei suoran mukaan höyrystyisi, ja tuloksen tulkinta
**Periaate:** Kohdassa, jossa suora leikkaa vaaka-akselin, $\Delta m = 0$. Energiataseen $(P - P_\text{h})\,t = r\,\Delta m$ mukaan näin käy, kun $P = P_\text{h}$. Silloin kuumentimen koko teho johtuu astian seinien ja vedenpinnan kautta huoneeseen. Kiehuva vesi on aina $100\,{}^\circ\text{C}$:ssa. Siksi lämpötilaero huoneeseen pysyy samana, ja myös häviöteho pysyy samana kaikilla tehoilla (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kuvaajan lukeminen:** Suora on jatkettu katkoviivana. Se leikkaa vaaka-akselin noin kohdassa $70\,\text{W}$.
**Kaava:** $0 = k\,(P_\text{h} - P_1) + \Delta m_1$, joten $P_\text{h} = P_1 - \dfrac{\Delta m_1}{k}$
**Muunnokset:** Ei tarvita. Kulmakerroin ja massa ovat grammoina ja teho watteina.
**Sijoitus:** $P_\text{h} = 100\,\text{W} - \dfrac{4{,}0\,\text{g}}{0{,}133\,\tfrac{\text{g}}{\text{W}}} = 100\,\text{W} - 30\,\text{W} = 70\,\text{W}$
**Vastaus:** $P_\text{h} \approx 70\,\text{W}$. Noin $70\,\text{W}$ kuumentimen tehosta johtuu siis huoneeseen eikä höyrystä vettä. Vastauksessa on yksi tai kaksi merkitsevää numeroa. Syy on se, että leikkauskohta saadaan jatkamalla suoraa mitatun alueen ulkopuolelle. Pieni muutos kulmakertoimessa siirtää leikkauskohtaa kymmeniä watteja.
**Järkevyys:** Pienimmän neliösumman suora leikkaa akselin kohdassa $69\,\text{W}$. Häviöteho on muutama prosentti suurimmasta tehosta, mutta yli kolmannes pienimmästä tehosta. Tämä sopii avoimeen teräsastiaan, josta lämpöä siirtyy johtumalla ja konvektiona.

### d)
**Kysytty:** miksi yhden mittauksen tulos $2{,}54\,\text{MJ/kg}$ on liian suuri ja kumpi tulos on luotettavampi
**Periaate:** Energia säilyy. Kuumentimen energia $P\,t$ jakautuu kahteen osaan: höyrystämiseen ja lämpöön, joka johtuu huoneeseen. $P\,t = r\,\Delta m + P_\text{h}\,t$ (luku *Olomuodon muutokset*).
**Mallivastaus:** Yhden mittauksen laskussa $r = \dfrac{P\,t}{\Delta m}$ oletetaan, että kuumentimen koko energia on kulunut höyrystämiseen. Todellisuudessa noin $70\,\text{W}$ johtuu huoneeseen. Teholla $600\,\text{W}$ höyrystämiseen jää siis vain noin $530\,\text{W}$. Laskussa on liikaa energiaa samaa massaa kohti. Siksi tulos on noin $\dfrac{P}{P - P_\text{h}} = 600 : 530 \approx 1{,}13$-kertainen eli noin $13\,\%$ liian suuri. Kuvaajasta saatu tulos on luotettavampi. Häviöteho pysyy vakiona, joten se siirtää suoraa sivulle, mutta ei muuta suoran kulmakerrointa. Siksi kulmakertoimesta laskettu $r$ ei sisällä häviötä. Lisäksi on viisi mittausta, ja suora on sovitettu niiden välistä. Se pienentää yksittäisen lukeman satunnaisvirheen vaikutusta. Menetelmässä oletetaan, että häviöteho on sama kaikilla tehoilla. Oletus on perusteltu, koska kiehuva vesi on aina $100\,{}^\circ\text{C}$:ssa. Myös se, että pisteet asettuvat suoralle, tukee oletusta.

### Yleisiä virheitä
- Suora pakotetaan kulkemaan origon kautta. Silloin kulmakerroin ja $r$ vääristyvät, eikä häviötehoa huomata.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- b-kohdassa grammoja ei muunneta kilogrammoiksi. Silloin tulos on tuhat kertaa liian pieni.
- b-kohdassa $r$:ksi otetaan itse kulmakerroin eikä $\dfrac{t}{k}$.
- d-kohdassa sanotaan vain ”mittausvirhe”. Vastaus ei kerro, mikä energia on laskettu väärin ja muuttuuko tulos suuremmaksi vai pienemmäksi.

### Hyväksytään myös
- Kulmakerroin $0{,}128$…$0{,}138\,\text{g/W}$, kun suora on sovitettu silmällä pisteiden välistä, ja sen mukaiset tulokset: b-kohdassa $2{,}2$–$2{,}3\,\text{MJ/kg}$ ja c-kohdassa $50$–$90\,\text{W}$.
- b-kohdassa voi laskea myös massan sekunnissa: $\dfrac{\Delta m}{t}$ tehon funktiona. Silloin kulmakerroin on $\dfrac{1}{r}$.

## fy9-lampo-s4

### a)
**Kysytty:** miksi järvi jäätyy pinnalta ja miksi pohjan vesi on noin $4\,{}^\circ\text{C}$:ista
**Periaate:** Useimmat aineet laajenevat, kun ne lämpenevät. Vesi kuitenkin kutistuu lämpötilojen $0\,{}^\circ\text{C}$ ja $4\,{}^\circ\text{C}$ välillä. Siksi veden tiheys on suurin noin $4\,{}^\circ\text{C}$:ssa. Tiheämpi vesi painuu alas, ja kevyempi vesi nousee ylös (luku *Lämpölaajeneminen*).
**Mallivastaus:** Syksyllä kylmä ilma jäähdyttää järven pintaa. Kun pintavesi on yli $4\,{}^\circ\text{C}$:ista, se tihenee jäähtyessään ja painuu pohjalle. Sen tilalle nousee lämpimämpää vettä. Näin koko järvi jäähtyy vähitellen noin $4\,{}^\circ\text{C}$:seen. Kun pinta jäähtyy alle tämän lämpötilan, vesi alkaa laajeta jäähtyessään. Nyt kylmempi vesi on kevyempää kuin pohjan $4\,{}^\circ\text{C}$:inen vesi. Siksi kylmä vesi jää pinnalle ja jäätyy siellä. Pohjalle jää tihein vesi, joka on noin $4\,{}^\circ\text{C}$:ista. Se ei nouse pintaan jäähtymään. Lisäksi jää on kevyempää kuin vesi, ja se kelluu. Siksi järvi jäätyy pinnalta alaspäin eikä pohjasta ylöspäin.

### b)
**Kysytty:** mihin jäätyvän veden energia menee ja miksi paksu jää kasvaa hitaammin
**Periaate:** Kun vesi jäätyy, se luovuttaa sulamislämmön $Q = sm$, vaikka lämpötila pysyy $0\,{}^\circ\text{C}$:ssa (luku *Olomuodon muutokset*). Lämpö johtuu lämpimästä kylmään. Kun lämpötilaero on sama, paksun kerroksen läpi johtuu pienempi teho kuin ohuen kerroksen läpi (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Mallivastaus:** Jään alapinnalla vesi on $0\,{}^\circ\text{C}$:ssa. Jotta vesi jäätyisi, siitä on siirryttävä pois sulamislämpö. Se on noin $334\,\text{kJ}$ jokaista kilogrammaa kohti. Yhden senttimetrin kerros yhden neliömetrin alalla vaatii noin $3\,\text{MJ}$. Energia säilyy. Siksi tämän energian on johduttava jään läpi kylmään ilmaan. Jää kasvaa vain sitä mukaa kuin energiaa johtuu pois. Jään läpi johtuva teho riippuu kahdesta asiasta: pakkasilman ja $0\,{}^\circ\text{C}$:n alapinnan lämpötilaerosta sekä jääkerroksen paksuudesta. Paksu kerros eristää paremmin eli sen U-arvo on pienempi. Siksi samalla pakkasella sen läpi johtuu pienempi teho. Ohut syysjää paksunee siis nopeasti, mutta $40\,\text{cm}$:n jää kasvaa samalla pakkasella hitaasti.

### c)
**Kysytty:** vahvistaako lumipeite jäätä
**Periaate:** Lumessa on paljon ilmaa, ja ilma johtaa lämpöä huonosti (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*). Jää kasvaa vain, jos jäätymisessä vapautuva energia johtuu pois (b-kohta).
**Mallivastaus:** Väite on väärä. Lumi ei siirrä jäähän ”kylmää”. Energiaa siirtyy aina lämpimämmästä kylmempään. Tässä energia siirtyy jäästä lumen kautta ilmaan. Lumi johtaa lämpöä huonosti, koska siinä on paljon ilmaa. Jään päällä lumi toimii eristeenä samalla tavalla kuin villa seinässä. Siksi jään alapinnalta johtuu vähemmän energiaa pois, ja vettä jäätyy vähemmän. Paksun lumipeitteen alla jää siis kasvaa hitaammin ja jää ohuemmaksi kuin paljas jää. Lisäksi raskas lumi voi painaa jäätä alas. Silloin vettä nousee halkeamista jään päälle, ja syntyy heikkoa sohjoa tai kohvajäätä. Kohvajää on jäätynyttä lumen ja veden seosta. Lumi siis heikentää jäätä eikä vahvista sitä.

### Yleisiä virheitä
- a-kohdassa sanotaan vain, että ”jää kelluu”. Vastaus ei selitä, miksi pohjan vesi on $4\,{}^\circ\text{C}$:ista.
- Väitetään, että kylmä vesi on aina tiheämpää kuin lämmin vesi.
- b-kohdassa unohdetaan, että jäätyminen vapauttaa energiaa. Jään kasvu selitetään pelkällä lämpötilalla.
- c-kohdassa hyväksytään ajatus, että kylmyys siirtyy lumesta jäähän.

## fy9-lampo-s5

### a)
**Annettu:** vesi $m_\text{v} = 0{,}200\,\text{kg}$, $T_\text{v} = 40{,}0\,{}^\circ\text{C}$; jää $m_\text{j} = 0{,}0500\,\text{kg}$; lopputila $T = 14{,}3\,{}^\circ\text{C}$; $c_\text{v} = 4190\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** ryhmän tulos $s$ yksikössä $\text{kJ/kg}$ ja ryhmän oletus jään alkulämpötilasta
**Periaate:** Oletetaan, että muki ja ilma eivät ota lämpöä. Silloin energia säilyy: vesi luovuttaa yhtä paljon lämpöä kuin jää vastaanottaa. Ryhmän laskussa jää vain sulaa ($Q = sm$), ja sulamisvesi lämpenee $0\,{}^\circ\text{C}$:sta lopun lämpötilaan ($Q = cm\Delta T$). Laskussa ei ole jään lämpenemistä. Siksi ryhmä on olettanut, että jää oli $0\,{}^\circ\text{C}$:ista (luku *Lämpötasapaino olomuodon muuttuessa*).
**Kaava:** $c_\text{v} m_\text{v} (T_\text{v} - T) = s\,m_\text{j} + c_\text{v} m_\text{j}\,(T - 0\,{}^\circ\text{C})$, joten $s = \dfrac{c_\text{v} m_\text{v} (T_\text{v} - T) - c_\text{v} m_\text{j} T}{m_\text{j}}$
**Muunnokset:** Lämpötilaerot ovat samat kelvineinä: vesi jäähtyy $25{,}7\,\text{K}$ ja sulamisvesi lämpenee $14{,}3\,\text{K}$. Lopuksi $1\,\text{kJ} = 1000\,\text{J}$.
**Sijoitus:** Vesi luovuttaa lämpöä $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}200\,\text{kg} \cdot 25{,}7\,\text{K} = 21\,537\,\text{J}$. Sulamisveden lämpenemiseen kuluu $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}0500\,\text{kg} \cdot 14{,}3\,\text{K} = 2996\,\text{J}$. Siis $s = \dfrac{21\,537\,\text{J} - 2996\,\text{J}}{0{,}0500\,\text{kg}} = 370\,800\,\tfrac{\text{J}}{\text{kg}} = 371\,\text{kJ/kg}$.
**Vastaus:** $371\,\text{kJ/kg}$. Vastauksessa on kolme merkitsevää numeroa, kuten massoissa ja lämpötiloissa. Ryhmä on olettanut, että jää oli $0\,{}^\circ\text{C}$:ista, vaikka se otettiin pakastimesta.
**Järkevyys:** Tulos on noin $11\,\%$ suurempi kuin taulukkoarvo $334\,\text{kJ/kg}$. Ero on liian suuri, jotta se olisi huolellisen mittauksen satunnaisvirhe. Ero viittaa systemaattiseen virheeseen eli virheeseen, joka muuttaa tulosta aina samaan suuntaan. Virhettä etsitään b-kohdassa.

### b)
**Annettu:** a-kohdan tiedot; jään alkulämpötila $T_\text{j} = -18{,}0\,{}^\circ\text{C}$, $c_\text{j} = 2100\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** korjattu ominaissulamislämpö $s$ ja johtopäätöksen arvio
**Periaate:** Pakastimen jää lämpenee ensin $-18{,}0\,{}^\circ\text{C}$:sta $0\,{}^\circ\text{C}$:seen. Siihen kuluu osa veden luovuttamasta energiasta. Ryhmän laskussa tämä osa on laskettu sulamislämmöksi. Siksi ryhmän tulos on liian suuri. Energiataseeseen lisätään jään lämpeneminen.
**Kaava:** $c_\text{v} m_\text{v} (T_\text{v} - T) = c_\text{j} m_\text{j} \Delta T_\text{j} + s\,m_\text{j} + c_\text{v} m_\text{j} T$, joten $s = \dfrac{c_\text{v} m_\text{v} (T_\text{v} - T) - c_\text{j} m_\text{j} \Delta T_\text{j} - c_\text{v} m_\text{j} T}{m_\text{j}}$
**Muunnokset:** Jään lämpeneminen on $\Delta T_\text{j} = 0\,{}^\circ\text{C} - (-18{,}0\,{}^\circ\text{C}) = 18{,}0\,\text{K}$, sama kelvineinä.
**Sijoitus:** $c_\text{j} m_\text{j} \Delta T_\text{j} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}0500\,\text{kg} \cdot 18{,}0\,\text{K} = 1890\,\text{J}$ ja $s = \dfrac{21\,537\,\text{J} - 1890\,\text{J} - 2996\,\text{J}}{0{,}0500\,\text{kg}} = 333\,000\,\tfrac{\text{J}}{\text{kg}} = 333\,\text{kJ/kg}$
**Vastaus:** $333\,\text{kJ/kg}$. Vastauksessa on kolme merkitsevää numeroa, kuten mittaustuloksissa. Ryhmän johtopäätös ei pidä. Korjattu tulos on sama kuin taulukkoarvo $334\,\text{kJ/kg}$. Ero johtui väärästä oletuksesta, ei taulukosta. Muki ei myöskään selitä eroa. Jos muki ottaisi lämpöä, ryhmän kaava laskisi senkin jään hyväksi. Tulos olisi silloin liian suuri. Ero $1890\,\text{J}$ vaatisi kuitenkin, että mukin lämpökapasiteetti on noin $1890\,\text{J} : 25{,}7\,\text{K} \approx 70\,\text{J/K}$. Styroksimuki painaa vain muutaman gramman, ja sen lämpökapasiteetti on vain muutama $\text{J/K}$. Lisäksi korjattu arvo on jo sama kuin taulukossa.
**Järkevyys:** Jään lämpeneminen vie $1890\,\text{J}$. Se on vain noin $9\,\%$ veden luovuttamasta lämmöstä. Kun se jaetaan pienellä jään massalla, saadaan $38\,\text{kJ/kg}$. Se on juuri tulosten ero $371 - 333$. Korjattu arvo poikkeaa taulukosta alle prosentin. Se on mittausten tarkkuuden rajoissa.

### c)
**Kysytty:** kolme parannusta mittaukseen ja niiden perustelut
**Periaate:** Luotettava mittaus poistaa systemaattiset virheet tai ottaa ne huomioon. Se myös pienentää satunnaisvirhettä, kun mittaus toistetaan monta kertaa (luku *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Ensimmäinen parannus: jää otetaan astiasta, jossa on jäävettä. Siellä jää on sulamassa, joten se on tasan $0\,{}^\circ\text{C}$:ista. Jään pinta kuivataan paperilla juuri ennen kuin jää pudotetaan veteen. Silloin laskun oletus pätee. Jään pinnalla oleva vesi ei myöskään kasvata mitattua jään massaa. Toinen tapa on mitata jään lämpötila ja ottaa jään lämpeneminen huomioon samalla tavalla kuin b-kohdassa. Toinen parannus: jään massa määritetään erotuksena. Muki ja vesi punnitaan ennen kuin jää lisätään ja sen jälkeen, kun jää on sulanut. Silloin punnittu massa on juuri se jää, joka päätyi veteen. Jää, joka suli tai putosi käsittelyn aikana, ei vääristä tulosta. Kolmas parannus: lämmönvaihtoa ympäristön kanssa pienennetään. Mukissa on kansi. Alkulämpötila valitaan niin, että se on yhtä paljon huoneenlämmön yläpuolella kuin loppulämpötila on sen alapuolella. Silloin huoneesta tuleva lämpö ja huoneeseen lähtevä lämpö lähes kumoavat toisensa. Lopuksi mittaus toistetaan monta kertaa. Tuloksena ilmoitetaan keskiarvo ja se, kuinka paljon tulokset vaihtelevat.

### Yleisiä virheitä
- Sulamisveden lämpeneminen $0\,{}^\circ\text{C}$:sta lopun lämpötilaan unohdetaan. Silloin a-kohdassa saadaan noin $431\,\text{kJ/kg}$.
- b-kohdassa jään lämpenemiseen käytetään veden ominaislämpökapasiteettia.
- Muki hyväksytään selitykseksi, mutta ei arvioida, kuinka suuri sen lämpökapasiteetin pitäisi olla. Styroksimukin lämpökapasiteetti on liian pieni selittämään $38\,\text{kJ/kg}$:n eroa.
- c-kohdassa ehdotetaan vain ”tarkempaa lämpömittaria”. Vastaus ei kerro, mihin virheeseen se vaikuttaa.

### Hyväksytään myös
- a-kohdassa sulamisveden lämpenemisen voi laskea omana terminään ja vähentää sen lopuksi. Tulos on sama.

## fy9-lampo-s6

### a)
**Annettu:** auton massa $m = 1600\,\text{kg}$, nopeus $v = 90\,\text{km/h}$; levyjen massa $m_\text{l} = 30\,\text{kg}$, $c = 450\,\text{J/(kg}\cdot\text{K)}$; levyihin siirtyvä osuus $k = 85\,\%$
**Kysytty:** kuinka paljon levyjen lämpötila nousee, $\Delta T$
**Periaate:** Tasaisella tiellä jarrutus muuttaa auton liike-energian kitkan avulla jarrujen sisäenergiaksi. Energia säilyy (luku *Mekaanisen energian säilyminen ja energiaperiaate*). Lyhyessä jarrutuksessa ilmanvastuksen osuus on pieni. Siksi sitä ei oteta huomioon. Levyt pysyvät kiinteinä. Siksi niiden vastaanottama lämpö nostaa niiden lämpötilaa kaavan $Q = cm\Delta T$ mukaan.
**Kaava:** $E_\text{k} = \tfrac{1}{2} m v^2$ ja $k\,E_\text{k} = c\,m_\text{l}\,\Delta T$, joten $\Delta T = \dfrac{k \cdot \tfrac{1}{2} m v^2}{c\,m_\text{l}}$
**Muunnokset:** $90\,\text{km/h} = 90 \cdot \dfrac{1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$ ja $85\,\% = 0{,}85$.
**Sijoitus:** $E_\text{k} = \tfrac{1}{2} \cdot 1600\,\text{kg} \cdot (25\,\tfrac{\text{m}}{\text{s}})^2 = 500\,000\,\text{J}$ ja $\Delta T = \dfrac{0{,}85 \cdot 500\,000\,\text{J}}{450\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 30\,\text{kg}} = \dfrac{425\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 31{,}5\,\text{K}$
**Vastaus:** noin $31\,\text{K}$. Vastauksessa on kaksi merkitsevää numeroa, kuten levyjen massassa $30\,\text{kg}$ ja nopeudessa $90\,\text{km/h}$.
**Järkevyys:** Yksi pysäytys lämmittää levyjä muutamia kymmeniä asteita. Tämä sopii kokemukseen: kovan jarrutuksen jälkeen jarrulevyt ovat kuumia, mutta ne eivät hehku. Ilmanvastus pienentäisi vähän energiaa, joka tulee levyihin. Tulos on siis yläraja eli suurin mahdollinen nousu.

### b)
**Annettu:** pudotus $h = 250\,\text{m}$, matka $s = 4{,}0\,\text{km}$, ajovastus $F = 450\,\text{N}$, nopeus on vakio; $g = 9{,}81\,\text{m/s}^2$; a-kohdan tiedot
**Kysytty:** kuinka paljon levyjen lämpötila nousee, $\Delta T$, jos levyt eivät jäähdy
**Periaate:** Nopeus on vakio, joten liike-energia ei muutu. Energiaperiaatteen mukaan potentiaalienergia pienenee määrän $mgh$. Tämä energia kuluu ajovastusten työhön $Fs$ ja jarruihin (luvut *Liike-energia, potentiaalienergia ja mekaaninen energia* ja *Mekaanisen energian säilyminen ja energiaperiaate*). Jarruihin tulevasta energiasta $85\,\%$ lämmittää levyjä.
**Kaava:** $Q_\text{jarrut} = mgh - Fs$ ja $k\,Q_\text{jarrut} = c\,m_\text{l}\,\Delta T$, joten $\Delta T = \dfrac{k\,(mgh - Fs)}{c\,m_\text{l}}$
**Muunnokset:** $4{,}0\,\text{km} = 4{,}0 \cdot 1000\,\text{m} = 4000\,\text{m}$.
**Sijoitus:** $mgh = 1600\,\text{kg} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 250\,\text{m} = 3\,924\,000\,\text{J}$, $Fs = 450\,\text{N} \cdot 4000\,\text{m} = 1\,800\,000\,\text{J}$ ja $\Delta T = \dfrac{0{,}85 \cdot 2\,124\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = \dfrac{1\,805\,400\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 133{,}7\,\text{K}$
**Vastaus:** noin $1{,}3 \cdot 10^{2}\,\text{K}$ eli $130\,\text{K}$. Vastauksessa on kaksi merkitsevää numeroa, kuten matkassa $4{,}0\,\text{km}$.
**Järkevyys:** Alamäessä jarruihin tulee noin neljä kertaa enemmän energiaa kuin yhdessä pysäytyksessä nopeudesta $90\,\text{km/h}$ ($1{,}81\,\text{MJ}$ ja $0{,}43\,\text{MJ}$). Siksi lämpötila nousee noin neljä kertaa enemmän. Jos levyt eivät jäähtyisi, ne kuumenisivat noin $150\,{}^\circ\text{C}$:seen. Se on mahdollista, mutta jo lähellä lämpötilaa, jossa tavallinen jarru vielä toimii hyvin.

### c)
**Annettu:** b-kohdassa levyihin tullut energia $Q = 1{,}805\,\text{MJ}$; levyjen lämpötila nousi $80\,\text{K}$; $c\,m_\text{l} = 13\,500\,\text{J/K}$
**Kysytty:** kuinka suuri osa energiasta siirtyi ilmaan, prosentteina, ja millä tavoilla energia siirtyi
**Periaate:** Energia säilyy. Levyihin tullut energia jäi levyihin ja nosti niiden lämpötilaa ($Q = cm\Delta T$), tai se siirtyi pois mäen aikana. Kuuma levy luovuttaa lämpöä konvektiona ilmaan, joka virtaa levyn ohi. Levy myös säteilee lämpöä ja johtaa lämpöä napaan ja vanteeseen (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kaava:** $Q_\text{ilma} = Q - c\,m_\text{l}\,\Delta T$ ja osuus $= \dfrac{Q_\text{ilma}}{Q}$
**Muunnokset:** Ei tarvita. Energiat ovat jouleina. Suhdeluku muutetaan prosenteiksi kertomalla se luvulla $100\,\%$.
**Sijoitus:** $Q_\text{ilma} = 1\,805\,400\,\text{J} - 13\,500\,\tfrac{\text{J}}{\text{K}} \cdot 80\,\text{K} = 1\,805\,400\,\text{J} - 1\,080\,000\,\text{J} = 725\,400\,\text{J}$ ja osuus $= \dfrac{725\,400\,\text{J}}{1\,805\,400\,\text{J}} = 0{,}402 = 40{,}2\,\%$
**Vastaus:** noin $40\,\%$. Vastauksessa on kaksi merkitsevää numeroa, kuten b-kohdan tuloksessa. Suurin osa energiasta siirtyi konvektiona ilmaan, joka virtasi levyn ohi. Lisäksi energiaa siirtyi lämpösäteilynä ja johtumalla navan ja vanteen kautta.
**Järkevyys:** Mäki kestää $4000\,\text{m} : 16{,}7\,\tfrac{\text{m}}{\text{s}} = 240\,\text{s}$. Levyihin tulee keskimäärin noin $7{,}5\,\text{kW}$. Ilmaan siirtyi keskimäärin $725\,\text{kJ} : 240\,\text{s} \approx 3\,\text{kW}$. Tämä on uskottavaa neljälle kuumalle levylle, joiden ohi ilma virtaa ajon aikana.

### d)
**Kysytty:** miksi moottorijarrutus säästää jarruja, kun asiaa ajatellaan energian kannalta
**Periaate:** Energia säilyy. Siksi potentiaalienergia muuttuu jossakin sisäenergiaksi. Moottorijarrutuksessa pyörät pyörittävät moottoria. Moottorin kitka vastustaa liikettä (luku *Mekaanisen energian säilyminen ja energiaperiaate*).
**Mallivastaus:** Moottorijarrutuksessa potentiaalienergia ei katoa. Se muuttuu moottorin kitkan kautta moottorin sisäenergiaksi. Moottorin jäähdytysjärjestelmä on tehty siirtämään paljon lämpöä ilmaan suurella teholla. Siksi moottori ei ylikuumene. Silloin jarrulevyihin tulee vähän energiaa, ja ne pysyvät viileinä. Jarrut toimivat täydellä teholla, kun niitä todella tarvitaan. Neuvo on siis perusteltu. Energia ei vähene, mutta se lämmittää eri kohdetta: jarrujen sijaan se lämmittää moottoria.

### Yleisiä virheitä
- Nopeutta ei muunneta metreiksi sekunnissa. Silloin liike-energia on yli kymmenen kertaa liian suuri.
- b-kohdassa koko potentiaalienergia annetaan jarruille. Silloin tulokseksi tulee noin $250\,\text{K}$.
- b-kohdassa lasketaan mukaan liike-energia, vaikka nopeus on vakio.
- c-kohdassa sanotaan, että energia ”kului” tai ”hävisi”. Vastaus ei kerro, mihin energia siirtyi.
- d-kohdassa väitetään, että moottorijarrutuksessa energia ei muutu lämmöksi lainkaan.

### Hyväksytään myös
- a-kohdassa vastaus $31{,}5\,\text{K}$ tai $32\,\text{K}$, kun perusteluna on pyöristys.
