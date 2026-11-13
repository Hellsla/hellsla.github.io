## fy7-15-L1-01
**Given:** intensity of unpolarised sunlight $I_0 = 640\,\text{W/m}^2$, ideal polariser
**Find:** intensity $I_1$ of the light after the polariser, in $\text{W/m}^2$
**Principle:** In unpolarised light all directions of oscillation perpendicular to the direction of travel are equally common. Every oscillation can be split into a component along the transmission axis and a component perpendicular to it, and on average half of the intensity falls on each. An ideal polariser lets through the component along the transmission axis, so the intensity is halved whatever the position of the film.
**Formula:** $I_1 = \tfrac{1}{2} I_0$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$.
**Substitution:** $I_1 = \tfrac{1}{2} \cdot 640\,\text{W/m}^2 = 320\,\text{W/m}^2$
**Answer:** $320\,\text{W/m}^2$, two or three significant figures like the intensity $640\,\text{W/m}^2$.
**Reasonableness:** The light that comes through is polarised, and its intensity is smaller than that of the incoming light. A real film would let through slightly less, because it also absorbs a little of the light along the transmission axis.

## fy7-15-L1-02
**Given:** intensity of polarised light $I_0 = 200\,\text{W/m}^2$, angle between the direction of polarisation and the transmission axis $\theta = 30.0^\circ$
**Find:** intensity $I$ of the light after the analyser, in $\text{W/m}^2$
**Principle:** Polarised light arrives at the analyser, so Malus's law applies. The component $E_0 \cos\theta$ of the electric field along the transmission axis passes through, and the intensity is proportional to the square of the amplitude.
**Formula:** $I = I_0 \cos^2\theta$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$, and the angle is in degrees.
**Substitution:** $I = 200\,\text{W/m}^2 \cdot \cos^2 30.0^\circ = 200\,\text{W/m}^2 \cdot 0.750 = 150\,\text{W/m}^2$
**Answer:** $150\,\text{W/m}^2$, three significant figures like the angle $30.0^\circ$.
**Reasonableness:** The angle is small, so most of the light passes through, three quarters. The result is smaller than $200\,\text{W/m}^2$ and larger than the half, $100\,\text{W/m}^2$, that corresponds to the angle $45^\circ$.

## fy7-15-L1-03
**Given:** intensity of polarised light $I_0 = 80.0\,\text{W/m}^2$, angle between the direction of polarisation and the transmission axis $\theta = 70.0^\circ$
**Find:** intensity $I$ of the light after the polariser, in $\text{W/m}^2$
**Principle:** Polarised light arrives at the polariser, so the intensity of the transmitted light follows from Malus's law. Only the component $E_0 \cos\theta$ of the amplitude of the electric field along the transmission axis passes through.
**Formula:** $I = I_0 \cos^2\theta$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$, and the angle is in degrees.
**Substitution:** $I = 80.0\,\text{W/m}^2 \cdot \cos^2 70.0^\circ = 80.0\,\text{W/m}^2 \cdot 0.11698 = 9.358\,\text{W/m}^2$
**Answer:** $9.36\,\text{W/m}^2$, three significant figures like the intensity $80.0\,\text{W/m}^2$ and the angle $70.0^\circ$.
**Reasonableness:** The angle is close to $90^\circ$, where nothing would pass through, so only a small share of the light passes, about $12\,\%$. At $60^\circ$ $25\,\%$, that is $20\,\text{W/m}^2$, would pass through, and the result is smaller than that, as it should be.

## fy7-15-L1-04
**Given:** refractive index of air $n_1 = 1.00$, refractive index of acrylic $n_2 = 1.49$
**Find:** Brewster's angle $\alpha_\text{B}$ in degrees
**Principle:** Light reflected from the surface of an insulator is completely polarised when the angle of incidence is Brewster's angle. The reflected and the refracted ray are then perpendicular to each other, and Brewster's law follows from the law of refraction. The light comes from air and is reflected back into air, so $n_1$ is the refractive index of air and $n_2$ that of acrylic.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices are numbers without units, and the angle comes out in degrees.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.49}{1.00} = \tan^{-1} 1.49 = 56.13^\circ$
**Answer:** $56.1^\circ$, three significant figures like the refractive indices.
**Reasonableness:** When $n_2 > n_1$, $\tan\alpha_\text{B} > 1$, so the angle must be larger than $45^\circ$, as in the result. Check: the angle of refraction is $90^\circ - 56.13^\circ = 33.87^\circ$, and $1.00 \cdot \sin 56.13^\circ = 0.830 = 1.49 \cdot \sin 33.87^\circ$, so the law of refraction holds.

