## fy9-magnetismi-valo-s1

### a)
**Annettu:** kierrokset $N = 60$, pinta-ala $A = 0{,}060\,\text{m}^2$, magneettivuon tiheys $B = 0{,}50\,\text{T}$, pyörimistaajuus $f = 50\,\text{Hz}$
**Kysytty:** jännitteen huippuarvo $e_0$ ja tehollinen arvo $U$
**Periaate:** Kun käämi pyörii tasaisesti homogeenisessa kentässä, sen läpi kulkeva vuo vaihtelee jaksollisesti, ja induktiolain mukaan käämiin syntyy sinimuotoinen jännite. Jännite on huippuarvossaan, kun käämin taso on kentän suuntainen, koska vuo muuttuu silloin nopeimmin (luvut *Sähkömagneettinen induktio* ja *Generaattori ja vaihtovirta*). Tehollinen arvo on se tasajännite, joka antaisi vastukseen saman keskimääräisen tehon; sinimuotoisella jännitteellä se on huippuarvo jaettuna luvulla $\sqrt{2}$.
**Kaava:** $e_0 = NBA \cdot 2\pi f$ ja $U = \dfrac{e_0}{\sqrt{2}}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $e_0 = 60 \cdot 0{,}50\,\text{T} \cdot 0{,}060\,\text{m}^2 \cdot 2\pi \cdot 50\,\tfrac{1}{\text{s}} = 565{,}5\,\text{V}$ ja $U = \dfrac{565{,}5\,\text{V}}{\sqrt{2}} = 399{,}9\,\text{V}$
**Vastaus:** Huippuarvo on $e_0 \approx 570\,\text{V}$ ja tehollinen arvo $U \approx 400\,\text{V}$, kaksi merkitsevää numeroa kuten magneettivuon tiheys $0{,}50\,\text{T}$ ja pinta-ala $0{,}060\,\text{m}^2$.
**Järkevyys:** Yksiköt sopivat: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. Tehollinen arvo on huippuarvoa pienempi, kuten pitää, ja $400\,\text{V}$ on tavallinen teollisuuden jännite.

### b)
**Annettu:** generaattorin tehollinen jännite $U_1 = 400\,\text{V}$, linjan jännite $U_2 = 20{,}0\,\text{kV}$, teho $P = 150\,\text{kW}$; muuntaja ideaalinen
**Kysytty:** kierrosten suhde $N_2 : N_1$ sekä virrat $I_1$ ja $I_2$
**Periaate:** Ideaalisessa muuntajassa jännitteiden suhde on kierrosten lukumäärien suhde, ja teho säilyy: $U_1 I_1 = U_2 I_2$ (luku *Muuntaja ja sähköenergian siirto*). Kun jännite kasvaa, virta pienenee samassa suhteessa. Jännitteet ja virrat ovat tehollisia arvoja, joten $P = UI$.
**Kaava:** $\dfrac{N_2}{N_1} = \dfrac{U_2}{U_1}$, $I_1 = \dfrac{P}{U_1}$ ja $I_2 = \dfrac{P}{U_2}$
**Muunnokset:** $20{,}0\,\text{kV} = 20{,}0 \cdot 1000\,\text{V} = 20\,000\,\text{V}$ ja $150\,\text{kW} = 150 \cdot 1000\,\text{W} = 150\,000\,\text{W}$
**Sijoitus:** $\dfrac{N_2}{N_1} = \dfrac{20\,000\,\text{V}}{400\,\text{V}} = 50$, $I_1 = \dfrac{150\,000\,\text{W}}{400\,\text{V}} = 375\,\text{A}$ ja $I_2 = \dfrac{150\,000\,\text{W}}{20\,000\,\text{V}} = 7{,}50\,\text{A}$
**Vastaus:** Toisiokäämissä on $50$ kertaa niin monta kierrosta kuin ensiökäämissä. Generaattorin puolella virta on $I_1 \approx 375\,\text{A}$ ja linjassa $I_2 \approx 7{,}50\,\text{A}$, kolme merkitsevää numeroa kuten jännite $20{,}0\,\text{kV}$ ja teho $150\,\text{kW}$.
**Järkevyys:** Virtojen suhde $375 : 7{,}50 = 50$ on sama kuin kierrosten suhde, ja $U_2 I_2 = 20\,000\,\text{V} \cdot 7{,}50\,\text{A} = 150\,\text{kW}$, sama kuin ensiössä.

### c)
**Annettu:** linjan virta $I_2 = 7{,}50\,\text{A}$ (b-kohta), resistanssi $R = 6{,}0\,\Omega$, teho $P = 150\,\text{kW}$; vertailuksi jännite $400\,\text{V}$
**Kysytty:** lämmöksi muuttuvan tehon osuus $\tfrac{P_\text{h}}{P}$ ja mitä tapahtuisi jännitteellä $400\,\text{V}$
**Periaate:** Linjan resistanssissa sähköenergiaa muuttuu sisäenergiaksi teholla $RI^2$. Siirtojännite $20\,\text{kV}$ ei ole linjan resistanssin yli, joten häviö lasketaan virrasta, joka saadaan siirrettävästä tehosta (luku *Muuntaja ja sähköenergian siirto*).
**Kaava:** $I = \dfrac{P}{U}$ ja $P_\text{h} = RI^2$, osuus $\dfrac{P_\text{h}}{P}$
**Muunnokset:** Lopuksi osuus prosentteina: kerrotaan luvulla $100\,\%$.
**Sijoitus:** $P_\text{h} = 6{,}0\,\Omega \cdot (7{,}50\,\text{A})^2 = 337{,}5\,\text{W}$, joten $\dfrac{P_\text{h}}{P} = \dfrac{337{,}5\,\text{W}}{150\,000\,\text{W}} = 0{,}00225 = 0{,}225\,\%$. Jännitteellä $400\,\text{V}$: $I = 375\,\text{A}$ ja $RI^2 = 6{,}0\,\Omega \cdot (375\,\text{A})^2 = 843\,750\,\text{W} \approx 844\,\text{kW}$
**Vastaus:** Linjassa muuttuu lämmöksi noin $0{,}23\,\%$ tehosta, kaksi merkitsevää numeroa kuten resistanssi $6{,}0\,\Omega$. Jännitteellä $400\,\text{V}$ lauseke $RI^2$ antaisi $844\,\text{kW}$, yli viisinkertaisen siirrettävään tehoon verrattuna. Se tarkoittaa, että siirto ei onnistuisi lainkaan: jo linjan jännitehäviö $RI = 6{,}0\,\Omega \cdot 375\,\text{A} = 2250\,\text{V}$ olisi suurempi kuin koko jännite.
**Järkevyys:** Häviö on verrannollinen virran neliöön, ja virta kääntäen verrannollinen jännitteeseen, joten $50$-kertainen jännite pienentää häviötä kertoimella $50^2 = 2500$: $844\,\text{kW} : 2500 \approx 340\,\text{W}$, sama tulos.

