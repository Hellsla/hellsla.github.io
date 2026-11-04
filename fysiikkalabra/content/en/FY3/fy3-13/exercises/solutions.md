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

## fy3-13-L1-06
**Find:** what the temperature $0\,\text{K}$, that is, absolute zero, means.
**Principle:** Temperature describes the average kinetic energy of the particles. The kelvin scale starts from the temperature below which there is nothing lower, because the energy of the particles is at its smallest there.
**Model answer:** Absolute zero is the lowest possible temperature, $0\,\text{K} = -273.15\,{}^\circ\text{C}$, at which the average kinetic energy of the particles is at its smallest. It is not the freezing point of water ($273.15\,\text{K}$), and it should not be understood to mean that the particles stop: it is a matter of the smallest possible energy, and the more precise picture belongs to a later course. Nor do all gases condense exactly there: the condensation temperature depends on the substance.

## fy3-13-L1-07
**Given:** the boiling point of nitrogen $\theta = -195.8\,{}^\circ\text{C}$
**Find:** the same temperature in kelvins, $T$
**Principle:** The size of a degree is the same on the Celsius and kelvin scales, but the zero points differ: the zero of the kelvin scale is absolute zero. So the conversion is only a shift.
**Formula:** $T = \theta + 273.15$
**Conversions:** The temperature $0\,{}^\circ\text{C}$ is $273.15\,\text{K}$, so $273.15$ is added to the Celsius value and the unit becomes kelvin.
**Substitution:** $T = (-195.8 + 273.15)\,\text{K} = 77.35\,\text{K} \approx 77.4\,\text{K}$
**Answer:** $77.4\,\text{K}$, to the tenth, like $-195.8\,{}^\circ\text{C}$; the exact $273.15$ does not limit.
**Reasonableness:** The result is positive, as a kelvin temperature should be, and clearly below the freezing point of water, $273.15\,\text{K}$. Check back: $77.4\,\text{K} - 273.15\,\text{K} = -195.75\,{}^\circ\text{C} \approx -195.8\,{}^\circ\text{C}$.

## fy3-13-L1-08
**Find:** what extrapolation means when a line fitted to the measurement points is extended to $p = 0$.
**Principle:** The measurement covers only the interval $20\ldots 100\,{}^\circ\text{C}$. When the line is extended beyond this interval, the result is not measured but inferred, and the inference assumes that the same linear dependence also holds outside the measured range.
**Model answer:** Extrapolation is extending a line beyond the measurement range on the assumption that the pressure behaves there as it does in the measured range. So the extrapolated value is an estimate, not a measurement result. Reading between two measured points is interpolation, repeating reduces the random error of the mean, and the line passes through the middle of the set of points, not through every point.

## fy3-13-L2-05
**Given:** five points from the table; the slope of the fitted line $k = 0.363\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$; the line passes through the centre point $(\theta_{\text{av}}, p_{\text{av}})$
**Find:** a) the centre point; b) the temperature at zero pressure $\theta_0$ in degrees Celsius
**Principle:** The flask is sealed and rigid, so the amount of substance and the volume stay constant and the pressure is a linear function of temperature. The fitted line passes through the middle of the set of points, so it passes through the centre point. The line is extended by extrapolation to $p = 0$.
**Reading the graph:** The centre point of the table is calculated as the means $\theta_{\text{av}}$ and $p_{\text{av}}$. The sum of the temperatures is $250\,{}^\circ\text{C}$ and the sum of the pressures is $588.9\,\text{kPa}$. The line passes through this point with the slope $k$.
**Formula:** The line through the point $(\theta_{\text{av}}, p_{\text{av}})$ is $p = p_{\text{av}} + k(\theta - \theta_{\text{av}})$. When $p = 0$ and $\theta = \theta_0$, then $\theta_0 = \theta_{\text{av}} - \dfrac{p_{\text{av}}}{k}$
**Conversions:** No conversions are needed: the pressures are in kilopascals, so in the quotient $p_{\text{av}}/k$ the kPa cancels and degrees Celsius remain.
**Substitution:** a) $\theta_{\text{av}} = 250\,{}^\circ\text{C} : 5 = 50\,{}^\circ\text{C}$ and $p_{\text{av}} = 588.9\,\text{kPa} : 5 = 117.78\,\text{kPa}$. b)

