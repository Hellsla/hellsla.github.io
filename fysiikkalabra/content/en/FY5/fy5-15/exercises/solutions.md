## fy5-15-L1-01
**Given:** area of the window opening $A = 1.5\,\text{m}^2$, sound power passing through the opening $P = 3.0\,\text{mW}$, the power is spread evenly
**Find:** the intensity $I$ in $\text{W/m}^2$
**Principle:** Intensity is the power passing through a surface divided by the area of the surface. Because the power is spread evenly over the whole opening, the intensity is the same everywhere in the opening.
**Formula:** $I = \dfrac{P}{A}$
**Conversions:** $P = 3.0\,\text{mW} = 3.0 \cdot 10^{-3}\,\text{W}$
**Substitution:** $I = \dfrac{3.0 \cdot 10^{-3}\,\text{W}}{1.5\,\text{m}^2} = 2.0 \cdot 10^{-3}\,\text{W/m}^2 = 0.0020\,\text{W/m}^2$
**Answer:** $0.0020\,\text{W/m}^2$, two significant figures like the power $3.0\,\text{mW}$ and the area $1.5\,\text{m}^2$.
**Reasonableness:** The area is greater than $1\,\text{m}^2$, so the numerical value of the intensity must be smaller than the numerical value of the power in watts, and $0.0020 < 0.0030$. As a sound intensity level this would be about $93\,\text{dB}$, which fits a lawn mower running right under the window.

## fy5-15-L1-02
**Given:** intensity $I = 3.2 \cdot 10^{-5}\,\text{W/m}^2$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** the sound intensity level $L$ in decibels
**Principle:** The sound intensity level compares the intensity with the threshold of hearing logarithmically: it tells how many tenfold steps the intensity is above the threshold of hearing, multiplied by ten.
**Formula:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$
**Conversions:** Not needed: both intensities are in $\text{W/m}^2$, and the units cancel in the quotient.
**Substitution:** $L = 10\,\text{dB} \cdot \lg \dfrac{3.2 \cdot 10^{-5}\,\text{W/m}^2}{1.0 \cdot 10^{-12}\,\text{W/m}^2} = 10\,\text{dB} \cdot \lg (3.2 \cdot 10^{7}) = 10\,\text{dB} \cdot 7.505 = 75.05\,\text{dB}$
**Answer:** $75\,\text{dB}$, in whole decibels, because the intensity is given to two significant figures.
**Reasonableness:** The intensity is between $10^{-5}$ and $10^{-4}\,\text{W/m}^2$, so the level must be between $70$ and $80\,\text{dB}$. A vacuum cleaner is usually about as loud as a busy street.

## fy5-15-L1-03
**Given:** the meter reading, taken as the sound intensity level in a free sound field, $L = 95\,\text{dB}$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** the intensity $I$ in $\text{W/m}^2$
**Principle:** The level is ten times the logarithm of the ratio of the intensities. The intensity is obtained by dividing the equation by $10\,\text{dB}$ and using the definition of the logarithm: if $\lg x = y$, then $x = 10^y$.
**Formula:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, so $\lg \dfrac{I}{I_0} = \dfrac{L}{10\,\text{dB}}$ and $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$
**Conversions:** Not needed: $\dfrac{L}{10\,\text{dB}} = \dfrac{95\,\text{dB}}{10\,\text{dB}} = 9.5$, the decibels cancel.
**Substitution:** $I = 1.0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{9.5} = 3.16 \cdot 10^{-3}\,\text{W/m}^2 = 0.00316\,\text{W/m}^2$
**Answer:** $0.0032\,\text{W/m}^2$, two significant figures, because the level is given in whole decibels.
**Reasonableness:** $90\,\text{dB}$ corresponds to an intensity of $10^{-3}\,\text{W/m}^2$ and $100\,\text{dB}$ to $10^{-2}\,\text{W/m}^2$, so the intensity at $95\,\text{dB}$ must lie between them. The factor for half a tenfold step is $\sqrt{10} \approx 3.16$, and $3.16 \cdot 10^{-3}\,\text{W/m}^2$ is exactly this.

## fy5-15-L1-04
**Given:** sound power of the siren $P = 2.0\,\text{W}$, distance $r = 25\,\text{m}$, the sound spreads evenly in all directions and is not reflected
**Find:** the intensity $I$ in $\text{W/m}^2$
**Principle:** The siren acts as a point source: when the sound is neither reflected nor absorbed, the whole power passes through a spherical surface of radius $25\,\text{m}$ around the siren and is spread evenly over it.
**Formula:** $I = \dfrac{P}{A} = \dfrac{P}{4\pi r^2}$
**Conversions:** Not needed: the power is in watts and the distance in metres.
**Substitution:** $I = \dfrac{2.0\,\text{W}}{4\pi \cdot (25\,\text{m})^2} = \dfrac{2.0\,\text{W}}{7854\,\text{m}^2} = 2.55 \cdot 10^{-4}\,\text{W/m}^2 = 0.000255\,\text{W/m}^2$
**Answer:** $0.00025\,\text{W/m}^2$, two significant figures like the power $2.0\,\text{W}$ and the distance $25\,\text{m}$.
**Reasonableness:** The area of the sphere is about $8000\,\text{m}^2$, and $2\,\text{W} : 8000\,\text{m}^2 = 0.00025\,\text{W/m}^2$. As a level this is about $84\,\text{dB}$, which is believable for a siren at $25\,\text{m}$.

