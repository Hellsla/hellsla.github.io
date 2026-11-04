## fy9-lampo-s1

### a)
**Given:** area $A = 1800\,\text{m}^2$, thickness of the water layer $d = 3.00\,\text{cm}$, density of water $\rho = 1000\,\text{kg/m}^3$; water $15.0\,{}^\circ\text{C}$, finished ice $-4.0\,{}^\circ\text{C}$; $c_\text{w} = 4190\,\text{J/(kg}\cdot\text{K)}$, $c_\text{i} = 2100\,\text{J/(kg}\cdot\text{K)}$, $s = 334\,\text{kJ/kg}$
**Find:** the quantity of heat $Q$ to be removed, in gigajoules
**Principle:** Energy is conserved: the refrigeration machine must remove all the energy the water releases on its way from water at $15.0\,{}^\circ\text{C}$ to ice at $-4.0\,{}^\circ\text{C}$. The way has three stages. The water cools to $0\,{}^\circ\text{C}$ ($Q = cm\Delta T$), freezes at constant temperature, releasing the latent heat of fusion ($Q = sm$), and the ice cools to $-4.0\,{}^\circ\text{C}$ ($Q = cm\Delta T$). The words "at least" mean that the heat conducted into the hall is not included.
**Formula:** $m = \rho A d$ and $Q = c_\text{w} m\,\Delta T_\text{w} + s m + c_\text{i} m\,\Delta T_\text{i}$, so $Q = \rho A d\,(c_\text{w}\,\Delta T_\text{w} + s + c_\text{i}\,\Delta T_\text{i})$
**Conversions:** $3.00\,\text{cm} = 3.00 \cdot 0.01\,\text{m} = 0.0300\,\text{m}$ and $334\,\text{kJ/kg} = 334\,000\,\text{J/kg}$. The changes in temperature are the same in kelvins: $\Delta T_\text{w} = 15.0\,\text{K}$ and $\Delta T_\text{i} = 4.0\,\text{K}$. Finally $1\,\text{GJ} = 10^{9}\,\text{J}$.
**Substitution:** $m = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1800\,\text{m}^2 \cdot 0.0300\,\text{m} = 54\,000\,\text{kg}$ and $Q = 54\,000\,\text{kg} \cdot (4190 \cdot 15.0 + 334\,000 + 2100 \cdot 4.0)\,\tfrac{\text{J}}{\text{kg}} = 54\,000\,\text{kg} \cdot 405\,250\,\tfrac{\text{J}}{\text{kg}} = 2.188 \cdot 10^{10}\,\text{J} = 21.9\,\text{GJ}$
**Answer:** $21.9\,\text{GJ}$, three significant figures like the thickness of the layer $3.00\,\text{cm}$ and the temperature of the water $15.0\,{}^\circ\text{C}$. The two figures of the cooling of the ice $4.0\,\text{K}$ concern only a small term.
**Reasonableness:** Stage by stage $Q_\text{w} = 3.39\,\text{GJ}$, $Q_\text{s} = 18.0\,\text{GJ}$ and $Q_\text{i} = 0.454\,\text{GJ}$, and the sum is the same $21.9\,\text{GJ}$. With rounded numbers $54\,\text{t} \cdot 400\,\text{kJ/kg} \approx 22\,\text{GJ}$. In kilowatt-hours it is about $6100\,\text{kWh}$, about as much as the electricity of a detached house in a year, which suits a large area of ice.

### b)
**Given:** $Q = 2.188 \cdot 10^{10}\,\text{J}$ from part a, power of the refrigeration machine $P = 350\,\text{kW}$
**Find:** the duration $t$ of the freezing in hours
**Principle:** The refrigeration machine removes energy at a constant power, so the time is the energy to be removed divided by the power (chapter *Power*). The result is a lower limit, because the machine also removes heat conducted into the hall and the concrete at the same time.
**Formula:** $P = \dfrac{Q}{t}$, so $t = \dfrac{Q}{P}$
**Conversions:** $350\,\text{kW} = 350 \cdot 1000\,\text{W} = 350\,000\,\text{W}$ and finally $1\,\text{h} = 3600\,\text{s}$.
**Substitution:** $t = \dfrac{2.188 \cdot 10^{10}\,\text{J}}{350\,000\,\text{W}} = 62\,500\,\text{s} = 62\,500 \cdot \tfrac{1}{3600}\,\text{h} = 17.4\,\text{h}$
**Answer:** at least $17.4\,\text{h}$, three significant figures like the power $350\,\text{kW}$ and the result of part a.
**Reasonableness:** About a day to make new ice is believable, and in reality it takes longer, because the layers are sprayed on gradually and the air of the hall warms the ice. Check: $350\,\text{kW} \cdot 17.4\,\text{h} \approx 6100\,\text{kWh} \approx 21.9\,\text{GJ}$.

