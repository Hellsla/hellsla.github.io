# FY6 Sähkö: tehtäväpankin täydennys

Nyt 16 lukua × 12 tehtävää (5/4/3), lähes kaikki laskuja (fy6-1:ssä ja fy6-2:ssa yksi sanallinen, muissa ei yhtään aineisto-, käsite- tai kokeellista tehtävää). Moduulin aineistopainotus (Lauri 2026-11-04): virtapiirien mittaustulokset ja kytkentäkaaviot; virran ja jännitteen riippuvuudet, ominaiskäyrät ja resistanssin määrittäminen; sähköteho, energiankulutus, komponenttien toiminta ja mittaustulosten tulkinta; virheellisten kytkentöjen ja mittausjärjestelyjen arviointi. Mittaustaulukot ovat malliaineistoa (realistinen hajonta, mittarin virheraja kerrottu), ellei lähdettä ja vuotta mainita. Sähköenergian hinnat ja kulutustilastot vain lähteellisinä (Energiavirasto, Tilastokeskus, Motiva, vuosi) tai malliaineistona. Figure-id:itä ei FY6:lle ole luettelossa (`docs/figures/catalog.json`), joten kuvaajat tehdään tehtäväkohtaisina. Tavoite 8/7/5.

### fy6-1 Virtapiiri, sähkövirta ja jännite
P1. +3/+3/+2. Luvussa vain laskuja, ei yhtään kytkentäkaaviotehtävää.
- Taso 1: monivalinta virran suunta (sopimus $+\to-$) vs. elektronien liike, väärät vaihtoehdot "virta kuluu lampussa" ja "elektronit liikkuvat valon nopeudella"; kytkentäkaavion symbolien tunnistus (monivalinta: mikä kaavio vastaa kuvattua piiriä); lasku: kuinka monta elektronia kulkee johtimen läpi, kun $I = 2{,}5\,\text{mA}$ ja $\Delta t = 1{,}0\,\text{min}$.
- Taso 2 (aineisto): taulukko (malliaineisto) lampun virran mittauksesta ajan funktiona 10 s:n välein, jolloin virta hiipuu (paristo kuluu) → varaus ajan mukaan kuvaajan pinta-alana ja keskivirta. Kuvaajan tulkinta: kaksi kytkentäkaaviota, joissa lamppu on piirretty väärin (ei suljettua piiriä / oikosulku) → päättele, palaako lamppu ja miksi. Kokeellinen: miten osoitat, ettei virta kulu lampussa (virta ennen ja jälkeen lampun on yhtä suuri), mittausjärjestely.
- Taso 3: akun purkautumisen mallinnus aineistosta ($U$ ja $I$ eri ajanhetkinä → energia $E = UIt$ summaamalla, numeerinen tulos Wh); perustelutehtävä: miksi sähkölaite toimii heti kytkimestä, vaikka yksittäisten elektronien ajautumisnopeus on millimetrejä sekunnissa.

### fy6-2 Mittaukset virtapiirissä
P1. +3/+3/+2. Moduulin mittausluku, kaikki neljä tavoiteaineistotyyppiä sopivat.
- Taso 1: monivalinta mittarien kytkentä (virtamittari sarjaan, jännitemittari rinnalle) kolmesta kytkentäkuvasta; monivalinta mittarin vaikutus piiriin (ihanteellisen virtamittarin resistanssi $\to 0$, jännitemittarin $\to \infty$); lasku: lukeman virheraja ja suhteellinen virhe annetusta valmistajan kaavasta.
- Taso 2 (aineisto): taulukko, jossa mittausarvot samalta komponentilta kolmella mittausalueella ja virherajat → valitse paras alue ja perustele. Virheellinen kytkentä: kolme kytkentäkuvaa (virtamittari rinnalle, jännitemittari sarjaan, mittari väärällä alueella) → mitä mittari näyttää ja mitä vahingoittuu. Toistomittaus: viisi lukemaa ($12{,}46$–$12{,}52\,\text{V}$) → keskiarvo ja epävarmuus $\Delta U$, onko tulos sopusoinnussa nimellisarvon kanssa.
- Taso 3: aineisto, jossa jännitemittarin sisäinen resistanssi $10\,\text{M}\Omega$ vääristää suuriresistanssista mittausta (jännitteenjakaja $1\,\text{M}\Omega + 1\,\text{M}\Omega$) → laske, paljonko mittari muuttaa jännitettä, ja arvioi sen vaikutus tulokseen; virheanalyysi: opiskelijan raportti, jossa $R = U : I$ on laskettu mittauksesta ilman mittarin vaikutusta ja virherajoja, mikä on korjattava.

