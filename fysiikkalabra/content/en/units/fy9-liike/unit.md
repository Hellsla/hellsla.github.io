# Motion as graphs

> **Why** can you work out the distance between tram stops from the tram's velocity graph, even though the graph does not contain a single metre?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a city street on a summer morning. In the middle of the street a tram runs along the rails to the right, with motion lines behind it. On the left and the right there are glass tram shelters. Above the tram an overhead wire runs between poles. In the background there are blocks of flats and birches. The picture has no text and no people." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9li-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfdcf2"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy9li-tram-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe6ec"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy9li-sky)"/>
  <path d="M159,108 Q157,77.5 193,81 Q207.5,48.5 243.5,59.5 Q276,41.5 294,75.5 Q326.5,79 323,108 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M761,92 Q759,54.5 803,59 Q820.5,19.5 864.5,32.5 Q904,10.5 926,52.5 Q965.5,57 961,92 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M1026,152 Q1025,131.5 1049,134 Q1058.5,112.5 1082.5,119.5 Q1104,107.5 1116,130.5 Q1137.5,133 1135,152 Z" fill="#ffffff" stroke-linejoin="round"/>
  <rect x="20" y="150" width="220" height="250" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="42" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="88" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="134" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="180" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="42" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="88" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="134" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="180" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="42" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="88" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="134" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="180" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="42" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="88" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="134" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="180" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="250" y="100" width="180" height="300" fill="#e9dcc8" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="272" y="126" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="318" y="126" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="364" y="126" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="272" y="178" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="318" y="178" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="364" y="178" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="272" y="230" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="318" y="230" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="364" y="230" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="272" y="282" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="318" y="282" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="364" y="282" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="272" y="334" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="318" y="334" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="364" y="334" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="450" y="170" width="240" height="230" fill="#f3e6d0" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="472" y="196" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="518" y="196" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="564" y="196" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="610" y="196" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="472" y="248" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="518" y="248" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="564" y="248" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="610" y="248" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="472" y="300" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="518" y="300" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="564" y="300" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="610" y="300" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="720" y="120" width="200" height="280" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="742" y="146" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="788" y="146" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="834" y="146" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="742" y="198" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="788" y="198" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="834" y="198" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="742" y="250" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="788" y="250" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="834" y="250" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="742" y="302" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="788" y="302" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="834" y="302" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="940" y="150" width="240" height="250" fill="#e9dcc8" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="962" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1008" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1054" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1100" y="176" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="962" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1008" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1054" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1100" y="228" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="962" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1008" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1054" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1100" y="280" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="962" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1008" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1054" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1100" y="332" width="26" height="30" fill="#eef5f9" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="195.5" y="260" width="9" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="195.5" y="392" width="4.5" height="2" fill="#1f2933"/>
  <rect x="200" y="374" width="4.5" height="2" fill="#1f2933"/>
  <rect x="195.5" y="356" width="4.5" height="2" fill="#1f2933"/>
  <rect x="200" y="338" width="4.5" height="2" fill="#1f2933"/>
  <rect x="195.5" y="320" width="4.5" height="2" fill="#1f2933"/>
  <rect x="200" y="302" width="4.5" height="2" fill="#1f2933"/>
  <rect x="195.5" y="284" width="4.5" height="2" fill="#1f2933"/>
  <line x1="200" y1="317" x2="173" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="200" y1="297.5" x2="227" y2="279.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="200" y1="282.5" x2="173" y2="264.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="200" cy="267.5" r="30" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="177.5" cy="290" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="222.5" cy="287" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="200" cy="302" r="22.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="685" y="240" width="10" height="170" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="685" y="389.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="690" y="369" width="5" height="2.5" fill="#1f2933"/>
  <rect x="685" y="349" width="5" height="2.5" fill="#1f2933"/>
  <rect x="690" y="328.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="685" y="308" width="5" height="2.5" fill="#1f2933"/>
  <rect x="690" y="287.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="685" y="267" width="5" height="2.5" fill="#1f2933"/>
  <line x1="690" y1="304.5" x2="659.5" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="690" y1="282.5" x2="720.5" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="690" y1="265.5" x2="659.5" y2="245" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="690" cy="248.5" r="34" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="664.5" cy="274" r="27" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="715.5" cy="270.5" r="29" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="690" cy="287.5" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="1155" y="250" width="9.5" height="160" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="1155" y="391" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1160" y="371.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1155" y="352.5" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1160" y="333" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1155" y="314" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1160" y="295" width="5" height="2.5" fill="#1f2933"/>
  <rect x="1155" y="275.5" width="5" height="2.5" fill="#1f2933"/>
  <line x1="1160" y1="311" x2="1131" y2="291.5" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1160" y1="290" x2="1189" y2="271" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="1160" y1="274" x2="1131" y2="255" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="1160" cy="258" r="32" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1136" cy="282" r="25.5" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1184" cy="279" r="27" fill="#2b8a3e" fill-opacity="0.85"/>
  <circle cx="1160" cy="295" r="24" fill="#2b8a3e" fill-opacity="0.85"/>
  <rect x="0" y="400" width="1200" height="34" fill="#d8d2c4"/>
  <line x1="0" y1="400" x2="1200" y2="400" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="0" y="434" width="1200" height="166" fill="#8a939c"/>
  <rect x="0" y="434" width="1200" height="166" fill="none" stroke="#1f2933" stroke-width="2"/>
  <rect x="0" y="524" width="1200" height="14" fill="#6c757d"/>
  <line x1="0" y1="528" x2="1200" y2="528" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="536" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <rect x="10" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="50" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="90" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="130" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="170" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="210" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="250" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="290" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="330" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="370" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="410" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="450" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="490" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="530" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="570" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="610" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="650" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="690" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="730" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="770" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="810" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="850" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="890" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="930" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="970" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="1010" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="1050" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="1090" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="1130" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="1170" y="538" width="20" height="6" fill="#6c757d"/>
  <rect x="40" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="220" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="400" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="580" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="760" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="940" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="1120" y="572" width="90" height="8" fill="#ffffff"/>
  <rect x="105" y="230" width="10" height="204" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="110" y1="318" x2="170" y2="318" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="595" y="230" width="10" height="204" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="600" y1="318" x2="540" y2="318" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="1085" y="230" width="10" height="204" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="1090" y1="318" x2="1030" y2="318" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M0,336 Q600,344 1200,336" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="80" y="284" width="140" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="86" y="296" width="128" height="138" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="86" y1="364" x2="214" y2="364" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <rect x="100" y="390" width="100" height="10" rx="2" fill="#d9b26a" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="236" y="258" width="8" height="176" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="224" y="228" width="32" height="32" rx="6" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="240" cy="244" r="8" fill="#ffffff"/>
  <rect x="970" y="284" width="140" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="976" y="296" width="128" height="138" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="976" y1="364" x2="1104" y2="364" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <rect x="990" y="390" width="100" height="10" rx="2" fill="#d9b26a" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1126" y="258" width="8" height="176" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="1114" y="228" width="32" height="32" rx="6" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1130" cy="244" r="8" fill="#ffffff"/>
  <path d="M342,514 L336,428 Q340,410 364,410 L844,410 Q884,416 890,456 L890,514 Z" fill="url(#fy9li-tram-body)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="342" y="484" width="548" height="18" fill="#1971c2"/>
  <rect x="350" y="396" width="490" height="14" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="507.5" y="416" width="18" height="96" fill="#c9d2da" stroke="#1f2933" stroke-width="2"/>
  <rect x="694.5" y="416" width="18" height="96" fill="#c9d2da" stroke="#1f2933" stroke-width="2"/>
  <rect x="356" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="401" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="446" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="405.5" y="432" width="36" height="78" rx="4" fill="#9fb8c8" stroke="#1f2933" stroke-width="2"/>
  <line x1="423.5" y1="434" x2="423.5" y2="508" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="542.5" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="587.5" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="632.5" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="592" y="432" width="36" height="78" rx="4" fill="#9fb8c8" stroke="#1f2933" stroke-width="2"/>
  <line x1="610" y1="434" x2="610" y2="508" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="729.5" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="774" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="819" y="432" width="35" height="46" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="778.5" y="432" width="36" height="78" rx="4" fill="#9fb8c8" stroke="#1f2933" stroke-width="2"/>
  <line x1="796.5" y1="434" x2="796.5" y2="508" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M850,416 Q882,422 886,456 L850,456 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="880" cy="498" r="6" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="373.5" y="510" width="100" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="393.5" cy="522" r="11" fill="#1f2933"/>
  <circle cx="393.5" cy="522" r="4" fill="#c4ccd4"/>
  <circle cx="453.5" cy="522" r="11" fill="#1f2933"/>
  <circle cx="453.5" cy="522" r="4" fill="#c4ccd4"/>
  <rect x="560" y="510" width="100" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="580" cy="522" r="11" fill="#1f2933"/>
  <circle cx="580" cy="522" r="4" fill="#c4ccd4"/>
  <circle cx="640" cy="522" r="11" fill="#1f2933"/>
  <circle cx="640" cy="522" r="4" fill="#c4ccd4"/>
  <rect x="746.5" y="510" width="100" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="766.5" cy="522" r="11" fill="#1f2933"/>
  <circle cx="766.5" cy="522" r="4" fill="#c4ccd4"/>
  <circle cx="826.5" cy="522" r="11" fill="#1f2933"/>
  <circle cx="826.5" cy="522" r="4" fill="#c4ccd4"/>
  <line x1="620" y1="396" x2="650" y2="358" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="680" y1="396" x2="650" y2="358" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="626" y1="358" x2="674" y2="358" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="200" y1="440" x2="310" y2="440" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <line x1="230" y1="468" x2="320" y2="468" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
  <line x1="190" y1="496" x2="310" y2="496" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
