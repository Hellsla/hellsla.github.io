# Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö

> **Miksi** auto suistuu liukkaassa kaarteessa ulos tieltä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Talvinen maantie kaartaa metsän läpi oikealle. Kaarteessa ajaa auto takaapäin nähtynä. Tien reunoilla on lumipenkat ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy54h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy54h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy54h-snow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy54h-asf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy54h-sky)"/>
  <circle cx="1060" cy="92" r="61" fill="#ffffff" fill-opacity="0.5"/>
  <circle cx="1060" cy="92" r="38" fill="url(#fy54h-sun)"/>
  <path d="M160,106 Q158,72 198,76 Q214,40 254,52 Q290,32 310,70 Q346,74 342,106 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M632.5,75 Q631,49.5 661,52.5 Q673,25.5 703,34.5 Q730,19.5 745,48 Q772,51 769,75 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,300 Q220,220 470,262 T900,236 T1200,250 V340 H0 Z" fill="#ffffff" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round"/>
  <path d="M0,300 L13,272.5 L26,300 L40,268.5 L54.5,300 L67.5,272 L80.5,300 L99.5,256.5 L118,300 L134,263.5 L150,300 L169,256.5 L187.5,300 L204,262 L221,300 L232.5,276 L244,300 L262,258 L280,300 L291,278 L302.5,300 L315.5,272 L328.5,300 L345.5,260.5 L363,300 L379,263.5 L395,300 L407,276 L418.5,300 L429.5,277.5 L440.5,300 L453,274 L465.5,300 L480.5,267 L495,300 L509.5,268 L524,300 L536,275.5 L548,300 L559,278.5 L569.5,300 L581,276 L593,300 L609,263.5 L625,300 L642.5,259.5 L660.5,300 L672.5,274.5 L685,300 L697,275 L709,300 L720.5,277 L731.5,300 L751,254 L770.5,300 L781.5,277.5 L793,300 L810.5,259 L828.5,300 L842.5,269.5 L856.5,300 L873.5,260.5 L891,300 L909,258 L927,300 L942,266.5 L957,300 L969,275.5 L980.5,300 L994.5,269.5 L1008.5,300 L1025.5,262 L1042,300 L1061,255.5 L1080,300 L1091.5,276 L1103.5,300 L1120,262.5 L1136.5,300 L1150,270 L1164,300 L1178,270 L1191.5,300 L1208,262.5 L1224.5,300 V330 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="318" width="1200" height="282" fill="url(#fy54h-snow)"/>
  <path d="M603.5,737.5 L594,732 L585,725.5 L576.5,718 L569,710 L562,701.5 L556,692 L551,682 L547,671.5 L544.5,660 L543,648 L542.5,636 L543,623 L545,610 L548.5,596.5 L553,583 L559,569.5 L566,556 L574,542 L583.5,528.5 L594,515 L606,502 L619,489 L633,476 L648,464 L664,452 L681.5,440 L699.5,429 L718.5,418.5 L738,408 L759,398.5 L780.5,389 L803,380.5 L826.5,372.5 L850.5,365 L875.5,358 L901,352 L927.5,346.5 L954.5,341.5 L982.5,337.5 L1011,335 L1009,309 L980,310.5 L952,311 L924,312 L896.5,312 L869.5,312.5 L843,313 L817,313 L791,313.5 L766,313.5 L741,314 L716.5,314.5 L692,315 L668,315.5 L644.5,316.5 L621,317 L597.5,318.5 L574.5,320 L551.5,321.5 L528.5,323.5 L506,326 L483,328.5 L460.5,332 L437.5,335.5 L415,340 L392,345 L369,350.5 L346.5,357 L323.5,364.5 L300.5,373 L277,382 L254,392.5 L231,404 L208.5,416.5 L185.5,430.5 L163,446 L141,462.5 L119,480.5 L97.5,500 L77,520.5 L56.5,542.5 Z" fill="#ffffff" stroke="#c9c2b2" stroke-width="2" stroke-linejoin="round"/>
  <path d="M561.5,722.5 L554.5,715.5 L547.5,708 L541.5,700 L536,691.5 L531.5,682 L528,672.5 L525,662 L523,651 L522.5,639.5 L522.5,628 L524,616 L526.5,603.5 L530,590.5 L534.5,578 L540.5,565 L548,552 L556,539 L565.5,526 L576,513.5 L587.5,500.5 L600,488.5 L614,476 L628.5,464.5 L644,453 L661,441.5 L678.5,431 L697,420.5 L716.5,410.5 L736.5,401 L757.5,392 L779.5,383.5 L802.5,375.5 L826,368 L850,361 L875,354.5 L901,349 L927,343.5 L954.5,339.5 L982,335.5 L1010.5,333 L1009.5,311 L980.5,312.5 L952,313.5 L924,314.5 L897,315 L870,316 L843.5,317 L817.5,317.5 L792,318.5 L767,319.5 L742.5,320.5 L718,321.5 L694,322.5 L670.5,324 L647,325.5 L624,327.5 L601.5,329.5 L579,331.5 L556.5,334.5 L534.5,337 L512.5,340.5 L490.5,344 L469,348 L447.5,352.5 L426,357.5 L404.5,363 L383,369.5 L361.5,376.5 L340,384 L318.5,393 L297.5,402.5 L276.5,413 L255.5,424.5 L234.5,437 L214,450.5 L193.5,465.5 L173.5,481.5 L154,498.5 L135,517 L116,536.5 L98.5,557.5 Z" fill="url(#fy54h-asf)" stroke="#6c757d" stroke-width="2" stroke-linejoin="round"/>
  <line x1="330" y1="640" x2="337" y2="622" stroke="#ffffff" stroke-width="14.76" stroke-linecap="round"/>
  <line x1="347.5" y1="599.5" x2="357" y2="582.5" stroke="#ffffff" stroke-width="13.1065" stroke-linecap="round"/>
  <line x1="371" y1="561.5" x2="382.5" y2="546" stroke="#ffffff" stroke-width="11.5315" stroke-linecap="round"/>
  <line x1="399.5" y1="526.5" x2="413.5" y2="512" stroke="#ffffff" stroke-width="10.0378" stroke-linecap="round"/>
  <line x1="433" y1="494" x2="449.5" y2="480.5" stroke="#ffffff" stroke-width="8.62849" stroke-linecap="round"/>
  <line x1="472.5" y1="464" x2="491" y2="452" stroke="#ffffff" stroke-width="7.30702" stroke-linecap="round"/>
  <line x1="517" y1="437" x2="538" y2="426" stroke="#ffffff" stroke-width="6.07751" stroke-linecap="round"/>
  <line x1="567.5" y1="412.5" x2="590.5" y2="403" stroke="#ffffff" stroke-width="4.94478" stroke-linecap="round"/>
  <line x1="623" y1="391" x2="648.5" y2="382.5" stroke="#ffffff" stroke-width="3.91473" stroke-linecap="round"/>
  <line x1="683.5" y1="372.5" x2="712" y2="365" stroke="#ffffff" stroke-width="2.99471" stroke-linecap="round"/>
  <line x1="750" y1="356" x2="780.5" y2="350" stroke="#ffffff" stroke-width="2.19435" stroke-linecap="round"/>
  <line x1="821.5" y1="342.5" x2="854.5" y2="337.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="899" y1="332" x2="934" y2="328" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <line x1="981.5" y1="324" x2="1018.5" y2="321.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="81.5" y="495" width="17" height="25" fill="#b8622d"/>
  <path d="M14.5,499 L90,415 L165.5,499 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,415 L165.5,499 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M31,453 L90,369 L149,453 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,369 L149,453 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M48,406.5 L90,310 L132,406.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M90,310 L132,406.5 H90 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="184" y="402" width="12" height="18" fill="#b8622d"/>
  <path d="M136,405 L190,345 L244,405 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,345 L244,405 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M148,372 L190,312 L232,372 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,312 L232,372 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M160,339 L190,270 L220,339 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,270 L220,339 H190 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="35" y="365.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M-3,368 L40,320 L83,368 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,320 L83,368 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M6.5,341.5 L40,293.5 L73.5,341.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,293.5 L73.5,341.5 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M16,315 L40,260 L64,315 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M40,260 L64,315 H40 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1112.5" y="447" width="15" height="23" fill="#b8622d"/>
  <path d="M1051.5,451 L1120,375 L1188.5,451 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,375 L1188.5,451 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1067,409 L1120,333 L1173,409 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,333 L1173,409 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M1082,367.5 L1120,280 L1158,367.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1120,280 L1158,367.5 H1120 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="975" y="385.5" width="9.5" height="14.5" fill="#b8622d"/>
  <path d="M937,388 L980,340 L1023,388 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,340 L1023,388 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M946.5,361.5 L980,313.5 L1013.5,361.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,313.5 L1013.5,361.5 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M956,335 L980,280 L1004,335 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M980,280 L1004,335 H980 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="757" y="341.5" width="5.5" height="8.5" fill="#b8622d"/>
  <path d="M735,343 L760,315 L785,343 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,315 L785,343 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M740.5,327.5 L760,299.5 L779.5,327.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,299.5 L779.5,327.5 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M746,312 L760,280 L774,312 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M760,280 L774,312 H760 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="867.5" y="338" width="5" height="7" fill="#b8622d"/>
  <path d="M848.5,339 L870,315 L891.5,339 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M870,315 L891.5,339 H870 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M853,326 L870,302 L887,326 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M870,302 L887,326 H870 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M858,312.5 L870,285 L882,312.5 Z" fill="#2b8a3e" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M870,285 L882,312.5 H870 Z" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="449" y="386.5" width="99.5" height="47.5" rx="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <path d="M463,386.5 L471,361 H526.5 L534.5,386.5 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M472,384 L477,366.5 H520.5 L525.5,384 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="459" y="397.5" width="12" height="8" rx="2" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="457.5" y="433" width="17" height="20" rx="5" fill="#1f2933"/>
  <rect x="526.5" y="397.5" width="12" height="8" rx="2" fill="#f2a69c" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="523" y="433" width="17" height="20" rx="5" fill="#1f2933"/>
  <rect x="483" y="414" width="32" height="9.5" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="1.5"/>
</svg>

## Ydinajatus

### Nopeuden suunta muuttuu, joten kappale kiihtyy
Luvussa *Ympyrärata: jaksonaika ja ratanopeus* opit, että tasaisessa ympyräliikkeessä kappale kiertää ympyrärataa vakiovauhdilla. Nopeuden suuruus eli ratanopeus $v$ pysyy samana. Nopeuden suunta kuitenkin muuttuu koko ajan, sillä nopeus $\overline{v}$ osoittaa aina radan tangentin suuntaan. Tangentti on suora, joka koskettaa rataa yhdessä pisteessä. Nopeus on vektori, eli sillä on suuruus ja suunta. Siksi myös suunnan muutos on nopeuden muutos. Kun nopeus muuttuu, kappale kiihtyy. Tasaisessa ympyräliikkeessä kappale siis kiihtyy, vaikka sen vauhti ei muutu.

<svg data-fig="muutos" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa. Vasemmalla kappale kiertää ympyrärataa tasaisella vauhdilla. Siniset nopeusnuolet v 1 ja v 2 ovat yhtä pitkät mutta osoittavat eri suuntiin. Oikealla samat nuolet on piirretty samasta pisteestä: niiden kärkien välinen nuoli, nopeuden muutos, osoittaa kohti radan keskipistettä." style="max-width:100%;font-size:24px">
  <foreignObject x="65" y="7.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kappaleen rata}$</div></foreignObject>
  <circle cx="160" cy="200" r="105" fill="none" stroke="#c9c2b2" stroke-width="2.5"/>
  <circle cx="160" cy="200" r="5" fill="#1f2933"/>
  <foreignObject x="93.5" y="209.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{keskipiste}$</div></foreignObject>
  <circle cx="251" cy="147.5" r="11" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="244.5" y1="136" x2="210.5" y2="77.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="209.5" y1="75.5" x2="210" y2="90.5" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="209.5" y1="75.5" x2="222" y2="83.5" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="209" y="51" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <circle cx="69" cy="147.5" r="11" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="62.5" y1="159" x2="28.5" y2="217.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="27.5" y1="219.5" x2="40" y2="211.5" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="27.5" y1="219.5" x2="28" y2="204.5" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="1" y="227" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <circle cx="160" cy="95" r="11" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <line x1="160" y1="111" x2="160" y2="165" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <line x1="160" y1="167" x2="167" y2="154" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="160" y1="167" x2="153" y2="154" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="174" y="136.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <line x1="318" y1="20" x2="318" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="368.5" y="7.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nopeuden muutos}$</div></foreignObject>
  <line x1="540" y1="150" x2="506" y2="91" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="505" y1="89.5" x2="505.5" y2="104" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="505" y1="89.5" x2="517.5" y2="97" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="540" y1="150" x2="506" y2="209" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="505" y1="210.5" x2="517.5" y2="203" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="505" y1="210.5" x2="505.5" y2="196" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="516.5" y="71" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="516.5" y="204" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <line x1="505" y1="93.5" x2="505" y2="194.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <path d="M505,208.5 L498,194.5 L512,194.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="446" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\Delta\overline{v}$</div></foreignObject>
