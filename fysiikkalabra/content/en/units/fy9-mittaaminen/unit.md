# Measurement, uncertainty and graphs

> **Why** is a result obtained from a straight line fitted to a graph usually more reliable than one calculated from a single measurement?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a workbench in a school laboratory. On the left, a measuring cylinder with liquid stands on a digital balance, and a bottle is beside it. In the middle is an open notebook: on the left page a table of measurements and on the right page a graph whose points, with their error bars, are scattered slightly around one fitted straight line. On the right of the bench are a ruler and a stopwatch." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9m-h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efe7d6"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy9m-h-bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#e9c98a"/></linearGradient><linearGradient id="fy9m-h-scale" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy9m-h-liquid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy9m-h-bottle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="360" fill="url(#fy9m-h-wall)"/>
  <line x1="0" y1="60" x2="1200" y2="60" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="120" x2="1200" y2="120" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="180" x2="1200" y2="180" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="240" x2="1200" y2="240" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="1200" y2="300" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="360" x2="1200" y2="360" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="0" y="360" width="1200" height="240" fill="url(#fy9m-h-bench)"/>
  <line x1="0" y1="360" x2="1200" y2="360" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <path d="M0,392 q300,-7 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.45"/>
  <path d="M0,436 q300,-5.5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.45"/>
  <path d="M0,480 q300,-6 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.45"/>
  <path d="M0,524 q300,5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.45"/>
  <path d="M0,568 q300,-5 600,0 t600,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.45"/>
  <ellipse cx="190" cy="452" rx="150" ry="16" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="52" y="404" width="276" height="44" rx="10" fill="url(#fy9m-h-scale)" stroke="#1f2933" stroke-width="3"/>
  <rect x="78" y="414" width="92" height="24" rx="4" fill="#1f2933"/>
  <rect x="86" y="420" width="18" height="12" rx="2" fill="#b2f2bb"/>
  <rect x="112" y="420" width="18" height="12" rx="2" fill="#b2f2bb"/>
  <rect x="138" y="420" width="18" height="12" rx="2" fill="#b2f2bb"/>
  <circle cx="214" cy="426" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="248" cy="426" r="9" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="64" y="392" width="252" height="14" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="118" y="376" width="132" height="16" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="146" y="128" width="76" height="250" fill="#eef5f9" fill-opacity="0.85"/>
  <rect x="148" y="238" width="72" height="138" fill="url(#fy9m-h-liquid)"/>
  <path d="M148,238 Q184,250 220,238" fill="#ffffff" stroke-linejoin="round" fill-opacity="0.6"/>
  <path d="M146,378 V128 M222,128 V378" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M140,124 Q146,128 152,126 M216,126 Q222,128 228,124" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="146" y1="360" x2="168" y2="360" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="342" x2="159" y2="342" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="324" x2="159" y2="324" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="306" x2="159" y2="306" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="288" x2="159" y2="288" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="270" x2="168" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="252" x2="159" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="234" x2="159" y2="234" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="216" x2="159" y2="216" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="198" x2="159" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="180" x2="168" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="162" x2="159" y2="162" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146" y1="144" x2="159" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="160" y1="150" x2="160" y2="370" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <path d="M330,360 V250 Q330,226 350,214 V180 H378 V214 Q398,226 398,250 V360 Z" fill="url(#fy9m-h-bottle)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="346" y="166" width="36" height="16" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="336" y="268" width="56" height="52" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <line x1="346" y1="284" x2="382" y2="284" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="346" y1="300" x2="372" y2="300" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <path d="M444,402 L956,402 L968,560 L432,560 Z" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M440,386 L696,396 L696,548 L428,544 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M696,396 L952,386 L964,544 L696,548 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="696" y1="396" x2="696" y2="548" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="456" y1="418" x2="680" y2="420" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="440" x2="680" y2="442" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="462" x2="680" y2="464" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="484" x2="680" y2="486" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="506" x2="680" y2="508" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="456" y1="528" x2="680" y2="530" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="560" y1="410" x2="560" y2="534" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="472" y1="429" x2="512.5" y2="429" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="580" y1="430" x2="634" y2="430" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="472" y1="451" x2="513" y2="451" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="580" y1="452" x2="646.5" y2="452" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="472" y1="473" x2="516.5" y2="473" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="580" y1="474" x2="641" y2="474" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="472" y1="495" x2="516" y2="495" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="580" y1="496" x2="630.5" y2="496" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="472" y1="517" x2="523.5" y2="517" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="580" y1="518" x2="632" y2="518" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <line x1="746" y1="412" x2="746" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="768" y1="412" x2="768" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="790" y1="412" x2="790" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="812" y1="412" x2="812" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="834" y1="412" x2="834" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="856" y1="412" x2="856" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="878" y1="412" x2="878" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="900" y1="412" x2="900" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="922" y1="412" x2="922" y2="528" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="506" x2="938" y2="506" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="484" x2="938" y2="484" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="462" x2="938" y2="462" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="440" x2="938" y2="440" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="418" x2="938" y2="418" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="724" y1="528" x2="936" y2="528" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M946,528 L935,533 L935,523 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="724" y1="528" x2="724" y2="414" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M724,404 L729,415 L719,415 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="730" y1="514" x2="930" y2="420" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="754" y1="494.5" x2="754" y2="520.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="749" y1="494.5" x2="759" y2="494.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="749" y1="520.5" x2="759" y2="520.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="754" cy="507.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="784" y1="469.5" x2="784" y2="495.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="779" y1="469.5" x2="789" y2="469.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="779" y1="495.5" x2="789" y2="495.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="784" cy="482.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="814" y1="465.5" x2="814" y2="491.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="809" y1="465.5" x2="819" y2="465.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="809" y1="491.5" x2="819" y2="491.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="814" cy="478.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="846" y1="441.5" x2="846" y2="467.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="841" y1="441.5" x2="851" y2="441.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="841" y1="467.5" x2="851" y2="467.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="846" cy="454.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="876" y1="438.5" x2="876" y2="464.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="871" y1="438.5" x2="881" y2="438.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="871" y1="464.5" x2="881" y2="464.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="876" cy="451.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="906" y1="415.5" x2="906" y2="441.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="901" y1="415.5" x2="911" y2="415.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="901" y1="441.5" x2="911" y2="441.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="906" cy="428.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <g transform="translate(640,568) rotate(-8)"><rect x="-150" y="-9" width="230" height="18" fill="#ffc078" stroke="#1f2933" stroke-width="2"/><rect x="-168" y="-9" width="18" height="18" rx="4" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/><path d="M80,-9 L110,0 L80,9 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/><path d="M101,-3 L110,0 L101,3 Z" fill="#1f2933"/></g>
  <g transform="translate(1062,500) rotate(-14)"><rect x="-120" y="-20" width="240" height="40" rx="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/><line x1="-108" y1="-20" x2="-108" y2="2" stroke="#1f2933" stroke-width="2"/><line x1="-96" y1="-20" x2="-96" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-84" y1="-20" x2="-84" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-72" y1="-20" x2="-72" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-60" y1="-20" x2="-60" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-48" y1="-20" x2="-48" y2="2" stroke="#1f2933" stroke-width="2"/><line x1="-36" y1="-20" x2="-36" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-24" y1="-20" x2="-24" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="-12" y1="-20" x2="-12" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="0" y1="-20" x2="0" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="12" y1="-20" x2="12" y2="2" stroke="#1f2933" stroke-width="2"/><line x1="24" y1="-20" x2="24" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="36" y1="-20" x2="36" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="48" y1="-20" x2="48" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="60" y1="-20" x2="60" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="72" y1="-20" x2="72" y2="2" stroke="#1f2933" stroke-width="2"/><line x1="84" y1="-20" x2="84" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="96" y1="-20" x2="96" y2="-6" stroke="#1f2933" stroke-width="2"/><line x1="108" y1="-20" x2="108" y2="-6" stroke="#1f2933" stroke-width="2"/></g>
  <ellipse cx="1060" cy="404" rx="70" ry="12" fill="#1f2933" fill-opacity="0.18"/>
  <rect x="1048" y="219.5" width="24.5" height="18" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1054.5" y="236.5" width="10.5" height="10.5" fill="#6c757d"/>
  <circle cx="1060" cy="320" r="76" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="1060" cy="320" r="62.32" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="1060" y1="268.5" x2="1060" y2="260.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1086" y1="275" x2="1089.5" y2="268.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1105" y1="294" x2="1111.5" y2="290.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1111.5" y1="320" x2="1119.5" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1105" y1="346" x2="1111.5" y2="349.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1086" y1="365" x2="1089.5" y2="371.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1060" y1="371.5" x2="1060" y2="379.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1034" y1="365" x2="1030.5" y2="371.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1015" y1="346" x2="1008.5" y2="349.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1008.5" y1="320" x2="1000.5" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1015" y1="294" x2="1008.5" y2="290.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1034" y1="275" x2="1030.5" y2="268.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1060" y1="320" x2="1105.5" y2="298.5" stroke="#c92a2a" stroke-width="5.32" stroke-linecap="round"/>
  <circle cx="1060" cy="320" r="6.08" fill="#1f2933"/>