### c)
**Find:** whether freezing is a quick stage once the water is already at $0\,{}^\circ\text{C}$
**Principle:** When water freezes it releases the latent heat of fusion although the temperature stays at $0\,{}^\circ\text{C}$: the particles settle into a regular order and the interaction energy between them decreases. The refrigeration machine must remove this energy at the same power as the rest (chapter *Changes of state*).
**Model answer:** The claim is wrong. Of the stages of part a, freezing needs $18.0\,\text{GJ}$, that is about $82\,\%$ of the total heat, cooling the water from $15.0\,{}^\circ\text{C}$ to $0\,{}^\circ\text{C}$ only about $16\,\%$ and cooling the ice about $2\,\%$. At the power $350\,\text{kW}$ cooling the water takes about $2.7\,\text{h}$, but freezing about $14\,\text{h}$. The temperature does not change during freezing, but energy must still be removed, because freezing releases $334\,\text{kJ}$ from every kilogram, as much as water cooling by almost $80\,\text{K}$. Freezing is therefore the slowest stage of the process, and the ice master should not expect it to happen in a moment.

### Yleisiä virheitä
- The latent heat of fusion of the freezing is forgotten because the temperature does not change, and the result is only about $3.8\,\text{GJ}$.
- The thickness is not converted to metres, so the mass is a hundred times too large.
- The specific heat capacity of water is used for the cooling of the ice.
- In part b the result is left in seconds or the power is left in kilowatts, and the unit of the answer goes wrong.
- In part c the claim is assessed without numbers.

### Hyväksytään myös
- In part a the stages can be calculated separately and added up; the answer $22\,\text{GJ}$ to two significant figures, when justified by the temperature of the ice $-4.0\,{}^\circ\text{C}$.

## fy9-lampo-s2

### a)
**Given:** mass of the birch logs $m_\text{wood} = 12.0\,\text{kg}$, heat of combustion $H = 15\,\text{MJ/kg}$, share transferred to the stone $\eta = 80\,\%$; stone mass $m_\text{stone} = 1800\,\text{kg}$, $c = 980\,\text{J/(kg}\cdot\text{K)}$
**Find:** the average rise in temperature $\Delta T$ of the stone mass
**Principle:** Burning wood releases the energy $Hm$ (chapter *Fuels and heat of combustion*), and $80\,\%$ of it is transferred to the stone; the rest leaves up the chimney with the flue gases. The stone stays solid, so the heat it receives raises its temperature according to $Q = cm\Delta T$ (chapter *Heating and cooling of matter*). During the firing some heat is already conducted from the stone to the room, which is ignored.
**Formula:** $Q = \eta H m_\text{wood}$ and $Q = c\,m_\text{stone}\,\Delta T$, so $\Delta T = \dfrac{\eta H m_\text{wood}}{c\,m_\text{stone}}$
**Conversions:** $15\,\text{MJ/kg} = 15 \cdot 10^{6}\,\text{J/kg}$ and $80\,\% = 0.80$.
**Substitution:** $\Delta T = \dfrac{0.80 \cdot 15 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} \cdot 12.0\,\text{kg}}{980\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 1800\,\text{kg}} = \dfrac{1.44 \cdot 10^{8}\,\text{J}}{1.764 \cdot 10^{6}\,\tfrac{\text{J}}{\text{K}}} = 81.6\,\text{K}$
**Answer:** about $82\,\text{K}$, two significant figures like the heat of combustion $15\,\text{MJ/kg}$ and the share $80\,\%$. The result is an average: the inner parts of the stone mass warm up more than the surface.
**Reasonableness:** If the stone is at $25\,{}^\circ\text{C}$ in the morning, its average temperature rises to about $105\,{}^\circ\text{C}$. The surface of the fireplace then feels hot but does not burn, because the surface is colder than the inner parts. The heat capacity of the stone mass, $1.76\,\text{MJ/K}$, is large, so $144\,\text{MJ}$ does not raise the temperature by hundreds of degrees.

### b)
**Given:** $Q = 144\,\text{MJ}$ from part a, time $t = 24\,\text{h}$
**Find:** the average heating power $P$ in kilowatts
**Principle:** In a day the stone cools back to its initial temperature, so it gives out to the rooms the same energy it received. The average power is the energy divided by the time (chapter *Power*).
**Formula:** $P = \dfrac{Q}{t}$
**Conversions:** $144\,\text{MJ} = 144 \cdot 10^{6}\,\text{J}$ and $24\,\text{h} = 24 \cdot 3600\,\text{s} = 86\,400\,\text{s}$; finally $1\,\text{W} = 0.001\,\text{kW}$.
**Substitution:** $P = \dfrac{144 \cdot 10^{6}\,\text{J}}{86\,400\,\text{s}} = 1667\,\text{W} = 1.67\,\text{kW}$
**Answer:** about $1.7\,\text{kW}$, two significant figures like the data of part a.
**Reasonableness:** The power equals one or two electric radiators, which is a usual average power for a fireplace. The power is not constant: right after the firing the stone is at its hottest and gives out more.

