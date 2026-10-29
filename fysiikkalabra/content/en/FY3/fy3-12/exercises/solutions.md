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
**Reading the graph:** The left arrow of the figure gives the incoming power $P_\text{in} = 341\,\tfrac{\text{W}}{\text{m}^2}$ and the upper right arrow the reflected power $P_\text{refl} = 102\,\tfrac{\text{W}}{\text{m}^2}$. The lower right arrow, whose value is a question mark, is the thermal radiation asked for.
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
