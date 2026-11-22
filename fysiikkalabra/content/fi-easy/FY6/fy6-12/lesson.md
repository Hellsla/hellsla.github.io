# Potentiaalienergia ja potentiaali sähkökentässä

> **Miksi** revontulissa yläilmakehään syöksyvät elektronit ovat niin nopeita, että ne saavat ilman hehkumaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: revontulet talvisen Lapin yllä. Tummalla tähtitaivaalla kaartuu vihreitä revontuliverhoja. Verhojen pystysuorat säteet hehkuvat kirkkaimmin alareunastaan. Alhaalla on lumisia tuntureita, kuusikko ja punainen mökki. Mökin ikkunasta loistaa lämmin valo." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Sähkökenttä tekee työtä kuten painovoima
Homogeenisessa sähkökentässä varattuun hiukkaseen vaikuttaa kaikkialla levyjen välissä sama voima $\overline{F} = q\overline{E}$ (luku *Homogeeninen sähkökenttä*). Tilanne muistuttaa painovoimaa maan pinnan lähellä. Siellä pallon paino $m\overline{g}$ on sama joka korkeudella. Kun pallo putoaa korkeudelta $h$, paino tekee työn $W = mgh$. Pallon potentiaalienergia eli paikan mukaan muuttuva energia muuttuu liike-energiaksi (luku *Liike-energia, potentiaalienergia ja mekaaninen energia*). Samalla tavalla toimii sähkökenttä. Positiivinen varaus $q$ kulkee positiiviselta levyltä negatiiviselle levylle kentän suuntaan matkan $d$. Silloin sähköinen voima tekee työn $W = Fd = qEd$. Voima ja siirtymä ovat samansuuntaiset, joten työ on positiivinen.

<svg data-fig="kentta" viewBox="0 0 600 340" role="img" aria-label="Kaksi rinnakkaista kaavakuvaa, ei mittakaavassa. Vasemmalla pallo on korkeudella h maanpinnan yläpuolella. Siihen vaikuttaa alaspäin punainen painovoima m kertaa g. Kun pallo putoaa maahan, painovoima tekee työn W = mgh. Oikealla on kaksi vaakasuoraa metallilevyä: ylempi on positiivinen ja alempi negatiivinen. Levyjen väli on d. Levyjen välissä on homogeeninen sähkökenttä E, ja sen kenttäviivat osoittavat alaspäin. Positiiviseen levyyn on kiinni positiivinen varaus q. Siihen vaikuttaa alaspäin punainen voima q kertaa E. Kun varaus kulkee levystä toiseen, sähköinen voima tekee työn W = qEd." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-kentta.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="124" y="133.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$m\overline{g}$</div></foreignObject>
  <foreignObject x="226" y="162.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="80" y="291.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = mgh$</div></foreignObject>
  <foreignObject x="306" y="53.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="306" y="253.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="384" y="181.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="452" y="133.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$q\overline{E}$</div></foreignObject>
  <foreignObject x="574" y="153.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="380" y="291.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = qEd$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lightning-dallas.webp" alt="Yötaivas ja ukkospilvi. Salama kulkee pilvestä alas maassa olevaan mastoon."><figcaption>Salama iskee mastoon. Pilven ja maan välillä on hyvin suuri potentiaaliero, jopa satoja miljoonia voltteja. Kun varaus purkautuu, sähköinen potentiaalienergia muuttuu valoksi ja ääneksi. Lisäksi ilman sisäenergia kasvaa, ja tämä energia siirtyy lämpönä ympäristöön.</figcaption></figure>

### Sähköinen potentiaalienergia
Sähköinen voima on konservatiivinen kuten painovoima. Se tarkoittaa, että voiman tekemä työ riippuu vain alkukohdasta ja loppukohdasta, ei reitistä. Siksi varauksella on kentässä **potentiaalienergiaa** $E_\text{p}$, joka riippuu varauksen paikasta. Kun kenttä tekee positiivista työtä, potentiaalienergia pienenee saman verran. Kun varausta siirretään kentän voimaa vastaan, potentiaalienergia kasvaa. Potentiaalienergian nollatason saa valita vapaasti, kuten korkeuden nollatason. Usein nollataso on negatiivinen levy tai maadoitettu kohta. Tärkeitä ovat vain potentiaalienergian muutokset, eivätkä ne riipu nollatason valinnasta.

