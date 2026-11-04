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
**Model answer:** Mira's mean is $\bar{t} = (13.80 + 14.12 + 13.96)\,\text{s} : 3 = 13.96\,\text{s}$ and the uncertainty $(14.12 - 13.80)\,\text{s} : 2 = 0.16\,\text{s}$, so Mira's time is $(13.96 \pm 0.16)\,\text{s}$ and Liisa's $(13.71 \pm 0.19)\,\text{s}$. Liisa's interval is $13.52$–$13.90\,\text{s}$ and Mira's $13.80$–$14.12\,\text{s}$, so the intervals overlap. The difference $0.25\,\text{s}$ is of the same order of magnitude as the uncertainties. So these measurements cannot show that Liisa was faster, although her mean is smaller. This does not, however, mean that the runners are equally fast: showing a difference would require more precise timing, for example a photo-finish camera.

### d)
**Find:** the systematic error of the timing, its effect on the speed and why the mean does not remove it
**Principle:** A systematic error shifts every result in the same direction. It cannot be seen from the spread of the results, and repetition or the mean does not remove it.
**Model answer:** The timekeeper starts the watch only after seeing the flag drop and reacting to it. The watch therefore starts one reaction time late, typically a few tenths of a second. The finish, on the other hand, the timekeeper sees coming, so the watch is stopped almost on time. The measured time is thus shorter than the true time, and the speed in part a is larger than the true speed. The same delay happens with all three timekeepers, so all the watches show too short a time and the mean is too small as well. The mean only reduces the random variation between the watches. The error is removed, for example, by electronic timing that starts itself from the start signal.

### Hyväksytään myös
- In part b, the relative uncertainty of the speed as the sum of the relative uncertainties of the time and the distance: $\tfrac{0.19}{13.71} + \tfrac{0.3}{100.0} \approx 0.0169$, so $\Delta v \approx 0.0169 \cdot 7.294\,\text{m/s} \approx 0.12\,\text{m/s}$.
- In part b, the typical $0.2\,\text{s}$ of hand timing as the uncertainty of the time, when the choice is justified. Then $\Delta v \approx 0.1\,\text{m/s}$ and $v = (7.3 \pm 0.1)\,\text{m/s}$ are also accepted.
- In part d, a mention that a timekeeper $100\,\text{m}$ away who reacts to the sound of a starting pistol would start the watch even later, because sound travels the distance in about $0.3\,\text{s}$.

### Yleisiä virheitä
- One watch or the fastest time is used as the time instead of the mean.
- The speed is converted by multiplying or dividing the wrong way, for example $7.29 : 3.6 = 2.0\,\text{km/h}$; a reasonableness check reveals the error.
- The speed is given to calculator precision, $7.2939\,\text{m/s}$, or the uncertainty and the speed to different precisions.
- In part c, it is concluded from the difference of the means that Liisa was faster, or from the overlapping intervals that the runners were equally fast.
- In part d, the reaction time is said to cause only a random error; its average part is systematic.

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
**Principle:** Density is mass per volume. The mass of a piece of paper of one square metre is the grammage and its volume is $1\,\text{m}^2 \cdot d$, so the density is obtained by dividing the grammage by the thickness.
**Formula:** $\rho = \dfrac{m}{V} = \dfrac{\sigma \cdot 1\,\text{m}^2}{d \cdot 1\,\text{m}^2} = \dfrac{\sigma}{d}$
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
- In part c, the density of the whole stack: $\rho = \tfrac{M}{N a b d} = \tfrac{2.49\,\text{kg}}{31.185\,\text{m}^2 \cdot 1.02 \cdot 10^{-4}\,\text{m}} \approx 783\,\text{kg/m}^3$, or $\rho \approx 784\,\text{kg/m}^3$ calculated with the label of the pack, $80\,\text{g/m}^2$.
- In part a, the thickness in millimetres and the conversion at the end: $d = 51\,\text{mm} : 500 = 0.102\,\text{mm} = 102\,\mu\text{m}$.