</svg>

Kuvassa kappaleen nopeus on ensin $\overline{v}_1$ ja hetken kuluttua $\overline{v}_2$. Kun nuolet piirretään samasta pisteestä, niiden kärkien välinen nuoli on nopeuden muutos $\Delta\overline{v}$. Se osoittaa kohti radan keskipistettä. Kiihtyvyys kertoo, kuinka nopeasti nopeus muuttuu. Siksi myös kiihtyvyys osoittaa kohti keskipistettä.

### Normaalikiihtyvyys osoittaa keskipisteeseen
Tasaisessa ympyräliikkeessä kiihtyvyys on kohtisuorassa nopeutta vastaan. Se osoittaa radan joka kohdassa kohti ympyrän keskipistettä. Tätä kiihtyvyyttä kutsutaan **normaalikiihtyvyydeksi** $\overline{a}_\text{n}$ tai **keskeiskiihtyvyydeksi**. Nimi tulee siitä, että kiihtyvyys on radan normaalin suuntainen. Normaali on suora, joka on kohtisuorassa tangenttia vastaan. Kiihtyvyydellä ei ole nopeuden suuntaista osaa, joten vauhti ei kasva eikä pienene. Kiihtyvyys muuttaa vain nopeuden suuntaa.

### Kokonaisvoima osoittaa keskipisteeseen
Newtonin toisen lain mukaan kokonaisvoima $\Sigma\overline{F}$ on samansuuntainen kuin kiihtyvyys. Kokonaisvoima on kaikkien kappaleeseen vaikuttavien voimien summa. Tasaisessa ympyräliikkeessä tämä summa osoittaa siis kohti radan keskipistettä. Keskipisteeseen osoittavaa kokonaisvoimaa kutsutaan **keskeisvoimaksi**. Ilman sitä kappale jatkaisi Newtonin ensimmäisen lain mukaan suoraan, radan tangentin suuntaan.

