# Magneetit, magneettinen dipoli ja magneettikenttä

> **Miksi** kompassin neula osoittaa metsässä yleensä likimain kohti pohjoista, mutta kääntyy heti muualle, kun sen viereen tuodaan magneetti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: suunnistuskartta kivellä kuusimetsässä. Kartan päällä on kompassi, ja sen vieressä sauvamagneetti, jonka punertava ja sininen pää näkyvät. Kompassin neula on kääntynyt kohti magneettia eikä osoita kartan pohjoisnuolen suuntaan." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Magneetin navat
Magneetin vaikutus on voimakkain sen päissä, joita sanotaan magneetin navoiksi. Kun sauvamagneetti ripustetaan langasta niin, että se pääsee kääntymään vapaasti, se asettuu pohjois–eteläsuuntaan. Pohjoiseen kääntyvä pää on magneetin **pohjoisnapa** $\text{N}$ ja etelään kääntyvä pää **etelänapa** $\text{S}$. Kahden magneetin samannimiset navat hylkivät toisiaan ja erinimiset navat vetävät toisiaan puoleensa. Magneetit vaikuttavat toisiinsa myös koskematta toisiinsa, ja vaikutus heikkenee nopeasti, kun magneetit loittonevat toisistaan.

### Magneettinen dipoli
Kun sauvamagneetti katkaistaan kahtia, kummastakin palasta tulee kokonainen magneetti, jolla on sekä pohjoisnapa että etelänapa. Sama toistuu, vaikka paloja pilkottaisiin yhä pienemmiksi. Magneetin navat esiintyvät siis aina pareittain: magneetti on **magneettinen dipoli**. Tässä magneettinen vuorovaikutus eroaa sähköisestä. Positiivisen ja negatiivisen sähkövarauksen voi erottaa toisistaan, mutta yksittäistä magneettinapaa ei ole koskaan havaittu.

<svg data-fig="cut-magnet" viewBox="0 0 600 300" role="img" aria-label="Periaatekuva: sauvamagneetti katkaistaan ensin kahtia ja sitten neljään osaan. Jokaisessa palassa on edelleen sekä pohjoisnapa N että etelänapa S samassa järjestyksessä kuin alkuperäisessä magneetissa. Erillistä yksittäistä napaa ei synny." style="max-width:100%;font-size:24px">
  <path d="M115,28 H300 V72 H115 Q110,72 110,67 V33 Q110,28 115,28 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M300,28 H485 Q490,28 490,33 V67 Q490,72 485,72 H300 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="28" width="380" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="300" y1="28" x2="300" y2="72" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="195" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="385" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="35.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <line x1="300" y1="80" x2="300" y2="120" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M115,128 H200 V172 H115 Q110,172 110,167 V133 Q110,128 115,128 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M200,128 H285 Q290,128 290,133 V167 Q290,172 285,172 H200 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="128" width="180" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="128" x2="200" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="145" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="235" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M315,128 H400 V172 H315 Q310,172 310,167 V133 Q310,128 315,128 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M400,128 H485 Q490,128 490,133 V167 Q490,172 485,172 H400 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="310" y="128" width="180" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="400" y1="128" x2="400" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="345" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="435" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$2$</div></foreignObject>
  <line x1="300" y1="180" x2="300" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <path d="M115,228 H150 V272 H115 Q110,272 110,267 V233 Q110,228 115,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M150,228 H185 Q190,228 190,233 V267 Q190,272 185,272 H150 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="110" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="228" x2="150" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="120" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="160" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M215,228 H250 V272 H215 Q210,272 210,267 V233 Q210,228 215,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M250,228 H285 Q290,228 290,233 V267 Q290,272 285,272 H250 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="210" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="250" y1="228" x2="250" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="220" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="260" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M315,228 H350 V272 H315 Q310,272 310,267 V233 Q310,228 315,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M350,228 H385 Q390,228 390,233 V267 Q390,272 385,272 H350 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="310" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="350" y1="228" x2="350" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="320" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="360" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <path d="M415,228 H450 V272 H415 Q410,272 410,267 V233 Q410,228 415,228 Z" fill="#d0e6fb" stroke-linejoin="round"/>
  <path d="M450,228 H485 Q490,228 490,233 V267 Q490,272 485,272 H450 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <rect x="410" y="228" width="80" height="44" rx="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="228" x2="450" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="420" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="460" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="50" y="235.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$4$</div></foreignObject>
