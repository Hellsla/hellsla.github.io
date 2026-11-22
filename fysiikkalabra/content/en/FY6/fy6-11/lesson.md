# Uniform electric field

> **Why** do the dust particles of an air purifier end up on the surface of the plates of the device, although the air flows past the plates?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a sunny living room. On the left a slanting sunbeam from the window has dust particles floating in it. In the middle, a white column-shaped air purifier with a grille on its side stands on the floor. The dust particles travel in curved lines from the sunbeam towards the grille of the purifier. On the right there are a blue sofa and a potted plant." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A charge changes the space around it
In the chapter *Electric charge and Coulomb's law* two charges acted on each other with a force although they did not touch each other. This action at a distance is described with the **electric field**. A charge changes the space around it so that an electric force acts on every other charge there. The electric field exists at every point, even if there is no charge at that point right now for the field to act on. When a charge is brought to the point, the field acts on it. The idea is the same as in gravity: the Earth pulls an apple through a field, although the apple does not touch the Earth.

### Electric field strength
The field is studied with a small positive **test charge** $q$, so small that it does not change the positions of the charges that cause the field. When a force $\overline{F}$ acts on the test charge, the **electric field strength** at that point is the force divided by the test charge: $\overline{E} = \overline{F} : q$. So the electric field strength tells how large a force acts on one coulomb, and its unit is $\text{N/C}$. If a force of $100\,\mu\text{N}$ acts on a charge of $2.0\,\text{nC}$, the field strength is $5.0 \cdot 10^{4}\,\text{N/C}$. The quantity does not depend on the test charge: a doubled charge gets a doubled force, but the quotient stays the same. The symbol $E$ is the same as for the source voltage in the chapter *Electromotive force and internal resistance*, so in this chapter $E$ always means the electric field strength.

The electric field is a vector. Its direction is the direction in which the field pushes a positive charge. A force against the field acts on a negative charge, for example an electron. In the picture the field at the point $P$ is the same in both situations, but the direction of the force depends on the sign of the test charge.

```pysahdy
The field strength is measured with a test charge. The test charge is doubled at the same point. Does the field strength change?
---
No. The force doubles, but $E = F : q$ stays the same, because the charge grows by the same factor.
```

<svg data-fig="test" viewBox="0 0 600 330" role="img" aria-label="Two diagrams side by side, not to scale. In each, on the left there is a large positive charge Q and to the right of it a point P where a small test charge has been brought. The green arrow E of the electric field at P points to the right in both pictures, away from the charge Q. In the left picture the test charge is positive, and the red arrow F of the force on it points in the same direction as the field. In the right picture the test charge is negative, and the force arrow points in the opposite direction, towards the charge Q." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-test.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="20" y="19.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{positive } q$</div></foreignObject>
  <foreignObject x="47" y="207.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="165" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="210" y="69.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="224" y="127.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="65" y="265.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{F} = q\overline{E}$</div></foreignObject>
  <foreignObject x="320" y="19.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{negative } q$</div></foreignObject>
  <foreignObject x="347" y="207.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="465" y="191.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="510" y="69.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="400" y="127.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="365" y="265.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{F} = q\overline{E}$</div></foreignObject>
</svg>

### Field lines
The field is illustrated with **field lines**. The direction of a field line at each point is the direction of the field, that is, the arrow shows in which direction the force on a positive charge points. Field lines start from positive charges and end on negative charges. Where the lines are dense, the field is strong, and where they are sparse, the field is weak. Two field lines never cross each other, because the field has only one direction at every point. A field line is not the path of a charge: it shows the direction of the force, not the direction in which the charge moves.

The field lines of a point charge are radial straight lines, and they thin out farther from the charge, because the field weakens as the distance grows, as Coulomb's law says. The field lines of two charges of opposite signs curve from the positive charge to the negative one.

<svg data-fig="lines" viewBox="0 0 600 340" role="img" aria-label="Two field line pictures side by side, a diagram. On the left a positive point charge, from which twelve green straight field lines start evenly in all directions with arrows pointing outwards; the lines thin out farther from the charge. On the right a positive and an equally large negative charge side by side. The field lines start from the positive charge and curve to the negative charge; the lines are densest near the charges and between them. The lines do not cross each other." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-lines.webp" x="0" y="0" width="600" height="347.5" preserveAspectRatio="none"/>
  <foreignObject x="95" y="297.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q$</div></foreignObject>
  <foreignObject x="345" y="297.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+Q \text{ and } -Q$</div></foreignObject>
</svg>

### A uniform field between plates
When two large metal plates are placed parallel to each other, facing each other, and connected to the terminals of a voltage source, positive charge collects on one plate and an equal amount of negative charge on the other. Between the plates the field lines are straight, parallel and evenly spaced. Then the strength and direction of the field are the same everywhere between the plates: the field is **uniform**. The same force acts on a small charged ball whether it is near the positive plate, near the negative plate or halfway between them.