### c)
**Given:** heat loss $150\,\text{W}$ per kelvin, $21\,{}^\circ\text{C}$ indoors, $-10\,{}^\circ\text{C}$ outdoors; $P = 1667\,\text{W}$ from part b
**Find:** the share of the heat demand covered by the fireplace, as a percentage
**Principle:** The indoor temperature stays constant when the heating gives as much power as leaves the house. The power leaving is proportional to the difference between the indoor and outdoor temperatures, like $P = UA\Delta T$ (chapter *Heat transfer, energy balance and climate change*).
**Formula:** $P_\text{loss} = 150\,\tfrac{\text{W}}{\text{K}} \cdot (T_\text{in} - T_\text{out})$ and share $= \dfrac{P}{P_\text{loss}}$
**Conversions:** The temperature difference is the same in kelvins: $21\,{}^\circ\text{C} - (-10\,{}^\circ\text{C}) = 31\,\text{K}$. The ratio is turned into a percentage by multiplying by $100\,\%$.
**Substitution:** $P_\text{loss} = 150\,\tfrac{\text{W}}{\text{K}} \cdot 31\,\text{K} = 4650\,\text{W}$ and share $= \dfrac{1667\,\text{W}}{4650\,\text{W}} = 0.358 = 35.8\,\%$
**Answer:** about $36\,\%$, two significant figures like the power of the fireplace.
**Reasonableness:** To cover the whole demand, $4650\,\text{W} \cdot 86\,400\,\text{s} : (0.80 \cdot 15\,\text{MJ/kg}) \approx 33\,\text{kg}$ of wood would have to be burnt in a day, almost three times the evening load. The fireplace is therefore supplementary heating, as heat-storing fireplaces usually are.

### d)
**Find:** why the heating of a sheet-metal stove stops quickly and that of a heat-storing fireplace does not
**Principle:** The heat capacity $C = cm$ of a body tells how much energy a change of one kelvin needs. Heat is transferred from the surface to the room at a higher power the larger the temperature difference is (chapters *Heating and cooling of matter* and *Heat transfer, energy balance and climate change*).
**Model answer:** The mass and heat capacity of a thin sheet-metal stove are small, so the fire quickly heats its surface very hot. The large temperature difference to the room transfers energy at a high power, so the room warms up quickly. The sheet metal, however, stores hardly any energy, so when the fire goes out the stove soon cools and the heating stops. The $1800\,\text{kg}$ stone mass of the heat-storing fireplace stores the same energy with a temperature rise of only about $80\,\text{K}$. Its surface is moderately warm, so energy is transferred to the room at a lower power but over the whole day. The fireplace therefore evens out the heating over time: the energy does not disappear in either, but it is released at a different rate.

### Yleisiä virheitä
- In part a it is forgotten that only $80\,\%$ of the energy of the wood is transferred to the stone.
- The megajoules of the heat of combustion are not converted to joules, and the rise in temperature comes out as less than a kelvin.
- In part b the energy is divided by hours, but the result is given in watts.
- In part c the temperature difference is taken as $21\,\text{K} - 10\,\text{K} = 11\,\text{K}$ instead of $31\,\text{K}$.
- In part d it is said that the stone "contains heat"; the stone stores internal energy, and heat is energy in transfer.

## fy9-lampo-s3

### a)
**Find:** a graph of the mass of water vaporised $\Delta m$ as a function of the power $P$ of the heater and a model fitted to it
**Graph:** The power $P\ (\text{W})$ is on the horizontal axis and the mass $\Delta m\ (\text{g})$ on the vertical axis. The scales start from zero, so that the point where the line crosses the horizontal axis can be seen for part c.

<svg data-fig="fy9-lampo-s3-graph" viewBox="0 0 480 420" role="img" aria-label="Graph: the mass Δm of water vaporised in five minutes as a function of the power P of the immersion heater. Five black points at powers of 200–1000 W. A rising straight line is fitted to the points and extended as a dashed line to the horizontal axis and up to the power 1100 W. The line passes through the points (100 W; 4 g) and (1100 W; 137 g); these two points of the line are circled, and the slope, about 0.133 g/W, is read from them. The line crosses the horizontal axis at a power of about 70 W. The line does not pass through the origin." style="max-width:100%;font-size:26px">
  <line x1="107.5" y1="370" x2="107.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130.5" y1="370" x2="130.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="154" y1="370" x2="154" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="177.5" y1="370" x2="177.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200.5" y1="370" x2="200.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="370" x2="224" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247.5" y1="370" x2="247.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270.5" y1="370" x2="270.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="370" x2="294" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="370" x2="317.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340.5" y1="370" x2="340.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="370" x2="364" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="349.5" x2="364" y2="349.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="328.5" x2="364" y2="328.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="308" x2="364" y2="308" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="287.5" x2="364" y2="287.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="266.5" x2="364" y2="266.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="246" x2="364" y2="246" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="225.5" x2="364" y2="225.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="204.5" x2="364" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="184" x2="364" y2="184" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="163.5" x2="364" y2="163.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="142.5" x2="364" y2="142.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="122" x2="364" y2="122" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="101.5" x2="364" y2="101.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="80.5" x2="364" y2="80.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="60" x2="364" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="370" x2="378" y2="370" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M390,370 L377,376 L377,364 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="371" x2="84" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,34 L90,47 L78,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="107.5" y1="370" x2="107.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="130.5" y1="370" x2="130.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="154" y1="370" x2="154" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="177.5" y1="370" x2="177.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153" y="378.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$400$</div></foreignObject>
  <line x1="200.5" y1="370" x2="200.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="224" y1="370" x2="224" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="247.5" y1="370" x2="247.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="270.5" y1="370" x2="270.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="378.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$800$</div></foreignObject>
  <line x1="294" y1="370" x2="294" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="317.5" y1="370" x2="317.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="340.5" y1="370" x2="340.5" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="364" y1="370" x2="364" y2="377" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333" y="378.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$1200$</div></foreignObject>
  <line x1="77" y1="349.5" x2="84" y2="349.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="328.5" x2="84" y2="328.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="308" x2="84" y2="308" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="287.5" x2="84" y2="287.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="266.5" x2="84" y2="266.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37" y="251" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$50$</div></foreignObject>
  <line x1="77" y1="246" x2="84" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="225.5" x2="84" y2="225.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="204.5" x2="84" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="184" x2="84" y2="184" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="163.5" x2="84" y2="163.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="148" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$100$</div></foreignObject>
  <line x1="77" y1="142.5" x2="84" y2="142.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="122" x2="84" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="101.5" x2="84" y2="101.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="80.5" x2="84" y2="80.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="60" x2="84" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="44.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$150$</div></foreignObject>
  <foreignObject x="52" y="374.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="396" y="354.5" width="66" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$P\ (\text{W})$</div></foreignObject>
  <foreignObject x="74" y="2.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\Delta m\ (\text{g})$</div></foreignObject>
  <polyline points="130.5,334 317.5,115" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="100,370 130.5,334" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="317.5,115 340.5,87.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="130.5" cy="333" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="177.5" cy="281" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="224" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="270.5" cy="171" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="317.5" cy="114" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="107.5" cy="361.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="340.5" cy="87" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="100.1" cy="370" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="106.1" y1="364" x2="144.7" y2="351.4" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="148.5" y="336" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$P_\text{loss} \approx 70\,\text{W}$</span></div></foreignObject>
  <foreignObject x="81" y="110.5" width="157" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$k \approx 0.133\,\text{g/W}$</span></div></foreignObject>
