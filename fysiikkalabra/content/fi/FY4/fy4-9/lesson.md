# Liikemäärä ja impulssi

> **Miksi** korkeushyppääjä voi pudota riman yli selälleen paksulle patjalle loukkaamatta itseään, vaikka samanlainen pudotus kovalle maalle olisi vaarallinen?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: korkeushyppy ulkostadionilla kesäpäivänä. Kuvan keskellä hyppääjä kaartuu selällään riman yli, ja riman alla on paksu sininen alastulopatja. Katkoviiva näyttää hyppääjän radan, joka kaartuu riman yli alas patjalle. Taustalla on katsomo ja juoksurata, ja patjan vieressä nurmikkoa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-9-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Liikemäärä: massa ja nopeus yhdessä
Luvussa *Newtonin toinen laki* opit, että voima muuttaa kappaleen nopeutta ja että raskaan kappaleen nopeuden muuttaminen vaatii suuremman voiman kuin kevyen. Liikkuvan kappaleen pysäyttämiseen tai kiihdyttämiseen vaikuttavat siis sekä massa että nopeus. Niiden tuloa sanotaan **liikemääräksi**. Kevyellä ja nopealla jalkapallolla voi olla yhtä suuri liikemäärä kuin raskaalla ja hitaalla keilapallolla. Liikemäärä on vektori, jolla on sama suunta kuin nopeudella. Suoraviivaisessa liikkeessä valitaan positiivinen suunta, ja vastakkaiseen suuntaan liikkuvan kappaleen liikemäärä on negatiivinen.

```pysahdy
Jalkapallolla ja keilapallolla on yhtä suuri liikemäärä. Kumpi liikkuu suuremmalla nopeudella ja miksi?
---
Jalkapallo, koska sen massa on pienempi. Liikemäärä on $mv$, joten yhtä suuri tulo vaatii pienemmällä massalla suuremman nopeuden.
```