<svg data-fig="plates" viewBox="0 0 600 340" role="img" aria-label="Diagram: two horizontal parallel metal plates. The upper plate has positive charge and the lower one negative charge. Green field lines go from the upper plate to the lower one. Between the plates the lines are straight, parallel and evenly spaced, so the field is uniform. At the ends of the plates the lines curve outwards and thin out. Between the plates there are two identical positive balls at different places, and on each acts an equally large red force arrow F pointing down, in the direction of the field." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-plates.webp" x="1.2" y="-1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="62" y="91.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="62" y="223.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="224" y="161.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="420" y="201.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="540" y="157.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
</svg>

Why does the force not grow when the ball is moved closer to a plate? Near the plate the nearest charges act strongly on the ball, but then most of the charges of the plate are at the sides of the ball. Their forces point almost along the plate, so the sideways parts cancel each other and do not pull the ball towards the plate. Farther from the plate each charge acts more weakly, but the force of more and more charges points almost perpendicular to the plate. For a large plate these two effects balance each other, so the field of the plate does not depend on the distance from the plate. Outside the plates the fields of the positive and the negative plate point in opposite directions and almost cancel each other, but between the plates they point in the same direction and add up. The field is uniform only between the plates and far from the ends of the plates. At the ends of the plates the field lines curve outwards and thin out.

### The air purifier
In an electric air purifier the air first passes through a charging section, where the dust particles get an electric charge. Then the air flows between parallel plates, and there is a voltage of several kilovolts between the plates. The uniform field pushes every charged particle towards a plate with the same force the whole way, so the particle drifts to the surface of the plate and stays there, although the air goes on. The same principle is used in the electrostatic precipitators of power plants, which remove almost all the dust from flue gases.

## Formula: Electric field strength
The electric field strength at a point where an electric force $\overline{F}$ acts on a small test charge $q$ is
```kaavat
electric field strength :: \overline{E} = \frac{\overline{F}}{q}
```
where $\overline{E}$ is the electric field strength ($\text{N/C}$), $\overline{F}$ the electric force ($\text{N}$) and $q$ the test charge ($\text{C}$). When the field is known, the force on any charge is obtained by multiplying: $\overline{F} = q\overline{E}$. If $q$ is negative, the force points against the field.

### The field from the voltage of the plates
The strength of a uniform field can be calculated from the voltage between the plates. When a positive charge $q$ moves from the positive plate to the negative one, the same force $F = qE$ acts on it the whole way, and the field does the work $W = Fd = qEd$. According to the chapter *Circuit, electric current and voltage*, voltage tells the energy per unit charge, so the same work is also $W = qU$. When these are set equal, the charge cancels, and the strength of a uniform field is
```kaavat
voltage in a uniform electric field :: E = \frac{U}{d}
```
where $E$ is the electric field strength ($\text{V/m}$), $U$ the voltage between the plates ($\text{V}$) and $d$ the distance between the plates ($\text{m}$). The units $\text{V/m}$ and $\text{N/C}$ are the same unit, because $1\,\text{V/m} = 1\,\tfrac{\text{J}}{\text{C} \cdot \text{m}} = 1\,\tfrac{\text{N} \cdot \text{m}}{\text{C} \cdot \text{m}} = 1\,\text{N/C}$. For example, a voltage of $2.0\,\text{kV}$ across a plate distance of $4.0\,\text{cm}$ gives the field $2000\,\text{V} : 0.040\,\text{m} = 5.0 \cdot 10^{4}\,\text{V/m}$.

```pysahdy
The voltage between the plates is $600\,\text{V}$ and the distance is $3.0\,\text{cm}$. How strong is the field between the plates?
---
The field strength is $E = U : d$. With $d = 0.030\,\text{m}$, $E = 600\,\text{V} : 0.030\,\text{m}$, so $E = 2.0 \cdot 10^{4}\,\text{V/m}$.
```

<svg data-fig="work" viewBox="0 0 600 340" role="img" aria-label="Diagram, not to scale: a voltage source U is connected with wires to two horizontal plates, the positive terminal to the upper one and the negative terminal to the lower one. The distance of the plates is d. Between the plates green field lines point down. A positive charge q starts near the upper plate and moves along a dashed line to the lower plate. The same red force F acts on it the whole way, equal to q times E and pointing down. When the charge travels the distance d, the field does the work F times d, which is equal to q times U." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-work.webp" x="7.4" y="1.2" width="591.1" height="342.4" preserveAspectRatio="none"/>
  <foreignObject x="28" y="155.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="122" y="135.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="122" y="175.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="284" y="105.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$q$</div></foreignObject>
  <foreignObject x="342" y="157.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = q\overline{E}$</span></div></foreignObject>
  <foreignObject x="566" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="210" y="285.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = Fd = qEd = qU$</div></foreignObject>