$$\begin{aligned} \theta_0 &= 50\,{}^\circ\text{C} - \dfrac{117.78\,\text{kPa}}{0.363\,\text{kPa}/{}^\circ\text{C}} \\ &= 50\,{}^\circ\text{C} - 324.46\,{}^\circ\text{C} \\ &= -274.46\,{}^\circ\text{C} \end{aligned}$$

**Answer:** $-274\,{}^\circ\text{C}$, three significant figures, like the slope $0.363$. The centre point is $(50\,{}^\circ\text{C};\ 117.78\,\text{kPa})$.
**Reasonableness:** At the temperature $\theta = 10\,{}^\circ\text{C}$ the line gives the pressure $117.78\,\text{kPa} + 0.363\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot (-40\,{}^\circ\text{C}) = 103.26\,\text{kPa}$, which differs from the measured $103.4\,\text{kPa}$ by only $0.14\,\text{kPa}$, clearly less than the uncertainty $1.0\,\text{kPa}$. The result differs from the accepted value $-273.15\,{}^\circ\text{C}$ by only about $1.3\,{}^\circ\text{C}$.

## fy3-13-L2-06
**Given:** group B uses the points $(\theta_1, p_1) = (20\,{}^\circ\text{C};\ 107.4\,\text{kPa})$ and $(\theta_2, p_2) = (35\,{}^\circ\text{C};\ 112.4\,\text{kPa})$; group A's result $-270\,{}^\circ\text{C}$; the pressure uncertainty $\pm 1.0\,\text{kPa}$
**Find:** a) group B's temperature at zero pressure $\theta_0$ in degrees Celsius; b) why the result differs from group A's result
**Principle:** In a sealed rigid container the pressure is a linear function of temperature, so two points determine a line, which is extended to $p = 0$. The measurement points have random scatter, so the shorter the interval from which the slope is calculated, the more uncertain it is.
**Reading the graph:** Group B reads only the first two rows of the table, the temperatures $20\,{}^\circ\text{C}$ and $35\,{}^\circ\text{C}$.
**Formula:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ and $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Conversions:** No conversions are needed: the pressures are in kilopascals, so the kPa cancels in the quotient $p_1/k$. The temperature difference $15\,{}^\circ\text{C}$ is the same in kelvins.
**Substitution:**

$$\begin{aligned} k &= \dfrac{(112.4 - 107.4)\,\text{kPa}}{(35 - 20)\,{}^\circ\text{C}} \\ &= \dfrac{5.0\,\text{kPa}}{15\,{}^\circ\text{C}} \\ &= 0.3333\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 20\,{}^\circ\text{C} - \dfrac{107.4\,\text{kPa}}{0.3333\,\text{kPa}/{}^\circ\text{C}} \\ &= 20\,{}^\circ\text{C} - 322.2\,{}^\circ\text{C} \\ &= -302.2\,{}^\circ\text{C} \end{aligned}$$

**Answer:** $-302\,{}^\circ\text{C}$, but only to about two figures ($-3.0 \cdot 10^{2}\,{}^\circ\text{C}$), because the slope $0.33\,\text{kPa}/{}^\circ\text{C}$ is known to two figures.
**Model answer (b):** Group B calculates the slope from an interval of only $15\,{}^\circ\text{C}$, over which the pressure rises by $5.0\,\text{kPa}$. The uncertainty $1.0\,\text{kPa}$ of each pressure can change the pressure difference by as much as $2.0\,\text{kPa}$, so the slope is uncertain by about $2.0 : 15 = 0.13\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$, which is about $40\,\%$ of the value itself. The extrapolation distance is over $300\,{}^\circ\text{C}$, so a small error in the slope grows large. Group A uses six points from an interval $75\,{}^\circ\text{C}$ wide, so the scatter evens out and the slope $0.370\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ is more reliable.
**Reasonableness:** At the temperature $95\,{}^\circ\text{C}$ group B's line would give the pressure $107.4\,\text{kPa} + 0.3333\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 75\,{}^\circ\text{C} = 132.4\,\text{kPa}$, but the measured value is $135.0\,\text{kPa}$. The difference $2.6\,\text{kPa}$ is larger than the uncertainty $1.0\,\text{kPa}$, so group B's line does not fit the other points. Group A's difference from the measured value would be under $0.2\,\text{kPa}$.

