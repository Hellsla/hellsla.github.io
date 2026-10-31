Graphical Analysis Pron taulukossa jokainen suure on oma sarakkeensa. Laskettu sarake laskee uuden suureen kaikille riveille yhdellä lausekkeella, ja kuvaaja päivittyy samalla.

## Mihin tarvitset tätä

Tutkimuksessa *Putoamiskiihtyvyyden määrittäminen heilurin avulla* lasket jaksonajan neliön jokaiselle pituudelle, ja tutkimuksessa *Hissin kulkema matka kiihtyvyydestä* lasket tuhansista kiihtyvyyslukemista nopeuden ja matkan. Tutkimuksessa *Liikemäärän säilyminen törmäyksissä* sama lauseke lasketaan monelle törmäykselle.

## Työvaiheet

1. **Aloita uusi koe.** Valitse **Manual Entry**, kun kirjoitat mittaukset itse, tai **Sensor Data Collection**, kun anturi mittaa ([[ohje:tvt-mittausohjelma|Anturit ja mittausohjelma]]).

2. **Nimeä sarake ja anna sille yksikkö.** Avaa sarakkeen nimen vierestä **Column Options**. Kirjoita nimeksi suureen tunnus, esimerkiksi `l`, ja yksiköksi `m`. Valitse samasta kohdasta näytettävä tarkkuus niin, että luvut näkyvät mittauksen tarkkuudella. Kuvaajan akselin otsikko tulee sarakkeen nimestä ja yksiköstä.

3. **Kirjoita mittaukset.** Kaksoisnapsauta solua ja kirjoita luku, yksi mittaus riville. Lisää jokaiselle uudelle mitatulle suureelle oma sarakkeensa valinnalla **Add Manual Column**.

4. **Pidä mitatut arvot koskemattomina.** Älä muuta mitattuja lukuja. Laskettu suure saa oman sarakkeensa. Jos jätät jonkin pisteen pois sovituksesta, kirjaa piste ja syy, mutta älä poista riviä.

5. **Laske uusi sarake lausekkeella.** Valitse **Add Calculated Column**, anna sarakkeelle nimi ja yksikkö ja kirjoita lauseke. Lausekkeessa sarakkeen nimi on lainausmerkeissä: jaksonajan neliö on `"T"^2`, neliöjuuri `sqrt("h")` ja etäisyyden neliön käänteisluku `1/"r"^2`. Laskutoimitukset ovat `+ - * / ^`, ja funktion argumentit ovat suluissa. Oma lauseke on Pro-ominaisuus. Ohjelma laskee sarakkeen kaikille riveille ja laskee sen uudelleen, jos korjaat mitattua arvoa. Tarkista yksi rivi laskimella.

    <svg data-fig="sheet" viewBox="0 0 600 372" role="img" aria-label="Kaaviokuva mittausohjelman datataulukosta keksityin esimerkkiarvoin. Ensimmäisen sarakkeen otsikko on l metreinä ja toisen T sekunteina; niissä ovat mitatut arvot. Kolmas sarake on laskettu sarake, jonka otsikko on T toiseen sekunnin neliöinä. Sen yläpuolella näkyy sarakkeen lauseke: T lainausmerkeissä potenssiin kaksi. Kolmannella rivillä laskettu arvo näkyy pyöristämättömänä, 1,6129." style="max-width:100%;font-size:24px">
  <foreignObject x="192.5" y="25.5" width="295" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{laskettu sarake, lauseke:}$</div></foreignObject>
  <rect x="340" y="64" width="180" height="38" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="354" y="68.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\texttt{"T"\textasciicircum 2}$</div></foreignObject>
  <line x1="430" y1="102" x2="430" y2="120" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="120" width="480" height="44" fill="#e3dccb"/>
  <rect x="340" y="164" width="180" height="120" fill="#eef5f9"/>
  <line x1="40" y1="120" x2="40" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="190" y1="120" x2="190" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="120" x2="340" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="120" x2="520" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="204" x2="520" y2="204" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="244" x2="520" y2="244" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="40" y1="164" x2="520" y2="164" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="120" width="480" height="164" fill="none" stroke="#c9c2b2" stroke-width="2"/>
  <foreignObject x="84" y="127.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="234" y="127.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T\ (\text{s})$</div></foreignObject>
  <foreignObject x="386.5" y="127.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <foreignObject x="104" y="169.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}200$</div></foreignObject>
  <foreignObject x="266" y="169.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}90$</div></foreignObject>
  <foreignObject x="446" y="169.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}81$</div></foreignObject>
  <foreignObject x="104" y="209.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}300$</div></foreignObject>
  <foreignObject x="266" y="209.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}10$</div></foreignObject>
  <foreignObject x="446" y="209.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}21$</div></foreignObject>
  <foreignObject x="104" y="249.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}400$</div></foreignObject>
  <foreignObject x="266" y="249.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}27$</div></foreignObject>
  <foreignObject x="421" y="249.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}6129$</div></foreignObject>
  <line x1="44" y1="300" x2="336" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="44" y1="292" x2="44" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336" y1="292" x2="336" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="111" y="307.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{mitatut arvot}$</div></foreignObject>
  <line x1="344" y1="300" x2="516" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="344" y1="292" x2="344" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="516" y1="292" x2="516" y2="300" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="376" y="307.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{laskettu}$</div></foreignObject>
  <foreignObject x="40" y="68.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{esimerkkiarvoja}$</div></foreignObject>
