## fy7-1-L1-01
**Given:** magnetic flux density of the MRI scanner $B_1 = 3.0\,\text{T}$, magnetic flux density of the Earth's field $B_2 = 50\,\mu\text{T}$
**Find:** ratio of the fields $k = B_1 : B_2$, a plain number
**Principle:** The question "how many times greater" is answered by dividing the greater value by the smaller. A ratio can be calculated only when the fields are in the same unit, so the microtesla is converted to tesla first.
**Formula:** $k = \dfrac{B_1}{B_2}$
**Conversions:** $B_2 = 50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$
**Substitution:** $k = \dfrac{3.0\,\text{T}}{50 \cdot 10^{-6}\,\text{T}} = 0.060 \cdot 10^{6} = 60\,000$
**Answer:** $6.0 \cdot 10^{4}$ times, two significant figures like the field of the scanner $3.0\,\text{T}$ and the Earth's field $50\,\mu\text{T}$.
**Reasonableness:** One tesla is a million microtesla, so $3\,\text{T}$ is $3\,000\,000\,\mu\text{T}$. Dividing this by $50$ gives $60\,000$. The ratio is enormous, which explains why iron objects must not be taken into an MRI room.

## fy7-1-L1-02
**Given:** magnetic flux density of the Earth's field $B = 53\,\mu\text{T}$, inclination $I = 75^\circ$ below the horizontal
**Find:** horizontal component $B_\text{h}$ of the field in microtesla
**Principle:** The field points obliquely into the ground. The horizontal component is the leg adjacent to the angle $I$ in a right-angled triangle whose hypotenuse is the whole field.
**Formula:** $B_\text{h} = B\cos I$
**Conversions:** Not needed: the result comes out in the same unit as $B$, that is in microtesla.
**Substitution:** $B_\text{h} = 53\,\mu\text{T} \cdot \cos 75^\circ = 53\,\mu\text{T} \cdot 0.2588 = 13.72\,\mu\text{T}$
**Answer:** $14\,\mu\text{T}$, two significant figures like the field $53\,\mu\text{T}$ and the angle $75^\circ$.
**Reasonableness:** The field is almost vertical, so the horizontal component must be a small part of the whole field: $\cos 75^\circ$ is about a quarter, and $53 : 4 \approx 13$. The result is of the same order of magnitude as the $14\,\mu\text{T}$ of southern Finland, as expected from the location of Kuopio.

## fy7-1-L1-03
**Given:** horizontal component of the Earth's field $B_\text{h} = 14\,\mu\text{T}$ towards the north, field of the magnet $B_\text{m} = 48\,\mu\text{T}$ towards the east
**Find:** magnitude $B$ of the horizontal total field in microtesla
**Principle:** The total field is the vector sum of the fields. Fields pointing north and east are perpendicular to each other, so they are the legs of a right-angled triangle and the total field is the hypotenuse.
**Formula:** $B = \sqrt{B_\text{h}^2 + B_\text{m}^2}$
**Conversions:** Not needed: both fields are in microtesla.
**Substitution:** $B = \sqrt{(14\,\mu\text{T})^2 + (48\,\mu\text{T})^2} = \sqrt{196 + 2304}\,\mu\text{T} = \sqrt{2500}\,\mu\text{T} = 50\,\mu\text{T}$
**Answer:** $50\,\mu\text{T}$, two significant figures like the fields.
**Reasonableness:** The hypotenuse is longer than either leg but shorter than their sum $62\,\mu\text{T}$. The result $50\,\mu\text{T}$ is only a little greater than $48\,\mu\text{T}$, because the field of the magnet is much greater than the Earth's field.

## fy7-1-L1-04
**Find:** the poles of the pieces and whether the cut faces attract or repel each other
**Principle:** A magnet is a magnetic dipole: its poles always occur in pairs. Every part of a magnet consists of atomic dipoles lined up in the same direction, so every piece is also a dipole. Unlike poles attract and like poles repel each other.
**Model answer:** Each piece becomes a complete magnet with a north pole and a south pole. If the north pole of the original magnet was on the right, the north pole of each piece is on the right. So a north pole appears on the cut face of the left piece and a south pole on the cut face of the right piece. When the cut faces are brought back together, they have unlike poles, so the pieces attract each other and form one magnet again.

## fy7-1-L1-05
**Find:** the direction of the north end of the compass needle in front of the north pole of the magnet, and the reason
**Principle:** The direction of the field is the direction in which the north end of a compass needle points. Outside a magnet the field lines start from the north pole. The north end of the needle is itself a north pole, and like poles repel each other.
**Model answer:** The north end of the needle points directly away from the magnet, along the axis of the magnet. On the axis in front of the north pole the field lines leave the pole straight outwards, so the field points away from the magnet. The same follows from the poles: the north pole of the magnet repels the north end of the needle and attracts its south end, so the south end turns towards the magnet and the north end away from it.

