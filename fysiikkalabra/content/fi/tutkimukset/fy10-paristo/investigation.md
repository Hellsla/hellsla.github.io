# Pariston kuormituskäyrä

> **Tutkimuskysymys:** Miten pariston napajännite riippuu paristosta otettavasta sähkövirrasta, ja mitkä ovat pariston lähdejännite, sisäinen resistanssi ja oikosulkuvirta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on pidikkeessä oleva paristo, liukuvastus, kaksi yleismittaria ja niiden mittajohdot, muutama johdin sekä vihko mittaustulosten kirjaamiseen. Osia ei ole vielä kytketty yhteen, eikä mittareiden näytöissä ole lukemia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-paristo-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Taskulampun paristoon on painettu jännite. Onko pariston napojen välinen jännite aina sama, kytkettiinpä paristoon mitä tahansa? Tässä tutkimuksessa selvität mittaamalla, miten pariston napajännite käyttäytyy, kun paristosta otetaan eri suuria virtoja, ja määrität mittauksista kolme paristoa kuvaavaa suuretta. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten pariston napajännite riippuu sen antamasta virrasta, kuvaako lähdejännitteen ja sisäisen resistanssin malli mittauksiasi, ja kuinka suuret ovat pariston lähdejännite $E$, sisäinen resistanssi $R_\text{s}$ ja oikosulkuvirta $I_\text{k}$ epävarmuuksineen. Perustele lisäksi, miten nämä kolme suuretta saadaan kuvaajasta.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** mittarien kytkennän, virta-alueen opettajan ilmoittaman rajan sisällä, mittauspisteiden määrän ja mittausjärjestyksen sekä kuvaajan akselit perusteluineen. Ohjatussa työtavassa sivu kiinnittää nämä valinnat, ja sinä perustelet ne raportissa. Kaikissa työtavoissa valitset lisäksi tavan, jolla arvioit tulosten epävarmuudet: ohjatussa ja osittain ohjatussa työtavassa valitset jommankumman sivun antamasta kahdesta tavasta, itsenäisessä työtavassa päätät tavan itse.

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Miten pariston napajännite muuttuu, kun piirin virtaa kasvatetaan pienentämällä kuormitusvastuksen resistanssia?
2. Millainen on kuvaaja, jossa pystyakselilla on napajännite $U$ ja vaaka-akselilla virta $I$: nouseva vai laskeva, suora vai käyrä?
3. Mitä jännitemittari näyttää, kun se on kytketty pariston napoihin eikä paristoon ole kytketty muuta kuormaa? Onko lukema suurempi, pienempi vai yhtä suuri kuin kuormitettuna?
4. Mitä tapahtuisi virralle ja napajännitteelle, jos pariston navat yhdistettäisiin suoraan johtimella? **Älä kokeile tätä**, vaan vastaa ajattelemalla.

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

Sähkövirta $I$ kertoo, kuinka paljon sähkövarausta kulkee johtimen poikkileikkauksen läpi aikayksikössä; sen yksikkö on ampeeri $(\text{A})$. Jännite $U$ kahden pisteen välillä kertoo, kuinka paljon sähköenergiaa varausyksikkö luovuttaa kulkiessaan pisteestä toiseen; sen yksikkö on voltti $(\text{V})$. Vastuksen resistanssi $R$ on sen jännitteen ja virran suhde, $R = \dfrac{U}{I}$, ja sen yksikkö on ohmi $(\Omega)$. Kun piiriin kytketyn kuormitusvastuksen resistanssia pienennetään, piirin virta kasvaa.

Paristossa kemialliset reaktiot erottavat varauksia toisistaan ja ylläpitävät napojen välillä jännitettä. Pariston **lähdejännite** $E$ kertoo, kuinka paljon energiaa paristo antaa kullekin sen läpi kulkevalle varausyksikölle. Virta kulkee myös pariston sisällä elektrodien ja elektrolyytin läpi, ja niilläkin on resistanssia. Tätä sanotaan pariston **sisäiseksi resistanssiksi** $R_\text{s}$. Paristoa voi siksi ajatella ideaalisena jännitelähteenä, jonka kanssa sarjassa on vastus $R_\text{s}$:

<svg data-fig="model" viewBox="0 0 600 400" role="img" aria-label="Kaaviokuva pariston mallista. Katkoviivalla rajatun pariston sisällä on lähdejännite E ja sen kanssa sarjassa sisäinen resistanssi R s. Pariston plusnapa on ylhäällä ja miinusnapa alhaalla. Navoista johtimet menevät pariston ulkopuolella olevaan kuormaan. Ylemmässä johtimessa kulkee virta I plusnavasta kuormaan päin. Napojen välinen jännite on napajännite U." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-paristo-model.webp" x="0" y="-1.2" width="600" height="406.2" preserveAspectRatio="none"/>
  <foreignObject x="107.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paristo}$</div></foreignObject>
  <foreignObject x="90" y="125.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="178" y="105.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="85" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="526" y="183" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{kuorma}$</div></foreignObject>
  <foreignObject x="390" y="51.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="344" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
</svg>

Kun paristosta otetaan virta $I$, osa lähdejännitteestä kuluu pariston omaan sisäiseen resistanssiin. Ohmin lain mukaan tämä jännitehäviö on $R_\text{s} I$. Pariston napojen välinen jännite, **napajännite** $U$, on siksi

```latex
U = E - R_\text{s} I
```

missä $E$ on lähdejännite, $R_\text{s}$ sisäinen resistanssi ja $I$ paristosta otettava virta. Yhtälöä kirjoitetaan usein myös muotoon $U = E - RI$, jolloin $R$ tarkoittaa sisäistä resistanssia. Malli olettaa, että $E$ ja $R_\text{s}$ pysyvät samoina koko mittauksen ajan eivätkä riipu virrasta. Todellisella paristolla tämä pätee vain likimäärin, joten tutkimuksessa selvität myös, kuinka hyvin malli kuvaa juuri sinun paristoasi.

**Oikosulkuvirta** $I_\text{k}$ on virta, joka kulkisi, jos pariston navat yhdistettäisiin johtimella, jonka resistanssi on käytännössä nolla. Napajännite olisi silloin nolla. Oikosulkuvirtaa ei mitata: oikosulku kuumentaa paristoa ja voi vaurioittaa sitä. Se määritetään mittauksista laskemalla tai kuvaajan avulla.

Kuvaajaa, joka esittää pariston napajännitteen ja virran yhteyden, sanotaan pariston **kuormituskäyräksi**.

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ja näytä se opettajalle ennen kuin kokoat piirin. Tarkista opettajalta, mikä on suurin virta, jota paristosta saa ottaa.

::: tuki OO
**Osittain ohjattu.** Muuttuja on paristosta otettava virta, ja sitä säädetään säädettävällä vastuksella. Päätä itse, miten kytket virta- ja jännitemittarin, kuinka monta mittauspistettä teet ja missä järjestyksessä. Piirrä kytkentäkaavio ja kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Mihin kohtaan piiriä jännitemittari kytketään, jotta se mittaa pariston napajännitettä? Mitä muuttuisi, jos se mitattaisiin säädettävän vastuksen yli?
- Miten varmistat, ettei piirin resistanssi voi laskea nollaan?
- Muuttuuko pariston jännite, jos virtaa otetaan pitkään? Miten huomaisit sen mittaussarjasta?
:::

::: tuki O
**Ohjattu.** Muutat säädettävän vastuksen resistanssia, jolloin piirin virta $I$ muuttuu. Mittaat jokaisella säädöllä virran $I$ ja pariston napajännitteen $U$. Vakiona pidät pariston, kytkennän ja mittarien mittausalueet. Kytke piiri tämän kaavion mukaan:

<svg data-fig="circuit" viewBox="0 0 600 360" role="img" aria-label="Kytkentäkaavio. Paristo, kytkin, virtamittari A, säädettävä vastus ja opettajan antama suojavastus on kytketty sarjaan yhdeksi silmukaksi. Jännitemittari V on kytketty rinnan suoraan pariston napoihin, pariston molemmin puolin olevista liitoskohdista." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-paristo-circuit.webp" x="1.2" y="-1.2" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="194" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="60" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="225" y="24" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{kytkin}$</div></foreignObject>
  <foreignObject x="360" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="266" y="178" width="174" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{säädettävä vastus}$</div></foreignObject>
  <foreignObject x="269" y="320" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{suojavastus}$</div></foreignObject>
</svg>

Jännitemittari kytketään suoraan pariston napoihin, ei säädettävän vastuksen yli. Silloin se mittaa juuri napajännitteen: suojavastuksen, virtamittarin ja johtimien jännitehäviöt eivät sekoitu sisäiseen resistanssiin. Jos paristo on pidikkeessä, kytke jännitemittari mahdollisimman lähelle pariston napoja, sillä muuten pidikkeen kosketusresistanssi näkyy osana sisäistä resistanssia. Suojavastus estää resistanssia laskemasta nollaan, vaikka säädettävä vastus käännettäisiin ääriasentoonsa. Jos opettaja ei anna suojavastusta, kysy, miten säädettävän vastuksen pienin resistanssi rajoitetaan.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Mittaa lisäksi pariston napajännite, kun paristoon ei ole kytketty muuta kuin jännitemittari, ja kirjaa se erikseen.

