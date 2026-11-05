## fy9-magnetismi-valo-s1

### a)
**Annettu:** kierrokset $N = 60$, pinta-ala $A = 0{,}060\,\text{m}^2$, magneettivuon tiheys $B = 0{,}50\,\text{T}$, pyörimistaajuus $f = 50\,\text{Hz}$
**Kysytty:** jännitteen huippuarvo $e_0$ ja tehollinen arvo $U$
**Periaate:** Käämi pyörii tasaisesti homogeenisessa kentässä. Silloin käämin läpi kulkeva vuo vaihtelee jaksollisesti eli samalla tavalla yhä uudelleen. Induktiolain mukaan käämiin syntyy sinimuotoinen jännite. Jännite on huippuarvossaan, kun käämin taso on kentän suuntainen. Silloin vuo muuttuu nopeimmin (luvut *Sähkömagneettinen induktio* ja *Generaattori ja vaihtovirta*). Tehollinen arvo on se tasajännite, joka antaisi vastukseen saman keskimääräisen tehon. Sinimuotoisella jännitteellä tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.
**Kaava:** $e_0 = NBA \cdot 2\pi f$ ja $U = \dfrac{e_0}{\sqrt{2}}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $e_0 = 60 \cdot 0{,}50\,\text{T} \cdot 0{,}060\,\text{m}^2 \cdot 2\pi \cdot 50\,\tfrac{1}{\text{s}} = 565{,}5\,\text{V}$ ja $U = \dfrac{565{,}5\,\text{V}}{\sqrt{2}} = 399{,}9\,\text{V}$
**Vastaus:** Huippuarvo on $e_0 \approx 570\,\text{V}$ ja tehollinen arvo $U \approx 400\,\text{V}$. Vastauksissa on kaksi merkitsevää numeroa, kuten magneettivuon tiheydessä $0{,}50\,\text{T}$ ja pinta-alassa $0{,}060\,\text{m}^2$.
**Järkevyys:** Yksiköt sopivat: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. Tehollinen arvo on pienempi kuin huippuarvo, kuten pitää. Lisäksi $400\,\text{V}$ on tavallinen teollisuuden jännite.

### b)
**Annettu:** generaattorin tehollinen jännite $U_1 = 400\,\text{V}$, linjan jännite $U_2 = 20{,}0\,\text{kV}$, teho $P = 150\,\text{kW}$; muuntaja on ideaalinen
**Kysytty:** kierrosten suhde $N_2 : N_1$ sekä virrat $I_1$ ja $I_2$
**Periaate:** Ideaalisessa muuntajassa jännitteiden suhde on sama kuin kierrosten lukumäärien suhde. Teho säilyy: $U_1 I_1 = U_2 I_2$ (luku *Muuntaja ja sähköenergian siirto*). Kun jännite kasvaa, virta pienenee samassa suhteessa. Jännitteet ja virrat ovat tehollisia arvoja, joten $P = UI$.
**Kaava:** $\dfrac{N_2}{N_1} = \dfrac{U_2}{U_1}$, $I_1 = \dfrac{P}{U_1}$ ja $I_2 = \dfrac{P}{U_2}$
**Muunnokset:** $20{,}0\,\text{kV} = 20{,}0 \cdot 1000\,\text{V} = 20\,000\,\text{V}$ ja $150\,\text{kW} = 150 \cdot 1000\,\text{W} = 150\,000\,\text{W}$
**Sijoitus:** $\dfrac{N_2}{N_1} = \dfrac{20\,000\,\text{V}}{400\,\text{V}} = 50$, $I_1 = \dfrac{150\,000\,\text{W}}{400\,\text{V}} = 375\,\text{A}$ ja $I_2 = \dfrac{150\,000\,\text{W}}{20\,000\,\text{V}} = 7{,}50\,\text{A}$
**Vastaus:** Toisiokäämissä on $50$ kertaa niin monta kierrosta kuin ensiökäämissä. Generaattorin puolella virta on $I_1 \approx 375\,\text{A}$ ja linjassa $I_2 \approx 7{,}50\,\text{A}$. Vastauksissa on kolme merkitsevää numeroa, kuten jännitteessä $20{,}0\,\text{kV}$ ja tehossa $150\,\text{kW}$.
**Järkevyys:** Virtojen suhde on $375 : 7{,}50 = 50$. Se on sama kuin kierrosten suhde. Lisäksi $U_2 I_2 = 20\,000\,\text{V} \cdot 7{,}50\,\text{A} = 150\,\text{kW}$, eli teho on sama kuin ensiössä.

### c)
**Annettu:** linjan virta $I_2 = 7{,}50\,\text{A}$ (b-kohta), resistanssi $R = 6{,}0\,\Omega$, teho $P = 150\,\text{kW}$; vertailuksi jännite $400\,\text{V}$
**Kysytty:** lämmöksi muuttuvan tehon osuus $\tfrac{P_\text{h}}{P}$ ja mitä tapahtuisi jännitteellä $400\,\text{V}$
**Periaate:** Linjan resistanssissa sähköenergiaa muuttuu sisäenergiaksi teholla $RI^2$. Siirtojännite $20\,\text{kV}$ ei ole linjan resistanssin yli. Siksi häviö lasketaan virrasta. Virta saadaan siirrettävästä tehosta (luku *Muuntaja ja sähköenergian siirto*).
**Kaava:** $I = \dfrac{P}{U}$ ja $P_\text{h} = RI^2$, osuus $\dfrac{P_\text{h}}{P}$
**Muunnokset:** Lopuksi osuus muutetaan prosenteiksi: kerrotaan luvulla $100\,\%$.
**Sijoitus:** $P_\text{h} = 6{,}0\,\Omega \cdot (7{,}50\,\text{A})^2 = 337{,}5\,\text{W}$, joten $\dfrac{P_\text{h}}{P} = \dfrac{337{,}5\,\text{W}}{150\,000\,\text{W}} = 0{,}00225 = 0{,}225\,\%$. Jännitteellä $400\,\text{V}$: $I = 375\,\text{A}$ ja $RI^2 = 6{,}0\,\Omega \cdot (375\,\text{A})^2 = 843\,750\,\text{W} \approx 844\,\text{kW}$
**Vastaus:** Linjassa muuttuu lämmöksi noin $0{,}23\,\%$ tehosta. Vastauksessa on kaksi merkitsevää numeroa, kuten resistanssissa $6{,}0\,\Omega$. Jännitteellä $400\,\text{V}$ lauseke $RI^2$ antaisi $844\,\text{kW}$. Se on yli viisi kertaa niin paljon kuin siirrettävä teho. Siirto ei siis onnistuisi lainkaan. Jo linjan jännitehäviö $RI = 6{,}0\,\Omega \cdot 375\,\text{A} = 2250\,\text{V}$ olisi suurempi kuin koko jännite.
**Järkevyys:** Häviö on verrannollinen virran neliöön. Virta on kääntäen verrannollinen jännitteeseen. Kun jännite on $50$-kertainen, häviö pienenee kertoimella $50^2 = 2500$: $844\,\text{kW} : 2500 \approx 340\,\text{W}$. Tulos on sama.

