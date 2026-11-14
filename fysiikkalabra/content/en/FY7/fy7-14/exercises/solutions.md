## fy7-14-L1-01
**Given:** refractive index of the soap film $n = 1.33$, thickness of the film $d = 420\,\text{nm}$, normal incidence
**Find:** the path difference $\Delta s$ between the waves reflected from the two surfaces, in nanometres
**Principle:** The wave reflected from the lower surface travels through the film and back, that is, an extra distance $2d$. In the film the wavelength is $n$ times shorter than in air, so the extra distance holds as many wavelengths as the distance $2nd$ does in air. At normal incidence the path difference is therefore $2nd$.
**Formula:** $\Delta s = 2nd$
**Conversions:** Not needed: the thickness is in nanometres, and the refractive index has no unit.
**Substitution:** $\Delta s = 2 \cdot 1.33 \cdot 420\,\text{nm} = 1117.2\,\text{nm}$
**Answer:** $1120\,\text{nm}$, that is, $1.12\,\mu\text{m}$, three significant figures like the refractive index $1.33$ and the thickness $420\,\text{nm}$.
**Reasonableness:** The path difference is more than twice the thickness of the film, because the light travels through the film and back and the wavelength in the film is shorter. Without the refractive index the path difference would be $840\,\text{nm}$; the factor $1.33$ increases it by about a third, as in the result.

## fy7-14-L1-02
**Given:** wavelength in air $\lambda = 633\,\text{nm}$, refractive index of magnesium fluoride $n = 1.38$
**Find:** the wavelength in magnesium fluoride $\lambda_n$ in nanometres
**Principle:** In a material light travels at the speed $v = c : n$, but its frequency $f$ does not change at an interface. Since $\lambda = v : f$, the wavelength shortens in the same ratio as the speed, that is, by the factor $n$.
**Formula:** $\lambda_n = \dfrac{v}{f} = \dfrac{c}{nf}$, so $\lambda_n = \dfrac{\lambda}{n}$
**Conversions:** Not needed: the wavelength is in nanometres, and the refractive index has no unit.
**Substitution:** $\lambda_n = \dfrac{633\,\text{nm}}{1.38} = 458.70\,\text{nm}$
**Answer:** $459\,\text{nm}$, three significant figures like the wavelength $633\,\text{nm}$ and the refractive index $1.38$.
**Reasonableness:** The wavelength in the material is shorter than in air, because the refractive index is greater than one. The colour of the light still does not change, because the frequency stays the same. Check: $1.38 \cdot 458.70\,\text{nm} = 633\,\text{nm}$.