</svg>

## Key idea

Motion is always described in a chosen coordinate system: a straight $x$ axis, an origin, a positive direction and a clock. The **position** $x$ tells you where a body is, the **displacement** $\Delta x$ the change in position and the **velocity** $v$ how fast and in which direction the position changes. The **acceleration** $a$ tells you how fast the velocity changes. The sign of the displacement, the velocity and the acceleration gives the direction. The distance is the length of the route, and it is never negative.

The same motion can be shown as three graphs: $(t,x)$, $(t,v)$ and $(t,a)$. You move between the graphs in two ways. Downwards: the **slope** of a graph is the value of the next quantity, so the slope of the $(t,x)$ graph is the velocity and the slope of the $(t,v)$ graph the acceleration. Upwards: the **area** between a graph and the time axis is the change in the previous quantity, so the area of the $(t,v)$ graph is the displacement.

<svg data-fig="kartta" viewBox="0 0 400 600" role="img" aria-label="Concept map of three graphs one above the other. At the top the position graph, with the straight line of uniform motion and the upward-bending curve of uniformly accelerated motion. In the middle the velocity graph, with a horizontal line and a rising line. At the bottom the acceleration graph, with zero and a constant. On the right, arrows pointing down: the slope of a graph is the value of the next quantity, v = Δx/Δt and a = Δv/Δt. The position graphs are black, the velocity graphs blue and the acceleration graphs orange; uniform motion is a solid line and uniformly accelerated motion a dashed line. On the left, arrows pointing up: the area between a graph and the time axis is the change in the previous quantity, Δx and Δv." style="max-width:100%;font-size:21px">
  <rect x="92" y="14" width="216" height="136" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="104" y="21.5" width="63" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$(t,x)$</div></foreignObject>
  <foreignObject x="213" y="23" width="83" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{position}$</div></foreignObject>
  <line x1="116" y1="134" x2="288" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="134" x2="116" y2="46" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <polyline points="116,134 124,131 132.5,128 140.5,125 149,122 157,119 165,116 173.5,113 181.5,110 190,107 198,104 206,101 214.5,98 222.5,95 231,92 239,89 247,86 255.5,83 263.5,80 272,77 280,74" fill="none" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <polyline points="116,134 124,133 132.5,132 140.5,130.5 149,129 157,127 165,124.5 173.5,121.5 181.5,118.5 190,115 198,111 206,107 214.5,102.5 222.5,97.5 231,92.5 239,87 247,81 255.5,74.5 263.5,68 272,61 280,54" fill="none" stroke="#1f2933" stroke-width="3" stroke-dasharray="9 6" stroke-linecap="round"/>
  <line x1="338" y1="156" x2="338" y2="184" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M338,196 L332,183 L344,183 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="62" y1="196" x2="62" y2="168" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M62,156 L68,169 L56,169 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="352" y="163.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\tfrac{\Delta x}{\Delta t}$</div></foreignObject>
  <foreignObject x="18" y="163.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <rect x="92" y="202" width="216" height="136" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="104" y="209.5" width="63" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$(t,v)$</div></foreignObject>
  <foreignObject x="213" y="211" width="83" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{velocity}$</div></foreignObject>
  <line x1="116" y1="322" x2="288" y2="322" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="322" x2="116" y2="234" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <polyline points="116,278 124,278 132.5,278 140.5,278 149,278 157,278 165,278 173.5,278 181.5,278 190,278 198,278 206,278 214.5,278 222.5,278 231,278 239,278 247,278 255.5,278 263.5,278 272,278 280,278" fill="none" stroke="#1971c2" stroke-width="3" stroke-linecap="round"/>
  <polyline points="116,312.5 124,309 132.5,306 140.5,303 149,299.5 157,296.5 165,293 173.5,290 181.5,287 190,283.5 198,280.5 206,277 214.5,274 222.5,271 231,267.5 239,264.5 247,261 255.5,258 263.5,255 272,251.5 280,248.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-dasharray="9 6" stroke-linecap="round"/>
  <line x1="338" y1="344" x2="338" y2="372" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M338,384 L332,371 L344,371 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="62" y1="384" x2="62" y2="356" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M62,344 L68,357 L56,357 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <foreignObject x="352" y="351.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\tfrac{\Delta v}{\Delta t}$</div></foreignObject>
  <foreignObject x="18" y="351.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#2b8a3e">$\Delta v$</div></foreignObject>
  <rect x="92" y="390" width="216" height="136" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="104" y="397.5" width="63" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$(t,a)$</div></foreignObject>
  <foreignObject x="176" y="399" width="120" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{acceleration}$</div></foreignObject>
  <line x1="116" y1="510" x2="288" y2="510" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="510" x2="116" y2="422" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <polyline points="116,510 124,510 132.5,510 140.5,510 149,510 157,510 165,510 173.5,510 181.5,510 190,510 198,510 206,510 214.5,510 222.5,510 231,510 239,510 247,510 255.5,510 263.5,510 272,510 280,510" fill="none" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <polyline points="116,466 124,466 132.5,466 140.5,466 149,466 157,466 165,466 173.5,466 181.5,466 190,466 198,466 206,466 214.5,466 222.5,466 231,466 239,466 247,466 255.5,466 263.5,466 272,466 280,466" fill="none" stroke="#e8590c" stroke-width="3" stroke-dasharray="9 6" stroke-linecap="round"/>
  <line x1="14" y1="534" x2="386" y2="534" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="14" y="545.5" width="77" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$\downarrow\ \text{slope}$</div></foreignObject>
  <foreignObject x="320" y="545.5" width="66" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#2b8a3e">$\uparrow\ \text{area}$</div></foreignObject>
  <line x1="14" y1="590" x2="50" y2="590" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="58" y="579" width="74" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\text{uniform}$</div></foreignObject>
  <line x1="150" y1="590" x2="186" y2="590" stroke="#1f2933" stroke-width="3" stroke-linecap="butt" stroke-dasharray="9 6"/>
  <foreignObject x="194" y="579" width="195" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\text{uniformly accelerated}$</div></foreignObject>
