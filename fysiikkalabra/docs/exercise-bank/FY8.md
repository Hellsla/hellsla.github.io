# FY8 Aine, säteily ja kvantittuminen: tehtäväpankin täydennys

Nyt 16 lukua × 12 tehtävää (5/4/3), kaikki laskuja (`calc`); aineisto-, kuvaaja-, käsite- ja kokeellisia tehtäviä ei ole. Moduulin aineistopainotus (Lauri 2026-11-04): valosähköilmiön mittausaineistot ja kuvaajat; emissio- ja absorptiospektrit; radioaktiivisen hajoamisen mittaussarjat ja puoliintumisajan määrittäminen; säteilymittaukset, annokset ja tilastollinen vaihtelu; ydinreaktioiden ja kvantti-ilmiöiden tulkinta kokeellisista havainnoista. De Broglien aallonpituutta ei käytetä missään tehtävässä (opettajan päätös 2026-11-03). Tilastot vain lähteellä ja vuodella (STUK-A263, 2020; Planck-satelliitti), muuten "malliaineisto". Tavoite 8/7/5.

Olemassa olevia kuvia, joita kuvaajatehtävät voivat käyttää uudelleen (`reuse: safe`, ei paljasta vastausta): `fy8-2/lamp-spectrum`, `fy8-3/levels-task`, `fy8-5/string`, `fy8-5/nodes`, `fy8-6/ryhma`, `fy8-7/tunnel`, `fy8-8/spectrum`, `fy8-9/pa-points`, `fy8-9/aktiivisuus`, `fy8-10/kayra-points`, `fy8-11/sidosenergia-luku`, `fy8-12/tuntematon`, `fy8-13/vaimennus`, `fy8-16/hubble-t`. `reveals`-kuvia ei käytetä tehtävän kuvana, jos ne antavat vastauksen. Muille aineistoille tehdään uudet kuvaajat tai taulukot (`"data"`).

### fy8-1 Valosähköinen ilmiö ja fotoni
P1. +3/+3/+2. Keskeinen YO-sisältö; luvussa ei yhtään aineistoa.
- Taso 1: monivalinta "kirkkaampi valo irrottaa nopeampia elektroneja" (intensiteetti vs. taajuus, vaihtoehdoilla aaltomallin tyypilliset virheet); lasku: rajataajuus ja rajan aallonpituus annetusta irrotustyöstä (kalium); lyhyt perustelu: miksi himmeä UV irrottaa elektroneja heti mutta kirkas punainen ei.
- Taso 2 (aineisto): taulukko $U_\text{s}$ (estojännite) eri aallonpituuksilla (malliaineisto, 5 pistettä, hajonta $\pm 0{,}02\,\text{V}$) → piirrä $U_\text{s}(f)$, sovita suora, lue $h/e$, $f_0$ ja irrotustyö. Kuvaajan tulkinta: kahden metallin $E_\text{k,max}(f)$ -suorat samassa kuvassa (kaksi suoraa, uusi kuvaaja) → mikä metalli, jolla on suurempi irrotustyö, ja miksi suorat ovat yhdensuuntaiset. Virheanalyysi: opiskelija lukee rajataajuuden kuvaajasta pystyakselin leikkauspisteestä.
- Taso 3: aineisto virta–jännite-käyrästä kahdella intensiteetillä (kyllästysvirta kaksinkertainen, $U_\text{s}$ sama) → fotonien lukumäärä sekunnissa valotehosta ja kyllästysvirrasta (kvanttisaanto, numeerinen tulos); perustelu: miksi estojännite ei muutu. (Kokeen sovitus 1/virran riippuvuudesta jätetty pois.)

### fy8-2 Spektrit paljastavat atomin energiatasot
P1. +3/+3/+2.
- Taso 1: monivalinta emissio vs. absorptio (kumpi on jatkuvan spektrin päällä tummina viivoina); lasku: kaasun absorptioviivan aallonpituudesta energiatilojen ero; lyhyt perustelu: miksi eri alkuaineilla on eri viivat.
- Taso 2 (aineisto): taulukko tuntemattoman lampun emissioviivoista (tarkoitukseen käy `fy8-2/lamp-spectrum`) ja vertailutaulukko alkuaineiden viivoista → tunnista alkuaine, laske yhden viivan fotonin energia. Auringon absorptiospektrin tummat viivat (taulukko, aallonpituudet, malliaineisto) → mitkä alkuaineet Auringon ilmakehässä. Kokeellinen: miten erotat kaasupurkausputken viivaspektrin hehkulampun spektristä spektroskoopilla ja miten kalibroit aallonpituusasteikon.
- Taso 3: energiatasoaineisto (malliatomi, mitatut viivat 5 kpl) → päättele tasokaavio ja ennusta yksi uusi viiva, numeerisesti; fluoresenssimittaus (virityspituus ja emissiopituus, taulukko) → Stokesin siirtymän energia ja häviön osuus. (Ilmastotehtävä jää valinnaiseen laatikkoon: CO₂:n absorptio $15\,\mu\text{m}$ on jo L3-02.)