### d)
**Kysytty:** toimiiko muuntaja tasajännitteellä
**Periaate:** Muuntajan toisiojännite syntyy induktiolla. Ensiövirta synnyttää rautasydämeen magneettivuon. Vain vuon muutos indusoi eli synnyttää toisiokäämiin jännitteen (luvut *Sähkömagneettinen induktio* ja *Muuntaja ja sähköenergian siirto*).
**Mallivastaus:** Ehdotus ei toimi. Tasavirta synnyttää rautasydämeen vakiovuon eli vuon, joka ei muutu. Muuttumaton vuo ei indusoi toisiokäämiin jännitettä. Vuo muuttuu vain sillä hetkellä, kun virta kytketään. Silloin toisioon syntyy lyhyt jännitepiikki. Siksi aurinkopaneelien tasajännite muutetaan ensin vaihtojännitteeksi vaihtosuuntaajalla. Vasta sen jälkeen muuntaja voi nostaa sen linjan jännitteeksi. Lisäksi tasavirralla ensiökäämin virtaa rajoittaa vain käämin pieni resistanssi. Siksi käämi voisi ylikuumentua.

### Yleisiä virheitä
- a-kohdassa annetaan huippuarvo tehollisena arvona, tai jaetaan väärään suuntaan, $e_0 \cdot \sqrt{2} \approx 800\,\text{V}$.
- a-kohdassa unohdetaan kerroin $2\pi$. Silloin tulos on $e_0 = 90\,\text{V}$.
- b-kohdassa virrat käännetään väärin päin. Oikein on näin: suuremman jännitteen puolella virta on pienempi.
- c-kohdassa häviö lasketaan lausekkeesta $\tfrac{U^2}{R} = \tfrac{(20\,000\,\text{V})^2}{6{,}0\,\Omega} \approx 67\,\text{MW}$. Tämä on väärin, koska siirtojännite ei ole linjan resistanssin yli.

### Hyväksytään myös
- c-kohdassa vertailu suhteena: $\tfrac{P_\text{h,400}}{P_\text{h,20k}} = \left(\tfrac{20\,000}{400}\right)^2 = 2500$, kun todetaan, että siirto $400\,\text{V}$:n jännitteellä on mahdoton.

## fy9-magnetismi-valo-s2

### a)
**Annettu:** ytimen taitekerroin $n_1 = 1{,}470$, kuoren taitekerroin $n_2 = 1{,}455$
**Kysytty:** pienin tulokulma $\alpha_\text{r}$, jolla valo pysyy ytimessä, ja suurin kulma säteen ja kuidun akselin välillä
**Periaate:** Valo pysyy ytimessä, jos se kokonaisheijastuu ytimen ja kuoren rajapinnasta. Kokonaisheijastuminen tarkoittaa, että kaikki valo heijastuu takaisin. Se on mahdollista, koska valo tulee aineesta, jonka taitekerroin on suurempi, aineeseen, jonka taitekerroin on pienempi. Kokonaisheijastuminen tapahtuu, kun tulokulma on suurempi kuin rajakulma (luku *Kokonaisheijastuminen ja valokuitu*). Tulokulma mitataan rajapinnan normaalista. Normaali on kohtisuorassa kuidun akselia vastaan. Siksi säteen ja akselin välinen kulma on $90^\circ - \alpha$.
**Kaava:** $n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ$, joten $\sin\alpha_\text{r} = \dfrac{n_2}{n_1}$, ja akselin suhteen $\beta_\text{max} = 90^\circ - \alpha_\text{r}$
**Muunnokset:** Taitekertoimilla ei ole yksikköä, joten muunnoksia ei tarvita.
**Sijoitus:** $\sin\alpha_\text{r} = \dfrac{1{,}455}{1{,}470} = 0{,}9898$, joten $\alpha_\text{r} = 81{,}81^\circ$ ja $\beta_\text{max} = 90^\circ - 81{,}81^\circ = 8{,}19^\circ$
**Vastaus:** Tulokulman on oltava vähintään $81{,}8^\circ$. Säde saa siis olla enintään $8{,}2^\circ$:n kulmassa kuidun akseliin nähden. Taitekertoimien ero $0{,}015$ tunnetaan vain kahden numeron tarkkuudella. Jo $0{,}001$:n muutos erossa siirtää rajakulmaa noin $0{,}3^\circ$. Rehellinen tarkkuus on siis noin $82^\circ$ ja $8^\circ$. Kymmenesosa ilmoitetaan vain vertailua varten.
**Järkevyys:** Taitekertoimet ovat lähes yhtä suuret. Siksi rajakulma on lähellä $90^\circ$:ta: vain säteet, jotka kulkevat lähes akselin suuntaisesti, pysyvät ytimessä. Lasin ja ilman välillä rajakulma olisi noin $43^\circ$.

### b)
**Annettu:** kuidun pituus $s = 14{,}0\,\text{km}$, ytimen taitekerroin $n_1 = 1{,}470$, $c = 3{,}00 \cdot 10^8\,\text{m/s}$, $\sin\alpha_\text{r} = 0{,}9898$ (a-kohta)
**Kysytty:** akselin suuntaisen pulssin kulkuaika $t$ ja jyrkimmän säteen lisäaika $\Delta t$
**Periaate:** Aineessa valo etenee nopeudella $v = \tfrac{c}{n}$ (luku *Valon heijastuminen ja taittuminen*). Akselin suuntainen säde kulkee kuidun pituuden. Jyrkin säde, joka vielä pysyy ytimessä, etenee kulmassa $90^\circ - \alpha_\text{r}$ akseliin nähden. Sen kulkema matka on kuidun pituus jaettuna tämän kulman kosinilla eli $\tfrac{s}{\sin\alpha_\text{r}}$ (luku *Kokonaisheijastuminen ja valokuitu*). Molemmat säteet etenevät ytimessä samalla nopeudella.
**Kaava:** $t = \dfrac{n_1 s}{c}$, jyrkimmälle säteelle $t' = \dfrac{t}{\sin\alpha_\text{r}}$ ja $\Delta t = t' - t$
**Muunnokset:** $14{,}0\,\text{km} = 14{,}0 \cdot 1000\,\text{m} = 14\,000\,\text{m}$ ja lopuksi $1\,\text{s} = 10^6\,\mu\text{s}$
**Sijoitus:** $t = \dfrac{1{,}470 \cdot 14\,000\,\text{m}}{3{,}00 \cdot 10^8\,\text{m/s}} = 6{,}860 \cdot 10^{-5}\,\text{s} = 68{,}60\,\mu\text{s}$, $t' = \dfrac{68{,}60\,\mu\text{s}}{0{,}9898} = 69{,}31\,\mu\text{s}$ ja $\Delta t = 69{,}31\,\mu\text{s} - 68{,}60\,\mu\text{s} = 0{,}71\,\mu\text{s}$
**Vastaus:** Akselin suuntainen pulssi kulkee matkan ajassa $t \approx 68{,}6\,\mu\text{s}$. Vastauksessa on kolme merkitsevää numeroa, kuten pituudessa $14{,}0\,\text{km}$. Jyrkimmin etenevä pulssi tulee perille noin $0{,}7\,\mu\text{s}$ myöhemmin. Tämä erotus tunnetaan vain yhden tai kahden numeron tarkkuudella.
**Järkevyys:** Valo etenee kuidussa nopeudella $\tfrac{3{,}00 \cdot 10^8\,\text{m/s}}{1{,}470} \approx 2{,}04 \cdot 10^8\,\text{m/s}$. Se on noin kaksi kolmasosaa valon nopeudesta tyhjiössä. Ero on noin $1\,\%$. Se vastaa matkojen suhdetta $\tfrac{1}{0{,}9898} \approx 1{,}010$. Jos pulssit lähtisivät tiheämmin kuin noin mikrosekunnin välein, ne voisivat sekoittua.

