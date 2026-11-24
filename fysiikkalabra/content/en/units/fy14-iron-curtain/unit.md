# Science across the Iron Curtain

> **Why** should a scientist believe a result from a rival country?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a large, dim laboratory hall in winter. Through three tall arched windows snow falls on a dark blue evening. In the middle of the hall stands an early tokamak: a ring-shaped metal chamber wrapped in copper coils, held by a massive dark iron core that passes through the ring. Cables run from it across the floor. In the front right corner stands a small wooden table with two teacups and a teapot." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-iron-curtain-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Before you read the sources {Intro}

In 1968 the world was divided by the **Iron Curtain**, the border between the Soviet Union and its allies in the East and the countries of Western Europe and North America. Travel across it was difficult, and scientists in nuclear research were watched by security services on both sides. In August 1968, Warsaw Pact armies invaded Czechoslovakia to end the reforms of the *Prague Spring*.

Fusion research had been open since the Geneva conference of 1958, but it was stuck. Most machines lost their plasma much faster than theory predicted, at a rate known as **Bohm diffusion**. If that rate was a law of nature, a fusion reactor would be impossible. The five sources below follow what happened next. They are short texts written for this course from historical documents; words in quotation marks are the original words.

```pysahdy
If the Bohm rate were a law of nature, what would it mean for a fusion reactor?
---
The plasma would be lost far too fast to be held long enough, so a reactor would be impossible.
```

## Source A: Novosibirsk, August 1968 {Source A}

*Type: a summary of results presented at a scientific conference. Based on the International Atomic Energy Agency's conference of 1–7 August 1968 and on later accounts.*

> At the third IAEA conference on plasma physics and controlled fusion research, held in Novosibirsk in Siberia, **Lev Artsimovich**, the head of the Soviet fusion programme, presented results from the **T-3 tokamak** at the Kurchatov Institute in Moscow. T-3 had reached an electron temperature of about $1\ \text{keV}$, roughly ten million degrees, and it held its energy for more than $10\ \text{ms}$. This was many times better than the Bohm rate and about ten times better than any other machine in the world. The temperature was not measured directly: it was calculated from the magnetic properties of the plasma.

<figure class="unit-photo"><img src="units/fy14/pics/artsimovich.jpg" alt="Black-and-white photograph of Lev Artsimovich pointing at a large experimental machine full of pipes and cables while visitors in suits look on." width="1600" height="1199" loading="lazy"><figcaption>Lev Artsimovich (1909–1973) led Soviet tokamak research. Photographed at the Kurchatov Institute in 1967. <span class="photo-credit">Photo: В. Савостьянов, Е. Кассин, CC BY 4.0, via Wikimedia Commons</span></figcaption></figure>

## Source B: Why the West doubted {Source B}

*Type: a summary of the scientific objections, based on histories of the tokamak.*

> Many Western physicists did not accept the T-3 temperature. Already in 1965, when Artsimovich had shown earlier, smaller improvements, **Lyman Spitzer** of Princeton had questioned the Soviet measurements. The critics' main argument was physical: the magnetic method measures the *total* energy of the electrons. A small group of extremely fast **runaway electrons**, accelerated by the electric field that drives the current, could carry a lot of energy while the bulk of the plasma stayed much colder. Then the true temperature would be far lower than claimed. The Soviet scientists answered that their plasma was in thermal equilibrium, but with their method they could not prove it.

## Source C: An invitation across the Iron Curtain {Source C}

*Type: a summary of memories of the people involved, published by the ITER Organization and in a biography of Derek Robinson.*

> Artsimovich made an unusual offer to **Bas Pease**, the director of the British fusion laboratory at **Culham**: a British team could come to Moscow and measure T-3 themselves. Culham had used a new laser method for measuring plasma temperatures for about five years, and the British wanted to test it on the best machine in the world. In December 1968, less than six months after Novosibirsk, the team was chosen: **Nicol Peacock**, **Mike Forrest**, **Peter Wilcock** and **Derek Robinson**, with a technician, later known together as the *Culham Five*. British rules said that a person with valuable knowledge could travel to the Soviet Union only if "properly accompanied by a reliable person". In Moscow the team felt watched: once, a broken light bulb that the Robinsons had mentioned at breakfast was replaced before they came back. Forrest later wrote that they felt safe "enjoying the powerful patronage of Lev Artsimovitch" (the original spells his name with *-tch*; it is the same Artsimovich).