## fy3-13-L2-07
**Given:** the points $(20\,{}^\circ\text{C};\ 104.0\,\text{kPa})$, $(40\,{}^\circ\text{C};\ 110.6\,\text{kPa})$, $(60\,{}^\circ\text{C};\ 116.0\,\text{kPa})$ and $(80\,{}^\circ\text{C};\ 120.0\,\text{kPa})$; the pressure uncertainty $\pm 0.5\,\text{kPa}$; a line through the first and last points
**Find:** a) the temperature at zero pressure $\theta_0$ obtained by the group, in degrees Celsius; b) whether the table supports the suspicion of a leak and why a leak distorts the result
**Principle:** In a sealed flask with no leak the amount of substance is constant and the pressure rises linearly with temperature. If gas escapes, the amount of substance decreases and the linear model no longer holds. Extrapolation assumes that the model holds, so the result is distorted.
**Reading the graph:** From the table we read the first point $(20\,{}^\circ\text{C};\ 104.0\,\text{kPa})$ and the last point $(80\,{}^\circ\text{C};\ 120.0\,\text{kPa})$.
**Formula:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ and $\theta_0 = \theta_1 - \dfrac{p_1}{k}$
**Conversions:** No conversions are needed: the kilopascals cancel in the quotient, and the temperature difference $60\,{}^\circ\text{C}$ is the same in kelvins.
**Substitution:**

$$\begin{aligned} k &= \dfrac{(120.0 - 104.0)\,\text{kPa}}{(80 - 20)\,{}^\circ\text{C}} \\ &= \dfrac{16.0\,\text{kPa}}{60\,{}^\circ\text{C}} \\ &= 0.2667\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 20\,{}^\circ\text{C} - \dfrac{104.0\,\text{kPa}}{0.2667\,\text{kPa}/{}^\circ\text{C}} \\ &= 20\,{}^\circ\text{C} - 390\,{}^\circ\text{C} \\ &= -370\,{}^\circ\text{C} \end{aligned}$$

**Answer:** $-370\,{}^\circ\text{C}$, three significant figures, like the pressures; the result is clearly below $-273.15\,{}^\circ\text{C}$.
**Model answer (b):** The table supports the suspicion. The pressure rises less over each $20\,{}^\circ\text{C}$ interval: $6.6\,\text{kPa}$, $5.4\,\text{kPa}$ and $4.0\,\text{kPa}$, so the slope decreases from $0.33$ and $0.27$ to $0.20\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$. The differences are much larger than the uncertainty $\pm 0.5\,\text{kPa}$, so this is not scatter but a breakdown of the model: the points do not lie on a line. In a leak, gas escapes from the hot flask, so the amount of substance decreases and the pressure rises less than in a flask with no leak. The slope $0.267\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ of the end-point line is too small, and a small slope takes the zero-pressure point too far away, to $-370\,{}^\circ\text{C}$.
**Reasonableness:** The slope $0.33\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ of the first two points would give $20\,{}^\circ\text{C} - 104.0\,\text{kPa} : 0.33\,\tfrac{\text{kPa}}{{}^\circ\text{C}} = -295\,{}^\circ\text{C}$, which is closer to the correct value, because less of a leak has had time to occur. The result $-370\,{}^\circ\text{C}$ differs from the accepted value $-273.15\,{}^\circ\text{C}$ by almost a hundred degrees, which is too much to be mere measurement uncertainty.

## fy3-13-L3-04
**Given:** series A: $(25\,{}^\circ\text{C};\ 108.0\,\text{kPa})$ and $(85\,{}^\circ\text{C};\ 130.0\,\text{kPa})$; series B: $(25\,{}^\circ\text{C};\ 108.0\,\text{kPa})$ and $(225\,{}^\circ\text{C};\ 181.5\,\text{kPa})$; the pressure uncertainty $\Delta p = 1.0\,\text{kPa}$
**Find:** a) the uncertainty $\Delta\theta_0$ of the zero-pressure temperature for each series, in degrees Celsius; b) the effect of the width of the measurement range and the consistency with the value $-273.15\,{}^\circ\text{C}$
**Principle:** The pressure at each point is known within $p \pm \Delta p$. The steepest line passes through the lower end of the lower point and the upper end of the upper point, the shallowest the other way round; both fit the data. Their zero-pressure temperatures bound an interval, and the uncertainty is half of the interval. The model assumes that in a sealed rigid container the pressure is a linear function of temperature also outside the measured range.
**Reading the graph:** Two points are read from each series. The steepest line passes through the points $(\theta_1;\ p_1 - \Delta p)$ and $(\theta_2;\ p_2 + \Delta p)$, the shallowest through the points $(\theta_1;\ p_1 + \Delta p)$ and $(\theta_2;\ p_2 - \Delta p)$.
**Formula:** The pressure of the line at the point $\theta_1$ is $p_a$ and at the point $\theta_2$ it is $p_b$. Then $k = \dfrac{p_b - p_a}{\theta_2 - \theta_1}$, $\theta_0 = \theta_1 - \dfrac{p_a}{k}$ and $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Conversions:** No conversions are needed: the kilopascals cancel in the quotient $p_a/k$, and the temperature differences are the same in kelvins.
**Substitution:**