```pysahdy
Vaikuttaako nollatason valinta siihen, kuinka paljon työtä kenttä tekee, kun varaus siirtyy kohdasta toiseen?
---
Ei vaikuta. Kentän tekemä työ on potentiaalienergian vähenemä, $W = -\Delta E_\text{p}$. Nollatason siirto muuttaa alku- ja loppuenergiaa yhtä paljon. Siksi erotus pysyy samana.
```

### Potentiaali: energia varausyksikköä kohti
Kaksinkertaiseen varaukseen vaikuttaa kaksinkertainen voima, joten samassa kohdassa sillä on kaksinkertainen potentiaalienergia. Suhde $E_\text{p} : q$ ei siis riipu varauksesta. Se kuvaa kentän kohtaa. Tätä suhdetta sanotaan kohdan **potentiaaliksi** $V$, ja sen yksikkö on $1\,\text{J/C} = 1\,\text{V}$. Tämä on sama potentiaali kuin luvussa *Kirchhoffin lait ja potentiaali virtapiirissä*: kohdan jännite valittuun nollakohtaan nähden. Kahden kohdan **potentiaaliero** on niiden välinen jännite.

Levyjen välissä potentiaali kasvaa tasaisesti negatiivisesta levystä positiiviseen levyyn. Kun negatiivinen levy on nollakohta, positiivisen levyn potentiaali on levyjen välinen jännite $U$. Kenttä osoittaa aina suuremmasta potentiaalista pienempään. Kohdat, joilla on sama potentiaali, muodostavat **tasapotentiaalipinnan**. Levyjen välissä tasapotentiaalipinnat ovat levyjen suuntaisia tasoja. Kenttäviivat ovat niitä vastaan kohtisuorassa eli suorassa kulmassa. Kun varausta siirretään tasapotentiaalipintaa pitkin, kenttä ei tee työtä, koska voima on kohtisuorassa siirtymää vastaan.

<svg data-fig="tasapotentiaali" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva mittakaavassa: kaksi vaakasuoraa metallilevyä on 4,0 senttimetrin päässä toisistaan. Ylempi levy on positiivinen, ja sen potentiaali on 200 V. Alempi levy on negatiivinen nollakohta 0 V. Levyjen välissä ovat harmaat katkoviivat, joiden potentiaalit ovat 150 V, 100 V ja 50 V. Viivojen väli on 1,0 senttimetriä. Vihreät kenttäviivat E osoittavat ylhäältä alas ja leikkaavat katkoviivat kohtisuorasti. Potentiaali pienenee kentän suuntaan 50 V jokaisella senttimetrillä." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-12-tasapotentiaali.webp" x="35.5" y="4.7" width="568.7" height="332.9" preserveAspectRatio="none"/>
  <foreignObject x="70" y="100.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="155.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="210.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="45.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="70" y="265.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="242" y="128" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="512" y="238" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1{,}0\,\text{cm}$</div></foreignObject>
  <foreignObject x="512" y="73" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{V}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/lightning-strikes.webp" alt="Sininen iltataivas tasaisen maan yllä. Kaukana on monta salamaa."><figcaption>Salamoita illalla. Pilven alaosassa on yleensä negatiivinen varaus. Sen potentiaali on pienempi kuin maan. Salamassa elektronit liikkuvat kohti suurempaa potentiaalia. Silloin niiden potentiaalienergia pienenee.</figcaption></figure>

### Positiivinen ja negatiivinen varaus
Positiivinen varaus lähtee levosta liikkeelle kentän suuntaan eli kohti pienempää potentiaalia. Sen potentiaalienergia pienenee. Elektronin varaus on negatiivinen, $q = -e$, joten siihen vaikuttava voima osoittaa kenttää vastaan. Elektroni lähtee siis kohti suurempaa potentiaalia. Silloinkin sen potentiaalienergia pienenee, koska negatiivisen varauksen potentiaalienergia on sitä pienempi, mitä suurempi potentiaali on. Samassa $150\,\text{V}$:n kohdassa protonin potentiaalienergia on positiivinen ja elektronin negatiivinen. **Kumpikin varaus lähtee levosta liikkeelle suuntaan, jossa sen potentiaalienergia pienenee**, kuten pallo putoaa alaspäin.

