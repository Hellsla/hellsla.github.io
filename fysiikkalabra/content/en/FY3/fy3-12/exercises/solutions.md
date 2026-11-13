## fy3-12-L1-01
**Given:** $A = 45\,\text{m}^2$, $T_\text{in} = 22\,{}^\circ\text{C}$, $T_\text{out} = -18\,{}^\circ\text{C}$; roof $U = 0.24\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$
**Find:** the thermal power $P$ conducted through the roof, in watts
**Principle:** Heat is conducted through the structure from warm to cold, and when the temperatures stay constant, the power is proportional to the area and the temperature difference. The U-value tells you how much power passes through one square metre when the difference is one kelvin.
**Formula:** $P = UA\Delta T$, where $\Delta T = T_\text{in} - T_\text{out}$; the power is already solved: $P = UA(T_\text{in} - T_\text{out})$
**Conversions:** The temperature difference is the same in degrees Celsius and in kelvins, so $\Delta T = 22\,{}^\circ\text{C} - (-18\,{}^\circ\text{C}) = 40\,\text{K}$. No other conversions are needed, because $U$ is already in $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$.
**Substitution:** $P = 0.24\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 45\,\text{m}^2 \cdot 40\,\text{K} = 432\,\text{W}$
**Answer:** $430\,\text{W}$, two significant figures. The limiting data are the U-value $0.24$, the area $45\,\text{m}^2$ and the difference of whole degrees $\Delta T = 40\,\text{K}$, all with two figures, so the calculator result $432\,\text{W}$ is rounded.
**Reasonableness:** With rounded numbers $0.25 \cdot 45 \cdot 40 \approx 450\,\text{W}$, so $432\,\text{W}$ is the right order of magnitude. Units: $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot \text{m}^2 \cdot \text{K} = \text{W}$. If it were the same temperature indoors and outdoors, $\Delta T = 0$ and $P = 0$, as it should be. The power corresponds to a small electric radiator, and the walls, windows and floor add to the heating need of the cabin.

## fy3-12-L1-02
**Given:** $P = 96\,\text{W}$, $A = 2.0\,\text{m}^2$, $T_\text{in} = 21\,{}^\circ\text{C}$, $T_\text{out} = -19\,{}^\circ\text{C}$
**Find:** the U-value $U$ of the door, in $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$
**Principle:** The door conducts heat out steadily when the temperatures stay constant, so the measured power is proportional to the area and the temperature difference. The constant of proportionality is exactly the U-value, and you get it by dividing the power by the area and the difference.
**Formula:** $P = UA\Delta T$, so $U = \dfrac{P}{A\Delta T}$
**Conversions:** The temperature difference is the same in kelvins and in degrees Celsius: $\Delta T = 21\,{}^\circ\text{C} - (-19\,{}^\circ\text{C}) = 40\,\text{K}$. No other conversions are needed, because the power is in watts and the area in square metres.
**Substitution:** $U = \dfrac{96\,\text{W}}{2.0\,\text{m}^2 \cdot 40\,\text{K}} = \dfrac{96\,\text{W}}{80\,\text{m}^2\cdot\text{K}} = 1.2\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$
**Answer:** $1.2\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, two significant figures. The limiting data are the power $96\,\text{W}$, the area $2.0\,\text{m}^2$ and the difference of whole degrees $\Delta T = 40\,\text{K}$, all with two figures.
**Reasonableness:** Check with the formula: $1.2 \cdot 2.0 \cdot 40 = 96\,\text{W}$, as measured. The U-value of a new front door is about $1.0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$ and that of a modern wall $0.17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, so the value of the old door is of the same order as a new door and clearly worse than a wall, as you would expect.

## fy3-12-L1-03
**Given:** $A = 28\,\text{m}^2$, $U = 0.25\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $P = 210\,\text{W}$
**Find:** the difference $\Delta T$ between the indoor and outdoor temperature, in kelvins
**Principle:** The power conducted through the wall is proportional to the temperature difference when the area and the U-value of the wall do not change. So from a known power you can work out how large the temperature difference across the wall is.
**Formula:** $P = UA\Delta T$, so $\Delta T = \dfrac{P}{UA}$
**Conversions:** No conversions are needed: the power is in watts, the area in square metres and $U$ in $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, so the result comes out directly in kelvins. A temperature difference in kelvins is the same as in degrees Celsius.
**Substitution:** $\Delta T = \dfrac{210\,\text{W}}{0.25\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 28\,\text{m}^2} = \dfrac{210\,\text{W}}{7.0\,\tfrac{\text{W}}{\text{K}}} = 30\,\text{K}$
**Answer:** $30\,\text{K}$, two significant figures. The limiting data are the power $210\,\text{W}$, the U-value $0.25$ and the area $28\,\text{m}^2$, all with at least two figures, so the result $30\,\text{K}$ is a two-figure value.
**Reasonableness:** For example, $21\,{}^\circ\text{C}$ indoors and $-9\,{}^\circ\text{C}$ outdoors gives a difference of $30\,\text{K}$, which is an ordinary winter night. Back-calculation: $0.25 \cdot 28 \cdot 30 = 210\,\text{W}$. Units: $\text{W} / (\text{W/K}) = \text{K}$.

## fy3-12-L1-04
**Given:** $P = 3.5\,\text{kW}$, $t = 14\,\text{h}$
**Find:** the energy $E$ the heating must produce, in kilowatt-hours
**Principle:** The indoor temperature stays the same only if the heating produces the same energy as escapes from the house. The power is constant, so the energy is the power multiplied by the time.
**Formula:** $E = Pt$
**Conversions:** No conversions are needed, because a kilowatt multiplied by an hour is directly a kilowatt-hour: $1\,\text{kW} \cdot 1\,\text{h} = 1\,\text{kWh}$. For comparison in joules, $1\,\text{kWh} = 3.6\,\text{MJ}$.
**Substitution:** $E = 3.5\,\text{kW} \cdot 14\,\text{h} = 49\,\text{kWh}$
**Answer:** $49\,\text{kWh}$, two significant figures. The limiting data are the power $3.5\,\text{kW}$ and the time $14\,\text{h}$, each with two figures.
**Reasonableness:** With rounded numbers $3.5 \cdot 14 \approx 4 \cdot 12 = 48$, so the result is correct. In joules the energy is $49 \cdot 3.6\,\text{MJ} \approx 176\,\text{MJ}$. The consumption over a whole frosty day would be $3.5\,\text{kW} \cdot 24\,\text{h} = 84\,\text{kWh}$, which fits an electrically heated detached house.

