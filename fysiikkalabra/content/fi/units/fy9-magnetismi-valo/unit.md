# Magnetismi, induktio ja valo

> **Miksi** saaren mökeille tuleva sähkö kulkee merikaapelissa $20\,\text{kV}$:n jännitteellä, vaikka mökeissä käytetään $230\,\text{V}$:n jännitettä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: saaristomaisema poikkileikkauksena iltahämärässä. Vasemmalla mantereen rannalla voimajohdon pylväs ja harmaa muuntamo. Muuntamosta lähtee tumma merikaapeli, joka laskeutuu kalliorantaa pitkin meren pohjaan, kulkee hiekkapohjaa pitkin veden alla ja nousee oikealla saareen. Saaressa on toinen pieni muuntamo ja punainen mökki, jonka ikkunasta loistaa valo. Mökin takana koivu ja kuusi, taivaanrannassa kaukaisia saaria." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Moduulin ilmiöt liittyvät kahteen kenttään. **Magneettikenttä** $\overline{B}$ ei vaikuta levossa olevaan varaukseen; liikkuvaan varaukseen ja virtajohtimeen se kohdistaa voiman, kun liike tai virta ei ole kentän suuntainen, ja voima on kohtisuorassa sekä liikettä että kenttää vastaan. **Muuttuva magneettivuo** synnyttää jännitteen: tähän perustuvat generaattori, muuntaja, induktioliesi ja pyörrevirtajarru. Kun sähkö- ja magneettikenttä muuttuvat ja synnyttävät toisensa, syntyy **sähkömagneettinen aalto**, jonka näkyvä osa on valo.

```pysahdy
Mitä käämin magneettivuolle täytyy tapahtua, jotta käämiin indusoituu jännite?
---
Magneettivuon täytyy muuttua. Jos vuo pysyy samana, jännitettä ei synny.
```

<svg data-fig="kartta" viewBox="0 0 380 866" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Tee ensin kuva ja merkitse suunnat, ja katso sitten, mikä  tehtävän tunnusmerkki sopii. Hiukkanen liikkuu kentässä: magneettinen voima on varaus kertaa nopeus kertaa  kohtisuora magneettivuon tiheys. Virtajohdin kentässä: voima on virta kertaa johtimen pituus kertaa kohtisuora  magneettivuon tiheys. Hiukkanen kiertää ympyrää: magneettinen voima on keskeisvoima, ja säde on massa kertaa  nopeus jaettuna varauksen ja magneettivuon tiheyden tulolla. Magneettivuo muuttuu: käämiin indusoituva jännite  on miinus kierrosluku kertaa vuon muutos jaettuna ajalla. Muuntaja: kierroslukujen suhde on jännitteiden suhde.  Generaattori pyörii: indusoituvan jännitteen huippuarvo on kierrosluku kertaa pinta-ala kertaa magneettivuon  tiheys kertaa kaksi pii kertaa taajuus. Valo kulkee aineesta toiseen: taittumisessa käytetään Snellin lakia.  Valo ei pääse ulos aineesta: kokonaisheijastuksen rajakulman sini on taitekertoimien suhde. Valo osuu hilaan:  hilayhtälö on rakovälin ja kulman sinin tulo yhtä suuri kuin kertaluku kertaa aallonpituus." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{kuva ja suunnat ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{hiukkanen liikkuu kentässä}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voima}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{M} = QvB_\perp$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{virtajohdin kentässä}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voima}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{M} = I\ell B_\perp$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{hiukkanen kiertää ympyrää}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{keskeisvoima}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$r = mv/(QB)$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{magneettivuo muuttuu}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{induktio}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$e = -N\Delta\Phi/\Delta t$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{muuntaja}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kierrokset ja jännite}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$N_1/N_2 = U_1/U_2$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{generaattori pyörii}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{huippujännite}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$u_0 = NAB\,2\pi f$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{valo kulkee aineesta toiseen}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{taittuminen}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{Snellin laki}$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{valo ei pääse ulos aineesta}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kokonaisheijastus}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\sin\alpha_\text{r} = n_2/n_1$</div></foreignObject>
  <line x1="14" y1="822" x2="30" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{valo osuu hilaan}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{interferenssi}$</div></foreignObject>
  <rect x="238" y="830" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="832" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$d\sin\alpha = n\lambda$</div></foreignObject>
</svg>

