## fy9-mittaaminen-s1

### a)
**Given:** distance $s = 100.0\,\text{m}$; Liisa's times $13.52\,\text{s}$, $13.90\,\text{s}$ and $13.71\,\text{s}$
**Find:** Liisa's average speed $v$ in the units $\text{m/s}$ and $\text{km/h}$
**Principle:** The average speed is the distance travelled divided by the time taken. The three watches measure the same run, so the best estimate of the time is their mean: in it the random errors partly cancel each other.
**Formula:** $\bar{t} = \dfrac{t_1 + t_2 + t_3}{3}$ and $v = \dfrac{s}{\bar{t}}$
**Conversions:** $1\,\tfrac{\text{m}}{\text{s}} = \dfrac{0.001\,\text{km}}{\tfrac{1}{3600}\,\text{h}} = 3.6\,\tfrac{\text{km}}{\text{h}}$
**Substitution:** $\bar{t} = \dfrac{13.52\,\text{s} + 13.90\,\text{s} + 13.71\,\text{s}}{3} = 13.71\,\text{s}$ and $v = \dfrac{100.0\,\text{m}}{13.71\,\text{s}} = 7.294\,\tfrac{\text{m}}{\text{s}} = 7.294 \cdot 3.6\,\tfrac{\text{km}}{\text{h}} = 26.26\,\tfrac{\text{km}}{\text{h}}$
**Answer:** $v \approx 7.29\,\text{m/s} \approx 26.3\,\text{km/h}$. Three significant figures: the watch readings differ from each other by tenths of a second, that is, by about one percent, so in the speed too only the hundredths of a metre per second are uncertain. (The uncertainty $0.12\,\text{m/s}$ of part b confirms this.)
**Reasonableness:** About $26\,\text{km/h}$ is a brisk sprinting speed for an upper secondary student. It is clearly below the roughly $36\,\text{km/h}$ of a top sprinter and clearly above the roughly $10\,\text{km/h}$ of jogging.

### b)
**Given:** $s = (100.0 \pm 0.3)\,\text{m}$; times $13.52\,\text{s}$, $13.90\,\text{s}$ and $13.71\,\text{s}$; from part a $\bar{t} = 13.71\,\text{s}$
**Find:** the uncertainty $\Delta v$ of the average speed and the speed with its uncertainty
**Principle:** The uncertainty of the time is estimated as half the range of the results of the three watches. The speed is largest when the distance is the longest and the time the shortest possible, and smallest the other way round. Half of the interval obtained in this way is taken as the uncertainty.
**Formula:** $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$, $v_\text{max} = \dfrac{s + \Delta s}{\bar{t} - \Delta t}$, $v_\text{min} = \dfrac{s - \Delta s}{\bar{t} + \Delta t}$ and $\Delta v = \dfrac{v_\text{max} - v_\text{min}}{2}$
**Conversions:** Not needed: the distance is in metres and the times in seconds.
**Substitution:** $\Delta t = \dfrac{13.90\,\text{s} - 13.52\,\text{s}}{2} = 0.19\,\text{s}$, $v_\text{max} = \dfrac{100.3\,\text{m}}{13.52\,\text{s}} = 7.419\,\tfrac{\text{m}}{\text{s}}$, $v_\text{min} = \dfrac{99.7\,\text{m}}{13.90\,\text{s}} = 7.173\,\tfrac{\text{m}}{\text{s}}$ and $\Delta v = \dfrac{7.419\,\tfrac{\text{m}}{\text{s}} - 7.173\,\tfrac{\text{m}}{\text{s}}}{2} = 0.123\,\tfrac{\text{m}}{\text{s}}$
**Answer:** $v = (7.29 \pm 0.12)\,\text{m/s}$. The first digit of the uncertainty is $1$, so it keeps two significant figures, and the speed is rounded to the same decimal place.
**Reasonableness:** The relative uncertainty of the time, $0.19 : 13.71 \approx 1.4\,\%$, is much larger than that of the distance, $0.3 : 100 = 0.3\,\%$, so the uncertainty of the speed comes almost entirely from the hand timing. About $0.2\,\text{s}$ is a typical uncertainty of a time taken by hand.

### c)
**Find:** whether the measurements can show that Liisa was faster than Mira
**Principle:** Two results are shown to differ only if their uncertainty intervals do not overlap. Overlapping intervals do not prove that the results are equal.
**Model answer:** Mira's mean is $$
\begin{aligned}
\bar{t} &= (13.80 + 14.12 + 13.96)\,\text{s} \\
&: 3 \\
&= 13.96\,\text{s}
\end{aligned}
$$ and the uncertainty $(14.12 - 13.80)\,\text{s} : 2 = 0.16\,\text{s}$, so Mira's time is $(13.96 \pm 0.16)\,\text{s}$ and Liisa's $(13.71 \pm 0.19)\,\text{s}$. Liisa's interval is $13.52$–$13.90\,\text{s}$ and Mira's $13.80$–$14.12\,\text{s}$, so the intervals overlap. The difference $0.25\,\text{s}$ is of the same order of magnitude as the uncertainties. So these measurements cannot show that Liisa was faster, although her mean is smaller. This does not, however, mean that the runners are equally fast: showing a difference would require more precise timing, for example a photo-finish camera.

### d)
**Find:** the systematic sources of error in hand timing, whether the direction of the error can be concluded for certain and why the mean does not necessarily remove a systematic error
**Principle:** A systematic error shifts every result in the same direction. It cannot be seen from the spread of the results, and repetition or the mean does not remove it. The effect of random error, on the other hand, usually decreases when the results are averaged.
**Model answer:** The timekeeper starts the watch only after seeing the flag drop and reacting to it. The watch therefore starts with a delay $\tau_\text{start}$, typically a few tenths of a second. Stopping the watch also has a delay $\tau_\text{stop}$. The timekeeper sees the finish coming, so this delay can be shorter, but the watch may also be stopped slightly too early or too late. The measured time is $t_\text{meas} = t_\text{true} + \tau_\text{stop} - \tau_\text{start}$, where $t_\text{true}$ is the true time. The measured time is thus shorter than the true time if $\tau_\text{start} > \tau_\text{stop}$, and longer if $\tau_\text{stop} > \tau_\text{start}$. The delays are not known from the information in the problem, so the direction cannot be concluded for certain. Most likely the start delay is larger, so the time is slightly too short and the speed in part a too large. The three timekeepers work in the same way, so the average part of the delays is in the same direction for all of them. It is a systematic error, and it remains in the mean as well. The mean usually reduces only the effect of random error, that is, the variation between the watches. The systematic error is removed, for example, by electronic timing that starts itself from the start signal.

### Hyväksytään myös
- In part b, the relative uncertainty of the speed as the sum of the relative uncertainties of the time and the distance: $\tfrac{0.19}{13.71} + \tfrac{0.3}{100.0} \approx 0.0169$, so $$
\begin{aligned}
\Delta v &\approx 0.0169 \cdot 7.294\,\text{m/s} \\
&\approx 0.12\,\text{m/s}
\end{aligned}
$$.
- In part b, the typical $0.2\,\text{s}$ of hand timing as the uncertainty of the time, when the choice is justified. Then $\Delta v \approx 0.1\,\text{m/s}$ and $v = (7.3 \pm 0.1)\,\text{m/s}$ are also accepted.
- In part d, a mention that a timekeeper $100\,\text{m}$ away who reacts to the sound of a starting pistol would start the watch even later, because sound travels the distance in about $0.3\,\text{s}$.
- In part d, a justified estimate of the direction of the error, for example that the measured time is probably shorter than the true time, when the answer states that the conclusion rests on an assumption about the sizes of the delays.

### Yleisiä virheitä
- One watch or the fastest time is used as the time instead of the mean.
- The speed is converted by multiplying or dividing the wrong way, for example $7.29 : 3.6 = 2.0\,\text{km/h}$; a reasonableness check reveals the error.
- The speed is given to calculator precision, $7.2939\,\text{m/s}$, or the uncertainty and the speed to different precisions.
- In part c, it is concluded from the difference of the means that Liisa was faster, or from the overlapping intervals that the runners were equally fast.
- In part d, the reaction time is said to cause only a random error; its average part is systematic.
- In part d, it is claimed as certain that the measured time is shorter or longer than the true time, although the direction depends on the difference between the start and stop delays.

## fy9-mittaaminen-s2

### a)
**Given:** height of the stack $h = 51\,\text{mm}$, its uncertainty $\Delta h = 1\,\text{mm}$, number of sheets $N = 500$
**Find:** the thickness $d$ of one sheet and its uncertainty $\Delta d$ in micrometres
**Principle:** The sheets are identical and the stack is measured once, so the thickness of one sheet is the height of the stack divided by the number of sheets. The same division also applies to the uncertainty of the height, because it is the uncertainty of one measurement.
**Formula:** $d = \dfrac{h}{N}$ and $\Delta d = \dfrac{\Delta h}{N}$
**Conversions:** $1\,\text{mm} = 1000\,\mu\text{m}$, so $51\,\text{mm} = 51 \cdot 1000\,\mu\text{m} = 51\,000\,\mu\text{m}$ and $1\,\text{mm} = 1000\,\mu\text{m}$.
**Substitution:** $d = \dfrac{51\,000\,\mu\text{m}}{500} = 102\,\mu\text{m}$ and $\Delta d = \dfrac{1000\,\mu\text{m}}{500} = 2\,\mu\text{m}$
**Answer:** $d = (102 \pm 2)\,\mu\text{m}$. The uncertainty is a one-significant-figure estimate, and the thickness is rounded to the same precision, to whole micrometres.
**Reasonableness:** A tenth of a millimetre is the thickness of ordinary copy paper: a sheet feels thin but not translucent. The relative uncertainty is $2 : 102 \approx 2\,\%$, the same as that of the height of the stack, $1 : 51$.