## fy5-15-L1-05
**Given:** ratio of the intensities $\dfrac{I_2}{I_1} = 100$
**Find:** the difference in levels $L_2 - L_1$ in decibels
**Principle:** The difference in levels depends only on the ratio of the intensities, because the threshold of hearing $I_0$ cancels when the levels are subtracted.
**Formula:** $L_2 - L_1 = 10\,\text{dB} \cdot \lg \dfrac{I_2}{I_1}$
**Conversions:** Not needed: the ratio is a plain number.
**Substitution:** $L_2 - L_1 = 10\,\text{dB} \cdot \lg 100 = 10\,\text{dB} \cdot 2 = 20\,\text{dB}$
**Answer:** $20\,\text{dB}$; the factor $100$ is exact, so the result is exact.
**Reasonableness:** A hundredfold increase is two tenfold steps in succession, and each raises the level by $10\,\text{dB}$: $10\,\text{dB} + 10\,\text{dB} = 20\,\text{dB}$. The level rises by $20\,\text{dB}$, not a hundredfold: the decibel scale is logarithmic.

## fy5-15-L2-01
**Given:** sound power of the loudspeaker $P = 0.050\,\text{W}$, distance $r = 3.0\,\text{m}$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$; the sound spreads evenly and is not reflected
**Find:** the sound intensity level $L$ in decibels
**Principle:** The loudspeaker is a point source whose power is spread evenly over a spherical surface of radius $3.0\,\text{m}$. First the intensity is calculated, then it is compared with the threshold of hearing.
**Formula:** $I = \dfrac{P}{4\pi r^2}$ and $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, so $L = 10\,\text{dB} \cdot \lg \dfrac{P}{4\pi r^2 I_0}$
**Conversions:** Not needed: the power is in watts and the distance in metres.
**Substitution:** $I = \dfrac{0.050\,\text{W}}{4\pi \cdot (3.0\,\text{m})^2} = 4.42 \cdot 10^{-4}\,\text{W/m}^2$, so $L = 10\,\text{dB} \cdot \lg \dfrac{4.42 \cdot 10^{-4}\,\text{W/m}^2}{1.0 \cdot 10^{-12}\,\text{W/m}^2} = 10\,\text{dB} \cdot \lg (4.42 \cdot 10^{8}) = 86.45\,\text{dB}$
**Answer:** $86\,\text{dB}$, in whole decibels, because the power and the distance are given to two significant figures.
**Reasonableness:** The intensity is between $10^{-4}$ and $10^{-3}\,\text{W/m}^2$, so the level must be between $80$ and $90\,\text{dB}$. A portable loudspeaker playing loudly sounds a few metres away about as loud as a busy street or louder.

## fy5-15-L2-02
**Given:** lawn mower alone $L_1 = 85\,\text{dB}$, leaf blower alone $L_2 = 88\,\text{dB}$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** by how much the combined level $L$ is greater than $L_2$, that is $L - L_2$ in decibels
**Principle:** The machines are independent sound sources, so their intensities add up. Decibels cannot be added, so the levels are first converted to intensities.
**Formula:** $L - L_2 = 10\,\text{dB} \cdot \lg \dfrac{I_1 + I_2}{I_0} - L_2$, where the intensities and the combined level are
```latex
\begin{aligned}
&I_1 = I_0 \cdot 10^{\,L_1/(10\,\text{dB})} \\
&I_2 = I_0 \cdot 10^{\,L_2/(10\,\text{dB})} \\
&L = 10\,\text{dB} \cdot \lg \dfrac{I_1 + I_2}{I_0}
\end{aligned}
```
**Conversions:** Not needed: all levels are in decibels and the intensities in $\text{W/m}^2$.
**Substitution:** $I_1 = 10^{-12}\,\text{W/m}^2 \cdot 10^{8.5} = 3.16 \cdot 10^{-4}\,\text{W/m}^2$ and $I_2 = 10^{-12}\,\text{W/m}^2 \cdot 10^{8.8} = 6.31 \cdot 10^{-4}\,\text{W/m}^2$, so $L = 10\,\text{dB} \cdot \lg (9.47 \cdot 10^{8}) = 89.76\,\text{dB}$ and $L - L_2 = 89.76\,\text{dB} - 88\,\text{dB} = 1.76\,\text{dB}$
**Answer:** $1.8\,\text{dB}$, to two significant figures, because the levels are given in whole decibels.
**Reasonableness:** If the lawn mower were as loud as the leaf blower, the level would rise by $3\,\text{dB}$. A weaker source adds less, and a very weak one would add hardly anything, so $1.8\,\text{dB}$ lies between these. The combined level $89.8\,\text{dB}$ is much smaller than the incorrect sum $173\,\text{dB}$.