Kokeen tehtävissä kannattaa ensin kysyä, mikä muuttuu. Jos vuo ei muutu, jännitettä ei synny. Kun valo siirtyy aineesta toiseen, taajuus säilyy, mutta nopeus ja aallonpituus muuttuvat. Valon värit ja kirkkaat ja tummat kohdat selittyvät joko taittumisella tai interferenssillä, ja tehtävässä on tunnistettava, kummasta on kyse.

Tästä saadaan vastaus alun kysymykseen. Kaapelia pitkin siirretään mantereelta $40\,\text{kW}$:n teho, ja kaapelin resistanssi on $0{,}50\,\Omega$. Jännitteellä $230\,\text{V}$ kaapelissa kulkisi virta $I = \tfrac{P}{U} \approx 174\,\text{A}$, ja kaapelin resistanssissa sisäenergiaksi muuttuisi noin $15\,\text{kW}$ eli $38\,\%$ tehosta (häviöteho johdetaan kohdassa *Induktio ja vaihtovirta*). Jännitteellä $20\,\text{kV}$ virta on vain $2{,}0\,\text{A}$, ja häviö on $2{,}0\,\text{W}$. Muuntajat nostavat jännitteen mantereella ja laskevat sen saaressa.

<svg data-fig="siirto" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva mittakaavassa: sama 40 kilowatin teho siirretään kaapelilla, jonka resistanssi on 0,50 ohmia. Ylempi palkki: jännitteellä 230 volttia virta on 174 ampeeria, ja palkin ruskeanpunainen osa, kaapelin sisäenergiaksi muuttuva teho 15 kilowattia, on 38 prosenttia koko palkista. Alempi palkki: jännitteellä 20 kilovolttia virta on 2,0 ampeeria, ja sisäenergiaksi muuttuu vain 2,0 wattia, 0,005 prosenttia, mikä on palkissa ohuempi kuin viiva." style="max-width:100%;font-size:24px">
  <foreignObject x="194.5" y="7.5" width="211" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P = 40\,\text{kW},\ R = 0{,}50\,\Omega$</div></foreignObject>
  <foreignObject x="24" y="59.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 230\,\text{V}$</div></foreignObject>
  <foreignObject x="481" y="59.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I \approx 174\,\text{A}$</div></foreignObject>
  <rect x="24" y="100" width="552" height="46" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="367.5" y="100" width="208.5" height="46" fill="#8f3b1b"/>
  <rect x="24" y="100" width="552" height="46" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="108.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{perille } 25\,\text{kW}$</div></foreignObject>
  <foreignObject x="494" y="108.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$15\,\text{kW}$</div></foreignObject>
  <foreignObject x="456" y="155.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8f3b1b">$\text{häviö } 38\,\%$</div></foreignObject>
  <foreignObject x="24" y="199.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 20\,\text{kV}$</div></foreignObject>
  <foreignObject x="481" y="199.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I = 2{,}0\,\text{A}$</div></foreignObject>
  <rect x="24" y="240" width="552" height="46" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="574" y="240" width="2" height="46" fill="#8f3b1b"/>
  <rect x="24" y="240" width="552" height="46" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="248.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{perille lähes } 40\,\text{kW}$</div></foreignObject>
  <foreignObject x="343" y="295.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8f3b1b">$\text{häviö } 2{,}0\,\text{W} = 0{,}005\,\%$</div></foreignObject>
</svg>

## Kaava: Magnetismi, induktio ja valo

### Magneettikenttä ja voimat

```kaavat
varattuun hiukkaseen kohdistuva magneettinen voima :: F_\text{M} = QvB_\perp
suoraan johtimeen kohdistuva magneettinen voima :: F_\text{M} = I\ell B_\perp
suoran virtajohtimen magneettivuon tiheys :: B = \frac{\mu_0}{2\pi r}\,I
pitkän käämin magneettivuon tiheys :: B = N\,\frac{\mu_0}{\ell}\,I
```

missä $F_\text{M}$ on magneettinen voima ($\text{N}$), $Q$ varaus ($\text{C}$), $v$ vauhti ($\text{m/s}$), $B$ magneettivuon tiheys ($\text{T}$), $B_\perp = B\sin\alpha$ sen nopeutta tai johdinta vastaan kohtisuora komponentti, kun $\alpha$ on nopeuden tai johtimen ja kentän välinen kulma, $r$ etäisyys johtimesta ($\text{m}$), $I$ virta ($\text{A}$), $\ell$ johtimen tai käämin pituus ($\text{m}$), $N$ kierrosten lukumäärä ja $\mu_0 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$. Magneettinen voima ei muuta vauhtia. Johtimen kaava pätee pitkälle suoralle johtimelle ja käämin kaava pitkän käämin keskelle.