### b)
**Given:** mass of the paper $M = 2.49\,\text{kg}$, $N = 500$ sheets, dimensions of a sheet $a = 210\,\text{mm}$ and $b = 297\,\text{mm}$; label $80\,\text{g/m}^2$
**Find:** the measured grammage $\sigma$ in the unit $\text{g/m}^2$
**Principle:** Grammage is mass per unit area. The total area of all the sheets is the area of one sheet multiplied by the number of sheets, and its mass is the weighed mass.
**Formula:** $A = N \cdot ab$ and $\sigma = \dfrac{M}{A} = \dfrac{M}{N ab}$
**Conversions:** $a = 210\,\text{mm} = 210 \cdot 0.001\,\text{m} = 0.210\,\text{m}$, $b = 297 \cdot 0.001\,\text{m} = 0.297\,\text{m}$ and $M = 2.49\,\text{kg} = 2.49 \cdot 1000\,\text{g} = 2490\,\text{g}$
**Substitution:** $A = 500 \cdot 0.210\,\text{m} \cdot 0.297\,\text{m} = 31.185\,\text{m}^2$ and $\sigma = \dfrac{2490\,\text{g}}{31.185\,\text{m}^2} = 79.85\,\tfrac{\text{g}}{\text{m}^2}$
**Answer:** $\sigma \approx 79.8\,\text{g/m}^2$, three significant figures as in the mass $2.49\,\text{kg}$. The difference from the label $80\,\text{g/m}^2$ is less than $0.3\,\%$, so the label is correct to the precision of the scale.
**Reasonableness:** As an estimate, one A4 sheet is about $\tfrac{1}{16}\,\text{m}^2$, so $500$ sheets are about $31\,\text{m}^2$, and $31\,\text{m}^2 \cdot 80\,\text{g/m}^2 \approx 2.5\,\text{kg}$, which matches the weighed mass.

### c)
**Given:** from part a $d = 102\,\mu\text{m}$, from part b $\sigma = 79.85\,\text{g/m}^2$; density of water $1000\,\text{kg/m}^3$
**Find:** the density $\rho$ of the paper in the unit $\text{kg/m}^3$
**Principle:** Density is mass per volume. The paper has a uniform thickness, so a piece of paper of area $A$ has mass $\sigma A$ and volume $Ad$. The area cancels, so the density is obtained by dividing the grammage by the thickness.
**Formula:** $\rho = \dfrac{m}{V} = \dfrac{\sigma A}{A d} = \dfrac{\sigma}{d}$
**Conversions:** $\sigma = 79.85\,\text{g/m}^2 = 79.85 \cdot 0.001\,\text{kg/m}^2 = 0.07985\,\text{kg/m}^2$ and $d = 102\,\mu\text{m} = 102 \cdot 10^{-6}\,\text{m} = 1.02 \cdot 10^{-4}\,\text{m}$
**Substitution:** $\rho = \dfrac{0.07985\,\text{kg/m}^2}{1.02 \cdot 10^{-4}\,\text{m}} = 782.8\,\tfrac{\text{kg}}{\text{m}^3}$
**Answer:** $\rho \approx 780\,\text{kg/m}^3$, that is, $7.8 \cdot 10^{2}\,\text{kg/m}^3$, two significant figures, because the height of the stack, $51\,\text{mm}$, is a two-figure number. The density of the paper is about $0.78$ times the density of water.
**Reasonableness:** Paper is wood fibre with air between the fibres, so its density is of the same order as that of wood, a few hundred kilograms per cubic metre. The relative uncertainty is the same as that of the thickness, about $2\,\%$, that is, about $\pm 20\,\text{kg/m}^3$.

### d)
**Find:** whether measuring one sheet directly makes sense, and why the uncertainty of the height of the stack is larger than half the scale division
**Principle:** In a simple situation the uncertainty of a reading can be estimated as half the smallest scale division, but the measuring method and other sources of error also affect the total uncertainty of the measurement. The relative uncertainty tells whether the uncertainty is small compared with the result.
**Model answer:** One sheet is about $0.1\,\text{mm}$ thick, so the ruler would show the reading $0$ or $1\,\text{mm}$. The reading uncertainty $0.5\,\text{mm}$ would be about five times the thickness itself, about $500\,\%$ in relative terms, so the measurement would give no information at all. When the stack is measured, a reading uncertainty of the same size is shared by $500$ sheets, and the relative uncertainty is only about $2\,\%$. So the suggestion is a poor one.

The uncertainty of the height of the stack is larger than $0.5\,\text{mm}$, because reading the scale is not the only source of uncertainty. The edges of the stack are uneven, so the height depends on where it is measured, and the stack is compressed when the ruler is pressed against it. The scale division only tells the resolution of the ruler, not the uncertainty of the whole measurement.

### Hyväksytään myös
- In part c, the density of the whole stack: $$
\begin{aligned}
\rho &= \tfrac{M}{N a b d} \\
&= \tfrac{2.49\,\text{kg}}{31.185\,\text{m}^2 \cdot 1.02 \cdot 10^{-4}\,\text{m}} \\
&\approx 783\,\text{kg/m}^3
\end{aligned}
$$, or $\rho \approx 784\,\text{kg/m}^3$ calculated with the label of the pack, $80\,\text{g/m}^2$.
- In part a, the thickness in millimetres and the conversion at the end: $$
\begin{aligned}
d &= 51\,\text{mm} : 500 \\
&= 0.102\,\text{mm} \\
&= 102\,\mu\text{m}
\end{aligned}
$$.

### Yleisiä virheitä
- The uncertainty is not divided by the number of sheets, so the thickness of a sheet comes out as $(102 \pm 1000)\,\mu\text{m}$.
- Millimetres are converted to micrometres in the wrong direction: $$
\begin{aligned}
&51\,\text{mm} : 500 \\
&= 0.102\,\text{mm} \\
&= 0.000102\,\mu\text{m}
\end{aligned}
$$. In a smaller unit the number grows.
- The area is calculated in millimetres and converted to square metres with the factor $1000$, although $1\,\text{m}^2 = 10^{6}\,\text{mm}^2$.
- The density is given three or four significant figures, although the height of the stack is known only to two figures.

## fy9-mittaaminen-s3

### a)
**Find:** a graph of the measurement results
**Graph:** The horizontal axis gets the volume of the liquid $V\ (\text{ml})$, which the student chooses, and the vertical axis the measured total mass $m\ (\text{g})$. Here the vertical axis starts at $100\,\text{g}$, which is marked, and the horizontal axis at zero, so that the line can later be extended to the vertical axis.

<svg data-fig="s3-pisteet" viewBox="0 0 600 440" role="img" aria-label="Graph: the total mass m of the measuring cylinder and the liquid in grams as a function of the volume V of the liquid in millilitres. Horizontal axis 0–110 ml and vertical axis 100–220 g, with its starting value marked. Eight blue points form a rising row at the volumes 20–100 ml, and each has a horizontal uncertainty bar of ±1 ml. The point of the row 60 ml (60 ml; 183.4 g) is drawn as a hollow red circle: it is clearly above the others, at almost the same height as the point 70 ml." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="384" x2="129.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="384" x2="197" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="384" x2="264" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="384" x2="331.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="384" x2="398.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="384" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="357.5" x2="466" y2="357.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="330.5" x2="466" y2="330.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="304" x2="466" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="277.5" x2="466" y2="277.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="250.5" x2="466" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="224" x2="466" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="466" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170.5" x2="466" y2="170.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="144" x2="466" y2="144" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="117.5" x2="466" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="90.5" x2="466" y2="90.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="384" x2="480" y2="384" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,384 L479,390 L479,378 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="385" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="384" x2="129.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="197" y1="384" x2="197" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="211" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="264" y1="384" x2="264" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="278.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$60$</div></foreignObject>
  <line x1="331.5" y1="384" x2="331.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="345.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$80$</div></foreignObject>
  <line x1="398.5" y1="384" x2="398.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="390" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="466" y1="384" x2="466" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="357.5" x2="96" y2="357.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="330.5" x2="96" y2="330.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$120$</div></foreignObject>
  <line x1="89" y1="304" x2="96" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="277.5" x2="96" y2="277.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="259.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$140$</div></foreignObject>
  <line x1="89" y1="250.5" x2="96" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="224" x2="96" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="206" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$160$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="170.5" x2="96" y2="170.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="152.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$180$</div></foreignObject>
  <line x1="89" y1="144" x2="96" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="117.5" x2="96" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="99.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$200$</div></foreignObject>
  <line x1="89" y1="90.5" x2="96" y2="90.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="46" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$220$</div></foreignObject>
  <foreignObject x="498" y="366" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="4" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m\ (\text{g})$</div></foreignObject>
  <line x1="160" y1="283.5" x2="166.5" y2="283.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="163.5" cy="283.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="193.5" y1="262" x2="200.5" y2="262" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="197" cy="262" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="227" y1="235.5" x2="234" y2="235.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="230.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="261" y1="213.5" x2="267.5" y2="213.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="264" cy="213.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="328" y1="162.5" x2="335" y2="162.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="331.5" cy="162.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="361.5" y1="139" x2="368.5" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="365" cy="139" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="395.5" y1="112" x2="402" y2="112" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="398.5" cy="112" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="429" y1="90" x2="435.5" y2="90" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="432.5" cy="90" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="161.5" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="182" y="133.5" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$60\,\text{ml?}$</div></foreignObject>
  <foreignObject x="109.5" y="342" width="273" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\text{axis starts at } 100\,\text{g}$</div></foreignObject>