### fy8-3 Vetyatomin energiatasot ja Bohrin malli
P2. +3/+3/+2.
- Taso 1: monivalinta mikä siirtymä antaa lyhimmän aallonpituuden; lasku: Lymanin sarjan pisin aallonpituus; lasku: ionisaatioenergia tilasta $n = 3$.
- Taso 2 (aineisto): taulukko mitatuista Balmerin viivoista (4 viivaa, aallonpituudet $\pm 0{,}5\,\text{nm}$) → päättele ylempi taso $n$ jokaiselle ja arvioi ionisaatioenergia sovittamalla $f$ vs. $1/n^2$. Absorptiospektri (`fy8-3/levels-task` + taulukko absorptiopituuksista) → mitkä siirtymät ovat sallittuja. Virheanalyysi: väite "elektroni kiertää ytimen radalla $n^2$ kertaa kauempana, joten fotonin energia on $n^2$ kertaa suurempi".
- Taso 3: tähtispektrin viivojen aallonpituudet (malliaineisto) → päättele vedyn viritystaso ja ionisaatioon tarvittava taajuus; hiukkasen siirtymän todennäköisyyden perustelu. (Energiatasojen johtaminen $E_n$ jätetty pois, koska arvot annetaan.)

### fy8-4 Valo ja elektroni aaltoina ja hiukkasina
P3. +3/+3/+2. De Broglie jätetty pois; aineistotehtävät rakennetaan fotoneista ja osumajakaumista.
- Taso 1: monivalinta "yksittäinen fotoni kaksoisraossa" (kulkeeko raosta toiseen vai molempiin); lasku: fotonien lukumäärä sekunnissa laserin tehosta; lyhyt perustelu: miksi Comptonin ilmiö vaatii hiukkasmallin.
- Taso 2 (aineisto): taulukko kaksoisrakokokeen osumamääristä ruudukossa ($N = 50, 500, 5000$ fotonia) → milloin juovat erottuvat, tilastollisen vaihtelun arviointi. Comptonin sironnan mittaus (taulukko: sirontakulma ja sironneen fotonin aallonpituus, 5 pistettä) → sovita $\Delta\lambda$ vs. $1 - \cos\theta$ ja lue vakio.
- Taso 3: yhdistelmä: laserin fotonivuo + osumalaskuri, jonka havaitsemishyötysuhde on 40 % → montako fotonia ilmaisimelle tulee, ja kuinka kauan kestää kerätä 5000 osumaa; perustelutehtävä: miksi kokeen tulos kaksoisraossa katoaa, kun mitataan rako.

### fy8-5 Aaltomekaaninen atomimalli ja orbitaalit
P3. +3/+3/+2. Luku on laadullinen (ei Schrödingerin yhtälöä), joten datatehtävät ovat osumajakaumia ja energia-aineistoja.
- Taso 1: monivalinta orbitaali vs. Bohrin rata; monivalinta todennäköisyystulkinta; elektronien lukumäärä alikuorella.
- Taso 2 (aineisto): taulukko elektronin paikkamittausten etäisyyksistä ytimestä (histogrammi, esim. 400 mittausta ja luokat $0{,}05\,\text{nm}$) → mikä etäisyys on yleisin, kuinka suuri osuus on alle $0{,}1\,\text{nm}$; seisova aalto kielellä (`fy8-5/string`) → montako solmua tilassa, perustelu. Virheanalyysi: "orbitaalin raja on seinä, jonka sisällä elektroni on koko ajan".
- Taso 3: aineisto kolmen alkuaineen ensimmäisistä ionisaatioenergioista (Li, Na, K; malliaineisto tai lähteellinen) → miksi energia pienenee ryhmässä alaspäin, perusteltu laadullisesti; kvanttitilojen lukumäärä ja täyttö argonille/kalsiumille (elektronikonfiguraatio ja ensimmäisen virityksen energia). (Numeerinen tulos: viritysfotonin aallonpituus annetusta energiaerosta.)

