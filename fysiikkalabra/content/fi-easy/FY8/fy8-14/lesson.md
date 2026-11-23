# Säteily lääketieteessä ja teknologiassa

> **Miksi** PET-kuvauksessa potilaaseen ruiskutetaan radioaktiivista sokeria, ja miten laite päättelee, mistä kohdasta kehon sisältä säteily tuli?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: sairaalan PET-TT-kuvaushuone. Keskellä on suuri valkoinen kuvauslaite, ja sen keskellä on pyöreä aukko. Potilas makaa peiton alla kuvauspöydällä. Pöytä liukuu aukkoon. Vasemmalla seinässä on ikkuna valvomoon. Valvomon näytöllä on tumma poikkileikkauskuva, ja siinä on yksi kirkas oranssi täplä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Röntgensäteily syntyy, kun nopeat elektronit osuvat anodiin

**Röntgensäteily** on fotonisäteilyä, jonka fotoneilla on paljon energiaa. Fotoni on sähkömagneettisen säteilyn pieni energiapaketti. Röntgensäteilyä syntyy kahdella tavalla. Ensimmäisessä tavassa nopeat elektronit jarruttavat aineessa. Tätä säteilyä sanotaan jarrutussäteilyksi. Toisessa tavassa nopea elektroni irrottaa atomin sisimmältä kuorelta elektronin, ja ulomman kuoren elektroni siirtyy sen paikalle. Tätä säteilyä sanotaan karakteristiseksi röntgensäteilyksi.

Röntgenputkessa hehkuva katodi lähettää elektroneja. Katodi on putken negatiivinen napa. Jännite $U$ kiihdyttää elektronit kohti volframista tehtyä anodia. Anodi on putken positiivinen napa. Jokainen elektroni saa liike-energian $eU$. Jos jännite on esimerkiksi $80\,\text{kV}$, syntyvän fotonin energia on enintään $80\,\text{keV}$. Noin $99\,\%$ elektronien energiasta muuttuu anodin sisäenergiaksi. Vain pieni osa säteilee röntgenfotoneina.

Jarrutussäteilyn spektri on jatkuva. Spektri kertoo, kuinka paljon säteilyä on kullakin energialla. Jatkuvan spektrin päällä näkyy anodin atomien karakteristiset terävät piikit. Volframilla piikit ovat noin $59\,\text{keV}$:n kohdalla. Röntgen- ja gammafotoni ovat samaa sähkömagneettista säteilyä. Nimi kertoo vain, mistä fotoni syntyi. Röntgenfotoni syntyy elektronien jarrutuksessa tai atomin sisäkuoren siirtymässä. Gammafotoni syntyy ytimen siirtymässä. Molemmat ionisoivat ja vaimenevat aineessa samalla tavalla (luku *Ionisoiva säteily ja elimistö*).

<svg data-fig="rontgen" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: röntgenkuvaus. Ylhäällä on lasinen röntgenputki. Sen vasemmalla puolella on hehkuva katodi, josta elektronit kiihtyvät oikealle anodille. Anodista lähtee alaspäin viuhkan muotoinen joukko röntgenfotoneja, jotka on piirretty aaltoviivoina. Niiden tiellä on kyynärvarren poikkileikkaus. Siinä on pehmytkudos ja sen sisällä kaksi luuta. Luihin osuvat fotonit pysähtyvät. Muut fotonit kulkevat kudoksen läpi alla olevaan ilmaisimeen. Ilmaisimeen tulee luiden kohdalle vaaleampi varjo, koska sinne osuu vähemmän säteilyä." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-rontgen.webp" x="20.7" y="0" width="585.4" height="376.8" preserveAspectRatio="none"/>
  <foreignObject x="293.5" y="57.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="52" y="40.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{röntgenputki}$</div></foreignObject>
  <foreignObject x="105" y="151.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pehmytkudos}$</div></foreignObject>
  <foreignObject x="542" y="191.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{luu}$</div></foreignObject>
  <foreignObject x="130" y="300.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ilmaisin}$</div></foreignObject>
  <foreignObject x="327.5" y="337.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{luiden varjo}$</div></foreignObject>
</svg>

### Röntgenkuva ja tietokonetomografia

Röntgenkuva on varjokuva. Säteily kulkee potilaan läpi ilmaisimeen, ja jokainen kudoskerros vaimentaa eli heikentää siitä osan. Luu vaimentaa röntgensäteilyä paljon enemmän kuin pehmytkudos. Luu on tiheämpää, ja siinä on kalsiumia. Kalsiumin järjestysluku $20$ on paljon suurempi kuin pehmytkudoksen vedyn, hiilen ja hapen. Röntgenkuvauksen energioilla valosähköisen absorption todennäköisyys kasvaa voimakkaasti järjestysluvun mukana (luku *Ionisoiva säteily ja elimistö*). Siksi ero riippuu myös säteilyn energiasta. Noin $60\,\text{keV}$:n säteilylle pehmytkudoksen puoliintumispaksuus on noin $3{,}4\,\text{cm}$ ja luun vain noin $1{,}1\,\text{cm}$. Puoliintumispaksuus on paksuus, joka päästää läpi puolet säteilystä.