### c)
**Annettu:** vaimennuskerroin $a = 0{,}22\,\text{dB/km}$, pituus $L = 14{,}0\,\text{km}$, neljä jatkosta, joista kukin vaimentaa $0{,}10\,\text{dB}$, lähetysteho $P_0 = 2{,}0\,\text{mW}$
**Kysytty:** vastaanotettu teho $P$
**Periaate:** Kuidun lasi vaimentaa eli heikentää valoa samassa suhteessa joka kilometrillä. Vaimennus ilmoitetaan desibeleinä. Peräkkäisten osien ja jatkosten vaimennukset desibeleinä lasketaan yhteen (luku *Soveltava luku: langaton lataus, induktioliesi ja kuituyhteys*).
**Kaava:** $A = aL + 4 \cdot 0{,}10\,\text{dB}$ ja $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, joten $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$
**Muunnokset:** Pituus on jo kilometreinä ja teho milliwatteina, joten muunnoksia ei tarvita.
**Sijoitus:** $A = 0{,}22\,\tfrac{\text{dB}}{\text{km}} \cdot 14{,}0\,\text{km} + 0{,}40\,\text{dB} = 3{,}08\,\text{dB} + 0{,}40\,\text{dB} = 3{,}48\,\text{dB}$, joten $P = 2{,}0\,\text{mW} \cdot 10^{-0{,}348} = 2{,}0\,\text{mW} \cdot 0{,}4487 = 0{,}897\,\text{mW}$
**Vastaus:** Vastaanottimeen saapuu noin $0{,}90\,\text{mW}$. Vastauksessa on kaksi merkitsevää numeroa, kuten lähetystehossa $2{,}0\,\text{mW}$ ja vaimennuskertoimessa $0{,}22\,\text{dB/km}$.
**Järkevyys:** $3\,\text{dB}$ vastaa suunnilleen sitä, että teho puolittuu. Siksi $3{,}5\,\text{dB}$ jättää vähän alle puolet, $45\,\%$. Tulos on uskottava, koska tietoliikennekuidussa valo kulkee kymmeniä kilometrejä ilman vahvistusta.

### d)
**Kysytty:** miksi loivasti kaartuva kuitu johtaa valoa mutta jyrkkä mutka päästää valon ulos
**Periaate:** Valo pysyy ytimessä, kun tulokulma ytimen ja kuoren rajapinnassa on suurempi kuin rajakulma. Tässä kuidussa tulokulman on oltava vähintään $81{,}8^\circ$ (luku *Kokonaisheijastuminen ja valokuitu*).
**Mallivastaus:** Loivassa kaaressa rajapinnan suunta muuttuu säteen matkalla vain vähän. Siksi säde osuu rajapintaan edelleen lähes sen suuntaisesti, ja tulokulma pysyy suurempana kuin rajakulma. Valo kokonaisheijastuu ja seuraa kuitua. Jyrkässä mutkassa ulkokaaren rajapinta kääntyy säteen eteen. Siksi säde osuu rajapintaan jyrkemmin. Tulokulma pienenee alle $81{,}8^\circ$:n, valo taittuu kuoreen ja vuotaa ulos. Rajakulma on lähellä $90^\circ$:ta. Siksi jo melko pieni muutos tulokulmassa riittää. Tämän vuoksi kuitukaapelille ilmoitetaan pienin sallittu taivutussäde.

### Yleisiä virheitä
- a-kohdassa taitekertoimet käännetään väärin päin, $\sin\alpha_\text{r} = \tfrac{n_1}{n_2} > 1$, tai kulma akselin suhteen annetaan tulokulmana.
- b-kohdassa käytetään valon nopeutta tyhjiössä. Silloin tulos on $t \approx 46{,}7\,\mu\text{s}$.
- c-kohdassa vaimennus jaetaan kymmenellä ja kerrotaan tehoon, tai jatkosten vaimennus unohdetaan. Silloin tulos on $P \approx 0{,}98\,\text{mW}$.

## fy9-magnetismi-valo-s3

### a)
**Kysytty:** kuvaaja, jossa magneettivuon tiheys on etäisyyden funktiona, ja onko magneettivuon tiheys kääntäen verrannollinen etäisyyteen
**Kuvaaja:** Vaaka-akselilla on $r\ (\text{cm})$ ja pystyakselilla $B\ (\mu\text{T})$. Akselit alkavat nollasta. Kuusi pistettä merkitään taulukosta. Pisteitä ei yhdistetä murtoviivaksi. Niiden kautta voi piirtää tasaisen käyrän.

<svg data-fig="fy9-magnetismi-valo-s3-B" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden r funktiona senttimetreinä. Kuvassa on kuusi mustaa pistettä etäisyyksillä 2–12 cm. Arvot ovat 132 mikroteslasta 31 mikroteslaan. Pisteiden kautta kulkee katkoviivakäyrä. Käyrä laskee ensin jyrkästi ja sitten loivenee eli laskee hitaammin. Kun etäisyys kaksinkertaistuu 2 senttimetristä 4 senttimetriin, kenttä pienenee vain 132:sta 72:een. Kenttä ei pienene puoleen." style="max-width:100%;font-size:30px">
  <line x1="121.5" y1="380" x2="121.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="147.5" y1="380" x2="147.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="173" y1="380" x2="173" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="199" y1="380" x2="199" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224.5" y1="380" x2="224.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="380" x2="250" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="301.5" y1="380" x2="301.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="327" y1="380" x2="327" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="353" y1="380" x2="353" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="378.5" y1="380" x2="378.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="404.5" y1="380" x2="404.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="359.5" x2="430" y2="359.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="339.5" x2="430" y2="339.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="319" x2="430" y2="319" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="299" x2="430" y2="299" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="278.5" x2="430" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="258.5" x2="430" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="430" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218" x2="430" y2="218" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="430" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="177.5" x2="430" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="157" x2="430" y2="157" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137" x2="430" y2="137" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="116.5" x2="430" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="430" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="121.5" y1="380" x2="121.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="147.5" y1="380" x2="147.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="135.5" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="173" y1="380" x2="173" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="199" y1="380" x2="199" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="224.5" y1="380" x2="224.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250" y1="380" x2="250" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="238" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$6$</div></foreignObject>
  <line x1="276" y1="380" x2="276" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="301.5" y1="380" x2="301.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289.5" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="327" y1="380" x2="327" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="353" y1="380" x2="353" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$10$</div></foreignObject>
  <line x1="378.5" y1="380" x2="378.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404.5" y1="380" x2="404.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$12$</div></foreignObject>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="359.5" x2="96" y2="359.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="339.5" x2="96" y2="339.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="319" x2="96" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="299" x2="96" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="278.5" x2="96" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="260.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="89" y1="258.5" x2="96" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218" x2="96" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="177.5" x2="96" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="159.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="89" y1="157" x2="96" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137" x2="96" y2="137" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="116.5" x2="96" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="58" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$150$</div></foreignObject>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="16" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="142,86 144.5,99.5 147,112 149.5,123 152,133 154,142.5 156.5,151 159,158.5 161.5,166 164,173 166,179 168.5,185 171,190.5 173.5,196 176,201 178,205.5 180.5,210 183,214 185.5,217.5 188,221.5 190,225 192.5,228 195,231.5 197.5,234.5 200,237.5 202,240 204.5,242.5 207,245 209.5,247.5 212,250 214,252 216.5,254 219,256 221.5,258 224,260 226,262 228.5,263.5 231,265.5 233.5,267 236,268.5 238,270 240.5,271.5 243,273 245.5,274.5 248,275.5 250,277 252.5,278 255,279.5 257.5,280.5 259.5,282 262,283 264.5,284 267,285 269.5,286 271.5,287 274,288 276.5,289 279,290 281.5,290.5 283.5,291.5 286,292.5 288.5,293.5 291,294 293.5,295 295.5,295.5 298,296.5 300.5,297 303,298 305.5,298.5 307.5,299 310,300 312.5,300.5 315,301 317.5,302 319.5,302.5 322,303 324.5,303.5 327,304 329.5,304.5 331.5,305.5 334,306 336.5,306.5 339,307 341.5,307.5 343.5,308 346,308.5 348.5,309 351,309.5 353.5,309.5 355.5,310 358,310.5 360.5,311 363,311.5 365.5,312 367.5,312.5 370,312.5 372.5,313 375,313.5 377,314 379.5,314.5 382,314.5 384.5,315 387,315.5 389,315.5 391.5,316 394,316.5 396.5,317 399,317 401,317.5 403.5,318 406,318 408.5,318.5 411,318.5 413,319 415.5,319.5 418,319.5 420.5,320 423,320 425,320.5 427.5,320.5 430,321" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="147.5" cy="112.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="173" cy="197.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="199" cy="234" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250" cy="278.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="301.5" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="404.5" cy="317" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="263" y="169.5" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#6b7480">$\text{loivenee}$</div></foreignObject>