Keskeisvoima ei ole uusi voiman laji. Sitä ei piirretä voimakuvioon omana nuolenaan. Se on todellisten voimien summa, ja tilanne kertoo, mitkä voimat sen muodostavat. Oletetaan, että auto ajaa kaarteessa vaakasuoralla tiellä ja ilmanvastus jätetään huomiotta. Silloin autoon vaikuttaa vaakasuunnassa vain tien kitka renkaisiin. Kitka osoittaa siis kohti kaarteen keskipistettä. Narun päässä pyörivässä kivessä keskeisvoiman tuottaa narun jännitysvoima. Karusellissa istujaan sen tuottavat istuimen ja tuen voimat.

<svg data-fig="kaarre" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla kaarteessa oleva auto ylhäältä katsottuna: nopeus osoittaa tien suuntaan ja kiihtyvyys vasemmalle kohti keskipistettä. Oikealla auton voimakuvio takaa katsottuna: paino alas, yhtä pitkä tukivoima ylös ja kitkavoima vasemmalle kohti keskipistettä." style="max-width:100%;font-size:24px">
  <foreignObject x="27.5" y="7.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva ylhäältä}$</div></foreignObject>
  <rect x="12" y="40" width="276" height="320" rx="10" fill="#b2f2bb"/>
  <path d="M145.5,369 L159.5,359.5 L172.5,348.5 L184.5,337 L195.5,324.5 L205.5,311 L214,296.5 L221.5,281.5 L228,266 L232.5,250 L236,233.5 L238.5,217 L239,200 L238.5,183 L236,166.5 L232.5,150 L228,134 L221.5,118.5 L214,103.5 L205.5,89 L195.5,75.5 L184.5,63 L172.5,51.5 L159.5,40.5 L145.5,31 L120,72 L130.5,79 L140.5,87 L149.5,96 L158,105.5 L165.5,116 L172,127 L178,138 L182.5,150 L186,162 L189,174.5 L190.5,187.5 L191,200 L190.5,212.5 L189,225.5 L186,238 L182.5,250 L178,262 L172,273 L165.5,284 L158,294.5 L149.5,304 L140.5,313 L130.5,321 L120,328 Z" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2" stroke-linejoin="round"/>
  <line x1="132.5" y1="348.5" x2="145" y2="340" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="167" y1="320.5" x2="176.5" y2="309.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="193" y1="285" x2="199.5" y2="271.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="209.5" y1="244" x2="212.5" y2="229.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="215" y1="200" x2="214.5" y2="185.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="209.5" y1="156" x2="205" y2="142" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="193" y1="115" x2="185.5" y2="102.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="167" y1="79.5" x2="156.5" y2="69.5" stroke="#ffffff" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="40" cy="200" r="6" fill="#1f2933"/>
  <foreignObject x="44" y="211.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskipiste}$</div></foreignObject>
  <line x1="48" y1="200" x2="189" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="100" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <path d="M204.5,208.5 L204.5,220.5 L199.5,220.5 L199.5,208.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M230.5,208.5 L230.5,220.5 L225.5,220.5 L225.5,208.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M204.5,179.5 L204.5,191.5 L199.5,191.5 L199.5,179.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M230.5,179.5 L230.5,191.5 L225.5,191.5 L225.5,179.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M205,177 L225,177 L227,223 L203,223 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M207,186 L223,186 L223,194.5 L207,194.5 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M207,214 L223,214 L223,208.5 L207,208.5 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="255" y1="234" x2="255" y2="156" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="255" y1="154" x2="248" y2="167" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="255" y1="154" x2="262" y2="167" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="262.5" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="209" y1="254" x2="141" y2="254" stroke="#e8590c" stroke-width="3" stroke-linecap="butt"/>
  <line x1="139" y1="254" x2="152" y2="261" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <line x1="139" y1="254" x2="152" y2="247" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <foreignObject x="132.5" y="265.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="360" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="352.5" y="7.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio takaa}$</div></foreignObject>
  <line x1="360" y1="226" x2="588" y2="226" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="360" y1="226" x2="350" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="226" x2="366" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="392" y1="226" x2="382" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="226" x2="398" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424" y1="226" x2="414" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="226" x2="430" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="456" y1="226" x2="446" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="226" x2="462" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="488" y1="226" x2="478" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="504" y1="226" x2="494" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="226" x2="510" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="536" y1="226" x2="526" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="552" y1="226" x2="542" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="568" y1="226" x2="558" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="584" y1="226" x2="574" y2="238" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="415" y="166" width="110" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="470" y1="196" x2="470" y2="287" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M470,304 L462,286 L478,286 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="477.5" y="283.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="492" y1="226" x2="492" y2="135" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M492,118 L500,136 L484,136 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="499.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="415" y1="226" x2="378" y2="226" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M361,226 L379,218 L379,234 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="332.5" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="440" y1="132" x2="378" y2="132" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M389,125.5 L376,132 L389,138.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="331.5" y="113.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
