## fy9-aallot-s1

### a)
**Given:** length of the vibrating part of the string $L = 648\,\text{mm}$, fundamental frequency $f_1 = 110.0\,\text{Hz}$, speed of sound in air $v_\text{air} = 343\,\text{m/s}$
**Find:** the speed $v$ of the wave in the string and the wavelength of the fundamental in the string $\lambda_1$ and in air $\lambda_\text{air}$
**Principle:** The string is fixed at the nut and at the bridge, so there are nodes at the ends. At the fundamental frequency the string has one antinode, and the length of the string is half the wavelength (chapter *Standing waves: nodes, antinodes and natural frequencies*). The string makes the air vibrate at the same frequency, but sound travels in air at a different speed from the wave in the string, so the wavelength is different (chapter *How waves form and travel*).
**Formula:** $L = \dfrac{\lambda_1}{2}$, so $\lambda_1 = 2L$ and $v = f_1\lambda_1 = 2Lf_1$; in air $\lambda_\text{air} = \dfrac{v_\text{air}}{f_1}$
**Conversions:** $648\,\text{mm} = 648 \cdot 0.001\,\text{m} = 0.648\,\text{m}$
**Substitution:** $\lambda_1 = 2 \cdot 0.648\,\text{m} = 1.296\,\text{m}$, $v = 110.0\,\tfrac{1}{\text{s}} \cdot 1.296\,\text{m} = 142.56\,\text{m/s}$ and $\lambda_\text{air} = \dfrac{343\,\text{m/s}}{110.0\,\text{Hz}} = 3.118\,\text{m}$
**Answer:** The wave travels along the string at the speed $v \approx 143\,\text{m/s}$. The wavelength of the fundamental is $1.30\,\text{m}$ in the string and $3.12\,\text{m}$ in air, three significant figures like the speed of sound $343\,\text{m/s}$ and the length $648\,\text{mm}$.
**Reasonableness:** The frequency is the same in both, so the ratio of the wavelengths is the ratio of the speeds: $3.118 : 1.296 \approx 2.41 = 343 : 142.6$. The wavelength in the string is twice the length of the string, as it should be at the fundamental frequency.

### b)
**Given:** speed of the wave in the string $v = 142.56\,\text{m/s}$ (part a), wanted frequency $f' = 123.5\,\text{Hz}$, full length $L = 648\,\text{mm}$
**Find:** the length $L'$ of the vibrating part of the string and the distance of the fret from the nut
**Principle:** The string and its tension stay the same, so the speed of the wave in the string does not change. The fret is a new node, so the part vibrating at the fundamental frequency is half the new wavelength (chapter *Standing waves: nodes, antinodes and natural frequencies*). The distance of the fret from the nut is the difference between the full length and the vibrating part.
**Formula:** $f' = \dfrac{v}{2L'}$, so $L' = \dfrac{v}{2f'}$, and the distance from the nut is $L - L'$
**Conversions:** Finally $1\,\text{m} = 1000\,\text{mm}$.
**Substitution:** $L' = \dfrac{142.56\,\text{m/s}}{2 \cdot 123.5\,\tfrac{1}{\text{s}}} = 0.5772\,\text{m} = 577.2\,\text{mm}$, and $648\,\text{mm} - 577.2\,\text{mm} = 70.8\,\text{mm}$
**Answer:** The vibrating part must be $L' \approx 577\,\text{mm}$, three significant figures like the given data, and the fret is about $71\,\text{mm}$ from the nut. The distance is a difference, so it is known to the nearest millimetre.
**Reasonableness:** The frequency grows by the factor $123.5 : 110.0 \approx 1.12$, so the length must become shorter by the same factor: $648\,\text{mm} : 1.123 \approx 577\,\text{mm}$. On a guitar the second fret is about $7\,\text{cm}$ from the nut, so the result fits.

### c)
**Given:** $6$ beats in $4.0$ seconds, reference note $110.0\,\text{Hz}$; tightening makes the beats slower
**Find:** the frequency of the string $f_\text{string}$ before tightening
**Principle:** The beat frequency of two sounds of almost the same frequency is the difference of the frequencies (chapter *Sound as a wave: pitch, timbre and the Doppler effect*). The beats tell only the difference, not its direction, so the direction is deduced from the tightening: in a tighter string the wave travels faster, and the frequency $f = \tfrac{v}{2L}$ rises (chapter *Standing waves: nodes, antinodes and natural frequencies*). When the frequency rose and the beats became slower, the frequency difference became smaller, so the frequency of the string was below $110.0\,\text{Hz}$.
**Formula:** $f_\text{h} = \dfrac{N}{t}$ and $f_\text{h} = |f_\text{string} - f_\text{ref}|$, so $f_\text{string} = f_\text{ref} - f_\text{h}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $f_\text{h} = \dfrac{6}{4.0\,\text{s}} = 1.5\,\text{Hz}$, so $f_\text{string} = 110.0\,\text{Hz} - 1.5\,\text{Hz} = 108.5\,\text{Hz}$
**Answer:** $f_\text{string} = 108.5\,\text{Hz}$. The precision is a tenth, because the reference note is known to $0.1\,\text{Hz}$ and the beats $1.5\,\text{Hz}$ to two figures.
**Reasonableness:** If the string had been at $111.5\,\text{Hz}$, tightening would have increased the difference and the beats would have become faster. The frequency difference $1.5\,\text{Hz}$ is below about $10\,\text{Hz}$, so the beats really can be heard.