<svg data-fig="liikemaara" viewBox="0 0 600 370" role="img" aria-label="Kaavakuva, nuolet mittakaavassa: kolme palloa x-akselilla, jonka positiivinen suunta on oikealle. Ylhäällä 0,45 kilogramman jalkapallo liikkuu oikealle nopeudella 20 metriä sekunnissa: pitkä sininen nopeusnuoli ja violetti liikemääränuoli, liikemäärä 9,0 kilogrammametriä sekunnissa. Keskellä 6,0 kilogramman keilapallo liikkuu oikealle nopeudella 1,5 metriä sekunnissa: hyvin lyhyt nopeusnuoli mutta yhtä pitkä liikemääränuoli kuin jalkapallolla, sillä liikemäärä on sama 9,0. Alhaalla jalkapallo liikkuu vasemmalle nopeudella 10 metriä sekunnissa: nuolet osoittavat vasemmalle, ja liikemäärä on miinus 4,5 kilogrammametriä sekunnissa." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy49-liikemaara-c0"><circle cx="70" cy="62" r="22"/></clipPath><clipPath id="fy49-liikemaara-c1"><circle cx="336" cy="274" r="22"/></clipPath></defs>
  <circle cx="70" cy="62" r="22" fill="#ffffff"/>
  <path d="M70,54.5 L77,59.5 L74.5,68 L65.5,68 L63,59.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M74.5,77.5 L77.5,86.5 L70,92 L62.5,86.5 L65.5,77.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c0)"/>
  <path d="M53.5,62.5 L56.5,71 L49,76.5 L41.5,71 L44.5,62.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c0)"/>
  <path d="M61.5,38 L64.5,46.5 L57,52 L49.5,46.5 L52.5,38 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c0)"/>
  <path d="M87.5,38 L90.5,46.5 L83,52 L75.5,46.5 L78.5,38 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c0)"/>
  <path d="M95.5,62.5 L98.5,71 L91,76.5 L83.5,71 L86.5,62.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c0)"/>
  <line x1="70" y1="54.5" x2="70" y2="46.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="77" y1="59.5" x2="84.5" y2="57" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="74.5" y1="68" x2="79" y2="74.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="65.5" y1="68" x2="61" y2="74.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="63" y1="59.5" x2="55.5" y2="57" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="70" cy="62" r="22" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="22.5" y="87.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}45\,\text{kg}$</div></foreignObject>
  <line x1="108" y1="46" x2="336" y2="46" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M348,46 L335,52 L335,40 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="108" y1="78" x2="238" y2="78" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M252,78 L237,85 L237,71 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="388" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v = 20\,\text{m/s}$</div></foreignObject>
  <foreignObject x="388" y="63.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$p = 9{,}0\,\text{kg}\cdot\text{m/s}$</div></foreignObject>
  <line x1="20" y1="122" x2="580" y2="122" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="70" cy="168" r="30" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="62.5" cy="157.5" r="3.3" fill="#1f2933"/>
  <circle cx="73.5" cy="155.5" r="3.3" fill="#1f2933"/>
  <circle cx="69.5" cy="166.5" r="3.3" fill="#1f2933"/>
  <foreignObject x="28.5" y="195.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6{,}0\,\text{kg}$</div></foreignObject>
  <line x1="116" y1="152" x2="125" y2="152" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M134,152 L124,156.5 L124,147.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="116" y1="184" x2="246" y2="184" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M260,184 L245,191 L245,177 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="388" y="137.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v = 1{,}5\,\text{m/s}$</div></foreignObject>
  <foreignObject x="388" y="169.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$p = 9{,}0\,\text{kg}\cdot\text{m/s}$</div></foreignObject>
  <line x1="20" y1="228" x2="580" y2="228" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <circle cx="336" cy="274" r="22" fill="#ffffff"/>
  <path d="M336,266.5 L343,271.5 L340.5,280 L331.5,280 L329,271.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M340.5,289.5 L343.5,298.5 L336,304 L328.5,298.5 L331.5,289.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c1)"/>
  <path d="M319.5,274.5 L322.5,283 L315,288.5 L307.5,283 L310.5,274.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c1)"/>
  <path d="M327.5,250 L330.5,258.5 L323,264 L315.5,258.5 L318.5,250 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c1)"/>
  <path d="M353.5,250 L356.5,258.5 L349,264 L341.5,258.5 L344.5,250 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c1)"/>
  <path d="M361.5,274.5 L364.5,283 L357,288.5 L349.5,283 L352.5,274.5 Z" fill="#1f2933" stroke-linejoin="round" clip-path="url(#fy49-liikemaara-c1)"/>
  <line x1="336" y1="266.5" x2="336" y2="258.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="343" y1="271.5" x2="350.5" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340.5" y1="280" x2="345" y2="286.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="280" x2="327" y2="286.5" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="329" y1="271.5" x2="321.5" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="336" cy="274" r="22" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="288.5" y="299.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}45\,\text{kg}$</div></foreignObject>
  <line x1="298" y1="258" x2="190" y2="258" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M178,258 L191,252 L191,264 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="298" y1="290" x2="240" y2="290" stroke="#7048e8" stroke-width="5" stroke-linecap="butt"/>
  <path d="M226,290 L241,283 L241,297 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="388" y="243.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v = -10\,\text{m/s}$</div></foreignObject>
  <foreignObject x="388" y="275.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$p = -4{,}5\,\text{kg}\cdot\text{m/s}$</div></foreignObject>
  <line x1="40" y1="352" x2="349" y2="352" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360,352 L348,357.5 L348,346.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="368" y="337.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
</svg>

### Voima ja aika muuttavat liikemäärää
Kun kappaleeseen vaikuttaa kokonaisvoima, sen nopeus muuttuu, ja niin muuttuu myös liikemäärä. Muutoksen suuruus riippuu kahdesta asiasta: kuinka suuri voima on ja kuinka kauan se vaikuttaa. Voiman ja sen vaikutusajan tuloa sanotaan **impulssiksi**. Pieni voima pitkän aikaa voi muuttaa liikemäärää yhtä paljon kuin suuri voima lyhyen aikaa. Keihäänheittäjä vetää keihästä pitkän matkan, jotta voima ehtii vaikuttaa mahdollisimman kauan ja keihään liikemäärä kasvaa suureksi.