### Yleisiä virheitä
- The uncertainty is not divided by the number of sheets, so the thickness of a sheet comes out as $(102 \pm 1000)\,\mu\text{m}$.
- Millimetres are converted to micrometres in the wrong direction: $51\,\text{mm} : 500 = 0.102\,\text{mm} = 0.000102\,\mu\text{m}$. In a smaller unit the number grows.
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
**Given:** the graph of part b, where the points have uncertainty bars of $\pm 1\,\text{ml}$; from part c $k = 0.919\,\text{g/cm}^3$; the densities of the table $1.00$, $0.92$ and $0.79\,\text{g/cm}^3$
**Find:** the uncertainty of the density $\Delta\rho$ and the identification of the liquid
**Principle:** The steepest and the shallowest line that still pass through all the uncertainty bars bound the estimated range of the slope. Half of it is taken as the uncertainty, and the result is compared with the densities of the table.
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
**Answer:** $m \approx 1.38\,\text{kg}$, three significant figures as in the volume $1.50\,\text{l}$; according to the uncertainty of part d, about $\pm 0.02\,\text{kg}$. The volume is $15$ times the measured range, but the calculation does not extend the line of the measuring cylinder; it uses the density, which is a property of the substance and stays the same at the same temperature. Therefore the result is physically justified, as long as the temperature of the oil is the same as in the measurement.
**Reasonableness:** The same volume of water would weigh $1.50\,\text{kg}$, and oil is about $8\,\%$ lighter, so $1.38\,\text{kg}$ has the right size.

### Hyväksytään myös
- In part c, a calculator or spreadsheet fit of a straight line without the row $60\,\text{ml}$: $k = 0.918\,\text{g/cm}^3$ and $b = 118.6\,\text{g}$. Slopes $0.90$–$0.94\,\text{g/cm}^3$ and constant terms $117.5$–$119.5\,\text{g}$ are accepted.
- In part b, keeping the row $60\,\text{ml}$, when its effect is checked: the slope does not change, because the point is in the middle of the measured range, but the constant term grows by about $1\,\text{g}$. The solution must be justified.
- In part d, $\Delta\rho = 0.01$–$0.02\,\text{g/cm}^3$ obtained from limit lines drawn by eye.

### Yleisiä virheitä
- The density is calculated by dividing the mass of some row by the volume, for example $210.3\,\text{g} : 100\,\text{ml} = 2.10\,\text{g/cm}^3$. The mass includes the measuring cylinder.
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
**Model answer:** The claim does not hold. Half the resolution, $0.5\,\text{g}$, only tells how precisely the display can be read. According to part a, the scale shows about $2\,\%$ too much, and the repetitions vary by about $1\,\text{g}$. The corrected mass is obtained by dividing the reading by the ratio given by the weights, $1020\,\text{g} : 1000\,\text{g} = 1.02$: $m \approx 765\,\text{g} : 1.02 = 750\,\text{g}$. The uncertainty is increased by the variation of the repetitions and by the fact that the correction factor is known only to about a thousandth, which makes less than a gram in the reading $765\,\text{g}$. A better estimate is about $(750 \pm 2)\,\text{g}$. So the friend's result is about $15\,\text{g}$ too large, and its uncertainty is too small.

### c)
**Find:** the shape of the graph, what it shows about the kind of error, and why repetition does not help
**Principle:** If the scale were right, the reading would be the same as the mass of the weight, and the points would be on a line with slope $1$ and constant term $0$. A zero error would show in the constant term and a relative error in the slope.
**Model answer:** The points are on a straight line through the origin. The slope is $(1020.3\,\text{g} - 101.7\,\text{g}) : (1000.0\,\text{g} - 100.0\,\text{g}) \approx 1.02$ and not $1$, and the constant term is zero. A constant term of zero tells that the zero point is right, and the slope $1.02$ tells that the scale shows $2\,\%$ too much for every mass. The points of the graph are very precisely on the line, because the random variation, about $1\,\text{g}$, is small.

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
  <foreignObject x="158.5" y="130" width="86" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px;color:#c92a2a">$\text{check}$</div></foreignObject>
  <circle cx="84" cy="306" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="433.5" cy="91.5" r="12" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="258.5" y="274.5" width="164" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$v = k \approx 0.48\,\tfrac{\text{m}}{\text{s}}$</div></foreignObject>
</svg>

**Model answer:** Six points are close to one straight line, so the car moved uniformly. The point $t = 1.5\,\text{s}$ is about $0.25\,\text{m}$ above the line, almost at the same position as the point $t = 2.0\,\text{s}$, so it has probably been marked in the wrong frame. The point is checked from the video. If an error is found, it is corrected, or the point is left out and the reason recorded.

