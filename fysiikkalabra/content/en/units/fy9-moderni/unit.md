# Quantum phenomena, the nucleus and radiation

> **Why** do the bright red grow lights of a greenhouse not damage the DNA of the plants or of the gardener, even though their power is kilowatts, while even weak X-rays can?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a glass greenhouse on a snowy winter night. There are stars in the dark sky and spruce forest in the background. Under the roof of the greenhouse are rows of red and blue LED lamps whose light fills the greenhouse with a pink glow. Inside, rows of tomato plants with red tomatoes are growing. The light is reflected on the snow in front of the greenhouse." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-moderni-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

What joins the phenomena of the module is **quantised energy**. Light exchanges energy with matter as photons whose energy is $E = hf$, and one photon gives its energy to one electron. The electrons of an atom and the nucleons of a nucleus can only be in certain energy states, so in transitions a photon of a definite energy is created or disappears. The differences between electron levels are electronvolts, the energies of nuclear levels and nuclear reactions millions of electronvolts. In the nucleus mass and energy are linked: $E = mc^2$.

```pysahdy
To how many electrons does one photon give its energy?
---
One photon gives its energy to one electron.
```

<svg data-fig="kartta" viewBox="0 0 380 896" role="img" aria-label="Recognition chart: how do I tell which law to use? First see which quantity the task gives, then which sign fits. Frequency or wavelength of a photon: the photon energy is Planck&#x27;s constant times the frequency. Light ejects electrons: in the photoelectric effect the photon energy is the work function plus the maximum kinetic energy of the electron. An atom emits or absorbs: a quantum jump, the photon energy is the difference between the upper and lower energy levels. A nucleus decays as time passes: the decay law, the amount left is the initial amount times e to the power minus the decay constant times the time. How many decays per second: the activity is the decay constant times the number of nuclei. Mass difference of a nuclear reaction: the released energy is the mass difference times the speed of light squared. The type of radiation matters: the equivalent dose is the radiation weighting factor times the absorbed dose. The distance from the source changes: for a point source the dose rate is inversely proportional to the square of the distance. Radiation passes through matter: the attenuation law, the intensity is the initial intensity times e to the power minus the attenuation coefficient times the thickness." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="852" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{which quantity is given? then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{frequency or wavelength of a photon}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{photon energy}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = hf$</div></foreignObject>
  <line x1="14" y1="235" x2="30" y2="235" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{light ejects electrons}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{photoelectric effect}$</div></foreignObject>
  <rect x="182" y="257" width="180" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="186" y="260" width="172" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$hf = W + E_\text{k,max}$</div></foreignObject>
  <line x1="14" y1="336" x2="30" y2="336" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="300" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="310.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{an atom emits or absorbs}$</div></foreignObject>
  <line x1="40" y1="340" x2="362" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="345" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{quantum jump}$</div></foreignObject>
  <rect x="238" y="344" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="346" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$hf = E_\text{u} - E_\text{l}$</div></foreignObject>
  <line x1="14" y1="422" x2="30" y2="422" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a nucleus decays as time passes}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{decay law}$</div></foreignObject>
  <rect x="238" y="430" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="432" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$N = N_0 e^{-\lambda t}$</div></foreignObject>
  <line x1="14" y1="508" x2="30" y2="508" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{how many decays per second}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{activity}$</div></foreignObject>
  <rect x="238" y="516" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="518" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$A = \lambda N$</div></foreignObject>
  <line x1="14" y1="594" x2="30" y2="594" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="558" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="568.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{mass difference of a nuclear reaction}$</div></foreignObject>
  <line x1="40" y1="598" x2="362" y2="598" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="603" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{released energy}$</div></foreignObject>
  <rect x="238" y="602" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="604" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = \Delta m c^2$</div></foreignObject>
  <line x1="14" y1="680" x2="30" y2="680" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="644" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="654.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{the type of radiation matters}$</div></foreignObject>
  <line x1="40" y1="684" x2="362" y2="684" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="689" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{equivalent dose}$</div></foreignObject>
  <rect x="238" y="688" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="690" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$H = w_\text{R} D$</div></foreignObject>
  <line x1="14" y1="766" x2="30" y2="766" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="730" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="740.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{the distance from the source changes}$</div></foreignObject>
  <line x1="40" y1="770" x2="362" y2="770" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="775" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{point source}$</div></foreignObject>
  <rect x="238" y="774" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="776" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\dot{H} \propto 1/r^2$</div></foreignObject>
  <line x1="14" y1="852" x2="30" y2="852" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="816" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="826.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{radiation passes through matter}$</div></foreignObject>
  <line x1="40" y1="856" x2="362" y2="856" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="861" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{attenuation}$</div></foreignObject>
  <rect x="238" y="860" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="862" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$I = I_0 e^{-\mu x}$</div></foreignObject>