## fy3-12-L1-05
**Given:** read from the figure, $341\,\tfrac{\text{W}}{\text{m}^2}$ comes from the Sun and $102\,\tfrac{\text{W}}{\text{m}^2}$ of it is reflected; the mean temperature of the Earth stays constant
**Find:** the power per square metre leaving into space as thermal radiation $P_\text{rad}$
**Principle:** The temperature stays constant, so the Earth is in energy balance: the power it absorbs is equal to the thermal radiation leaving into space. The reflected radiation does not warm the Earth, so the absorbed part is the incoming power minus the reflected power.
**Reading the graph:** The left arrow of the figure gives the incoming power $P_\text{in} = 341\,\tfrac{\text{W}}{\text{m}^2}$ and the arrow between the Sun and the Earth that points up and to the left the reflected power $P_\text{refl} = 102\,\tfrac{\text{W}}{\text{m}^2}$. The dashed arrow on the right, whose value is a question mark and which is labelled "heat radiation", is the thermal radiation asked for.
**Formula:** $P_\text{abs} = P_\text{in} - P_\text{refl}$ and in balance $P_\text{rad} = P_\text{abs}$
**Conversions:** Not needed: all the powers are in the unit $\tfrac{\text{W}}{\text{m}^2}$.
**Substitution:** $P_\text{rad} = 341\,\tfrac{\text{W}}{\text{m}^2} - 102\,\tfrac{\text{W}}{\text{m}^2} = 239\,\tfrac{\text{W}}{\text{m}^2}$
**Answer:** $239\,\tfrac{\text{W}}{\text{m}^2}$, three significant figures, because the values read, $341$ and $102$, are given in whole watts per square metre and the difference is known with the same precision.
**Reasonableness:** Check the balance: $102 + 239 = 341\,\tfrac{\text{W}}{\text{m}^2}$, so all the incoming power is accounted for. The reflected fraction is $102 / 341 \approx 0.30$, that is, about $30\,\%$ of the incoming radiation. The result is smaller than the incoming power, as it should be.

## fy3-12-L2-01
**Given:** walls $A_\text{s} = 70\,\text{m}^2$, $U_\text{s} = 0.50\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$; roof $A_\text{y} = 50.0\,\text{m}^2$, $U_\text{y} = 0.30\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$; power of the radiators $P = 2.0\,\text{kW}$; $T_\text{in} = 20\,{}^\circ\text{C}$
**Find:** the lowest outdoor temperature $T_\text{out}$ at which the radiators are enough
**Principle:** The walls and the roof conduct heat in parallel, so their powers are added. The indoor temperature stays constant when the power of the radiators is equal to the conducted power. The lowest outdoor temperature corresponds to the situation in which the radiators work at full power.
**Formula:** $P = (U_\text{s} A_\text{s} + U_\text{y} A_\text{y})(T_\text{in} - T_\text{out})$, so $T_\text{out} = T_\text{in} - \dfrac{P}{U_\text{s} A_\text{s} + U_\text{y} A_\text{y}}$
**Conversions:** The power is converted to watts: $2.0\,\text{kW} = 2000\,\text{W}$. The temperature difference is the same in kelvins and in degrees Celsius, so the outdoor temperature can be calculated directly in degrees Celsius.
**Substitution:** $U_\text{s} A_\text{s} + U_\text{y} A_\text{y} = 0.50 \cdot 70\,\tfrac{\text{W}}{\text{K}} + 0.30 \cdot 50.0\,\tfrac{\text{W}}{\text{K}} = 50\,\tfrac{\text{W}}{\text{K}}$. $T_\text{out} = 20\,{}^\circ\text{C} - \dfrac{2000\,\text{W}}{50\,\tfrac{\text{W}}{\text{K}}} = 20\,{}^\circ\text{C} - 40\,\text{K} = -20\,{}^\circ\text{C}$
**Answer:** $-20\,{}^\circ\text{C}$, two significant figures. The limiting data are the power $2.0\,\text{kW}$ and the conduction coefficient $50\,\tfrac{\text{W}}{\text{K}}$ (the sum $35 + 15.0$ keeps two figures, because the wall term $0.50 \cdot 70$ is a two-figure value), so $\Delta T = 40\,\text{K}$ and $T = 20\,{}^\circ\text{C} - 40\,\text{K} = -20\,{}^\circ\text{C}$ in whole degrees.
**Reasonableness:** Back-calculation: $50\,\tfrac{\text{W}}{\text{K}} \cdot 40\,\text{K} = 2000\,\text{W}$, which is the power of the radiators. The result is below the indoor temperature, as it should be. In colder weather the loss exceeds $2.0\,\text{kW}$, and the cabin cools until the balance settles at a lower indoor temperature.

## fy3-12-L2-02
**Given:** $A = 130\,\text{m}^2$, $U = 0.090\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $\Delta T = 21\,\text{K}$, $t = 230\,\text{days}$, price $h = 0.11\,\tfrac{\text{€}}{\text{kWh}}$
**Find:** the cost $H$ of the escaping heat in euros over the heating season
**Principle:** The temperature difference stays constant on average, so the conducted power is constant and the energy is the power multiplied by the time. The cost is the amount of energy multiplied by the unit price.
**Formula:** $P = UA\Delta T$, $E = Pt$ and $H = hE$, so $H = hUA\Delta T\,t$
**Conversions:** The price is per kilowatt-hour, so the power is converted to kilowatts and the time to hours: $t = 230 \cdot 24\,\text{h} = 5520\,\text{h}$, and $P$ in watts is divided by a thousand.
**Substitution:** $P = 0.090\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 130\,\text{m}^2 \cdot 21\,\text{K} = 245.7\,\text{W} = 0.2457\,\text{kW}$. $E = 0.2457\,\text{kW} \cdot 5520\,\text{h} = 1356.264\,\text{kWh}$. $H = 0.11\,\tfrac{\text{€}}{\text{kWh}} \cdot 1356.264\,\text{kWh} \approx 149.2\,\text{€}$
**Answer:** $150\,\text{€}$, two significant figures. The limiting data are the U-value $0.090$, the price $0.11\,\tfrac{\text{€}}{\text{kWh}}$ and the temperature difference $21\,\text{K}$, all with two figures, so the calculator result $149.2\,\text{€}$ is rounded.
**Reasonableness:** With rounded numbers $0.25\,\text{kW} \cdot 5500\,\text{h} \approx 1400\,\text{kWh}$ and $1400 \cdot 0.11 \approx 150\,\text{€}$. A well-insulated roof, despite its large area, loses only about $250\,\text{W}$. District heating for a whole house typically costs over a thousand euros a year, so one building part is only a small share of the bill.