Sama pätee pysäyttämiseen. Kun liikkuva kappale pysäytetään, sen liikemäärän muutos on määrätty: koko alkuperäinen liikemäärä on poistettava. Pysäyttävä voima voi olla suuri ja lyhytaikainen tai pieni ja pitkäaikainen, mutta voiman ja ajan tulo on kummassakin tapauksessa sama. Kun voiman $x$-komponentti piirretään ajan funktiona, impulssin $x$-komponentti on käyrän ja aika-akselin väliin jäävä etumerkillinen pinta-ala: aika-akselin alapuolinen pinta-ala lasketaan negatiiviseksi. Jos voiman $x$-komponentti on negatiivinen, myös sen impulssi on negatiivinen, kuten alla olevan kuvan puskureissa. Kova puskuri pysäyttää kärryn nopeasti suurella voimalla ja pehmeä puskuri hitaasti pienellä voimalla, mutta pinta-alat ovat yhtä suuret.

<svg data-fig="pysaytys" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa, simulaation mallin arvoja: puskurin kärryyn kohdistaman voiman x-komponentti F_x newtoneina ajan funktiona, kun 1,0 kilogramman kärry pysähtyy nopeudesta 2,0 metriä sekunnissa. Kärry liikkuu positiiviseen suuntaan ja voima osoittaa negatiiviseen suuntaan, joten käyrät ovat vaaka-akselin alapuolella. Kova puskuri: voima on suurimmillaan miinus 80 newtonia ja törmäys kestää 0,039 sekuntia, kapea ja syvä käyrä. Pehmeä puskuri: voima on suurimmillaan vain miinus 20 newtonia, mutta törmäys kestää 0,157 sekuntia, matala ja leveä käyrä. Käyrien ja vaaka-akselin väliset alueet on varjostettu, ja ne ovat yhtä suuret: kummankin impulssi on miinus 2,0 newtonsekuntia." style="max-width:100%;font-size:24px">
  <line x1="188.5" y1="300" x2="188.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="300" x2="285" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="381.5" y1="300" x2="381.5" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="478" y1="300" x2="478" y2="72" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="254.5" x2="478" y2="254.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="209" x2="478" y2="209" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="163" x2="478" y2="163" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="117.5" x2="478" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="300" x2="92" y2="72" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="91" y1="72" x2="492" y2="72" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,72 L491,78 L491,66 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="73" x2="92" y2="58" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,46 L98,59 L86,59 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="188.5" y1="72" x2="188.5" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159.5" y="35.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}05$</div></foreignObject>
  <line x1="285" y1="72" x2="285" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="35.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}1$</div></foreignObject>
  <line x1="381.5" y1="72" x2="381.5" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352.5" y="35.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}15$</div></foreignObject>
  <line x1="478" y1="72" x2="478" y2="79" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="455.5" y="35.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}2$</div></foreignObject>
  <line x1="85" y1="300" x2="92" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="22" y="285.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-100$</div></foreignObject>
  <line x1="85" y1="254.5" x2="92" y2="254.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="240" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-80$</div></foreignObject>
  <line x1="85" y1="209" x2="92" y2="209" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="194.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-60$</div></foreignObject>
  <line x1="85" y1="163" x2="92" y2="163" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="148.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-40$</div></foreignObject>
  <line x1="85" y1="117.5" x2="92" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="103" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="85" y1="72" x2="92" y2="72" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="57.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="510" y="57.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="82" y="15.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x\ (\text{N})$</div></foreignObject>
  <polygon points="92,72 92,72 93.5,81.5 94.5,91 96,100.5 97,110 98.5,119 99.5,128.5 101,137.5 102,146 103.5,155 104.5,163 106,171.5 107,179 108.5,187 109.5,194 111,201 112,207.5 113.5,214 114.5,219.5 116,225 117.5,230 118.5,234.5 120,238.5 121,242.5 122.5,245.5 123.5,248 125,250.5 126,252 127.5,253.5 128.5,254 130,254.5 131,254 132.5,253.5 133.5,252 135,250.5 136,248 137.5,245.5 138.5,242.5 140,238.5 141.5,234.5 142.5,230 144,225 145,219.5 146.5,214 147.5,207.5 149,201 150,194 151.5,187 152.5,179 154,171.5 155,163 156.5,155 157.5,146 159,137.5 160,128.5 161.5,119 162.5,110 164,100.5 165.5,91 166.5,81.5 168,72" fill="#f2a69c" fill-opacity="0.45"/>
  <polyline points="92,72 93.5,81.5 94.5,91 96,100.5 97,110 98.5,119 99.5,128.5 101,137.5 102,146 103.5,155 104.5,163 106,171.5 107,179 108.5,187 109.5,194 111,201 112,207.5 113.5,214 114.5,219.5 116,225 117.5,230 118.5,234.5 120,238.5 121,242.5 122.5,245.5 123.5,248 125,250.5 126,252 127.5,253.5 128.5,254 130,254.5 131,254 132.5,253.5 133.5,252 135,250.5 136,248 137.5,245.5 138.5,242.5 140,238.5 141.5,234.5 142.5,230 144,225 145,219.5 146.5,214 147.5,207.5 149,201 150,194 151.5,187 152.5,179 154,171.5 155,163 156.5,155 157.5,146 159,137.5 160,128.5 161.5,119 162.5,110 164,100.5 165.5,91 166.5,81.5 168,72" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="184.5" y="240" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kova}$</span></div></foreignObject>
  <polygon points="92,72 92,72 97,74.5 102,77 107,79 112,81.5 117.5,84 122.5,86 127.5,88.5 132.5,90.5 137.5,92.5 142.5,95 147.5,97 152.5,99 157.5,100.5 162.5,102.5 168,104 173,106 178,107.5 183,109 188,110 193,111.5 198,112.5 203,113.5 208,114.5 213.5,115.5 218.5,116 223.5,116.5 228.5,117 233.5,117.5 238.5,117.5 243.5,117.5 248.5,117.5 253.5,117.5 258.5,117 264,116.5 269,116 274,115.5 279,114.5 284,113.5 289,112.5 294,111.5 299,110 304,109 309.5,107.5 314.5,106 319.5,104 324.5,102.5 329.5,100.5 334.5,99 339.5,97 344.5,95 349.5,92.5 354.5,90.5 360,88.5 365,86 370,84 375,81.5 380,79 385,77 390,74.5 395,72" fill="#f2a69c" fill-opacity="0.45"/>
  <polyline points="92,72 97,74.5 102,77 107,79 112,81.5 117.5,84 122.5,86 127.5,88.5 132.5,90.5 137.5,92.5 142.5,95 147.5,97 152.5,99 157.5,100.5 162.5,102.5 168,104 173,106 178,107.5 183,109 188,110 193,111.5 198,112.5 203,113.5 208,114.5 213.5,115.5 218.5,116 223.5,116.5 228.5,117 233.5,117.5 238.5,117.5 243.5,117.5 248.5,117.5 253.5,117.5 258.5,117 264,116.5 269,116 274,115.5 279,114.5 284,113.5 289,112.5 294,111.5 299,110 304,109 309.5,107.5 314.5,106 319.5,104 324.5,102.5 329.5,100.5 334.5,99 339.5,97 344.5,95 349.5,92.5 354.5,90.5 360,88.5 365,86 370,84 375,81.5 380,79 385,77 390,74.5 395,72" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <foreignObject x="404.5" y="126" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{pehmeä}$</span></div></foreignObject>
  <foreignObject x="210" y="176" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{yhtä suuret pinta-alat}$</span></div></foreignObject>