</svg>

Voimakuviossa auto on piirretty takaa katsottuna, joten kaarteen keskipiste on vasemmalla. Pystysuunnassa auto ei kiihdy. Siksi tukivoima $\overline{N}$ ja paino $\overline{G}$ kumoavat toisensa. Kitkavoima $\overline{F}_\mu$ jää kokonaisvoimaksi. Jos tie on liukas, lepokitka ei riitä tähän. Silloin auto kääntyy vähemmän kuin tie kaartaa ja ajautuu kaarteen ulkoreunalle. Mikään ei silti työnnä autoa ulospäin.

## Kaava: Normaalikiihtyvyys
Kun kappale liikkuu tasaisessa ympyräliikkeessä, sen normaalikiihtyvyyden suuruus on
```latex
a_\text{n} = \frac{v^2}{r}
```
missä $a_\text{n}$ on normaalikiihtyvyys ($\text{m/s}^2$), $v$ ratanopeus ($\text{m/s}$) ja $r$ radan säde ($\text{m}$). Kiihtyvyys kasvaa nopeuden neliön mukana. Kun nopeus kaksinkertaistuu, kiihtyvyys nelinkertaistuu. Samalla nopeudella tiukka kaarre eli pieni säde antaa suuren kiihtyvyyden. Jos tunnetaan kierrosaika $T$, ratanopeus lasketaan ensin kaavalla $v = \tfrac{2\pi r}{T}$.

