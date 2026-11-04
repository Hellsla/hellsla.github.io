# The decay law and half-life

> **Why** does the activity of a hospital's technetium preparation always halve in about six hours, even though nobody can predict when a single nucleus will decay?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a hospital isotope laboratory. On a wooden table is a thick-walled lead shield, inside which is a small glass vial of radioactive medicine. Above the vial floats an enlarged group of nuclei: some are orange and undecayed, some are grey rings, that is, already decayed, and a ray is just leaving two of them. Next to it is a radiation meter whose probe points at the vial and whose needle trembles. On the wall is a clock." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy89h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="470" fill="#f6f1e6"/>
  <line x1="0" y1="0" x2="0" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="75" y1="0" x2="75" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="150" y1="0" x2="150" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="225" y1="0" x2="225" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="300" y1="0" x2="300" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="375" y1="0" x2="375" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="450" y1="0" x2="450" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="525" y1="0" x2="525" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="600" y1="0" x2="600" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="675" y1="0" x2="675" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="750" y1="0" x2="750" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="825" y1="0" x2="825" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="900" y1="0" x2="900" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="975" y1="0" x2="975" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="0" x2="1050" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1125" y1="0" x2="1125" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1200" y1="0" x2="1200" y2="470" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="0" x2="1200" y2="0" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="75" x2="1200" y2="75" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="150" x2="1200" y2="150" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="225" x2="1200" y2="225" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="300" x2="1200" y2="300" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="375" x2="1200" y2="375" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <line x1="0" y1="450" x2="1200" y2="450" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="470" width="1120" height="40" rx="4" fill="url(#fy89h-table)" stroke="#1f2933" stroke-width="3"/>
  <path d="M50,480 q280,-2.5 560,0 t540,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M50,490 q280,-2.5 560,0 t540,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M50,500 q280,-2.5 560,0 t540,0" fill="none" stroke="#a97a35" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.6"/>
  <rect x="80" y="510" width="30" height="76" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="1090" y="510" width="30" height="76" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="176" y="56.5" width="27.5" height="20.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="184" y="75.5" width="12" height="12" fill="#6c757d"/>
  <circle cx="190" cy="170" r="86" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="190" cy="170" r="70.52" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="190" y1="111.5" x2="190" y2="103" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="219" y1="119.5" x2="223.5" y2="112" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240.5" y1="141" x2="248" y2="136.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248.5" y1="170" x2="257" y2="170" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240.5" y1="199" x2="248" y2="203.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="219" y1="220.5" x2="223.5" y2="228" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="228.5" x2="190" y2="237" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="161" y1="220.5" x2="156.5" y2="228" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="139.5" y1="199" x2="132" y2="203.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="131.5" y1="170" x2="123" y2="170" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="139.5" y1="141" x2="132" y2="136.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="161" y1="119.5" x2="156.5" y2="112" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="190" y1="170" x2="236" y2="203.5" stroke="#c92a2a" stroke-width="6.02" stroke-linecap="round"/>
  <circle cx="190" cy="170" r="6.88" fill="#1f2933"/>
  <rect x="470" y="330" width="260" height="140" rx="10" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="450" y="316" width="300" height="24" rx="6" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <rect x="560" y="250" width="80" height="86" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="574" y="290" width="52" height="44" rx="4" fill="#ffc078"/>
  <rect x="572" y="232" width="56" height="22" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <path d="M770,470 L800,330 L860,330 L840,470 Z" fill="#8a96a3" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="510.5" cy="56.5" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="564.5" cy="65" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="452.5" cy="104.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="690" cy="75.5" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="612.5" cy="84.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="712" cy="169" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="535.5" cy="140.5" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="636" cy="147.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="739" cy="131.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="485" cy="89" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="445.5" cy="140" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="690" cy="138.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="569.5" cy="191" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="764" cy="108" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="514.5" cy="182.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="657" cy="47" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="684" cy="188.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="729" cy="72.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="658.5" cy="93" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="590.5" cy="124" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="509.5" cy="118" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="614" cy="184.5" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="650" cy="183.5" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="603" cy="40" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="475" cy="161.5" r="11" fill="none" stroke="#6b7480" stroke-width="3"/>
  <circle cx="557.5" cy="114" r="13" fill="#e8590c" stroke="#ffffff" stroke-width="2.5"/>
  <circle cx="564.5" cy="65" r="22" fill="none" stroke="#ffc078" stroke-width="4"/>
  <line x1="586" y1="50" x2="613.5" y2="31.5" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M629,21 L617.5,39.5 L607.5,24.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="612.5" cy="84.5" r="22" fill="none" stroke="#ffc078" stroke-width="4"/>
  <line x1="593.5" y1="102" x2="569" y2="124" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M555,137 L563.5,117 L576,130 Z" fill="#e8590c" stroke-linejoin="round"/>
  <rect x="900" y="330" width="200" height="140" rx="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="924" y="350" width="152" height="70" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M940,410 A60,60 0 0 1 1060,410" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round"/>
  <line x1="1000" y1="410" x2="1036" y2="366" stroke="#e8590c" stroke-width="4" stroke-linecap="round"/>
  <circle cx="1000" cy="410" r="6" fill="#1f2933"/>
  <circle cx="940" cy="446" r="10" fill="#1f2933"/>
  <circle cx="1060" cy="446" r="10" fill="#e8590c"/>
  <path d="M900,400 C860,400 840,300 800,280" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M800,280 L700,262 L696,284 L796,302 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="684" y="258" width="14" height="30" rx="3" fill="#1f2933"/>
