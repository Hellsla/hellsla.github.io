# Oscillation, waves and sound

> **Why** can the lifeguard's whistle also be heard under water, and does the sound change on its way from air into water?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a swimming hall in cross-section. In the background a tiled wall and tall windows. On the left, at the edge of the pool, is the lifeguard&#x27;s tall chair, with a whistle hanging from its armrest. From the whistle, closely spaced arcs of wavefronts spread through the air towards the pool. On the right the pool seen from the side: water, a lane rope with floats on the surface and a dark lane marking on the bottom. Under the water the same wavefronts continue about four times farther apart." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-aallot-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

All the phenomena of the module start from **oscillation**: a body moves back and forth on both sides of its equilibrium position, and the motion is described by the period $T$, the frequency $f$ and the amplitude $A$. The period of a spring and of a pendulum is set by the oscillator itself. A **wave** is an oscillation that travels through a medium: the particles oscillate in place, and the wave carries energy but not matter. **Sound** is a longitudinal pressure wave. Its pitch is set by the frequency and its loudness by the intensity.

<svg data-fig="kartta" viewBox="0 0 380 896" role="img" aria-label="Recognition chart: how do I tell which law to use? Start by asking whether the task is about a motion or a wave, and see which sign fits. Mass on a spring: the period of the oscillator is two pi times the square root of the mass divided by the spring constant. Pendulum, small angle: the period is two pi times the square root of the length divided by the acceleration of free fall. Wave speed, frequency, wavelength: the wave equation, speed is frequency times wavelength. Two sources, reinforce: the path difference is a whole number times the wavelength. Two sources, cancel: the path difference is a whole number plus a half, times the wavelength. String or open pipe: a standing wave, the natural frequency is n times the speed divided by twice the length. Two almost equal frequencies: beats, the beat frequency is the absolute value of the difference of the frequencies. Source or observer moves: the frequency changes, this is the Doppler effect. Loudness in decibels: the sound intensity level is ten times the base-ten logarithm of the ratio of the intensity to the threshold intensity, in decibels." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="837" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{motion or wave? look at the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{mass on a spring}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{period}$</div></foreignObject>
  <rect x="212" y="140" width="150" height="28" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="133.5" width="142" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = 2\pi\sqrt{m/k}$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{pendulum, small angle}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{period}$</div></foreignObject>
  <rect x="212" y="226" width="150" height="28" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="219.5" width="142" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = 2\pi\sqrt{l/g}$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{wave speed, frequency, wavelength}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{wave equation}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = f\lambda$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two sources, reinforce}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{path difference}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta s = n\lambda$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two sources, cancel}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="146" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{path difference}$</div></foreignObject>
  <rect x="202" y="486" width="160" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="206" y="488" width="152" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta s = (n + 1/2)\lambda$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{string or open pipe}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{standing wave}$</div></foreignObject>
  <rect x="232" y="572" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="574" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$f_n = n\,v/(2L)$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{two almost equal frequencies}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{beats}$</div></foreignObject>
  <rect x="212" y="658" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="660" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$f_\text{H} = |f_1 - f_2|$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{source or observer moves}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{frequency changes}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{Doppler}$</div></foreignObject>
  <line x1="14" y1="837" x2="30" y2="837" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{loudness in decibels}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{intensity level}$</div></foreignObject>
  <rect x="172" y="860" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="862" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$L = 10\lg(I/I_0)\,\text{dB}$</div></foreignObject>
</svg>

In the wave problems of the exam it pays to ask first what determines which quantity. The source determines the frequency, the medium the speed, and the wavelength follows from them. When a wave meets an obstacle, a gap or another wave, it reflects, diffracts or interferes, and in every case what decides is comparing distances with the wavelength.

This gives the answer to the opening question. The whistle vibrates at the frequency $3.0\,\text{kHz}$, and the same frequency is kept when the sound passes into water, so the pitch is the same. The speed of sound is about $350\,\text{m/s}$ in the warm air of the hall and about $1500\,\text{m/s}$ in water, so the wavelength grows from $0.12\,\text{m}$ to $0.50\,\text{m}$. Most of the sound is, however, reflected from the water surface, so under water the whistle sounds faint.