</svg>

A motion problem in the exam starts with choosing the coordinate system and identifying the type of motion: is the velocity constant or the acceleration constant? Only then do you write the equation.

This answers the opening question. The velocity tells you how many metres the tram travels in a second, so the product of velocity and time is in metres. The area under the $(t,v)$ graph is exactly this product added up over the whole trip, that is, the displacement. The tram in the Investigate task travelled $450\,\text{m}$ from one stop to the next.

## Formula: Equations and graphs of motion

### Uniform motion

The average velocity is the displacement divided by the time it took:

```kaavat
average velocity :: \overline{v}_\text{k} = \frac{\Delta\overline{x}}{\Delta t}
```

where $\Delta\overline{x}$ is the displacement ($\text{m}$) and $\Delta t$ the time elapsed ($\text{s}$). In linear motion the signed displacement $\Delta x = x_2 - x_1$ is enough, and the average velocity is $v_\text{k} = \tfrac{\Delta x}{\Delta t}$. When the velocity $v$ is constant and the body is at the position $x_0$ at $t = 0$,

```kaavat
position in uniform linear motion :: x = x_0 + v\,t
```

This is the straight line of the $(t,x)$ graph: $x_0$ is its intercept on the position axis and $v$ its slope. The position is directly proportional to the time only when $x_0 = 0$.