## fy7-15-L1-05
**Given:** refractive index of air $n_1 = 1.00$, refractive index of diamond $n_2 = 2.42$
**Find:** Brewster's angle $\alpha_\text{B}$ in degrees
**Principle:** Reflected light is completely polarised when the angle of incidence is Brewster's angle, at which the reflected and the refracted ray are perpendicular to each other. The light comes from air and is reflected into air, so $n_1$ is the refractive index of air and $n_2$ that of diamond.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices are numbers without units.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{2.42}{1.00} = \tan^{-1} 2.42 = 67.55^\circ$
**Answer:** $67.5^\circ$, three significant figures like the refractive indices.
**Reasonableness:** The refractive index of diamond is much larger than that of acrylic, so Brewster's angle must be larger than the $56.1^\circ$ of acrylic but smaller than $90^\circ$, as in the result. Check: $\tan 67.55^\circ = 2.42$.

## fy7-15-L2-01
**Given:** intensity of unpolarised light $I_0 = 900\,\text{W/m}^2$, angle between the transmission axes of the polarisers $\theta = 40.0^\circ$
**Find:** intensity $I_2$ after the second polariser, in $\text{W/m}^2$
**Principle:** The first polariser lets through half of the intensity of the unpolarised light, and the light that comes through is polarised along its transmission axis. The light arriving at the second polariser is therefore polarised at an angle of $40.0^\circ$ to its transmission axis, so Malus's law applies to it.
**Formula:** $I_1 = \tfrac{1}{2} I_0$ and $I_2 = I_1 \cos^2\theta$, so $I_2 = \tfrac{1}{2} I_0 \cos^2\theta$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$, and the angle is in degrees.
**Substitution:** $I_2 = \tfrac{1}{2} \cdot 900\,\text{W/m}^2 \cdot \cos^2 40.0^\circ = 450\,\text{W/m}^2 \cdot 0.5868 = 264.1\,\text{W/m}^2$
**Answer:** $264\,\text{W/m}^2$, three significant figures like the angle $40.0^\circ$.
**Reasonableness:** After the first polariser the intensity is $450\,\text{W/m}^2$. The angle $40^\circ$ is smaller than $45^\circ$, so the second polariser lets through slightly more than half of it, and $264\,\text{W/m}^2$ is slightly more than $225\,\text{W/m}^2$, as it should be.

## fy7-15-L2-02
**Given:** $25.0\,\%$ of the intensity of the polarised light arriving at the analyser passes through it, that is, $I : I_0 = 0.250$
**Find:** the angle $\theta$ between the direction of polarisation and the transmission axis, in degrees
**Principle:** Polarised light arrives at the analyser, so the share of the light that passes through follows from Malus's law. The angle is solved from the law.
**Formula:** $I = I_0 \cos^2\theta$, so $\cos\theta = \sqrt{\dfrac{I}{I_0}}$ and $\theta = \cos^{-1}\sqrt{\dfrac{I}{I_0}}$
**Conversions:** $25.0\,\% = 25.0 \cdot 0.01 = 0.250$
**Substitution:** $\theta = \cos^{-1}\sqrt{0.250} = \cos^{-1} 0.500 = 60.0^\circ$
**Answer:** $60.0^\circ$, three significant figures like the share $25.0\,\%$.
**Reasonableness:** Less than half of the light passes through, so the angle must be larger than $45^\circ$ and smaller than $90^\circ$, as in the result. Check: $\cos^2 60.0^\circ = 0.500^2 = 0.250$.

## fy7-15-L2-03
**Given:** Brewster's angle $\alpha_\text{B} = 57.5^\circ$, refractive index of air $n_1 = 1.00$
**Find:** refractive index $n_2$ of the plastic (no unit)
**Principle:** Light is reflected completely polarised when the angle of incidence is Brewster's angle. The light comes from air and is reflected into air, so in Brewster's law $n_1$ is the refractive index of air and $n_2$ that of the plastic. $n_2$ is solved from the law.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $n_2 = n_1 \tan\alpha_\text{B}$
**Conversions:** Not needed: the angle is in degrees, and the refractive indices have no units.
**Substitution:** $n_2 = 1.00 \cdot \tan 57.5^\circ = 1.00 \cdot 1.5697 = 1.5697$
**Answer:** $1.57$, three significant figures like the angle $57.5^\circ$.
**Reasonableness:** The refractive indices of transparent plastics, such as $1.49$ for acrylic and about $1.58$ for polycarbonate, are of the same order. The angle is larger than $45^\circ$, so the refractive index must be larger than $1$, as in the result.