</svg>

**Mallivastaus:** Kenttä pienenee yhä hitaammin, kun etäisyys kasvaa. Kenttä ei kuitenkaan ole kääntäen verrannollinen etäisyyteen. Jos se olisi, kaksinkertainen etäisyys puolittaisi kentän. Kun etäisyys kasvaa $2{,}0\,\text{cm}$:stä $4{,}0\,\text{cm}$:iin, kenttä pienenee vain $132\,\mu\text{T}$:sta $72\,\mu\text{T}$:iin. Kun etäisyys kasvaa $4{,}0\,\text{cm}$:stä $8{,}0\,\text{cm}$:iin, kenttä pienenee $72\,\mu\text{T}$:sta $41\,\mu\text{T}$:iin. Myös tulo $Br$ kasvaa: $264$, $270$, $288$, $300$, $328$ ja $372\,\mu\text{T} \cdot \text{cm}$. Jos riippuvuus olisi kääntäen verrannollinen, tulo olisi vakio. Käyrä ei siis lähesty nollaa vaan jotakin positiivista arvoa. Kentässä näyttää olevan osa, joka ei riipu etäisyydestä.

### b)
**Kysytty:** aineiston esitys niin, että pisteisiin sopii suora, perustelu ja sovitettu suora
**Kuvaaja:** Pitkän suoran johtimen kenttä on $B = \tfrac{\mu_0 I}{2\pi r} = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r}$. Siksi $B$ on suoraan verrannollinen etäisyyden käänteislukuun. Jos mukana on lisäksi vakiokenttä $b$, $B = k \cdot \tfrac{1}{r} + b$. Se on edelleen suora $(\tfrac{1}{r}, B)$-koordinaatistossa. Lasketaan käänteisluvut: $50{,}0$, $33{,}3$, $25{,}0$, $16{,}7$, $12{,}5$ ja $8{,}33\,\tfrac{1}{\text{m}}$. Vaaka-akselilla on $\tfrac{1}{r}\ (\tfrac{1}{\text{m}})$ ja pystyakselilla $B\ (\mu\text{T})$. Suora sovitetaan pisteiden lomitse eli niiden välistä. Suoraa ei pakoteta kulkemaan origon kautta, jotta mahdollinen vakiokenttä näkyy.

<svg data-fig="fy9-magnetismi-valo-s3-lin" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden käänteisluvun 1 per r funktiona yksikössä 1 per metri. Kuvassa on kuusi mustaa pistettä välillä 8–50 per metri. Arvot ovat 31:stä 132 mikroteslaan. Pisteisiin on sovitettu nouseva suora. Suoraa on jatkettu katkoviivana pystyakselille. Suora leikkaa pystyakselin noin arvossa 11 mikroteslaa, selvästi origon yläpuolella. Suoralta on ympyröity kaksi pistettä, (5,0; 23) ja (50; 132). Niistä luetaan kulmakerroin, noin 2,42 mikroteslaa kertaa metri." style="max-width:100%;font-size:30px">
  <line x1="126.5" y1="380" x2="126.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156.5" y1="380" x2="156.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="187" y1="380" x2="187" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217.5" y1="380" x2="217.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="380" x2="248" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278" y1="380" x2="278" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308.5" y1="380" x2="308.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339" y1="380" x2="339" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="369.5" y1="380" x2="369.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="399.5" y1="380" x2="399.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="359.5" x2="430" y2="359.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="339.5" x2="430" y2="339.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="319" x2="430" y2="319" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="299" x2="430" y2="299" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="278.5" x2="430" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="258.5" x2="430" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="430" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218" x2="430" y2="218" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="430" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="177.5" x2="430" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="157" x2="430" y2="157" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137" x2="430" y2="137" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="116.5" x2="430" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="430" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="126.5" y1="380" x2="126.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="156.5" y1="380" x2="156.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="137" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$10$</div></foreignObject>
  <line x1="187" y1="380" x2="187" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="217.5" y1="380" x2="217.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="198" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="248" y1="380" x2="248" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="278" y1="380" x2="278" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$30$</div></foreignObject>
  <line x1="308.5" y1="380" x2="308.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="339" y1="380" x2="339" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="319.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="369.5" y1="380" x2="369.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="399.5" y1="380" x2="399.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="359.5" x2="96" y2="359.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="339.5" x2="96" y2="339.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="319" x2="96" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="299" x2="96" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="278.5" x2="96" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="260.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="89" y1="258.5" x2="96" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218" x2="96" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="177.5" x2="96" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="159.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="89" y1="157" x2="96" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137" x2="96" y2="137" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="116.5" x2="96" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="58" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$150$</div></foreignObject>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\tfrac{1}{r}\ (\tfrac{1}{\text{m}})$</div></foreignObject>
  <foreignObject x="86" y="16" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="146.5,318 399.5,113.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,358.5 146.5,318" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="399.5" cy="112.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298.5" cy="197.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="248" cy="234" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="197" cy="278.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="172" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="146.5" cy="317" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="126.5" cy="333.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="126.5" y1="333.5" x2="126.5" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="333.5" x2="126.5" y2="333.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="399.5" cy="112.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="399.5" y1="112.5" x2="399.5" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="112.5" x2="399.5" y2="112.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="96" cy="358.5" r="6" fill="#2b8a3e"/>
  <line x1="101" y1="353.5" x2="114" y2="254.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="105" y="216" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b \approx 11\,\mu\text{T}$</span></div></foreignObject>
  <foreignObject x="108" y="78.5" width="148" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$k \approx 2{,}42\,\mu\text{T}\cdot\text{m}$</div></foreignObject>
</svg>

**Mallivastaus:** Pisteet asettuvat hyvin suoralle. Siksi pitkän suoran johtimen malli kuvaa aineistoa. Suora ei kuitenkaan kulje origon kautta. Se leikkaa pystyakselin noin arvossa $10$–$11\,\mu\text{T}$. Tätä tulkitaan d-kohdassa.