Luun taakse osuu siksi vähemmän säteilyä, ja luu näkyy kuvassa vaaleana. Keuhkojen ilma päästää säteilyn läpi lähes kokonaan, joten keuhkot näkyvät tummina. Kuvan **kontrasti** eli kirkkausero syntyy siitä, että eri kudokset vaimentavat säteilyä eri tavalla.

Tietokonetomografiassa (TT) röntgenputki ja ilmaisimet kiertävät potilaan ympäri. Laite mittaa vaimenemisen tuhansista suunnista. Tietokone laskee mittauksista, kuinka paljon kukin pieni tilavuusalkio vaimentaa. Tuloksena on poikkileikkauskuva, jossa näkyvät myös toistensa takana olevat elimet. TT-tutkimuksen annos on kuitenkin kymmeniä kertoja suurempi kuin keuhkojen röntgenkuvan annos.

```pysahdy
Tietokonetomografiassa otetaan $800$ projektiota, joista kukin antaa annoksen $0{,}010\,\text{mSv}$. Keuhkojen röntgenkuvan annos on $0{,}1\,\text{mSv}$. Kuinka moninkertainen TT:n kokonaisannos on röntgenkuvaan verrattuna?
---
Annokset summautuvat: $800 \cdot 0{,}010\,\text{mSv} = 8\,\text{mSv}$. Suhde on $\tfrac{8\,\text{mSv}}{0{,}1\,\text{mSv}} = 80$, eli TT:n annos on noin $80$-kertainen. Yhden suunnan annos on paljon pienempi kuin yhden röntgenkuvan annos. Siksi ero on kymmeniä kertoja eikä tuhatkertainen.
```

| Tutkimus | Efektiivinen annos |
| --- | --- |
| hampaan röntgenkuva | $< 0{,}01\,\text{mSv}$ |
| keuhkojen röntgenkuva (etu- ja sivukuva) | noin $0{,}1\,\text{mSv}$ |
| pään TT | noin $2\,\text{mSv}$ |
| vartalon TT | noin $5$–$10\,\text{mSv}$ |
| luuston isotooppikuvaus | noin $3\,\text{mSv}$ |
| PET-kuvaus | noin $6\,\text{mSv}$ |

