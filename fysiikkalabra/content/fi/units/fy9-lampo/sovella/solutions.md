## fy9-lampo-s1

### a)
**Annettu:** ala $A = 1800\,\text{m}^2$, vesikerroksen paksuus $d = 3{,}00\,\text{cm}$, veden tiheys $\rho = 1000\,\text{kg/m}^3$; vesi $15{,}0\,{}^\circ\text{C}$, valmis jää $-4{,}0\,{}^\circ\text{C}$; $c_\text{v} = 4190\,\text{J/(kg}\cdot\text{K)}$, $c_\text{j} = 2100\,\text{J/(kg}\cdot\text{K)}$, $s = 334\,\text{kJ/kg}$
**Kysytty:** poistettava lämpömäärä $Q$ gigajouleina
**Periaate:** Energia säilyy: kylmäkoneen on poistettava kaikki energia, jonka vesi luovuttaa matkalla $15{,}0\,{}^\circ\text{C}$:n vedestä $-4{,}0\,{}^\circ\text{C}$:n jääksi. Matka on kolme vaihetta. Vesi jäähtyy $0\,{}^\circ\text{C}$:seen ($Q = cm\Delta T$), jäätyy vakiolämpötilassa, jolloin se luovuttaa sulamislämmön ($Q = sm$), ja jää jäähtyy $-4{,}0\,{}^\circ\text{C}$:seen ($Q = cm\Delta T$). Vähintään-sana tarkoittaa, että halliin johtuvaa lämpöä ei lasketa mukaan.
**Kaava:** $m = \rho A d$ ja $Q = c_\text{v} m\,\Delta T_\text{v} + s m + c_\text{j} m\,\Delta T_\text{j}$, joten $Q = \rho A d\,(c_\text{v}\,\Delta T_\text{v} + s + c_\text{j}\,\Delta T_\text{j})$
**Muunnokset:** $3{,}00\,\text{cm} = 3{,}00 \cdot 0{,}01\,\text{m} = 0{,}0300\,\text{m}$ ja $334\,\text{kJ/kg} = 334\,000\,\text{J/kg}$. Lämpötilan muutokset ovat samat kelvineinä: $\Delta T_\text{v} = 15{,}0\,\text{K}$ ja $\Delta T_\text{j} = 4{,}0\,\text{K}$. Lopuksi $1\,\text{GJ} = 10^{9}\,\text{J}$.
**Sijoitus:** $m = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1800\,\text{m}^2 \cdot 0{,}0300\,\text{m} = 54\,000\,\text{kg}$ ja $Q = 54\,000\,\text{kg} \cdot (4190 \cdot 15{,}0 + 334\,000 + 2100 \cdot 4{,}0)\,\tfrac{\text{J}}{\text{kg}} = 54\,000\,\text{kg} \cdot 405\,250\,\tfrac{\text{J}}{\text{kg}} = 2{,}188 \cdot 10^{10}\,\text{J} = 21{,}9\,\text{GJ}$
**Vastaus:** $21{,}9\,\text{GJ}$, kolme merkitsevää numeroa kuten kerroksen paksuus $3{,}00\,\text{cm}$ ja veden lämpötila $15{,}0\,{}^\circ\text{C}$. Jään jäähtymisen $4{,}0\,\text{K}$ kaksi numeroa koskee vain pientä termiä.
**Järkevyys:** Vaiheittain $Q_\text{v} = 3{,}39\,\text{GJ}$, $Q_\text{s} = 18{,}0\,\text{GJ}$ ja $Q_\text{j} = 0{,}454\,\text{GJ}$, ja summa on sama $21{,}9\,\text{GJ}$. Pyöristetyillä luvuilla $54\,\text{t} \cdot 400\,\text{kJ/kg} \approx 22\,\text{GJ}$. Kilowattitunteina se on noin $6100\,\text{kWh}$, saman verran kuin omakotitalon sähkö noin vuodessa, mikä sopii suureen jääalaan.

### b)
**Annettu:** a-kohdan $Q = 2{,}188 \cdot 10^{10}\,\text{J}$, kylmäkoneen teho $P = 350\,\text{kW}$
**Kysytty:** jäädytyksen kesto $t$ tunteina
**Periaate:** Kylmäkone poistaa energiaa tasaisella teholla, joten aika on poistettava energia jaettuna teholla (luku *Teho*). Tulos on alaraja, koska kone poistaa samalla myös halliin ja betoniin johtuvaa lämpöä.
**Kaava:** $P = \dfrac{Q}{t}$, joten $t = \dfrac{Q}{P}$
**Muunnokset:** $350\,\text{kW} = 350 \cdot 1000\,\text{W} = 350\,000\,\text{W}$ ja lopuksi $1\,\text{h} = 3600\,\text{s}$.
**Sijoitus:** $t = \dfrac{2{,}188 \cdot 10^{10}\,\text{J}}{350\,000\,\text{W}} = 62\,500\,\text{s} = 62\,500 \cdot \tfrac{1}{3600}\,\text{h} = 17{,}4\,\text{h}$
**Vastaus:** vähintään $17{,}4\,\text{h}$, kolme merkitsevää numeroa kuten teho $350\,\text{kW}$ ja a-kohdan tulos.
**Järkevyys:** Noin vuorokausi uuden jään tekemiseen on uskottava, ja todellisuudessa aikaa kuluu enemmän, koska kerrokset ruiskutetaan vähitellen ja hallin ilma lämmittää jäätä. Tarkistus: $350\,\text{kW} \cdot 17{,}4\,\text{h} \approx 6100\,\text{kWh} \approx 21{,}9\,\text{GJ}$.

