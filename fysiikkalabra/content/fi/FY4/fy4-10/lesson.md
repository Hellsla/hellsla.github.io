# Liikemäärän säilyminen ja yksiulotteiset törmäykset

> **Miksi** biljardin lyöntipallo voi pysähtyä paikalleen, kun se osuu suoraan levossa olevaan palloon, ja toinen pallo jatkaa matkaa lähes samalla nopeudella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: biljardipöytä läheltä nähtynä pöydän yllä roikkuvan lampun valossa. Vasemmalta alhaalta pöydälle osoittaa biljardikeppi, jolla valkoista lyöntipalloa on juuri lyöty. Lyöntipallo on osunut suoraan punaiseen palloon ja pysähtynyt pöydän keskelle; sen takana näkyy haalea jälki kuljetusta matkasta. Punainen pallo kiitää eteenpäin kohti pöydän oikeaa reunaa, ja sen takana on liikeviivoja. Pöydän takaosassa on kolme muuta palloa." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy410h-wall" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="420"><stop offset="0" stop-color="#f6f1e6"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy410h-panel" gradientUnits="userSpaceOnUse" x1="0" y1="150" x2="0" y2="270"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#8a5f22"/></linearGradient><linearGradient id="fy410h-felt" gradientUnits="userSpaceOnUse" x1="0" y1="180" x2="0" y2="640"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><radialGradient id="fy410h-yellow" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><radialGradient id="fy410h-blue" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></radialGradient><radialGradient id="fy410h-black" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#1f2933"/></radialGradient><radialGradient id="fy410h-white" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></radialGradient><radialGradient id="fy410h-red" cx="0.35" cy="0.3" r="0.75"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy410h-wall)"/>
  <rect x="0" y="150" width="1200" height="120" fill="url(#fy410h-panel)"/>
  <line x1="75" y1="150" x2="75" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="225" y1="150" x2="225" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="375" y1="150" x2="375" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="525" y1="150" x2="525" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="675" y1="150" x2="675" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="825" y1="150" x2="825" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="975" y1="150" x2="975" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1125" y1="150" x2="1125" y2="270" stroke="#8a5f22" stroke-width="3" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="1200" y2="150" stroke="#8a5f22" stroke-width="4" stroke-linecap="butt"/>
  <line x1="600" y1="0" x2="600" y2="40" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M420,118 L780,118 L1080,520 L120,520 Z" fill="#ffc078" fill-opacity="0.16"/>
  <path d="M430,118 L770,118 L720,44 L480,44 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="450" y="118" width="300" height="8" rx="3" fill="#ffc078"/>
  <path d="M20,590 L1180,590 L1040,236 L160,236 Z" fill="#b8622d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M20,590 L1180,590 L1180,600 L20,600 Z" fill="#8a5f22" stroke-linejoin="round"/>
  <path d="M74,566 L1126,566 L1006,256 L194,256 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M104,550 L1096,550 L986,270 L214,270 Z" fill="url(#fy410h-felt)" stroke-linejoin="round"/>
  <ellipse cx="600" cy="400" rx="380" ry="120" fill="#ffffff" fill-opacity="0.16"/>
  <ellipse cx="64" cy="572" rx="34" ry="17" fill="#1f2933"/>
  <ellipse cx="600" cy="576" rx="32" ry="16" fill="#1f2933"/>
  <ellipse cx="1136" cy="572" rx="34" ry="17" fill="#1f2933"/>
  <ellipse cx="180" cy="250" rx="24" ry="12" fill="#1f2933"/>
  <ellipse cx="600" cy="248" rx="22" ry="11" fill="#1f2933"/>
  <ellipse cx="1020" cy="250" rx="24" ry="12" fill="#1f2933"/>
  <circle cx="300" cy="578" r="5" fill="#f1dfb5"/>
  <circle cx="340" cy="244" r="4" fill="#f1dfb5"/>
  <circle cx="900" cy="578" r="5" fill="#f1dfb5"/>
  <circle cx="860" cy="244" r="4" fill="#f1dfb5"/>
  <ellipse cx="364" cy="318" rx="19" ry="5.5" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="360" cy="300" r="20" fill="url(#fy410h-yellow)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="874" cy="314" rx="19" ry="5.5" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="870" cy="296" r="20" fill="url(#fy410h-blue)" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="918" cy="337" rx="20" ry="6" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="914" cy="318" r="21" fill="url(#fy410h-black)" stroke="#1f2933" stroke-width="2"/>
  <line x1="330" y1="440" x2="356" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="372" y1="440" x2="398" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="414" y1="440" x2="440" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="456" y1="440" x2="482" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="498" y1="440" x2="524" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="540" y1="440" x2="566" y2="440" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="626.5" cy="461" rx="30.5" ry="9" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="620" cy="432" r="32" fill="url(#fy410h-white)" stroke="#1f2933" stroke-width="2"/>
  <line x1="700" y1="414" x2="760" y2="414" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="710" y1="430" x2="764" y2="430" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <line x1="720" y1="446" x2="768" y2="446" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="818.5" cy="459" rx="30.5" ry="9" fill="#1f2933" fill-opacity="0.25"/>
  <circle cx="812" cy="430" r="32" fill="url(#fy410h-red)" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,566 L4,598 L292,468 L284,452 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M-10,566 L4,598 L100,554 L88,524 Z" fill="#8a5f22" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,468 L284,452 L298,446 L306,462 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Systeemi ja sen kokonaisliikemäärä
Luvussa *Liikemäärä ja impulssi* opit, että kappaleen liikemäärä on $\overline{p} = m\overline{v}$ ja että voiman impulssi muuttaa sitä: $\Delta\overline{p} = \overline{F}\,\Delta t$. Törmäyksessä on kuitenkin kaksi kappaletta, jotka vaikuttavat toisiinsa. Siksi tarkastellaan niitä yhdessä **systeeminä**. Systeemin **kokonaisliikemäärä** on sen kappaleiden liikemäärien vektorisumma, $\overline{p}_\text{kok} = \overline{p}_1 + \overline{p}_2$.

Systeemin kappaleiden toisiinsa kohdistamat voimat ovat **sisäisiä voimia**, esimerkiksi vaunujen puskurien voimat toisiinsa törmäyksessä. Systeemin ulkopuolelta tulevat voimat ovat **ulkoisia voimia**, esimerkiksi vaunujen paino, radan tukivoima ja kitka.

### Miksi kokonaisliikemäärä säilyy
Kun vaunu 1 työntää vaunua 2 voimalla $\overline{F}$, Newtonin kolmannen lain mukaan vaunu 2 työntää vaunua 1 yhtä suurella vastakkaissuuntaisella voimalla $-\overline{F}$. Voimat alkavat ja loppuvat samalla hetkellä, joten ne vaikuttavat saman ajan $\Delta t$. Vaunun 2 liikemäärä muuttuu impulssin $\overline{F}\,\Delta t$ verran ja vaunun 1 liikemäärä yhtä paljon vastakkaiseen suuntaan. Se, minkä toinen vaunu saa liikemäärää, on täsmälleen se, minkä toinen menettää. Kokonaisliikemäärä ei muutu. Sama pätee, vaikka voima muuttuisi törmäyksen aikana, koska voimat ovat joka hetki yhtä suuret ja vastakkaissuuntaiset.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi ilmatyynyradan vaunua törmäyksen aikana. Vaunujen väliin jäävä jousipuskuri on puristunut. Ylhäällä punaiset voimanuolet: vaunu 1 työntää vaunua 2 oikealle voimalla F, ja vaunu 2 työntää vaunua 1 vasemmalle yhtä suurella vastakkaissuuntaisella voimalla −F. Molemmat voimat vaikuttavat saman ajan Δt. Alhaalla violetit nuolet ovat liikemäärien muutokset: vaunun 1 muutos Δp1 = −FΔt osoittaa vasemmalle ja vaunun 2 muutos Δp2 = FΔt oikealle, yhtä pitkinä. Niiden summa on nolla." style="max-width:100%;font-size:24px">
  <rect x="30" y="150" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="157" r="1.8" fill="#8a96a3"/>
  <rect x="135" y="86" width="150" height="64" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="141" y="144" width="138" height="6" fill="#8a96a3"/>
  <rect x="325" y="86" width="150" height="64" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="331" y="144" width="138" height="6" fill="#8a96a3"/>
  <foreignObject x="240" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="350" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <path d="M285,128 L288.5,120 L295,136 L301.5,120 L308.5,136 L315,120 L321.5,136 L325,128" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="325" y1="128" x2="426" y2="128" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,128 L425,135 L425,121 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="285" y1="128" x2="184" y2="128" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M170,128 L185,121 L185,135 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="488.5" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="72.5" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$-\overline{F}$</div></foreignObject>
  <line x1="497" y1="74" x2="440" y2="122" stroke="#c92a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="103" y1="74" x2="170" y2="122" stroke="#c92a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="283.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <line x1="20" y1="196" x2="580" y2="196" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="300" y1="236" x2="185" y2="236" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M170,236 L186,229 L186,243 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="300" y1="236" x2="415" y2="236" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M430,236 L414,243 L414,229 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="300" y1="222" x2="300" y2="250" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="87.5" y="257.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_1 = -\overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="373.5" y="257.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_2 = \overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="221" y="299.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta\overline{p}_1 + \Delta\overline{p}_2 = \overline{0}$</div></foreignObject>
</svg>

Päättely toimii vain, kun ulkoiset voimat eivät muuta liikemäärää. Vaakasuoralla ilmatyynyradalla paino ja tukivoima kumoavat toisensa, ja kitka on hyvin pieni. Törmäävät autot taas kokevat tien kitkan, mutta törmäys kestää vain sekunnin murto-osan. Puskurien voimat ovat silloin paljon suurempia kuin kitka, joten kitkan impulssi jää törmäyksen aikana merkityksettömän pieneksi. Tästä saadaan **liikemäärän säilymislaki**: kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni, systeemin kokonaisliikemäärä säilyy.

### Törmäysten lajit
Liikemäärä säilyy jokaisessa törmäyksessä, kun säilymislain ehto täyttyy. Liike-energia ei säily aina. Törmäys on **kimmoisa**, jos kappaleiden yhteinen liike-energia on törmäyksen jälkeen yhtä suuri kuin ennen sitä. Teräskuulat, biljardipallot ja jousipuskurilla varustetut vaunut törmäävät lähes kimmoisasti. Törmäys on **kimmoton**, jos osa liike-energiasta muuttuu muiksi energiamuodoiksi. Kappaleet muuttavat silloin muotoaan, ja liike-energiaa muuttuu niiden sisäenergiaksi ja ääneksi. Kun kappaleet jäävät kiinni toisiinsa ja jatkavat yhdessä, törmäys on **täysin kimmoton**, ja liike-energiaa häviää suurin mahdollinen määrä.

<svg data-fig="tarra" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva mittakaavassa: kaksi samanmassaista vaunua ilmatyynyradalla, ylhäällä ennen törmäystä ja alhaalla sen jälkeen. Ennen törmäystä vaunu 1 liikkuu oikealle nopeudella v, ja sen liikemäärä p on violetti nuoli; vaunu 2 on levossa. Vaunujen päissä on tarranauhat. Törmäyksen jälkeen vaunut ovat tarttuneet yhteen ja liikkuvat yhdessä puolella alkuperäisestä nopeudesta, sininen nuoli on puolet lyhyempi. Yhteisen liikemäärän violetti nuoli on yhtä pitkä kuin vaunun 1 liikemäärä ennen törmäystä." style="max-width:100%;font-size:24px">
  <rect x="30" y="150" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="157" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="157" r="1.8" fill="#8a96a3"/>
  <foreignObject x="36" y="7.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ennen}$</div></foreignObject>
  <rect x="30" y="318" width="540" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <circle cx="44" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="62" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="80" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="98" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="116" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="134" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="152" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="170" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="188" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="206" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="224" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="242" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="260" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="278" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="296" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="314" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="332" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="350" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="368" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="386" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="404" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="422" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="440" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="458" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="476" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="494" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="512" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="530" cy="325" r="1.8" fill="#8a96a3"/>
  <circle cx="548" cy="325" r="1.8" fill="#8a96a3"/>
  <foreignObject x="36" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jälkeen}$</div></foreignObject>
  <rect x="120" y="102" width="100" height="48" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="126" y="144" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="160" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="350" y="102" width="100" height="48" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="356" y="144" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="390" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <rect x="220" y="110" width="5" height="32" fill="#6b7480"/>
  <rect x="345" y="110" width="5" height="32" fill="#6b7480"/>
  <line x1="120" y1="84" x2="241" y2="84" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M252,84 L240,89.5 L240,78.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="260" y="69.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="120" y1="52" x2="237" y2="52" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M252,52 L236,59 L236,45 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="260" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="358.5" y="65.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{0}$</div></foreignObject>
  <line x1="20" y1="178" x2="580" y2="178" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="200" y="270" width="100" height="48" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="206" y="312" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="240" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="300" y="270" width="100" height="48" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="306" y="312" width="88" height="6" fill="#8a96a3"/>
  <foreignObject x="340" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="200" y1="252" x2="255" y2="252" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M266,252 L254,257.5 L254,246.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="274" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\tfrac{1}{2}\overline{v}$</div></foreignObject>
  <line x1="200" y1="220" x2="317" y2="220" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M332,220 L316,227 L316,213 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="340" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
