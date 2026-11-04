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