### Elektronivoltti
Hiukkasen varauksen suuruus on alkeisvaraus $e$. Kun hiukkanen kulkee potentiaalieron $U$ läpi, kenttä tekee työn $eU$. Jos vain sähköinen voima tekee työtä, hiukkasen liike-energia kasvaa saman verran. Hiukkasten energiat ilmoitetaan siksi usein **elektronivoltteina** ($\text{eV}$). Yksi elektronivoltti on energia, jonka alkeisvarauksen suuruinen varaus saa, kun se kulkee $1\,\text{V}$:n potentiaalieron läpi. Protoni ja elektroni kulkevat levosta $200\,\text{V}$:n potentiaalieron läpi. Kumpikin saa liike-energiaa $200\,\text{eV}$, vaikka ne liikkuvat vastakkaisiin suuntiin. Kummallakin liike-energian ja potentiaalienergian summa pysyy samana koko matkan.

```pysahdy
Alkeisvarauksen suuruinen varaus lähtee levosta ja kulkee $45\,\text{V}$:n potentiaalieron läpi. Kuinka suuri liike-energia sillä on elektronivoltteina?
---
Jos vain sähköinen voima tekee työtä, liike-energia on $eU$ eli $45\,\text{eV}$.
```

<svg data-fig="energia" viewBox="0 0 600 380" role="img" aria-label="Pylväskuvaaja mittakaavassa: energia elektronivoltteina, kun hiukkanen lähtee levosta ja kulkee levyjen välisen 200 voltin potentiaalieron läpi. Vasemmalla on protoni, joka lähtee positiiviselta levyltä. Alussa sen potentiaalienergia on 200 eV ja liike-energia nolla. Lopussa negatiivisella levyllä potentiaalienergia on nolla ja liike-energia 200 eV. Oikealla on elektroni, joka lähtee negatiiviselta levyltä. Alussa kumpikin energia on nolla. Lopussa positiivisella levyllä potentiaalienergia on miinus 200 eV ja liike-energia 200 eV. Kummallakin hiukkasella energioiden summa pysyy samana. Potentiaalienergian pylväät ovat tummia ja liike-energian pylväät oransseja." style="max-width:100%;font-size:24px">
  <line x1="78" y1="306" x2="78" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M78,50 L84,63 L72,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="68" y="19.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{eV})$</div></foreignObject>
  <line x1="71" y1="70" x2="78" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="55.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="71" y1="180" x2="78" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="165.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="71" y1="290" x2="78" y2="290" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="12" y="275.5" width="54" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-200$</div></foreignObject>
  <line x1="78" y1="180" x2="584" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="338" y1="24" x2="338" y2="366" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="181" y="15.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{protoni}$</div></foreignObject>
  <rect x="108" y="70" width="42" height="110" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="107" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <line x1="158" y1="180" x2="200" y2="180" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="157" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="99" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alussa}$</div></foreignObject>
  <line x1="230" y1="180" x2="272" y2="180" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="229" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="280" y="70" width="42" height="110" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="279" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="221" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lopussa}$</div></foreignObject>
  <foreignObject x="435" y="15.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{elektroni}$</div></foreignObject>
  <line x1="362" y1="180" x2="404" y2="180" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="361" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <line x1="412" y1="180" x2="454" y2="180" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <foreignObject x="411" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="353" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alussa}$</div></foreignObject>
  <rect x="484" y="180" width="42" height="110" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="483" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="534" y="70" width="42" height="110" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="533" y="305.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="475" y="337.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lopussa}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/plasma-lamp.webp" alt="Plasmapallo pimeässä. Keskeltä lähtee violetteja ja punaisia valonauhoja lasiin asti."><figcaption>Plasmapallon keskellä on suuri jännite, monta kilovolttia. Kaasun elektronit kiihtyvät sähkökentässä. Kun ne törmäävät kaasun atomeihin, atomit lähettävät valoa. Revontulet syntyvät samalla tavalla.</figcaption></figure>