Kun varattu hiukkanen, jonka massa on $m$ ($\text{kg}$) ja varaus $Q$, liikkuu vauhdilla $v$ kohtisuoraan homogeenista magneettikenttää vastaan, magneettinen voima on koko ajan kohtisuorassa nopeutta vastaan. Hiukkanen kulkee silloin tasaista ympyräliikettä radalla, jonka säde on $r$ ($\text{m}$).

```pysahdy
Miksi magneettinen voima ei muuta varatun hiukkasen vauhtia?
---
Voima on koko ajan kohtisuorassa nopeutta vastaan, joten se muuttaa vain liikkeen suuntaa.
```

<svg data-fig="ympyra" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva: positiivinen hiukkanen homogeenisessa magneettikentässä, joka osoittaa paperiin sisään (vihreät ristit). Hiukkasen rata on katkoviivalla piirretty ympyrä, jota se kiertää vastapäivään. Neljässä radan kohdassa sininen nopeusnuoli on radan suuntainen ja punainen magneettisen voiman nuoli osoittaa ympyrän keskipisteeseen, kohtisuoraan nopeutta vastaan. Säde r on merkitty keskipisteestä rataan." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-ympyra.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="302" y="169.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="241" y="342" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="381" y="202" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="241" y="62" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="101" y="202" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="334" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="264" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{M}$</div></foreignObject>
  <foreignObject x="453" y="387.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{paperiin}$</div></foreignObject>
</svg>

```johda
Varattu hiukkanen (massa $m$, varaus $Q$) liikkuu vauhdilla $v$ kohtisuoraan homogeenista magneettikenttää $B$ vastaan. Johda hiukkasen ympyräradan säde $r$.
---
Magneettinen voima on kohtisuorassa nopeutta vastaan, joten se ei muuta vauhtia vaan vain liikkeen suuntaa: hiukkanen on tasaisessa ympyräliikkeessä. Magneettinen voima on ainoa vaikuttava voima, joten Newtonin 2. lain mukaan se antaa hiukkaselle normaalikiihtyvyyden $a_\text{n} = \tfrac{v^2}{r}$:

$$F_\text{M} = ma_\text{n} = m\frac{v^2}{r}$$

Nopeus on kohtisuorassa kenttää vastaan, joten $B_\perp = B$, ja varattuun hiukkaseen kohdistuva magneettinen voima on $F_\text{M} = QvB$. Sijoitetaan:

$$QvB = m\frac{v^2}{r}$$

Jaetaan puolittain $v$:llä ja ratkaistaan säde:

$$r = \frac{mv}{QB}$$

Tässä $Q$ on varauksen itseisarvo. Tulos pätee, kun vauhti on pieni valon nopeuteen verrattuna ja painovoima on häviävän pieni magneettiseen voimaan verrattuna.
```

### Induktio ja vaihtovirta

```kaavat
käämiin indusoituva jännite :: e = -N\frac{\Delta\Phi}{\Delta t}
generaattorissa käämiin indusoituvan sinimuotoisen vaihtojännitteen huippuarvo :: u_0 = NAB\cdot 2\pi f
sinimuotoisen vaihtojännitteen tehollinen arvo :: U_\text{eff} = \frac{u_0}{\sqrt{2}}
muuntaja :: \frac{N_1}{N_2} = \frac{U_1}{U_2} \approx \frac{I_2}{I_1}
```

missä $e$ on induktiojännite ($\text{V}$), $\Phi = BA$ magneettivuo ($\text{Wb}$), kun kenttä on kohtisuorassa pintaa $A$ vastaan, $u_0$ generaattorin jännitteen huippuarvo, $f$ pyörimistaajuus ($\text{Hz}$), $U_\text{eff}$ ja $u_0$ tehollinen arvo ja huippuarvo, indeksit $1$ ja $2$ muuntajan ensiö- ja toisiopuoli. Miinusmerkki on Lenzin laki: induktiovirta vastustaa vuon muutosta. Kentässä liikkuvan tangon jännite on $e = vBl$. Muuntajan yhtälö koskee vaihtojännitettä; virtojen suhde on yhtäsuuruus vain ideaalisessa, häviöttömässä muuntajassa.