### d)
**Kysytty:** toimiiko muuntaja tasajännitteellä
**Periaate:** Muuntajan toisiojännite syntyy induktiolla: ensiövirta synnyttää rautasydämeen magneettivuon, ja vain vuon muutos indusoi toisiokäämiin jännitteen (luvut *Sähkömagneettinen induktio* ja *Muuntaja ja sähköenergian siirto*).
**Mallivastaus:** Ehdotus ei toimi. Tasavirta synnyttää rautasydämeen vakiovuon, eikä muuttumaton vuo indusoi toisiokäämiin jännitettä. Vain virran kytkentähetkellä vuo muuttuu, ja toisioon syntyy lyhyt jännitepiikki. Siksi aurinkopaneelien tasajännite muutetaan ensin vaihtojännitteeksi vaihtosuuntaajalla, ja vasta sen jälkeen muuntaja voi nostaa sen linjan jännitteeksi. Lisäksi tasavirralla ensiökäämin virtaa rajoittaa vain sen pieni resistanssi, joten käämi voisi ylikuumentua.

### Yleisiä virheitä
- a-kohdassa annetaan huippuarvo tehollisena arvona tai jaetaan väärään suuntaan, $e_0 \cdot \sqrt{2} \approx 800\,\text{V}$.
- a-kohdassa unohdetaan kerroin $2\pi$, jolloin $e_0 = 90\,\text{V}$.
- b-kohdassa virrat käännetään: suuremman jännitteen puolella virta on pienempi.
- c-kohdassa häviö lasketaan lausekkeesta $\tfrac{U^2}{R} = \tfrac{(20\,000\,\text{V})^2}{6{,}0\,\Omega} \approx 67\,\text{MW}$; siirtojännite ei ole linjan resistanssin yli.

### Hyväksytään myös
- c-kohdassa vertailu suhteena: $\tfrac{P_\text{h,400}}{P_\text{h,20k}} = \left(\tfrac{20\,000}{400}\right)^2 = 2500$, kun todetaan, että $400\,\text{V}$:n siirto on mahdoton.

## fy9-magnetismi-valo-s2

### a)
**Annettu:** ytimen taitekerroin $n_1 = 1{,}470$, kuoren taitekerroin $n_2 = 1{,}455$
**Kysytty:** pienin tulokulma $\alpha_\text{r}$, jolla valo pysyy ytimessä, ja suurin kulma säteen ja kuidun akselin välillä
**Periaate:** Valo pysyy ytimessä, jos se kokonaisheijastuu ytimen ja kuoren rajapinnasta. Kokonaisheijastuminen on mahdollista, koska valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen, ja se tapahtuu, kun tulokulma on rajakulmaa suurempi (luku *Kokonaisheijastuminen ja valokuitu*). Tulokulma mitataan rajapinnan normaalista, ja normaali on kohtisuorassa kuidun akselia vastaan, joten säteen ja akselin välinen kulma on $90^\circ - \alpha$.
**Kaava:** $n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ$, joten $\sin\alpha_\text{r} = \dfrac{n_2}{n_1}$, ja akselin suhteen $\beta_\text{max} = 90^\circ - \alpha_\text{r}$
**Muunnokset:** Taitekertoimet ovat yksiköttömiä, joten muunnoksia ei tarvita.
**Sijoitus:** $\sin\alpha_\text{r} = \dfrac{1{,}455}{1{,}470} = 0{,}9898$, joten $\alpha_\text{r} = 81{,}81^\circ$ ja $\beta_\text{max} = 90^\circ - 81{,}81^\circ = 8{,}19^\circ$
**Vastaus:** Tulokulman on oltava vähintään $81{,}8^\circ$, eli säde saa olla enintään $8{,}2^\circ$:n kulmassa kuidun akseliin nähden. Taitekertoimien ero $0{,}015$ tunnetaan vain kahden numeron tarkkuudella: jo $0{,}001$:n muutos siinä siirtää rajakulmaa noin $0{,}3^\circ$. Rehellinen tarkkuus on siis noin $82^\circ$ ja $8^\circ$; kymmenesosa ilmoitetaan vain vertailua varten.
**Järkevyys:** Taitekertoimet ovat lähes yhtä suuret, joten rajakulma on lähellä $90^\circ$: vain lähes akselin suuntaiset säteet pysyvät ytimessä. Lasin ja ilman välillä rajakulma olisi noin $43^\circ$.

### b)
**Annettu:** kuidun pituus $s = 14{,}0\,\text{km}$, ytimen taitekerroin $n_1 = 1{,}470$, $c = 3{,}00 \cdot 10^8\,\text{m/s}$, $\sin\alpha_\text{r} = 0{,}9898$ (a-kohta)
**Kysytty:** akselin suuntaisen pulssin kulkuaika $t$ ja jyrkimmän säteen lisäaika $\Delta t$
**Periaate:** Aineessa valo etenee nopeudella $v = \tfrac{c}{n}$ (luku *Valon heijastuminen ja taittuminen*). Akselin suuntainen säde kulkee kuidun pituuden. Jyrkin ytimessä pysyvä säde etenee kulmassa $90^\circ - \alpha_\text{r}$ akseliin nähden, joten sen kulkema matka on kuidun pituus jaettuna tämän kulman kosinilla, eli $\tfrac{s}{\sin\alpha_\text{r}}$ (luku *Kokonaisheijastuminen ja valokuitu*). Molemmat säteet etenevät ytimessä samalla nopeudella.
**Kaava:** $t = \dfrac{n_1 s}{c}$, jyrkimmälle säteelle $t' = \dfrac{t}{\sin\alpha_\text{r}}$ ja $\Delta t = t' - t$
**Muunnokset:** $14{,}0\,\text{km} = 14{,}0 \cdot 1000\,\text{m} = 14\,000\,\text{m}$ ja lopuksi $1\,\text{s} = 10^6\,\mu\text{s}$
**Sijoitus:** $t = \dfrac{1{,}470 \cdot 14\,000\,\text{m}}{3{,}00 \cdot 10^8\,\text{m/s}} = 6{,}860 \cdot 10^{-5}\,\text{s} = 68{,}60\,\mu\text{s}$, $t' = \dfrac{68{,}60\,\mu\text{s}}{0{,}9898} = 69{,}31\,\mu\text{s}$ ja $\Delta t = 69{,}31\,\mu\text{s} - 68{,}60\,\mu\text{s} = 0{,}71\,\mu\text{s}$
**Vastaus:** Akselin suuntainen pulssi kulkee matkan ajassa $t \approx 68{,}6\,\mu\text{s}$, kolme merkitsevää numeroa kuten pituus $14{,}0\,\text{km}$. Jyrkimmin etenevä pulssi tulee perille noin $0{,}7\,\mu\text{s}$ myöhemmin; erotus tunnetaan vain yhden tai kahden numeron tarkkuudella.
**Järkevyys:** Valo etenee kuidussa nopeudella $\tfrac{3{,}00 \cdot 10^8\,\text{m/s}}{1{,}470} \approx 2{,}04 \cdot 10^8\,\text{m/s}$, noin kaksi kolmasosaa tyhjiön valonnopeudesta. Ero noin $1\,\%$ vastaa matkojen suhdetta $\tfrac{1}{0{,}9898} \approx 1{,}010$. Jos pulssit lähtisivät tiheämmin kuin noin mikrosekunnin välein, ne voisivat sekoittua.