</svg>

6. **Kirjoita vakio lukuna.** Lausekkeessa ei voi käyttää muuttuvia parametreja, kuten $A$ tai $B$, joten kirjoita vakio lukuarvona. Esimerkiksi painon $G = mg$ lauseke on `"m"*9.81`, kun massa on kilogrammoina. Jos ohjelma ei hyväksy desimaalipistettä, kokeile pilkkua. Trigonometriset funktiot käyttävät radiaaneja, joten muunna asteina mitattu kulma ensin radiaaneiksi.

7. **Laske muutos ja kertyvä summa.** Lauseke `delta("x")` antaa rivin arvon ja edellisen rivin arvon erotuksen, joten ensimmäinen rivi jää tyhjäksi. Lauseke `sum("x")` laskee sarakkeen arvot yhteen ensimmäisestä rivistä nykyiseen riviin asti eli antaa kertyvän summan.

8. **Laske pinta-ala kuvaajan alla.** Lauseke `integral("a","t")` laskee $(t, a)$-kuvaajan ja aika-akselin välisen pinta-alan alusta nykyiseen riviin asti: se laskee kahden peräkkäisen rivin välisen kapean suikaleen alan ja lisää sen aiempien suikaleiden summaan. Kiihtyvyydestä saat näin nopeuden, ja kun lasket nopeussarakkeesta `integral("v","t")`, saat matkan. Kirjoita sarakkeiden nimet lausekkeeseen täsmälleen kuten taulukossa. Periaate on selitetty ohjeessa [[ohje:tvt-nopeus-datasta|Nopeuden ja matkan määrittäminen mittausdatasta]].

9. **Tuo data puhelimesta.** Puhelimen mittaussovellus tallentaa mittauksen usein CSV-tiedostona. Graphical Analysis Pro avaa CSV-tiedoston, tai voit kopioida sarakkeet ja liittää ne taulukkoon (Ctrl+C ja Ctrl+V, macOS:ssä Cmd). Tarkista sen jälkeen sarakkeiden nimet ja yksiköt ja se, että pisteet näkyvät kuvaajassa.

10. **Tallenna ja vie data.** Tallenna koe ohjelman omana tiedostona (.gambl), jolloin lasketut sarakkeet säilyvät. Valinta **Export data as csv** vie taulukon CSV-tiedostoksi esimerkiksi työselostuksen liitteeksi. Kuvaajan ja suoran sovituksen ohjeet ovat [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-suoran-sovitus|Suoran sovittaminen mittauspisteisiin]].

## Ohjelmakohtaisia vinkkejä

- **Pro-ominaisuudet.** Omat lausekkeet, käsin säädettävä suora, sovitusparametrien epävarmuus ja video ovat vain Pro-versiossa. Jos et löydä lausekkeen kirjoituskenttää, kysy opettajalta, onko käytössäsi Pro-versio.
- **Useampi mittaussarja.** Käsin syötettävässä kokeessa saat uuden sarjan valikosta **Data Set Options** valinnalla **Add New Data Set** ja nimeät sen valinnalla **Rename Data Set**, esimerkiksi "jousi 1".
- **Väärä sarake.** **Delete Column** poistaa sarakkeen. Poista vain itse tekemäsi laskettu sarake, älä mitattua.

## Tavallisimmat virheet

- **Sarakkeen nimi on lausekkeessa väärin.** Lauseke antaa virheilmoituksen tai tyhjän sarakkeen. Kirjoita nimi lainausmerkkeihin täsmälleen kuten sarakkeen otsikossa.
- **Liitetyt luvut eivät ole lukuja.** Pisteet eivät näy kuvaajassa, tai sarake on tyhjä. Syy on yleensä desimaalierotin: CSV-tiedostossa se on usein piste.
- **Lasketulla sarakkeella ei ole yksikköä.** Akselin otsikosta puuttuu yksikkö. Anna yksikkö valinnassa **Column Options**.
- **Kulma on lausekkeessa asteina.** Sinin tai kosinin arvot ovat järjettömiä. Muunna kulma radiaaneiksi.
- **Mitatut arvot on korvattu lasketuilla.** Laskua ei voi enää tarkistaa. Pidä mitatut arvot omissa sarakkeissaan.

## Tarkista ennen kuin jatkat

- Jokaisella sarakkeella on nimi ja yksikkö.
- Mitatut arvot ovat muuttamattomina omissa sarakkeissaan.
- Laskettu sarake on tarkistettu yhdeltä riviltä laskimella.
- Koe on tallennettu, ja data on viety CSV-tiedostoksi, jos sitä tarvitaan muualla.