### c)
**Annettu:** kuvaajaan sovitettu suora; suoralta luetut pisteet $(5{,}0\,\tfrac{1}{\text{m}};\ 23\,\mu\text{T})$ ja $(50\,\tfrac{1}{\text{m}};\ 132\,\mu\text{T})$; virta $I = 12{,}0\,\text{A}$
**Kysytty:** tyhjiön permeabiliteetti $\mu_0$ ja sen vertailu taulukkoarvoon
**Periaate:** Mallin $B = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r} + b$ mukaan $(\tfrac{1}{r}, B)$-kuvaajan kulmakerroin on $k = \tfrac{\mu_0 I}{2\pi}$ (luku *Virtajohtimen ja käämin magneettikenttä*). Kulmakerroin luetaan sovitetulta suoralta kahdesta pisteestä, jotka ovat kaukana toisistaan. Mittauspisteitä ei käytetä (luku *Graafinen esitys ja suoran sovittaminen*). Vakiokenttä siirtää suoraa, mutta se ei muuta suoran kulmakerrointa. Siksi vakiokenttä ei vaikuta tulokseen.
**Kuvaajan lukeminen:** Suoralta luetaan kohdissa $\tfrac{1}{r} = 5{,}0\,\tfrac{1}{\text{m}}$ ja $\tfrac{1}{r} = 50\,\tfrac{1}{\text{m}}$ arvot $B \approx 23\,\mu\text{T}$ ja $B \approx 132\,\mu\text{T}$.
**Kaava:** $k = \dfrac{\Delta B}{\Delta(1/r)}$ ja $k = \dfrac{\mu_0 I}{2\pi}$, joten $\mu_0 = \dfrac{2\pi k}{I}$
**Muunnokset:** $1\,\mu\text{T} = 10^{-6}\,\text{T}$, ja $\text{T} = \tfrac{\text{Vs}}{\text{m}^2}$, joten $\tfrac{\text{T} \cdot \text{m}}{\text{A}} = \tfrac{\text{Vs}}{\text{Am}}$.
**Sijoitus:** $k = \dfrac{132\,\mu\text{T} - 23\,\mu\text{T}}{50\,\tfrac{1}{\text{m}} - 5{,}0\,\tfrac{1}{\text{m}}} = \dfrac{109\,\mu\text{T}}{45\,\tfrac{1}{\text{m}}} = 2{,}422\,\mu\text{T} \cdot \text{m} = 2{,}422 \cdot 10^{-6}\,\text{T} \cdot \text{m}$, joten $\mu_0 = \dfrac{2\pi \cdot 2{,}422 \cdot 10^{-6}\,\text{T} \cdot \text{m}}{12{,}0\,\text{A}} = 1{,}268 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$
**Vastaus:** $\mu_0 \approx 1{,}27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$. Vastauksessa on kolme merkitsevää numeroa, kuten virrassa $12{,}0\,\text{A}$ ja kuvaajalta luetuissa arvoissa.
**Järkevyys:** Taulukkoarvo on $4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} = 1{,}257 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$. Ero on siis noin $0{,}9\,\%$. Lukemat vaihtelevat noin $1\,\mu\text{T}$. Suurimmilla $\tfrac{1}{r}$-arvoilla vaihtelu on alle $1\,\%$. Ero on siis mittaustarkkuuden rajoissa.

### d)
**Annettu:** suoran kulmakerroin $k \approx 2{,}42\,\mu\text{T} \cdot \text{m}$ ja vakiotermi $b \approx 10{,}9\,\mu\text{T}$ (c-kohdan luetuista pisteistä: $23\,\mu\text{T} - 2{,}422\,\mu\text{T} \cdot \text{m} \cdot 5{,}0\,\tfrac{1}{\text{m}}$), etäisyys $r = 50\,\text{cm}$, johtimen pituus $2{,}0\,\text{m}$
**Kysytty:** mitä vakiotermi kertoo mittauksesta ja anturin lukema $50\,\text{cm}$:n päässä
**Periaate:** Johtimen oma kenttä on kääntäen verrannollinen etäisyyteen. Siksi vakiotermi on kenttää, joka ei riipu virrasta eikä etäisyydestä. Anturi pysyi samassa asennossa, eikä sitä nollattu. Siksi sen lukemaan sisältyy kaksi asiaa: Maan magneettikentän komponentti anturin suunnassa ja anturin oma nollakohta (luvut *Magneetit, magneettinen dipoli ja magneettikenttä* ja *Mittaaminen ja mittauksen luotettavuus*). Lukema kauempana saadaan sovitetun suoran yhtälöstä. Pitkän johtimen malli pätee kuitenkin vain, kun etäisyys on paljon pienempi kuin johtimen pituus.
**Kuvaajan lukeminen:** Suora leikkaa $B$-akselin noin arvossa $11\,\mu\text{T}$. Luetuista pisteistä saadaan $b = 23\,\mu\text{T} - 2{,}422\,\mu\text{T} \cdot \text{m} \cdot 5{,}0\,\tfrac{1}{\text{m}} = 10{,}9\,\mu\text{T}$.
**Kaava:** $B = \dfrac{k}{r} + b$
**Muunnokset:** $50\,\text{cm} = 50 \cdot 0{,}01\,\text{m} = 0{,}50\,\text{m}$
**Sijoitus:** $B = \dfrac{2{,}422\,\mu\text{T} \cdot \text{m}}{0{,}50\,\text{m}} + 10{,}9\,\mu\text{T} = 4{,}84\,\mu\text{T} + 10{,}9\,\mu\text{T} = 15{,}7\,\mu\text{T}$
**Vastaus:** Vakiotermi on noin $11\,\mu\text{T}$. Se on vakiokenttä, joka ei riipu johtimen virrasta. Se on Maan magneettikentän komponentti anturin suunnassa ja anturin nollakohdan siirtymä. Tämän voi tarkistaa: mitataan lukema, kun virta on katkaistu. Silloin anturin pitäisi näyttää noin $11\,\mu\text{T}$. Mallin mukaan anturi näyttäisi $50\,\text{cm}$:n päässä noin $16\,\mu\text{T}$. Vastauksessa on kaksi merkitsevää numeroa, koska tulos riippuu kuvaajalta luetusta vakiotermistä. Tulos on vain arvio, koska $50\,\text{cm}$ on mitatun alueen ($2$–$12\,\text{cm}$) ulkopuolella. Lisäksi johtimen pituus $2{,}0\,\text{m}$ ei ole enää paljon suurempi kuin etäisyys. Siksi johtimen oma kenttä on hieman pienempi kuin $4{,}8\,\mu\text{T}$.
**Järkevyys:** Etelä-Suomessa Maan kentän vaakakomponentti on noin $14\,\mu\text{T}$. Siksi $11\,\mu\text{T}$:n komponentti anturin suunnassa on uskottava. Vakiotermin saa myös kahdesta mittauksesta. Jos $B = \tfrac{k}{r} + b$, niin $b = 2B(4{,}0\,\text{cm}) - B(2{,}0\,\text{cm}) = 2 \cdot 72\,\mu\text{T} - 132\,\mu\text{T} = 12\,\mu\text{T}$. Tulos on lähes sama.

### Yleisiä virheitä
- a-kohdassa pisteet yhdistetään murtoviivaksi, tai kääntäen verrannollisuus päätellään pelkästä laskevasta käyrästä.
- b-kohdassa $B$ piirretään etäisyyden funktiona logaritmiasteikolla ilman perustelua, tai suora pakotetaan kulkemaan origon kautta. Silloin kulmakerroin ja $\mu_0$ tulevat liian suuriksi.
- c-kohdassa unohdetaan muuntaa mikroteslat tesloiksi tai etäisyys metreiksi. Silloin tulos on kertaluokkia väärä.
- d-kohdassa vakiotermi selitetään satunnaisvirheellä. Vakiotermi nostaa kuitenkin kaikkia lukemia saman verran.

### Hyväksytään myös
- c-kohdassa sovitusohjelman kulmakerroin $2{,}42\,\mu\text{T} \cdot \text{m}$ ja $\mu_0 \approx 1{,}27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$.
- d-kohdassa johtimen oman kentän arvio $4{,}8\,\mu\text{T}$ ja toteamus, että lukema on vakiokentän kanssa noin $16\,\mu\text{T}$.

## fy9-magnetismi-valo-s4