## fy5-15-L2-03
**Given:** level $L_1 = 85\,\text{dB}$ at distance $r_1 = 3.0\,\text{m}$, new distance $r_2 = 12\,\text{m}$; the sound spreads evenly and is not reflected
**Find:** the level $L_2$ at distance $r_2$ in decibels
**Principle:** The intensity of a point source is inversely proportional to the square of the distance, because the same power is spread over a spherical surface $4\pi r^2$. The difference in levels is obtained from the ratio of the intensities.
**Formula:** $\dfrac{I_2}{I_1} = \dfrac{r_1^2}{r_2^2}$ and $L_2 - L_1 = 10\,\text{dB} \cdot \lg \dfrac{I_2}{I_1}$, so $L_2 = L_1 + 10\,\text{dB} \cdot \lg \dfrac{r_1^2}{r_2^2}$
**Conversions:** Not needed: both distances are in metres, and the units cancel.
**Substitution:** $\dfrac{r_1^2}{r_2^2} = \dfrac{(3.0\,\text{m})^2}{(12\,\text{m})^2} = \dfrac{1}{16}$, so $L_2 = 85\,\text{dB} + 10\,\text{dB} \cdot \lg \dfrac{1}{16} = 85\,\text{dB} - 12.04\,\text{dB} = 72.96\,\text{dB}$
**Answer:** $73\,\text{dB}$, in whole decibels like the initial level $85\,\text{dB}$.
**Reasonableness:** The distance doubles twice ($3\,\text{m} \to 6\,\text{m} \to 12\,\text{m}$), and each doubling lowers the level by about $6\,\text{dB}$: $85\,\text{dB} - 6\,\text{dB} - 6\,\text{dB} = 73\,\text{dB}$. The level decreases, as it should farther from the source.

## fy5-15-L2-04
**Given:** one saw $L_1 = 85\,\text{dB}$, all saws together $L = 91\,\text{dB}$, the saws are identical and equally far from the meter
**Find:** the number of saws $N$
**Principle:** The intensities of independent sources add up. When $N$ identical saws are running, the intensity is $N$ times as great, so the difference in levels tells the ratio $N$ of the intensities.
**Formula:** $L - L_1 = 10\,\text{dB} \cdot \lg \dfrac{N I_1}{I_1} = 10\,\text{dB} \cdot \lg N$, so $\lg N = \dfrac{L - L_1}{10\,\text{dB}}$ and $N = 10^{\,(L - L_1)/(10\,\text{dB})}$
**Conversions:** Not needed: the levels are in decibels, and the decibels cancel.
**Substitution:** $N = 10^{\,(91\,\text{dB} - 85\,\text{dB})/(10\,\text{dB})} = 10^{0.6} = 3.98$
**Answer:** $4$ saws; the number is a whole number, and $3.98$ rounds to it, because the levels are given in whole decibels.
**Reasonableness:** Two saws would raise the level by $3\,\text{dB}$ and four by $6\,\text{dB}$, that is $85\,\text{dB} + 6\,\text{dB} = 91\,\text{dB}$. This matches the given level, so four saws is the right number.

## fy5-15-L2-08
**Find:** how many times as great the sound intensity is on the street ($82\,\text{dB}$) as in the living room ($42\,\text{dB}$), as an order of magnitude
**Principle:** The difference of the levels of two sounds depends only on the ratio of the intensities, because the threshold of hearing $I_0$ cancels: $L_2 - L_1 = 10\,\text{dB} \cdot \lg \tfrac{I_2}{I_1}$. The scale is logarithmic: whenever the intensity becomes ten times as great, $10\,\text{dB}$ is added to the level.
**Model answer:** The intensity on the street is about $10^{4}$ times as great. The difference of the levels is

$L_2 - L_1 = 82\,\text{dB} - 42\,\text{dB}$

$L_2 - L_1 = 40\,\text{dB}$

Divide the difference by $10\,\text{dB}$:

$\lg \dfrac{I_2}{I_1} = \dfrac{40\,\text{dB}}{10\,\text{dB}} = 4$

From the definition of the logarithm we get

$\dfrac{I_2}{I_1} = 10^{4}$

So the intensity on the street is about $10\,000$ times as great. The ratio $2$ results when the decibel readings are compared like ordinary numbers, the ratio $40$ when the difference is read directly as the ratio, and the ratio $10^{40}$ when the difference is not divided by $10\,\text{dB}$.

## fy5-15-L3-01
**Given:** spectators $N = 12\,000$, level of one shout at the centre of the rink $L_1 = 42\,\text{dB}$, level of the public address system alone $L_K = 80\,\text{dB}$; the shouts are equally strong and all sources are independent
**Find:** the combined level $L$ of all the sounds in decibels
**Principle:** The intensities of independent sources add up, the decibels do not. First the combined level of the shouts is calculated: when each shout produces the same intensity $I_1$, the intensity of the shouts is $N I_1$. Then the intensities of the shouts and of the public address system are added.
**Formula:** shouts together $L_H = L_1 + 10\,\text{dB} \cdot \lg N$, and the whole sound
```latex
\begin{aligned}
&L = 10\,\text{dB} \cdot \lg \frac{I_H + I_K}{I_0} \\
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})}
\end{aligned}
```
**Conversions:** Not needed: the levels are in decibels, $N$ is a plain number and the intensities are in $\text{W/m}^2$.
**Substitution:** $L_H = 42\,\text{dB} + 10\,\text{dB} \cdot \lg 12\,000 = 42\,\text{dB} + 40.79\,\text{dB} = 82.79\,\text{dB}$, so $I_H = 10^{-12}\,\text{W/m}^2 \cdot 10^{8.279} = 1.90 \cdot 10^{-4}\,\text{W/m}^2$ and $I_K = 10^{-12}\,\text{W/m}^2 \cdot 10^{8} = 1.0 \cdot 10^{-4}\,\text{W/m}^2$, so $L = 10\,\text{dB} \cdot \lg \dfrac{2.90 \cdot 10^{-4}\,\text{W/m}^2}{1.0 \cdot 10^{-12}\,\text{W/m}^2} = 84.63\,\text{dB}$
**Answer:** $85\,\text{dB}$, in whole decibels, because the levels are given in whole decibels.
**Reasonableness:** $10\,000$ sources would add exactly $40\,\text{dB}$ to the level, so the shouts alone are about $83\,\text{dB}$. The public address system is quieter than the shouts, so it raises the combined level by less than $3\,\text{dB}$, and $2\,\text{dB}$ fits. The sum of the decibels $12\,000 \cdot 42\,\text{dB} + 80\,\text{dB}$ would be absurd. In a real hall reflections raise the level still more.