### fy6-3 Resistanssi ja Ohmin laki
P1. +3/+3/+2. Luvun ydin: ominaiskäyrä, resistanssin määrittäminen.
- Taso 1: monivalinta ominaiskäyrän muodosta (suora = Ohmin laki pätee, ei "resistanssi on jännite jaettuna virralla riippumatta"); monivalinta resistiivisyys vs. resistanssi (kaksi saman metallin lankaa); lasku: virta vastuksen läpi, kun resistanssi muuttuu langan pituuden kaksinkertaistuessa.
- Taso 2 (aineisto): taulukko vastuksen $U$–$I$-mittauksesta (8 pistettä, hajonta ± yleismittarin virheraja) → sovita suora, lue $R$ kulmakertoimesta ja arvioi epävarmuus. Hehkulampun ominaiskäyrä taulukkona (5 pistettä, $R = U:I$ kasvaa) → näytä, ettei Ohmin laki päde, ja selitä lämpötilan avulla. Virheanalyysi: opiskelija laski resistanssin yhdestä mittauspisteestä ja toteaa "jännite 0 V → resistanssi 0".
- Taso 3: aineisto kolmesta komponentista (vastus, hehkulamppu, diodi) samaan $U$–$I$-koordinaatistoon → tunnista komponentit ja laske resistanssi (tai differentiaaliresistanssi arvona) työpisteessä $U = 1{,}5\,\text{V}$; kokeellisen tutkimuksen suunnittelu: miten selvität, riippuuko lankavastus lämpötilasta (muuttujat, mittausjärjestely, virheen lähteet). (Lämpötilakerroin ja $R(T)$-kaava jätetty pois: ei luvun kaavoissa, vain kvalitatiivinen yhteys.)

### fy6-4 Vastusten sarja- ja rinnankytkennät
P2. +3/+3/+2.
- Taso 1: monivalinta mikä kytkentä antaa pienimmän kokonaisresistanssin; monivalinta "lisäämällä rinnan vastus kokonaisresistanssi kasvaa" -virhekäsitys; lasku: tuntematon rinnan vastus, kun kokonaisresistanssi annettu.
- Taso 2 (aineisto): mittaustaulukko, jossa kolme vastusta mitattu erikseen, sarjassa ja rinnan (yleismittarin virheraja) → vertaa mitattua ja laskettua kokonaisresistanssia, onko ero virherajan sisällä. Kytkentäkaavio (figure): sekakytkentä ja kolmen mittarin lukemat → päättele kunkin vastuksen virta ja jännite sekä tunnista mittarilukemista kytkentävirhe (yksi vastus irti).
- Taso 3: aineistosta paljastuva kytkentävirhe: kuvattu piirilevy, jossa mittausten mukaan kokonaisresistanssi on $R = 180\,\Omega$ odotetun $125\,\Omega$:n sijaan → päättele, mikä vastus on kytketty väärin tai poikki, ja todista laskulla; yhdistelmätehtävä: valitse vakiosarjan (E12) vastuksista kaksi, joiden kytkentä antaa tarkimmin $470\,\Omega$ (numeerinen tulos ja virhe-%).

