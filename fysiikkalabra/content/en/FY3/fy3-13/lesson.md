# Determining absolute zero

> **Why** can the lowest possible temperature be found in a school laboratory, even though a thermometer does not come anywhere near it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a laboratory bench there are three containers: ice water, water at room temperature, and water boiling on a hot plate. The middle bath holds a sealed glass flask connected by a hose to a pressure gauge." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea
In a closed rigid container, the volume and the amount of gas do not change, so the pressure depends only on temperature. In a gas thermometer, a glass flask stands in a water bath. As the bath warms up, you read the bath temperature $\theta$ from a thermometer and the gas pressure $p$ from a pressure gauge.

<svg data-fig="thermometer" viewBox="0 0 600 372" role="img" aria-label="Gas thermometer: a sealed glass flask containing air stands in a water bath that is being heated. The volume of the gas in the flask does not change. The temperature of the water bath is read from a thermometer and the pressure of the gas from a pressure gauge. The picture is a diagram, not to scale." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-13-thermometer.webp" x="0" y="0" width="600" height="378.8" preserveAspectRatio="none"/>
  <foreignObject x="75" y="88.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="460" y="130.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="380" y="171.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pressure gauge}$</div></foreignObject>
  <foreignObject x="316" y="338.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="320" y="211.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{water bath}$</div></foreignObject>
  <foreignObject x="320" y="255.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{air},\ V=\text{constant}$</div></foreignObject>
</svg>

When you plot the measurements on a graph, the points lie almost on a straight line: the pressure rises by almost the same amount for every degree Celsius. In real data sets the points are usually not exactly on one line, because of measurement uncertainty. Measurement uncertainty describes the uncertainty attached to a measurement result. It does not usually mean an absolute maximum possible deviation from the true value. Here the uncertainty of the pressure reading is estimated as $\pm 1\,\text{kPa}$. The error limit that a manufacturer states for a gauge is a different thing: it is a property of the device, and the uncertainty of the measurement is also affected by, for example, reading the scale and the bath temperature settling. So you draw the line through the middle of the group of points, so that it passes through the uncertainty bars, not necessarily through every point.

```pysahdy
The line is drawn through the middle of the group of points. Must it pass through every point?
---
No. It must pass through the uncertainty bars, not necessarily through every point, because measurement uncertainty makes the points scatter.
```

<figure class="unit-photo"><img src="pics/fy3/liquid-nitrogen-dish.webp" alt="A hand holds a glass dish containing liquid nitrogen. White mist flows from around the dish against a dark background."><figcaption>Liquid nitrogen in a glass dish at a science festival in 2025. The white mist is water droplets condensed around the cold nitrogen vapour.</figcaption></figure>

You extend the line beyond the measurement range towards colder temperatures until the pressure is zero. This is called extrapolation: the result comes from a region where nothing has been measured. According to the microscopic model, pressure comes from particles colliding with the wall. In the ideal gas model, the pressure would be zero at the temperature where the average kinetic energy of the particles is at its lowest. The temperature where the line meets zero pressure is the experiment's estimate of absolute zero. It is only an estimate: a real gas liquefies before that point, and the extension is a model.

```pysahdy
Why is the temperature where the line meets zero pressure only an estimate of absolute zero?
---
It comes from extrapolation, a region where nothing has been measured, and a real gas liquefies before that point. The extension is a model.
```

## Formula: Temperature at zero pressure
Within the measurement range, the pressure of a gas is a linear function of temperature:
```latex
p = p_0 + k\theta
```
where $p$ is the pressure (kPa), $p_0$ is the pressure of the line at $0\,{}^\circ\text{C}$ (kPa), $k$ is the slope of the line (kPa/°C) and $\theta$ is the temperature in degrees Celsius. You calculate the slope from two points read far apart from the drawn line:
```latex
k = \frac{p_2 - p_1}{\theta_2 - \theta_1}
```
where $(\theta_1, p_1)$ and $(\theta_2, p_2)$ are points on the line. Zero pressure is reached when $p = 0$. The temperature is then $\theta_0$, and the equation gives:
```latex
\begin{aligned}
0 &= p_0 + k\theta_0 \\
\theta_0 &= -\frac{p_0}{k}
\end{aligned}
```
You get the same result from any point $(\theta_1, p_1)$ on the line by substituting $p = 0$ into the equation $p = p_1 + k(\theta - \theta_1)$:
```latex
\theta_0 = \theta_1 - \frac{p_1}{k}
```