## Source D: Five tonnes of equipment and a laser {Source D}

*Type: a summary of the team's own accounts and of their scientific paper (Peacock, Robinson, Forrest, Wilcock and Sannikov, Nature, November 1969).*

> In the spring of 1969 the team arrived at the Kurchatov Institute with about five tonnes of equipment. They opened the machine to fit windows, built optical benches that did not shake, and placed a powerful **ruby laser** in the basement under the tokamak. Vibrations from the huge generators that powered T-3 made the floor move "like the skin of a drum". At first the scattered light was lost in the noise, and the team had to make the laser much more powerful. On **22 July 1969** the signal finally appeared, and a short note in Robinson's notebook recorded an electron temperature of about $1\ \text{keV}$. By early August they had measured about 88 plasma shots. Most showed electron temperatures of about ten million degrees, as Artsimovich had said. The results were phoned to Culham. The paper in *Nature* reported electron temperatures from $100\ \text{eV}$ to $1\ \text{keV}$ and agreed with the other methods where they could be compared. One of its five authors, **V. V. Sannikov**, was a Soviet scientist.

## Source E: The tokamak stampede {Source E}

*Type: a summary of what laboratories did after 1969, based on histories of the tokamak and the stellarator and on the ITER Organization's account.*

> The British measurement changed fusion research. At Princeton, the stellarator *Model C* was shut down in December 1969 and rebuilt as a tokamak, the **Symmetric Tokamak**, which started in May 1970 and within months matched the T-3 results. Laboratories in the United States, France, Japan and Germany also built tokamaks, and the tokamak became the main road to fusion. The Soviet physicist Evgeny Velikhov later said that the British measurement "led to the beginning of active research on tokamaks all over the world". Today's largest fusion experiment, ITER, is a tokamak.

## How Thomson scattering works {Thomson}

When laser light passes through a plasma, a tiny fraction of it is scattered sideways by the free electrons. This is **Thomson scattering**. An electron that moves towards the detector scatters the light with a slightly shorter wavelength, and one that moves away with a slightly longer wavelength, because of the **Doppler effect**. In a plasma the electrons move in all directions at random, so the scattered light is spread over a range of wavelengths around the laser's own wavelength, $694\ \text{nm}$ for a ruby laser.

```pysahdy
An electron moves towards the detector. Does it scatter the laser light with a shorter or a longer wavelength?
---
Shorter. Because of the Doppler effect, motion towards the detector shortens the wavelength, and motion away lengthens it.
```

The hotter the electrons, the faster they move, and the **wider** the spread. So the width of the scattered spectrum gives the electron temperature *directly*, from the motion of the bulk of the electrons. A few runaway electrons cannot fake it, because they would add only a weak, far-away tail to the spectrum. And the method does not depend on the Soviet magnetic measurements at all. Its difficulty is that very little light is scattered, which is why the team needed such a powerful laser and why the vibrations and the noise were such a problem.