## fy7-1-L2-01
**Given:** field of the magnet $B_\text{m} = 25\,\mu\text{T}$ towards the east, horizontal component of the Earth's field $B_\text{h} = 14\,\mu\text{T}$ towards the north
**Find:** angle of deflection $\theta$ of the needle from north towards east in degrees
**Principle:** The needle turns to point along the horizontal total field. The fields are perpendicular to each other, so the total field is the diagonal of a rectangle. For the angle measured from north, the opposite leg is the field pointing east and the adjacent leg is the field pointing north.
**Formula:** $\tan\theta = \dfrac{B_\text{m}}{B_\text{h}}$, so $\theta = \tan^{-1}\dfrac{B_\text{m}}{B_\text{h}}$
**Conversions:** Not needed: both fields are in microtesla, and the unit cancels.
**Substitution:** $\theta = \tan^{-1}\dfrac{25\,\mu\text{T}}{14\,\mu\text{T}} = \tan^{-1} 1.786 = 60.75^\circ$
**Answer:** $61^\circ$ from north towards east, two significant figures like the fields.
**Reasonableness:** The field of the magnet is greater than the Earth's field, so the needle must turn more than $45^\circ$ but less than $90^\circ$. A check in the other direction: $14\,\mu\text{T} \cdot \tan 60.75^\circ = 25\,\mu\text{T}$.

## fy7-1-L2-02
**Given:** components from the magnetometer $B_x = 12\,\mu\text{T}$, $B_y = -5.0\,\mu\text{T}$ and $B_z = -48\,\mu\text{T}$, perpendicular to each other
**Find:** magnetic flux density $B$ of the Earth's magnetic field in microtesla
**Principle:** The field is the vector sum of its components. The sum of two perpendicular components is given by the Pythagorean theorem, and when a third perpendicular component is added, the same theorem gives the sum of the squares of the three components. The sign gives only the direction, and squaring removes it.
**Formula:** $B^2 = B_x^2 + B_y^2 + B_z^2$, so $B = \sqrt{B_x^2 + B_y^2 + B_z^2}$
**Conversions:** Not needed: all components are in microtesla.
**Substitution:** $B^2 = (12\,\mu\text{T})^2 + (-5.0\,\mu\text{T})^2 + (-48\,\mu\text{T})^2 = 2473\,(\mu\text{T})^2$, so $B = \sqrt{2473}\,\mu\text{T} = 49.73\,\mu\text{T}$
**Answer:** $50\,\mu\text{T}$, two significant figures like the components $12\,\mu\text{T}$ and $48\,\mu\text{T}$.
**Reasonableness:** The result is greater than the greatest component $48\,\mu\text{T}$ and close to the value of about $52\,\mu\text{T}$ for Finland. The large $z$-component fits the fact that in Finland the field points steeply into the ground when the phone is horizontal.

## fy7-1-L2-03
**Given:** vertical component of the Earth's field $B_\text{v} = 52\,\mu\text{T}$, inclination $I = 77^\circ$ below the horizontal
**Find:** magnetic flux density $B$ of the field in microtesla
**Principle:** The whole field is the hypotenuse of a right-angled triangle and the vertical component is the leg opposite to the angle $I$, so $B_\text{v} = B\sin I$. The whole field is solved from the formula.
**Formula:** $B_\text{v} = B\sin I$, so $B = \dfrac{B_\text{v}}{\sin I}$
**Conversions:** Not needed: the result comes out in microtesla like $B_\text{v}$.
**Substitution:** $B = \dfrac{52\,\mu\text{T}}{\sin 77^\circ} = \dfrac{52\,\mu\text{T}}{0.9744} = 53.4\,\mu\text{T}$
**Answer:** $53\,\mu\text{T}$, two significant figures like the vertical component $52\,\mu\text{T}$.
**Reasonableness:** The hypotenuse is longer than the leg, so $B$ is greater than $52\,\mu\text{T}$. The field is almost vertical, so the difference is small. The horizontal component left is $53.4\,\mu\text{T} \cdot \cos 77^\circ \approx 12\,\mu\text{T}$, less than in southern Finland, as it should be further north.

## fy7-1-L2-04
**Given:** at a distance of $10\,\text{cm}$ the angle of the needle is $\theta_1 = 60^\circ$, at a distance of $20\,\text{cm}$ the angle is $\theta_2 = 10^\circ$; the field of the magnet is perpendicular to the horizontal component $B_\text{h}$ of the Earth's field
**Find:** ratio of the fields $k = B_1 : B_2$, a plain number
**Principle:** When the field of the magnet is perpendicular to the horizontal component of the Earth's field, the angle of the needle satisfies $\tan\theta = B_\text{m} : B_\text{h}$, so $B_\text{m} = B_\text{h}\tan\theta$. The Earth's field is the same at both positions, so it cancels from the ratio and need not be known.
**Formula:** $B_1 = B_\text{h}\tan\theta_1$ and $B_2 = B_\text{h}\tan\theta_2$, so $k = \dfrac{B_1}{B_2} = \dfrac{\tan\theta_1}{\tan\theta_2}$
**Conversions:** Not needed: the ratio is a plain number, and the distances do not appear in the calculation.
**Substitution:** $k = \dfrac{\tan 60^\circ}{\tan 10^\circ} = \dfrac{1.732}{0.1763} = 9.82$
**Answer:** about $9.8$ times, to two significant figures like the angles $60^\circ$ and $10^\circ$.
**Reasonableness:** When the distance doubles, the field weakens by much more than a half or a quarter, as the field of a magnet does in the simulation of the chapter. The ratio of the angles $60 : 10 = 6$ would be a wrong answer, because the angle is not directly proportional to the field.

