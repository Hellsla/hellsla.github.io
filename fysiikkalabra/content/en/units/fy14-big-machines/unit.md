# Big machines and world politics: 1970s to 1985

> **Why** did fusion machines grow so large in the 1970s and 1980s?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a vast, brightly lit experimental hall with a travelling crane under the roof. In the middle stands a huge ring-shaped machine as tall as a three-storey house: a grey vacuum vessel inside large D-shaped blue coils, surrounded by pipes. To its right, a big box on legs points a tube into the ring. Five small people in different coloured shirts stand on the floor in front of it and look tiny next to the machine." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-big-machines-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## After the stampede {Stampede}

After the Culham measurement of 1969, laboratories in many countries built tokamaks. They soon found that the tokamak worked, but not well enough. A useful fusion plasma of deuterium and tritium must reach about $100$ million kelvin, be dense enough, and keep its energy long enough. The early tokamaks reached about ten million kelvin. The 1970s became a decade of three problems: how to **heat** the plasma further, how to build **stronger magnets**, and how to pay for **much larger machines**, because a bigger plasma loses its heat more slowly.

## Heating beyond the current {Heating}

A tokamak plasma carries a large electric current. Like the current in a kettle, it heats the plasma because the plasma has electrical resistance. This is **ohmic heating**. But a hot plasma is a better conductor than a cold one: as the temperature rises, the resistance falls, and the current heats less and less. Above about $20$–$30$ million kelvin, ohmic heating is no longer enough, and other methods are needed.

```pysahdy
Why does ohmic heating fade as the plasma gets hotter?
---
The resistance of a plasma falls as its temperature rises. With less resistance the same current produces less heat, so the current alone cannot heat the plasma much beyond $20\text{–}30$ million kelvin.
```

The main new method of the 1970s was **neutral beam injection**. Ions of hydrogen or deuterium are accelerated to tens of kiloelectronvolts and then turned into **neutral** atoms, so that the magnetic field does not deflect them on their way in. Inside the plasma the fast atoms are ionised, trapped by the field and share their energy with the plasma in collisions. A second method uses **radio waves**: an antenna sends waves at a frequency that matches the circling motion of the ions or electrons, and the particles absorb their energy.

In Princeton, the **Princeton Large Torus (PLT)** started in December 1975. With four neutral beam injectors, it reached ion temperatures of about $60$ million kelvin on the night of 24 July 1978. The result was shown at a conference in Innsbruck in August 1978: a tokamak could reach the temperatures a reactor needs. Temperature alone is not enough, though: density and confinement time had to improve too.

<svg data-fig="heating" viewBox="0 0 600 492" role="img" aria-label="Diagram of three ways to heat a tokamak plasma, drawn on a cross-section of the plasma ring seen from above. In the middle, an orange ring of plasma. A dark arrow along the ring shows the plasma current: ohmic heating. From the right, outside the ring, a box labelled neutral beam sends a short arrow and a row of dark dots, fast neutral atoms, into the plasma band, where the dots fade out: the atoms are caught in the plasma. From the lower left, an antenna sends curved wave lines into the plasma: radio waves." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-big-machines-heating.webp" x="0" y="0" width="600" height="496.2" preserveAspectRatio="none"/>
  <foreignObject x="80" y="23.5" width="360" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{current: ohmic heating}$</div></foreignObject>
  <foreignObject x="495" y="143.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{neutral}$</div></foreignObject>
  <foreignObject x="495" y="173.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{beam}$</div></foreignObject>
  <foreignObject x="124" y="442.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{antenna: radio waves}$</div></foreignObject>
</svg>

## Stronger magnets {Magnets}

The magnetic field of a tokamak comes from coils of copper. Copper has resistance, so a strong field needs huge electric power and heats the coils, and the machines could run only in short pulses. A **superconductor** has no electrical resistance at all when it is cooled to a few kelvin, usually with liquid helium. A current then flows without losses, and a strong field can be kept for a long time. The Soviet tokamak **T-7** at the Kurchatov Institute was the first to use superconducting magnets, in 1979. Its larger successor **T-15** produced its first plasma in 1988. Today ITER and many other machines use superconducting magnets.