<svg data-fig="thomson" viewBox="0 0 600 720" role="img" aria-label="Diagram of Thomson scattering. Top: a red laser beam enters from the left and crosses a grey cross-section of the plasma. In the plasma, small blue dots are electrons moving in random directions. A little light is scattered upwards, at a right angle, into a box labelled spectrometer. Bottom: a graph of the intensity of the scattered light against wavelength, with both curves centred on the laser wavelength 694 nanometres. The cooler plasma gives a tall, narrow curve; the hotter plasma gives a low, wide curve, twice as wide." style="max-width:100%;font-size:28px">
  <rect x="0" y="0" width="600" height="720" fill="#ffffff"/>
  <ellipse cx="300" cy="230" rx="150" ry="110" fill="#e3dccb" stroke="#8a96a3" stroke-width="3"/>
  <line x1="10" y1="230" x2="590" y2="230" stroke="#c92a2a" stroke-width="10" stroke-linecap="butt"/>
  <foreignObject x="14" y="179" width="81" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#c92a2a">$\text{laser}$</div></foreignObject>
  <circle cx="202.5" cy="163" r="5" fill="#1971c2"/>
  <line x1="202.5" y1="163" x2="212" y2="146.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M216,140.5 L215,149.5 L208.5,145.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="224.5" cy="284" r="5" fill="#1971c2"/>
  <line x1="224.5" y1="284" x2="227.5" y2="303" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M228.5,309.5 L223.5,302.5 L231,301 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="214.5" cy="224" r="5" fill="#1971c2"/>
  <line x1="214.5" y1="224" x2="216" y2="242.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M216.5,249.5 L212.5,242 L219.5,241.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="368.5" cy="169" r="5" fill="#1971c2"/>
  <line x1="368.5" y1="169" x2="354" y2="156" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M349,151.5 L357,154 L352.5,159.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="234" cy="188.5" r="5" fill="#1971c2"/>
  <line x1="234" y1="188.5" x2="235" y2="207.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M235.5,214.5 L231.5,207 L238.5,206.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="231.5" cy="287.5" r="5" fill="#1971c2"/>
  <line x1="231.5" y1="287.5" x2="249" y2="281.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M256,279 L249.5,285 L247,278.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="339.5" cy="268" r="5" fill="#1971c2"/>
  <line x1="339.5" y1="268" x2="357" y2="275" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M363.5,278 L355,278 L357.5,271.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="395" cy="165.5" r="5" fill="#1971c2"/>
  <line x1="395" y1="165.5" x2="376" y2="167" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M369,167.5 L376.5,163 L377.5,170.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="338" cy="221" r="5" fill="#1971c2"/>
  <line x1="338" y1="221" x2="350.5" y2="207" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M355,201.5 L352.5,210 L347,205.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="404.5" cy="283" r="5" fill="#1971c2"/>
  <line x1="404.5" y1="283" x2="415.5" y2="298.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M419.5,304.5 L412,300 L417.5,296 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="382" cy="279.5" r="5" fill="#1971c2"/>
  <line x1="382" y1="279.5" x2="366.5" y2="290.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360.5,294.5 L365,287 L369.5,293 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="306" cy="208.5" r="5" fill="#1971c2"/>
  <line x1="306" y1="208.5" x2="287.5" y2="211.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M280.5,212.5 L288,207.5 L289,214.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="392.5" cy="267" r="5" fill="#1971c2"/>
  <line x1="392.5" y1="267" x2="392" y2="248" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M392,241 L396,248.5 L388.5,249 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="305.5" cy="217.5" r="5" fill="#1971c2"/>
  <line x1="305.5" y1="217.5" x2="310" y2="236" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M312,242.5 L306.5,236 L313.5,234 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="260.5" cy="214.5" r="5" fill="#1971c2"/>
  <line x1="260.5" y1="214.5" x2="274" y2="227.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M279.5,232 L271,229.5 L276,224 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="340.5" cy="223.5" r="5" fill="#1971c2"/>
  <line x1="340.5" y1="223.5" x2="322" y2="227.5" stroke="#1971c2" stroke-width="2" stroke-linecap="butt"/>
  <path d="M315.5,229.5 L322.5,224 L324,231 Z" fill="#1971c2" stroke-linejoin="round"/>
  <path d="M300,222 L300,96" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round" stroke-dasharray="10 7"/>
  <path d="M300,92 l-9,16 h18 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <rect x="200" y="26" width="200" height="56" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="202" y="38.5" width="196" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#ffffff">$\text{spectrometer}$</div></foreignObject>
  <foreignObject x="390" y="313" width="140" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{plasma}$</div></foreignObject>
  <line x1="70" y1="680" x2="570" y2="680" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="70" y1="680" x2="70" y2="420" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M570,680 l-14,-7 v14 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M70,420 l-7,14 h14 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="320" y1="680" x2="320" y2="688" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="250" y="690.5" width="140" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$694\ \text{nm}$</div></foreignObject>
  <foreignObject x="546" y="640" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$\lambda$</div></foreignObject>
  <foreignObject x="82" y="408.5" width="130" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{intensity}$</div></foreignObject>
  <path d="M90,680 L95,680 L100,680 L105,680 L110,680 L115,680 L120,680 L125,680 L130,680 L135,680 L140,680 L145,680 L150,680 L155,680 L160,680 L165,680 L170,680 L175,680 L180,680 L185,680 L190,680 L195,680 L200,679.5 L205,679.5 L210,679 L215,678 L220,677 L225,676 L230,673.5 L235,671 L240,667 L245,661.5 L250,655 L255,646 L260,635.5 L265,623 L270,609 L275,592.5 L280,575 L285,556.5 L290,537.5 L295,519.5 L300,503.5 L305,489.5 L310,479 L315,472.5 L320,470 L325,472.5 L330,479 L335,489.5 L340,503.5 L345,519.5 L350,537.5 L355,556.5 L360,575 L365,592.5 L370,609 L375,623 L380,635.5 L385,646 L390,655 L395,661.5 L400,667 L405,671 L410,673.5 L415,676 L420,677 L425,678 L430,679 L435,679.5 L440,679.5 L445,680 L450,680 L455,680 L460,680 L465,680 L470,680 L475,680 L480,680 L485,680 L490,680 L495,680 L500,680 L505,680 L510,680 L515,680 L520,680 L525,680 L530,680 L535,680 L540,680 L545,680 L550,680" fill="none" stroke="#1971c2" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="372" y="449" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#1971c2">$\text{cooler}$</div></foreignObject>
  <path d="M90,679.5 L95,679.5 L100,679.5 L105,679.5 L110,679 L115,679 L120,678.5 L125,678.5 L130,678 L135,677.5 L140,677 L145,676 L150,675.5 L155,674.5 L160,673.5 L165,672 L170,671 L175,669 L180,667.5 L185,665.5 L190,663 L195,660.5 L200,658 L205,655 L210,651.5 L215,648 L220,644.5 L225,640.5 L230,636.5 L235,632 L240,627.5 L245,623 L250,618 L255,613.5 L260,609 L265,604.5 L270,600 L275,595.5 L280,591.5 L285,588 L290,584.5 L295,582 L300,579.5 L305,577.5 L310,576 L315,575.5 L320,575 L325,575.5 L330,576 L335,577.5 L340,579.5 L345,582 L350,584.5 L355,588 L360,591.5 L365,595.5 L370,600 L375,604.5 L380,609 L385,613.5 L390,618 L395,623 L400,627.5 L405,632 L410,636.5 L415,640.5 L420,644.5 L425,648 L430,651.5 L435,655 L440,658 L445,660.5 L450,663 L455,665.5 L460,667.5 L465,669 L470,671 L475,672 L480,673.5 L485,674.5 L490,675.5 L495,676 L500,677 L505,677.5 L510,678 L515,678.5 L520,678.5 L525,679 L530,679 L535,679.5 L540,679.5 L545,679.5 L550,679.5" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-dasharray="12 8"/>
  <foreignObject x="448" y="551" width="95" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#e8590c">$\text{hotter}$</div></foreignObject>