Lähde: tyypilliset suuruusluokat STUKin terveydenhuollon säteilyaltistusta koskevista julkaisuista ([STUK: Röntgentutkimuksen säteilyannokset vaihtelevat](https://www.julkari.fi/server/api/core/bitstreams/89234513-99f8-4ee2-a720-20bd04eb2cfb/content)) ja ICRP:n julkaisusta 128 (2015). Yksittäisen tutkimuksen annos riippuu laitteesta, kuvausprotokollasta ja potilaasta. Vertailun vuoksi suomalainen saa luonnon säteilystä keskimäärin noin $5{,}1\,\text{mSv}$ vuodessa (luku *Säteilyannos ja säteilyturvallisuus Suomessa*).

<figure class="unit-photo"><img src="pics/fy8/pet-ct-scanner.webp" alt="Sairaalan huone. Siinä on iso rengas ja potilaspöytä."><figcaption>PET-TT-laite. Renkaan sisällä on ilmaisimia, jotka havaitsevat fotoneja. Siellä on myös röntgenputki. Potilas liikkuu pöydän mukana renkaan läpi.</figcaption></figure>


### Isotooppikuvaus: merkkiaine näyttää elimen toiminnan

**Merkkiaine** on radioaktiivinen nuklidi eli tietynlainen atomiydin. Se on liitetty yhdisteeseen, jota elimistö käsittelee kuten omaa ainettaan. Siksi merkkiaine kertyy tutkittavaan elimeen. Kehon ulkopuolinen ilmaisin havaitsee merkkiaineen säteilyn. Kuva ei näytä vain rakennetta, kuten röntgenkuva, vaan sen, missä elimistö toimii. Esimerkiksi luuston isotooppikuvauksessa merkkiaine kertyy kohtiin, joissa luu uusiutuu vilkkaasti, kuten murtumiin ja etäpesäkkeisiin. Etäpesäke on syöpäkasvaimen levinnyt osa.

Yleisin merkkiaineen nuklidi on teknetium-$99\text{m}$. Se lähettää lähes pelkästään $140\,\text{keV}$:n gammasäteilyä. Säteily pääsee kehosta ulos ja ionisoi matkallaan harvakseltaan. Teknetium-$99\text{m}$:n puoliintumisaika on $6{,}01\,\text{h}$ (luku *Hajoamislaki ja puoliintumisaika*). Vuorokauden kuluttua aktiivisuudesta on siis jäljellä vain noin $6\,\%$. Lisäksi osa aineesta poistuu virtsan mukana. Gammakamera kuvaa potilaan säteilyä. SPECT-laitteessa kamera kiertää potilaan ympäri, ja tuloksena on kolmiulotteinen kuva.

### PET: kaksi fotonia vastakkaisiin suuntiin

PET-kuvauksen eli positroniemissiotomografian merkkiaineena on yleensä fluori-18. Se on sokerin kaltaisessa yhdisteessä (FDG). Syöpäsolut käyttävät paljon sokeria, joten merkkiainetta kertyy niihin tavallista enemmän. Merkkiaine ei kuitenkaan ole täysin spesifinen syöpäsoluille. Sitä kertyy myös esimerkiksi tulehtuneeseen kudokseen ja aivoihin. Siksi kirkas kohta PET-kuvassa ei yksin osoita syöpää. Fluori-18 hajoaa $\beta^+$-hajoamisella, ja sen puoliintumisaika on $110\,\text{min}$. Hajoamisessa syntyy positroni. Positroni on elektronin antihiukkanen, jolla on positiivinen varaus. Positroni kulkee kudoksessa noin millimetrin ja kohtaa elektronin. Ne annihiloituvat eli häviävät: niiden massa muuttuu kahdeksi fotoniksi. Kummankin fotonin energia on $511\,\text{keV}$, ja fotonit lähtevät lähes vastakkaisiin suuntiin, koska hiukkasten yhteinen liikemäärä on pieni.

<svg data-fig="pet" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: PET-kuvaus. Vasemmalla on potilaan poikkileikkaus ilmaisinrenkaan keskellä. Kehon sisällä fluori-18-ydin lähettää positronin. Positroni kulkee lyhyen matkan ja kohtaa elektronin. Kohtaamispisteestä lähtee kaksi fotonia vastakkaisiin suuntiin. Ne osuvat renkaan kahteen ilmaisimeen, jotka on värjätty oransseiksi. Ilmaisimien välille on piirretty katkoviiva. Annihilaation täytyy tapahtua jossain tällä viivalla. Oikealla on suurennos: positroni ja elektroni kohtaavat, ja syntyy kaksi 511 kiloelektronivoltin fotonia. Fotonit lähtevät vastakkaisiin suuntiin eli 180 asteen kulmaan toisiinsa nähden." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-pet.webp" x="0" y="0" width="600" height="390" preserveAspectRatio="none"/>
  <foreignObject x="94.5" y="347.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilmaisinrengas}$</div></foreignObject>
  <foreignObject x="416" y="25.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$e^+ + e^- \rightarrow \gamma + \gamma$</div></foreignObject>
  <foreignObject x="393.5" y="73.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$e^+$</div></foreignObject>
  <foreignObject x="525.5" y="73.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="376.5" y="179.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$511\,\text{keV}$</div></foreignObject>
  <foreignObject x="480.5" y="237.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$511\,\text{keV}$</div></foreignObject>
  <foreignObject x="401" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$180^\circ$</div></foreignObject>
  <foreignObject x="420" y="303.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lähde janalla}$</div></foreignObject>
</svg>

Potilasta ympäröi ilmaisinrengas. Kaksi vastakkaista ilmaisinta voi havaita fotonin muutaman nanosekunnin sisällä toisistaan. Tätä sanotaan **koinsidenssiksi**. Silloin laite päättelee, että fotonit syntyivät samassa annihilaatiossa. Lähde on jossain näiden ilmaisimien välisellä janalla. Jos fotonien saapumisaikojen eroa ei mitata, yksi jana ei kerro, missä kohdassa janaa lähde on.

Nykyaikaiset PET-laitteet mittaavat myös tämän aikaeron (lentoaika-PET) noin $0{,}3\,\text{ns}$:n tarkkuudella. Valo kulkee nanosekunnissa noin $30\,\text{cm}$. Aikaero rajaa siis lähteen janalla muutaman senttimetrin matkalle. Positroni kulkee hetken ennen annihilaatiota. Siksi jana kertoo annihilaation paikan eikä aivan hajoamispaikkaa. Varsinainen kuva syntyy vasta monista janoista. Kun janoja kertyy miljoonia, ne leikkaavat tiheimmin siellä, missä merkkiainetta on eniten. Tietokone laskee janoista kuvan.

Fluori-18:n puoliintumisaika on lyhyt. Siksi se valmistetaan hiukkaskiihdyttimellä, syklotronilla, lähellä kuvauspaikkaa. Yksi tällainen paikka on Turun PET-keskus.

```pysahdy
PET-laitteen kaksi vastakkaista ilmaisinta havaitsee annihilaation fotonit $0{,}40\,\text{ns}$:n aikaerolla. Valo kulkee $30\,\text{cm}$ nanosekunnissa. Kuinka kaukana janan keskipisteestä lähde on ja kummalla puolella?
---
Myöhemmin havaittu fotoni kulkee ylimääräisen matkan $2x$: $2x = c\,\Delta t = 30\,\tfrac{\text{cm}}{\text{ns}} \cdot 0{,}40\,\text{ns} = 12\,\text{cm}$, joten $x = 6{,}0\,\text{cm}$. Lähde on $6{,}0\,\text{cm}$ keskipisteestä sen ilmaisimen puolella, joka havaitsi fotonin ensin.
```

### Sädehoito: suuri annos kasvaimeen, pieni terveelle kudokselle

**Sädehoito** on syövän hoitoa ionisoivalla säteilyllä. Suuri annos vaurioittaa syöpäsolujen DNA:ta niin paljon, että solut kuolevat. Tavallisimmin säteily tulee kehon ulkopuolelta lineaarikiihdyttimestä. Laite kiihdyttää elektronit miljooniin elektronivoltteihin ja jarruttaa ne röntgensäteilyksi.

Säteily kulkee aina myös terveen kudoksen läpi. Siksi kasvainta säteilytetään useasta suunnasta. Keilat leikkaavat kasvaimen kohdalla. Kasvain saa kaikkien keilojen annoksen. Terve kudos keilojen varrella saa vain osan kokonaisannoksesta. Hoito suunnitellaan TT-kuvan avulla.

<svg data-fig="sadehoito" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: sädehoito viidestä suunnasta. Potilaan poikkileikkauksen keskellä on kasvain. Viisi säteilykeilaa tulee kehon ulkopuolelta eri suunnista. Jokainen keila kulkee kasvaimen kautta. Keilat leikkaavat vain kasvaimen kohdalla. Siksi kasvain saa kaikkien viiden keilan annoksen: 5 kertaa 0,40 graytä eli 2,0 graytä. Terve kudos keilan varrella saa vain yhden keilan annoksen, noin 0,40 graytä." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-sadehoito.webp" x="1.2" y="0" width="597" height="369.4" preserveAspectRatio="none"/>
  <foreignObject x="440" y="109.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kasvain}$</div></foreignObject>
  <foreignObject x="440" y="141.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$2{,}0\,\text{Gy}$</div></foreignObject>
  <foreignObject x="440" y="229.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{terve kudos}$</div></foreignObject>
  <foreignObject x="440" y="261.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$0{,}40\,\text{Gy}$</div></foreignObject>
  <foreignObject x="452" y="25.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keila}$</div></foreignObject>
</svg>

Kuvan malli on yksinkertaistettu. Todellisessa hoidossa annos jakautuu kolmiulotteisesti. Keilan annos muuttuu syvyyden mukana, ja sironnut säteily osuu myös keilojen ulkopuolelle. Siksi terve kudos saa aina jonkin verran säteilyä. Hoitosuunnitelma tehdään niin, että kasvain saa riittävän annoksen. Terveen kudoksen ja erityisesti herkkien elinten annos pidetään mahdollisimman pienenä.

Hoito jaetaan yleensä moneen osaan. Tyypillisesti kasvain saa $2\,\text{Gy}$ kerrallaan arkipäivisin. Yhteensä annos on esimerkiksi $60\,\text{Gy}$ noin kuuden viikon aikana. Terveet solut korjaavat vaurioitaan hoitokertojen välillä paremmin kuin syöpäsolut.

Säteilylähde voidaan myös viedä kasvaimen sisään tai viereen. Toinen tapa on antaa potilaalle lääke, joka kertyy kasvaimeen merkkiaineen tapaan. Esimerkiksi kilpirauhassyövän hoidossa käytetään jodi-131:tä. Potilas voi niellä sen.

### Säteily teollisuudessa ja tutkimuksessa

Lääkintätarvikkeet, kuten ruiskut ja leikkauskäsineet, **steriloidaan** valmiissa pakkauksissaan. Sterilointi tarkoittaa, että mikrobit tapetaan. Siihen käytetään koboltti-60:n gammasäteilyä tai elektronisuihkua. Tavallinen annos on $25\,\text{kGy}$. Se tappaa mikrobit, vaikka se lämmittäisi vettä vain noin $6\,\text{K}$. Vaikutus perustuu siis ionisaatioon eikä lämpenemiseen. Tuote ei myöskään muutu radioaktiiviseksi.

Paperikoneen **paksuusmittarissa** beetasäteily kulkee paperiradan läpi ilmaisimeen. Mitä paksumpaa paperi on, sitä vähemmän säteilyä pääsee läpi. Mittarin lukema ohjaa koneen säätöä jatkuvasti. Samaan tapaan gammasäteilyllä mitataan teräslevyjä. Hitsaussaumoja kuvataan gammalähteellä.

<svg data-fig="mittari" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: paperikoneen paksuusmittari. Vaakasuora paperirata kulkee vasemmalta oikealle kahden telaparin välistä. Radan alapuolella on beetasäteilyn lähde. Siitä elektronit kulkevat sinisinä pisteinä ylöspäin paperin läpi. Osa elektroneista pysähtyy paperiin. Osa pääsee radan yläpuolella olevaan ilmaisimeen. Ilmaisimesta johto vie lukeman säätölaitteeseen. Säätölaite ohjaa telojen puristusta. Mitä paksumpi paperi on, sitä vähemmän säteilyä pääsee läpi." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-mittari.webp" x="1.2" y="0" width="597" height="348.3" preserveAspectRatio="none"/>
  <foreignObject x="142" y="83.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ilmaisin}$</div></foreignObject>
  <foreignObject x="126" y="243.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{lähde}\ (\beta^-)$</div></foreignObject>
  <foreignObject x="362" y="199.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paperirata}$</div></foreignObject>
  <foreignObject x="441" y="5.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säätö}$</div></foreignObject>
  <foreignObject x="127.5" y="301.5" width="345" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paksumpi paperi: vähemmän läpi}$</div></foreignObject>
</svg>

Kodin **savuilmaisimessa** on noin $37\,\text{kBq}$ amerikium-241:tä. Sen alfasäteily ionisoi ilmaa pienessä kammiossa, ja kammion läpi kulkee heikko sähkövirta. Savuhiukkaset sitovat ioneja, joten virta pienenee ja hälytin soi. Amerikium-241:n puoliintumisaika on $432\,\text{a}$. Kymmenessä vuodessa aktiivisuus pienenee siis vain noin $2\,\%$.

**Radiohiiliajoitus** perustuu siihen, että ilmakehässä syntyy jatkuvasti hiili-14:ää. Elävä eliö pitää hiili-14:n osuuden hiilestään samana. Kuoleman jälkeen hiili-14 hajoaa puoliintumisajalla $5700\,\text{a}$. Jäljellä olevasta osuudesta voi laskea eliön iän noin $50\,000$ vuoteen asti.

<figure class="unit-photo"><img src="pics/fy8/linear-accelerator.webp" alt="Sininen hoitohuone. Siinä on iso valkoinen laite ja hoitopöytä."><figcaption>Sädehoidon laite. Se tekee voimakasta röntgensäteilyä. Laite kiertää potilaan ympäri. Säteily osuu kasvaimeen monesta suunnasta. Terve kudos saa vähemmän säteilyä.</figcaption></figure>

### Potilaan ja henkilökunnan turvallisuus

Säteilylaki (859/2018) asettaa säteilyn käytölle kolme periaatetta.

**Oikeutus:** Tutkimuksesta tai hoidosta saatavan hyödyn on oltava suurempi kuin säteilyn haitta. Röntgentutkimus tehdään siksi vain, kun sen tulos vaikuttaa potilaan hoitoon.

**Optimointi:** Annos pidetään niin pienenä kuin käytännössä on mahdollista, kun kuva silti vastaa kysymykseen (ALARA, *as low as reasonably achievable*). Esimerkiksi lapsia kuvataan pienemmillä säädöillä kuin aikuisia.

**Annosrajat:** Säteilytyötä tekevän efektiivinen annos saa olla enintään $20\,\text{mSv}$ vuodessa. Potilaan annokseen annosrajoja ei sovelleta. Potilaan suojana ovat oikeutus ja optimointi.

Henkilökunta suojautuu ajalla, etäisyydellä ja suojalla (luku *Säteilyannos ja säteilyturvallisuus Suomessa*). Röntgenhoitaja käynnistää kuvauksen suojaseinän takaa. Kuvaushuoneessa käytetään lyijyesiliinaa. Merkkiainetta käsitellään lyijy- tai volframisuojatulla ruiskulla.

PET:n $511\,\text{keV}$:n fotonit läpäisevät lyijyä paljon paremmin kuin teknetium-$99\text{m}$:n $140\,\text{keV}$:n fotonit. Lyijyn puoliintumispaksuus on niille noin $3{,}9\,\text{mm}$ ja $0{,}26\,\text{mm}$. Säteilytyöntekijät kantavat annosmittaria. Säteilyn käyttöön tarvitaan Säteilyturvakeskuksen (STUK) turvallisuuslupa.

## Kaava: Vaimeneminen kerroksittain ja annihilaatio

### Säteily usean kerroksen läpi

Jokainen kudoskerros vaimentaa säteilyä puoliintumispaksuutensa mukaan (luku *Ionisoiva säteily ja elimistö*). Säde kulkee ensin pehmytkudoksen ja sitten luun läpi. Luun läpi pääsee sama osuus siitä säteilystä, joka pääsi pehmytkudoksen läpi. Osuudet siis kerrotaan:

```latex
I = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{kudos}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{luu}}
```

Tässä $I_0$ on säteeseen tulevan säteilyn intensiteetti. Intensiteetti on teho pinta-alaa kohti: se kertoo, kuinka paljon säteilyenergiaa osuu sekunnissa yhtä pinta-alayksikköä kohti. $I$ on kerrosten läpi päässeen säteilyn intensiteetti. Luku $n$ kertoo kerroksen paksuuden puoliintumispaksuuksina: $n_\text{kudos} = d_\text{kudos} : d_{1/2}^\text{kudos}$ ja $n_\text{luu} = d_\text{luu} : d_{1/2}^\text{luu}$. Tässä $d_\text{kudos}$ ja $d_\text{luu}$ ovat pehmytkudoksen ja luun paksuudet. Symbolit $d_{1/2}^\text{kudos}$ ja $d_{1/2}^\text{luu}$ ovat niiden puoliintumispaksuudet.

Koska $\left(\tfrac{1}{2}\right)^{n_\text{kudos}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{luu}} = \left(\tfrac{1}{2}\right)^{n_\text{kudos} + n_\text{luu}}$, voit myös laskea puoliintumispaksuuksien lukumäärät yhteen. Kerrosten järjestyksellä ei ole väliä. Kolmannelle kerrokselle tulee kolmas samanlainen tekijä.

Röntgenkuvan kontrasti saadaan vertaamalla kahta sädettä. Toinen säde kulkee pelkän pehmytkudoksen läpi, ja toinen kulkee myös luun läpi. Puoliintumispaksuus riippuu fotonien energiasta. Todellisessa röntgenputken säteilyssä on monen energian fotoneja. Siksi tässä käytetään keskimääräistä energiaa, joka on noin $60\,\text{keV}$.

<svg data-fig="kontrasti" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: läpi päässeen röntgensäteilyn osuus I per I nolla kerroksen paksuuden d funktiona. Paksuus on nollasta 8 senttimetriin. Fotonien energia on noin 60 kiloelektronivolttia. Pehmytkudoksessa osuus puolittuu jokaisen 3,4 senttimetrin kerroksen jälkeen. Luussa osuus puolittuu jo 1,1 senttimetrin jälkeen. Kohdassa 1,1 senttimetriä luun läpi pääsee puolet ja kohdassa 2,2 senttimetriä neljäsosa. Pehmytkudoksen läpi pääsee puolet vasta kohdassa 3,4 senttimetriä. Luun käyrä laskee siis paljon jyrkemmin." style="max-width:100%;font-size:24px">
  <line x1="146" y1="312" x2="146" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="312" x2="192.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="239" y1="312" x2="239" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="312" x2="285" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331" y1="312" x2="331" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="377.5" y1="312" x2="377.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424" y1="312" x2="424" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="312" x2="470" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="253" x2="470" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="194.5" x2="470" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="135.5" x2="470" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="77" x2="470" y2="77" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="484" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,312 L483,318 L483,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="146" y1="312" x2="146" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="136" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="192.5" y1="312" x2="192.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="182.5" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="239" y1="312" x2="239" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="229" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="285" y1="312" x2="285" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="275" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="331" y1="312" x2="331" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="321" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="377.5" y1="312" x2="377.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367.5" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="424" y1="312" x2="424" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="414" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="470" y1="312" x2="470" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="93" y1="253" x2="100" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="238.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}25$</div></foreignObject>
  <line x1="93" y1="194.5" x2="100" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="180" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}50$</div></foreignObject>
  <line x1="93" y1="135.5" x2="100" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="121" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}75$</div></foreignObject>
  <line x1="93" y1="77" x2="100" y2="77" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="62.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="297.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{cm})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I : I_0$</div></foreignObject>
  <polyline points="100,77 103,80 106,83 109,86 112.5,89.5 115.5,92.5 118.5,95 121.5,98 124.5,101 128,104 131,106.5 134,109.5 137,112 140,115 143,117.5 146,120 149.5,123 152.5,125.5 155.5,128 158.5,130.5 161.5,133 165,135 168,137.5 171,140 174,142.5 177,144.5 180,147 183,149 186.5,151.5 189.5,153.5 192.5,155.5 195.5,157.5 198.5,160 202,162 205,164 208,166 211,168 214,170 217,171.5 220,173.5 223.5,175.5 226.5,177.5 229.5,179 232.5,181 235.5,182.5 239,184.5 242,186 245,188 248,189.5 251,191 254,193 257,194.5 260.5,196 263.5,197.5 266.5,199 269.5,200.5 272.5,202 276,203.5 279,205 282,206.5 285,208 288,209.5 291,210.5 294,212 297.5,213.5 300.5,215 303.5,216 306.5,217.5 309.5,218.5 313,220 316,221 319,222.5 322,223.5 325,225 328,226 331,227 334.5,228.5 337.5,229.5 340.5,230.5 343.5,231.5 346.5,232.5 350,234 353,235 356,236 359,237 362,238 365,239 368,240 371.5,241 374.5,242 377.5,243 380.5,243.5 383.5,244.5 387,245.5 390,246.5 393,247.5 396,248 399,249 402,250 405,251 408.5,251.5 411.5,252.5 414.5,253 417.5,254 420.5,255 424,255.5 427,256.5 430,257 433,258 436,258.5 439,259.5 442,260 445.5,260.5 448.5,261.5 451.5,262 454.5,262.5 457.5,263.5 461,264 464,264.5 467,265.5 470,266" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="100,77 103,86.5 106,96 109,104.5 112.5,113 115.5,121.5 118.5,129 121.5,136.5 124.5,144 128,151 131,157.5 134,164 137,170 140,176 143,181.5 146,187 149.5,192 152.5,197 155.5,201.5 158.5,206 161.5,210.5 165,214.5 168,218.5 171,222.5 174,226 177,229.5 180,233 183,236.5 186.5,239.5 189.5,242.5 192.5,245.5 195.5,248 198.5,250.5 202,253 205,255.5 208,258 211,260 214,262.5 217,264.5 220,266.5 223.5,268 226.5,270 229.5,271.5 232.5,273.5 235.5,275 239,276.5 242,278 245,279.5 248,280.5 251,282 254,283 257,284.5 260.5,285.5 263.5,286.5 266.5,287.5 269.5,288.5 272.5,289.5 276,290.5 279,291.5 282,292.5 285,293 288,294 291,294.5 294,295.5 297.5,296 300.5,296.5 303.5,297.5 306.5,298 309.5,298.5 313,299 316,299.5 319,300 322,300.5 325,301 328,301.5 331,302 334.5,302.5 337.5,302.5 340.5,303 343.5,303.5 346.5,304 350,304 353,304.5 356,305 359,305 362,305.5 365,305.5 368,306 371.5,306 374.5,306.5 377.5,306.5 380.5,307 383.5,307 387,307.5 390,307.5 393,307.5 396,308 399,308 402,308 405,308.5 408.5,308.5 411.5,308.5 414.5,309 417.5,309 420.5,309 424,309 427,309.5 430,309.5 433,309.5 436,309.5 439,309.5 442,310 445.5,310 448.5,310 451.5,310 454.5,310 457.5,310 461,310.5 464,310.5 467,310.5 470,310.5" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="257" y1="194.5" x2="257" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="257" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="257" cy="194.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <line x1="151" y1="194.5" x2="151" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="151" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="151" cy="194.5" r="6.5" fill="#a97a35" stroke="#ffffff" stroke-width="2"/>
  <line x1="202" y1="253" x2="202" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="253" x2="202" y2="253" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="202" cy="253" r="6.5" fill="#a97a35" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="77" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="329" y="189.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{pehmytkudos}$</span></div></foreignObject>
  <foreignObject x="109" y="213" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{luu}$</span></div></foreignObject>
  <foreignObject x="266.5" y="81" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$</span></div></foreignObject>
  <foreignObject x="276.5" y="151.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 3{,}4\,\text{cm}$</span></div></foreignObject>
  <foreignObject x="299" y="262" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 1{,}1\,\text{cm}$</span></div></foreignObject>