## fy5-15-L3-02
**Given:** level $L_1 = 30\,\text{dB}$ at distance $r_1 = 0.50\,\text{m}$, level of the threshold of hearing $L_2 = 0\,\text{dB}$; a point source, even spreading, no reflections, absorption or background sounds
**Find:** the distance $r_2$ at which the level is $0\,\text{dB}$, in metres
**Principle:** The intensity of a point source is inversely proportional to the square of the distance. The difference in levels tells by what factor the intensity must decrease, and from it the ratio of the distances is obtained.
**Formula:** $L_1 - L_2 = 10\,\text{dB} \cdot \lg \dfrac{I_1}{I_2} = 10\,\text{dB} \cdot \lg \dfrac{r_2^2}{r_1^2}$, so $\dfrac{r_2^2}{r_1^2} = 10^{\,(L_1 - L_2)/(10\,\text{dB})}$ and $r_2 = r_1 \sqrt{10^{\,(L_1 - L_2)/(10\,\text{dB})}}$
**Conversions:** Not needed: the distance is in metres, and the decibels cancel.
**Substitution:** $r_2 = 0.50\,\text{m} \cdot \sqrt{10^{\,(30\,\text{dB} - 0\,\text{dB})/(10\,\text{dB})}} = 0.50\,\text{m} \cdot \sqrt{1000} = 0.50\,\text{m} \cdot 31.6 = 15.8\,\text{m}$
**Answer:** $16\,\text{m}$, two significant figures like the distance $0.50\,\text{m}$.
**Reasonableness:** A drop of $30\,\text{dB}$ means the intensity falls to a thousandth, and a distance $\sqrt{1000} \approx 32$ times as great does this. In reality the whine cannot be heard from so far away, because background sounds mask it and one's own threshold of hearing may be higher; the result is an upper limit for an ideal situation.

## fy5-15-L3-03
**Find:** whether a negative sound intensity level is impossible, what it means, and whether the fan can be heard
**Principle:** The sound intensity level $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$ is not an intensity but a comparison with the threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$. A logarithm is negative when its argument is positive but less than one.
**Model answer:** The student is not right. A negative level does not mean a negative intensity but that the intensity is smaller than the threshold of hearing: $\lg \dfrac{I}{I_0} = -0.5$, so
```latex
I = I_0 \cdot 10^{-0.5} \approx 3.2 \cdot 10^{-13}\,\text{W/m}^2
```
It is positive, about a third of the threshold of hearing. Every time the intensity decreases to a tenth, the level falls by $10\,\text{dB}$, so for sounds weaker than the threshold of hearing the level is negative, even though the intensity is always positive. The average listener cannot hear the fan, because the sound is below the threshold of hearing. The threshold of hearing $I_0$ is, however, an agreed reference value: the threshold of hearing varies from person to person and from frequency to frequency, and young, sensitive-eared people can hear sounds slightly below $0\,\text{dB}$ at the most sensitive frequencies, around $3000\,\text{Hz}$. In a quiet anechoic room the measurement is therefore quite possible.

**Self-assessment:** In my answer I

- say that the intensity is always positive and a negative level means an intensity smaller than the threshold of hearing $I_0$
- calculate or estimate the intensity from the level $-5\,\text{dB}$ as the power $10^{-0.5}$
- say that the threshold of hearing depends on the person and the frequency, so the fan can be heard only by the most sensitive listeners at the most sensitive frequencies.


## fy5-15-L1-06
**Find:** what a sound intensity level of $0\,\text{dB}$ means
**Principle:** The sound intensity level is $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, so it compares the intensity with the threshold of hearing $I_0$. The level is zero when the argument of the logarithm is $1$.
**Model answer:** The correct option is the one according to which the intensity is $I_0$, because then $\lg(I/I_0) = \lg 1 = 0$. A level of $0\,\text{dB}$ is therefore the threshold of hearing, the weakest sound that a listener can just barely perceive, not silence. The option that says there is no sound is wrong, because the logarithm of zero does not exist and the intensity $I = 0$ gives no level. The option about the threshold of pain is wrong, because the threshold of pain is many times the threshold of hearing, that is, at the upper end of the scale. The option that says zero is the lower limit of the scale is wrong, because for weaker sounds the quotient $I/I_0$ is less than $1$ and the level is negative.