</svg>

Kuvassa samanmassaiset vaunut tarttuvat yhteen tarranauhalla. Kokonaisliikemäärä on sama ennen ja jälkeen, mutta nyt sama liikemäärä jakautuu kaksinkertaiselle massalle, joten yhteinen nopeus on puolet alkuperäisestä. Liike-energia $\tfrac12 mv^2$ ei säily: kaksinkertainen massa ja puolet nopeudesta antavat puolet alkuperäisestä liike-energiasta. Toinen puoli muuttuu tarranauhan ja vaunujen sisäenergiaksi.

### Räjähdys
**Räjähdyksessä** levossa oleva tai yhdessä liikkuva systeemi hajoaa osiin sisäisten voimien vaikutuksesta: jousi laukeaa vaunujen välissä, luistelijat työntävät toisiaan tai ruuti työntää luotia ja kivääriä. Jos systeemi on aluksi levossa, sen kokonaisliikemäärä on nolla ja pysyy nollana. Osat saavat yhtä suuret vastakkaissuuntaiset liikemäärät, ja kevyempi osa saa suuremman nopeuden. Siksi kivääri potkaisee taaksepäin, kun luoti lähtee eteenpäin. Liike-energia kasvaa räjähdyksessä, koska jousen, lihasten tai ruudin energiaa muuttuu liike-energiaksi.