</svg>

```pysahdy
Röntgensäde kulkee pehmytkudoksen läpi kahden puoliintumispaksuuden matkan. Sen jälkeen se kulkee luun läpi yhden puoliintumispaksuuden matkan. Kuinka suuri osa säteilystä pääsee läpi?
---
Puoliintumispaksuuksien lukumäärät lasketaan yhteen: $\left(\tfrac{1}{2}\right)^{2+1} = \tfrac{1}{8}$. Läpi pääsee siis $12{,}5\,\%$.
```

### Annihilaatiofotonin energia

Positroni ja elektroni annihiloituvat lähes levossa. Niiden yhteinen massa $2m_e$ muuttuu kokonaan fotonien energiaksi (luku *Massavaje ja ytimen sidosenergia*). Alussa liikemäärä on lähes nolla. Siksi fotoneja syntyy kaksi, ne lähtevät lähes vastakkaisiin suuntiin ja niillä on likimain sama energia:

```latex
E_\gamma = m_e c^2
```

Tässä $E_\gamma$ on yhden fotonin energia ($\text{J}$). Massa $m_e = 9{,}109 \cdot 10^{-31}\,\text{kg}$ on elektronin ja positronin massa. Nopeus $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ on valon nopeus. Sijoittamalla saadaan $$
\begin{aligned}
&E_\gamma \\
&= 9{,}109 \cdot 10^{-31}\,\text{kg} \\
&\cdot (2{,}998 \cdot 10^{8}\,\text{m/s})^2 \\
&= 8{,}187 \cdot 10^{-14}\,\text{J}
\end{aligned}
$$.