### c)
**Kysytty:** onko jäätyminen nopea vaihe, kun vesi on jo $0\,{}^\circ\text{C}$:ssa
**Periaate:** Jäätyessään vesi luovuttaa sulamislämmön, vaikka lämpötila pysyy $0\,{}^\circ\text{C}$:ssa: hiukkaset asettuvat säännölliseen järjestykseen ja niiden välinen vuorovaikutusenergia pienenee. Kylmäkoneen on poistettava tämä energia samalla teholla kuin muutkin (luku *Olomuodon muutokset*).
**Mallivastaus:** Väite on väärä. a-kohdan vaiheista jäätyminen vaatii $18{,}0\,\text{GJ}$ eli noin $82\,\%$ kokonaislämmöstä, veden jäähtyminen $15{,}0\,{}^\circ\text{C}$:sta $0\,{}^\circ\text{C}$:seen vain noin $16\,\%$ ja jään jäähtyminen noin $2\,\%$. Teholla $350\,\text{kW}$ veden jäähdyttäminen kestää noin $2{,}7\,\text{h}$, mutta jäätyminen noin $14\,\text{h}$. Lämpötila ei muutu jäätymisen aikana, mutta energiaa on silti poistettava, koska jäätyminen vapauttaa jokaisesta kilogrammasta $334\,\text{kJ}$, saman verran kuin veden jäähtyminen lähes $80\,\text{K}$. Jäätyminen on siis jäädytyksen hitain vaihe, eikä jäämestarin kannata odottaa sen käyvän hetkessä.

### Yleisiä virheitä
- Jäätymisen sulamislämpö unohdetaan, koska lämpötila ei muutu, jolloin tulokseksi tulee vain noin $3{,}8\,\text{GJ}$.
- Paksuutta ei muunneta metreiksi, jolloin massa on sata kertaa liian suuri.
- Jään jäähtymisessä käytetään veden ominaislämpökapasiteettia.
- b-kohdassa tulos jätetään sekunneiksi tai teho jätetään kilowateiksi, ja vastauksen yksikkö menee väärin.
- c-kohdassa väitettä arvioidaan ilman lukuja.

### Hyväksytään myös
- a-kohdassa vaiheet voi laskea erikseen ja laskea yhteen; vastaus $22\,\text{GJ}$ kahdella merkitsevällä numerolla, kun perusteluna on jään lämpötila $-4{,}0\,{}^\circ\text{C}$.

## fy9-lampo-s2

### a)
**Annettu:** koivuklapien massa $m_\text{p} = 12{,}0\,\text{kg}$, lämpöarvo $H = 15\,\text{MJ/kg}$, kiveen siirtyvä osuus $\eta = 80\,\%$; kivimassa $m_\text{k} = 1800\,\text{kg}$, $c = 980\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** kivimassan keskimääräinen lämpötilan nousu $\Delta T$
**Periaate:** Palava puu vapauttaa energian $Hm$ (luku *Polttoaineet ja lämpöarvo*), ja siitä $80\,\%$ siirtyy kiveen; loput lähtee savukaasujen mukana piippuun. Kivi pysyy kiinteänä, joten sen vastaanottama lämpö nostaa lämpötilaa $Q = cm\Delta T$:n mukaan (luku *Aineen lämpeneminen ja jäähtyminen*). Lämmityksen aikana kivestä johtuu huoneeseen jo jonkin verran lämpöä, mikä jätetään huomiotta.
**Kaava:** $Q = \eta H m_\text{p}$ ja $Q = c\,m_\text{k}\,\Delta T$, joten $\Delta T = \dfrac{\eta H m_\text{p}}{c\,m_\text{k}}$
**Muunnokset:** $15\,\text{MJ/kg} = 15 \cdot 10^{6}\,\text{J/kg}$ ja $80\,\% = 0{,}80$.
**Sijoitus:** $\Delta T = \dfrac{0{,}80 \cdot 15 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} \cdot 12{,}0\,\text{kg}}{980\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 1800\,\text{kg}} = \dfrac{1{,}44 \cdot 10^{8}\,\text{J}}{1{,}764 \cdot 10^{6}\,\tfrac{\text{J}}{\text{K}}} = 81{,}6\,\text{K}$
**Vastaus:** noin $82\,\text{K}$, kaksi merkitsevää numeroa kuten lämpöarvo $15\,\text{MJ/kg}$ ja osuus $80\,\%$. Tulos on keskiarvo: kivimassan sisäosat lämpenevät enemmän kuin pinta.
**Järkevyys:** Jos kivi on aamulla $25\,{}^\circ\text{C}$:ista, sen keskilämpötila nousee noin $105\,{}^\circ\text{C}$:seen. Takan pinta tuntuu silloin kuumalta mutta ei polta, koska pinta on sisäosia kylmempi. Kivimassan lämpökapasiteetti $1{,}76\,\text{MJ/K}$ on suuri, joten $144\,\text{MJ}$ ei nosta lämpötilaa satoja asteita.

### b)
**Annettu:** a-kohdan $Q = 144\,\text{MJ}$, aika $t = 24\,\text{h}$
**Kysytty:** keskimääräinen lämmitysteho $P$ kilowatteina
**Periaate:** Kivi jäähtyy vuorokaudessa takaisin alkulämpötilaansa, joten se luovuttaa huoneisiin saman energian, jonka se sai. Keskiteho on energia jaettuna ajalla (luku *Teho*).
**Kaava:** $P = \dfrac{Q}{t}$
**Muunnokset:** $144\,\text{MJ} = 144 \cdot 10^{6}\,\text{J}$ ja $24\,\text{h} = 24 \cdot 3600\,\text{s} = 86\,400\,\text{s}$; lopuksi $1\,\text{W} = 0{,}001\,\text{kW}$.
**Sijoitus:** $P = \dfrac{144 \cdot 10^{6}\,\text{J}}{86\,400\,\text{s}} = 1667\,\text{W} = 1{,}67\,\text{kW}$
**Vastaus:** noin $1{,}7\,\text{kW}$, kaksi merkitsevää numeroa kuten a-kohdan lähtötiedot.
**Järkevyys:** Teho vastaa yhtä sähköpatteria tai kahta, mikä on tavallinen tulisijan keskiteho. Teho ei ole vakio: heti lämmityksen jälkeen kivi on kuumimmillaan ja luovuttaa enemmän.