You estimate the uncertainty by drawing two limit lines that still pass through all the uncertainty bars: the steepest and the shallowest. For each you calculate the temperature at zero pressure, and the smaller and larger values give an interval. You give the result using the midpoint and half of the interval:
```latex
\Delta\theta_0 = \frac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}
```
where $\theta_{0,\text{max}}$ is the larger (less negative) and $\theta_{0,\text{min}}$ the smaller temperature at zero pressure. The result has the form $\theta_0 \pm \Delta\theta_0$. The interval is an estimate, not a guaranteed limit: it takes into account the uncertainty of the points but not whether the dependence stays linear outside the measurement range.

<svg viewBox="0 0 600 368" role="img" aria-label="Gas pressure as a function of temperature over the whole range from −300 °C to 100 °C. The measurement points are only in the range 10–100 °C. The best-fit line and its dashed extension extrapolate to zero pressure at a temperature θ₀ ≈ −276 °C. The steepest and shallowest limit lines meet the p = 0 axis at about −259 °C and −295 °C, which gives the uncertainty interval. The picture is to scale; the ±1 kPa error bars are about the size of the points." style="max-width:100%;font-size:24px">
<line x1="78.0" y1="270.0" x2="78.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="202.0" y1="270.0" x2="202.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="326.0" y1="270.0" x2="326.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="450.0" y1="270.0" x2="450.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="574.0" y1="270.0" x2="574.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="190.0" x2="574.0" y2="190.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="110.0" x2="574.0" y2="110.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="30.0" x2="574.0" y2="30.0" stroke="#e3dccb" stroke-width="1.5"/>
<line x1="78.0" y1="270.0" x2="582.0" y2="270.0" stroke="#1f2933" stroke-width="3"/>
<line x1="78.0" y1="270.0" x2="78.0" y2="22.0" stroke="#1f2933" stroke-width="3"/>
<foreignObject x="43" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}300$</div></foreignObject>
<foreignObject x="167" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}200$</div></foreignObject>
<foreignObject x="291" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">${-}100$</div></foreignObject>
<foreignObject x="415" y="274" width="70" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0$</div></foreignObject>
<foreignObject x="530" y="274" width="68" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$100$</div></foreignObject>
<foreignObject x="6" y="173" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$50$</div></foreignObject>
<foreignObject x="6" y="93" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$100$</div></foreignObject>
<foreignObject x="6" y="13" width="64" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$150$</div></foreignObject>
<foreignObject x="424" y="226" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\theta\ (^\circ\text{C})$</div></foreignObject>
<foreignObject x="86" y="0" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$p\ (\text{kPa})$</div></foreignObject>
<line x1="128.9" y1="270.0" x2="462.4" y2="103.6" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="84.0" y1="270.0" x2="462.4" y2="100.7" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="7 5"/>
<line x1="107.6" y1="270.0" x2="462.4" y2="102.1" stroke="#1f2933" stroke-width="3" stroke-dasharray="10 7"/>
<line x1="462.4" y1="102.1" x2="574.0" y2="49.3" stroke="#1f2933" stroke-width="4"/>
<circle cx="462.4" cy="102.0" r="4" fill="#1f2933"/>
<circle cx="481.0" cy="94.0" r="4" fill="#1f2933"/>
<circle cx="499.6" cy="84.4" r="4" fill="#1f2933"/>
<circle cx="518.2" cy="74.8" r="4" fill="#1f2933"/>
<circle cx="536.8" cy="66.8" r="4" fill="#1f2933"/>
<circle cx="555.4" cy="58.8" r="4" fill="#1f2933"/>
<circle cx="574.0" cy="49.2" r="4" fill="#1f2933"/>
<path d="M84.0,314.0 V322.0 H128.9 V314.0" fill="none" stroke="#c92a2a" stroke-width="3"/>
<circle cx="107.6" cy="270.0" r="6" fill="#c92a2a"/>
<foreignObject x="4" y="324" width="210" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\theta_0 \pm \Delta\theta_0$</div></foreignObject>
<foreignObject x="204" y="76" width="200" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{extrapolation}$</div></foreignObject><line x1="264" y1="114" x2="264" y2="184" stroke="#1f2933" stroke-width="1.5"/><foreignObject x="240" y="6" width="212" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{measurement range}$</div></foreignObject><path d="M462,48 V32 H574 V48" fill="none" stroke="#1f2933" stroke-width="2"/>
</svg>