</svg>

```pysahdy
Kärry pysähtyy kovaan ja pehmeään puskuriin. Miksi pehmeä puskuri kohdistaa kärryyn pienemmän voiman?
---
Kummassakin tapauksessa liikemäärän muutos ja impulssi ovat yhtä suuret. Pehmeä puskuri pysäyttää kärryn pidemmässä ajassa, joten voiman riittää olla pienempi.
```

### Kimpoaminen muuttaa liikemäärää enemmän kuin pysähtyminen
Jos kappale ei vain pysähdy vaan kimpoaa takaisin, sen liikemäärä muuttuu enemmän. Kun pallo osuu seinään ja kimpoaa suoraan takaisin yhtä suurella vauhdilla, sen liikemäärä muuttuu arvosta $mv$ arvoon $-mv$. Muutos on $-2mv$, ja sen suuruus on kaksi kertaa niin suuri kuin pysähtyessä. Seinän on siis annettava kimpoavalle pallolle kaksinkertainen impulssi. Liikemäärän muutosta laskettaessa etumerkit ovat välttämättömiä, sillä myös pelkkä liikkeen suunnan muuttuminen muuttaa liikemäärää.

```pysahdy
Pallo osuu seinään ja kimpoaa takaisin samalla vauhdilla. Miksi seinän impulssi on suurempi kuin jos pallo vain pysähtyisi?
---
Liikemäärä muuttuu arvosta $mv$ arvoon $-mv$, eli muutos on $-2mv$. Se on kaksi kertaa niin suuri kuin pysähtyessä, joten myös impulssi on kaksinkertainen.
```