## fy3-12-L2-03
**Given:** old $U_\text{v} = 2.8\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, new $U_\text{u} = 0.80\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $A = 14\,\text{m}^2$, $T_\text{in} = 21\,{}^\circ\text{C}$, $T_\text{out} = -24\,{}^\circ\text{C}$, $t = 7\,\text{days}$
**Find:** the energy $E$ saved in a week, in kilowatt-hours
**Principle:** Through each type of window the power $UA\Delta T$ is conducted, with the same area and the same temperature difference, when the temperatures stay constant. The saving is the difference of the loss powers multiplied by the time.
**Formula:** $\Delta P = U_\text{v} A\Delta T - U_\text{u} A\Delta T$, so $E = \Delta P\,t = (U_\text{v} - U_\text{u})A\Delta T\,t$
**Conversions:** The temperature difference is the same in kelvins: $\Delta T = 21\,{}^\circ\text{C} - (-24\,{}^\circ\text{C}) = 45\,\text{K}$. The time is $t = 7 \cdot 24\,\text{h} = 168\,\text{h}$, and the power is converted to kilowatts.
**Substitution:** $\Delta P = (2.8 - 0.80)\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 14\,\text{m}^2 \cdot 45\,\text{K} = 1260\,\text{W} = 1.26\,\text{kW}$. $E = 1.26\,\text{kW} \cdot 168\,\text{h} = 211.68\,\text{kWh}$
**Answer:** $210\,\text{kWh}$, two significant figures. The limiting data are the difference of the U-values $2.8 - 0.80 = 2.0$ (the difference has the decimals of the less precise number $2.8$, so two figures), the area $14\,\text{m}^2$ and the temperature difference $45\,\text{K}$, all with two figures; the time $7\,\text{days} = 168\,\text{h}$ is exact.
**Reasonableness:** Check the balance: from the old windows $2.8 \cdot 14 \cdot 45\,\text{W} = 1.76\,\text{kW}$ escaped and from the new ones $0.80 \cdot 14 \cdot 45\,\text{W} = 0.50\,\text{kW}$, a difference of $1.26\,\text{kW}$. In a week the old ones would lose $296\,\text{kWh}$ and the new ones $85\,\text{kWh}$. The saving is greatest in frost, when $\Delta T$ is large.

## fy3-12-L2-04
**Given:** $P_\text{in} = 340\,\tfrac{\text{W}}{\text{m}^2}$, $r_1 = 30.0\,\% = 0.300$, $r_2 = 29.0\,\% = 0.290$
**Find:** the increase in the absorbed power per square metre $\Delta P_\text{abs}$ and its comparison with the current imbalance $1.0\,\tfrac{\text{W}}{\text{m}^2}$
**Principle:** The incoming power divides into a reflected and an absorbed part, and only the absorbed part warms the Earth. When the reflected fraction decreases and the power of the Sun stays the same, the absorbed power increases.
**Formula:** $P_\text{abs} = (1 - r)P_\text{in}$, so $\Delta P_\text{abs} = (1 - r_2)P_\text{in} - (1 - r_1)P_\text{in} = (r_1 - r_2)P_\text{in}$
**Conversions:** The percentages are converted to decimal numbers: $30.0\,\% = 0.300$ and $29.0\,\% = 0.290$. The power stays in the unit $\tfrac{\text{W}}{\text{m}^2}$.
**Substitution:** $\Delta P_\text{abs} = (0.300 - 0.290) \cdot 340\,\tfrac{\text{W}}{\text{m}^2} = 0.010 \cdot 340\,\tfrac{\text{W}}{\text{m}^2} = 3.4\,\tfrac{\text{W}}{\text{m}^2}$
**Answer:** $3.4\,\tfrac{\text{W}}{\text{m}^2}$, two significant figures. There are two limiting data: the difference $0.300 - 0.290 = 0.010$ (two figures, because the percentages are given to a tenth of a percent) and the incoming power $340\,\tfrac{\text{W}}{\text{m}^2}$ (at least two figures). If the percentages had been given only as whole numbers, the difference $30 - 29 = 1$ would be a one-figure value. The result is $\dfrac{3.4}{1.0} = 3.4$ times the current imbalance.
**Reasonableness:** A separate calculation: the absorbed power increases from $238\,\tfrac{\text{W}}{\text{m}^2}$ to $241.4\,\tfrac{\text{W}}{\text{m}^2}$, a difference of $3.4\,\tfrac{\text{W}}{\text{m}^2}$. The increase is positive, because reflection decreases. A change of one percentage point is small, but large compared with the imbalance, and the warming melts ice, which increases absorption further.