<svg data-fig="pilli" viewBox="0 0 600 380" role="img" aria-label="Diagram to scale: the sound of the same whistle as a pressure wave in air and in water, with a distance of one metre drawn equally long in both. Above, in air, the wavelength is 0.12 metres, so almost nine waves fit into a metre. Below, in water, the wavelength is 0.50 metres, and two waves fit into a metre. In both, one wavelength is marked with a bracket, and an arrow shows the direction of travel. The curve shows how the pressure varies. The frequency is the same in both, 3.0 kilohertz, but the speed of sound is about 350 metres per second in air and about 1500 in water." style="max-width:100%;font-size:26px">
  <foreignObject x="59.5" y="4.5" width="481" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{pressure wave, same frequency } f = 3.0\,\text{kHz}$</div></foreignObject>
  <rect x="14" y="72" width="420" height="92" rx="8" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <line x1="24" y1="118" x2="424" y2="118" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <polyline points="24,118 25.5,111.5 27.5,105 29,99.5 30.5,94.5 32.5,91 34,89 35.5,88 37.5,89 39,91 40.5,94.5 42.5,99.5 44,105 45.5,111.5 47.5,118 49,124.5 50.5,131 52.5,136.5 54,141.5 55.5,145 57.5,147 59,148 60.5,147 62.5,145 64,141.5 65.5,136.5 67.5,131 69,124.5 70.5,118 72.5,111.5 74,105 75.5,99.5 77.5,94.5 79,91 80.5,89 82.5,88 84,89 85.5,91 87.5,94.5 89,99.5 90.5,105 92.5,111.5 94,118 95.5,124.5 97.5,131 99,136.5 100.5,141.5 102.5,145 104,147 105.5,148 107.5,147 109,145 110.5,141.5 112.5,136.5 114,131 115.5,124.5 117.5,118 119,111.5 120.5,105 122.5,99.5 124,94.5 125.5,91 127.5,89 129,88 130.5,89 132.5,91 134,94.5 135.5,99.5 137.5,105 139,111.5 140.5,118 142.5,124.5 144,131 145.5,136.5 147.5,141.5 149,145 150.5,147 152.5,148 154,147 155.5,145 157.5,141.5 159,136.5 160.5,131 162.5,124.5 164,118 165.5,111.5 167.5,105 169,99.5 170.5,94.5 172.5,91 174,89 175.5,88 177.5,89 179,91 180.5,94.5 182.5,99.5 184,105 185.5,111.5 187.5,118 189,124.5 190.5,131 192.5,136.5 194,141.5 195.5,145 197.5,147 199,148 200.5,147 202.5,145 204,141.5 205.5,136.5 207.5,131 209,124.5 210.5,118 212.5,111.5 214,105 215.5,99.5 217.5,94.5 219,91 220.5,89 222.5,88 224,89 225.5,91 227.5,94.5 229,99.5 230.5,105 232.5,111.5 234,118 235.5,124.5 237.5,131 239,136.5 240.5,141.5 242.5,145 244,147 245.5,148 247.5,147 249,145 250.5,141.5 252.5,136.5 254,131 255.5,124.5 257.5,118 259,111.5 260.5,105 262.5,99.5 264,94.5 265.5,91 267.5,89 269,88 270.5,89 272.5,91 274,94.5 275.5,99.5 277.5,105 279,111.5 280.5,118 282.5,124.5 284,131 285.5,136.5 287.5,141.5 289,145 290.5,147 292.5,148 294,147 295.5,145 297.5,141.5 299,136.5 300.5,131 302.5,124.5 304,118 305.5,111.5 307.5,105 309,99.5 310.5,94.5 312.5,91 314,89 315.5,88 317.5,89 319,91 320.5,94.5 322.5,99.5 324,105 325.5,111.5 327.5,118 329,124.5 330.5,131 332.5,136.5 334,141.5 335.5,145 337.5,147 339,148 340.5,147 342.5,145 344,141.5 345.5,136.5 347.5,131 349,124.5 350.5,118 352.5,111.5 354,105 355.5,99.5 357.5,94.5 359,91 360.5,89 362.5,88 364,89 365.5,91 367.5,94.5 369,99.5 370.5,105 372.5,111.5 374,118 375.5,124.5 377.5,131 379,136.5 380.5,141.5 382.5,145 384,147 385.5,148 387.5,147 389,145 390.5,141.5 392.5,136.5 394,131 395.5,124.5 397.5,118 399,111.5 400.5,105 402.5,99.5 404,94.5 405.5,91 407.5,89 409,88 410.5,89 412.5,91 414,94.5 415.5,99.5 417.5,105 419,111.5 420.5,118 422.5,124.5 424,131" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="446" y="84.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{air}$</div></foreignObject>
  <foreignObject x="446" y="119.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda \approx 0.12\,\text{m}$</div></foreignObject>
  <path d="M35.5,84 V78 H82.5 V84" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="49" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="24" y="167.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v \approx 350\,\text{m/s}$</div></foreignObject>
  <rect x="14" y="232" width="420" height="92" rx="8" fill="#dcecf8" stroke="#c9c2b2" stroke-width="1.5"/>
  <line x1="24" y1="278" x2="424" y2="278" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <polyline points="24,278 25.5,276.5 27.5,275 29,273.5 30.5,272 32.5,270 34,268.5 35.5,267 37.5,266 39,264.5 40.5,263 42.5,261.5 44,260.5 45.5,259 47.5,258 49,257 50.5,255.5 52.5,254.5 54,253.5 55.5,253 57.5,252 59,251.5 60.5,250.5 62.5,250 64,249.5 65.5,249 67.5,248.5 69,248.5 70.5,248 72.5,248 74,248 75.5,248 77.5,248 79,248.5 80.5,248.5 82.5,249 84,249.5 85.5,250 87.5,250.5 89,251.5 90.5,252 92.5,253 94,253.5 95.5,254.5 97.5,255.5 99,257 100.5,258 102.5,259 104,260.5 105.5,261.5 107.5,263 109,264.5 110.5,266 112.5,267 114,268.5 115.5,270 117.5,272 119,273.5 120.5,275 122.5,276.5 124,278 125.5,279.5 127.5,281 129,282.5 130.5,284 132.5,286 134,287.5 135.5,289 137.5,290 139,291.5 140.5,293 142.5,294.5 144,295.5 145.5,297 147.5,298 149,299 150.5,300.5 152.5,301.5 154,302.5 155.5,303 157.5,304 159,304.5 160.5,305.5 162.5,306 164,306.5 165.5,307 167.5,307.5 169,307.5 170.5,308 172.5,308 174,308 175.5,308 177.5,308 179,307.5 180.5,307.5 182.5,307 184,306.5 185.5,306 187.5,305.5 189,304.5 190.5,304 192.5,303 194,302.5 195.5,301.5 197.5,300.5 199,299 200.5,298 202.5,297 204,295.5 205.5,294.5 207.5,293 209,291.5 210.5,290 212.5,289 214,287.5 215.5,286 217.5,284 219,282.5 220.5,281 222.5,279.5 224,278 225.5,276.5 227.5,275 229,273.5 230.5,272 232.5,270 234,268.5 235.5,267 237.5,266 239,264.5 240.5,263 242.5,261.5 244,260.5 245.5,259 247.5,258 249,257 250.5,255.5 252.5,254.5 254,253.5 255.5,253 257.5,252 259,251.5 260.5,250.5 262.5,250 264,249.5 265.5,249 267.5,248.5 269,248.5 270.5,248 272.5,248 274,248 275.5,248 277.5,248 279,248.5 280.5,248.5 282.5,249 284,249.5 285.5,250 287.5,250.5 289,251.5 290.5,252 292.5,253 294,253.5 295.5,254.5 297.5,255.5 299,257 300.5,258 302.5,259 304,260.5 305.5,261.5 307.5,263 309,264.5 310.5,266 312.5,267 314,268.5 315.5,270 317.5,272 319,273.5 320.5,275 322.5,276.5 324,278 325.5,279.5 327.5,281 329,282.5 330.5,284 332.5,286 334,287.5 335.5,289 337.5,290 339,291.5 340.5,293 342.5,294.5 344,295.5 345.5,297 347.5,298 349,299 350.5,300.5 352.5,301.5 354,302.5 355.5,303 357.5,304 359,304.5 360.5,305.5 362.5,306 364,306.5 365.5,307 367.5,307.5 369,307.5 370.5,308 372.5,308 374,308 375.5,308 377.5,308 379,307.5 380.5,307.5 382.5,307 384,306.5 385.5,306 387.5,305.5 389,304.5 390.5,304 392.5,303 394,302.5 395.5,301.5 397.5,300.5 399,299 400.5,298 402.5,297 404,295.5 405.5,294.5 407.5,293 409,291.5 410.5,290 412.5,289 414,287.5 415.5,286 417.5,284 419,282.5 420.5,281 422.5,279.5 424,278" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="446" y="244.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{water}$</div></foreignObject>
  <foreignObject x="446" y="279.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda \approx 0.50\,\text{m}$</div></foreignObject>
  <path d="M74,244 V238 H274 V244" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="164" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="24" y="327.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v \approx 1500\,\text{m/s}$</div></foreignObject>
  <line x1="446" y1="362" x2="528" y2="362" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M540,362 L527,368 L527,356 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="446" y="321.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{travels}$</div></foreignObject>
  <line x1="24" y1="360" x2="424" y2="360" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="24" y1="352" x2="24" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="424" y1="352" x2="424" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="201.5" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{m}$</div></foreignObject>