## fy7-15-L2-04
**Given:** refractive index of air $n_1 = 1.00$, refractive index of glass $n_2 = 1.50$, the light arrives at Brewster's angle
**Find:** angle of refraction $\alpha_2$ in degrees from the normal of the surface
**Principle:** Brewster's angle follows from Brewster's law. At Brewster's angle the reflected and the refracted ray are perpendicular to each other, and the angle of reflection equals the angle of incidence. The angle of incidence and the angle of refraction therefore add up to $90^\circ$.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$ and $\alpha_\text{B} + \alpha_2 = 90^\circ$, so $\alpha_2 = 90^\circ - \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices have no units, and the angles are in degrees.
**Substitution:** $\alpha_2 = 90^\circ - \tan^{-1}\dfrac{1.50}{1.00} = 90^\circ - 56.31^\circ = 33.69^\circ$
**Answer:** $33.7^\circ$, three significant figures like the refractive indices.
**Reasonableness:** The light goes from air into glass, so it is refracted towards the normal, and the angle of refraction must be smaller than the angle of incidence $56.3^\circ$, as in the result. Check with the law of refraction: $1.00 \cdot \sin 56.31^\circ = 0.832$ and $1.50 \cdot \sin 33.69^\circ = 0.832$.

## fy7-15-L3-01
**Given:** intensity of unpolarised light $I_0 = 800\,\text{W/m}^2$, the transmission axes of the first and the last polariser are perpendicular, the transmission axis of the middle one is at an angle of $30.0^\circ$ to the first
**Find:** intensity $I_3$ of the light that passes through the last polariser, in $\text{W/m}^2$
**Principle:** The first polariser halves the unpolarised light. After that, polarised light arrives at every polariser, so Malus's law applies to each one with the angle measured from the transmission axis of the previous polariser. The middle one is at an angle of $30.0^\circ$ to the first, so it is at an angle of $90.0^\circ - 30.0^\circ = 60.0^\circ$ to the last.
**Formula:** $I_1 = \tfrac{1}{2} I_0$, $I_2 = I_1 \cos^2\theta_1$ and $I_3 = I_2 \cos^2\theta_2$, so $I_3 = \tfrac{1}{2} I_0 \cos^2\theta_1 \cos^2\theta_2$, where $\theta_1 = 30.0^\circ$ and $\theta_2 = 60.0^\circ$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$, and the angles are in degrees.
**Substitution:** $I_3 = \tfrac{1}{2} \cdot 800\,\text{W/m}^2 \cdot \cos^2 30.0^\circ \cdot \cos^2 60.0^\circ = 400\,\text{W/m}^2 \cdot 0.750 \cdot 0.250 = 75.0\,\text{W/m}^2$
**Answer:** $75.0\,\text{W/m}^2$, three significant figures like the angles $30.0^\circ$ and $60.0^\circ$.
**Reasonableness:** Without the middle polariser no light would get through. After the middle film the light is polarised at an angle of $30^\circ$, so it has a component along the transmission axis of the last film. The largest possible value, at the angle $45^\circ$, would be $400\,\text{W/m}^2 \cdot 0.5 \cdot 0.5 = 100\,\text{W/m}^2$, and the result is smaller than that, as it should be.

## fy7-15-L3-02
**Given:** refractive index of water $n_1 = 1.33$ (the light comes from water and is reflected into water), refractive index of air $n_2 = 1.00$
**Find:** the angle of incidence $\alpha_\text{B}$ in degrees at which the light reflected from the water surface back into the water is completely polarised
**Principle:** Reflected light is completely polarised at Brewster's angle, at which the reflected and the refracted ray are perpendicular to each other. In Brewster's law $n_1$ is the refractive index of the substance from which the light comes and into which it is reflected, here water, and $n_2$ that of the substance into which the light is refracted, here air. A refracted ray exists only if the angle of incidence is smaller than the critical angle, $\sin\alpha_\text{r} = n_2 : n_1$.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices have no units, and the angle comes out in degrees.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.00}{1.33} = \tan^{-1} 0.7519 = 36.94^\circ$
**Answer:** $36.9^\circ$, three significant figures like the refractive indices.
**Reasonableness:** The critical angle is $\sin^{-1}(1.00 : 1.33) = 48.8^\circ$, and $36.9^\circ$ is smaller than that, so part of the light is refracted into the air and Brewster's angle exists. The angle of refraction in the air is $90^\circ - 36.94^\circ = 53.06^\circ$, which is Brewster's angle for light going from air into water: the path of a ray is reversible.

## fy7-15-L3-03
**Given:** reading $E_\text{max} = 420\,\text{lx}$ when the film is aligned with the polarisation of the display; reading $E_\text{b} = 16\,\text{lx}$ when the film has been turned by $90.0^\circ$ (background light); angle of rotation $\theta = 60.0^\circ$
**Find:** the reading $E$ of the sensor in lux at the angle $60.0^\circ$
**Principle:** The reading is the sum of the share of the polarised light of the display and the background light. At $90^\circ$ no light of the display passes through, so the reading $16\,\text{lx}$ is background light alone. The share of the light of the display is at most $E_\text{max} - E_\text{b}$, and according to Malus's law it decreases by the factor $\cos^2\theta$. The reading is proportional to the intensity, so Malus's law also applies to the reading.
**Formula:** $E = (E_\text{max} - E_\text{b}) \cos^2\theta + E_\text{b}$
**Conversions:** Not needed: the readings are in lux, and the angle is in degrees.
**Substitution:** $E = (420\,\text{lx} - 16\,\text{lx}) \cdot \cos^2 60.0^\circ + 16\,\text{lx} = 404\,\text{lx} \cdot 0.250 + 16\,\text{lx} = 117\,\text{lx}$
**Answer:** $117\,\text{lx}$, three significant figures like the reading $420\,\text{lx}$.
**Reasonableness:** Without the background light the result would be $420\,\text{lx} \cdot 0.250 = 105\,\text{lx}$. The share of the background light does not change as the film is turned, so the reading must be slightly larger, as in the result. The result lies between the largest reading and the background light, as it should.