::: tuki O
Aloita säädettävän vastuksen suurimmasta resistanssista ja pienennä resistanssia vähitellen, kunnes virta on lähellä opettajan ilmoittamaa rajaa. Tee ainakin kahdeksan mittauspistettä, joiden virrat jakautuvat mahdollisimman tasaisesti tälle välille. Sulje kytkin vain lukemien ajaksi: lue virta ja jännite heti, kirjaa ne ja avaa piiri. Mittaa lopuksi ensimmäinen mittauspiste uudelleen ja vertaa: jos lukemat poikkeavat selvästi, pariston tila on muuttunut mittauksen aikana.

Voit käyttää esimerkiksi tällaista taulukkoa ja lisätä rivejä niin monta kuin mittauspisteitä on:

| $I\ (\text{A})$ | $U\ (\text{V})$ |
|---|---|
| | |
| | |
| | |
:::

Muista mittausepävarmuus: kirjaa mittarien lukematarkkuus ja valmistajan ilmoittama tarkkuus, jos se on saatavilla, ja merkitse ne taulukkoon. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä mittaustuloksista pariston kuormituskäyrä. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin malliin sopiva kuvaaja. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse pystyakselille napajännite $U$ ja vaaka-akselille virta $I$. Ulota molemmat akselit nollaan asti, jotta näet, missä sovitettu suora leikkaa akselit.
:::

Kirjoita sovitetun kuvaajan yhtälö ja vastaa:

1. Ovatko pisteet suoralla? Jos eivät, millä virroilla ne poikkeavat?
2. Mikä kuvaajan kohta tai ominaisuus kertoo lähdejännitteen $E$? Perustele mallin $U = E - R_\text{s} I$ avulla.
3. Mikä kuvaajan ominaisuus kertoo sisäisen resistanssin $R_\text{s}$? Perustele.
4. Miten oikosulkuvirta $I_\text{k}$ saadaan kuvaajasta, ja miten sen voi laskea suureista $E$ ja $R_\text{s}$? Perustele.
5. Vertaa kuvaajasta saamaasi lähdejännitettä siihen napajännitteeseen, jonka mittasit ilman kuormaa. Selitä, miksi ne ovat tai eivät ole samat.

::: tuki O OO
**Tarkista vastauksesi tästä.** Malli $U = E - R_\text{s} I$ on suoran yhtälö, kun pystyakselille valitaan $U$ ja vaaka-akselille $I$. Kun virta on nolla, napajännite on $E$, joten lähdejännite on pystyakselin leikkauskohta. Suoran kulmakerroin on $-R_\text{s}$, joten sisäinen resistanssi on kulmakertoimen itseisarvo. Oikosulussa napajännite on nolla, joten oikosulkuvirta on vaaka-akselin leikkauskohta. Asettamalla $U = 0$ saadaan $I_\text{k} = \dfrac{E}{R_\text{s}}$.

<svg data-fig="curve" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: napajännite U virran I funktiona mallin U = E miinus R s kertaa I mukaan. Kuvaaja on laskeva suora. Pienten virtojen osa on piirretty yhtenäisellä viivalla: sillä alueella voidaan mitata. Suoran jatkeet akseleille on piirretty katkoviivalla. Pystyakselin leikkauskohta on lähdejännite E ja vaaka-akselin leikkauskohta oikosulkuvirta I k. Suoralle on merkitty muutokset delta I ja delta U; kulmakerroin on miinus R s. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U$</span></div></foreignObject>
  <polyline points="90,96 101.5,102" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 7"/>
  <polyline points="101.5,102 227,169.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="227,169.5 432,280" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 7"/>
  <line x1="83" y1="96" x2="90" y2="96" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="81.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="432" y1="280" x2="432" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="415.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_\text{k}$</div></foreignObject>
  <line x1="124" y1="114.5" x2="211.5" y2="114.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="211.5" y1="114.5" x2="211.5" y2="161.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="151.5" y="80" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta I$</div></foreignObject>
  <foreignObject x="221.5" y="123.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta U$</div></foreignObject>
  <foreignObject x="216.5" y="30" width="233" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{\Delta U}{\Delta I} = -R_\text{s}$</div></foreignObject>