### fy6-5 Kirchhoffin lait ja potentiaali virtapiirissä
P1. +3/+3/+2.
- Taso 1: monivalinta Kirchhoffin virtalaki (haarapisteessä virta säilyy, ei kulu); monivalinta potentiaaliero vs. potentiaali (mitä tarkoittaa maan valinta nollatasoksi); lasku: potentiaali kohdassa $C$, kun piiri ja virta annettu.
- Taso 2 (aineisto): potentiaalikuvaaja sarjapiiristä (figure, kolme vastusta) → lue vastusten jännitteet, päättele resistanssien suhde ja laske virta. Taulukko haaroittuvan piirin virtamittauksista (neljä mittariarvoa, yksi ristiriitainen) → tunnista virheellinen lukema Kirchhoffin virtalailla. Kuvaajan tulkinta: miksi potentiaali ei muutu johtimen kohdalla.
- Taso 3: kahden silmukan piiri (kaksi lähdettä, kolme vastusta) → muodosta yhtälöryhmä Kirchhoffin laeilla ja ratkaise haaravirrat numeerisesti, tarkista energiataseella (lähteiden teho = vastusten teho); virheanalyysi: opiskelija on käynyt silmukan väärään suuntaan ja saanut virralle negatiivisen merkin, mitä se tarkoittaa.

### fy6-6 Sähköteho ja vastuksen lämpeneminen
P1. +3/+3/+2.
- Taso 1: monivalinta $P = U^2 : R$ vs. $P = RI^2$ (milloin kumpikin sopii: sarja vs. rinnan); lasku: suurin sallittu virta vastukselle, jonka nimellisteho on $0{,}25\,\text{W}$; lasku: tehon muutos, kun jännite kaksinkertaistuu.
- Taso 2 (aineisto): taulukko vastuksen mitatusta lämpenemisestä (jännite $U$, virta $I$, vastuksen pinnan lämpötila) → laske teho ja piirrä lämpötila teho-akselille, päättele riippuvuus ja tasapainon ehto. Hehkulampun $U$–$I$-aineisto → $P = UI$ jokaiselle pisteelle ja tehon riippuvuus jännitteestä (ei $\propto U^2$, miksi). Virheanalyysi: opiskelija väittää sarjaan kytketyistä lampuista "kirkkaampi lamppu kuluttaa vähemmän", korjaa.
- Taso 3: eri tehon vastukset sarjassa ja rinnan (kolme mittaustulosta tehosta eri kytkennöissä) → päättele tuntemattomat resistanssit ja laske, kumpi paahtimen vastus palaa ensin, kun jännite kasvaa 10 %; laadullinen perustelu: miksi pitkä ohut jatkojohto lämpenee mutta paksu ei (sama virta).

### fy6-7 Sähköenergia kotona
P2. +3/+3/+2. Luvussa jo yksi kuvaajatehtävä.
- Taso 1: monivalinta kW vs. kWh (väärät vaihtoehdot "kilowattitunti on teho"); lasku: laitteen kuukausikulutus ja hinta annetulla käytöllä; lasku: kuinka monta tuntia $1{,}0\,\text{kWh}$ kestää eri laitteilla.
- Taso 2 (aineisto): kotitalouden laitelista (teho, käyttöaika/vrk) → vuorokauden ja vuoden kulutus laitteittain, suurin kuluttaja ja säästökohde. Sähkömittarin lukemat 7 päivältä (malliaineisto, 5 merkitsevää numeroa) → vuorokausikulutus, keskiteho ja kustannus. Kokeellinen: miten mittaat jääkaapin vuosikulutuksen energiamittarilla ja mitkä tekijät vääristävät.
- Taso 3: aineisto sähkön tuntihinnasta ja tuntikulutuksesta yhden vuorokauden ajalta (malliaineisto tai Nord Pool / Energiavirasto, vuosi mainittu) → laske kokonaiskustannus ja hinta/kWh, arvioi säästö, jos lämminvesivaraajan lataus siirretään halvimmille tunneille; mallinnus: vanhan jääkaapin vaihdon takaisinmaksuaika energiamerkinnän kulutuksesta.