</svg>

**Model answer:** Both axes are evenly spaced, and the end of each axis has the quantity and the unit. The points fill most of the graph. Each point has a horizontal uncertainty bar of $\pm 1\,\text{ml}$; the resolution of the balance, $0.1\,\text{g}$, is so small that a vertical bar cannot be seen. The points are not joined to each other. The point of the row $60\,\text{ml}$ stands out at once: it is at almost the same height as the point of the row $70\,\text{ml}$, although the mass should grow evenly.

### b)
**Find:** the fitted model and how the row $60\,\text{ml}$ is dealt with
**Graph:** One straight line is fitted among the seven other points and the point $20\,\text{ml}$, and it is extended as a dashed line to the vertical axis. The grey dashed lines are the steepest and the shallowest line of part d.

<svg data-fig="s3-sovitus" viewBox="0 0 600 440" role="img" aria-label="Graph: the same data as above. One straight line is fitted among the eight reliable points and extended as a dashed line to the vertical axis; it crosses the axis at about 118.6 g, which is the mass of the empty measuring cylinder. The points (20 ml; 137.0 g) and (100 ml; 210.5 g), far apart and read from the line, are circled, so the slope is 0.919 g/ml. The grey dashed lines are the steepest and the shallowest line, with slopes 0.932 and 0.908 g/ml. The line passes the hollow point 60 ml at a distance of about 10 g." style="max-width:100%;font-size:30px">
  <line x1="129.5" y1="384" x2="129.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="384" x2="197" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="264" y1="384" x2="264" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="384" x2="331.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398.5" y1="384" x2="398.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="384" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="357.5" x2="466" y2="357.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="330.5" x2="466" y2="330.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="304" x2="466" y2="304" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="277.5" x2="466" y2="277.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="250.5" x2="466" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="224" x2="466" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="466" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170.5" x2="466" y2="170.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="144" x2="466" y2="144" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="117.5" x2="466" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="90.5" x2="466" y2="90.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="466" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="384" x2="480" y2="384" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M492,384 L479,390 L479,378 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="385" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="129.5" y1="384" x2="129.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="384" x2="163.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="144" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="197" y1="384" x2="197" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="230.5" y1="384" x2="230.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="211" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="264" y1="384" x2="264" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="298" y1="384" x2="298" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="278.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$60$</div></foreignObject>
  <line x1="331.5" y1="384" x2="331.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="365" y1="384" x2="365" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="345.5" y="390" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$80$</div></foreignObject>
  <line x1="398.5" y1="384" x2="398.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="432.5" y1="384" x2="432.5" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="390" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="466" y1="384" x2="466" y2="391" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="357.5" x2="96" y2="357.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="330.5" x2="96" y2="330.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="312.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$120$</div></foreignObject>
  <line x1="89" y1="304" x2="96" y2="304" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="277.5" x2="96" y2="277.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="259.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$140$</div></foreignObject>
  <line x1="89" y1="250.5" x2="96" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="224" x2="96" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="206" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$160$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="170.5" x2="96" y2="170.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="152.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$180$</div></foreignObject>
  <line x1="89" y1="144" x2="96" y2="144" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="117.5" x2="96" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="99.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$200$</div></foreignObject>
  <line x1="89" y1="90.5" x2="96" y2="90.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="46" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$220$</div></foreignObject>
  <foreignObject x="498" y="366" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="4" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m\ (\text{g})$</div></foreignObject>
  <polyline points="136.5,303.5 452.5,75.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="136.5,306 452.5,72.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="96,334.5 146.5,297.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <polyline points="146.5,297.5 452.5,74.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="160" y1="283.5" x2="166.5" y2="283.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="163.5" cy="283.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="193.5" y1="262" x2="200.5" y2="262" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="197" cy="262" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="227" y1="235.5" x2="234" y2="235.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="230.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="261" y1="213.5" x2="267.5" y2="213.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="264" cy="213.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="328" y1="162.5" x2="335" y2="162.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="331.5" cy="162.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="361.5" y1="139" x2="368.5" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="365" cy="139" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="395.5" y1="112" x2="402" y2="112" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="398.5" cy="112" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="429" y1="90" x2="435.5" y2="90" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="432.5" cy="90" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="161.5" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <circle cx="163.5" cy="285.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="432.5" cy="89.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="96" cy="334.5" r="9" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="109.5" y="346.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$m_0 \approx 118.6\,\text{g}$</div></foreignObject>
  <foreignObject x="120.5" y="83.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$k \approx 0.919\,\tfrac{\text{g}}{\text{ml}}$</div></foreignObject>
</svg>

**Model answer:** The points are approximately on a straight line, so the line $m = kV + b$ suits as the model. The line is not forced through the origin, because the balance also weighs the measuring cylinder: when there is no liquid, the mass is not zero. The point of the row $60\,\text{ml}$ is about $10\,\text{g}$ above the line, which is more than ten times the deviations of the other points. Its mass $183.4\,\text{g}$ would fit the line at a volume of about $70\,\text{ml}$, and according to the note the reading was written down afterwards from memory. A likely cause, a gross error, has thus been found for the deviation, so the point is left out of the fit. The omission and its reason are recorded in the report. The point should not have been removed just because it differs from the others; the best thing would be to repeat the measurement.

### c)
**Given:** the fitted line of part b
**Find:** the slope $k$ and the constant term $b$ of the line with their units, and their meaning
**Principle:** The balance weighs the measuring cylinder and the liquid: $m = \rho V + m_0$. The mass $m_0$ of the measuring cylinder does not change when liquid is added, so the change in mass comes only from the liquid. Therefore the slope is the density of the liquid and the constant term the mass of the empty measuring cylinder.
**Reading the graph:** Two points of the line far apart are read: $(V_1;\ m_1) = (20\,\text{ml};\ 137.0\,\text{g})$ and $(V_2;\ m_2) = (100\,\text{ml};\ 210.5\,\text{g})$.
**Formula:** $k = \dfrac{m_2 - m_1}{V_2 - V_1}$ and $b = m_1 - k V_1$
**Conversions:** $1\,\text{ml} = 1\,\text{cm}^3$, so $1\,\tfrac{\text{g}}{\text{ml}} = 1\,\tfrac{\text{g}}{\text{cm}^3}$.
**Substitution:** $k = \dfrac{210.5\,\text{g} - 137.0\,\text{g}}{100\,\text{ml} - 20\,\text{ml}} = \dfrac{73.5\,\text{g}}{80\,\text{ml}} = 0.919\,\tfrac{\text{g}}{\text{ml}}$ and $b = 137.0\,\text{g} - 0.919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 118.6\,\text{g}$
**Answer:** The slope $k \approx 0.919\,\text{g/cm}^3$ is the density of the liquid, and the constant term $b \approx 118.6\,\text{g}$ is the mass of the empty measuring cylinder. The slope has three significant figures, because the difference of the masses, $73.5\,\text{g}$, is read to three figures; the uncertainty of part d shows that the third figure is already uncertain.
**Reasonableness:** The mass of a $100\,\text{ml}$ glass measuring cylinder is typically about $100$–$200\,\text{g}$, and the density is smaller than that of water but larger than that of ethanol. According to the line, the mass on the row $20\,\text{ml}$ is $118.6\,\text{g} + 0.919\,\tfrac{\text{g}}{\text{ml}} \cdot 20\,\text{ml} = 137.0\,\text{g}$, which matches the measured $137.6\,\text{g}$.

### d)
**Given:** the graph of part b, where the points have uncertainty bars of $\pm 1\,\text{ml}$; from part c $k = 0.919\,\text{g/cm}^3$; the data-book densities $1.00$, $0.92$ and $0.79\,\text{g/cm}^3$
**Find:** the uncertainty of the density $\Delta\rho$ and the identification of the liquid
**Principle:** The steepest and the shallowest line that still pass through all the uncertainty bars bound the estimated range of the slope. Half of it is taken as the uncertainty, and the result is compared with the data-book densities.
**Reading the graph:** The slope of the steepest line is about $k_\text{max} = 0.932\,\text{g/cm}^3$ and that of the shallowest $k_\text{min} = 0.908\,\text{g/cm}^3$.
**Formula:** $\Delta\rho = \dfrac{k_\text{max} - k_\text{min}}{2}$
**Conversions:** Not needed: all the densities are in the unit $\text{g/cm}^3$.
**Substitution:** $\Delta\rho = \dfrac{0.932\,\text{g/cm}^3 - 0.908\,\text{g/cm}^3}{2} = 0.012\,\text{g/cm}^3$
**Answer:** $\rho = (0.919 \pm 0.012)\,\text{g/cm}^3$; the first digit of the uncertainty is $1$, so it has two figures, and the density is given to the same decimal place. The interval $0.907$–$0.931\,\text{g/cm}^3$ contains the density of cooking oil, $0.92\,\text{g/cm}^3$, but not that of water, $1.00$, or of ethanol, $0.79\,\text{g/cm}^3$. The liquid is probably cooking oil. The conclusion is not certain, since some other liquid may have the same density.
**Reasonableness:** The relative uncertainty is $0.012 : 0.919 \approx 1.3\,\%$, which fits the fact that the uncertainty of the volume reading, $1\,\text{ml}$, is about $1\,\%$ of the measured $80\,\text{ml}$ range. The difference from water, $0.08\,\text{g/cm}^3$, is many times the uncertainty.