</svg>

## Key idea

### The decay of a single nucleus is random
A radioactive nucleus decays and becomes another nucleus (chapter *The atomic nucleus and radioactive decay*), but the moment of decay cannot be predicted. Of two identical nuclei, one may decay at once and the other only after years. All that can be predicted is how likely a nucleus is to decay within a given time. This probability is the same for all nuclei of the same isotope, and in practice it does not depend on the temperature, the pressure or the chemical bonds of the surroundings. Nor does it depend on the age of the nucleus: a nucleus does not grow old. A nucleus that has survived without decaying for a long time is just as likely to decay during the next second as a newly formed one.

### A large group of nuclei behaves regularly
Because every nucleus has the same probability of decaying, about the same *fraction* of the remaining nuclei decays in a given time. In the figure, of the same hundred nuclei about half are left after one half-life and about a quarter after two, but the decayed nuclei are in random places. In a small group chance shows: the fraction can differ clearly from a half. An ordinary sample, however, contains for example $10^{15}$ nuclei, and then the relative deviations are so small that they cannot be noticed.

<svg data-fig="ydin" viewBox="0 0 600 330" role="img" aria-label="Three grids side by side: the same 100 radioactive nuclei at three moments. An undecayed nucleus is an orange filled circle, a decayed nucleus a grey ring. At the time t = 0 all 100 are undecayed. After one half-life 52 are undecayed and after two half-lives 28. The decayed nuclei are in random places of the grid, and neither the place nor the age of a nucleus predicts its decay." style="max-width:100%;font-size:24px">
  <rect x="24" y="58" width="162" height="162" rx="6" fill="#f6f1e6" stroke="#c9c2b2" stroke-width="1.5"/>
  <circle cx="37.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="37.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="52.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="67.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="82.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="97.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="112.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="127.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="142.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="157.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="172.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="82.5" y="15.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 0$</div></foreignObject>
  <foreignObject x="70" y="237.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 100$</div></foreignObject>
  <line x1="205" y1="62" x2="205" y2="222" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="214" y="58" width="162" height="162" rx="6" fill="#f6f1e6" stroke="#c9c2b2" stroke-width="1.5"/>
  <circle cx="227.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="257.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="272.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="287.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="302.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="332.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="362.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="242.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="257.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="272.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="317.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="332.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="227.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="257.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="272.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="287.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="332.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="257.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="272.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="332.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="257.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="272.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="287.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="302.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="332.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="347.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="242.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="257.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="272.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="317.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="332.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="347.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="227.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="257.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="272.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="332.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="347.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="242.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="257.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="272.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="287.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="317.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="332.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="242.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="257.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="272.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="302.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="332.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="347.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="362.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="227.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="242.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="257.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="272.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="287.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="302.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="317.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="332.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="347.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="362.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="253.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = T_{1/2}$</div></foreignObject>
  <foreignObject x="266" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 52$</div></foreignObject>
  <line x1="395" y1="62" x2="395" y2="222" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="404" y="58" width="162" height="162" rx="6" fill="#f6f1e6" stroke="#c9c2b2" stroke-width="1.5"/>
  <circle cx="417.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="492.5" cy="71.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="507.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="71.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="447.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="462.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="477.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="86.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="552.5" cy="86.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="417.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="432.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="462.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="101.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="432.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="447.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="462.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="477.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="116.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="507.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="116.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="447.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="131.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="537.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="131.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="477.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="146.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="146.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="417.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="432.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="477.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="522.5" cy="161.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="537.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="161.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="447.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="507.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="176.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="552.5" cy="176.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="507.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="522.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="191.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="552.5" cy="191.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="417.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="432.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="447.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="462.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="477.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="492.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="507.5" cy="206.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="522.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="537.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <circle cx="552.5" cy="206.5" r="3.96" fill="none" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="437.5" y="15.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 2T_{1/2}$</div></foreignObject>
  <foreignObject x="456" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$N = 28$</div></foreignObject>
  <foreignObject x="113" y="285.5" width="374" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{orange: undecayed,\ grey: decayed}$</div></foreignObject>
