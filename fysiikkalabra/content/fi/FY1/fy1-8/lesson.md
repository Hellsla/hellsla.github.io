# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: lattialla rata, jolla leluauto kulkee mittanauhan vieressä. Radan molemmin puolin seisoo ryhmä, ja kummallakin ryhmällä on oma sekuntikello; kellojen viisarit ovat pysähtyneet eri kohtiin." class="fig-hero" style="max-width:100%;font-size:24px">
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <path d="M0,330 H1200 V600 H0 Z" fill="#f1dfb5" stroke-linejoin="round"/>
  <line x1="-200" y1="600" x2="80" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="60" y1="600" x2="280" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320" y1="600" x2="480" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="580" y1="600" x2="680" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="840" y1="600" x2="880" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1100" y1="600" x2="1080" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1360" y1="600" x2="1280" y2="330" stroke="#d9b26a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="330" x2="1200" y2="330" stroke="#e9c98a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M120,470 L1080,470 L1040,420 L160,420 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="140" y="476" width="920" height="28" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <line x1="150" y1="476" x2="150" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="169.5" y1="476" x2="169.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189" y1="476" x2="189" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="209" y1="476" x2="209" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228.5" y1="476" x2="228.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="476" x2="248" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="267.5" y1="476" x2="267.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="287" y1="476" x2="287" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="307" y1="476" x2="307" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="476" x2="326.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346" y1="476" x2="346" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365.5" y1="476" x2="365.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="385" y1="476" x2="385" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="476" x2="405" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424.5" y1="476" x2="424.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="444" y1="476" x2="444" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="463.5" y1="476" x2="463.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="483" y1="476" x2="483" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="503" y1="476" x2="503" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="522.5" y1="476" x2="522.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="476" x2="542" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="561.5" y1="476" x2="561.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="581" y1="476" x2="581" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="601" y1="476" x2="601" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="620.5" y1="476" x2="620.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="476" x2="640" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="659.5" y1="476" x2="659.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="679" y1="476" x2="679" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="699" y1="476" x2="699" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="718.5" y1="476" x2="718.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="738" y1="476" x2="738" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="757.5" y1="476" x2="757.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="777" y1="476" x2="777" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="797" y1="476" x2="797" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="816.5" y1="476" x2="816.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="836" y1="476" x2="836" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="855.5" y1="476" x2="855.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="875" y1="476" x2="875" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="895" y1="476" x2="895" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="914.5" y1="476" x2="914.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="934" y1="476" x2="934" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="953.5" y1="476" x2="953.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="973" y1="476" x2="973" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="993" y1="476" x2="993" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1012.5" y1="476" x2="1012.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1032" y1="476" x2="1032" y2="492" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1051.5" y1="476" x2="1051.5" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M530,452 V428 Q536,420 560,418 L578,390 H630 L652,418 Q672,420 674,434 V452 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M586,398 H626 L640,416 H574 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="560" cy="454" r="15" fill="#1f2933"/>
  <circle cx="560" cy="454" r="6" fill="#c4ccd4"/>
  <circle cx="644" cy="454" r="15" fill="#1f2933"/>
  <circle cx="644" cy="454" r="6" fill="#c4ccd4"/>
  <line x1="480" y1="436" x2="516" y2="436" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="470" y1="416" x2="510" y2="416" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <path d="M74,400 L77.5,307 H102.5 L106,400 H93.5 L90,338 L86.5,400 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M69,313 Q66.5,245 90,241.5 Q113.5,245 111,313 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M71.5,253.5 L65,313" fill="none" stroke="#1971c2" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="65" cy="318" r="6.82" fill="#f1dfb5"/>
  <path d="M108.5,253.5 L115,313" fill="none" stroke="#1971c2" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="115" cy="318" r="6.82" fill="#f1dfb5"/>
  <rect x="84.5" y="229" width="11" height="15" fill="#f1dfb5"/>
  <circle cx="90" cy="216.5" r="18.6" fill="#f1dfb5"/>
  <path d="M71,216.5 Q71.5,194 90,195.5 Q110,195.5 109,214 Q93.5,206.5 71,216.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M184.5,404 L188,314 H212 L215.5,404 H203.5 L200,344 L196.5,404 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M179.5,320 Q177,254 200,250.5 Q223,254 220.5,320 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M182,262.5 L176,320" fill="none" stroke="#2b8a3e" stroke-width="13.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="176" cy="325" r="6.6" fill="#f1dfb5"/>
  <path d="M218,262.5 L224,320" fill="none" stroke="#2b8a3e" stroke-width="13.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="224" cy="325" r="6.6" fill="#f1dfb5"/>
  <rect x="194.5" y="238.5" width="11" height="14.5" fill="#f1dfb5"/>
  <circle cx="200" cy="226.5" r="18" fill="#f1dfb5"/>
  <path d="M181.5,226.5 Q182,205 200,206 Q219,206 218.5,224 Q203.5,217 181.5,226.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M984,400 L987.5,307 H1012.5 L1016,400 H1003.5 L1000,338 L996.5,400 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M979,313 Q976.5,245 1000,241.5 Q1023.5,245 1021,313 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M981.5,253.5 L975,313" fill="none" stroke="#e8590c" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="975" cy="318" r="6.82" fill="#f1dfb5"/>
  <path d="M1018.5,253.5 L1025,313" fill="none" stroke="#e8590c" stroke-width="13.64" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1025" cy="318" r="6.82" fill="#f1dfb5"/>
  <rect x="994.5" y="229" width="11" height="15" fill="#f1dfb5"/>
  <circle cx="1000" cy="216.5" r="18.6" fill="#f1dfb5"/>
  <path d="M981,216.5 Q981.5,194 1000,195.5 Q1020,195.5 1019,214 Q1003.5,206.5 981,216.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M1094.5,404 L1098,314 H1122 L1125.5,404 H1113.5 L1110,344 L1106.5,404 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M1089.5,320 Q1087,254 1110,250.5 Q1133,254 1130.5,320 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M1092,262.5 L1086,320" fill="none" stroke="#1971c2" stroke-width="13.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1086" cy="325" r="6.6" fill="#f1dfb5"/>
  <path d="M1128,262.5 L1134,320" fill="none" stroke="#1971c2" stroke-width="13.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="1134" cy="325" r="6.6" fill="#f1dfb5"/>
  <rect x="1104.5" y="238.5" width="11" height="14.5" fill="#f1dfb5"/>
  <circle cx="1110" cy="226.5" r="18" fill="#f1dfb5"/>
  <path d="M1091.5,226.5 Q1092,205 1110,206 Q1129,206 1128.5,224 Q1113.5,217 1091.5,226.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="241" y="66" width="18" height="13.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="246" y="78.5" width="8" height="8" fill="#6c757d"/>
  <circle cx="250" cy="140" r="56" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="250" cy="140" r="45.92" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="250" y1="102" x2="250" y2="96.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="269" y1="107" x2="272" y2="102" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="121" x2="288" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="288" y1="140" x2="293.5" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="159" x2="288" y2="162" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="269" y1="173" x2="272" y2="178" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250" y1="178" x2="250" y2="183.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231" y1="173" x2="228" y2="178" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="217" y1="159" x2="212" y2="162" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="212" y1="140" x2="206.5" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="217" y1="121" x2="212" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231" y1="107" x2="228" y2="102" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250" y1="140" x2="286.5" y2="144.5" stroke="#c92a2a" stroke-width="3.92" stroke-linecap="round"/>
  <circle cx="250" cy="140" r="4.48" fill="#1f2933"/>
  <rect x="941" y="66" width="18" height="13.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="946" y="78.5" width="8" height="8" fill="#6c757d"/>
  <circle cx="950" cy="140" r="56" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="950" cy="140" r="45.92" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="950" y1="102" x2="950" y2="96.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="969" y1="107" x2="972" y2="102" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="983" y1="121" x2="988" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="988" y1="140" x2="993.5" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="983" y1="159" x2="988" y2="162" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="969" y1="173" x2="972" y2="178" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="950" y1="178" x2="950" y2="183.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="931" y1="173" x2="928" y2="178" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="917" y1="159" x2="912" y2="162" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="912" y1="140" x2="906.5" y2="140" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="917" y1="121" x2="912" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="931" y1="107" x2="928" y2="102" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="950" y1="140" x2="982.5" y2="158" stroke="#c92a2a" stroke-width="3.92" stroke-linecap="round"/>
  <circle cx="950" cy="140" r="4.48" fill="#1f2933"/>