### e)
**Given:** from part d $\rho = 0.919\,\text{g/cm}^3$; volume $V = 1.50\,\text{l}$
**Find:** the mass $m$ of the liquid and whether using the result is justified
**Principle:** Density is a property of the substance, so the mass of the same liquid is directly proportional to its volume: $m = \rho V$. The mass of the measuring cylinder does not belong to the liquid, so it is not added.
**Formula:** $m = \rho V$
**Conversions:** $V = 1.50\,\text{l} = 1.50 \cdot 1000\,\text{cm}^3 = 1500\,\text{cm}^3$, and finally $1000\,\text{g} = 1\,\text{kg}$.
**Substitution:** $m = 0.919\,\tfrac{\text{g}}{\text{cm}^3} \cdot 1500\,\text{cm}^3 = 1378\,\text{g} = 1.378\,\text{kg}$
**Answer:** $m \approx 1.38\,\text{kg}$. According to part d the density is known to about $1.3\,\%$, so the result is $(1.38 \pm 0.02)\,\text{kg}$ and the uncertainty reaches the third digit, as does the volume $1.50\,\text{l}$. The volume is $15$ times the measured range, but the calculation does not extend the line of the measuring cylinder; it uses the density, which is a property of the substance and stays the same at the same temperature. Therefore the result is physically justified, as long as the temperature of the oil is the same as in the measurement.
**Reasonableness:** The same volume of water would weigh $1.50\,\text{kg}$, and oil is about $8\,\%$ lighter, so $1.38\,\text{kg}$ has the right size.

### Hyväksytään myös
- In part c, a calculator or spreadsheet fit of a straight line without the row $60\,\text{ml}$: $k = 0.918\,\text{g/cm}^3$ and $b = 118.6\,\text{g}$. Slopes $0.90$–$0.94\,\text{g/cm}^3$ and constant terms $117.5$–$119.5\,\text{g}$ are accepted.
- In part b, keeping the row $60\,\text{ml}$, when its effect is checked: the slope does not change, because the point is in the middle of the measured range, but the constant term grows by about $1\,\text{g}$. The solution must be justified.
- In part d, $\Delta\rho = 0.01$–$0.02\,\text{g/cm}^3$ obtained from limit lines drawn by eye.

### Yleisiä virheitä
- The density is calculated by dividing the mass of some row by the volume, for example $$
\begin{aligned}
&210.3\,\text{g} : 100\,\text{ml} \\
&= 2.10\,\text{g/cm}^3
\end{aligned}
$$. The mass includes the measuring cylinder.
- The line is forced through the origin, so the slope comes out too large and the liquid is identified wrongly.
- The point of the row $60\,\text{ml}$ is removed without stating a reason, or because of it the points are joined with a broken line.
- The slope is read from two adjacent measurement points.
- In part e, the mass of the measuring cylinder is added to the mass, or the line of the measuring cylinder is extended to $1500\,\text{ml}$, which adds an extra $119\,\text{g}$ to the result.

## fy9-mittaaminen-s4

### a)
**Find:** the types of error seen in the data, with justifications
**Principle:** A systematic error shifts the results in the same direction, a random error shows as variation between repetitions, and a gross error as a single result clearly different from the others.
**Model answer:** *Systematic error.* Every reading is larger than the known mass of the weight, and the difference repeats in the same way in every weighing. The means of the readings are about $101.7$, $204.3$, $510.3$ and $1020.3\,\text{g}$, so the error is about $2$, $4$, $10$ and $20\,\text{g}$. The error grows in the same proportion as the mass, about $2\,\%$: $20\,\text{g} : 1000\,\text{g} = 0.02$. Because the empty scale shows $0\,\text{g}$, the zero point is right and the error is relative.

*Random error.* The three readings of the same weight differ from each other by at most $1\,\text{g}$. The variation is of the same order of magnitude as the display resolution $1\,\text{g}$.

*Gross error.* No reading differs clearly from the other readings of the same weight, so no gross error can be seen.

### b)
**Find:** whether the claim $(765 \pm 0.5)\,\text{g}$ is right, and a better estimate of the mass of the flour
**Principle:** The resolution is the smallest change shown on the display. It says nothing about systematic error, so the uncertainty can be much larger than the resolution. A known systematic error is corrected.
**Model answer:** The claim does not hold. Half the resolution, $0.5\,\text{g}$, only tells how precisely the display can be read. According to part a, the scale shows about $2\,\%$ too much, and the repetitions vary by about $1\,\text{g}$. The scale shows $m_\text{reading} = k\,m$ for a mass $m$, where $k$ is the ratio given by the weights, $1020\,\text{g} : 1000\,\text{g} = 1.02$. The corrected mass is therefore $$
\begin{aligned}
m &= \dfrac{m_\text{reading}}{k} \\
&= 765\,\text{g} : 1.02 \\
&= 750\,\text{g}
\end{aligned}
$$. The uncertainty is increased by the variation of the repetitions and by the fact that the correction factor is known only to about a thousandth, which makes less than a gram in the reading $765\,\text{g}$. A better estimate is about $(750 \pm 2)\,\text{g}$. So the friend's result is about $15\,\text{g}$ too large, and its uncertainty is too small.

### c)
**Find:** the shape of the graph, what it shows about the kind of error, and why repetition does not help
**Principle:** If the scale were right, the reading would be the same as the mass of the weight, and the points would be on a line with slope $1$ and constant term $0$. A zero error would show in the constant term and a relative error in the slope.
**Model answer:** The points are on a straight line through the origin: the reading is directly proportional to the mass of the weight, $m_\text{reading} \propto m_\text{weight}$. The slope $k = \dfrac{\Delta m_\text{reading}}{\Delta m_\text{weight}}$ is read from the fitted line at two points far apart, the points at $100.0\,\text{g}$ and $1000.0\,\text{g}$ (all points are on the line): $$
\begin{aligned}
k &= (1020.3\,\text{g} - 101.7\,\text{g}) \\
&: (1000.0\,\text{g} - 100.0\,\text{g}) \\
&\approx 1.02
\end{aligned}
$$ and not $1$, and the constant term is zero. A constant term of zero tells that the zero point is right, and the slope $1.02$ tells that the scale shows $2\,\%$ too much for every mass. The points of the graph are very precisely on the line, because the random variation, about $1\,\text{g}$, is small.

Repetition reduces the effect of random error in the mean, because readings that are too large and too small partly cancel each other. A systematic error, however, is the same in every weighing, so the mean is just as wrong as a single reading. The error is corrected by dividing the readings by the slope $1.02$ or by calibrating the scale with a weight.

### Yleisiä virheitä
- All the deviations are taken as random because they are small; they are, however, all in the same direction.
- The error is taken as a constant $2\,\text{g}$, and the correction subtracts $2\,\text{g}$ from the reading; the error is relative.
- The display resolution is taken as the uncertainty of the measurement.
- The correction is made in the wrong direction, $765\,\text{g} \cdot 1.02 = 780\,\text{g}$.

## fy9-mittaaminen-s5

### a)
**Find:** the shortcomings of the report and why each weakens the result
**Principle:** A model is fitted to the measurement points, and its choice is justified physically. The slope is read from the fitted line, a deviating point is checked before it is left out, and the result is stated with its uncertainty.
**Model answer:**
- *A broken line.* A line joining the points also follows the measurement errors, and it is not a model. In uniform motion the position changes evenly, so one straight line is fitted to the points.
- *Speed from two adjacent points.* The marking error of each point affects the result fully: if each position can be $0.03\,\text{m}$ wrong, the speed can be $0.12\,\text{m/s}$ wrong. That is why the result $0.42\,\text{m/s}$ is uncertain.
- *A line through the origin.* The timing began when the car was already moving, at about $0.35\,\text{m}$, so the position is not zero at the moment $t = 0$. The forced line is too steep, and the slope $0.63\,\text{m/s}$ is too large.
- *A point was removed without a reason.* The point deviates by about $0.25\,\text{m}$, which is a lot. The reason should have been checked from the video, for example whether the car was marked in the wrong frame, and the omission recorded with its reason.
- *The result and the conclusion.* The result has four significant figures and no uncertainty, and the result was chosen by what felt suitable, not on the basis of the method.

### b)
**Find:** the speed of the toy car with its uncertainty, and how the point $t = 1.5\,\text{s}$ is dealt with
**Graph:** The horizontal axis has the time $t\ (\text{s})$ and the vertical axis the position $x\ (\text{m})$. The points have uncertainty bars of $\pm 0.03\,\text{m}$, which is an estimate of the precision of marking from the video.