### d)
**Find:** why a string lightly touched at its midpoint sounds an octave higher
**Principle:** The natural frequencies of a string fixed at both ends are $f_n = n f_1$, and at the natural frequency $f_n$ the string has $n$ antinodes. The touch stops the motion of the string at that point, so a node forms there (chapter *Standing waves: nodes, antinodes and natural frequencies*).
**Model answer:** A freely sounding string vibrates at the fundamental frequency and at the overtones at the same time. At the fundamental frequency the midpoint is an antinode, so the finger damps the fundamental and all the odd natural frequencies, which have an antinode at the midpoint. What remains are the natural frequencies $n = 2, 4, 6, \ldots$, which have a node at the midpoint, because the finger does not stop their motion. The lowest of them is $f_2 = 2f_1 = 220\,\text{Hz}$: the string vibrates in two segments, with an antinode in each half, and twice the frequency sounds an octave higher. The finger can be lifted, and the string still sounds the same way, because the standing wave goes on.

### Yleisiä virheitä
- In part a the length of the string is taken as the wavelength, so that $v = f_1 L \approx 71\,\text{m/s}$; at the fundamental frequency $L = \tfrac{\lambda}{2}$.
- In part a the wavelength in the string $1.30\,\text{m}$ is given as the wavelength in air: the frequency stays the same, the wavelength does not.
- In part b the speed is assumed to change, or the length is calculated as directly proportional to the frequency.
- In part c the beat frequency is taken as $6\,\text{Hz}$, or both alternatives are given without justification.

### Hyväksytään myös
- In part b with a ratio: $L' = L \cdot \dfrac{f_1}{f'} = 648\,\text{mm} \cdot \dfrac{110.0}{123.5} \approx 577\,\text{mm}$, because the speed is the same.

## fy9-aallot-s2

### a)
**Given:** frequency of the pulse $f = 30.0\,\text{kHz}$, speed of sound in air $v = 340\,\text{m/s}$
**Find:** the wavelength $\lambda$
**Principle:** Ultrasound is sound, so it travels in air at the speed of sound, and the speed, frequency and wavelength are related by the wave equation (chapter *How waves form and travel*).
**Formula:** $v = f\lambda$, so $\lambda = \dfrac{v}{f}$
**Conversions:** $30.0\,\text{kHz} = 30.0 \cdot 1000\,\text{Hz} = 30\,000\,\text{Hz}$ and finally $1\,\text{m} = 1000\,\text{mm}$
**Substitution:** $\lambda = \dfrac{340\,\text{m/s}}{30\,000\,\tfrac{1}{\text{s}}} = 0.01133\,\text{m} = 11.33\,\text{mm}$
**Answer:** $\lambda \approx 11.3\,\text{mm}$, three significant figures like the frequency $30.0\,\text{kHz}$.
**Reasonableness:** The wavelength of a sound at the upper limit of hearing, $20\,\text{kHz}$, is $17\,\text{mm}$, so a higher frequency gives a shorter wavelength, as it should. The centimetre range is the size range of small insects.

### b)
**Given:** travel time of the echo $t = 12.0\,\text{ms}$, speed of sound $v = 340\,\text{m/s}$, speed of the bat $6.0\,\text{m/s}$
**Find:** the distance $d$ of the insect and the effect of the bat's motion on it
**Principle:** The pulse travels from the bat to the insect and back as an echo, so it travels the distance $d$ twice at a constant speed (chapter *Applied chapter: ultrasound imaging and earthquake waves*). The bat's own motion during the echo is estimated separately.
**Formula:** $2d = vt$, so $d = \dfrac{vt}{2}$; displacement of the bat $s = v_\text{b} t$
**Conversions:** $12.0\,\text{ms} = 12.0 \cdot 0.001\,\text{s} = 0.0120\,\text{s}$
**Substitution:** $d = \dfrac{340\,\tfrac{\text{m}}{\text{s}} \cdot 0.0120\,\text{s}}{2} = 2.04\,\text{m}$ and $s = 6.0\,\tfrac{\text{m}}{\text{s}} \cdot 0.0120\,\text{s} = 0.072\,\text{m}$
**Answer:** The insect is about $2.04\,\text{m}$ away, three significant figures like the travel time $12.0\,\text{ms}$. During the echo the bat moves about $7\,\text{cm}$, that is about $3.5\,\%$ of the distance, so the distance is really known only to about $2.0\,\text{m}$.
**Reasonableness:** A distance of two metres there and back is $4\,\text{m}$, and sound travels it in about a hundredth of a second, as measured. The speed of the bat is less than $2\,\%$ of the speed of sound, so the effect of its motion is small.

### c)
**Given:** frequency of the pulse $f_0 = 30.0\,\text{kHz}$, speed of the bat $v_\text{b} = 6.0\,\text{m/s}$ towards the wall, speed of sound $v = 340\,\text{m/s}$, the wall at rest
**Find:** the frequency $f$ of the echo the bat hears
**Principle:** The Doppler effect happens twice (chapter *Sound as a wave: pitch, timbre and the Doppler effect*). The bat is first the source and then the listener, and its speed is $v_\text{b}$. First the bat is a moving source and the wall a receiver at rest: in front of an approaching source the wavelength becomes shorter. The wall reflects the frequency it receives as a source at rest, and the bat is now a listener that approaches it and meets the wavefronts more often. In both stages approaching raises the frequency.
**Formula:** $f_\text{s} = f_0 \cdot \dfrac{v}{v - v_\text{b}}$ and $f = f_\text{s} \cdot \dfrac{v + v_\text{b}}{v}$, so $f = f_0 \cdot \dfrac{v + v_\text{b}}{v - v_\text{b}}$
**Conversions:** The frequency stays in the unit $\text{kHz}$, because the ratio of the speeds has no unit.
**Substitution:** $f_\text{s} = 30.0\,\text{kHz} \cdot \dfrac{340\,\text{m/s}}{334\,\text{m/s}} = 30.54\,\text{kHz}$ and $f = 30.54\,\text{kHz} \cdot \dfrac{346\,\text{m/s}}{340\,\text{m/s}} = 31.08\,\text{kHz}$
**Answer:** $f \approx 31.1\,\text{kHz}$, that is about $1.1\,\text{kHz}$ higher than the pulse sent, three significant figures like the frequency $30.0\,\text{kHz}$.
**Reasonableness:** At small speeds each stage raises the frequency by about the fraction $\tfrac{v_\text{b}}{v} = \tfrac{6.0}{340} \approx 1.8\,\%$, about $3.5\,\%$ in all, and $30.0\,\text{kHz} \cdot 1.035 \approx 31.1\,\text{kHz}$. The heard frequency is greater than $f_0$, as it should be when approaching.