Series A, steepest:

$$\begin{aligned} k &= \dfrac{(131.0 - 107.0)\,\text{kPa}}{(85 - 25)\,{}^\circ\text{C}} \\ &= 0.4000\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{107.0\,\text{kPa}}{0.4000\,\text{kPa}/{}^\circ\text{C}} \\ &= -242.5\,{}^\circ\text{C} \end{aligned}$$

Series A, shallowest:

$$\begin{aligned} k &= \dfrac{(129.0 - 109.0)\,\text{kPa}}{(85 - 25)\,{}^\circ\text{C}} \\ &= 0.3333\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{109.0\,\text{kPa}}{0.3333\,\text{kPa}/{}^\circ\text{C}} \\ &= -302.0\,{}^\circ\text{C} \end{aligned}$$

So $\Delta\theta_{0,\text{A}} = \dfrac{(-242.5 + 302.0)\,{}^\circ\text{C}}{2} = 29.75\,{}^\circ\text{C}$.

Series B, steepest:

$$\begin{aligned} k &= \dfrac{(182.5 - 107.0)\,\text{kPa}}{(225 - 25)\,{}^\circ\text{C}} \\ &= 0.3775\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{107.0\,\text{kPa}}{0.3775\,\text{kPa}/{}^\circ\text{C}} \\ &= -258.44\,{}^\circ\text{C} \end{aligned}$$

Series B, shallowest:

$$\begin{aligned} k &= \dfrac{(180.5 - 109.0)\,\text{kPa}}{(225 - 25)\,{}^\circ\text{C}} \\ &= 0.3575\,\text{kPa}/{}^\circ\text{C} \\ \theta_0 &= 25\,{}^\circ\text{C} - \dfrac{109.0\,\text{kPa}}{0.3575\,\text{kPa}/{}^\circ\text{C}} \\ &= -279.90\,{}^\circ\text{C} \end{aligned}$$

$$\begin{aligned} \Delta\theta_{0,\text{B}} &= \dfrac{(-258.44 + 279.90)\,{}^\circ\text{C}}{2} \\ &= 10.73\,{}^\circ\text{C} \end{aligned}$$

**Answer:** The uncertainty of series B is $10.7\,{}^\circ\text{C}$; three significant figures, because the pressures are given to four figures and the difference of the extreme values, $21.46\,{}^\circ\text{C}$, is known to three. The uncertainty of series A is about $30\,{}^\circ\text{C}$. The results are $\theta_{0,\text{A}} = -272 \pm 30\,{}^\circ\text{C}$ and $\theta_{0,\text{B}} = -269 \pm 11\,{}^\circ\text{C}$.
**Model answer (b):** The measurement range of series B is $200\,{}^\circ\text{C}$ wide and that of series A $60\,{}^\circ\text{C}$, and the uncertainty of B is only about a third of the uncertainty of A. The same pressure uncertainty $\pm 1.0\,\text{kPa}$ affects the slope less the longer the interval from which it is calculated, and a small error in the slope grows in extrapolation. So a wider measurement range reduces the uncertainty. The interval of each series contains the value $-273.15\,{}^\circ\text{C}$ (A: $-302\ldots -243\,{}^\circ\text{C}$, B: $-280\ldots -258\,{}^\circ\text{C}$), so the results are consistent with the accepted value. The interval is an estimate, and it assumes that the pressure stays linear also outside the measured range.
**Reasonableness:** The ratio of the widths of the ranges is $200:60 \approx 3.3$ and the ratio of the uncertainties $29.75:10.73 \approx 2.8$, so the uncertainty decreases roughly in step with the increase in width. The midpoints of the intervals of the series, $-272\,{}^\circ\text{C}$ and $-269\,{}^\circ\text{C}$, are close to each other and close to the value $-273.15\,{}^\circ\text{C}$.