### c)
**Annettu:** vaimennuskerroin $a = 0{,}22\,\text{dB/km}$, pituus $L = 14{,}0\,\text{km}$, neljä jatkosta à $0{,}10\,\text{dB}$, lähetysteho $P_0 = 2{,}0\,\text{mW}$
**Kysytty:** vastaanotettu teho $P$
**Periaate:** Kuidun lasi vaimentaa valoa samassa suhteessa joka kilometrillä, ja vaimennus ilmoitetaan desibeleinä. Peräkkäisten osien ja jatkosten vaimennukset desibeleinä lasketaan yhteen (luku *Soveltava luku: langaton lataus, induktioliesi ja kuituyhteys*).
**Kaava:** $A = aL + 4 \cdot 0{,}10\,\text{dB}$ ja $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, joten $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$
**Muunnokset:** Pituus on jo kilometreinä ja teho milliwatteina, joten muunnoksia ei tarvita.
**Sijoitus:** $A = 0{,}22\,\tfrac{\text{dB}}{\text{km}} \cdot 14{,}0\,\text{km} + 0{,}40\,\text{dB} = 3{,}08\,\text{dB} + 0{,}40\,\text{dB} = 3{,}48\,\text{dB}$, joten $P = 2{,}0\,\text{mW} \cdot 10^{-0{,}348} = 2{,}0\,\text{mW} \cdot 0{,}4487 = 0{,}897\,\text{mW}$
**Vastaus:** Vastaanottimeen saapuu noin $0{,}90\,\text{mW}$, kaksi merkitsevää numeroa kuten lähetysteho $2{,}0\,\text{mW}$ ja vaimennuskerroin $0{,}22\,\text{dB/km}$.
**Järkevyys:** $3\,\text{dB}$ vastaa noin tehon puolittumista, joten $3{,}5\,\text{dB}$ jättää vähän alle puolet, $45\,\%$. Tulos on uskottava, koska tietoliikennekuidussa valo kulkee kymmeniä kilometrejä ilman vahvistusta.

### d)
**Kysytty:** miksi loivasti kaartuva kuitu johtaa valoa mutta jyrkkä mutka päästää sen ulos
**Periaate:** Valo pysyy ytimessä, kun tulokulma ytimen ja kuoren rajapinnassa on rajakulmaa suurempi, tässä kuidussa vähintään $81{,}8^\circ$ (luku *Kokonaisheijastuminen ja valokuitu*).
**Mallivastaus:** Loivassa kaaressa rajapinnan suunta muuttuu säteen matkalla vain vähän, joten säde osuu rajapintaan edelleen lähes sen suuntaisesti, ja tulokulma pysyy rajakulmaa suurempana. Valo kokonaisheijastuu ja seuraa kuitua. Jyrkässä mutkassa ulkokaaren rajapinta kääntyy säteen eteen, joten säde osuu siihen jyrkemmin: tulokulma pienenee alle $81{,}8^\circ$:n, valo taittuu kuoreen ja vuotaa ulos. Koska rajakulma on lähellä $90^\circ$, jo melko pieni muutos tulokulmassa riittää. Siksi kuitukaapelille ilmoitetaan pienin sallittu taivutussäde.

### Yleisiä virheitä
- a-kohdassa taitekertoimet käännetään, $\sin\alpha_\text{r} = \tfrac{n_1}{n_2} > 1$, tai kulma annetaan akselin suhteen tulokulmana.
- b-kohdassa käytetään tyhjiön valonnopeutta, jolloin $t \approx 46{,}7\,\mu\text{s}$.
- c-kohdassa vaimennus jaetaan kymmenellä ja kerrotaan tehoon, tai jatkosten vaimennus unohdetaan, jolloin $P \approx 0{,}98\,\text{mW}$.

## fy9-magnetismi-valo-s3

### a)
**Kysytty:** magneettivuon tiheys etäisyyden funktiona kuvaajana ja onko se kääntäen verrannollinen etäisyyteen
**Kuvaaja:** Vaaka-akselilla on $r\ (\text{cm})$ ja pystyakselilla $B\ (\mu\text{T})$, ja akselit alkavat nollasta. Kuusi pistettä merkitään taulukosta. Pisteitä ei yhdistetä murtoviivaksi; niiden kautta voi piirtää tasaisen käyrän.

<svg data-fig="fy9-magnetismi-valo-s3-B" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden r funktiona senttimetreinä. Kuusi mustaa pistettä etäisyyksillä 2–12 cm, arvot 132 mikroteslasta 31 mikroteslaan. Pisteiden kautta kulkee katkoviivakäyrä, joka laskee jyrkästi ja loivenee. Kun etäisyys kaksinkertaistuu 2 senttimetristä 4 senttimetriin, kenttä pienenee vain 132:sta 72:een eikä puoleen." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Kenttä pienenee etäisyyden kasvaessa yhä hitaammin, mutta se ei ole kääntäen verrannollinen etäisyyteen. Jos olisi, kaksinkertainen etäisyys puolittaisi kentän, mutta $2{,}0\,\text{cm}$:stä $4{,}0\,\text{cm}$:iin kenttä pienenee vain $132\,\mu\text{T}$:sta $72\,\mu\text{T}$:iin, ja $4{,}0\,\text{cm}$:stä $8{,}0\,\text{cm}$:iin $72\,\mu\text{T}$:sta $41\,\mu\text{T}$:iin. Myös tulo $Br$ kasvaa: $264$, $270$, $288$, $300$, $328$ ja $372\,\mu\text{T} \cdot \text{cm}$. Kääntäen verrannollisessa riippuvuudessa se olisi vakio. Käyrä ei siis lähesty nollaa vaan jotakin positiivista arvoa: kenttään näyttää sisältyvän etäisyydestä riippumaton osa.