### fy8-6 LEDin valo ja Planckin vakion mittaaminen
P1. +3/+3/+2. Keskeinen kokeellinen luku; virheenarviointi lisätään.
- Taso 1: monivalinta miksi LED syttyy vasta kynnysjännitteellä; lasku: kynnysjännitteestä aallonpituus; lasku: $h$ yhdestä LEDistä.
- Taso 2 (aineisto): taulukko neljästä LEDistä ($\lambda$, $U_\text{k}$) → sovita suora $U_\text{k}(f)$ ja laske $h$; toinen ryhmä: virta–jännite-taulukko (10 pistettä, kynnys $\approx 1{,}85\,\text{V}$, punainen LED) → määritä $U_\text{k}$ lineaarisesta osasta. Kokeellinen: miten valitset LEDin huippuaallonpituuden spektrometrilla ja miksi LED ei ole yksivärinen. Virheanalyysi: kynnysjännite luettu virran alkuhetkestä (virta $0{,}1\,\text{mA}$ vs. $10\,\text{mA}$) → systemaattinen virhe.
- Taso 3: aineisto, jossa jännitemittarin nollapiste on $+0{,}05\,\text{V}$ pielessä (malliaineisto) → paljasta virhe suoran vakioterminä ja korjaa $h$; vertaa tulosta taulukkoarvoon, prosenttivirhe numeerisesti. Perustelu: miksi kynnysjännitteestä saatu $h$ on tyypillisesti hieman liian suuri.

### fy8-7 Laser ja kvanttirakenteet
P3. +3/+3/+2.
- Taso 1: monivalinta mikä erottaa stimuloidun emission spontaanista; lasku: laserin fotonivuo; monivalinta populaatioinversio.
- Taso 2 (aineisto): taulukko kvanttipisteen koosta ja emissioaallonpituudesta (malliaineisto, `fy8-7/qdots` on `reveals`, uusi taulukko) → päättele riippuvuus ja arvioi energia-aukko; laserdiodien taulukko ($\lambda$, teho, fotonivuo) → vertaile. Virheanalyysi: "laser lisää valon energiaa, koska yksi fotoni tuottaa kaksi".
- Taso 3: laserin hyötysuhteen mallinnus (pumpun teho $\to$ lasersäteilyn teho, fotonivuot, kvanttihyötysuhde numeerisesti); perustelu: miksi inversio vaatii vähintään kolme tasoa. (Tunneloituminen valinnaisena: ei datalaskuja.)

### fy8-8 Atomiydin ja radioaktiivinen hajoaminen
P2. +3/+3/+2.
- Taso 1: monivalinta mikä hajoaminen muuttaa $Z$:ta; hajoamisyhtälö: alfa ja beeta; lyhyt perustelu: miksi gammahajoamisessa $A$ ja $Z$ eivät muutu.
- Taso 2 (aineisto): nuklidikartan ote (taulukko, $Z$ ja $N$) → mikä hajoaminen kullekin ytimelle; gammaspektrin huiput (`fy8-8/spectrum` + taulukko lisähuipusta) → energiatasokaavio. Virheanalyysi: hajoamisyhtälön $A$ ja $Z$ eivät täsmää.
- Taso 3: hajoamissarja (taulukko tytärytimistä) → montako alfaa ja beetaa, numeerisesti; gammaspektristä päätelty ytimen tasokaavio ja yhden puuttuvan gammaviivan energia numeerisesti. (Viritystilan elinaika linjanleveydestä jätetty pois: epävarmuusperiaate ei kuulu kurssiin.)