</svg>

In a modern physics problem in the exam it pays to ask first what one particle does: what is the energy of one photon, which transition or decay happens and which numbers are conserved. Only then do you calculate how many photons or nuclei there are, that is the power, the activity or the dose.

This answers the opening question. The energy of a red photon of a grow light ($660\,\text{nm}$) is $E = \tfrac{hc}{\lambda} \approx 1.9\,\text{eV}$, which is much less than the ionisation energy of a water molecule, $12.6\,\text{eV}$. A larger power only brings more photons of the same kind, and not one of them frees an electron. The photon energy of a dental X-ray is about $60\,\text{keV}$, over $30\,000$ times as much, so a single photon can already ionise and damage DNA.

<svg data-fig="fotonit" viewBox="0 0 600 392" role="img" aria-label="Diagram, an energy axis on a logarithmic scale: the photon energy in electronvolts from a tenth to ten million, each division ten times the previous one. Visible light is a narrow coloured band 1.7–3.3 electronvolts, and the photon of red LED light is 1.9 electronvolts. A dashed line at 12.6 electronvolts is the ionisation energy of a water molecule: to its left a photon does not ionise water, to its right it does. The photon of a dental X-ray, about 60 kiloelectronvolts, and the gamma photon of caesium-137, 662 kiloelectronvolts, are far to the right. Brackets below the axis: the differences between the energy levels of the electrons of an atom are of the order of electronvolts, those of the nucleus of kilo- and megaelectronvolts." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy9mo-vis" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c92a2a"/><stop offset="0.35" stop-color="#e8590c"/><stop offset="0.6" stop-color="#2b8a3e"/><stop offset="1" stop-color="#1971c2"/></linearGradient></defs>
  <rect x="184" y="92" width="374" height="104" fill="#f2a69c" fill-opacity="0.28"/>
  <rect x="130.5" y="182" width="18" height="28" fill="url(#fy9mo-vis)" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="40" y1="196" x2="576" y2="196" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M588,196 L575,202 L575,190 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="54" y1="196" x2="54" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="196" x2="116" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="106" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="178" y1="196" x2="178" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="196" x2="240" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="217.5" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{2}$</div></foreignObject>
  <line x1="302" y1="196" x2="302" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="364" y1="196" x2="364" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="341.5" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{4}$</div></foreignObject>
  <line x1="426" y1="196" x2="426" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="488" y1="196" x2="488" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="465.5" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10^{6}$</div></foreignObject>
  <line x1="550" y1="196" x2="550" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="514" y="161.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E\ (\text{eV})$</div></foreignObject>
  <line x1="184" y1="48" x2="184" y2="212" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <foreignObject x="192" y="13.5" width="382" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ionisation energy of water } 12.6\,\text{eV}$</div></foreignObject>
  <foreignObject x="0" y="55.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{does not ionise}$</div></foreignObject>
  <foreignObject x="198" y="55.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{ionises}$</div></foreignObject>
  <line x1="133" y1="182" x2="133" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="133" cy="182" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="12" y="97.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{red LED}$</div></foreignObject>
  <foreignObject x="12" y="127.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1.9\,\text{eV}$</div></foreignObject>
  <line x1="412" y1="196" x2="412" y2="150" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="412" cy="196" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="363" y="89.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{X-ray}$</div></foreignObject>
  <foreignObject x="356.5" y="119.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60\,\text{keV}$</div></foreignObject>
  <line x1="477" y1="196" x2="477" y2="150" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="477" cy="196" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="464" y="89.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gamma}$</div></foreignObject>
  <foreignObject x="451.5" y="119.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$662\,\text{keV}$</div></foreignObject>
  <path d="M116,254 V262 H240 V254" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="86.5" y="271.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{electron levels}$</div></foreignObject>
  <path d="M364,254 V262 H550 V254" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="372" y="271.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nuclear levels}$</div></foreignObject>
  <foreignObject x="124.5" y="311.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{visible light } 1.7\text{–}3.3\,\text{eV}$</div></foreignObject>
  <foreignObject x="380" y="347.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{logarithmic scale}$</div></foreignObject>