### d)
**Find:** why a mosquito could not be detected with a $3\,\text{kHz}$ sound
**Principle:** Diffraction is strong when the obstacle is about the wavelength or smaller: the wave bends round the obstacle and leaves no shadow (chapter *A wave meets an obstacle or a gap*). The wavelength is $\lambda = \tfrac{v}{f}$.
**Model answer:** At the frequency $3\,\text{kHz}$ the wavelength would be $\tfrac{340\,\text{m/s}}{3000\,\text{Hz}} \approx 11\,\text{cm}$, more than twenty times the length of the mosquito, $5\,\text{mm}$. Such a small obstacle hardly changes the travel of a long wave: the wave bends round it, and no detectable echo or shadow comes back from the mosquito. The wavelength of the ultrasound, $11\,\text{mm}$, is of the order of the mosquito's size, so the mosquito reflects a detectable echo from it, and the bat can also tell apart targets that are close together. That is why the bat uses ultrasound: a short wavelength is a condition for detecting small prey.

### Yleisiä virheitä
- In part b the distance is calculated as $d = vt \approx 4.1\,\text{m}$ without dividing by two.
- In part c only one stage is calculated, so that the result is $30.5\,\text{kHz}$, or the signs are chosen so that the approaching bat hears a lower frequency.
- In part c the speed of the bat is added to the speed of sound without the Doppler formula, and the wavelength is left the same.
- In part d the argument is that a low sound is weaker; what decides is the ratio of the wavelength to the size of the target.

### Hyväksytään myös
- In part c directly with the combined formula $f = f_0 \cdot \dfrac{v + v_\text{b}}{v - v_\text{b}}$, when its two stages are justified.

## fy9-aallot-s3

### a)
**Find:** the period as a function of the length of the string as a graph, and whether the period is directly proportional to the length
**Graph:** The period is the time of ten swings divided by ten: $0.936\,\text{s}$, $1.207\,\text{s}$, $1.444\,\text{s}$, $1.629\,\text{s}$, $1.814\,\text{s}$ and $1.976\,\text{s}$. On the horizontal axis is $l\ (\text{m})$ and on the vertical axis $T\ (\text{s})$, and the axes start from zero, so that it shows whether a straight line would pass through the origin. The points are not joined with a broken line.

<svg data-fig="fy9-aallot-s3-T" viewBox="0 0 600 440" role="img" aria-label="Graph: the period T of a pendulum in seconds as a function of the length l of the string in metres. Six black points at lengths 0.20–0.95 m, periods from 0.94 seconds to 1.98 seconds. A dashed curve that levels off runs through the points: four times the length gives only about twice the period, so no straight line through the origin fits the points." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="380" x2="129.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163" y1="380" x2="163" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196" y1="380" x2="196" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229.5" y1="380" x2="229.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="380" x2="263" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296.5" y1="380" x2="296.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="380" x2="330" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="380" x2="363" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396.5" y1="380" x2="396.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="349.5" x2="430" y2="349.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="319" x2="430" y2="319" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="289" x2="430" y2="289" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="258.5" x2="430" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228" x2="430" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="430" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="167" x2="430" y2="167" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137" x2="430" y2="137" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="106.5" x2="430" y2="106.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="380" x2="129.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163" y1="380" x2="163" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="196" y1="380" x2="196" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229.5" y1="380" x2="229.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="263" y1="380" x2="263" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0.5$</div></foreignObject>
  <line x1="296.5" y1="380" x2="296.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="330" y1="380" x2="330" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="363" y1="380" x2="363" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="396.5" y1="380" x2="396.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="402.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1.0$</div></foreignObject>
  <line x1="89" y1="349.5" x2="96" y2="349.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="319" x2="96" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="301" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0.5$</div></foreignObject>
  <line x1="89" y1="289" x2="96" y2="289" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="258.5" x2="96" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="240.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1.0$</div></foreignObject>
  <line x1="89" y1="228" x2="96" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="179.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1.5$</div></foreignObject>
  <line x1="89" y1="167" x2="96" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137" x2="96" y2="137" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="119" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$2.0$</div></foreignObject>
  <line x1="89" y1="106.5" x2="96" y2="106.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="58" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$2.5$</div></foreignObject>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="16" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$T\ (\text{s})$</div></foreignObject>
  <polyline points="96,351.5 99,344 101.5,337.5 104.5,332 107,327 110,322.5 112.5,318.5 115.5,314.5 118.5,311 121,307.5 124,304 126.5,300.5 129.5,297.5 132,294.5 135,292 138,289 140.5,286.5 143.5,283.5 146,281 149,278.5 151.5,276 154.5,274 157,271.5 160,269.5 163,267 165.5,265 168.5,262.5 171,260.5 174,258.5 176.5,256.5 179.5,254.5 182.5,252.5 185,250.5 188,248.5 190.5,247 193.5,245 196,243 199,241.5 202,239.5 204.5,238 207.5,236 210,234.5 213,232.5 215.5,231 218.5,229.5 221,227.5 224,226 227,224.5 229.5,223 232.5,221 235,219.5 238,218 240.5,216.5 243.5,215 246.5,213.5 249,212 252,210.5 254.5,209 257.5,207.5 260,206.5 263,205 266,203.5 268.5,202 271.5,200.5 274,199.5 277,198 279.5,196.5 282.5,195 285.5,194 288,192.5 291,191 293.5,190 296.5,188.5 299,187.5 302,186 305,184.5 307.5,183.5 310.5,182 313,181 316,179.5 318.5,178.5 321.5,177 324,176 327,174.5 330,173.5 332.5,172.5 335.5,171 338,170 341,169 343.5,167.5 346.5,166.5 349.5,165.5 352,164 355,163 357.5,162 360.5,160.5 363,159.5 366,158.5 369,157.5 371.5,156 374.5,155 377,154 380,153 382.5,152 385.5,150.5 388,149.5 391,148.5 394,147.5 396.5,146.5 399.5,145.5 402,144.5 405,143 407.5,142 410.5,141 413.5,140 416,139 419,138 421.5,137 424.5,136 427,135 430,134" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="163" cy="266" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="213" cy="233" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="263" cy="204.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="313" cy="182" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="363" cy="159.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="413.5" cy="139.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="236.5" y="295" width="148" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#6b7480">$\text{levels off}$</div></foreignObject>