## fy5-15-L1-07
**Find:** what the error is in the calculation in which the combined level of two $64\,\text{dB}$ machines comes out as $128\,\text{dB}$
**Principle:** The intensities of independent sound sources are added, and the combined level is calculated from the total intensity. Decibels are a logarithmic scale, so they cannot be added.
**Model answer:** The error is that the student adds the decibels. Two identical machines double the intensity, and doubling the intensity raises the level by only $10\,\text{dB} \cdot \lg 2 \approx 3.0\,\text{dB}$, so the combined level is about $67\,\text{dB}$. The claim that each machine would add three decibels and the level would be $70\,\text{dB}$ is wrong, because the increase of three decibels applies to the whole combined level only once. The claim about the average $64\,\text{dB}$ is wrong, because the second machine adds sound. The claim about a tenfold intensity and a level of $74\,\text{dB}$ is wrong, because two machines give only twice the intensity; an increase of $10\,\text{dB}$ would require ten machines.

## fy5-15-L1-08
**Given:** intensity at the threshold of pain $I = 1.0\,\text{W/m}^2$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** the sound intensity level $L$ in decibels
**Principle:** The sound intensity level is obtained by comparing the intensity with the threshold of hearing $I_0$ on a logarithmic scale.
**Formula:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$
**Conversions:** Not needed: both intensities are in $\text{W/m}^2$, so the units cancel in the quotient.
**Substitution:** the quotient is $I/I_0 = 10^{12}$, so
```latex
\begin{aligned}
L &= 10\,\text{dB} \cdot \lg \dfrac{1.0\,\text{W/m}^2}{1.0 \cdot 10^{-12}\,\text{W/m}^2} \\
&= 10\,\text{dB} \cdot \lg 10^{12} \\
&= 120\,\text{dB}
\end{aligned}
```
**Answer:** $120\,\text{dB}$, two significant figures like the threshold of pain $1.0\,\text{W/m}^2$.
**Reasonableness:** The ratio of the intensities is $10^{12}$, and every tenfold increase raises the level by $10\,\text{dB}$, so $12 \cdot 10\,\text{dB} = 120\,\text{dB}$. This matches the common knowledge that $120\,\text{dB}$ is the level near a jet aircraft and hurts the ear.

## fy5-15-L2-05
**Given:** from the table the distances $1.0\,\text{m}$, $2.0\,\text{m}$, $4.0\,\text{m}$, $8.0\,\text{m}$ and $16\,\text{m}$ and the levels $84.2\,\text{dB}$, $78.1\,\text{dB}$, $72.3\,\text{dB}$, $66.2\,\text{dB}$ and $60.1\,\text{dB}$
**Find:** the average drop in level $\Delta L_1$ per doubling of the distance, in decibels
**Principle:** Each measuring point is twice the previous one, so the distances are $1.0\,\text{m} \to 2.0\,\text{m} \to 4.0\,\text{m} \to 8.0\,\text{m} \to 16\,\text{m}$, so there are $n = 4$ doublings. The average drop is obtained by dividing the total change in level by $n$.
**Formula:** $\Delta L_1 = \dfrac{L(1.0\,\text{m}) - L(16\,\text{m})}{n}$
**Conversions:** Not needed: the levels are in decibels, and $n$ is a plain number.
**Substitution:** there are $n = 4$ doublings, so
```latex
\begin{aligned}
\Delta L_1 &= \dfrac{84.2\,\text{dB} - 60.1\,\text{dB}}{4} \\
&= \dfrac{24.1\,\text{dB}}{4} \\
&= 6.025\,\text{dB}
\end{aligned}
```
**Answer:** $6.03\,\text{dB}$, three significant figures like the meter readings; the division by $4$ is exact.
**Reasonableness:** The point source model predicts that doubling the distance reduces the intensity to a quarter, so the level drops by $10\,\text{dB} \cdot \lg 4 = 6.02\,\text{dB}$. The measured average drop $6.03\,\text{dB}$ is practically the same, and the individual drops $6.1\,\text{dB}$, $5.8\,\text{dB}$, $6.1\,\text{dB}$ and $6.1\,\text{dB}$ vary only by the measurement error. An open field therefore works as a point source model.