### Vastaus alun kysymykseen
Hyppääjä osuu alustaan samalla nopeudella, oli alusta kova tai pehmeä, ja pysähtyy kummassakin tapauksessa. Hänen liikemääränsä muutos on siis sama, joten myös häneen kohdistuvan kokonaisvoiman impulssi on sama. Alustan voima on tätä kokonaisvoimaa painon verran suurempi, mutta sekin pienenee, kun pysähtymisaika pitenee. Paksu patja painuu kasaan kymmenien senttimetrien matkalta, joten pysähtyminen kestää monta kertaa kauemmin kuin kovalla maalla, jossa keho pysähtyy muutamassa senttimetrissä. Koska impulssi on voima kertaa aika, pidempi pysähtymisaika tarkoittaa pienempää keskimääräistä kokonaisvoimaa ja siksi myös pienempää alustan keskimääräistä voimaa. Pienempi voima rasittaa kehoa vähemmän, joten loukkaantumisen riski pienenee. Samasta syystä alastulossa koukistetaan polvia, nyrkkeilyhanskat ovat pehmustettuja ja pyöräilykypärän sisällä on kasaan painuvaa vaahtomuovia.

<figure class="unit-photo"><img src="pics/fy4/punching-bag.webp" alt="Nyrkkeilijä lyö hanskalla keltamustaa nyrkkeilysäkkiä salilla."><figcaption>Nyrkkeilijä lyö raskasta nyrkkeilysäkkiä.</figcaption></figure>

## Kaava: Impulssiperiaate

### Liikemäärä ja impulssi
Kappaleen liikemäärä on
```kaavat
liikemäärä :: \overline{p} = m\overline{v}
```
missä $m$ on kappaleen massa ($\text{kg}$) ja $\overline{v}$ sen nopeus ($\text{m/s}$). Liikemäärän yksikkö on $\text{kg}\cdot\text{m/s}$. Suoraviivaisessa liikkeessä vektorit korvataan etumerkillisillä luvuilla, $p = mv$, ja $v$ on negatiivinen, kun kappale liikkuu negatiiviseen suuntaan.

Kun kappaleeseen vaikuttaa vakiovoima $\overline{F}$ aikavälin $\Delta t$, voiman impulssi on
```kaavat
voiman impulssi :: \overline{I} = \overline{F}\,\Delta t
```
missä $\overline{F}$ on voima ($\text{N}$) ja $\Delta t$ sen vaikutusaika ($\text{s}$). Impulssilla on voiman suunta, ja sen yksikkö on $\text{N}\cdot\text{s}$. Koska $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$, on $1\,\text{N}\cdot\text{s} = 1\,\text{kg}\cdot\text{m/s}$: impulssilla ja liikemäärällä on sama yksikkö.

### Impulssiperiaate Newtonin toisesta laista
Kun kokonaisvoima $\Sigma\overline{F}$ on vakio, kappale kiihtyy tasaisesti. Luvussa *Kiihtyvyys ja tasaisesti kiihtyvä liike* opit, että silloin kiihtyvyys on nopeuden muutos jaettuna ajalla, $\overline{a} = \tfrac{\overline{v} - \overline{v}_0}{\Delta t}$. Kun tämä sijoitetaan Newtonin toiseen lakiin $\Sigma\overline{F} = m\overline{a}$ ja yhtälö kerrotaan puolittain ajalla $\Delta t$, saadaan
```latex
\Sigma\overline{F}\,\Delta t = m\overline{v} - m\overline{v}_0
```
Vasemmalla on kokonaisvoiman impulssi ja oikealla liikemäärän muutos. Tämä on **impulssiperiaate**:
```kaavat
impulssi-liikemääräperiaate :: \overline{I} = \Delta\overline{p}
```
missä $\Delta\overline{p} = \overline{p} - \overline{p}_0$ on liikemäärän muutos ($\text{kg}\cdot\text{m/s}$) ja $\overline{I}$ kappaleeseen vaikuttavan kokonaisvoiman impulssi ($\text{N}\cdot\text{s}$). Sanoin: kappaleen liikemäärä muuttuu yhtä paljon kuin kokonaisvoima antaa sille impulssia. Kun esimerkiksi $2{,}0\,\text{kg}$:n kärryä työnnetään liikkeen suuntaan $4{,}0\,\text{N}$:n kokonaisvoimalla $0{,}50\,\text{s}$, impulssi on $2{,}0\,\text{N}\cdot\text{s}$, ja kärryn nopeus kasvaa $1{,}0\,\text{m/s}$.