### Revontulet
Maan magneettikenttä ohjaa avaruudesta tulevia elektroneja napa-alueiden yläpuolelle. Tuhansien kilometrien korkeudella elektronit kulkevat usein muutaman kilovoltin potentiaalieron läpi. Jokainen voltti antaa elektronille yhden elektronivoltin liike-energiaa. Potentiaaliero $5\,\text{kV}$ antaa liike-energian $5\,\text{keV}$ ja nopeuden noin $40\,000\,\text{km/s}$. Elektronin massa on niin pieni, että jo tällainen energia antaa sille valtavan nopeuden. Noin $100$–$300\,\text{km}$:n korkeudella elektronit törmäävät ilman happi- ja typpiatomeihin ja -molekyyleihin. Elektronit luovuttavat niille energiaansa, ja atomit ja molekyylit säteilevät energian valona. Vihreä valo tulee hapesta.

## Kaava: Sähköinen potentiaalienergia ja potentiaali
Kohdan potentiaali on varauksen potentiaalienergia varausyksikköä kohti. Siitä saadaan varauksen potentiaalienergia kohdassa, jonka potentiaali on $V$:
```kaavat
sähkökentän potentiaali :: V = \frac{E_\text{p}}{q}
:: E_\text{p} = qV
```
Kaavassa $E_\text{p}$ on potentiaalienergia ($\text{J}$), $q$ on varaus etumerkkeineen ($\text{C}$) ja $V$ on kohdan potentiaali ($\text{V}$) valittuun nollakohtaan nähden. Elektronille $q = -e$.

Kun varaus siirtyy kohdasta $A$ kohtaan $B$, sähköinen voima tekee työn
```kaavat
sähkökentän tekemä työ :: W_{AB} = q(V_A - V_B) = qU_{AB}
```
Kaavassa $W_{AB}$ on työ ($\text{J}$) ja $U_{AB} = V_A - V_B$ on kohtien potentiaaliero eli jännite ($\text{V}$). Työ on yhtä suuri kuin potentiaalienergian väheneminen $E_{\text{p},A} - E_{\text{p},B}$, eikä se riipu reitistä. Homogeenisessa kentässä levyjen välinen jännite on $U = Ed$ (luku *Homogeeninen sähkökenttä*). Siksi kentän suuntaan levystä toiseen kulkevaan varaukseen kenttä tekee työn $qU = qEd$.

```pysahdy
Varaus $2{,}0\,\text{nC}$ siirtyy kohdasta, jonka potentiaali on $90\,\text{V}$, kohtaan, jonka potentiaali on $40\,\text{V}$. Kuinka suuren työn sähköinen voima tekee?
---
Työ on $W_{AB} = q(V_A - V_B)$. Lukuarvoilla $V_A - V_B = 90\,\text{V} - 40\,\text{V} = 50\,\text{V}$ ja $W_{AB} = 2{,}0 \cdot 10^{-9}\,\text{C} \cdot 50\,\text{V}$, joten $W_{AB} = 1{,}0 \cdot 10^{-7}\,\text{J}$.
```

Kun negatiivinen levy on nollakohta, homogeenisen kentän potentiaali on
```latex
V = Ex
```
Kaavassa $E$ on kentänvoimakkuus ($\text{V/m}$) ja $x$ on kohdan etäisyys negatiivisesta levystä ($\text{m}$). Kuvaaja $(x, V)$ on suora, jonka kulmakerroin on kentänvoimakkuus. Kuvan levyjen välissä potentiaali muuttuu $100\,\text{V}$ matkalla $2{,}0\,\text{cm}$, joten $E = 100\,\text{V} : 0{,}020\,\text{m} = 5000\,\text{V/m}$.