The picture is drawn to scale. The limit lines run close to each other in the measurement range but move apart when you extrapolate, so the uncertainty grows as you extend the line. A more precise pressure gauge, more measurement points and a wider measurement range reduce the uncertainty. Once the result is known, the zero of the kelvin scale is placed there: the temperature in kelvins is $T = \theta - \theta_0$.

```pysahdy
The limit lines move apart when the line is extended. What does this mean for the uncertainty of $\theta_0$?
---
The farther the line is extended, the greater the uncertainty of $\theta_0$ becomes.
```

## Worked example
The example data give the pressure of the air in a sealed flask at seven temperatures, as a gas thermometer would measure them. The values have been calculated from the ideal gas model, and scatter corresponding to measurement imprecision has been added; they are not the results of a real measurement. The uncertainty of the pressure reading is estimated as $\pm 1\,\text{kPa}$.

| $\theta$ (°C) | $p$ (kPa) |
| --- | --- |
| 10 | 105 |
| 25 | 110 |
| 40 | 116 |
| 55 | 122 |
| 70 | 127 |
| 85 | 132 |
| 100 | 138 |

Determine absolute zero by extrapolation and estimate the uncertainty of the result. The best-fit line through the points is in the figure above; its steepest and shallowest alternatives, which still pass through all the uncertainty bars, are $p = 100.1\,\text{kPa} + 0.387\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ and $p = 102.3\,\text{kPa} + 0.347\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$. The steepest touches the ends of the uncertainty bars at $10\,{}^\circ\text{C}$ and $85\,{}^\circ\text{C}$, the shallowest at $25\,{}^\circ\text{C}$ and $100\,{}^\circ\text{C}$.

<!-- vaihe -->

**Given and find.** Two points far apart are read from the best-fit line:

- $(\theta_1, p_1) = (0\,{}^\circ\text{C};\ 101.3\,\text{kPa})$ and
- $(\theta_2, p_2) = (100\,{}^\circ\text{C};\ 138.0\,\text{kPa})$.

The temperature $0\,{}^\circ\text{C}$ is outside the measurement range, so point 1 is read from the extension of the line: it is not a measurement but already a little extrapolation.

The limit lines have

- $p_0 = 100.1\,\text{kPa}$, $k = 0.387\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ and
- $p_0 = 102.3\,\text{kPa}$, $k = 0.347\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$.

You are asked for the temperature at zero pressure $\theta_0$ and its uncertainty $\Delta\theta_0$.

<!-- vaihe -->

**Principle.** The flask is sealed and rigid, so the amount and volume of the gas stay constant, and within the measurement range the pressure is a linear function of temperature, $p = p_0 + k\theta$. So you can extend the line to the point where $p = 0$.

The uncertainty comes from the limit lines: they pass through all the uncertainty bars, so they fit the data just as well as the best-fit line, and their zero-pressure points bound the interval where the true absolute zero probably lies.

<!-- vaihe -->