</svg>

**Model answer:** The period is not directly proportional to the length. The graph levels off: as the length grows, the period grows more and more slowly, and no straight line through the origin fits the points. For example, when the length becomes four times as long, from $0.200\,\text{m}$ to $0.800\,\text{m}$, the period grows by a factor of only $1.814 : 0.936 \approx 1.9$. This fits the pendulum model, in which the period is proportional to the square root of the length, and $\sqrt{4} = 2$.

### b)
**Find:** a presentation of the data in which a straight line fits the points, a justification and the fitted line
**Graph:** For small swings $T = 2\pi\sqrt{\tfrac{l}{g}}$. Squaring the equation gives $T^2 = \tfrac{4\pi^2}{g}\,l$, so $T^2$ is directly proportional to the length. Calculate $T^2$: $0.876\,\text{s}^2$, $1.457\,\text{s}^2$, $2.085\,\text{s}^2$, $2.654\,\text{s}^2$, $3.291\,\text{s}^2$ and $3.905\,\text{s}^2$. On the horizontal axis is $l\ (\text{m})$ and on the vertical axis $T^2\ (\text{s}^2)$. The line is fitted among the points and not forced through the origin, so that a possible systematic error shows.

<svg data-fig="fy9-aallot-s3-lin" viewBox="0 0 600 440" role="img" aria-label="Graph: the square of the period, T squared, in seconds squared as a function of the length l of the string in metres. Six black points at lengths 0.20–0.95 m, values from 0.88 to 3.90. A rising straight line has been fitted to the points and extended as a dashed line to the vertical axis, which it crosses at about 0.055 s², a little above the origin. Two points on the line are circled, (0.10 m; 0.46 s²) and (0.90 m; 3.69 s²), from which the slope is read as about 4.04 s² per metre." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="380" x2="129.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163" y1="380" x2="163" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196" y1="380" x2="196" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="229.5" y1="380" x2="229.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="380" x2="263" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296.5" y1="380" x2="296.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="380" x2="330" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="380" x2="363" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396.5" y1="380" x2="396.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="346" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="312.5" x2="430" y2="312.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="278.5" x2="430" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="245" x2="430" y2="245" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="211" x2="430" y2="211" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="177.5" x2="430" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="143.5" x2="430" y2="143.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="430" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="380" x2="129.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163" y1="380" x2="163" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="196" y1="380" x2="196" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229.5" y1="380" x2="229.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="263" y1="380" x2="263" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0.5$</div></foreignObject>
  <line x1="296.5" y1="380" x2="296.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="330" y1="380" x2="330" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="363" y1="380" x2="363" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="396.5" y1="380" x2="396.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="402.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1.0$</div></foreignObject>
  <line x1="89" y1="346" x2="96" y2="346" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="312.5" x2="96" y2="312.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="294.5" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="89" y1="278.5" x2="96" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="245" x2="96" y2="245" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="227" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="89" y1="211" x2="96" y2="211" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="177.5" x2="96" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="159.5" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="89" y1="143.5" x2="96" y2="143.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="92" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="16" width="106" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <polyline points="163,321.5 413.5,117" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,376.5 163,321.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="163" cy="321" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="213" cy="281.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="263" cy="239" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="313" cy="200.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="363" cy="157.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="413.5" cy="116" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="129.5" cy="349" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="129.5" y1="349" x2="129.5" y2="380" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="349" x2="129.5" y2="349" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="396.5" cy="130.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="396.5" y1="130.5" x2="396.5" y2="380" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="130.5" x2="396.5" y2="130.5" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="96" cy="376.5" r="6" fill="#2b8a3e"/>
  <foreignObject x="196" y="325" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b \approx 0.055\,\text{s}^2$</span></div></foreignObject>
  <foreignObject x="109.5" y="85" width="180" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$k \approx 4.04\,\text{s}^2/\text{m}$</div></foreignObject>
</svg>

**Model answer:** The points lie well on a straight line, so the pendulum model describes the data. The line does not, however, pass exactly through the origin, but crosses the vertical axis at about $0.055$–$0.056\,\text{s}^2$. This is interpreted in part d.

