## fy9-tasavirta-s1

### a)
**Annettu:** raitoja $10$, kiskojen välinen jännite $U = 13{,}5\,\text{V}$, lämmittimen virta $I = 12{,}0\,\text{A}$
**Kysytty:** lämmittimen teho $P$ ja yhden raidan resistanssi $R_1$
**Periaate:** Jokainen raita kulkee kiskosta toiseen, joten raidat ovat rinnan. Kaikkien raitojen yli on sama jännite $13{,}5\,\text{V}$, ja samanlaiset raidat jakavat virran tasan (luku *Vastusten sarja- ja rinnankytkennät*). Lämmittimen teho on jännitteen ja virran tulo (luku *Sähköteho ja vastuksen lämpeneminen*). Raidan resistanssi on raidan jännitteen ja virran suhde (luku *Resistanssi ja Ohmin laki*).
**Kaava:** $P = UI$, $I_1 = \dfrac{I}{10}$ ja $R_1 = \dfrac{U}{I_1}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $P = 13{,}5\,\text{V} \cdot 12{,}0\,\text{A} = 162\,\text{W}$, $I_1 = \dfrac{12{,}0\,\text{A}}{10} = 1{,}20\,\text{A}$ ja $R_1 = \dfrac{13{,}5\,\text{V}}{1{,}20\,\text{A}} = 11{,}25\,\Omega$
**Vastaus:** Lämmittimen teho on $P \approx 162\,\text{W}$, ja yhden raidan resistanssi on $R_1 \approx 11{,}3\,\Omega$. Tarkkuus on kolme merkitsevää numeroa kuten jännitteessä ja virrassa.
**Järkevyys:** Koko lämmittimen resistanssi on $\tfrac{11{,}25\,\Omega}{10} = 1{,}125\,\Omega$, ja $\tfrac{13{,}5\,\text{V}}{1{,}125\,\Omega} = 12{,}0\,\text{A}$, kuten mitattiin. Muutaman sadan watin teho riittää sulattamaan ohuen huurteen lasista muutamassa minuutissa.

