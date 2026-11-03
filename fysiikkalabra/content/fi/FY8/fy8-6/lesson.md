# LEDin valo ja Planckin vakion mittaaminen

> **Miksi** sininen LED tarvitsee syttyäkseen suuremman jännitteen kuin punainen LED?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä on säädettävä jännitelähde, josta punainen ja musta johto vievät virran kytkentälevylle. Levyllä on rinnakkain neljä LEDiä samassa jännitteessä. Punainen ja keltainen LED loistavat kirkkaasti ja lähettävät valoaan aaltoviivoina, vihreä hehkuu himmeästi, ja sininen LED on pimeä." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy86h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy86h-case" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><radialGradient id="fy86h-g630" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="#db3d00" stop-opacity="0.8"/><stop offset="1" stop-color="#db3d00" stop-opacity="0"/></radialGradient><radialGradient id="fy86h-g590" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="#dbad00" stop-opacity="0.8"/><stop offset="1" stop-color="#dbad00" stop-opacity="0"/></radialGradient><radialGradient id="fy86h-g525" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="#3fc600" stop-opacity="0.8"/><stop offset="1" stop-color="#3fc600" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="440" fill="#f6f1e6"/>
  <line x1="0" y1="0" x2="0" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="75" y1="0" x2="75" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="0" x2="150" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="225" y1="0" x2="225" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="0" x2="300" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="375" y1="0" x2="375" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="0" x2="450" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="525" y1="0" x2="525" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="0" x2="600" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="675" y1="0" x2="675" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="750" y1="0" x2="750" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="825" y1="0" x2="825" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="900" y1="0" x2="900" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="975" y1="0" x2="975" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="0" x2="1050" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1125" y1="0" x2="1125" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="0" x2="1200" y2="440" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="75" x2="1200" y2="75" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="1200" y2="150" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="225" x2="1200" y2="225" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="1200" y2="300" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="375" x2="1200" y2="375" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="30" y="440" width="1140" height="40" rx="4" fill="url(#fy86h-table)" stroke="#1f2933" stroke-width="3"/>
  <path d="M40,450 q285,-2.5 570,0 t550,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M40,460 q285,-2.5 570,0 t550,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M40,470 q285,-2.5 570,0 t550,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <rect x="70" y="480" width="30" height="100" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="1100" y="480" width="30" height="100" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="90" y="250" width="250" height="190" rx="10" fill="url(#fy86h-case)" stroke="#1f2933" stroke-width="3"/>
  <rect x="118" y="276" width="194" height="64" rx="6" fill="#1f2933"/>
  <rect x="140" y="294" width="34" height="30" rx="3" fill="#c92a2a"/>
  <rect x="194" y="286" width="34" height="38" rx="3" fill="#c92a2a"/>
  <rect x="248" y="302" width="34" height="22" rx="3" fill="#c92a2a"/>
  <circle cx="170" cy="390" r="28" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <line x1="170" y1="390" x2="186" y2="370" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="262" cy="392" r="13" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="306" cy="392" r="13" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="420" y="392" width="680" height="48" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="436" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="436" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="455.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="455.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="475" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="475" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="494.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="494.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="514" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="514" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="533.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="533.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="553" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="553" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="572.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="572.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="592" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="592" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="611.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="611.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="631" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="631" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="650.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="650.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="670" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="670" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="689.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="689.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="709" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="709" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="728.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="728.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="748" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="748" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="767.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="767.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="787" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="787" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="806.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="806.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="826" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="826" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="845.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="845.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="865" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="865" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="884.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="884.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="904" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="904" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="923.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="923.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="943" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="943" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="962.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="962.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="982" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="982" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1001.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1001.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1021" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1021" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1040.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1040.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1060" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1060" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1079.5" y="404" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <rect x="1079.5" y="420" width="6" height="6" rx="1" fill="#c9c2b2"/>
  <path d="M262,392 C262,470 380,470 420,404" fill="none" stroke="#c92a2a" stroke-width="6" stroke-linejoin="round"/>
  <path d="M306,392 C306,500 400,500 432,432" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round"/>
  <circle cx="560" cy="300" r="130" fill="url(#fy86h-g630)" fill-opacity="0.85"/>
  <line x1="548" y1="352" x2="548" y2="404" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <line x1="572" y1="352" x2="572" y2="410" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,352 L530,300 A30,30 0 0 1 590,300 L590,352 Z" fill="#db3d00" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" fill-opacity="1"/>
  <rect x="524" y="348" width="72" height="10" rx="3" fill="#db3d00" stroke="#1f2933" stroke-width="3"/>
  <polyline points="522,268 521,267 520,265 519.5,263.5 518,263 515.5,263.5 513,265.5 510.5,266.5 509,266.5 508,264.5 508,262 508.5,258.5 508.5,255.5 507.5,254 506,254 503.5,255 500.5,256.5 498,258 496,258.5 495,258 494.5,255.5 494.5,252 494.5,249 494.5,246.5 493,246 491,246.5 488.5,248 485.5,249.5 483.5,251 481.5,250.5 481,249 481,246 481,242.5 481,240 480,238 478.5,238 476,239 473.5,241 471,242.5 469,243 467.5,242 467,239.5 467.5,236.5 467.5,233.5 467,231 466,230 464,230.5 461,232 458.5,234 456,235 454.5,235 453.5,233 453.5,230.5 454,227 453.5,224.5 452,224 450,224 448,224.5 446.5,224.5" fill="none" stroke="#db3d00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M430,215 L450,216 L441,232 Z" fill="#db3d00" stroke-linejoin="round"/>
  <polyline points="545,248.5 545,247 545.5,245 546,243.5 545.5,242 543,241.5 540,241 537.5,240.5 536,239 536.5,237.5 538.5,235 540.5,232.5 542.5,230.5 543,228.5 542,227.5 539.5,227 536,226.5 533,226 531,225 531,223.5 532,221.5 534,219 536.5,216.5 537.5,214.5 537,213 535.5,212.5 532.5,212 529,211.5 526.5,210.5 525.5,209.5 526,207.5 527.5,205.5 530,203 531.5,201 532,199 531,198 528.5,197 525.5,197 522.5,196.5 520.5,195.5 520,194 521.5,192 523.5,189.5 525.5,187 527,185 526.5,183.5 524.5,182.5 521.5,182 518.5,181.5 515.5,181 514.5,180 515,178 517,176 519,173.5 520.5,171.5 520,170 518.5,169 516.5,168 515,167" fill="none" stroke="#db3d00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M508.5,149 L523.5,163 L506.5,169 Z" fill="#db3d00" stroke-linejoin="round"/>
  <polyline points="575,248.5 576,247.5 577.5,246.5 579,245.5 579.5,244 578.5,242 576,239.5 574.5,237.5 574.5,235.5 576,234.5 579,234 582,233.5 585,233 586.5,232 586.5,230.5 585,228.5 582.5,226 580.5,223.5 579.5,221.5 580.5,220.5 582.5,219.5 586,219 589,218.5 591,218 592,216.5 591,214.5 589,212.5 587,210 585.5,207.5 585,206 587,205 589.5,204.5 593,204 595.5,203.5 597,202.5 597,201 595.5,198.5 593.5,196 591.5,194 590.5,192 591,190.5 593.5,190 596.5,189.5 600,189 602,188 602.5,187 602,185 600,182.5 597.5,180.5 596,178 596,176.5 597.5,175.5 600.5,175 603.5,174.5 606,173.5 606.5,172.5 606,170.5 605,168.5 604.5,167" fill="none" stroke="#db3d00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M611.5,149 L613.5,169 L596.5,163 Z" fill="#db3d00" stroke-linejoin="round"/>
  <polyline points="598,268 599.5,267.5 601.5,268 603.5,268 604.5,267 605,265 605,261.5 605,259 606,257.5 608,258 610.5,259 613,261 615.5,262.5 617.5,262.5 618.5,261 618.5,258.5 618.5,255.5 618.5,252.5 619,250.5 620.5,249.5 622.5,250.5 625.5,252 628,254 630.5,255 631.5,254 632.5,252 632.5,249 632,246 632.5,243 633.5,242 635,242 637.5,243.5 640.5,245.5 643,246.5 645,247 645.5,245.5 646,243 646,239.5 646,236.5 646.5,234.5 647.5,234 650,235 652.5,236.5 655.5,238 657.5,239 659,238.5 659.5,236.5 659.5,233.5 659.5,230 659.5,227.5 660.5,226 662.5,226.5 665,227.5 667.5,229.5 670,230.5 671.5,229.5 672,228 672.5,226 673.5,224.5" fill="none" stroke="#db3d00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M690,215 L679,232 L670,216 Z" fill="#db3d00" stroke-linejoin="round"/>
  <circle cx="700" cy="300" r="130" fill="url(#fy86h-g590)" fill-opacity="0.85"/>
  <line x1="688" y1="352" x2="688" y2="404" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <line x1="712" y1="352" x2="712" y2="410" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <path d="M670,352 L670,300 A30,30 0 0 1 730,300 L730,352 Z" fill="#dbad00" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" fill-opacity="1"/>
  <rect x="664" y="348" width="72" height="10" rx="3" fill="#dbad00" stroke="#1f2933" stroke-width="3"/>
  <polyline points="662,268 661,267 660,265 659.5,263.5 657.5,263 655.5,264.5 652.5,266.5 650.5,267 649,266 649,263.5 649,260 649.5,257 649,254.5 647.5,254.5 645,255.5 642,257.5 639.5,259 637.5,259.5 636.5,258.5 636,255.5 636.5,252 636.5,249 636,247 634,247 631.5,248.5 629,250.5 626,252 624.5,252 623.5,250.5 623.5,247.5 623.5,244 623.5,241 623,239.5 621,240 618.5,241.5 615.5,243.5 613,244.5 611.5,244.5 610.5,243 610.5,239.5 611,236 611,233.5 610,232 608,232.5 605,234.5 602.5,236 600,237.5 598.5,237 598,235 598,231.5 598,228.5 598,226 597,225 594.5,225.5 592,227.5 589.5,228.5 588,228 587,226.5 586.5,225" fill="none" stroke="#dbad00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M570,215 L590,216 L581,232 Z" fill="#dbad00" stroke-linejoin="round"/>
  <polyline points="685,248.5 685,247 685.5,245 686,243.5 685,242.5 682,241.5 679,241.5 677,240.5 676.5,239 678,237 680.5,234.5 682.5,232 683.5,230 682.5,229 680,228 676.5,228 673.5,227.5 671.5,226.5 671.5,225 673.5,222.5 675.5,220 677.5,218 678.5,216 677,215 674.5,214 671,214 668,213.5 666.5,212.5 666.5,210.5 668.5,208.5 671,206 673,203.5 673,202 671.5,201 668.5,200.5 665.5,200 662.5,199.5 661.5,198 662,196.5 664,194 666.5,191.5 668,189.5 668,188 666.5,187 663,186.5 659.5,186 657,185.5 656,184 657,182 659.5,180 661.5,177.5 663,175 663,173.5 661,173 657.5,172.5 655,172 654,170.5 654.5,169 655,167" fill="none" stroke="#dbad00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M648.5,149 L663.5,163 L646.5,169 Z" fill="#dbad00" stroke-linejoin="round"/>
  <polyline points="715,248.5 716,247.5 718,246.5 719,245.5 719,243.5 717.5,241.5 715,239 714,237 715,236 717.5,235 720.5,234.5 724,234.5 726,233.5 726,232 724.5,229.5 722,227 720,225 719,223 720,222 723,221 726.5,221 729.5,220.5 731,219.5 731,217.5 729,215.5 726.5,213 724.5,210.5 724,209 725.5,208 728.5,207 732,207 735,206.5 736,205.5 735.5,203.5 733.5,201 731.5,198.5 729.5,196.5 729.5,195 731,194 734,193.5 737.5,193 740,192.5 741.5,191 740.5,189.5 738.5,187 736,184.5 734.5,182.5 734.5,180.5 736.5,180 739.5,179.5 743,179 745.5,178.5 746.5,177 745,175 743,172.5 741.5,170.5 741.5,169 743,168 744.5,167" fill="none" stroke="#dbad00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M751.5,149 L753.5,169 L736.5,163 Z" fill="#dbad00" stroke-linejoin="round"/>
  <polyline points="738,268 739.5,267.5 741.5,268 743.5,268 744.5,267 744.5,264 744.5,260.5 745,258.5 746,258 748.5,259 751.5,261 754,262.5 756,263.5 757,262 757.5,259.5 757,256 757,253 757.5,251 759.5,250.5 762,252 764.5,254 767.5,255.5 769,256 770,254.5 770,251.5 770,248 770,245 770.5,243.5 772.5,243.5 775,245 778,247 780.5,248.5 782,248.5 783,246.5 783,243.5 782.5,240 783,237.5 783.5,236 785.5,236 788,238 791,240 793.5,241 795,241 796,239 795.5,235.5 795.5,232.5 795.5,229.5 796.5,228.5 799,229 801.5,231 804.5,232.5 806.5,233.5 808,233 808.5,231 808.5,227.5 808.5,225 809.5,224 811.5,224 813.5,224" fill="none" stroke="#dbad00" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M830,215 L819,232 L810,216 Z" fill="#dbad00" stroke-linejoin="round"/>
  <circle cx="840" cy="300" r="62.5" fill="url(#fy86h-g525)" fill-opacity="0.475"/>
  <line x1="828" y1="352" x2="828" y2="404" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <line x1="852" y1="352" x2="852" y2="410" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <path d="M810,352 L810,300 A30,30 0 0 1 870,300 L870,352 Z" fill="#3fc600" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" fill-opacity="0.685"/>
  <rect x="804" y="348" width="72" height="10" rx="3" fill="#3fc600" stroke="#1f2933" stroke-width="3"/>
  <line x1="968" y1="352" x2="968" y2="404" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <line x1="992" y1="352" x2="992" y2="410" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <path d="M950,352 L950,300 A30,30 0 0 1 1010,300 L1010,352 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" fill-opacity="0.685"/>
  <rect x="944" y="348" width="72" height="10" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
</svg>

## Ydinajatus

### LED on puolijohdekomponentti
**LED** eli **valodiodi** on puolijohteesta valmistettu diodi: se päästää sähkövirtaa läpi vain yhteen suuntaan ja säteilee valoa, kun virta kulkee. Luvussa *Spektrit paljastavat atomin energiatasot* nähtiin, että yksittäisen atomin elektronilla on vain tietyt energiatasot. Kiinteässä aineessa atomit ovat niin lähellä toisiaan, että niiden energiatasot sulautuvat leveiksi **energiavöiksi**. Puolijohteessa elektronien lähes täyttämän **valenssivyön** ja lähes tyhjän **johtavuusvyön** välissä on **energia-aukko** $E_\text{g}$: energiaväli, jolla elektronilla ei voi olla tilaa.

### Elektroni putoaa aukkoon, ja fotoni syntyy
LED on tehty kahdesta erilaisesta puolijohteesta. Toisen, n-alueen, johtavuusvyössä on vapaita elektroneja. Toisen, p-alueen, valenssivyössä on tyhjiä elektronin paikkoja eli **aukkoja**. Kun LEDin läpi kulkee virta, elektronit ja aukot kohtaavat alueiden rajapinnalla. Elektroni putoaa johtavuusvyöstä valenssivyön aukkoon ja luovuttaa energiansa yhtenä fotonina. Fotonin energia on likimain energia-aukon suuruinen, $hf \approx E_\text{g}$. LEDin väri riippuu siis puolijohdemateriaalista: punaisen LEDin puolijohteessa energia-aukko on noin $1{,}9\,\text{eV}$, sinisen noin $2{,}6\,\text{eV}$.

<svg data-fig="vyot" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei mittakaavassa: LEDin puolijohteen energiavyöt. Pystysuunnassa on energia. Ylhäällä on johtavuusvyö ja alhaalla valenssivyö, ja niiden välissä on energia-aukko E g, jonka energioilla elektronilla ei voi olla tilaa. Pystysuora katkoviiva on rajapinta: vasemmalla on n-alue, jonka johtavuusvyössä on sinisiä elektroneja e miinus, oikealla p-alue, jonka valenssivyössä on tyhjiä paikkoja eli aukkoja valkoisina ympyröinä. Rajapinnalla elektroni putoaa johtavuusvyöstä valenssivyön aukkoon, ja siitä lähtee oikealle punainen aaltoviivanuoli, fotoni, jonka energia hf on likimain energia-aukon suuruinen." style="max-width:100%;font-size:24px">
  <line x1="26" y1="300" x2="26" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M26,34 L32,47 L20,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="40" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <rect x="200" y="54" width="340" height="56" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="200" y="226" width="340" height="56" rx="4" fill="#e3dccb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="67.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{johtavuusvyö}$</div></foreignObject>
  <foreignObject x="43" y="239.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{valenssivyö}$</div></foreignObject>
  <line x1="370" y1="40" x2="370" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="243.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{n-alue}$</div></foreignObject>
  <foreignObject x="413.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{p-alue}$</div></foreignObject>
  <line x1="222" y1="110" x2="222" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="214" y1="110" x2="230" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="214" y1="226" x2="230" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{g}$</div></foreignObject>
  <circle cx="282" cy="96" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="314" cy="96" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="346" cy="96" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="430" cy="240" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="466" cy="240" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="502" cy="240" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="297.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="431" y="189.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{aukko}$</div></foreignObject>
  <circle cx="370" cy="96" r="8" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="370" y1="106" x2="370" y2="216" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M370,230 L363,214 L377,214 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="370" cy="240" r="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <polyline points="384,168 385.5,168.5 387,170 388.5,171 390,170 391.5,166.5 393,163.5 394.5,162 396,163.5 397.5,166.5 399,170.5 400.5,173.5 402,174 403.5,171.5 405,168 406.5,164.5 408,162 409.5,162.5 411,165.5 412.5,169.5 414,172.5 415.5,174 417,172.5 418.5,169.5 420,165.5 421.5,162.5 423,162 424.5,164.5 426,168 427.5,171.5 429,174 430.5,173.5 432,170.5 433.5,166.5 435,163.5 436.5,162 438,163.5 439.5,166.5 441,170.5 442.5,173.5 444,174 445.5,171.5 447,168 448.5,164.5 450,162 451.5,162.5 453,165.5 454.5,169.5 456,172.5 457.5,174 459,172.5 460.5,169.5 462,165.5 463.5,162.5 465,162 466.5,164.5 468,168 469.5,171.5 471,174 472.5,173.5 474,170.5 475.5,166.5 477,163.5 478.5,162 480,163.5 481.5,166.5 483,170.5 484.5,173.5 486,174 487.5,171.5 489,168 490.5,164.5 492,162 493.5,162.5 495,165.5 496.5,169.5 498,172.5 499.5,174 501,172.5 502.5,169.5 504,165.5 505.5,162.5 507,162 508.5,164.5 510,168 511.5,171.5 513,174 514.5,173.5 516,170.5 517.5,166.5 519,164.5 520.5,164.5 522,166 523.5,167.5 525,168" fill="none" stroke="#db3d00" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M540,168 L525,175.5 L525,160.5 Z" fill="#db3d00" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#db3d00">$hf$</div></foreignObject>
</svg>

### Kynnysjännite
Kun elektroni kulkee jännitteen $U$ yli, sähkökenttä tekee siihen työn $eU$, missä $e$ on alkeisvaraus. Juuri näin määriteltiin elektronivoltti luvussa *Valosähköinen ilmiö ja fotoni*. Jotta elektroni voisi synnyttää fotonin, jonka energia on $E_\text{g}$, sen on saatava jännitelähteeltä vähintään likimain tämä energia. Siksi LED ei pienellä jännitteellä juuri johda virtaa eikä säteile. Virta alkaa kasvaa jyrkästi, kun jännite saavuttaa LEDin **kynnysjännitteen** $U_\text{k}$, jolle $eU_\text{k} \approx E_\text{g} \approx hf$. Sinisen valon fotoni tarvitsee enemmän energiaa kuin punaisen, joten sinisen LEDin kynnysjännite on suurempi.

Kynnysjännitettä suurempi jännite kasvattaa virtaa, eli LEDin läpi kulkee sekunnissa enemmän elektroneja ja syntyy enemmän fotoneja. Yksittäisen fotonin energia ei kuitenkaan kasva, koska sen määrää energia-aukko. Ylimääräinen energia muuttuu LEDissä lämmöksi. LEDin väri pysyy siis samana, kun jännite kasvaa; vain valon kirkkaus kasvaa.

### LED, laserdiodi ja hehkulamppu
Valonlähteitä voi vertailla mittaamalla niiden spektrin spektrometrillä, kuten luvussa *Spektrit paljastavat atomin energiatasot*. Hehkulampun kuuma hehkulanka säteilee jatkuvan spektrin, jossa on kaikkia näkyvän valon aallonpituuksia. LEDin spektri on kapea kaista, jonka leveys on tyypillisesti $20$–$40\,\text{nm}$, koska elektronien ja aukkojen energiat vaihtelevat hieman vöiden reunoilla. LEDin aallonpituudeksi ilmoitetaan spektrin huipun aallonpituus. **Laserdiodi** on LEDin kaltainen puolijohdediodi, jossa valo vahvistuu: sen spektri on hyvin kapea viiva, leveydeltään noin $1\,\text{nm}$, ja valo kulkee kapeana säteenä. Laserin toimintaan palataan luvussa *Laser ja kvanttirakenteet*. Laserdiodin säteeseen ei saa koskaan katsoa.

<svg data-fig="spektrit" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: kolmen valonlähteen spektri samalla aallonpituusakselilla 380–720 nanometriä, pystyakselilla suhteellinen intensiteetti. Hehkulampun spektri on jatkuva: oranssi käyrä nousee tasaisesti violetista punaiseen. Punaisen LEDin spektri on kapea huippu aallonpituudella 630 nanometriä, ja sen leveys on noin 20 nanometriä. Punaisen laserdiodin spektri on hyvin kapea viiva aallonpituudella 650 nanometriä, leveys noin 2 nanometriä. LEDin ja laserdiodin huiput on skaalattu samaan korkeuteen, hehkulampun käyrä matalammaksi." style="max-width:100%;font-size:24px">
  <line x1="106.5" y1="306" x2="106.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="306" x2="163.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="306" x2="220" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="277" y1="306" x2="277" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="334" y1="306" x2="334" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390.5" y1="306" x2="390.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="447.5" y1="306" x2="447.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="198.5" x2="470" y2="198.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="91.5" x2="470" y2="91.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="306" x2="484" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,306 L483,312 L483,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="307" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="106.5" y1="306" x2="106.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="84" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="163.5" y1="306" x2="163.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="141" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$450$</div></foreignObject>
  <line x1="220" y1="306" x2="220" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="197.5" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="277" y1="306" x2="277" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="254.5" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$550$</div></foreignObject>
  <line x1="334" y1="306" x2="334" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311.5" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="390.5" y1="306" x2="390.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="368" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$650$</div></foreignObject>
  <line x1="447.5" y1="306" x2="447.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="425" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="77" y1="198.5" x2="84" y2="198.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="184" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="77" y1="91.5" x2="84" y2="91.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="77" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <foreignObject x="502" y="291.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suhteellinen intensiteetti}$</div></foreignObject>
  <polyline points="95.5,299 98.5,299 101.5,298.5 104.5,298 108,297.5 111,297 114,296.5 117,296 120.5,295.5 123.5,295 126.5,294.5 129.5,294 133,293.5 136,292.5 139,292 142,291.5 145.5,291 148.5,290 151.5,289.5 154.5,289 158,288 161,287.5 164,286.5 167,286 170.5,285 173.5,284 176.5,283.5 179.5,282.5 183,281.5 186,281 189,280 192,279 195.5,278 198.5,277.5 201.5,276.5 204.5,275.5 207.5,274.5 211,273.5 214,272.5 217,271.5 220,270.5 223.5,269.5 226.5,268.5 229.5,267 232.5,266 236,265 239,264 242,263 245,261.5 248.5,260.5 251.5,259.5 254.5,258.5 257.5,257 261,256 264,254.5 267,253.5 270,252.5 273.5,251 276.5,250 279.5,248.5 282.5,247.5 286,246 289,245 292,243.5 295,242.5 298.5,241 301.5,240 304.5,238.5 307.5,237.5 311,236 314,235 317,233.5 320,232 323.5,231 326.5,229.5 329.5,228.5 332.5,227 336,226 339,224.5 342,223 345,222 348,220.5 351.5,219.5 354.5,218 357.5,216.5 360.5,215.5 364,214 367,213 370,211.5 373,210 376.5,209 379.5,207.5 382.5,206.5 385.5,205 389,204 392,202.5 395,201.5 398,200 401.5,199 404.5,197.5 407.5,196.5 410.5,195 414,194 417,192.5 420,191.5 423,190 426.5,189 429.5,188 432.5,186.5 435.5,185.5 439,184.5 442,183 445,182 448,181 451.5,179.5 454.5,178.5 457.5,177.5 460.5,176.5 464,175 467,174 470,173" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="316.5,306 317.5,306 318,306 318.5,306 319,306 319.5,306 320,306 320.5,306 321.5,306 322,306 322.5,306 323,306 323.5,306 324,306 324.5,306 325,306 326,306 326.5,306 327,306 327.5,306 328,306 328.5,306 329,306 330,306 330.5,306 331,306 331.5,306 332,306 332.5,305.5 333,305.5 334,305.5 334.5,305.5 335,305.5 335.5,305 336,305 336.5,305 337,304.5 337.5,304.5 338.5,304 339,303.5 339.5,303 340,302.5 340.5,302 341,301.5 341.5,300.5 342.5,299.5 343,298.5 343.5,297.5 344,296 344.5,294.5 345,292.5 345.5,290.5 346.5,288.5 347,286 347.5,283.5 348,280.5 348.5,277 349,273.5 349.5,269.5 350,265.5 351,261 351.5,256 352,251 352.5,245.5 353,239.5 353.5,233.5 354,227 355,220 355.5,213.5 356,206 356.5,198.5 357,191 357.5,183.5 358,176 358.5,168.5 359.5,160.5 360,153 360.5,146 361,139 361.5,132 362,125.5 362.5,119.5 363.5,114 364,109 364.5,104.5 365,100.5 365.5,97.5 366,95 366.5,93 367.5,92 368,91.5 368.5,92 369,93 369.5,95 370,97.5 370.5,100.5 371,104.5 372,109 372.5,114 373,119.5 373.5,125.5 374,132 374.5,139 375,146 376,153 376.5,160.5 377,168.5 377.5,176 378,183.5 378.5,191 379,198.5 379.5,206 380.5,213.5 381,220 381.5,227 382,233.5 382.5,239.5 383,245.5 383.5,251 384.5,256 385,261 385.5,265.5 386,269.5 386.5,273.5 387,277 387.5,280.5 388.5,283.5 389,286 389.5,288.5 390,290.5 390.5,292.5 391,294.5 391.5,296 392,297.5 393,298.5 393.5,299.5 394,300.5 394.5,301.5 395,302 395.5,302.5 396,303 397,303.5 397.5,304 398,304.5 398.5,304.5 399,305 399.5,305 400,305 400.5,305.5 401.5,305.5 402,305.5 402.5,305.5 403,305.5 403.5,306 404,306 404.5,306 405.5,306 406,306 406.5,306 407,306 407.5,306 408,306 408.5,306 409.5,306 410,306 410.5,306 411,306 411.5,306 412,306 412.5,306 413,306 414,306 414.5,306 415,306 415.5,306 416,306 416.5,306 417,306 418,306 418.5,306 419,306" fill="none" stroke="#db3d00" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="383.5,306 384,306 384,306 384,306 384,306 384.5,306 384.5,306 384.5,306 384.5,306 384.5,306 385,306 385,306 385,306 385,306 385.5,306 385.5,306 385.5,306 385.5,306 386,306 386,306 386,306 386,306 386,306 386.5,306 386.5,306 386.5,306 386.5,306 387,306 387,306 387,305.5 387,305.5 387,305.5 387.5,305 387.5,304.5 387.5,304 387.5,303 388,302 388,300.5 388,298.5 388,296 388.5,292.5 388.5,288.5 388.5,283.5 388.5,277 388.5,269.5 389,261 389,251 389,239.5 389,227 389.5,213.5 389.5,198.5 389.5,183.5 389.5,168.5 389.5,153 390,139 390,125.5 390,114 390,104.5 390.5,97.5 390.5,93 390.5,91.5 390.5,93 391,97.5 391,104.5 391,114 391,125.5 391,139 391.5,153 391.5,168.5 391.5,183.5 391.5,198.5 392,213.5 392,227 392,239.5 392,251 392,261 392.5,269.5 392.5,277 392.5,283.5 392.5,288.5 393,292.5 393,296 393,298.5 393,300.5 393.5,302 393.5,303 393.5,304 393.5,304.5 393.5,305 394,305.5 394,305.5 394,305.5 394,306 394.5,306 394.5,306 394.5,306 394.5,306 394.5,306 395,306 395,306 395,306 395,306 395.5,306 395.5,306 395.5,306 395.5,306 396,306 396,306 396,306 396,306 396,306 396.5,306 396.5,306 396.5,306 396.5,306 397,306 397,306 397,306 397,306 397,306 397.5,306" fill="none" stroke="#db0000" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="113.5" y="188.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{hehkulamppu}$</div></foreignObject>
  <foreignObject x="302.5" y="102.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#db3d00">$\text{LED}$</div></foreignObject>
  <foreignObject x="399.5" y="77" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#db0000">$\text{laserdiodi}$</div></foreignObject>
</svg>

## Kaava: Kynnysjännite ja fotonin energia

### Kynnysjännite ja aallonpituus
Kun LEDin kynnysjännite saavutetaan, elektronin jännitelähteeltä saama energia on likimain yhden fotonin energia:
```latex
eU_\text{k} \approx hf = \frac{hc}{\lambda}
```
missä $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ on alkeisvaraus, $U_\text{k}$ LEDin kynnysjännite ($\text{V}$), $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ Planckin vakio, $f$ valon taajuus ($\text{Hz}$), $c = 2{,}998 \cdot 10^8\,\text{m/s}$ valon nopeus ja $\lambda$ LEDin spektrin huipun aallonpituus ($\text{m}$). Punaisen LEDin, $\lambda = 630\,\text{nm}$, kynnysjännitteeksi tämä antaa $U_\text{k} \approx \tfrac{hc}{e\lambda}$. Luvussa *Valosähköinen ilmiö ja fotoni* laskettiin $hc = 1240\,\text{eV}\,\text{nm}$, ja koska $1\,\text{eV} = e \cdot 1\,\text{V}$, on $\tfrac{hc}{e} = 1240\,\text{V}\,\text{nm}$. Siten $U_\text{k} \approx 1240\,\text{V}\,\text{nm} : 630\,\text{nm} = 1{,}97\,\text{V}$. Mitattu kynnysjännite on yleensä hieman pienempi, esimerkiksi $1{,}88\,\text{V}$. Fotonin energia elektronivoltteina on sama luku kuin kynnysjännite voltteina, koska $1\,\text{eV}$ on energia, jonka elektroni saa $1\,\text{V}$:n jännitteessä.

### Kynnysjännitteen määrittäminen
Kynnysjännite mitataan kytkemällä LED sarjaan suojavastuksen ja virtamittarin kanssa säädettävään jännitelähteeseen ja jännitemittari LEDin napojen väliin. Jännitettä kasvatetaan vähitellen, ja kullakin jännitteellä kirjataan virta. Kuvaajassa $(U, I)$ virta on aluksi lähes nolla ja kasvaa sitten lähes suoraviivaisesti. Kynnysjännite saadaan, kun kuvaajan suoraan osaan sovitettu suora jatketaan jänniteakselille, jolla $I = 0$. Menetelmä on toistettavampi kuin sen jännitteen etsiminen, jolla LED näyttää alkavan hehkua, koska silmän herkkyys vaihtelee eri väreillä ja eri ihmisillä.

<svg data-fig="iu" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: kolmen LEDin virta milliampeereina jännitteen funktiona, jänniteakseli 0–3,5 volttia. Punaisen LEDin virta on lähes nolla noin 1,8 volttiin asti ja kasvaa sitten suoraviivaisesti. Vihreän LEDin käyrä on samanmuotoinen mutta oikealla, sinisen vielä oikeammalla. Kunkin käyrän suora osa on jatkettu katkoviivalla jänniteakselille, ja leikkauskohta on LEDin kynnysjännite U k: punaisella 1,88, vihreällä 2,30 ja sinisellä 2,52 volttia." style="max-width:100%;font-size:24px">
  <line x1="148.5" y1="322" x2="148.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207" y1="322" x2="207" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="265.5" y1="322" x2="265.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324.5" y1="322" x2="324.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383" y1="322" x2="383" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="441.5" y1="322" x2="441.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="322" x2="500" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="279" x2="500" y2="279" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="236" x2="500" y2="236" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="193" x2="500" y2="193" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="150" x2="500" y2="150" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="107" x2="500" y2="107" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="64" x2="500" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="322" x2="514" y2="322" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,322 L513,328 L513,316 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="323" x2="90" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,38 L96,51 L84,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="148.5" y1="322" x2="148.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="126" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="207" y1="322" x2="207" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="184.5" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <line x1="265.5" y1="322" x2="265.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="243" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="324.5" y1="322" x2="324.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="302" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}0$</div></foreignObject>
  <line x1="383" y1="322" x2="383" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="360.5" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="441.5" y1="322" x2="441.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="419" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}0$</div></foreignObject>
  <line x1="500" y1="322" x2="500" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="477.5" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}5$</div></foreignObject>
  <line x1="83" y1="279" x2="90" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="264.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="83" y1="236" x2="90" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="83" y1="193" x2="90" y2="193" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="178.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="83" y1="150" x2="90" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="83" y1="107" x2="90" y2="107" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="92.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="83" y1="64" x2="90" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <foreignObject x="60" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="307.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="80" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{mA})$</div></foreignObject>
  <polyline points="310,322 338.5,207.5" fill="none" stroke="#db3d00" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,322 91.5,322 93,322 94.5,322 95.5,322 97,322 98.5,322 100,322 101.5,322 103,322 104,322 105.5,322 107,322 108.5,322 110,322 111.5,322 112.5,322 114,322 115.5,322 117,322 118.5,322 120,322 121,322 122.5,322 124,322 125.5,322 127,322 128.5,322 129.5,322 131,322 132.5,322 134,322 135.5,322 137,322 138,322 139.5,322 141,322 142.5,322 144,322 145.5,322 146.5,322 148,322 149.5,322 151,322 152.5,322 154,322 155,322 156.5,322 158,322 159.5,322 161,322 162.5,322 163.5,322 165,322 166.5,322 168,322 169.5,322 171,322 172,322 173.5,322 175,322 176.5,322 178,322 179.5,322 180.5,322 182,322 183.5,322 185,322 186.5,322 188,322 189,322 190.5,322 192,322 193.5,322 195,322 196.5,322 197.5,322 199,322 200.5,322 202,322 203.5,322 205,322 206,322 207.5,322 209,322 210.5,322 212,322 213.5,322 214.5,322 216,322 217.5,322 219,322 220.5,322 222,322 223,322 224.5,322 226,322 227.5,322 229,322 230.5,322 231.5,322 233,322 234.5,322 236,322 237.5,322 239,322 240,322 241.5,322 243,322 244.5,322 246,322 247.5,322 249,322 250,322 251.5,322 253,322 254.5,322 256,322 257.5,322 258.5,322 260,322 261.5,322 263,322 264.5,322 266,322 267,322 268.5,322 270,322 271.5,322 273,322 274.5,322 275.5,322 277,322 278.5,322 280,322 281.5,322 283,322 284,322 285.5,322 287,322 288.5,322 290,322 291.5,322 292.5,322 294,321.5 295.5,321.5 297,321.5 298.5,321 300,320.5 301,320 302.5,319.5 304,318.5 305.5,317.5 307,316 308.5,314 309.5,311.5 311,308.5 312.5,305 314,301 315.5,297 317,292 318,287 319.5,282 321,276.5 322.5,271.5 324,265.5 325.5,260 326.5,254.5 328,249 329.5,243 331,237.5 332.5,231.5 334,226 335,220 336.5,214.5 338,208.5 339.5,202.5 341,197 342.5,191 343.5,185.5 345,179.5 346.5,174 348,168 349.5,162.5 351,156.5 352,150.5 353.5,145 355,139 356.5,133.5 358,127.5 359.5,122 360.5,116 362,110 363.5,104.5 365,98.5 366.5,93 368,87 369,81.5 370.5,75.5 372,70 373.5,64" fill="none" stroke="#db3d00" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="310" cy="322" r="6" fill="#db3d00" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="383.5" y="49.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#db3d00">$\text{punainen}$</div></foreignObject>
  <polyline points="359.5,322 387.5,207.5" fill="none" stroke="#3fc600" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,322 91.5,322 93,322 95,322 96.5,322 98,322 99.5,322 101.5,322 103,322 104.5,322 106,322 107.5,322 109.5,322 111,322 112.5,322 114,322 116,322 117.5,322 119,322 120.5,322 122,322 124,322 125.5,322 127,322 128.5,322 130.5,322 132,322 133.5,322 135,322 136.5,322 138.5,322 140,322 141.5,322 143,322 145,322 146.5,322 148,322 149.5,322 151,322 153,322 154.5,322 156,322 157.5,322 159.5,322 161,322 162.5,322 164,322 165.5,322 167.5,322 169,322 170.5,322 172,322 174,322 175.5,322 177,322 178.5,322 180,322 182,322 183.5,322 185,322 186.5,322 188.5,322 190,322 191.5,322 193,322 194.5,322 196.5,322 198,322 199.5,322 201,322 203,322 204.5,322 206,322 207.5,322 209,322 211,322 212.5,322 214,322 215.5,322 217,322 219,322 220.5,322 222,322 223.5,322 225.5,322 227,322 228.5,322 230,322 231.5,322 233.5,322 235,322 236.5,322 238,322 240,322 241.5,322 243,322 244.5,322 246,322 248,322 249.5,322 251,322 252.5,322 254.5,322 256,322 257.5,322 259,322 260.5,322 262.5,322 264,322 265.5,322 267,322 269,322 270.5,322 272,322 273.5,322 275,322 277,322 278.5,322 280,322 281.5,322 283.5,322 285,322 286.5,322 288,322 289.5,322 291.5,322 293,322 294.5,322 296,322 298,322 299.5,322 301,322 302.5,322 304,322 306,322 307.5,322 309,322 310.5,322 312.5,322 314,322 315.5,322 317,322 318.5,322 320.5,322 322,322 323.5,322 325,322 327,322 328.5,322 330,322 331.5,322 333,322 335,322 336.5,322 338,322 339.5,322 341.5,322 343,321.5 344.5,321.5 346,321.5 347.5,321 349.5,320.5 351,320 352.5,319 354,318 356,316.5 357.5,314 359,311.5 360.5,308 362,304 364,299 365.5,294 367,288.5 368.5,282.5 370.5,276.5 372,270.5 373.5,264 375,257.5 376.5,251.5 378.5,245 380,238.5 381.5,231.5 383,225 385,218.5 386.5,212 388,205.5 389.5,199 391,192.5 393,186 394.5,179.5 396,172.5 397.5,166 399.5,159.5 401,153 402.5,146.5 404,140 405.5,133.5 407.5,126.5 409,120 410.5,113.5 412,107" fill="none" stroke="#3fc600" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="359.5" cy="322" r="6" fill="#3fc600" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="422" y="92.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#3fc600">$\text{vihreä}$</div></foreignObject>
  <polyline points="385,322 413.5,207.5" fill="none" stroke="#0083db" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,322 91.5,322 93.5,322 95,322 96.5,322 98.5,322 100,322 102,322 103.5,322 105,322 107,322 108.5,322 110,322 112,322 113.5,322 115.5,322 117,322 118.5,322 120.5,322 122,322 123.5,322 125.5,322 127,322 129,322 130.5,322 132,322 134,322 135.5,322 137,322 139,322 140.5,322 142.5,322 144,322 145.5,322 147.5,322 149,322 150.5,322 152.5,322 154,322 156,322 157.5,322 159,322 161,322 162.5,322 164,322 166,322 167.5,322 169.5,322 171,322 172.5,322 174.5,322 176,322 177.5,322 179.5,322 181,322 183,322 184.5,322 186,322 188,322 189.5,322 191,322 193,322 194.5,322 196.5,322 198,322 199.5,322 201.5,322 203,322 204.5,322 206.5,322 208,322 210,322 211.5,322 213,322 215,322 216.5,322 218,322 220,322 221.5,322 223.5,322 225,322 226.5,322 228.5,322 230,322 231.5,322 233.5,322 235,322 237,322 238.5,322 240,322 242,322 243.5,322 245,322 247,322 248.5,322 250.5,322 252,322 253.5,322 255.5,322 257,322 258.5,322 260.5,322 262,322 263.5,322 265.5,322 267,322 269,322 270.5,322 272,322 274,322 275.5,322 277,322 279,322 280.5,322 282.5,322 284,322 285.5,322 287.5,322 289,322 290.5,322 292.5,322 294,322 296,322 297.5,322 299,322 301,322 302.5,322 304,322 306,322 307.5,322 309.5,322 311,322 312.5,322 314.5,322 316,322 317.5,322 319.5,322 321,322 323,322 324.5,322 326,322 328,322 329.5,322 331,322 333,322 334.5,322 336.5,322 338,322 339.5,322 341.5,322 343,322 344.5,322 346.5,322 348,322 350,322 351.5,322 353,322 355,322 356.5,322 358,322 360,322 361.5,322 363.5,322 365,322 366.5,322 368.5,321.5 370,321.5 371.5,321.5 373.5,321 375,320.5 377,320 378.5,319 380,317.5 382,316 383.5,313.5 385,310.5 387,306.5 388.5,302 390.5,297 392,291.5 393.5,285.5 395.5,279.5 397,273 398.5,266.5 400.5,259.5 402,253 404,246 405.5,239.5 407,232.5 409,225.5 410.5,219 412,212 414,205 415.5,198 417.5,191.5 419,184.5 420.5,177.5 422.5,170.5 424,164 425.5,157 427.5,150" fill="none" stroke="#0083db" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="385" cy="322" r="6" fill="#0083db" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="437.5" y="135.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#0083db">$\text{sininen}$</div></foreignObject>
  <foreignObject x="268" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#db3d00">$U_\text{k}$</div></foreignObject>
