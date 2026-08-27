/* ===============================================================
   Käsitekortit – sisältötiedosto
   ---------------------------------------------------------------
   Muoto:
   { id:"FY3", nimi:"Energia ja lämpö", aiheet:[
       { nimi:"Lämpö", kortit:[
           ["Käsite", "Määritelmä"],
           ...
       ]}
   ]}
   Ohje uusien korttien tekemiseen: KORTTIOHJE.md
   =============================================================== */
/* ---------------------------------------------------------------
   Käsitekortit – sisältö
   Muoto: [käsite, määritelmä]
----------------------------------------------------------------*/
window.KORTIT = [
{ id:"FY1", nimi:"Fysiikka luonnontieteenä", aiheet:[
  { nimi:"Fysiikka ja tutkimusmenetelmä", kortit:[
    ["Fysiikka","Kokeellinen luonnontiede, joka tutkii luonnon perusilmiöitä, rakenteita ja niitä kuvaavia lainalaisuuksia."],
    ["Empiirinen tiede","Tieto perustuu havaintoihin, mittauksiin ja kokeisiin."],
    ["Luonnontieteellinen menetelmä","Havaintoja, oletuksia, kokeita ja malleja yhdistävä tapa rakentaa luotettavaa tietoa."],
    ["Hypoteesi","Perusteltu oletus, jota voidaan testata kokeellisesti."],
    ["Fysiikan teoria","Laaja selityskokonaisuus, joka yhdistää havaintoja ja mahdollistaa uusien ilmiöiden ennustamisen."],
    ["Malli","Yksinkertaistettu kuvaus todellisuudesta, jolla selitetään ilmiöitä tai tehdään ennusteita."],
    ["Pätevyysalue","Olosuhteet ja rajat, joissa mallia voidaan käyttää luotettavasti."]
  ]},
  { nimi:"Mittaaminen ja virheet", kortit:[
    ["Suure","Mitattava ominaisuus, kuten pituus, massa tai aika."],
    ["Yksikkö","Sovittu vertailuarvo, jonka avulla mitattu ominaisuus ilmaistaan."],
    ["Mittaustulos","Lukuarvon ja mittayksikön muodostama suureen arvo."],
    ["Mittausvirhe","Mitatun arvon poikkeama suureen todellisesta arvosta."],
    ["Satunnainen virhe","Vaihteleva poikkeama, jonka vaikutusta voidaan pienentää toistamalla mittaus ja laskemalla keskiarvo."],
    ["Systemaattinen virhe","Samaan suuntaan vaikuttava poikkeama, jonka syynä voi olla viallinen laite tai menetelmä."],
    ["Karkea virhe","Selvä poikkeama, joka syntyy esimerkiksi lukuvirheestä, väärästä kirjauksesta tai laitteen virheellisestä käytöstä."],
    ["Merkitsevät numerot","Luvun numerot, jotka kuvaavat mittaustuloksen käytettävissä olevaa tarkkuutta."],
    ["Mittalaitteen tarkkuus","Kertoo, kuinka pieniä muutoksia mittavälineellä voidaan luotettavasti havaita."]
  ]},
  { nimi:"SI-järjestelmä ja suuruusluokat", kortit:[
    ["SI-järjestelmä","Kansainvälisesti sovittu mittayksikkökokonaisuus, jonka seitsemästä perusyksiköstä muut yksiköt muodostetaan."],
    ["Perussuure","Yksi seitsemästä perustaksi valitusta mitattavasta ominaisuudesta, kuten pituus, massa tai aika."],
    ["Perusyksikkö","Perustaksi valitulle suureelle sovittu yksikkö, kuten metri, kilogramma tai sekunti."],
    ["Johdannaisyksikkö","Perusyksiköistä muodostettu yhdistelmä, kuten nopeuden m/s tai voiman N."],
    ["Kerrannaisyksikkö","Etuliitteen avulla muodostettu käytännöllinen yksikkö hyvin suurille tai pienille arvoille."],
    ["Etuliite","Yksikön edessä oleva merkintä kertoo kymmenpotenssikertoimen, kuten kilo 10³ tai milli 10⁻³."],
    ["Kymmenpotenssi","Muoto 10ⁿ helpottaa erittäin suurten ja pienten lukujen kirjoittamista ja vertailua."],
    ["Suuruusluokka","Kohteen kokoa kuvataan sopivan kymmenen potenssin avulla."]
  ]},
  { nimi:"Maailmankaikkeuden perusrakenteet", kortit:[
    ["Perushiukkanen","Aineen pienimpiä tunnettuja rakenneosia, joihin kuuluvat kvarkit ja leptonit."],
    ["Kvarkki","Protonien ja neutronien rakenneosa, joita näkyvässä aineessa ovat erityisesti ylös- ja alas-kvarkit."],
    ["Leptoni","Perushiukkasten ryhmä, johon esimerkiksi elektroni kuuluu."],
    ["Protoni","Positiivisesti varautunut atomin ytimen rakenneosa, joka koostuu kvarkeista."],
    ["Neutroni","Sähköisesti neutraali atomin ytimen rakenneosa, joka koostuu kvarkeista."],
    ["Atomin ydin","Tiivis keskiosa, jossa protonit ja neutronit sijaitsevat."],
    ["Atomi","Ytimen ja sitä ympäröivien elektronien muodostama aineen rakenneosa."],
    ["Molekyyli","Kahden tai useamman atomin muodostama sitoutunut kokonaisuus."],
    ["Aurinkokunta","Tähti ja sitä kiertävät planeetat, pienkappaleet sekä muu aine."],
    ["Galaksi","Valtava tähtien, kaasun, pölyn ja muun aineen gravitaation sitoma järjestelmä."],
    ["Galaksijoukko","Useiden galaksien gravitaation sitoma suuri rakenne."]
  ]},
  { nimi:"Avaruus ja maailmankaikkeuden kehitys", kortit:[
    ["Alkuräjähdys","Malli, jonka mukaan aika ja avaruus kehittyivät hyvin kuumasta ja tiheästä alkutilasta."],
    ["Maailmankaikkeuden laajeneminen","Galaksien keskimääräiset etäisyydet kasvavat ajan kuluessa."],
    ["Punasiirtymä","Kaukaisen kohteen spektriviivat siirtyvät pidemmille aallonpituuksille, mikä kertoo sen etääntymisestä."],
    ["Eksoplaneetta","Aurinkokunnan ulkopuolella toista tähteä kiertävä planeetta."],
    ["Punainen jättiläinen","Kehitysvaihe, jossa tähti laajenee vedyn vähetessä ja raskaampien ytimien fuusioiden alkaessa."],
    ["Valkoinen kääpiö","Keskikokoisen tähden jäljelle jäänyt tiivis ja kuuma ydin, joka vähitellen jäähtyy."],
    ["Neutronitähti","Raskaan tähden luhistumisessa syntyvä erittäin tiheä jäännös, joka koostuu pääosin neutroneista."],
    ["Musta aukko","Erittäin tiheä massakeskittymä, jonka gravitaatio on niin voimakas, ettei valokaan pääse pois."]
  ]},
  { nimi:"Mallintaminen ja kuvaajat", kortit:[
    ["Fysikaalinen malli","Mittauksiin perustuva yksinkertaistus, joka kuvaa luonnon ilmiötä tai rakennetta."],
    ["Graafinen malli","Suureiden välinen riippuvuus esitetään koordinaatiston kuvaajana."],
    ["Matemaattinen malli","Suureiden välinen riippuvuus esitetään yhtälön avulla."],
    ["Kvantitatiivinen malli","Lukuarvoihin perustuva kuvaus, jonka avulla voidaan tehdä numeerisia ennusteita."],
    ["Lineaarinen malli","Tasaista muutosta kuvaava suora, jonka kulmakerroin pysyy vakiona."],
    ["Suoran sovite","Mittauspisteisiin asetettu suora, joka kuvaa aineiston yleistä riippuvuutta."],
    ["Kulmakerroin","Pystyakselin suureen muutos jaetaan vaaka-akselin suureen muutoksella."],
    ["Fysikaalinen kulmakerroin","Kuvaajan kaltevuus tulkitaan suureeksi yksiköineen ja ilmiöön liittyvine merkityksineen."],
    ["Interpolointi","Mallia käytetään arvon arvioimiseen mitattujen pisteiden väliltä."],
    ["Ekstrapolointi","Mallia jatketaan mittausalueen ulkopuolelle, jolloin ennuste on yleensä epävarmempi."]
  ]},
  { nimi:"Tiheys ja liikeilmiöt", kortit:[
    ["Tiheys","Kertoo, kuinka suuri massa aineella on tilavuusyksikköä kohti; ρ = m/V."],
    ["Suoraan verrannollisuus","Toisen suureen kaksinkertaistuessa myös toinen kaksinkertaistuu, ja kuvaaja kulkee origon kautta."],
    ["Paikka","Kertoo kappaleen sijainnin valitussa koordinaatistossa tiettynä hetkenä."],
    ["Tasainen liike","Paikka muuttuu yhtä paljon yhtä pitkissä aikaväleissä."],
    ["Nopeus","Kertoo paikan muutoksen aikayksikössä ja liikkeen suunnan."],
    ["Keskinopeus","Koko siirtymä jaetaan siihen kuluneella ajalla."],
    ["Kiihtyvyys","Kertoo nopeuden muutoksen aikayksikössä; a = Δv/Δt."],
    ["Vapaa putoaminen","Liike, jossa ilmanvastus sivuutetaan ja kappaleeseen vaikuttaa vain painovoima."],
    ["Putoamiskiihtyvyys","Maan lähellä nopeus muuttuu noin 9,81 m/s joka sekunti; g ≈ 9,81 m/s²."]
  ]},
  { nimi:"Kokeellinen tutkimus", kortit:[
    ["Tutkimuskysymys","Täsmällinen kysymys, johon tutkimuksella pyritään vastaamaan."],
    ["Koesuunnitelma","Etukäteen laadittu kuvaus mittauksista, välineistä ja tutkimuksen toteutuksesta."],
    ["Mittaussarja","Samasta ilmiöstä järjestelmällisesti kerätty joukko mittaustuloksia."],
    ["Toistettavuus","Hyvin kuvattu koe voidaan tehdä uudelleen ja saada samansuuntaisia tuloksia."],
    ["Mittausaineisto","Kokeessa kerätyt arvot, havainnot, kuvat tai videot, joita analysoidaan."],
    ["Tulosten analyysi","Aineistoa käsitellään laskuilla ja kuvaajilla riippuvuuksien löytämiseksi."],
    ["Johtopäätös","Tuloksista tehty perusteltu vastaus tutkimuskysymykseen."],
    ["Virhelähde","Tekijä, joka voi aiheuttaa mittaustulokseen poikkeamaa tai epävarmuutta."],
    ["Luotettavuus","Arvio siitä, kuinka hyvin menetelmä ja tulokset tukevat tehtyä päätelmää."],
    ["Tutkimusraportti","Kirjallinen kuvaus tutkimuskysymyksestä, menetelmästä, tuloksista, johtopäätöksistä ja arvioinnista."]
  ]},
  { nimi:"Tiedonhankinta", kortit:[
    ["Tiedonhankinta","Luotettavan tiedon etsimistä esimerkiksi tutkimuksista, oppikirjoista, tietokannoista ja asiantuntijalähteistä."],
    ["Tiedontuottaja","Tahon tausta ja tarkoitus vaikuttavat siihen, miten sen julkaisemaa tietoa kannattaa arvioida."],
    ["Lähdekritiikki","Lähteen luotettavuutta arvioidaan tekijän, perustelujen, ajantasaisuuden ja muiden lähteiden avulla."],
    ["Aineisto","Tutkittava teksti, kuva, taulukko, kuvaaja tai muu tietolähde, josta tehdään päätelmiä."],
    ["Objektiivisuus","Tavoite kuvata havaintoja riippumatta tutkijan henkilökohtaisista mielipiteistä."]
  ]}
]},

{ id:"FY2", nimi:"Fysiikka, ympäristö ja yhteiskunta", aiheet:[
  { nimi:"Energia ympäristössä ja yhteiskunnassa", kortit:[
    ["Energialähde","Aine tai ilmiö, jota hyödynnetään käyttökelpoisen energian tuottamiseen."],
    ["Uusiutuva energialähde","Luonnonvara tai ilmiö, jota syntyy jatkuvasti lisää ihmisen käytön kannalta riittävän nopeasti."],
    ["Uusiutumaton energialähde","Luonnonvara, jota on rajallinen määrä eikä muodostu nopeasti lisää."],
    ["Hiilineutraali energialähde","Sen käyttö ei lisää ilmakehän kasvihuonekaasujen pitoisuutta pitkällä aikavälillä."],
    ["Säteilyenergia","Auringosta Maahan kulkeutuva energiamuoto, joka mahdollistaa suuren osan maapallon energiavirroista."],
    ["Infrapunasäteily","Näkyvää valoa pitkäaaltoisempaa sähkömagneettista säteilyä, jota lämmin maanpinta lähettää."],
    ["Absorptio","Säteily imeytyy aineeseen ja sen kuljettama energia siirtyy aineeseen."],
    ["Heijastuminen","Säteily muuttaa pinnalla suuntaansa eikä sen energia absorboidu pintaan."]
  ]},
  { nimi:"Ilmastonmuutos", kortit:[
    ["Kasvihuoneilmiö","Ilmakehän kaasut vähentävät Maan lähettämän lämpösäteilyn pääsyä suoraan avaruuteen."],
    ["Kasvihuonekaasu","Ilmakehän kaasu, joka absorboi Maan lähettämää infrapunasäteilyä."],
    ["Hiilidioksidi","Kasvihuonekaasu, jonka pitoisuutta fossiilisten polttoaineiden käyttö lisää."],
    ["Metaani","Voimakas kasvihuonekaasu, jota vapautuu esimerkiksi maataloudessa ja fossiilisten polttoaineiden tuotannossa."],
    ["Ilmastonmuutos","Maapallon ilmaston pitkäaikainen muutos, jonka nykyistä lämpenemistä ihmisen kasvihuonekaasupäästöt voimistavat."],
    ["Hiilinielu","Järjestelmä, joka sitoo ilmakehästä hiilidioksidia enemmän kuin vapauttaa sitä."],
    ["Takaisinkytkentä","Muutos käynnistää vaikutuksen, joka voi vahvistaa tai heikentää alkuperäistä muutosta."],
    ["Päästövähennys","Kasvihuonekaasujen vapautumista ilmakehään pienennetään esimerkiksi muuttamalla energiantuotantoa ja kulutusta."]
  ]},
  { nimi:"Energia ja energialajit", kortit:[
    ["Energia","Fysiikan keskeinen suure, joka säilyy kaikissa ilmiöissä mutta voi siirtyä ja muuntua."],
    ["Joule","SI-järjestelmän energian yksikkö."],
    ["Energialaji","Tapa kuvata, missä muodossa energia esiintyy tai varastoituu."],
    ["Liike-energia","Kappaleella on tätä liikkeensä vuoksi, ja määrä kasvaa massan tai nopeuden kasvaessa."],
    ["Potentiaalienergia","Vuorovaikutukseen liittyvä varastoitunut energiamuoto, jonka määrä riippuu kappaleiden asemasta."],
    ["Mekaaninen energia","Liike-energian ja potentiaalienergian muodostama kokonaisuus."],
    ["Kemiallinen energia","Atomien ja molekyylien vuorovaikutuksiin varastoitunut energiamuoto, jota vapautuu esimerkiksi palamisessa."],
    ["Ydinenergia","Atomiytimien vuorovaikutuksiin liittyvä energiamuoto, jota vapautuu ydinreaktioissa."],
    ["Sähköenergia","Sähköisiin vuorovaikutuksiin liittyvä energiamuoto, jota on helppo siirtää sähköverkossa."],
    ["Sisäenergia","Aineen rakenneosasten liikkeeseen ja vuorovaikutuksiin liittyvä energiamuoto."]
  ]},
  { nimi:"Energian säilyminen", kortit:[
    ["Energian säilymislaki","Energiaa ei synny eikä häviä, vaan sitä voi siirtyä tai muuntua muodosta toiseen."],
    ["Energian muuntuminen","Yhden energialajin määrä pienenee samalla kun jonkin toisen määrä kasvaa."],
    ["Energian siirtyminen","Energia kulkee kohteesta tai systeemistä toiseen muuttamatta säilymisen periaatetta."],
    ["Energiakaavio","Esitys, jolla havainnollistetaan energialajeja sekä niiden muuntumista ja säilymistä."],
    ["Lämpö","Energiaa, joka siirtyy lämpötilaeron vuoksi kuumemmasta kohteesta kylmempään."],
    ["Hukkaenergia","Energiaa, joka muuntuu laitteen varsinaisen käyttötarkoituksen kannalta hyödyttömään muotoon."],
    ["Hyötyenergia","Se osa laitteen ottamasta energiasta, joka saadaan haluttuun tarkoitukseen."]
  ]},
  { nimi:"Teho ja energiankulutus", kortit:[
    ["Teho","Kertoo, kuinka nopeasti energiaa siirtyy tai muuntuu; P = ΔE/Δt."],
    ["Watti","SI-järjestelmän tehon yksikkö, joka vastaa yhtä joulea sekunnissa."],
    ["Ottoteho","Kertoo, kuinka nopeasti laite ottaa energiaa energialähteestään."],
    ["Antoteho","Kertoo, kuinka nopeasti laite siirtää energiaa haluttuun käyttötarkoitukseen."],
    ["Energiankulutus","Tietyssä ajassa käytetty energiamäärä voidaan laskea tehon avulla; E = PΔt."],
    ["Kilowattitunti","Energiamäärä, joka siirtyy yhden kilowatin teholla yhden tunnin aikana."],
    ["Arvokilpi","Laitteen merkintä, josta voidaan lukea esimerkiksi sen sähköverkosta ottama teho."],
    ["Sähkön hinta","Käytetyn sähköenergian kustannus saadaan kertomalla kilowattitunnit energian yksikköhinnalla."]
  ]},
  { nimi:"Hyötysuhde ja lämpöarvo", kortit:[
    ["Hyötysuhde","Kertoo, kuinka suuri osa otetusta energiasta saadaan hyödyksi; η = Eₐ/Eₒ."],
    ["Tehohyötysuhde","Voidaan laskea anto- ja ottotehon suhteena; η = Pₐ/Pₒ."],
    ["Ottoenergia","Kokonaisenergiamäärä, jonka laite ottaa toimintaansa varten."],
    ["Antoenergia","Laitteen varsinaiseen tarkoitukseen siirtämä tai muuntama energiamäärä."],
    ["Siirtohäviö","Energian siirrossa osa energiasta muuntuu hyödyntämättömään muotoon, yleensä lämmöksi."],
    ["Lämpöarvo","Kertoo täydellisessä palamisessa vapautuvan energian polttoaineen massayksikköä kohti."],
    ["Palamisenergia","Polttoaineesta vapautuva määrä voidaan laskea massan ja lämpöarvon avulla; E = Hm."],
    ["Energiatehokkuus","Haluttu hyöty saavutetaan mahdollisimman pienellä energian kulutuksella ja vähäisillä häviöillä."]
  ]},
  { nimi:"Energiantuotanto", kortit:[
    ["Energiantuotanto","Luonnossa olevan energian muuntamista ihmisille käyttökelpoiseen muotoon, kuten sähköksi tai lämmöksi."],
    ["Voimalaitos","Tuotantolaitos, jossa energialähteen energiaa muunnetaan sähköksi, lämmöksi tai molemmiksi."],
    ["Generaattori","Laite, joka muuntaa pyörimisliikkeen energiaa sähköenergiaksi."],
    ["Turbiini","Virtaava vesi, ilma tai höyry saa tämän laitteen pyörimään ja käyttämään generaattoria."],
    ["Lämpövoimalaitos","Lämpöenergiaa käytetään höyryn tuottamiseen, joka pyörittää turbiinia ja generaattoria."],
    ["Lauhdutin","Jäähdyttää turbiinista tulevan höyryn takaisin vedeksi ja siirtää samalla lämpöä ympäristöön."],
    ["Yhteistuotanto","Samassa laitoksessa tuotetaan sekä sähköä että hyödynnettävää lämpöä, jolloin hyötysuhde paranee."],
    ["Kaukolämpö","Keskitetysti tuotettua lämpöenergiaa siirretään kuuman veden avulla rakennusten lämmitykseen."],
    ["Lauhdutusvoima","Sähköntuotantoa, jossa turbiinin jälkeen jäävää lämpöä ei yleensä hyödynnetä kaukolämpönä."]
  ]},
  { nimi:"Energiantuotantotavat", kortit:[
    ["Aurinkovoima","Auringon säteilyenergiaa muunnetaan esimerkiksi aurinkopaneelissa suoraan sähköenergiaksi."],
    ["Tuulivoima","Ilman liike-energia pyörittää turbiinia ja generaattoria, joka tuottaa sähköä."],
    ["Vesivoima","Veden potentiaali- ja liike-energiaa muunnetaan turbiinin ja generaattorin avulla sähköksi."],
    ["Bioenergia","Eloperäiseen aineeseen sitoutunutta kemiallista energiaa hyödynnetään esimerkiksi polttamalla."],
    ["Fossiiliset polttoaineet","Kivihiili, öljy ja maakaasu ovat uusiutumattomia polttoaineita, joiden käyttö lisää hiilidioksidipäästöjä."],
    ["Ydinvoima","Ydinreaktioissa vapautuvaa energiaa käytetään veden höyrystämiseen ja edelleen sähköntuotantoon."],
    ["Maalämpö","Maaperään tai kallioon varastoitunutta lämpöenergiaa siirretään rakennusten lämmitykseen."],
    ["Geoterminen energia","Maan sisäisestä lämmöstä peräisin olevaa energiaa hyödynnetään lämmön- tai sähköntuotannossa."]
  ]},
  { nimi:"Ympäristövaikutukset", kortit:[
    ["Elinkaari","Tuotantomuodon vaikutuksia tarkastellaan rakentamisesta ja käytöstä aina laitoksen poistamiseen asti."],
    ["Hiilidioksidipäästö","Energiantuotannon ilmastovaikutusta voidaan vertailla vapautuvan hiilidioksidin määrän avulla."],
    ["Maankäyttö","Eri tuotantotavat tarvitsevat erilaisia pinta-aloja voimaloille, polttoaineille ja siirtoyhteyksille."],
    ["Luonnonvarat","Energiantuotanto käyttää materiaaleja ja polttoaineita, joiden saatavuus ja uusiutuminen vaihtelevat."],
    ["Ekosysteemivaikutus","Energiantuotanto voi muuttaa eliöiden elinympäristöjä, vesistöjä ja luonnon monimuotoisuutta."],
    ["Terveysvaikutus","Tuotantotapojen päästöt, onnettomuusriskit ja muut tekijät voivat vaikuttaa ihmisten terveyteen."],
    ["Suuruusluokka","Tuotantotapoja voidaan vertailla esimerkiksi tehon, päästöjen, kustannusten tai pinta-alan mittakaavan avulla."]
  ]},
  { nimi:"Joustava energiajärjestelmä", kortit:[
    ["Energiajärjestelmä","Kokonaisuus, johon kuuluvat energian tuotanto, siirto, varastointi ja kulutus."],
    ["Hajautettu tuotanto","Energiaa tuotetaan useissa pienissä kohteissa lähellä kuluttajia suurten keskitettyjen laitosten lisäksi."],
    ["Älykäs sähköverkko","Digitaalinen verkko ohjaa tuotantoa ja kulutusta sekä välittää tietoa molempiin suuntiin."],
    ["Säätövoima","Sähköntuotantoa, jonka määrää voidaan muuttaa nopeasti tuotannon ja kulutuksen tasapainottamiseksi."],
    ["Energiavarasto","Energiaa muunnetaan säilytettävään muotoon ja vapautetaan myöhemmin tarpeen mukaan."],
    ["Lämpövarasto","Lämpöenergiaa säilytetään esimerkiksi vedessä, maaperässä tai rakennusten rakenteissa myöhempää käyttöä varten."],
    ["Vesipumppuvoimala","Ylimääräisellä sähköllä vettä pumpataan ylemmäs, jolloin energia varastoituu veden potentiaalienergiaksi."],
    ["Vauhtipyörä","Pyörivään kappaleeseen varastoidaan liike-energiaa, jota voidaan myöhemmin muuntaa takaisin sähköksi."],
    ["Mikroverkko","Paikallinen energiaverkko yhdistää lähellä sijaitsevia tuottajia, varastoja ja kuluttajia."]
  ]},
  { nimi:"Kestävä energiatalous", kortit:[
    ["Kestävä energiatalous","Energiantuotannossa ja kulutuksessa huomioidaan ekologiset, taloudelliset ja sosiaaliset vaikutukset."],
    ["Ekologinen kestävyys","Luonnonvaroja käytetään niin, että ympäristön uusiutumis- ja kantokyky eivät vaarannu."],
    ["Taloudellinen kestävyys","Energiaratkaisujen tulee olla kustannuksiltaan ja resurssien käytöltään pitkäjänteisesti toteuttamiskelpoisia."],
    ["Sosiaalinen kestävyys","Energiaratkaisuissa huomioidaan ihmisten hyvinvointi, turvallisuus ja oikeudenmukaiset mahdollisuudet saada energiaa."],
    ["Energian säästö","Turhaa kulutusta vähennetään muuttamalla toimintaa ja käyttämällä energiaa vain tarpeeseen."],
    ["Hukkalämpö","Muuten käyttämättä jäävä lämpö voidaan kerätä talteen ja hyödyntää toisessa kohteessa."],
    ["Energian varastointi","Tuotannon ja kulutuksen eriaikaisuutta tasataan säilyttämällä energiaa myöhempää käyttöä varten."],
    ["Kestävä kulutus","Energiaa käytetään tarpeisiin tehokkaasti ja ympäristövaikutuksia pyritään vähentämään."]
  ]}
]},

{ id:"FY3", nimi:"Energia ja lämpö", aiheet:[
  { nimi:"Lämpötila ja termodynaaminen systeemi", kortit:[
    ["Lämpötila","Kuvaa aineen rakenneosasten lämpöliikkeen voimakkuutta."],
    ["Kelvinasteikko","Absoluuttinen lämpötila-asteikko, jonka nollakohta on alin mahdollinen lämpötila, 0 K."],
    ["Absoluuttinen nollapiste","Alin mahdollinen lämpötila on 0 K eli −273,15 °C."],
    ["Lämpöliike","Aineen rakenneosasten jatkuvaa satunnaista liikettä ja värähtelyä."],
    ["Tilanmuuttuja","Systeemin tilaa kuvaava suure, kuten lämpötila, paine tai tilavuus."],
    ["Termodynaaminen systeemi","Tarkasteltavaksi rajattu aine tai alue, jonka energian muutoksia tutkitaan."],
    ["Avoin systeemi","Ympäristön kanssa voi vaihtua sekä ainetta että energiaa."],
    ["Suljettu systeemi","Ympäristön kanssa voi vaihtua energiaa mutta ei ainetta."],
    ["Eristetty systeemi","Ympäristön kanssa ei vaihdu ainetta eikä energiaa."],
    ["Lämpötasapaino","Kosketuksissa olevien systeemien lämpötilat ovat tasoittuneet samoiksi."]
  ]},
  { nimi:"Lämpölaajeneminen ja lämmön siirtyminen", kortit:[
    ["Lämpölaajeneminen","Useimpien aineiden mitat kasvavat lämmetessä ja pienenevät jäähtyessä."],
    ["Pituuden lämpölaajeneminen","Kappaleen pituuden muutos riippuu alkuperäisestä pituudesta, lämpötilan muutoksesta ja materiaalista; Δl = αl₀ΔT."],
    ["Tilavuuden lämpölaajeneminen","Kappaleen tilavuuden muutos riippuu alkuperäisestä tilavuudesta, lämpötilan muutoksesta ja materiaalista; ΔV = γV₀ΔT."],
    ["Lämpö","Energiaa, joka siirtyy lämpötilaeron vuoksi kuumemmasta systeemistä kylmempään."],
    ["Johtuminen","Energia siirtyy aineen rakenneosasten vuorovaikutusten kautta ilman aineen kokonaisliikettä."],
    ["Kuljettuminen","Energia siirtyy liikkuvan nesteen tai kaasun mukana."],
    ["Lämpösäteily","Energia siirtyy sähkömagneettisena säteilynä eikä tarvitse väliainetta."],
    ["Lämmönjohde","Aine, jossa energia siirtyy johtumalla tehokkaasti."],
    ["Lämmöneriste","Aine, jossa energia siirtyy johtumalla hitaasti."],
    ["Energiatasapaino","Systeemin energiamäärä pysyy vakiona, kun siihen tulee ja siitä poistuu yhtä paljon energiaa."]
  ]},
  { nimi:"Voima ja paine", kortit:[
    ["Voima","Kuvaa kahden kappaleen välisen vuorovaikutuksen voimakkuutta."],
    ["Paino","Maan ja kappaleen gravitaatiovuorovaikutuksen voimakkuus; G = mg."],
    ["Paine","Kertoo pintaa vastaan kohtisuoran voiman pinta-alayksikköä kohti; p = F/A."],
    ["Pascal","Paineen SI-yksikkö, joka vastaa yhtä newtonia neliömetrille."],
    ["Ilmanpaine","Ilmakehän painosta ja kaasumolekyylien törmäyksistä aiheutuva paine."],
    ["Normaalipaine","Sovittu vertailupaine, jonka arvo on noin 101 325 Pa."],
    ["Hydrostaattinen paine","Nesteen oman painon aiheuttama paine kasvaa syvyyden mukana; pₕ = ρgh."],
    ["Kokonaispaine","Nesteessä vallitseva paine on pinnan paineen ja hydrostaattisen paineen summa; p = p₀ + ρgh."],
    ["Paine-ero","Kahden alueen erisuuruiset paineet voivat aiheuttaa kappaleeseen voiman."]
  ]},
  { nimi:"Kaasun tila ja tilanmuutokset", kortit:[
    ["Kaasun paine","Rakenneosasten törmäykset säiliön seinämiin aiheuttavat makroskooppisesti havaittavan paineen."],
    ["Ainemäärä","Kuvaa aineen rakenneosasten lukumäärää, ja sen yksikkö on mooli."],
    ["Mooli","Ainemäärä, jossa on noin 6,02·10²³ rakenneosasta."],
    ["Ideaalikaasu","Yksinkertaistettu kaasumalli, jossa hiukkasten oma tilavuus ja keskinäiset vuorovaikutukset sivuutetaan."],
    ["Tilanyhtälö","Yhdistää ideaalikaasun paineen, tilavuuden, ainemäärän ja lämpötilan; pV = nRT."],
    ["Isokoorinen muutos","Tilavuus pysyy vakiona, joten paine on suoraan verrannollinen absoluuttiseen lämpötilaan."],
    ["Isobaarinen muutos","Paine pysyy vakiona, joten tilavuus on suoraan verrannollinen absoluuttiseen lämpötilaan."],
    ["Isoterminen muutos","Lämpötila pysyy vakiona, joten paine ja tilavuus ovat kääntäen verrannolliset; pV = vakio."],
    ["Boylen laki","Vakiolämpötilassa kaasun paine kasvaa tilavuuden pienentyessä; p₁V₁ = p₂V₂."],
    ["Yleinen kaasulaki","Suljetun kaasumäärän tiloja voidaan verrata yhtälöllä p₁V₁/T₁ = p₂V₂/T₂."]
  ]},
  { nimi:"Lämpeneminen ja jäähtyminen", kortit:[
    ["Lämpökapasiteetti","Kertoo energiamäärän, joka tarvitaan kappaleen lämpötilan nostamiseen yhdellä asteella."],
    ["Ominaislämpökapasiteetti","Kertoo energiamäärän, joka tarvitaan yhden kilogramman lämpötilan nostamiseen yhdellä asteella."],
    ["Lämpömäärä","Lämpötilan muutoksessa siirtyvä energia voidaan laskea massan ja ominaislämpökapasiteetin avulla; Q = cmΔT."],
    ["Veden ominaislämpökapasiteetti","Suuri arvo tarkoittaa, että veden lämpötilan muuttamiseen tarvitaan paljon energiaa."],
    ["Sekoituskoe","Eristetyssä systeemissä lämpenevien osien vastaanottama energia vastaa jäähtyvien osien luovuttamaa energiaa."],
    ["Lämmitysteho","Kertoo, kuinka nopeasti energiaa siirtyy lämmitettävään kohteeseen; P = Q/Δt."],
    ["Jäähtyminen","Systeemin lämpötila laskee, kun siitä siirtyy energiaa ympäristöön."],
    ["Lämpeneminen","Systeemin lämpötila nousee, kun sen sisäenergia kasvaa ilman olomuodon muutosta."]
  ]},
  { nimi:"Olomuodon muutokset", kortit:[
    ["Kiinteä aine","Rakenneosat ovat sidottuja paikoilleen ja värähtelevät tasapainoasemiensa ympärillä."],
    ["Neste","Rakenneosat ovat lähekkäin mutta voivat liikkua toistensa suhteen."],
    ["Kaasu","Rakenneosat liikkuvat lähes vapaasti ja täyttävät käytettävissä olevan tilan."],
    ["Sulaminen","Kiinteä aine muuttuu nesteeksi ja vastaanottaa energiaa."],
    ["Jähmettyminen","Neste muuttuu kiinteäksi ja luovuttaa energiaa ympäristöön."],
    ["Höyrystyminen","Neste muuttuu kaasuksi ja vastaanottaa energiaa."],
    ["Tiivistyminen","Kaasu muuttuu nesteeksi ja luovuttaa energiaa ympäristöön."],
    ["Sublimoituminen","Kiinteä aine muuttuu suoraan kaasuksi ilman nestemäistä vaihetta."],
    ["Härmistyminen","Kaasu muuttuu suoraan kiinteäksi aineeksi ilman nestemäistä vaihetta."],
    ["Ominaissulamislämpö","Kertoo yhden kilogramman sulattamiseen tarvittavan energian sulamispisteessä; Q = sm."],
    ["Ominaishöyrystymislämpö","Kertoo yhden kilogramman höyrystämiseen tarvittavan energian kiehumispisteessä; Q = rm."]
  ]},
  { nimi:"Faasikaavio ja kosteus", kortit:[
    ["Faasikaavio","Esittää aineen olomuodon lämpötilan ja paineen funktiona."],
    ["Kolmoispiste","Lämpötila ja paine, joissa kiinteä, neste ja kaasu voivat esiintyä tasapainossa yhtä aikaa."],
    ["Kriittinen piste","Tämän lämpötilan yläpuolella kaasua ei voi nesteyttää pelkästään painetta kasvattamalla."],
    ["Kiehuminen","Höyrystymistä tapahtuu koko nesteessä, kun höyrynpaine saavuttaa ympäristön paineen."],
    ["Haihtuminen","Nesteen pinnalta tapahtuvaa höyrystymistä, jota voi tapahtua kaikissa lämpötiloissa."],
    ["Kylläinen höyry","Kaasussa on tietyssä lämpötilassa suurin mahdollinen määrä kyseisen aineen höyryä."],
    ["Suhteellinen kosteus","Kertoo vesihöyryn määrän suhteessa kyseisen lämpötilan suurimpaan mahdolliseen määrään."],
    ["Kastepiste","Lämpötila, johon ilma on jäähdytettävä, jotta vesihöyry alkaa tiivistyä."],
    ["Kiehumispiste","Lämpötila riippuu ympäristön paineesta ja nousee paineen kasvaessa."]
  ]},
  { nimi:"Mekaaninen työ ja sisäenergia", kortit:[
    ["Mekaaninen työ","Voiman avulla siirtyvä energia saadaan voiman ja voiman suuntaisen matkan tulona; W = Fs."],
    ["Sisäenergia","Rakenneosasten liike- ja vuorovaikutusenergioiden muodostama systeemin energiamäärä."],
    ["Ensimmäinen pääsääntö","Sisäenergia muuttuu lämmön siirtymisen ja systeemiin tehdyn työn vaikutuksesta; ΔU = Q + W."],
    ["Joulen koe","Mekaanisen työn muuttuminen sisäenergiaksi havaitaan veden lämpötilan nousuna."],
    ["Kaasun työ","Laajeneva kaasu tekee työtä ympäristöön, kun sen tilavuus kasvaa."],
    ["Tilavuustyö","Vakiopaineessa kaasun tekemän työn suuruus riippuu paineesta ja tilavuuden muutoksesta; W = pΔV."],
    ["Adiabaattinen muutos","Systeemin ja ympäristön välillä ei siirry lämpöä, joten työ muuttaa sisäenergiaa."],
    ["Isoterminen prosessi","Lämpötila ja ideaalikaasun sisäenergia pysyvät vakioina prosessin aikana."],
    ["Energian säilyminen","Energia ei synny eikä häviä, vaan siirtyy ja muuntuu eri muotoihin."]
  ]},
  { nimi:"Lämpövoimakoneet", kortit:[
    ["Lämpövoimakone","Muuntaa osan kuumasta systeemistä saadusta energiasta mekaaniseksi työksi."],
    ["Kuumalähde","Korkeamman lämpötilan systeemi, josta kone vastaanottaa energiaa lämpönä."],
    ["Kylmälähde","Matalamman lämpötilan systeemi, johon kone luovuttaa osan vastaanottamastaan energiasta."],
    ["Hukkalämpö","Kylmempään ympäristöön siirtyvä energia, jota ei saada muutettua hyödylliseksi työksi."],
    ["Hyötysuhde","Kertoo, kuinka suuri osa vastaanotetusta energiasta saadaan hyödylliseksi työksi."],
    ["Kiertoprosessi","Systeemi käy läpi tilanmuutoksia ja palaa lopuksi alkuperäiseen tilaansa."],
    ["Jäähdytyskone","Työn avulla siirtää energiaa kylmemmästä tilasta lämpimämpään ympäristöön."],
    ["Lämpöpumppu","Siirtää ulkopuolisen työn avulla energiaa viileämmästä ympäristöstä lämmitettävään tilaan."],
    ["Kompressori","Puristaa jäähdytysainetta, jolloin sen paine ja yleensä myös lämpötila kasvavat."]
  ]},
  { nimi:"Ilmasto ja lämpö", kortit:[
    ["Säteilytasapaino","Maapallon lämpötila pysyy vakaana, kun vastaanotettu ja avaruuteen säteilevä teho ovat yhtä suuret."],
    ["Kasvihuoneilmiö","Ilmakehä absorboi osan Maan lämpösäteilystä ja nostaa maanpinnan keskilämpötilaa."],
    ["Kasvihuonekaasu","Ilmakehän kaasu, joka absorboi ja lähettää infrapunasäteilyä."],
    ["Hiilidioksidi","Pitkäikäinen kasvihuonekaasu, jonka pitoisuutta fossiilisten polttoaineiden käyttö lisää."],
    ["Albedo","Kertoo, kuinka suuri osa pintaan saapuvasta säteilystä heijastuu takaisin."],
    ["Jääpalaute","Jään väheneminen pienentää heijastavuutta ja lisää Auringon energian absorboitumista."],
    ["Merien lämpeneminen","Veden suuri ominaislämpökapasiteetti saa meret varastoimaan suuren määrän energiaa."],
    ["Merenpinnan nousu","Johtuu erityisesti mannerjään sulamisesta ja meriveden lämpölaajenemisesta."],
    ["Merijään sulaminen","Kelluvan jään sulaminen ei itsessään merkittävästi nosta merenpintaa."],
    ["Ilmastonmuutos","Maapallon pitkäaikainen lämpeneminen muuttaa energiatasapainoa, jäätiköitä, meriä ja muita ilmastojärjestelmän osia."]
  ]}
]},

{ id:"FY4", nimi:"Voima ja liike", aiheet:[
  { nimi:"Liikkeen suureet", kortit:[
    ["Paikka","Kertoo kappaleen sijainnin valitussa koordinaatistossa tiettynä ajanhetkenä."],
    ["Matka","Kertoo kappaleen kulkeman reitin kokonaispituuden."],
    ["Siirtymä","Kertoo kappaleen paikan muutoksen ja suunnan; Δx = x₂ − x₁."],
    ["Nopeus","Kertoo paikan muuttumisnopeuden ja liikkeen suunnan."],
    ["Vauhti","Kertoo liikkeen nopeuden suuruuden ilman tietoa suunnasta."],
    ["Keskinopeus","Koko siirtymä jaetaan siihen kuluneella ajalla; vₖ = Δx/Δt."],
    ["Hetkellinen nopeus","Kertoo kappaleen nopeuden tietyllä ajanhetkellä."],
    ["Tasainen liike","Nopeus pysyy vakiona, joten paikka muuttuu yhtä paljon yhtä pitkissä aikaväleissä."]
  ]},
  { nimi:"Liikkeen kuvaajat", kortit:[
    ["Paikan kuvaaja","Esittää kappaleen paikan ajan funktiona."],
    ["Kuvaajan tangentti","Suora, joka koskettaa käyrää tarkasteltavassa pisteessä ja kertoo hetkellisen muutosnopeuden."],
    ["Tangentin kulmakerroin","Paikan kuvaajassa se antaa kappaleen hetkellisen nopeuden."],
    ["Nopeuden kuvaaja","Esittää kappaleen nopeuden ajan funktiona."],
    ["Kuvaajan pinta-ala","Nopeuden aika-kuvaajan ja aika-akselin välinen etumerkillinen pinta-ala antaa siirtymän."],
    ["Kiihtyvyyden kuvaaja","Esittää kappaleen kiihtyvyyden ajan funktiona."],
    ["Nopeuden muutos","Kiihtyvyyden aika-kuvaajan etumerkillinen pinta-ala antaa nopeuden muutoksen."],
    ["Graafinen derivointi","Kuvaajan kulmakertoimien avulla muodostetaan muuttumisnopeutta kuvaava uusi kuvaaja."]
  ]},
  { nimi:"Kiihtyvä liike", kortit:[
    ["Kiihtyvyys","Kertoo nopeuden muuttumisnopeuden; a = Δv/Δt."],
    ["Keskikiihtyvyys","Nopeuden kokonaismuutos jaetaan siihen kuluneella ajalla."],
    ["Hetkellinen kiihtyvyys","Kertoo nopeuden muuttumisnopeuden tietyllä ajanhetkellä."],
    ["Tasainen kiihtyvyys","Kiihtyvyys pysyy vakiona, joten nopeus muuttuu tasaisesti."],
    ["Nopeusyhtälö","Tasaisesti kiihtyvässä liikkeessä nopeus saadaan ajan avulla; v = v₀ + at."],
    ["Paikkayhtälö","Tasaisesti kiihtyvässä liikkeessä paikka voidaan laskea yhtälöllä x = x₀ + v₀t + ½at²."],
    ["Putoamiskiihtyvyys","Maan lähellä vapaasti putoavan kappaleen kiihtyvyyden suuruus on noin 9,81 m/s²."],
    ["Vapaa putoaminen","Liike, jossa kappaleeseen vaikuttaa vain gravitaatiovoima ja ilmanvastus jätetään huomiotta."]
  ]},
  { nimi:"Vuorovaikutus ja Newtonin lait", kortit:[
    ["Vuorovaikutus","Kahden kappaleen välinen tapahtuma, jossa kappaleet voivat muuttaa toistensa liikettä tai muotoa."],
    ["Voima","Kuvaa vuorovaikutuksen voimakkuutta, ja sen yksikkö on newton."],
    ["Jatkavuuden laki","Kappale säilyttää liiketilansa, jos siihen vaikuttava kokonaisvoima on nolla."],
    ["Hitaus","Kappaleen ominaisuus vastustaa liiketilansa muuttumista."],
    ["Dynamiikan peruslaki","Kokonaisvoima aiheuttaa kappaleelle kiihtyvyyden; ΣF = ma."],
    ["Kokonaisvoima","Kappaleeseen vaikuttavien voimien vektorisumma."],
    ["Newtonin III laki","Vuorovaikutuksessa kappaleet kohdistavat toisiinsa yhtä suuret mutta vastakkaissuuntaiset voimat."],
    ["Vastavoimapari","Kaksi yhtä suurta vastakkaissuuntaista voimaa vaikuttavat eri kappaleisiin samassa vuorovaikutuksessa."]
  ]},
  { nimi:"Voimat ja liikeyhtälö", kortit:[
    ["Voimakuvio","Piirros, jossa esitetään kaikki tarkasteltavaan kappaleeseen vaikuttavat voimat nuolina."],
    ["Paino","Maan kappaleeseen kohdistama gravitaatiovoima; G = mg."],
    ["Tukivoima","Pinnan kappaleeseen kohdistama voima, joka suuntautuu kohtisuoraan pintaa vastaan."],
    ["Jännitysvoima","Kireän langan tai narun kappaleeseen kohdistama voima suuntautuu langan suuntaisesti."],
    ["Liikeyhtälö","Newtonin II lain sovellus, jossa kappaleeseen vaikuttavien voimien summa yhdistetään kiihtyvyyteen."],
    ["Voimakomponentti","Voiman osa valitussa koordinaatiston suunnassa."],
    ["Komponenttimuoto","Liikeyhtälö kirjoitetaan erikseen esimerkiksi vaaka- ja pystysuunnassa."],
    ["Tasapainoehto","Etenemisliikkeen tasapainossa kappaleeseen vaikuttavien voimien vektorisumma on nolla; ΣF = 0."],
    ["Kalteva taso","Tilanne helpottuu valitsemalla koordinaatisto tason suuntaiseksi ja jakamalla voimat komponentteihin."]
  ]},
  { nimi:"Kitka, vastusvoimat ja noste", kortit:[
    ["Kitka","Kosketuksessa olevien pintojen välinen voima vastustaa niiden suhteellista liikettä tai liikkeelle lähtöä."],
    ["Lepokitka","Estää pintojen liukumisen toistensa suhteen ja mukautuu tarvittavaan suuruuteen enimmäisarvoonsa asti."],
    ["Liukukitka","Vastustaa toistensa suhteen liukuvien pintojen liikettä; Fₖ = μN."],
    ["Kitkakerroin","Aineparista riippuva dimensioton luku, joka kuvaa pintojen välistä kitkaa."],
    ["Väliaineen vastus","Kaasu tai neste kohdistaa liikkuvaan kappaleeseen liikkeen suuntaa vastustavan voiman."],
    ["Ilmanvastus","Ilman kappaleeseen kohdistama vastusvoima kasvaa yleensä nopeuden kasvaessa."],
    ["Rajanopeus","Vakionopeus, joka saavutetaan, kun vastusvoima ja muut liikkeen suuntaiset voimat kumoavat toisensa."],
    ["Noste","Nesteen tai kaasun kappaleeseen kohdistama ylöspäin suuntautuva voima."]
  ]},
  { nimi:"Työ ja mekaaninen energia", kortit:[
    ["Mekaaninen työ","Voima siirtää energiaa kappaleeseen tai siitä pois siirtymän aikana; W = Fs cos α."],
    ["Liike-energia","Liikkeeseen liittyvä energia riippuu massasta ja nopeudesta; Eₖ = ½mv²."],
    ["Potentiaalienergia","Konservatiiviseen vuorovaikutukseen liittyvä energia riippuu kappaleiden asemasta."],
    ["Painon potentiaalienergia","Maan lähellä gravitaatioon liittyvä energia voidaan laskea Eₚ = mgh."],
    ["Konservatiivinen voima","Voiman tekemä työ riippuu vain alku- ja loppuasemasta, ei kuljetusta reitistä."],
    ["Mekaaninen energia","Liike-energian ja potentiaalienergian summa; Eₘ = Eₖ + Eₚ."],
    ["Energian säilyminen","Eristetyssä systeemissä energian kokonaismäärä pysyy vakiona."],
    ["Mekaaninen säilyminen","Mekaaninen energia säilyy, kun vain konservatiiviset voimat tekevät työtä."],
    ["Energiaperiaate","Mekaanisen energian muutos on yhtä suuri kuin ei-konservatiivisten voimien tekemä työ; ΔEₘ = Wₑᵢ₋ₖ."],
    ["Työperiaate","Kappaleeseen vaikuttavan kokonaisvoiman tekemä työ on yhtä suuri kuin liike-energian muutos; W = ΔEₖ."]
  ]},
  { nimi:"Liikemäärä, impulssi ja törmäykset", kortit:[
    ["Liikemäärä","Kappaleen massan ja nopeuden tulo on vektorisuure; p = mv."],
    ["Impulssi","Kuvaa voiman kokonaisvaikutusta tietyn ajan kuluessa; I = FΔt vakioisella voimalla."],
    ["Impulssiperiaate","Kappaleen saama impulssi on yhtä suuri kuin sen liikemäärän muutos; I = Δp."],
    ["Voima-aikakuvaaja","Kuvaajan ja aika-akselin välinen pinta-ala antaa kappaleen saaman impulssin."],
    ["Liikemäärän säilyminen","Eristetyn systeemin kokonaisliikemäärä pysyy vuorovaikutuksessa muuttumattomana."],
    ["Törmäys","Lyhytkestoinen vuorovaikutus, jossa kappaleiden nopeudet ja liikemäärät voivat muuttua nopeasti."],
    ["Kimmoisa törmäys","Kokonaisliikemäärän lisäksi myös kappaleiden yhteenlaskettu liike-energia säilyy."],
    ["Kimmoton törmäys","Kokonaisliikemäärä säilyy, mutta osa liike-energiasta muuttuu muihin energiamuotoihin."],
    ["Täysin kimmoton","Törmäyksen jälkeen kappaleet liikkuvat yhdessä samalla nopeudella."],
    ["Yksiulotteinen törmäys","Kappaleiden liike tapahtuu samalla suoralla, joten liikemäärän suunnat voidaan käsitellä etumerkeillä."]
  ]}
]},

{ id:"FY5", nimi:"Jaksollinen liike ja aallot", aiheet:[
  { nimi:"Ympyräliike ja gravitaatio", kortit:[
    ["Tasainen ympyräliike","Liike ympyrärataa pitkin vakionopeudella; nopeuden suunta muuttuu jatkuvasti."],
    ["Keskeiskiihtyvyys","Ympyrän keskipistettä kohti osoittava kiihtyvyys, a = v² / r."],
    ["Keskeisvoima","Kokonaisvoima, joka pitää kappaleen ympyräradalla; osoittaa keskipisteeseen."],
    ["Jaksonaika","Aika, jossa tapahtuu yksi täysi kierros tai värähdys."],
    ["Taajuus","Värähdysten tai kierrosten määrä aikayksikössä, f = 1 / T."],
    ["Gravitaatiolaki","Kahden massan välinen vetovoima, F = G·m₁m₂ / r²."],
    ["Ratanopeus","Nopeus, jolla satelliitti kiertää keskuskappaletta vakiokorkeudella."]
  ]},
  { nimi:"Värähtely", kortit:[
    ["Harmoninen värähtely","Värähtely, jossa palauttava voima on verrannollinen poikkeamaan tasapainoasemasta."],
    ["Amplitudi","Suurin poikkeama tasapainoasemasta."],
    ["Vaimeneminen","Värähtelyn amplitudin pieneneminen energian siirtyessä ympäristöön."],
    ["Resonanssi","Voimakas värähtely, kun herätteen taajuus vastaa systeemin ominaistaajuutta."],
    ["Ominaistaajuus","Taajuus, jolla systeemi värähtelee vapaasti."],
    ["Matemaattinen heiluri","Malli heilurista, jonka jaksonaika pienillä kulmilla on T = 2π√(l/g)."]
  ]},
  { nimi:"Aallot ja ääni", kortit:[
    ["Aallonpituus","Kahden peräkkäisen samassa vaiheessa olevan kohdan etäisyys."],
    ["Aaltoliikkeen perusyhtälö","Aallon etenemisnopeus on taajuuden ja aallonpituuden tulo, v = fλ."],
    ["Poikittainen aalto","Aalto, jossa väliaine värähtelee kohtisuoraan etenemissuuntaa vastaan."],
    ["Pitkittäinen aalto","Aalto, jossa väliaine värähtelee etenemissuunnassa, esimerkiksi ääni."],
    ["Interferenssi","Kahden aallon yhteisvaikutus, joka vahvistaa tai kumoaa värähtelyä."],
    ["Diffraktio","Aallon taipuminen esteen reunan tai raon takana."],
    ["Seisova aalto","Kahden vastakkain etenevän aallon summa, jossa on paikallaan pysyviä solmuja."],
    ["Dopplerin ilmiö","Havaitun taajuuden muuttuminen, kun lähde ja havaitsija liikkuvat toistensa suhteen."],
    ["Äänen intensiteetti","Ääniaallon teho pinta-alaa kohti; desibeliasteikko on sen logaritminen mitta."]
  ]}
]},

{ id:"FY6", nimi:"Sähkö", aiheet:[
  { nimi:"Varaus ja kenttä", kortit:[
    ["Sähkövaraus","Aineen ominaisuus, joka aiheuttaa sähköisen vuorovaikutuksen; yksikkö coulombi."],
    ["Alkeisvaraus","Pienin vapaana esiintyvä varaus, e = 1,602 · 10⁻¹⁹ C."],
    ["Coulombin laki","Kahden pistevarauksen välinen voima, F = k·q₁q₂ / r²."],
    ["Sähkökenttä","Varauksen ympäristö, jossa toiseen varaukseen kohdistuu voima, E = F / q."],
    ["Jännite","Kahden pisteen välinen sähköinen potentiaaliero, U = W / q."],
    ["Varauksen säilymislaki","Suljetun systeemin kokonaisvaraus pysyy vakiona."]
  ]},
  { nimi:"Virtapiirit", kortit:[
    ["Sähkövirta","Varauksen kulkeutuminen aikayksikköä kohti, I = Q / t."],
    ["Resistanssi","Komponentin kyky vastustaa sähkövirtaa, R = U / I."],
    ["Ohmin laki","Virta on suoraan verrannollinen jännitteeseen, kun resistanssi on vakio."],
    ["Resistiivisyys","Aineelle ominainen suure, joka kertoo sen sähkönjohtavuudesta."],
    ["Sarjaankytkentä","Kytkentä, jossa virta on sama ja jännitteet summautuvat; R = R₁ + R₂."],
    ["Rinnankytkentä","Kytkentä, jossa jännite on sama ja virrat summautuvat; 1/R = 1/R₁ + 1/R₂."],
    ["Kirchhoffin virtalaki","Solmuun tulevien virtojen summa on yhtä suuri kuin siitä lähtevien."],
    ["Kirchhoffin jännitelaki","Suljetun silmukan jännitteiden summa on nolla."],
    ["Lähdejännite","Virtalähteen napojen välinen jännite ilman kuormaa."]
  ]},
  { nimi:"Sähköenergia ja komponentit", kortit:[
    ["Sähköteho","Sähkövirran tekemä työ aikayksikössä, P = UI."],
    ["Joulen laki","Resistanssissa kehittyvä lämpöteho, P = RI²."],
    ["Kondensaattori","Komponentti, joka varastoi energiaa sähkökenttään."],
    ["Kapasitanssi","Kondensaattorin kyky varata varausta jännitettä kohti, C = Q / U."],
    ["Puolijohde","Aine, jonka johtavuus on eristeen ja johteen välillä ja säädettävissä."],
    ["Diodi","Komponentti, joka päästää virran kulkemaan vain toiseen suuntaan."]
  ]}
]},

{ id:"FY7", nimi:"Sähkömagnetismi ja valo", aiheet:[
  { nimi:"Magnetismi", kortit:[
    ["Magneettikenttä","Alue, jossa magneettiseen aineeseen tai liikkuvaan varaukseen kohdistuu voima."],
    ["Magneettivuon tiheys","Magneettikentän voimakkuutta kuvaava suure B; yksikkö tesla."],
    ["Lorentzin voima","Magneettikentän liikkuvaan varaukseen kohdistama voima, F = qvB sin α."],
    ["Virtajohtimen voima","Magneettikentässä olevaan virralliseen johtimeen kohdistuva voima, F = BIl sin α."],
    ["Magneettivuo","Pinnan läpi kulkeva magneettikentän määrä, Φ = BA cos α."],
    ["Solenoidi","Käämi, jonka sisällä syntyy tasainen magneettikenttä virran kulkiessa."]
  ]},
  { nimi:"Induktio", kortit:[
    ["Faradayn induktiolaki","Muuttuva magneettivuo synnyttää jännitteen, e = −ΔΦ / Δt."],
    ["Lenzin laki","Indusoitunut virta vastustaa sen syntyyn johtanutta muutosta."],
    ["Generaattori","Laite, joka muuttaa liike-energiaa sähköenergiaksi induktion avulla."],
    ["Muuntaja","Laite, joka muuttaa vaihtojännitteen suuruutta käämien kierroslukujen suhteessa."],
    ["Vaihtovirta","Virta, jonka suunta ja suuruus vaihtelevat jaksollisesti."],
    ["Tehollisarvo","Vaihtovirran arvo, joka vastaa lämpövaikutukseltaan yhtä suurta tasavirtaa."]
  ]},
  { nimi:"Valo", kortit:[
    ["Sähkömagneettinen aalto","Etenevä sähkö- ja magneettikentän värähtely, joka ei tarvitse väliainetta."],
    ["Valon nopeus","Valon nopeus tyhjiössä, c = 299 792 458 m/s."],
    ["Taitekerroin","Valon nopeuden suhde tyhjiössä ja aineessa, n = c / v."],
    ["Snellin laki","Taittumislaki, n₁ sin α₁ = n₂ sin α₂."],
    ["Kokonaisheijastus","Ilmiö, jossa valo heijastuu kokonaan takaisin tiheämmästä aineesta rajakulman ylittyessä."],
    ["Hila","Optinen komponentti, jonka rakojen kautta valo taipuu ja hajoaa spektriksi."],
    ["Polarisaatio","Valon värähtelysuunnan rajoittuminen yhteen tasoon."],
    ["Linssin polttoväli","Etäisyys, jolla optiselta akselilta tuleva säteily kootaan pisteeseen."]
  ]}
]},

{ id:"FY8", nimi:"Aine, säteily ja kvantittuminen", aiheet:[
  { nimi:"Kvantittuminen", kortit:[
    ["Fotoni","Sähkömagneettisen säteilyn energiakvantti, jonka energia on E = hf."],
    ["Planckin vakio","Luonnonvakio h = 6,626 · 10⁻³⁴ Js, joka yhdistää energian ja taajuuden."],
    ["Valosähköinen ilmiö","Elektronien irtoaminen metallista, kun siihen osuu riittävän suurienergistä valoa."],
    ["Irrotustyö","Pienin energia, joka tarvitaan elektronin irrottamiseen metallista."],
    ["Energiatasot","Atomin sallitut, kvantittuneet energia-arvot."],
    ["Viivaspektri","Spektri, jossa esiintyy vain tiettyjä aallonpituuksia; syntyy energiatasojen välisistä siirtymistä."],
    ["Bohrin atomimalli","Malli, jossa elektronit kiertävät ydintä vain tietyillä sallituilla radoilla."],
    ["Ionisaatioenergia","Energia, joka tarvitaan elektronin irrottamiseen atomista kokonaan."]
  ]},
  { nimi:"Aineen aaltoluonne", kortit:[
    ["De Broglien aallonpituus","Hiukkasen aallonpituus, λ = h / p."],
    ["Aalto-hiukkasdualismi","Aineella ja säteilyllä on sekä aalto- että hiukkasominaisuuksia."],
    ["Epätarkkuusperiaate","Paikkaa ja liikemäärää ei voi tuntea samanaikaisesti mielivaltaisen tarkasti."],
    ["Todennäköisyysluonne","Kvanttimekaniikka antaa vain todennäköisyyksiä mittaustuloksille."],
    ["Tunneloituminen","Ilmiö, jossa hiukkanen läpäisee energiavallin, jonka yli se ei klassisesti pääsisi."],
    ["Kaksoisrakokoe","Koe, jossa yksittäiset hiukkaset muodostavat interferenssikuvion."]
  ]},
  { nimi:"Ydinfysiikka", kortit:[
    ["Nukleoni","Ytimen rakenneosa eli protoni tai neutroni."],
    ["Isotooppi","Saman alkuaineen ydin, jossa on eri määrä neutroneja."],
    ["Radioaktiivisuus","Epästabiilin ytimen hajoaminen, jossa lähtee säteilyä."],
    ["Alfasäteily","Ytimestä lähtevä heliumydin; pysähtyy paperiin."],
    ["Beetasäteily","Ytimestä lähtevä elektroni tai positroni; pysähtyy ohueen metallilevyyn."],
    ["Gammasäteily","Ytimestä lähtevä suurienerginen sähkömagneettinen säteily."],
    ["Puoliintumisaika","Aika, jossa puolet radioaktiivisista ytimistä on hajonnut."],
    ["Aktiivisuus","Hajoamisten määrä aikayksikössä; yksikkö becquerel."],
    ["Massavaje","Ytimen massan ja sen rakenneosien yhteismassan erotus."],
    ["Sidosenergia","Energia, joka tarvitaan ytimen hajottamiseen nukleoneiksi; E = mc²."],
    ["Ionisoiva säteily","Säteily, jolla on riittävästi energiaa irrottamaan elektroneja atomeista."],
    ["Efektiivinen annos","Säteilyn terveysvaikutusta kuvaava suure; yksikkö sievert."]
  ]},
  { nimi:"Hiukkasfysiikka", kortit:[
    ["Standardimalli","Teoria, joka kuvaa alkeishiukkaset ja niiden vuorovaikutukset gravitaatiota lukuun ottamatta."],
    ["Kvarkki","Alkeishiukkanen, joista protonit ja neutronit koostuvat."],
    ["Leptoni","Alkeishiukkasryhmä, johon kuuluvat muun muassa elektroni ja neutriino."],
    ["Antihiukkanen","Hiukkanen, jolla on sama massa mutta vastakkainen varaus."],
    ["Annihilaatio","Hiukkasen ja antihiukkasen häviäminen, jolloin syntyy säteilyä."],
    ["Perusvuorovaikutukset","Gravitaatio, sähkömagneettinen, vahva ja heikko vuorovaikutus."]
  ]}
]}
];