</svg>

The circled points in the graph are the two points of the line from which the slope of part b is read. The orange point is where the line crosses the horizontal axis (part c).

**Model answer:** The points lie almost on a straight line: the mass vaporised grows steadily with the power. One rising straight line passing between the points is fitted to them. The line is not forced through the origin, because no physical reason requires it: part of the power can go into something other than vaporisation. The line is extended as a dashed line to the horizontal axis, and it crosses the axis clearly to the right of zero.

### b)
**Given:** the line of part a and the points read from it; measuring time $t = 300\,\text{s}$
**Find:** the specific latent heat of vaporisation of water $r$ in $\text{MJ/kg}$
**Principle:** The water boils all the time, so its temperature does not rise, and the part of the heater's power that is not conducted to the surroundings goes into vaporisation. Energy is conserved: $(P - P_\text{loss})\,t = r\,\Delta m$, where $P_\text{loss}$ is the loss power. From this $\Delta m = \dfrac{t}{r}\,P - \dfrac{t}{r}\,P_\text{loss}$, so the slope of the line is $\dfrac{t}{r}$ (chapters *Changes of state* and *Graphing and fitting a straight line*).
**Reading the graph:** Two points of the line far apart are read from the line, not measured points: $(100\,\text{W};\ 4.0\,\text{g})$ and $(1100\,\text{W};\ 137.0\,\text{g})$.
**Formula:** $k = \dfrac{\Delta(\Delta m)}{\Delta P} = \dfrac{t}{r}$, so $r = \dfrac{t}{k}$
**Conversions:** The slope from grams to kilograms: $1\,\text{g} = 10^{-3}\,\text{kg}$. The unit $\tfrac{\text{s}}{\text{kg/W}} = \tfrac{\text{W}\cdot\text{s}}{\text{kg}} = \tfrac{\text{J}}{\text{kg}}$, and finally $1\,\text{MJ} = 10^{6}\,\text{J}$.
**Substitution:** $k = \dfrac{137.0\,\text{g} - 4.0\,\text{g}}{1100\,\text{W} - 100\,\text{W}} = \dfrac{133.0\,\text{g}}{1000\,\text{W}} = 0.133\,\tfrac{\text{g}}{\text{W}}$ and $r = \dfrac{300\,\text{s}}{0.133 \cdot 10^{-3}\,\tfrac{\text{kg}}{\text{W}}} = 2.26 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} = 2.26\,\text{MJ/kg}$
**Answer:** $r \approx 2.26\,\text{MJ/kg}$. Three significant figures is the upper limit, because the slope of a line fitted by eye is accurate to about $\pm 2\,\%$; $2.3\,\text{MJ/kg}$ is an equally good answer.
**Reasonableness:** The table value is $2.26\,\text{MJ/kg}$, and the least-squares line also gives $2.26\,\text{MJ/kg}$. Check with one point: at $600\,\text{W}$ about $530\,\text{W}$ is left for vaporisation, and $530\,\text{W} \cdot 300\,\text{s} : 2.26\,\tfrac{\text{MJ}}{\text{kg}} \approx 70\,\text{g}$, as in the table.