## fy5-15-L2-06
**Given:** from the table $L(1.0\,\text{m}) = 86.0\,\text{dB}$ and $L(8.0\,\text{m}) = 71.9\,\text{dB}$; the distance increases by the factor $\dfrac{8.0\,\text{m}}{1.0\,\text{m}} = 8.0$
**Find:** the difference between the measured level $L_\text{obs}$ and the prediction of the point source model $L_\text{mod}$, $L_\text{obs} - L_\text{mod}$, in decibels
**Principle:** If the sound travelled from a point source without reflections, the intensity would be inversely proportional to the square of the distance, and the difference in levels would depend only on the ratio of the distances. The prediction is calculated from the reading at $1.0\,\text{m}$ and compared with the measurement.
**Formula:** $\Delta L = L_\text{obs} - L_\text{mod}$, where the prediction is
```latex
L_\text{mod} = L_1 - 10\,\text{dB} \cdot \lg \left[\left(\dfrac{r_2}{r_1}\right)^{2}\right]
```
**Conversions:** Not needed: the distances are in metres and the ratio has no unit.
**Substitution:** the ratio of the distances is $8.0$, so
```latex
\begin{aligned}
L_\text{mod} &= 86.0\,\text{dB} - 10\,\text{dB} \cdot \lg 64 \\
&= 86.0\,\text{dB} - 18.06\,\text{dB} \\
&= 67.94\,\text{dB} \\
L_\text{obs} - L_\text{mod} &= 71.9\,\text{dB} - 67.94\,\text{dB} \\
&= 3.96\,\text{dB}
\end{aligned}
```
**Answer:** $4.0\,\text{dB}$, two significant figures, because the readings of the difference are given to a tenth of a decibel and the prediction is rounded. The prediction of part a) is about $67.9\,\text{dB}$.
**Reasonableness:** A level $3.96\,\text{dB}$ higher means that the measured intensity is about $10^{0.396} = 2.5$ times that of the model. Explanation: the walls, ceiling and floor of the hall reflect the sound, so in addition to the direct sound, reflected sound arrives at the listening position. The direct sound weakens with distance, but the reflected sound does not nearly as much, so the difference grows farther away: the measured drops $5.9\,\text{dB}$, $5.1\,\text{dB}$ and $3.1\,\text{dB}$ remain smaller than the $6.0\,\text{dB}$ of a point source.

## fy5-15-L2-07
**Given:** from the table the levels of the reference meter $50.0\,\text{dB}$, $60.0\,\text{dB}$, $70.0\,\text{dB}$ and $80.0\,\text{dB}$ and the readings of the phone $54.1\,\text{dB}$, $63.8\,\text{dB}$, $74.2\,\text{dB}$ and $83.9\,\text{dB}$; in addition $90.0\,\text{dB}$ and $88.6\,\text{dB}$
**Find:** the factor $k = \dfrac{I_\text{phone}}{I_\text{ref}}$, that is, by what factor the phone overestimates the intensity
**Principle:** The error of the phone $\Delta L = L_\text{phone} - L_\text{ref}$ is almost the same at the four lowest levels, so it is a systematic error. The difference in levels depends only on the ratio of the intensities, so the ratio of the intensities can be obtained from the mean error.
**Formula:** $\Delta L_\text{avg} = \dfrac{\Sigma \Delta L}{4}$ and $\Delta L_\text{avg} = 10\,\text{dB} \cdot \lg k$, so
```latex
k = 10^{\,\Delta L_\text{avg}/(10\,\text{dB})}
```
**Conversions:** Not needed: all levels are in decibels, and the ratio $k$ has no unit.
**Substitution:** The errors are $4.1\,\text{dB}$, $3.8\,\text{dB}$, $4.2\,\text{dB}$ and $3.9\,\text{dB}$. Their sum is $16.0\,\text{dB}$, so
```latex
\begin{aligned}
\Delta L_\text{avg} &= \dfrac{16.0\,\text{dB}}{4} \\
&= 4.0\,\text{dB} \\
k &= 10^{\,4.0\,\text{dB}/(10\,\text{dB})} \\
&= 2.51
\end{aligned}
```
**Answer:** $2.5$, two significant figures like the mean error $4.0\,\text{dB}$. The phone exceeds the level by $4.0\,\text{dB}$ on average, that is, it estimates the intensity to be about $2.5$ times too great. Result of part c): at $90.0\,\text{dB}$ the error would be expected to be $+4\,\text{dB}$, but the phone shows $1.4\,\text{dB}$ too little, so the reading does not follow the others; the microphone probably saturates (overloads) at a loud sound.
**Reasonableness:** Three decibels would correspond to double the intensity and five decibels to an intensity $10^{0.5} = 3.2$ times as great, so $4.0\,\text{dB}$ gives a number between $2$ and $3.2$, and $2.5$ is one. A systematic error is corrected by subtracting about $4\,\text{dB}$ from the readings, but the correction is valid only in the measured range $50\,\text{dB}$–$80\,\text{dB}$.

