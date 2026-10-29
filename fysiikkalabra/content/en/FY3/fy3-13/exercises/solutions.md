## fy3-13-L1-01
**Given:** the line $p = p_0 + k\theta$, where $p_0 = 98.0\,\text{kPa}$ and $k = 0.360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Find:** the temperature $\theta_0$ in degrees Celsius at which the line gives the pressure $p = 0$
**Principle:** The container is closed and rigid, so the amount and volume of the gas stay constant and the pressure depends linearly on temperature. So the equation of the line describes the gas within the measurement range, and the line can be extended (extrapolated) beyond it: the point of zero pressure is found by setting $p = 0$ in the equation.
**Formula:** $p = p_0 + k\theta$. When $p = 0$ and $\theta = \theta_0$, then $0 = p_0 + k\theta_0$, so $\theta_0 = -\dfrac{p_0}{k}$
**Conversions:** No conversions are needed: $p_0$ and $k$ are in kilopascals, so the kPa cancels and the result is in degrees Celsius, as asked.
**Substitution:** $\theta_0 = -\dfrac{98.0\,\text{kPa}}{0.360\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -272.22\,{}^\circ\text{C}$
**Answer:** $-272\,{}^\circ\text{C}$, three significant figures, like the values $98.0\,\text{kPa}$ and $0.360$.
**Reasonableness:** The pressure drops by $0.360\,\text{kPa}$ for every degree, so $98\,\text{kPa}$ runs out after about $98/0.36 \approx 270$ degrees, which is close to the result. The result is also close to absolute zero, $-273.15\,{}^\circ\text{C}$. Check: $p = 98.0\,\text{kPa} + 0.360\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-272.22\,{}^\circ\text{C}) = 0\,\text{kPa}$.

## fy3-13-L1-02
**Given:** two points on the line: $(\theta_1, p_1) = (20.0\,{}^\circ\text{C};\ 105.0\,\text{kPa})$ and $(\theta_2, p_2) = (80.0\,{}^\circ\text{C};\ 127.0\,\text{kPa})$
**Find:** the slope $k$ of the line in the unit $\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Principle:** In a closed rigid container, the pressure of a dilute gas is a linear function of temperature within the measurement range, so the slope of the line is the same everywhere: it tells you how many kilopascals the pressure rises per degree Celsius. So you can calculate it from any two points on the line.
**Formula:** $k = \dfrac{\Delta p}{\Delta\theta}$, where $\Delta p = p_2 - p_1$ and $\Delta\theta = \theta_2 - \theta_1$, so $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$
**Conversions:** No units are converted, because the slope is asked for in the unit $\text{kPa}/{}^\circ\text{C}$. The temperature difference is $\Delta\theta = 80.0\,{}^\circ\text{C} - 20.0\,{}^\circ\text{C} = 60.0\,{}^\circ\text{C}$, and it is the same in kelvins.
**Substitution:** $k = \dfrac{(127.0 - 105.0)\,\text{kPa}}{(80.0 - 20.0)\,{}^\circ\text{C}} = \dfrac{22.0\,\text{kPa}}{60.0\,{}^\circ\text{C}} = 0.36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$
**Answer:** $0.367\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, three significant figures, because both differences, the pressure change $22.0\,\text{kPa}$ and the temperature difference $60.0\,{}^\circ\text{C}$, are known to three figures.
**Reasonableness:** The slope is positive because the pressure increases as the temperature rises. Check: $105.0\,\text{kPa} + 0.36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 60.0\,{}^\circ\text{C} = 127.0\,\text{kPa}$. The value is of the same order of magnitude as in the other experiments in this chapter ($0.36\ldots 0.39\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$).

