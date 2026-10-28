# Measuring and the reliability of a measurement

> **Why** do ten students get ten different results for the rolling time of the same ball, even though they all use the same stopwatch?

## Key idea
A **measurement** means determining the value of a quantity by comparing it with a unit. A measurement result is a numerical value and a unit, for example $2.43\,\text{s}$. The result is never exactly the true value of the quantity, because reading the instrument, the method of measuring and the conditions all add a deviation to it. The difference between the result and the true value is the **measurement error** $\Delta x = x - x_\text{true}$. A small error belongs to every measurement, also to the result of a skilled measurer. In physics the error is estimated and stated together with the result.

Errors are divided into three kinds: gross error, random error and systematic error. You can tell them apart by how they behave when the measurement is repeated.

### Gross error
A **gross error** is a single clear mistake: the instrument is read wrongly, a number is recorded wrongly (for example $3.52\,\text{s}$ instead of $3.25\,\text{s}$), the stopwatch is accidentally started only once the ball is already moving, or the result is recorded in the wrong unit. It usually shows up as a result that differs clearly from the others. A gross error is not estimated or averaged but looked for and removed: the odd result is checked, and if it is clearly wrong, it is left out of the calculations and the measurement is made again. The result that was left out and the reason are written down.

### Random error
A **random error** varies from one measurement to the next by chance and can be in either direction. When the rolling time of a ball is measured with a hand stopwatch, it comes from reaction time: sometimes the stopwatch is started a little too early and sometimes too late. Reading a scale between two marks also brings random error. It shows up as scatter: a slightly different number is obtained for the same quantity each time. Repeating the measurement makes the scatter visible, and the mean damps it, because results that are too large and too small partly cancel each other.

### Systematic error
A **systematic error** is almost the same in direction and size in every measurement. It comes, for example, from a wrong zero (a scale shows $1.2\,\text{g}$ when empty), from a badly adjusted instrument, or from the way of measuring, such as looking at a scale from the side. All results shift in the same direction, so they can be in a tight group but in the wrong place. Repeating and the mean do not remove it. It is noticed by comparing the result with a known reference value or with another method of measurement, and then it is corrected.

<svg data-fig="error-types" viewBox="0 0 600 400" role="img" aria-label="Schematic of the same measurement in two ways, time axis to scale. At the top is random error: ten results scatter on both sides of the true value 2.40 s, and the mean 2.41 s is close to the true value. At the bottom is systematic error: ten results are in a tight group, but the group is entirely to the right of the true value and the mean 2.59 s is about 0.19 s too large." style="max-width:100%;font-size:24px">
  <foreignObject x="14" y="11.5" width="370" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Random error: the results scatter}$</div></foreignObject>
  <line x1="203.5" y1="158" x2="203.5" y2="72" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="208.5" y1="158" x2="208.5" y2="72" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="131.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="160.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="174.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="203.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="203.5" cy="130" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="232" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="232" cy="130" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="260.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="289.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="48" y1="158" x2="502" y2="158" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,158 L501,164 L501,152 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="158" x2="60" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.2$</div></foreignObject>
  <line x1="131.5" y1="158" x2="131.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.3$</div></foreignObject>
  <line x1="203.5" y1="158" x2="203.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.4$</div></foreignObject>
  <line x1="275" y1="158" x2="275" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="346.5" y1="158" x2="346.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.6$</div></foreignObject>
  <line x1="418.5" y1="158" x2="418.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="396" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.7$</div></foreignObject>
  <line x1="490" y1="158" x2="490" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.8$</div></foreignObject>
  <foreignObject x="520" y="143.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74.5" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{true value}$</div></foreignObject>
  <foreignObject x="217.5" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mean}$</div></foreignObject>
  <foreignObject x="14" y="207.5" width="395" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Systematic error: the results shift}$</div></foreignObject>
  <line x1="203.5" y1="354" x2="203.5" y2="268" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="342.5" y1="354" x2="342.5" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="303.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="318" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="326" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="326" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="310" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="294" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="361" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="375.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="48" y1="354" x2="502" y2="354" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,354 L501,360 L501,348 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="354" x2="60" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.2$</div></foreignObject>
  <line x1="131.5" y1="354" x2="131.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.3$</div></foreignObject>
  <line x1="203.5" y1="354" x2="203.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.4$</div></foreignObject>
  <line x1="275" y1="354" x2="275" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="346.5" y1="354" x2="346.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.6$</div></foreignObject>
  <line x1="418.5" y1="354" x2="418.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="396" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.7$</div></foreignObject>
  <line x1="490" y1="354" x2="490" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2.8$</div></foreignObject>
  <foreignObject x="520" y="339.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74.5" y="239.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{true value}$</div></foreignObject>
  <foreignObject x="351.5" y="239.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mean}$</div></foreignObject>
  <line x1="205.5" y1="288" x2="327.5" y2="288" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M340.5,288 L326.5,294.5 L326.5,281.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="238" y="255.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\Delta t_\text{sys}$</div></foreignObject>
  <line x1="24" y1="206" x2="576" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
