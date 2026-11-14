# Moment: the turning effect of a force

> **Why** does a stuck wheel nut come loose with a long spanner, when the same force on a short spanner cannot make it budge?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: changing tyres in autumn in a home yard. A man kneels beside the rear wheel of a car and presses down with both hands on the end of a long breaker bar. The bar&#x27;s socket is on a wheel nut in the middle of the rim, and the bar reaches far to the left of the wheel. Behind him is a stack of winter tyres, and in front of him a short spanner lies on the asphalt. In the background are a red house and birches in yellow leaf." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy51h-lawn" gradientUnits="userSpaceOnUse" x1="0" y1="352" x2="0" y2="444"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy51h-asphalt" gradientUnits="userSpaceOnUse" x1="0" y1="440" x2="0" y2="600"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-car" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy51h-glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy51h-glass2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#a5d8ff"/></linearGradient><linearGradient id="fy51h-rim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-sock" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy51h-span" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="400" fill="url(#fy51h-sky)"/>
  <path d="M788,108 Q786.5,81 818.5,84 Q831,55 863,65 Q892,49 908,79 Q937,82.5 933.5,108 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M250.5,75 Q249.5,56.5 271.5,58.5 Q280,38.5 302,45.5 Q322,34.5 333,55 Q353,57.5 350.5,75 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,330 L11,304 L22,330 L34,301 L46,330 L57.5,302.5 L69,330 L86.5,281.5 L104.5,330 L116.5,300 L129,330 L141,300 L153.5,330 L170,285.5 L186.5,330 L205.5,278 L224.5,330 L241,285.5 L257.5,330 L277,276.5 L296,330 L314.5,280 L332.5,330 L348,290 L363,330 L382,278.5 L401,330 L416,290 L431.5,330 L444.5,296 L458,330 L474.5,285.5 L491.5,330 L506.5,289.5 L522,330 L537,292 L551.5,330 L562.5,304.5 L573,330 L592,279 L610.5,330 L629.5,278 L648.5,330 L664.5,287.5 L680.5,330 L698,282.5 L715.5,330 L731.5,287 L747.5,330 L765,283 L782.5,330 L800.5,281.5 L818.5,330 L831.5,296.5 L845,330 L857,300.5 L869,330 L888,277.5 L907,330 L926.5,276.5 L946,330 L962.5,286.5 L978.5,330 L997.5,278 L1016.5,330 L1032,288.5 L1048,330 L1064.5,285.5 L1081,330 L1097.5,286.5 L1113.5,330 L1126.5,299 L1139,330 L1156.5,282.5 L1174,330 L1192,280 L1210.5,330 V360 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="352" width="1200" height="92" fill="url(#fy51h-lawn)"/>
  <rect x="40" y="222" width="300" height="150" fill="#c92a2a" stroke="#1f2933" stroke-width="3"/>
  <line x1="54" y1="225" x2="54" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="68" y1="225" x2="68" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="82" y1="225" x2="82" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="225" x2="96" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="110" y1="225" x2="110" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="124" y1="225" x2="124" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="138" y1="225" x2="138" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="152" y1="225" x2="152" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="166" y1="225" x2="166" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="180" y1="225" x2="180" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="194" y1="225" x2="194" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="208" y1="225" x2="208" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="222" y1="225" x2="222" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="236" y1="225" x2="236" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="250" y1="225" x2="250" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="264" y1="225" x2="264" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="278" y1="225" x2="278" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="292" y1="225" x2="292" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="306" y1="225" x2="306" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <line x1="320" y1="225" x2="320" y2="369" stroke="#f2a69c" stroke-width="1" stroke-linecap="butt"/>
  <rect x="40" y="222" width="10" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="330" y="222" width="10" height="150" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M20,222 L190,139.5 L360,222 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="70" y="264" width="40" height="60" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="70" y="264" width="40" height="60" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="90" y1="264" x2="90" y2="324" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="140" y="264" width="40" height="60" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="140" y="264" width="40" height="60" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="160" y1="264" x2="160" y2="324" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="210" y="264" width="40" height="60" fill="#eef5f9" stroke="#ffffff" stroke-width="5"/>
  <rect x="210" y="264" width="40" height="60" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="230" y1="264" x2="230" y2="324" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <rect x="402.5" y="122" width="15" height="250" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="402.5" y="342" width="7.5" height="4" fill="#1f2933"/>
  <rect x="410" y="312" width="7.5" height="4" fill="#1f2933"/>
  <rect x="402.5" y="282" width="7.5" height="4" fill="#1f2933"/>
  <rect x="410" y="252" width="7.5" height="4" fill="#1f2933"/>
  <rect x="402.5" y="222" width="7.5" height="4" fill="#1f2933"/>
  <rect x="410" y="192" width="7.5" height="4" fill="#1f2933"/>
  <line x1="410" y1="234.5" x2="450" y2="207" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="209.5" x2="370" y2="182" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="184.5" x2="450" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="410" y1="159.5" x2="370" y2="132" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="399.5" cy="204.5" r="17.5" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="432.5" cy="167" r="17.5" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="372.5" cy="185" r="17.5" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="388.5" cy="156" r="17.5" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="430.5" cy="195" r="17.5" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="423.5" cy="150" r="17.5" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="403" cy="138.5" r="17.5" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="409" cy="154.5" r="17.5" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="383.5" cy="194" r="17.5" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="420.5" cy="128.5" r="17.5" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="370.5" cy="155" r="17.5" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="390.5" cy="179" r="17.5" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="381.5" cy="153.5" r="17.5" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="395.5" cy="219.5" r="17.5" fill="#d9b26a" fill-opacity="0.9"/>
  <rect x="466" y="172" width="12" height="200" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="466" y="348" width="6" height="3" fill="#1f2933"/>
  <rect x="472" y="324" width="6" height="3" fill="#1f2933"/>
  <rect x="466" y="300" width="6" height="3" fill="#1f2933"/>
  <rect x="472" y="276" width="6" height="3" fill="#1f2933"/>
  <rect x="466" y="252" width="6" height="3" fill="#1f2933"/>
  <rect x="472" y="228" width="6" height="3" fill="#1f2933"/>
  <line x1="472" y1="262" x2="504" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="472" y1="242" x2="440" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="472" y1="222" x2="504" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <line x1="472" y1="202" x2="440" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="round"/>
  <circle cx="471.5" cy="232.5" r="14" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="454" cy="218" r="14" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="483" cy="233.5" r="14" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="446.5" cy="215.5" r="14" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="466" cy="191" r="14" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="464" cy="242.5" r="14" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="466.5" cy="205.5" r="14" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="461.5" cy="246" r="14" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="454.5" cy="181.5" r="14" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="459.5" cy="229.5" r="14" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="441.5" cy="199" r="14" fill="#d9b26a" fill-opacity="0.9"/>
  <circle cx="472.5" cy="201" r="14" fill="#e8590c" fill-opacity="0.9"/>
  <circle cx="488.5" cy="218.5" r="14" fill="#ffc078" fill-opacity="0.9"/>
  <circle cx="478" cy="246.5" r="14" fill="#d9b26a" fill-opacity="0.9"/>
  <ellipse cx="332.5" cy="391" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="507" cy="423" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="364" cy="408" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="1068" cy="382" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="736.5" cy="385.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="1071.5" cy="394" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="818" cy="430.5" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="160.5" cy="402.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="999.5" cy="380" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="88.5" cy="406" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="352" cy="410" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="879.5" cy="418.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="753" cy="413" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="174.5" cy="381" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="93.5" cy="402" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="261" cy="398.5" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="588.5" cy="392.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="531" cy="404" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="204" cy="397.5" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="50.5" cy="426.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="178" cy="422.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="741" cy="402.5" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="935.5" cy="429.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="244" cy="402.5" rx="6" ry="3" fill="#e8590c"/>
  <ellipse cx="223" cy="421" rx="6" ry="3" fill="#ffc078"/>
  <ellipse cx="133" cy="403" rx="6" ry="3" fill="#e8590c"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy51h-asphalt)"/>
  <rect x="0" y="438" width="1200" height="6" fill="#c9c2b2"/>
  <ellipse cx="1036" cy="552" rx="494" ry="14" fill="#1f2933" fill-opacity="0.25"/>
  <path d="M635.5,480.5 Q612,470 615,405 L625,293 Q630.5,267 661.5,262 Q698,179 776,168.5 H1212 V480.5 H950 A109,109 0 0 0 732,480.5 Z" fill="url(#fy51h-car)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M703,267 Q729,202 791.5,192 H1015 V267 Z" fill="url(#fy51h-glass)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M1046.5,267 V192 H1212 V267 Z" fill="url(#fy51h-glass2)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="1031" y1="184" x2="1031" y2="475" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M635.5,288 H1212" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.55"/>
  <rect x="1067" y="296" width="41.5" height="12" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="615" y="324.5" width="18" height="41.5" rx="4" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="609.5" y="418" width="31" height="31" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M732,480.5 A109,109 0 0 1 950,480.5 Z" fill="#6c757d" stroke="#1f2933" stroke-width="6" stroke-linejoin="round"/>
  <circle cx="841" cy="462" r="85.8" fill="#1f2933"/>
  <circle cx="841" cy="462" r="77.22" fill="none" stroke="#6c757d" stroke-width="2"/>
  <circle cx="841" cy="462" r="56.628" fill="url(#fy51h-rim)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M861.5,466 L888,478 L878.5,495 L854,478 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M848,481.5 L851,511 L831,511 L834,481.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M828,478 L803.5,495 L794,478 L820.5,466 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M820.5,458.5 L794,446.5 L803.5,429.5 L828,446.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M834,443 L831,413.5 L851,413.5 L848,443 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <path d="M854,446.5 L878.5,429.5 L888,446.5 L861.5,458.5 Z" fill="#8a96a3" stroke-linejoin="round"/>
  <circle cx="841" cy="462" r="22.308" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="836.5" cy="448.5" r="4.5" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="853" cy="453.5" r="4.5" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="853" cy="471" r="4.5" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="836.5" cy="476" r="4.5" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M470,420 L582,384 L590,524" fill="none" stroke="#1f2933" stroke-width="45" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M470,420 L582,384 L590,524" fill="none" stroke="#1971c2" stroke-width="40" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M470,420 L582,384 L590,524" fill="none" stroke="#1f2933" stroke-width="40" stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.3"/>
  <path d="M578,538 L626,540" fill="none" stroke="#1f2933" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M552,322 L586,390 L630,454" fill="none" stroke="#1f2933" stroke-width="29" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M552,322 L586,390 L630,454" fill="none" stroke="#e8590c" stroke-width="24" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M552,322 L586,390 L630,454" fill="none" stroke="#1f2933" stroke-width="24" stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.3"/>
  <circle cx="630" cy="456" r="14" fill="#a97a35" stroke="#1f2933" stroke-width="2"/>
  <path d="M611,455 H826.5 V469 H611 Z" fill="url(#fy51h-bar)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="605" y="452" width="74" height="20" rx="10" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <circle cx="826.5" cy="462" r="13" fill="url(#fy51h-sock)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="826.5" cy="462" r="5" fill="#6c757d" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M470,420 L482,530 L378,534" fill="none" stroke="#1f2933" stroke-width="45" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M470,420 L482,530 L378,534" fill="none" stroke="#1971c2" stroke-width="40" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M384,530 L352,546" fill="none" stroke="#1f2933" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M470,420 L560,318" fill="none" stroke="#1f2933" stroke-width="77" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M470,420 L560,318" fill="none" stroke="#e8590c" stroke-width="72" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M509.5,425.5 L460,381.5" fill="none" stroke="#ffc078" stroke-width="9" stroke-linejoin="round"/>
  <path d="M572,304.5 L603,272" fill="none" stroke="#f1dfb5" stroke-width="22" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="603" cy="272" r="31" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M570,274 Q572,228 607,230 Q636,234 636,264 Z" fill="#1971c2" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="568" y="262" width="70" height="12" rx="5" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="627" cy="278" r="4" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M560,318 L600,386 L648,452" fill="none" stroke="#1f2933" stroke-width="31" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M560,318 L600,386 L648,452" fill="none" stroke="#e8590c" stroke-width="26" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="648" cy="454" r="15" fill="#a97a35" stroke="#1f2933" stroke-width="2"/>
  <rect x="40" y="516" width="172" height="50" rx="18" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <path d="M54,541 L66,550 L78,532 L90,550 L102,532 L114,550 L126,532 L138,550 L150,532 L162,550 L174,532 L186,550 L198,532" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <rect x="46" y="520" width="160" height="6" fill="#6c757d" fill-opacity="0.55" rx="3"/>
  <rect x="40" y="464" width="172" height="50" rx="18" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <path d="M54,489 L66,498 L78,480 L90,498 L102,480 L114,498 L126,480 L138,498 L150,480 L162,498 L174,480 L186,498 L198,480" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <rect x="46" y="468" width="160" height="6" fill="#6c757d" fill-opacity="0.55" rx="3"/>
  <rect x="40" y="412" width="172" height="50" rx="18" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <path d="M54,437 L66,446 L78,428 L90,446 L102,428 L114,446 L126,428 L138,446 L150,428 L162,446 L174,428 L186,446 L198,428" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <rect x="46" y="416" width="160" height="6" fill="#6c757d" fill-opacity="0.55" rx="3"/>
  <rect x="40" y="360" width="172" height="50" rx="18" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <path d="M54,385 L66,394 L78,376 L90,394 L102,376 L114,394 L126,376 L138,394 L150,376 L162,394 L174,376 L186,394 L198,376" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round"/>
  <rect x="46" y="364" width="160" height="6" fill="#6c757d" fill-opacity="0.55" rx="3"/>
  <path d="M318,572 H438 V584 H318 Z" fill="url(#fy51h-span)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="318" cy="578" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="318" cy="578" r="6" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M438,566 h18 l-6,8 v8 l6,8 h-18 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
</svg>

## Key idea
A force can change the motion of a body, but it can also rotate the body. When a body is fixed to an axis, like a door on its hinges, a nut on a bolt or a seesaw on its support, it cannot move away but can only rotate about the axis. This axis is called the **axis of rotation**. The ability of a force to rotate a body about the axis of rotation is called the **turning effect**, and its size is measured by the **moment** (the moment of a force). The turning effect does not depend only on the size of the force. It also depends on the direction of the force and on the point of the body where the force acts.

### A door and the point of application of a force
A door is easy to open by pushing at the handle, which is far from the hinges. If the same force pushes close to the hinge, the door turns much less easily. If the door is pushed at its edge in the direction of the door towards the hinge, the door does not turn at all, even though the force is equally large. The three forces $\overline{F}_1$, $\overline{F}_2$ and $\overline{F}_3$ in the figure are therefore equally large, but their turning effects about the hinge are completely different.

<svg data-fig="ovi" viewBox="0 0 600 330" role="img" aria-label="A door seen from above. On the left is a wall and a hinge, from which the door extends to the right as a horizontal board. Three equally long red force arrows: F1 at the handle perpendicular to the door, F2 near the hinge, also perpendicular, and F3 at the end of the door along the door towards the hinge. A dashed arc shows the direction in which the door opens. Schematic figure, not to scale." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-ovi-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy51-ovi-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="24" y="200" width="40" height="110" fill="url(#fy51-ovi-wall)" stroke="#1f2933" stroke-width="2"/>
  <line x1="26" y1="214" x2="62" y2="204" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="234" x2="62" y2="224" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="254" x2="62" y2="244" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="274" x2="62" y2="264" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="26" y1="294" x2="62" y2="284" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt"/>
  <foreignObject x="15" y="167.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{wall}$</div></foreignObject>
  <path d="M524,250 A440,440 0 0 0 486,71" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-dasharray="7 6"/>
  <rect x="84" y="242" width="440" height="16" rx="2" fill="url(#fy51-ovi-wood)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="84" cy="250" r="11" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="75" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{hinge}$</div></foreignObject>
  <rect x="452" y="258" width="26" height="12" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="423.5" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{handle}$</div></foreignObject>
  <line x1="465" y1="242" x2="465" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M465,150 L473,168 L457,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="403" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <line x1="150" y1="242" x2="150" y2="167" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,150 L158,168 L142,168 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="167" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <line x1="622" y1="250" x2="547" y2="250" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,250 L548,242 L548,258 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="547.5" y="207.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_3$</div></foreignObject>
  <foreignObject x="215" y="15.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{seen from above}$</div></foreignObject>
</svg>

### The lever arm of a force
The turning effect is decided by the **line of action** of the force, the straight line that passes through the point of application of the force (in a spanner, the point where the hand grips) in the direction of the force. The **lever arm** $r$ of a force is the perpendicular distance from the axis of rotation to the line of action. When the force is perpendicular to the handle of the spanner, the lever arm equals the distance $d$ of the point of application from the axis. When the force is oblique, the lever arm is shorter than $d$. If the line of action passes through the axis of rotation, the lever arm is zero and the force does not rotate the body at all. This is why the force $\overline{F}_3$ along the door does not open the door.

<svg data-fig="varsi" viewBox="0 0 600 340" role="img" aria-label="A spanner around a nut. The axis of rotation O is at the centre of the nut. The handle of the spanner points horizontally to the right, and a hand pulls it at a point at the distance d from the axis. The force F points obliquely up and to the right, at an angle of 60 degrees to the extension of the handle. The line of action of the force is drawn dashed in both directions. The segment drawn from the axis perpendicular to the line of action is the lever arm r of the force, and it is shorter than d. Schematic figure." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-varsi-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <line x1="308" y1="284" x2="493" y2="-36.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="398" y1="128" x2="468" y2="128" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <path d="M118,138 L404,138 L404,118 L118,118 Z" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="404" cy="128" r="10" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="118" cy="128" r="32" fill="url(#fy51-varsi-steel)" stroke="#1f2933" stroke-width="2.5"/>
  <polygon points="137,139 118,150 99,139 99,117 118,106 137,117" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="118" cy="128" r="9.24" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="118" y1="128" x2="328" y2="249" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M322,259.5 L311.5,253.5 L317.5,243" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="328" cy="249" r="3.5" fill="#1f2933"/>
  <foreignObject x="191" y="192" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="118" y1="82" x2="398" y2="82" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="74" x2="118" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398" y1="74" x2="398" y2="90" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="248" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <line x1="398" y1="128" x2="445.5" y2="45.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,31 L452,50.5 L438,42.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="461.5" y="20.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M438,128 A40,40 0 0 0 418,93.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="442" y="87" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <circle cx="398" cy="128" r="4" fill="#1f2933"/>
  <foreignObject x="68" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="319" y="264.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{line of action}$</div></foreignObject>
</svg>

## Formula: Moment of a force
The moment of a force about the axis of rotation is the product of the magnitude of the force and its lever arm:
```kaavat
moment of a force :: M = F r
```
where $M$ is the moment of the force ($\text{Nm}$), $F$ the magnitude of the force ($\text{N}$) and $r$ the lever arm of the force, that is the perpendicular distance from the axis of rotation to the line of action ($\text{m}$). The unit of moment is the newton metre $\text{Nm}$. It is not the same thing as the unit of energy, the joule, even though both are a product of a newton and a metre: in a moment the distance is perpendicular to the force, in work it is a displacement in the direction of the force.

### Direction of rotation and sign
In addition to its magnitude, a moment has a direction of rotation. In this book a moment that rotates anticlockwise is positive and a moment that rotates clockwise is negative. When several forces act on a body, their moments are added together with their signs. The result is the **net moment**:
```latex
\Sigma M = M_1 + M_2 + M_3 + \ldots
```
where $\Sigma M$ is the net moment ($\text{Nm}$) and $M_1$, $M_2$, … are the moments of the individual forces about the same chosen axis of rotation ($\text{Nm}$). If the net moment on a body at rest that can rotate about a fixed axis is not zero, the body starts to rotate in the direction of the net moment. When a body stays at rest is studied more closely in the chapter *Equilibrium of a body: forces and moments*.

<svg data-fig="suunta" viewBox="0 0 600 320" role="img" aria-label="Two situations side by side. In both, a horizontal rod is fixed to the axis O at its left end. On the left, the force F acts on the right end of the rod upwards, and the curved arrow around the axis rotates anticlockwise: the moment is positive. On the right, the force acts on the end of the rod downwards, and the curved arrow rotates clockwise: the moment is negative." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy51-suunta-44" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy51-suunta-344" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="300" y1="14" x2="300" y2="306" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="70" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-44)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="70" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="258" y1="157" x2="258" y2="87" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M258,70 L266,88 L250,88 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="263.5" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M113,150.5 A46,46 0 0 0 30,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M27,150.5 L25.5,136 L36.5,140 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="66" y="19.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{anticlockwise}$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M > 0$</div></foreignObject>
  <foreignObject x="34" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <rect x="370" y="157" width="200" height="18" rx="4" fill="url(#fy51-suunta-344)" stroke="#a97a35" stroke-width="2.5"/>
  <circle cx="370" cy="166" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="558" y1="175" x2="558" y2="245" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M558,262 L550,244 L566,244 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="563.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <path d="M327,150.5 A46,46 0 0 1 410,143.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M413,150.5 L403.5,140 L414.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="366" y="19.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{clockwise}$</div></foreignObject>
  <foreignObject x="366" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M < 0$</div></foreignObject>
  <foreignObject x="334" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
</svg>

### The lever arm of an oblique force
Often the distance $d$ of the point of application from the axis of rotation is known, together with the angle $\alpha$ that the force makes with the line from the axis to the point of application (for example, the extension of the handle of the spanner). The axis, the point of application and the foot of the lever arm form a right-angled triangle whose hypotenuse is $d$. The lever arm is the side opposite the angle $\alpha$:
```latex
r = d\sin\alpha
```
where $r$ is the lever arm of the force ($\text{m}$), $d$ the distance of the point of application from the axis of rotation ($\text{m}$) and $\alpha$ the angle between the force and the extension of the arm. When $\alpha = 90^\circ$, $r = d$ and the moment is greatest. When $\alpha = 0^\circ$ or $\alpha = 180^\circ$, $r = 0$.

<svg data-fig="kulma" viewBox="0 0 600 340" role="img" aria-label="A right-angled triangle whose vertices are the axis of rotation O, the point of application of the force and the foot of the perpendicular drawn from the axis to the line of action. The hypotenuse is the distance d between the axis and the point of application. The side from the axis to the foot is the lever arm r of the force. The angle at the point of application is alpha, the same as the angle between the force and the extension of the arm. Therefore r is d times sine alpha." style="max-width:100%;font-size:24px">
  <path d="M92,104 L422,104 L228.5,266.5 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <line x1="201" y1="289.5" x2="514" y2="27" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="422" y1="104" x2="486" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="92" y1="104" x2="422" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="92" y1="104" x2="228.5" y2="266.5" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M217.5,275.5 L208.5,265 L219.5,256" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="422" y1="104" x2="485.5" y2="50.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M498.5,39.5 L490,57.5 L479.5,45 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="508" y="41" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <circle cx="92" cy="104" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="422" cy="104" r="4.5" fill="#1f2933"/>
  <foreignObject x="56" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="247" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="128" y="186.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <path d="M378,104 A44,44 0 0 0 388.5,132.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="352" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <path d="M460,104 A38,38 0 0 0 451,79.5" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="466.5" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="385" y="271.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = d\sin\alpha$</div></foreignObject>
</svg>

## Worked example
A stuck nut is being loosened with a spanner. The hand grips the handle at a distance of $0.35\,\text{m}$ from the centre of the nut, which is the axis of rotation. The hand pulls the handle with a force of $240\,\text{N}$ that makes an angle of $65^\circ$ with the extension of the handle and turns the nut in the loosening direction. The nut comes loose only when the moment is at least $80\,\text{Nm}$. What is the moment of the hand's force about the axis of the nut, and does the nut come loose?

<!-- vaihe -->

**Given and find.** $F = 240\,\text{N}$, $d = 0.35\,\text{m}$, $\alpha = 65^\circ$ and the moment required by the nut $80\,\text{Nm}$. We are asked for the moment $M$ of the force and whether it is enough.

<!-- vaihe -->

**Principle.** The nut can only rotate about its axis, so the turning effect of the force is given by its moment $M = Fr$. The force is oblique to the handle, so the lever arm $r$ is shorter than the distance $d$: it is obtained from the right-angled triangle, $r = d\sin\alpha$.

<!-- vaihe -->

**Formula solved.** Substitute the expression for the lever arm into the formula for the moment:
```latex
\begin{aligned}
&M = F r \\
&M = F d\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** Not needed: the force is in newtons and the distance in metres, so the moment comes in newton metres.

<!-- vaihe -->

**Substitution.** Substitute the numerical values with their units:
```latex
\begin{aligned}
M &= F d\sin\alpha \\
&= 240\,\text{N}\cdot 0.35\,\text{m}\cdot\sin 65^\circ \\
&\approx 76.1\,\text{Nm}
\end{aligned}
```

<!-- vaihe -->

**Result.** The moment of the force is $M \approx 76\,\text{Nm}$, to two significant figures like the distance $0.35\,\text{m}$. It is smaller than the $80\,\text{Nm}$ required by the nut, so the nut does not come loose.

<!-- vaihe -->

**Reasonableness.** If the same force acted perpendicular to the handle, the lever arm would be the whole $0.35\,\text{m}$ and the moment $240\,\text{N}\cdot 0.35\,\text{m} = 84\,\text{Nm}$. An oblique pull gives less, because $\sin 65^\circ \approx 0.91 < 1$. So the nut would come loose with the same force if the pull were perpendicular to the handle.

## Common misconception
The moment is not obtained by multiplying the force by the distance to the point of application, but by the distance to the line of action. The distance $d$ and the lever arm $r$ are equal only when the force is perpendicular to the line from the axis to the point of application. Another mistake is to think that a long spanner adds force. The force of the hand is the same, but with a long spanner its lever arm is longer, so the moment is greater. Loosening a nut does not require a certain force but a certain moment.

## Summary
- The turning effect of a force about an axis of rotation is measured by the moment $M = Fr$, whose unit is the newton metre $\text{Nm}$.
- The lever arm $r$ of a force is the perpendicular distance from the axis of rotation to the line of action of the force, not the distance to the point of application.
- The lever arm of an oblique force is $r = d\sin\alpha$. A force whose line of action passes through the axis does not rotate the body.
- A moment that rotates anticlockwise is positive and one that rotates clockwise is negative. The net moment is the sum of the moments with their signs.
- If the net moment on a body at rest that can rotate about an axis is not zero, the body starts to rotate.