</svg>

### Half-life
The **half-life** $T_{1/2}$ is the time in which half of the undecayed nuclei of a sample decay. During the next half-life half of the *remaining* nuclei decay, so after two half-lives a quarter is left, not nothing. The half-life is a property of the isotope: it does not depend on the size of the sample or on when the timing is started. The table lists some half-lives; the unit $\text{d}$ is a day and $\text{a}$ a year.

| Isotope | $T_{1/2}$ | Where |
| --- | --- | --- |
| barium-$137\text{m}$ | $2.55\,\text{min}$ | school decay experiment |
| fluorine-18 | $110\,\text{min}$ | PET scan |
| technetium-$99\text{m}$ | $6.01\,\text{h}$ | isotope imaging |
| radon-222 | $3.82\,\text{d}$ | radon in indoor air |
| iodine-131 | $8.02\,\text{d}$ | thyroid treatment |
| caesium-137 | $30.1\,\text{a}$ | Chernobyl fallout |
| carbon-14 | $5700\,\text{a}$ | radiocarbon dating |
| uranium-238 | $4.47 \cdot 10^{9}\,\text{a}$ | bedrock |

Source: literature values from the NNDC NuDat 3 database (Brookhaven National Laboratory), rounded to three significant figures.

### Activity
The **activity** $A$ of a sample is the number of decays in it per unit of time. Its unit is the becquerel: $1\,\text{Bq}$ is one decay per second, that is, $1\,\tfrac{1}{\text{s}}$. Because every nucleus is equally likely to decay, the activity is directly proportional to the number of undecayed nuclei: when half of the nuclei are left, the activity has also halved. A radiation meter does not measure the activity directly. It counts the pulses from the quanta of radiation that hit its detector. The number of pulses is proportional to the activity, but the **background radiation** of the surroundings is always added to it.

## Formula: The decay law

### The half-life in the form of a law
If a sample initially contains $N_0$ undecayed nuclei, every half-life multiplies the number by $\tfrac{1}{2}$. After a time $t$ the number of undecayed nuclei is
```latex
N = N_0 \left(\frac{1}{2}\right)^{t/T_{1/2}}
```
where $N$ is the number of undecayed nuclei at the time $t$, $N_0$ their number at the time $t = 0$ and $T_{1/2}$ the half-life. The exponent $\tfrac{t}{T_{1/2}}$ tells how many half-lives have passed, and it need not be an integer. The time $t$ and the half-life must be in the same unit. The law describes the behaviour of a large group of nuclei: in a small group the real $N$ deviates from it randomly.