## fy3-13-L1-03
**Given:** the group's result $\theta_0 = -267.90\,{}^\circ\text{C}$ and the accepted value $\theta_\text{acc} = -273.15\,{}^\circ\text{C}$
**Find:** the deviation $d$ in degrees Celsius
**Principle:** The error of a measurement is the difference between the result and the accepted value, and its sign tells the direction. The deviation asked for here is the magnitude of this difference, that is, the distance, which is positive whether the result is above or below the accepted value, so you take the absolute value of the difference.
**Formula:** $d = |\theta_0 - \theta_\text{acc}|$
**Conversions:** Both values are in degrees Celsius on the same scale. The difference of temperatures is the same in degrees Celsius and in kelvins, so no conversions are needed.
**Substitution:** $d = |-267.90\,{}^\circ\text{C} - (-273.15\,{}^\circ\text{C})| = |5.25\,{}^\circ\text{C}| = 5.25\,{}^\circ\text{C}$
**Answer:** $5.25\,{}^\circ\text{C}$, three significant figures, because both temperatures, $-267.90\,{}^\circ\text{C}$ and $-273.15\,{}^\circ\text{C}$, are given to the hundredth, and the difference has as many decimals as the least precise number.
**Reasonableness:** The group's result is less negative than the accepted value, so the difference is positive and the result is slightly too warm. Check: $-273.15\,{}^\circ\text{C} + 5.25\,{}^\circ\text{C} = -267.90\,{}^\circ\text{C}$. The deviation is only about $5.25/273 \approx 2\,\%$ of the whole extrapolation distance, so the result is good.

## fy3-13-L1-04
**Given:** the temperature at zero pressure of the steeper limit line $\theta_{0,\text{max}} = -258\,{}^\circ\text{C}$ and of the shallower one $\theta_{0,\text{min}} = -284\,{}^\circ\text{C}$
**Find:** the uncertainty of the result $\Delta\theta_0$ in degrees Celsius
**Principle:** All the lines that pass through all the uncertainty bars fit the data equally well. The steepest and the shallowest of them bound the interval where the true absolute zero probably lies. The result is written in the form $\theta_0 \pm \Delta\theta_0$, so the uncertainty is half of the interval.
**Formula:** $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Conversions:** Both temperatures are in degrees Celsius, and their difference is the same in kelvins, so no conversions are needed.
**Substitution:** $\Delta\theta_0 = \dfrac{-258\,{}^\circ\text{C} - (-284\,{}^\circ\text{C})}{2} = \dfrac{26\,{}^\circ\text{C}}{2} = 13\,{}^\circ\text{C}$
**Answer:** $13\,{}^\circ\text{C}$, two significant figures, because the difference of the limit values, $26\,{}^\circ\text{C}$, is given in whole degrees, that is, to two figures; the divisor $2$ is an exact number and does not limit the precision.
**Reasonableness:** The midpoint of the interval is $\dfrac{-258 + (-284)}{2}\,{}^\circ\text{C} = -271\,{}^\circ\text{C}$, and $13\,{}^\circ\text{C}$ in each direction from it reaches exactly the limit values $-258\,{}^\circ\text{C}$ and $-284\,{}^\circ\text{C}$. The accepted value $-273.15\,{}^\circ\text{C}$ lies in the interval, so the result agrees with it.

## fy3-13-L1-05
**Given:** the pressure gauge reading $p = 112\,\text{kPa}$ and the estimated uncertainty of the pressure reading $\Delta p = 1.0\,\text{kPa}$
**Find:** the relative uncertainty $\varepsilon$ as a percentage of the reading
**Principle:** What an uncertainty means depends on how large it is compared with the measured value. The relative uncertainty is the quotient of the uncertainty and the reading, and multiplying it by $100\,\%$ gives the percentage.
**Formula:** $\varepsilon = \dfrac{\Delta p}{p} \cdot 100\,\%$
**Conversions:** Both pressures are in kilopascals, so the unit cancels and no conversions are needed. The quotient is a ratio, and multiplying by $100\,\%$ turns it into a percentage.
**Substitution:** $\varepsilon = \dfrac{1.0\,\text{kPa}}{112\,\text{kPa}} \cdot 100\,\% = 0.8929\,\%$
**Answer:** $0.89\,\%$, two significant figures, because the uncertainty $1.0\,\text{kPa}$ is given to two figures (the reading $112\,\text{kPa}$ has three and limits less).
**Reasonableness:** As an estimate, $\dfrac{1}{112} \approx \dfrac{1}{100} = 1\,\%$, and since 112 is slightly more than a hundred, the result is slightly less than one percent. If the reading were only $1\,\text{kPa}$, the uncertainty would be $100\,\%$, so a large reading makes the relative uncertainty smaller. In extrapolation, though, even this small uncertainty grows many times larger.