### a)
**Kysytty:** miten sateenkaari syntyy ja kummalla reunalla punainen on
**Periaate:** Taitekerroin riippuu aallonpituudesta. Tätä kutsutaan dispersioksi. Vedessä violetin taitekerroin on suurin ja punaisen pienin. Sateenkaaressa valo taittuu pisaraan, heijastuu pisaran takapinnasta ja taittuu ulos (luku *Dispersio: prisma ja sateenkaari*).
**Mallivastaus:** Auringonvalo tulee pisaraan ja taittuu sen etupinnassa. Sitten valo heijastuu pisaran takapinnasta ja taittuu uudelleen ulos. Veden taitekerroin on punaiselle $1{,}331$ ja violetille $1{,}343$. Siksi värit taittuvat eri määrän ja lähtevät pisarasta hieman eri suuntiin. Kirkkain valo lähtee punaisella noin $42^\circ$:n kulmassa ja violetilla noin $40{,}6^\circ$:n kulmassa vastapisteen suuntaan nähden. Vastapiste on katsojan pään varjon suunta. Katsoja näkee punaista niistä pisaroista, jotka ovat $42^\circ$:n kulmassa. Violettia hän näkee pisaroista, jotka ovat hieman sisempänä. Siksi punainen on kaaren ulkoreunalla ja violetti sisäreunalla. Sateenkaaren kohdalla juhlavieraan väite pitää paikkansa: värit erottuvat, koska eri värit taittuvat vedessä eri määrän.

### b)
**Kysytty:** miten saippuakuplan värit syntyvät ja miksi ohuin kohta näyttää tummalta
**Periaate:** Aallot heijastuvat ohuen kalvon kahdesta pinnasta ja interferoivat eli yhdistyvät. Kun valo tulee kohtisuoraan, aaltojen matkaero on $2nd$. Aalto kääntyy, kun se heijastuu ainetta vasten, jonka taitekerroin on suurempi (luku *Ohuen kalvon interferenssi*).
**Mallivastaus:** Kupla on ohut saippuavesikalvo. Kalvon molemmin puolin on ilmaa. Osa valosta heijastuu kalvon ulkopinnasta ja osa sisäpinnasta. Nämä aallot interferoivat. Niiden matkaero $2nd$ riippuu kalvon paksuudesta $d$. Joillakin aallonpituuksilla aallot vahvistavat toisiaan, toisilla ne heikentävät toisiaan. Valkoisesta valosta jää jäljelle aallonpituuksien sekoitus, ja se näkyy värinä. Kalvon paksuus vaihtelee, joten väri vaihtuu raidoittain. Vain ulkopinnan heijastus kääntää aallon, koska siinä valo heijastuu ilmasta saippuavettä vasten. Juuri ennen puhkeamista kuplan yläosa on hyvin ohut, $2nd \approx 0$. Siksi heijastuneet aallot ovat lähes vastakkaisessa vaiheessa. Ne kumoavat toisensa kaikilla aallonpituuksilla, ja kohta näyttää tummalta. Kuplan kohdalla väite on väärä. Värit syntyvät interferenssistä, eivät taittumisesta. Väri riippuu kalvon paksuudesta.

### c)
**Kysytty:** miten CD-levy synnyttää värit, punaisen ja violetin ensimmäisen kertaluvun kulmat ja arvio väitteestä
**Periaate:** CD-levyssä on tiheitä uria, jotka toistuvat säännöllisin välein. Urat toimivat heijastushilana. Vierekkäisistä urista heijastuneet aallot vahvistavat toisiaan niissä suunnissa, joille $d\sin\theta = k\lambda$ (luku *Valon interferenssi ja diffraktio*).
**Mallivastaus:** CD-levyn pinnassa on ura, joka kulkee spiraalina. Uran vierekkäiset kierrokset ovat $1{,}6\,\mu\text{m}$:n päässä toisistaan. Jokainen ura heijastaa valoa. Eri urista heijastuneet aallot vahvistavat toisiaan vain niissä suunnissa, joissa niiden matkaero on kokonainen määrä aallonpituuksia. Kun valo tulee kohtisuoraan, ensimmäinen kertaluku on punaiselle $\sin\theta = \tfrac{650 \cdot 10^{-9}\,\text{m}}{1{,}6 \cdot 10^{-6}\,\text{m}} = 0{,}41$ eli $\theta \approx 24^\circ$. Violetille se on $\sin\theta = \tfrac{400 \cdot 10^{-9}\,\text{m}}{1{,}6 \cdot 10^{-6}\,\text{m}} = 0{,}25$ eli $\theta \approx 14{,}5^\circ$. Punainen poikkeaa siis eniten. Pisarassa ja prismassa on päinvastoin. Tämä osoittaa, että värit syntyvät eri tavalla. Kokonaisuutena juhlavieraan väite on väärä. Se pitää paikkansa vain sateenkaaressa. Kuplan värit syntyvät, kun kalvon kahden pinnan heijastukset interferoivat. CD-levyn värit syntyvät, kun monen uran heijastukset interferoivat. Niissä ei tarvita taittumista.

### Yleisiä virheitä
- a-kohdassa sanotaan, että punainen taittuu eniten, koska sen aallonpituus on pisin. Vedessä violetti taittuu kuitenkin eniten.
- b-kohdassa värit selitetään saippuan väriaineella tai taittumisella. Tai unohdetaan, että heijastus kääntää aallon. Silloin väitetään, että ohuin kohta on kirkas.
- c-kohdassa kulma lasketaan ilman sinin käänteisfunktiota, tai sanotaan, että violetti poikkeaa hilassa eniten.

## fy9-magnetismi-valo-s5

### a)
**Annettu:** hilassa on $N = 600$ viivaa millimetrillä, $L = 80{,}0\,\text{cm}$, $x_1 = 27{,}0\,\text{cm}$, $x_2 = 66{,}4\,\text{cm}$
**Kysytty:** laserin aallonpituus $\lambda$ kummastakin maksimista
**Periaate:** Hilan maksimit ovat niissä suunnissa, joille $d\sin\theta = k\lambda$. Hilavakio on viivojen välin pituus (luku *Valon interferenssi ja diffraktio*). Kulma saadaan varjostimen suorakulmaisesta kolmiosta: $\tan\theta = \tfrac{x}{L}$. Sini ja tangentti ovat lähes yhtä suuret vain pienillä kulmilla. Siksi kulma lasketaan ensin tangentista. Kulman sini lasketaan vasta sitten.
**Kaava:** $d = \dfrac{1\,\text{mm}}{N}$, $\theta_k = \tan^{-1}\dfrac{x_k}{L}$ ja $\lambda = \dfrac{d\sin\theta_k}{k}$
**Muunnokset:** $d = \dfrac{1\,\text{mm}}{600} = \dfrac{1 \cdot 10^{-3}\,\text{m}}{600} = 1{,}667 \cdot 10^{-6}\,\text{m}$. Etäisyyksien suhteessa yksiköt supistuvat pois. Lopuksi $1\,\text{m} = 10^9\,\text{nm}$.
**Sijoitus:** $\tan\theta_1 = \dfrac{27{,}0\,\text{cm}}{80{,}0\,\text{cm}} = 0{,}3375$, joten $\theta_1 = 18{,}65^\circ$ ja $\lambda = 1{,}667 \cdot 10^{-6}\,\text{m} \cdot \sin 18{,}65^\circ = 1{,}667 \cdot 10^{-6}\,\text{m} \cdot 0{,}3198 = 533{,}0\,\text{nm}$. $\tan\theta_2 = \dfrac{66{,}4\,\text{cm}}{80{,}0\,\text{cm}} = 0{,}830$, joten $\theta_2 = 39{,}69^\circ$ ja $\lambda = \dfrac{1{,}667 \cdot 10^{-6}\,\text{m} \cdot 0{,}6386}{2} = 532{,}2\,\text{nm}$
**Vastaus:** Ensimmäisestä kertaluvusta saadaan $\lambda \approx 533\,\text{nm}$ ja toisesta $\lambda \approx 532\,\text{nm}$. Vastauksissa on kolme merkitsevää numeroa, kuten etäisyyksissä.
**Järkevyys:** Molemmat kertaluvut antavat saman tuloksen. Se on vihreän valon aallonpituus, kuten laserin väri kertoo. Kulma $\theta_2 \approx 40^\circ$ on niin suuri, että $\sin\theta_2 = 0{,}64$ ja $\tan\theta_2 = 0{,}83$ eroavat selvästi.