Siirtojohtoa pitkin siirretään teho $P$ ($\text{W}$) siirtojännitteellä $U$ ($\text{V}$), ja johdon resistanssi on $R$ ($\Omega$). Osa tehosta muuttuu johdon sisäenergiaksi, joka siirtyy lämpönä ympäristöön, ja tämä häviöteho $P_\text{h}$ ($\text{W}$) riippuu johdossa kulkevasta virrasta.

```johda
Siirtojohtoa pitkin siirretään teho $P$ jännitteellä $U$, ja johdon resistanssi on $R$. Johda johdon häviöteho $P_\text{h}$ ensin virran $I$ avulla ja sitten tehon $P$ ja jännitteen $U$ avulla.
---
Johdossa kulkeva virta saadaan siirrettävästä tehosta. Tehonkulutus johtimessa on $P = UI$, joten

$$I = \frac{P}{U}$$

Siirtojännite $U$ ei ole johdon yli. Johdon päiden välinen jännite on jännitehäviö johtimessa $RI$, ja johdossa sisäenergiaksi muuttuva teho on tämän jännitteen ja virran tulo:

$$P_\text{h} = RI \cdot I = RI^2$$

Sijoitetaan virta:

$$P_\text{h} = R\left(\frac{P}{U}\right)^2 = \frac{RP^2}{U^2}$$

Häviö on kääntäen verrannollinen siirtojännitteen neliöön. Kun muuntaja nostaa siirtojännitteen $10$-kertaiseksi, virta pienenee kymmenesosaan ja häviö sadasosaan.
```

### Valo

```kaavat
aaltoliikkeen perusyhtälö :: c = f\lambda
Wienin siirtymälaki :: \lambda_\text{max} = \frac{b}{T}
taittumislaki (Snellin laki) :: \frac{\sin\alpha_1}{\sin\alpha_2} = \frac{v_1}{v_2} = \frac{n_2}{n_1}
hilayhtälö :: d\sin\alpha = n\lambda
I = I_0\cos^2\theta
```

missä $c = 3{,}00 \cdot 10^8\,\text{m/s}$, $f$ taajuus, $\lambda$ aallonpituus, $T$ absoluuttinen lämpötila ($\text{K}$), $b = 2{,}898 \cdot 10^{-3}\,\text{m} \cdot \text{K}$, $n = \tfrac{c}{v}$ taitekerroin ja $v$ valon nopeus aineessa, $\alpha_1$ ja $\alpha_2$ tulo- ja taitekulma normaalista, $d$ hilavakio, hilayhtälössä $\alpha$ maksimin suunta ja $n = 0, 1, 2, \ldots$ kertaluku ja $I_0$ polarisoituneen valon intensiteetti ennen analysaattoria. Malusin laissa $\theta$ on polarisaation suunnan ja analysaattorin läpäisysuunnan välinen kulma. Ohuessa kalvossa matkaero on $2nd$, kun valo tulee lähes kohtisuoraan. Kun vain toinen heijastus kääntää aallon, $2nd = \left(k + \tfrac12\right)\lambda$ antaa vahvistavan interferenssin; kun molemmat kääntävät, $2nd = k\lambda$.

Kun valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen ($n_1 > n_2$), taitekulma on tulokulmaa suurempi. Tulokulma, jolla taitekulma on $90^\circ$, on rajakulma $\alpha_\text{r}$, ja sitä suuremmilla tulokulmilla valo kokonaisheijastuu.

```pysahdy
Taittuuko valo kohti pinnan normaalia vai siitä poispäin, kun se tulee aineesta, jonka taitekerroin on suurempi, aineeseen, jonka taitekerroin on pienempi?
---
Taitekulma on tällöin tulokulmaa suurempi, joten säde taittuu pois normaalista.
```