### fy8-9 Hajoamislaki ja puoliintumisaika
P1. +3/+3/+2. Moduulin ydinaineisto; Lauri korostaa mittaussarjoja ja tilastollista vaihtelua.
- Taso 1: monivalinta "kahden puoliintumisajan jälkeen kaikki on hajonnut"; lasku: jäljellä oleva osuus $n$ puoliintumisajan jälkeen; lasku: aika, jolloin aktiivisuus on 10 % alkuarvosta.
- Taso 2 (aineisto): taulukko Ba-137m:n pulssimääristä (10 s jaksoissa, 0–400 s, tausta $\approx 8$ pulssia/10 s, hajonta $\pm\sqrt{N}$) → vähennä tausta, piirrä logaritmiasteikolla, lue $T_{1/2}$. `fy8-9/pa-points`-kuvaaja: lue puoliintumisaika kuvaajasta. Virheanalyysi: puoliintumisaika luettu ilman taustan vähennystä ja miksi se tuottaa liian pitkän ajan.
- Taso 3: kahden radionuklidin seoksen aktiivisuusaineisto (taulukko, kaksi eksponenttia, $T_{1/2} = 6{,}0\,\text{h}$ ja $T_{1/2} = 2{,}7\,\text{d}$) → erota komponentit lopusta alkuun, numeerinen $T_{1/2}$ molemmille; mallinnus: lääkeaine, jossa jodi-131 hajoaa fysikaalisesti ja poistuu myös biologisesti (efektiivinen puoliintumisaika numeerisesti). (K-40-ajoitus jätetty pois: tytärytimen kertymä vaatii haarautuvan hajoamisen käsittelyä.)

### fy8-10 Massavaje ja ytimen sidosenergia
P2. +3/+3/+2.
- Taso 1: monivalinta sidosenergia vs. massavaje; lasku: massavajeesta MeV; lasku: $E_\text{B}/A$.
- Taso 2 (aineisto): taulukko 8 nuklidin atomimassoista (u) → massavaje, $E_\text{B}$ ja $E_\text{B}/A$, järjestä; `fy8-10/kayra-points`: lue, missä on maksimi ja mitä se kertoo. Virheanalyysi: protonin ja neutronin massat laskettu vetyatomin massalla ilman elektroneja.
- Taso 3: reaktioenergia kolmella tavalla (massoista, sidosenergioista, kuvaajasta lukien) ja vertailu; arvioi Auringon massan menetys vuodessa tehosta (kertaus, uusi tilanne: tähti $L = 10^{28}\,\text{W}$).

### fy8-11 Fissio, fuusio ja ydinvoima
P2. +3/+3/+2.
- Taso 1: monivalinta moderaattorin tehtävä; monivalinta miksi fuusio vaatii korkean lämpötilan; lasku: yhden fission energia MeV:stä J:ksi.
- Taso 2 (aineisto): taulukko polttoainesauvan uraanipitoisuudesta ja ketjureaktion kasvukertoimesta ajan funktiona (malliaineisto) → onko reaktori alikriittinen/kriittinen; Suomen ydinvoimaloiden nettosähköteho (Fortum, TVO; lähteellinen, vuosi) → vuosituotanto kapasiteettikertoimella. Virheanalyysi: "fissio ei vapauta massaa, koska nukleonien lukumäärä säilyy".
- Taso 3: fission jätteen aktiivisuus ajan funktiona (aineisto taulukkona) → kuinka kauan jäähdytys tai loppusijoitus (Onkalo); polttoaineen kulutus vuodessa annetusta lämpöteholla ja hyötysuhteesta (numeerinen, yhdistää fy8-9).

### fy8-12 Ionisoiva säteily ja elimistö
P1. +3/+3/+2. Tilastollinen vaihtelu ja mittaus ovat luvun tärkein aineistoaihe.
- Taso 1: monivalinta kumpi suoja pysäyttää alfan ja beetan; lasku: pulssit minuutissa nollataustalla; lyhyt perustelu: miksi alfa on vaarallinen sisälle mutta ei ulkona.
- Taso 2 (aineisto): taulukko GM-laskurin pulssimääristä 10 s jaksoissa (20 mittausta, keskiarvo $\approx 48$, hajonta $\approx \sqrt{48}$) → keskiarvo, $\sqrt{N}$ ja suhteellinen epävarmuus; vaimennusmittaus eri lyijypaksuuksilla (taulukko, tausta mukana) → $d_{1/2}$. `fy8-12/tuntematon`: lue aine kuvaajasta. Kokeellinen: miten erotat beeta- ja gammasäteilyn suojilla.
- Taso 3: tunnista säteilylaji ja aine mittausaineistosta (paperi, alumiini, lyijy; taulukko) → perusteltu päätelmä ja numeerinen $d_{1/2}$; lähteen aktiivisuuden arvio pulssitaajuudesta ja ilmaisimen tilakulmasta (geometrinen hyötysuhde 1,5 %).