<svg data-fig="s5-kuvaaja" viewBox="0 0 600 410" role="img" aria-label="Graph: the position x of a toy car in metres as a function of the time t in seconds, 0–3.0 s. Six blue points are close to one rising straight line; the position uncertainty ±0.03 m is smaller than the size of a point, so the uncertainty bars stay inside the points. The point (1.5 s; 1.32 m) is drawn as a hollow red circle: it is about 0.25 m above the line. The line crosses the vertical axis at 0.36 m, not at the origin, and its slope is 0.48 m/s. The points (0 s; 0.36 m) and (3.0 s; 1.79 m) read from the line are circled." style="max-width:100%;font-size:30px">
  <line x1="142" y1="360" x2="142" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200.5" y1="360" x2="200.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258.5" y1="360" x2="258.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317" y1="360" x2="317" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="360" x2="375" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="433.5" y1="360" x2="433.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="270" x2="480" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="180" x2="480" y2="180" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="90" x2="480" y2="90" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="360" x2="494" y2="360" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,360 L493,366 L493,354 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="361" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="142" y1="360" x2="142" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="114.5" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0.5$</div></foreignObject>
  <line x1="200.5" y1="360" x2="200.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="188.5" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="258.5" y1="360" x2="258.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="231" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1.5$</div></foreignObject>
  <line x1="317" y1="360" x2="317" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="305" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="375" y1="360" x2="375" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="347.5" y="366" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2.5$</div></foreignObject>
  <line x1="433.5" y1="360" x2="433.5" y2="367" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="421.5" y="366" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="77" y1="270" x2="84" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="252" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0.6$</div></foreignObject>
  <line x1="77" y1="180" x2="84" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="162" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1.2$</div></foreignObject>
  <line x1="77" y1="90" x2="84" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="72" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1.8$</div></foreignObject>
  <foreignObject x="50" y="362" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="512" y="342" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="84,306.5 468.5,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="84" y1="312" x2="84" y2="303" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="84" cy="307.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="142" y1="273" x2="142" y2="264" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="142" cy="268.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="200.5" y1="240" x2="200.5" y2="231" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="200.5" cy="235.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="317" y1="169.5" x2="317" y2="160.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="317" cy="165" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="375" y1="129" x2="375" y2="120" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="375" cy="124.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="433.5" y1="97.5" x2="433.5" y2="88.5" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="433.5" cy="93" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="258.5" cy="162" r="6.5" fill="#ffffff" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="127.5" y="130" width="117" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$\text{check it}$</div></foreignObject>
  <circle cx="84" cy="306" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="433.5" cy="91.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="258.5" y="274.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$v = k \approx 0.48\,\tfrac{\text{m}}{\text{s}}$</div></foreignObject>
</svg>

**Model answer:** Six points are close to one straight line, so the car moved uniformly and the position is a linear function of time, $x = vt + x_0$. The speed is the slope of the line, $v = \dfrac{x_2 - x_1}{t_2 - t_1}$. The point $t = 1.5\,\text{s}$ is about $0.25\,\text{m}$ above the line, almost at the same position as the point $t = 2.0\,\text{s}$, so it has probably been marked in the wrong frame. The point is checked from the video. If an error is found, it is corrected, or the point is left out and the reason recorded.

The line is not forced through the origin. Two points of it far apart are read, $(0\,\text{s};\ 0.36\,\text{m})$ and $(3.0\,\text{s};\ 1.79\,\text{m})$, so the speed is $$
\begin{aligned}
v &= \dfrac{1.79\,\text{m} - 0.36\,\text{m}}{3.0\,\text{s} - 0\,\text{s}} \\
&= 0.477\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
$$. The constant term $0.36\,\text{m}$ is the position of the car when the timing began. The steepest and the shallowest line through all the bars give slopes of about $0.492$ and $0.464\,\text{m/s}$, so $$
\begin{aligned}
\Delta v &= (0.492 - 0.464)\,\text{m/s} \\
&: 2 \\
&= 0.014\,\text{m/s}
\end{aligned}
$$.

The result is $v = (0.477 \pm 0.014)\,\text{m/s}$, when the uncertainty keeps two figures because its first digit is $1$. The result agrees with the report's two-point value $0.42\,\text{m/s}$ only thanks to that value's large uncertainty, but not with the value of the line forced through the origin, $0.63\,\text{m/s}$.

### c)
**Find:** two justified improvements, one of which concerns a systematic error
**Principle:** The effect of random error is reduced by adding measurements and by lengthening the measured interval. A systematic error is revealed only by comparing with a known value or with another method.
**Model answer:** *Checking the scale.* If the measuring tape is closer to the camera than the car, or the camera films at an angle, a metre in the video is not a metre on the car's path. Then all the positions and the speed are wrong in the same proportion, and the error does not show in the spread of the points. The measuring tape is placed on the car's path, the camera perpendicular to the motion and far enough away, and the scale is checked by measuring some other known length from the video.

*More and longer data.* When the car is filmed over a longer distance and the position is marked, for example, every $0.1\,\text{s}$, the slope is determined from more points and over a longer interval. Then the marking error of one point matters less, and the difference between the steepest and the shallowest line gets smaller. Repeated runs also tell whether the speed of the car varies from run to run.

### Hyväksytään myös
- In part b, a calculator or spreadsheet fit of a straight line without the point $1.5\,\text{s}$: $v = 0.477\,\text{m/s}$ and constant term $0.358\,\text{m}$. Speeds $0.46$–$0.50\,\text{m/s}$ are accepted.
- In part b, keeping the point, when its effect is checked: the point is in the middle of the measured range, so the slope does not change, but the points are no longer on the line within their uncertainties.
- In part b, the uncertainty $\pm 0.02\,\text{m/s}$ and the result $(0.48 \pm 0.02)\,\text{m/s}$.

### Yleisiä virheitä
- Shortcomings of the report are named without justifying why they weaken the result.
- Removing a deviating point is considered always wrong or always right; what matters is whether a reason is found for the deviation and whether it is recorded.
- In part b, the line is forced through the origin or the speed is calculated from one point as $x : t$.
- In part c, only "more precise measuring" is suggested without saying what is done and why it helps.

## fy9-mittaaminen-s6

### a)
**Find:** whether the pressure is inversely proportional to the syringe reading $V$
**Principle:** If $p$ is inversely proportional to the quantity $V$, the product $pV$ is constant. The claim is tested by calculating the product on different rows and seeing whether it varies randomly or changes systematically in the same direction.
**Model answer:** On the first row $$
\begin{aligned}
pV &= 189.1\,\text{kPa} \cdot 12\,\text{ml} \\
&= 2269\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$ and on the last $$
\begin{aligned}
&81.8\,\text{kPa} \cdot 30\,\text{ml} \\
&= 2454\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$. The products of the rows in between grow steadily row by row, and the total growth is $(2454 - 2269) : 2269 \approx 8\,\%$. The pressures are given to a tenth of a kilopascal, and the product grows in the same direction on every row. A random error would vary haphazardly, so the steady growth of $8\,\%$ is not caused by it. So the claim does not hold for the syringe reading $V$. The growth of the product suggests that the true volume of the air is larger than the reading: part of the air is in the tube and the sensor, and its share is largest when the volume of the syringe is small.

### b)
**Find:** a graph in which the relationship is linear, and a straight line fitted to it
**Graph:** The true volume of the air is $V + V_0$. When the temperature and the amount of air stay the same, according to Boyle's law $p(V + V_0) = C$, so $V = C \cdot \tfrac{1}{p} - V_0$. The horizontal axis is therefore given $\tfrac{1}{p}$ and the vertical axis $V$. For example, on the first row $$
\begin{aligned}
&\tfrac{1}{p} \\
&= \tfrac{1}{189.1\,\text{kPa}} \\
&= \tfrac{1}{0.1891\,\text{MPa}} \\
&= 5.29\,\tfrac{1}{\text{MPa}}
\end{aligned}
$$ and on the last $12.2\,\tfrac{1}{\text{MPa}}$.

<svg data-fig="s6-kuvaaja" viewBox="0 0 600 440" role="img" aria-label="Graph: the volume V on the syringe scale in millilitres as a function of the reciprocal of the pressure 1/p in the unit 1/MPa. Ten blue points between 5.3 and 12.2 1/MPa are on one rising straight line. The line is extended as a dashed line to the vertical axis, which it crosses on the negative side at −1.8 ml. The slope is 2.60 MPa · ml. The horizontal axis is drawn at V = 0." style="max-width:100%;font-size:30px">
  <line x1="132" y1="400" x2="132" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="400" x2="180" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228" y1="400" x2="228" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="400" x2="276" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="400" x2="324" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="372" y1="400" x2="372" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="400" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="369" x2="420" y2="369" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="307.5" x2="420" y2="307.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="276.5" x2="420" y2="276.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="245.5" x2="420" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="214.5" x2="420" y2="214.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="183.5" x2="420" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="152.5" x2="420" y2="152.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="122" x2="420" y2="122" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="91" x2="420" y2="91" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="400" x2="84" y2="338" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="83" y1="338" x2="434" y2="338" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,338 L433,344 L433,332.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="339" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="132" y1="338" x2="132" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="180" y1="338" x2="180" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="168" y="298" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="228" y1="338" x2="228" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="276" y1="338" x2="276" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="264" y="298" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="324" y1="338" x2="324" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="372" y1="338" x2="372" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352.5" y="298" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$12$</div></foreignObject>
  <line x1="420" y1="338" x2="420" y2="345" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="400" x2="84" y2="400" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="382" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$-8$</div></foreignObject>
  <line x1="77" y1="369" x2="84" y2="369" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="338" x2="84" y2="338" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="307.5" x2="84" y2="307.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="276.5" x2="84" y2="276.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="258.5" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="77" y1="245.5" x2="84" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="214.5" x2="84" y2="214.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="196.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$16$</div></foreignObject>
  <line x1="77" y1="183.5" x2="84" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="152.5" x2="84" y2="152.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="134.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$24$</div></foreignObject>
  <line x1="77" y1="122" x2="84" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="91" x2="84" y2="91" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="33" y="73" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$32$</div></foreignObject>
  <line x1="77" y1="60" x2="84" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="452" y="320" width="106" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\tfrac{1}{p}\ (\tfrac{1}{\text{MPa}})$</div></foreignObject>
  <foreignObject x="74" y="0" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$V\ (\text{ml})$</div></foreignObject>
  <polyline points="84,352 194.5,259.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <polyline points="194.5,259.5 405.5,82.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="211" cy="245.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="230" cy="230" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="247.5" cy="214.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="266" cy="199" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="285.5" cy="183.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="303" cy="168" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="321" cy="152.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="340.5" cy="137.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="358" cy="122" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="377.5" cy="106.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="84" cy="352" r="9" fill="none" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="104" y="360.5" width="180" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$-V_0 \approx -1.8\,\text{ml}$</div></foreignObject>
  <foreignObject x="96" y="80.5" width="195" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$k \approx 2.6\,\text{MPa} \cdot \text{ml}$</div></foreignObject>