</svg>

### Planckin vakio kulmakertoimesta
Yhtälöstä $eU_\text{k} = hf$ saadaan kynnysjännite taajuuden funktiona:
```latex
U_\text{k} = \frac{h}{e}\,f
```
Kun usean eri värisen LEDin kynnysjännitteet piirretään kuvaajaksi $(f, U_\text{k})$, pisteet ovat likimain suoralla, jonka kulmakerroin on $k = \tfrac{h}{e}$. Planckin vakio saadaan kulmakertoimesta:
```latex
h = ek
```
missä $k$ on sovitetun suoran kulmakerroin ($\tfrac{\text{V}}{\text{Hz}} = \text{V}\,\text{s}$) ja $e$ alkeisvaraus; $\text{C} \cdot \text{V}\,\text{s} = \text{J}\,\text{s}$. Kulmakerroin luetaan sovitetulta suoralta, ei kahdesta mittauspisteestä. Graphical Analysis Prossa suora sovitetaan valinnoilla **Käyrän sovitus** ja **Lineaarinen**, ja tulosruudun $m$ on kulmakerroin.

<svg data-fig="sovitus" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: kuuden LEDin kynnysjännite U k voltteina niiden valon taajuuden f funktiona, taajuusakseli nollasta 8 kertaa 10 potenssiin 14 hertsiin. Pisteet ovat LEDien värisiä: punainen 4,76 ja 1,88; oranssi 4,96 ja 1,95; keltainen 5,08 ja 2,00; vihreä 5,71 ja 2,30; sininen 6,38 ja 2,52; violetti 7,40 ja 2,95, taajuudet kertaa 10 potenssiin 14 hertsiä ja jännitteet voltteina. Pisteisiin on sovitettu suora, joka jatkuu katkoviivana lähelle origoa ja leikkaa pystyakselin hieman nollan alapuolella. Suoralle on piirretty kulmakerrointa kuvaava kolmio, ja merkintä kertoo, että kulmakerroin k on h jaettuna e:llä." style="max-width:100%;font-size:24px">
  <line x1="131" y1="322" x2="131" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="172.5" y1="322" x2="172.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="214" y1="322" x2="214" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255" y1="322" x2="255" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="322" x2="296" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="337.5" y1="322" x2="337.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="379" y1="322" x2="379" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="322" x2="420" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="285" x2="420" y2="285" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="248.5" x2="420" y2="248.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="211.5" x2="420" y2="211.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="174.5" x2="420" y2="174.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="137.5" x2="420" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="101" x2="420" y2="101" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="64" x2="420" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="322" x2="434" y2="322" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,322 L433,328 L433,316 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="323" x2="90" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,38 L96,51 L84,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="131" y1="322" x2="131" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="121" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="172.5" y1="322" x2="172.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="162.5" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="214" y1="322" x2="214" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="204" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="255" y1="322" x2="255" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="296" y1="322" x2="296" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="286" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="337.5" y1="322" x2="337.5" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="327.5" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="379" y1="322" x2="379" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="369" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="420" y1="322" x2="420" y2="329" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="410" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="83" y1="285" x2="90" y2="285" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="270.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="83" y1="248.5" x2="90" y2="248.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <line x1="83" y1="211.5" x2="90" y2="211.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="197" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="83" y1="174.5" x2="90" y2="174.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="160" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2{,}0$</div></foreignObject>
  <line x1="83" y1="137.5" x2="90" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="123" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="83" y1="101" x2="90" y2="101" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="86.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3{,}0$</div></foreignObject>
  <line x1="83" y1="64" x2="90" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3{,}5$</div></foreignObject>
  <foreignObject x="60" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="307.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="80" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{k}\ (\text{V})$</div></foreignObject>
  <polyline points="106.5,313.5 267.5,197" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 6"/>
  <polyline points="267.5,197 416,89.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="296" y1="176.5" x2="379" y2="176.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="379" y1="176.5" x2="379" y2="116.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="321" y="182" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta f$</div></foreignObject>
  <foreignObject x="389" y="142" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta U_\text{k}$</div></foreignObject>
  <foreignObject x="115" y="86.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kulmakerroin } k = \tfrac{h}{e}$</span></div></foreignObject>
  <circle cx="286.5" cy="183.5" r="6.5" fill="#db3d00" stroke="#ffffff" stroke-width="2"/>
  <circle cx="294.5" cy="178.5" r="6.5" fill="#db8600" stroke="#ffffff" stroke-width="2"/>
  <circle cx="299.5" cy="174.5" r="6.5" fill="#dbad00" stroke="#ffffff" stroke-width="2"/>
  <circle cx="325.5" cy="152.5" r="6.5" fill="#3fc600" stroke="#ffffff" stroke-width="2"/>
  <circle cx="353" cy="136" r="6.5" fill="#0083db" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395.5" cy="104.5" r="6.5" fill="#6f00ac" stroke="#ffffff" stroke-width="2"/>