### c)
**Given:** the fitted line in the graph; points read from the line $(0.10\,\text{m};\ 0.46\,\text{s}^2)$ and $(0.90\,\text{m};\ 3.69\,\text{s}^2)$; reference value $9.81\,\text{m/s}^2$
**Find:** the acceleration of free fall $g$ and its comparison with the value $9.81\,\text{m/s}^2$
**Principle:** By the model $T^2 = \tfrac{4\pi^2}{g}\,l$ the slope of the $(l, T^2)$ graph is $k = \tfrac{4\pi^2}{g}$ (chapter *The mass–spring oscillator and the pendulum*). The slope is read from two points of the fitted line far apart, not from the measured points (chapter *Graphing and fitting a straight line*). A possible systematic error in the length shifts the line but does not change its slope.
**Reading the graph:** From the line the points at $l = 0.10\,\text{m}$ and $l = 0.90\,\text{m}$ are read: $T^2 \approx 0.46\,\text{s}^2$ and $T^2 \approx 3.69\,\text{s}^2$.
**Formula:** $k = \dfrac{\Delta (T^2)}{\Delta l}$ and $k = \dfrac{4\pi^2}{g}$, so $g = \dfrac{4\pi^2}{k}$
**Conversions:** The quantities are in base units, so no conversions are needed; $\tfrac{\text{m}}{\text{s}^2}$ comes from dividing by the unit $\tfrac{\text{s}^2}{\text{m}}$.
**Substitution:** $k = \dfrac{3.69\,\text{s}^2 - 0.46\,\text{s}^2}{0.90\,\text{m} - 0.10\,\text{m}} = \dfrac{3.23\,\text{s}^2}{0.80\,\text{m}} = 4.0375\,\text{s}^2\text{/m}$, so $g = \dfrac{4\pi^2}{4.0375\,\text{s}^2\text{/m}} = 9.778\,\text{m/s}^2$
**Answer:** $g \approx 9.8\,\text{m/s}^2$, two significant figures, because the values read from the graph are good to about a hundredth and hand timing limits the precision.
**Reasonableness:** The difference from the value $9.81\,\text{m/s}^2$ is about $0.3\,\%$. The uncertainty of hand timing of ten swings, about $0.1$–$0.2\,\text{s}$, is $1$–$2\,\%$ of the time $t_{10}$ and $2$–$4\,\%$ of the value $T^2$, so the difference is within the precision of the measurement. For small swings of $5^\circ$ the period differs from the model by less than $0.1\,\%$.

### d)
**Given:** slope of the fitted line $k \approx 4.04\,\text{s}^2\text{/m}$ and constant term $b \approx 0.056\,\text{s}^2$ (from the points read in part c; the intercept in the graph is about $0.055\,\text{s}^2$, and the difference does not change the result), wanted period $T = 2.00\,\text{s}$
**Find:** what the constant term tells about the measurement, and the length $l$, measured the group's way, for which $T = 2.00\,\text{s}$
**Principle:** If the true length of the pendulum is $l + \Delta l$, the model gives $T^2 = k(l + \Delta l) = kl + k\Delta l$, so the line shifts upwards and crosses the $l$ axis at $-\Delta l$ (chapter *Measuring and the reliability of a measurement*). The length of a pendulum is the distance from the point of suspension to the centre of gravity of the ball (chapter *The mass–spring oscillator and the pendulum*). The wanted length is found from the equation of the fitted line, so that the same systematic error is included.
**Reading the graph:** From the points read in part c, the equation of the line is $T^2 = 4.04\,\tfrac{\text{s}^2}{\text{m}} \cdot l + 0.056\,\text{s}^2$; it crosses the $l$ axis when $T^2 = 0$.
**Formula:** $T^2 = kl + b$, so $l = \dfrac{T^2 - b}{k}$, and the $l$ intercept is $-\dfrac{b}{k}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $-\dfrac{b}{k} = -\dfrac{0.0563\,\text{s}^2}{4.0375\,\text{s}^2\text{/m}} = -0.014\,\text{m}$ and $l = \dfrac{(2.00\,\text{s})^2 - 0.0563\,\text{s}^2}{4.0375\,\text{s}^2\text{/m}} = \dfrac{3.944\,\text{s}^2}{4.0375\,\text{s}^2\text{/m}} = 0.9768\,\text{m}$
**Answer:** The line crosses the $l$ axis at about $-1.4\,\text{cm}$: the true length of the pendulum is about $1.4\,\text{cm}$ greater than the measured one. The length was measured to the top of the ball and not to its centre, so the measurement has a systematic error the size of the radius of the ball. The length measured the group's way must be about $0.98\,\text{m}$, two significant figures, because the result depends on the constant term read from the graph.
**Reasonableness:** By the known model the length of a pendulum with the period $2.00\,\text{s}$ is $\tfrac{9.81\,\text{m/s}^2 \cdot (2.00\,\text{s})^2}{4\pi^2} \approx 0.994\,\text{m}$ to the centre of the ball. Subtracting about $1.4\,\text{cm}$ gives $0.98\,\text{m}$, the same result. A radius of $1$–$2\,\text{cm}$ is believable for a small ball.

### Yleisiä virheitä
- In part a the points are joined with a broken line, or the time of ten swings is taken as the period.
- In part b $T$ is plotted against the square root, or $T^2$ without justification, or the line is forced through the origin, which gives $g$ as about $9.6\,\text{m/s}^2$.
- In part c the slope is calculated from two measured points or interpreted directly as the acceleration of free fall without the formula $k = \tfrac{4\pi^2}{g}$.
- In part d the constant term is explained by a random error; it shifts all the points in the same direction.

### Hyväksytään myös
- In parts b and c a $(\sqrt{l}, T)$ graph, when its slope is $\tfrac{2\pi}{\sqrt{g}}$ and the interpretation is correct.
- In part d calculating the length from the model $l = \tfrac{gT^2}{4\pi^2} - 0.014\,\text{m}$.

## fy9-aallot-s4