</svg>

Mittauspisteet ovat yleensä vain osalla suoraa, kuvan yhtenäisellä osalla. Molemmat leikkauskohdat saadaan jatkamalla sovitettua suoraa mittausalueen ulkopuolelle, katkoviivalla merkityille osille. Erityisesti oikosulkuvirta on usein kaukana mitatuista virroista. Jatkaminen voi antaa väärän tuloksen, koska suurilla virroilla paristo lämpenee ja polarisoituu, jolloin sen sisäinen resistanssi ja lähdejännite eivät enää pysy vakioina eikä kuormituskäyrä ole siellä välttämättä suora.
:::

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita lähdejännite, sisäinen resistanssi ja oikosulkuvirta muodossa $\bar{x} \pm \Delta x$ yksikköineen ja perustele, miten arvioit kunkin epävarmuuden.

::: tuki O OO
Epävarmuudet voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirheet.** Monet ohjelmat ilmoittavat kulmakertoimen ja vakiotermin keskivirheen. Käytä vakiotermin keskivirhettä epävarmuutena $\Delta E$ ja kulmakertoimen keskivirhettä epävarmuutena $\Delta R_\text{s}$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Arvioi kunkin suureen epävarmuus näiden suorien antamien arvojen vaihteluvälin puolikkaana.

Oikosulkuvirran epävarmuuden saat parhaiten jyrkimmän ja loivimman suoran menetelmällä: lue $I_\text{k}$:n vaihteluväli suoraan niiden vaaka-akselin leikkauskohdista. Osamäärän $I_\text{k} = \dfrac{E}{R_\text{s}}$ suhteellisten epävarmuuksien summa $\dfrac{\Delta E}{E} + \dfrac{\Delta R_\text{s}}{R_\text{s}}$ antaa vain ylärajan, koska $E$ ja $R_\text{s}$ saadaan samasta sovituksesta eivätkä niiden virheet ole toisistaan riippumattomia.

Muista myös systemaattiset virheet: mittarin kalibrointivirhe siirtää kaikkia saman mittarin lukemia samaan suuntaan, eikä sovitus pienennä sitä. Valmistajan ilmoittama tarkkuus kertoo, kuinka suuri se voi olla.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti:

- Kumman suureen, $E$:n vai $I_\text{k}$:n, suhteellinen epävarmuus on suurempi, ja miksi?
- Pysyikö pariston tila samana koko mittauksen ajan? Mihin perustat vastauksesi?
- Mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tuloksia? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Kuvaako malli $U = E - R_\text{s} I$ paristoasi koko mittausalueella? Perustele, kuinka luotettava kuvaajan jatkamiseen perustuva oikosulkuvirta on: millä ehdolla tulos pätee, ja täyttyykö se todennäköisesti myös mittausalueen ulkopuolella? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki yhdeksän osaa. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** lähdejännite, sisäinen resistanssi, oikosulkuvirta ja malli $U = E - R_\text{s} I$ sekä se, miksi valitsit juuri nämä akselit.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, mitä muutit, mitä mittasit ja mitä pidit vakiona, sekä miten estit oikosulun.
- **Mittaustulokset:** alkuperäiset virran ja jännitteen lukemat sekä ilman kuormaa mitattu napajännite.
- **Tulos:** $E$, $R_\text{s}$ ja $I_\text{k}$ epävarmuuksineen oikein pyöristettyinä ja perustelu sille, miten kukin saatiin kuvaajasta.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, niiden vaikutuksen suunta ja arvio kuvaajan jatkamisen luotettavuudesta.

## Laajennus: uusi ja käytetty paristo

Mittaa samalla tavalla myös käytetyn pariston kuormituskäyrä samoilla mittareilla ja samalla kytkennällä, ja toista lopuksi ensimmäinen mittauspiste. Piirrä molemmat kuormituskäyrät samaan kuvaajaan ja vertaa niitä sillä virta-alueella, jonka kumpikin paristo saavuttaa.

Vertaa paristojen lähdejännitteitä ja sisäisiä resistansseja epävarmuuksineen: mahtuvatko arvot toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Kumpi suure erottaa paristot toisistaan selvemmin?

Pohdi lopuksi: riittääkö pelkkä jännitemittarin lukema ilman kuormaa kertomaan, jaksaako paristo vielä käyttää laitetta, joka ottaa suuren virran? Perustele kuormituskäyriesi avulla.

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi ja kytkentäkaaviosi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