### c)
**Given:** the line of part a, which crosses the horizontal axis; the slope $k = 0.133\,\text{g/W}$ of part b and the point of the line $(100\,\text{W};\ 4.0\,\text{g})$
**Find:** the power $P_\text{loss}$ at which, according to the line, the water would not vaporise, and its interpretation
**Principle:** Where the line crosses the horizontal axis, $\Delta m = 0$. According to the energy balance $(P - P_\text{loss})\,t = r\,\Delta m$ this happens when $P = P_\text{loss}$: the whole power of the heater is then conducted through the walls of the container and the water surface to the room. Boiling water is always at $100\,{}^\circ\text{C}$, so the temperature difference to the room, and therefore the loss power, stay the same at all powers (chapter *Heat transfer, energy balance and climate change*).
**Reading the graph:** The line extended as a dashed line crosses the horizontal axis at about $70\,\text{W}$.
**Formula:** $0 = k\,(P_\text{loss} - P_1) + \Delta m_1$, so $P_\text{loss} = P_1 - \dfrac{\Delta m_1}{k}$
**Conversions:** None needed: the slope and the mass are in grams and the power in watts.
**Substitution:** $P_\text{loss} = 100\,\text{W} - \dfrac{4.0\,\text{g}}{0.133\,\tfrac{\text{g}}{\text{W}}} = 100\,\text{W} - 30\,\text{W} = 70\,\text{W}$
**Answer:** $P_\text{loss} \approx 70\,\text{W}$, that is, about $70\,\text{W}$ of the heater's power is conducted to the room and does not vaporise water. One or two significant figures, because the intercept is found by extending the line outside the measured range, and a small change in the slope moves it by tens of watts.
**Reasonableness:** The least-squares line crosses the axis at $69\,\text{W}$. The loss power is a few per cent of the largest power but more than a third of the smallest, which suits conduction and convection from an open steel container.

### d)
**Find:** why the result $2.54\,\text{MJ/kg}$ from one measurement is too large and which result is more reliable
**Principle:** Energy is conserved: the energy $P\,t$ of the heater is divided between vaporisation and heat conducted to the room, $P\,t = r\,\Delta m + P_\text{loss}\,t$ (chapter *Changes of state*).
**Model answer:** In the calculation $r = \dfrac{P\,t}{\Delta m}$ from one measurement, all the energy of the heater is assumed to have gone into vaporisation. In reality about $70\,\text{W}$ is conducted to the room, so at the power $600\,\text{W}$ only about $530\,\text{W}$ is left for vaporisation. The calculation therefore has too much energy per unit of mass, and the result is about $600 : 530 \approx 1.13$ times, that is about $13\,\%$, too large. The result from the graph is more reliable. A constant loss power shifts the line sideways but does not change its slope, so the $r$ calculated from the slope does not include the loss. In addition, five measurements and a line fitted between them reduce the effect of the random error of a single reading. The method assumes that the loss power is the same at all powers. This is justified, because boiling water is always at $100\,{}^\circ\text{C}$, and the points lying on a straight line support the assumption.

### Yleisiä virheitä
- The line is forced through the origin, so the slope and $r$ are distorted and the loss power is not seen.
- The slope is calculated from two neighbouring measured points and not from the fitted line.
- In part b grams are not converted to kilograms, so the result is a thousand times too small.
- In part b the slope itself is taken as $r$ instead of $\dfrac{t}{k}$.
- In part d only "measurement error" is said, without saying which energy has been calculated wrongly and in which direction it changes the result.

### Hyväksytään myös
- A slope of $0.128$…$0.138\,\text{g/W}$ when the line has been fitted by eye between the points, and the corresponding results: $2.2$–$2.3\,\text{MJ/kg}$ in part b and $50$–$90\,\text{W}$ in part c.
- In part b the mass produced can also be calculated per second: $\dfrac{\Delta m}{t}$ as a function of power, and then the slope is $\dfrac{1}{r}$.

## fy9-lampo-s4

### a)
**Find:** why a lake freezes from the surface and why the water at the bottom is at about $4\,{}^\circ\text{C}$
**Principle:** Most substances expand as they warm, but water contracts between $0\,{}^\circ\text{C}$ and $4\,{}^\circ\text{C}$, so its density is greatest at about $4\,{}^\circ\text{C}$. Denser water sinks and lighter water rises (chapter *Thermal expansion*).
**Model answer:** In autumn cold air cools the surface of the lake. As long as the surface water is above $4\,{}^\circ\text{C}$, it becomes denser as it cools and sinks to the bottom, and warmer water rises in its place. In this way the whole lake gradually cools to about $4\,{}^\circ\text{C}$. When the surface cools below this, the water starts to expand as it cools: the colder water is now lighter than the water at $4\,{}^\circ\text{C}$ at the bottom, so it stays at the surface and freezes there. The densest water, at about $4\,{}^\circ\text{C}$, stays at the bottom and does not rise to the surface to cool. In addition, ice is lighter than water and floats, so the lake freezes from the surface downwards and not from the bottom upwards.