### a)
**Find:** whether claim 1 is true and what the level is at the houses
**Principle:** The power of a point source spreads over the surface of a sphere, so $I = \tfrac{P}{4\pi r^2}$, and the difference of the levels is $L_2 - L_1 = 10\,\text{dB} \cdot \lg \tfrac{I_2}{I_1}$ (chapter *Intensity and the decibel scale*).
**Model answer:** The claim is false. When the distance doubles, the intensity drops to a quarter, and the level falls by $10\,\text{dB} \cdot \lg 4 \approx 6\,\text{dB}$, not by half: $40\,\text{m}$ away the level is about $100\,\text{dB}$. The decibel scale is logarithmic, so a decibel reading cannot be divided like an intensity. At the houses the distance is $20$ times as large, so the intensity is $\tfrac{1}{400}$ and the level is $106\,\text{dB} - 10\,\text{dB} \cdot \lg 400 \approx 106\,\text{dB} - 26\,\text{dB} = 80\,\text{dB}$, the level of a busy street. The model is a rough estimate: the air and the terrain absorb sound, but a following wind and reflections from the surface of the lake can raise the level. The music will in any case be heard clearly at the houses.

### b)
**Find:** whether claim 2 is true and why mostly low sounds are heard behind the fence
**Principle:** Diffraction is strong when the obstacle is about the wavelength or smaller (chapter *A wave meets an obstacle or a gap*). The wavelength is $\lambda = \tfrac{v}{f}$.
**Model answer:** The observation is true, but the reasoning is wrong. Low sounds are heard behind the fence because they bend over the fence. For example, the wavelength of a $60\,\text{Hz}$ bass sound is $\tfrac{340\,\text{m/s}}{60\,\text{Hz}} \approx 5.7\,\text{m}$, much longer than the fence, so the wave bends behind the fence almost without weakening. The wavelength of a high $4\,\text{kHz}$ sound is only about $9\,\text{cm}$, so it is left with a sound shadow behind the $2\,\text{m}$ fence. The bass sounds are not necessarily louder: even if the low and high sounds were equally loud when they leave, the fence weakens the high ones. That is why the fence protects mainly against high sounds, and reducing the bass needs measures at the source, for example limiting the level or pointing the loudspeakers away from the houses.

### c)
**Find:** whether claim 3 is true, the permitted exposure time and the effect of hearing protectors
**Principle:** In the rule of thumb for noise, the upper action value $85\,\text{dB}$ corresponds to $8\,\text{h}$, and each rise of $3\,\text{dB}$ halves the permitted time: $t_\text{allowed} = \tfrac{t_0}{2^{\,n}}$, $n = \tfrac{L - 85\,\text{dB}}{3\,\text{dB}}$ (chapter *Noise, acoustics and sound reproduction*). A hearing protector lowers the level that reaches the ear by its attenuation.
**Model answer:** The claim is false. The level $100\,\text{dB}$ is $15\,\text{dB}$, that is five steps of $3\,\text{dB}$, above the action value, so the permitted time is $8\,\text{h} : 2^5 = 8\,\text{h} : 32 = 0.25\,\text{h} = 15\,\text{min}$. "Only $15\,\text{dB}$" means $10^{1.5} \approx 32$ times the intensity, so a dose harmful to hearing builds up in about $\tfrac{1}{32}$ of the time. A four-hour concert without protectors is therefore many times the dose. With well-fitted $20\,\text{dB}$ protectors the level at the ear is about $80\,\text{dB}$, below $85\,\text{dB}$, so four hours is within the rule of thumb when the protectors are worn the whole time. The rule of thumb is an estimate, not a guarantee: different people's hearing tolerates noise differently.

### Yleisiä virheitä
- In part a the level is calculated as inversely proportional to the distance, so that the drop is $3\,\text{dB}$ per doubling, or the decibels are divided like intensities.
- In part b the explanation is that low sounds travel faster; in air the speed does not depend on the frequency.
- In part c $15\,\text{dB}$ is interpreted as an increase of $15\,\%$, or the time is halved every $15\,\text{dB}$.

## fy9-aallot-s5

### a)
**Given:** distance to the wall $d = 85.0\,\text{m}$, five echo times $0.45\,\text{s}$, $0.52\,\text{s}$, $0.41\,\text{s}$, $0.55\,\text{s}$ and $0.47\,\text{s}$
**Find:** the speed of sound $v$ from the mean and its uncertainty $\Delta v$
**Principle:** The sound travels to the wall and back, the distance $2d$, at a constant speed (chapter *Applied chapter: ultrasound imaging and earthquake waves*). The best estimate from repeated measurements is the mean, and half the range is a rough estimate of the spread, which is chosen here as the uncertainty of the result (chapter *Measuring and the reliability of a measurement*). The uncertainty of the distance is small, so the relative uncertainty of the time is also the relative uncertainty of the speed.
**Formula:** $\bar{t} = \dfrac{t_1 + \ldots + t_5}{5}$, $v = \dfrac{2d}{\bar{t}}$, $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$ and $\Delta v = v \cdot \dfrac{\Delta t}{\bar{t}}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $\bar{t} = \dfrac{2.40\,\text{s}}{5} = 0.48\,\text{s}$, $v = \dfrac{2 \cdot 85.0\,\text{m}}{0.48\,\text{s}} = 354.2\,\text{m/s}$, $\Delta t = \dfrac{0.55\,\text{s} - 0.41\,\text{s}}{2} = 0.07\,\text{s}$ and $\Delta v = 354.2\,\tfrac{\text{m}}{\text{s}} \cdot \dfrac{0.07\,\text{s}}{0.48\,\text{s}} = 51.6\,\text{m/s}$
**Answer:** $v = (350 \pm 50)\,\text{m/s}$. The uncertainty is rounded to one significant figure and the result to the same precision; the relative uncertainty is about $15\,\%$.
**Reasonableness:** With the extreme values the speed would be $\tfrac{170\,\text{m}}{0.55\,\text{s}} \approx 309\,\text{m/s}$ and $\tfrac{170\,\text{m}}{0.41\,\text{s}} \approx 415\,\text{m/s}$, so the estimate of the uncertainty matches the spread of the results. The result is of the right order of magnitude, about $340\,\text{m/s}$.