## fy7-15-L1-06
**Find:** why polarised sunglasses reduce especially the glare reflected from the surface of water.
**Principle:** Light reflected from the surface of a dielectric such as water is partially polarised along the surface, so the glare from the surface of the water is polarised in the horizontal direction. A polariser lets through only the component of the electric field along its transmission axis and absorbs the component perpendicular to it. The transmission axis means the direction of oscillation of the electric field, not the direction in which the light travels.
**Model answer:** Light reflected from the surface of water is partially polarised in the horizontal direction. The transmission axis of the film in the glasses is vertical, so the film absorbs the horizontal oscillation and lets through only the vertical one. In this way the glare is dimmed much more than other light. If the film were tilted, it would let horizontally polarised light through, which is why the orientation of the glasses matters. Mere tinting would not separate glare from other light, and the transmission axis does not limit the direction in which the light travels.

## fy7-15-L1-07
**Given:** intensity of the polarised light $I_0 = 300\,\text{W/m}^2$, angle between the polarisation direction and the transmission axis $\theta = 55.0^\circ$
**Find:** intensity $I$ of the light after the film, in $\text{W/m}^2$
**Principle:** Polarised light arrives at the film, so Malus's law applies. Only the component of the electric field along the transmission axis, $E_0 \cos\theta$, passes through, and the intensity is proportional to the square of the amplitude.
**Formula:** $I = I_0 \cos^2\theta$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$, and the angle is in degrees.
**Substitution:** $I = 300\,\text{W/m}^2 \cdot \cos^2 55.0^\circ = 300\,\text{W/m}^2 \cdot 0.3290 = 98.70\,\text{W/m}^2$
**Answer:** $98.7\,\text{W/m}^2$, three significant figures like the angle $55.0^\circ$.
**Reasonableness:** The angle $55^\circ$ is larger than $45^\circ$, at which half would pass through, that is $150\,\text{W/m}^2$, and smaller than $60^\circ$, at which a quarter would pass through, that is $75\,\text{W/m}^2$. The result $98.7\,\text{W/m}^2$ lies between these, about a third of the incident light.

## fy7-15-L1-08
**Given:** refractive index of air $n_1 = 1.00$, refractive index of quartz glass $n_2 = 1.46$
**Find:** Brewster's angle $\alpha_\text{B}$ in degrees
**Principle:** Reflected light is completely polarised when the angle of incidence is Brewster's angle, at which the reflected and the refracted ray are perpendicular to each other. The light comes from air and is reflected back into air, so $n_1$ is the refractive index of air and $n_2$ that of quartz glass.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices are numbers without units, and the angle comes out in degrees.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.46}{1.00} = \tan^{-1} 1.46 = 55.59^\circ$
**Answer:** $55.6^\circ$, three significant figures like the refractive indices.
**Reasonableness:** The refractive index of quartz glass is larger than that of water, $1.33$, and smaller than that of acrylic, $1.49$, so the angle must lie between the $53.1^\circ$ of water and the $56.1^\circ$ of acrylic, as in the result. Check: $\tan 55.59^\circ = 1.46$.

## fy7-15-L1-09
**Find:** the order of situations A–E by the intensity $I$ passing through the last polariser, from the smallest to the largest.
**Principle:** An ideal polariser lets through half of the intensity of unpolarised light, whatever its position. For polarised light Malus's law $I = I_0 \cos^2\theta$ applies, where $\theta$ is the angle between the polarisation direction of the light and the transmission direction. The light that has passed through a polariser is polarised in its transmission direction, so the angle of the next polariser is measured from that.
**Model answer:** The intensities:

$I_\text{A} = 600\,\text{W/m}^2 \cdot \cos^2 60.0^\circ$, that is $I_\text{A} = 150\,\text{W/m}^2$

$I_\text{B} = \tfrac{1}{2} \cdot 400\,\text{W/m}^2 = 200\,\text{W/m}^2$

$I_\text{C} = 320\,\text{W/m}^2 \cdot \cos^2 30.0^\circ$, that is $I_\text{C} = 240\,\text{W/m}^2$

$I_\text{D} = \tfrac{1}{2} \cdot 800\,\text{W/m}^2 \cdot \cos^2 60.0^\circ$, that is $I_\text{D} = 100\,\text{W/m}^2$