### fy6-8 Lähdejännite ja sisäinen resistanssi
P1. +3/+3/+2. Tavoiteaineiston ydin (sisäisen resistanssin määrittäminen kokeellisesti).
- Taso 1: monivalinta napajännite vs. lähdejännite (milloin ne ovat yhtä suuret); monivalinta oikosulku (mitä tapahtuu paristolle); lasku: oikosulkuvirta annetusta $\mathcal{E}$:stä ja $r$:stä.
- Taso 2 (aineisto): taulukko pariston napajännitteestä eri kuormavirroilla (6 pistettä, mittarin virheraja) → sovita suora $U = \mathcal{E} - rI$, lue $\mathcal{E}$ ja $r$ ja arvioi epävarmuus. Kuvaajan tulkinta: kaksi paristoa samaan $U$–$I$-koordinaatistoon → kumpi on parempi suurella virralla ja miksi. Kokeellinen/virheanalyysi: napajännite mitataan jännitemittarilla ilman kuormaa → mitä saadaan, miksi ei voi määrittää $r$:ää yhdellä mittauksella.
- Taso 3: uuden ja vanhan paristoryhmän vertailu aineistosta (tuoreen pariston $r$ ja ikääntyneen $r$ kasvaa) → laske, kuinka suuri osa teholla $P$ lämpenee paristossa itsessään ja mikä kuorma antaa maksimitehon ($R = r$, laskettu numeerisesti); virheanalyysi: opiskelijan mittaus, jossa jännitemittari on kytketty vastuksen jälkeen niin, että johtimen resistanssi sisältyy $r$:ään.

### fy6-9 Akut ja latauspiiri
P2. +3/+3/+2.
- Taso 1: monivalinta Ah vs. Wh (miksi varaus ei yksin kerro energiaa); monivalinta latausvirran merkki (virta kulkee akun sisällä $-\to+$); lasku: latausaika, kun kapasiteetti ja virta annettu.
- Taso 2 (aineisto): akun purkautumismittaus (taulukko: napajännite ajan funktiona vakiovirralla, malliaineisto litiumakulle) → kapasiteetti ($It$) ja energia ($\sum UI\Delta t$ tai pinta-ala), keskijännite. Latausvirran kuvaajan tulkinta: lataus vakiovirralla ja sen jälkeen vakiojännitteellä (figure) → varaus eri vaiheissa. Virheanalyysi: väite "akku täyttyy nopeammin, kun laturin jännite on paljon akun jännitettä suurempi" → mikä menee pieleen (sisäinen resistanssi, lämpeneminen).
- Taso 3: aineisto kahden eri akun purkautumiskäyristä eri virroilla (suuri virta → pienempi saatu kapasiteetti) → vertaa, laske hyötysuhde latauksessa ja purussa (mitattu syöttö vs. saatu energia, numeerinen tulos); perustelu: miksi pieni sisäinen resistanssi on tärkeä pikalatauksessa.

### fy6-10 Sähkövaraus ja Coulombin laki
P2. +3/+3/+2. Pistevarauksen kenttä vain kvalitatiivisesti.
- Taso 1: monivalinta varauksen säilyminen kappaleita hierottaessa; monivalinta Coulombin voiman suuruus, kun etäisyys kaksinkertaistuu (väärät: $\tfrac12$, $2$ kertaa); lasku: etäisyys, jolla voima on annettu.
- Taso 2 (aineisto): torsiovaa'an/mallimittaus: voima $F$ eri etäisyyksillä $r$ (6 pistettä, hajonta) → osoita $F \propto r^{-2}$ piirtämällä $F$ vs. $1 : r^2$ ja laske $\propto$ varaustulo. Kuvaajan tulkinta: voimakuvaajat kahdelle varausparille → päättele varausten suuruussuhde. Kokeellinen: miksi sähköstaattiset kokeet onnistuvat huonosti kosteana päivänä ja miten järjestelet mittauksen.
- Taso 3: kolmen varauksen suora (voimat vektoreina) → tasapainokohta ja sen perustelu (laskettu numeerisesti); laadullinen perustelu: miksi varattu kampa vetää neutraaleja paperinpaloja, mutta ei työnnä niitä pois.