### Vastaus alun kysymykseen
Biljardipallot ovat yhtä raskaita, ja niiden törmäys on lähes kimmoisa. Kun lyöntipallon nopeus on $v$, liikemäärän säilymisestä seuraa, että pallojen nopeuksien summa pysyy samana: $v_1' + v_2' = v$. Liike-energian säilymisestä seuraa, että nopeuksien neliöiden summa pysyy samana: $v_1'^2 + v_2'^2 = v^2$. Kumpikin ehto täyttyy vain, jos toinen palloista on törmäyksen jälkeen levossa. Lyöntipallo ei voi kulkea toisen läpi, joten se pysähtyy, ja toinen pallo jatkaa nopeudella $v$. Todellisuudessa pallot myös pyörivät ja törmäys ei ole täysin kimmoisa, joten lyöntipallo voi jäädä hiukan liikkeeseen.

## Kaava: Liikemäärän säilymislaki

### Säilymislaki vektoreina ja yhdessä ulottuvuudessa
Kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen tai räjähdyksen aikana merkityksettömän pieni, kokonaisliikemäärä on sama ennen ja jälkeen:
```latex
\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'
```
missä $\overline{p}_1$ ja $\overline{p}_2$ ovat kappaleiden liikemäärät ennen ja $\overline{p}_1'$ ja $\overline{p}_2'$ niiden liikemäärät jälkeen ($\text{kg}\cdot\text{m/s}$).