### b)
**Find:** where the energy of the freezing water goes and why the ice grows more slowly when it is thick
**Principle:** When water freezes it releases the latent heat of fusion $Q = sm$, although the temperature stays at $0\,{}^\circ\text{C}$ (chapter *Changes of state*). Heat is conducted from warm to cold, and for the same temperature difference the conducted power is smaller the thicker the layer is (chapter *Heat transfer, energy balance and climate change*).
**Model answer:** At the lower surface of the ice the water is at $0\,{}^\circ\text{C}$. For it to freeze, the latent heat of fusion must leave it, about $334\,\text{kJ}$ for every kilogram; a layer one centimetre thick on one square metre needs about $3\,\text{MJ}$. Energy is conserved, so this energy must be conducted through the ice to the cold air, and the ice grows only as fast as the energy is conducted away. The power conducted through the ice depends on the temperature difference between the frosty air and the lower surface at $0\,{}^\circ\text{C}$ and on the thickness of the layer. A thick layer insulates better, that is, its U-value is smaller, so in the same frost a smaller power is conducted through it. That is why thin autumn ice thickens quickly, but $40\,\text{cm}$ ice grows slowly in the same frost.

### c)
**Find:** whether a snow cover strengthens the ice
**Principle:** Snow contains a lot of air, and air is a poor conductor of heat (chapter *Heat transfer, energy balance and climate change*). For the ice to grow, the energy released in freezing must be conducted away (part b).
**Model answer:** The claim is wrong. Snow does not transfer "cold" to the ice: energy always flows from warmer to colder, that is, from the ice through the snow to the air. Snow is a poor conductor of heat, because it contains a lot of air. On top of the ice it acts as an insulator, like wool in a wall, so less energy is conducted away from the lower surface of the ice and less water freezes. Under a thick snow cover the ice therefore grows more slowly and stays thinner than bare ice. In addition, heavy snow can press the ice down, so that water rises through cracks on top of the ice and weak slush or snow ice forms. Snow weakens the ice rather than strengthening it.

### Yleisiä virheitä
- In part a it is only said that "ice floats", but it is not explained why the water at the bottom is at $4\,{}^\circ\text{C}$.
- It is claimed that cold water is always denser than warm water.
- In part b it is forgotten that freezing releases energy, and the growth is explained by temperature alone.
- In part c the idea of cold moving from the snow to the ice is accepted.

## fy9-lampo-s5

### a)
**Given:** water $m_\text{w} = 0.200\,\text{kg}$, $T_\text{w} = 40.0\,{}^\circ\text{C}$; ice $m_\text{i} = 0.0500\,\text{kg}$; final temperature $T = 14.3\,{}^\circ\text{C}$; $c_\text{w} = 4190\,\text{J/(kg}\cdot\text{K)}$
**Find:** the group's result $s$ in $\text{kJ/kg}$ and its assumption about the initial temperature of the ice
**Principle:** Energy is conserved when the cup and the air take no heat: the heat released by the water equals the heat received by the ice. In the group's calculation the ice only melts ($Q = sm$) and the meltwater warms from $0\,{}^\circ\text{C}$ to the final temperature ($Q = cm\Delta T$). There is no warming of the ice, so the group has assumed that the ice was at $0\,{}^\circ\text{C}$ (chapter *Thermal balance during a change of state*).
**Formula:** $c_\text{w} m_\text{w} (T_\text{w} - T) = s\,m_\text{i} + c_\text{w} m_\text{i}\,(T - 0\,{}^\circ\text{C})$, so $s = \dfrac{c_\text{w} m_\text{w} (T_\text{w} - T) - c_\text{w} m_\text{i} T}{m_\text{i}}$
**Conversions:** The temperature differences are the same in kelvins: the water cools by $25.7\,\text{K}$ and the meltwater warms by $14.3\,\text{K}$. Finally $1\,\text{kJ} = 1000\,\text{J}$.
**Substitution:** The heat released by the water is $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.200\,\text{kg} \cdot 25.7\,\text{K} = 21\,537\,\text{J}$ and the warming of the meltwater $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.0500\,\text{kg} \cdot 14.3\,\text{K} = 2996\,\text{J}$. So $s = \dfrac{21\,537\,\text{J} - 2996\,\text{J}}{0.0500\,\text{kg}} = 370\,800\,\tfrac{\text{J}}{\text{kg}} = 371\,\text{kJ/kg}$.
**Answer:** $371\,\text{kJ/kg}$, three significant figures like the masses and temperatures. The group has assumed that the ice was at $0\,{}^\circ\text{C}$, although it was taken from the freezer.
**Reasonableness:** The result is about $11\,\%$ larger than the table value $334\,\text{kJ/kg}$, which is too much for the random error of a careful measurement. It points to a systematic error, which is looked for in part b.