In situation E, after the first polariser the light is polarised in its transmission direction, and the second polariser is at an angle of $45.0^\circ$ to it:

$$\begin{aligned}
&I_\text{E} = 500\,\text{W/m}^2 \cdot \left(\cos^2 45.0^\circ\right)^2 \\
&I_\text{E} = 125\,\text{W/m}^2
\end{aligned}$$

From the smallest intensity to the largest, the order is D, E, A, B, C.

If the factor $\cos\theta$ were taken without the square, the intensity of situation A would be $300\,\text{W/m}^2$ and the order would change. If the halving of unpolarised light were forgotten, situation B would be $400\,\text{W/m}^2$ and the largest. In situation E the second polariser is crossed with the polarisation direction of the incoming light, but light still gets through, because the polariser in between turns the polarisation direction.

## fy7-15-L2-05
**Given:** the measured points $(\theta;\ E)$ of the table at ten angles, of which the largest reading is $322\,\text{lx}$ at $0^\circ$ and the smallest $7\,\text{lx}$ at $90^\circ$
**Find:** the reading $E_0$ that the polarised light of the display alone gives when the transmission axis is aligned with the polarisation of the display, in $\text{lx}$
**Principle:** The light of the display is polarised, so according to Malus's law its share of the reading is $E_0 \cos^2\theta$. The background light adds the same amount $E_\text{b}$ to every reading, so the reading is $E = E_0 \cos^2\theta + E_\text{b}$. When $E$ is plotted as a function of $\cos^2\theta$, the points lie on a straight line whose slope is $E_0$ and whose constant term is $E_\text{b}$.
**Reading the graph:** The points lie on a rising line with points on both sides of it. The angles $0^\circ$, $30^\circ$, $60^\circ$ and $90^\circ$ give the values $\cos^2\theta = 1$, $0.75$, $0.25$ and $0$. The fitted line passes approximately through the points $(0;\ 7\,\text{lx})$ and $(1;\ 321\,\text{lx})$. The constant term $7\,\text{lx}$ is the background light, and the values are read from the line, not from individual measured points.
**Formula:** $E_0 = \dfrac{\Delta E}{\Delta (\cos^2\theta)} = \dfrac{E_2 - E_1}{x_2 - x_1}$, where $x = \cos^2\theta$
**Conversions:** Not needed: the readings are in lux, and $\cos^2\theta$ is a number without units.
**Substitution:** $E_0 = \dfrac{321\,\text{lx} - 7\,\text{lx}}{1 - 0} = 314\,\text{lx}$
**Answer:** $314\,\text{lx}$, three significant figures like the readings. A fit by eye varies, so about $309\text{–}319\,\text{lx}$ is a good answer.
**Reasonableness:** At $0^\circ$ the reading is $314\,\text{lx} + 7\,\text{lx} = 321\,\text{lx}$, which agrees with the value $322\,\text{lx}$ of the table. At $60^\circ$ the line gives $314 \cdot 0.25 + 7 = 85.5\,\text{lx}$, which agrees with the value $88\,\text{lx}$ of the table. In real series of measurements the points do not usually lie exactly on one line because of measurement uncertainty. If the background light were not subtracted, the answer would be the largest reading $322\,\text{lx}$, which lies outside the accepted range.

## fy7-15-L2-06
**Given:** the measured points $(\theta;\ I : I_0)$ of the table, for example $(45^\circ;\ 0.51)$ and $(60^\circ;\ 0.26)$; the ratio asked about is $I : I_0 = 0.40$
**Find:** the angle $\theta$ in degrees at which the intensity is $40\,\%$ of the intensity of the incident light
**Principle:** The share of polarised light that passes through follows Malus's law, $I : I_0 = \cos^2\theta$. A smooth curve is drawn through the measured points, because the points have scatter caused by measurement uncertainty. The angle is read from the curve where the ratio is $0.40$, and the result is checked by calculating with Malus's law.
**Reading the graph:** The curve falls from the angle $45^\circ$, where the ratio is about $0.51$, to the angle $60^\circ$, where it is about $0.26$. A line parallel to the horizontal axis from $0.40$ meets the curve at the angle $51^\circ$, because the curve is almost straight between these points.
**Formula:** $\cos^2\theta = \dfrac{I}{I_0}$, so $\theta = \cos^{-1}\sqrt{\dfrac{I}{I_0}}$
**Conversions:** Not needed: the share $40\,\% = 0.40$ is a ratio, and the angle comes out in degrees.
**Substitution:** $\theta = \cos^{-1}\sqrt{0.40} = \cos^{-1} 0.6325 = 50.77^\circ$
**Answer:** $50.8^\circ$, three significant figures like the angles of the measured points. About $51^\circ$ read from the curve is a good answer.
**Reasonableness:** At $45^\circ$ the share is $0.50$ and at $60^\circ$ it is $0.25$, so the share $0.40$ must lie between these, closer to $45^\circ$. The result $50.8^\circ$ lies between them. Check: $\cos^2 50.8^\circ = 0.40$.