<svg data-fig="rajakulma" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei lukuarvoja. Alhaalla on aine, jonka taitekerroin n 1 on suurempi, ja ylhäällä aine, jonka taitekerroin n 2 on pienempi. Pohjalla oleva lamppu lähettää kaksi valonsädettä rajapintaan. Osumakohtiin on piirretty pinnan normaali katkoviivana. Vasemman säteen tulokulma on rajakulma alfa r: taittunut säde kulkee pitkin rajapintaa, eli taitekulma alfa 2 on 90 astetta, ja heikko osa heijastuu takaisin. Oikean säteen tulokulma on rajakulmaa suurempi: valo ei taitu ylempään aineeseen, vaan koko säde heijastuu takaisin, eli tapahtuu kokonaisheijastuminen." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-rajakulma.webp" x="1.2" y="1.2" width="597" height="335.8" preserveAspectRatio="none"/>
  <foreignObject x="226" y="195.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_\text{r}$</div></foreignObject>
  <foreignObject x="309.5" y="81.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_2 = 90^\circ$</div></foreignObject>
  <foreignObject x="389.5" y="19.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1 > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="24" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_2$</div></foreignObject>
  <foreignObject x="24" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1$</div></foreignObject>
  <foreignObject x="300" y="275.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{kokonaisheijastuminen}$</div></foreignObject>
</svg>

```johda
Valo tulee aineesta, jonka taitekerroin on $n_1$, rajapinnalle aineeseen, jonka taitekerroin on $n_2 < n_1$. Johda kokonaisheijastumisen rajakulma $\alpha_\text{r}$.
---
Taittumislaki (Snellin laki) yhdistää tulokulman $\alpha_1$ ja taitekulman $\alpha_2$:

$$\frac{\sin\alpha_1}{\sin\alpha_2} = \frac{n_2}{n_1}$$

Rajakulmalla taittunut säde kulkee pitkin rajapintaa, eli $\alpha_1 = \alpha_\text{r}$ ja $\alpha_2 = 90^\circ$. Koska $\sin 90^\circ = 1$, saadaan

$$\sin\alpha_\text{r} = \frac{n_2}{n_1}$$

Suuremmalla tulokulmalla taittumislaista tulisi $\sin\alpha_2 > 1$, mikä on mahdotonta. Valo ei silloin taitu toiseen aineeseen vaan heijastuu kokonaan takaisin.
```

## Yleisiä virheitä {Virheet}

- **Voima kentän suuntaan.** Magneettinen voima on kohtisuorassa nopeutta ja kenttää vastaan, ja negatiiviseen varaukseen se osoittaa vastakkaiseen suuntaan.
- **Suuri kenttä, suuri jännite.** Induktiojännite riippuu vuon muutosnopeudesta, ei vuon suuruudesta.
- **Lenz vastustaa kenttää.** Induktiovirta vastustaa vuon muutosta: loittonevaa magneettia rengas vetää.
- **Häviö kaavasta $\tfrac{U^2}{R}$.** Siirtojännite ei ole johdon yli. Laske ensin virta $I = \tfrac{P}{U}$ ja sitten häviöteho johdon resistanssista ja virrasta.
- **Huippuarvo ja tehollinen arvo sekaisin.** Pistorasian $230\,\text{V}$ on tehollinen arvo.
- **Kulma pinnasta.** Tulo- ja taitekulmat mitataan normaalista.
- **Pieni kulma hilassa.** Laske kulma ensin tangentista $\tan\theta = \tfrac{x}{L}$ ja vasta sitten sini.
- **Wien celsiusasteina.** Lämpötila on kelvineinä.

## Kertaa tarvittaessa {Kertaa}

- Kenttä ja voimat: [*Magneetit, magneettinen dipoli ja magneettikenttä*](fy7-1.html), [*Varatun hiukkasen liike sähkö- ja magneettikentässä*](fy7-2.html), [*Virtajohtimen ja käämin magneettikenttä*](fy7-3.html) ja [*Voima virtajohtimeen: sähkömoottori ja kaiutin*](fy7-4.html).
- Induktio: [*Sähkömagneettinen induktio*](fy7-5.html), [*Lenzin laki ja pyörrevirrat*](fy7-6.html), [*Generaattori ja vaihtovirta*](fy7-7.html) ja [*Muuntaja ja sähköenergian siirto*](fy7-8.html).
- Säteily ja valon kulku: [*Sähkömagneettinen säteily ja mustan kappaleen spektri*](fy7-9.html), [*Valon heijastuminen ja taittuminen*](fy7-10.html), [*Dispersio: prisma ja sateenkaari*](fy7-11.html) ja [*Kokonaisheijastuminen ja valokuitu*](fy7-12.html).
- Valo aaltona: [*Valon interferenssi ja diffraktio*](fy7-13.html), [*Ohuen kalvon interferenssi*](fy7-14.html) ja [*Valon polarisaatio*](fy7-15.html).
- Sovellukset: [*Soveltava luku: langaton lataus, induktioliesi ja kuituyhteys*](fy7-16.html).