### b)
**Kysytty:** aineiston esitys niin, että pisteisiin sopii suora, perustelu ja sovitettu suora
**Kuvaaja:** Pitkän suoran johtimen kenttä on $B = \tfrac{\mu_0 I}{2\pi r} = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r}$, joten $B$ on suoraan verrannollinen etäisyyden käänteislukuun. Jos mukana on lisäksi vakiokenttä $b$, $B = k \cdot \tfrac{1}{r} + b$, joka on edelleen suora $(\tfrac{1}{r}, B)$-koordinaatistossa. Lasketaan käänteisluvut: $50{,}0$, $33{,}3$, $25{,}0$, $16{,}7$, $12{,}5$ ja $8{,}33\,\tfrac{1}{\text{m}}$. Vaaka-akselilla on $\tfrac{1}{r}\ (\tfrac{1}{\text{m}})$ ja pystyakselilla $B\ (\mu\text{T})$. Suora sovitetaan pisteiden lomitse eikä pakoteta origon kautta, jotta mahdollinen vakiokenttä näkyy.

<svg data-fig="fy9-magnetismi-valo-s3-lin" viewBox="0 0 600 440" role="img" aria-label="Kuvaaja: magneettivuon tiheys B mikrotesloina etäisyyden käänteisluvun 1 per r funktiona yksikössä 1 per metri. Kuusi mustaa pistettä välillä 8–50 per metri, arvot 31:stä 132 mikroteslaan. Pisteisiin on sovitettu nouseva suora, jota on jatkettu katkoviivana pystyakselille, jonka se leikkaa noin arvossa 11 mikroteslaa, selvästi origon yläpuolella. Suoralta on ympyröity kaksi pistettä, (5,0; 23) ja (50; 132), joista luetaan kulmakerroin noin 2,42 mikroteslaa kertaa metri." style="max-width:100%;font-size:30px">
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

**Mallivastaus:** Pisteet asettuvat hyvin suoralle, joten pitkän suoran johtimen malli kuvaa aineistoa. Suora ei kuitenkaan kulje origon kautta, vaan leikkaa pystyakselin noin arvossa $10$–$11\,\mu\text{T}$. Tätä tulkitaan d-kohdassa.

### c)
**Annettu:** sovitettu suora kuvaajassa; suoralta luetut pisteet $(5{,}0\,\tfrac{1}{\text{m}};\ 23\,\mu\text{T})$ ja $(50\,\tfrac{1}{\text{m}};\ 132\,\mu\text{T})$; virta $I = 12{,}0\,\text{A}$
**Kysytty:** tyhjiön permeabiliteetti $\mu_0$ ja sen vertailu taulukkoarvoon
**Periaate:** Mallin $B = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r} + b$ mukaan $(\tfrac{1}{r}, B)$-kuvaajan kulmakerroin on $k = \tfrac{\mu_0 I}{2\pi}$ (luku *Virtajohtimen ja käämin magneettikenttä*). Kulmakerroin luetaan kahdesta kaukana toisistaan olevasta sovitetun suoran pisteestä, ei mittauspisteistä (luku *Graafinen esitys ja suoran sovittaminen*). Vakiokenttä siirtää suoraa mutta ei muuta sen kulmakerrointa, joten se ei vaikuta tulokseen.
**Kuvaajan lukeminen:** Suoralta luetaan kohdissa $\tfrac{1}{r} = 5{,}0\,\tfrac{1}{\text{m}}$ ja $\tfrac{1}{r} = 50\,\tfrac{1}{\text{m}}$ arvot $B \approx 23\,\mu\text{T}$ ja $B \approx 132\,\mu\text{T}$.
**Kaava:** $k = \dfrac{\Delta B}{\Delta(1/r)}$ ja $k = \dfrac{\mu_0 I}{2\pi}$, joten $\mu_0 = \dfrac{2\pi k}{I}$
**Muunnokset:** $1\,\mu\text{T} = 10^{-6}\,\text{T}$, ja $\text{T} = \tfrac{\text{Vs}}{\text{m}^2}$, joten $\tfrac{\text{T} \cdot \text{m}}{\text{A}} = \tfrac{\text{Vs}}{\text{Am}}$.
**Sijoitus:** $k = \dfrac{132\,\mu\text{T} - 23\,\mu\text{T}}{50\,\tfrac{1}{\text{m}} - 5{,}0\,\tfrac{1}{\text{m}}} = \dfrac{109\,\mu\text{T}}{45\,\tfrac{1}{\text{m}}} = 2{,}422\,\mu\text{T} \cdot \text{m} = 2{,}422 \cdot 10^{-6}\,\text{T} \cdot \text{m}$, joten $\mu_0 = \dfrac{2\pi \cdot 2{,}422 \cdot 10^{-6}\,\text{T} \cdot \text{m}}{12{,}0\,\text{A}} = 1{,}268 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$
**Vastaus:** $\mu_0 \approx 1{,}27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$, kolme merkitsevää numeroa kuten virta $12{,}0\,\text{A}$ ja kuvaajalta luetut arvot.
**Järkevyys:** Taulukkoarvo on $4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} = 1{,}257 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$, joten ero on noin $0{,}9\,\%$. Lukemien vaihtelu noin $1\,\mu\text{T}$ on suurimmilla $\tfrac{1}{r}$-arvoilla alle $1\,\%$, joten ero on mittaustarkkuuden rajoissa.