Kun sijoitetaan $1\,\text{J} = \tfrac{1}{1{,}602 \cdot 10^{-19}}\,\text{eV}$, saadaan $$
\begin{aligned}
E_\gamma &= 8{,}187 \cdot 10^{-14} \\
&\cdot \tfrac{1}{1{,}602 \cdot 10^{-19}}\,\text{eV} \\
&= 5{,}11 \cdot 10^{5}\,\text{eV} \\
&= 511\,\text{keV}
\end{aligned}
$$. Energia on noin $150\,000$-kertainen näkyvän valon fotoniin verrattuna. Energia on sama jokaisessa annihilaatiossa. PET-laite voi siksi hylätä fotonit, joiden energia poikkeaa siitä selvästi, koska ne ovat sironneet eli muuttaneet suuntaa matkalla.

## Esimerkki

Kyynärvarren röntgenkuvassa säde A kulkee $8{,}0\,\text{cm}$ pehmytkudosta. Säde B kulkee $5{,}0\,\text{cm}$ pehmytkudosta ja $3{,}0\,\text{cm}$ luuta. Säteilyn keskimääräinen energia on noin $60\,\text{keV}$. Sillä pehmytkudoksen puoliintumispaksuus on $3{,}4\,\text{cm}$ ja luun $1{,}1\,\text{cm}$. Kuinka monta kertaa suurempi intensiteetti osuu ilmaisimeen säteen A kohdalla kuin säteen B kohdalla?