</svg>

Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Lisäksi suora ei yleensä kulje täsmälleen origon kautta: kuvan aineistossa se leikkaa pystyakselin noin $0{,}05\,\text{V}$ nollan alapuolella. Mitattu kynnysjännite ei ole tarkalleen $\tfrac{hf}{e}$: elektronit saavat hieman lisäenergiaa myös lämpöliikkeestä, ja kynnysjännite määritellään suoran jatkeena. Ero on tyypillisesti noin $0{,}1\,\text{V}$. Kun ero on lähes sama kaikille LEDeille, se siirtää suoraa mutta ei muuta sen kulmakerrointa. Siksi Planckin vakio määritetään monen LEDin suorasta eikä yhdestä LEDistä. Epävarmuutta tuo myös LEDin spektrin leveys: huipun aallonpituus tunnetaan vain muutaman nanometrin tarkkuudella.

## Esimerkki
Ryhmä mittasi viiden eri värisen LEDin kynnysjännitteet ja sovitti pisteisiin $(f, U_\text{k})$ suoran. Sovitettu suora kulkee pisteiden $(4{,}50 \cdot 10^{14}\,\text{Hz};\ 1{,}74\,\text{V})$ ja $(7{,}50 \cdot 10^{14}\,\text{Hz};\ 2{,}96\,\text{V})$ kautta. Alkeisvaraus on $e = 1{,}602 \cdot 10^{-19}\,\text{C}$. Minkä arvon ryhmä sai Planckin vakiolle?