</svg>

**Model answer:** The points lie well on a straight line, so the model $p(V + V_0) = C$ fits the data. The line does not pass through the origin: it is extended to the vertical axis, which it crosses on the negative side. If there were no air in the tube, the line would pass through the origin. The unit $\tfrac{1}{\text{MPa}}$ has been chosen so that the numbers on the axis are easy to read.

### c)
**Given:** the line of part b; $T = 22\,{}^\circ\text{C}$; $R = 8.314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}}$
**Find:** the air volume $V_0$ of the tube and the sensor and the amount of substance $n$ of the air
**Principle:** The equation of the line is $V = C \cdot \tfrac{1}{p} - V_0$, so the constant term is $-V_0$ and the slope $C = p(V + V_0)$. According to the ideal gas law $p(V + V_0) = nRT$, so the amount of substance is obtained from the slope. In the ideal gas law the temperature is in kelvins.
**Reading the graph:** The line crosses the vertical axis at $-1.8\,\text{ml}$. Two points of the line far apart are read, $(4.0\,\tfrac{1}{\text{MPa}};\ 8.6\,\text{ml})$ and $(12.0\,\tfrac{1}{\text{MPa}};\ 29.5\,\text{ml})$.
**Formula:** $V_0 = -b$, $C = \dfrac{\Delta V}{\Delta (1/p)}$ and $C = nRT$, so $n = \dfrac{C}{RT}$
**Conversions:** $$
\begin{aligned}
&1\,\text{MPa} \cdot \text{ml} \\
&= 10^{6}\,\text{Pa} \cdot 10^{-6}\,\text{m}^3 \\
&= 1\,\text{Pa} \cdot \text{m}^3 \\
&= 1\,\text{J}
\end{aligned}
$$ and $T = (22 + 273.15)\,\text{K} = 295.15\,\text{K}$
**Substitution:** $V_0 = 1.8\,\text{ml}$, $C = \dfrac{29.5\,\text{ml} - 8.6\,\text{ml}}{12.0\,\tfrac{1}{\text{MPa}} - 4.0\,\tfrac{1}{\text{MPa}}} = 2.61\,\text{MPa} \cdot \text{ml} = 2.61\,\text{J}$ and $n = \dfrac{2.61\,\text{J}}{8.314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}} \cdot 295.15\,\text{K}} = 1.06 \cdot 10^{-3}\,\text{mol}$
**Answer:** $V_0 \approx 1.8\,\text{ml}$ and $n \approx 1.06 \cdot 10^{-3}\,\text{mol}$. The volume has two significant figures, because it is read from the graph to about $0.1\,\text{ml}$; the amount of substance has three, as the slope does.
**Reasonableness:** At normal pressure and room temperature a mole of gas takes up about $24\,\text{l}$, so about $26\,\text{ml}$ of air is about $26\,\text{ml} : 24\,000\,\text{ml/mol} \approx 1.1 \cdot 10^{-3}\,\text{mol}$. An air space of a few millilitres in the tube and the sensor is plausible for a short tube. When $V_0$ is added, the product $p(V + V_0)$ is $$
\begin{aligned}
&189.1\,\text{kPa} \cdot 13.8\,\text{ml} \\
&= 2610\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$ on the first row and $$
\begin{aligned}
&81.8\,\text{kPa} \cdot 31.8\,\text{ml} \\
&= 2601\,\text{kPa} \cdot \text{ml}
\end{aligned}
$$ on the last, that is, almost constant.

### d)
**Find:** the assumptions of the result and their effect
**Principle:** The model $p(V + V_0) = nRT$ assumes that the amount and the temperature of the air stay the same and that the whole volume has been measured. For each assumption we consider in which direction the result would change if it did not hold.
**Model answer:** *The temperature stays the same.* Compressing is work that increases the internal energy of the air. When the plunger is pushed slowly, the air has time to give off the heat through the walls of the syringe and stays at room temperature. In a fast compression the air would warm up, the pressure would momentarily be larger than the model gives, and the product $p(V + V_0)$ would grow during the compression.

*No air leaks.* If air leaked past the plunger at high pressure, the amount of substance would decrease during the measurement, and the product $p(V + V_0)$ would decrease at small volumes.

*The whole volume is included.* Without $V_0$ the product $pV$ would seem to grow with the volume, and one could wrongly conclude from the data that Boyle's law does not hold. The amount of substance would also be calculated from the wrong volume.

*Conclusion.* When $V_0 = 1.8\,\text{ml}$ is added to the reading, $p(V + V_0)$ is about $2600\,\text{kPa} \cdot \text{ml}$ over the whole measured range, with less than half a percent of variation. So the data agree with the model, which supports the view that the assumptions held.

### Hyväksytään myös
- In part b, a $(\tfrac{1}{p}, V)$ graph in the unit $\tfrac{1}{\text{kPa}}$, in which case the slope is $2600\,\text{kPa} \cdot \text{ml} = 2.60\,\text{J}$.
- In parts b and c, a calculator or spreadsheet fit: $C = 2.603\,\text{J}$ and $V_0 = 1.77\,\text{ml}$. The values $V_0 = 1.5$–$2.1\,\text{ml}$ and $n = (1.01$–$1.11) \cdot 10^{-3}\,\text{mol}$ are accepted.
- In part c, the amount of substance from one row, when $V_0$ has been added: $$
\begin{aligned}
n &= \tfrac{101.2\,\text{kPa} \cdot 25.8\,\text{ml}}{RT} \\
&\approx 1.06 \cdot 10^{-3}\,\text{mol}
\end{aligned}
$$.

### Yleisiä virheitä
- In part a, $pV$ is said to be "almost constant" without looking at the direction in which the product changes row by row, so the systematic growth goes unnoticed.
- In part b, a $(\tfrac{1}{V}, p)$ graph is drawn and the line is forced through the origin; the air space of the tube then does not show.
- In part c, the temperature is substituted in degrees Celsius, or the volume in millilitres and the pressure in kilopascals without conversion, so the amount of substance is wrong by a factor of a thousand.
- In part d, assumptions are listed without saying in which direction they would change the result.

## fy9-mittaaminen-s7

### a)
**Given:** the ruler of the picture, whose smallest scale division is $1\,\text{mm}$; the left end of the rod is at $2.0\,\text{cm}$ and the right end at $13.6\,\text{cm}$
**Find:** the length $l$ of the rod
**Principle:** The length is the difference of the positions of the ends of the rod on the ruler. The rod does not start at the zero of the ruler, so the reading of the right-hand end alone is not the length (chapter *Quantities, units and the SI system*).
**Reading the graph:** The ends of the rod are read from the millimetre scale: the left end $2.0\,\text{cm}$ and the right end $13.6\,\text{cm}$.
**Formula:** $l = x_\text{right} - x_\text{left}$
**Conversions:** None needed: both readings are in centimetres.
**Substitution:** $$
\begin{aligned}
l &= 13.6\,\text{cm} - 2.0\,\text{cm} \\
&= 11.6\,\text{cm}
\end{aligned}
$$
**Answer:** $l = 11.6\,\text{cm}$, three significant figures like the values read.
**Reasonableness:** The length of the rod is smaller than the $15\,\text{cm}$ of the ruler. If only the right-hand reading $13.6\,\text{cm}$ were taken as the length, it would be $2.0\,\text{cm}$, about $17\,\%$, too large, because the rod does not start at the zero of the ruler.

### b)
**Given:** the readings $2.0\,\text{cm}$ and $13.6\,\text{cm}$, scale division $1\,\text{mm}$; $l = 11.6\,\text{cm}$ from part a
**Find:** the uncertainty $\Delta l$ of the length, the length with its uncertainty and the relative uncertainty
**Principle:** The uncertainty of one reading is half of the scale division. The length is the difference of two readings, so in the worst case both readings are wrong in opposite directions and the uncertainties add.
**Formula:** $\Delta l = \Delta x_\text{right} + \Delta x_\text{left}$ and the relative uncertainty $\dfrac{\Delta l}{l}$
**Conversions:** $1\,\text{mm} = 0.1\,\text{cm}$, so the uncertainty of a reading, $0.5\,\text{mm}$, is $0.05\,\text{cm}$.
**Substitution:** $$
\begin{aligned}
\Delta x &= 0.5\,\text{mm} \\
&= 0.5 \cdot 0.1\,\text{cm} \\
&= 0.05\,\text{cm}
\end{aligned}
$$ $$
\begin{aligned}
\Delta l &= 0.05\,\text{cm} + 0.05\,\text{cm} \\
&= 0.10\,\text{cm}
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta l}{l} &= \dfrac{0.10\,\text{cm}}{11.6\,\text{cm}} \\
&= 0.0086 \\
&\approx 0.9\,\%
\end{aligned}
$$
**Answer:** $l = (11.6 \pm 0.1)\,\text{cm}$ and the relative uncertainty about $0.9\,\%$. The uncertainty is given with one digit and the length to the same decimal.
**Reasonableness:** An uncertainty of $1\,\text{mm}$ equals one small division of the ruler, which fits reading the ends by eye from the scale. The uncertainty of the difference of two readings is larger than that of one reading ($0.5\,\text{mm}$).