## fy7-1-L3-01
**Given:** north pole of the magnet towards the north, compass east of the magnet at the level of its middle, field of the magnet there $B_\text{m} = 25\,\mu\text{T}$, horizontal component of the Earth's field $B_\text{h} = 14\,\mu\text{T}$ towards the north
**Find:** north component $B_y$ of the horizontal total field in microtesla (north positive) and the direction of the needle
**Principle:** Outside the magnet the field lines run from the north pole to the south pole, so at the side of the magnet at the level of its middle the field is parallel to the magnet and points from the north-pole end to the south-pole end, that is towards the south. It is opposite to the Earth's field, so the fields are added together with their signs. The needle turns to point along the total field, so the sign of the component tells whether the needle points north or south.
**Formula:** with north positive, $B_y = B_\text{h} - B_\text{m}$
**Conversions:** Not needed: both fields are in microtesla.
**Substitution:** $B_y = 14\,\mu\text{T} - 25\,\mu\text{T} = -11\,\mu\text{T}$
**Answer:** $-11\,\mu\text{T}$, that is $11\,\mu\text{T}$ towards the south, two significant figures like the fields. The sign is negative, so the north end of the needle points south: the needle has turned round.
**Reasonableness:** The field of the magnet is greater than the Earth's field, so it wins and the total field points in the direction of the field of the magnet. If the field of the magnet were exactly $14\,\mu\text{T}$, the horizontal total field would be zero and the needle would settle in no direction.

## fy7-1-L3-02
**Find:** why a steel clip drawn along a magnet becomes a magnet and why heating removes the magnetisation
**Principle:** Steel is ferromagnetic. Its atomic dipoles form magnetic domains whose directions vary in an unmagnetised piece. An external field aligns the domains, and in hard steel the alignment is kept. At a high enough temperature the thermal motion of the atoms destroys the alignment of the atomic dipoles.
**Model answer:** At first the domains of the clip point in different directions, and their effects cancel. When a pole of the magnet is drawn along the clip, always in the same direction, the field of the magnet turns the domains and makes those that point along the field grow. In hard steel the domains stay aligned when the magnet is taken away, so the clip becomes a permanent magnet with its own north pole and south pole. It magnetises the pins and attracts them. When the clip is heated hot enough (the Curie temperature of iron is about $770\,{}^\circ\text{C}$), the thermal motion of the atoms mixes up the alignment of the atomic dipoles and the domains disappear. When the clip cools, the domains form again but in random directions, so the clip is no longer a magnet.

## fy7-1-L3-03
**Given:** Helsinki $B_1 = 53\,\mu\text{T}$ and $I_1 = 74^\circ$, Longyearbyen $B_2 = 55\,\mu\text{T}$ and $I_2 = 82.5^\circ$ below the horizontal
**Find:** ratio of the horizontal components $k = B_\text{h1} : B_\text{h2}$, a plain number, and the reason why a compass works worse
**Principle:** A compass needle turns only in the horizontal plane, so it is steered only by the horizontal component of the field, $B_\text{h} = B\cos I$. The more steeply the field points into the ground, the smaller the horizontal part of it.
**Formula:** $k = \dfrac{B_\text{h1}}{B_\text{h2}} = \dfrac{B_1\cos I_1}{B_2\cos I_2}$
**Conversions:** Not needed: both fields are in microtesla, and the unit cancels.
**Substitution:** $k = \dfrac{53\,\mu\text{T} \cdot \cos 74^\circ}{55\,\mu\text{T} \cdot \cos 82.5^\circ} = \dfrac{14.6\,\mu\text{T}}{7.18\,\mu\text{T}} = 2.03$
**Answer:** about $2.0$ times, two significant figures like the fields $53\,\mu\text{T}$ and $55\,\mu\text{T}$. In Longyearbyen the field is almost vertical, so its horizontal component is only about half of the value in Helsinki.
**Model answer (why):** Only the horizontal component turns the needle. In Longyearbyen it is only about half of that in Helsinki, even though the whole field is greater, because the field points almost straight into the ground. The field that turns the needle is weak, so the needle settles slowly and even small disturbances, such as an iron object nearby, turn it easily. The answer is correct if it says that a compass is steered by the horizontal component and not by the whole field.
**Reasonableness:** The whole field is a little greater in Longyearbyen, but $\cos 82.5^\circ \approx 0.13$ is much smaller than $\cos 74^\circ \approx 0.28$, so the ratio is close to two. At the magnetic pole the field would be vertical, the horizontal component zero and the compass would not work at all.