</svg>

## Formula: Oscillation, waves and sound

### Oscillators

```kaavat
frequency :: f = \frac{1}{T}
harmonic force :: \overline{F} = -k\overline{x}
period of a harmonic oscillator :: T = 2\pi\sqrt{\frac{m}{k}}
period of a simple pendulum :: T = 2\pi\sqrt{\frac{l}{g}}
```

where $f$ is the frequency ($\text{Hz}$), $T$ the period ($\text{s}$), $\overline{F}$ the spring force ($\text{N}$), $k$ the spring constant ($\text{N/m}$), $\overline{x}$ the displacement from the equilibrium position ($\text{m}$); the minus sign says that the force points towards the equilibrium position, $m$ the mass ($\text{kg}$) and $l$ the length of the pendulum ($\text{m}$). The spring force holds when the spring is not stretched too far. The period of the pendulum holds for small swings, and it does not depend on the mass. The elastic potential energy of a spring is $E_\text{p} = \tfrac12 kx^2$, and without friction the energy of the oscillation $\tfrac12 kA^2$ is conserved.

### Waves

```kaavat
wave equation :: v = f\lambda
\Delta s = n\lambda
\Delta s = \left(n + \tfrac12\right)\lambda
```

where $v$ is the speed of the wave ($\text{m/s}$), $\lambda$ the wavelength ($\text{m}$) and $\Delta s$ the path difference from two sources oscillating in phase ($\text{m}$), $n = 0, 1, 2, \ldots$ The first condition gives constructive and the second destructive interference. Diffraction is strong when the width of the gap or obstacle is about the wavelength or smaller. In reflection the angle of incidence equals the angle of reflection, when the angles are measured from the normal to the surface.