## fy3-12-L3-01
**Given:** $m = 0.60\,\text{kg}$, $P = 1.4\,\text{W}$, $t = 10.0\,\text{h}$; from the table $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ (coffee like water)
**Find:** the cooling of the coffee $\Delta T$ in kelvins, and an explanation of which ways of heat transfer the vacuum and the shiny surfaces prevent and through which route heat still escapes
**Principle:** The coffee loses only as much heat as escapes from the flask, so energy is conserved: the decrease in the internal energy of the coffee is equal to the escaping energy $Pt$. The coffee only cools and its phase does not change, so use $Q = cm\Delta T$.
**Formula:** $cm\Delta T = Pt$, so $\Delta T = \dfrac{Pt}{cm}$
**Conversions:** The time is converted to seconds, because the power is in watts, that is, joules per second: $t = 10.0 \cdot 3600\,\text{s} = 36\,000\,\text{s}$. The mass is already in kilograms.
**Substitution:** $\Delta T = \dfrac{1.4\,\text{W} \cdot 36\,000\,\text{s}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.60\,\text{kg}} = \dfrac{50\,400\,\text{J}}{2514\,\tfrac{\text{J}}{\text{K}}} \approx 20.05\,\text{K}$
**Answer:** $20\,\text{K}$, two significant figures. The limiting data are the mass $0.60\,\text{kg}$ and the power $1.4\,\text{W}$ (both with two figures); the time $10.0\,\text{h}$ and the specific heat capacity $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ are three-figure values. In a vacuum there are no particles, so heat is neither conducted nor carried by convection from one wall to the other. The shiny surfaces reflect thermal radiation back. Heat escapes mainly by conduction through the neck and the stopper of the flask.
**Reasonableness:** Coffee at $90\,{}^\circ\text{C}$ in the morning is still about $70\,{}^\circ\text{C}$ in the evening, as in a good thermos flask. Balance: the $4190 \cdot 0.60 \cdot 20.05\,\text{J} \approx 50\,400\,\text{J}$ given out by the coffee is equal to the $1.4 \cdot 36\,000\,\text{J}$ that escaped. Units: $\text{W} \cdot \text{s} = \text{J}$ and $\tfrac{\text{J}}{\text{J}/\text{K}} = \text{K}$.

## fy3-12-L3-02
**Given:** $I = 1.0\,\tfrac{\text{W}}{\text{m}^2}$, $A = 5.1 \cdot 10^{14}\,\text{m}^2$, $t_\text{v} = 365\,\text{days}$, share of the oceans $f = 0.90$, $m = 2.6 \cdot 10^{20}\,\text{kg}$, $c = 4.0 \cdot 10^{3}\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, time $10\,\text{years}$
**Find:** the energy accumulating in a year $E_\text{v}$ and the warming of the ocean layer $\Delta T$ in ten years, and an explanation of why a large mass of water slows down the warming
**Principle:** The extra power is constant, so the energy is the power times the time. The seawater only warms and its phase does not change, so the energy stored in it is $Q = cm\Delta T$.
**Formula:** $E_\text{v} = IAt_\text{v}$ and $cm\Delta T = 10fE_\text{v}$, so $\Delta T = \dfrac{10fIAt_\text{v}}{cm}$
**Conversions:** A year in seconds: $t_\text{v} = 365 \cdot 24 \cdot 3600\,\text{s} = 3.1536 \cdot 10^{7}\,\text{s}$. Ten years is the factor $10$ in the formula, and the percentage is $90\,\% = 0.90$.
**Substitution:** $E_\text{v} = 1.0\,\tfrac{\text{W}}{\text{m}^2} \cdot 5.1 \cdot 10^{14}\,\text{m}^2 \cdot 3.1536 \cdot 10^{7}\,\text{s} \approx 1.608 \cdot 10^{22}\,\text{J}$. $\Delta T = \dfrac{10 \cdot 0.90 \cdot 1.608 \cdot 10^{22}\,\text{J}}{4.0 \cdot 10^{3}\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 2.6 \cdot 10^{20}\,\text{kg}} = \dfrac{1.447 \cdot 10^{23}\,\text{J}}{1.04 \cdot 10^{24}\,\tfrac{\text{J}}{\text{K}}} \approx 0.139\,\text{K}$
**Answer:** $E_\text{v} = 1.6 \cdot 10^{22}\,\text{J}$ and $\Delta T = 0.14\,\text{K}$, two significant figures. The limiting data are the power $1.0\,\tfrac{\text{W}}{\text{m}^2}$, the area $5.1 \cdot 10^{14}\,\text{m}^2$, the mass $2.6 \cdot 10^{20}\,\text{kg}$ and the specific heat capacity $4.0 \cdot 10^{3}\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, all with two figures; the calculator result $0.139\,\text{K}$ is rounded. A large mass of water slows down the warming, because a large heat capacity $cm$ needs a lot of energy for a change of one kelvin.
**Reasonableness:** Order of magnitude: $10^{23}\,\text{J}$ divided by $10^{24}\,\tfrac{\text{J}}{\text{K}}$ is about $0.1\,\text{K}$. The heat capacity is $4.0 \cdot 10^{3} \cdot 2.6 \cdot 10^{20}\,\tfrac{\text{J}}{\text{K}} = 1.04 \cdot 10^{24}\,\tfrac{\text{J}}{\text{K}}$. For comparison, the mass of the atmosphere is only about $5 \cdot 10^{18}\,\text{kg}$, and the same energy would warm it by tens of kelvins. The ocean slows down the warming, but the stored energy keeps it going for a long time.