### Uniformly accelerated motion

Acceleration is the change in velocity per unit of time:

```kaavat
average acceleration :: \overline{a}_\text{k} = \frac{\Delta\overline{v}}{\Delta t}
```

When the acceleration is constant and the motion rectilinear, the velocity and the position at time $t$ are

```kaavat
velocity in uniformly accelerated linear motion :: v = v_0 + a\,t
position in uniformly accelerated linear motion :: x = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2
```

where $v_0$ is the initial velocity ($\text{m/s}$) and $a$ the acceleration ($\text{m/s}^2$). The speed increases when $a$ and $v$ point in the same direction and decreases when they point in opposite directions. In free fall $a = g = 9.81\,\text{m/s}^2$ downwards when air resistance is small.

### Slope and area

The instantaneous velocity on a curved $(t,x)$ graph is the slope $k$ of the tangent. A ratio calculated through two points of the curve is the average velocity. The displacement is the area between the $(t,v)$ graph and the time axis, and the part below the axis is counted as negative. In uniformly accelerated motion the region is a trapezium, so the average velocity is the mean of the initial and final velocities:

```kaavat
displacement in uniformly accelerated linear motion :: \Delta x = \frac{v_0 + v}{2}\,t
```

<svg data-fig="kuvaajat" viewBox="0 0 440 650" role="img" aria-label="Schematic of one motion as two graphs with the same time axis. Below, the velocity graph: the velocity grows uniformly from zero until t1, stays constant until t2 and falls uniformly to zero at t3. The region under the graph is coloured green, and its area is the displacement Δx. Above, the position graph: first a curve bending upwards, then a rising straight line and finally a curve that levels off to horizontal. Over the whole motion the position grows by Δx in total. A blue tangent is drawn at the point P of the curve; its slope k is the velocity v_P, and the same value is marked in the lower graph." style="max-width:100%;font-size:21px">
  <line x1="49" y1="280" x2="370" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,280 L369,286 L369,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="281" x2="50" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,48 L56,61 L44,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="280" x2="127.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="280" x2="244" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="280" x2="321" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="267.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="19.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$x$</div></foreignObject>
  <line x1="49" y1="590" x2="370" y2="590" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M382,590 L369,596 L369,584 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="591" x2="50" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M50,388 L56,401 L44,401 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="127.5" y1="590" x2="127.5" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="244" y1="590" x2="244" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="321" y1="590" x2="321" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="388" y="577.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$t$</div></foreignObject>
  <foreignObject x="40" y="359.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px">$v$</div></foreignObject>
  <polygon points="50,590 127.5,451.5 244,451.5 321,590" fill="#b2f2bb" fill-opacity="0.8"/>
  <line x1="127.5" y1="241" x2="127.5" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="244" y1="124.5" x2="244" y2="451.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="321" y1="85.5" x2="321" y2="590" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="50,280 52.5,280 54.5,280 57,279.5 59,279.5 61.5,279 63.5,279 66,278.5 68,278 70.5,277.5 72.5,276.5 75,276 77,275 79.5,274.5 81.5,273.5 84,272.5 86,271.5 88.5,270.5 90.5,269.5 93,268 95,267 97.5,265.5 99.5,264 102,262.5 104,261 106.5,259.5 109,257.5 111,256 113.5,254 115.5,252 118,250 120,248 122.5,246 124.5,244 127,242 129,239.5 131.5,237 133.5,235 136,232.5 138,230.5 140.5,228 142.5,226 145,223.5 147,221.5 149.5,219 151.5,217 154,214.5 156,212.5 158.5,210 161,207.5 163,205.5 165.5,203 167.5,201 170,198.5 172,196.5 174.5,194 176.5,192 179,189.5 181,187.5 183.5,185 185.5,183 188,180.5 190,178 192.5,176 194.5,173.5 197,171.5 199,169 201.5,167 203.5,164.5 206,162.5 208,160 210.5,158 213,155.5 215,153.5 217.5,151 219.5,149 222,146.5 224,144 226.5,142 228.5,139.5 231,137.5 233,135 235.5,133 237.5,130.5 240,128.5 242,126 244.5,124 246.5,121.5 249,119.5 251,117.5 253.5,115.5 255.5,113.5 258,111.5 260,109.5 262.5,108 264.5,106 267,104.5 269.5,103 271.5,101.5 274,100 276,99 278.5,97.5 280.5,96.5 283,95 285,94 287.5,93 289.5,92 292,91 294,90.5 296.5,89.5 298.5,89 301,88 303,87.5 305.5,87 307.5,86.5 310,86.5 312,86 314.5,86 316.5,85.5 319,85.5 321,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="321,85.5 352,85.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="50,590 127.5,451.5 244,451.5 321,590 352,590" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90.5,270.5 158.5,223" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <line x1="104" y1="261" x2="104" y2="493" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="3 4"/>
  <circle cx="104" cy="261" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="73" y="244.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$P$</div></foreignObject>
  <foreignObject x="164.5" y="238.5" width="52" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#1971c2">$k = v_\text{P}$</div></foreignObject>
  <circle cx="104" cy="493" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="62" y="466.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$v_\text{P}$</div></foreignObject>
  <foreignObject x="170.5" y="515" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <line x1="350" y1="280" x2="356" y2="280" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="350" y1="85.5" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <line x1="356" y1="280" x2="356" y2="85.5" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="364" y="170.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:21px;color:#2b8a3e">$\Delta x$</div></foreignObject>
  <foreignObject x="112.5" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_1$</div></foreignObject>
  <foreignObject x="229" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_2$</div></foreignObject>
  <foreignObject x="306" y="601.5" width="30" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$t_3$</div></foreignObject>
  <foreignObject x="21" y="597.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
  <foreignObject x="21" y="287.5" width="19" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px">$0$</div></foreignObject>