</svg>

## Ydinajatus
Fysiikka on kokeellinen tiede: väite pätee vasta, kun sitä on testattu mittauksilla, jotka kuka tahansa voi toistaa. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Se alkaa kysymyksestä ja päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi, vaan sellainen, jossa mittaus voisi näyttää oletuksen vääräksi.

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata: "Miten leluauton kulkema matka riippuu ajasta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste kysymykseen. Esimerkiksi: "Jos auto liikkuu vakionopeudella, kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa, joka voi osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei kumoa sitä.

### Muuttujat
**Muuttuja** on suure, jonka arvo voi vaihdella tutkimuksessa. Kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään kaikki muut samoina:
- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Jos kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot, tuloksen muutoksen syytä ei voi päätellä. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

<svg data-fig="setup" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kokeen asetelmasta: leluauto ajaa pöydän tasaisella radalla lähtöviivalta maaliviivalle. Radan vieressä on matka-asteikko metreinä, ja lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Käsikello mittaa aikaa t, joka on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy18-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <foreignObject x="24" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muutettava: } s$</div></foreignObject>
  <foreignObject x="24" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mitattava: } t$</div></foreignObject>
  <foreignObject x="24" y="81.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vakiona: auto, alusta, paristot}$</div></foreignObject>
  <rect x="514" y="20" width="12" height="12" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="66" r="30" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="520" y1="44" x2="520" y2="39" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="47" x2="533.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="55" x2="543.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="66" x2="547" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="77" x2="543.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="85" x2="533.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="88" x2="520" y2="93" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="85" x2="506.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="77" x2="496.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="498" y1="66" x2="493" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="55" x2="496.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="47" x2="506.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="66" x2="536" y2="52" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="520" cy="66" r="3.5" fill="#1f2933"/>
  <foreignObject x="510" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <rect x="40" y="200" width="520" height="16" fill="url(#fy18-wood)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="72" y1="216" x2="72" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="62" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="147" y1="216" x2="147" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="124.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="222" y1="216" x2="222" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="212" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="297" y1="216" x2="297" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="274.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="372" y1="216" x2="372" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="362" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="447" y1="216" x2="447" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="424.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <foreignObject x="475" y="227.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <line x1="72" y1="140" x2="72" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="37" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
  <line x1="372" y1="140" x2="372" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="337" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maali}$</div></foreignObject>
  <rect x="92" y="166" width="68" height="22" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="108" y="148" width="36" height="18" rx="5" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="110" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="144" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="176" y1="160" x2="237" y2="160" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M250,160 L236,166.5 L236,153.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="264" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <line x1="72" y1="268" x2="372" y2="268" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="72" y1="258" x2="72" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="258" x2="372" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="168" y="285.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$s = 2{,}00\,\text{m}$</div></foreignObject>
