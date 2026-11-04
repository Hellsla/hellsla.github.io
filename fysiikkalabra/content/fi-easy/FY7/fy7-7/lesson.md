# Generaattori ja vaihtovirta

> **Miksi** tuulivoimalan pyörivä roottori antaa sähköverkkoon jännitteen, joka vaihtaa suuntaansa sata kertaa sekunnissa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: tuulivoimapuisto suomalaisella pellolla meren rannalla. Keskellä on suuri tuulivoimala, jonka siivet pyörivät. Sen takana on pienempiä voimaloita. Oikealla voimalinja kulkee pylväiden varassa punaisten talojen luo. Taivaalla on pilviä. Tuuli taivuttaa koivujen latvoja." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy77h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy77h-sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy77h-field" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="470" fill="url(#fy77h-sky)"/>
  <path d="M122,134 Q119.5,93 167.5,98 Q187,55 235,69 Q278,45 302,91 Q345,95.5 340.5,134 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M879,98 Q877,67.5 913,71 Q927.5,38.5 963.5,49.5 Q996,31.5 1014,65.5 Q1046.5,69 1043,98 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M697,184 Q695.5,160 723.5,163 Q735,138 763,146 Q788,132 802,159 Q827,161.5 824.5,184 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="0" y="380" width="1200" height="90" fill="url(#fy77h-sea)"/>
  <path d="M640,412 L654.5,388 L669.5,412 L685.5,385 L701.5,412 L716.5,387.5 L731.5,412 L752.5,374 L773.5,412 L792,380.5 L810,412 L831.5,374 L852.5,412 L871.5,379 L890.5,412 L903.5,391.5 L916.5,412 L937,375.5 L957.5,412 L970,392.5 L982.5,412 L997.5,387.5 L1012,412 L1031.5,377.5 L1051,412 L1069.5,380 L1088,412 L1101,391 L1114.5,412 L1127,392.5 L1139.5,412 L1153.5,389.5 L1167.5,412 L1184.5,383 L1201.5,412 V472 H640 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <path d="M0,440 Q100,427 200,437 Q300,426 400,437.5 Q500,417 600,439 Q700,418 800,439 Q900,400 1000,442.5 Q1100,412 1200,440 Q1300,411 1400,440.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,467 Q100,443.5 200,465.5 Q300,427.5 400,466.5 Q500,430.5 600,466 Q700,449 800,469.5 Q900,432.5 1000,467.5 Q1100,435 1200,469.5 Q1300,426.5 1400,468 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <rect x="0" y="500" width="1200" height="100" fill="url(#fy77h-field)"/>
  <line x1="0" y1="512" x2="1200" y2="508" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="522" x2="1200" y2="519" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="532" x2="1200" y2="530" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="542" x2="1200" y2="541" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="552" x2="1200" y2="552" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="562" x2="1200" y2="563" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="574" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="582" x2="1200" y2="585" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="592" x2="1200" y2="596" stroke="#e9c98a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M144.5,420 L147.5,290 H152.5 L155.5,420 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M154,291 Q166.5,269.5 174,213 L146,289 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M147,292.5 Q159.5,314.5 205,349 L153,287.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M149,286 Q124.5,286 71.5,308 L151,294 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="150" cy="290" r="5.6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M294.5,412 L297.5,252 H302.5 L305.5,412 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M302,255.5 Q331,247 388.5,207 L298,248.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M296,252 Q289,281 295,351 L304,252 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M302,248.5 Q280.5,227.5 217,198 L298,255.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="300" cy="252" r="5.6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M834.5,440 L837.5,270 H842.5 L845.5,440 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M843,272.5 Q867.5,252 908,189.5 L837,267.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M836,271.5 Q841.5,303 876,369 L844,268.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M840.5,266 Q810.5,255 736,251.5 L839.5,274 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="840" cy="270" r="5.6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M974.5,432 L977.5,292 H982.5 L985.5,432 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,296 Q1005.5,302.5 1067,294.5 L980,288 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M976.5,290 Q958,309 934.5,366 L983.5,294 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M983.5,290 Q976,264.5 939,215.5 L976.5,294 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="980" cy="292" r="5.6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M589,520 L595,190 H605 L611,520 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M608,191.5 Q631,133.5 640.5,-10.5 L592,188.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M594.5,196 Q633.5,245 753.5,325.5 L605.5,184 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M597.5,182.5 Q535.5,191.5 406,255 L602.5,197.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="600" cy="190" r="11.2" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M789.5,540 L814.5,390 H825.5 L850.5,540" fill="none" stroke="#6c757d" stroke-width="2.7" stroke-linejoin="round"/>
  <line x1="789.5" y1="540" x2="845.5" y2="510" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="850.5" y1="540" x2="794.5" y2="510" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="794.5" y1="510" x2="840.5" y2="480" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="845.5" y1="510" x2="799.5" y2="480" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="799.5" y1="480" x2="835.5" y2="450" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="840.5" y1="480" x2="804.5" y2="450" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="804.5" y1="450" x2="830.5" y2="420" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="835.5" y1="450" x2="809.5" y2="420" stroke="#6c757d" stroke-width="1.35" stroke-linecap="butt"/>
  <line x1="773" y1="420" x2="867" y2="420" stroke="#6c757d" stroke-width="2.7" stroke-linecap="butt"/>
  <line x1="773" y1="420" x2="773" y2="432.5" stroke="#1f2933" stroke-width="1.8" stroke-linecap="butt"/>
  <line x1="867" y1="420" x2="867" y2="432.5" stroke="#1f2933" stroke-width="1.8" stroke-linecap="butt"/>
  <line x1="789.5" y1="390" x2="850.5" y2="390" stroke="#6c757d" stroke-width="2.7" stroke-linecap="butt"/>
  <line x1="789.5" y1="390" x2="789.5" y2="402.5" stroke="#1f2933" stroke-width="1.8" stroke-linecap="butt"/>
  <line x1="850.5" y1="390" x2="850.5" y2="402.5" stroke="#1f2933" stroke-width="1.8" stroke-linecap="butt"/>
  <path d="M977.5,545 L1004.5,385 H1015.5 L1042.5,545" fill="none" stroke="#6c757d" stroke-width="2.85" stroke-linejoin="round"/>
  <line x1="977.5" y1="545" x2="1037" y2="513" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="1042.5" y1="545" x2="983" y2="513" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="983" y1="513" x2="1031.5" y2="481" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="1037" y1="513" x2="988.5" y2="481" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="988.5" y1="481" x2="1026.5" y2="449" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="1031.5" y1="481" x2="993.5" y2="449" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="993.5" y1="449" x2="1021" y2="417" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="1026.5" y1="449" x2="999" y2="417" stroke="#6c757d" stroke-width="1.425" stroke-linecap="butt"/>
  <line x1="960.5" y1="417" x2="1059.5" y2="417" stroke="#6c757d" stroke-width="2.85" stroke-linecap="butt"/>
  <line x1="960.5" y1="417" x2="960.5" y2="430.5" stroke="#1f2933" stroke-width="1.9" stroke-linecap="butt"/>
  <line x1="1059.5" y1="417" x2="1059.5" y2="430.5" stroke="#1f2933" stroke-width="1.9" stroke-linecap="butt"/>
  <line x1="977.5" y1="385" x2="1042.5" y2="385" stroke="#6c757d" stroke-width="2.85" stroke-linecap="butt"/>
  <line x1="977.5" y1="385" x2="977.5" y2="398.5" stroke="#1f2933" stroke-width="1.9" stroke-linecap="butt"/>
  <line x1="1042.5" y1="385" x2="1042.5" y2="398.5" stroke="#1f2933" stroke-width="1.9" stroke-linecap="butt"/>
  <path d="M773,432.5 Q867,455.5 960.5,430.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M867,432.5 Q963,455.5 1059.5,430.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M789.5,402.5 Q883.5,424.5 977.5,398.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M850.5,402.5 Q946.5,424.5 1042.5,398.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M960.5,430.5 Q1080.5,456.5 1200,450.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1059.5,430.5 Q1129.5,456.5 1200,450.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="1060" y="505" width="110" height="70" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="1074" y1="508" x2="1074" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1088" y1="508" x2="1088" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1102" y1="508" x2="1102" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1116" y1="508" x2="1116" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1130" y1="508" x2="1130" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="1144" y1="508" x2="1144" y2="572" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="1060" y="505" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1160" y="505" width="10" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M1040,505 L1115,466.5 L1190,505 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="1090" y="524.5" width="40" height="28" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="1090" y="524.5" width="40" height="28" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="1110" y1="524.5" x2="1110" y2="552.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="60" y="500" width="120" height="72" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="74" y1="503" x2="74" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="88" y1="503" x2="88" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="102" y1="503" x2="102" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="116" y1="503" x2="116" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="130" y1="503" x2="130" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="144" y1="503" x2="144" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="158" y1="503" x2="158" y2="569" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="60" y="500" width="10" height="72" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="170" y="500" width="10" height="72" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M40,500 L120,460.5 L200,500 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="90" y="520" width="40" height="29" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="90" y="520" width="40" height="29" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="110" y1="520" x2="110" y2="549" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="226.5" y="455" width="7" height="120" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="226.5" y="560.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="230" y="546" width="3.5" height="2" fill="#1f2933"/>
  <rect x="226.5" y="532" width="3.5" height="2" fill="#1f2933"/>
  <rect x="230" y="517.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="226.5" y="503" width="3.5" height="2" fill="#1f2933"/>
  <rect x="230" y="488.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="226.5" y="474" width="3.5" height="2" fill="#1f2933"/>
  <line x1="230" y1="500.5" x2="208.5" y2="486" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="230" y1="485" x2="251.5" y2="470.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="230" y1="473" x2="208.5" y2="458.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="230" cy="461" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="212" cy="479" r="19" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="248" cy="476.5" r="20.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="230" cy="488.5" r="18" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="466.5" y="455" width="7" height="120" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="466.5" y="560.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="470" y="546" width="3.5" height="2" fill="#1f2933"/>
  <rect x="466.5" y="532" width="3.5" height="2" fill="#1f2933"/>
  <rect x="470" y="517.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="466.5" y="503" width="3.5" height="2" fill="#1f2933"/>
  <rect x="470" y="488.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="466.5" y="474" width="3.5" height="2" fill="#1f2933"/>
  <line x1="470" y1="500.5" x2="448.5" y2="486" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="470" y1="485" x2="491.5" y2="470.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="470" y1="473" x2="448.5" y2="458.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="470" cy="461" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="452" cy="479" r="19" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="488" cy="476.5" r="20.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="470" cy="488.5" r="18" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="716.5" y="455" width="7" height="120" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="716.5" y="560.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="720" y="546" width="3.5" height="2" fill="#1f2933"/>
  <rect x="716.5" y="532" width="3.5" height="2" fill="#1f2933"/>
  <rect x="720" y="517.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="716.5" y="503" width="3.5" height="2" fill="#1f2933"/>
  <rect x="720" y="488.5" width="3.5" height="2" fill="#1f2933"/>
  <rect x="716.5" y="474" width="3.5" height="2" fill="#1f2933"/>
  <line x1="720" y1="500.5" x2="698.5" y2="486" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="720" y1="485" x2="741.5" y2="470.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="720" y1="473" x2="698.5" y2="458.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="720" cy="461" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="702" cy="479" r="19" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="738" cy="476.5" r="20.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="720" cy="488.5" r="18" fill="#2b8a3e" fill-opacity="0.85"/>
</svg>

## Ydinajatus

### Pyörivä käämi magneettikentässä
Luvussa *Sähkömagneettinen induktio* käämiin syntyi induktiojännite, kun sen läpi kulkeva magneettivuo muuttui. **Generaattori** on laite, joka muuttaa pyörimisen sähköksi. Se saa vuon muuttumaan pyörittämällä käämiä magneetin napojen välissä.

Kun käämin taso on kohtisuorassa kenttää vastaan, kenttäviivoja kulkee käämin läpi eniten. Silloin vuo on suurin, $\Phi = BA$. Neljänneskierroksen jälkeen käämin taso on kentän suuntainen. Yksikään kenttäviiva ei kulje käämin läpi, joten vuo on nolla. Seuraavan neljänneksen jälkeen kenttä kulkee käämin läpi taas kohtisuoraan, mutta käämin toiselta puolelta. Silloin vuo on $-BA$. Kun käämi pyörii tasaisesti, vuo vaihtelee siis koko ajan arvojen $BA$ ja $-BA$ välillä.

<svg data-fig="generator" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva vaihtovirtageneraattorista, ei mittakaavassa. Ylhäällä on magneetin N-napa ja alhaalla S-napa, joten magneettikenttä osoittaa alaspäin. Napojen välissä on kuparinen käämi. Käämiä pyöritetään vaakasuoran akselin ympäri. Käämin johtimen päät on kytketty akselilla oleviin kahteen liukurenkaaseen. Renkaita koskettavat hiiliharjat. Harjoista johdot kulkevat lamppuun." style="max-width:100%;font-size:24px">
  <rect x="60" y="26" width="300" height="50" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="200" y="36.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <rect x="60" y="294" width="300" height="50" rx="4" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="200" y="304.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <line x1="82" y1="84" x2="82" y2="274" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M82,286 L76,273 L88,273 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="338" y1="84" x2="338" y2="274" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M338,286 L332,273 L344,273 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="348" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <path d="M130,116 L306,116 L290,254 L114,254 Z" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round"/>
  <path d="M137,123 L299,123 L283,247 L121,247 Z" fill="none" stroke="#b8622d" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="165" y="171.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{käämi}$</div></foreignObject>
  <line x1="54" y1="185" x2="118" y2="185" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <path d="M64,154 A12,32 0 1 0 74,214" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M74,222 L68,208 L80,209 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="300" y1="185" x2="456" y2="185" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="298" y1="179" x2="404" y2="179" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="298" y1="191" x2="434" y2="191" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <ellipse cx="410" cy="185" rx="9" ry="26" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="440" cy="185" rx="9" ry="26" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <rect x="402" y="211" width="16" height="20" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="432" y="139" width="16" height="20" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M440,139 V122 H497 V172" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M410,231 V248 H497 V198" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="488" y="172" width="20" height="26" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="553" y1="157.5" x2="564.5" y2="143.5" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="564" y1="172.5" x2="580.5" y2="166.5" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="565.5" y1="191.5" x2="583" y2="194.5" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="557.5" y1="208" x2="571.5" y2="219.5" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="530" cy="185" r="24" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M518,185 q6,-10 12,0 t12,0" fill="none" stroke="#e8590c" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="365" y="81.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hiiliharjat}$</div></foreignObject>
  <line x1="440" y1="112" x2="440" y2="136" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="372" y="267.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liukurenkaat}$</div></foreignObject>
  <line x1="425" y1="266" x2="425" y2="215" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

<figure class="unit-photo"><img src="pics/fy7/bicycle-dynamo.webp" alt="Polkupyörän etupyörä ja valo. Renkaan vieressä on pieni hopeinen dynamo."><figcaption>Polkupyörän dynamo on pieni generaattori. Rengas pyörittää dynamon sisällä magneettia. Magneetti pyörii käämin sisällä. Magneettivuo käämin läpi muuttuu, ja käämiin syntyy vaihtojännite.</figcaption></figure>

### Liukurenkaat ja harjat
Käämin johtimen päät on kytketty akselilla oleviin kahteen **liukurenkaaseen**. Renkaita koskettavat hiiliharjat. Harjojen kautta jännite johdetaan ulkoiseen virtapiiriin, esimerkiksi kuvan lamppuun. Tasavirtamoottorissa kommutaattori kääntää virran suunnan (luku *Voima virtajohtimeen: sähkömoottori ja kaiutin*). Liukurenkaat eivät käännä virran suuntaa. Siksi ulkoiseen piiriin tulee käämiin syntyvä jännite sellaisenaan.

### Miksi jännite on sinimuotoinen
Induktiolain mukaan jännite ei riipu siitä, kuinka suuri vuo on. Jännite riippuu siitä, kuinka nopeasti vuo muuttuu. Kuvaajassa $\Phi(t)$ muutosnopeus on kuvaajan jyrkkyys.

Kun vuo on suurimmillaan, käämin sivut liikkuvat kenttäviivojen suuntaisesti. Vuo ei silloin hetkeen juuri muutu, ja jännite on nolla. Kun käämin taso on kentän suuntainen, vuo on nolla. Silloin sivut liikkuvat kohtisuoraan kenttäviivojen poikki, ja vuo muuttuu nopeimmin. Silloin jännite on suurimmillaan.

Vuo vaihtelee kosinin tavoin, ja sen jyrkkyys vaihtelee sinin tavoin. Siksi jännite on sinimuotoinen eli sen kuvaaja on siniaallon muotoinen. Jokaisella puolikierroksella vuon muutoksen suunta kääntyy. Silloin myös jännitteen merkki kääntyy. Syntyy **vaihtojännite**. Suljetussa piirissä kulkee **vaihtovirta**, jonka suunta vaihtuu kahdesti jokaisen kierroksen aikana.

<svg data-fig="phi-e" viewBox="0 0 600 440" role="img" aria-label="Kaksi kuvaajaa samalla aika-akselilla yhden jaksonajan T ajalta. Ylemmässä kuvaajassa vihreä magneettivuo Phi alkaa suurimmasta arvostaan BA. Se laskee nollaan neljäsosajakson kohdalla. Puolen jakson kohdalla se on pienimmillään, miinus BA. Sitten se palaa arvoon BA. Alemmassa kuvaajassa violetti jännite e alkaa nollasta. Se on suurin, e0, neljäsosajakson kohdalla. Puolen jakson kohdalla se on nolla. Kolmen neljäsosajakson kohdalla se on pienin, miinus e0. Katkoviiva neljäsosajakson kohdalla näyttää, että jännite on suurin, kun vuo on nolla. Alimpana on pieniä kuvia käämistä päästä katsottuna. Kenttä osoittaa oikealle. Hetkellä nolla käämin taso on kohtisuorassa kenttää vastaan. Neljäsosajakson kohdalla se on kentän suuntainen, ja niin edelleen." style="max-width:100%;font-size:24px">
  <line x1="208" y1="170" x2="208" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="170" x2="296" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="170" x2="384" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="170" x2="472" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="159" x2="500" y2="159" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="115" x2="500" y2="115" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="71" x2="500" y2="71" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="170" x2="514" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,170 L513,176 L513,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="171" x2="120" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,34 L126,47 L114,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="170" x2="208" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="296" y1="170" x2="296" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="384" y1="170" x2="384" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="472" y1="170" x2="472" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="159" x2="120" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="144.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-BA$</div></foreignObject>
  <line x1="113" y1="115" x2="120" y2="115" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="100.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="71" x2="120" y2="71" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$BA$</div></foreignObject>
  <foreignObject x="532" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi$</div></foreignObject>
  <polyline points="120,71 123,71 126,71 129,71.5 131.5,72 134.5,72.5 137.5,73 140.5,74 143.5,75 146.5,76 149.5,77 152.5,78 155,79.5 158,81 161,82.5 164,84 167,85.5 170,87.5 173,89 175.5,91 178.5,93 181.5,95 184.5,97 187.5,99 190.5,101.5 193.5,103.5 196,106 199,108 202,110.5 205,112.5 208,115 211,117.5 214,119.5 217,122 219.5,124 222.5,126.5 225.5,128.5 228.5,131 231.5,133 234.5,135 237.5,137 240,139 243,141 246,142.5 249,144.5 252,146 255,147.5 258,149 260.5,150.5 263.5,152 266.5,153 269.5,154 272.5,155 275.5,156 278.5,157 281.5,157.5 284,158 287,158.5 290,159 293,159 296,159 299,159 302,159 304.5,158.5 307.5,158 310.5,157.5 313.5,157 316.5,156 319.5,155 322.5,154 325,153 328,152 331,150.5 334,149 337,147.5 340,146 343,144.5 346,142.5 348.5,141 351.5,139 354.5,137 357.5,135 360.5,133 363.5,131 366.5,128.5 369,126.5 372,124 375,122 378,119.5 381,117.5 384,115 387,112.5 390,110.5 392.5,108 395.5,106 398.5,103.5 401.5,101.5 404.5,99 407.5,97 410.5,95 413,93 416,91 419,89 422,87.5 425,85.5 428,84 431,82.5 433.5,81 436.5,79.5 439.5,78 442.5,77 445.5,76 448.5,75 451.5,74 454.5,73 457,72.5 460,72 463,71.5 466,71 469,71 472,71" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="56.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <line x1="208" y1="330" x2="208" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="330" x2="296" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="330" x2="384" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="330" x2="472" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="320" x2="500" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="280" x2="500" y2="280" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="240" x2="500" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="330" x2="514" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,330 L513,336 L513,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="331" x2="120" y2="216" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,204 L126,217 L114,217 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="330" x2="208" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="296" y1="330" x2="296" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="339.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="384" y1="330" x2="384" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="472" y1="330" x2="472" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="320" x2="120" y2="320" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-e_0$</div></foreignObject>
  <line x1="113" y1="280" x2="120" y2="280" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="240" x2="120" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$e_0$</div></foreignObject>
  <foreignObject x="532" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e$</div></foreignObject>
  <polyline points="120,280 123,278 126,276 129,273.5 131.5,271.5 134.5,269.5 137.5,267.5 140.5,265.5 143.5,263.5 146.5,262 149.5,260 152.5,258 155,256.5 158,255 161,253 164,251.5 167,250.5 170,249 173,247.5 175.5,246.5 178.5,245.5 181.5,244.5 184.5,243.5 187.5,242.5 190.5,242 193.5,241.5 196,241 199,240.5 202,240 205,240 208,240 211,240 214,240 217,240.5 219.5,241 222.5,241.5 225.5,242 228.5,242.5 231.5,243.5 234.5,244.5 237.5,245.5 240,246.5 243,247.5 246,249 249,250.5 252,251.5 255,253 258,255 260.5,256.5 263.5,258 266.5,260 269.5,262 272.5,263.5 275.5,265.5 278.5,267.5 281.5,269.5 284,271.5 287,273.5 290,276 293,278 296,280 299,282 302,284 304.5,286.5 307.5,288.5 310.5,290.5 313.5,292.5 316.5,294.5 319.5,296.5 322.5,298 325,300 328,302 331,303.5 334,305 337,307 340,308.5 343,309.5 346,311 348.5,312.5 351.5,313.5 354.5,314.5 357.5,315.5 360.5,316.5 363.5,317.5 366.5,318 369,318.5 372,319 375,319.5 378,320 381,320 384,320 387,320 390,320 392.5,319.5 395.5,319 398.5,318.5 401.5,318 404.5,317.5 407.5,316.5 410.5,315.5 413,314.5 416,313.5 419,312.5 422,311 425,309.5 428,308.5 431,307 433.5,305 436.5,303.5 439.5,302 442.5,300 445.5,298 448.5,296.5 451.5,294.5 454.5,292.5 457,290.5 460,288.5 463,286.5 466,284 469,282 472,280" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$e$</div></foreignObject>
  <line x1="208" y1="60" x2="208" y2="170" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="208" y1="230" x2="208" y2="330" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="49.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <line x1="94" y1="418" x2="138" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M146,418 L137,422 L137,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="120" y1="375" x2="120" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="120" cy="375" r="4" fill="#1f2933"/>
  <circle cx="120" cy="409" r="4" fill="#1f2933"/>
  <line x1="182" y1="418" x2="226" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M234,418 L225,422 L225,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="191" y1="392" x2="225" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="191" cy="392" r="4" fill="#1f2933"/>
  <circle cx="225" cy="392" r="4" fill="#1f2933"/>
  <line x1="270" y1="418" x2="314" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M322,418 L313,422 L313,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="296" y1="409" x2="296" y2="375" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="296" cy="409" r="4" fill="#1f2933"/>
  <circle cx="296" cy="375" r="4" fill="#1f2933"/>
  <line x1="358" y1="418" x2="402" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M410,418 L401,422 L401,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="401" y1="392" x2="367" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="401" cy="392" r="4" fill="#1f2933"/>
  <circle cx="367" cy="392" r="4" fill="#1f2933"/>
  <line x1="446" y1="418" x2="490" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M498,418 L489,422 L489,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="472" y1="375" x2="472" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="472" cy="375" r="4" fill="#1f2933"/>
  <circle cx="472" cy="409" r="4" fill="#1f2933"/>
</svg>

<figure class="unit-photo"><img src="pics/fy7/generator-stator.webp" alt="Iso pyöreä kuilu ylhäältä. Seinissä on käämejä, ja reunoilla on keltaiset kaiteet."><figcaption>Vesivoimalan generaattori. Roottori on nostettu pois. Käämit ovat paikallaan kehän ympärillä. Kun roottori pyörii sisällä, käämeihin syntyy jännite.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy7/generator-rotor.webp" alt="Suuri punaruskea lieriö hallin lattialla. Sen ympärillä ihmiset näyttävät pieniltä."><figcaption>Voimalan generaattorin roottori huollossa Belgiassa. Roottorin reunalla on sähkömagneetteja. Kun roottori pyörii, magneettivuo käämien läpi muuttuu koko ajan.</figcaption></figure>

### Voimalaitoksen generaattori ja tuulivoimala
Voimalaitosten suurissa generaattoreissa pyörii sähkömagneetti, ja käämit ovat paikallaan sen ympärillä. Paikallaan olevan käämin läpi kulkeva vuo muuttuu samalla tavalla kuin pyörivässä käämissä. Siksi syntyy samanlainen vaihtojännite. Suuri virta saadaan käämeistä ilman liukukoskettimia.

Tuulivoimalassa tuuli pyörittää roottoria, ja roottorin akseli pyörittää generaattoria. Roottori pyörii hitaasti, noin $10$–$15$ kierrosta minuutissa. Siksi generaattorissa on joko vaihteisto, joka nostaa pyörimisnopeutta, tai paljon magneettinapoja. Tuulen nopeus vaihtelee. Siksi taajuusmuuttaja muuntaa generaattorin jännitteen verkon taajuuteen $50\,\text{Hz}$.

Suomessa oli vuoden 2024 lopussa $1835$ tuulivoimalaa. Niiden yhteenlaskettu nimellisteho oli $8358\,\text{MW}$. Ne tuottivat vuonna 2024 sähköä $19{,}8\,\text{TWh}$. Se on noin $24\,\%$ Suomen sähkönkulutuksesta (Suomen Uusiutuvat ry, tuulivoimatilastot 2024).

## Kaava: Generaattorin jännite
Käämissä on $N$ kierrosta, ja sen pinta-ala on $A$. Käämi pyörii tasaisesti homogeenisessa eli joka kohdassa samanlaisessa magneettikentässä $B$. Pyörimistaajuus on $f$. Hetkellä $t = 0$ käämin taso on kohtisuorassa kenttää vastaan. Silloin käämin läpi kulkeva vuo ja käämiin syntyvä jännite ovat
```latex
\begin{aligned}
&\Phi = BA\cos(2\pi f t) \\[4pt]
&e = e_0 \sin(2\pi f t) \\[4pt]
&e_0 = NBA \cdot 2\pi f
\end{aligned}
```
missä $\Phi$ on magneettivuo yhden kierroksen läpi (Wb), $e$ jännitteen hetkellinen arvo eli arvo tietyllä hetkellä (V), $e_0$ jännitteen huippuarvo eli suurin arvo (V), $N$ kierrosten lukumäärä, $B$ magneettivuon tiheys (T), $A$ käämin pinta-ala (m²) ja $f$ pyörimistaajuus eli kierrosten määrä sekunnissa (Hz). Jännitteen taajuus on sama kuin pyörimistaajuus. Jaksonaika eli yhden kierroksen kesto on $T = 1 : f$.

### Mistä huippuarvo tulee
Huippuarvo saadaan liikkuvan johtimen jännitteestä $e = vBl$ (luku *Sähkömagneettinen induktio*). Suorakulmaisen käämin kaksi sivua, joiden pituus on $l$, kiertävät akselia säteellä $b : 2$. Tässä $b$ on käämin leveys. Sivujen nopeus on $v = 2\pi f \cdot b : 2 = \pi f b$.

Jännitteeseen vaikuttaa vain se nopeuden osa, joka on kohtisuorassa kenttää vastaan. Se on $v \sin\theta$, missä $\theta$ on nopeuden ja kentän välinen kulma. Kumpaankin sivuun syntyy jännite $B l v \sin\theta$, ja sivujen jännitteet summautuvat kierroksessa.

Yhdessä kierroksessa jännite on siis $2 B l \cdot \pi f b \sin\theta = BA \cdot 2\pi f \sin\theta$, koska $lb = A$. Kun kierroksia on $N$, jännite on $N$-kertainen. Kun $\theta = 90^\circ$, käämin taso on kentän suuntainen ja jännite on huippuarvossaan $e_0 = NBA \cdot 2\pi f$. Kaksinkertainen pyörimistaajuus kaksinkertaistaa sekä jännitteen taajuuden että huippuarvon, koska sivut liikkuvat kaksi kertaa nopeammin.

<svg data-fig="derive" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva, ei mittakaavassa. Käämi nähdään akselin suunnasta. Vaakasuorat vihreät kenttäviivat osoittavat oikealle. Käämin taso on vinossa. Käämin kaksi sivua ovat ympyröinä, koska niiden pituus l on kohtisuoraan paperia vastaan. Oikean alemman sivun virta kulkee paperiin päin ja vasemman ylemmän paperista ulos. Sivujen nopeudet ovat siniset nuolet. Ne ovat kohtisuorassa käämin tasoa vastaan ja vastakkaissuuntaiset. Oikean sivun nopeuden ja kentän välinen kulma on theeta. Nopeuden kenttää vastaan kohtisuora osa v sin theeta on piirretty katkoviivalla. Käämin leveys on b." style="max-width:100%;font-size:24px">
  <line x1="24" y1="40" x2="576" y2="40" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M548,40 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="24" y1="110" x2="576" y2="110" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M548,110 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="24" y1="180" x2="576" y2="180" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M548,180 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="24" y1="250" x2="576" y2="250" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M548,250 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="24" y1="320" x2="576" y2="320" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M548,320 l-14,-7 v14 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="527" y="3.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{B}$</span></div></foreignObject>
  <line x1="153.5" y1="115.5" x2="306.5" y2="244.5" stroke="#b8622d" stroke-width="6" stroke-linecap="round"/>
  <circle cx="230" cy="180" r="6" fill="#1f2933"/>
  <foreignObject x="180" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b$</span></div></foreignObject>
  <line x1="317" y1="232" x2="385.5" y2="150" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M394,140 L390,155 L380,147 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="143" y1="128" x2="74.5" y2="210" stroke="#1971c2" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M66,220 L70,205 L80,213 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="404" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{v}$</span></div></foreignObject>
  <foreignObject x="23" y="209.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{v}$</span></div></foreignObject>
  <line x1="317" y1="232" x2="467" y2="232" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M387,232 A70,70 0 0 0 362,178.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="350.5" y="197" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <line x1="394" y1="232" x2="394" y2="150" stroke="#1971c2" stroke-width="2.5" stroke-dasharray="7 5"/>
  <path d="M394,140 L388,152 L400,152 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="406" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v\sin\theta$</span></div></foreignObject>
  <circle cx="306.5" cy="244.5" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <line x1="299" y1="236.5" x2="314.5" y2="252" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="314.5" y1="236.5" x2="299" y2="252" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="153.5" cy="115.5" r="14" fill="#ffffff" stroke="#7048e8" stroke-width="2.5"/>
  <circle cx="153.5" cy="115.5" r="4.48" fill="#7048e8"/>
  <foreignObject x="264.5" y="250" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I$</span></div></foreignObject>
</svg>

### Tehollinen arvo
Vaihtojännitteen keskiarvo yhden jakson aikana on nolla. Lamppu tai vastus lämpenee silti, koska teho $p = ui$ on positiivinen kummallakin virran suunnalla. Vastuksen teho vaihtelee nollan ja huippuarvon $P_0 = U_0 I_0$ välillä. Sen keskiarvo on puolet huippuarvosta.

**Tehollinen arvo** on se tasajännite tai tasavirta, joka tuottaisi vastukseen saman keskimääräisen tehon:
```latex
\begin{aligned}
&U = \frac{U_0}{\sqrt{2}} \\[4pt]
&I = \frac{I_0}{\sqrt{2}}
\end{aligned}
```
missä $U_0$ ja $I_0$ ovat jännitteen ja virran **huippuarvot** ja $U$ ja $I$ tehollisarvot. Silloin keskimääräinen teho on $P = UI$, kuten tasavirralla.

Pistorasian $230\,\text{V}$ on tehollinen arvo. Jännitteen huippuarvo on $230\,\text{V} \cdot \sqrt{2} \approx 325\,\text{V}$. Taajuus on $50\,\text{Hz}$, joten jännite vaihtaa suuntaansa sata kertaa sekunnissa. Fingrid pitää kantaverkon taajuuden normaalisti välillä $49{,}9$–$50{,}1\,\text{Hz}$. Mittarit näyttävät vaihtojännitteen ja -virran tehollisarvoina.

<svg data-fig="power" viewBox="0 0 600 320" role="img" aria-label="Kuvaaja: vastuksen teho p ajan t funktiona yhden jaksonajan T ajalta, kun vastukseen on kytketty sinimuotoinen vaihtojännite. Oranssi käyrä vaihtelee nollan ja huippuarvon P0 välillä. Se on nolla hetkillä 0, puoli jaksoa ja T. Huipussaan se on neljäsosajakson ja kolmen neljäsosajakson kohdalla. Katkoviiva korkeudella puolet P0:sta on tehon keskiarvo. Käyrän huiput sen yläpuolella ovat yhtä suuret kuin kuopat sen alapuolella." style="max-width:100%;font-size:24px">
  <line x1="202.5" y1="262" x2="202.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="262" x2="285" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367" y1="262" x2="367" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="449.5" y1="262" x2="449.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="168" x2="476" y2="168" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="74.5" x2="476" y2="74.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="262" x2="490" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,262 L489,268 L489,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="263" x2="120" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,26 L126,39 L114,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="202.5" y1="262" x2="202.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="285" y1="262" x2="285" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="271.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="367" y1="262" x2="367" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="325.5" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="449.5" y1="262" x2="449.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="439.5" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="168" x2="120" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="154" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}P_0$</div></foreignObject>
  <line x1="113" y1="74.5" x2="120" y2="74.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="60" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_0$</div></foreignObject>
  <foreignObject x="90" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="-4.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <polygon points="120,168 120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262 449.5,168" fill="#ffc078" fill-opacity="0.3"/>
  <polyline points="120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="120" y1="168" x2="449.5" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="459.5" y="154" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskiarvo}$</div></foreignObject>
</svg>

## Esimerkki
Opetuskäytössä olevan generaattorin käämissä on $250$ kierrosta. Suorakulmaisen käämin sivujen pituudet ovat $4{,}0\,\text{cm}$ ja $5{,}0\,\text{cm}$. Käämi pyörii homogeenisessa magneettikentässä, jonka magneettivuon tiheys on $0{,}18\,\text{T}$. Se tekee $12$ kierrosta sekunnissa. Kuinka suuri on käämiin syntyvän vaihtojännitteen tehollinen arvo?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kierrosten lukumäärä on $N = 250$. Käämin sivut ovat $4{,}0\,\text{cm}$ ja $5{,}0\,\text{cm}$. Magneettivuon tiheys on $B = 0{,}18\,\text{T}$ ja pyörimistaajuus $f = 12\,\text{Hz}$. Kysytään jännitteen tehollista arvoa $U$.

<!-- vaihe -->

**Periaate.** Käämi pyörii tasaisesti homogeenisessa kentässä. Siksi siihen syntyy sinimuotoinen vaihtojännite, jonka huippuarvo on $e_0 = NBA \cdot 2\pi f$. Sinimuotoisen jännitteen tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&e_0 = NBA \cdot 2\pi f \\
&U = \frac{e_0}{\sqrt{2}} = \frac{NBA \cdot 2\pi f}{\sqrt{2}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Pinta-ala neliömetreinä: $A = 4{,}0 \cdot 0{,}01\,\text{m} \cdot 5{,}0 \cdot 0{,}01\,\text{m} = 0{,}0020\,\text{m}^2$. Pyörimistaajuus on $12$ kierrosta sekunnissa eli $f = 12\,\text{Hz}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin huippuarvo ja sitten tehollinen arvo:
```latex
\begin{aligned}
&e_0 = NBA \cdot 2\pi f \\
&= 250 \cdot 0{,}18\,\text{T} \cdot 0{,}0020\,\text{m}^2 \\
&\quad \cdot 2\pi \cdot 12\,\tfrac{1}{\text{s}} \\
&= 6{,}786\,\text{V} \\[6pt]
&U = \frac{6{,}786\,\text{V}}{\sqrt{2}} \\
&= 4{,}798\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Jännitteen tehollinen arvo on $U \approx 4{,}8\,\text{V}$ ja huippuarvo noin $6{,}8\,\text{V}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, kuten käämin mitat ja magneettivuon tiheys.

<!-- vaihe -->

**Järkevyys.** Yksiköt sopivat: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. Pyöreillä luvuilla $250 \cdot 0{,}2\,\text{T} \cdot 0{,}002\,\text{m}^2 \cdot 6 \cdot 10\,\tfrac{1}{\text{s}} \approx 6\,\text{V}$, mikä sopii huippuarvoon. Tehollinen arvo on pienempi kuin huippuarvo, kuten pitääkin. Muutaman voltin jännite on samaa suuruusluokkaa kuin polkupyörän dynamon jännite.

## Yleinen virhekäsitys
Moni ajattelee, että jännite on suurin silloin, kun käämin läpi kulkee eniten kenttäviivoja eli käämin taso on kohtisuorassa kenttää vastaan. Silloin jännite on kuitenkin **nolla**, koska vuo ei sillä hetkellä muutu. Jännite on suurin, kun käämin taso on kentän suuntainen ja vuo on nolla, koska silloin vuo muuttuu nopeimmin.

Toinen yleinen virhe on pitää pistorasian $230\,\text{V}$:a jännitteen suurimpana arvona. Se on tehollinen arvo. Jännite käy välillä $-325\,\text{V}$ ja $325\,\text{V}$.

Kolmas virhe on päätellä, että vaihtovirta ei siirrä energiaa, koska sen keskiarvo on nolla. Teho on positiivinen kummallakin virran suunnalla.

## Tiivistelmä
- Generaattorissa käämi pyörii magneettikentässä (tai magneetti käämin sisällä). Käämin läpi kulkeva vuo $\Phi = BA\cos(2\pi f t)$ vaihtelee jatkuvasti.
- Induktiojännite riippuu vuon muutosnopeudesta. Se on nolla, kun vuo on suurin. Se on suurin, kun käämin taso on kentän suuntainen ja vuo on nolla.
- Syntyy sinimuotoinen vaihtojännite $e = e_0 \sin(2\pi f t)$. Sen huippuarvo on $e_0 = NBA \cdot 2\pi f$, ja sen taajuus on sama kuin pyörimistaajuus.
- Sinimuotoisen vaihtojännitteen tehollinen arvo on $U = U_0 : \sqrt{2}$ ja virran $I = I_0 : \sqrt{2}$. Keskimääräinen teho on $P = UI$. Verkkojännitteen $230\,\text{V}$ huippuarvo on noin $325\,\text{V}$ ja taajuus $50\,\text{Hz}$.
- Tuulivoimalan roottori pyörittää generaattoria, ja taajuusmuuttaja sovittaa jännitteen verkon taajuuteen.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: pyöräilijä ajaa iltahämärässä. Etupyörän navassa on dynamo, joka antaa lampulle vaihtojännitteen. Lampun valokeila valaisee tietä pyörän edessä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy77s-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy77s-road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6c757d"/><stop offset="1" stop-color="#1f2933"/></linearGradient></defs>
  <rect x="0" y="0" width="600" height="360" fill="url(#fy77s-sky)"/>
  <path d="M0,250 L11,226 L22,250 L34,223 L46,250 L57.5,224.5 L69,250 L86.5,205 L104.5,250 L116.5,222 L129,250 L141,222.5 L153.5,250 L170,209 L186.5,250 L205.5,202 L224.5,250 L241,209 L257.5,250 L277,200.5 L296,250 L314.5,203.5 L332.5,250 L348,213 L363,250 L382,202 L401,250 L416,213 L431.5,250 L444.5,218.5 L458,250 L474.5,208.5 L491.5,250 L506.5,212.5 L522,250 L537,214.5 L551.5,250 L562.5,226.5 L573,250 L592,202.5 L610.5,250 V290 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="286" width="600" height="74" fill="url(#fy77s-road)"/>
  <path d="M410,214 L600,250 L600,330 Z" fill="#ffc078" fill-opacity="0.55"/>
  <circle cx="200" cy="286" r="52" fill="none" stroke="#1f2933" stroke-width="7.8"/>
  <circle cx="200" cy="286" r="46.8" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="200" y1="286" x2="244.5" y2="286" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="238.5" y2="308.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="222.5" y2="324.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="200" y2="330.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="177.5" y2="324.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="161.5" y2="308.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="155.5" y2="286" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="161.5" y2="263.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="177.5" y2="247.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="200" y2="241.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="222.5" y2="247.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="286" x2="238.5" y2="263.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="200" cy="286" r="4.68" fill="#1f2933"/>
  <circle cx="380" cy="286" r="52" fill="none" stroke="#1f2933" stroke-width="7.8"/>
  <circle cx="380" cy="286" r="46.8" fill="none" stroke="#8a96a3" stroke-width="2"/>
  <line x1="380" y1="286" x2="424.5" y2="286" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="418.5" y2="308.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="402.5" y2="324.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="380" y2="330.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="357.5" y2="324.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="341.5" y2="308.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="335.5" y2="286" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="341.5" y2="263.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="357.5" y2="247.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="380" y2="241.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="402.5" y2="247.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="286" x2="418.5" y2="263.5" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="380" cy="286" r="4.68" fill="#1f2933"/>
  <path d="M200,286 L265,286 L342,210.5 L252,210.5 Z" fill="none" stroke="#c92a2a" stroke-width="6.24" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M265,286 L250.5,190.5" fill="none" stroke="#c92a2a" stroke-width="6.24" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M342,210.5 L380,286" fill="none" stroke="#c92a2a" stroke-width="6.24" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M342,210.5 L337,190.5" fill="none" stroke="#c92a2a" stroke-width="6.24" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M229,190.5 H256" fill="none" stroke="#1f2933" stroke-width="7.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M324,192.5 Q337,185 353,192.5" fill="none" stroke="#1f2933" stroke-width="5.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="265" cy="286" r="10.4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M243,183.5 L283,205 L275.5,297" fill="none" stroke="#1f2933" stroke-width="13.5" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M268.5,300.5 h14.5" fill="none" stroke="#6c757d" stroke-width="8.1" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M238,187 L297,129.5" fill="none" stroke="#d0e6fb" stroke-width="19.8" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M297,129.5 L337,189" fill="none" stroke="#d0e6fb" stroke-width="10.8" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="337" cy="189" r="5.4" fill="#f1dfb5"/>
  <circle cx="315" cy="115" r="13.5" fill="#f1dfb5"/>
  <path d="M299,114 Q304.5,95 322.5,98 Q333,102.5 330.5,111.5 Z" fill="#e8590c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="392" y="206" width="22" height="16" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="414" cy="214" r="6" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <circle cx="380" cy="286" r="11" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="382" y1="280" x2="400" y2="222" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
</svg>