<!-- vaihe -->

**Tunnetut ja kysytty.** Sovitetun suoran pisteet $(f_1, U_1) = (4{,}50 \cdot 10^{14}\,\text{Hz};\ 1{,}74\,\text{V})$ ja $(f_2, U_2) = (7{,}50 \cdot 10^{14}\,\text{Hz};\ 2{,}96\,\text{V})$ sekä alkeisvaraus $e = 1{,}602 \cdot 10^{-19}\,\text{C}$. Kysytään Planckin vakiota $h$.

<!-- vaihe -->

**Periaate.** Kynnysjännitteellä elektronin saama energia on likimain fotonin energia, $eU_\text{k} \approx hf$, joten kuvaajan $(f, U_\text{k})$ kulmakerroin on $k = \tfrac{h}{e}$. Kulmakerroin lasketaan kahdesta sovitetun suoran pisteestä, jotka ovat kaukana toisistaan, ei yksittäisistä mittauspisteistä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kulmakerroin on $k = \tfrac{U_2 - U_1}{f_2 - f_1}$, ja yhtälöstä $k = \tfrac{h}{e}$ ratkaistaan $h$:
```latex
h = ek = \frac{e\,(U_2 - U_1)}{f_2 - f_1}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: jännitteet ovat voltteina ja taajuudet hertseinä. Yksiköistä $\text{C} \cdot \tfrac{\text{V}}{\text{Hz}} = \text{C} \cdot \text{V} \cdot \text{s} = \text{J}\,\text{s}$, koska $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$ ja $1\,\text{Hz} = 1\,\tfrac{1}{\text{s}}$.

<!-- vaihe -->

**Sijoitus.** Erotukset ovat $U_2 - U_1 = 2{,}96\,\text{V} - 1{,}74\,\text{V} = 1{,}22\,\text{V}$ ja $f_2 - f_1 = 7{,}50 \cdot 10^{14}\,\text{Hz} - 4{,}50 \cdot 10^{14}\,\text{Hz} = 3{,}00 \cdot 10^{14}\,\text{Hz}$.
```latex
\begin{aligned}
&h = \frac{e\,(U_2 - U_1)}{f_2 - f_1} \\
&= \frac{1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1{,}22\,\text{V}}{3{,}00 \cdot 10^{14}\,\tfrac{1}{\text{s}}} \\
&= 6{,}515 \cdot 10^{-34}\,\text{J}\,\text{s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ryhmän arvo Planckin vakiolle on $h = 6{,}52 \cdot 10^{-34}\,\text{J}\,\text{s}$. Tulos ilmoitetaan kolmella merkitsevällä numerolla, koska jännitteiden erotuksessa $1{,}22\,\text{V}$ ja taajuuksien erotuksessa $3{,}00 \cdot 10^{14}\,\text{Hz}$ on kolme merkitsevää numeroa.

<!-- vaihe -->

**Järkevyys.** Planckin vakion hyväksytty arvo on $6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, ja ryhmän tulos poikkeaa siitä $(6{,}515 - 6{,}626) : 6{,}626 \approx -1{,}7\,\%$. Ero on pieni, kun kynnysjännitteet ja aallonpituudet tunnetaan vain muutaman prosentin tarkkuudella. Arvio pyöreillä luvuilla: $1{,}2\,\text{V} : (3 \cdot 10^{14}\,\text{Hz}) = 4 \cdot 10^{-15}\,\text{V}\,\text{s}$, ja $1{,}6 \cdot 10^{-19}\,\text{C} \cdot 4 \cdot 10^{-15}\,\text{V}\,\text{s} \approx 6{,}4 \cdot 10^{-34}\,\text{J}\,\text{s}$.

## Yleinen virhekäsitys
Moni ajattelee, että LEDin jännitettä kasvattamalla sen valo muuttuu sinisemmäksi, koska elektronit saavat enemmän energiaa. Fotonin energian määrää kuitenkin puolijohteen energia-aukko, ei jännite. Kynnysjännitettä suurempi jännite kasvattaa virtaa, joten fotoneja syntyy enemmän ja LED loistaa kirkkaammin, mutta jokaisen fotonin energia on yhä likimain $E_\text{g}$. Ylimääräinen energia lämmittää LEDiä. Punaisesta LEDistä ei siksi saa sinistä valoa millään jännitteellä, ja liian suuri virta vain rikkoo LEDin.

Toinen virhe on luulla, että mittaus on epäonnistunut, jos kuvaajan $(f, U_\text{k})$ suora ei kulje origon kautta. Mitattu kynnysjännite eroaa arvosta $\tfrac{hf}{e}$ lähes yhtä paljon kaikilla LEDeillä. Ero siirtää suoraa ylös tai alas mutta ei muuta sen kulmakerrointa $\tfrac{h}{e}$, josta Planckin vakio saadaan.

## Tiivistelmä
- LEDissä elektroni putoaa puolijohteen johtavuusvyöstä valenssivyön aukkoon ja synnyttää yhden fotonin, jonka energia on likimain energia-aukon suuruinen: $hf \approx E_\text{g}$.
- LED alkaa johtaa ja säteillä, kun jännite saavuttaa kynnysjännitteen: $eU_\text{k} \approx hf = \tfrac{hc}{\lambda}$. Lyhyemmän aallonpituuden LED tarvitsee suuremman kynnysjännitteen.
- Kynnysjännite saadaan jatkamalla $(U, I)$-kuvaajan suora osa jänniteakselille.
- Kuvaajan $(f, U_\text{k})$ kulmakerroin on $k = \tfrac{h}{e}$, joten $h = ek$. Suoran ei tarvitse kulkea origon kautta.
- Hehkulampun spektri on jatkuva, LEDin spektri kapea kaista ja laserdiodin spektri hyvin kapea viiva.