The line is not forced through the origin. Two points of it far apart are read, $(0\,\text{s};\ 0.36\,\text{m})$ and $(3.0\,\text{s};\ 1.79\,\text{m})$, so the speed is $v = \dfrac{1.79\,\text{m} - 0.36\,\text{m}}{3.0\,\text{s} - 0\,\text{s}} = 0.477\,\tfrac{\text{m}}{\text{s}}$. The constant term $0.36\,\text{m}$ is the position of the car when the timing began. The steepest and the shallowest line through all the bars give slopes of about $0.492$ and $0.464\,\text{m/s}$, so $\Delta v = (0.492 - 0.464)\,\text{m/s} : 2 = 0.014\,\text{m/s}$.

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
**Model answer:** On the first row $pV = 189.1\,\text{kPa} \cdot 12\,\text{ml} = 2269\,\text{kPa} \cdot \text{ml}$ and on the last $81.8\,\text{kPa} \cdot 30\,\text{ml} = 2454\,\text{kPa} \cdot \text{ml}$. The products of the rows in between grow steadily row by row, and the total growth is $(2454 - 2269) : 2269 \approx 8\,\%$. The pressures are given to a tenth of a kilopascal, and the product grows in the same direction on every row. A random error would vary haphazardly, so the steady growth of $8\,\%$ is not caused by it. So the claim does not hold for the syringe reading $V$. The growth of the product suggests that the true volume of the air is larger than the reading: part of the air is in the tube and the sensor, and its share is largest when the volume of the syringe is small.

### b)
**Find:** a graph in which the relationship is linear, and a straight line fitted to it
**Graph:** The true volume of the air is $V + V_0$. When the temperature and the amount of air stay the same, according to Boyle's law $p(V + V_0) = C$, so $V = C \cdot \tfrac{1}{p} - V_0$. The horizontal axis is therefore given $\tfrac{1}{p}$ and the vertical axis $V$. For example, on the first row $\tfrac{1}{p} = \tfrac{1}{189.1\,\text{kPa}} = \tfrac{1}{0.1891\,\text{MPa}} = 5.29\,\tfrac{1}{\text{MPa}}$ and on the last $12.2\,\tfrac{1}{\text{MPa}}$.

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
**Conversions:** $1\,\text{MPa} \cdot \text{ml} = 10^{6}\,\text{Pa} \cdot 10^{-6}\,\text{m}^3 = 1\,\text{Pa} \cdot \text{m}^3 = 1\,\text{J}$ and $T = (22 + 273.15)\,\text{K} = 295.15\,\text{K}$
**Substitution:** $V_0 = 1.8\,\text{ml}$, $C = \dfrac{29.5\,\text{ml} - 8.6\,\text{ml}}{12.0\,\tfrac{1}{\text{MPa}} - 4.0\,\tfrac{1}{\text{MPa}}} = 2.61\,\text{MPa} \cdot \text{ml} = 2.61\,\text{J}$ and $n = \dfrac{2.61\,\text{J}}{8.314\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}} \cdot 295.15\,\text{K}} = 1.06 \cdot 10^{-3}\,\text{mol}$
**Answer:** $V_0 \approx 1.8\,\text{ml}$ and $n \approx 1.06 \cdot 10^{-3}\,\text{mol}$. The volume has two significant figures, because it is read from the graph to about $0.1\,\text{ml}$; the amount of substance has three, as the slope does.
**Reasonableness:** At normal pressure and room temperature a mole of gas takes up about $24\,\text{l}$, so about $26\,\text{ml}$ of air is about $26\,\text{ml} : 24\,000\,\text{ml/mol} \approx 1.1 \cdot 10^{-3}\,\text{mol}$. An air space of a few millilitres in the tube and the sensor is plausible for a short tube. When $V_0$ is added, the product $p(V + V_0)$ is $189.1\,\text{kPa} \cdot 13.8\,\text{ml} = 2610\,\text{kPa} \cdot \text{ml}$ on the first row and $81.8\,\text{kPa} \cdot 31.8\,\text{ml} = 2601\,\text{kPa} \cdot \text{ml}$ on the last, that is, almost constant.

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
- In part c, the amount of substance from one row, when $V_0$ has been added: $n = \tfrac{101.2\,\text{kPa} \cdot 25.8\,\text{ml}}{RT} \approx 1.06 \cdot 10^{-3}\,\text{mol}$.

### Yleisiä virheitä
- In part a, $pV$ is said to be "almost constant" without looking at the direction in which the product changes row by row, so the systematic growth goes unnoticed.
- In part b, a $(\tfrac{1}{V}, p)$ graph is drawn and the line is forced through the origin; the air space of the tube then does not show.
- In part c, the temperature is substituted in degrees Celsius, or the volume in millilitres and the pressure in kilopascals without conversion, so the amount of substance is wrong by a factor of a thousand.
- In part d, assumptions are listed without saying in which direction they would change the result.
