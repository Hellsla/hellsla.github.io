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
  { nimi:"Energiantuotanto", kortit:[
    ["Uusiutuva energialähde","Energialähde, joka uusiutuu luonnossa ihmisen aikaskaalassa, esimerkiksi tuuli ja aurinko."],
    ["Fossiilinen polttoaine","Muinaisesta eloperäisestä aineksesta syntynyt polttoaine, kuten kivihiili tai maakaasu."],
    ["Fissio","Raskaan atomiytimen halkeaminen, jossa vapautuu energiaa."],
    ["Fuusio","Kevyiden ytimien yhtyminen raskaammaksi ytimeksi; Auringon energialähde."],
    ["Hyötysuhde","Hyödyksi saadun energian osuus otetusta energiasta, η = W_hyöty / W_otettu."],
    ["Energian säilymislaki","Energia ei häviä eikä synny tyhjästä, vaan muuttaa muodosta toiseen."],
    ["Säätövoima","Nopeasti säädettävä sähköntuotanto, joka pitää tuotannon ja kulutuksen tasapainossa."],
    ["Peruskuormatuotanto","Tasaisesti käyvä tuotanto, joka kattaa jatkuvan sähkön tarpeen."]
  ]},
  { nimi:"Ilmasto ja ympäristö", kortit:[
    ["Kasvihuoneilmiö","Ilmakehän kaasut päästävät auringon säteilyn läpi mutta hidastavat lämpösäteilyn karkaamista."],
    ["Kasvihuonekaasu","Kaasu, joka absorboi maapallon lähettämää lämpösäteilyä, esimerkiksi CO₂ ja metaani."],
    ["Albedo","Pinnan heijastussuhde eli se osuus säteilystä, joka heijastuu takaisin."],
    ["Säteilypakote","Ilmakehän muutoksen aiheuttama muutos maapallon energiatasapainossa (W/m²)."],
    ["Hiilijalanjälki","Toiminnan aiheuttamat kasvihuonekaasupäästöt hiilidioksidiekvivalentteina."],
    ["Energiatehokkuus","Saman hyödyn tuottaminen pienemmällä energiamäärällä."]
  ]},
  { nimi:"Sähkön käyttö", kortit:[
    ["Kilowattitunti","Energiayksikkö, joka vastaa kilowatin tehoa tunnin ajan; 1 kWh = 3,6 MJ."],
    ["Siirtohäviö","Sähköverkossa lämmöksi muuttuva osa siirretystä energiasta."],
    ["Suurjännitesiirto","Siirto korkealla jännitteellä, jolloin virta ja siirtohäviöt pienenevät."],
    ["Kulutushuippu","Hetki, jolloin sähkön kulutus on suurimmillaan."],
    ["Energiavarasto","Järjestelmä, johon energiaa varastoidaan myöhempää käyttöä varten, esimerkiksi akku tai pumppuvoimalaitos."]
  ]}
]},

{ id:"FY3", nimi:"Energia ja lämpö", aiheet:[
  { nimi:"Työ ja energia", kortit:[
    ["Työ","Energian siirto voiman vaikuttaessa siirtymän suuntaan, W = Fs cos α."],
    ["Liike-energia","Liikkeestä johtuva energia, Eₖ = ½mv²."],
    ["Potentiaalienergia","Asemasta johtuva energia; painovoimakentässä Eₚ = mgh."],
    ["Mekaaninen energia","Liike-energian ja potentiaalienergian summa."],
    ["Teho","Tehty työ aikayksikköä kohti, P = W / t."],
    ["Hyötysuhde","Hyödyksi saadun energian suhde otettuun energiaan."]
  ]},
  { nimi:"Lämpö", kortit:[
    ["Lämpötila","Suure, joka kuvaa aineen hiukkasten keskimääräistä liike-energiaa."],
    ["Absoluuttinen nollapiste","Alin mahdollinen lämpötila, 0 K = −273,15 °C."],
    ["Sisäenergia","Kappaleen hiukkasten liike- ja potentiaalienergian summa."],
    ["Ominaislämpökapasiteetti","Energia, joka tarvitaan lämmittämään yksi kilogramma ainetta yhden kelvinin: Q = cmΔT."],
    ["Ominaissulamislämpö","Energia, joka tarvitaan sulattamaan yksi kilogramma ainetta sulamislämpötilassa."],
    ["Lämpölaajeneminen","Kappaleen mittojen kasvu lämpötilan noustessa."],
    ["Johtuminen","Lämmön siirtyminen aineessa hiukkasten törmäysten välityksellä."],
    ["Konvektio","Lämmön siirtyminen virtaavan nesteen tai kaasun mukana."],
    ["Lämpösäteily","Lämmön siirtyminen sähkömagneettisena säteilynä ilman väliainetta."],
    ["Lämpötasapaino","Tila, jossa kappaleiden lämpötilat ovat yhtä suuret eikä lämpöä siirry."]
  ]},
  { nimi:"Kaasut ja termodynamiikka", kortit:[
    ["Paine","Pinta-alaa kohti kohtisuoraan vaikuttava voima, p = F / A."],
    ["Ideaalikaasu","Malli kaasusta, jonka hiukkasilla ei ole tilavuutta eikä keskinäisiä vuorovaikutuksia."],
    ["Tilanyhtälö","Ideaalikaasun paineen, tilavuuden ja lämpötilan yhteys, pV = nRT."],
    ["Isoterminen prosessi","Prosessi vakiolämpötilassa; pV = vakio."],
    ["Isobaarinen prosessi","Prosessi vakiopaineessa; V / T = vakio."],
    ["Isokoorinen prosessi","Prosessi vakiotilavuudessa; p / T = vakio."],
    ["Termodynamiikan 1. pääsääntö","Systeemin sisäenergian muutos on siihen tuodun lämmön ja tehdyn työn summa, ΔU = Q + W."],
    ["Termodynamiikan 2. pääsääntö","Lämpö siirtyy itsestään vain kuumemmasta kylmempään."],
    ["Lämpövoimakone","Laite, joka muuttaa osan lämpöenergiasta työksi ja luovuttaa loput kylmempään."],
    ["Lämpöpumppu","Laite, joka siirtää työn avulla lämpöä kylmemmästä lämpimämpään."]
  ]}
]},