## fy7-14-L1-03
**Given:** refractive index of the coating $n = 1.38$, of the glass $1.52$, wavelength $\lambda = 500\,\text{nm}$, normal incidence
**Find:** the thickness $d$ of the thinnest reflection-reducing coating, in nanometres
**Principle:** Both reflections occur at a material of higher refractive index ($1.00 \to 1.38 \to 1.52$), so both waves are inverted, and the inversions cancel each other. The waves then weaken each other when $2nd = (k + \tfrac{1}{2})\lambda$, and the thinnest coating is given by $k = 0$.
**Formula:** $2nd = \tfrac{1}{2}\lambda$, so $d = \dfrac{\lambda}{4n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{500\,\text{nm}}{4 \cdot 1.38} = 90.580\,\text{nm}$
**Answer:** $90.6\,\text{nm}$, three significant figures like the refractive index $1.38$ and the wavelength $500\,\text{nm}$.
**Reasonableness:** The coating is a quarter of the wavelength in the coating, $500\,\text{nm} : 1.38 = 362\,\text{nm}$, and $362\,\text{nm} : 4 \approx 91\,\text{nm}$. The result is a little smaller than the $99.6\,\text{nm}$ coating of the chapter for a wavelength of $550\,\text{nm}$, because the wavelength is shorter.

## fy7-14-L1-04
**Given:** refractive index of the soap film $n = 1.33$, air on both sides, wavelength $\lambda = 600\,\text{nm}$, normal incidence
**Find:** the thickness $d$ of the thinnest strongly reflecting film, in nanometres
**Principle:** The reflection from the upper surface, from air into the film, inverts the wave; the reflection from the lower surface, from the film into air, does not. Because of the single inversion, the waves strengthen each other when $2nd = (k + \tfrac{1}{2})\lambda$, and the thinnest such film is given by $k = 0$.
**Formula:** $2nd = \tfrac{1}{2}\lambda$, so $d = \dfrac{\lambda}{4n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{600\,\text{nm}}{4 \cdot 1.33} = 112.78\,\text{nm}$
**Answer:** $113\,\text{nm}$, three significant figures like the refractive index $1.33$ and the wavelength $600\,\text{nm}$.
**Reasonableness:** The same formula $d = \lambda : (4n)$ gives the strongest reflection in a soap film but the weakest in a coating, because the number of inverting reflections is different. The thickness is greater than the $103\,\text{nm}$ of the simulation for a wavelength of $550\,\text{nm}$, as it should be for a longer wavelength.

## fy7-14-L1-05
**Given:** refractive index of the plastic of the lens $n_\text{plastic} = 1.60$, normal incidence
**Find:** the refractive index $n_\text{c}$ of the ideal coating
**Principle:** The more the refractive indices at an interface differ, the stronger the reflected wave is. When the waves reflected from the upper and lower surfaces of the coating are equally strong, they can cancel each other completely. At normal incidence this happens when the refractive index of the coating is the square root of the refractive index of the lens material, as stated in the chapter: then $1.00 : n_\text{c} = n_\text{c} : n_\text{plastic}$.
**Formula:** $n_\text{c} = \sqrt{n_\text{plastic}}$
**Conversions:** Not needed: the refractive indices have no unit.
**Substitution:** $n_\text{c} = \sqrt{1.60} = 1.2649$
**Answer:** $1.26$, three significant figures like the refractive index $1.60$.
**Reasonableness:** The refractive index of the coating lies between $1.00$ for air and $1.60$ for the plastic, so both reflections invert the wave. The result is a little greater than the $1.23$ calculated for ordinary glass, because the refractive index of the plastic is greater. Check: $1.2649 \cdot 1.2649 = 1.60$.

## fy7-14-L1-06
**Find:** at which surface of the soap film the wave is inverted in the reflection, and why.
**Principle:** A reflected wave is inverted, that is, gets a shift of half a wavelength, when the light is reflected from a material with a greater refractive index. At the upper surface the light arrives from air into the film ($1.00 \to 1.33$), so the refractive index increases and the wave is inverted. At the lower surface the light arrives from the film into air ($1.33 \to 1.00$), so the refractive index decreases and the wave is not inverted. Inversion does not depend on whether the light arrives at normal incidence.
**Model answer:** The wave is inverted only at the upper surface of the film, because the light is reflected there from a material with a greater refractive index. At the lower surface the light is reflected from a material with a smaller refractive index, so its reflection keeps its phase. The fact that there is the same material on both sides of the film does not make the surfaces alike: what matters is whether the refractive index increases or decreases in the direction of travel. That is why there is one shift of half a wavelength in the reflections, and for a soap film the condition for reinforcement is $2nd = (k + \tfrac{1}{2})\lambda$.

## fy7-14-L1-07
**Given:** refractive index of the oil $n_\text{oil} = 1.47$, refractive index of the water $n_\text{w} = 1.33$, refractive index of air $1.00$, wavelength $\lambda = 570\,\text{nm}$, normal incidence
**Find:** the thickness $d$ of the thinnest oil film that reflects most strongly, in nanometres
**Principle:** At the upper surface the light arrives from air into oil ($1.00 \to 1.47$), so the refractive index increases and the wave is inverted. At the lower surface the light arrives from oil into water ($1.47 \to 1.33$), so the refractive index decreases and the wave is not inverted. There is one inversion, so the waves reinforce each other when $2nd = (k + \tfrac{1}{2})\lambda$, and the thinnest film is obtained with $k = 0$.
**Formula:** $2n_\text{oil}d = \tfrac{1}{2}\lambda$, so $d = \dfrac{\lambda}{4n_\text{oil}}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{570\,\text{nm}}{4 \cdot 1.47} = 96.94\,\text{nm}$
**Answer:** $96.9\,\text{nm}$, three significant figures like the refractive index $1.47$ and the wavelength $570\,\text{nm}$.
**Reasonableness:** Check: the path difference is $2 \cdot 1.47 \cdot 96.94\,\text{nm} = 285\,\text{nm} = \tfrac{1}{2} \cdot 570\,\text{nm}$. The film is thinner than a soap film for the same wavelength ($570\,\text{nm} : (4 \cdot 1.33) = 107\,\text{nm}$), because the refractive index of oil is greater and the wavelength in oil is therefore shorter.

## fy7-14-L1-08
**Given:** refractive index of the soap film $n = 1.33$, thickness $d = 300\,\text{nm}$, wavelength in air $\lambda = 532\,\text{nm}$, normal incidence
**Find:** the number of wavelengths that fit into the path difference, $\Delta s : \lambda$
**Principle:** At normal incidence the path difference between the waves reflected from the two surfaces of the film is $\Delta s = 2nd$. When it is divided by the wavelength measured in air, we get how many wavelengths fit into the path difference.
**Formula:** $\Delta s = 2nd$ and number $= \dfrac{\Delta s}{\lambda}$
**Conversions:** Not needed: the thickness and the wavelength are both in nanometres.
**Substitution:** $\Delta s = 2 \cdot 1.33 \cdot 300\,\text{nm} = 798\,\text{nm}$, so $\dfrac{\Delta s}{\lambda} = \dfrac{798\,\text{nm}}{532\,\text{nm}} = 1.5$
**Answer:** $1.5$ wavelengths, two significant figures like the thickness $300\,\text{nm}$.
**Reasonableness:** The path difference is greater than twice the thickness of the film, $600\,\text{nm}$, because the wavelength in the film is shorter. The result $1.5 = 1 + \tfrac{1}{2}$ is of the form $k + \tfrac{1}{2}$ with $k = 1$, so the soap film reflects green laser light strongly at this point.

## fy7-14-L1-09
**Find:** the expression for the thickness $d$ of the film at the first dark ring outside the black spot.
**Principle:** The path difference of the waves reflected from the two surfaces of the film is $2nd$, because the wave reflected from the lower surface travels through the film back and forth, and the wavelength in the film is $\lambda : n$. The reflection at the upper surface, from air to the film, inverts the wave; the reflection at the lower surface, from the film to air, does not. When there is one shift, the condition for destructive interference is $2nd = k\lambda$, where $k = 0, 1, 2, \ldots$
**Model answer:** The black spot is so thin that the path difference is almost zero. It corresponds to the value $k = 0$ of the destructive condition: the waves cancel each other because of the shift at the upper surface. When the film thickens, a bright ring comes first, where $2nd = \tfrac{1}{2}\lambda$, that is $d = \lambda : (4n)$. After that comes the first dark ring, where $k = 1$:

$$\begin{aligned}
&2nd = 1 \cdot \lambda \\
&d = \frac{\lambda}{2n}
\end{aligned}$$

At the first dark ring the thickness of the film is $d = \dfrac{\lambda}{2n}$. For example, when $\lambda = 589\,\text{nm}$ and $n = 1.33$, the thickness is $589\,\text{nm} : 2.66 \approx 221\,\text{nm}$.

The expression $\lambda : (4n)$ is obtained if the shift is forgotten, but it is the thickness of the first bright ring. The expression $\lambda : n$ forgets that the light travels through the film back and forth. The expression $\lambda : 2$ uses the wavelength in air, and the expression $n\lambda : 2$ wrongly assumes that the wavelength becomes longer in the film. Light slows down in the film, so the wavelength becomes shorter.

## fy7-14-L2-01
**Given:** refractive index of the soap film $n = 1.33$, thickness $d = 240\,\text{nm}$, air on both sides, visible light $400$–$700\,\text{nm}$
**Find:** the wavelength $\lambda$ missing from the reflected light, in nanometres
**Principle:** The reflection from the upper surface, from air into the film, inverts the wave; the reflection from the lower surface, from the film into air, does not. Because of the single inversion, the waves weaken each other when the path difference is a whole number of wavelengths, $2nd = k\lambda$. We calculate $\lambda$ for $k = 1, 2$ and choose the visible one.
**Formula:** $2nd = k\lambda$, so $\lambda = \dfrac{2nd}{k}$
**Conversions:** Not needed: the thickness and the wavelength are both in nanometres.
**Substitution:** $k = 1$: $\lambda = \dfrac{2 \cdot 1.33 \cdot 240\,\text{nm}}{1} = 638.4\,\text{nm}$; for $k = 2$ we get $319.2\,\text{nm}$, which is ultraviolet.
**Answer:** $638\,\text{nm}$, three significant figures like the refractive index $1.33$ and the thickness $240\,\text{nm}$.
**Reasonableness:** The missing light is red, so the film looks blue-green at this point. The result is close to, and greater than, the $532\,\text{nm}$ missing for the $200\,\text{nm}$ film of the chapter, as it should be for a thicker film: the missing wavelength grows in the same ratio as the thickness. The thickness is $1.2$ times as great, and $1.2 \cdot 532\,\text{nm}$ is $638.4\,\text{nm}$.

## fy7-14-L2-02
**Given:** refractive index of the coating $n = 1.38$, thickness $d = 110\,\text{nm}$, refractive index of the glass $1.52$, visible light $400$–$700\,\text{nm}$
**Find:** the most weakly reflected wavelength $\lambda$ in nanometres
**Principle:** Both reflections occur at a material of higher refractive index ($1.00 \to 1.38 \to 1.52$), so the inversions cancel each other. The waves weaken each other when $2nd = (k + \tfrac{1}{2})\lambda$. We calculate $\lambda$ for $k = 0, 1$ and choose the visible one.
**Formula:** $2nd = (k + \tfrac{1}{2})\lambda$, so $\lambda = \dfrac{2nd}{k + \frac{1}{2}}$
**Conversions:** Not needed: the thickness and the wavelength are both in nanometres.
**Substitution:** $k = 0$: $\lambda = \dfrac{2 \cdot 1.38 \cdot 110\,\text{nm}}{0.5} = \dfrac{303.6\,\text{nm}}{0.5} = 607.2\,\text{nm}$; for $k = 1$ we get $303.6\,\text{nm} : 1.5 = 202.4\,\text{nm}$, which is ultraviolet.
**Answer:** $607\,\text{nm}$, three significant figures like the thickness $110\,\text{nm}$ and the refractive index $1.38$.
**Reasonableness:** For $k = 0$ the coating is a quarter-wave layer: $4 \cdot 1.38 \cdot 110\,\text{nm} = 607.2\,\text{nm}$. The coating is thicker than the $99.6\,\text{nm}$ designed for $550\,\text{nm}$, so it cancels a longer, orange wavelength.

## fy7-14-L2-03
**Given:** refractive index of the coating $n = 1.38$, of the glass $1.52$, wavelength $\lambda = 520\,\text{nm}$, normal incidence
**Find:** the thickness $d$ of the second thinnest destructive coating, in nanometres
**Principle:** Both reflections invert the wave ($1.00 \to 1.38 \to 1.52$), so the inversions cancel each other, and the waves weaken each other when $2nd = (k + \tfrac{1}{2})\lambda$. The thinnest coating is $k = 0$, so the second thinnest is given by $k = 1$.
**Formula:** $2nd = (1 + \tfrac{1}{2})\lambda$, so $d = \dfrac{3\lambda}{4n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{3 \cdot 520\,\text{nm}}{4 \cdot 1.38} = \dfrac{1560\,\text{nm}}{5.52} = 282.61\,\text{nm}$
**Answer:** $283\,\text{nm}$, three significant figures like the refractive index $1.38$ and the wavelength $520\,\text{nm}$.
**Reasonableness:** The thinnest coating would be $520\,\text{nm} : (4 \cdot 1.38) = 94.2\,\text{nm}$, and the second thinnest is three times that, because the path difference increases by one wavelength, that is, by two half wavelengths. Check: $2 \cdot 1.38 \cdot 282.61\,\text{nm} = 780\,\text{nm} = 1.5 \cdot 520\,\text{nm}$.

## fy7-14-L2-04
**Given:** refractive index of the layer $n = 2.30$, of the glass $1.52$, wavelength $\lambda = 550\,\text{nm}$, light from air at normal incidence
**Find:** the thickness $d$ of the thinnest strongly reflecting layer, in nanometres
**Principle:** The reflection from the upper surface, from air into the layer ($1.00 \to 2.30$), inverts the wave. At the lower surface the light is reflected from the layer into the glass ($2.30 \to 1.52$), that is, at a material of lower refractive index, so the wave is not inverted. Because of the single inversion, the conditions are the same as in a soap film: the waves strengthen each other when $2nd = (k + \tfrac{1}{2})\lambda$, and the thinnest layer is given by $k = 0$.
**Formula:** $2nd = \tfrac{1}{2}\lambda$, so $d = \dfrac{\lambda}{4n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{550\,\text{nm}}{4 \cdot 2.30} = 59.783\,\text{nm}$
**Answer:** $59.8\,\text{nm}$, three significant figures like the refractive index $2.30$ and the wavelength $550\,\text{nm}$.
**Reasonableness:** The layer is thinner than an $\text{MgF}_2$ coating of $99.6\,\text{nm}$ for the same wavelength, because the refractive index is greater and the wavelength in the layer is therefore shorter. The decisive point is that behind the lower surface there is a lower refractive index: the same quarter-wave thickness therefore strengthens the reflection instead of weakening it.

## fy7-14-L2-05
**Given:** the data points of the table $(d;\ \lambda)$: $(90\,\text{nm};\ 483\,\text{nm})$, $(100\,\text{nm};\ 534\,\text{nm})$, $(110\,\text{nm};\ 584\,\text{nm})$, $(120\,\text{nm};\ 640\,\text{nm})$ and $(130\,\text{nm};\ 693\,\text{nm})$; soap film in air, normal incidence
**Find:** the refractive index $n$ of the film
**Principle:** A soap film has one inverting reflection, so the wavelength reflected most strongly is the one for which $2nd = (k + \tfrac{1}{2})\lambda$, that is, $\lambda = \dfrac{2n}{k + \frac{1}{2}} \cdot d$. The wavelength is directly proportional to the thickness, so the line of the graph passes approximately through the origin and its slope is $\dfrac{2n}{k + \frac{1}{2}}$. The order is deduced from the slope: with $k = 0$ we get $n = \tfrac{1}{4} \cdot$ slope and with $k = 1$ we get $n = 0.75 \cdot$ slope. The refractive index must suit soapy water, about $1.3$.
**Reading the graph:** The points lie on a rising line with points on both sides of it, and the line passes close to the origin. The fitted line passes approximately through the points $(90\,\text{nm};\ 482\,\text{nm})$ and $(130\,\text{nm};\ 692\,\text{nm})$. They are read from the line and chosen far apart.
**Formula:** slope $a = \dfrac{\Delta\lambda}{\Delta d}$ and $a = \dfrac{2n}{k + \frac{1}{2}}$, so with $k = 0$ we get $n = \dfrac{a}{4}$
**Conversions:** Not needed: the thickness and the wavelength are both in nanometres, and the slope has no unit.
**Substitution:** $a = \dfrac{692\,\text{nm} - 482\,\text{nm}}{130\,\text{nm} - 90\,\text{nm}} = \dfrac{210\,\text{nm}}{40\,\text{nm}} = 5.25$. With $k = 1$ we would get $n = 0.75 \cdot 5.25 = 3.9$, which is far from the refractive index of soapy water. With $k = 0$ we get $n = \dfrac{5.25}{4} = 1.31$.
**Answer:** $1.3$, two significant figures, because the line is fitted by eye. A fit by eye varies, so about $1.26$–$1.37$ is a good answer.
**Reasonableness:** The order is $k = 0$, because only it gives a refractive index that suits soapy water. Check: in the row $d = 110\,\text{nm}$ the formula $\lambda = 4nd$ gives $4 \cdot 1.3 \cdot 110\,\text{nm} = 572\,\text{nm}$, and the table has $584\,\text{nm}$; the difference is less than $3\,\%$. All the wavelengths are in the visible range $400$–$700\,\text{nm}$, as they should be.

## fy7-14-L2-06
**Given:** refractive index of the soap film $n = 1.33$, thickness $d = 250\,\text{nm}$, air on both sides, visible light $400$–$700\,\text{nm}$, normal incidence; the path difference calculated by the student $2nd = 665\,\text{nm}$
**Find:** the error in the student's reasoning and the visible wavelength $\lambda$ that is reflected most strongly, in nanometres
**Principle:** The student calculated the path difference correctly but forgot the shift of half a wavelength in the reflection. The reflection at the upper surface from air into the film inverts the wave, and the reflection at the lower surface from the film into air does not. When the path difference is a whole wavelength, the other wave is in opposite phase because of the inversion, so the waves weaken each other: $2nd = k\lambda$ is the condition for weakening. The waves of red light, $665\,\text{nm}$, weaken each other, and the film does not look red. The wavelength reflected most strongly is the one for which $2nd = (k + \tfrac{1}{2})\lambda$.
**Formula:** $2nd = (k + \tfrac{1}{2})\lambda$, so $\lambda = \dfrac{2nd}{k + \frac{1}{2}}$
**Conversions:** Not needed: the thickness and the wavelength are both in nanometres.
**Substitution:** $k = 1$: $\lambda = \dfrac{665\,\text{nm}}{1.5} = 443.3\,\text{nm}$. With $k = 0$ we get $1330\,\text{nm}$ (infrared) and with $k = 2$ we get $266\,\text{nm}$ (ultraviolet), so they are not visible light.
**Answer:** $443\,\text{nm}$, three significant figures like the refractive index $1.33$ and the thickness $250\,\text{nm}$.
**Reasonableness:** Check: $1.5 \cdot 443.3\,\text{nm} = 665\,\text{nm}$. Red ($665\,\text{nm}$, condition $2nd = 1 \cdot \lambda$) is missing from the film, and the reflected light is blue-violet, so the film looks blue-violet at this point and not red. The incorrect condition thus gave the opposite result.

## fy7-14-L2-07
**Given:** refractive index of the coating $n = 1.38$, refractive index of the glass $1.52$, the reflected shares $R$ of the table at wavelengths $420$–$700\,\text{nm}$, coating the thinnest possible ($k = 0$)
**Find:** the wavelength for which the coating is designed and the thickness $d$ of the coating in nanometres; also the reason for the purple colour of the lens
**Principle:** The coating is designed for the wavelength at which the reflection is smallest. The reflection at each surface of the coating inverts the wave ($1.00 \to 1.38 \to 1.52$), so the waves weaken each other when $2nd = (k + \tfrac{1}{2})\lambda$. For the thinnest coating $k = 0$ and $d = \dfrac{\lambda}{4n}$.
**Reading the graph:** The graph is cup-shaped: the reflection decreases from $1.84\,\%$ towards the middle, is smallest, $1.26\,\%$, at the wavelength $540\,\text{nm}$, and increases again to $1.64\,\%$ at the wavelength $700\,\text{nm}$. So the smallest reflection is at the wavelength $\lambda = 540\,\text{nm}$.
**Formula:** $d = \dfrac{\lambda}{4n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{540\,\text{nm}}{4 \cdot 1.38} = 97.83\,\text{nm}$
**Answer:** $97.8\,\text{nm}$, three significant figures like the refractive index $1.38$ and the wavelength $540\,\text{nm}$. The coating is designed for the green wavelength $540\,\text{nm}$. The purple colour arises because the reflection is greatest at both ends of the graph: violet ($420\,\text{nm}$) is reflected $1.84\,\%$ and red ($700\,\text{nm}$) $1.64\,\%$, while green is reflected only $1.26\,\%$, that is, violet about $1.5$ times and red about $1.3$ times as much as green. A mixture of red and violet looks purple, whereas green passes through the glass.
**Reasonableness:** Check: $4 \cdot 1.38 \cdot 97.83\,\text{nm} = 540\,\text{nm}$. The coating is a little thinner than the $99.6\,\text{nm}$ designed for $550\,\text{nm}$, because the wavelength is a little shorter. The coating does not cancel all wavelengths equally well, as stated in the chapter: the reflection at the edges is about $1.3$–$1.5$ times that in the middle, and the smallest reflection $1.26\,\%$ is close to the $1.3\,\%$ mentioned in the chapter.

## fy7-14-L2-08
**Given:** refractive index of the coating $1.38$, refractive index of the glass $1.52$, the reflected shares $R$ read from the figure at wavelengths $400$–$700\,\text{nm}$
**Find:** by what percentage the coating reduces the reflection of uncoated glass at the point where the reflection is smallest
**Principle:** No light is lost in the coating: destructive interference reduces the reflected share. The smallest reflection marks the wavelength for which the coating is designed. The share removed follows from comparing the reflection of the coated lens $R_\text{coat}$ with the reflection of uncoated glass $R_0$ at the same wavelength.
**Reading the graph:** The reflection of uncoated glass is the horizontal black line, and $R_0 \approx 4.3\,\%$ is read from it. The green curve is cup-shaped. At its bottom, at about $500\,\text{nm}$, $R_\text{coat} \approx 1.3\,\%$ is read. The bottom is the lowest point of the curve, and the line is above it.
**Formula:** share removed $= \dfrac{R_0 - R_\text{coat}}{R_0} = 1 - \dfrac{R_\text{coat}}{R_0}$
**Conversions:** Not needed: both shares are read in percent, and the ratio has no unit.
**Substitution:** $\text{removed share} = 1 - \dfrac{R_\text{coated}}{R_0} = 1 - \dfrac{1.3\,\%}{4.3\,\%} = 1 - 0.302 = 0.698 = 69.8\,\%$
**Answer:** about $70\,\%$, two significant figures like the values read from the graph. The uncertainty of reading the graph affects the third figure.
**Reasonableness:** The coating reduces the reflection by more than half, as in the chapter: the reflection falls from about $4.3\,\%$ to about $1.3\,\%$. The result is below $100\,\%$, so the coating does not cancel the reflection completely, as expected, because a single coating layer cannot cancel the reflection at all wavelengths.

## fy7-14-L3-01
**Given:** refractive index of the soap film $n = 1.33$, air on both sides, wavelength $\lambda = 589\,\text{nm}$, normal incidence; the film thickens from top to bottom, and the topmost part is black
**Find:** the thickness $d$ of the film at the second dark band, in nanometres
**Principle:** The reflection from the upper surface inverts the wave and that from the lower surface does not, so the waves weaken each other when $2nd = k\lambda$. The black top is the value $k = 0$, where the film is much thinner than the wavelength. The film thickens downwards, so the next dark bands are in order $k = 1$ and $k = 2$; at the second dark band $k = 2$. The bright bands lie between the dark ones.
**Formula:** $2nd = 2\lambda$, so $d = \dfrac{\lambda}{n}$
**Conversions:** Not needed: the wavelength and the thickness are both in nanometres.
**Substitution:** $d = \dfrac{589\,\text{nm}}{1.33} = 442.86\,\text{nm}$
**Answer:** $443\,\text{nm}$, three significant figures like the refractive index $1.33$ and the wavelength $589\,\text{nm}$.
**Reasonableness:** The first dark band is at a thickness of $589\,\text{nm} : (2 \cdot 1.33) = 221\,\text{nm}$, and the second is twice that, because between consecutive dark bands the thickness always grows by the same amount, $\lambda : (2n)$. The thickness is less than a micrometre, as is fitting for a thin film.

## fy7-14-L3-02
**Given:** eight surfaces, each of which reflects $1.3\,\%$ of the light arriving at it; the glass does not absorb light, and reflected light does not return to the sensor
**Find:** the percentage of light that gets through the objective
**Principle:** Light does not disappear in the coating: what is not reflected goes through the surface. Through each surface therefore passes $98.7\,\%$ of the light arriving at it, since $100\,\% - 1.3\,\% = 98.7\,\%$. The next surface receives only the light that passed the previous one, so the fractions are multiplied together eight times.
**Formula:** $\dfrac{I_\text{out}}{I_0} = (1 - R)^8$
**Conversions:** $R = 1.3\,\% = 0.013$. Finally the fraction is multiplied by one hundred to give a percentage.
**Substitution:** $\dfrac{I_\text{out}}{I_0} = (1 - 0.013)^8 = 0.987^8 = 0.9006 = 90.06\,\%$
**Answer:** $90\,\%$, two significant figures like the reflected fraction $1.3\,\%$.
**Reasonableness:** Estimate: the eight surfaces reflect altogether about $8 \cdot 1.3\,\% \approx 10\,\%$, so about $90\,\%$ gets through. Without coatings each surface would reflect about $4.26\,\%$, and only $(1 - 0.0426)^8 \approx 70.6\,\%$ would get through. The coatings thus increase the light reaching the sensor by about $19$ percentage points, that is, by a good quarter ($90.06 : 70.6 \approx 1.28$), and reduce ghost images.

## fy7-14-L3-03
**Given:** refractive index of the soap film $n = 1.33$, air on both sides, most strongly reflected wavelengths $\lambda_1 = 630\,\text{nm}$ and $\lambda_2 = 450\,\text{nm}$, none between them
**Find:** the thickness $d$ of the film in nanometres
**Principle:** There is one inverting reflection, so the waves strengthen each other when $2nd = (k + \tfrac{1}{2})\lambda$. The same thickness strengthens both wavelengths. The shorter wavelength fits into the path difference more times, and since there are no others between them, its order is greater by one: $(k + \tfrac{1}{2})\lambda_1 = (k + \tfrac{3}{2})\lambda_2$. From this we first solve $k$ and then $d$.
**Formula:** $(k + \tfrac{1}{2})\lambda_1 = (k + \tfrac{3}{2})\lambda_2$, so $k = \dfrac{\tfrac{3}{2}\lambda_2 - \tfrac{1}{2}\lambda_1}{\lambda_1 - \lambda_2}$; thickness $d = \dfrac{(k + \frac{1}{2})\lambda_1}{2n}$
**Conversions:** Not needed: the wavelengths and the thickness are all in nanometres.
**Substitution:** $k = \dfrac{1.5 \cdot 450\,\text{nm} - 0.5 \cdot 630\,\text{nm}}{630\,\text{nm} - 450\,\text{nm}} = \dfrac{360\,\text{nm}}{180\,\text{nm}} = 2$, so $d = \dfrac{2.5 \cdot 630\,\text{nm}}{2 \cdot 1.33} = \dfrac{1575\,\text{nm}}{2.66} = 592.11\,\text{nm}$
**Answer:** $592\,\text{nm}$, three significant figures like the refractive index $1.33$ and the wavelengths.
**Reasonableness:** Check: $3.5 \cdot 450\,\text{nm} = 1575\,\text{nm}$ and $2.5 \cdot 630\,\text{nm} = 1575\,\text{nm}$, so the same path difference strengthens both. The other orders give $1575\,\text{nm} : 1.5 = 1050\,\text{nm}$ (infrared) and $1575\,\text{nm} : 4.5 = 350\,\text{nm}$ (ultraviolet), so in the visible range there really are only these two.

## fy7-14-L3-04
**Given:** refractive index of air $1.00$, of oil $n = 1.47$, of water $1.33$, thickness of the film $d = 450\,\text{nm}$, white light at normal incidence, visible light $400$–$700\,\text{nm}$
**Find:** a) the visible wavelengths reflected most strongly and the colour of the point; b) the thickness at which the wavelength of part a) is reflected most weakly for the first time as the film thins; c) the reason for the dark and almost colourless appearance of the film when $d \ll \lambda$
**Principle:** a) At the upper surface the light arrives from air into oil ($1.00 \to 1.47$), so the refractive index increases and the wave is inverted. At the lower surface the light arrives from oil into water ($1.47 \to 1.33$), so the refractive index decreases and the wave is not inverted. There is one inversion, so the wavelengths reflected most strongly satisfy the condition $2nd = (k + \tfrac{1}{2})\lambda$ and those reflected most weakly satisfy the condition $2nd = k\lambda$. b) As the film thins, the path difference $2nd$ decreases. A wavelength is reflected most weakly (destructive interference) when the path difference is a whole number of wavelengths. The path difference is at first $2.5$ wavelengths, so the first weakening during the thinning is at the point where the path difference is $2$ wavelengths. c) In a very thin film the path difference is almost zero, but one reflection has been inverted. The air–oil interface reflects more strongly than the oil–water interface, so the waves do not cancel each other completely.
**Formula:** $\lambda = \dfrac{2nd}{k + \frac{1}{2}}$ (reflected most strongly) and $d = \dfrac{k\lambda}{2n}$ (destructive interference)
**Conversions:** Not needed: the thickness and the wavelengths are both in nanometres.
**Substitution:** a) The path difference is $2nd = 2 \cdot 1.47 \cdot 450\,\text{nm} = 1323\,\text{nm}$. With $k = 0$ we get $2646\,\text{nm}$ and with $k = 1$ we get $882\,\text{nm}$, both infrared. With $k = 2$ we get $\lambda = \dfrac{1323\,\text{nm}}{2.5} = 529.2\,\text{nm}$, and with $k = 3$ we get $378\,\text{nm}$, which is ultraviolet. In the visible range only $529\,\text{nm}$, green, is therefore reflected strongly. The weakened wavelengths are $\lambda = \dfrac{1323\,\text{nm}}{k}$, so with $k = 2$ red $661.5\,\text{nm}$ is missing and with $k = 3$ violet-blue $441\,\text{nm}$ is missing. The point looks green. b) The path difference of the green wavelength $529.2\,\text{nm}$ was $1323\,\text{nm} = 2.5\lambda$. As the film thins, the path difference decreases, and the first whole number is $2$. Then $2nd' = 2\lambda$, that is, $d' = \dfrac{2 \cdot 529.2\,\text{nm}}{2 \cdot 1.47} = \dfrac{1058.4\,\text{nm}}{2.94} = 360.0\,\text{nm}$.
**Answer:** $360\,\text{nm}$, three significant figures like the refractive index $1.47$ and the wavelength. c) When the thickness of the film is much smaller than the wavelength, the path difference $2nd$ is almost zero for all wavelengths of visible light. The reflection from the upper surface has been inverted and that from the lower surface has not, so the reflected waves are in opposite phase at all wavelengths and weaken each other. All wavelengths of visible light are reflected equally, so the film looks colourless, and the reflection is small: about $2.0\,\%$, as much as from water alone, whereas in a thicker place the colour reflected most strongly is reflected about $5.8\,\%$. The film is thus darker than any colour in the thicker place. Complete cancellation does not occur, because the reflection from the air–oil interface (amplitude about $0.19$) is much stronger than that from the oil–water interface (about $0.05$).
**Reasonableness:** Check: $2 \cdot 1.47 \cdot 360\,\text{nm} = 1058.4\,\text{nm} = 2 \cdot 529.2\,\text{nm}$. The thickness has decreased by $450\,\text{nm} - 360\,\text{nm} = 90\,\text{nm}$, and this is a quarter of the wavelength in oil, $\dfrac{529.2\,\text{nm}}{4 \cdot 1.47} = 90.0\,\text{nm}$, because the path difference decreased by half a wavelength ($2.5\lambda \to 2\lambda$). As the film thins further, the next dark point would be at $k = 1$, at the thickness $180\,\text{nm}$.