### c)
**Given:** $m = (15.7 \pm 0.05)\,\text{g}$, $d = (8.0 \pm 0.05)\,\text{mm}$ and $l = (11.6 \pm 0.1)\,\text{cm}$; the uncertainty is half of the resolution
**Find:** the density $\rho$ with its uncertainty in $\text{kg/m}^3$ and the measurement that affects the uncertainty the most
**Principle:** Density is mass divided by volume (chapter *Density*). The rod is a cylinder, so the volume is the cross-sectional area times the length. When the result is a product or a quotient, the relative uncertainties add, and the power $d^2$ doubles the relative uncertainty of the diameter.
**Formula:** $\rho = \dfrac{m}{V}$ and $V = \dfrac{\pi d^2}{4}\,l$, so $\rho = \dfrac{4m}{\pi d^2 l}$. Uncertainty: $\dfrac{\Delta\rho}{\rho} = \dfrac{\Delta m}{m} + 2\,\dfrac{\Delta d}{d} + \dfrac{\Delta l}{l}$
**Conversions:** $d = 8.0\,\text{mm} = 0.80\,\text{cm}$ and $\Delta d = 0.05\,\text{mm}$. Unit of density: $1\,\text{g} = 10^{-3}\,\text{kg}$ and $1\,\text{cm}^3 = 10^{-6}\,\text{m}^3$, so $1\,\text{g/cm}^3 = 1000\,\text{kg/m}^3$.
**Substitution:** Volume: $$
\begin{aligned}
V &= \dfrac{\pi d^2}{4}\,l \\
&= \dfrac{\pi \cdot (0.80\,\text{cm})^2}{4} \cdot 11.6\,\text{cm} \\
&= 0.503\,\text{cm}^2 \cdot 11.6\,\text{cm} \\
&= 5.83\,\text{cm}^3
\end{aligned}
$$ Density: $$
\begin{aligned}
\rho &= \dfrac{m}{V} \\
&= \dfrac{15.7\,\text{g}}{5.83\,\text{cm}^3} \\
&= 2.69\,\text{g/cm}^3 \\
&= 2.69 \cdot \dfrac{10^{-3}\,\text{kg}}{10^{-6}\,\text{m}^3} \\
&= 2.69 \cdot 10^3\,\text{kg/m}^3
\end{aligned}
$$ Relative uncertainties: $$
\begin{aligned}
\dfrac{\Delta m}{m} &= \dfrac{0.05\,\text{g}}{15.7\,\text{g}} \\
&= 0.0032
\end{aligned}
$$ $$
\begin{aligned}
2\,\dfrac{\Delta d}{d} &= 2 \cdot \dfrac{0.05\,\text{mm}}{8.0\,\text{mm}} \\
&= 0.0125
\end{aligned}
$$ and for the length $\dfrac{\Delta l}{l} = 0.0086$ from part b. Together: $$
\begin{aligned}
\dfrac{\Delta\rho}{\rho} &= 0.0032 \\
&\quad + 0.0125 \\
&\quad + 0.0086 \\
&= 0.0243 \\
&\approx 2.4\,\%
\end{aligned}
$$ Uncertainty: $$
\begin{aligned}
\Delta\rho &= 0.0243 \cdot 2693\,\text{kg/m}^3 \\
&= 65\,\text{kg/m}^3
\end{aligned}
$$
**Answer:** $\rho = (2.69 \pm 0.07) \cdot 10^3\,\text{kg/m}^3$. The uncertainty is rounded to one digit ($65 \to 0.07 \cdot 10^3$) and the result to the same decimal. The diameter affects the uncertainty the most: its share is $1.25\,\%$, that of the length $0.9\,\%$ and that of the mass $0.3\,\%$. The diameter dominates because the resolution $0.1\,\text{mm}$ is large compared with $8.0\,\text{mm}$ (relative uncertainty $0.6\,\%$) and the square doubles it; without the square the length would be the largest.
**Reasonableness:** A density of $2.7\,\text{g/cm}^3$ means that the mass of the rod is $2.7$ times that of the same volume of water (the density of water is $1.0 \cdot 10^3\,\text{kg/m}^3$), which fits a light metal. The total uncertainty $2.4\,\%$ is of the same order as the single shares.