<svg data-fig="kuvaaja" viewBox="0 0 600 380" role="img" aria-label="Graph to scale: the number N of undecayed nuclei as a function of time. On the horizontal axis the time in half-lives from zero to five, on the vertical axis N, the scale from zero to the initial number N zero in quarters. The curve starts from the value N zero and falls ever more gently. Dashed lines show that at one half-life a half of the initial number is left, at two a quarter and at three an eighth. The curve never reaches zero." style="max-width:100%;font-size:24px">
  <line x1="178" y1="312" x2="178" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256.5" y1="312" x2="256.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="334.5" y1="312" x2="334.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="412.5" y1="312" x2="412.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="491" y1="312" x2="491" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="253" x2="530" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="194.5" x2="530" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="135.5" x2="530" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="77" x2="530" y2="77" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="544" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M556,312 L543,318 L543,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="178" y1="312" x2="178" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="149" y="321.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_{1/2}$</div></foreignObject>
  <line x1="256.5" y1="312" x2="256.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="221.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2T_{1/2}$</div></foreignObject>
  <line x1="334.5" y1="312" x2="334.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3T_{1/2}$</div></foreignObject>
  <line x1="412.5" y1="312" x2="412.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="377.5" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4T_{1/2}$</div></foreignObject>
  <line x1="491" y1="312" x2="491" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="456" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5T_{1/2}$</div></foreignObject>
  <line x1="93" y1="253" x2="100" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="238.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{4}N_0$</div></foreignObject>
  <line x1="93" y1="194.5" x2="100" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="180" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}N_0$</div></foreignObject>
  <line x1="93" y1="135.5" x2="100" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="121" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{3}{4}N_0$</div></foreignObject>
  <line x1="93" y1="77" x2="100" y2="77" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="62.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N_0$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="562" y="297.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <polyline points="100,77 103.5,84 107,91.5 111,98 114.5,105 118,111.5 121.5,117.5 125,123.5 128.5,129.5 132,135.5 136,141 139.5,146 143,151.5 146.5,156.5 150,161.5 154,166 157.5,170.5 161,175 164.5,179 168,183.5 171.5,187.5 175,191.5 179,195 182.5,198.5 186,202.5 189.5,205.5 193,209 197,212.5 200.5,215.5 204,218.5 207.5,221.5 211,224 214.5,227 218,229.5 222,232 225.5,234.5 229,237 232.5,239.5 236,241.5 240,244 243.5,246 247,248 250.5,250 254,252 257.5,254 261,255.5 265,257.5 268.5,259 272,261 275.5,262.5 279,264 283,265.5 286.5,267 290,268.5 293.5,269.5 297,271 300.5,272.5 304,273.5 308,274.5 311.5,276 315,277 318.5,278 322,279 326,280 329.5,281 333,282 336.5,283 340,284 343.5,285 347,285.5 351,286.5 354.5,287.5 358,288 361.5,289 365,289.5 369,290.5 372.5,291 376,291.5 379.5,292.5 383,293 386.5,293.5 390,294 394,294.5 397.5,295 401,295.5 404.5,296 408,296.5 412,297 415.5,297.5 419,298 422.5,298.5 426,299 429.5,299.5 433,299.5 437,300 440.5,300.5 444,301 447.5,301 451,301.5 455,302 458.5,302 462,302.5 465.5,303 469,303 472.5,303.5 476,303.5 480,304 483.5,304 487,304.5 490.5,304.5 494,305 498,305 501.5,305.5 505,305.5 508.5,305.5 512,306 515.5,306 519,306.5 523,306.5 526.5,306.5 530,307" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="178" y1="194.5" x2="178" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="178" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="178" cy="194.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="256.5" y1="253" x2="256.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="253" x2="256.5" y2="253" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="256.5" cy="253" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="334.5" y1="282.5" x2="334.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="282.5" x2="334.5" y2="282.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="334.5" cy="282.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="77" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="356.5" y="236" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\tfrac{1}{8}N_0$</div></foreignObject>
  <foreignObject x="213.5" y="86" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$</span></div></foreignObject>
</svg>

### The decay constant and activity
The probability of a nucleus decaying per unit of time is described by the **decay constant** $\lambda$, whose unit is $\tfrac{1}{\text{s}}$. When there are $N$ nuclei, on average $\lambda N$ nuclei decay per second, so the activity is
```latex
A = \lambda N
```
where $A$ is the activity ($\text{Bq}$), $\lambda$ the decay constant ($\tfrac{1}{\text{s}}$) and $N$ the number of undecayed nuclei. The decay law can also be written with the natural exponential function:
```latex
N = N_0 e^{-\lambda t}
```
At the half-life $N = \tfrac{1}{2}N_0$, so $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$, that is, $\lambda T_{1/2} = \ln 2$. The decay constant and the half-life are therefore related by the equation
```latex
\lambda = \frac{\ln 2}{T_{1/2}}
```
where $\ln 2 \approx 0.693$. For example, for technetium-$99\text{m}$ $\lambda = \tfrac{0.693}{6.01 \cdot 3600\,\text{s}} \approx 3.20 \cdot 10^{-5}\,\tfrac{1}{\text{s}}$: of a million nuclei, on average about $32$ decay per second. Because $A = \lambda N$ and $\lambda$ is constant, the activity decreases according to the same law as the number of nuclei:
```latex
A = A_0 \left(\frac{1}{2}\right)^{t/T_{1/2}}
```
where $A_0$ is the activity at the time $t = 0$. The mass of the undecayed substance decreases in the same way, because it is proportional to the number of nuclei.