</svg>

The equation holds only in a uniform field, that is, between the plates when the plates are large compared with the distance between them. The graph shows the field calculated with the plate model of the simulation at the height halfway between the plates. From the middle of the plates to about $7\,\text{cm}$ away the field is $U : d = 50\,\text{kV/m}$, but at the ends of the plates and outside them it weakens. In an air purifier a voltage of $5.0\,\text{kV}$ and a plate gap of $1.0\,\text{cm}$ give the field $5.0 \cdot 10^{5}\,\text{V/m}$. On the surface of the Earth in clear weather there is a field of about $100\,\text{V/m}$, and under a thundercloud the field can be as much as tens of kilovolts per metre.

<svg data-fig="profile" viewBox="0 0 600 340" role="img" aria-label="Graph to scale, calculated with the plate model of the simulation: the electric field strength E in kilovolts per metre at the height halfway between the plates as a function of the position x, when the voltage is 2.0 kV and the plate distance 4.0 cm. The middle of the plates is x = 0 and the end of the plate is x = 10 cm. In the range 0–7 cm the field strength is constant 50 kV/m, which is U divided by d. Near the end of the plate it starts to decrease, at the end of the plate it is about 38 kV/m, and outside the plates at 14 cm it is only about 9 kV/m." style="max-width:100%;font-size:24px">
  <line x1="151.5" y1="280" x2="151.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207" y1="280" x2="207" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262.5" y1="280" x2="262.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="280" x2="317.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="373" y1="280" x2="373" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428.5" y1="280" x2="428.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="484" y1="280" x2="484" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="243.5" x2="484" y2="243.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="206.5" x2="484" y2="206.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="484" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="133.5" x2="484" y2="133.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="484" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="484" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="280" x2="498" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M510,280 L497,286 L497,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="281" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="151.5" y1="280" x2="151.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="141.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="207" y1="280" x2="207" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="197" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="262.5" y1="280" x2="262.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="317.5" y1="280" x2="317.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="307.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="373" y1="280" x2="373" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="356.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="428.5" y1="280" x2="428.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="484" y1="280" x2="484" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$14$</div></foreignObject>
  <line x1="89" y1="243.5" x2="96" y2="243.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="229" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="206.5" x2="96" y2="206.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="192" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="133.5" x2="96" y2="133.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="119" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="82" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="66" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="516" y="265.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{kV/m})$</div></foreignObject>
  <line x1="373" y1="60" x2="373" y2="280" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="381" y="60" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{end of plate}$</span></div></foreignObject>
  <line x1="96" y1="96.5" x2="290" y2="96.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="96,96.5 123.5,96.5 151.5,96.5 179,96.5 207,96.5 234.5,96.5 262.5,97 290,97.5 304,98 317.5,100 331.5,103.5 345.5,110.5 359.5,123 373,141 387,162.5 401,183.5 414.5,201.5 428.5,215.5 456.5,235 484,247" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="106.5" y="60" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E = \tfrac{U}{d}$</span></div></foreignObject>
</svg>

### A charged particle in a uniform field
In a uniform field a constant force $F = qE$ acts on a charged particle, so by Newton's second law its acceleration $a = qE : m$ is constant in vacuum when other forces are small. A particle at rest accelerates uniformly along the field, a positive one in the direction of the field and a negative one against the field. If the particle enters between the plates from the side, its path curves towards one plate in the same way as the path of a ball thrown horizontally curves downwards. In a field of $5.0 \cdot 10^{4}\,\text{V/m}$ a force of $8.0 \cdot 10^{-15}\,\text{N}$ acts on an electron, but its weight is only $8.9 \cdot 10^{-30}\,\text{N}$. The weight of an electron can therefore be ignored. For heavier bodies, such as oil droplets and dust particles, gravity can be as important as the electric force.

```pysahdy
The charge of a particle doubles, but its mass and the field stay the same. How does the acceleration change?
---
It doubles, because $a = qE : m$ is directly proportional to the charge $q$.
```

<svg data-fig="electron" viewBox="0 0 600 340" role="img" aria-label="Diagram, not to scale: two horizontal plates, the upper one positive and the lower one negative; green field lines point down. An electron comes between the plates from the left horizontally, and its blue velocity arrow v points to the right. Between the plates the path of the electron curves evenly upwards towards the positive plate. At a point on the path there are a red force arrow F and an orange acceleration arrow a, both pointing up, against the field." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-11-electron.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="556" y="121.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="90" y="207.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="262" y="121.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F}$</span></div></foreignObject>
  <foreignObject x="340" y="127.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{a}$</span></div></foreignObject>
  <foreignObject x="40" y="215.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-e$</div></foreignObject>