In a standing wave the distance between neighbouring nodes is $\tfrac{\lambda}{2}$. A string and an open tube have the natural frequencies $f_n = n \cdot \tfrac{v}{2L}$, $n = 1, 2, 3, \ldots$, and a tube closed at one end $f_n = n \cdot \tfrac{v}{4L}$, $n = 1, 3, 5, \ldots$, where $L$ is the length of the string or the tube.

<svg data-fig="ominais" viewBox="0 0 600 466" role="img" aria-label="Diagram, not to scale: three standing waves at the fundamental frequency one below the other, each of length L. At the top a string fixed at both ends: there is a node at each end and an antinode in the middle, and the length of the string is half the wavelength. In the middle a tube open at both ends: the displacement antinodes of the air are at the ends of the tube and the node in the middle, and the length of the tube is half the wavelength. At the bottom a tube closed at one end: there is a node at the closed end and an antinode at the open end, and the length of the tube is a quarter of the wavelength." style="max-width:100%;font-size:26px">
  <image href="pics/fy9/fy9-aallot-ominais.webp" x="0" y="0" width="600" height="470" preserveAspectRatio="none"/>
  <foreignObject x="390" y="36.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{string}$</div></foreignObject>
  <foreignObject x="390" y="74.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/2$</div></foreignObject>
  <foreignObject x="190" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{N}$</div></foreignObject>
  <foreignObject x="30" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="350" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="390" y="174.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{open tube}$</div></foreignObject>
  <foreignObject x="390" y="212.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/2$</div></foreignObject>
  <foreignObject x="54" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{N}$</div></foreignObject>
  <foreignObject x="350" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{A}$</div></foreignObject>
  <foreignObject x="390" y="308.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{closed tube}$</div></foreignObject>
  <foreignObject x="390" y="346.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/4$</div></foreignObject>
  <foreignObject x="189" y="412.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$L$</div></foreignObject>
  <foreignObject x="390" y="431.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{N node, A antinode}$</div></foreignObject>