Miksi juuri nopeuden neliö? Nopeus vaikuttaa kahdesti. Kun nopeus on suurempi, nopeusnuoli on pidempi. Silloin sama suunnan kääntyminen tarkoittaa suurempaa nopeuden muutosta $\Delta\overline{v}$. Lisäksi kappale kiertää kaaren nopeammin. Nopeus kääntyy siis saman kulman lyhyemmässä ajassa. Molemmat tekijät kasvavat nopeuden mukana, joten kiihtyvyys kasvaa nopeuden neliön mukana. Kun nopeus on sama mutta säde pienempi, nopeuden suunta kääntyy nopeammin. Silloin kiihtyvyys on suurempi.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: vaaka-akselilla ratanopeus nollasta 30:een, pystyakselilla normaalikiihtyvyys nollasta 18:aan. Kaksi käyrää nousee yhä jyrkemmin. Säteellä 50 metriä kiihtyvyys on nopeuksilla 10, 20 ja 30 arvoltaan 2, 8 ja 18. Säteellä 100 metriä arvot ovat puolet pienempiä." style="max-width:100%;font-size:24px">
  <line x1="141.5" y1="300" x2="141.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197.5" y1="300" x2="197.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253" y1="300" x2="253" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308.5" y1="300" x2="308.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364.5" y1="300" x2="364.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="260" x2="420" y2="260" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="220" x2="420" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="180" x2="420" y2="180" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="140" x2="420" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="100" x2="420" y2="100" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="85" y1="300" x2="434" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,300 L433,306 L433,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="86" y1="301" x2="86" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M86,34 L92,47 L80,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141.5" y1="300" x2="141.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="131.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="197.5" y1="300" x2="197.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="253" y1="300" x2="253" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="308.5" y1="300" x2="308.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="292" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="364.5" y1="300" x2="364.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="420" y1="300" x2="420" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="79" y1="260" x2="86" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="79" y1="220" x2="86" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="79" y1="180" x2="86" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <line x1="79" y1="140" x2="86" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="79" y1="100" x2="86" y2="100" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="79" y1="60" x2="86" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$18$</div></foreignObject>
  <foreignObject x="56" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\tfrac{\text{m}}{\text{s}})$</div></foreignObject>
  <foreignObject x="76" y="3.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a_\text{n}\ (\tfrac{\text{m}}{\text{s}^2})$</div></foreignObject>
  <polyline points="86,300 89,300 91.5,300 94.5,300 97,299.5 100,299.5 102.5,299.5 105.5,299 108.5,299 111,298.5 114,298.5 116.5,298 119.5,297.5 122,297 125,296.5 128,296 130.5,295.5 133.5,295 136,294.5 139,294 141.5,293.5 144.5,292.5 147,292 150,291 153,290.5 155.5,289.5 158.5,288.5 161,288 164,287 166.5,286 169.5,285 172.5,284 175,283 178,282 180.5,280.5 183.5,279.5 186,278.5 189,277 192,276 194.5,274.5 197.5,273.5 200,272 203,270.5 205.5,269 208.5,267.5 211,266 214,264.5 217,263 219.5,261.5 222.5,260 225,258.5 228,256.5 230.5,255 233.5,253 236.5,251.5 239,249.5 242,247.5 244.5,246 247.5,244 250,242 253,240 256,238 258.5,236 261.5,234 264,231.5 267,229.5 269.5,227.5 272.5,225 275.5,223 278,220.5 281,218.5 283.5,216 286.5,213.5 289,211 292,208.5 295,206 297.5,203.5 300.5,201 303,198.5 306,196 308.5,193.5 311.5,190.5 314,188 317,185 320,182.5 322.5,179.5 325.5,176.5 328,174 331,171 333.5,168 336.5,165 339.5,162 342,159 345,156 347.5,152.5 350.5,149.5 353,146.5 356,143 359,140 361.5,136.5 364.5,133.5 367,130 370,126.5 372.5,123 375.5,119.5 378,116 381,112.5 384,109 386.5,105.5 389.5,102 392,98.5 395,94.5 397.5,91 400.5,87 403.5,83.5 406,79.5 409,75.5 411.5,72 414.5,68 417,64 420,60" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,300 89,300 91.5,300 94.5,300 97,300 100,300 102.5,299.5 105.5,299.5 108.5,299.5 111,299.5 114,299 116.5,299 119.5,299 122,298.5 125,298.5 128,298 130.5,298 133.5,297.5 136,297.5 139,297 141.5,296.5 144.5,296.5 147,296 150,295.5 153,295 155.5,295 158.5,294.5 161,294 164,293.5 166.5,293 169.5,292.5 172.5,292 175,291.5 178,291 180.5,290.5 183.5,290 186,289 189,288.5 192,288 194.5,287.5 197.5,286.5 200,286 203,285.5 205.5,284.5 208.5,284 211,283 214,282.5 217,281.5 219.5,281 222.5,280 225,279 228,278.5 230.5,277.5 233.5,276.5 236.5,275.5 239,275 242,274 244.5,273 247.5,272 250,271 253,270 256,269 258.5,268 261.5,267 264,266 267,265 269.5,263.5 272.5,262.5 275.5,261.5 278,260.5 281,259 283.5,258 286.5,257 289,255.5 292,254.5 295,253 297.5,252 300.5,250.5 303,249.5 306,248 308.5,246.5 311.5,245.5 314,244 317,242.5 320,241 322.5,240 325.5,238.5 328,237 331,235.5 333.5,234 336.5,232.5 339.5,231 342,229.5 345,228 347.5,226.5 350.5,225 353,223 356,221.5 359,220 361.5,218.5 364.5,216.5 367,215 370,213.5 372.5,211.5 375.5,210 378,208 381,206.5 384,204.5 386.5,203 389.5,201 392,199 395,197.5 397.5,195.5 400.5,193.5 403.5,191.5 406,190 409,188 411.5,186 414.5,184 417,182 420,180" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 7"/>
  <line x1="197.5" y1="273.5" x2="197.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="86" y1="273.5" x2="197.5" y2="273.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="197.5" cy="273.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="308.5" y1="193.5" x2="308.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="86" y1="193.5" x2="308.5" y2="193.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="308.5" cy="193.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="45.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$r = 50\,\text{m}$</div></foreignObject>
  <foreignObject x="430" y="165.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$r = 100\,\text{m}$</div></foreignObject>