</svg>

```pysahdy
Sauvamagneetti katkaistaan keskeltä kahtia. Onko toisessa palassa vain pohjoisnapa ja toisessa vain etelänapa?
---
Ei ole. Kummassakin palassa on sekä pohjoisnapa että etelänapa, koska magneetin navat esiintyvät aina pareittain.
```

### Ferromagnetismi ja alkeisalueet
Magneetti vetää puoleensa rautaa, nikkeliä, kobolttia ja monia niiden seoksia, kuten terästä. Näitä aineita sanotaan **ferromagneettisiksi**. Jokainen niiden atomi on pieni magneettinen dipoli. Ferromagneettisessa aineessa vierekkäisten atomien dipolit asettuvat samansuuntaisiksi, ja aine jakautuu tyypillisesti mikrometrien kokoisiin **alkeisalueisiin**, joissa kaikki atomidipolit osoittavat samaan suuntaan. Magnetoimattomassa raudassa alkeisalueiden suunnat vaihtelevat, joten niiden vaikutukset kumoavat toisensa eikä kappale ole magneetti.

Kun rautakappale tuodaan magneetin lähelle, magneetin kenttä kääntää alkeisalueiden suuntia ja kasvattaa niitä alkeisalueita, joiden suunta on kentän suuntainen. Rauta **magnetoituu**: siitä tulee magneetti, jonka magneetin puoleinen pää on erinimisen navan kaltainen. Siksi magneetti vetää magnetoimatontakin rautanaulaa. Pehmeä rauta menettää magnetoitumansa lähes kokonaan, kun magneetti viedään pois, mutta kovassa teräksessä ja neodyymimagneetin seoksessa alkeisalueet jäävät järjestykseen. Niistä tehdään **kestomagneetteja**.

Kuumennus riittävän korkeaan lämpötilaan, raudalla noin $770\,{}^\circ\text{C}$:n lämpötilaan, sekoittaa järjestyksen, ja ferromagnetismi katoaa.

<svg data-fig="domains" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: rautakappaleen alkeisalueet. Vasemmalla magnetoimaton rauta, jonka alkeisalueiden magneettiset suunnat, valkoiset nuolet, osoittavat eri suuntiin, joten niiden vaikutukset kumoavat toisensa. Oikealla rautakappaleen viereen on tuotu magneetti pohjoisnapa N edellä. Magneetin kenttä kääntää alkeisalueet ja kasvattaa niitä, joilla on kentän suunta, joten lähes kaikki nuolet osoittavat magneetista poispäin. Rauta on magnetoitunut: sen magneetin puoleinen pää on etelänapa S, ja magneetti vetää sitä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-domains.webp" x="0" y="-1.2" width="600" height="347.5" preserveAspectRatio="none"/>
  <foreignObject x="20" y="11.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnetoimaton rauta}$</div></foreignObject>
  <foreignObject x="330" y="11.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magnetoitu rauta}$</div></foreignObject>
  <foreignObject x="318" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="350" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="390" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="556" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
</svg>

Useimmat muut aineet, kuten alumiini, kupari, puu, muovi ja vesi, eivät tartu magneettiin: niiden magneettiset vaikutukset ovat niin heikkoja, ettei niitä arkisilla magneeteilla huomaa.

### Magneettikenttä ja kenttäviivat
Magneetti muuttaa ympäröivää tilaa niin, että toinen magneetti tai rautakappale kokee siinä voiman. Tätä magneetin ympärille syntyvää tilaa sanotaan **magneettikentäksi**. Kentän suunta jossakin pisteessä on se suunta, johon pisteeseen asetetun kompassin neulan pohjoispää osoittaa. Kompassi on siis pieni koetinmagneetti, jolla kentän suunnan voi selvittää paikka kerrallaan.

Kenttää havainnollistetaan **kenttäviivoilla**. Kenttäviivan suunta kussakin pisteessä on kentän suunta. Magneetin ulkopuolella kenttäviivat kulkevat pohjoisnavasta etelänapaan ja magneetin sisällä etelänavasta pohjoisnapaan, joten jokainen viiva on suljettu silmukka. Missä viivat ovat tiheässä, kenttä on voimakas. Kenttäviivat eivät koskaan leikkaa toisiaan, koska kentällä on kussakin pisteessä vain yksi suunta.