## fy7-15-L2-07
**Given:** refractive index of air $1.00$ and of ethanol $1.36$, the light comes from air; the student's result $36.3^\circ$
**Find:** Brewster's angle $\alpha_\text{B}$ in degrees and the meaning of the student's angle $36.3^\circ$
**Principle:** In Brewster's law $\tan\alpha_\text{B} = n_2 : n_1$ the numerator is the refractive index of the substance into which the light is refracted, and the denominator is that of the substance from which the light comes. Here the light goes from air into ethanol, so $n_1$ is the refractive index of air and $n_2$ that of ethanol. The student swapped the refractive indices and calculated the ratio $n_1 : n_2$.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: the refractive indices are numbers without units, and the angle comes out in degrees.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.36}{1.00} = \tan^{-1} 1.36 = 53.67^\circ$
**Answer:** $53.7^\circ$, three significant figures like the refractive indices.
**Reasonableness:** When $n_2 > n_1$, $\tan\alpha_\text{B} > 1$, so Brewster's angle must be more than $45^\circ$. The student's $36.3^\circ$ is less than $45^\circ$, so it cannot be Brewster's angle for light arriving from air into a denser substance. The student's angle is $90^\circ - 53.67^\circ = 36.33^\circ$, which is the angle of refraction in ethanol: at Brewster's angle the reflected and the refracted ray are perpendicular to each other. The same angle is also Brewster's angle for light arriving from inside the ethanol into air, because then $\tan\alpha_\text{B} = 1.00 : 1.36$.
**Model answer:** The error was the order of the refractive indices in Brewster's law. The angle $36.3^\circ$ that the student calculated is not an angle of incidence but the angle of refraction in ethanol when the angle of incidence is the correct Brewster's angle $53.7^\circ$. It would be Brewster's angle only for light arriving from inside the ethanol into air.

## fy7-15-L3-04
**Given:** intensity of unpolarised light $I_0 = 960\,\text{W/m}^2$, three ideal polarisers, of which the transmission axes of the first and the last are perpendicular and the middle one is at an angle $\theta$ to the first; the measured points $(\theta;\ I_3)$ of the table
**Find:** what percentage of $I_0$ passes through at most, the ratio $I_3 : I_0$ in $\%$; also the angle of the greatest intensity and the justification for the effect of the third polariser
**Principle:** The first polariser halves the unpolarised light. After that the light is polarised, so Malus's law applies to the middle and the last polariser. The middle one is at an angle $\theta$ to the first and therefore at an angle $90^\circ - \theta$ to the last, because the first and the last are perpendicular.
**Reading the graph:** The greatest reading of the table, $114\,\text{W/m}^2$, is at the angle $45^\circ$. The readings at the angles $15^\circ$ and $75^\circ$ are $32\,\text{W/m}^2$ and $28\,\text{W/m}^2$, so approximately equal, and the readings at the angles $0^\circ$ and $90^\circ$ are almost zero.
**Formula:** $I_1 = \tfrac{1}{2} I_0$, $I_2 = I_1 \cos^2\theta$ and $I_3 = I_2 \cos^2(90^\circ - \theta) = I_2 \sin^2\theta$, so $I_3 = \tfrac{1}{2} I_0 \cos^2\theta \sin^2\theta = \tfrac{1}{8} I_0 \sin^2 2\theta$. The greatest value is obtained when $\sin 2\theta = 1$, that is $\theta = 45^\circ$, and then $\dfrac{I_3}{I_0} = \dfrac{1}{8}$.
**Conversions:** Not needed: the angles are in degrees, and the share is converted to a percentage by multiplying by $100$.
**Substitution:** $I_3 = \tfrac{1}{2} \cdot 960\,\text{W/m}^2 \cdot \cos^2 45^\circ \cdot \sin^2 45^\circ = 480\,\text{W/m}^2 \cdot 0.500 \cdot 0.500 = 120\,\text{W/m}^2$ and $\dfrac{I_3}{I_0} = \dfrac{120\,\text{W/m}^2}{960\,\text{W/m}^2} = 0.125 = 12.5\,\%$
**Answer:** $12.5\,\%$, that is $120\,\text{W/m}^2$. The result is exact, because the ideal model gives exactly $\tfrac{1}{8} = 0.125$. The intensity is greatest at the angle $45^\circ$. At the angles $15^\circ$ and $75^\circ$ the expression gives the same value, $30\,\text{W/m}^2$, because $\sin 2\theta$ is the same at the angles $\theta$ and $90^\circ - \theta$.
**Reasonableness:** The greatest reading of the table, $114\,\text{W/m}^2$, is close to the calculated $120\,\text{W/m}^2$, and the calculated $30\,\text{W/m}^2$ at $15^\circ$ agrees with the reading $32\,\text{W/m}^2$ of the table. The readings differ from the calculated ones by a few $\text{W/m}^2$ in both directions (at $60^\circ$ the reading $93\,\text{W/m}^2$ is above the calculated $90\,\text{W/m}^2$), which is measurement uncertainty. The share $12.5\,\%$ is below the $50\,\%$ that the first polariser lets through, as it should be.
**Model answer (part c):** After the first one the light is polarised perpendicular to the transmission axis of the last one, so the last one would block it. The middle one lets through only the component along its own transmission axis, so after it the light is polarised along that direction. The light then has a component also along the transmission axis of the last one, and part of it passes through. A polariser does not merely dim the light: the polarisation direction of the light that has passed through is always the transmission axis of the polariser, and part of the light is absorbed.