</svg>

### Suunnittelu ennen mittausta
Suunnitelma vastaa ennen mittausta kysymyksiin: mitä mitataan ja millä välineellä, mitkä arvot muutettavalle muuttujalle valitaan ja kuinka monta, montako toistoa kustakin arvosta tehdään ja mitä pidetään vakiona. Kokeile ensin esikokeella. Se kertoo, onko mittaus ylipäätään mahdollinen, ja antaa karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse arvoja tasavälein ja useita, koska yksi tai kaksi pistettä ei näytä, onko riippuvuus suora.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana, ei muistista jälkikäteen. Siihen kirjataan tutkimuskysymys, päivämäärä, välineet ja niiden tarkkuus, vakioidut asiat, mittaukset taulukkona yksiköineen sekä havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta: merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

| $s\ (\text{m})$ | $t_1\ (\text{s})$ | $t_2\ (\text{s})$ | $t_3\ (\text{s})$ | huomio |
|---|---|---|---|---|
| 0,50 | 1,3 | 1,1 | 1,4 | vaikea ajoittaa |
| 1,00 | 2,5 | 2,3 | 2,6 | |
| 1,50 | 3,7 | 3,5 | 3,6 | |

### Raportti
**Raportti** kertoo tutkimuksen niin, että toinen voi toistaa sen ja arvioida johtopäätöksen. Sen osat ovat:
1. tutkimuskysymys ja hypoteesi
2. menetelmä: välineet, muuttujat ja toteutus
3. tulokset: taulukko, kuvaaja ja suureen arvo epävarmuuksineen
4. pohdinta: virhelähteet ja se, mitä seuraavalla kerralla tehtäisiin toisin
5. johtopäätös: vastaus tutkimuskysymykseen ja se, tukevatko tulokset hypoteesia.

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset osuvat epävarmuuden sisällä ennusteeseen, hypoteesi on saanut tukea, mutta sitä ei ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta, ja se on lähes sama lyhyessä ja pitkässä mittauksessa. Mittauksen laatua kuvaa siksi **suhteellinen epävarmuus**, epävarmuus suhteessa mitattuun arvoon. Jotta se pysyy enintään arvossa $\varepsilon_\text{max}$, mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Epävarmuuden $\Delta t = 0{,}2\,\text{s}$ ja rajan $5\,\%$ yhdistelmällä aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja suhteellisesta epävarmuudesta ajan funktiona, kun ajan epävarmuus on 0,2 s: kun aika on 1 s, epävarmuus on 20 %, kun aika on 4 s, se on 5,0 %, ja kun aika on 10 s, se on 2,0 %. Vihreä alue kuvaa mittauksia, joiden epävarmuus on enintään 5,0 %: ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="176" y1="286" x2="176" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="286" x2="256" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="286" x2="336" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="286" x2="416" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="286" x2="496" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189.5" x2="496" y2="189.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="141" x2="496" y2="141" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="92.5" x2="496" y2="92.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="510" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,286 L509,292 L509,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,28 L102,41 L90,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="176" y1="286" x2="176" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256" y1="286" x2="256" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="336" y1="286" x2="336" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="326" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="416" y1="286" x2="416" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="406" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="496" y1="286" x2="496" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="237.5" x2="96" y2="237.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="223" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="189.5" x2="96" y2="189.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="175" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="141" x2="96" y2="141" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="126.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="92.5" x2="96" y2="92.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="271.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="-2.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\varepsilon\ (\%)$</div></foreignObject>
  <polygon points="256,286 496,286 496,237.5 256,237.5" fill="#b2f2bb" fill-opacity="0.7"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <polyline points="136,92.5 139,106 142,118 145,128 148,137.5 151,145.5 154,152.5 157,159 160,165 163,170.5 166,175.5 169,180 172,184 175,188 178,191.5 181,195 184,198 187,201 190,203.5 193,206.5 196,208.5 199,211 202,213 205,215 208,217 211,219 214,220.5 217,222 220,223.5 223,225 226,226.5 229,228 232,229 235,230.5 238,231.5 241,232.5 244,233.5 247,235 250,236 253,236.5 256,237.5 259,238.5 262,239.5 265,240 268,241 271,242 274,242.5 277,243.5 280,244 283,244.5 286,245.5 289,246 292,246.5 295,247 298,247.5 301,248.5 304,249 307,249.5 310,250 313,250.5 316,251 319,251.5 322,252 325,252 328,252.5 331,253 334,253.5 337,254 340,254.5 343,254.5 346,255 349,255.5 352,256 355,256 358,256.5 361,257 364,257 367,257.5 370,258 373,258 376,258.5 379,258.5 382,259 385,259 388,259.5 391,260 394,260 397,260.5 400,260.5 403,261 406,261 409,261.5 412,261.5 415,262 418,262 421,262 424,262.5 427,262.5 430,263 433,263 436,263.5 439,263.5 442,263.5 445,264 448,264 451,264 454,264.5 457,264.5 460,265 463,265 466,265 469,265.5 472,265.5 475,265.5 478,266 481,266 484,266 487,266 490,266.5 493,266.5 496,266.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="256" y1="237.5" x2="256" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="237.5" x2="256" y2="237.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="256" cy="237.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="304" y="188.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\varepsilon \le 5\,\%$</div></foreignObject>
  <foreignObject x="184" y="73.5" width="180" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\varepsilon = \dfrac{0{,}2\,\text{s}}{t}$</div></foreignObject>