<!-- vaihe -->

**Tunnetut ja kysytty.** Säde A: pehmytkudosta $d_\text{A} = 8{,}0\,\text{cm}$. Säde B: pehmytkudosta $d_\text{kudos} = 5{,}0\,\text{cm}$ ja luuta $d_\text{luu} = 3{,}0\,\text{cm}$. Puoliintumispaksuudet ovat $d_{1/2}^\text{kudos} = 3{,}4\,\text{cm}$ ja $d_{1/2}^\text{luu} = 1{,}1\,\text{cm}$.

Kysytään intensiteettien suhdetta ${I_\text{A} : I_\text{B}}$.

<!-- vaihe -->

**Periaate.** Kumpaankin säteeseen tulee sama intensiteetti $I_0$. Jokainen kerros päästää läpi osuuden $\left(\tfrac{1}{2}\right)^{n}$ siihen tulevasta säteilystä. Tässä $n$ on kerroksen paksuus puoliintumispaksuuksina. Säteen B osuudet kerrotaan, eli sen puoliintumispaksuuksien lukumäärät lasketaan yhteen. Suhteessa $I_0$ supistuu pois.

<!-- vaihe -->

**Kaava ratkaistuna.** Säteelle A $n_\text{A} = d_\text{A} : d_{1/2}^\text{kudos}$ ja säteelle B $n_\text{B} = d_\text{kudos} : d_{1/2}^\text{kudos} + d_\text{luu} : d_{1/2}^\text{luu}$. Kun $I_\text{A} = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{A}}$ ja $I_\text{B} = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{B}}$, suhde on