</svg>

Kuvaajassa säteellä $50\,\text{m}$ normaalikiihtyvyys on nopeudella $10\,\text{m/s}$ vain $2{,}0\,\text{m/s}^2$. Nopeudella $20\,\text{m/s}$ se on jo $8{,}0\,\text{m/s}^2$. Kun säde on kaksinkertainen, $100\,\text{m}$, kiihtyvyys on samalla nopeudella puolet pienempi, $4{,}0\,\text{m/s}^2$.

### Newtonin toinen laki ympyräliikkeessä
Newtonin toisen lain mukaan kappaleeseen vaikuttavien voimien summan suuruus on tasaisessa ympyräliikkeessä
```latex
\Sigma F = m\,\frac{v^2}{r}
```
missä $\Sigma F$ on keskipisteeseen osoittava kokonaisvoima ($\text{N}$) ja $m$ kappaleen massa ($\text{kg}$). Lasku tehdään kuten luvussa *Voimakuvio ja voimien yhteisvaikutus*. Piirrä ensin voimakuvio ja valitse yksi akseli osoittamaan kohti radan keskipistettä. Silloin keskipisteeseen osoittavat voimat ovat positiivisia ja poispäin osoittavat negatiivisia. Niiden summa on $m\tfrac{v^2}{r}$. Kohtisuoraan ratatasoa vastaan kappale ei kiihdy, joten siinä suunnassa voimien summa on nolla.

### Nyppylä ja notko
Kun auto ajaa tasaisella vauhdilla nyppylän huipun yli, se on hetken ympyräradalla. Radan keskipiste on tien alapuolella. Kiihtyvyys osoittaa silloin alas, joten paino on suurempi kuin tien tukivoima: $G - N = m\tfrac{v^2}{r}$. Tukivoima on painoa pienempi, ja matkustaja tuntee itsensä kevyeksi. Mitä suurempi nopeus, sitä pienempi tukivoima. Jos $\tfrac{v^2}{r}$ kasvaa yhtä suureksi kuin $g$, tukivoima on nolla. Jos se kasvaa suuremmaksi kuin $g$, auto irtoaa hetkeksi tiestä.