Yksiulotteisessa törmäyksessä kaikki nopeudet ovat samalla suoralla. Valitaan positiivinen suunta, jolloin jokainen nopeus on etumerkillinen luku: vastakkaiseen suuntaan liikkuvan kappaleen nopeus on negatiivinen. Säilymislaki tulee muotoon
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```
missä $m_1$ ja $m_2$ ovat kappaleiden massat ($\text{kg}$), $v_1$ ja $v_2$ niiden nopeudet ennen ja $v_1'$ ja $v_2'$ nopeudet jälkeen ($\text{m/s}$).

### Täysin kimmoton törmäys
Kun kappaleet jäävät kiinni toisiinsa, niillä on törmäyksen jälkeen yhteinen nopeus $v'$:
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = (m_1 + m_2)\,v'
\end{aligned}
```
missä $v'$ on kappaleiden yhteinen nopeus törmäyksen jälkeen ($\text{m/s}$). Esimerkiksi kun $0{,}40\,\text{kg}$:n vaunu nopeudella $0{,}60\,\text{m/s}$ tarttuu levossa olevaan samanlaiseen vaunuun, yhteinen nopeus on $0{,}30\,\text{m/s}$, ja liike-energia pienenee $0{,}072\,\text{J}$:sta $0{,}036\,\text{J}$:iin.