### c)
**Annettu:** lämpöhäviö $150\,\text{W}$ kelviniä kohti, sisällä $21\,{}^\circ\text{C}$, ulkona $-10\,{}^\circ\text{C}$; b-kohdan $P = 1667\,\text{W}$
**Kysytty:** takan osuus lämmöntarpeesta prosentteina
**Periaate:** Sisälämpötila pysyy vakiona, kun lämmitys antaa yhtä suuren tehon kuin taloa lähtee. Lähtevä teho on verrannollinen sisä- ja ulkolämpötilan eroon kuten $P = UA\Delta T$ (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kaava:** $P_\text{h} = 150\,\tfrac{\text{W}}{\text{K}} \cdot (T_\text{sisä} - T_\text{ulko})$ ja osuus $= \dfrac{P}{P_\text{h}}$
**Muunnokset:** Lämpötilaero on sama kelvineinä: $21\,{}^\circ\text{C} - (-10\,{}^\circ\text{C}) = 31\,\text{K}$. Suhdeluku muutetaan prosenteiksi kertomalla luvulla $100\,\%$.
**Sijoitus:** $P_\text{h} = 150\,\tfrac{\text{W}}{\text{K}} \cdot 31\,\text{K} = 4650\,\text{W}$ ja osuus $= \dfrac{1667\,\text{W}}{4650\,\text{W}} = 0{,}358 = 35{,}8\,\%$
**Vastaus:** noin $36\,\%$, kaksi merkitsevää numeroa kuten takan teho.
**Järkevyys:** Koko tarpeen kattamiseen takassa pitäisi polttaa vuorokaudessa $4650\,\text{W} \cdot 86\,400\,\text{s} : (0{,}80 \cdot 15\,\text{MJ/kg}) \approx 33\,\text{kg}$ puuta, lähes kolme kertaa iltapesällinen. Takka on siis lisälämmitys, kuten varaavat takat yleensä ovat.

### d)
**Kysytty:** miksi peltikamiinan lämmitys loppuu nopeasti ja varaavan takan ei
**Periaate:** Kappaleen lämpökapasiteetti $C = cm$ kertoo, kuinka paljon energiaa yhden kelvinin muutos vaatii. Lämpö siirtyy pinnalta huoneeseen sitä suuremmalla teholla, mitä suurempi lämpötilaero on (luvut *Aineen lämpeneminen ja jäähtyminen* ja *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Mallivastaus:** Ohuen peltikamiinan massa ja lämpökapasiteetti ovat pienet, joten tuli kuumentaa sen pinnan nopeasti hyvin kuumaksi. Suuri lämpötilaero huoneeseen siirtää energiaa suurella teholla, joten huone lämpenee nopeasti. Pelti ei kuitenkaan varastoi juuri energiaa, joten kun tuli sammuu, kamiina jäähtyy pian ja lämmitys loppuu. Varaavan takan $1800\,\text{kg}$:n kivimassa sitoo saman energian vain noin $80\,\text{K}$:n lämpötilan nousulla. Sen pinta on maltillisen lämmin, joten energiaa siirtyy huoneeseen pienemmällä teholla mutta koko vuorokauden. Takka siis tasaa lämmitystä ajassa: energia ei katoa kummassakaan, mutta se vapautuu eri tahtiin.

### Yleisiä virheitä
- a-kohdassa unohdetaan, että vain $80\,\%$ puun energiasta siirtyy kiveen.
- Lämpöarvon megajouleja ei muunneta jouleiksi, ja lämpötilan nousuksi tulee alle kelvin.
- b-kohdassa jaetaan tunneilla, mutta ilmoitetaan tulos watteina.
- c-kohdassa lämpötilaeroksi otetaan $21\,\text{K} - 10\,\text{K} = 11\,\text{K}$ eikä $31\,\text{K}$.
- d-kohdassa sanotaan, että kivi ”sisältää lämpöä”; kivi varastoi sisäenergiaa, ja lämpö on siirtyvää energiaa.

## fy9-lampo-s3

### a)
**Kysytty:** höyrystyneen veden massa $\Delta m$ kuumentimen tehon $P$ funktiona kuvaajana ja siihen sovitettu malli
**Kuvaaja:** Vaaka-akselilla on teho $P\ (\text{W})$ ja pystyakselilla massa $\Delta m\ (\text{g})$. Asteikot alkavat nollasta, jotta suoran ja vaaka-akselin leikkauskohta näkyy c-kohtaa varten.

<svg data-fig="fy9-lampo-s3-graph" viewBox="0 0 480 420" role="img" aria-label="Kuvaaja: höyrystyneen veden massa Δm viidessä minuutissa uppokuumentimen tehon P funktiona. Viisi mustaa pistettä tehoilla 200–1000 W. Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana vaaka-akselille ja tehoon 1100 W asti. Suora kulkee pisteiden (100 W; 4 g) ja (1100 W; 137 g) kautta; nämä kaksi suoran pistettä on ympyröity, ja niistä luetaan kulmakerroin noin 0,133 g/W. Suora leikkaa vaaka-akselin noin teholla 70 W. Suora ei kulje origon kautta." style="max-width:100%;font-size:26px">
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

Kuvaajassa ympyröidyt kohdat ovat ne kaksi suoran pistettä, joista b-kohdan kulmakerroin luetaan. Oranssi piste on suoran ja vaaka-akselin leikkauskohta (c-kohta).

**Mallivastaus:** Pisteet ovat lähes suoralla: höyrystynyt massa kasvaa tasaisesti tehon mukana. Pisteisiin sovitetaan yksi nouseva suora, joka kulkee pisteiden lomitse. Suoraa ei pakoteta origon kautta, koska mikään fysikaalinen syy ei vaadi sitä: osa tehosta voi kulua muuhun kuin höyrystämiseen. Suoraa jatketaan katkoviivana vaaka-akselille asti, ja se leikkaa akselin selvästi nollan oikealla puolella.

### b)
**Annettu:** a-kohdan suora ja siltä luetut pisteet; mittausaika $t = 300\,\text{s}$
**Kysytty:** veden ominaishöyrystymislämpö $r$ yksikössä $\text{MJ/kg}$
**Periaate:** Vesi kiehuu koko ajan, joten sen lämpötila ei nouse, ja höyrystämiseen kuluu se osa kuumentimen tehosta, joka ei johdu ympäristöön. Energia säilyy: $(P - P_\text{h})\,t = r\,\Delta m$, missä $P_\text{h}$ on häviöteho. Siitä $\Delta m = \dfrac{t}{r}\,P - \dfrac{t}{r}\,P_\text{h}$, joten suoran kulmakerroin on $\dfrac{t}{r}$ (luvut *Olomuodon muutokset* ja *Graafinen esitys ja suoran sovittaminen*).
**Kuvaajan lukeminen:** Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä, ei mittauspisteitä: $(100\,\text{W};\ 4{,}0\,\text{g})$ ja $(1100\,\text{W};\ 137{,}0\,\text{g})$.
**Kaava:** $k = \dfrac{\Delta(\Delta m)}{\Delta P} = \dfrac{t}{r}$, joten $r = \dfrac{t}{k}$
**Muunnokset:** Kulmakerroin grammoista kilogrammoiksi: $1\,\text{g} = 10^{-3}\,\text{kg}$. Yksikkö $\tfrac{\text{s}}{\text{kg/W}} = \tfrac{\text{W}\cdot\text{s}}{\text{kg}} = \tfrac{\text{J}}{\text{kg}}$, ja lopuksi $1\,\text{MJ} = 10^{6}\,\text{J}$.
**Sijoitus:** $k = \dfrac{137{,}0\,\text{g} - 4{,}0\,\text{g}}{1100\,\text{W} - 100\,\text{W}} = \dfrac{133{,}0\,\text{g}}{1000\,\text{W}} = 0{,}133\,\tfrac{\text{g}}{\text{W}}$ ja $r = \dfrac{300\,\text{s}}{0{,}133 \cdot 10^{-3}\,\tfrac{\text{kg}}{\text{W}}} = 2{,}26 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} = 2{,}26\,\text{MJ/kg}$
**Vastaus:** $r \approx 2{,}26\,\text{MJ/kg}$. Kolme merkitsevää numeroa on yläraja, koska silmämääräisesti sovitetun suoran kulmakerroin on noin $\pm 2\,\%$ tarkka; $2{,}3\,\text{MJ/kg}$ on yhtä hyvä vastaus.
**Järkevyys:** Taulukkoarvo on $2{,}26\,\text{MJ/kg}$, ja pienimmän neliösumman suora antaa $2{,}26\,\text{MJ/kg}$ samoin. Tarkistus yhdellä pisteellä: teholla $600\,\text{W}$ höyrystämiseen jää noin $530\,\text{W}$, ja $530\,\text{W} \cdot 300\,\text{s} : 2{,}26\,\tfrac{\text{MJ}}{\text{kg}} \approx 70\,\text{g}$, kuten taulukossa.

### c)
**Annettu:** a-kohdan suora, joka leikkaa vaaka-akselin; b-kohdan kulmakerroin $k = 0{,}133\,\text{g/W}$ ja suoran piste $(100\,\text{W};\ 4{,}0\,\text{g})$
**Kysytty:** teho $P_\text{h}$, jolla vesi ei suoran mukaan höyrystyisi, ja sen tulkinta
**Periaate:** Suoran ja vaaka-akselin leikkauskohdassa $\Delta m = 0$. Energiataseen $(P - P_\text{h})\,t = r\,\Delta m$ mukaan se tapahtuu, kun $P = P_\text{h}$: kuumentimen koko teho johtuu silloin astian seinien ja vedenpinnan kautta huoneeseen. Kiehuva vesi on aina $100\,{}^\circ\text{C}$:ssa, joten lämpötilaero huoneeseen ja siksi häviöteho pysyvät samoina kaikilla tehoilla (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kuvaajan lukeminen:** Katkoviivana jatkettu suora leikkaa vaaka-akselin noin kohdassa $70\,\text{W}$.
**Kaava:** $0 = k\,(P_\text{h} - P_1) + \Delta m_1$, joten $P_\text{h} = P_1 - \dfrac{\Delta m_1}{k}$
**Muunnokset:** Ei tarvita: kulmakerroin ja massa ovat grammoina ja teho watteina.
**Sijoitus:** $P_\text{h} = 100\,\text{W} - \dfrac{4{,}0\,\text{g}}{0{,}133\,\tfrac{\text{g}}{\text{W}}} = 100\,\text{W} - 30\,\text{W} = 70\,\text{W}$
**Vastaus:** $P_\text{h} \approx 70\,\text{W}$, eli noin $70\,\text{W}$ kuumentimen tehosta johtuu huoneeseen eikä höyrystä vettä. Yksi tai kaksi merkitsevää numeroa, koska leikkauskohta saadaan jatkamalla suoraa mitatun alueen ulkopuolelle ja pieni muutos kulmakertoimessa siirtää sitä kymmenillä wateilla.
**Järkevyys:** Pienimmän neliösumman suora leikkaa akselin kohdassa $69\,\text{W}$. Häviöteho on muutama prosentti suurimmasta tehosta mutta yli kolmannes pienimmästä, mikä sopii avoimen teräsastian lämmönjohtumiseen ja konvektioon.

### d)
**Kysytty:** miksi yhden mittauksen tulos $2{,}54\,\text{MJ/kg}$ on liian suuri ja kumpi tulos on luotettavampi
**Periaate:** Energia säilyy: kuumentimen energia $P\,t$ jakautuu höyrystämiseen ja huoneeseen johtuvaan lämpöön, $P\,t = r\,\Delta m + P_\text{h}\,t$ (luku *Olomuodon muutokset*).
**Mallivastaus:** Yhden mittauksen laskussa $r = \dfrac{P\,t}{\Delta m}$ koko kuumentimen energia oletetaan kuluneen höyrystämiseen. Todellisuudessa noin $70\,\text{W}$ johtuu huoneeseen, joten teholla $600\,\text{W}$ höyrystämiseen jää vain noin $530\,\text{W}$. Laskussa on siis liikaa energiaa samaa massaa kohti, ja tulos on noin $600 : 530 \approx 1{,}13$-kertainen eli noin $13\,\%$ liian suuri. Kuvaajasta saatu tulos on luotettavampi. Vakiona pysyvä häviöteho siirtää suoraa sivulle mutta ei muuta sen kulmakerrointa, joten kulmakertoimesta laskettu $r$ ei sisällä häviötä. Lisäksi viisi mittausta ja niiden lomitse sovitettu suora pienentävät yksittäisen lukeman satunnaisvirheen vaikutusta. Menetelmä olettaa, että häviöteho on sama kaikilla tehoilla. Se on perusteltua, koska kiehuva vesi on aina $100\,{}^\circ\text{C}$:ssa, ja pisteiden asettuminen suoralle tukee oletusta.

### Yleisiä virheitä
- Suora pakotetaan origon kautta, jolloin kulmakerroin ja $r$ vääristyvät ja häviöteho jää näkemättä.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- b-kohdassa grammoja ei muunneta kilogrammoiksi, jolloin tulokseksi tulee tuhat kertaa liian pieni arvo.
- b-kohdassa $r$:ksi otetaan kulmakerroin itse eikä $\dfrac{t}{k}$.
- d-kohdassa sanotaan vain ”mittausvirhe” kertomatta, mikä energia on laskettu väärin ja mihin suuntaan se muuttaa tulosta.

### Hyväksytään myös
- Kulmakerroin $0{,}128$…$0{,}138\,\text{g/W}$, kun suora on sovitettu silmämääräisesti pisteiden lomitse, ja sen mukaiset tulokset: b-kohdassa $2{,}2$–$2{,}3\,\text{MJ/kg}$ ja c-kohdassa $50$–$90\,\text{W}$.
- b-kohdassa massan tuotto voidaan laskea myös sekunnissa: $\dfrac{\Delta m}{t}$ tehon funktiona, jolloin kulmakerroin on $\dfrac{1}{r}$.

## fy9-lampo-s4

### a)
**Kysytty:** miksi järvi jäätyy pinnalta ja miksi pohjan vesi on noin $4\,{}^\circ\text{C}$:ista
**Periaate:** Useimmat aineet laajenevat lämmetessään, mutta vesi kutistuu $0\,{}^\circ\text{C}$:n ja $4\,{}^\circ\text{C}$:n välillä, joten sen tiheys on suurin noin $4\,{}^\circ\text{C}$:ssa. Tiheämpi vesi painuu alas ja kevyempi nousee ylös (luku *Lämpölaajeneminen*).
**Mallivastaus:** Syksyllä kylmä ilma jäähdyttää järven pintaa. Niin kauan kuin pintavesi on yli $4\,{}^\circ\text{C}$:ista, jäähtyessään se tihenee ja painuu pohjalle, ja tilalle nousee lämpimämpää vettä. Näin koko järvi jäähtyy vähitellen noin $4\,{}^\circ\text{C}$:seen. Kun pinta jäähtyy tämän alle, vesi alkaa laajeta jäähtyessään: kylmempi vesi on nyt kevyempää kuin pohjan $4\,{}^\circ\text{C}$:inen, joten se jää pinnalle ja jäätyy siellä. Pohjalle jää tihein, noin $4\,{}^\circ\text{C}$:inen vesi, eikä se nouse pintaan jäähtymään. Lisäksi jää on vettä kevyempää ja kelluu, joten järvi jäätyy pinnalta alaspäin eikä pohjasta ylöspäin.

### b)
**Kysytty:** mihin jäätyvän veden energia menee ja miksi jää kasvaa hitaammin paksuna
**Periaate:** Jäätyessään vesi luovuttaa sulamislämmön $Q = sm$, vaikka lämpötila pysyy $0\,{}^\circ\text{C}$:ssa (luku *Olomuodon muutokset*). Lämpö johtuu lämpimästä kylmään, ja johtuva teho on sitä pienempi, mitä paksumpi kerros on samalla lämpötilaerolla (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Mallivastaus:** Jään alapinnalla vesi on $0\,{}^\circ\text{C}$:ssa. Jotta se jäätyisi, siitä on siirryttävä pois sulamislämpö, noin $334\,\text{kJ}$ jokaista kilogrammaa kohti; yhden senttimetrin kerros neliömetrillä vaatii noin $3\,\text{MJ}$. Energia säilyy, joten tämän energian on johduttava jään läpi kylmään ilmaan, ja jää kasvaa vain sitä mukaa kuin energiaa johtuu pois. Jään läpi johtuva teho riippuu lämpötilaerosta pakkasilman ja $0\,{}^\circ\text{C}$:n alapinnan välillä sekä kerroksen paksuudesta. Paksu kerros eristää paremmin, eli sen U-arvo on pienempi, joten samalla pakkasella sen läpi johtuu pienempi teho. Siksi ohut syysjää paksunee nopeasti, mutta $40\,\text{cm}$:n jää kasvaa samalla pakkasella hitaasti.

### c)
**Kysytty:** vahvistaako lumipeite jäätä
**Periaate:** Lumessa on paljon ilmaa, ja ilma johtaa lämpöä huonosti (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*). Jään kasvu vaatii, että jäätymisessä vapautuva energia johtuu pois (b-kohta).
**Mallivastaus:** Väite on väärä. Lumi ei siirrä jäähän ”kylmää”: energiaa siirtyy aina lämpimämmästä kylmempään, eli jäästä lumen kautta ilmaan. Lumi on huono lämmönjohde, koska siinä on paljon ilmaa. Se toimii jään päällä eristeenä kuin villa seinässä, joten jään alapinnalta johtuu vähemmän energiaa pois ja vettä jäätyy vähemmän. Paksun lumipeitteen alla jää siis kasvaa hitaammin ja jää ohuemmaksi kuin paljaana. Lisäksi raskas lumi voi painaa jäätä alas, jolloin vettä nousee halkeamista jään päälle ja syntyy heikkoa sohjoa tai kohvajäätä. Lumi heikentää jäätä eikä vahvista sitä.

### Yleisiä virheitä
- a-kohdassa sanotaan vain, että ”jää kelluu”, mutta ei selitetä, miksi pohjan vesi on $4\,{}^\circ\text{C}$:ista.
- Väitetään, että kylmä vesi on aina tiheämpää kuin lämmin.
- b-kohdassa unohdetaan, että jäätyminen vapauttaa energiaa, ja selitetään kasvu pelkällä lämpötilalla.
- c-kohdassa hyväksytään ajatus kylmyyden siirtymisestä lumesta jäähän.

## fy9-lampo-s5

### a)
**Annettu:** vesi $m_\text{v} = 0{,}200\,\text{kg}$, $T_\text{v} = 40{,}0\,{}^\circ\text{C}$; jää $m_\text{j} = 0{,}0500\,\text{kg}$; lopputila $T = 14{,}3\,{}^\circ\text{C}$; $c_\text{v} = 4190\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** ryhmän tulos $s$ yksikössä $\text{kJ/kg}$ ja sen oletus jään alkulämpötilasta
**Periaate:** Energia säilyy, kun muki ja ilma eivät ota lämpöä: veden luovuttama lämpö on yhtä suuri kuin jään vastaanottama. Ryhmän laskussa jää vain sulaa ($Q = sm$) ja sulamisvesi lämpenee $0\,{}^\circ\text{C}$:sta lopputilaan ($Q = cm\Delta T$). Jään lämpenemistä ei ole, joten ryhmä on olettanut jään olleen $0\,{}^\circ\text{C}$:ista (luku *Lämpötasapaino olomuodon muuttuessa*).
**Kaava:** $c_\text{v} m_\text{v} (T_\text{v} - T) = s\,m_\text{j} + c_\text{v} m_\text{j}\,(T - 0\,{}^\circ\text{C})$, joten $s = \dfrac{c_\text{v} m_\text{v} (T_\text{v} - T) - c_\text{v} m_\text{j} T}{m_\text{j}}$
**Muunnokset:** Lämpötilaerot ovat samat kelvineinä: vesi jäähtyy $25{,}7\,\text{K}$ ja sulamisvesi lämpenee $14{,}3\,\text{K}$. Lopuksi $1\,\text{kJ} = 1000\,\text{J}$.
**Sijoitus:** Veden luovuttama lämpö on $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}200\,\text{kg} \cdot 25{,}7\,\text{K} = 21\,537\,\text{J}$ ja sulamisveden lämpeneminen $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}0500\,\text{kg} \cdot 14{,}3\,\text{K} = 2996\,\text{J}$. Siis $s = \dfrac{21\,537\,\text{J} - 2996\,\text{J}}{0{,}0500\,\text{kg}} = 370\,800\,\tfrac{\text{J}}{\text{kg}} = 371\,\text{kJ/kg}$.
**Vastaus:** $371\,\text{kJ/kg}$, kolme merkitsevää numeroa kuten massat ja lämpötilat. Ryhmä on olettanut, että jää oli $0\,{}^\circ\text{C}$:ista, vaikka se otettiin pakastimesta.
**Järkevyys:** Tulos on noin $11\,\%$ taulukkoarvoa $334\,\text{kJ/kg}$ suurempi, mikä on liikaa huolellisen mittauksen satunnaisvirheeksi. Se viittaa systemaattiseen virheeseen, jota b-kohdassa etsitään.

### b)
**Annettu:** a-kohdan tiedot; jään alkulämpötila $T_\text{j} = -18{,}0\,{}^\circ\text{C}$, $c_\text{j} = 2100\,\text{J/(kg}\cdot\text{K)}$
**Kysytty:** korjattu ominaissulamislämpö $s$ ja johtopäätöksen arvio
**Periaate:** Pakastimen jää lämpenee ensin $-18{,}0\,{}^\circ\text{C}$:sta $0\,{}^\circ\text{C}$:seen, ja siihen kuluu osa veden luovuttamasta energiasta. Ryhmän laskussa tämä osa on luettu sulamislämmöksi, joten sen tulos on liian suuri. Energiataseeseen lisätään jään lämpeneminen.
**Kaava:** $c_\text{v} m_\text{v} (T_\text{v} - T) = c_\text{j} m_\text{j} \Delta T_\text{j} + s\,m_\text{j} + c_\text{v} m_\text{j} T$, joten $s = \dfrac{c_\text{v} m_\text{v} (T_\text{v} - T) - c_\text{j} m_\text{j} \Delta T_\text{j} - c_\text{v} m_\text{j} T}{m_\text{j}}$
**Muunnokset:** Jään lämpeneminen $\Delta T_\text{j} = 0\,{}^\circ\text{C} - (-18{,}0\,{}^\circ\text{C}) = 18{,}0\,\text{K}$, sama kelvineinä.
**Sijoitus:** $c_\text{j} m_\text{j} \Delta T_\text{j} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}0500\,\text{kg} \cdot 18{,}0\,\text{K} = 1890\,\text{J}$ ja $s = \dfrac{21\,537\,\text{J} - 1890\,\text{J} - 2996\,\text{J}}{0{,}0500\,\text{kg}} = 333\,000\,\tfrac{\text{J}}{\text{kg}} = 333\,\text{kJ/kg}$
**Vastaus:** $333\,\text{kJ/kg}$, kolme merkitsevää numeroa kuten mittaustulokset. Ryhmän johtopäätös ei pidä: korjattu tulos on taulukkoarvon $334\,\text{kJ/kg}$ mukainen, ja ero johtui virheellisestä oletuksesta, ei taulukosta. Muki ei myöskään selitä eroa. Jos muki ottaisi lämpöä, ryhmän kaava lukisi senkin jään hyväksi, ja tulos olisi tosin liian suuri, mutta erotus $1890\,\text{J}$ vaatisi mukilta noin $1890\,\text{J} : 25{,}7\,\text{K} \approx 70\,\text{J/K}$ lämpökapasiteetin. Muutaman gramman styroksimukin lämpökapasiteetti on vain muutama $\text{J/K}$, ja korjattu arvo on jo taulukon mukainen.
**Järkevyys:** Jään lämpeneminen vie $1890\,\text{J}$ eli vain noin $9\,\%$ veden luovuttamasta lämmöstä, mutta jaettuna pienellä jäämassalla se on $38\,\text{kJ/kg}$, juuri tulosten ero $371 - 333$. Korjattu arvo poikkeaa taulukosta alle prosentin, mikä on mittausten tarkkuuden rajoissa.