## fy7-15-L3-05
**Given:** intensity of the glare $I_0 = 40\,\text{W/m}^2$, refractive index of water $n_2 = 1.33$, refractive index of air $n_1 = 1.00$, the angle of incidence is Brewster's angle, the transmission axis of the glasses is $\varphi = 25.0^\circ$ from the vertical, transmittance of an ordinary lens $30\,\%$
**Find:** the height of the Sun above the horizon; the intensity $I$ of the glare after the polarised glasses, in $\text{W/m}^2$; a comparison of the lenses
**Principle:** The light goes from air into water, so $n_1$ is the refractive index of air and $n_2$ that of water, and Brewster's angle is $\alpha_\text{B} = \tan^{-1}(n_2 : n_1)$. The angle is measured from the normal of the surface, so the height of the Sun from the horizontal surface is $90^\circ - \alpha_\text{B}$. At Brewster's angle the reflected light is completely polarised along the surface, that is, horizontally. Malus's law applies to it: when the transmission axis is $25.0^\circ$ from the vertical, the angle between it and the horizontal polarisation direction is $\theta = 90^\circ - 25.0^\circ$.
**Formula:** $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$, height $h = 90^\circ - \alpha_\text{B}$, angle $\theta = 90^\circ - \varphi$ and $I = I_0 \cos^2\theta$
**Conversions:** Not needed: the angles are in degrees, and the intensity stays in $\text{W/m}^2$. The share $30\,\% = 0.30$.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.33}{1.00} = 53.06^\circ$, so $h = 90^\circ - 53.06^\circ = 36.94^\circ$. The angle is $\theta = 90^\circ - 25.0^\circ = 65.0^\circ$, and $I = 40\,\text{W/m}^2 \cdot \cos^2 65.0^\circ = 40\,\text{W/m}^2 \cdot 0.1786 = 7.144\,\text{W/m}^2$. An ordinary lens would let through $0.30 \cdot 40\,\text{W/m}^2 = 12\,\text{W/m}^2$.
**Answer:** $7.1\,\text{W/m}^2$, two significant figures like the intensity of the glare $40\,\text{W/m}^2$. The Sun is at a height of $36.9^\circ$. Polarised glasses reduce glare more, because $7.1\,\text{W/m}^2$ passes through them and $12\,\text{W/m}^2$ through an ordinary lens.
**Reasonableness:** If the head were upright, the angle would be $90^\circ$ and the glare would be extinguished completely, so even a small tilt lets a little light through, and $7.1\,\text{W/m}^2$ is less than a fifth of the original $40\,\text{W/m}^2$. The polarised lens is better when $\cos^2\theta < 0.30$, that is $\theta > 56.8^\circ$, and here $\theta = 65.0^\circ$ meets the condition.
**Model answer:** Polarised glasses reduce glare more, because the glare is completely polarised in the horizontal direction and the film absorbs it when the transmission axis is almost vertical. An ordinary lens dims glare and other light equally. If the tilt is more than $33.2^\circ$, the ordinary lens would be better. Polarised glasses halve the intensity of unpolarised light, whereas an ordinary lens lets through $30\,\%$, so for other light the ordinary lens dims more.

## fy7-15-L1-10
**Given:** intensity of the polarised light $I_0 = 400\,\text{W/m}^2$, angle between the direction of polarisation and the transmission axis $\theta = 35^\circ$; the graph of the share $I : I_0$ as a function of the angle
**Asked:** the intensity $I$ that comes through the polariser in $\text{W/m}^2$
**Principle:** The light is already polarised, so Malus's law $I = I_0 \cos^2\theta$ applies directly. The graph shows the share $I : I_0 = \cos^2\theta$ as a function of the angle, so the share is read from the graph at the angle $35^\circ$ and multiplied by the incident intensity.
**Reading the graph:** The vertical line at $35^\circ$ lies between $30^\circ$ and $45^\circ$ and meets the curve where the share is between $0.75$ and $0.50$, closer to $0.75$, about $0.67$. A good reading is $0.65\text{–}0.69$.
**Formula:** $I = I_0 \cdot \dfrac{I}{I_0}$, where $\dfrac{I}{I_0} = \cos^2\theta$
**Conversions:** Not needed: the intensity stays in $\text{W/m}^2$ and the share is a dimensionless number.
**Substitution:** $I = 400\,\text{W/m}^2 \cdot 0.67 = 268\,\text{W/m}^2$
**Answer:** $270\,\text{W/m}^2$ (read from the graph $268\,\text{W/m}^2$), two or three significant figures according to the accuracy of the reading. A good answer is $260\text{–}280\,\text{W/m}^2$.
**Reasonableness:** At $30^\circ$ the share is $0.75$ and at $45^\circ$ it is $0.50$, so the result $268\,\text{W/m}^2$ is between $300\,\text{W/m}^2$ and $200\,\text{W/m}^2$. Check by calculation: $400\,\text{W/m}^2 \cdot \cos^2 35^\circ = 268.4\,\text{W/m}^2$.