### d)
**Annettu:** suoran kulmakerroin $k \approx 2{,}42\,\mu\text{T} \cdot \text{m}$ ja vakiotermi $b \approx 10{,}9\,\mu\text{T}$ (c-kohdan luetuista pisteistä: $23\,\mu\text{T} - 2{,}422\,\mu\text{T} \cdot \text{m} \cdot 5{,}0\,\tfrac{1}{\text{m}}$), etäisyys $r = 50\,\text{cm}$, johtimen pituus $2{,}0\,\text{m}$
**Kysytty:** mitä vakiotermi kertoo mittauksesta ja anturin lukema $50\,\text{cm}$:n päässä
**Periaate:** Johtimen oma kenttä on kääntäen verrannollinen etäisyyteen, joten vakiotermi on kenttää, joka ei riipu virrasta eikä etäisyydestä. Anturi pysyi samassa asennossa eikä sitä nollattu, joten sen lukemaan sisältyy Maan magneettikentän komponentti anturin suunnassa ja anturin oma nollakohta (luvut *Magneetit, magneettinen dipoli ja magneettikenttä* ja *Mittaaminen ja mittauksen luotettavuus*). Lukema kauempana saadaan sovitetun suoran yhtälöstä, mutta pitkän johtimen malli pätee vain, kun etäisyys on paljon pienempi kuin johtimen pituus.
**Kuvaajan lukeminen:** Suora leikkaa $B$-akselin noin arvossa $11\,\mu\text{T}$; luetuista pisteistä $b = 23\,\mu\text{T} - 2{,}422\,\mu\text{T} \cdot \text{m} \cdot 5{,}0\,\tfrac{1}{\text{m}} = 10{,}9\,\mu\text{T}$.
**Kaava:** $B = \dfrac{k}{r} + b$
**Muunnokset:** $50\,\text{cm} = 50 \cdot 0{,}01\,\text{m} = 0{,}50\,\text{m}$
**Sijoitus:** $B = \dfrac{2{,}422\,\mu\text{T} \cdot \text{m}}{0{,}50\,\text{m}} + 10{,}9\,\mu\text{T} = 4{,}84\,\mu\text{T} + 10{,}9\,\mu\text{T} = 15{,}7\,\mu\text{T}$
**Vastaus:** Vakiotermi noin $11\,\mu\text{T}$ on johtimen virrasta riippumaton vakiokenttä: Maan magneettikentän komponentti anturin suunnassa ja anturin nollakohdan siirtymä. Sen voi tarkistaa mittaamalla lukeman virta katkaistuna, jolloin anturin pitäisi näyttää noin $11\,\mu\text{T}$. Mallin mukaan anturi näyttäisi $50\,\text{cm}$:n päässä noin $16\,\mu\text{T}$, kaksi merkitsevää numeroa, koska tulos riippuu kuvaajalta luetusta vakiotermistä. Tulos on vain arvio, koska $50\,\text{cm}$ on mitatun alueen ($2$–$12\,\text{cm}$) ulkopuolella ja johtimen pituus $2{,}0\,\text{m}$ ei ole enää paljon suurempi kuin etäisyys, joten johtimen oma kenttä on hieman pienempi kuin $4{,}8\,\mu\text{T}$.
**Järkevyys:** Etelä-Suomessa Maan kentän vaakakomponentti on noin $14\,\mu\text{T}$, joten $11\,\mu\text{T}$:n komponentti anturin suunnassa on uskottava. Vakiotermin saa myös kahdesta mittauksesta: jos $B = \tfrac{k}{r} + b$, niin $b = 2B(4{,}0\,\text{cm}) - B(2{,}0\,\text{cm}) = 2 \cdot 72\,\mu\text{T} - 132\,\mu\text{T} = 12\,\mu\text{T}$, lähes sama.

### Yleisiä virheitä
- a-kohdassa pisteet yhdistetään murtoviivaksi tai päätellään kääntäen verrannollisuus pelkästä laskevasta käyrästä.
- b-kohdassa piirretään $B$ etäisyyden funktiona logaritmiasteikolla ilman perustelua tai pakotetaan suora origon kautta, jolloin kulmakerroin ja $\mu_0$ saadaan liian suuriksi.
- c-kohdassa unohdetaan muuntaa mikroteslat tesloiksi tai etäisyys metreiksi, jolloin tulos on kertaluokkia väärä.
- d-kohdassa vakiotermi selitetään satunnaisvirheellä; se nostaa kaikkia lukemia saman verran.

### Hyväksytään myös
- c-kohdassa sovitusohjelman kulmakerroin $2{,}42\,\mu\text{T} \cdot \text{m}$ ja $\mu_0 \approx 1{,}27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$.
- d-kohdassa johtimen oman kentän arvio $4{,}8\,\mu\text{T}$ ja toteamus, että lukema on noin $16\,\mu\text{T}$ vakiokentän kanssa.

## fy9-magnetismi-valo-s4

### a)
**Kysytty:** miten sateenkaari syntyy ja kummalla reunalla punainen on
**Periaate:** Taitekerroin riippuu aallonpituudesta (dispersio): vedessä violetin taitekerroin on suurin ja punaisen pienin. Sateenkaaressa valo taittuu pisaraan, heijastuu sen takapinnasta ja taittuu ulos (luku *Dispersio: prisma ja sateenkaari*).
**Mallivastaus:** Auringonvalo tulee pisaraan, taittuu sen etupinnassa, heijastuu pisaran takapinnasta ja taittuu uudelleen ulos. Koska veden taitekerroin on punaiselle $1{,}331$ ja violetille $1{,}343$, värit taittuvat eri määrän ja lähtevät pisarasta hieman eri suuntiin. Kirkkain valo lähtee punaisella noin $42^\circ$:n ja violetilla noin $40{,}6^\circ$:n kulmassa vastapisteen suuntaan nähden. Katsoja näkee punaista niistä pisaroista, jotka ovat $42^\circ$:n kulmassa, ja violettia hieman sisempänä olevista pisaroista. Siksi punainen on kaaren ulkoreunalla ja violetti sisäreunalla. Sateenkaaren kohdalla juhlavieraan väite pitää paikkansa: värit erottuvat, koska eri värit taittuvat vedessä eri määrän.

### b)
**Kysytty:** miten saippuakuplan värit syntyvät ja miksi ohuin kohta näyttää tummalta
**Periaate:** Ohuen kalvon kahdesta pinnasta heijastuneet aallot interferoivat. Kohtisuorassa tulossa niiden matkaero on $2nd$, ja aalto kääntyy, kun se heijastuu suuremman taitekertoimen ainetta vasten (luku *Ohuen kalvon interferenssi*).
**Mallivastaus:** Kupla on ohut saippuavesikalvo, jonka molemmin puolin on ilmaa. Osa valosta heijastuu kalvon ulkopinnasta ja osa sisäpinnasta, ja nämä aallot interferoivat. Niiden matkaero $2nd$ riippuu kalvon paksuudesta $d$: joillakin aallonpituuksilla aallot vahvistavat toisiaan ja toisilla heikentävät. Valkoisesta valosta jää jäljelle aallonpituuksien sekoitus, joka näkyy värinä, ja kun kalvon paksuus vaihtelee, väri vaihtuu raidoittain. Vain ulkopinnan heijastus kääntää aallon, koska valo heijastuu siinä ilmasta saippuaveteen. Juuri ennen puhkeamista kuplan yläosa on hyvin ohut, $2nd \approx 0$, joten heijastuneet aallot ovat lähes vastakkaisessa vaiheessa ja kumoavat toisensa kaikilla aallonpituuksilla, ja kohta näyttää tummalta. Kuplan kohdalla väite on väärä: värit syntyvät interferenssistä, eivät taittumisesta, ja väri riippuu kalvon paksuudesta.