### Kimmoisa törmäys
Kimmoisassa törmäyksessä säilyy liikemäärän lisäksi kappaleiden yhteinen liike-energia:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{k},2} \\
&\quad = E_{\text{k},1}' + E_{\text{k},2}'
\end{aligned}
```
missä $E_\text{k} = \tfrac12 mv^2$ on kunkin kappaleen liike-energia ennen ja $E_\text{k}'$ jälkeen ($\text{J}$). Kun tunnetaan toisen kappaleen nopeus törmäyksen jälkeen, toinen saadaan liikemäärän säilymislaista, ja liike-energioita vertaamalla nähdään, oliko törmäys kimmoisa. Kun samanmassainen kappale osuu suoraan levossa olevaan kappaleeseen kimmoisasti, kappaleet vaihtavat nopeuksia.

<svg data-fig="tyypit" viewBox="0 0 600 434" role="img" aria-label="Kaavakuva, liikemäärät mittakaavassa: kolme tapahtumaa kahdelle samanmassaiselle vaunulle, vasemmalla ennen ja oikealla jälkeen. Ylimpänä kimmoisa törmäys: ennen vaunulla 1 on liikemäärä oikealle ja vaunu 2 on levossa, jälkeen vaunu 1 on levossa ja vaunulla 2 on sama liikemäärä; liike-energia säilyy. Keskellä täysin kimmoton törmäys: vaunut tarttuvat yhteen, ja yhteinen liikemäärä on yhtä suuri kuin ennen; liike-energia pienenee. Alimpana räjähdys: ennen vaunut ovat yhdessä levossa ja kokonaisliikemäärä on nolla, jälkeen vaunuilla on yhtä suuret vastakkaissuuntaiset liikemäärät; liike-energia kasvaa." style="max-width:100%;font-size:24px">
  <foreignObject x="90" y="45.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kimmoisa: } E_\text{k}\ \text{säilyy}$</div></foreignObject>
  <line x1="40" y1="152" x2="270" y2="152" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="152" x2="560" y2="152" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="132" x2="309" y2="132" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,132 L308,136.5 L308,127.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="65" y="122" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="71" y="146" width="38" height="6" fill="#8a96a3"/>
  <rect x="195" y="122" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="201" y="146" width="38" height="6" fill="#8a96a3"/>
  <line x1="70" y1="106" x2="167" y2="106" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,106 L166,112.5 L166,99.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <rect x="335" y="122" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="341" y="146" width="38" height="6" fill="#8a96a3"/>
  <rect x="425" y="122" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="431" y="146" width="38" height="6" fill="#8a96a3"/>
  <line x1="440" y1="106" x2="537" y2="106" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M550,106 L536,112.5 L536,99.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="20" y1="170" x2="580" y2="170" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="175.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{täysin kimmoton: } E_\text{k}\ \text{pienenee}$</div></foreignObject>
  <line x1="40" y1="282" x2="270" y2="282" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="282" x2="560" y2="282" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="262" x2="309" y2="262" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,262 L308,266.5 L308,257.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="65" y="252" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="71" y="276" width="38" height="6" fill="#8a96a3"/>
  <rect x="195" y="252" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="201" y="276" width="38" height="6" fill="#8a96a3"/>
  <line x1="70" y1="236" x2="167" y2="236" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,236 L166,242.5 L166,229.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <rect x="395" y="252" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="401" y="276" width="38" height="6" fill="#8a96a3"/>
  <rect x="445" y="252" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="451" y="276" width="38" height="6" fill="#8a96a3"/>
  <line x1="390" y1="236" x2="487" y2="236" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M500,236 L486,242.5 L486,229.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="20" y1="300" x2="580" y2="300" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="305.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{räjähdys: } E_\text{k}\ \text{kasvaa}$</div></foreignObject>
  <line x1="40" y1="412" x2="270" y2="412" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="330" y1="412" x2="560" y2="412" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="282" y1="392" x2="309" y2="392" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M318,392 L308,396.5 L308,387.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="105" y="382" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="111" y="406" width="38" height="6" fill="#8a96a3"/>
  <rect x="155" y="382" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="161" y="406" width="38" height="6" fill="#8a96a3"/>
  <path d="M150,397 L152.5,392 L157.5,402 L160,397" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="113.5" y="349.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$p_\text{kok} = 0$</div></foreignObject>
  <rect x="345" y="382" width="50" height="30" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="351" y="406" width="38" height="6" fill="#8a96a3"/>
  <rect x="495" y="382" width="50" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="501" y="406" width="38" height="6" fill="#8a96a3"/>
  <line x1="390" y1="366" x2="337" y2="366" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M324,366 L338,359.5 L338,372.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <line x1="500" y1="366" x2="553" y2="366" stroke="#7048e8" stroke-width="4" stroke-linecap="butt"/>
  <path d="M566,366 L552,372.5 L552,359.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="120" y="3.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="397.5" y="3.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
</svg>

Liikemäärän säilymislakia käytetään vain itse törmäyksen tai räjähdyksen yli, lyhyen ajan alusta loppuun. Ennen ja jälkeen ulkoiset voimat, kuten kitka tai paino, voivat muuttaa kappaleiden liikettä, ja silloin liikettä tarkastellaan muilla laeilla, esimerkiksi energiaperiaatteella.

## Esimerkki
Ratapihalla tavaravaunu A, jonka massa on $32\,000\,\text{kg}$, liikkuu nopeudella $1{,}5\,\text{m/s}$ ja saavuttaa samaan suuntaan nopeudella $0{,}50\,\text{m/s}$ liikkuvan vaunun B, jonka massa on $18\,000\,\text{kg}$. Vaunut kytkeytyvät yhteen ja jatkavat yhdessä. Kuinka suuri on vaunujen yhteinen nopeus heti kytkeytymisen jälkeen?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m_\text{A} = 32\,000\,\text{kg}$, $v_\text{A} = 1{,}5\,\text{m/s}$, $m_\text{B} = 18\,000\,\text{kg}$ ja $v_\text{B} = 0{,}50\,\text{m/s}$. Kysytään yhteistä nopeutta $v'$ heti kytkeytymisen jälkeen.

<!-- vaihe -->

**Periaate.** Valitaan systeemiksi molemmat vaunut ja positiiviseksi suunnaksi vaunujen liikkeen suunta. Kytkeytyminen kestää hetken, ja sen aikana kytkinten voimat ovat sisäisiä voimia. Paino ja kiskojen tukivoima kumoavat toisensa, ja vierimisvastuksen impulssi on lyhyen kytkeytymisen aikana merkityksettömän pieni, joten kokonaisliikemäärä säilyy. Vaunut jäävät kiinni toisiinsa, joten törmäys on täysin kimmoton.

<!-- vaihe -->

**Kaava ratkaistuna.** Liikemäärä ennen on yhtä suuri kuin yhteisen kappaleen liikemäärä jälkeen:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} + m_\text{B} v_\text{B} \\
&\quad = (m_\text{A} + m_\text{B})\,v' \\[6pt]
&v' = \frac{m_\text{A} v_\text{A} + m_\text{B} v_\text{B}}{m_\text{A} + m_\text{B}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: massat ovat kilogrammoina ja nopeudet yksikössä $\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin liikemäärät ennen kytkeytymistä ja sitten yhteinen nopeus:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} \\
&= 32\,000\,\text{kg} \cdot 1{,}5\,\tfrac{\text{m}}{\text{s}} \\
&= 48\,000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&m_\text{B} v_\text{B} \\
&= 18\,000\,\text{kg} \cdot 0{,}50\,\tfrac{\text{m}}{\text{s}} \\
&= 9000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&v' \\
&= \frac{48\,000 + 9000}{50\,000} \cdot \frac{\text{kg}\cdot\text{m/s}}{\text{kg}} \\
&= 1{,}14\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Vaunujen yhteinen nopeus on $v' \approx 1{,}1\,\text{m/s}$ vaunujen alkuperäiseen liikesuuntaan. Tulos ilmoitetaan kahdella merkitsevällä numerolla kuten nopeudet $1{,}5\,\text{m/s}$ ja $0{,}50\,\text{m/s}$.

<!-- vaihe -->

**Järkevyys.** Yhteinen nopeus on vaunujen alkunopeuksien $0{,}50\,\text{m/s}$ ja $1{,}5\,\text{m/s}$ välissä ja lähempänä raskaamman vaunun A nopeutta, kuten pitää. Liike-energia pienenee $38{,}3\,\text{kJ}$:sta $32{,}5\,\text{kJ}$:iin eli noin $15\,\%$, mikä sopii täysin kimmottomaan törmäykseen: liike-energiaa muuttuu kytkimien ja puskurien sisäenergiaksi ja ääneksi.

## Yleinen virhekäsitys
Moni ajattelee, että liike-energia säilyy törmäyksessä samalla tavalla kuin liikemäärä. Liikemäärä säilyy aina, kun ulkoisten voimien impulssi on merkityksettömän pieni, mutta liike-energia säilyy vain kimmoisassa törmäyksessä. Jos yhteen tarttuvien vaunujen nopeus lasketaan liike-energian säilymisestä, tulos on liian suuri.

Toinen virhe on unohtaa etumerkit. Kun kappaleet liikkuvat toisiaan kohti, niiden liikemäärät ovat vastakkaissuuntaiset, ja toinen niistä on negatiivinen. Kolmas virhe on ajatella, että liikemäärä katoaa, kun lattialle pudonnut savipallo pysähtyy. Pallon liikemäärä siirtyy Maahan: pallo ja Maa muodostavat systeemin, jonka kokonaisliikemäärä säilyy, mutta Maan massa on niin suuri, ettei sen nopeuden muutosta huomaa.

## Tiivistelmä
- Systeemin kokonaisliikemäärä säilyy, kun ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen tai räjähdyksen aikana merkityksettömän pieni: $\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'$.
- Säilyminen seuraa Newtonin kolmannesta laista: törmäyksen sisäiset voimat ovat yhtä suuret ja vastakkaissuuntaiset ja vaikuttavat saman ajan, joten kappaleiden liikemäärien muutokset kumoavat toisensa.
- Yhdessä ulottuvuudessa valitaan positiivinen suunta, ja nopeudet ovat etumerkillisiä: $m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$.
- Kimmoisassa törmäyksessä myös liike-energia säilyy. Kimmottomassa törmäyksessä osa liike-energiasta muuttuu sisäenergiaksi, ja täysin kimmottomassa kappaleet jatkavat yhdessä yhteisellä nopeudella.
- Räjähdyksessä levossa olevan systeemin kokonaisliikemäärä pysyy nollana: osat saavat yhtä suuret vastakkaissuuntaiset liikemäärät, ja liike-energia kasvaa.