### fy6-11 Homogeeninen sähkökenttä
P2. +3/+3/+2.
- Taso 1: monivalinta kenttäviivojen tulkinta (suunta, tiheys); monivalinta voima negatiiviseen varaukseen kentässä ($\overline{F} = q\overline{E}$ vastakkaissuuntainen); lasku: kentänvoimakkuus $E = U : d$ uuteen tilanteeseen.
- Taso 2 (aineisto): levykondensaattorin jännite–etäisyys-mittaus (taulukko: kun jännite kiinteä, $E$ lasketaan kuudelle etäisyydelle) tai kentän voimakkuus–kuormitus-aineisto → osoita $E = U : d$. Kuvaajan tulkinta: pisaran poikkeama vaakasuuntaisessa kentässä (figure) → päättele varauksen merkki ja suuruus. Kokeellinen: miten selvität, onko kenttä levyjen välissä homogeeninen (koevarauksen mittauspisteet).
- Taso 3: Millikanin koe mallilla (aineisto: viiden pisaran leijumisjännitteet, malliaineisto) → laske kunkin pisaran varaus ja päättele alkeisvaraus numeerisesti (varaukset ovat kokonaislukukertoja); laadullinen perustelu: miksi ilmanpuhdistin kerää hiukkasia ja mitä tapahtuu, kun jännite kasvaa.

### fy6-12 Potentiaalienergia ja potentiaali sähkökentässä
P3. +3/+3/+2.
- Taso 1: monivalinta positiivisen ja negatiivisen varauksen potentiaalienergian muutos kentän suuntaan liikuttaessa; monivalinta potentiaaliero vs. potentiaali; lasku: elektronin liike-energia eV:na tietyn jännitteen jälkeen.
- Taso 2 (aineisto): potentiaalin mittaus levyjen välissä (taulukko: etäisyys levystä, potentiaali, hajonta) → sovita, laske $E$ ja päättele levyjen jännite. Kuvaajan tulkinta: potentiaali $V(x)$ (figure) kahdelle erilaiselle tilanteelle → missä kenttä on voimakkain ja mihin suuntaan varaus kiihtyy. Virheanalyysi: opiskelija väittää positiivisen varauksen siirtyvän korkeampaan potentiaaliin "itsestään".
- Taso 3: elektronisuihkun kiihdytyksen ja poikkeutuksen mallinnus (kiihdytysjännite → nopeus, sitten poikkeutus levyparissa, numeerinen poikkeama); aineisto elektronien liike-energiamittauksesta vastajännitteellä (pysäytysjännite taulukkona → energiajakauma) → päättele liike-energia. (Pistevarauksen potentiaali $kq : r$ jätetty pois: ei luvun sisällössä, vain homogeeninen kenttä.)

### fy6-13 Kondensaattori ja sen energia
P2. +3/+3/+2. Ei kytkentöjä, ei eksponenttifunktiota.
- Taso 1: monivalinta kapasitanssi ei riipu $Q$:sta ja $U$:sta; monivalinta eristeen vaikutus (kun lähde kytkettynä vs. irrotettu); lasku: energia $E = \tfrac12 CU^2$ uudelle jännitteelle.
- Taso 2 (aineisto): kondensaattorin latausmittaus: $Q$ (laskettu mitatusta virrasta) eri jännitteillä (taulukko, 6 pistettä) → kapasitanssi kulmakertoimena ja energia pinta-alana. Kuvaajan tulkinta: lataus- ja purkautumiskäyrä kvalitatiivisesti (figure, jännite vs. aika) → missä virta on suurin ja mistä näkee. Virheanalyysi: "kondensaattoriin varastoituu varausta, joten sen netto­varaus on $Q$" → korjaa.
- Taso 3: kameran salamalaitteen mallinnus (aineisto: kapasitanssi, jännite, välähdyksen kesto, energiamittaus) → laske teho ja kokonaisenergia; vertaa kahta eristettä läpilyöntilujuuden ja kapasitanssin kannalta ja valitse (numeerinen tulos). Laadullinen: miksi sydäniskurin kondensaattoria ei saa koskea irrotettunakaan.