## fy3-12-L3-03
**Given:** coefficient of performance $\varepsilon = 2.8$, $U_1 = 0.35\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $U_2 = 0.10\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $A = 100\,\text{m}^2$, $\Delta T = 19\,\text{K}$, $t = 5800\,\text{h}$
**Find:** the electrical energy $W$ saved by the extra insulation, in kilowatt-hours, and a justification of why insulation is worthwhile with a heat pump
**Principle:** Insulation reduces the heat conducted through the roof, and the heat pump has to deliver less heat indoors. The coefficient of performance tells you that the pump delivers heat $\varepsilon$ times the electrical energy it uses, so the electricity is the heat divided by $\varepsilon$.
**Formula:** $Q = (U_1 - U_2)A\Delta T\,t$ and $W = \dfrac{Q}{\varepsilon}$, so $W = \dfrac{(U_1 - U_2)A\Delta T\,t}{\varepsilon}$
**Conversions:** The time is already in hours and the result is wanted in kilowatt-hours, so the power $\text{W}$ is converted to kilowatts by dividing by a thousand: $\text{Wh} / 1000 = \text{kWh}$.
**Substitution:** $Q = (0.35 - 0.10)\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 100\,\text{m}^2 \cdot 19\,\text{K} \cdot 5800\,\text{h} = 475\,\text{W} \cdot 5800\,\text{h} = 2\,755\,000\,\text{Wh} = 2755\,\text{kWh}$. $W = \dfrac{2755\,\text{kWh}}{2.8} \approx 983.9\,\text{kWh}$
**Answer:** $980\,\text{kWh}$, two significant figures. The limiting data are the coefficient of performance $2.8$, the difference of the U-values $0.35 - 0.10 = 0.25$ and the temperature difference $19\,\text{K}$, all with two figures; the area $100\,\text{m}^2$ and the time $5800\,\text{h}$ are values with at least two figures. The calculator result $983.9\,\text{kWh}$ is rounded. The pump does not create heat but moves it using electricity, and the more heat the house needs, the more electricity is used. That is why insulation is worthwhile: a smaller heating need means a smaller electricity bill.
**Reasonableness:** Back-calculation: $983.9 \cdot 2.8 \approx 2755\,\text{kWh}$. The electricity saving is smaller than the heat saving of $2755\,\text{kWh}$, because the pump delivers $2.8$ kWh of heat from one kilowatt-hour of electricity; in addition to the electricity, heat comes from the outdoor air. With direct electric heating ($\varepsilon = 1$) the saving would be the whole $2755\,\text{kWh}$. In frost the coefficient of performance decreases and the backup resistance heater starts, so the saving is then greatest.

## fy3-12-L1-06
**Find:** how heat is transferred from the campfire to the face when the air between them is cool
**Principle:** Heat is transferred by conduction, by convection or as thermal radiation. Thermal radiation passes through a medium without warming it much, so it can warm a body even when there is cool air in between. Conduction and convection require heat to travel with the medium or through it.
**Model answer:** Heat is transferred mainly as thermal radiation: the hot surface of the campfire emits radiation that passes through the air and is absorbed by the skin. Convection does not explain it, because the air heated by the campfire rises upwards and does not flow horizontally to the face. Conduction through the air does not explain it either, because air is a poor conductor of heat and the air in between stays cool. The face does not touch the hot embers either, so direct conduction by contact is ruled out.

## fy3-12-L1-07
**Find:** which statement about the greenhouse effect is correct
**Principle:** The greenhouse effect arises from the interaction of the gases of the atmosphere with the thermal radiation of the surface. Greenhouse gases absorb the thermal radiation emitted by the surface and radiate part of it back down, which raises the equilibrium temperature of the surface.
**Model answer:** The correct statement is the one saying that greenhouse gases absorb the thermal radiation of the surface and radiate part of it back down, so the surface is warmer. Thanks to the effect, the mean temperature of the surface is about $+15\,{}^\circ\text{C}$ and not about $-18\,{}^\circ\text{C}$. Ozone depletion is a different matter: it increases ultraviolet radiation but hardly warms the Earth. Greenhouse gases do not prevent the radiation of the Sun from reaching the surface. The natural greenhouse effect exists even without human emissions, and the emissions strengthen it.

## fy3-12-L1-08
**Find:** which statement about heat transfer through the wall is correct when it is $21\,{}^\circ\text{C}$ indoors and $-15\,{}^\circ\text{C}$ outdoors
**Principle:** A temperature difference transfers energy, as a net amount, from the warmer body to the colder one. Thermal radiation is emitted by both, however, and the warmer one emits more. The quantity that is transferred is energy, not cold.
**Model answer:** Heat is transferred as a net amount from indoors to outdoors, because the temperature difference transfers energy from the warmer to the colder. Cold does not move anywhere: the inner surface feels cold because heat is transferred from the skin and the room towards the wall. The transfer is not equal in both directions, because then the indoor temperature would stay the same without heating, which is not true in frost. Heat is conducted also through a solid wall, and insulation only reduces the power that passes through it.

## fy3-12-L2-05
**Given:** $m = 0.25\,\text{kg}$, $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, initial temperature $80.0\,{}^\circ\text{C}$; from the table at the time $t = 10\,\text{min}$, $T_\text{A} = 69.0\,{}^\circ\text{C}$ (open) and $T_\text{B} = 73.0\,{}^\circ\text{C}$ (lid)
**Find:** the mean thermal power $P_\text{lid}$, in watts, that the lid prevents from escaping during the first $10\,\text{min}$
**Principle:** The decrease in the internal energy of the water is equal to the heat transferred to the surroundings when the phase does not change: $Q = cm\Delta T$. The cups and the room are alike, so the extra cooling of the open cup is due to the lack of a lid. Power is heat divided by time.
**Formula:** $\Delta T_\text{diff} = T_\text{B} - T_\text{A}$, $Q = cm\Delta T_\text{diff}$ and $P_\text{lid} = \dfrac{Q}{t} = \dfrac{cm\,(T_\text{B} - T_\text{A})}{t}$
**Conversions:** The time is converted to seconds: $10\,\text{min} = 10 \cdot 60\,\text{s} = 600\,\text{s}$. A temperature difference is the same in kelvins and in degrees Celsius.
**Substitution:** $T_\text{B} - T_\text{A} = 73.0\,{}^\circ\text{C} - 69.0\,{}^\circ\text{C} = 4.0\,\text{K}$. $P_\text{lid} = \dfrac{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.25\,\text{kg} \cdot 4.0\,\text{K}}{600\,\text{s}} = \dfrac{4190\,\text{J}}{600\,\text{s}} = 6.98\,\text{W}$
**Answer:** $7.0\,\text{W}$, two significant figures. The limiting datum is the temperature difference $4.0\,\text{K}$, which is a two-figure value.
**Reasonableness:** The open cup gives out $\dfrac{4190 \cdot 0.25 \cdot 11.0}{600}\,\text{W} \approx 19.2\,\text{W}$ and the cup with a lid $\dfrac{4190 \cdot 0.25 \cdot 7.0}{600}\,\text{W} \approx 12.2\,\text{W}$, so the difference is $19.2\,\text{W} - 12.2\,\text{W} = 7.0\,\text{W}$, as calculated. The lid thus removes about a third of the loss. The power is small compared with, for example, the losses of a house, which fits a small cup.
**Model answer b):** The lid prevents above all evaporation: the evaporating water takes the heat of vaporisation with it, and convection carries the vapour and the warm air away from above the cup. The lid stops this flow, so the water in cup B cools more slowly. It still cools, because heat is conducted through the wall of the cup and the lid into the surrounding air and the cup radiates heat, and the lid does not prevent these. According to the table, the temperature of cup B falls from $80.0\,{}^\circ\text{C}$ to $67.4\,{}^\circ\text{C}$ in $20\,\text{min}$.