</svg>

## Worked example
A small oil droplet with a mass of $4.9 \cdot 10^{-15}\,\text{kg}$ hovers at rest between two horizontal plates. The distance of the plates is $6.0\,\text{mm}$, the voltage is $600\,\text{V}$, and the positive plate is on top. How large is the charge of the droplet, and how many elementary charges $e = 1.602 \cdot 10^{-19}\,\text{C}$ is it?

<!-- vaihe -->

**Given and find.** Mass $m = 4.9 \cdot 10^{-15}\,\text{kg}$, plate distance $d = 6.0\,\text{mm}$, voltage $U = 600\,\text{V}$, acceleration of free fall $g = 9.81\,\text{m/s}^2$ and elementary charge $e$. We are asked for the magnitude $q$ of the charge of the droplet and the number $n$ of elementary charges.

<!-- vaihe -->

**Principle.** The field between the plates is uniform, so $E = U : d$. The droplet is at rest, so by Newton's first law the forces on it cancel each other. The weight $mg$ points down, so the electric force $qE$ must point up, towards the positive plate: the droplet is negative. The charge is a multiple of the elementary charge, so the number is obtained by dividing.

<!-- vaihe -->

**Formula solved.**
```latex
\begin{aligned}
&E = \frac{U}{d} \\
&qE = mg \\
&q = \frac{mg}{E} \\
&n = \frac{q}{e}
\end{aligned}
```

<!-- vaihe -->

**Conversions.** $d = 6.0\,\text{mm} = 6.0 \cdot 0.001\,\text{m} = 6.0 \cdot 10^{-3}\,\text{m}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
E &= \frac{U}{d} \\
&= \frac{600\,\text{V}}{6.0 \cdot 10^{-3}\,\text{m}} \\
&= 1.0 \cdot 10^{5}\,\text{V/m} \\
mg &= 4.9 \cdot 10^{-15}\,\text{kg} \\
&\quad \cdot 9.81\,\text{m/s}^2 \\
&= 4.807 \cdot 10^{-14}\,\text{N} \\
q &= \frac{mg}{E} \\
&= \frac{4.807 \cdot 10^{-14}\,\text{N}}{1.0 \cdot 10^{5}\,\text{V/m}} \\
&= 4.807 \cdot 10^{-19}\,\text{C} \\
n &= \frac{q}{e} \\
&= \frac{4.807 \cdot 10^{-19}\,\text{C}}{1.602 \cdot 10^{-19}\,\text{C}} \\
&= 3.0
\end{aligned}
```

<!-- vaihe -->

**Answer.** The charge of the droplet is $-4.8 \cdot 10^{-19}\,\text{C}$, that is, three elementary charges: the droplet has three extra electrons. The charge is given with two significant figures like the mass and the distance.

<!-- vaihe -->

**Reasonableness.** The electric force of three elementary charges in the field $1.0 \cdot 10^{5}\,\text{V/m}$ is $3 \cdot 1.602 \cdot 10^{-19}\,\text{C} \cdot 1.0 \cdot 10^{5}\,\text{V/m} = 4.8 \cdot 10^{-14}\,\text{N}$, equal to the weight of the droplet $4.9 \cdot 10^{-15}\,\text{kg} \cdot 9.81\,\text{m/s}^2 = 4.8 \cdot 10^{-14}\,\text{N}$. The number is almost exactly a whole number, as it should be, because charge is made of elementary charges.

## Common misconception
Many people think that the force on a charged ball between plates grows when the ball is moved closer to a plate, because by Coulomb's law the force grows when the distance gets smaller. Coulomb's law applies to point charges. The field of large plates is uniform: between the plates the force is the same everywhere and does not depend on how close to a plate the ball is. The strength depends only on the voltage and the distance of the plates, $E = U : d$.

Another misconception is that a field line is the path a charge travels, or that the field exists only where the lines are. A field line shows the direction of the force at each point, and there is field also between the lines. A third mistake is to think that the electric field strength depends on the test charge. A larger charge gets a larger force, but the quotient of the force and the charge, $E = F : q$, is the same.

## Summary
- A charge changes the space around it: the electric field acts with an electric force on every charge there.
- The electric field strength is the force on a test charge divided by the charge, $\overline{E} = \overline{F} : q$, unit $\text{N/C} = \text{V/m}$. The force on a charge is $\overline{F} = q\overline{E}$: for a positive charge in the direction of the field, for a negative charge against the field.
- Field lines start from positive charges and end on negative charges, do not cross each other, and their density tells the strength of the field.
- Between parallel plates the field is uniform: the same strength and direction everywhere between the plates, when one is far from the ends of the plates.
- The strength of a uniform field is $E = U : d$. A constant force acts on a charged particle in it, so its acceleration is constant in vacuum when other forces are small.