### b)
**Given:** the data of part a; initial temperature of the ice $T_\text{i} = -18.0\,{}^\circ\text{C}$, $c_\text{i} = 2100\,\text{J/(kg}\cdot\text{K)}$
**Find:** the corrected specific latent heat of fusion $s$ and an assessment of the conclusion
**Principle:** The ice from the freezer first warms from $-18.0\,{}^\circ\text{C}$ to $0\,{}^\circ\text{C}$, and that takes part of the energy released by the water. In the group's calculation this part has been counted as latent heat of fusion, so its result is too large. The warming of the ice is added to the energy balance.
**Formula:** $c_\text{w} m_\text{w} (T_\text{w} - T) = c_\text{i} m_\text{i} \Delta T_\text{i} + s\,m_\text{i} + c_\text{w} m_\text{i} T$, so $s = \dfrac{c_\text{w} m_\text{w} (T_\text{w} - T) - c_\text{i} m_\text{i} \Delta T_\text{i} - c_\text{w} m_\text{i} T}{m_\text{i}}$
**Conversions:** The warming of the ice $\Delta T_\text{i} = 0\,{}^\circ\text{C} - (-18.0\,{}^\circ\text{C}) = 18.0\,\text{K}$, the same in kelvins.
**Substitution:** $c_\text{i} m_\text{i} \Delta T_\text{i} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.0500\,\text{kg} \cdot 18.0\,\text{K} = 1890\,\text{J}$ and $s = \dfrac{21\,537\,\text{J} - 1890\,\text{J} - 2996\,\text{J}}{0.0500\,\text{kg}} = 333\,000\,\tfrac{\text{J}}{\text{kg}} = 333\,\text{kJ/kg}$
**Answer:** $333\,\text{kJ/kg}$, three significant figures like the measurements. The group's conclusion does not hold: the corrected result agrees with the table value $334\,\text{kJ/kg}$, and the difference came from a wrong assumption, not from the table. Nor does the cup explain the difference. If the cup took heat, the group's formula would also credit that to the ice, and the result would indeed be too large, but the difference $1890\,\text{J}$ would require a heat capacity of about $1890\,\text{J} : 25.7\,\text{K} \approx 70\,\text{J/K}$ for the cup. The heat capacity of a polystyrene cup of a few grams is only a few $\text{J/K}$, and the corrected value already agrees with the table.
**Reasonableness:** The warming of the ice takes $1890\,\text{J}$, only about $9\,\%$ of the heat released by the water, but divided by the small mass of ice it is $38\,\text{kJ/kg}$, exactly the difference of the results $371 - 333$. The corrected value differs from the table by less than one per cent, which is within the precision of the measurements.

### c)
**Find:** three improvements to the measurement and their justifications
**Principle:** A reliable measurement removes systematic errors or takes them into account and reduces random error by repetition (chapter *Measuring and the reliability of a measurement*).
**Model answer:** First, the ice is taken from a container of ice water, where it is melting and therefore exactly at $0\,{}^\circ\text{C}$, and its surface is dried with paper just before it is dropped into the water. Then the assumption of the calculation holds, and water on the surface of the ice does not increase the measured mass of ice. Another way is to measure the temperature of the ice and take its warming into account as in part b. Second, the mass of the ice is determined as a difference: the cup and the water are weighed before adding the ice and after the melting, so that the mass weighed is exactly the ice that ended up in the water, and ice that melted or fell during handling does not distort the result. Third, heat exchange with the surroundings is reduced: the cup has a lid, and the initial temperature is chosen to be as far above room temperature as the final temperature is below it, so that the heat coming from the room and the heat going to the room almost cancel each other. Finally, the measurement is repeated several times, and the mean and the spread of the results are reported.

### Yleisiä virheitä
- The warming of the meltwater from $0\,{}^\circ\text{C}$ to the final temperature is forgotten, which gives about $431\,\text{kJ/kg}$ in part a.
- In part b the specific heat capacity of water is used for the warming of the ice.
- The cup is accepted as the explanation without estimating how large its heat capacity would have to be: the heat capacity of a polystyrene cup is too small to explain the difference of $38\,\text{kJ/kg}$.
- In part c only "a more accurate thermometer" is suggested, without saying which error it affects.

### Hyväksytään myös
- In part a the warming of the meltwater can be calculated as a separate term and subtracted at the end; the result is the same.

## fy9-lampo-s6