### b)
**Annettu:** raidan resistanssi $R_1 = 11{,}25\,\Omega$ (a-kohta), pituus $l = 1{,}10\,\text{m}$, leveys $b = 3{,}0\,\text{mm}$, resistiivisyys $\rho = 3{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m}$
**Kysytty:** raidan paksuus $h$
**Periaate:** Raita on johdin, joka on joka kohdasta yhtä paksu. Sen resistanssi on verrannollinen pituuteen ja kääntäen verrannollinen poikkipinta-alaan (luku *Resistanssi ja Ohmin laki*). Kääntäen verrannollinen tarkoittaa, että kun pinta-ala kasvaa kaksinkertaiseksi, resistanssi pienenee puoleen. Raidan poikkileikkaus on suorakulmio. Sen pinta-ala on leveys kertaa paksuus.
**Kaava:** $R_1 = \rho\,\dfrac{l}{A}$, joten $A = \dfrac{\rho l}{R_1}$, ja $A = bh$, joten $h = \dfrac{A}{b} = \dfrac{\rho l}{R_1 b}$
**Muunnokset:** $3{,}0\,\text{mm} = 3{,}0 \cdot 10^{-3}\,\text{m}$ ja lopuksi $1\,\text{m} = 10^{6}\,\mu\text{m}$
**Sijoitus:** $A = \dfrac{3{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 1{,}10\,\text{m}}{11{,}25\,\Omega} = 2{,}933 \cdot 10^{-8}\,\text{m}^2$ ja $h = \dfrac{2{,}933 \cdot 10^{-8}\,\text{m}^2}{3{,}0 \cdot 10^{-3}\,\text{m}} = 9{,}78 \cdot 10^{-6}\,\text{m} = 9{,}78\,\mu\text{m}$
**Vastaus:** Raidan paksuus on $h \approx 9{,}8\,\mu\text{m}$ eli noin sadasosamillimetri. Tarkkuus on kaksi merkitsevää numeroa kuten resistiivisyydessä ja leveydessä.
**Järkevyys:** Johdinraita on painettu lasin pintaan, ja se on hyvin ohut kalvo. Siksi muutaman mikrometrin paksuus on uskottava. Jos raita olisi millimetrin paksuinen, sen resistanssi olisi sata kertaa pienempi, ja virta olisi liian suuri.

### c)
**Kysytty:** miten virta ja teho muuttuvat, kun yksi raita katkeaa, ja lämpeneekö lasi ehjien raitojen kohdalta yhtä hyvin kuin ennen
**Periaate:** Rinnakkaisten haarojen yli on sama jännite. Siksi katkennut haara ei muuta muiden haarojen jännitettä eikä virtaa (luku *Vastusten sarja- ja rinnankytkennät*). Kiskoihin tuleva virta on haarojen virtojen summa (luku *Kirchhoffin lait ja potentiaali virtapiirissä*).
**Mallivastaus:** Katkenneen raidan läpi ei enää kulje virtaa. Yhdeksän ehjän raidan yli on kuitenkin edelleen $13{,}5\,\text{V}$. Jokaisen ehjän raidan virta on yhä $1{,}20\,\text{A}$ ja teho $13{,}5\,\text{V} \cdot 1{,}20\,\text{A} = 16{,}2\,\text{W}$. Siksi ehjät raidat lämmittävät lasia kuten ennen. Lämmittimen virta pienenee arvoon $9 \cdot 1{,}20\,\text{A} = 10{,}8\,\text{A}$, ja teho pienenee arvoon $13{,}5\,\text{V} \cdot 10{,}8\,\text{A} \approx 146\,\text{W}$. Kumpikin pienenee siis kymmenesosan. Katkenneen raidan kohdalle jää kapea kaista. Siinä huurre sulaa vain viereisten raitojen lämmön avulla. Jos raidat olisivat sarjassa, yksi katkos sammuttaisi koko lämmittimen.

### d)
**Annettu:** raidan resistanssi $R_1 = 11{,}25\,\Omega$ (a-kohta), $10$ raitaa rinnan, akun lähdejännite $E = 12{,}6\,\text{V}$ ja sisäinen resistanssi $R_\text{s} = 0{,}020\,\Omega$, lämmittimen teho moottorin käydessä $162\,\text{W}$ (a-kohta)
**Kysytty:** lämmittimen teho $P$, kun lämmitin saa sähkön pelkästä akusta
**Periaate:** Kymmenen samanlaista rinnakkaista raitaa vastaa yhtä vastusta. Sen resistanssi on kymmenesosa raidan resistanssista (luku *Vastusten sarja- ja rinnankytkennät*). Akun sisäinen resistanssi on sarjassa lämmittimen kanssa. Siksi virran määrää niiden yhteinen resistanssi (luku *Lähdejännite ja sisäinen resistanssi*). Lämmittimen teho saadaan sen virrasta Joulen lain avulla (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kaava:** $R = \dfrac{R_1}{10}$, $I = \dfrac{E}{R + R_\text{s}}$ ja $P = RI^2$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $R = \dfrac{11{,}25\,\Omega}{10} = 1{,}125\,\Omega$, $I = \dfrac{12{,}6\,\text{V}}{1{,}125\,\Omega + 0{,}020\,\Omega} = 11{,}00\,\text{A}$ ja $P = 1{,}125\,\Omega \cdot (11{,}00\,\text{A})^2 = 136{,}2\,\text{W}$
**Vastaus:** Lämmittimen teho on $P \approx 136\,\text{W}$. Tarkkuus on kolme merkitsevää numeroa kuten lähdejännitteessä $12{,}6\,\text{V}$.
**Järkevyys:** Napajännite on $12{,}6\,\text{V} - 0{,}020\,\Omega \cdot 11{,}0\,\text{A} = 12{,}38\,\text{V}$, ja $\tfrac{(12{,}38\,\text{V})^2}{1{,}125\,\Omega} \approx 136\,\text{W}$. Tulos on sama. Teho on noin $84\,\%$ siitä tehosta, joka saadaan moottorin käydessä. Syy on se, että teho on verrannollinen jännitteen neliöön ja $\left(\tfrac{12{,}38}{13{,}5}\right)^2 \approx 0{,}84$. Kun moottori käy, auton laturi pitää jännitteen korkeampana.

### Yleisiä virheitä
- a-kohdassa raidan resistanssiksi lasketaan koko lämmittimen resistanssi $\tfrac{13{,}5\,\text{V}}{12{,}0\,\text{A}} = 1{,}125\,\Omega$. Tai raidat oletetaan sarjaan, jolloin resistanssi jaetaan kymmenellä väärään suuntaan.
- b-kohdassa millimetrejä ei muuteta metreiksi. Tai poikkipinta-alaksi otetaan $\pi r^2$, vaikka raita on litteä.
- c-kohdassa oletetaan, että muiden raitojen virta kasvaa, koska kokonaisvirta "jakautuu" yhdeksälle.
- d-kohdassa sisäinen resistanssi unohdetaan. Tai teho lasketaan lähdejännitteellä $\tfrac{(12{,}6\,\text{V})^2}{1{,}125\,\Omega} = 141\,\text{W}$.

### Hyväksytään myös
- d-kohdassa teho napajännitteestä $P = \tfrac{U^2}{R}$, kun $U = E - R_\text{s} I$ on laskettu.

## fy9-tasavirta-s2

### a)
**Annettu:** nimellisjännite $U = 36\,\text{V}$, kapasiteetti $Q = 10{,}4\,\text{Ah}$
**Kysytty:** akkuun varastoitunut energia $W$ wattitunteina ja megajouleina
**Periaate:** Kapasiteetti kertoo, kuinka suuri varaus akun läpi voi kulkea. Jokainen varausyksikkö luovuttaa energiaa jännitteen verran. Siksi akun energia on nimellisjännite kertaa kapasiteetti (luku *Akut ja latauspiiri*).
**Kaava:** $W = UQ$
**Muunnokset:** $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$ ja $1\,\text{Wh} = 1\,\text{W} \cdot 3600\,\text{s} = 3600\,\text{J}$
**Sijoitus:** $W = 36\,\text{V} \cdot 10{,}4\,\text{Ah} = 374{,}4\,\text{Wh} = 374{,}4 \cdot 3600\,\text{J} = 1{,}348 \cdot 10^{6}\,\text{J}$
**Vastaus:** $W \approx 374\,\text{Wh} \approx 1{,}35\,\text{MJ}$, kolme merkitsevää numeroa kuten kapasiteetissa $10{,}4\,\text{Ah}$.
**Järkevyys:** Puhelimen akussa on noin $15\,\text{Wh}$ ja kannettavan tietokoneen akussa noin $50\,\text{Wh}$. Potkulaudan akussa on siis yhtä paljon energiaa kuin muutamassa kannettavan tietokoneen akussa. Se sopii ajoneuvolle.

### b)
**Annettu:** kapasiteetti $Q = 10{,}4\,\text{Ah}$, keskimääräinen virta $I = 7{,}5\,\text{A}$, nopeus $v = 20\,\text{km/h}$
**Kysytty:** ajomatka $s$ täydellä akulla
**Periaate:** Kun virta on vakio, akun läpi kulkeva varaus on virta kertaa aika. Siksi kapasiteetista ja virrasta saadaan ajoaika (luku *Akut ja latauspiiri*). Kun nopeus on tasainen, matka on nopeus kertaa aika. Oletetaan, että koko kapasiteetti voidaan käyttää ja virta pysyy keskiarvossaan.
**Kaava:** $Q = It$, joten $t = \dfrac{Q}{I}$, ja $s = vt$
**Muunnokset:** Kun ampeeritunnit jaetaan ampeereilla, saadaan aika suoraan tunteina.
**Sijoitus:** $t = \dfrac{10{,}4\,\text{Ah}}{7{,}5\,\text{A}} = 1{,}387\,\text{h}$ ja $s = 20\,\tfrac{\text{km}}{\text{h}} \cdot 1{,}387\,\text{h} = 27{,}7\,\text{km}$
**Vastaus:** Akulla voi ajaa noin $s \approx 28\,\text{km}$. Tarkkuus on kaksi merkitsevää numeroa kuten virrassa $7{,}5\,\text{A}$ ja nopeudessa $20\,\text{km/h}$.
**Järkevyys:** Ajoaika on noin $1\,\text{h}\ 23\,\text{min}$. Keskimääräinen teho on $36\,\text{V} \cdot 7{,}5\,\text{A} = 270\,\text{W}$, mikä on tavallinen potkulaudan moottorille. Oikea matka on usein lyhyempi: mäet, vastatuuli ja kylmä sää kasvattavat virtaa. Lisäksi akkua ei kannata purkaa aivan tyhjäksi.

### c)
**Annettu:** laturin jännite $U_\text{lat} = 42{,}0\,\text{V}$, tyhjän akun lähdejännite $E = 34{,}5\,\text{V}$ ja sisäinen resistanssi $R_\text{s} = 0{,}40\,\Omega$, laturin ja johtojen resistanssi $R = 2{,}6\,\Omega$
**Kysytty:** latausvirta $I$ ja akun napajännite $U$ latauksen alussa
**Periaate:** Latauspiirin silmukka kierretään virran suuntaan (luku *Kirchhoffin lait ja potentiaali virtapiirissä*). Potentiaali nousee laturissa $U_\text{lat}$:n verran. Se laskee resistansseissa $RI$:n ja $R_\text{s} I$:n verran. Lisäksi potentiaali laskee akun lähdejännitteen verran, koska latauksessa virta kulkee akun läpi plusnavalta miinusnavalle (luku *Akut ja latauspiiri*). Siksi latausvirtaa ajaa laturin jännitteen ja akun lähdejännitteen erotus.
**Kaava:** $U_\text{lat} - RI - R_\text{s} I - E = 0$, joten $I = \dfrac{U_\text{lat} - E}{R + R_\text{s}}$; napajännite latauksessa $U = E + R_\text{s} I$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $I = \dfrac{42{,}0\,\text{V} - 34{,}5\,\text{V}}{2{,}6\,\Omega + 0{,}40\,\Omega} = \dfrac{7{,}5\,\text{V}}{3{,}0\,\Omega} = 2{,}50\,\text{A}$ ja $U = 34{,}5\,\text{V} + 0{,}40\,\Omega \cdot 2{,}50\,\text{A} = 35{,}5\,\text{V}$
**Vastaus:** Latausvirta on $I \approx 2{,}5\,\text{A}$, kaksi merkitsevää numeroa kuten jännitteiden erotuksessa $7{,}5\,\text{V}$. Napajännite on $U \approx 35{,}5\,\text{V}$.
**Järkevyys:** Latauksessa napajännite on suurempi kuin lähdejännite, kuten pitää. Laturin ja johtojen yli on $2{,}6\,\Omega \cdot 2{,}5\,\text{A} = 6{,}5\,\text{V}$, ja $35{,}5\,\text{V} + 6{,}5\,\text{V} = 42{,}0\,\text{V}$. Kun akku latautuu, sen lähdejännite kasvaa. Siksi virta pienenee, ja lataus hidastuu lopussa.

### d)
**Annettu:** laturin jännite $U_\text{lat} = 42{,}0\,\text{V}$, akun läpi kulkeva varaus $Q = 10{,}4\,\text{Ah}$, akkuun varastoitunut energia $W_\text{akku} = 374{,}4\,\text{Wh}$ (a-kohta), hinta $15\,\text{snt/kWh}$
**Kysytty:** latauksen hyötysuhde $\eta$ ja yhden latauksen hinta $K$
**Periaate:** Laturin teho on $U_\text{lat} I$ (luku *Sähköteho ja vastuksen lämpeneminen*). Kun laturin jännite on vakio ja akun läpi kulkee varaus $Q$, laturi antaa energian $U_\text{lat} Q$. Akkuun varastoituu kemiallisena energiana vain lähdejännitettä vastaava osuus. Loput energiasta muuttuu resistanssien sisäenergiaksi (luku *Akut ja latauspiiri*). Mallissa akun lähdejännite on latauksen aikana keskimäärin yhtä suuri kuin nimellisjännite $36\,\text{V}$. Hinta lasketaan energiasta, jonka laturi antaa (luku *Sähköenergia kotona*).
**Kaava:** $W_\text{lat} = U_\text{lat} Q$, $\eta = \dfrac{W_\text{akku}}{W_\text{lat}}$ ja $K = aW_\text{lat}$
**Muunnokset:** $437\,\text{Wh} = 0{,}437\,\text{kWh}$ ja $15\,\text{snt/kWh} = 0{,}15\,\text{€/kWh}$
**Sijoitus:** $W_\text{lat} = 42{,}0\,\text{V} \cdot 10{,}4\,\text{Ah} = 436{,}8\,\text{Wh}$, $\eta = \dfrac{374{,}4\,\text{Wh}}{436{,}8\,\text{Wh}} = 0{,}857$ ja $K = 0{,}15\,\tfrac{\text{€}}{\text{kWh}} \cdot 0{,}4368\,\text{kWh} = 0{,}066\,\text{€}$
**Vastaus:** Hyötysuhde on $\eta \approx 86\,\%$, ja yksi täysi lataus maksaa noin $7\,\text{snt}$. Tarkkuus on kaksi merkitsevää numeroa, koska akun nimellisjännite $36\,\text{V}$ tunnetaan vain kahden numeron tarkkuudella.
**Järkevyys:** Hyötysuhde on alle $100\,\%$, koska $436{,}8\,\text{Wh} - 374{,}4\,\text{Wh} \approx 62\,\text{Wh}$ muuttuu laturin, johtojen ja akun resistanssien sisäenergiaksi. Siksi laturi ja akku lämpenevät latauksessa. Noin seitsemän senttiä noin $28\,\text{km}$:n matkasta on hyvin halpaa.

### Yleisiä virheitä
- a-kohdassa milliampeeritunteja tai ampeeritunteja pidetään energiana. Tai wattitunteja ei muuteta jouleiksi sijoittamalla.
- b-kohdassa aika lasketaan energiasta ja virrasta, jolloin yksiköt eivät täsmää eli sovi yhteen.
- c-kohdassa latausvirta lasketaan pelkästä laturin jännitteestä, $\tfrac{42{,}0\,\text{V}}{3{,}0\,\Omega} = 14\,\text{A}$. Tai napajännitteeksi annetaan $E - R_\text{s} I$, mikä koskee purkautumista.
- d-kohdassa hyötysuhteeksi saadaan yli $100\,\%$, koska energiat verrataan väärin päin. Tai hinta lasketaan akkuun varastoituneesta energiasta, vaikka se pitää laskea laturin energiasta.

### Hyväksytään myös
- d-kohdassa hyötysuhde suoraan jännitteiden suhteena $\eta = \tfrac{36\,\text{V}}{42{,}0\,\text{V}}$, kun on perusteltu, että sama varaus kulkee laturin ja akun läpi.

## fy9-tasavirta-s3

### a)
**Kysytty:** napajännite virran funktiona kuvaajana, sovitettu malli ja mallin perustelu
**Kuvaaja:** Vaaka-akselilla on $I\ (\text{A})$ ja pystyakselilla $U\ (\text{V})$. Jännitteet ovat välillä $3{,}89$–$4{,}56\,\text{V}$. Siksi pystyakseli katkaistaan, jotta pienet muutokset näkyvät. Katkaisu merkitään akseliin. Vaaka-akseli alkaa nollasta, jotta suoraa voi jatkaa pystyakselille. Pisteitä ei yhdistetä murtoviivaksi. Pisteiden lomitse eli välistä sovitetaan yksi suora.

<svg data-fig="fy9-tasavirta-s3-ui" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: paristokotelon napajännite U voltteina virran I funktiona ampeereina. Pystyakseli alkaa 3,6 voltista, ja katkaisu on merkitty akselille. Kuusi mustaa pistettä on virroilla 0,10–1,00 A, ja jännitteet ovat 4,56 voltista 3,89 volttiin. Pisteisiin on sovitettu laskeva suora. Suoraa on jatkettu katkoviivana pystyakselille, ja se leikkaa akselin noin arvossa 4,63 V. Suoraa on jatkettu myös virtaan 1,20 A asti. Suoralta on ympyröity kaksi pistettä, (0 A; 4,63 V) ja (1,20 A; 3,75 V). Niistä luetaan kulmakerroin." style="max-width:100%;font-size:30px">
  <line x1="137.5" y1="380" x2="137.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="165.5" y1="380" x2="165.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="380" x2="193" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="221" y1="380" x2="221" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248.5" y1="380" x2="248.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="380" x2="304" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="380" x2="331.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="380" x2="359" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="380" x2="387" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="380" x2="414.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="442.5" y1="380" x2="442.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="380" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="353.5" x2="470" y2="353.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="326.5" x2="470" y2="326.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="300" x2="470" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="273.5" x2="470" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="246.5" x2="470" y2="246.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="220" x2="470" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="193.5" x2="470" y2="193.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="166.5" x2="470" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="140" x2="470" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="113.5" x2="470" y2="113.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="86.5" x2="470" y2="86.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="380" x2="484" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,380 L483,386 L483,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="381" x2="110" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,34 L116,47 L104,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="380" x2="137.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="165.5" y1="380" x2="165.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193" y1="380" x2="193" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="221" y1="380" x2="221" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="193.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0{,}4$</div></foreignObject>
  <line x1="248.5" y1="380" x2="248.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="304" y1="380" x2="304" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="331.5" y1="380" x2="331.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="304" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0{,}8$</div></foreignObject>
  <line x1="359" y1="380" x2="359" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="387" y1="380" x2="387" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="414.5" y1="380" x2="414.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="442.5" y1="380" x2="442.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="415" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1{,}2$</div></foreignObject>
  <line x1="470" y1="380" x2="470" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="353.5" x2="110" y2="353.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="326.5" x2="110" y2="326.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="308.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$3{,}8$</div></foreignObject>
  <line x1="103" y1="300" x2="110" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="273.5" x2="110" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="255.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4{,}0$</div></foreignObject>
  <line x1="103" y1="246.5" x2="110" y2="246.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="220" x2="110" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="202" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4{,}2$</div></foreignObject>
  <line x1="103" y1="193.5" x2="110" y2="193.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="166.5" x2="110" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="148.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4{,}4$</div></foreignObject>
  <line x1="103" y1="140" x2="110" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="113.5" x2="110" y2="113.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="95.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4{,}6$</div></foreignObject>
  <line x1="103" y1="86.5" x2="110" y2="86.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="60" x2="110" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="42" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4{,}8$</div></foreignObject>
  <foreignObject x="502" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="100" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$U\ (\text{V})$</div></foreignObject>
  <path d="M101,366 L119,358 M101,356 L119,348" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="76" y="384" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <polyline points="137.5,126 387,300.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="110,106.5 137.5,126" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="387,300.5 442.5,339.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="137.5" cy="124" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="179" cy="158.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="221" cy="182.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="276" cy="225.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="331.5" cy="257.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="387" cy="302.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="110" cy="105.5" r="11" fill="none" stroke="#1971c2" stroke-width="2.5"/>
  <circle cx="442.5" cy="340" r="11" fill="none" stroke="#1971c2" stroke-width="2.5"/>
  <line x1="442.5" y1="340" x2="442.5" y2="380" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="340" x2="442.5" y2="340" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="126.5" y="63.5" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E \approx 4{,}63\,\text{V}$</span></div></foreignObject>
  <foreignObject x="158" y="322" width="247" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$(1{,}20\,\text{A};\ 3{,}75\,\text{V})$</span></div></foreignObject>
</svg>

**Mallivastaus:** Paristoryhmää kuvataan mallilla, jossa lähde ja sisäinen resistanssi $R_\text{s}$ ovat sarjassa. Lähteen lähdejännite on $E$. Kun ryhmästä otetaan virta $I$, napajännite pienenee sisäisen resistanssin jännitehäviön verran: $U = E - R_\text{s} I$. Jännitehäviö on verrannollinen virtaan, kun $E$ ja $R_\text{s}$ ovat vakioita. Siksi mallin kuvaaja on laskeva suora. Pisteet asettuvat hyvin suoralle. Niiden poikkeamat suorasta ovat noin $0{,}01\,\text{V}$, eli yhtä suuria kuin lukemien tarkkuus. Malli sopii siis aineistoon.

### b)
**Annettu:** sovitettu suora kuvaajassa; suoralta luetut pisteet $(0\,\text{A};\ 4{,}63\,\text{V})$ ja $(1{,}20\,\text{A};\ 3{,}75\,\text{V})$; uuden AA-pariston tyypilliset arvot $1{,}5$–$1{,}6\,\text{V}$ ja $0{,}1$–$0{,}3\,\Omega$
**Kysytty:** paristoryhmän lähdejännite $E$ ja sisäinen resistanssi $R_\text{s}$ sekä vertailu yhden pariston arvoihin
**Periaate:** Mallin $U = E - R_\text{s} I$ mukaan suora leikkaa pystyakselin kohdassa $U = E$. Syy on se, että ilman virtaa sisäisessä resistanssissa ei ole jännitehäviötä. Suoran kulmakerroin on $-R_\text{s}$ (luku *Lähdejännite ja sisäinen resistanssi*). Kulmakerroin luetaan kahdesta sovitetun suoran pisteestä, jotka ovat kaukana toisistaan. Mittauspisteitä ei käytetä (luku *Graafinen esitys ja suoran sovittaminen*). Kun paristot on kytketty sarjaan, niiden lähdejännitteet ja sisäiset resistanssit lasketaan yhteen.
**Kuvaajan lukeminen:** Suora leikkaa pystyakselin kohdassa $4{,}63\,\text{V}$. Kohdassa $I = 1{,}20\,\text{A}$ suoran arvo on $3{,}75\,\text{V}$.
**Kaava:** $E = U(0)$ ja $R_\text{s} = -\dfrac{\Delta U}{\Delta I}$; yhtä paristoa kohti $\dfrac{E}{3}$ ja $\dfrac{R_\text{s}}{3}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $E = 4{,}63\,\text{V}$ ja $R_\text{s} = -\dfrac{3{,}75\,\text{V} - 4{,}63\,\text{V}}{1{,}20\,\text{A} - 0\,\text{A}} = \dfrac{0{,}88\,\text{V}}{1{,}20\,\text{A}} = 0{,}733\,\Omega$; yhtä paristoa kohti $\dfrac{4{,}63\,\text{V}}{3} = 1{,}54\,\text{V}$ ja $\dfrac{0{,}733\,\Omega}{3} = 0{,}244\,\Omega$
**Vastaus:** Lähdejännite on $E \approx 4{,}63\,\text{V}$, ja sisäinen resistanssi on $R_\text{s} \approx 0{,}73\,\Omega$. Sisäinen resistanssi ilmoitetaan kahdella merkitsevällä numerolla, koska jännitteen muutos $0{,}88\,\text{V}$ luetaan kuvaajalta noin sadasosan tarkkuudella.
**Järkevyys:** Yhtä paristoa kohti saadaan $1{,}54\,\text{V}$ ja $0{,}24\,\Omega$. Ne ovat uuden AA-pariston tyypillisiä arvoja. Pienimmällä virralla mitattu $4{,}56\,\text{V}$ on vähän pienempi kuin lähdejännite, kuten pitää.

### c)
**Annettu:** $E \approx 4{,}63\,\text{V}$ ja $R_\text{s} \approx 0{,}733\,\Omega$ (b-kohta), suurin mitattu virta $1{,}00\,\text{A}$
**Kysytty:** oikosulkuvirta $I_\text{k}$, miksi sitä ei mitattu ja kuinka luotettava tulos on
**Periaate:** Oikosulussa ulkoisen piirin resistanssi on nolla. Siksi virtaa rajoittaa vain sisäinen resistanssi (luku *Lähdejännite ja sisäinen resistanssi*). Kuvaajassa oikosulkuvirta on kohta, jossa suora leikkaa vaaka-akselin. Siinä napajännite on nolla.
**Kaava:** $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $I_\text{k} = \dfrac{4{,}63\,\text{V}}{0{,}733\,\Omega} = 6{,}31\,\text{A}$

<svg data-fig="fy9-tasavirta-s3-ik" viewBox="0 0 600 400" role="img" aria-label="Kuvaaja: napajännite U voltteina virran I funktiona ampeereina. Akselit alkavat nollasta. Mittauspisteet ovat vasemmalla virroilla 0–1 A. Sovitettu suora jatkuu katkoviivana mittausalueen ulkopuolelle. Se leikkaa vaaka-akselin oikosulkuvirran kohdalla noin 6,3 ampeerissa. Tämä virta on yli kuusi kertaa suurempi kuin suurin mitattu virta." style="max-width:100%;font-size:30px">
  <line x1="145.5" y1="340" x2="145.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201.5" y1="340" x2="201.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="257" y1="340" x2="257" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="340" x2="313" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368.5" y1="340" x2="368.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424.5" y1="340" x2="424.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="340" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="284" x2="480" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="228" x2="480" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="172" x2="480" y2="172" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="116" x2="480" y2="116" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="340" x2="494" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,340 L493,346 L493,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="341" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145.5" y1="340" x2="145.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="133.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="201.5" y1="340" x2="201.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="189.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="257" y1="340" x2="257" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="313" y1="340" x2="313" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="368.5" y1="340" x2="368.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="356.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$5$</div></foreignObject>
  <line x1="424.5" y1="340" x2="424.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$6$</div></foreignObject>
  <line x1="480" y1="340" x2="480" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="468" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$7$</div></foreignObject>
  <line x1="83" y1="284" x2="90" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="266" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="83" y1="228" x2="90" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="210" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="83" y1="172" x2="90" y2="172" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="154" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="83" y1="116" x2="90" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="98" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="42" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$5$</div></foreignObject>
  <foreignObject x="56" y="342" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="512" y="322" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="80" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$U\ (\text{V})$</div></foreignObject>
  <polygon points="90,340 145.5,340 145.5,60 90,60" fill="#d0e6fb" fill-opacity="0.5"/>
  <polyline points="90,81 145.5,121.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="145.5,121.5 444,340" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="95.5" cy="84.5" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="104" cy="92" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="112.5" cy="97" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="123.5" cy="106" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="134.5" cy="112.5" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="145.5" cy="122" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="444" cy="340" r="7" fill="#c92a2a"/>
  <foreignObject x="380" y="255" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I_\text{k} \approx 6{,}3\,\text{A}$</span></div></foreignObject>
  <foreignObject x="154" y="260.5" width="180" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{mittausalue}$</span></div></foreignObject>
</svg>

**Vastaus:** Oikosulkuvirta olisi noin $I_\text{k} \approx 6{,}3\,\text{A}$, kaksi merkitsevää numeroa kuten sisäisessä resistanssissa. Virtaa ei mitattu, koska oikosulussa paristot kuumenisivat nopeasti ja voisivat vahingoittua. Tulos on vain arvio. Se on ekstrapolaatio eli arvio mittausalueen ulkopuolelta, yli kuusi kertaa suuremmalle virralle. Lisäksi se olettaa, että sisäinen resistanssi pysyy samana myös suurilla virroilla.
**Järkevyys:** Kun kuvaajan suoraa jatketaan, se leikkaa vaaka-akselin samassa kohdassa, noin $6{,}3\,\text{A}$. Uuden AA-pariston oikosulkuvirta on muutamia ampeereja, joten tulos on uskottava. Todellisuudessa paristojen kemialliset reaktiot eivät ehdi seurata suurta virtaa. Silloin jännite laskee enemmän kuin malli ennustaa, joten oikea virta olisi todennäköisesti pienempi.

### d)
**Annettu:** lampun resistanssi $R = 3{,}6\,\Omega$, $E \approx 4{,}63\,\text{V}$ ja $R_\text{s} \approx 0{,}733\,\Omega$ (b-kohta)
**Kysytty:** lamppuun siirtyvä teho $P$ ja sen osuus lähdetehosta $EI$
**Periaate:** Lamppu ja sisäinen resistanssi ovat sarjassa samassa silmukassa. Siksi virran määrää niiden resistanssien summa (luku *Lähdejännite ja sisäinen resistanssi*). Lampun teho saadaan sen resistanssista ja virrasta Joulen lain avulla. Lähde tuottaa sähköenergiaa teholla $EI$ (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$, $P = RI^2$ ja osuus $\dfrac{P}{EI}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $I = \dfrac{4{,}63\,\text{V}}{3{,}6\,\Omega + 0{,}733\,\Omega} = 1{,}069\,\text{A}$, $P = 3{,}6\,\Omega \cdot (1{,}069\,\text{A})^2 = 4{,}11\,\text{W}$, $EI = 4{,}63\,\text{V} \cdot 1{,}069\,\text{A} = 4{,}95\,\text{W}$ ja $\dfrac{4{,}11\,\text{W}}{4{,}95\,\text{W}} = 0{,}831$
**Vastaus:** Lamppuun siirtyy teho $P \approx 4{,}1\,\text{W}$. Se on noin $83\,\%$ lähdetehosta. Tarkkuus on kaksi merkitsevää numeroa kuten lampun resistanssissa $3{,}6\,\Omega$.
**Järkevyys:** Sisäiseen resistanssiin jää $0{,}733\,\Omega \cdot (1{,}069\,\text{A})^2 \approx 0{,}84\,\text{W}$, ja $4{,}11\,\text{W} + 0{,}84\,\text{W} = 4{,}95\,\text{W}$, kuten energian säilyminen vaatii. Osuus on myös $\tfrac{R}{R + R_\text{s}} = \tfrac{3{,}6}{4{,}33} \approx 0{,}83$. Virta $1{,}07\,\text{A}$ on vähän mittausalueen yläpuolella, joten malli pätee siihen todennäköisesti hyvin.

### Yleisiä virheitä
- a-kohdassa pisteet yhdistetään murtoviivaksi. Tai pystyakseli katkaistaan, mutta katkaisua ei merkitä.
- b-kohdassa lähdejännitteeksi annetaan pienimmän virran napajännite $4{,}56\,\text{V}$. Tai kulmakerroin lasketaan kahdesta mittauspisteestä, vaikka se pitää laskea suoralta.
- b-kohdassa sisäinen resistanssi lasketaan yhden mittauksen suhteena $\tfrac{U}{I}$. Se on kuormitusvastuksen eli ulkoisen vastuksen resistanssi.
- c-kohdassa oikosulkuvirta lasketaan napajännitteestä. Tai tulosta pidetään yhtä luotettavana kuin mitattuja arvoja.
- d-kohdassa sisäinen resistanssi unohdetaan, jolloin $I = \tfrac{4{,}63\,\text{V}}{3{,}6\,\Omega} = 1{,}29\,\text{A}$ ja $P = 5{,}95\,\text{W}$.

### Hyväksytään myös
- b-kohdassa sovitetun suoran yhtälö laskimella: $U = 4{,}625\,\text{V} - 0{,}727\,\Omega \cdot I$, joten $E \approx 4{,}63\,\text{V}$ ja $R_\text{s} \approx 0{,}73\,\Omega$.
- d-kohdassa teho napajännitteestä: $U = E - R_\text{s} I = 3{,}85\,\text{V}$ ja $P = UI \approx 4{,}1\,\text{W}$.

## fy9-tasavirta-s4

### a)
**Kysytty:** pitääkö väite 1 paikkansa, ja kuinka suuri teho muuttuu sisäenergiaksi $15\,\text{m}$:n jatkojohdossa
**Periaate:** Virta ei kulu. Sama varaus kulkee johtoa pitkin laitteeseen ja palaa takaisin toista johdinta pitkin (luku *Virtapiiri, sähkövirta ja jännite*). Johtimilla on resistanssi $R = \rho\,\tfrac{l}{A}$ (luku *Resistanssi ja Ohmin laki*). Resistanssissa sähköenergiaa muuttuu sisäenergiaksi teholla $P = RI^2$ (luku *Sähköteho ja vastuksen lämpeneminen*).
**Mallivastaus:** Väite on väärä. Johdossa ei kulu virtaa. Laitteeseen menevä virta ja laitteesta palaava virta ovat yhtä suuret. Johto lämpenee, koska sen resistanssissa sähköenergiaa muuttuu sisäenergiaksi teholla $P = RI^2$. Virta kulkee kahden johtimen kautta, joten matka on $2 \cdot 15\,\text{m} = 30\,\text{m}$, ja $R = 1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \tfrac{30\,\text{m}}{0{,}75 \cdot 10^{-6}\,\text{m}^2} = 0{,}68\,\Omega$. Kun virta on $10\,\text{A}$, teho on $0{,}68\,\Omega \cdot (10\,\text{A})^2 = 68\,\text{W}$. Se on kuin pieni lämmitin johdon sisällä. Resistanssi on verrannollinen pituuteen ja kääntäen verrannollinen poikkipinta-alaan. Siksi ohut johto lämpenee jokaista metriä kohti yhtä paljon, oli johto lyhyt tai pitkä. Teho kasvaa virran neliönä, joten suuri virta ratkaisee. Ohut johto on suurella virralla vaarallinen myös lyhyenä. Se on erityisen vaarallinen kelalle kierrettynä, koska silloin lämpö ei pääse pois. Paksumpi johto $1{,}5\,\text{mm}^2$ puolittaisi tehon $34\,\text{W}$:iin.

### b)
**Kysytty:** pitääkö väite 2 paikkansa, kun samassa $10\,\text{A}$:n ryhmässä ovat $2000\,\text{W}$:n vedenkeitin ja $850\,\text{W}$:n leivänpaahdin
**Periaate:** Kodin pistorasiat on kytketty rinnan. Siksi jokaisen laitteen yli on verkon jännite (luku *Vastusten sarja- ja rinnankytkennät*). Lämmittävän laitteen virta on $I = \tfrac{P}{U}$ (luku *Sähköenergia kotona*). Ryhmän johdossa kulkee haarojen virtojen summa (luku *Kirchhoffin lait ja potentiaali virtapiirissä*).
**Mallivastaus:** Väite on väärä. Pistorasiat ovat rinnan, joten jokaisen laitteen yli on $230\,\text{V}$. Laite ottaa oman virtansa $I = \tfrac{P}{U}$, eikä virta riipu muista laitteista. Vedenkeitin ottaa $\tfrac{2000\,\text{W}}{230\,\text{V}} = 8{,}7\,\text{A}$ ja leivänpaahdin $\tfrac{850\,\text{W}}{230\,\text{V}} = 3{,}7\,\text{A}$. Virrat ovat samat, onko toinen laite päällä tai ei. Virtalain mukaan ryhmän johdossa kulkee näiden virtojen summa $12{,}4\,\text{A}$. Se on suurempi kuin sulakkeen $10\,\text{A}$. Sulake katkaisee virran, koska liian suuri virta kuumentaisi ryhmän johtoja (teho $RI^2$). Uusi laite ei siis pienennä muiden laitteiden virtaa. Se kasvattaa ryhmän kokonaisvirtaa. Juuri siksi ryhmää ei saa kuormittaa liikaa.

### c)
**Kysytty:** pitääkö väite 3 paikkansa, ja kuinka suuri jännite on linnun jalkojen välillä
**Periaate:** Virtaa kehon läpi ajaa potentiaaliero eli jännite niiden kahden kohdan välillä, joissa keho koskettaa johdinta (luku *Kirchhoffin lait ja potentiaali virtapiirissä*). Johtimessa potentiaali laskee virran suuntaan $RI$:n verran. Lyhyen johtimen palan resistanssi on $R = \rho\,\tfrac{l}{A}$ (luku *Resistanssi ja Ohmin laki*).
**Mallivastaus:** Väite pitää paikkansa. Linnun jalkojen välinen johdon pala on $4{,}0\,\text{cm}$ pitkä. Sen resistanssi on $2{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \tfrac{0{,}040\,\text{m}}{400 \cdot 10^{-6}\,\text{m}^2} = 2{,}7 \cdot 10^{-6}\,\Omega$. Jalkojen välinen jännite on $2{,}7 \cdot 10^{-6}\,\Omega \cdot 600\,\text{A} \approx 1{,}6\,\text{mV}$. Näin pieni jännite ei aja linnun kehon läpi juuri ollenkaan virtaa. Koko lintu on kuitenkin johdon kanssa korkeassa potentiaalissa maahan verrattuna. Pylväs on maan potentiaalissa. Jos lintu koskettaa pylvästä samaan aikaan, linnun kehon yli on melkein koko johdon ja maan välinen jännite. Se on kymmeniä tai satoja kilovoltteja, ja kehon läpi kulkee vaarallinen virta. Vaarallista ei siis ole korkea potentiaali. Vaarallista on suuri potentiaaliero kehon kahden kohdan välillä.

### Yleisiä virheitä
- a-kohdassa johdon pituudeksi otetaan $15\,\text{m}$, vaikka virta kulkee kahden johtimen kautta. Tai neliömillimetrejä ei muuteta neliömetreiksi.
- a-kohdassa teho lasketaan verkon jännitteellä $\tfrac{(230\,\text{V})^2}{0{,}68\,\Omega}$, vaikka johdon yli on vain $RI \approx 6{,}8\,\text{V}$.
- b-kohdassa laitteet oletetaan sarjaan. Silloin uusi laite pienentäisi virtaa.
- c-kohdassa sanotaan, että linnun jalat eristävät eli eivät johda sähköä, tai että johdon jännite on pieni.

## fy9-tasavirta-s5

### a)
**Annettu:** mittaus 1: $U = 0{,}51\,\text{V}$ alueella $20\,\text{V}$ (resoluutio $0{,}01\,\text{V}$, $\pm(0{,}5\,\% + 2\ \text{numeroa})$) ja $I = 5{,}3\,\text{mA}$ alueella $200\,\text{mA}$ (resoluutio $0{,}1\,\text{mA}$, $\pm(1{,}0\,\% + 2\ \text{numeroa})$)
**Kysytty:** mittauksen 1 resistanssi $R$ ja sen virheraja $\Delta R$
**Periaate:** Resistanssi on jännitteen ja virran suhde (luku *Resistanssi ja Ohmin laki*). Kummankin mittarin virheraja lasketaan näin: prosenttiosuus lukemasta plus numeroiden määrä kertaa resoluutio (luku *Mittaukset virtapiirissä*). Resistanssin suurin mahdollinen arvo saadaan suurimmasta jännitteestä ja pienimmästä virrasta. Pienin arvo saadaan päinvastoin (luku *Mittaaminen ja mittauksen luotettavuus*).
**Kaava:** $R = \dfrac{U}{I}$, $\Delta x = p \cdot x + n \cdot r$, $R_\text{min} = \dfrac{U - \Delta U}{I + \Delta I}$ ja $R_\text{max} = \dfrac{U + \Delta U}{I - \Delta I}$
**Muunnokset:** $5{,}3\,\text{mA} = 5{,}3 \cdot 0{,}001\,\text{A} = 0{,}0053\,\text{A}$ ja $0{,}1\,\text{mA} = 0{,}0001\,\text{A}$
**Sijoitus:** $\Delta U = 0{,}005 \cdot 0{,}51\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0226\,\text{V}$, $\Delta I = 0{,}010 \cdot 5{,}3\,\text{mA} + 2 \cdot 0{,}1\,\text{mA} = 0{,}253\,\text{mA}$, $R = \dfrac{0{,}51\,\text{V}}{0{,}0053\,\text{A}} = 96{,}2\,\Omega$, $R_\text{min} = \dfrac{0{,}4874\,\text{V}}{0{,}005553\,\text{A}} = 87{,}8\,\Omega$ ja $R_\text{max} = \dfrac{0{,}5326\,\text{V}}{0{,}005047\,\text{A}} = 105{,}5\,\Omega$
**Vastaus:** Mittauksen 1 resistanssi on $R = (96 \pm 9)\,\Omega$. Mittarien virherajojen mukaan oikea arvo on siis todennäköisesti välillä noin $88$–$106\,\Omega$. Virheraja ilmoitetaan yhdellä merkitsevällä numerolla ja tulos samalla tarkkuudella.
**Järkevyys:** Suhteelliset virherajat ovat $\tfrac{0{,}0226}{0{,}51} \approx 4{,}4\,\%$ ja $\tfrac{0{,}253}{5{,}3} \approx 4{,}8\,\%$. Osamäärän suhteellinen virheraja on niiden summa, noin $9{,}2\,\%$ eli $9\,\Omega$. Tulos on sama. Kun lukema on pieni, numeroiden osuus $2 \cdot r$ on suuri, joten virheraja on suuri.

### b)
**Kysytty:** onko ryhmän johtopäätös perusteltu
**Periaate:** Kahden tuloksen ero on todellinen vain, jos ero on suurempi kuin tulosten virherajat (luku *Mittaaminen ja mittauksen luotettavuus*). Mitä pienempi lukema on alueeseen verrattuna, sitä suurempi osa virherajasta tulee numeroista (luku *Mittaukset virtapiirissä*). Metallin ja hiilikalvon resistanssi muuttuu lähinnä lämpötilan mukana (luku *Resistanssi ja Ohmin laki*).
**Mallivastaus:** Johtopäätös ei ole perusteltu. Kun virherajat lasketaan samalla tavalla, mittauksen 2 resistanssi on $(100 \pm 4)\,\Omega$ ja mittauksen 3 resistanssi $(102 \pm 3)\,\Omega$. Mittauksen 1 tulos on $(96 \pm 9)\,\Omega$. Kaikkiin kolmeen väliin kuuluu arvo $100\,\Omega$. Siksi resistanssit eivät eroa toisistaan mittaustarkkuuden rajoissa. Suurin poikkeama on mittauksessa 1. Siinä lukemat $0{,}51\,\text{V}$ ja $5{,}3\,\text{mA}$ ovat pieniä alueisiin verrattuna, joten numeroiden osuus on suurin osa virherajasta. Lämpeneminen voisi muuttaa resistanssia. Vastuksen teho on kuitenkin suurimmillaankin vain $3{,}02\,\text{V} \cdot 29{,}6\,\text{mA} \approx 0{,}09\,\text{W}$, joten vastus ei juuri lämpene. Aineisto sopii siis vakioresistanssiin noin $100\,\Omega$. Kolmesta epätarkasta pisteestä ei voi päätellä, että resistanssi riippuisi jännitteestä.

### c)
**Kysytty:** miten mittausta parannetaan, jotta Ohmin lain voimassaolo voidaan todeta luotettavasti
**Periaate:** Riippuvuus todetaan luotettavimmin kuvaajasta, jossa monen pisteen läpi on sovitettu suora (luku *Graafinen esitys ja suoran sovittaminen*). Mittarin virheraja on pienin, kun käytetään pienintä aluetta, jolle lukema mahtuu (luku *Mittaukset virtapiirissä*). Ohmin laki koskee vakiolämpötilaa, joten lämpötilan pitää pysyä samana (luku *Resistanssi ja Ohmin laki*).
**Mallivastaus:** Mitataan vähintään kahdeksan pistettä laajalla jännitealueella, esimerkiksi $0{,}5$–$10\,\text{V}$. Piirretään $(I, U)$-kuvaaja. Jos vastus noudattaa Ohmin lakia, pisteet ovat origon kautta kulkevalla suoralla, jonka kulmakerroin on $R$. Poikkeama suorasta näkyy kuvaajasta paremmin kuin kolmesta suhteesta. Jokainen lukema luetaan pienimmältä alueelta, jolle se mahtuu. Esimerkiksi $0{,}510\,\text{V}$ alueella $2\,\text{V}$ antaa virherajan $0{,}005 \cdot 0{,}510\,\text{V} + 2 \cdot 0{,}001\,\text{V} \approx 0{,}005\,\text{V}$ eli noin $0{,}9\,\%$. Lämpötila pidetään vakiona: vastuksen teho pidetään pienenä, ja lukemat otetaan nopeasti. Jännitettä sekä kasvatetaan että pienennetään. Jos lämpeneminen vaikuttaisi, se näkyisi eroina. Virtamittari pidetään sarjassa ja jännitemittari vastuksen rinnalla. Lisäksi arvioidaan mittarien vaikutus: jännitemittarin resistanssi on megaohmien luokkaa eli paljon suurempi kuin $100\,\Omega$. Siksi sen kautta kulkee hyvin pieni virta. Tulos ilmoitetaan virherajojen kanssa.

### Yleisiä virheitä
- a-kohdassa virheraja lasketaan pelkästä prosenttiosuudesta. Silloin numeroiden osuus $n \cdot r$ unohtuu, ja virheraja on liian pieni.
- a-kohdassa milliampeereja ei muuteta ampeereiksi. Silloin resistanssi on tuhat kertaa väärin.
- b-kohdassa johtopäätös hyväksytään, koska luvut kasvavat. Eroa ei verrata virherajoihin.
- c-kohdassa ehdotetaan vain, että mittaukset toistetaan samalla tavalla. Se ei pienennä mittarin virherajaa.

### Hyväksytään myös
- a-kohdassa virheraja suhteellisten virherajojen summana $\tfrac{\Delta R}{R} = \tfrac{\Delta U}{U} + \tfrac{\Delta I}{I} \approx 9\,\%$.

## fy9-tasavirta-s6

### a)
**Annettu:** veden tilavuus $300\,\text{l}$, joten massa $m = 300\,\text{kg}$; lämpötilat $15\,{}^\circ\text{C}$ ja $70\,{}^\circ\text{C}$; teho $P = 3{,}0\,\text{kW}$; $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Kysytty:** lämmitysaika $t$
**Periaate:** Vastuksessa sähköenergia muuttuu sisäenergiaksi (luku *Sähköteho ja vastuksen lämpeneminen*). Vastuksesta energia siirtyy lämpönä veteen. Vastuslämmittimen hyötysuhde on käytännössä $100\,\%$. Kun lämpöhäviöitä ei oteta huomioon, kaikki sähköenergia lämmittää vettä (luku *Aineen lämpeneminen ja jäähtyminen*). Teho on vakio, joten energia on teho kertaa aika.
**Kaava:** $Pt = cm\Delta T$, joten $t = \dfrac{cm\Delta T}{P}$
**Muunnokset:** $3{,}0\,\text{kW} = 3{,}0 \cdot 1000\,\text{W} = 3000\,\text{W}$; lämpötilan muutos $70\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 55\,{}^\circ\text{C} = 55\,\text{K}$; lopuksi $1\,\text{h} = 3600\,\text{s}$
**Sijoitus:** $Q = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 300\,\text{kg} \cdot 55\,\text{K} = 6{,}914 \cdot 10^{7}\,\text{J}$ ja $t = \dfrac{6{,}914 \cdot 10^{7}\,\text{J}}{3000\,\text{W}} = 23\,045\,\text{s} = 6{,}40\,\text{h}$
**Vastaus:** Lämmitys kestää noin $t \approx 6{,}4\,\text{h}$. Tarkkuus on kaksi merkitsevää numeroa kuten tehossa $3{,}0\,\text{kW}$.
**Järkevyys:** Vesi saa energiaa $\tfrac{6{,}914 \cdot 10^{7}\,\text{J}}{3{,}6 \cdot 10^{6}\,\text{J/kWh}} = 19{,}2\,\text{kWh}$, ja $3{,}0\,\text{kW} \cdot 6{,}4\,\text{h} = 19{,}2\,\text{kWh}$. Lämmitys mahtuu yön tunteihin. Se maksaa noin $19{,}2\,\text{kWh} \cdot 0{,}14\,\tfrac{\text{€}}{\text{kWh}} \approx 2{,}7\,\text{€}$. Lämpöhäviöt pidentävät aikaa vähän.

### b)
**Annettu:** lämpöhäviö $E = 1{,}6\,\text{kWh}$ vuorokaudessa, hinta $a = 14\,\text{snt/kWh}$
**Kysytty:** häviöiden keskimääräinen teho $P$ ja vuoden kustannus $K$
**Periaate:** Keskimääräinen teho on energia jaettuna ajalla (luku *Sähköteho ja vastuksen lämpeneminen*). Varaajan termostaatti korvaa häviöt sähköllä. Termostaatti on laite, joka pitää lämpötilan samana. Siksi häviöenergia maksaa saman verran kuin sähkö (luku *Sähköenergia kotona*).
**Kaava:** $P = \dfrac{E}{t}$ ja $K = a \cdot 365E$
**Muunnokset:** $1{,}6\,\text{kWh} = 1600\,\text{Wh}$, $1\,\text{vrk} = 24\,\text{h}$ ja $14\,\text{snt/kWh} = 0{,}14\,\text{€/kWh}$
**Sijoitus:** $P = \dfrac{1600\,\text{Wh}}{24\,\text{h}} = 66{,}7\,\text{W}$, vuodessa $365 \cdot 1{,}6\,\text{kWh} = 584\,\text{kWh}$ ja $K = 0{,}14\,\tfrac{\text{€}}{\text{kWh}} \cdot 584\,\text{kWh} = 81{,}8\,\text{€}$
**Vastaus:** Häviöiden keskimääräinen teho on $P \approx 67\,\text{W}$, ja häviöt maksavat noin $82\,\text{€}$ vuodessa. Tarkkuus on kaksi merkitsevää numeroa kuten häviössä $1{,}6\,\text{kWh}$ ja hinnassa $14\,\text{snt/kWh}$.
**Järkevyys:** Häviöteho on vain $2\,\%$ vastuksen tehosta. Häviö jatkuu kuitenkin koko ajan, yöt ja päivät. Siksi vuodessa häviöenergiaa kertyy yhtä paljon kuin kuukauden lämpimään veteen tarvitaan. Talvella häviölämpö lämmittää taloa, joten se ei mene kokonaan hukkaan.

### c)
**Annettu:** teho $P = 3{,}0\,\text{kW}$ jännitteellä $U = 230\,\text{V}$, uusi jännite $U' = 220\,\text{V}$, resistanssi oletetaan samaksi
**Kysytty:** vastuksen teho $P'$ jännitteellä $220\,\text{V}$
**Periaate:** Laitteeseen merkitty teho on teho nimellisjännitteellä. Siitä saadaan vastuksen resistanssi. Kun resistanssi pysyy samana, vastuksen teho on verrannollinen jännitteen neliöön (luku *Sähköteho ja vastuksen lämpeneminen*).
**Kaava:** $R = \dfrac{U^2}{P}$ ja $P' = \dfrac{U'^2}{R} = P\left(\dfrac{U'}{U}\right)^2$
**Muunnokset:** $3{,}0\,\text{kW} = 3000\,\text{W}$ ja lopuksi $1\,\text{kW} = 1000\,\text{W}$
**Sijoitus:** $R = \dfrac{(230\,\text{V})^2}{3000\,\text{W}} = 17{,}63\,\Omega$ ja $P' = \dfrac{(220\,\text{V})^2}{17{,}63\,\Omega} = 2745\,\text{W} = 2{,}74\,\text{kW}$
**Vastaus:** Teho on noin $P' \approx 2{,}7\,\text{kW}$. Tarkkuus on kaksi merkitsevää numeroa kuten tehossa $3{,}0\,\text{kW}$.
**Järkevyys:** Jännite pienenee $4{,}3\,\%$, ja teho pienenee noin kaksi kertaa niin paljon, $8{,}5\,\%$. Näin neliöriippuvuus antaa. Lämmitys kestäisi noin $\tfrac{19{,}2\,\text{kWh}}{2{,}74\,\text{kW}} \approx 7{,}0\,\text{h}$, mutta energiaa kuluu yhtä paljon.

### d)
**Annettu:** suihkun kesto $10\,\text{min}$, vesivirta $8{,}0\,\text{l/min}$, suihkuveden lämpötila $40\,{}^\circ\text{C}$, kylmän veden lämpötila $15\,{}^\circ\text{C}$, $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Kysytty:** sähköenergia $E$, jota suihkun lämmin vesi vaatii
**Periaate:** Suihkuvesi on lämmitetty $15\,{}^\circ\text{C}$:sta $40\,{}^\circ\text{C}$:een. Siksi vesi on saanut energiaa $cm\Delta T$ (luku *Aineen lämpeneminen ja jäähtyminen*). Sama energia on tullut varaajan vastuksesta sähköenergiana, koska vastuksen hyötysuhde on käytännössä $100\,\%$. Ei ole väliä, sekoitetaanko $70\,{}^\circ\text{C}$:n vettä kylmään veteen. Lopputulos on sama määrä $40\,{}^\circ\text{C}$:n vettä.
**Kaava:** $E = cm\Delta T$
**Muunnokset:** $m = 10 \cdot 8{,}0\,\text{kg} = 80\,\text{kg}$, $\Delta T = 40\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 25\,\text{K}$ ja lopuksi $1\,\text{kWh} = 3{,}6 \cdot 10^{6}\,\text{J}$
**Sijoitus:** $E = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 80\,\text{kg} \cdot 25\,\text{K} = 8{,}38 \cdot 10^{6}\,\text{J} = \dfrac{8{,}38 \cdot 10^{6}\,\text{J}}{3{,}6 \cdot 10^{6}\,\text{J/kWh}} = 2{,}33\,\text{kWh}$
**Vastaus:** Suihku vastaa noin $E \approx 2{,}3\,\text{kWh}$ sähköenergiaa. Tarkkuus on kaksi merkitsevää numeroa kuten vesivirrassa $8{,}0\,\text{l/min}$.
**Järkevyys:** Suihku maksaa noin $2{,}33\,\text{kWh} \cdot 0{,}14\,\tfrac{\text{€}}{\text{kWh}} \approx 33\,\text{snt}$. Täysi varaaja ($19{,}2\,\text{kWh}$) riittää noin $\tfrac{19{,}2}{2{,}33} \approx 8$ tällaiseen suihkuun. Samaan tulokseen päästään toisella tavalla: suihkuveteen tarvitaan noin $36\,\text{l}$ vettä, jonka lämpötila on $70\,{}^\circ\text{C}$.

### Yleisiä virheitä
- a-kohdassa teho jätetään kilowateiksi ja energia jouleiksi. Silloin aika on tuhat kertaa väärin. Tai lämpötilan muutokseksi otetaan $70\,{}^\circ\text{C}$.
- b-kohdassa häviöteho lasketaan niin, että $1{,}6\,\text{kWh}$ jaetaan vuorokauden sekunneilla, ja yksiköt jäävät sekaisin.
- c-kohdassa teho oletetaan suoraan verrannolliseksi jännitteeseen. Silloin saadaan $2{,}87\,\text{kW}$.
- d-kohdassa lämpötilan muutokseksi otetaan $70\,{}^\circ\text{C} - 40\,{}^\circ\text{C}$. Tai litroja ei muuteta kilogrammoiksi.

### Hyväksytään myös
- a-kohdassa energia kilowattitunteina: $19{,}2\,\text{kWh} : 3{,}0\,\text{kW} = 6{,}4\,\text{h}$.