## fy7-14-L3-05
**Given:** wavelength $\lambda = 589\,\text{nm}$, refractive index of air $1.00$, of glass $1.52$, distance of the foil from the line of contact $L = 80\,\text{mm}$, the points of the table $(k;\ x)$: $(1;\ 1.9\,\text{mm})$, $(2;\ 3.9\,\text{mm})$, $(3;\ 5.7\,\text{mm})$, $(4;\ 7.7\,\text{mm})$, $(5;\ 9.5\,\text{mm})$, $(6;\ 11.5\,\text{mm})$, $(7;\ 13.3\,\text{mm})$ and $(8;\ 15.2\,\text{mm})$
**Find:** a) which surface inverts the wave and why the line of contact is dark; b) the fringe spacing $\Delta x$ and the increase of the thickness of the air layer from one fringe to the next; c) the thickness $D$ of the foil in micrometres
**Principle:** a) At the upper surface of the air layer the light arrives from glass into air ($1.52 \to 1.00$), so the refractive index decreases and the wave is not inverted. At the lower surface the light arrives from air into glass ($1.00 \to 1.52$), so the refractive index increases and the wave is inverted. There is one inversion, so in the dark fringes $2nd = k\lambda$, where $n = 1.00$. At the line of contact $d = 0$, so the path difference is zero and the reflected waves are in opposite phase because of the inversion: the line is dark and its order is $k = 0$. b) The difference between the path differences of successive dark fringes is one wavelength, so the thickness of the air layer increases by $\Delta d = \dfrac{\lambda}{2}$ from one fringe to the next. The fringes are evenly spaced, so the thickness of the wedge increases steadily with the distance. c) Over the distance $L$ there are $\dfrac{L}{\Delta x}$ fringes in all, and for each the thickness increases by $\dfrac{\lambda}{2}$.
**Reading the graph:** The points lie on a rising line with points on both sides of it, and the line passes almost through the origin. The fitted line passes approximately through the points $(0;\ 0.05\,\text{mm})$ and $(8;\ 15.2\,\text{mm})$. The point $(0;\ 0.05\,\text{mm})$ is where the fitted line crosses the vertical axis and is not a measurement. The points are read from the line and chosen far apart. The slope is the fringe spacing $\Delta x$.
**Formula:** $\Delta x = \dfrac{x_2 - x_1}{k_2 - k_1}$, $\Delta d = \dfrac{\lambda}{2}$ and $D = \dfrac{L}{\Delta x} \cdot \dfrac{\lambda}{2}$
**Conversions:** $\dfrac{\lambda}{2} = \dfrac{589\,\text{nm}}{2} = 294.5\,\text{nm} = 0.2945\,\mu\text{m}$, because $1\,\mu\text{m} = 1000\,\text{nm}$. The distances $L$ and $\Delta x$ are both in millimetres, so their ratio has no unit.
**Substitution:** $\Delta x = \dfrac{15.2\,\text{mm} - 0.05\,\text{mm}}{8 - 0} = 1.894\,\text{mm}$. The thickness increases by $294.5\,\text{nm}$ from one fringe to the next. Over the distance $L$ there are $\dfrac{80\,\text{mm}}{1.894\,\text{mm}} = 42.24$ fringes, so $D = 42.24 \cdot 0.2945\,\mu\text{m} = 12.44\,\mu\text{m} \approx 12\,\mu\text{m}$.
**Answer:** $12\,\mu\text{m}$, two significant figures, because the distance $L = 80\,\text{mm}$ is given with two digits and the line is fitted by eye. A fit by eye varies, so about $11.9$–$12.9\,\mu\text{m}$ is a good answer.
**Reasonableness:** Check at the eighth fringe: the thickness of the air layer is $8 \cdot 294.5\,\text{nm} = 2.36\,\mu\text{m}$, and $\dfrac{2.36\,\mu\text{m}}{12.44\,\mu\text{m}} = 0.19 = \dfrac{15.2\,\text{mm}}{80\,\text{mm}}$, so the thickness of the wedge increases directly with the distance. The thickness of the foil is of the order of ten micrometres, like thin aluminium foil.