</svg>

### Two bodies and measurement data

The positions of two bodies are written in the same coordinate system, and the bodies meet when

```kaavat
condition for meeting :: x_\text{A}(t) = x_\text{B}(t)
```

In a $(t,x)$ graph a meeting is the crossing point of the lines. The upper line means a greater position coordinate. When the body behind is slower at first and accelerates, the distance between the bodies is at its greatest when their velocities are equal.

A straight line or a quadratic polynomial $x = A\,t^2 + B\,t + C$ is fitted to measured points. The acceleration is found from the coefficient of the polynomial: $a = 2A$.

## Common mistakes {Virheet}

- **The $(t,x)$ graph is read as a picture of the route.** A rising line means that the position grows, not an uphill.
- **The velocity is read as $x : t$ when it should be $\Delta x : \Delta t$.** The initial position is not velocity.
- **The slope from two adjacent measured points.** Read it from the fitted line or the tangent, from two points far apart.
- **A negative acceleration is always read as slowing down.** The speed decreases only when the acceleration and the velocity point in opposite directions.
- **At the highest point the acceleration is zero.** The velocity is zero for an instant, but the acceleration is still $g$ downwards.
- **The crossing point of $(t,v)$ graphs is read as a meeting.** There the velocities are equal; at a meeting it is the positions that are equal.
- **Mixed-up units.** Convert the units before you substitute, by writing them out: $72\,\text{km/h} = \dfrac{72 \cdot 1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$.

## Review if needed {Kertaa}

- Uniform motion, $x = x_0 + vt$ and unit conversions: [*Uniform motion: speed, position and graphs*](fy1-5.html).
- Position, displacement, average velocity and the slope of the $(t,x)$ graph: [*Position, velocity and uniform motion as graphs*](fy4-1.html).
- Acceleration, the tangent, the area and free fall: [*Acceleration and uniformly accelerated motion*](fy4-2.html).
- Meeting, overtaking and the greatest distance: [*Comparing the motions of two bodies*](fy4-12.html).
- Fitting a straight line and the slope from data: [*Graphing and fitting a straight line*](fy1-4.html). Measurement uncertainty: [*Measuring and the reliability of a measurement*](fy1-3.html).