<figure class="unit-photo"><img src="units/fy14/pics/t15-stamp.jpg" alt="Soviet postage stamp from 1987 showing a drawing of a large tokamak machine." width="565" height="800" loading="lazy"><figcaption>A 1987 Soviet stamp celebrating the T-15 tokamak at the Kurchatov Institute. Tokamaks were a source of national pride in the USSR. <span class="photo-credit">Photo: Scanned and processed by Mariluna, public domain, via Wikimedia Commons</span></figcaption></figure>

```pysahdy
What advantage does a superconducting coil have over a copper coil?
---
A superconductor has no electrical resistance, so the current flows without heating losses. A strong field can then be kept for a long time without huge electric power.
```

## Oil, money and big machines {Oil}

In October 1973 Arab oil-producing countries stopped selling oil to the United States and several other countries that had supported Israel in the Yom Kippur War. The **oil crisis** lasted until March 1974, and oil prices rose sharply. Suddenly, energy security was a political priority. Governments in the West spent much more on new energy sources, including fusion.

<svg data-fig="budget" viewBox="0 0 600 420" role="img" aria-label="Bar chart of the yearly US government budget for fusion research, in millions of dollars of the time: 40 in 1973, 332 in 1978 and 469 in 1984. The 1978 bar is about eight times as tall as the 1973 bar." style="max-width:100%;font-size:28px">
  <rect x="0" y="0" width="600" height="420" fill="#ffffff"/>
  <line x1="110" y1="350" x2="580" y2="350" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="334.5" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <line x1="110" y1="301" x2="580" y2="301" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="285.5" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$100$</div></foreignObject>
  <line x1="110" y1="251.5" x2="580" y2="251.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="236" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200$</div></foreignObject>
  <line x1="110" y1="202.5" x2="580" y2="202.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="187" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$300$</div></foreignObject>
  <line x1="110" y1="153" x2="580" y2="153" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="137.5" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$400$</div></foreignObject>
  <line x1="110" y1="104" x2="580" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="28" y="88.5" width="70" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$500$</div></foreignObject>
  <path d="M150,350 V334.5 Q150,330.5 154,330.5 H236 Q240,330.5 240,334.5 V350 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="150" y="291.5" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$40$</div></foreignObject>
  <foreignObject x="150" y="361" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$1973$</div></foreignObject>
  <path d="M300,350 V190.5 Q300,186.5 304,186.5 H386 Q390,186.5 390,190.5 V350 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="300" y="147.5" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$332$</div></foreignObject>
  <foreignObject x="300" y="361" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$1978$</div></foreignObject>
  <path d="M450,350 V123.5 Q450,119.5 454,119.5 H536 Q540,119.5 540,123.5 V350 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="450" y="80.5" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$469$</div></foreignObject>
  <foreignObject x="450" y="361" width="90" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$1984$</div></foreignObject>
  <foreignObject x="10" y="7" width="580" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$\text{US fusion budget, million dollars a year}$</div></foreignObject>
  <foreignObject x="10" y="42.5" width="580" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{(dollars of the time)}$</div></foreignObject>
</svg>

The money made bigger machines possible:

- **TFTR**, the *Tokamak Fusion Test Reactor* in Princeton, was approved in the mid-1970s, built from 1980 and started in 1982. It was designed to burn real deuterium–tritium fuel, which it did from December 1993; in 1994 it produced $10.7\ \text{MW}$ of fusion power.
- **JET**, the *Joint European Torus*, was a European project. After a long debate about the site, the Research Ministers chose Culham in England on 25 October 1977. The Council of Ministers agreed to set up the JET Joint Undertaking on 30 May 1978, and it began work on 1 June 1978, with funding from the European Community's members. JET made its first plasma on 25 June 1983.
- **JT-60** in Naka, Japan, built by the Japan Atomic Energy Research Institute, started on 8 April 1985.
- In the Soviet Union, the superconducting **T-15** followed in 1988.

With TFTR and JET, JT-60 was one of the "big three" tokamaks of the 1980s. In 1978 scientists from Europe, Japan, the Soviet Union and the United States also began **INTOR**, a study under the International Atomic Energy Agency for a shared international tokamak reactor. It was never built, but it brought the four sides' fusion experts together.

<figure class="unit-photo"><img src="units/fy14/pics/jet-exterior.jpg" alt="Colour photograph of the JET machine, a huge ring hidden under heating systems, pipes and diagnostics." width="1600" height="1257" loading="lazy"><figcaption>The Joint European Torus (JET) at Culham, UK, in 1991, the year it first produced fusion power with tritium. Its D-shaped vacuum chamber is 4.2 metres high and 2.5 metres wide. <span class="photo-credit">Photo: EFDA JET, CC BY-SA 3.0, via Wikimedia Commons</span></figcaption></figure>