### Fitting an exponential function to measurement data
The half-life is determined by measuring the number of pulses of a sample at regular intervals. In real series of measurements the data points are usually not exactly on the curve of the model, because of the randomness of decay and the measurement uncertainty. That is why the model
```latex
y = A\,e^{-Ct} + B
```
is fitted to the points, where $y$ is the number of pulses in a measuring period, $C$ the decay constant $\lambda$ and $B$ the number of pulses of the background radiation in the same period. The coefficient $A$ of the program is the number of pulses at the time $t = 0$ without the background, not the activity. The half-life is obtained from the coefficient of the fit: $T_{1/2} = \tfrac{\ln 2}{C}$.

In Graphical Analysis Pro the fit is made as follows:

1. In the start window, choose **Manual Entry** and type the time (s) and the number of pulses into the table.
2. Open the menu of graph tools from the icon in the lower left corner of the graph and choose **Curve Fit**.
3. From the drop-down menu, choose the exponential fit whose equation is of the form $A \cdot \exp(-C \cdot x) + B$ (*Natural Exponent*), and accept it with the **Apply** button.
4. Read the coefficients $A$, $B$ and $C$ from the result box.

The data in the figure are simulated from a decay experiment with barium-$137\text{m}$. The fit gives $C = 0.004564\,\tfrac{1}{\text{s}}$, so $T_{1/2} = 0.6931 : 0.004564\,\tfrac{1}{\text{s}} \approx 152\,\text{s}$. The literature value is $2.552\,\text{min} = 153\,\text{s}$, so the difference is less than one percent. The coefficient $B \approx 4.8$ pulses in a period of $10\,\text{s}$ is the level of the background radiation, towards which the points approach.

<svg data-fig="sovitus" viewBox="0 0 600 380" role="img" aria-label="Graph to scale, simulated example data: the number of pulses of a barium-137m sample in periods of 10 seconds as a function of time, time from zero to 900 seconds, 16 data points at intervals of 60 seconds. In the first period there are 249 pulses, and the number decreases exponentially towards the level of the background radiation, about 5 pulses in 10 seconds. A fitted curve A times e to the power minus C t plus B is drawn through the points, and the level B of the background radiation is a horizontal dashed line. The points are on both sides of the curve." style="max-width:100%;font-size:24px">
  <line x1="162.5" y1="312" x2="162.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="225.5" y1="312" x2="225.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="312" x2="288" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350.5" y1="312" x2="350.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="413.5" y1="312" x2="413.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="312" x2="476" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="263" x2="476" y2="263" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="214.5" x2="476" y2="214.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="165.5" x2="476" y2="165.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="116.5" x2="476" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="68" x2="476" y2="68" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="490" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,312 L489,318 L489,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="162.5" y1="312" x2="162.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="140" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="225.5" y1="312" x2="225.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="203" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="288" y1="312" x2="288" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="265.5" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$450$</div></foreignObject>
  <line x1="350.5" y1="312" x2="350.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="328" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="413.5" y1="312" x2="413.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="391" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$750$</div></foreignObject>
  <line x1="476" y1="312" x2="476" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="321.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$900$</div></foreignObject>
  <line x1="93" y1="263" x2="100" y2="263" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="248.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="214.5" x2="100" y2="214.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="200" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="165.5" x2="100" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="116.5" x2="100" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="102" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="93" y1="68" x2="100" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="53.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="297.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="153" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{pulses}\ /\ 10\,\text{s}$</div></foreignObject>
  <polyline points="100,307.5 476,307.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="106.5" y="275" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$B$</div></foreignObject>
  <polyline points="100,63.5 103,71.5 106.5,79.5 109.5,87 112.5,94.5 115.5,101.5 119,108.5 122,115.5 125,122 128,128 131.5,134 134.5,140 137.5,145.5 140.5,151 144,156 147,161.5 150,166 153.5,171 156.5,175.5 159.5,180 162.5,184.5 166,188.5 169,192.5 172,196.5 175,200 178.5,203.5 181.5,207 184.5,210.5 187.5,214 191,217 194,220 197,223 200.5,225.5 203.5,228.5 206.5,231 209.5,233.5 213,236 216,238.5 219,241 222,243 225.5,245.5 228.5,247.5 231.5,249.5 234.5,251.5 238,253 241,255 244,257 247.5,258.5 250.5,260 253.5,261.5 256.5,263.5 260,265 263,266 266,267.5 269,269 272.5,270 275.5,271.5 278.5,272.5 281.5,274 285,275 288,276 291,277 294.5,278 297.5,279 300.5,280 303.5,281 307,282 310,282.5 313,283.5 316,284.5 319.5,285 322.5,286 325.5,286.5 328.5,287.5 332,288 335,288.5 338,289 341.5,290 344.5,290.5 347.5,291 350.5,291.5 354,292 357,292.5 360,293 363,293.5 366.5,294 369.5,294.5 372.5,295 375.5,295.5 379,295.5 382,296 385,296.5 388.5,297 391.5,297 394.5,297.5 397.5,298 401,298 404,298.5 407,299 410,299 413.5,299.5 416.5,299.5 419.5,300 422.5,300 426,300.5 429,300.5 432,301 435.5,301 438.5,301.5 441.5,301.5 444.5,301.5 448,302 451,302 454,302 457,302.5 460.5,302.5 463.5,302.5 466.5,303 469.5,303 473,303 476,303.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="100" cy="68.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="125" cy="111" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="150" cy="171.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="175" cy="195" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="200.5" cy="233" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="225.5" cy="242.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250.5" cy="263" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275.5" cy="274" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="300.5" cy="276" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="325.5" cy="291.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350.5" cy="291.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="375.5" cy="289.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="401" cy="298.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="426" cy="301.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451" cy="303" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="476" cy="302" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="217" y="97" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$y = A\,e^{-Ct} + B$</span></div></foreignObject>