<svg data-fig="bar-field" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva sauvamagneetin magneettikentästä ylhäältä nähtynä. Vihreät kenttäviivat lähtevät magneetin pohjoisnavasta N, kaartuvat magneetin ympäri ja palaavat etelänapaan S; magneetin sisällä viivat jatkuvat etelänavasta pohjoisnapaan, joten jokainen viiva on suljettu silmukka. Nuolenkärjet näyttävät kentän suunnan. Neljä kompassia magneetin ympärillä kääntyy kenttäviivojen suuntaisiksi: kompassin pohjoispää osoittaa kentän suuntaan. Navoilla viivat ovat tiheimmillään, joten kenttä on siellä voimakkain." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-bar-field.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="250" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="330" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/horseshoe-magnet-filings.webp" alt="Hevosenkenkämagneetti, jonka navoille ja ympärille on tarttunut rautaviilaa tiheinä kaarina ja tupsuina."><figcaption>Rautaviila hevosenkenkämagneetin ympärillä. Jokainen hippu magnetoituu ja asettuu kentän suuntaiseksi, joten viila piirtää näkyviin kenttäviivojen kulun. Navoilla viilaa on eniten, koska kenttä on siellä voimakkain.</figcaption></figure>

```pysahdy
Pienen kompassin neula on sauvamagneetin pohjoisnavan vieressä. Mihin suuntaan neulan pohjoispää osoittaa?
---
Pois magneetin pohjoisnavasta. Neulan pohjoispää osoittaa kentän suuntaan, ja kenttäviivat kulkevat magneetin ulkopuolella pohjoisnavasta poispäin.
```

### Maan magneettikenttä
Maapallolla on magneettikenttä, joka muistuttaa sauvamagneetin kenttää. Se syntyy Maan ulkoytimen sulan raudan liikkeistä ja niihin liittyvistä sähkövirroista. Kompassin neulan pohjoispää kääntyy kohti maantieteellistä pohjoista. Koska erinimiset navat vetävät toisiaan, Maan kentän suunta vastaa maantieteellisen pohjoisnavan lähellä sauvamagneetin **etelänavan** $\text{S}$ kenttää, ja maantieteellisen etelänavan lähellä sauvamagneetin pohjoisnavan $\text{N}$ kenttää.

Maan pohjoisella pallonpuoliskolla sijaitsevaa magneettista napaa kutsutaan kuitenkin geomagnetismissa ja navigoinnissa **magneettiseksi pohjoisnavaksi**. Nimitykset perustuvat eri tarkastelutapoihin: sauvamagneettimallissa napa nimetään sen kentän mukaan, navigoinnissa sijainnin mukaan. Neula osoittaa vain likimain maantieteelliseen pohjoiseen, koska magneettinen napa ei ole maantieteellisen navan kohdalla ja paikalliset häiriöt vaikuttavat suuntaan.

Magneettiset navat eivät ole täsmälleen maantieteellisten napojen kohdalla, ja ne vaeltavat hitaasti. Siksi kompassi poikkeaa todellisesta pohjoisesta: Suomessa nykyään etelässä noin $10^\circ$ ja Lapissa noin $15^\circ$ itään. Suomessa kenttäviivat myös painuvat jyrkästi maata kohti, noin $73^\circ$–$79^\circ$ vaakatason alapuolelle. Tätä kulmaa sanotaan **inklinaatioksi**.

<svg data-fig="earth-field" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva, ei mittakaavassa: Maa ja sen magneettikenttä. Maan sisään on piirretty kuviteltu sauvamagneetti, joka on noin kymmenen astetta kallellaan pyörimisakseliin nähden. Sen etelänapa S on maantieteellisen pohjoisnavan lähellä ja pohjoisnapa N maantieteellisen etelänavan lähellä. Vihreät kenttäviivat lähtevät eteläiseltä pallonpuoliskolta ja kaartuvat avaruuden kautta pohjoiselle pallonpuoliskolle. Pohjoisella pallonpuoliskolla oleva kompassi osoittaa pohjoiseen ja viivat painuvat siellä jyrkästi maahan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-earth-field.webp" x="1.2" y="0" width="597" height="384.3" preserveAspectRatio="none"/>
  <foreignObject x="295" y="148" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="285" y="207" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="130" y="15.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maantieteellinen pohjoisnapa}$</div></foreignObject>
  <foreignObject x="140" y="337.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maantieteellinen etelänapa}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/aurora-saana.webp" alt="Vihreitä revontulia tähtitaivaalla Saana-tunturin yllä Kilpisjärvellä."><figcaption>Revontulet Saanan yllä Kilpisjärvellä. Maan magneettikenttä ohjaa Auringosta tulevia varattuja hiukkasia napa-alueille, ja siksi revontulia näkyy Lapissa usein.</figcaption></figure>