## fy7-14-L3-06
**Given:** refractive index of the soap film $n = 1.33$, air on both sides, normal incidence, graph $R(\lambda)$ for $400$–$700\,\text{nm}$; the thickness is not given
**Find:** the order $k$ of the destructive condition and the thickness $d$ of the film in nanometres
**Principle:** One reflection inverts the wave, so the reflection is at a minimum when $2nd = k\lambda_\text{min}$ and at a maximum when $2nd = (k' + \tfrac{1}{2})\lambda_\text{max}$. It is the same film, so the path difference $2nd$ is the same in both. Of two neighbouring extremes, the shorter wavelength fits into the path difference more times, so for the longer-wavelength maximum next to the minimum $k' = k - 1$. First $k$ is solved, then $d$.
**Reading the graph:** In the visible range the curve has one minimum and one maximum to the right of it. The minimum is almost zero at $\lambda_\text{min} \approx 466\,\text{nm}$. The maximum is highest, about $7.7\,\%$, at $\lambda_\text{max} \approx 621\,\text{nm}$.
**Formula:** $k\lambda_\text{min} = (k - \tfrac{1}{2})\lambda_\text{max}$, so $k = \dfrac{\lambda_\text{max}}{2(\lambda_\text{max} - \lambda_\text{min})}$; thickness $d = \dfrac{k\lambda_\text{min}}{2n}$
**Conversions:** Not needed: the wavelengths and the thickness are both in nanometres.
**Substitution:** $k = \dfrac{621\,\text{nm}}{2 \cdot (621\,\text{nm} - 466\,\text{nm})} = \dfrac{621}{310} = 2.003 \approx 2$, so $d = \dfrac{2 \cdot 466\,\text{nm}}{2 \cdot 1.33} = 350.4\,\text{nm}$
**Answer:** $k = 2$ and $d \approx 350\,\text{nm}$, three significant figures like the refractive index $1.33$. The order must be a whole number, so it is rounded, and a reading error affects the thickness only a little.
**Reasonableness:** Check: the maximum $(2 - \tfrac{1}{2}) \cdot 621\,\text{nm} = 931\,\text{nm} = 2 \cdot 466\,\text{nm}$ and $2nd = 2 \cdot 1.33 \cdot 350\,\text{nm} = 931\,\text{nm}$. The value $k = 1$ would put the minimum at $931\,\text{nm}$, in the infrared, so in the visible range the minimum is exactly $k = 2$. The thickness is below a micrometre, as for a thin film.