### c)
**Kysytty:** miten CD-levy synnyttää värit, punaisen ja violetin ensimmäisen kertaluvun kulmat ja arvio väitteestä
**Periaate:** Tiheät, säännöllisin välein toistuvat urat toimivat heijastushilana. Vierekkäisistä urista heijastuneet aallot vahvistavat toisiaan suunnissa, joille $d\sin\theta = k\lambda$ (luku *Valon interferenssi ja diffraktio*).
**Mallivastaus:** CD-levyn pinnassa on spiraalina kulkeva ura, jonka vierekkäiset kierrokset ovat $1{,}6\,\mu\text{m}$:n päässä toisistaan. Jokainen ura heijastaa valoa, ja eri urista heijastuneet aallot vahvistavat toisiaan vain suunnissa, joissa niiden matkaero on kokonainen määrä aallonpituuksia. Kohtisuorassa tulossa ensimmäinen kertaluku on punaiselle $\sin\theta = \tfrac{650 \cdot 10^{-9}\,\text{m}}{1{,}6 \cdot 10^{-6}\,\text{m}} = 0{,}41$ eli $\theta \approx 24^\circ$ ja violetille $\sin\theta = \tfrac{400 \cdot 10^{-9}\,\text{m}}{1{,}6 \cdot 10^{-6}\,\text{m}} = 0{,}25$ eli $\theta \approx 14{,}5^\circ$. Punainen poikkeaa siis eniten, päinvastoin kuin pisarassa ja prismassa, mikä osoittaa, että värit syntyvät eri tavalla. Kokonaisuutena juhlavieraan väite on väärä. Se pitää paikkansa vain sateenkaaressa. Kuplan värit syntyvät kalvon kahden pinnan heijastusten interferenssistä ja CD-levyn värit monen uran heijastusten interferenssistä, eikä niissä tarvita taittumista.

### Yleisiä virheitä
- a-kohdassa sanotaan, että punainen taittuu eniten, koska sen aallonpituus on pisin; vedessä violetti taittuu eniten.
- b-kohdassa värit selitetään saippuan väriaineella tai taittumisella, tai unohdetaan heijastuksen käännös, jolloin ohuin kohta väitetään kirkkaaksi.
- c-kohdassa kulma lasketaan ilman sinin käänteisfunktiota tai sanotaan violetin poikkeavan hilassa eniten.

## fy9-magnetismi-valo-s5

### a)
**Annettu:** hilassa $N = 600$ viivaa millimetrillä, $L = 80{,}0\,\text{cm}$, $x_1 = 27{,}0\,\text{cm}$, $x_2 = 66{,}4\,\text{cm}$
**Kysytty:** laserin aallonpituus $\lambda$ kummastakin maksimista
**Periaate:** Hilan maksimit ovat suunnissa, joille $d\sin\theta = k\lambda$, ja hilavakio on viivavälin pituus (luku *Valon interferenssi ja diffraktio*). Kulma saadaan varjostimen suorakulmaisesta kolmiosta, $\tan\theta = \tfrac{x}{L}$. Sini ja tangentti ovat lähes yhtä suuret vain pienillä kulmilla, joten kulma lasketaan ensin tangentista ja vasta sitten sen sini.
**Kaava:** $d = \dfrac{1\,\text{mm}}{N}$, $\theta_k = \tan^{-1}\dfrac{x_k}{L}$ ja $\lambda = \dfrac{d\sin\theta_k}{k}$
**Muunnokset:** $d = \dfrac{1\,\text{mm}}{600} = \dfrac{1 \cdot 10^{-3}\,\text{m}}{600} = 1{,}667 \cdot 10^{-6}\,\text{m}$; etäisyyksien suhteessa yksiköt supistuvat, ja lopuksi $1\,\text{m} = 10^9\,\text{nm}$.
**Sijoitus:** $\tan\theta_1 = \dfrac{27{,}0\,\text{cm}}{80{,}0\,\text{cm}} = 0{,}3375$, joten $\theta_1 = 18{,}65^\circ$ ja $\lambda = 1{,}667 \cdot 10^{-6}\,\text{m} \cdot \sin 18{,}65^\circ = 1{,}667 \cdot 10^{-6}\,\text{m} \cdot 0{,}3198 = 533{,}0\,\text{nm}$. $\tan\theta_2 = \dfrac{66{,}4\,\text{cm}}{80{,}0\,\text{cm}} = 0{,}830$, joten $\theta_2 = 39{,}69^\circ$ ja $\lambda = \dfrac{1{,}667 \cdot 10^{-6}\,\text{m} \cdot 0{,}6386}{2} = 532{,}2\,\text{nm}$
**Vastaus:** Ensimmäisestä kertaluvusta $\lambda \approx 533\,\text{nm}$ ja toisesta $\lambda \approx 532\,\text{nm}$, kolme merkitsevää numeroa kuten etäisyydet.
**Järkevyys:** Molemmat kertaluvut antavat saman tuloksen, ja se on vihreän valon aallonpituus, kuten laserin väri kertoo. Kulma $\theta_2 \approx 40^\circ$ on niin suuri, että $\sin\theta_2 = 0{,}64$ ja $\tan\theta_2 = 0{,}83$ eroavat selvästi.

### b)
**Kysytty:** ovatko ryhmän johtopäätökset perusteltuja
**Periaate:** Pienen kulman oletus $\sin\theta \approx \tfrac{x}{L}$ pätee vain pienillä kulmilla. Tulosta verrataan valmistajan arvoon epävarmuuden avulla, ja maksimien määrää rajoittaa ehto $k\lambda < d$ (luvut *Valon interferenssi ja diffraktio* ja *Mittaaminen ja mittauksen luotettavuus*).
**Mallivastaus:** Kumpikaan johtopäätös ei ole perusteltu. Virhe on laskutavassa, ei laserissa. Pienen kulman oletus antaa ensimmäisestä kertaluvusta $\tfrac{1{,}667\,\mu\text{m} \cdot 0{,}270\,\text{m}}{0{,}800\,\text{m}} \approx 562\,\text{nm}$, noin $6\,\%$ liikaa, ja toisesta $692\,\text{nm}$, noin $30\,\%$ liikaa, koska ero tangentin ja sinin välillä kasvaa kulman kasvaessa. Oikein laskettuna tulos on $532$–$533\,\text{nm}$. Jos etäisyydet tunnetaan noin $0{,}3\,\text{cm}$:n tarkkuudella, toisen kertaluvun ääriarvot antavat noin $530$–$535\,\text{nm}$, joten tulos on sopusoinnussa valmistajan arvon $532\,\text{nm}$ kanssa. Lisäksi laser näytti vihreältä, mikä jo sulkee pois punaisen valon. Kolmas kertaluku on olemassa, koska $3\lambda = 1{,}60\,\mu\text{m} < d = 1{,}667\,\mu\text{m}$, mutta $\sin\theta_3 = 0{,}958$, $\theta_3 \approx 73^\circ$ ja maksimi on $x_3 = 0{,}800\,\text{m} \cdot \tan 73{,}3^\circ \approx 2{,}7\,\text{m}$:n päässä keskimaksimista. Se on todennäköisesti seinän reunan ulkopuolella tai niin himmeä, ettei sitä huomattu. Hila ei siis ole viallinen.