## Kaava: Magneettikenttien yhteisvaikutus
Magneettikentän voimakkuutta ja suuntaa kuvaa vektorisuure **magneettivuon tiheys** $\overline{B}$. Sen suunta on kentän suunta ja sen suuruus $B$ kertoo, kuinka voimakas kenttä on. Magneettivuon tiheyden yksikkö on **tesla** $\text{T}$. Teslan määritelmä perustuu magneettikentän voimaan liikkuvaan varaukseen, ja se esitellään luvussa *Varatun hiukkasen liike sähkö- ja magneettikentässä*. Tesla on suuri yksikkö, joten arkisia kenttiä ilmoitetaan usein millitesloina, $1\,\text{mT} = 10^{-3}\,\text{T}$, tai mikrotesloina, $1\,\mu\text{T} = 10^{-6}\,\text{T}$.

| Kohde | $B$ |
| --- | --- |
| Maa, Etelä-Suomi | noin $52\,\mu\text{T}$ |
| jääkaappimagneetti | noin $5\,\text{mT}$ |
| neodyymimagneetti | noin $0{,}5\,\text{T}$ |
| magneettikuvaus | $1{,}5$–$3\,\text{T}$ |
| laboratoriomagneetti | noin $45\,\text{T}$ |

Maan kentän arvo ($52$–$53\,\mu\text{T}$ Etelä-Suomessa) on World Magnetic Model 2025 -mallista (NOAA ja British Geological Survey), sairaaloiden magneettikuvauslaitteiden kentät ovat tavallisesti $1{,}5\,\text{T}$ tai $3\,\text{T}$, ja noin $45\,\text{T}$:n jatkuvia kenttiä tuotetaan tutkimuslaboratorioissa, esimerkiksi National High Magnetic Field Laboratoryn hybridimagneetilla Yhdysvalloissa. Magneettien arvot ovat suuruusluokkia magneetin pinnalla.

Kun samaan pisteeseen vaikuttaa kaksi magneettikenttää, kokonaiskenttä on niiden vektorisumma:
```latex
\overline{B} = \overline{B}_1 + \overline{B}_2
```
missä $\overline{B}_1$ ja $\overline{B}_2$ ovat kenttien magneettivuon tiheydet (T) ja $\overline{B}$ kokonaiskenttä (T). Kompassin neula kääntyy kokonaiskentän suuntaiseksi. Kun kentät ovat kohtisuorassa toisiaan vastaan, kokonaiskentän suuruus saadaan Pythagoraan lauseesta ja suunta tangentista:
```latex
\begin{aligned}
B &= \sqrt{B_1^2 + B_2^2} \\
\tan\theta &= \frac{B_2}{B_1}
\end{aligned}
```
missä $\theta$ on kokonaiskentän ja kentän $\overline{B}_1$ välinen kulma.

```pysahdy
Paikassa, jossa Maan magneettikentän vaakakomponentti on $30\,\mu\text{T}$, kompassin lähellä on magneetti. Sen vaakasuora kenttä on $40\,\mu\text{T}$ ja kohtisuorassa Maan kentän vaakakomponenttia vastaan. Kuinka suuri on vaakasuora kokonaiskenttä?
---
Vaakasuora kokonaiskenttä saadaan Pythagoraan lauseella $B = \sqrt{(30\,\mu\text{T})^2 + (40\,\mu\text{T})^2} = 50\,\mu\text{T}$.
```

Tätä käytetään kompassimittauksessa. Kompassin kohdalla Maan kentän vaakakomponentti $\overline{B}_\text{h}$ osoittaa pohjoiseen. Kun magneetti asetetaan niin, että sen kenttä $\overline{B}_\text{m}$ on kompassin kohdalla itään, neula kääntyy pohjoisesta itään kulman $\theta$, jolle $\tan\theta = B_\text{m} : B_\text{h}$. Magneetin kentän voi siis mitata kompassilla, kun Maan kentän vaakakomponentti tunnetaan.