</svg>

## Worked example
An iodine-131 capsule made for the treatment of thyroid cancer has an activity of $550\,\text{MBq}$ at the time of manufacture. The half-life of iodine-131 is $8.02\,\text{d}$. What is the activity of the capsule $20.0\,\text{d}$ later?

<!-- vaihe -->

**Known and asked.** The initial activity is $A_0 = 550\,\text{MBq}$, the half-life $T_{1/2} = 8.02\,\text{d}$ and the time $t = 20.0\,\text{d}$. The activity $A$ at the time $t$ is asked.

<!-- vaihe -->

**Principle.** The activity is proportional to the number of undecayed nuclei, $A = \lambda N$, so it follows the same decay law: every half-life halves it. The capsule contains an enormous number of nuclei, so random deviations from the law are insignificant.

<!-- vaihe -->

**Formula solved.** The asked activity is obtained directly from the decay law:
```latex
A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}
```

<!-- vaihe -->

**Unit conversions.** None are needed: the time and the half-life are both in days, so their ratio is a pure number, and the activity is obtained in the same unit as $A_0$, that is, in megabecquerels.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}} \\
&= 550\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{20.0\,\text{d} / 8.02\,\text{d}} \\
&= 550\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{2.4938} \\
&= 550\,\text{MBq} \cdot 0.17754 \\
&= 97.65\,\text{MBq}
\end{aligned}
```

<!-- vaihe -->

**Result.** After $20.0\,\text{d}$ the activity of the capsule is about $97.6\,\text{MBq}$, with three significant figures like the half-life $8.02\,\text{d}$ and the time $20.0\,\text{d}$.

<!-- vaihe -->

**Reasonableness.** A little less than two and a half half-lives passed. After two half-lives the activity would be $550\,\text{MBq} : 4 \approx 138\,\text{MBq}$ and after three $550\,\text{MBq} : 8 \approx 69\,\text{MBq}$. The result $97.6\,\text{MBq}$ is between these, as it should be.

## Common misconception
Many people think that if half of the nuclei decay in one half-life, the rest decay in the next, and after two half-lives the sample is empty. Decay, however, does not proceed at a constant rate. In every half-life half of the *remaining* nuclei decay, so a quarter is left, then an eighth, and so on. The activity decreases at the same pace, because the fewer nuclei are left, the fewer decays there are.

Another mistake is to think that a nucleus that has lasted a long time is "due" and therefore more likely to decay. A nucleus has no memory: its probability of decaying during the next second is always the same, and that is why the same fraction of the remaining nuclei decays in every half-life.

## Summary
- The moment of decay of a single nucleus cannot be predicted. Every nucleus of the same isotope has the same probability of decaying per unit of time, and it does not depend on the age of the nucleus.
- The half-life $T_{1/2}$ is the time in which half of the undecayed nuclei decay: $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}} = N_0 e^{-\lambda t}$.
- The decay constant is $\lambda = \tfrac{\ln 2}{T_{1/2}}$, and the activity is $A = \lambda N$, with the unit $1\,\text{Bq} = 1\,\tfrac{1}{\text{s}}$. The activity decreases according to the same decay law as the number of nuclei.
- The half-life is determined by fitting the function $y = A\,e^{-Ct} + B$ to the data points: $C$ is the decay constant and $B$ the background radiation, and $T_{1/2} = \tfrac{\ln 2}{C}$.