</svg>

## The big picture {Kokonaiskuva}

Almost every matriculation exam in physics has a problem that gives a set of measurement data and asks for a quantity to be determined from it. Processing measurement data often proceeds from the measurement results and their uncertainties to a graph, where needed to fitting a model and interpreting it, and finally to the result with its uncertainty. Not every problem requires every step. Points can be gained or lost at every step.

<svg data-fig="kartta" viewBox="0 0 600 448" role="img" aria-label="Diagram: from measurement to result in five steps joined by downward arrows. 1 Measure: reading, uncertainty Δx and precision. 2 Graph: quantity and unit on the axes. 3 Fit: straight line or linearisation. 4 Interpret: slope k and constant term b with their units. 5 Result: k ± Δk and the range of validity of the model." style="max-width:100%;font-size:26px">
  <rect x="14" y="14" width="572" height="64" rx="10" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <rect x="14" y="14" width="196" height="64" rx="10" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5"/>
  <rect x="196" y="16.5" width="14" height="59" fill="#d0e6fb"/>
  <line x1="210" y1="14" x2="210" y2="78" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="42" cy="46" r="18" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <foreignObject x="31" y="30.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$1$</div></foreignObject>
  <foreignObject x="70" y="30.5" width="132" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{Measure}$</div></foreignObject>
  <foreignObject x="222" y="30.5" width="358" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{reading}, \ \Delta x, \ \text{precision}$</div></foreignObject>
  <line x1="110" y1="80" x2="110" y2="91" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,102 L104.5,90 L115.5,90 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="14" y="104" width="572" height="64" rx="10" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <rect x="14" y="104" width="196" height="64" rx="10" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5"/>
  <rect x="196" y="106.5" width="14" height="59" fill="#d0e6fb"/>
  <line x1="210" y1="104" x2="210" y2="168" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="42" cy="136" r="18" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <foreignObject x="31" y="120.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$2$</div></foreignObject>
  <foreignObject x="70" y="120.5" width="132" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{Graph}$</div></foreignObject>
  <foreignObject x="222" y="120.5" width="358" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{quantity (unit)}$</div></foreignObject>
  <line x1="110" y1="170" x2="110" y2="181" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,192 L104.5,180 L115.5,180 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="14" y="194" width="572" height="64" rx="10" fill="#ffffff" stroke="#e8590c" stroke-width="2.5"/>
  <rect x="14" y="194" width="196" height="64" rx="10" fill="#ffc078" stroke="#e8590c" stroke-width="2.5"/>
  <rect x="196" y="196.5" width="14" height="59" fill="#ffc078"/>
  <line x1="210" y1="194" x2="210" y2="258" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="42" cy="226" r="18" fill="#ffffff" stroke="#e8590c" stroke-width="2.5"/>
  <foreignObject x="31" y="210.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$3$</div></foreignObject>
  <foreignObject x="70" y="210.5" width="132" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{Fit}$</div></foreignObject>
  <foreignObject x="222" y="210.5" width="358" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{line or linearisation}$</div></foreignObject>
  <line x1="110" y1="260" x2="110" y2="271" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,282 L104.5,270 L115.5,270 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="14" y="284" width="572" height="64" rx="10" fill="#ffffff" stroke="#e8590c" stroke-width="2.5"/>
  <rect x="14" y="284" width="196" height="64" rx="10" fill="#ffc078" stroke="#e8590c" stroke-width="2.5"/>
  <rect x="196" y="286.5" width="14" height="59" fill="#ffc078"/>
  <line x1="210" y1="284" x2="210" y2="348" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="42" cy="316" r="18" fill="#ffffff" stroke="#e8590c" stroke-width="2.5"/>
  <foreignObject x="31" y="300.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$4$</div></foreignObject>
  <foreignObject x="70" y="300.5" width="132" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{Interpret}$</div></foreignObject>
  <foreignObject x="222" y="300.5" width="358" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$k \text{ and } b \text{ with units}$</div></foreignObject>
  <line x1="110" y1="350" x2="110" y2="361" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,372 L104.5,360 L115.5,360 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="14" y="374" width="572" height="64" rx="10" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5"/>
  <rect x="14" y="374" width="196" height="64" rx="10" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <rect x="196" y="376.5" width="14" height="59" fill="#b2f2bb"/>
  <line x1="210" y1="374" x2="210" y2="438" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="42" cy="406" r="18" fill="#ffffff" stroke="#2b8a3e" stroke-width="2.5"/>
  <foreignObject x="31" y="390.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$5$</div></foreignObject>
  <foreignObject x="70" y="390.5" width="132" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{Result}$</div></foreignObject>
  <foreignObject x="222" y="390.5" width="358" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$k \pm \Delta k, \ \text{range of validity}$</div></foreignObject>