```latex
\begin{aligned}
\frac{I_\text{A}}{I_\text{B}} &= \frac{I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{A}}}{I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{B}}} \\
&= 2^{\,n_\text{B} - n_\text{A}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Kaikki paksuudet ovat senttimetreinä, joten lukumäärien $n$ yksiköt supistuvat pois.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin puoliintumispaksuuksien lukumäärät:

```latex
\begin{aligned}
n_\text{A} &= d_\text{A} : d_{1/2}^\text{kudos} \\
&= 8{,}0\,\text{cm} : 3{,}4\,\text{cm} = 2{,}353
\end{aligned}
```

```latex
\begin{aligned}
n_\text{B} &= d_\text{kudos} : d_{1/2}^\text{kudos} + d_\text{luu} : d_{1/2}^\text{luu} \\
&= 5{,}0\,\text{cm} : 3{,}4\,\text{cm} \\
&\quad + 3{,}0\,\text{cm} : 1{,}1\,\text{cm} \\
&= 1{,}471 + 2{,}727 = 4{,}198
\end{aligned}
```

Suhde on

```latex
\begin{aligned}
\frac{I_\text{A}}{I_\text{B}} &= 2^{\,n_\text{B} - n_\text{A}} \\
&= 2^{\,4{,}198 - 2{,}353} \\
&= 2^{\,1{,}845} = 3{,}59
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Säteen A kohdalla ilmaisimeen osuu noin $3{,}6$-kertainen intensiteetti. Vastauksessa on kaksi merkitsevää numeroa, koska paksuuksissa ja puoliintumispaksuuksissa on kaksi merkitsevää numeroa. Luu näkyy siksi kuvassa selvästi vaaleampana kuin pelkkä pehmytkudos.