### fy8-13 Säteilyannos ja säteilyturvallisuus Suomessa
P1. +3/+3/+2. Lähteellinen aineisto: STUK-A263 (2020), suomalaisen keskimääräinen vuosiannos $5{,}9\,\text{mSv}$.
- Taso 1: monivalinta Gy vs. Sv; lasku: efektiivinen annos kudoksen painotuskertoimilla; lasku: annos annosnopeudesta ja ajasta.
- Taso 2 (aineisto): taulukko suomalaisen keskimääräisestä annoksesta lähteittäin (radon, luonnon gammasäteily, lääketieteelliset, ruoka, kosminen; STUK-A263, 2020) → osuudet ja kuinka suuri osuus on ihmisen vaikutettavissa; annosnopeuden etäisyysmittaus (taulukko, kolme etäisyyttä) → vahvista $1/r^2$-laki. `fy8-13/vaimennus`: lue betonin puoliintumispaksuus. Virheanalyysi: Sv ja Gy sekoitettu alfasäteilyssä.
- Taso 3: radonannos asunnossa: pitoisuus ($Bq/m^3$), oleskeluaika ja annoskerroin annettuna → vuosiannos ja vertailu STUKin viitearvoon; säteilytyöntekijän vuoron suunnittelu etäisyyden, ajan ja suojan yhdistelmänä (numeerinen: rajoittava aika).

### fy8-14 Säteily lääketieteessä ja teknologiassa
P2. +3/+3/+2.
- Taso 1: monivalinta miksi PET käyttää positronia; lasku: röntgenkuvan intensiteetti kudoskerroksen läpi; lyhyt perustelu: hoitoannoksen jako useaan suuntaan.
- Taso 2 (aineisto): taulukko eri tutkimusten efektiivisistä annoksista (STUK, lähteellä; vuosi mainittava) → vertaile taustasäteilyyn; merkkiaineen aktiivisuus potilaalla ajan funktiona (taulukko, $T_{1/2}$ ja biologinen poistuma) → efektiivinen puoliintumisaika. Virheanalyysi: suojalyijyn paksuus lasketaan käyttämällä väärää energiaa.
- Taso 3: kuvantamisen riskin ja hyödyn arviointi (annos, aktiivisuus ja kuvausaika; numeerinen tulos mSv); paksuusmittarin mittausaineisto (paperin paksuus vs. laskentataajuus, malliaineisto) → kalibrointisuora ja tuntemattoman paksuuden päättely.

### fy8-15 Standardimalli: perushiukkaset ja vuorovaikutukset
P3. +3/+3/+2. Datatehtävät ovat vähäisiä, koska luku on käsitteellinen; käytetään hiukkasreaktioiden taulukoita.
- Taso 1: monivalinta mikä vuorovaikutus välittyy fotonilla; varauksen laskeminen kvarkeista; monivalinta antihiukkanen.
- Taso 2 (aineisto): taulukko hiukkasten kvarkkikoostumuksista ja varauksista → tunnista, mikä on mahdollinen hadroni; reaktioluettelo (7 reaktiota, joista 3 kielletty varauksen/leptoniluvun säilymisen vuoksi) → kumpi säilyy. Virheanalyysi: "neutroni on hajoamaton, koska se on perushiukkanen".
- Taso 3: parinmuodostuksen kynnysenergia ja syntyneiden hiukkasten liike-energia annetusta fotonienergiasta (numeerinen, kertaus fy8-10); tulkitse bubble chamber -kuva kirjallisesti (kuvaus tekstinä: jäljet, kaareutuminen, säilymislait).

### fy8-16 Maailmankaikkeuden kehitys
P3. +3/+3/+2.
- Taso 1: monivalinta punasiirtymä vs. Doppler-ilmiö; lasku: punasiirtymästä nopeus; monivalinta mikä on kosminen taustasäteily.
- Taso 2 (aineisto): taulukko 9 galaksin etäisyydestä ja nopeudesta (malliaineisto, `fy8-16/hubble-t` toisena kuvana) → $H_0$ sovitus origon kautta, maailmankaikkeuden ikä $1/H_0$; Planck-satelliitti, vuosi mainittava (lähteellinen $H_0$). Virheanalyysi: "galaksit liikkuvat avaruudessa keskipisteestä poispäin".
- Taso 3: Hubblen lain ja taustasäteilyn yhdistelmä: lämpötilan ja aallonpituuden kehitys punasiirtymällä (numeerinen); pimeän aineen tulkinta pyörimiskäyrän aineistosta (taulukko: etäisyys ja ratanopeus; vertailu odotettuun laskevaan käyrään ja johtopäätös, ei painovoimalaskentaa).