</svg>

### Repeatability and correctness
The reliability of a measurement is described by two things. **Repeatability** tells how close to each other repeated measurements land, and it is weakened by random error. **Correctness** tells how close the mean is to the true value, and it is weakened by systematic error. A measurement can be repeatable but not correct, like the lower series in the figure. A reliable measurement has both.

## Formula: Mean and error estimate
The best estimate of a repeated measurement is the mean of the results:
```latex
\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n}
```
where $\bar{x}$ is the mean, $x_1, x_2, \dots, x_n$ are the individual measurement results and $n$ is the number of measurements. The mean adds up the results and divides the sum by the number, so the more measurements there are, the less a single stray result affects it.

The size of random error is estimated as half of the range:
```latex
\Delta x = \frac{x_\text{max} - x_\text{min}}{2}
```
where $\Delta x$ is the error estimate, $x_\text{max}$ is the largest and $x_\text{min}$ the smallest result. The notation is the same as for the measurement error, because the error estimate tells how large the measurement error in the result is estimated to be; the error estimate is always positive. The result is stated in the form $\bar{x} \pm \Delta x$. The error estimate is a rough estimate, not an exact limit: a single result can sometimes fall outside it.

<svg data-fig="range-half" viewBox="0 0 600 330" role="img" aria-label="Schematic, no numerical values: six measurement results on a time axis. The largest result t_max and the smallest result t_min bound the range, whose length is t_max − t_min. The mean is marked with a vertical line. Half of the range Δt is an estimate of the random error, and the result is given as the mean plus or minus Δt." style="max-width:100%;font-size:24px">
  <circle cx="143.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="196" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="269.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="143.5" y1="144" x2="143.5" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="395.5" y1="144" x2="395.5" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="151.5" y1="114" x2="376.5" y2="114" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M387.5,114 L375.5,119.5 L375.5,108.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="387.5" y1="114" x2="162.5" y2="114" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M151.5,114 L163.5,108.5 L163.5,119.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="209.5" y="67.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{max} - t_\text{min}$</div></foreignObject>
  <line x1="58" y1="170" x2="502" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,170 L501,176 L501,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="520" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="114.5" y="181.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{min}$</div></foreignObject>
  <foreignObject x="366.5" y="181.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{max}$</div></foreignObject>
  <path d="M260.75,177 L252.75,192 L268.75,192 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="244" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\bar{t}$</div></foreignObject>
  <rect x="134.5" y="236" width="252" height="16" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <line x1="261" y1="230" x2="261" y2="258" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="54.5" y="229.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\bar{t} - \Delta t$</div></foreignObject>
  <foreignObject x="397" y="229.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\bar{t} + \Delta t$</div></foreignObject>
  <foreignObject x="221" y="263" width="158" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$</div></foreignObject>
</svg>

The error estimate is rounded to one significant figure, or to two if the first figure is 1. The result is rounded to the same decimal place: $3.18 \pm 0.12\,\text{s}$ and not $3.1817 \pm 0.12\,\text{s}$. This way the result has no figures that the error already blurs. When the measurement is made only once, the error estimate is half of a scale division $d$:
```latex
\Delta x = \frac{d}{2}
```
With a ruler whose smallest scale division is $1.0\,\text{mm}$, the error estimate of a single reading is therefore $0.5\,\text{mm}$.