### b)
**Find:** whether the group's conclusion is justified
**Principle:** In a gas the speed of sound grows as the temperature rises, in air by about $0.6\,\text{m/s}$ per degree Celsius (chapter *Sound as a wave: pitch, timbre and the Doppler effect*). A difference between two values cannot be shown if the difference is smaller than the uncertainty (chapter *Measuring and the reliability of a measurement*).
**Model answer:** The conclusion is not justified. The book value $343\,\text{m/s}$ applies to air at $20\,{}^\circ\text{C}$, and at $5\,{}^\circ\text{C}$ sound should travel more slowly, about $343\,\text{m/s} - 0.6\,\tfrac{\text{m/s}}{{}^\circ\text{C}} \cdot 15\,{}^\circ\text{C} \approx 334\,\text{m/s}$. The group's result $(350 \pm 50)\,\text{m/s}$ covers both $334\,\text{m/s}$ and $343\,\text{m/s}$, so the measurement cannot tell them apart and shows no difference at all, least of all the one the group claims. The most important source of error is hand timing: the reaction time on starting and stopping is of the order of tenths of a second, as large as the variation of the results $0.14\,\text{s}$, and the delay is not necessarily the same at both ends. When the travel time of the echo is only about $0.5\,\text{s}$, even a systematic delay of $0.02\,\text{s}$ changes the result by $4\,\%$. The uncertainty of the distance $85.0\,\text{m}$ is insignificant. The correct conclusion is that the speed was about $350\,\text{m/s}$ with a large uncertainty, and that sound travels more slowly in cold air, not faster.

### c)
**Find:** a plan for a measurement in which the effect of temperature on the speed of sound can be detected
**Principle:** The speeds at the temperatures $5\,{}^\circ\text{C}$ and $20\,{}^\circ\text{C}$, $334\,\text{m/s}$ and $343\,\text{m/s}$, differ by about $3\,\%$, so the relative uncertainty of the measurement must be clearly smaller, about $1\,\%$ (chapters *Measuring and the reliability of a measurement* and *Your own experimental investigation: planning, carrying out and reporting*).
**Model answer:** The reaction time is removed from the timing. A phone or computer microphone records both the strike and the echo, and the time difference is read from the $(t, p)$ graph of the sound at the starts of the two peaks; the time can then be read to about a millisecond. Another way is two microphones a known distance apart on the same recorder. The measurement is made at several distances, for example $40$–$120\,\text{m}$, and the distance travelled $2d$ is plotted as a function of time: the slope of the line is the speed of sound, and a possible constant delay of the device shows in the constant term and does not distort the speed. Precision target: for a travel time of $0.5\,\text{s}$ the uncertainty of the time must be below $5\,\text{ms}$, which is possible from a recording but not with a stopwatch. The temperature is measured during each series of measurements, and the series is repeated at different temperatures, for example in autumn and in spring, so that the temperature is the only factor that changes. The measurements are made in calm weather or in both directions, so that the wind does not change the result, each measurement is repeated several times, and the speeds are given with their uncertainties, so that the difference can be compared with the uncertainty.

### Yleisiä virheitä
- In part a the speed is calculated as $v = \tfrac{d}{\bar{t}} \approx 177\,\text{m/s}$, forgetting that the echo travels the distance twice.
- In part a the result is given as $354.17\,\text{m/s}$ without an uncertainty, or the uncertainty is too precise.
- In part b the conclusion is assessed only by comparing the numbers $354$ and $343$ without the uncertainty.
- In part c only more repetitions are suggested; repetitions do not remove the systematic part of the reaction time.

## fy9-aallot-s6

### a)
**Given:** unstretched length of the cord $L_0 = 18.0\,\text{m}$, initial speed $0$, $g = 9.81\,\text{m/s}^2$; air resistance is neglected
**Find:** the speed $v$ when the cord starts to stretch
**Principle:** Before the cord becomes tight, only the weight acts on the jumper, so mechanical energy is conserved (chapter *Conservation of mechanical energy and the work–energy principle*). The zero level is chosen at the point where the cord starts to stretch.
**Formula:** $mgL_0 = \tfrac12 mv^2$, so the mass cancels and $v = \sqrt{2gL_0}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $v = \sqrt{2 \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 18.0\,\text{m}} = \sqrt{353.2\,\tfrac{\text{m}^2}{\text{s}^2}} = 18.79\,\text{m/s}$
**Answer:** $v \approx 18.8\,\text{m/s}$, that is about $68\,\text{km/h}$, three significant figures like the unstretched length $18.0\,\text{m}$.
**Reasonableness:** In free fall $18\,\text{m}$ takes $\sqrt{\tfrac{2 \cdot 18.0\,\text{m}}{9.81\,\text{m/s}^2}} \approx 1.9\,\text{s}$, and the speed is $gt \approx 18.8\,\text{m/s}$, the same result. In reality air resistance makes the speed a little smaller.