### c)
**Kysytty:** miten mittausta parannetaan
**Periaate:** Suhteellinen epävarmuus pienenee, kun mitattava etäisyys on suuri verrattuna sen lukemisen epävarmuuteen. Systemaattiset virheet, kuten vino asettelu, poistetaan mittaustavalla, ja tulos ilmoitetaan epävarmuuksineen (luvut *Mittaaminen ja mittauksen luotettavuus* ja *Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi*).
**Mallivastaus:** Mitataan keskimaksimin molemmin puolin olevien maksimien $+k$ ja $-k$ välinen etäisyys ja puolitetaan se. Kahden valopisteen välin mittaaminen on tarkempaa kuin keskimaksimin keskikohdan arvioiminen, ja jos etäisyydet eri puolille ovat yhtä suuret, säde osuu hilaan kohtisuoraan. Käytetään toista kertalukua, jonka $x$ on suuri, tai kasvatetaan etäisyyttä $L$, jotta lukemisen epävarmuus noin $0{,}3\,\text{cm}$ on pieni osa mitatusta etäisyydestä. Arvioidaan $\Delta x$ ja $\Delta L$, lasketaan aallonpituus niiden ääriarvoilla ja ilmoitetaan tulos muodossa $\lambda \pm \Delta\lambda$, esimerkiksi $(532 \pm 3)\,\text{nm}$, jotta sitä voi verrata valmistajan arvoon. Mittaus toistetaan, mieluiten eri henkilöiden lukemina, ja laskussa käytetään tangenttia eikä pienen kulman oletusta. Turvallisuus: lasersäteeseen ei katsota, eikä sitä suunnata kenenkään silmiin, eikä heijastavia esineitä jätetä säteen tielle.

### Yleisiä virheitä
- a-kohdassa käytetään $\sin\theta = \tfrac{x}{L}$ tai $\sin\theta = \tfrac{x}{\sqrt{x^2 + L^2}}$ unohtaen jakaa kertaluvulla.
- a-kohdassa hilavakioksi otetaan $600\,\text{mm}$ tai $\tfrac{1}{600}\,\text{m}$.
- b-kohdassa hyväksytään johtopäätös, koska laskettu luku ”näyttää punaiselta”, tai epävarmuutta ei verrata eroon.
- c-kohdassa ehdotetaan vain toistoja; ne eivät poista laskutavan systemaattista virhettä.

## fy9-magnetismi-valo-s6

### a)
**Annettu:** magneettivuon tiheys $B = 1{,}20\,\text{T}$, protonin massa $m = 1{,}673 \cdot 10^{-27}\,\text{kg}$ ja varaus $q = 1{,}602 \cdot 10^{-19}\,\text{C}$; nopeus kohtisuorassa kenttää vastaan
**Kysytty:** osoitus, että kierrosaika ei riipu vauhdista, ja jännitteen taajuus $f$
**Periaate:** Magneettinen voima $qvB$ on kohtisuorassa nopeutta vastaan, joten protoni on elektrodin sisällä tasaisessa ympyräliikkeessä, ja voima on sen keskeisvoima (luvut *Varatun hiukkasen liike sähkö- ja magneettikentässä* ja *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*). Kierroksella protoni kulkee ympyrän kehän $2\pi r$ (luku *Ympyrärata: jaksonaika ja ratanopeus*). Jännitteen suunnan on vaihduttava joka puolikierroksella, kun protoni ylittää raon, joten jännitteen taajuus on sama kuin kierrostaajuus.
**Kaava:** $qvB = \dfrac{mv^2}{r}$, joten $r = \dfrac{mv}{qB}$, ja $T = \dfrac{2\pi r}{v} = \dfrac{2\pi m}{qB}$; vauhti supistuu, ja $f = \dfrac{1}{T} = \dfrac{qB}{2\pi m}$
**Muunnokset:** Suureet ovat perusyksiköissä; lopuksi $1\,\text{MHz} = 10^6\,\text{Hz}$.
**Sijoitus:** $T = \dfrac{2\pi \cdot 1{,}673 \cdot 10^{-27}\,\text{kg}}{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}20\,\text{T}} = 5{,}468 \cdot 10^{-8}\,\text{s}$, joten $f = \dfrac{1}{5{,}468 \cdot 10^{-8}\,\text{s}} = 1{,}829 \cdot 10^{7}\,\text{Hz} = 18{,}29\,\text{MHz}$
**Vastaus:** Kierrosaika $T = \tfrac{2\pi m}{qB}$ ei riipu vauhdista eikä säteestä: nopeampi protoni kulkee suuremman ympyrän samassa ajassa. Jännitteen on vaihdeltava taajuudella $f \approx 18{,}3\,\text{MHz}$, kolme merkitsevää numeroa kuten magneettivuon tiheys $1{,}20\,\text{T}$.
**Järkevyys:** Yksiköt: $\tfrac{\text{kg}}{\text{C} \cdot \text{T}} = \tfrac{\text{kg}}{\text{C} \cdot \tfrac{\text{N}}{\text{A} \cdot \text{m}}} = \tfrac{\text{kg} \cdot \text{m}}{\text{N} \cdot \text{s}} = \text{s}$. Taajuus on radiotaajuusaluetta, kuten syklotronien kiihdytysjännitteillä.