### a)
**Given:** mass of the car $m = 1600\,\text{kg}$, speed $v = 90\,\text{km/h}$; mass of the discs $m_\text{discs} = 30\,\text{kg}$, $c = 450\,\text{J/(kg}\cdot\text{K)}$; share transferred to the discs $85\,\%$
**Find:** the rise in temperature $\Delta T$ of the discs
**Principle:** On a level road braking turns the kinetic energy of the car, through friction, into internal energy of the brakes; energy is conserved (chapter *Conservation of mechanical energy and the work–energy principle*). The share of air resistance in a short braking is small, so it is ignored. The discs stay solid, so the heat they receive raises their temperature according to $Q = cm\Delta T$.
**Formula:** $E_\text{k} = \tfrac{1}{2} m v^2$ and $0.85\,E_\text{k} = c\,m_\text{discs}\,\Delta T$, so $\Delta T = \dfrac{0.85 \cdot \tfrac{1}{2} m v^2}{c\,m_\text{discs}}$
**Conversions:** $90\,\text{km/h} = 90 \cdot \dfrac{1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$ and $85\,\% = 0.85$.
**Substitution:** $E_\text{k} = \tfrac{1}{2} \cdot 1600\,\text{kg} \cdot (25\,\tfrac{\text{m}}{\text{s}})^2 = 500\,000\,\text{J}$ and $\Delta T = \dfrac{0.85 \cdot 500\,000\,\text{J}}{450\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 30\,\text{kg}} = \dfrac{425\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 31.5\,\text{K}$
**Answer:** about $31\,\text{K}$, two significant figures like the mass of the discs $30\,\text{kg}$ and the speed $90\,\text{km/h}$.
**Reasonableness:** One stop heats the discs by a few tens of degrees, which fits experience: brake discs are hot after hard braking but do not glow. Air resistance would slightly reduce the energy reaching the discs, so the result is an upper limit.

### b)
**Given:** drop $h = 250\,\text{m}$, distance $s = 4.0\,\text{km}$, driving resistance $F = 450\,\text{N}$, constant speed; $g = 9.81\,\text{m/s}^2$; the data of part a
**Find:** the rise in temperature $\Delta T$ of the discs without cooling
**Principle:** The speed is constant, so the kinetic energy does not change. By the work–energy principle the decrease in potential energy $mgh$ goes into the work $Fs$ of the driving resistances and into the brakes (chapters *Kinetic energy, potential energy and mechanical energy* and *Conservation of mechanical energy and the work–energy principle*). Of the energy reaching the brakes, $85\,\%$ heats the discs.
**Formula:** $Q_\text{brakes} = mgh - Fs$ and $0.85\,Q_\text{brakes} = c\,m_\text{discs}\,\Delta T$, so $\Delta T = \dfrac{0.85\,(mgh - Fs)}{c\,m_\text{discs}}$
**Conversions:** $4.0\,\text{km} = 4.0 \cdot 1000\,\text{m} = 4000\,\text{m}$.
**Substitution:** $mgh = 1600\,\text{kg} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 250\,\text{m} = 3\,924\,000\,\text{J}$, $Fs = 450\,\text{N} \cdot 4000\,\text{m} = 1\,800\,000\,\text{J}$ and $\Delta T = \dfrac{0.85 \cdot 2\,124\,000\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = \dfrac{1\,805\,400\,\text{J}}{13\,500\,\tfrac{\text{J}}{\text{K}}} = 133.7\,\text{K}$
**Answer:** about $1.3 \cdot 10^{2}\,\text{K}$, that is $130\,\text{K}$, two significant figures like the distance $4.0\,\text{km}$.
**Reasonableness:** The downhill releases about four times more energy to the brakes than one stop from $90\,\text{km/h}$ ($1.81\,\text{MJ}$ and $0.43\,\text{MJ}$), so the rise is about four times larger. Without cooling the discs would heat to about $150\,{}^\circ\text{C}$, which is possible but already near the comfortable operating range of an ordinary brake.

### c)
**Given:** the energy reaching the discs in part b $Q = 1.805\,\text{MJ}$; the temperature of the discs rose by $80\,\text{K}$; $c\,m_\text{discs} = 13\,500\,\text{J/K}$
**Find:** the share of the energy transferred to the air, as a percentage, and the modes of transfer
**Principle:** Energy is conserved: the energy reaching the discs either stayed in the discs and raised their temperature ($Q = cm\Delta T$) or was transferred away during the descent. A hot disc gives out heat by convection to the air flowing past, radiates and conducts heat to the hub and the rim (chapter *Heat transfer, energy balance and climate change*).
**Formula:** $Q_\text{air} = Q - c\,m_\text{discs}\,\Delta T$ and share $= \dfrac{Q_\text{air}}{Q}$
**Conversions:** None needed: the energies are in joules, and the ratio is turned into a percentage by multiplying by $100\,\%$.
**Substitution:** $Q_\text{air} = 1\,805\,400\,\text{J} - 13\,500\,\tfrac{\text{J}}{\text{K}} \cdot 80\,\text{K} = 1\,805\,400\,\text{J} - 1\,080\,000\,\text{J} = 725\,400\,\text{J}$ and share $= \dfrac{725\,400\,\text{J}}{1\,805\,400\,\text{J}} = 0.402 = 40.2\,\%$
**Answer:** about $40\,\%$, two significant figures like the result of part b. The energy was transferred mainly by convection to the air flowing past the disc, in addition by thermal radiation and by conduction through the hub and the rim.
**Reasonableness:** The descent takes $4000\,\text{m} : 16.7\,\tfrac{\text{m}}{\text{s}} = 240\,\text{s}$, and on average about $7.5\,\text{kW}$ reaches the discs. On average $725\,\text{kJ} : 240\,\text{s} \approx 3\,\text{kW}$ was transferred to the air, which is believable for four hot discs in the airflow.

### d)
**Find:** why engine braking spares the brakes, in terms of energy
**Principle:** Energy is conserved, so the decrease in potential energy turns into internal energy somewhere. In engine braking the wheels turn the engine, whose friction opposes the motion (chapter *Conservation of mechanical energy and the work–energy principle*).
**Model answer:** In engine braking the potential energy does not disappear, but turns into internal energy of the engine through the friction of the engine. The cooling system of the engine is made to transfer large thermal powers to the air, so the engine does not overheat. Then little energy reaches the brake discs, they stay cool, and the brakes work at full power when they are really needed. The advice is therefore justified: the energy does not decrease, but the body it heats changes from the brakes to the engine.

### Yleisiä virheitä
- The speed is not converted to metres per second, so the kinetic energy is more than ten times too large.
- In part b all the potential energy is given to the brakes, and the result is about $250\,\text{K}$.
- In part b the kinetic energy is included, although the speed is constant.
- In part c it is said that the energy "was used up" or "disappeared", without saying where it was transferred.
- In part d it is claimed that in engine braking the energy does not turn into heat at all.

### Hyväksytään myös
- In part a the answer $31.5\,\text{K}$ or $32\,\text{K}$, when justified by rounding.