<!-- vaihe -->

**Järkevyys.** Lasketaan sama toista tietä, läpi päässeiden osuuksien kautta. Nyt $\left(\tfrac{1}{2}\right)^{2{,}353} = 0{,}1957$ ja $\left(\tfrac{1}{2}\right)^{4{,}198} = 0{,}05449$. Siis $I_\text{A} : I_\text{B} = 0{,}1957 : 0{,}05449 = 3{,}59$, kuten edellä. Suhde on myös suuruusluokaltaan järkevä. Säteellä B on noin kaksi puoliintumispaksuutta enemmän, ja $2^2 = 4$.

## Yleinen virhekäsitys

Moni ajattelee, että röntgenkuvauksen jälkeen potilaasta lähtee säteilyä. Näin ei ole. Röntgensäteily syntyy vain silloin, kun putkessa kulkee virta. Säteily loppuu heti, kun putki sammutetaan. Potilaaseen ei jää mitään radioaktiivista.

Isotooppitutkimuksessa tilanne on toinen. Merkkiaine on potilaan elimistössä, ja se säteilee, kunnes se on hajonnut tai poistunut. Siihen menee yleensä tunteja tai vuorokausi. Siksi PET-potilas odottaa kuvausta omassa huoneessaan, ja hoitajat pysyttelevät hänestä etäällä.

Toinen virhe on ajatella, että säteilysuojelu tarkoittaa mahdollisimman pientä annosta hinnalla millä hyvänsä. Jos annos on liian pieni, kuva jää kohinaiseksi. Kohina tarkoittaa, että kuvassa on satunnaisia häiriöitä. Kuvasta ei silloin näe sitä, mitä etsittiin. Tutkimus joudutaan uusimaan, ja potilas saa kaksi annosta. Optimointi tarkoittaa pienintä annosta, jolla kuva vastaa kysymykseen.

## Tiivistelmä

- Röntgensäteily syntyy, kun nopeat elektronit jarruttavat anodissa tai irrottavat elektroneja anodin atomien sisäkuorilta. Jännite $U$ antaa fotonille enintään energian $eU$.
- Röntgenkuvan ja TT-kuvan kontrasti syntyy siitä, että luu vaimentaa säteilyä enemmän kuin pehmytkudos. Kerrosten läpi pääsevät osuudet kerrotaan: $I = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{kudos}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{luu}}$, missä $n = d : d_{1/2}$.
- Merkkiaine kertyy tutkittavaan elimeen. Teknetium-$99\text{m}$ lähettää $140\,\text{keV}$:n gammasäteilyä, ja sen puoliintumisaika on $6{,}01\,\text{h}$.
- PET: positroni ja elektroni annihiloituvat kahdeksi lähes vastakkaiseksi fotoniksi, joiden energia on $E_\gamma = m_e c^2 = 511\,\text{keV}$. Koinsidenssi antaa janan, ja monien janojen leikkauskohdat paljastavat merkkiaineen paikan.
- Sädehoidossa kasvainta säteilytetään useasta suunnasta ja moneen osaan jaettuna. Silloin kasvain saa suuren annoksen ja terve kudos pienen.
- Säteilyä käytetään myös sterilointiin, paksuusmittareihin, savuilmaisimiin ja radiohiiliajoitukseen.
- Säteilyn käytön periaatteet ovat oikeutus, optimointi ja annosrajat. Henkilökunta suojautuu ajalla, etäisyydellä ja suojalla.