</svg>

## Formula: Photons, the nucleus and radiation

### The photon and the atom

```kaavat
photon energy :: E = hf = \frac{hc}{\lambda}
hf = W + E_\text{k,max}
hf = E_\text{u} - E_\text{l}
photon momentum :: p = \frac{E}{c} = \frac{h}{\lambda}
```

where $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is the Planck constant, $f$ the frequency, $\lambda$ the wavelength, $W$ the work function of the metal, $E_\text{k,max}$ the largest kinetic energy of an emitted electron, $E_\text{u}$ and $E_\text{l}$ the energies of the upper and the lower energy state and $p$ the momentum of the photon. Electrons are emitted only when $hf \geq W$. An atom absorbs only a photon whose energy is exactly the difference of levels, unless the photon ionises the atom. For hydrogen $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$. At the threshold voltage of an LED $eU_\text{k} \approx hf$. Conversions: $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$ and $hc \approx 1240\,\text{eV}\,\text{nm}$.

```pysahdy
Are electrons released from a metal if the photon energy $hf$ is smaller than the work function $W$?
---
No, because electrons are released only when $hf \geq W$.
```

### The nucleus and decay

```kaavat
law of radioactive decay :: N = N_0 e^{-\lambda t}
activity :: A = \lambda N
decay constant :: \lambda = \frac{\ln 2}{T_{1/2}}
mass difference in a nuclear reaction :: \Delta m = m_\text{reactants} - m_\text{products}
energy released in a nuclear reaction :: E = \Delta m c^2
```

where $N$ is the number of undecayed nuclei at the time $t$, $N_0$ the number at the start, $T_{1/2}$ the half-life, $A$ the activity ($\text{Bq}$), $\lambda$ the decay constant, $\Delta m$ the mass difference and $E$ the energy released in the reaction. Because $e^{-\lambda T_{1/2}} = \tfrac12$, the decay law can also be written $N = N_0 \left(\tfrac12\right)^{t/T_{1/2}}$, and the same law holds for the activity, $A = A_0 e^{-\lambda t}$. In a decay equation the mass number and the charge number are conserved: in alpha decay $Z$ decreases by two and $A$ by four, in beta minus decay $Z$ increases by one. The decay law describes a large set of nuclei. The binding energy is $E_\text{B} = \Delta m\,c^2$, and $1\,\text{u} = 931.5\,\tfrac{\text{MeV}}{c^2}$. Fission and fusion release energy, because the binding energy per nucleon of the products is larger.

```pysahdy
What fraction of the nuclei has not decayed after the time $2T_{1/2}$?
---
By the decay law $N = N_0 \left(\tfrac12\right)^{t/T_{1/2}}$ we get $N = N_0 \left(\tfrac12\right)^{2} = \tfrac14 N_0$, that is, one quarter.
```