## Geneva 1985: an offer between rivals {Geneva}

<!-- photo: geneva-summit-1985 -->

In 1985 the Cold War was still cold. Both superpowers had huge arsenals of nuclear weapons. In March 1985 **Mikhail Gorbachev** became the Soviet leader, and from 19 to 21 November 1985 he met US President **Ronald Reagan** in Geneva, their first summit. They did not agree on the big arms-control questions. But Gorbachev suggested that the two countries build a fusion experiment together, based on the INTOR studies. The idea came from his scientific adviser **Evgeny Velikhov**, a fusion physicist.

The joint statement of 21 November 1985 said that "a nuclear war cannot be won and must never be fought". In a section on fusion research, it began: "The two leaders emphasized the potential importance of the work aimed at utilizing controlled thermonuclear fusion". It called for "the widest practicable development of international cooperation in obtaining this source of energy", which it described as "essentially inexhaustible, for the benefit for all mankind" (the wording of the original text).

What followed took decades. At the Reykjavik summit of October 1986 a committee of four partners was formed: the European Community (through Euratom), Japan, the Soviet Union and the United States. In March 1987 they met at the IAEA in Vienna and launched conceptual design studies for the **International Thermonuclear Experimental Reactor**, **ITER** (*iter* is Latin for "the way"). The conceptual design itself was made in 1988–1990 and the engineering design in 1992–1998. The United States left the project in 1998 and returned in 2003, and China, South Korea and India joined. In 2005 Cadarache in France was chosen as the site, and the ITER Agreement was signed on 21 November 2006, 21 years to the day after the Geneva statement.

Big science has big problems. ITER's cost has grown to several times the first estimates, and its schedule has slipped again and again. As of November 2026, the official plan (the baseline of 2024) is to start research operation in 2034 and deuterium–tritium operation in 2039. These are institutional plans, not results.

## Key idea

From 1970 to 1985 fusion research moved from small laboratory machines to large national and international facilities, for reasons of physics, money and politics.

- **Physics:** the current alone cannot heat a plasma beyond about $20$–$30$ million kelvin, because a hotter plasma has less resistance. Neutral beams and radio waves took PLT to about $60$ million kelvin in 1978. Superconducting magnets (first in T-7, 1979) made strong fields possible without huge losses. A bigger plasma keeps its heat longer, so the machines grew.
- **Money:** the oil crisis of 1973–1974 made energy security urgent. The US fusion budget grew about eightfold from 1973 to 1978, and TFTR, JET, JT-60 and T-15 were built.
- **Politics:** machines became so expensive that countries shared them. JET was a European project, INTOR an international study, and in 1985 the Cold War rivals agreed at Geneva to work together on fusion. That decision led to ITER.

## Common misconception

"PLT reached $60$ million kelvin, so the main problem of fusion was solved in 1978." Temperature is only one of three conditions. The plasma must also be dense enough and keep its energy long enough (the **Lawson criterion**). In 1978 these were still far from reactor values, and no machine had yet used deuterium–tritium fuel.

A second mistake is to think that the Geneva summit of 1985 ended the Cold War. It did not: it was the first step of a slow thaw. Cooperation on fusion was easier than on weapons because fusion power was far away and gave neither side a military advantage.

## Summary

- Ohmic heating weakens as the plasma gets hotter (its resistance falls), so neutral beam injection and radio-wave heating were developed; PLT reached about $60$ million kelvin in July 1978.
- Superconducting magnets have no resistance when cold: T-7 (1979) was the first superconducting tokamak, T-15 (1988) its larger successor.
- The oil crisis of October 1973 – March 1974 increased energy research funding: the US fusion budget grew from about $40$ to $332$ million dollars from 1973 to 1978.
- The big tokamaks TFTR (USA, 1982), JET (Europe, 1983) and JT-60 (Japan, 1985) were built, and INTOR (from 1978) brought the four main fusion powers together.
- At Geneva in November 1985 Gorbachev and Reagan called for international cooperation on fusion. This led to ITER, designed from 1988 and agreed in 2006; as of November 2026, deuterium–tritium operation is planned for 2039.