## fy3-13-L2-01
**Given:** two measurement points $(\theta_1, p_1) = (15.0\,{}^\circ\text{C};\ 1.050\,\text{bar})$ and $(\theta_2, p_2) = (95.0\,{}^\circ\text{C};\ 1.360\,\text{bar})$; the pressure depends linearly on temperature
**Find:** the temperature $\theta_0$ in degrees Celsius at which the line gives zero pressure
**Principle:** The flask is sealed, so the amount and volume of the air stay constant and the pressure is a linear function of temperature. Two points determine the line, and it is extended by extrapolation to the point where $p = 0$.
**Formula:** The slope is $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$. The line through point 1 is $p = p_1 + k(\theta - \theta_1)$, and $p = 0$ gives $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Conversions:** Both pressures are in bar. In the quotient $p_1/k$ the unit bar cancels, so there is no need to convert to pascals. The temperature difference $95.0\,{}^\circ\text{C} - 15.0\,{}^\circ\text{C} = 80.0\,{}^\circ\text{C}$ is the same in kelvins.
**Substitution:** $k = \dfrac{(1.360 - 1.050)\,\text{bar}}{(95.0 - 15.0)\,{}^\circ\text{C}} = \dfrac{0.310\,\text{bar}}{80.0\,{}^\circ\text{C}} = 0.003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}$ and $\theta_0 = 15.0\,{}^\circ\text{C} - \dfrac{1.050\,\text{bar}}{0.003875\,\tfrac{\text{bar}}{{}^\circ\text{C}}} = 15.0\,{}^\circ\text{C} - 270.97\,{}^\circ\text{C} = -255.97\,{}^\circ\text{C}$
**Answer:** $-256\,{}^\circ\text{C}$, three significant figures, because the pressure difference $0.310\,\text{bar}$ and the temperature difference $80.0\,{}^\circ\text{C}$ are known to three figures; finally the subtraction $15.0 - 271$ gives the result in whole degrees.
**Reasonableness:** The pressure rises by about $0.310\,\text{bar}$ in eighty degrees, so one bar corresponds to about $270\,{}^\circ\text{C}$. A second check with kelvins: the ratio $p_1/p_2 = 1.050/1.360 = 0.772$ is close to the ratio $T_1/T_2 = 288.15/368.15 = 0.783$. So the result is close to $-273.15\,{}^\circ\text{C}$, and the difference comes from the measurement error of the two points, which grows in a long extrapolation.