</svg>

## Key idea

Scientists judge a result by its **evidence**: measurements that others can check, made by a method whose limits are understood. The **circumstances** of a result, such as who made it, in which country and during which political crisis, can explain why people trusted or doubted it, but they are not evidence about nature.

In 1968 the circumstances made Western scientists suspicious: T-3 was a Soviet machine in the middle of the Cold War, and earlier claims such as ZETA's had been wrong. But their doubt also had a *scientific* reason: the temperature came from an indirect method that runaway electrons could fool. The way to settle the question was **independent verification**: a different team, with its own equipment and a different method, measuring the same plasma. Thomson scattering measured the bulk electron temperature directly, and it agreed with the Soviet result.

Independent verification matters because every method has hidden weaknesses and every team has hopes. A result that two independent methods agree on is much stronger than a result that one team repeats many times. The T-3 story also shows that cooperation can serve both sides: Artsimovich gained trust for his result, and the British tested their method on the best plasma in the world.

## Common misconception

"The British confirmed the result because East–West relations had improved." The political situation was not good in 1968–1969, and the team worked under security rules and surveillance. The result was accepted because the measurement was independent and direct, not because of politics.

A second mistake is to think that *repeating* a measurement is the same as *verifying* it. Repeating the same indirect measurement many times does not remove its systematic weakness. A different method does.

## Summary

- In August 1968 at Novosibirsk, Artsimovich reported that the T-3 tokamak had reached about $1\ \text{keV}$ (about ten million degrees) and confinement far better than the Bohm rate.
- Western scientists doubted it for political and scientific reasons: the temperature was calculated indirectly, and runaway electrons could have fooled the method.
- Artsimovich invited a British team from Culham. In 1969 they measured T-3 with laser Thomson scattering, and from 22 July their data confirmed temperatures of about $1\ \text{keV}$. The paper appeared in *Nature* in November 1969 with a Soviet co-author.
- Thomson scattering measures the electron temperature directly from the Doppler width of the scattered laser light: the hotter the electrons, the wider the spectrum.
- After 1969 laboratories around the world built tokamaks; Princeton turned its Model C stellarator into the Symmetric Tokamak in 1970.
- Evidence is a checkable measurement; circumstances explain why people trust or doubt a result. Independent verification with a different method is the strongest test.