### c)
**Kysytty:** kolme parannusta mittaukseen ja niiden perustelut
**Periaate:** Luotettava mittaus poistaa systemaattiset virheet tai ottaa ne huomioon ja pienentää satunnaisvirhettä toistoilla (luku *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Ensiksi jää otetaan jäävesiastiasta, jossa se on sulamassa ja siis tasan $0\,{}^\circ\text{C}$:ista, ja sen pinta kuivataan paperilla juuri ennen kuin se pudotetaan veteen. Silloin laskun oletus pätee, eikä jään pinnalla oleva vesi kasvata mitattua jäämassaa. Toinen tapa on mitata jään lämpötila ja ottaa lämpeneminen huomioon kuten b-kohdassa. Toiseksi jään massa määritetään erotuksena: muki ja vesi punnitaan ennen jään lisäämistä ja sulamisen jälkeen, jolloin punnittu massa on juuri se jää, joka päätyi veteen eikä käsittelyn aikana sulanut tai pudonnut jää vääristä tulosta. Kolmanneksi lämmönvaihtoa ympäristön kanssa pienennetään: mukissa on kansi, ja alkulämpötila valitaan niin, että se on yhtä paljon huoneenlämmön yläpuolella kuin loppulämpötila sen alapuolella, jolloin huoneesta tuleva ja huoneeseen lähtevä lämpö lähes kumoavat toisensa. Lopuksi mittaus toistetaan useita kertoja, ja tuloksena ilmoitetaan keskiarvo ja tulosten vaihtelu.

### Yleisiä virheitä
- Sulamisveden lämpeneminen $0\,{}^\circ\text{C}$:sta lopputilaan unohdetaan, jolloin a-kohdassa saadaan noin $431\,\text{kJ/kg}$.
- b-kohdassa jään lämpenemiseen käytetään veden ominaislämpökapasiteettia.
- Muki hyväksytään selitykseksi arvioimatta, kuinka suuri sen lämpökapasiteetin pitäisi olla: styroksimukin lämpökapasiteetti on liian pieni selittämään $38\,\text{kJ/kg}$:n eroa.
- c-kohdassa ehdotetaan vain ”tarkempaa lämpömittaria” kertomatta, mihin virheeseen se vaikuttaa.

### Hyväksytään myös
- a-kohdassa sulamisveden lämpenemisen voi laskea omana terminään ja vähentää sen lopuksi; tulos on sama.

## fy9-lampo-s6

### a)
**Annettu:** auton massa $m = 1600\,\text{kg}$, nopeus $v = 90\,\text{km/h}$; levyjen massa $m_\text{l} = 30\,\text{kg}$, $c = 450\,\text{J/(kg}\cdot\text{K)}$; levyihin siirtyvä osuus $85\,\%$
**Kysytty:** levyjen lämpötilan nousu $\Delta T$
**Periaate:** Tasaisella tiellä jarrutus muuttaa auton liike-energian kitkassa jarrujen sisäenergiaksi; energia säilyy (luku *Mekaanisen energian säilyminen ja energiaperiaate*). Ilmanvastuksen osuus lyhyessä jarrutuksessa on pieni, joten se jätetään huomiotta. Levyt pysyvät kiinteinä, joten niiden vastaanottama lämpö nostaa lämpötilaa $Q = cm\Delta T$:n mukaan.
**Kaava:** $E_\text{k} = \tfrac{1}{2} m v^2$ ja $0{,}85\,E_\text{k} = c\,m_\text{l}\,\Delta T$, joten $\Delta T = \dfrac{0{,}85 \cdot \tfrac{1}{2} m v^2}{c\,m_\text{l}}$
**Muunnokset:** $90\,\text{km/h} = 90 \cdot \dfrac{1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$ ja $85\,\% = 0{,}85$.
**Sijoitus:** $E_\text{k} = \tfrac{1}{2} \cdot 1600\,\text{kg} \cdot (25\,\tfrac{\text{m}}{\text{s}})^2 = 500\,000\,\text{J}$ ja $\Delta T = \dfrac{0{,}85 \cdot 500\,000\,\text{J}}{450\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 30\,\text{kg}} = \dfrac{425\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 31{,}5\,\text{K}$
**Vastaus:** noin $31\,\text{K}$, kaksi merkitsevää numeroa kuten levyjen massa $30\,\text{kg}$ ja nopeus $90\,\text{km/h}$.
**Järkevyys:** Yksi pysäytys lämmittää levyjä muutamia kymmeniä asteita, mikä sopii kokemukseen: jarrulevyt ovat kovan jarrutuksen jälkeen kuumia mutta eivät hehku. Ilmanvastus pienentäisi levyihin tulevaa energiaa vähän, joten tulos on yläraja.

### b)
**Annettu:** pudotus $h = 250\,\text{m}$, matka $s = 4{,}0\,\text{km}$, ajovastus $F = 450\,\text{N}$, vakionopeus; $g = 9{,}81\,\text{m/s}^2$; a-kohdan tiedot
**Kysytty:** levyjen lämpötilan nousu $\Delta T$ ilman jäähtymistä
**Periaate:** Nopeus on vakio, joten liike-energia ei muutu. Energiaperiaatteen mukaan potentiaalienergian väheneminen $mgh$ kuluu ajovastusten työhön $Fs$ ja jarruihin (luvut *Liike-energia, potentiaalienergia ja mekaaninen energia* ja *Mekaanisen energian säilyminen ja energiaperiaate*). Jarruihin tulevasta energiasta $85\,\%$ lämmittää levyjä.
**Kaava:** $Q_\text{jarrut} = mgh - Fs$ ja $0{,}85\,Q_\text{jarrut} = c\,m_\text{l}\,\Delta T$, joten $\Delta T = \dfrac{0{,}85\,(mgh - Fs)}{c\,m_\text{l}}$
**Muunnokset:** $4{,}0\,\text{km} = 4{,}0 \cdot 1000\,\text{m} = 4000\,\text{m}$.
**Sijoitus:** $mgh = 1600\,\text{kg} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 250\,\text{m} = 3\,924\,000\,\text{J}$, $Fs = 450\,\text{N} \cdot 4000\,\text{m} = 1\,800\,000\,\text{J}$ ja $\Delta T = \dfrac{0{,}85 \cdot 2\,124\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = \dfrac{1\,805\,400\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 133{,}7\,\text{K}$
**Vastaus:** noin $1{,}3 \cdot 10^{2}\,\text{K}$ eli $130\,\text{K}$, kaksi merkitsevää numeroa kuten matka $4{,}0\,\text{km}$.
**Järkevyys:** Alamäki vapauttaa noin neljä kertaa enemmän energiaa jarruihin kuin yksi pysäytys nopeudesta $90\,\text{km/h}$ ($1{,}81\,\text{MJ}$ ja $0{,}43\,\text{MJ}$), joten nousu on noin neljä kertaa suurempi. Ilman jäähtymistä levyt kuumenisivat noin $150\,{}^\circ\text{C}$:seen, mikä on mahdollista mutta jo lähellä tavallisen jarrun mukavaa käyttöaluetta.

### c)
**Annettu:** b-kohdan levyihin tullut energia $Q = 1{,}805\,\text{MJ}$; levyjen lämpötila nousi $80\,\text{K}$; $c\,m_\text{l} = 13\,500\,\text{J/K}$
**Kysytty:** ilmaan siirtyneen energian osuus prosentteina ja siirtymistavat
**Periaate:** Energia säilyy: levyihin tullut energia joko jäi levyihin ja nosti niiden lämpötilaa ($Q = cm\Delta T$) tai siirtyi mäen aikana pois. Kuuma levy luovuttaa lämpöä ohi virtaavaan ilmaan konvektiona, säteilee ja johtaa lämpöä napaan ja vanteeseen (luku *Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*).
**Kaava:** $Q_\text{ilma} = Q - c\,m_\text{l}\,\Delta T$ ja osuus $= \dfrac{Q_\text{ilma}}{Q}$
**Muunnokset:** Ei tarvita: energiat ovat jouleina, ja suhdeluku muutetaan prosenteiksi kertomalla luvulla $100\,\%$.
**Sijoitus:** $Q_\text{ilma} = 1\,805\,400\,\text{J} - 13\,500\,\tfrac{\text{J}}{\text{K}} \cdot 80\,\text{K} = 1\,805\,400\,\text{J} - 1\,080\,000\,\text{J} = 725\,400\,\text{J}$ ja osuus $= \dfrac{725\,400\,\text{J}}{1\,805\,400\,\text{J}} = 0{,}402 = 40{,}2\,\%$
**Vastaus:** noin $40\,\%$, kaksi merkitsevää numeroa kuten b-kohdan tulos. Energia siirtyi pääosin konvektiona levyn ohi virtaavaan ilmaan, lisäksi lämpösäteilynä ja johtumalla navan ja vanteen kautta.
**Järkevyys:** Mäki kestää $4000\,\text{m} : 16{,}7\,\tfrac{\text{m}}{\text{s}} = 240\,\text{s}$, ja levyihin tulee keskimäärin noin $7{,}5\,\text{kW}$. Ilmaan siirtyi keskimäärin $725\,\text{kJ} : 240\,\text{s} \approx 3\,\text{kW}$, mikä on uskottava neljälle kuumalle levylle ajoviimassa.

### d)
**Kysytty:** miksi moottorijarrutus säästää jarruja energian kannalta
**Periaate:** Energia säilyy, joten potentiaalienergian väheneminen muuttuu sisäenergiaksi jossakin. Moottorijarrutuksessa pyörät pyörittävät moottoria, jonka kitka vastustaa liikettä (luku *Mekaanisen energian säilyminen ja energiaperiaate*).
**Mallivastaus:** Moottorijarrutuksessa potentiaalienergia ei katoa, vaan se muuttuu moottorin kitkassa moottorin sisäenergiaksi. Moottorin jäähdytysjärjestelmä on tehty siirtämään suuria lämpötehoja ilmaan, joten moottori ei ylikuumene. Silloin jarrulevyihin tulee vähän energiaa, ne pysyvät viileinä, ja jarrut toimivat täydellä teholla, kun niitä todella tarvitaan. Neuvo on siis perusteltu: energia ei vähene, mutta sen lämmittämä kohde vaihtuu jarruista moottoriin.

### Yleisiä virheitä
- Nopeutta ei muunneta metreiksi sekunnissa, jolloin liike-energia on yli kymmenkertainen.
- b-kohdassa koko potentiaalienergia annetaan jarruille, jolloin tulokseksi tulee noin $250\,\text{K}$.
- b-kohdassa lasketaan mukaan liike-energia, vaikka nopeus on vakio.
- c-kohdassa sanotaan, että energia ”kului” tai ”hävisi”, kertomatta, mihin se siirtyi.
- d-kohdassa väitetään, että moottorijarrutuksessa energia ei muutu lämmöksi lainkaan.

### Hyväksytään myös
- a-kohdassa vastaus $31{,}5\,\text{K}$ tai $32\,\text{K}$, kun perusteluna on pyöristys.