### b)
**Annettu:** liike-energia $E_\text{k} = 8{,}0\,\text{MeV}$, $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$, $m$, $q$ ja $B$ kuten a-kohdassa
**Kysytty:** protonin vauhti $v$ ja radan säde $r$ ulos tullessa
**Periaate:** Klassisessa mekaniikassa liike-energia on $\tfrac12 mv^2$. Radan säde saadaan keskeisvoiman yhtälöstä kuten a-kohdassa (luku *Varatun hiukkasen liike sähkö- ja magneettikentässä*). Ehto on täytetty, jos vauhti jää selvästi valon nopeutta pienemmäksi.
**Kaava:** $v = \sqrt{\dfrac{2E_\text{k}}{m}}$ ja $r = \dfrac{mv}{qB}$
**Muunnokset:** $8{,}0\,\text{MeV} = 8{,}0 \cdot 10^6 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}282 \cdot 10^{-12}\,\text{J}$
**Sijoitus:** $v = \sqrt{\dfrac{2 \cdot 1{,}282 \cdot 10^{-12}\,\text{J}}{1{,}673 \cdot 10^{-27}\,\text{kg}}} = 3{,}914 \cdot 10^{7}\,\text{m/s}$ ja $r = \dfrac{1{,}673 \cdot 10^{-27}\,\text{kg} \cdot 3{,}914 \cdot 10^{7}\,\text{m/s}}{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}20\,\text{T}} = 0{,}3406\,\text{m}$
**Vastaus:** Protonin vauhti on $v \approx 3{,}9 \cdot 10^7\,\text{m/s}$ ja radan säde $r \approx 0{,}34\,\text{m}$, kaksi merkitsevää numeroa kuten energia $8{,}0\,\text{MeV}$.
**Järkevyys:** $\tfrac{v}{c} = \tfrac{3{,}914 \cdot 10^7\,\text{m/s}}{3{,}00 \cdot 10^8\,\text{m/s}} \approx 0{,}13$, alle viidesosa, joten klassinen malli on tehtävän ehdon mukaan riittävä. Elektrodien halkaisija noin $70\,\text{cm}$ sopii sairaalan laitteeseen.

### c)
**Annettu:** raon jännite $U = 50\,\text{kV}$ ylityksellä, kaksi ylitystä kierroksessa, $E_\text{k} = 8{,}0\,\text{MeV}$, $T = 5{,}468 \cdot 10^{-8}\,\text{s}$ (a-kohta)
**Kysytty:** kierrosten lukumäärä $n$ ja kiihdytyksen kesto $t$
**Periaate:** Magneettinen voima on kohtisuorassa nopeutta vastaan, joten se ei tee työtä eikä muuta vauhtia. Vain raon sähkökenttä tekee työtä: jokaisella ylityksellä protonin liike-energia kasvaa määrän $qU$ (luku *Potentiaalienergia ja potentiaali sähkökentässä*). Protoni ylittää raon kahdesti kierroksessa, ja kierrosaika pysyy samana koko kiihdytyksen ajan (a-kohta).
**Kaava:** $n = \dfrac{E_\text{k}}{2qU}$ ja $t = nT$
**Muunnokset:** Protonin varaus on alkeisvaraus, joten $qU = 50\,\text{keV} = 0{,}050\,\text{MeV}$; lopuksi $1\,\text{s} = 10^6\,\mu\text{s}$.
**Sijoitus:** $n = \dfrac{8{,}0\,\text{MeV}}{2 \cdot 0{,}050\,\text{MeV}} = 80$ ja $t = 80 \cdot 5{,}468 \cdot 10^{-8}\,\text{s} = 4{,}37 \cdot 10^{-6}\,\text{s} = 4{,}37\,\mu\text{s}$
**Vastaus:** Protoni tekee noin $80$ kierrosta, ja kiihdytys kestää noin $4{,}4\,\mu\text{s}$, kaksi merkitsevää numeroa kuten energia $8{,}0\,\text{MeV}$.
**Järkevyys:** Ilman magneettikenttää sama energia vaatisi $8{,}0\,\text{MV}$:n jännitteen; syklotroni saavuttaa sen $50\,\text{kV}$:n jännitteellä, koska sama rako käytetään $160$ kertaa. Kulkumatka on alle $80 \cdot 2\pi \cdot 0{,}34\,\text{m} \approx 170\,\text{m}$, joten lyhyt aika on uskottava.

### d)
**Annettu:** $v = 3{,}914 \cdot 10^{7}\,\text{m/s}$ ja $r = 0{,}3406\,\text{m}$ (b-kohta)
**Kysytty:** kiihtyvyys $a$ ja sen suunta ulos tultaessa
**Periaate:** Elektrodin sisällä protoni on tasaisessa ympyräliikkeessä, joten sen kiihtyvyys on normaalikiihtyvyys, joka osoittaa radan keskipisteeseen (luku *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*). Saman antaa Newtonin toinen laki magneettiselle voimalle.
**Kaava:** $a_\text{n} = \dfrac{v^2}{r}$, ja tarkistukseksi $a = \dfrac{qvB}{m}$
**Muunnokset:** Suureet ovat perusyksiköissä, joten muunnoksia ei tarvita.
**Sijoitus:** $a_\text{n} = \dfrac{(3{,}914 \cdot 10^{7}\,\text{m/s})^2}{0{,}3406\,\text{m}} = 4{,}498 \cdot 10^{15}\,\text{m/s}^2$
**Vastaus:** Kiihtyvyys on $a \approx 4{,}5 \cdot 10^{15}\,\text{m/s}^2$ ja osoittaa radan keskipisteeseen, kaksi merkitsevää numeroa kuten b-kohdan tulokset.
**Järkevyys:** $\tfrac{qvB}{m} = \tfrac{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 3{,}914 \cdot 10^{7}\,\text{m/s} \cdot 1{,}20\,\text{T}}{1{,}673 \cdot 10^{-27}\,\text{kg}} \approx 4{,}5 \cdot 10^{15}\,\text{m/s}^2$, sama tulos. Kiihtyvyys on valtava, koska protonin massa on hyvin pieni ja voima noin $7{,}5 \cdot 10^{-12}\,\text{N}$.

### Yleisiä virheitä
- a-kohdassa kierrosaika lasketaan erikseen jollekin vauhdille, eikä todeta, että vauhti supistuu.
- b-kohdassa megaelektronivoltteja ei muunneta jouleiksi tai käytetään elektronin massaa.
- c-kohdassa unohdetaan, että rako ylitetään kahdesti kierroksessa, jolloin kierroksia tulee $160$.
- d-kohdassa kiihtyvyyden sanotaan osoittavan nopeuden suuntaan tai kiihdyttävän protonia magneettikentässä.

### Hyväksytään myös
- a-kohdassa taajuuden laskeminen suoraan lausekkeesta $f = \tfrac{qB}{2\pi m}$.
- c-kohdassa vastaus $n = 80$ ilman desimaaleja, koska kierrosten määrä on kokonaisluku.