### b)
**Given:** $m = 72.0\,\text{kg}$, $L_0 = 18.0\,\text{m}$, spring constant $k = 120\,\text{N/m}$, $g = 9.81\,\text{m/s}^2$
**Find:** the depth of the lowest point below the bridge $L_0 + x$, where $x$ is the greatest extension of the cord
**Principle:** The weight and the force of the cord, which is harmonic like a spring force, act on the jumper. Both are conservative, so mechanical energy is conserved during the whole fall (chapters *Conservation of mechanical energy and the work–energy principle* and *Spring force and spring energy*). At the lowest point the speed is zero, so the change in the gravitational potential energy over the whole distance $L_0 + x$ has turned into the elastic potential energy of the cord. The zero level is chosen at the lowest point.
**Formula:** $mg(L_0 + x) = \tfrac12 kx^2$, that is $\tfrac12 kx^2 - mgx - mgL_0 = 0$, whose positive solution is $x = \dfrac{mg + \sqrt{(mg)^2 + 2kmgL_0}}{k}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $mg = 72.0\,\text{kg} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} = 706.32\,\text{N}$, $(mg)^2 = (706.32\,\text{N})^2 \approx 498\,888\,\text{N}^2$ and $2kmgL_0 = 2 \cdot 120\,\tfrac{\text{N}}{\text{m}} \cdot 706.32\,\text{N} \cdot 18.0\,\text{m} \approx 3\,051\,302\,\text{N}^2$, so the square root is $\sqrt{3\,550\,190\,\text{N}^2} \approx 1884.2\,\text{N}$ and $x = \dfrac{706.32\,\text{N} + 1884.2\,\text{N}}{120\,\text{N/m}} = 21.59\,\text{m}$ and the depth $18.0\,\text{m} + 21.59\,\text{m} = 39.59\,\text{m}$
**Answer:** The jumper falls about $39.6\,\text{m}$ below the bridge, three significant figures like the given data.
**Reasonableness:** The energy balance checks: $mg(L_0 + x) = 706.32\,\text{N} \cdot 39.59\,\text{m} \approx 27.96\,\text{kJ}$ and $\tfrac12 kx^2 = \tfrac12 \cdot 120\,\tfrac{\text{N}}{\text{m}} \cdot (21.59\,\text{m})^2 \approx 27.96\,\text{kJ}$. The cord stretches more than its unstretched length, which is usual for a bungee cord; the bridge must be clearly more than $40\,\text{m}$ high.

### c)
**Given:** extension $x = 21.59\,\text{m}$, $k = 120\,\text{N/m}$, $m = 72.0\,\text{kg}$, $g = 9.81\,\text{m/s}^2$
**Find:** the acceleration $a$ at the lowest point with its direction
**Principle:** At the lowest point the weight acts on the jumper downwards and the force of the cord $kx$ upwards. By Newton's second law the net force gives the acceleration (chapter *Newton's second law*). Upwards is chosen as the positive direction.
**Formula:** $kx - mg = ma$, so $a = \dfrac{kx}{m} - g$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $kx = 120\,\tfrac{\text{N}}{\text{m}} \cdot 21.59\,\text{m} = 2590.5\,\text{N}$, so $a = \dfrac{2590.5\,\text{N}}{72.0\,\text{kg}} - 9.81\,\tfrac{\text{m}}{\text{s}^2} = 35.98\,\tfrac{\text{m}}{\text{s}^2} - 9.81\,\tfrac{\text{m}}{\text{s}^2} = 26.17\,\text{m/s}^2$
**Answer:** $a \approx 26.2\,\text{m/s}^2$ upwards, three significant figures like the given data.
**Reasonableness:** The acceleration is about $2.7g$, and the force of the cord is $2590\,\text{N} : 706\,\text{N} \approx 3.7$ times the weight. That is a strong but brief load, which the harness spreads over the ankles and legs. The acceleration points upwards although the jumper is momentarily at rest, as it should at an extreme position.

### d)
**Given:** $m = 72.0\,\text{kg}$, $k = 120\,\text{N/m}$
**Find:** the period $T$ of small oscillations
**Principle:** The weight and the harmonic force of the cord act on the hanging jumper. The weight only shifts the equilibrium position to the point where the cord is stretched by $x_0 = \tfrac{mg}{k}$, and the displacement from there follows the law of the mass–spring oscillator (chapter *The mass–spring oscillator and the pendulum*).
**Formula:** $T = 2\pi\sqrt{\dfrac{m}{k}}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $T = 2\pi\sqrt{\dfrac{72.0\,\text{kg}}{120\,\text{N/m}}} = 2\pi \cdot 0.7746\,\text{s} = 4.867\,\text{s}$
**Answer:** $T \approx 4.87\,\text{s}$, three significant figures like the mass $72.0\,\text{kg}$. The result is an estimate, because the force of the rubber cord is not exactly harmonic and air resistance damps the oscillation.
**Reasonableness:** At the equilibrium position the cord is stretched by $\tfrac{706.32\,\text{N}}{120\,\text{N/m}} \approx 5.9\,\text{m}$. The period of a vertical spring is also $2\pi\sqrt{\tfrac{x_0}{g}} = 2\pi\sqrt{\tfrac{5.886\,\text{m}}{9.81\,\text{m/s}^2}} \approx 4.87\,\text{s}$, the same result. A slow bobbing of about five seconds suits a long, slack cord.

### Yleisiä virheitä
- In part b only $mgL_0$ is taken as the gravitational potential energy, so that the extension comes out as $\sqrt{\tfrac{2mgL_0}{k}} \approx 14.6\,\text{m}$; the weight also does work while the cord stretches.
- In part b the extension $21.6\,\text{m}$ is given as the answer instead of the depth below the bridge.
- In part c the acceleration is calculated as $\tfrac{kx}{m} \approx 36\,\text{m/s}^2$, forgetting the weight, or the acceleration is said to be zero because the speed is zero.
- In part d the pendulum formula is used with the length of the cord.

### Hyväksytään myös
- In part b the zero level at the bridge, when the signs of the potential energy are consistent.
- In part c the answer in the form $a \approx 2.7g$ upwards.