## fy3-13-L3-05
**Given:** the calibration points from the table, the first $(\theta_1, p_1) = (0\,{}^\circ\text{C};\ 100.4\,\text{kPa})$ and the last $(\theta_2, p_2) = (100\,{}^\circ\text{C};\ 137.0\,\text{kPa})$; the pressure read in the freezer $p = 94.0\,\text{kPa}$ and its uncertainty $\Delta p = 1.0\,\text{kPa}$
**Find:** a) the temperature of the freezer $\theta$ in degrees Celsius; b) the uncertainty of the temperature $\Delta\theta$ caused by the uncertainty of the pressure reading; c) why the result is extrapolation but reliable
**Principle:** The flask is sealed and rigid, so the amount of substance and the volume of the gas stay constant and the pressure is a linear function of temperature. The calibration line passes through points far apart, and it is solved for the temperature when the pressure is known. The temperature of the freezer is outside the calibration range $0\ldots 100\,{}^\circ\text{C}$.
**Reading the graph:** From the table we read the points farthest apart, $(0\,{}^\circ\text{C};\ 100.4\,\text{kPa})$ and $(100\,{}^\circ\text{C};\ 137.0\,\text{kPa})$. The other points serve as a check.
**Formula:** $k = \dfrac{p_2 - p_1}{\theta_2 - \theta_1}$ and the solution of the line $p = p_1 + k(\theta - \theta_1)$ is $\theta = \theta_1 + \dfrac{p - p_1}{k}$. The uncertainty of the pressure reading corresponds to the temperature uncertainty $\Delta\theta = \dfrac{\Delta p}{k}$.
**Conversions:** No conversions are needed: the kilopascals cancel, so the result is in degrees Celsius. The temperature difference $100\,{}^\circ\text{C}$ is the same in kelvins.
**Substitution:**

$$\begin{aligned} k &= \dfrac{(137.0 - 100.4)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\ &= 0.3660\,\text{kPa}/{}^\circ\text{C} \end{aligned}$$

a)

$$\begin{aligned} \theta &= 0\,{}^\circ\text{C} + \dfrac{(94.0 - 100.4)\,\text{kPa}}{0.3660\,\text{kPa}/{}^\circ\text{C}} \\ &= -17.49\,{}^\circ\text{C} \end{aligned}$$

b)

$$\begin{aligned} \Delta\theta &= \dfrac{1.0\,\text{kPa}}{0.3660\,\text{kPa}/{}^\circ\text{C}} \\ &= 2.73\,{}^\circ\text{C} \end{aligned}$$

**Answer:** $-17.5\,{}^\circ\text{C}$ with an uncertainty of about $2.7\,{}^\circ\text{C}$, so the result is $-17.5 \pm 2.7\,{}^\circ\text{C}$. The limiting piece of data is the pressure difference $94.0 - 100.4 = -6.4\,\text{kPa}$ (two figures), so in its simplest form the result is $-17 \pm 3\,{}^\circ\text{C}$; the decimal is given so that the result matches the value in the answer field.
**Model answer (c):** The temperature of the freezer is outside the calibrated range $0\ldots 100\,{}^\circ\text{C}$, so the line is extended beyond the measured range and the result is extrapolation, which assumes that the pressure stays linear. The extension is, however, only about $17.5\,{}^\circ\text{C}$ long, whereas in determining absolute zero the line is extended over $270\,{}^\circ\text{C}$. The uncertainty of the slope of the calibration line affects the result only over the length of the extension, so its effect is a few degrees. In addition, the temperature $-17.5\,{}^\circ\text{C}$ is far from the temperature at which air would begin to condense, so the linear model is reasonable.
**Reasonableness:** The result is a typical freezer temperature. The intermediate point checks the line: $100.4\,\text{kPa} + 0.3660\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \cdot 50\,{}^\circ\text{C} = 118.7\,\text{kPa}$, when the measured value is $118.6\,\text{kPa}$. In kelvins the temperature is $T = 273.15\,\text{K} - 17.49\,\text{K} = 255.66\,\text{K}$, and the ratio of the pressures $94.0:100.4 = 0.936$ is the same as the ratio of the temperatures $255.66:273.15 = 0.936$.