<svg data-fig="vx-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: potentiaali V volteissa etäisyyden x funktiona senttimetreinä. Etäisyys x mitataan negatiivisesta levystä, jonka potentiaali on nolla. Levyjen väli on 4,0 cm ja jännite 200 V. Kuvaaja on origon kautta kulkeva nouseva suora. Suora päättyy positiivisen levyn kohdalle pisteeseen (4,0 cm; 200 V). Kulmakerroinkolmio näyttää, että kahden senttimetrin matkalla potentiaali muuttuu 100 V. Siksi kentänvoimakkuus on 5000 V/m." style="max-width:100%;font-size:24px">
  <line x1="186.5" y1="280" x2="186.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272.5" y1="280" x2="272.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="280" x2="359" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="445.5" y1="280" x2="445.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="227.5" x2="480" y2="227.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="175.5" x2="480" y2="175.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="123" x2="480" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="71" x2="480" y2="71" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="280" x2="494" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,280 L493,286 L493,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="281" x2="100" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,24 L106,37 L94,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186.5" y1="280" x2="186.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="272.5" y1="280" x2="272.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="359" y1="280" x2="359" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="349" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="445.5" y1="280" x2="445.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="435.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="93" y1="227.5" x2="100" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="213" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="175.5" x2="100" y2="175.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="161" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="123" x2="100" y2="123" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="108.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="71" x2="100" y2="71" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="56.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="70" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="265.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <foreignObject x="114" y="15.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$V\ (\text{V})$</span></div></foreignObject>
  <polyline points="100,280 445.5,71" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="445.5" cy="71" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="186.5" y1="227.5" x2="359" y2="227.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="359" y1="227.5" x2="359" y2="123" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="187.5" y="235" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta x = 2{,}0\,\text{cm}$</span></div></foreignObject>
  <foreignObject x="371" y="161" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V = 100\,\text{V}$</span></div></foreignObject>
  <foreignObject x="233.5" y="32.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{positiivinen levy}$</div></foreignObject>
</svg>

Kun vain sähköinen voima tekee työtä, liike-energian ja potentiaalienergian summa säilyy eli pysyy samana. Hiukkanen lähtee levosta ja kulkee potentiaalieron $U$ läpi. Silloin sen liike-energia on
```latex
\frac{1}{2}mv^2 = |q|U
```
Kaavassa $m$ on hiukkasen massa ($\text{kg}$), $v$ on sen nopeus ($\text{m/s}$) ja $|q|$ on varauksen suuruus ($\text{C}$). Painovoima jätetään huomiotta. Esimerkiksi protonin paino on kuvan kentässä kymmeniä miljardeja kertoja pienempi kuin sähköinen voima. Hiukkasen energian yksikkö elektronivoltti on
```latex
1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}
```
koska $$1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1\,\text{V} = 1{,}602 \cdot 10^{-19}\,\text{J}$$. Siis $1\,\text{keV} = 1000\,\text{eV}$.

## Esimerkki
Revontulielektroni lähtee lähes levosta ja kulkee kohti suurempaa potentiaalia $3{,}0\,\text{kV}$:n potentiaalieron läpi. Kuinka suuri on elektronin liike-energia elektronivoltteina ja jouleina? Kuinka suuri on sen nopeus? Elektronin varaus on $-e$, missä $e = 1{,}602 \cdot 10^{-19}\,\text{C}$, ja massa on $m = 9{,}109 \cdot 10^{-31}\,\text{kg}$. Muut voimat kuin sähköinen voima jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** $U = 3{,}0\,\text{kV}$, $e = 1{,}602 \cdot 10^{-19}\,\text{C}$, $m = 9{,}109 \cdot 10^{-31}\,\text{kg}$ ja alkunopeus nolla.

Kysytään liike-energiaa $E_\text{k}$ elektronivoltteina ja jouleina sekä nopeutta $v$.

<!-- vaihe -->