### Etumerkit yhdessä ulottuvuudessa
Ennen laskemista valitaan positiivinen suunta. Nopeudet, liikemäärät ja voimat, jotka osoittavat vastakkaiseen suuntaan, saavat miinusmerkin. Kun pallo kimpoaa seinästä suoraan takaisin samalla vauhdilla ja positiivinen suunta on kohti seinää, $p_0 = mv$ ja $p = -mv$, joten $\Delta p = -mv - mv = -2mv$. Muutos osoittaa poispäin seinästä, samaan suuntaan kuin seinän palloon kohdistama voima.

<svg data-fig="kimpoaminen" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, nuolet mittakaavassa. Vasemmalla pallo ennen törmäystä ja sen jälkeen: ennen törmäystä pallo liikkuu oikealle kohti seinää ja sen liikemäärä p0 osoittaa oikealle, jälkeen pallo liikkuu yhtä nopeasti vasemmalle ja sen liikemäärä p osoittaa vasemmalle. Oikealla liikemäärän muutos: p ja miinus p0 peräkkäin muodostavat nuolen Delta p, joka on kaksi kertaa niin pitkä kuin p0 ja osoittaa vasemmalle. Alimpana seinän voiman impulssi I, yhtä pitkä kuin Delta p ja samaan suuntaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-9-kimpoaminen.webp" x="3.7" y="1.2" width="594.1" height="337.9" preserveAspectRatio="none"/>
  <foreignObject x="40" y="35.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="137.5" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\overline{p}_0$</div></foreignObject>
  <foreignObject x="40" y="165.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="147.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="503.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="411" y="25.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$-\overline{p}_0$</div></foreignObject>
  <foreignObject x="457.5" y="115.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}$</div></foreignObject>
  <foreignObject x="463.5" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{I}$</div></foreignObject>
  <foreignObject x="438.5" y="277.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{I} = \Delta\overline{p}$</div></foreignObject>
</svg>

### Muuttuva voima
Törmäyksessä voima ei ole vakio: se kasvaa nollasta suurimpaan arvoonsa ja pienenee takaisin. Impulssiperiaate pätee silloinkin, kun impulssi lasketaan voiman $(t, F)$-kuvaajan ja aika-akselin väliin jäävänä etumerkillisenä pinta-alana. Muuttuvan voiman vaikutusta kuvataan usein keskimääräisellä voimalla, joka antaisi samassa ajassa saman impulssin:
```latex
F_\text{ka} = \frac{|\Delta p|}{\Delta t}
```
missä $F_\text{ka}$ on keskimääräinen voima ($\text{N}$), $|\Delta p|$ liikemäärän muutoksen suuruus ($\text{kg}\cdot\text{m/s}$) ja $\Delta t$ törmäyksen kesto ($\text{s}$). Kaava antaa keskimääräisen voiman suuruuden. Keskimääräisen voiman $x$-komponentti on etumerkillinen, $F_{\text{ka},x} = \tfrac{\Delta p_x}{\Delta t}$; esimerkiksi pysäyttävän puskurin voiman komponentti on negatiivinen, kun kärry liikkuu positiiviseen suuntaan. Kuvaajassa keskimääräinen voima on sen suorakulmion korkeus, jonka pinta-ala on sama kuin käyrän alle jäävä pinta-ala. Muuttuvan voiman suurin itseisarvo on aina keskimääräisen voiman suuruutta suurempi.