<svg data-fig="puolitus" viewBox="0 0 600 380" role="img" aria-label="Graph to scale: the remaining fraction as a function of the number n of half-lives or half-value thicknesses, n from zero to five. The curve starts at 1 and falls ever more gently. Dashed lines show that n = 1 gives a half, n = 2 a quarter and n = 3 an eighth. The curve approaches zero but does not reach it: decay and the attenuation of gamma radiation have no end point." style="max-width:100%;font-size:26px">
  <line x1="174" y1="312" x2="174" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="312" x2="248" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="322" y1="312" x2="322" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396" y1="312" x2="396" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="312" x2="470" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="281" x2="470" y2="281" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="249.5" x2="470" y2="249.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="218" x2="470" y2="218" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="187" x2="470" y2="187" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="156" x2="470" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="124.5" x2="470" y2="124.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="93" x2="470" y2="93" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="62" x2="470" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="484" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,312 L483,318 L483,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,36 L106,49 L94,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="174" y1="312" x2="174" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="163" y="320.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$1$</div></foreignObject>
  <line x1="248" y1="312" x2="248" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="320.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$2$</div></foreignObject>
  <line x1="322" y1="312" x2="322" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311" y="320.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$3$</div></foreignObject>
  <line x1="396" y1="312" x2="396" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="320.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$4$</div></foreignObject>
  <line x1="470" y1="312" x2="470" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="459" y="320.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$5$</div></foreignObject>
  <line x1="93" y1="281" x2="100" y2="281" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="249.5" x2="100" y2="249.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="234" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$\tfrac14$</div></foreignObject>
  <line x1="93" y1="218" x2="100" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="187" x2="100" y2="187" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="171.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$\tfrac12$</div></foreignObject>
  <line x1="93" y1="156" x2="100" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="124.5" x2="100" y2="124.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="93" x2="100" y2="93" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="62" x2="100" y2="62" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="46.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$1$</div></foreignObject>
  <foreignObject x="68" y="316.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="502" y="296.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$n$</div></foreignObject>
  <foreignObject x="90" y="4.5" width="134" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$N/N_0,\ I/I_0$</div></foreignObject>
  <polyline points="100,62 103,69 106,76 109,82.5 112.5,89.5 115.5,95.5 118.5,102 121.5,108 124.5,113.5 128,119 131,124.5 134,130 137,135 140,140.5 143,145 146,150 149.5,154.5 152.5,159 155.5,163.5 158.5,167.5 161.5,171.5 165,175.5 168,179.5 171,183.5 174,187 177,190.5 180,194 183,197.5 186.5,200.5 189.5,204 192.5,207 195.5,210 198.5,213 202,215.5 205,218.5 208,221 211,223.5 214,226 217,228.5 220,231 223.5,233.5 226.5,235.5 229.5,237.5 232.5,240 235.5,242 239,244 242,246 245,247.5 248,249.5 251,251.5 254,253 257,254.5 260.5,256.5 263.5,258 266.5,259.5 269.5,261 272.5,262.5 276,264 279,265 282,266.5 285,268 288,269 291,270.5 294,271.5 297.5,272.5 300.5,273.5 303.5,275 306.5,276 309.5,277 313,278 316,279 319,280 322,281 325,281.5 328,282.5 331,283.5 334.5,284 337.5,285 340.5,285.5 343.5,286.5 346.5,287 350,288 353,288.5 356,289.5 359,290 362,290.5 365,291 368,291.5 371.5,292.5 374.5,293 377.5,293.5 380.5,294 383.5,294.5 387,295 390,295.5 393,296 396,296.5 399,297 402,297.5 405,297.5 408.5,298 411.5,298.5 414.5,299 417.5,299 420.5,299.5 424,300 427,300.5 430,300.5 433,301 436,301.5 439,301.5 442,302 445.5,302 448.5,302.5 451.5,302.5 454.5,303 457.5,303 461,303.5 464,303.5 467,304 470,304" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="174" y1="187" x2="174" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="187" x2="174" y2="187" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="174" cy="187" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="248" y1="249.5" x2="248" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="249.5" x2="248" y2="249.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="248" cy="249.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="322" y1="281" x2="322" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="281" x2="322" y2="281" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="322" cy="281" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="62" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="336" y="252" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac18$</div></foreignObject>
  <foreignObject x="277.5" y="79" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$n = t/T_{1/2}$</span></div></foreignObject>
  <foreignObject x="277.5" y="110" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{or}\ n = d/d_{1/2}$</span></div></foreignObject>
</svg>

### Radiation and dose

```kaavat
D = \frac{E}{m}
equivalent dose :: H = w_\text{R} D
+ H = \dot{H} t
attenuation law :: I = I_0 e^{-\mu x}
```

where $D$ is the absorbed dose ($\text{Gy}$), $E$ the absorbed energy, $m$ the mass of the tissue, $H$ the equivalent dose ($\text{Sv}$), $w_\text{R}$ the radiation weighting factor (alpha $20$, beta and gamma $1$), $I_0$ the intensity of the radiation arriving at the surface of the medium and $I$ the intensity of the radiation that passes through, $\mu$ the attenuation coefficient ($1/\text{m}$) and $x$ the thickness of the medium. The half-value thickness is $d_{1/2} = \tfrac{\ln 2}{\mu}$. It applies to photon radiation, because alpha and beta radiation have a range. The recession speed of galaxies is $v = H_0 d$, and for a small redshift $v = cz$.

The **dose rate** $\dot{H}$ ($\text{Sv/h}$) is the equivalent dose per unit time, and $t$ is the time over which the dose accumulates at a constant dose rate. Behind a shield the dose rate decreases as $\dot{H} = \dot{H}_0 \left(\tfrac12\right)^{x/d_{1/2}}$. The formula $H = \dot{H} t$ is extra information: it is not in the MAFY tables, and an exam gives it in the task when it is needed.