## fy5-15-L3-04
**Given:** from the table the distances $5.0\,\text{m}$, $10.0\,\text{m}$, $20.0\,\text{m}$ and $40.0\,\text{m}$ and the levels $91.1\,\text{dB}$, $84.8\,\text{dB}$, $79.3\,\text{dB}$ and $72.6\,\text{dB}$; limit $L_\text{limit} = 55\,\text{dB}$ and threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$; point source, even spreading, no reflections or attenuation
**Find:** a) the sound power $P$ of the loudspeaker and b) the distance $r$ at which the level is $55\,\text{dB}$, in metres
**Principle:** The intensity is calculated from each reading using the level equation, and for a point source $I = \dfrac{P}{4\pi r^2}$ gives the power $P = I \cdot 4\pi r^2$. Because the readings contain measurement error, the power is the mean of all the values. When the power is known, the same formula is solved for the distance at which the intensity corresponds to the limit level.
**Formula:** $r = \sqrt{\dfrac{P}{4\pi I_\text{limit}}}$, where the power and the intensities are
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\
&P = I \cdot 4\pi r^2
\end{aligned}
```
**Conversions:** Not needed: the distances are in metres and the intensities in $\text{W/m}^2$.
**Substitution:** From the readings the intensities are $1.288 \cdot 10^{-3}\,\text{W/m}^2$, $3.020 \cdot 10^{-4}\,\text{W/m}^2$, $8.51 \cdot 10^{-5}\,\text{W/m}^2$ and $1.820 \cdot 10^{-5}\,\text{W/m}^2$, and the powers $0.4047\,\text{W}$, $0.3795\,\text{W}$, $0.4278\,\text{W}$ and $0.3659\,\text{W}$. The sum of the powers is $1.578\,\text{W}$, so the mean is $P = 0.3945\,\text{W}$. The intensity at the limit level is $I_\text{limit} = 1.0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{5.5} = 3.162 \cdot 10^{-7}\,\text{W/m}^2$, and
```latex
\begin{aligned}
r &= \sqrt{\dfrac{0.3945\,\text{W}}{4\pi \cdot 3.162 \cdot 10^{-7}\,\text{W/m}^2}} \\
&= \sqrt{9.93 \cdot 10^{4}\,\text{m}^2} \\
&= 315\,\text{m} \approx 3.2 \cdot 10^{2}\,\text{m}
\end{aligned}
```
**Answer:** The result of part b) is $3.2 \cdot 10^{2}\,\text{m}$, two significant figures, because the limit $55\,\text{dB}$ is given in whole decibels and $\pm 0.5\,\text{dB}$ changes the distance between $297\,\text{m}$ and $334\,\text{m}$; the sound power of part a) is about $0.39\,\text{W}$.
**Reasonableness:** The level drops by $6.0\,\text{dB}$ with every doubling of the distance. From the level $72.6\,\text{dB}$ at $40\,\text{m}$ to the level $55\,\text{dB}$ is about $17.6\,\text{dB}$, that is, about $2.9$ doublings, so the distance is about $40\,\text{m} \cdot 2^{2.9} \approx 300\,\text{m}$, which fits the result $3.2 \cdot 10^{2}\,\text{m}$. **Justification (part c):** A single reading contains measurement error: the power estimates vary between $0.366\,\text{W}$ and $0.428\,\text{W}$, so the mean evens out the error. Over a long distance, the attenuation of sound by air, attenuation by the ground and vegetation, wind and temperature layers, and reflections from buildings can differ from the model, because the model does not include them; the real level may be lower or higher than the model predicts (attenuation by air and ground usually lowers it, reflections raise it), so the result $3.2 \cdot 10^{2}\,\text{m}$ is an estimate.

## fy5-15-L3-05
**Given:** power of the guitar amplifier $P_1 = 0.20\,\text{W}$, level of the drum kit $L_2 = 90\,\text{dB}$ at distance $r_2 = 2.0\,\text{m}$, distance of the listener $r = 8.0\,\text{m}$, target level $L_\text{limit} = 70\,\text{dB}$ and $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$; the sources are in the same place, independent and point sources
**Find:** a) the combined level $L$ at a distance of $8.0\,\text{m}$ and b) the distance $r_\text{limit}$ at which the combined level is $70\,\text{dB}$, in metres
**Principle:** The sources are independent, so their intensities are added. The intensity of the amplifier is obtained from the power with the formula $I = \dfrac{P}{4\pi r^2}$, and that of the drums from the level using the level equation and the effect of doubling the distance. Both intensities decrease like $\dfrac{1}{r^2}$, so the total intensity does too, and the distance is obtained from the ratio.
**Formula:** $r_\text{limit} = r \sqrt{\dfrac{I}{I_\text{limit}}}$, where the total intensity and the level are
```latex
\begin{aligned}
&I = I_1 + I_2 \\
&L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}
\end{aligned}
```
**Conversions:** Not needed: the distances are in metres and the levels in decibels.
**Substitution:** Amplifier: $I_1 = \dfrac{0.20\,\text{W}}{4\pi \cdot (8.0\,\text{m})^2} = 2.487 \cdot 10^{-4}\,\text{W/m}^2$. Drums: from the level $90\,\text{dB}$ nearby we get $I = 10^{-12}\,\text{W/m}^2 \cdot 10^{9} = 1.0 \cdot 10^{-3}\,\text{W/m}^2$ at a distance of $2.0\,\text{m}$, and at a distance of $8.0\,\text{m}$ the intensity is $\left(\dfrac{2.0}{8.0}\right)^2 = \dfrac{1}{16}$ of that, that is, $I_2 = 6.25 \cdot 10^{-5}\,\text{W/m}^2$. Thus
```latex
\begin{aligned}
I &= 2.487 \cdot 10^{-4}\,\text{W/m}^2 \\
&\quad + 6.25 \cdot 10^{-5}\,\text{W/m}^2 \\
&= 3.112 \cdot 10^{-4}\,\text{W/m}^2 \\
L &= 10\,\text{dB} \cdot \lg \dfrac{3.112 \cdot 10^{-4}}{10^{-12}} \\
&= 84.93\,\text{dB}
\end{aligned}
```
The level $70\,\text{dB}$ corresponds to $I_\text{limit} = 10^{-12}\,\text{W/m}^2 \cdot 10^{7} = 1.0 \cdot 10^{-5}\,\text{W/m}^2$, so
```latex
\begin{aligned}
r_\text{limit} &= 8.0\,\text{m} \cdot \sqrt{\dfrac{3.112 \cdot 10^{-4}}{1.0 \cdot 10^{-5}}} \\
&= 8.0\,\text{m} \cdot 5.579 \\
&= 44.6\,\text{m}
\end{aligned}
```
**Answer:** The result of part b) is $45\,\text{m}$, two significant figures like the power $0.20\,\text{W}$ and the distance $8.0\,\text{m}$; the combined level of part a) is about $85\,\text{dB}$.
**Reasonableness:** The level drops from the combined level $84.9\,\text{dB}$ to $70\,\text{dB}$, that is, by $14.9\,\text{dB}$, which is about $2.5$ doublings of the distance ($6.0\,\text{dB}$ each), and $8.0\,\text{m} \cdot 2^{2.5} \approx 45\,\text{m}$. The combined level is greater than either source alone ($84.0\,\text{dB}$ and $78.0\,\text{dB}$) but smaller than the sum of their decibels. **Justification (part c):** The range of intensities of hearing is enormous: from the threshold of hearing to the threshold of pain the intensity grows by a factor of $10^{12}$. The logarithmic scale compresses this range into the numbers $0\,\text{dB}$–$120\,\text{dB}$, and hearing distinguishes roughly relative differences, so the same factor of intensity, for example doubling, feels like roughly the same change (about $3\,\text{dB}$) at a quiet and at a loud sound.

## fy5-15-L1-09
**Given:** from the figure the level at the distance $r = 4.0\,\text{m}$, the hearing threshold $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** the intensity $I$ in $\text{W/m}^2$
**Principle:** The level is ten times the logarithm of the ratio of the intensities. The intensity is obtained by dividing the equation by $10\,\text{dB}$ and using the definition of the logarithm: if $\lg x = y$, then $x = 10^y$.
**Reading the figure:** At the distance $4.0\,\text{m}$ the marked point is at the level $L = 74.0\,\text{dB}$.
**Formula:** $L = 10\,\text{dB} \cdot \lg \dfrac{I}{I_0}$, so $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$
**Conversions:** None are needed: $\dfrac{L}{10\,\text{dB}} = \dfrac{74.0\,\text{dB}}{10\,\text{dB}} = 7.40$, the decibels cancel.
**Substitution:** $I = 1.0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{7.40} = 2.51 \cdot 10^{-5}\,\text{W/m}^2$
**Answer:** $2.5 \cdot 10^{-5}\,\text{W/m}^2$, that is $0.000025\,\text{W/m}^2$, two significant figures like the hearing threshold $1.0 \cdot 10^{-12}\,\text{W/m}^2$.
**Reasonableness:** $70\,\text{dB}$ corresponds to the intensity $10^{-5}\,\text{W/m}^2$ and $80\,\text{dB}$ to $10^{-4}\,\text{W/m}^2$, so the intensity of $74\,\text{dB}$ must lie between them, nearer the lower one. At $r = 2.0\,\text{m}$ in the figure, at $80\,\text{dB}$, the intensity is $1.0 \cdot 10^{-4}\,\text{W/m}^2$, and at double the distance it is a quarter of that, $2.5 \cdot 10^{-5}\,\text{W/m}^2$, as it should be.

## fy5-15-L2-09
**Given:** from the figure the level at the distance $r = 2.0\,\text{m}$; the sound spreads evenly in all directions, so the source is point-like, and the hearing threshold is $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
**Find:** the sound power $P$ in $\text{mW}$
**Principle:** The sound power of a point source is spread evenly over a spherical surface of area $4\pi r^2$, so $I = \dfrac{P}{4\pi r^2}$. From the level read from the figure we first calculate the intensity and then the sound power.
**Reading the figure:** At the distance $2.0\,\text{m}$ the marked point is at the level $L = 80.0\,\text{dB}$.
**Formula:** $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$ and $I = \dfrac{P}{4\pi r^2}$, so $P = 4\pi r^2 I$
**Conversions:** $\dfrac{L}{10\,\text{dB}} = 8.00$. The result comes out in watts, and $1\,\text{W} = 1000\,\text{mW}$.
**Substitution:** $I = 1.0 \cdot 10^{-12}\,\text{W/m}^2 \cdot 10^{8.00} = 1.0 \cdot 10^{-4}\,\text{W/m}^2$, and $P = 4\pi \cdot (2.0\,\text{m})^2 \cdot 1.0 \cdot 10^{-4}\,\text{W/m}^2 = 5.03 \cdot 10^{-3}\,\text{W} = 5.03\,\text{mW}$
**Answer:** $5.0\,\text{mW}$, two significant figures like the distance $2.0\,\text{m}$ read from the figure.
**Reasonableness:** The other point in the figure gives the same result: $r = 4.0\,\text{m}$ and $L = 74.0\,\text{dB}$ give $I = 2.51 \cdot 10^{-5}\,\text{W/m}^2$ and $P = 4\pi \cdot (4.0\,\text{m})^2 \cdot 2.51 \cdot 10^{-5}\,\text{W/m}^2 = 5.05\,\text{mW}$, which differs by less than $1\,\%$ from the first (reading accuracy). The power is small, as for a small loudspeaker: the electric power is many times greater because only a small part of it becomes sound.