<svg data-fig="keskivoima" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei lukuarvoja: törmäyksen aikana voima F kasvaa nollasta suurimpaan arvoonsa ja pienenee takaisin nollaan aikavälin Delta t aikana. Käyrän alle jäävä pinta-ala on impulssi I. Katkoviivoin piirretty suorakulmio, jonka korkeus on keskimääräinen voima F_ka ja leveys Delta t, on pinta-alaltaan yhtä suuri kuin käyrän alle jäävä alue." style="max-width:100%;font-size:24px">
  <line x1="79" y1="262" x2="484" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,262 L483,268 L483,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="263" x2="80" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,26 L86,39 L74,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="50" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="94" y="17.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$F$</span></div></foreignObject>
  <polygon points="127,262 127,262 130.5,254.5 134,247 137.5,239.5 141,232 144.5,225 148,217.5 151.5,210 155,203 158.5,196 162,189 165.5,182 169,175.5 172.5,168.5 176,162.5 179.5,156 183,150 186.5,144 190,138 193.5,132.5 197,127 200.5,122 204,117 207.5,112 211,107.5 214.5,103.5 218,99 221.5,95.5 225,92 228.5,88.5 232,85.5 235.5,83 239,80.5 242.5,78.5 246,76.5 249.5,75 253,73.5 256.5,72.5 260,71.5 263.5,71 267,71 270.5,71 274,71.5 277.5,72.5 281,73.5 285,75 288.5,76.5 292,78.5 295.5,80.5 299,83 302.5,85.5 306,88.5 309.5,92 313,95.5 316.5,99 320,103.5 323.5,107.5 327,112 330.5,117 334,122 337.5,127 341,132.5 344.5,138 348,144 351.5,150 355,156 358.5,162.5 362,168.5 365.5,175.5 369,182 372.5,189 376,196 379.5,203 383,210 386.5,217.5 390,225 393.5,232 397,239.5 400.5,247 404,254.5 407.5,262 407.5,262" fill="#f2a69c" fill-opacity="0.45"/>
  <rect x="127" y="140.5" width="281" height="121.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-dasharray="7 5"/>
  <polyline points="127,262 130.5,254.5 134,247 137.5,239.5 141,232 144.5,225 148,217.5 151.5,210 155,203 158.5,196 162,189 165.5,182 169,175.5 172.5,168.5 176,162.5 179.5,156 183,150 186.5,144 190,138 193.5,132.5 197,127 200.5,122 204,117 207.5,112 211,107.5 214.5,103.5 218,99 221.5,95.5 225,92 228.5,88.5 232,85.5 235.5,83 239,80.5 242.5,78.5 246,76.5 249.5,75 253,73.5 256.5,72.5 260,71.5 263.5,71 267,71 270.5,71 274,71.5 277.5,72.5 281,73.5 285,75 288.5,76.5 292,78.5 295.5,80.5 299,83 302.5,85.5 306,88.5 309.5,92 313,95.5 316.5,99 320,103.5 323.5,107.5 327,112 330.5,117 334,122 337.5,127 341,132.5 344.5,138 348,144 351.5,150 355,156 358.5,162.5 362,168.5 365.5,175.5 369,182 372.5,189 376,196 379.5,203 383,210 386.5,217.5 390,225 393.5,232 397,239.5 400.5,247 404,254.5 407.5,262" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="417.5" y="126" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\text{ka}$</div></foreignObject>
  <foreignObject x="257" y="190" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I$</span></div></foreignObject>
  <line x1="127" y1="284" x2="127" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="407.5" y1="284" x2="407.5" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="127" y1="294" x2="237" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="297" y1="294" x2="407.5" y2="294" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
</svg>

## Esimerkki
Tennispallo, jonka massa on $58\,\text{g}$, lentää vaakasuoraan nopeudella $25\,\text{m/s}$ kohti mailaa. Maila lyö pallon suoraan takaisin, ja pallo lähtee mailasta vaakasuoraan nopeudella $35\,\text{m/s}$. Pallo on kosketuksissa mailaan $4{,}0\,\text{ms}$. Kuinka suuri on keskimääräinen voima, jolla maila työntää palloa?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 58\,\text{g}$, tulonopeus $25\,\text{m/s}$, lähtönopeus $35\,\text{m/s}$ vastakkaiseen suuntaan ja kosketusaika $\Delta t = 4{,}0\,\text{ms}$.

Kysytään mailan keskimääräistä voimaa $F_\text{ka}$.

<!-- vaihe -->