### b)
**Kysytty:** ovatko ryhmän johtopäätökset perusteltuja
**Periaate:** Pienen kulman oletus $\sin\theta \approx \tfrac{x}{L}$ pätee vain pienillä kulmilla. Tulosta verrataan valmistajan arvoon epävarmuuden avulla. Ehto $k\lambda < d$ rajoittaa maksimien määrää (luvut *Valon interferenssi ja diffraktio* ja *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Kumpikaan johtopäätös ei ole perusteltu. Virhe on laskutavassa, ei laserissa. Pienen kulman oletus antaa ensimmäisestä kertaluvusta $\tfrac{1{,}667\,\mu\text{m} \cdot 0{,}270\,\text{m}}{0{,}800\,\text{m}} \approx 562\,\text{nm}$, eli noin $6\,\%$ liikaa. Toisesta kertaluvusta se antaa $692\,\text{nm}$, eli noin $30\,\%$ liikaa. Ero tangentin ja sinin välillä kasvaa, kun kulma kasvaa. Oikein laskettuna tulos on $532$–$533\,\text{nm}$. Oletetaan, että etäisyydet tunnetaan noin $0{,}3\,\text{cm}$:n tarkkuudella. Silloin toisen kertaluvun ääriarvot antavat noin $530$–$535\,\text{nm}$. Tulos on siis sopusoinnussa eli sopii yhteen valmistajan arvon $532\,\text{nm}$ kanssa. Lisäksi laser näytti vihreältä. Jo se sulkee pois punaisen valon. Kolmas kertaluku on olemassa, koska $3\lambda = 1{,}60\,\mu\text{m} < d = 1{,}667\,\mu\text{m}$. Kuitenkin $\sin\theta_3 = 0{,}958$, $\theta_3 \approx 73^\circ$, ja maksimi on $x_3 = 0{,}800\,\text{m} \cdot \tan 73{,}3^\circ \approx 2{,}7\,\text{m}$:n päässä keskimaksimista. Se on todennäköisesti seinän reunan ulkopuolella. Tai se on niin himmeä, ettei sitä huomattu. Hila ei siis ole viallinen.

### c)
**Kysytty:** miten mittausta parannetaan
**Periaate:** Suhteellinen epävarmuus pienenee, kun mitattava etäisyys on suuri verrattuna lukemisen epävarmuuteen. Systemaattiset virheet poistetaan mittaustavalla. Systemaattinen virhe on esimerkiksi vino asettelu, ja se vaikuttaa kaikkiin mittauksiin samalla tavalla. Tulos ilmoitetaan epävarmuuksineen (luvut *Mittaaminen ja mittauksen luotettavuus* ja *Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi*).
**Mallivastaus:** Mitataan keskimaksimin molemmin puolin olevien maksimien $+k$ ja $-k$ välinen etäisyys ja puolitetaan se. Kahden valopisteen välin mittaaminen on tarkempaa kuin keskimaksimin keskikohdan arvioiminen. Jos etäisyydet eri puolille ovat yhtä suuret, säde osuu hilaan kohtisuoraan. Käytetään toista kertalukua, jonka $x$ on suuri, tai kasvatetaan etäisyyttä $L$. Silloin lukemisen epävarmuus, noin $0{,}3\,\text{cm}$, on pieni osa mitatusta etäisyydestä. Arvioidaan $\Delta x$ ja $\Delta L$. Lasketaan aallonpituus niiden ääriarvoilla. Ilmoitetaan tulos muodossa $\lambda \pm \Delta\lambda$, esimerkiksi $(532 \pm 3)\,\text{nm}$, jotta sitä voi verrata valmistajan arvoon. Mittaus toistetaan, mieluiten niin, että eri henkilöt lukevat tulokset. Laskussa käytetään tangenttia eikä pienen kulman oletusta. Turvallisuus: lasersäteeseen ei katsota, eikä sädettä suunnata kenenkään silmiin. Säteen tielle ei jätetä esineitä, jotka heijastavat valoa.

### Yleisiä virheitä
- a-kohdassa käytetään $\sin\theta = \tfrac{x}{L}$, tai käytetään $\sin\theta = \tfrac{x}{\sqrt{x^2 + L^2}}$ mutta unohdetaan jakaa kertaluvulla.
- a-kohdassa hilavakioksi otetaan $600\,\text{mm}$ tai $\tfrac{1}{600}\,\text{m}$.
- b-kohdassa johtopäätös hyväksytään, koska laskettu luku ”näyttää punaiselta”, tai epävarmuutta ei verrata eroon.
- c-kohdassa ehdotetaan vain toistoja. Toistot eivät poista laskutavan systemaattista virhettä.

## fy9-magnetismi-valo-s6

### a)
**Annettu:** magneettivuon tiheys $B = 1{,}20\,\text{T}$, protonin massa $m = 1{,}673 \cdot 10^{-27}\,\text{kg}$ ja varaus $q = 1{,}602 \cdot 10^{-19}\,\text{C}$; nopeus on kohtisuorassa kenttää vastaan
**Kysytty:** osoitus, että kierrosaika ei riipu vauhdista, ja jännitteen taajuus $f$
**Periaate:** Magneettinen voima $qvB$ on kohtisuorassa nopeutta vastaan. Siksi protoni on elektrodin sisällä tasaisessa ympyräliikkeessä. Voima on sen keskeisvoima eli voima, joka osoittaa ympyrän keskipisteeseen (luvut *Varatun hiukkasen liike sähkö- ja magneettikentässä* ja *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*). Yhdellä kierroksella protoni kulkee ympyrän kehän $2\pi r$ (luku *Ympyrärata: jaksonaika ja ratanopeus*). Protoni ylittää raon joka puolikierroksella. Silloin jännitteen suunnan on vaihduttava. Siksi jännitteen taajuus on sama kuin kierrostaajuus.
**Kaava:** $qvB = \dfrac{mv^2}{r}$, joten $r = \dfrac{mv}{qB}$, ja $T = \dfrac{2\pi r}{v} = \dfrac{2\pi m}{qB}$; vauhti supistuu pois, ja $f = \dfrac{1}{T} = \dfrac{qB}{2\pi m}$
**Muunnokset:** Suureet ovat perusyksiköissä. Lopuksi $1\,\text{MHz} = 10^6\,\text{Hz}$.
**Sijoitus:** $T = \dfrac{2\pi \cdot 1{,}673 \cdot 10^{-27}\,\text{kg}}{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}20\,\text{T}} = 5{,}468 \cdot 10^{-8}\,\text{s}$, joten $f = \dfrac{1}{5{,}468 \cdot 10^{-8}\,\text{s}} = 1{,}829 \cdot 10^{7}\,\text{Hz} = 18{,}29\,\text{MHz}$
**Vastaus:** Kierrosaika $T = \tfrac{2\pi m}{qB}$ ei riipu vauhdista eikä säteestä. Nopeampi protoni kulkee suuremman ympyrän samassa ajassa. Jännitteen on vaihdeltava taajuudella $f \approx 18{,}3\,\text{MHz}$. Vastauksessa on kolme merkitsevää numeroa, kuten magneettivuon tiheydessä $1{,}20\,\text{T}$.
**Järkevyys:** Yksiköt: $\tfrac{\text{kg}}{\text{C} \cdot \text{T}} = \tfrac{\text{kg}}{\text{C} \cdot \tfrac{\text{N}}{\text{A} \cdot \text{m}}} = \tfrac{\text{kg} \cdot \text{m}}{\text{N} \cdot \text{s}} = \text{s}$. Taajuus on radiotaajuusaluetta. Syklotronien kiihdytysjännitteillä on tällaisia taajuuksia.