<svg data-fig="vector-sum" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva mittakaavassa, ylhäältä nähtynä: kompassin kohdalla Maan magneettikentän vaakakomponentti B_h = 14 µT osoittaa pohjoiseen eli ylöspäin ja magneetin kenttä B_m = 20 µT itään eli oikealle, kohti oikealla olevan magneetin etelänapaa S. Kenttien summa B on suorakulmion lävistäjä, ja kompassin neula kääntyy sen suuntaiseksi kulman θ verran pohjoisesta itään." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-vector-sum.webp" x="0" y="0" width="600" height="357.5" preserveAspectRatio="none"/>
  <foreignObject x="170" y="183.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="93" y="216.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\overline{B}_\text{h}$</div></foreignObject>
  <foreignObject x="217.5" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{B}_\text{m}$</div></foreignObject>
  <foreignObject x="302" y="151.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{B}$</div></foreignObject>
  <foreignObject x="407.5" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="482.5" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="456" y="19.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pohjoinen}$</div></foreignObject>
</svg>

Maan kenttä osoittaa Suomessa vinosti maahan. Kompassin neula kääntyy vain vaakatasossa, joten vain kentän vaakakomponentti kääntää sitä. Kun kentän suuruus on $B$ ja inklinaatio $I$, komponentit ovat
```latex
\begin{aligned}
B_\text{h} &= B\cos I \\
B_\text{v} &= B\sin I
\end{aligned}
```
missä $B_\text{h}$ on vaakakomponentti ja $B_\text{v}$ pystykomponentti. Etelä-Suomessa $B \approx 52\,\mu\text{T}$ ja $I \approx 74^\circ$, joten vaakakomponentti on vain noin $14\,\mu\text{T}$ ja pystykomponentti noin $50\,\mu\text{T}$. Nämä ovat kurssin pyöristetyt arvot: tarkempi malli antaa Helsingissä vaakakomponentiksi noin $15\,\mu\text{T}$.

<svg data-fig="inclination" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva mittakaavassa, sivulta nähtynä: Etelä-Suomessa Maan magneettikenttä B = 52 µT osoittaa pohjoiseen ja 74 astetta vaakatason alapuolelle. Kentän vaakakomponentti B_h on noin 14 µT ja pystykomponentti B_v noin 50 µT. Kompassi kääntyy vain vaakakomponentin mukaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-inclination.webp" x="0" y="-1.2" width="600" height="347.5" preserveAspectRatio="none"/>
  <foreignObject x="456" y="55.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{maanpinta}$</div></foreignObject>
  <foreignObject x="244" y="107.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="207.5" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{B}_\text{h}$</div></foreignObject>
  <foreignObject x="143" y="197.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\overline{B}_\text{v}$</div></foreignObject>
  <foreignObject x="274" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{B}$</div></foreignObject>
  <foreignObject x="236" y="25.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{pohjoinen}$</div></foreignObject>
</svg>

## Esimerkki
Kompassi on vaakasuoralla pöydällä Etelä-Suomessa, missä Maan magneettikentän vaakakomponentti on $14\,\mu\text{T}$. Pöydälle asetetaan sauvamagneetti kompassin itäpuolelle itä–länsi-suuntaisesti niin, että magneetin etelänapa $\text{S}$ on kompassia kohti. Kompassin neula kääntyy $52^\circ$ pohjoisesta itään. Kuinka suuri on magneetin magneettivuon tiheys kompassin kohdalla?

<!-- vaihe -->

**Tunnetut ja kysytty.** Maan kentän vaakakomponentti $B_\text{h} = 14\,\mu\text{T}$ pohjoiseen ja neulan kääntymiskulma $\theta = 52^\circ$ itään.

Kysytään magneetin magneettivuon tiheyttä $B_\text{m}$ kompassin kohdalla.

<!-- vaihe -->