**Periaate.** Pallon liikemäärä muuttuu, koska maila työntää sitä. Liike on vaakasuoraa, ja kosketuksen aikana mailan voima on niin suuri, että pallon painon vaikutus jätetään huomiotta. Silloin mailan voima on kokonaisvoima, ja käytetään impulssiperiaatetta. Positiivinen suunta valitaan pallon lähtösuuntaan, joten tulonopeus on $v_0 = -25\,\text{m/s}$ ja lähtönopeus $v = +35\,\text{m/s}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Impulssiperiaatteesta $F_\text{ka}\,\Delta t = mv - mv_0$, joten
```latex
F_\text{ka} = \frac{m(v - v_0)}{\Delta t}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massa kilogrammoiksi ja aika sekunneiksi: $58\,\text{g} = 0{,}058\,\text{kg}$ ja $4{,}0\,\text{ms} = 0{,}0040\,\text{s}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin liikemäärän muutos ja jaetaan se sitten ajalla:
```latex
\begin{aligned}
&m(v - v_0) \\
&= 0{,}058\,\text{kg} \cdot (35 + 25)\,\tfrac{\text{m}}{\text{s}} \\
&= 3{,}48\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&F_\text{ka} = \frac{3{,}48\,\text{kg}\cdot\text{m/s}}{0{,}0040\,\text{s}} \\
&= 870\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Maila työntää palloa keskimäärin voimalla $8{,}7 \cdot 10^2\,\text{N}$, kahden merkitsevän numeron tarkkuudella kuten massa $58\,\text{g}$ ja aika $4{,}0\,\text{ms}$. Voima on positiivinen eli osoittaa pallon lähtösuuntaan.

<!-- vaihe -->

**Järkevyys.** Pallon paino on $0{,}058\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 0{,}57\,\text{N}$, noin $1500$ kertaa pienempi kuin mailan voima, joten painon jättäminen huomiotta oli perusteltua. Jos etumerkki unohtuisi ja nopeudet vähennettäisiin suoraan, $35\,\text{m/s} - 25\,\text{m/s}$, voimaksi tulisi vain $145\,\text{N}$, vaikka mailan täytyy ensin pysäyttää pallo ja sitten kiihdyttää se vastakkaiseen suuntaan.

## Yleinen virhekäsitys
Moni ajattelee, että pehmeä patja tai turvatyyny pienentää törmäyksen impulssia tai "imee liikemäärän". Liikemäärän muutos on kuitenkin sama, pysähtyipä kappale kovaan tai pehmeään alustaan, joten myös kokonaisvoiman impulssi on sama. Pehmeä alusta pidentää pysähtymisaikaa, ja siksi samaan impulssiin riittää pienempi keskimääräinen kokonaisvoima.

Toinen virhe on unohtaa etumerkit, kun kappale kimpoaa. Jos pallo osuu seinään nopeudella $10\,\text{m/s}$ ja kimpoaa takaisin nopeudella $10\,\text{m/s}$, sen nopeuden suuruus ei muutu, mutta liikemäärä muuttuu arvosta $mv$ arvoon $-mv$. Muutos on $-2mv$ eikä nolla: sen suuruus on $2mv$. Kolmas virhe on sekoittaa liikemäärä ja liike-energia: liikemäärä on vektori ja verrannollinen nopeuteen, liike-energia on skalaari ja verrannollinen nopeuden neliöön.

## Tiivistelmä
- Liikemäärä on massan ja nopeuden tulo, $\overline{p} = m\overline{v}$. Se on vektori, jolla on nopeuden suunta; yksikkö on $\text{kg}\cdot\text{m/s}$.
- Vakiovoiman impulssi on $\overline{I} = \overline{F}\,\Delta t$. Muuttuvan voiman impulssi on $(t, F)$-kuvaajan ja aika-akselin väliin jäävä etumerkillinen pinta-ala; yksikkö on $\text{N}\cdot\text{s} = \text{kg}\cdot\text{m/s}$.
- Impulssiperiaate: kokonaisvoiman impulssi on yhtä suuri kuin liikemäärän muutos, $\overline{I} = \Delta\overline{p}$.
- Sama liikemäärän muutos saadaan suurella voimalla lyhyessä ajassa tai pienellä voimalla pitkässä ajassa. Pehmeä alusta, koukistetut polvet ja kypärän vaahtomuovi pidentävät pysähtymisaikaa ja pienentävät voimaa.
- Yhdessä ulottuvuudessa valitaan positiivinen suunta ja käytetään etumerkkejä. Suoraan takaisin samalla vauhdilla kimpoavan kappaleen liikemäärän muutoksen suuruus on $2mv$, kaksi kertaa niin suuri kuin pysähtyvän.