</svg>

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Kun $t$ on vaaka-akselilla ja $s$ pystyakselilla, suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Sitä lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan, ja tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla, ja ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Mittauksen suhteellinen epävarmuus halutaan enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

<!-- vaihe -->

**Tunnetut ja kysytty.** Nopeus $v = 0{,}42\,\text{m/s}$, ajan epävarmuus $\Delta t = 0{,}2\,\text{s}$ ja suurin sallittu suhteellinen epävarmuus $\varepsilon_\text{max} = 5{,}0\,\% = 0{,}050$. Kysytään lyhintä matkaa $s_\text{min}$.

<!-- vaihe -->

**Periaate.** Suhteellinen epävarmuus pienenee, kun mitattava aika kasvaa, koska $\Delta t$ pysyy samana. Lasketaan ensin lyhin sallittu aika epävarmuuden rajasta. Auto liikkuu vakionopeudella, joten tasaisen liikkeen malli $s = vt$ antaa ajasta matkan.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&t_\text{min} = \frac{\Delta t}{\varepsilon_\text{max}} \\
&s_\text{min} = v\, t_\text{min} = \frac{v\,\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: nopeus on yksikössä $\text{m/s}$ ja aika sekunteina, joten matka tulee metreinä. Prosentti on muunnettu desimaaliluvuksi: $5{,}0\,\% = 0{,}050$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
t_\text{min} &= \frac{\Delta t}{\varepsilon_\text{max}} \\
&= \frac{0{,}2\,\text{s}}{0{,}050} = 4\,\text{s} \\
s_\text{min} &= v\, t_\text{min} \\
&= 0{,}42\,\tfrac{\text{m}}{\text{s}} \cdot 4\,\text{s} \\
&= 1{,}68\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tulos pyöristetään kahteen merkitsevään numeroon kuten nopeus $0{,}42\,\text{m/s}$; epävarmuus $0{,}2\,\text{s}$ on annettu yhdellä numerolla, ja se antaa vain arvion lyhimmästä ajasta.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$, jolloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli tasan rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$, ja siksi lyhyt matka oli huono valinta.

## Yleinen virhekäsitys
Moni ajattelee, että tutkimus on epäonnistunut, jos mittaus ei tue hypoteesia. Näin ei ole: jos mittaus kumoaa hypoteesin, tutkija tietää jotakin, mitä hän ei aiemmin tiennyt. Epäonnistunut tutkimus on sellainen, josta ei voi päätellä mitään, koska muuttujia ei ole hallittu tai mittaukset ovat liian epävarmoja.

Toinen yleinen virhe on pitää yhtä mittausta riittävänä. Yksi lukema ei kerro, kuinka paljon tulos vaihtelee, joten satunnaisvirheen aiheuttamaa hajontaa ei voi arvioida. Kolmas virhe on valita tulokseen sopivat mittaukset ja jättää muut pois: kaikki mittaukset kirjataan, ja poikkeava mittaus selitetään tai merkitään.

## Tiivistelmä
- Tutkimus alkaa mitattavissa olevasta kysymyksestä ja testattavasta hypoteesista, joka voi osoittautua vääräksi.
- Reilussa kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään muut vakioina.
- Mittaus suunnitellaan etukäteen: mittausalue, pisteiden määrä, toistot ja vakioidut asiat. Esikoe tarkistaa suunnitelman.
- Pöytäkirjaan kirjataan lukemat, yksiköt, välineet ja havainnot kokeen aikana. Mitään mittausta ei poisteta hiljaa.
- Suhteellinen epävarmuus $\varepsilon = \Delta t : t$ pienenee, kun mitattava aika kasvaa; siksi aikaa on oltava vähintään $\Delta t : \varepsilon_\text{max}$.
- Raportti kertoo kysymyksen, menetelmän, tulokset, pohdinnan ja johtopäätöksen niin, että toinen voi toistaa tutkimuksen.