**Periaate.** Kompassin neula kääntyy kokonaiskentän suuntaiseksi. Magneetin kenttä osoittaa kompassin kohdalla kohti magneetin etelänapaa eli itään, joten se on kohtisuorassa pohjoiseen osoittavaa Maan kentän vaakakomponenttia vastaan. Kokonaiskenttä on suorakulmion lävistäjä, ja kulman $\theta$ tangentti on vastaisen ja viereisen kateetin suhde.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
\tan\theta &= \frac{B_\text{m}}{B_\text{h}} \\
B_\text{m} &= B_\text{h}\tan\theta
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: $\tan\theta$ on pelkkä luku, joten $B_\text{m}$ saadaan samassa yksikössä kuin $B_\text{h}$ eli mikrotesloina. Tarvittaessa $1\,\mu\text{T} = 10^{-6}\,\text{T}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
B_\text{m} &= B_\text{h}\tan\theta \\
&= 14\,\mu\text{T} \cdot \tan 52^\circ \\
&= 14\,\mu\text{T} \cdot 1{,}280 \\
&= 17{,}9\,\mu\text{T}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Magneetin magneettivuon tiheys kompassin kohdalla on noin $18\,\mu\text{T} = 1{,}8 \cdot 10^{-5}\,\text{T}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska vaakakomponentti $14\,\mu\text{T}$ ja kulma $52^\circ$ tunnetaan kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kulmalla $45^\circ$ magneetin kenttä olisi yhtä suuri kuin $B_\text{h}$. Kulma on yli $45^\circ$, joten $B_\text{m}$ on suurempi kuin $14\,\mu\text{T}$, kuten tulos. Kokonaiskenttä on $\sqrt{(14\,\mu\text{T})^2 + (17{,}9\,\mu\text{T})^2} \approx 22{,}7\,\mu\text{T}$, ja saman antaa $B_\text{h} : \cos 52^\circ$. Kenttä on Maan kentän suuruusluokkaa, mikä sopii magneetille, joka on noin kymmenen senttimetrin päässä.

## Yleinen virhekäsitys
Moni ajattelee, että kompassin neulan pohjoispää hakeutuu sauvamagneetin pohjoisnavan luo, koska Maan pohjoista magneettista napaa kutsutaan magneettiseksi pohjoisnavaksi. Kompassin neulan pohjoispää on kuitenkin magneetin pohjoisnapa, ja sitä vetää puoleensa eriniminen napa. Sauvamagneettimallissa maantieteellisen pohjoisnavan lähellä on siis etelänapa, vaikka geomagnetismissa sitä kutsutaan magneettiseksi pohjoisnavaksi.

Toinen virhe on luulla, että magneetin navat voi erottaa katkaisemalla magneetin keskeltä. Katkaisukohtaan syntyy kaksi uutta napaa, ja kummastakin palasta tulee kokonainen dipoli. Kolmas virhe on ajatella, että magneetti vetää kaikkia metalleja. Alumiinitölkki tai kuparikolikko ei tartu magneettiin, koska ne eivät ole ferromagneettisia.

Laskuissa yleisin virhe on laskea kohtisuorat kentät yhteen kuin lukuja. Kentät $14\,\mu\text{T}$ pohjoiseen ja $18\,\mu\text{T}$ itään antavat kokonaiskentän $$\begin{aligned} &\sqrt{(14\,\mu\text{T})^2 + (18\,\mu\text{T})^2} \\ &\approx 23\,\mu\text{T} \end{aligned}$$, ei $32\,\mu\text{T}$.

## Tiivistelmä
- Magneetilla on aina kaksi napaa, pohjoisnapa $\text{N}$ ja etelänapa $\text{S}$: se on magneettinen dipoli. Samannimiset navat hylkivät ja erinimiset vetävät toisiaan, eikä yksittäistä napaa ole havaittu.
- Ferromagneettisissa aineissa, kuten raudassa, atomidipolit muodostavat alkeisalueita. Magneetin kenttä järjestää ne, jolloin aine magnetoituu ja magneetti vetää sitä.
- Magneettikentän suunta on se, johon kompassin neulan pohjoispää osoittaa. Kenttäviivat kulkevat magneetin ulkopuolella pohjoisnavasta etelänapaan, ja niiden tiheys kertoo kentän voimakkuuden.
- Sauvamagneettimallissa maantieteellisen pohjoisnavan lähellä on etelänapa, vaikka geomagnetismissa sitä kutsutaan magneettiseksi pohjoisnavaksi. Suomessa Maan kenttä on noin $52\,\mu\text{T}$ ja osoittaa jyrkästi maahan.
- Magneettivuon tiheys $\overline{B}$ on vektori, jonka yksikkö on tesla $\text{T}$. Kentät lasketaan yhteen vektoreina: kohtisuorille kentille $B = \sqrt{B_1^2 + B_2^2}$ ja $\tan\theta = B_2 : B_1$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: jääkaapin ovi, jossa magneetit pitävät kiinni lapsen piirustusta ja kauppalistaa. Oven teräslevy vetää magneetteja puoleensa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-1-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