## fy3-12-L2-06
**Given:** $A = 1.6\,\text{m}^2$, $U = 1.0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $T_\text{in} = 21\,{}^\circ\text{C}$, $T_\text{out} = -15\,{}^\circ\text{C}$; the student's result $\Delta T = 6\,\text{K}$ and $P = 9.6\,\text{W}$
**Find:** the student's error and the correct thermal power $P$ in watts
**Principle:** The power conducted through a window is $P = UA\Delta T$, and $\Delta T$ is the difference between the indoor and the outdoor temperature. When it is frosty outside, the outdoor temperature is negative, and subtracting it increases the difference, because subtracting $-15$ is the same as adding $15$.
**Formula:** $\Delta T = T_\text{in} - T_\text{out}$ and $P = UA\Delta T = UA\,(T_\text{in} - T_\text{out})$
**Conversions:** A temperature difference is the same in degrees Celsius and in kelvins, so no conversions are needed: $\Delta T = 21\,{}^\circ\text{C} - (-15\,{}^\circ\text{C}) = 36\,\text{K}$. The other units are already $\text{m}^2$ and $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$.
**Substitution:** $P = 1.0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 1.6\,\text{m}^2 \cdot 36\,\text{K} = 57.6\,\text{W}$
**Answer:** $58\,\text{W}$, two significant figures. The limiting data are $U = 1.0$, $A = 1.6\,\text{m}^2$ and the difference of whole degrees $\Delta T = 36\,\text{K}$.
**Reasonableness:** The student calculated $21 - 15 = 6$, that is, treated the frost reading of the outdoor temperature as a positive number. The correct difference is $21 + 15 = 36\,\text{K}$. The error can be noticed with rounded numbers: the temperature difference between the room and the frost is about $20 + 15 = 35\,\text{K}$, so the power is about $1.0 \cdot 1.6 \cdot 35 \approx 56\,\text{W}$, not $9.6\,\text{W}$. The student's value is $36 / 6 = 6$ times too small. Back-calculation: $57.6 / (1.0 \cdot 1.6) = 36\,\text{K}$.
**Model answer a):** The student calculated the temperature difference incorrectly: they subtracted $15$ from $21$ instead of subtracting $-15$. With rounded numbers the error can be noticed, because the difference between the room and the frost is clearly over $30\,\text{K}$, so the result $9.6\,\text{W}$ is about six times too small.

## fy3-12-L2-07
**Given:** $A = 0.50\,\text{m}^2$; the points $(\Delta T, P)$ of the table; the line passes approximately through the points $(0\,\text{K};\ 0\,\text{W})$ and $(50.0\,\text{K};\ 8.75\,\text{W})$
**Find:** the U-value $U$ of the panel in the unit $\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$
**Principle:** When the temperatures stay constant, the power conducted through the panel is $P = UA\Delta T$, so $P$ is proportional to the temperature difference $\Delta T$. In the graph $(\Delta T, P)$ the line passes through the origin, because without a temperature difference no heat is transferred ($\Delta T = 0$, so $P = 0$). The slope of the line is $UA$.
**Reading the graph:** In real series of measurements the data points are usually not exactly on the same line because of measurement uncertainty, so individual points deviate from the line because of the variation in the measurements. The line is drawn between the points, and the slope is read from two points of the line, not from two neighbouring data points: $(0\,\text{K};\ 0\,\text{W})$ and $(50.0\,\text{K};\ 8.75\,\text{W})$.
**Formula:** $k = \dfrac{\Delta P}{\Delta(\Delta T)}$, $k = UA$, so $U = \dfrac{k}{A}$
**Conversions:** Not needed: the power is in watts, the temperature difference in kelvins and the area in square metres.
**Substitution:** $k = \dfrac{8.75\,\text{W} - 0\,\text{W}}{50.0\,\text{K} - 0\,\text{K}} = 0.175\,\tfrac{\text{W}}{\text{K}}$. $U = \dfrac{0.175\,\tfrac{\text{W}}{\text{K}}}{0.50\,\text{m}^2} = 0.35\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$
**Answer:** $0.35\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, two significant figures, like the area $0.50\,\text{m}^2$.
**Reasonableness:** Back-calculation: $0.35 \cdot 0.50 \cdot 40.0 = 7.0\,\text{W}$, and the table has the value $6.9\,\text{W}$ at $\Delta T = 40.0\,\text{K}$, so the line passes between the points. The value is larger than that of a modern wall, $0.17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, about double, but much smaller than that of a window, $1.0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, that is, a plausible value for a somewhat older insulated wall panel.
**Model answer b):** The points lie on a line, so the power is proportional to the temperature difference: when the difference doubles, the power doubles, as the formula $P = UA\Delta T$ says. The temperatures had to stay constant, because the formula holds only when both surfaces of the structure are at a uniform temperature and the temperatures do not change during the measurement. Otherwise the panel would store or release energy, and the measured power would not equal $UA\Delta T$.