### d)
**Find:** whether the result agrees with the table value of aluminium and whether the rod can be concluded to be aluminium from the density
**Principle:** The result and the table value agree if the table value is inside the uncertainty interval of the result. The mere difference of the numbers tells nothing without the uncertainty.
**Model answer:** The interval of the result is $$
\begin{aligned}
\rho_\text{min} &= 2693\,\text{kg/m}^3 \\
&\quad - 65\,\text{kg/m}^3 \\
&= 2628\,\text{kg/m}^3 \\
\rho_\text{max} &= 2693\,\text{kg/m}^3 \\
&\quad + 65\,\text{kg/m}^3 \\
&= 2758\,\text{kg/m}^3
\end{aligned}
$$ that is $2.63 \cdot 10^3 \ldots 2.76 \cdot 10^3\,\text{kg/m}^3$. The table value of aluminium is $2.70 \cdot 10^3\,\text{kg/m}^3$ ([MAFY table](https://mafytaulukot.fi/d67c966e-4e50-48d3-beae-9ae0a5f7838c/fi/1787666412/theory.html), densities at $20\,{}^\circ\text{C}$), and it is inside the interval. The difference is $$
\begin{aligned}
\text{ero} &= 2700\,\text{kg/m}^3 \\
&\quad - 2693\,\text{kg/m}^3 \\
&= 7\,\text{kg/m}^3
\end{aligned}
$$ that is much smaller than the uncertainty $65\,\text{kg/m}^3$. The result therefore agrees with the density of aluminium within the accuracy of the measurement, and it does not contradict the claim that the rod is aluminium. Density alone does not prove the material, however: other materials or alloys can have almost the same density, so the correct conclusion is "the rod can be aluminium". The result is affected for example by chamfered or rounded ends of the rod, which reduce the true volume and raise the density, and by a zero error of the calliper. Cavities inside the rod would, in turn, lower the measured density.

### Yleisiä virheitä
- In part a the right-hand reading $13.6\,\text{cm}$ is taken as the length, although the rod starts at $2.0\,\text{cm}$.
- In part b only the uncertainty of one reading, $0.5\,\text{mm}$, is used as the uncertainty of the length, although the difference contains two readings.
- In part c the diameter is substituted in millimetres but the length in centimetres, or the diameter is used as the radius in $\pi d^2/4$.
- In part c the relative uncertainty of the diameter is calculated without the square ($0.6\,\%$ instead of $1.25\,\%$), so the length seems to give the largest uncertainty.
- In part d the comparison is made by looking at the numbers only ("$2.69$ is not $2.70$") without considering the uncertainty.

### Hyväksytään myös
- In part b the uncertainties of independent readings can be combined in quadrature: $\Delta l = \sqrt{(0.05)^2 + (0.05)^2}\,\text{cm} = 0.07\,\text{cm}$. Then $l = (11.6 \pm 0.1)\,\text{cm}$ rounds in the same way.
- In part c the density $2.69\,\text{g/cm}^3$ and the uncertainty $0.07\,\text{g/cm}^3$ in the unit $\text{g/cm}^3$ are accepted when the conversion or the unit is written down.

## fy9-mittaaminen-s8

### a)
**Given:** five measurements from the picture: $12.2\,\text{s}$, $12.4\,\text{s}$, $12.6\,\text{s}$, $12.7\,\text{s}$ and $12.9\,\text{s}$; the time of ten swings
**Find:** the mean $\bar{t}$ of the time of ten swings and its uncertainty $\Delta t$
**Principle:** From repeated measurements the best estimate is the mean, and the size of the random variation is estimated as half of the range (chapter *Measuring and the reliability of measurement*).
**Reading the graph:** The dots are read from the time axis, where the vertical lines are $0.1\,\text{s}$ apart: $12.2\,\text{s}$, $12.4\,\text{s}$, $12.6\,\text{s}$, $12.7\,\text{s}$ and $12.9\,\text{s}$.
**Formula:** $\bar{t} = \dfrac{t_1 + t_2 + t_3 + t_4 + t_5}{5}$ and $\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$
**Conversions:** None needed: all times are in seconds.
**Substitution:** $12.2 + 12.4 + 12.6 + 12.7 + 12.9 = 62.8\,\text{s}$ $$
\begin{aligned}
\bar{t} &= \dfrac{62.8\,\text{s}}{5} \\
&= 12.56\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\Delta t &= \dfrac{12.9\,\text{s} - 12.2\,\text{s}}{2} \\
&= \dfrac{0.7\,\text{s}}{2} \\
&= 0.35\,\text{s}
\end{aligned}
$$
**Answer:** $t = (12.56 \pm 0.35)\,\text{s}$. Two digits are kept in the uncertainty because it is used in further calculations; the final result is rounded only at the end.
**Reasonableness:** The spread is about $2.8\,\%$ of the mean, which is usual for a stopwatch pressed by hand. The interval $12.56 \pm 0.35\,\text{s}$ reaches roughly the extreme values of the dots, $12.2\,\text{s}$ and $12.9\,\text{s}$.

### b)
**Given:** $\bar{t} = 12.56\,\text{s}$ and $\Delta t = 0.35\,\text{s}$ for ten swings
**Find:** the period $T$ with its uncertainty and a justification for timing ten swings
**Principle:** The period is the duration of one swing, so it is the time of ten swings divided by $10$. The number $10$ is exact, so both the time and its uncertainty are divided by it.
**Formula:** $T = \dfrac{t}{10}$ and $\Delta T = \dfrac{\Delta t}{10}$
**Conversions:** None needed.
**Substitution:** $$
\begin{aligned}
T &= \dfrac{t}{10} \\
&= \dfrac{12.56\,\text{s}}{10} \\
&= 1.256\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\Delta T &= \dfrac{\Delta t}{10} \\
&= \dfrac{0.35\,\text{s}}{10} \\
&= 0.035\,\text{s}
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta T}{T} &= \dfrac{0.035\,\text{s}}{1.256\,\text{s}} \\
&= 0.028 \\
&= 2.8\,\%
\end{aligned}
$$
**Answer:** $T = (1.26 \pm 0.04)\,\text{s}$; the uncertainty $0.035\,\text{s}$ rounds to one digit, $0.04\,\text{s}$, and the relative uncertainty is $2.8\,\%$. The unrounded values $1.256\,\text{s}$ and $0.035\,\text{s}$ are used in the further calculation.
**Reasonableness:** A period of about $1.3\,\text{s}$ fits a pendulum of length $40\,\text{cm}$. The uncertainty $0.04\,\text{s}$ is a small fraction of the period.
**Model answer:** The uncertainty caused by starting and stopping the watch is about $0.35\,\text{s}$ regardless of how long a time is measured. If one swing were timed, the relative uncertainty would be $$
\begin{aligned}
\dfrac{\Delta t}{T} &= \dfrac{0.35\,\text{s}}{1.256\,\text{s}} \\
&= 0.28 \\
&= 28\,\%
\end{aligned}
$$ For the time of ten swings it is only $2.8\,\%$, because the same $0.35\,\text{s}$ is shared between ten periods. The assumption is that the error of pressing does not grow when the swings are counted; the swings must, however, be counted correctly.

### c)
**Given:** $T = 1.256\,\text{s}$ and $\Delta T = 0.035\,\text{s}$ from part b; $l = 40.0\,\text{cm}$ and $\Delta l = 0.2\,\text{cm}$; at a small angle $T = 2\pi\sqrt{l/g}$
**Find:** the acceleration of free fall $g$ with its uncertainty
**Principle:** For a pendulum with a small angle $T = 2\pi\sqrt{l/g}$ (chapter *Spring oscillator and pendulum*). The equation is squared and $g$ is solved before numbers are substituted. Because $g \propto l\,T^{-2}$, the relative uncertainties add and the share of the period is multiplied by the power $2$.
**Formula:** $T^2 = \dfrac{4\pi^2 l}{g}$, so $g = \dfrac{4\pi^2 l}{T^2}$ and $\dfrac{\Delta g}{g} = \dfrac{\Delta l}{l} + 2\,\dfrac{\Delta T}{T}$
**Conversions:** $l = 40.0\,\text{cm} = 0.400\,\text{m}$ and $\Delta l = 0.2\,\text{cm} = 0.002\,\text{m}$.
**Substitution:** $$
\begin{aligned}
g &= \dfrac{4\pi^2 l}{T^2} \\
&= \dfrac{4\pi^2 \cdot 0.400\,\text{m}}{(1.256\,\text{s})^2} \\
&= \dfrac{15.79\,\text{m}}{1.578\,\text{s}^2} \\
&= 10.01\,\text{m/s}^2
\end{aligned}
$$ Relative uncertainties: $$
\begin{aligned}
2\,\dfrac{\Delta T}{T} &= 2 \cdot \dfrac{0.035\,\text{s}}{1.256\,\text{s}} \\
&= 0.0557
\end{aligned}
$$ $$
\begin{aligned}
\dfrac{\Delta l}{l} &= \dfrac{0.002\,\text{m}}{0.400\,\text{m}} \\
&= 0.0050
\end{aligned}
$$ Together: $$
\begin{aligned}
\dfrac{\Delta g}{g} &= 0.0557 + 0.0050 \\
&= 0.0607 \\
&\approx 6.1\,\%
\end{aligned}
$$ Uncertainty: $$
\begin{aligned}
\Delta g &= 0.0607 \cdot 10.01\,\text{m/s}^2 \\
&= 0.61\,\text{m/s}^2
\end{aligned}
$$
**Answer:** $g = (10.0 \pm 0.6)\,\text{m/s}^2$. The uncertainty has one digit and the result is rounded to the same decimal. Almost all of the uncertainty ($5.6\,\%$ of $6.1\,\%$) comes from the period.
**Reasonableness:** The result is close to the known value $9.81\,\text{m/s}^2$ (difference about $2\,\%$). Check the other way round: with $9.81\,\text{m/s}^2$ the period would be $T = 2\pi\sqrt{0.400/9.81}\,\text{s} = 1.27\,\text{s}$, close to the measured $1.26\,\text{s}$.

### d)
**Find:** whether the result agrees with $9.81\,\text{m/s}^2$, why the angle must be small and one improvement
**Principle:** The results agree if the reference value is inside the uncertainty interval of the result. The formula $T = 2\pi\sqrt{l/g}$ is derived with the small-angle approximation (chapter *Spring oscillator and pendulum*).
**Model answer:** The interval of the result is $$
\begin{aligned}
g_\text{min} &= 10.01\,\text{m/s}^2 \\
&\quad - 0.61\,\text{m/s}^2 \\
&= 9.40\,\text{m/s}^2 \\
g_\text{max} &= 10.01\,\text{m/s}^2 \\
&\quad + 0.61\,\text{m/s}^2 \\
&= 10.62\,\text{m/s}^2
\end{aligned}
$$ that is $9.4 \ldots 10.6\,\text{m/s}^2$. The value $9.81\,\text{m/s}^2$ is inside the interval, and the difference is $$
\begin{aligned}
\text{ero} &= 10.01\,\text{m/s}^2 \\
&\quad - 9.81\,\text{m/s}^2 \\
&= 0.20\,\text{m/s}^2
\end{aligned}
$$ that is much smaller than the uncertainty $0.61\,\text{m/s}^2$. The result therefore agrees with $9.81\,\text{m/s}^2$ within the accuracy of the measurement. The measurement does not prove the value exactly, but there is no contradiction. The angle must be small because the derivation assumes $\sin\theta \approx \theta$. At a large angle the period is longer: for example at the amplitude $30^\circ$ by about $1.7\,\%$, and because $g \propto T^{-2}$, the $g$ calculated from the formula would be about $3.4\,\%$ too small. The length must also be measured from the point of suspension to the centre of the bob. Most of the uncertainty comes from the timing ($5.6\,\%$ vs $0.5\,\%$), so the improvement should be aimed at it: for example the time of $30$ swings is measured. Then $$
\begin{aligned}
t_{30} &= 30 \cdot 1.256\,\text{s} \\
&= 37.7\,\text{s} \\
\dfrac{\Delta t}{t_{30}} &= \dfrac{0.35\,\text{s}}{37.7\,\text{s}} \\
&= 0.0093
\end{aligned}
$$ and $$
\begin{aligned}
\dfrac{\Delta g}{g} &= 2 \cdot 0.0093 + 0.0050 \\
&= 0.0236 \\
&\approx 2.4\,\%
\end{aligned}
$$ that is $\Delta g \approx 0.24\,\text{m/s}^2$. A light gate that measures the time without a reaction delay would improve the result even more. After that the uncertainty of the length ($0.5\,\%$) would begin to show in the result.

### Yleisiä virheitä
- In part a the whole range $0.7\,\text{s}$ is taken as the uncertainty instead of half of it, $0.35\,\text{s}$, or the mean is calculated from three dots only.
- In part b the time is divided by ten but the uncertainty is left at $0.35\,\text{s}$, so the uncertainty of the period seems larger than it is.
- In part c the square of the period is forgotten in the relative uncertainty ($2.8\,\%$ instead of $5.6\,\%$), or the length is left in centimetres ($40.0$ instead of $0.400\,\text{m}$), so $g$ is $100$ times too large.
- In part d the result $10.0$ is declared "wrong" because it is not $9.81$, although the difference is smaller than the uncertainty.

### Hyväksytään myös
- In part a the standard deviation can also be used as the uncertainty when it has been calculated and named; it is of a different size than half of the range, and the further calculations are done in the same way.
- In part c the uncertainty can be calculated with extreme values: $g_\text{max} = \dfrac{4\pi^2 \cdot 0.402\,\text{m}}{(1.221\,\text{s})^2} = 10.65\,\text{m/s}^2$ and $g_\text{min} = \dfrac{4\pi^2 \cdot 0.398\,\text{m}}{(1.291\,\text{s})^2} = 9.43\,\text{m/s}^2$, so $\Delta g \approx 0.6\,\text{m/s}^2$.
