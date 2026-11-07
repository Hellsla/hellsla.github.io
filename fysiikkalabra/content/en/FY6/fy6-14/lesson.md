# Semiconductors, the diode, the LED and the solar cell

> **Why** does an LED light up only when it is connected one way round, and why must the current of an LED be limited, although a light bulb can be connected straight to a battery?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a school workbench there is a breadboard. On the left is a battery holder with three AA batteries, from which a red and a black wire run to the breadboard. On the board there is a resistor and two red LEDs. The first LED shines brightly; the second, identical LED is connected the other way round and does not light. In the background, outside a window, the sun is shining, and on the windowsill there is a small solar panel." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy614h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy614h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy614h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy614h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy614h-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="0.25" stop-color="#f2a69c" stop-opacity="0.75"/><stop offset="1" stop-color="#f2a69c" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy614h-wall)"/>
  <rect x="840" y="48" width="300" height="250" rx="6" fill="url(#fy614h-sky)" stroke="#1f2933" stroke-width="4"/>
  <circle cx="1050" cy="126" r="61" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1093.5,145 L1114,143 L1097.5,131.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1078.5,164.5 L1097,173 L1088.5,154.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1055.5,173.5 L1067,190 L1069,169.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1031,169.5 L1033,190 L1044.5,173.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1011.5,154.5 L1003,173 L1021.5,164.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1002.5,131.5 L986,143 L1006.5,145 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1006.5,107 L986,109 L1002.5,120.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1021.5,87.5 L1003,79 L1011.5,97.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1044.5,78.5 L1033,62 L1031,82.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1069,82.5 L1067,62 L1055.5,78.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1088.5,97.5 L1097,79 L1078.5,87.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1097.5,120.5 L1114,109 L1093.5,107 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1050" cy="126" r="38" fill="url(#fy614h-sun)"/>
  <line x1="990" y1="48" x2="990" y2="298" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <rect x="820" y="296" width="340" height="18" rx="3" fill="#e9c98a" stroke="#1f2933" stroke-width="3"/>
  <path d="M866,294 L896,236 L980,236 L950,294 Z" fill="#1f2933" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M872,288 L884,264 L906,264 L894,288 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <path d="M887,260 L899,236 L921,236 L909,260 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <path d="M898,288 L910,264 L932,264 L920,288 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <path d="M913,260 L925,236 L947,236 L935,260 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <path d="M924,288 L936,264 L958,264 L946,288 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <path d="M939,260 L951,236 L973,236 L961,260 Z" fill="#2f74b5" stroke-linejoin="round"/>
  <rect x="0" y="380" width="1200" height="220" fill="url(#fy614h-table)"/>
  <rect x="0" y="374" width="1200" height="12" fill="#a97a35"/>
  <path d="M0,430 C340,424 780,438 1200,428" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,474 C340,468 780,482 1200,472" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,518 C340,512 780,526 1200,516" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <path d="M0,562 C340,556 780,570 1200,560" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.35"/>
  <rect x="118" y="420" width="236" height="104" rx="10" fill="#1f2933"/>
  <rect x="132" y="432" width="196" height="24" rx="6" fill="#2b8a3e"/>
  <rect x="328" y="438" width="12" height="12" rx="2" fill="#c4ccd4"/>
  <rect x="132" y="460" width="196" height="24" rx="6" fill="#2b8a3e"/>
  <rect x="328" y="466" width="12" height="12" rx="2" fill="#c4ccd4"/>
  <rect x="132" y="488" width="196" height="24" rx="6" fill="#2b8a3e"/>
  <rect x="328" y="494" width="12" height="12" rx="2" fill="#c4ccd4"/>
  <rect x="420" y="420" width="400" height="140" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="436" y1="438" x2="804" y2="438" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="436" y1="542" x2="804" y2="542" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="430" y="486" width="380" height="8" fill="#e3dccb"/>
  <circle cx="444" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="444" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="460" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="476" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="492" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="508" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="524" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="540" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="556" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="572" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="588" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="604" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="620" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="636" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="652" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="668" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="684" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="700" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="716" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="732" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="748" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="764" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="780" cy="543" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="454" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="504" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="467" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="517" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="480" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="530" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="493" r="2.6" fill="#c9c2b2"/>
  <circle cx="796" cy="543" r="2.6" fill="#c9c2b2"/>
  <path d="M354,444 C392,444 400,438 444,438" fill="none" stroke="#c92a2a" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M354,500 C392,500 400,542 444,542" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="476" y1="454" x2="476" y2="420" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <line x1="556" y1="454" x2="556" y2="420" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <path d="M476,420 C476,396 496,392 516,392 C536,392 556,396 556,420" fill="none" stroke="#c4ccd4" stroke-width="4" stroke-linejoin="round"/>
  <rect x="490" y="380" width="52" height="26" rx="12" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="498" y="381" width="5" height="24" fill="#e8590c"/>
  <rect x="508" y="381" width="5" height="24" fill="#e8590c"/>
  <rect x="518" y="381" width="5" height="24" fill="#b8622d"/>
  <rect x="528" y="381" width="5" height="24" fill="#6c757d"/>
  <circle cx="636" cy="352" r="120" fill="url(#fy614h-glow)"/>
  <line x1="626" y1="452" x2="626" y2="380" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <line x1="646" y1="452" x2="646" y2="380" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <path d="M614,384 L614,352 A22,22 0 0 1 658,352 L658,384 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="608" y="380" width="56" height="10" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <circle cx="628" cy="348" r="7" fill="#ffffff"/>
  <line x1="736" y1="452" x2="736" y2="380" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <line x1="756" y1="452" x2="756" y2="380" stroke="#c4ccd4" stroke-width="4" stroke-linecap="butt"/>
  <path d="M724,384 L724,352 A22,22 0 0 1 768,352 L768,384 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="718" y="380" width="56" height="10" rx="2" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <path d="M444,438 L444,420 C444,404 460,404 476,420" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M556,420 C580,440 600,440 626,452" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M646,452 L646,520 L646,542" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M756,452 L756,438" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M736,452 L736,542" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

## Key idea

### Semiconductors lie between conductors and insulators
Metals conduct electricity well, and insulators, such as plastic and glass, hardly at all. A **semiconductor**, for example silicon, lies between them. Its ability to conduct electricity can be changed by adding very small amounts of other substances to it, and it also depends on temperature and light. Semiconductors are used to make electronic components: diodes, LEDs, solar cells, and the transistors of phones and computers. In this chapter semiconductors are studied as components: what they do in an electric circuit and how their voltage and current depend on each other.

### A diode lets current through in one direction only
A **diode** has two different layers of semiconductor, and the boundary between them lets current through in one direction only. The symbol of a diode is a triangle and a bar: the triangle points in the direction in which the current can flow. The terminal on the side of the triangle is the **anode** and the terminal on the side of the bar is the **cathode**, which is usually marked on the component with a ring.

When the anode is connected to the side of the positive terminal of the source, the diode is in the **forward direction**, and current flows. When the diode is turned round, it is in the **reverse direction**: practically no current flows, and the whole voltage of the source is across the diode, as long as the voltage stays below the breakdown voltage of the diode. This is why an LED lights up only when it is connected the right way round. The metal wire of a light bulb conducts in both directions, so a bulb lights up either way round. The resistance of the wire of a bulb grows as it heats up, so the bulb limits its own current.

<svg data-fig="suunnat" viewBox="0 0 600 352" role="img" aria-label="Two circuit diagrams side by side, not to scale. In each, a voltage source U, a series resistor R and a red LED are in series, and the positive terminal of the source is at the top. On the left the triangle of the LED points downwards, in the direction of the current: the anode of the LED is above, towards the positive terminal of the source, and the cathode, the bar, below. The LED shines, and purple arrows show the current I flowing from the positive terminal through the resistor and the LED to the negative terminal. This is the forward direction. On the right the same LED has been turned round, and the triangle points upwards. The LED does not shine, and no current flows in the circuit: I = 0. This is the reverse direction." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy614-glow1" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c92a2a" stop-opacity="0.55"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0"/></radialGradient></defs>
  <polyline points="60,171 60,70 238,70 238,163" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="238,193 238,286 60,286 60,185" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="36" y1="171" x2="84" y2="171" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="48" y1="185" x2="72" y2="185" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="-2" y="163.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="90" y="141.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <rect x="119" y="58" width="60" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="134" y="25.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="238" cy="178" r="46" fill="url(#fy614-glow1)"/>
  <path d="M222,164 L254,164 L238,192 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="221" y1="192" x2="255" y2="192" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="260" y1="169" x2="272" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M278,154 L273.5,163 L268.5,156.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="260" y1="181" x2="272" y2="171" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M278,166 L273.5,175 L268.5,168.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M114,70 L94,62 L94,78 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="92" y="27.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <path d="M238,250 L230,230 L246,230 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M139,286 L159,278 L159,294 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="128" y="141.5" width="84" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{anode}$</div></foreignObject>
  <foreignObject x="122" y="187.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{cathode}$</div></foreignObject>
  <foreignObject x="54" y="315.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{forward direction}$</div></foreignObject>
  <line x1="300" y1="24" x2="300" y2="340" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <polyline points="360,171 360,70 538,70 538,163" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="538,193 538,286 360,286 360,185" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="336" y1="171" x2="384" y2="171" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="348" y1="185" x2="372" y2="185" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="298" y="163.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="390" y="141.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <rect x="419" y="58" width="60" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="434" y="25.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <path d="M522,192 L554,192 L538,164 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="521" y1="164" x2="555" y2="164" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="560" y1="169" x2="572" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M578,154 L573.5,163 L568.5,156.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="560" y1="181" x2="572" y2="171" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M578,166 L573.5,175 L568.5,168.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="414" y="163.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = 0$</div></foreignObject>
  <foreignObject x="369" y="315.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{reverse direction}$</div></foreignObject>
</svg>

### The threshold voltage and the characteristic curve
A diode does not obey Ohm's law. Even in the forward direction the current is almost zero until the voltage of the diode reaches the **threshold voltage**. After that a small increase in voltage increases the current a lot. The threshold voltage of a silicon diode is about $0.6$–$0.7\,\text{V}$.

The characteristic curve of a diode is usually drawn with the voltage $U_\text{D}$ on the horizontal axis and the current $I$ on the vertical axis, the other way round than in the chapter *Resistance and Ohm's law*. From such a $(U, I)$ graph you can see directly at which voltage the current starts to flow. A negative voltage on the graph means the reverse direction, and there the current is zero.

<svg data-fig="ominaiskayra" viewBox="0 0 600 360" role="img" aria-label="Graph to scale, calculated with the diode model of the chapter: the current I of a diode in milliamperes as a function of its voltage U_D in volts, the voltage ranging from −2 V to 4 V and the current from 0 to 30 mA. At negative voltages, that is, in the reverse direction, the current is zero for all three components. In the forward direction the current of the silicon diode stays almost zero up to about 0.6 volts and then rises steeply, and a current of 10 milliamperes is reached at 0.70 volts. The curve of the red LED rises steeply from about 1.8 volts, and 10 mA is reached at 1.9 volts. The curve of the blue LED rises from about 2.8 volts, and 10 mA is reached at 2.9 volts. The grid spacings are 1 V and 5 mA." style="max-width:100%;font-size:24px">
  <line x1="158.5" y1="300" x2="158.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="300" x2="220.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="300" x2="283" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="300" x2="345.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407.5" y1="300" x2="407.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="300" x2="470" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="261" x2="470" y2="261" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="222" x2="470" y2="222" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183" x2="470" y2="183" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="144" x2="470" y2="144" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="105" x2="470" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="66" x2="470" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,40 L102,53 L90,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="158.5" y1="300" x2="158.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="142" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-1$</div></foreignObject>
  <line x1="220.5" y1="300" x2="220.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="210.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="283" y1="300" x2="283" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="345.5" y1="300" x2="345.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="335.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="407.5" y1="300" x2="407.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="470" y1="300" x2="470" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="261" x2="96" y2="261" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="246.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="222" x2="96" y2="222" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="207.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="183" x2="96" y2="183" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="168.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="144" x2="96" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="129.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="105" x2="96" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="90.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="89" y1="66" x2="96" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{D}\ (\text{V})$</div></foreignObject>
  <foreignObject x="86" y="9.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <foreignObject x="79.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-2$</div></foreignObject>
  <polyline points="96,300 220.5,300" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="220.5,300 221,300 221,300 221.5,300 221.5,300 222,300 222,300 222.5,300 222.5,300 223,300 223,300 223,300 223.5,300 223.5,300 224,300 224,300 224.5,300 224.5,300 225,300 225,300 225.5,300 225.5,300 226,300 226,300 226,300 226.5,300 226.5,300 227,300 227,300 227.5,300 227.5,300 228,300 228,300 228.5,300 228.5,300 229,300 229,300 229,300 229.5,300 229.5,300 230,300 230,300 230.5,300 230.5,300 231,300 231,300 231.5,300 231.5,300 232,300 232,300 232.5,300 232.5,300 232.5,300 233,300 233,300 233.5,300 233.5,300 234,300 234,300 234.5,300 234.5,300 235,300 235,300 235.5,300 235.5,300 235.5,300 236,300 236,300 236.5,300 236.5,300 237,300 237,300 237.5,300 237.5,300 238,300 238,300 238.5,300 238.5,300 239,300 239,300 239,300 239.5,300 239.5,300 240,300 240,300 240.5,300 240.5,300 241,300 241,300 241.5,300 241.5,300 242,300 242,300 242,300 242.5,300 242.5,300 243,300 243,300 243.5,300 243.5,300 244,300 244,300 244.5,300 244.5,300 245,300 245,300 245,300 245.5,300 245.5,300 246,300 246,300 246.5,300 246.5,300 247,300 247,300 247.5,300 247.5,300 248,300 248,300 248.5,300 248.5,300 248.5,300 249,300 249,300 249.5,300 249.5,300 250,300 250,299.5 250.5,299.5 250.5,299.5 251,299.5 251,299.5 251.5,299.5 251.5,299.5 251.5,299.5 252,299.5 252,299.5 252.5,299.5 252.5,299.5 253,299 253,299 253.5,299 253.5,299 254,299 254,298.5 254.5,298.5 254.5,298.5 255,298.5 255,298 255,298 255.5,298 255.5,297.5 256,297.5 256,297 256.5,297 256.5,296.5 257,296 257,295.5 257.5,295.5 257.5,295 258,294.5 258,294 258,293 258.5,292.5 258.5,292 259,291 259,290 259.5,289 259.5,288 260,287 260,285.5 260.5,284 260.5,282.5 261,281 261,279 261,277 261.5,275 261.5,272.5 262,270 262,267 262.5,263.5 262.5,260 263,256 263,252 263.5,247 263.5,242 264,236.5 264,230 264.5,223.5 264.5,216 264.5,207.5 265,198.5 265,189 265.5,178 265.5,166 266,153 266,138.5 266.5,123 266.5,105.5 267,87 267,66" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="220.5,300 221.5,300 222,300 222.5,300 223,300 223.5,300 224.5,300 225,300 225.5,300 226,300 227,300 227.5,300 228,300 228.5,300 229,300 230,300 230.5,300 231,300 231.5,300 232,300 233,300 233.5,300 234,300 234.5,300 235.5,300 236,300 236.5,300 237,300 237.5,300 238.5,300 239,300 239.5,300 240,300 241,300 241.5,300 242,300 242.5,300 243,300 244,300 244.5,300 245,300 245.5,300 246.5,300 247,300 247.5,300 248,300 248.5,300 249.5,300 250,300 250.5,300 251,300 251.5,300 252.5,300 253,300 253.5,300 254,300 255,300 255.5,300 256,300 256.5,300 257,300 258,300 258.5,300 259,300 259.5,300 260.5,300 261,300 261.5,300 262,300 262.5,300 263.5,300 264,300 264.5,300 265,300 266,300 266.5,300 267,300 267.5,300 268,300 269,300 269.5,300 270,300 270.5,300 271,300 272,300 272.5,300 273,300 273.5,300 274.5,300 275,300 275.5,300 276,300 276.5,300 277.5,300 278,300 278.5,300 279,300 280,300 280.5,300 281,300 281.5,300 282,300 283,300 283.5,300 284,300 284.5,300 285.5,300 286,300 286.5,300 287,300 287.5,300 288.5,300 289,300 289.5,300 290,300 290.5,300 291.5,300 292,300 292.5,300 293,300 294,300 294.5,300 295,300 295.5,300 296,300 297,300 297.5,300 298,300 298.5,300 299.5,300 300,300 300.5,300 301,300 301.5,300 302.5,300 303,300 303.5,300 304,300 304.5,300 305.5,300 306,300 306.5,300 307,300 308,300 308.5,300 309,300 309.5,300 310,300 311,300 311.5,300 312,300 312.5,300 313.5,300 314,300 314.5,300 315,300 315.5,300 316.5,300 317,300 317.5,300 318,300 319,300 319.5,300 320,300 320.5,300 321,300 322,299.5 322.5,299.5 323,299.5 323.5,299.5 324,299.5 325,299 325.5,299 326,299 326.5,298.5 327.5,298 328,298 328.5,297.5 329,297 329.5,296 330.5,295.5 331,294.5 331.5,293 332,291.5 333,289.5 333.5,287.5 334,285 334.5,281.5 335,277.5 336,273 336.5,267 337,259.5 337.5,251 338.5,240.5 339,227.5 339.5,212 340,193 340.5,170 341.5,141.5 342,107.5 342.5,66" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="220.5,300 221.5,300 222.5,300 223.5,300 224.5,300 225.5,300 226,300 227,300 228,300 229,300 230,300 231,300 232,300 232.5,300 233.5,300 234.5,300 235.5,300 236.5,300 237.5,300 238,300 239,300 240,300 241,300 242,300 243,300 244,300 244.5,300 245.5,300 246.5,300 247.5,300 248.5,300 249.5,300 250,300 251,300 252,300 253,300 254,300 255,300 256,300 256.5,300 257.5,300 258.5,300 259.5,300 260.5,300 261.5,300 262.5,300 263,300 264,300 265,300 266,300 267,300 268,300 268.5,300 269.5,300 270.5,300 271.5,300 272.5,300 273.5,300 274.5,300 275,300 276,300 277,300 278,300 279,300 280,300 281,300 281.5,300 282.5,300 283.5,300 284.5,300 285.5,300 286.5,300 287,300 288,300 289,300 290,300 291,300 292,300 293,300 293.5,300 294.5,300 295.5,300 296.5,300 297.5,300 298.5,300 299,300 300,300 301,300 302,300 303,300 304,300 305,300 305.5,300 306.5,300 307.5,300 308.5,300 309.5,300 310.5,300 311.5,300 312,300 313,300 314,300 315,300 316,300 317,300 317.5,300 318.5,300 319.5,300 320.5,300 321.5,300 322.5,300 323.5,300 324,300 325,300 326,300 327,300 328,300 329,300 329.5,300 330.5,300 331.5,300 332.5,300 333.5,300 334.5,300 335.5,300 336,300 337,300 338,300 339,300 340,300 341,300 342,300 342.5,300 343.5,300 344.5,300 345.5,300 346.5,300 347.5,300 348,300 349,300 350,300 351,300 352,300 353,300 354,300 354.5,300 355.5,300 356.5,300 357.5,300 358.5,300 359.5,300 360,300 361,300 362,300 363,300 364,300 365,300 366,300 366.5,300 367.5,300 368.5,300 369.5,300 370.5,300 371.5,300 372.5,300 373,300 374,300 375,300 376,300 377,300 378,300 378.5,300 379.5,300 380.5,299.5 381.5,299.5 382.5,299.5 383.5,299.5 384.5,299 385,299 386,298.5 387,298.5 388,298 389,297.5 390,296.5 391,295.5 391.5,294.5 392.5,292.5 393.5,290.5 394.5,288 395.5,284.5 396.5,280 397,274.5 398,267.5 399,258.5 400,247 401,232 402,213 403,188.5 403.5,157.5 404.5,117 405.5,66" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="108" y1="84" x2="136" y2="84" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="144" y="69.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{silicon diode}$</div></foreignObject>
  <line x1="108" y1="120" x2="136" y2="120" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="144" y="105.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{red LED}$</div></foreignObject>
  <line x1="108" y1="156" x2="136" y2="156" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="144" y="141.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{blue LED}$</div></foreignObject>
  <foreignObject x="123.5" y="263.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I = 0$</span></div></foreignObject>
</svg>

### An LED changes electrical energy into light
An **LED**, a light-emitting diode, is a diode that emits light when current flows through it in the forward direction. The colour of the light depends on the semiconductor material of the LED, and the colour shows also in the threshold voltage. When the current is a few milliamperes, the voltage of a red LED is about $1.8$–$2.0\,\text{V}$, of a green one about $2.2\,\text{V}$ and of a blue or white one about $2.9$–$3.3\,\text{V}$. An LED changes a greater part of the electrical energy into light than a light bulb, in which most of the electrical energy becomes internal energy of the wire and is transferred to the surroundings as heat.

### Why an LED needs a series resistor
When an LED is lit, its voltage changes only a little although the current changes a lot. If an LED were connected straight to a $4.5\,\text{V}$ battery, almost the whole $4.5\,\text{V}$ would be across the LED, which is clearly above its threshold voltage. Only the internal resistance of the battery and the wires would limit the current, so the current would grow so large that the LED would overheat and break. This is why the current of an LED must be limited with a suitable circuit. In a simple LED circuit connected to a constant-voltage source this is done with a **series resistor** connected in series. The part of the voltage of the source that is not across the LED is left across the resistor, and the resistor determines the current. In other LED devices the current can be controlled, for example, with a constant-current driver. The resistance of the wire of a light bulb grows as the wire heats up, so a bulb limits its own current.

### A solar cell is a direct-voltage source
A **solar cell** is a large semiconductor component that produces electric current in light. The light brings energy to the cell, and the cell separates charges so that a voltage appears between its terminals. The cell has a positive and a negative terminal, and like a battery it gives direct current: in the external circuit the current always flows from the positive terminal to the negative terminal. One silicon cell gives only about $0.5$–$0.6\,\text{V}$, so a solar panel has many cells in series. A cell does not store energy: in the dark it gives no current, so a solar lamp also has a battery.

The $(U, I)$ graph of a cell is not a falling straight line like that of a battery (chapter *Electromotive force and internal resistance*). When the terminals are connected with a conductor, the **short-circuit current** $I_\text{sc}$ flows, and it is directly proportional to the radiant power incident on the cell per unit area, that is, the **irradiance** $G$. When no current is drawn, there is an **open-circuit voltage** $U_\text{oc}$ between the terminals, and it changes only a little with the light. Between these the current stays almost constant at first and then falls steeply. The small panel in the figure has ten cells in series.

<svg data-fig="kenno" viewBox="0 0 600 360" role="img" aria-label="Graph to scale, calculated with the solar panel model of the chapter: the current I of a small solar panel in milliamperes as a function of its voltage U in volts at two irradiances. When the irradiance G is 1000 W/m², the curve starts on the vertical axis at the short-circuit current I_sc = 200 mA, stays almost horizontal up to about four volts and then falls steeply to the horizontal axis at the open-circuit voltage U_oc = 6.0 V. When the irradiance is 500 W/m², the short-circuit current is half, 100 mA, but the open-circuit voltage is 5.7 V, only a little smaller. The grid spacings are 1 V and 50 mA." style="max-width:100%;font-size:24px">
  <line x1="150.5" y1="300" x2="150.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204.5" y1="300" x2="204.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="300" x2="259" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="300" x2="313" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367.5" y1="300" x2="367.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="421.5" y1="300" x2="421.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="300" x2="476" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="252" x2="476" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="204" x2="476" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="156" x2="476" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="108" x2="476" y2="108" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="476" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="490" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,300 L489,306 L489,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150.5" y1="300" x2="150.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="204.5" y1="300" x2="204.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="194.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="259" y1="300" x2="259" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="249" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="313" y1="300" x2="313" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="367.5" y1="300" x2="367.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="421.5" y1="300" x2="421.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="411.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="476" y1="300" x2="476" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="466" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="237.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="204" x2="96" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="189.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="156" x2="96" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="108" x2="96" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="93.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <polyline points="96,108 97.5,108 99.5,108 101,108 102.5,108 104,108 106,108 107.5,108 109,108 110.5,108 112.5,108 114,108 115.5,108 117,108 119,108 120.5,108 122,108 123.5,108 125.5,108 127,108 128.5,108 130,108 132,108 133.5,108 135,108 136.5,108 138.5,108 140,108 141.5,108 143,108 145,108 146.5,108 148,108 149.5,108 151.5,108 153,108 154.5,108 156.5,108 158,108 159.5,108 161,108 163,108 164.5,108 166,108 167.5,108 169.5,108 171,108 172.5,108 174,108 176,108 177.5,108 179,108 180.5,108 182.5,108 184,108 185.5,108 187,108 189,108 190.5,108 192,108 193.5,108 195.5,108 197,108 198.5,108 200,108 202,108 203.5,108 205,108 206.5,108 208.5,108 210,108 211.5,108 213.5,108 215,108 216.5,108 218,108 220,108 221.5,108 223,108 224.5,108 226.5,108 228,108 229.5,108 231,108 233,108 234.5,108 236,108 237.5,108 239.5,108 241,108 242.5,108 244,108 246,108 247.5,108 249,108 250.5,108 252.5,108 254,108 255.5,108 257,108 259,108 260.5,108 262,108 263.5,108 265.5,108 267,108 268.5,108 270.5,108 272,108 273.5,108 275,108 277,108 278.5,108.5 280,108.5 281.5,108.5 283.5,108.5 285,108.5 286.5,108.5 288,108.5 290,108.5 291.5,108.5 293,108.5 294.5,108.5 296.5,108.5 298,108.5 299.5,108.5 301,108.5 303,109 304.5,109 306,109 307.5,109 309.5,109 311,109 312.5,109.5 314,109.5 316,109.5 317.5,109.5 319,109.5 320.5,110 322.5,110 324,110 325.5,110.5 327.5,110.5 329,110.5 330.5,111 332,111 334,111.5 335.5,111.5 337,112 338.5,112 340.5,112.5 342,113 343.5,113 345,113.5 347,114 348.5,114.5 350,115 351.5,115.5 353.5,116 355,117 356.5,117.5 358,118.5 360,119 361.5,120 363,121 364.5,122 366.5,123 368,124 369.5,125.5 371,127 373,128 374.5,130 376,131.5 377.5,133.5 379.5,135.5 381,137.5 382.5,139.5 384.5,142 386,145 387.5,147.5 389,151 391,154 392.5,158 394,161.5 395.5,166 397.5,170.5 399,175 400.5,180.5 402,186 404,192 405.5,198.5 407,206 408.5,213.5 410.5,221.5 412,230.5 413.5,240 415,250 417,261.5 418.5,273.5 420,286 421.5,300" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="96" cy="108" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="421.5" cy="300" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <polyline points="96,204 97.5,204 99,204 100.5,204 102,204 104,204 105.5,204 107,204 108.5,204 110,204 111.5,204 113,204 114.5,204 116,204 117.5,204 119.5,204 121,204 122.5,204 124,204 125.5,204 127,204 128.5,204 130,204 131.5,204 133.5,204 135,204 136.5,204 138,204 139.5,204 141,204 142.5,204 144,204 145.5,204 147.5,204 149,204 150.5,204 152,204 153.5,204 155,204 156.5,204 158,204 159.5,204 161,204 163,204 164.5,204 166,204 167.5,204 169,204 170.5,204 172,204 173.5,204 175,204 177,204 178.5,204 180,204 181.5,204 183,204 184.5,204 186,204 187.5,204 189,204 191,204 192.5,204 194,204 195.5,204 197,204 198.5,204 200,204 201.5,204 203,204 204.5,204 206.5,204 208,204 209.5,204 211,204 212.5,204 214,204 215.5,204 217,204 218.5,204 220.5,204 222,204 223.5,204 225,204 226.5,204 228,204 229.5,204 231,204 232.5,204 234,204 236,204 237.5,204 239,204 240.5,204 242,204 243.5,204 245,204 246.5,204 248,204 250,204 251.5,204 253,204 254.5,204 256,204 257.5,204 259,204 260.5,204 262,204 264,204 265.5,204 267,204 268.5,204 270,204 271.5,204 273,204 274.5,204 276,204 277.5,204.5 279.5,204.5 281,204.5 282.5,204.5 284,204.5 285.5,204.5 287,204.5 288.5,204.5 290,204.5 291.5,204.5 293.5,204.5 295,204.5 296.5,204.5 298,204.5 299.5,204.5 301,204.5 302.5,205 304,205 305.5,205 307.5,205 309,205 310.5,205 312,205 313.5,205.5 315,205.5 316.5,205.5 318,205.5 319.5,205.5 321,206 323,206 324.5,206 326,206.5 327.5,206.5 329,206.5 330.5,207 332,207 333.5,207.5 335,207.5 337,208 338.5,208 340,208.5 341.5,209 343,209 344.5,209.5 346,210 347.5,210.5 349,211 350.5,211.5 352.5,212 354,212.5 355.5,213 357,213.5 358.5,214.5 360,215 361.5,216 363,217 364.5,218 366.5,219 368,220 369.5,221 371,222.5 372.5,224 374,225.5 375.5,227 377,228.5 378.5,230.5 380.5,232.5 382,234.5 383.5,237 385,239.5 386.5,242 388,244.5 389.5,247.5 391,251 392.5,254.5 394,258 396,262 397.5,266.5 399,271 400.5,276 402,281.5 403.5,287 405,293.5 406.5,300" fill="none" stroke="#4f8fbf" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 7"/>
  <circle cx="96" cy="204" r="6" fill="#6b7480" stroke="#ffffff" stroke-width="2"/>
  <circle cx="406.5" cy="300" r="6" fill="#6b7480" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="161" y="72.5" width="176" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$G = 1000\,\text{W/m}^2$</div></foreignObject>
  <foreignObject x="161" y="166.5" width="164" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#4f8fbf">$G = 500\,\text{W/m}^2$</div></foreignObject>
  <foreignObject x="110" y="89.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I_\text{sc}$</span></div></foreignObject>
  <foreignObject x="427.5" y="255.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U_\text{oc}$</span></div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/solar-panels-jyvaskyla.webp" alt="A dark house roof against a blue sky; on the roof are two rows of dark blue solar panels and a chimney."><figcaption>Solar panels on the roof of a detached house in Jyväskylä, Finland. Each panel contains many solar cells connected in series. The panels produce a direct voltage, which an inverter converts into the alternating voltage of the grid.</figcaption></figure>

## Formula: Series resistor and power of a solar cell

### Sizing the series resistor
When the source, the series resistor and the LED are in series, the same current $I$ flows through all of them. By Kirchhoff's voltage law the voltage of the source is shared between the resistor and the LED, $U = U_R + U_\text{D}$ (chapter *Kirchhoff's laws and potential in a circuit*). The resistor obeys Ohm's law, $U_R = RI$, so the resistance of the series resistor is
```latex
R = \frac{U - U_\text{D}}{I}
```
where $R$ is the resistance of the series resistor ($\Omega$), $U$ the voltage of the source ($\text{V}$), $U_\text{D}$ the voltage of the LED or the diode ($\text{V}$) and $I$ the current ($\text{A}$). For the voltage of the LED the value given by the manufacturer is used, because it changes only a little with the current. When the resistor is known, the current is solved from the same equation: $I = \tfrac{U - U_\text{D}}{R}$.

<svg data-fig="etuvastus" viewBox="0 0 600 340" role="img" aria-label="On the left a circuit diagram, not to scale: a voltage source U, a series resistor R and an LED in series, the LED in the forward direction. A purple arrow shows the current I flowing from the positive terminal of the source through the resistor and the LED to the negative terminal. The voltage of the resistor is U_R and the voltage of the LED U_D. On the right a bar to scale: the voltage of the source, 6.0 V, is divided into a resistor voltage of 4.0 V and an LED voltage of 2.0 V, so U = U_R + U_D." style="max-width:100%;font-size:24px">
  <defs><radialGradient id="fy614-glow-k" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c92a2a" stop-opacity="0.55"/><stop offset="1" stop-color="#c92a2a" stop-opacity="0"/></radialGradient></defs>
  <polyline points="60,171 60,70 290,70 290,163" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="290,193 290,286 60,286 60,185" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="36" y1="171" x2="84" y2="171" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="48" y1="185" x2="72" y2="185" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="-2" y="163.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="90" y="141.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <rect x="145" y="58" width="60" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="160" y="25.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="150" y="89.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_R$</div></foreignObject>
  <circle cx="290" cy="178" r="46" fill="url(#fy614-glow-k)"/>
  <path d="M274,164 L306,164 L290,192 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="273" y1="192" x2="307" y2="192" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="312" y1="169" x2="324" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M330,154 L325.5,163 L320.5,156.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="312" y1="181" x2="324" y2="171" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M330,166 L325.5,175 L320.5,168.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="214" y="163.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_\text{D}$</div></foreignObject>
  <path d="M120,70 L100,62 L100,78 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="98" y="27.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <path d="M290,254 L282,234 L298,234 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M165,286 L185,278 L185,294 Z" fill="#7048e8" stroke-linejoin="round"/>
  <rect x="500" y="84" width="44" height="144" fill="#e3dccb" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="500" y="228" width="44" height="72" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="360" y="141.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_R = 4.0\,\text{V}$</div></foreignObject>
  <foreignObject x="360" y="249.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_\text{D} = 2.0\,\text{V}$</div></foreignObject>
  <foreignObject x="457" y="43.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U = 6.0\,\text{V}$</div></foreignObject>
</svg>

The power of a component is its voltage times its current (chapter *Electric power and the heating of a resistor*): the power of the LED is $P_\text{D} = U_\text{D} I$ and the power of the resistor $P_R = U_R I$. In the resistor electrical energy becomes internal energy of the resistor, so the resistor is chosen so that it withstands this power. In the reverse direction $I = 0$, so $U_R = RI = 0$ and the voltage of the diode is the whole voltage $U$ of the source.

### The power of a solar cell
The electric power given by a solar cell or panel is
```latex
P = U I
```
where $P$ is the power ($\text{W}$), $U$ the voltage between the terminals of the cell ($\text{V}$) and $I$ the current ($\text{A}$). In a short circuit $U = 0$ and at open circuit $I = 0$, so in both the power is zero. Between them is the **maximum power point**, the knee of the curve, where the power is greatest. On a $(U, I)$ graph the power is the area of the rectangle between the origin and a point of the curve.

The greatest power of the panel in the figure is about $0.92\,\text{W}$, when the voltage is about $5.0\,\text{V}$ and the current $184\,\text{mA}$. The load resistance is then $5.0\,\text{V} : 0.184\,\text{A} \approx 27\,\Omega$. The maximum power point changes with the irradiance, so the control electronics of solar power plants and chargers keep seeking it.

<svg data-fig="teho" viewBox="0 0 600 470" role="img" aria-label="Two graphs to scale with a common voltage axis, calculated with the solar panel model of the chapter at an irradiance of 1000 W/m². Upper: the current I of the panel in milliamperes as a function of the voltage U, the curve running from 200 mA to 6.0 volts. At 5.0 V and 184 mA there is a point, and the rectangle between it and the origin is shaded orange: its area is the power P = U I. Lower: the power P in watts as a function of the voltage. The power is zero in a short circuit and at open circuit and greatest, about 0.92 W, when the voltage is about 5.0 V. A dashed line joins the maximum power points of both graphs." style="max-width:100%;font-size:24px">
  <line x1="150.5" y1="204" x2="150.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204.5" y1="204" x2="204.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="204" x2="259" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="204" x2="313" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367.5" y1="204" x2="367.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="421.5" y1="204" x2="421.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="204" x2="476" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="147" x2="476" y2="147" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="90.5" x2="476" y2="90.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="204" x2="490" y2="204" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,204 L489,210 L489,198 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="205" x2="96" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,36 L102,49 L90,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150.5" y1="204" x2="150.5" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="204.5" y1="204" x2="204.5" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="259" y1="204" x2="259" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="313" y1="204" x2="313" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="367.5" y1="204" x2="367.5" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="421.5" y1="204" x2="421.5" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="204" x2="476" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="147" x2="96" y2="147" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="132.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="90.5" x2="96" y2="90.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="76" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="508" y="189.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="86" y="5.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <line x1="150.5" y1="420" x2="150.5" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="204.5" y1="420" x2="204.5" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="259" y1="420" x2="259" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="420" x2="313" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367.5" y1="420" x2="367.5" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="421.5" y1="420" x2="421.5" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="420" x2="476" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="345" x2="476" y2="345" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="270" x2="476" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="420" x2="490" y2="420" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,420 L489,426 L489,414 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="421" x2="96" y2="256" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,244 L102,257 L90,257 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150.5" y1="420" x2="150.5" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140.5" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="204.5" y1="420" x2="204.5" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="194.5" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="259" y1="420" x2="259" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="249" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="313" y1="420" x2="313" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="367.5" y1="420" x2="367.5" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357.5" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="421.5" y1="420" x2="421.5" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="411.5" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="476" y1="420" x2="476" y2="427" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="466" y="429.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="89" y1="345" x2="96" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="330.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.5$</div></foreignObject>
  <line x1="89" y1="270" x2="96" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="255.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.0$</div></foreignObject>
  <foreignObject x="66" y="425.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="405.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="86" y="213.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{W})$</div></foreignObject>
  <polygon points="96,204 96,99 365.5,99 365.5,204" fill="#ffc078" fill-opacity="0.6"/>
  <polyline points="96,90.5 97.5,90.5 99.5,90.5 101,90.5 102.5,90.5 104,90.5 106,90.5 107.5,90.5 109,90.5 110.5,90.5 112.5,90.5 114,90.5 115.5,90.5 117,90.5 119,90.5 120.5,90.5 122,90.5 123.5,90.5 125.5,90.5 127,90.5 128.5,90.5 130,90.5 132,90.5 133.5,90.5 135,90.5 136.5,90.5 138.5,90.5 140,90.5 141.5,90.5 143,90.5 145,90.5 146.5,90.5 148,90.5 149.5,90.5 151.5,90.5 153,90.5 154.5,90.5 156.5,90.5 158,90.5 159.5,90.5 161,90.5 163,90.5 164.5,90.5 166,90.5 167.5,90.5 169.5,90.5 171,90.5 172.5,90.5 174,90.5 176,90.5 177.5,90.5 179,90.5 180.5,90.5 182.5,90.5 184,90.5 185.5,90.5 187,90.5 189,90.5 190.5,90.5 192,90.5 193.5,90.5 195.5,90.5 197,90.5 198.5,90.5 200,90.5 202,90.5 203.5,90.5 205,90.5 206.5,90.5 208.5,90.5 210,90.5 211.5,90.5 213.5,90.5 215,90.5 216.5,90.5 218,90.5 220,90.5 221.5,90.5 223,90.5 224.5,90.5 226.5,90.5 228,90.5 229.5,90.5 231,90.5 233,90.5 234.5,90.5 236,90.5 237.5,90.5 239.5,90.5 241,90.5 242.5,90.5 244,90.5 246,90.5 247.5,90.5 249,90.5 250.5,90.5 252.5,90.5 254,90.5 255.5,90.5 257,90.5 259,90.5 260.5,90.5 262,90.5 263.5,90.5 265.5,90.5 267,90.5 268.5,90.5 270.5,90.5 272,90.5 273.5,90.5 275,90.5 277,90.5 278.5,90.5 280,90.5 281.5,90.5 283.5,90.5 285,90.5 286.5,90.5 288,90.5 290,90.5 291.5,90.5 293,90.5 294.5,90.5 296.5,91 298,91 299.5,91 301,91 303,91 304.5,91 306,91 307.5,91 309.5,91 311,91 312.5,91 314,91 316,91.5 317.5,91.5 319,91.5 320.5,91.5 322.5,91.5 324,91.5 325.5,92 327.5,92 329,92 330.5,92 332,92 334,92.5 335.5,92.5 337,92.5 338.5,93 340.5,93 342,93.5 343.5,93.5 345,93.5 347,94 348.5,94.5 350,94.5 351.5,95 353.5,95.5 355,95.5 356.5,96 358,96.5 360,97 361.5,97.5 363,98 364.5,98.5 366.5,99.5 368,100 369.5,100.5 371,101.5 373,102.5 374.5,103.5 376,104.5 377.5,105.5 379.5,106.5 381,108 382.5,109 384.5,110.5 386,112 387.5,114 389,115.5 391,117.5 392.5,120 394,122 395.5,124.5 397.5,127.5 399,130 400.5,133 402,136.5 404,140 405.5,144 407,148 408.5,152.5 410.5,157.5 412,163 413.5,168.5 415,174.5 417,181 418.5,188 420,196 421.5,204" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,420 97.5,419 99.5,418 101,417.5 102.5,416.5 104,415.5 106,414.5 107.5,413.5 109,413 110.5,412 112.5,411 114,410 115.5,409 117,408.5 119,407.5 120.5,406.5 122,405.5 123.5,404.5 125.5,404 127,403 128.5,402 130,401 132,400 133.5,399.5 135,398.5 136.5,397.5 138.5,396.5 140,395.5 141.5,395 143,394 145,393 146.5,392 148,391 149.5,390.5 151.5,389.5 153,388.5 154.5,387.5 156.5,386.5 158,386 159.5,385 161,384 163,383 164.5,382 166,381.5 167.5,380.5 169.5,379.5 171,378.5 172.5,377.5 174,377 176,376 177.5,375 179,374 180.5,373 182.5,372.5 184,371.5 185.5,370.5 187,369.5 189,368.5 190.5,368 192,367 193.5,366 195.5,365 197,364 198.5,363.5 200,362.5 202,361.5 203.5,360.5 205,359.5 206.5,359 208.5,358 210,357 211.5,356 213.5,355 215,354.5 216.5,353.5 218,352.5 220,351.5 221.5,350.5 223,350 224.5,349 226.5,348 228,347 229.5,346 231,345.5 233,344.5 234.5,343.5 236,342.5 237.5,341.5 239.5,341 241,340 242.5,339 244,338 246,337 247.5,336.5 249,335.5 250.5,334.5 252.5,333.5 254,332.5 255.5,332 257,331 259,330 260.5,329 262,328.5 263.5,327.5 265.5,326.5 267,325.5 268.5,324.5 270.5,324 272,323 273.5,322 275,321 277,320 278.5,319.5 280,318.5 281.5,317.5 283.5,316.5 285,316 286.5,315 288,314 290,313 291.5,312.5 293,311.5 294.5,310.5 296.5,309.5 298,309 299.5,308 301,307 303,306 304.5,305.5 306,304.5 307.5,303.5 309.5,303 311,302 312.5,301 314,300.5 316,299.5 317.5,298.5 319,298 320.5,297 322.5,296 324,295.5 325.5,294.5 327.5,294 329,293 330.5,292.5 332,291.5 334,291 335.5,290 337,289.5 338.5,289 340.5,288 342,287.5 343.5,287 345,286.5 347,286 348.5,285.5 350,285 351.5,284.5 353.5,284 355,283.5 356.5,283 358,283 360,282.5 361.5,282.5 363,282.5 364.5,282.5 366.5,282.5 368,282.5 369.5,282.5 371,283 373,283 374.5,283.5 376,284 377.5,285 379.5,285.5 381,286.5 382.5,288 384.5,289 386,290.5 387.5,292 389,294 391,296.5 392.5,298.5 394,301.5 395.5,304.5 397.5,307.5 399,311 400.5,315 402,319.5 404,324.5 405.5,330 407,335.5 408.5,342 410.5,349 412,356.5 413.5,365 415,374.5 417,384.5 418.5,395 420,407 421.5,420" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="365.5" y1="99" x2="365.5" y2="420" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="365.5" cy="99" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="365.5" cy="282.5" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="182.5" y="137" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$P = U I$</span></div></foreignObject>
  <foreignObject x="203.5" y="242" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{maximum power point}$</span></div></foreignObject>
</svg>

### Efficiency
The efficiency of a cell is the electric power it gives divided by the power of the light arriving at the cell (chapter *Efficiency*). The radiant power incident on the cell is the irradiance times the area of the cell, and the electric power $P$ is the power of the cell at the maximum power point, so
```latex
\eta = \frac{P}{G A}
```
where $\eta$ is the efficiency, $P$ the electric power of the cell ($\text{W}$), $G$ the irradiance of the radiation incident on the surface, that is, the radiant power per unit area ($\text{W/m}^2$), and $A$ the area of the cell ($\text{m}^2$). On a clear summer day, when the sun shines perpendicularly onto the cell, $G$ is about $1000\,\text{W/m}^2$. The area of the panel in the figure is $60\,\text{cm}^2 = 0.0060\,\text{m}^2$, so the light arriving at it is $1000\,\tfrac{\text{W}}{\text{m}^2} \cdot 0.0060\,\text{m}^2 = 6.0\,\text{W}$, and the efficiency is $0.92\,\text{W} : 6.0\,\text{W} \approx 15\,\%$. The efficiency of ordinary silicon cells is about $15$–$22\,\%$.

## Worked example
The red LED of a bicycle's rear light is run on a $6.0\,\text{V}$ battery. The voltage of the LED is $2.0\,\text{V}$ when its current is $20\,\text{mA}$. What series resistor is needed, and how large is the power that becomes internal energy in the resistor?

<!-- vaihe -->

**Given and find.** The voltage of the source $U = 6.0\,\text{V}$, the voltage of the LED $U_\text{D} = 2.0\,\text{V}$ and the current $I = 20\,\text{mA}$. We are asked for the resistance $R$ of the series resistor and the power $P_R$ of the resistor.

<!-- vaihe -->

**Principle.** The battery, the resistor and the LED are in series, so the same current flows through all of them. The voltage of the battery is shared between the resistor and the LED, $U = U_R + U_\text{D}$, and the voltage of the resistor is $U_R = RI$. The power of the resistor is its voltage times the current.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&R = \frac{U - U_\text{D}}{I} \\
&P_R = (U - U_\text{D}) I
\end{aligned}
```

<!-- vaihe -->

**Conversions.** The current in amperes: $I = 20\,\text{mA} = 20 \cdot 10^{-3}\,\text{A} = 0.020\,\text{A}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&R = \frac{U - U_\text{D}}{I} \\
&\phantom{R} = \frac{6.0\,\text{V} - 2.0\,\text{V}}{0.020\,\text{A}} \\
&\phantom{R} = 200\,\Omega \\
&P_R = 4.0\,\text{V} \cdot 0.020\,\text{A} \\
&\phantom{P_R} = 0.080\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The resistance of the series resistor is $200\,\Omega$, and the power that becomes internal energy in the resistor is $0.080\,\text{W}$, two significant figures like the voltages and the current.

<!-- vaihe -->

**Reasonableness.** The power of the LED is $2.0\,\text{V} \cdot 0.020\,\text{A} = 0.040\,\text{W}$, and the total $0.080\,\text{W} + 0.040\,\text{W} = 0.12\,\text{W}$ is the same as the power of the battery $6.0\,\text{V} \cdot 0.020\,\text{A}$. If a shop has only $220\,\Omega$ resistors, the current is $4.0\,\text{V} : 220\,\Omega \approx 18\,\text{mA}$, slightly smaller, so the LED is not overloaded.

## Common misconception
Many calculate the series resistor by dividing the whole voltage of the source by the current, $R = \tfrac{U}{I}$. But across the resistor there is only the part of the voltage that is not across the LED, $U - U_\text{D}$. A resistor that is too large gives too small a current, and the LED shines dimly.

Another mistake is to think that a diode is a resistor with a constant resistance. The ratio of the voltage to the current of a diode, $U_\text{D} : I$, changes strongly with the current: below the threshold voltage hardly any current flows, and above it a small increase in voltage increases the current a lot. A third mistake is to calculate the power of a solar cell as the product of the short-circuit current and the open-circuit voltage. They do not occur at the same time: in a short circuit the voltage is zero and at open circuit the current is zero.

## Summary
- Semiconductors, such as silicon, conduct electricity worse than metals and better than insulators. Diodes, LEDs and solar cells are made of them.
- A diode lets current through in one direction only. In the forward direction the anode is on the side of the positive terminal of the source and current flows; in the reverse direction no current flows and the whole voltage of the source is across the diode.
- Current starts to flow when the voltage of the diode reaches the threshold voltage: about $0.6$–$0.7\,\text{V}$ for a silicon diode and about $1.8$–$3.3\,\text{V}$ for LEDs, depending on the colour. A diode does not obey Ohm's law.
- The current of an LED must be limited. In a simple circuit connected to a constant-voltage source, a series resistor is connected in series with the LED: $R = \tfrac{U - U_\text{D}}{I}$. In LED devices the current can also be controlled by a constant-current driver.
- A solar cell is a direct-voltage source. The short-circuit current is directly proportional to the irradiance, and the open-circuit voltage changes only a little. The power $P = UI$ is greatest at the maximum power point, and the efficiency is $\eta = \tfrac{P}{GA}$.
