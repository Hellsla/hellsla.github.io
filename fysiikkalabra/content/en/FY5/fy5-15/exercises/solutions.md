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
**Given:** sound intensity level $L = 95\,\text{dB}$, threshold of hearing $I_0 = 1.0 \cdot 10^{-12}\,\text{W/m}^2$
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