**Periaate.** Vain sähköinen voima tekee työtä, joten liike-energian ja potentiaalienergian summa säilyy. Elektroni kulkee kohti suurempaa potentiaalia. Sen potentiaalienergia pienenee määrän $eU$, ja liike-energia kasvaa saman verran. Jokainen voltti antaa elektronille yhden elektronivoltin.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\tfrac{1}{2}mv^2 = eU \\
&E_\text{k} = eU \\
&v = \sqrt{\frac{2eU}{m}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $U = 3{,}0\,\text{kV} = 3{,}0 \cdot 1000\,\text{V} = 3000\,\text{V}$. Lisäksi $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$ ja $\sqrt{1\,\text{J} : 1\,\text{kg}} = 1\,\text{m/s}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&E_\text{k} = eU \\
&= 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 3000\,\text{V} \\
&= 4{,}806 \cdot 10^{-16}\,\text{J} \\
&v = \sqrt{\frac{2E_\text{k}}{m}} \\
&= \sqrt{\frac{2 \cdot 4{,}806 \cdot 10^{-16}\,\text{J}}{9{,}109 \cdot 10^{-31}\,\text{kg}}} \\
&= 3{,}248 \cdot 10^{7}\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Elektronin liike-energia on $3{,}0\,\text{keV}$ eli $4{,}8 \cdot 10^{-16}\,\text{J}$, ja sen nopeus on $3{,}2 \cdot 10^{7}\,\text{m/s}$. Tulokset ilmoitetaan kahdella merkitsevällä numerolla kuten potentiaaliero $3{,}0\,\text{kV}$.

<!-- vaihe -->

**Järkevyys.** Pyöristetyillä luvuilla $v \approx \sqrt{2 \cdot 5 \cdot 10^{-16}\,\text{J} : 10^{-30}\,\text{kg}} \approx 3 \cdot 10^{7}\,\text{m/s}$, joten suuruusluokka on oikea. Nopeus on noin $11\,\%$ valon nopeudesta $3{,}00 \cdot 10^{8}\,\text{m/s}$. Se jää selvästi valon nopeuden alle, joten lauseke $\tfrac{1}{2}mv^2$ antaa vielä hyvän tuloksen.

## Yleinen virhekäsitys
Potentiaali ja potentiaalienergia eivät ole sama asia. Potentiaali on kentän kohdan ominaisuus, eikä se riipu siitä, onko kohdassa varausta. Potentiaalienergia on varauksen energiaa. Se riippuu varauksen suuruudesta ja etumerkistä. Samassa $150\,\text{V}$:n kohdassa protonin potentiaalienergia on $+150\,\text{eV}$ ja elektronin $-150\,\text{eV}$. Siksi ei voi sanoa, että varaus liikkuu aina kohti pienempää potentiaalia. Elektroni liikkuu kohti suurempaa.

Moni ajattelee myös, että pidempi kiihdytysmatka antaa hiukkaselle enemmän energiaa. Oletetaan, että levyjen välinen jännite pysyy samana. Jos levyjen välimatka kasvaa, kenttä on heikompi, $E = U : d$, ja työ $qEd = qU$ on sama. Ratkaisevaa on potentiaaliero, ei matka. Matka vaikuttaa vain siihen, kuinka kauan kiihdytys kestää.

## Tiivistelmä
- Sähköinen voima on konservatiivinen, joten varauksella on kentässä potentiaalienergiaa $E_\text{p} = qV$. Kentän tekemä työ on potentiaalienergian väheneminen.
- Potentiaali $V$ on potentiaalienergia varausyksikköä kohti, $1\,\text{V} = 1\,\text{J/C}$. Se on kentän kohdan ominaisuus. Kahden kohdan potentiaaliero on niiden välinen jännite.
- Homogeenisessa kentässä potentiaali muuttuu tasaisesti, $V = Ex$, kun negatiivinen levy on potentiaalin nollakohta ja $x$ on etäisyys siitä. Kenttä osoittaa suuremmasta potentiaalista pienempään. Tasapotentiaalipinnat ovat levyjen suuntaisia, ja kenttäviivat ovat niitä vastaan kohtisuorassa.
- Kun varaus kulkee potentiaalieron $U$ läpi, kenttä tekee työn $qU$ matkasta ja reitistä riippumatta. Levosta lähtenyt hiukkanen saa liike-energian $\tfrac{1}{2}mv^2 = |q|U$.
- Positiivinen varaus lähtee liikkeelle kohti pienempää potentiaalia ja negatiivinen kohti suurempaa. Kummankin potentiaalienergia pienenee.
- Elektronivoltti on hiukkasten energian yksikkö: $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.