{ id:"FY4", nimi:"Voima ja liike", aiheet:[
  { nimi:"Liike", kortit:[
    ["Keskinopeus","Kuljettu matka jaettuna siihen käytetyllä ajalla."],
    ["Hetkellinen nopeus","Nopeus tietyllä hetkellä; paikkakuvaajan kulmakerroin."],
    ["Kiihtyvyys","Nopeuden muutos aikayksikköä kohti, a = Δv / Δt."],
    ["Tasainen liike","Liike, jossa nopeus pysyy vakiona."],
    ["Tasaisesti kiihtyvä liike","Liike, jossa kiihtyvyys on vakio, s = v₀t + ½at²."],
    ["Putoamiskiihtyvyys","Vapaasti putoavan kappaleen kiihtyvyys, maan pinnalla noin 9,81 m/s²."],
    ["Heittoliike","Liike, jossa vaakasuunnassa liike on tasaista ja pystysuunnassa kiihtyvää."]
  ]},
  { nimi:"Newtonin lait", kortit:[
    ["Newtonin I laki","Kappale jatkaa liiketilaansa, ellei siihen vaikuta nollasta poikkeava kokonaisvoima."],
    ["Newtonin II laki","Kappaleen kiihtyvyys on suoraan verrannollinen kokonaisvoimaan ja kääntäen massaan, a = ΣF / m."],
    ["Newtonin III laki","Voimaa vastaa aina yhtä suuri vastakkaissuuntainen vastavoima toisessa kappaleessa."],
    ["Kokonaisvoima","Kappaleeseen vaikuttavien voimien vektorisumma."],
    ["Hitaus","Kappaleen pyrkimys vastustaa liiketilan muutosta; mittana massa."],
    ["Paino","Kappaleeseen kohdistuva painovoima, G = mg."],
    ["Tasapaino","Tila, jossa kappaleeseen vaikuttava kokonaisvoima on nolla."]
  ]},
  { nimi:"Voimat ja liikemäärä", kortit:[
    ["Normaalivoima","Tukipinnan kappaleeseen kohdistama pintaa vastaan kohtisuora voima."],
    ["Lepokitka","Voima, joka estää paikallaan olevan kappaleen lähtemisen liikkeelle."],
    ["Liikekitka","Liikettä vastustava voima liikkuvan kappaleen ja alustan välillä, F = μN."],
    ["Hooken laki","Jousivoima on verrannollinen venymään, F = kx."],
    ["Liikemäärä","Massan ja nopeuden tulo, p = mv."],
    ["Liikemäärän säilymislaki","Suljetun systeemin kokonaisliikemäärä säilyy vuorovaikutuksissa."],
    ["Impulssi","Voiman ja vaikutusajan tulo, joka vastaa liikemäärän muutosta."],
    ["Kimmoinen törmäys","Törmäys, jossa sekä liikemäärä että liike-energia säilyvät."],
    ["Kimmoton törmäys","Törmäys, jossa liikemäärä säilyy mutta osa liike-energiasta muuttuu muihin muotoihin."]
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