The ratio of the error estimate to the result is called the relative error:
```latex
\varepsilon = \frac{\Delta x}{\bar{x}} \cdot 100\,\%
```
where $\varepsilon$ is the relative error as a percentage. It tells whether the error is small or large compared with the size of the result: an error of $0.5\,\text{mm}$ is small for measuring a metre but large for a wire one millimetre thick.

A systematic error is estimated by measuring a quantity whose true value is known and comparing with the mean. The known value can be, for example, an empty scale, $0\,{}^\circ\text{C}$ in ice water or a rod of precisely known length:
```latex
\Delta x_\text{sys} = \bar{x}_\text{ref} - x_\text{true}
```
where $\bar{x}_\text{ref}$ is the mean of the reference measurements and $x_\text{true}$ is the true value of the reference quantity. The corrected result is obtained by subtracting the error from the reading:
```latex
x = x_\text{reading} - \Delta x_\text{sys}
```

<svg data-fig="zero-scale" viewBox="0 0 600 392" role="img" aria-label="Schematic, not to scale: a kitchen scale shown twice. On the left the pan is empty, but the scale shows 1.2 g, so the zero is wrong. On the right the pan has an iron object and the scale shows 48.7 g. The mass of the object is obtained by subtracting the zero reading from the reading: 48.7 g minus 1.2 g is 47.5 g." style="max-width:100%;font-size:24px">
  <rect x="50" y="206" width="200" height="100" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="74" y="188" width="152" height="18" rx="6" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="90" y="238" width="120" height="44" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="115" y="245.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1.2\,\text{g}$</div></foreignObject>
  <rect x="350" y="206" width="200" height="100" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="374" y="188" width="152" height="18" rx="6" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="390" y="238" width="120" height="44" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="408.5" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$48.7\,\text{g}$</div></foreignObject>
  <rect x="412" y="128" width="76" height="60" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="424" y1="142" x2="476" y2="142" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="96" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{empty: } m_0$</div></foreignObject>
  <foreignObject x="352.5" y="321.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{reading } m_\text{reading}$</div></foreignObject>
  <line x1="300" y1="48" x2="300" y2="352" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="171" y="13.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{systematic error: zero}$</div></foreignObject>
  <foreignObject x="215" y="357.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = m_\text{reading} - m_0$</div></foreignObject>
</svg>

## Worked example
A student measures the rolling time of a ball on a ramp with a hand stopwatch six times and gets the results $3.12\,\text{s}$, $3.25\,\text{s}$, $3.07\,\text{s}$, $3.31\,\text{s}$, $3.19\,\text{s}$ and $3.15\,\text{s}$. What is the measurement result with its error estimate, and how large is the relative error?

<svg data-fig="example-plot" viewBox="0 0 600 330" role="img" aria-label="Measurement results (t, time) to scale: six results between 3.07 s and 3.31 s, mean 3.18 s and the result 3.18 s ± 0.12 s on a green bar." style="max-width:100%;font-size:24px">
  <line x1="261" y1="150" x2="261" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="196" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="143.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="269.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="58" y1="150" x2="502" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,150 L501,156 L501,144 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="150" x2="70" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="175" y1="150" x2="175" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="152.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3.1$</div></foreignObject>
  <line x1="280" y1="150" x2="280" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="257.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3.2$</div></foreignObject>
  <line x1="385" y1="150" x2="385" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="362.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3.3$</div></foreignObject>
  <line x1="490" y1="150" x2="490" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3.4$</div></foreignObject>
  <foreignObject x="520" y="135.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="131" y="35.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\bar{t} = 3.18\,\text{s}$</div></foreignObject>
  <rect x="134.5" y="236" width="252" height="16" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <line x1="261" y1="230" x2="261" y2="258" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="202.5" y="277.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 3.18\,\text{s} \pm 0.12\,\text{s}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Given and find.** The number of measurements is $n = 6$, and the smallest result is $t_\text{min} = 3.07\,\text{s}$ and the largest $t_\text{max} = 3.31\,\text{s}$. The mean $\bar{t}$, the error estimate $\Delta t$ and the relative error $\varepsilon$ are asked for.