### fy6-14 Puolijohteet, diodi, LED ja aurinkokenno
P1. +3/+3/+2. Moduulin komponenttiluku, aineisto sopii hyvin.
- Taso 1: monivalinta diodin toimintasuunta (päästö- ja estosuunta); monivalinta miksi LED tarvitsee etuvastuksen; lasku: aurinkokennon hyötysuhde annetusta säteilytehosta ja sähkötehosta.
- Taso 2 (aineisto): kolmen eriväristen LEDien kynnysjännitteet taulukkona → päättele järjestys ja laske etuvastus; aurinkokennon $U$–$I$-kuvaaja eri kuormilla (taulukko, malliaineisto) → hae maksimiteho ja vastaava kuormitus. Virheanalyysi: LED on kytketty vastuksettomana 3,0 V:n paristoon ja palaa loppuun → selitä ominaiskäyrän avulla (virta kasvaa jyrkästi).
- Taso 3: aurinkopaneelin vuoden tuotannon mallinnus (aineisto: kuukausittainen säteilymäärä Ilmatieteen laitos, vuosi mainittu, tai malliaineisto) → paneelin tuotanto ja kulutus, omavaraisuusaste; diodin ominaiskäyrä taulukkona → kynnysjännite ja työpiste sarjavastuksella piirtämällä kuormasuora (numeerinen virta). (Puolijohteiden kidehilarakenne ja $\text{p}$–$\text{n}$-liitoksen mikrofysiikka jätetty pois: LOPS rajaa komponenttitasolle.)

### fy6-15 Sähköturvallisuus kotona ja työssä
P2. +3/+3/+2.
- Taso 1: monivalinta maadoituksen tarkoitus (vikavirran ohjaus); monivalinta suojausluokat (esim. luokka II); lasku: sulakkeen sallima suurin teho ryhmäjohdolle.
- Taso 2 (aineisto): taulukko kosketusvirran vaikutuksista (kynnysarvot, lähde mainittuna: esim. Tukes tai standardin IEC 60479 tyyppiset arvot) ja kehon resistanssi eri tilanteissa → laske virta ja arvioi riski jokaiselle. Ryhmäjohdon kuormituslista (laitteet, tehot) → mitkä yhdistelmät laukaisevat sulakkeen. Virheanalyysi: "sulake suojaa ihmistä sähköiskulta" → korjaa vikavirtasuojan ja sulakkeen ero.
- Taso 3: mallinnus: jatkojohdon lämpeneminen aineistosta (virta, johtimen poikkipinta, pituus, johtimen mitattu lämpötilanousu) → laske häviöteho $P = RI^2$ ja arvioi, milloin johto on vaarallinen; vikavirtasuojan laukeamisen perustelu aineistosta (vuotovirta mA, laukaisuraja 30 mA, numeerinen kehon virta). Laadullinen: askeljännite ja miksi oikea toiminta on pienet askeleet jalat yhdessä.

### fy6-16 Soveltava luku: sähköauto ja kodin sähköjärjestelmä
P3. +3/+3/+2. Soveltava luku, joka yhdistää modulin ideat; tehtävät uusissa arkitilanteissa.
- Taso 1: monivalinta kW vs. kWh latausasemaa ostettaessa; lasku: latausaika tehosta ja akun energiasta; lasku: kolmivaihelatauksen teho $P = 3UI$ ja latausaika.
- Taso 2 (aineisto): latauskäyrä (figure: teho ajan funktiona, tehon lasku akun täyttyessä) → energia pinta-alana ja keskiteho. Talon sähkönkulutus tunneittain ennen ja jälkeen latausaseman (malliaineisto) → huipputeho ja pääsulakkeen riittävyys; vertaa hintaa eri aikoina. Virheanalyysi: opiskelija laskee latausajan akun koko kapasiteetista ottamatta huomioon laturin hyötysuhdetta.
- Taso 3: sähköauton ja polttomoottoriauton käyttökustannukset vuodessa (aineisto: kulutus kWh/100 km ja l/100 km, hinnat malliaineistona tai lähteellisenä) → kustannusvertailu ja päästövertailu; kodin sähköjärjestelmän mitoitusmalli (laitelista, pääsulake, latausvirran rajoitus, kaapelin häviöteho) → suurin sallittu latausvirta (numeerinen) ja perustelu. Laadullinen: miksi latausteho kannattaa rajoittaa illalla.