</svg>

## Formula: The measurement result and the equation of a line

### The result and its uncertainty

The best estimate of a repeated measurement is the mean $\bar{x}$. In this course the spread is estimated as half the range, and the result is stated in the form $\bar{x} \pm \Delta x$:

```latex
\begin{aligned}
\Delta x &= \frac{x_\text{max} - x_\text{min}}{2} \\
\varepsilon &= \frac{\Delta x}{\bar{x}} \cdot 100\,\%
\end{aligned}
```

where $x_\text{max}$ and $x_\text{min}$ are the largest and the smallest result, $\Delta x$ the measurement uncertainty and $\varepsilon$ the relative uncertainty. In a single measurement, the uncertainty of a reading can in a simple situation be estimated as half the smallest scale division, but the method and other sources of error also affect the total uncertainty. The uncertainty is rounded to one significant figure (two, if the first digit is 1), and the result to the same decimal place. The result of a multiplication or a division gets as many significant figures as the least precise measured starting value; exact quantities, such as integers and conversion factors, do not limit the precision.

Repetition reduces the effect of random error in the mean, but it does not remove systematic error. A gross error is looked for: a deviating result is checked, and it is not removed without a reason.

### The equation of a line and its interpretation

If the points lie approximately on a straight line, a line is fitted among the points:

```kaavat
y = kx + b
slope :: k = \frac{\Delta y}{\Delta x}
```

where $k$ is the slope and $b$ the constant term, that is, the value of $y$ when $x = 0$. The slope is read from two points of the line far apart, not from the measurement points. Its unit is the unit of the vertical axis divided by the unit of the horizontal axis, and it usually has a physical meaning: in a $(V, m)$ graph it is the density. The model has been shown to be valid only in the measured range, so extrapolation outside it must be justified.

<svg data-fig="anatomia" viewBox="0 0 600 410" role="img" aria-label="Graph to scale, invented example data: the temperature θ of water in degrees Celsius as a function of the time t in minutes. Six measurement points at the moments 1–6 min, each with a vertical uncertainty bar of ±1 °C. A solid straight line θ = 6.2 °C/min · t + 19 °C is fitted among the points, and dashed lines show the steepest and the shallowest line that still pass through all the bars. A triangle is drawn on the line between the points t = 1 min and t = 6 min, which are far apart: the horizontal side is Δt and the vertical side Δθ, and the slope is k = Δθ/Δt. The line crosses the vertical axis at b, which is the initial temperature. In the lower right corner a legend says that the dashed line means the steepest and the shallowest line." style="max-width:100%;font-size:27px">
  <line x1="138" y1="356" x2="138" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192" y1="356" x2="192" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="246" y1="356" x2="246" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="356" x2="300" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="354" y1="356" x2="354" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="408" y1="356" x2="408" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="462" y1="356" x2="462" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="282" x2="462" y2="282" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="208" x2="462" y2="208" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="134" x2="462" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="60" x2="462" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="356" x2="476" y2="356" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M488,356 L475,362 L475,350 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="357" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138" y1="356" x2="138" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="127" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$1$</div></foreignObject>
  <line x1="192" y1="356" x2="192" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$2$</div></foreignObject>
  <line x1="246" y1="356" x2="246" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$3$</div></foreignObject>
  <line x1="300" y1="356" x2="300" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$4$</div></foreignObject>
  <line x1="354" y1="356" x2="354" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="343" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$5$</div></foreignObject>
  <line x1="408" y1="356" x2="408" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="397" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$6$</div></foreignObject>
  <line x1="462" y1="356" x2="462" y2="363" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="451" y="364" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$7$</div></foreignObject>
  <line x1="77" y1="282" x2="84" y2="282" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="266" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$15$</div></foreignObject>
  <line x1="77" y1="208" x2="84" y2="208" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="192" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$30$</div></foreignObject>
  <line x1="77" y1="134" x2="84" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="118" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$45$</div></foreignObject>
  <line x1="77" y1="60" x2="84" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="44" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$60$</div></foreignObject>
  <foreignObject x="52" y="360" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$0$</div></foreignObject>
  <foreignObject x="494" y="340" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$t\ (\text{min})$</div></foreignObject>
  <foreignObject x="74" y="2" width="68" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$\theta\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="84,270.5 440.5,57.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="84,258 462,55.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="84,264 456.5,52.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="138" y1="233.5" x2="408" y2="233.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="408" y1="233.5" x2="408" y2="80" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="138" y1="238" x2="138" y2="228" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="132" y1="238" x2="144" y2="238" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="132" y1="228" x2="144" y2="228" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="138" cy="233" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="192" y1="210" x2="192" y2="200" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="186" y1="210" x2="198" y2="210" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="186" y1="200" x2="198" y2="200" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="192" cy="205" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="246" y1="174.5" x2="246" y2="164.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="240" y1="174.5" x2="252" y2="174.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="240" y1="164.5" x2="252" y2="164.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="246" cy="169.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="300" y1="148.5" x2="300" y2="138.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="294" y1="148.5" x2="306" y2="148.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="294" y1="138.5" x2="306" y2="138.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="300" cy="143.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="354" y1="113.5" x2="354" y2="103.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="348" y1="113.5" x2="360" y2="113.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="348" y1="103.5" x2="360" y2="103.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="354" cy="108.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="408" y1="86.5" x2="408" y2="77" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="402" y1="86.5" x2="414" y2="86.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="402" y1="77" x2="414" y2="77" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="408" cy="81.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="255" y="239.5" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px;color:#e8590c">$\Delta t$</div></foreignObject>
  <foreignObject x="420" y="167" width="36" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px;color:#e8590c">$\Delta \theta$</div></foreignObject>
  <foreignObject x="193" y="67" width="64" height="65" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$k = \dfrac{\Delta \theta}{\Delta t}$</div></foreignObject>
  <circle cx="84" cy="264" r="9" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="100" y="262" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$b$</div></foreignObject>
  <line x1="284" y1="321.5" x2="318" y2="321.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="326" y="305.5" width="275" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px;color:#6b7480">$\text{steepest, shallowest}$</div></foreignObject>