<svg data-fig="nyppyla" viewBox="0 0 600 420" role="img" aria-label="Neljä kuvaa. Vasemmalla auto nyppylän huipulla, oikealla auto notkon pohjalla, ja alla kummankin voimakuvio. Nyppylän huipulla tukivoima on painoa pienempi ja kiihtyvyys osoittaa alas. Notkon pohjalla tukivoima on painoa suurempi ja kiihtyvyys osoittaa ylös." style="max-width:100%;font-size:24px">
  <foreignObject x="58.5" y="7.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nyppylän huippu}$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{notkon pohja}$</div></foreignObject>
  <path d="M16,132 C80,132 100,84 150,84 C200,84 220,132 284,132 V146 H16 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M114,77 V63.5 Q116,60 126.5,59 L136.5,47 H162.5 L174.5,59 Q186,60 187,69 V77 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M139,51 H149 V58 H133 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M152.5,51 H161 L168,58 H152.5 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="128.5" cy="77" r="8.1" fill="#1f2933"/>
  <circle cx="128.5" cy="77" r="3.15" fill="#c4ccd4"/>
  <circle cx="172.5" cy="77" r="8.1" fill="#1f2933"/>
  <circle cx="172.5" cy="77" r="3.15" fill="#c4ccd4"/>
  <path d="M316,64 C380,64 400,124 450,124 C500,124 520,64 584,64 V146 H316 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M414,117 V103.5 Q416,100 426.5,99 L436.5,87 H462.5 L474.5,99 Q486,100 487,109 V117 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M439,91 H449 V98 H433 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M452.5,91 H461 L468,98 H452.5 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="428.5" cy="117" r="8.1" fill="#1f2933"/>
  <circle cx="428.5" cy="117" r="3.15" fill="#c4ccd4"/>
  <circle cx="472.5" cy="117" r="8.1" fill="#1f2933"/>
  <circle cx="472.5" cy="117" r="3.15" fill="#c4ccd4"/>
  <line x1="300" y1="20" x2="300" y2="410" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="16" y1="156" x2="584" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="60" y1="308" x2="240" y2="308" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="60" y1="308" x2="50" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="76" y1="308" x2="66" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="308" x2="82" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="108" y1="308" x2="98" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="124" y1="308" x2="114" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="308" x2="130" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156" y1="308" x2="146" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="172" y1="308" x2="162" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="308" x2="178" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204" y1="308" x2="194" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="308" x2="210" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="308" x2="226" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="100" y="272" width="100" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="150" y1="290" x2="150" y2="373" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,390 L142,372 L158,372 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="111.5" y="371.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="170" y1="308" x2="170" y2="265" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M170,248 L178,266 L162,266 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="185.5" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="240" y1="234" x2="240" y2="284" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M233.5,273 L240,286 L246.5,273" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="241.5" y="271.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <line x1="360" y1="308" x2="540" y2="308" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="360" y1="308" x2="350" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="308" x2="366" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="392" y1="308" x2="382" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="308" x2="398" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424" y1="308" x2="414" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="308" x2="430" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="456" y1="308" x2="446" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="308" x2="462" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="488" y1="308" x2="478" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="504" y1="308" x2="494" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="308" x2="510" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="536" y1="308" x2="526" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="400" y="272" width="100" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="450" y1="290" x2="450" y2="373" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M450,390 L442,372 L458,372 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="411.5" y="371.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="308" x2="470" y2="185" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M470,168 L478,186 L462,186 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="485.5" y="163.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="540" y1="310" x2="540" y2="260" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M546.5,271 L540,258 L533.5,271" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="541.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
</svg>

Notkon pohjalla keskipiste on tien yläpuolella, ja kiihtyvyys osoittaa ylös. Silloin tukivoiman on oltava painoa suurempi: $N - G = m\tfrac{v^2}{r}$. Siksi vuoristoradan notkossa matkustaja painuu istuinta vasten ja tuntee itsensä raskaaksi. Kummassakin tapauksessa paino on sama $mg$. Vain tukivoima muuttuu niin, että kokonaisvoima osoittaa kohti kaaren keskipistettä.

## Esimerkki
Henkilöauto, jonka massa on $1200\,\text{kg}$, ajaa vaakasuoran tien kaarteessa tasaisella nopeudella $54\,\text{km/h}$. Kaarteen säde on $45\,\text{m}$. Kuinka suuri kitkavoima tien on kohdistettava autoon? Kuinka suuri renkaiden ja tien välisen lepokitkakertoimen on vähintään oltava? Ilmanvastus ja vierimisvastus jätetään huomiotta. Renkaiden voimat lasketaan yhteen.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 1200\,\text{kg}$, $v = 54\,\text{km/h}$, $r = 45\,\text{m}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään tien kitkavoimaa $F_\mu$ ja pienintä lepokitkakerrointa $\mu_0$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi auto. Siihen vaikuttavat Maa (paino $\overline{G}$) ja tie (tukivoima $\overline{N}$ ja kitka $\overline{F}_\mu$). Auto on tasaisessa ympyräliikkeessä. Newtonin toisen lain mukaan kokonaisvoima osoittaa siis kohti kaarteen keskipistettä, ja sen suuruus on $m\tfrac{v^2}{r}$. Ainoa vaakasuora voima on kitka, joten se osoittaa kohti keskipistettä. Renkaat eivät liu'u sivuttain, joten kitka on lepokitkaa. Lepokitka on enintään $\mu_0 N$. Voimakuviossa auto on takaa katsottuna ja kaarteen keskipiste on oikealla. $x$-akseli osoittaa kohti keskipistettä ja $y$-akseli ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Auton voimakuvio takaa katsottuna. Kaarteen keskipiste on oikealla. Paino alas, yhtä pitkä tukivoima ylös ja kitkavoima oikealle kohti keskipistettä, noin puolet painon pituudesta. Akselit: x oikealle ja y ylös." style="max-width:100%;font-size:24px">
  <line x1="80" y1="208" x2="440" y2="208" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="80" y1="208" x2="70" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="208" x2="86" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="112" y1="208" x2="102" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="128" y1="208" x2="118" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="144" y1="208" x2="134" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="160" y1="208" x2="150" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="176" y1="208" x2="166" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192" y1="208" x2="182" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="208" y1="208" x2="198" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="208" x2="214" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="208" x2="230" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="208" x2="246" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272" y1="208" x2="262" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="208" x2="278" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="208" x2="294" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="208" x2="310" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="208" x2="326" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="208" x2="342" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368" y1="208" x2="358" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="208" x2="374" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="208" x2="390" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="208" x2="406" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432" y1="208" x2="422" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="195" y="132" width="150" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="170" x2="270" y2="283" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,300 L262,282 L278,282 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="279.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="246" y1="208" x2="246" y2="95" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M246,78 L254,96 L238,96 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="203.5" y="71.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="345" y1="208" x2="394.5" y2="208" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M411.5,208 L393.5,216 L393.5,200 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="393" y="217.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="310" y1="90" x2="378" y2="90" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M367,96.5 L380,90 L367,83.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="71.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="347" y="25.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kohti keskipistettä}$</div></foreignObject>
  <line x1="52" y1="318" x2="87" y2="318" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M96,318 L86,322.5 L86,313.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="52" y1="318" x2="52" y2="283" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M52,274 L56.5,284 L47.5,284 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="100" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="42" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt, ja kysytyt suureet ratkaistaan:
```latex
\begin{aligned}
&x\text{:}\ \ F_\mu = m\frac{v^2}{r} \\
&y\text{:}\ \ N - mg = 0 \\
&F_\mu \le \mu_0 N = \mu_0 mg \\
&\mu_0 \ge \frac{v^2}{gr}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeus muutetaan yksikköön $\text{m/s}$: $v = 54\,\text{km/h} = \tfrac{54\cdot 1000\,\text{m}}{3600\,\text{s}} = 15\,\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&F_\mu = m\frac{v^2}{r} \\
&\phantom{F_\mu} = 1200\,\text{kg}\cdot\frac{(15\,\text{m/s})^2}{45\,\text{m}} \\
&\phantom{F_\mu} = 6000\,\text{N} \\[4pt]
&\mu_0 \ge \frac{v^2}{gr} \\
&\phantom{\mu_0} = \frac{(15\,\text{m/s})^2}{9{,}81\,\text{m/s}^2\cdot 45\,\text{m}} \\
&\phantom{\mu_0} \approx 0{,}510
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Tien kitkavoima on $F_\mu \approx 6{,}0\,\text{kN}$ kohti kaarteen keskipistettä. Lepokitkakertoimen on oltava vähintään $0{,}51$. Tuloksessa on kaksi merkitsevää numeroa, kuten nopeudessa $54\,\text{km/h}$ ja säteessä $45\,\text{m}$.

<!-- vaihe -->

**Järkevyys.** Normaalikiihtyvyys on $a_\text{n} = \tfrac{(15\,\text{m/s})^2}{45\,\text{m}} = 5{,}0\,\text{m/s}^2$. Se on noin puolet putoamiskiihtyvyydestä, joten kitkan on oltava noin puolet painosta $11{,}8\,\text{kN}$. Kuivalla asfaltilla lepokitkakerroin on noin $0{,}8$, joten auto pysyy kaarteessa. Märällä asfaltilla kerroin voi olla noin $0{,}5$. Silloin pito on rajoilla. Jäällä pito pettäisi. Massa supistuu, joten kertoimen vaatimus on sama kevyelle ja raskaalle autolle.

## Yleinen virhekäsitys
Moni ajattelee, että ympyräliikkeessä kappaleeseen vaikuttaa ulospäin **keskipakoisvoima**. Sen luullaan pitävän kappaleen radalla tai heittävän sen ulos kaarteesta. Sellaista voimaa ei ole. Mikään kappale ei vedä tai työnnä autoa tai matkustajaa ulospäin. Kun auto kääntyy, matkustajan keho pyrkii jatkamaan suoraan. Ovi painuu häntä vasten ja työntää häntä sisäänpäin, kohti kaarteen keskipistettä. Tämä tuntuu painautumisena ulospäin. Kun pito pettää, auto ei lennä säteen suuntaan ulos. Se jatkaa suoremmin kuin tie kaartaa. Toinen virhe on piirtää keskeisvoima voimakuvioon omaksi nuolekseen. Keskeisvoima on todellisten voimien, kuten kitkan tai jännitysvoiman, summa.

## Tiivistelmä
- Tasaisessa ympyräliikkeessä ratanopeus on vakio, mutta nopeuden suunta muuttuu. Siksi kappale kiihtyy.
- Normaalikiihtyvyys eli keskeiskiihtyvyys osoittaa kohti radan keskipistettä. Sen suuruus on $a_\text{n} = \tfrac{v^2}{r}$.
- Kappaleeseen vaikuttavien voimien summa eli keskeisvoima osoittaa kohti keskipistettä: $\Sigma F = m\tfrac{v^2}{r}$. Se on todellisten voimien summa, ei oma voimansa.
- Kaarteessa keskeisvoiman antaa tien kitka ja narussa jännitysvoima. Nyppylän huipulla tukivoima on painoa pienempi, notkon pohjalla suurempi.
- Keskipakoisvoimaa ei ole. Kun keskipisteeseen osoittava voima ei riitä, kappale jatkaa suoremmin kuin rata kaartaa.