<!-- vaihe -->

**Principle.** Hand timing has a random error, because reaction time varies. So the mean is taken as the result and half of the range as the error estimate. The relative error compares the error estimate with the result.

<!-- vaihe -->

**Rearranged formula.**
```latex
\begin{aligned}
\bar{t} &= \frac{t_1 + t_2 + \dots + t_n}{n} \\
\Delta t &= \frac{t_\text{max} - t_\text{min}}{2} \\
\varepsilon &= \frac{\Delta t}{\bar{t}} \cdot 100\,\%
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None needed: all times are in seconds, and the relative error is a number without a unit, which is multiplied by a hundred to get percent.

<!-- vaihe -->

**Substitution.** The sum of the results is $3.12\,\text{s} + 3.25\,\text{s} + 3.07\,\text{s} + 3.31\,\text{s} + 3.19\,\text{s} + 3.15\,\text{s} = 19.09\,\text{s}$. Substitute it and the other numerical values with their units:
```latex
\begin{aligned}
\bar{t} &= \frac{t_1 + t_2 + \dots + t_n}{n} \\
&= \frac{19.09\,\text{s}}{6} \\
&= 3.1817\,\text{s}
\\[4pt]
\Delta t &= \frac{t_\text{max} - t_\text{min}}{2} \\
&= \frac{3.31\,\text{s} - 3.07\,\text{s}}{2} \\
&= 0.12\,\text{s}
\\[4pt]
\varepsilon &= \frac{\Delta t}{\bar{t}} \cdot 100\,\% \\
&= \frac{0.12\,\text{s}}{3.1817\,\text{s}} \cdot 100\,\% \\
&= 3.8\,\%
\end{aligned}
```

<!-- vaihe -->

**Result.** The error estimate $0.12\,\text{s}$ is a number with two figures, because its first figure is 1. The mean is rounded to the same decimal place, so the measurement result is $t = 3.18\,\text{s} \pm 0.12\,\text{s}$. The relative error is $3.8\,\%$, two significant figures like the error estimate.

<!-- vaihe -->

**Reasonableness.** The interval $3.18\,\text{s} \pm 0.12\,\text{s}$, that is, $3.06\,\text{s}$–$3.30\,\text{s}$, covers five of the six results. The result $3.31\,\text{s}$ falls just outside it, which fits the fact that the error estimate is rough. The relative error is a few percent, which is usual for a hand-timed measurement. However, the repeats tell only about random error: a systematic error would be revealed only by comparison with another method of measurement.

## Common misconception
Many people think that an accurate instrument or many repeats guarantee a correct result. Repeats reduce random error but not systematic error, and good repeatability tells nothing about correctness. Another misconception is to regard all error as carelessness. Carelessness causes a gross error, which is removed, but random and systematic error belong to the result of a skilled measurer too, and that is why they are estimated and stated. A third is to calculate a mean of numbers that are in different units: the results are converted to the same unit first.

## Summary
- A measurement error is the difference between the result and the true value, $\Delta x = x - x_\text{true}$. An error belongs to every measurement, and it is estimated and stated together with the result.
- A gross error is a single mistake, such as a wrongly read or recorded reading. It shows up as a result that clearly differs from the others, which is checked and left out.
- A random error varies from one measurement to the next and shows up as scatter. The mean $\bar{x}$ damps it, and its size is estimated by half of the range $\Delta x$.
- A systematic error shifts all results in the same direction, and repeating does not remove it. It is noticed with a reference value and corrected: $x = x_\text{reading} - \Delta x_\text{sys}$.
- Repeatability tells about random error and correctness about systematic error. A reliable measurement is both repeatable and correct.
- The result is stated in the form $\bar{x} \pm \Delta x$ with its unit. The error estimate is rounded to one significant figure (two if the first figure is 1), and the result to the same decimal place.