## fy3-13-L2-02
**Given:** two limit lines $p = 100\,\text{kPa} + 0.380\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (steeper) and $p = 102\,\text{kPa} + 0.350\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot \theta$ (shallower)
**Find:** the uncertainty $\Delta\theta_0$ in degrees Celsius
**Principle:** Both lines pass through the uncertainty bars of all the measurement points, so the true line probably lies between them. The temperatures at zero pressure of the limit lines bound the estimated interval for the zero point, and the uncertainty is half of this interval.
**Formula:** The zero pressure of each line follows from the condition $0 = p_0 + k\theta_0$, that is, $\theta_0 = -\dfrac{p_0}{k}$. The steeper line gives the value $\theta_{0,\text{max}}$ and the shallower one the value $\theta_{0,\text{min}}$, and $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Conversions:** No conversions are needed: $p_0$ is in kilopascals and $k$ in the unit $\text{kPa}/{}^\circ\text{C}$, so the quotient is in degrees Celsius.
**Substitution:** $\theta_{0,\text{max}} = -\dfrac{100\,\text{kPa}}{0.380\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -263.16\,{}^\circ\text{C}$ and $\theta_{0,\text{min}} = -\dfrac{102\,\text{kPa}}{0.350\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -291.43\,{}^\circ\text{C}$. So $\Delta\theta_0 = \dfrac{-263.16\,{}^\circ\text{C} - (-291.43\,{}^\circ\text{C})}{2} = 14.14\,{}^\circ\text{C}$
**Answer:** $14\,{}^\circ\text{C}$, two significant figures, because the zero points $-263\,{}^\circ\text{C}$ and $-291\,{}^\circ\text{C}$ are known to three figures, that is, in whole degrees, and their difference $28\,{}^\circ\text{C}$ is only a two-figure number; the divisor $2$ is exact.
**Reasonableness:** The interval is $-277 \pm 14\,{}^\circ\text{C}$, since the midpoint is $\dfrac{-263.16 + (-291.43)}{2} = -277.3\,{}^\circ\text{C}$. The accepted value $-273.15\,{}^\circ\text{C}$ lies in the interval, so the result is consistent. The order of magnitude is the same as in the worked example of the chapter ($18\,{}^\circ\text{C}$), when the points and the uncertainty of the pressure reading are similar.

## fy3-13-L2-03
**Given:** atmospheric pressure $p_\text{air} = 101.0\,\text{kPa}$; the gauge pressure from the gauge $p_\text{g,1} = 9.0\,\text{kPa}$ at the temperature $\theta_1 = 30.0\,{}^\circ\text{C}$ and $p_\text{g,2} = 31.0\,\text{kPa}$ at the temperature $\theta_2 = 90.0\,{}^\circ\text{C}$
**Find:** the temperature $\theta_0$ in degrees Celsius at which the absolute pressure of the gas is zero
**Principle:** The pressure of a gas means the absolute pressure, and only that is linear with respect to temperature in such a way that the zero of the line predicts a vacuum. The gauge shows the gauge pressure compared with atmospheric pressure, so you must add the atmospheric pressure before fitting the line.
**Formula:** $p = p_\text{g} + p_\text{air}$. Then $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ and for zero pressure $0 = p_1 + k(\theta_0 - \theta_1)$, so $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Conversions:** The gauge pressures are converted to absolute pressures: $p_1 = 9.0\,\text{kPa} + 101.0\,\text{kPa} = 110.0\,\text{kPa}$ and $p_2 = 31.0\,\text{kPa} + 101.0\,\text{kPa} = 132.0\,\text{kPa}$. The units are already kilopascals and degrees Celsius.
**Substitution:** $k = \dfrac{(132.0 - 110.0)\,\text{kPa}}{(90.0 - 30.0)\,{}^\circ\text{C}} = \dfrac{22.0\,\text{kPa}}{60.0\,{}^\circ\text{C}} = 0.36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ and $\theta_0 = 30.0\,{}^\circ\text{C} - \dfrac{110.0\,\text{kPa}}{0.36667\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = 30.0\,{}^\circ\text{C} - 300\,{}^\circ\text{C} = -270\,{}^\circ\text{C}$
**Answer:** $-270\,{}^\circ\text{C}$, three significant figures, because the pressure difference $22.0\,\text{kPa}$ and the temperature difference $60.0\,{}^\circ\text{C}$ are known to three figures; finally the subtraction $30.0 - 300$ gives the result in whole degrees.
**Reasonableness:** The result is close to $-273.15\,{}^\circ\text{C}$, as it should be. If the atmospheric pressure were not added, the line of the gauge pressure would reach zero already at $30.0 - 9.0/0.36667 = 5.5\,{}^\circ\text{C}$, which is impossible, because a gas at room temperature is nowhere near a vacuum.

## fy3-13-L2-04
**Given:** the reading precision of the temperature $\Delta\theta = 0.50\,{}^\circ\text{C}$, the slope of the line $k = 0.36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ and the uncertainty of the pressure $\Delta p = 1.0\,\text{kPa}$
**Find:** the change in pressure $\Delta p_\theta$ corresponding to the temperature uncertainty, as a percentage of the uncertainty $\Delta p$
**Principle:** The measurement points lie on the line $p = p_0 + k\theta$, so an error $\Delta\theta$ in temperature moves the point horizontally, and at the line it corresponds to a vertical deviation $k\,\Delta\theta$. Once it is converted to a pressure, you can compare it directly with the uncertainty of the pressure reading.
**Formula:** $\Delta p_\theta = k\,\Delta\theta$ and the proportion $s = \dfrac{\Delta p_\theta}{\Delta p} \cdot 100\,\%$
**Conversions:** No conversions are needed: the degrees Celsius cancel in the product $k\,\Delta\theta$, and the kilopascals cancel in the quotient. Multiplying by $100\,\%$ turns the ratio into a percentage.
**Substitution:** $\Delta p_\theta = 0.36\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 0.50\,{}^\circ\text{C} = 0.18\,\text{kPa}$ and $s = \dfrac{0.18\,\text{kPa}}{1.0\,\text{kPa}} \cdot 100\,\% = 18\,\%$
**Answer:** $18\,\%$, two significant figures, because the slope $0.36\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ is given to two figures; the uncertainties $0.50\,{}^\circ\text{C}$ and $1.0\,\text{kPa}$ also have two figures.
**Reasonableness:** The temperature error corresponds to only about a fifth of the uncertainty of the pressure reading, so the precision of the result is limited by the pressure gauge, not by the thermometer. Limiting case: the proportion would be $100\,\%$ if the temperature error were $1.0/0.36 = 2.8\,{}^\circ\text{C}$, so the thermometer would have to be much less precise than it is now.

## fy3-13-L3-01
**Given:** the end points $106.0 \pm 1.0\,\text{kPa}$ at the temperature $20.0\,{}^\circ\text{C}$ and $137.0 \pm 1.0\,\text{kPa}$ at the temperature $100.0\,{}^\circ\text{C}$. The steepest limit line passes through the points $(20.0\,{}^\circ\text{C};\ 105.0\,\text{kPa})$ and $(100.0\,{}^\circ\text{C};\ 138.0\,\text{kPa})$, the shallowest through the points $(20.0\,{}^\circ\text{C};\ 107.0\,\text{kPa})$ and $(100.0\,{}^\circ\text{C};\ 136.0\,\text{kPa})$
**Find:** the uncertainty $\Delta\theta_0$ in degrees Celsius and the reason why the result is larger than with the seven-point data
**Principle:** The steeper or shallower a line you allow, the wider the interval of zero points. The zero-pressure point of each limit line is calculated from two points of the line, and the uncertainty is half of the interval between these two values.
**Formula:** For each line $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ and $\theta_0 = \theta_1 - \dfrac{p_1}{k}$, and then $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Conversions:** No conversions are needed: the pressures are in kilopascals and the temperatures in degrees Celsius, and the temperature difference $100.0\,{}^\circ\text{C} - 20.0\,{}^\circ\text{C} = 80.0\,{}^\circ\text{C}$ is the same in kelvins.
**Substitution:** Steepest: $k = \dfrac{(138.0 - 105.0)\,\text{kPa}}{80.0\,{}^\circ\text{C}} = 0.4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ and $\theta_0 = 20.0\,{}^\circ\text{C} - \dfrac{105.0\,\text{kPa}}{0.4125\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -234.55\,{}^\circ\text{C}$. Shallowest: $k = \dfrac{(136.0 - 107.0)\,\text{kPa}}{80.0\,{}^\circ\text{C}} = 0.3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ and $\theta_0 = 20.0\,{}^\circ\text{C} - \dfrac{107.0\,\text{kPa}}{0.3625\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} = -275.17\,{}^\circ\text{C}$. So $\Delta\theta_0 = \dfrac{-234.55 - (-275.17)}{2}\,{}^\circ\text{C} = 20.31\,{}^\circ\text{C}$
**Answer:** $20\,{}^\circ\text{C}$ (exactly $20.3\,{}^\circ\text{C}$), two significant figures, because the zero points $-235\,{}^\circ\text{C}$ and $-275\,{}^\circ\text{C}$ are known to three figures, that is, in whole degrees, and their difference $40\,{}^\circ\text{C}$ is a two-figure number. A third figure would require initial values to the hundredth, which does not fit the uncertainty $\pm 1.0\,\text{kPa}$.
**Reasonableness:** The interval $-275.2\ldots -234.5\,{}^\circ\text{C}$ contains the accepted value $-273.15\,{}^\circ\text{C}$. The result is larger than the $18\,{}^\circ\text{C}$ of the seven-point data, as it should be: a line through two points has no other constraints, so the steepest line may rise at one end and fall at the other to the edge of an uncertainty bar. In the seven-point data every line must also pass through the bars of the five intermediate points, which narrows the range of allowed slopes.

## fy3-13-L3-02
**Given:** $p_0 = 100.0\,\text{kPa}$ at the temperature $0\,{}^\circ\text{C}$, the target temperature $T = 77.0\,\text{K}$ and $p \propto T$ in kelvins; at this pressure nitrogen condenses into a liquid only at about $67\,\text{K}$
**Find:** the pressure $p$ at the temperature $77.0\,\text{K}$ in kilopascals, and a justification of why the line cannot be extended all the way to zero
**Principle:** In a rigid closed container, the amount and volume of the gas stay constant, so the pressure is directly proportional to the temperature in kelvins and $\dfrac{p}{T}$ is constant. The proportionality holds only in kelvins, because only the zero of the kelvin scale is absolute zero. It also requires that the gas stays a gas.
**Formula:** $\dfrac{p}{T} = \dfrac{p_0}{T_0}$, so $p = p_0\,\dfrac{T}{T_0}$
**Conversions:** The initial temperature is converted to kelvins: $T_0 = 0\,{}^\circ\text{C} = 273.15\,\text{K}$. The temperature $77.0\,\text{K}$ is already in kelvins. In the ratio $T/T_0$ the kelvins cancel, so the pressure stays in kilopascals.
**Substitution:** $p = 100.0\,\text{kPa} \cdot \dfrac{77.0\,\text{K}}{273.15\,\text{K}} = 28.19\,\text{kPa}$
**Answer:** $28.2\,\text{kPa}$, three significant figures, because the temperature $77.0\,\text{K}$ is given to three figures ($273.15\,\text{K}$ is a definition and does not limit). The line cannot be extended all the way to zero, because nitrogen condenses into a liquid at about $67\,\text{K}$. Then the amount of gas decreases, the pressure falls faster than the line predicts, and the condition "amount of substance constant" no longer holds.
**Reasonableness:** The temperature $77.0\,\text{K}$ is about $0.28$ times the temperature $273.15\,\text{K}$, and the pressure is in the same proportion: about $0.28 \cdot 100 = 28\,\text{kPa}$. At the temperature $67\,\text{K}$ the line would give a pressure of $100 \cdot 67/273.15 = 24.5\,\text{kPa}$, but at about that temperature the gas starts to condense into a liquid, and after that the pressure no longer follows the line. So extrapolation is reliable only as far as the assumption of a gas holds true.

## fy3-13-L3-03
**Given:** group A's result $\theta_0 = -262.00\,{}^\circ\text{C}$ and uncertainty $\Delta\theta_0 = 6.00\,{}^\circ\text{C}$; the accepted value $\theta_\text{acc} = -273.15\,{}^\circ\text{C}$
**Find:** the ratio $n$ of the deviation to the uncertainty (how many times $\Delta\theta_0$ fits between the result and the accepted value) and the reason for the disagreement
**Principle:** In this chapter a result is considered consistent with the accepted value if the value lies in the uncertainty interval $\theta_0 \pm \Delta\theta_0$, that is, when the deviation is at most one uncertainty. The ratio $n$ tells you how many times larger the deviation is than the uncertainty. The uncertainty is not an absolute limit, so a deviation alone does not prove an error, but the larger $n$ is, the more likely it is that the measurement has a systematic error or that the uncertainty was estimated too small.
**Formula:** $n = \dfrac{|\theta_0 - \theta_\text{acc}|}{\Delta\theta_0}$
**Conversions:** All temperatures are in degrees Celsius, and temperature differences are the same in kelvins. The ratio $n$ is dimensionless, so no conversions are needed.
**Substitution:** $n = \dfrac{|-262.00\,{}^\circ\text{C} - (-273.15\,{}^\circ\text{C})|}{6.00\,{}^\circ\text{C}} = \dfrac{11.15\,{}^\circ\text{C}}{6.00\,{}^\circ\text{C}} = 1.858$
**Answer:** $1.86$ times, three significant figures, because the difference $11.15\,{}^\circ\text{C}$ and the uncertainty $6.00\,{}^\circ\text{C}$ are given to three figures (the result $-262.00\,{}^\circ\text{C}$ and the accepted value are given to the hundredth).
**Reasonableness:** The deviation $11.15\,{}^\circ\text{C}$ is almost two uncertainties ($2 \cdot 6.00 = 12.0$). The uncertainty interval $-268\ldots -256\,{}^\circ\text{C}$ does not contain the accepted value $-273.15\,{}^\circ\text{C}$, so by this rule the result is not consistent with it. The cause may be a systematic error, for example an imprecise thermometer, an air leak or a change in the volume of the flask, or an uncertainty that was estimated too small. Check: $1.858 \cdot 6.00\,{}^\circ\text{C} = 11.15\,{}^\circ\text{C}$.