A point source radiates evenly in all directions, and the air does not attenuate the radiation. At the distance $r_1$ ($\text{m}$) from the source the dose rate is $\dot{H}_1$, and at the distance $r_2$ it is $\dot{H}_2$.

<svg data-fig="pallo" viewBox="0 0 530 372" role="img" aria-label="Schematic, no numerical values. On the left is a point source from which radiation leaves evenly in all directions. Around the source are two sphere surfaces, the nearer one at the distance r 1 and the farther one at the distance r 2. A beam of radiation from the source meets both surfaces. Farther away the same radiation is spread over a larger area. At the nearer surface the dose rate is H dot 1 and at the farther surface H dot 2." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-moderni-pallo.webp" x="-1.1" y="0" width="532.7" height="379.5" preserveAspectRatio="none"/>
  <foreignObject x="125" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_1$</div></foreignObject>
  <foreignObject x="149.5" y="233" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r_2$</div></foreignObject>
  <foreignObject x="-2.5" y="210.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{point source}$</div></foreignObject>
  <foreignObject x="254" y="170.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\dot{H}_1$</div></foreignObject>
  <foreignObject x="424" y="170.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\dot{H}_2$</div></foreignObject>
  <foreignObject x="180.5" y="8.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{sphere surface}$</div></foreignObject>
</svg>

```johda
A point source radiates evenly in all directions. The dose rate is $\dot{H}_1$ at the distance $r_1$. Derive the dose rate $\dot{H}_2$ at the distance $r_2$.
---
The source radiates the power $P$ evenly in all directions. At the distance $r$ the radiation is spread over a sphere of area $A = 4\pi r^2$. The intensity is the power per unit area:

$$I = \frac{P}{A} = \frac{P}{4\pi r^2}$$

The dose rate is proportional to the intensity, because the greater the intensity, the more radiation energy reaches the tissue per unit time. Form the ratio of the dose rates, so that $P$ and $4\pi$ cancel:

$$\frac{\dot{H}_2}{\dot{H}_1} = \frac{I_2}{I_1} = \frac{P/(4\pi r_2^2)}{P/(4\pi r_1^2)} = \frac{r_1^2}{r_2^2}$$

Solve for $\dot{H}_2$:

$$\dot{H}_2 = \dot{H}_1 \left(\frac{r_1}{r_2}\right)^2$$

When the distance doubles, the dose rate falls to a quarter.
```

## Common mistakes {Virheet}

- **Brighter light, more energetic photons.** The intensity tells the number of photons; the frequency sets the energy of one photon.
- **The photon carries the energy of a level.** The photon energy is the difference of levels $E_\text{u} - E_\text{l}$, not $|E_n|$.
- **Electronvolts into a formula with $h$ in joules.** Convert first: $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.
- **Two half-lives make everything decay.** After two half-lives a quarter is left, and each half-life halves what is left.
- **Mixing up mass number and mass.** The mass number is conserved, but the mass decreases when energy is released.
- **The background is not subtracted.** The background radiation is subtracted from the counts before ratios are calculated.
- **Doubling the distance halves the dose rate.** The dose rate of a point source falls to a quarter.

## Review if needed {Kertaa}

- The photon and the atom: [*The photoelectric effect and the photon*](fy8-1.html), [*Spectra reveal the energy levels of atoms*](fy8-2.html), [*Energy levels of the hydrogen atom and the Bohr model*](fy8-3.html), [*Light and electrons as waves and particles*](fy8-4.html) and [*The wave-mechanical model of the atom and orbitals*](fy8-5.html).
- Applications: [*Light from an LED and measuring the Planck constant*](fy8-6.html) and [*Lasers and quantum structures*](fy8-7.html).
- The nucleus: [*The atomic nucleus and radioactive decay*](fy8-8.html), [*The decay law and half-life*](fy8-9.html), [*Mass defect and nuclear binding energy*](fy8-10.html) and [*Fission, fusion and nuclear power*](fy8-11.html).
- Radiation: [*Ionising radiation and the body*](fy8-12.html), [*Radiation dose and radiation safety in Finland*](fy8-13.html) and [*Radiation in medicine and technology*](fy8-14.html).
- Particles and the universe: [*The Standard Model: elementary particles and interactions*](fy8-15.html) and [*The evolution of the universe*](fy8-16.html).