## fy3-12-L3-04
**Given:** from the table $A_{1980} = 7.5 \cdot 10^{6}\,\text{km}^2$ and $A_{2020} = 3.9 \cdot 10^{6}\,\text{km}^2$; radiation power $I = 90\,\tfrac{\text{W}}{\text{m}^2}$, albedos $a_\text{ice} = 0.60$ and $a_\text{sea} = 0.06$, area of the Earth $A_\text{Earth} = 5.1 \cdot 10^{14}\,\text{m}^2$, energy imbalance $1.0\,\tfrac{\text{W}}{\text{m}^2}$
**Find:** the increase in absorbed power caused by the loss of ice, per area of the Earth, $\Delta P_\text{Earth}$, in the unit $\tfrac{\text{W}}{\text{m}^2}$
**Principle:** A surface absorbs the share $1 - a$ of the incoming radiation, because the albedo $a$ is reflected. When ice is replaced by open sea, the same area absorbs a larger share of the same radiation, so the absorbed power increases. The increase is divided by the area of the Earth so that it can be compared with the energy imbalance.
**Formula:** $\Delta A = A_{1980} - A_{2020}$ and $\Delta P = I\,\Delta A\,\bigl[(1 - a_\text{sea}) - (1 - a_\text{ice})\bigr] = I\,\Delta A\,(a_\text{ice} - a_\text{sea})$, so $\Delta P_\text{Earth} = \dfrac{\Delta P}{A_\text{Earth}}$
**Conversions:** The area is converted to square metres: $1\,\text{km}^2 = 10^{6}\,\text{m}^2$, so $\Delta A = 3.6 \cdot 10^{6}\,\text{km}^2 = 3.6 \cdot 10^{6} \cdot 10^{6}\,\text{m}^2 = 3.6 \cdot 10^{12}\,\text{m}^2$.
**Substitution:** $\Delta A = 7.5 \cdot 10^{6}\,\text{km}^2 - 3.9 \cdot 10^{6}\,\text{km}^2 = 3.6 \cdot 10^{6}\,\text{km}^2$. $\Delta P = 90\,\tfrac{\text{W}}{\text{m}^2} \cdot 3.6 \cdot 10^{12}\,\text{m}^2 \cdot (0.60 - 0.06) = 1.7496 \cdot 10^{14}\,\text{W}$. $\Delta P_\text{Earth} = \dfrac{1.7496 \cdot 10^{14}\,\text{W}}{5.1 \cdot 10^{14}\,\text{m}^2} = 0.343\,\tfrac{\text{W}}{\text{m}^2}$
**Answer:** $0.34\,\tfrac{\text{W}}{\text{m}^2}$, two significant figures, because the radiation power $90\,\tfrac{\text{W}}{\text{m}^2}$ and the difference of the albedos $0.54$ are two-figure values. It is about a third of the energy imbalance $1.0\,\tfrac{\text{W}}{\text{m}^2}$, because $0.34 / 1.0 \approx 0.3$.
**Reasonableness:** The change in the area of ice is $3.6 \cdot 10^{12} / 5.1 \cdot 10^{14} \approx 0.7\,\%$ of the area of the Earth. Over it the absorbed power increases by the factor $0.54$ relative to $90\,\tfrac{\text{W}}{\text{m}^2}$, that is, $0.007 \cdot 90 \cdot 0.54 \approx 0.34\,\tfrac{\text{W}}{\text{m}^2}$, as calculated. If the albedos were the same, the increase would be zero, as it should be. The result is positive, because open sea absorbs more.
**Model answer c):** The feedback is positive because it strengthens the original change: warming melts ice, so reflection decreases and the absorbed power increases, which warms things even more. The model is rough because it uses all the time the same radiation power $90\,\tfrac{\text{W}}{\text{m}^2}$ and fixed albedos. In reality the radiation of the Sun varies strongly with the season, the albedo of ice changes because of melt ponds, and clouds change the absorbed power. The loss of ice cannot continue indefinitely, because there is only a limited amount of ice. The biggest simplification is that the loss of the September minimum is calculated as if the sea were open all year round at the annual mean of $90\,\tfrac{\text{W}}{\text{m}^2}$, so the estimate is an upper limit.

## fy3-12-L3-05
**Given:** $P_\text{abs} = 239\,\tfrac{\text{W}}{\text{m}^2}$, the share absorbed by the atmosphere $f = 0.80$, the remaining $1 - f = 0.20$ goes straight into space; the atmosphere radiates half upwards and half downwards; the points $(T, P)$ of the table
**Find:** the power $S$ radiated by the surface and the temperature $T$ of the surface in degrees Celsius
**Principle:** In energy balance the incoming and outgoing powers are equal. At the top of the atmosphere the power leaving into space must be $239\,\tfrac{\text{W}}{\text{m}^2}$, because the power absorbed from the Sun is the same. In addition to the Sun, the surface receives the power radiated downwards by the atmosphere, and the greenhouse effect raises the temperature.
**Formula:** At the top $239\,\tfrac{\text{W}}{\text{m}^2} = (1 - f)\,S + \tfrac{fS}{2}$, so $S = \dfrac{239\,\text{W/m}^2}{1 - f/2}$. Check at the surface: $S = 239\,\tfrac{\text{W}}{\text{m}^2} + \tfrac{fS}{2}$. The temperature is interpolated between the points $(T_1, P_1)$ and $(T_2, P_2)$ of the table: $T = T_1 + \dfrac{S - P_1}{P_2 - P_1}\,(T_2 - T_1)$
**Conversions:** A temperature in kelvins is converted to degrees Celsius by subtracting $273.15$: $T_\text{C} = T - 273.15\,\text{K}$.
**Substitution:** $S = \dfrac{239\,\tfrac{\text{W}}{\text{m}^2}}{1 - 0.40} = 398.3\,\tfrac{\text{W}}{\text{m}^2}$. Check: $239 + 0.40 \cdot 398.3 = 398.3\,\tfrac{\text{W}}{\text{m}^2}$. The value $398.3$ is between the points $288\,\text{K}$ ($390$) and $303\,\text{K}$ ($478$) of the table: $T = 288\,\text{K} + \dfrac{398.3 - 390}{478 - 390} \cdot 15\,\text{K} = 289.4\,\text{K}$. $T_\text{C} = 289.4\,\text{K} - 273.15\,\text{K} = 16.3\,{}^\circ\text{C}$
**Answer:** $16\,{}^\circ\text{C}$ (calculated $16.3\,{}^\circ\text{C}$), two significant figures, because linear interpolation on a curved table limits the result to an accuracy of about $\pm 0.5\,\text{K}$.
**Reasonableness:** A temperature of $16\,{}^\circ\text{C}$ is close to the real mean temperature of the Earth, about $+15\,{}^\circ\text{C}$. The power $398.3\,\tfrac{\text{W}}{\text{m}^2}$ is larger than $239\,\tfrac{\text{W}}{\text{m}^2}$, as it should be, because the surface receives extra energy from the atmosphere. The limiting case $f = 0$ gives $S = 239\,\tfrac{\text{W}}{\text{m}^2}$, which corresponds in the table to about $255\,\text{K}$.
**Model answer c):** Without the atmosphere the surface would radiate only the power it absorbs, $239\,\tfrac{\text{W}}{\text{m}^2}$, which corresponds in the table to $255\,\text{K}$, that is, $255 - 273.15 \approx -18\,{}^\circ\text{C}$. With the atmosphere the model gives a temperature of $16.3\,{}^\circ\text{C}$, about $34\,\text{K}$ warmer, so the greenhouse effect raises the surface temperature by this much. The model is still rough: the real atmosphere absorbs the radiation of the Sun, the share $0.80$ varies with wavelength, and clouds, convection and the evaporation of water transfer energy upwards from the surface in other ways than by radiation.