</svg>

The uncertainty of the slope can be estimated with the steepest and the shallowest line that still pass through the uncertainty bars:

```latex
\Delta k = \frac{k_\text{max} - k_\text{min}}{2}
```

They bound an estimated range, not certain limits.

### Linearisation

When the model is not a straight line, the axes are given quantities between which the relationship is a straight line. The model is written in the form $y = kx + b$:

```latex
\begin{aligned}
s &= \tfrac{a}{2} \cdot t^2 \\
p &= C \cdot \tfrac{1}{V} \\
m &= \rho V + m_0
\end{aligned}
```

In uniformly accelerated motion from rest, when time is counted from the start of the motion, the $(t^2, s)$ graph is a straight line through the origin with slope $\tfrac{a}{2}$. When the amount and the temperature of a gas stay the same, according to Boyle's law the $(\tfrac{1}{V}, p)$ graph is a straight line; the constant $C$ is the product of the pressure and the volume. The total mass $m$ of a liquid weighed in a container is a straight line with respect to the volume $V$, whose slope is the density $\rho$ and whose constant term is the mass $m_0$ of the container.

<svg data-fig="linearisointi" viewBox="0 0 600 340" role="img" aria-label="Two graphs of the same model data: a trolley accelerating uniformly from rest, acceleration 0.50 m/s². On the left, the distance s in metres as a function of the time t: six points at the moments 0.5–3.0 s lie on a curve that bends upwards. On the right, the same distance as a function of the square of the time t²: the points are on a straight line through the origin whose slope is half the acceleration, 0.25 m/s²." style="max-width:100%;font-size:27px">
  <line x1="94.5" y1="284" x2="94.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="136.5" y1="284" x2="136.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="179" y1="284" x2="179" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="194.5" x2="200" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="105" x2="200" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51" y1="284" x2="208" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M220,284 L207,290 L207,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="52" y1="285" x2="52" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M52,40 L58,53 L46,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="94.5" y1="284" x2="94.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="83.5" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$1$</div></foreignObject>
  <line x1="136.5" y1="284" x2="136.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="125.5" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$2$</div></foreignObject>
  <line x1="179" y1="284" x2="179" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="168" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$3$</div></foreignObject>
  <line x1="45" y1="194.5" x2="52" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="18" y="178.5" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$1$</div></foreignObject>
  <line x1="45" y1="105" x2="52" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="18" y="89" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$2$</div></foreignObject>
  <foreignObject x="20" y="288" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$0$</div></foreignObject>
  <foreignObject x="226" y="268" width="68" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="42" y="8" width="68" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$s\ (\text{m})$</div></foreignObject>
  <polyline points="52,284 53,284 54.5,284 55.5,284 56.5,283.5 57.5,283.5 59,283.5 60,283 61,283 62,282.5 63.5,282.5 64.5,282 65.5,281.5 66.5,281.5 68,281 69,280.5 70,280 71,279.5 72.5,279 73.5,278 74.5,277.5 75.5,277 77,276.5 78,275.5 79,275 80,274 81.5,273 82.5,272.5 83.5,271.5 84.5,270.5 86,269.5 87,268.5 88,267.5 89,266.5 90.5,265.5 91.5,264.5 92.5,263.5 93.5,262 95,261 96,260 97,258.5 98,257 99.5,256 100.5,254.5 101.5,253 102.5,251.5 104,250.5 105,249 106,247.5 107.5,246 108.5,244 109.5,242.5 110.5,241 112,239.5 113,237.5 114,236 115,234 116.5,232 117.5,230.5 118.5,228.5 119.5,226.5 121,224.5 122,223 123,221 124,219 125.5,216.5 126.5,214.5 127.5,212.5 128.5,210.5 130,208 131,206 132,203.5 133,201.5 134.5,199 135.5,197 136.5,194.5 137.5,192 139,189.5 140,187 141,184.5 142,182 143.5,179.5 144.5,177 145.5,174.5 146.5,171.5 148,169 149,166 150,163.5 151,160.5 152.5,158 153.5,155 154.5,152 155.5,149 157,146 158,143.5 159,140 160.5,137 161.5,134 162.5,131 163.5,128 165,124.5 166,121.5 167,118.5 168,115 169.5,111.5 170.5,108.5 171.5,105 172.5,101.5 174,98 175,94.5 176,91.5 177,87.5 178.5,84 179.5,80.5 180.5,77 181.5,73.5 183,69.5 184,66 185,62 186,58.5 187.5,54.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 6"/>
  <circle cx="73" cy="278.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="94.5" cy="261.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="115.5" cy="233.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="136.5" cy="194.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="157.5" cy="144" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="179" cy="82.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="387.5" y1="284" x2="387.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423" y1="284" x2="423" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458" y1="284" x2="458" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="194.5" x2="470" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="105" x2="470" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="351" y1="284" x2="478" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,284 L477,290 L477,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="352" y1="285" x2="352" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M352,40 L358,53 L346,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="387.5" y1="284" x2="387.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="376.5" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$3$</div></foreignObject>
  <line x1="423" y1="284" x2="423" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$6$</div></foreignObject>
  <line x1="458" y1="284" x2="458" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447" y="292" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:27px">$9$</div></foreignObject>
  <line x1="345" y1="194.5" x2="352" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="318" y="178.5" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$1$</div></foreignObject>
  <line x1="345" y1="105" x2="352" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="318" y="89" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$2$</div></foreignObject>
  <foreignObject x="320" y="288" width="22" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:27px">$0$</div></foreignObject>
  <foreignObject x="496" y="268" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$t^2\ (\text{s}^2)$</div></foreignObject>
  <foreignObject x="342" y="8" width="68" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$s\ (\text{m})$</div></foreignObject>
  <polyline points="352,284 467.5,64.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="355" cy="278.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="364" cy="261.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="378.5" cy="233.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="399" cy="194.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="426" cy="144" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="458" cy="82.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="480" y="133.5" width="78" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$k = a/2$</div></foreignObject>
</svg>

## Common mistakes {Yleisiä virheitä}

- The points are joined with a broken line, or the line is forced through the origin without a physical reason.
- The slope is calculated from two adjacent measurement points, or it is given without a unit.
- An axis lacks its quantity or unit, or the scale is not evenly spaced.
- The result keeps all the digits of the calculator, or the uncertainty and the result are rounded to different precisions.
- Repetitions are believed to remove a systematic error.
- A straight line is fitted to curved data, although the deviations form an arc.

## Review if needed {Kertaa tarvittaessa}

- Units, prefixes and significant figures: in the chapter [*Quantities, units and the SI system*](fy1-2.html).
- Types of error, the mean and uncertainty: in the chapter [*Measuring and the reliability of a measurement*](fy1-3.html).
- The graph, fitting a straight line and the slope: in the chapter [*Graphing and fitting a straight line*](fy1-4.html).
- Density as the slope and the mass of the container as the constant term: in the chapter [*Density*](fy1-7.html).
- Drawing and fitting a graph with a program: the ICT guides *Graph of measurement points*, *Fitting a straight line to measurement points*, *Interpreting the slope and the constant term* and *Uncertainty of the slope* (in Finnish).