</svg>

### Sound

```kaavat
beat frequency :: f_\text{H} = |f_1 - f_2|
Doppler effect, source moving towards the observer :: f = f_0\,\frac{v}{v - v_\text{L}}
Doppler effect, source moving away from the observer :: f = f_0\,\frac{v}{v + v_\text{L}}
Doppler effect, observer moving towards the source :: f = f_0\,\frac{v + v_\text{H}}{v}
Doppler effect, observer moving away from the source :: f = f_0\,\frac{v - v_\text{H}}{v}
intensity :: I = \frac{P}{A}
sound intensity level :: L = 10\lg\left(\frac{I}{I_0}\right)\,\text{dB}
```

where $f_\text{H}$ is the beat frequency ($\text{Hz}$), $f_0$ the frequency of the source and $f$ the heard frequency ($\text{Hz}$), $v$ the speed of sound, $v_\text{L}$ the speed of the source and $v_\text{H}$ the speed of the observer relative to the air ($\text{m/s}$). The Doppler formulas hold when only one of them moves and the speed is smaller than the speed of sound. The intensity is the power $P$ per unit area $A$. The sound of a point source spreads at the distance $r$ over a sphere of area $A = 4\pi r^2$, when there are no reflections. $L$ is the intensity level and $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$. The distance from an echo is $d = \tfrac{vt}{2}$, because the pulse travels the distance twice.

## Common mistakes {Virheet}

- **Amplitude from one extreme position to the other.** The amplitude is measured from the equilibrium position, so it is half the distance between the extreme positions.
- **Half a period.** Two successive passes through the equilibrium position are only $\tfrac{T}{2}$ apart; a period is the interval between two peaks.
- **The frequency changes in the medium.** The frequency stays the same when a wave passes from one medium into another; the speed and the wavelength change.
- **A snapshot and the graph of one point mixed up.** Read the horizontal axis first: from an $(x, y)$ graph you read $\lambda$, from a $(t, y)$ graph $T$.
- **Decibels are added.** Two equally loud independent sources raise the level by about $3\,\text{dB}$, because the intensities are added.
- **An echo without dividing by two.** An echo travels the distance there and back, so $d = \tfrac{vt}{2}$.
- **The sign in the Doppler formula.** Check at the end that approaching gives $f > f_0$ and moving away $f < f_0$.

## Review if needed {Kertaa}

- The quantities of oscillation: [*Describing oscillation: period, frequency and amplitude*](fy5-7.html). The spring and its energy: [*Spring force and spring energy*](fy5-8.html). Periods: [*The mass–spring oscillator and the pendulum*](fy5-9.html).
- Waves: [*How waves form and travel*](fy5-10.html), [*A wave meets an obstacle or a gap*](fy5-11.html), [*When waves combine: superposition and interference*](fy5-12.html) and [*Standing waves: nodes, antinodes and natural frequencies*](fy5-13.html).
- Sound: [*Sound as a wave: pitch, timbre and the Doppler effect*](fy5-14.html), [*Intensity and the decibel scale*](fy5-15.html) and [*Noise, acoustics and sound reproduction*](fy5-16.html).
- Echoes and earthquakes: [*Applied chapter: ultrasound imaging and earthquake waves*](fy5-17.html).