### b)
**Annettu:** liike-energia $E_\text{k} = 8{,}0\,\text{MeV}$, $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$, $m$, $q$ ja $B$ kuten a-kohdassa
**Kysytty:** protonin vauhti $v$ ja radan säde $r$, kun protoni tulee ulos
**Periaate:** Klassisessa mekaniikassa liike-energia on $\tfrac12 mv^2$. Radan säde saadaan keskeisvoiman yhtälöstä kuten a-kohdassa (luku *Varatun hiukkasen liike sähkö- ja magneettikentässä*). Klassinen mekaniikka riittää, jos vauhti jää selvästi pienemmäksi kuin valon nopeus.
**Kaava:** $v = \sqrt{\dfrac{2E_\text{k}}{m}}$ ja $r = \dfrac{mv}{qB}$
**Muunnokset:** $8{,}0\,\text{MeV} = 8{,}0 \cdot 10^6 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}282 \cdot 10^{-12}\,\text{J}$
**Sijoitus:** $v = \sqrt{\dfrac{2 \cdot 1{,}282 \cdot 10^{-12}\,\text{J}}{1{,}673 \cdot 10^{-27}\,\text{kg}}} = 3{,}914 \cdot 10^{7}\,\text{m/s}$ ja $r = \dfrac{1{,}673 \cdot 10^{-27}\,\text{kg} \cdot 3{,}914 \cdot 10^{7}\,\text{m/s}}{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}20\,\text{T}} = 0{,}3406\,\text{m}$
**Vastaus:** Protonin vauhti on $v \approx 3{,}9 \cdot 10^7\,\text{m/s}$ ja radan säde $r \approx 0{,}34\,\text{m}$. Vastauksissa on kaksi merkitsevää numeroa, kuten energiassa $8{,}0\,\text{MeV}$.
**Järkevyys:** $\tfrac{v}{c} = \tfrac{3{,}914 \cdot 10^7\,\text{m/s}}{3{,}00 \cdot 10^8\,\text{m/s}} \approx 0{,}13$. Se on alle viidesosa. Tehtävän ehdon mukaan klassinen malli siis riittää. Elektrodien halkaisija on noin $70\,\text{cm}$. Se sopii sairaalan laitteeseen.

### c)
**Annettu:** raon jännite $U = 50\,\text{kV}$ ylityksellä, kaksi ylitystä kierroksessa, $E_\text{k} = 8{,}0\,\text{MeV}$, $T = 5{,}468 \cdot 10^{-8}\,\text{s}$ (a-kohta)
**Kysytty:** kierrosten lukumäärä $n$ ja kiihdytyksen kesto $t$
**Periaate:** Magneettinen voima on kohtisuorassa nopeutta vastaan. Siksi se ei tee työtä eikä muuta vauhtia. Vain raon sähkökenttä tekee työtä. Jokaisella ylityksellä protonin liike-energia kasvaa määrän $qU$ (luku *Potentiaalienergia ja potentiaali sähkökentässä*). Protoni ylittää raon kahdesti kierroksessa. Kierrosaika pysyy samana koko kiihdytyksen ajan (a-kohta).
**Kaava:** $n = \dfrac{E_\text{k}}{2qU}$ ja $t = nT$
**Muunnokset:** Protonin varaus on alkeisvaraus eli pienin vapaa varaus. Siksi $qU = 50\,\text{keV} = 0{,}050\,\text{MeV}$. Lopuksi $1\,\text{s} = 10^6\,\mu\text{s}$.
**Sijoitus:** $n = \dfrac{8{,}0\,\text{MeV}}{2 \cdot 0{,}050\,\text{MeV}} = 80$ ja $t = 80 \cdot 5{,}468 \cdot 10^{-8}\,\text{s} = 4{,}37 \cdot 10^{-6}\,\text{s} = 4{,}37\,\mu\text{s}$
**Vastaus:** Protoni tekee noin $80$ kierrosta, ja kiihdytys kestää noin $4{,}4\,\mu\text{s}$. Vastauksissa on kaksi merkitsevää numeroa, kuten energiassa $8{,}0\,\text{MeV}$.
**Järkevyys:** Ilman magneettikenttää sama energia vaatisi $8{,}0\,\text{MV}$:n jännitteen. Syklotroni saavuttaa sen $50\,\text{kV}$:n jännitteellä, koska samaa rakoa käytetään $160$ kertaa. Kulkumatka on alle $80 \cdot 2\pi \cdot 0{,}34\,\text{m} \approx 170\,\text{m}$. Siksi lyhyt aika on uskottava.

### d)
**Annettu:** $v = 3{,}914 \cdot 10^{7}\,\text{m/s}$ ja $r = 0{,}3406\,\text{m}$ (b-kohta)
**Kysytty:** kiihtyvyys $a$ ja sen suunta, kun protoni tulee ulos
**Periaate:** Elektrodin sisällä protoni on tasaisessa ympyräliikkeessä. Siksi sen kiihtyvyys on normaalikiihtyvyys. Normaalikiihtyvyys osoittaa radan keskipisteeseen (luku *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*). Saman tuloksen antaa Newtonin toinen laki magneettiselle voimalle.
**Kaava:** $a_\text{n} = \dfrac{v^2}{r}$, ja tarkistukseksi $a = \dfrac{qvB}{m}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $a_\text{n} = \dfrac{(3{,}914 \cdot 10^{7}\,\text{m/s})^2}{0{,}3406\,\text{m}} = 4{,}498 \cdot 10^{15}\,\text{m/s}^2$
**Vastaus:** Kiihtyvyys on $a \approx 4{,}5 \cdot 10^{15}\,\text{m/s}^2$, ja se osoittaa radan keskipisteeseen. Vastauksessa on kaksi merkitsevää numeroa, kuten b-kohdan tuloksissa.
**Järkevyys:** $\tfrac{qvB}{m} = \tfrac{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 3{,}914 \cdot 10^{7}\,\text{m/s} \cdot 1{,}20\,\text{T}}{1{,}673 \cdot 10^{-27}\,\text{kg}} \approx 4{,}5 \cdot 10^{15}\,\text{m/s}^2$. Tulos on sama. Kiihtyvyys on valtava, koska protonin massa on hyvin pieni. Voima on noin $7{,}5 \cdot 10^{-12}\,\text{N}$.

### Yleisiä virheitä
- a-kohdassa kierrosaika lasketaan erikseen jollekin vauhdille, eikä todeta, että vauhti supistuu pois.
- b-kohdassa megaelektronivoltteja ei muunneta jouleiksi, tai käytetään elektronin massaa.
- c-kohdassa unohdetaan, että rako ylitetään kahdesti kierroksessa. Silloin kierroksia tulee $160$.
- d-kohdassa sanotaan, että kiihtyvyys osoittaa nopeuden suuntaan tai kiihdyttää protonia magneettikentässä.

### Hyväksytään myös
- a-kohdassa taajuuden laskeminen suoraan lausekkeesta $f = \tfrac{qB}{2\pi m}$.
- c-kohdassa vastaus $n = 80$ ilman desimaaleja, koska kierrosten määrä on kokonaisluku.