## fy7-15-L1-11
**Given:** refractive index of air $n_1 = 1.00$; the refractive index of crown glass is looked up in the MAFY table *Taitekertoimia*: $n_2 = 1.520$
**Asked:** Brewster's angle $\alpha_\text{B}$ in degrees
**Principle:** Light reflected from an insulator is completely polarised when the angle of incidence is Brewster's angle. Then the reflected and the refracted ray are perpendicular to each other, and Brewster's law follows from the law of refraction. The light comes from air into glass, so $n_1$ is the refractive index of air and $n_2$ that of glass.
**Formula:** $\tan\alpha_\text{B} = \dfrac{n_2}{n_1}$, so $\alpha_\text{B} = \tan^{-1}\dfrac{n_2}{n_1}$
**Conversions:** Not needed: refractive indices have no unit, and the angle comes out in degrees.
**Substitution:** $\alpha_\text{B} = \tan^{-1}\dfrac{1.520}{1.00} = \tan^{-1} 1.520 = 56.66^\circ$
**Answer:** $56.7^\circ$, three significant figures like the refractive index.
**Reasonableness:** When $n_2 > n_1$, $\tan\alpha_\text{B} > 1$, so the angle must be over $45^\circ$. The result is slightly larger than the angle $56.3^\circ$ of ordinary glass ($n = 1.50$), as it should be, because the refractive index of crown glass is slightly larger. Check: the angle of refraction is $90^\circ - 56.66^\circ = 33.34^\circ$, and $1.00 \cdot \sin 56.66^\circ = 0.835 = 1.520 \cdot \sin 33.34^\circ$.

## fy7-15-L2-08
**Given:** the line in the figure, passing approximately through the points $(0;\ 15\,\text{lx})$ and $(1;\ 375\,\text{lx})$ when the horizontal axis is $\cos^2\theta$; sensor reading $E = 200\,\text{lx}$
**Asked:** the angle of the film $\theta$ in degrees
**Principle:** The light of the display is polarised, so by Malus's law its share of the reading is $E_0 \cos^2\theta$. The background light adds a constant $E_\text{t}$ to the reading, so $E = E_0 \cos^2\theta + E_\text{t}$. The constant term of the line is $E_\text{t}$ and its slope is $E_0$. The angle is found by solving $\cos^2\theta$ and taking the inverse cosine.
**Reading the graph:** The line starts at $\cos^2\theta = 0$ from the reading $E_\text{t} = 15\,\text{lx}$ and rises to $375\,\text{lx}$ at $\cos^2\theta = 1$, so the slope is $E_0 = 375\,\text{lx} - 15\,\text{lx} = 360\,\text{lx}$. The reading $200\,\text{lx}$ corresponds on the line to a point slightly to the right of the middle ($\cos^2\theta = 0.5$), about $\cos^2\theta = 0.51$. The value is read from the line, not from individual data points.
**Formula:** $E = E_0 \cos^2\theta + E_\text{t}$, so $\cos^2\theta = \dfrac{E - E_\text{t}}{E_0}$ and $\theta = \cos^{-1}\sqrt{\dfrac{E - E_\text{t}}{E_0}}$
**Conversions:** Not needed: all readings are in lux, and $\cos^2\theta$ is a dimensionless number.
**Substitution:** $\cos^2\theta = \dfrac{200\,\text{lx} - 15\,\text{lx}}{360\,\text{lx}} = 0.514$ and $\theta = \cos^{-1}\sqrt{0.514} = \cos^{-1} 0.717 = 44.2^\circ$
**Answer:** $44^\circ$, two significant figures according to the accuracy of reading the graph. A good answer is $43\text{–}46^\circ$.
**Reasonableness:** The reading $200\,\text{lx}$ is close to $195\,\text{lx}$, which corresponds to $45^\circ$ ($\cos^2 45^\circ = 0.50$), so the angle must be slightly below $45^\circ$. Check: $360\,\text{lx} \cdot \cos^2 44.2^\circ + 15\,\text{lx} = 360\,\text{lx} \cdot 0.514 + 15\,\text{lx} = 200\,\text{lx}$.