**Rearranged formula.** The slope, the temperature at zero pressure (with $p_0 = p_1$, because point 1 is at $0\,{}^\circ\text{C}$) and the uncertainty as half of the interval:
```latex
\begin{aligned}
&k = \frac{p_2 - p_1}{\theta_2 - \theta_1} \\
&\theta_0 = -\frac{p_0}{k} \\
&\Delta\theta_0 \\
&= \frac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** No conversions are needed: the pressures are in kilopascals, so in the quotient $p_0/k$ the kPa cancels and what is left is the degree Celsius, which is what you are asked for.

The temperature difference $100\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 100\,{}^\circ\text{C}$ is the same in kelvins, and the temperature at zero pressure is given in degrees Celsius.

<!-- vaihe -->

**Substitution.** First calculate the slope and then the temperature at zero pressure:
```latex
\begin{aligned}
&k = \frac{p_2 - p_1}{\theta_2 - \theta_1} \\
&= \frac{(138.0 - 101.3)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\
&= 0.367\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \\[6pt]
&\theta_0 = -\frac{p_0}{k} \\
&= -\frac{101.3\,\text{kPa}}{0.367\,\text{kPa}/{}^\circ\text{C}} \\
&= -276.02\,{}^\circ\text{C}
\end{aligned}
```
For the limit lines $\theta_{0,\text{max}} = -\tfrac{100.1}{0.387}\,{}^\circ\text{C} = -258.66\,{}^\circ\text{C}$ and $\theta_{0,\text{min}} = -\tfrac{102.3}{0.347}\,{}^\circ\text{C} = -294.81\,{}^\circ\text{C}$, so $\Delta\theta_0 = \tfrac{-258.66 - (-294.81)}{2}\,{}^\circ\text{C} = 18.08\,{}^\circ\text{C}$.

<!-- vaihe -->

**Result.** Absolute zero is $\theta_0 = -276 \pm 18\,{}^\circ\text{C}$.

The uncertainty is given with two significant figures ($18.08 \approx 18$), because the zero points of the limit lines, $-259\,{}^\circ\text{C}$ and $-295\,{}^\circ\text{C}$, are known to three figures and their difference $36\,{}^\circ\text{C}$ to only two.

The result is rounded to the same precision, that is, to one degree.

<!-- vaihe -->

**Reasonableness.** The accepted value $-273.15\,{}^\circ\text{C}$ lies in the interval $-294\,{}^\circ\text{C}\ldots -258\,{}^\circ\text{C}$, so the result agrees with it; the deviation is about $3\,{}^\circ\text{C}$ and the uncertainty is $18\,{}^\circ\text{C}$.

An estimate in your head: the pressure rises by about $0.37\,\text{kPa}$ per degree, so $101\,\text{kPa}$ runs out after about $101/0.37 \approx 270$ degrees.

The uncertainty is large because the measurement was made more than $270\,{}^\circ\text{C}$ away from zero pressure, and the uncertainty of the points, $1\,\text{kPa}$, is about one percent of the reading.

## Common misconception
Many people think that absolute zero has been measured because it is on the graph. Only the seven points in the range 10–$100\,{}^\circ\text{C}$ are measured; the rest is an extension of the line, and the extension is an assumption that the pressure behaves in the same way at colder temperatures. Another mistake is to consider the result a failure if it is not exactly $-273.15\,{}^\circ\text{C}$. The result $-276\,{}^\circ\text{C}$ differs from the accepted value by about 3 degrees when the uncertainty is 18 degrees, so it agrees with the value. A third mistake is to draw a wiggly line through every point: the variation of the points up and down is caused by measurement uncertainty, and the line should be drawn through the middle of the group of points.

## Summary
- In a closed rigid container, the pressure of a dilute gas is a linear function of temperature within the measurement range: $p = p_0 + k\theta$. You turn the measurement data into a straight line by plotting $p$ as a function of temperature and drawing the line through the middle of the group of points.
- Measurement uncertainty describes the uncertainty attached to a measurement result, and it is not usually an absolute maximum possible deviation from the true value. The line does not have to hit every point, only pass through the uncertainty bars.
- Extrapolation extends the line beyond the measurement range: the temperature at zero pressure is $\theta_0 = -p_0/k$.
- You estimate the uncertainty from the limit lines: $\Delta\theta_0 = (\theta_{0,\text{max}} - \theta_{0,\text{min}})/2$. The result $\theta_0 \pm \Delta\theta_0$ agrees with the accepted value $-273.15\,{}^\circ\text{C}$ if that value lies in the interval.