## fy3-12-L2-08
**Find:** the thermal powers $P$ conducted through the building parts and their order from smallest to largest.
**Principle:** When the temperatures on both sides of a building part stay constant, the thermal power conducted through it is $P = UA\Delta T$. The temperature difference is the same $30\,\text{K}$ for all parts, but the U-value and the area vary, so the order becomes clear only when both are taken into account.
**Model answer:** First calculate $UA$ of each part and then the power:

Door: $UA = 2.0\,\text{W/K}$, $P = 2.0\,\text{W/K} \cdot 30\,\text{K} = 60\,\text{W}$

Roof: $UA = 7.2\,\text{W/K}$, $P = 7.2\,\text{W/K} \cdot 30\,\text{K} = 216\,\text{W}$

Windows: $UA = 9.6\,\text{W/K}$, $P = 9.6\,\text{W/K} \cdot 30\,\text{K} = 288\,\text{W}$

Wall: $UA = 15.3\,\text{W/K}$, $P = 15.3\,\text{W/K} \cdot 30\,\text{K} = 459\,\text{W}$

From smallest to largest: door, roof, windows, wall. The U-value alone would give the wrong order, because the windows and the door have a large U-value but a small area, and the area alone would also give it wrong, because the wall has a small U-value but a large area. The results are given with two significant figures, because the U-values are given with two: about $60\,\text{W}$, $220\,\text{W}$, $290\,\text{W}$ and $460\,\text{W}$. Estimate: the wall's $UA \approx 0.2 \cdot 90 = 18\,\text{W/K}$ is the largest and the door's $2\,\text{W/K}$ the smallest, which fits.

## fy3-12-L1-09
**Given:** $A = 10\,\text{m}^2$, $d = 0.20\,\text{m}$, $T_\text{in} = 20\,{}^\circ\text{C}$, $T_\text{out} = -10\,{}^\circ\text{C}$, $U = \dfrac{\lambda}{d}$; from the table (MAFY table, thermal conductivities: solids, wood (pine)) $\lambda = 0.14\,\tfrac{\text{W}}{\text{m}\cdot\text{K}}$
**Find:** the thermal power $P$ conducted through the wall, in watts
**Principle:** Heat is conducted from warm to cold, and the power is directly proportional to the area and the temperature difference. The U-value describes the conduction through the wall by the formula $U = \lambda / d$ given in the task.
**Formula:** $P = UA\,\Delta T$ and $U = \dfrac{\lambda}{d}$, so $P = \dfrac{\lambda}{d}\,A\,\Delta T$
**Conversions:** The temperature difference is the same in degrees Celsius and in kelvins: $\Delta T = 20\,{}^\circ\text{C} - (-10\,{}^\circ\text{C}) = 30\,\text{K}$. No other conversions are needed.
**Substitution:** $U = \dfrac{0.14\,\tfrac{\text{W}}{\text{m}\cdot\text{K}}}{0.20\,\text{m}} = 0.70\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$ and $P = 0.70\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}} \cdot 10\,\text{m}^2 \cdot 30\,\text{K} = 210\,\text{W}$
**Answer:** $P \approx 210\,\text{W}$, two significant figures, as in $\lambda = 0.14$. The thermal conductivity is from the MAFY table (thermal conductivities: solids); the answer is accepted within about $\pm 4\,\%$.
**Reasonableness:** The U-value $0.70\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$ is about four times the U-value $0.17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$ of a modern wall, which fits the weaker insulation of a log wall. The power through $10\,\text{m}^2$ is small because the area is small: $0.7 \cdot 10 \cdot 30 = 210\,\text{W}$.

## fy3-12-L2-09
**Given:** read from the figure, $P_\text{refl} = 102\,\tfrac{\text{W}}{\text{m}^2}$ is reflected; $A = 5.1 \cdot 10^{14}\,\text{m}^2$
**Find:** the total power $P$ of the reflected radiation over the whole Earth, in petawatts
**Principle:** The power in the figure is given per square metre, so the total power is found by multiplying it by the area. The power is a uniform average.
**Reading the graph:** The arrow between the Sun and the Earth that points up and to the left gives the reflected power $102\,\tfrac{\text{W}}{\text{m}^2}$. The other arrows are not needed.
**Formula:** $P = P_\text{refl}\,A$
**Conversions:** $1\,\text{PW} = 10^{15}\,\text{W}$, so the value in watts is divided by $10^{15}$.
**Substitution:** $P = 102\,\tfrac{\text{W}}{\text{m}^2} \cdot 5.1 \cdot 10^{14}\,\text{m}^2 = 5.202 \cdot 10^{16}\,\text{W} = \dfrac{5.202 \cdot 10^{16}\,\text{W}}{10^{15}\,\text{W/PW}} = 52.02\,\text{PW}$
**Answer:** $P \approx 52\,\text{PW}$, two significant figures, as in the area $5.1 \cdot 10^{14}\,\text{m}^2$.
**Reasonableness:** Order of magnitude: $100 \cdot 5 \cdot 10^{14}\,\text{W} = 5 \cdot 10^{16}\,\text{W}$, which is $50\,\text{PW}$, so it agrees. Back-calculation: $\dfrac{5.2 \cdot 10^{16}\,\text{W}}{5.1 \cdot 10^{14}\,\text{m}^2} \approx 102\,\tfrac{\text{W}}{\text{m}^2}$.
