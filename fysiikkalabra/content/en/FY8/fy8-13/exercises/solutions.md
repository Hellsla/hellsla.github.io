## fy8-13-L1-01
**Given:** absorbed energy $E = 0.130\,\text{J}$, mass of the body $m = 65.0\,\text{kg}$
**Asked:** the absorbed dose $D$ in milligrays
**Principle:** The absorbed dose is the radiation energy absorbed by tissue per unit mass. The energy is spread over the whole body, so we divide by the mass of the whole body.
**Formula:** $D = \dfrac{E}{m}$
**Conversions:** $1\,\tfrac{\text{J}}{\text{kg}} = 1\,\text{Gy} = 1000\,\text{mGy}$
**Substitution:** $D = \dfrac{0.130\,\text{J}}{65.0\,\text{kg}} = 0.00200\,\tfrac{\text{J}}{\text{kg}} = 0.00200\,\text{Gy} = 2.00\,\text{mGy}$
**Answer:** $2.00\,\text{mGy}$, three significant figures like the energy $0.130\,\text{J}$ and the mass $65.0\,\text{kg}$.
**Reasonableness:** Estimate $0.13\,\text{J} : 65\,\text{kg} = 0.002\,\tfrac{\text{J}}{\text{kg}}$. The dose is about a third of the average annual dose of a Finn, so it is small but measurable.

## fy8-13-L1-02
**Given:** absorbed dose of the lungs $D_\text{T} = 0.30\,\text{mGy}$, weighting factor of alpha radiation $w_\text{R} = 20$
**Asked:** the equivalent dose of the lungs $H_\text{T}$ in millisieverts
**Principle:** An alpha particle ionises densely and, at the same absorbed dose, damages cells $20$ times more than gamma radiation. The equivalent dose is obtained by multiplying the absorbed dose by the radiation weighting factor.
**Formula:** $H_\text{T} = w_\text{R} D_\text{T}$
**Conversions:** Not needed: when the absorbed dose is in milligrays, the equivalent dose comes directly in millisieverts, because $w_\text{R}$ is a pure number.
**Substitution:** $H_\text{T} = 20 \cdot 0.30\,\text{mGy} = 6.0\,\text{mSv}$
**Answer:** $6.0\,\text{mSv}$, two significant figures like the dose $0.30\,\text{mGy}$.
**Reasonableness:** The numerical value of the equivalent dose is $20$ times that of the absorbed dose, as it should be for alpha radiation. From gamma radiation the same absorbed dose would give only $0.30\,\text{mSv}$.

## fy8-13-L1-03
**Given:** dose rate $\dot{H} = 3\,\mu\text{Sv/h}$ (approximately, a typical long-haul flight), duration of the flight $t = 5.0\,\text{h}$
**Asked:** the passenger's dose $H$ in microsieverts
**Principle:** The dose rate is the dose per unit time. When it stays roughly constant at cruising altitude, the dose is the dose rate times the time.
**Formula:** $H = \dot{H} t$
**Conversions:** Not needed: the dose rate is in the unit $\mu\text{Sv/h}$ and the time in hours.
**Substitution:** $H = 3\,\mu\text{Sv/h} \cdot 5.0\,\text{h} = 15\,\mu\text{Sv}$
**Answer:** about $15\,\mu\text{Sv}$; the dose rate is given only approximately (about $3\,\mu\text{Sv/h}$), so the result is an order-of-magnitude estimate.
**Reasonableness:** The flight gives about $0.015\,\text{mSv}$, or less than $0.3\,\%$ of the average annual dose of a Finn, $5.9\,\text{mSv}$. An occasional flight therefore hardly increases the annual dose.

## fy8-13-L1-04
**Given:** dose rate $\dot{H}_1 = 120\,\mu\text{Sv/h}$ at distance $r_1 = 1.0\,\text{m}$, new distance $r_2 = 4.0\,\text{m}$
**Asked:** the dose rate $\dot{H}_2$ at distance $r_2$
**Principle:** From a point source radiation spreads in all directions over the surface of a sphere with area $4\pi r^2$. The air does not attenuate the radiation, so the dose rate is inversely proportional to the square of the distance.
**Formula:** $\dot{H}_2 = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2$
**Conversions:** Not needed: the distances are in the same unit, so their ratio is a pure number.
**Substitution:** $\dot{H}_2 = 120\,\mu\text{Sv/h} \cdot \left(\dfrac{1.0\,\text{m}}{4.0\,\text{m}}\right)^2 = 120\,\mu\text{Sv/h} \cdot \tfrac{1}{16} = 7.5\,\mu\text{Sv/h}$
**Answer:** $7.5\,\mu\text{Sv/h}$, two significant figures like the distances $1.0\,\text{m}$ and $4.0\,\text{m}$.
**Reasonableness:** The distance becomes four times as large, that is, it doubles twice, and each doubling reduces the dose rate to a quarter: $120 \to 30 \to 7.5\,\mu\text{Sv/h}$.

## fy8-13-L1-05
**Given:** dose rate without a shield $\dot{H}_0 = 64\,\mu\text{Sv/h}$, thickness of lead $d = 18\,\text{mm}$, half-value thickness $d_{1/2} = 6.0\,\text{mm}$
**Asked:** the dose rate $\dot{H}$ behind the shield
**Principle:** Every layer one half-value thickness thick attenuates half of the gamma radiation arriving at it, so the dose rate is halved after every layer.
**Formula:** $\dot{H} = \dot{H}_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Conversions:** Not needed: the thickness and the half-value thickness are both in millimetres.
**Substitution:** $\dot{H} = 64\,\mu\text{Sv/h} \cdot \left(\tfrac{1}{2}\right)^{18\,\text{mm} / 6.0\,\text{mm}} = 64\,\mu\text{Sv/h} \cdot \left(\tfrac{1}{2}\right)^{3} = 64\,\mu\text{Sv/h} \cdot \tfrac{1}{8} = 8.0\,\mu\text{Sv/h}$
**Answer:** $8.0\,\mu\text{Sv/h}$, two significant figures like the dose rate $64\,\mu\text{Sv/h}$ and the half-value thickness $6.0\,\text{mm}$.
**Reasonableness:** Three halvings in a row: $64 \to 32 \to 16 \to 8\,\mu\text{Sv/h}$. The radiation weakens but does not disappear, as it should for gamma radiation.

## fy8-13-L2-01
**Given:** beta radiation of iodine-131, mass of the thyroid $m = 20\,\text{g}$, absorbed energy $E = 0.60\,\text{mJ}$, weighting factor of beta radiation $w_\text{R} = 1$, weighting factor of the thyroid $w_\text{T} = 0.04$
**Asked:** the effective dose $H_\text{E}$ in millisieverts
**Principle:** Energy per unit mass gives the absorbed dose of the thyroid. The weighting factor of beta radiation is $1$, so the equivalent dose has the same numerical value. Only the thyroid receives a dose, so the effective dose is its equivalent dose multiplied by its weighting factor.
**Formula:** $D_\text{T} = \dfrac{E}{m}$, $H_\text{T} = w_\text{R} D_\text{T}$ and $H_\text{E} = w_\text{T} H_\text{T}$, so $H_\text{E} = w_\text{T} w_\text{R} \dfrac{E}{m}$
**Conversions:** $E = 0.60\,\text{mJ} = 0.60 \cdot 0.001\,\text{J} = 0.00060\,\text{J}$ and $m = 20\,\text{g} = 20 \cdot 0.001\,\text{kg} = 0.020\,\text{kg}$; $1\,\tfrac{\text{J}}{\text{kg}}$ is $1\,\text{Sv}$ when weighted.
**Substitution:** $H_\text{E} = 0.04 \cdot 1 \cdot \dfrac{0.00060\,\text{J}}{0.020\,\text{kg}} = 0.04 \cdot 0.030\,\text{Sv} = 0.0012\,\text{Sv} = 1.2\,\text{mSv}$
**Answer:** $1.2\,\text{mSv}$, two significant figures like the energy $0.60\,\text{mJ}$ and the mass $20\,\text{g}$.
**Reasonableness:** The thyroid's own dose of $30\,\text{mSv}$ is large, but because only a small and fairly insensitive organ is irradiated, the effective dose, which estimates the long-term cancer risk to the whole body for an average person, is only $4\,\%$ of it.

## fy8-13-L2-02
**Given:** dose rate $\dot{H}_1 = 150\,\mu\text{Sv/h}$ at distance $r_1 = 1.0\,\text{m}$, distance of the workplace $r_2 = 2.5\,\text{m}$, permitted dose $H = 100\,\mu\text{Sv}$
**Asked:** the working time $t$ in hours
**Principle:** The dose rate of a point source decreases with the square of the distance. At the workplace the dose rate is constant, so the dose grows in direct proportion to time.
**Formula:** $\dot{H}_2 = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2$ and $H = \dot{H}_2 t$, so $t = \dfrac{H}{\dot{H}_1} \left(\dfrac{r_2}{r_1}\right)^2$
**Conversions:** Not needed: the dose is in microsieverts and the dose rate in the unit $\mu\text{Sv/h}$, so the time comes out in hours.
**Substitution:** $t = \dfrac{100\,\mu\text{Sv}}{150\,\mu\text{Sv/h}} \cdot \left(\dfrac{2.5\,\text{m}}{1.0\,\text{m}}\right)^2 = 0.66667\,\text{h} \cdot 6.25 = 4.1667\,\text{h}$
**Answer:** $4.2\,\text{h}$, two significant figures like the distances $1.0\,\text{m}$ and $2.5\,\text{m}$.
**Reasonableness:** The dose rate at the workplace is $150 : 6.25 = 24\,\mu\text{Sv/h}$, and $4.2\,\text{h} \cdot 24\,\mu\text{Sv/h} \approx 100\,\mu\text{Sv}$. At a distance of one metre the same dose would accumulate in under an hour, so distance lengthens the working time many times over.

## fy8-13-L2-03
**Given:** average concentration $94\,\tfrac{\text{Bq}}{\text{m}^3}$ and the resulting dose $4.0\,\text{mSv}$ per year, concentration at home $300\,\tfrac{\text{Bq}}{\text{m}^3}$; the dose is proportional to the concentration
**Asked:** the annual dose $H$ the resident receives from radon, in millisieverts
**Principle:** The more radon and its decay products there are in the air, the more alpha decays take place in the airways. When the time spent at home is the same, the dose is by assumption directly proportional to the concentration, so the doses are in the same ratio as the concentrations.
**Formula:** $\dfrac{H}{H_\text{avg}} = \dfrac{c}{c_\text{avg}}$, so $H = H_\text{avg} \dfrac{c}{c_\text{avg}}$, where $c$ is the concentration and the subscript $\text{avg}$ means the average
**Conversions:** Not needed: the concentrations are in the same unit, so their ratio is a pure number.
**Substitution:** $H = 4.0\,\text{mSv} \cdot \dfrac{300\,\tfrac{\text{Bq}}{\text{m}^3}}{94\,\tfrac{\text{Bq}}{\text{m}^3}} = 4.0\,\text{mSv} \cdot 3.1915 = 12.766\,\text{mSv}$
**Answer:** $13\,\text{mSv}$ per year, two significant figures like the dose $4.0\,\text{mSv}$ and the concentration $94\,\tfrac{\text{Bq}}{\text{m}^3}$.
**Reasonableness:** The concentration is about three times the average, so the dose is about $3 \cdot 4.0\,\text{mSv} = 12\,\text{mSv}$. In a home at the reference level the radon dose alone is already more than twice the whole average annual dose of a Finn.

## fy8-13-L2-04
**Given:** dose rate without a shield $\dot{H}_0 = 96\,\mu\text{Sv/h}$, target $\dot{H} = 3.0\,\mu\text{Sv/h}$, half-value thickness $d_{1/2} = 6.0\,\text{mm}$
**Asked:** the thickness of the lead shield $d$ in millimetres
**Principle:** Every half-value thickness halves the dose rate of gamma radiation. We calculate how many halvings are needed and multiply that by the half-value thickness.
**Formula:** $\dot{H} = \dot{H}_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, so $2^{d/d_{1/2}} = \dfrac{\dot{H}_0}{\dot{H}}$ and $d = d_{1/2} \cdot \log_2 \dfrac{\dot{H}_0}{\dot{H}}$
**Conversions:** Not needed: the dose rates are in the same unit, and the thickness comes out in the same unit as the half-value thickness, that is, in millimetres.
**Substitution:** $\dfrac{\dot{H}_0}{\dot{H}} = \dfrac{96\,\mu\text{Sv/h}}{3.0\,\mu\text{Sv/h}} = 32 = 2^5$, so $d = 6.0\,\text{mm} \cdot 5 = 30\,\text{mm}$
**Answer:** $30\,\text{mm}$, two significant figures like the half-value thickness $6.0\,\text{mm}$ and the target $3.0\,\mu\text{Sv/h}$.
**Reasonableness:** Five halvings in a row: $96 \to 48 \to 24 \to 12 \to 6 \to 3$ (in $\mu\text{Sv/h}$). Three centimetres of lead is a typical thickness for the shield of a gamma source.

## fy8-13-L3-01
**Given:** dose rate $\dot{H}_1 = 80\,\mu\text{Sv/h}$ at distance $r_1 = 1.0\,\text{m}$ without a shield, working time $t = 30\,\text{min}$; A: $r = 2.0\,\text{m}$ without a shield; B: $r = 1.0\,\text{m}$ and lead $d = 18\,\text{mm}$, $d_{1/2} = 6.0\,\text{mm}$
**Asked:** the difference of the doses $H_\text{A} - H_\text{B}$ in microsieverts, with its sign
**Principle:** In method A the dose rate is reduced by distance according to the inverse-square law, in method B by lead according to the half-value thickness. The working time is the same in both, so the doses are obtained by multiplying each dose rate by the same time.
**Formula:** $H_\text{A} = \dot{H}_1 \left(\dfrac{r_1}{r_\text{A}}\right)^2 t$ and $H_\text{B} = \dot{H}_1 \left(\tfrac{1}{2}\right)^{d/d_{1/2}} t$, so $H_\text{A} - H_\text{B} = \dot{H}_1 t \left[\left(\tfrac{r_1}{r_\text{A}}\right)^2 - \left(\tfrac{1}{2}\right)^{d/d_{1/2}}\right]$
**Conversions:** $t = 30\,\text{min} = 30 \cdot \tfrac{1}{60}\,\text{h} = 0.50\,\text{h}$
**Substitution:** $H_\text{A} = 80\,\mu\text{Sv/h} \cdot \left(\tfrac{1.0\,\text{m}}{2.0\,\text{m}}\right)^2 \cdot 0.50\,\text{h} = 20\,\mu\text{Sv/h} \cdot 0.50\,\text{h} = 10\,\mu\text{Sv}$ and $H_\text{B} = 80\,\mu\text{Sv/h} \cdot \left(\tfrac{1}{2}\right)^{3} \cdot 0.50\,\text{h} = 10\,\mu\text{Sv/h} \cdot 0.50\,\text{h} = 5.0\,\mu\text{Sv}$, so $H_\text{A} - H_\text{B} = 10\,\mu\text{Sv} - 5.0\,\mu\text{Sv} = 5.0\,\mu\text{Sv}$
**Answer:** $H_\text{A} - H_\text{B} = +5.0\,\mu\text{Sv}$, so method B gives the smaller dose; two significant figures like the distances and the half-value thickness.
**Reasonableness:** Doubling the distance reduces the dose rate to a quarter, but three half-value thicknesses reduce it to an eighth, so B is better and the difference should be positive.

## fy8-13-L3-02
**Given:** radon concentration of the home $400\,\tfrac{\text{Bq}}{\text{m}^3}$, average concentration $94\,\tfrac{\text{Bq}}{\text{m}^3}$ and the resulting dose $4.0\,\text{mSv}$ per year, other sources $1.9\,\text{mSv}$ per year
**Asked:** the resident's annual effective dose $H$ from all sources in millisieverts
**Principle:** Effective doses from different sources can be added together, because they estimate the same thing: the long-term cancer risk to the whole body for an average person. The radon dose is by assumption directly proportional to the concentration, and the other sources give the average dose.
**Formula:** $H_\text{radon} = H_\text{avg} \dfrac{c}{c_\text{avg}}$ and $H = H_\text{radon} + H_\text{other}$, so $H = H_\text{avg} \dfrac{c}{c_\text{avg}} + H_\text{other}$
**Conversions:** Not needed: the concentrations are in the same unit and the doses in millisieverts.
**Substitution:** $H = 4.0\,\text{mSv} \cdot \dfrac{400\,\tfrac{\text{Bq}}{\text{m}^3}}{94\,\tfrac{\text{Bq}}{\text{m}^3}} + 1.9\,\text{mSv} = 17.021\,\text{mSv} + 1.9\,\text{mSv} = 18.921\,\text{mSv}$
**Answer:** about $19\,\text{mSv}$ per year, two significant figures like the doses $4.0\,\text{mSv}$ and $1.9\,\text{mSv}$.
**Reasonableness:** The concentration is about four times the average, so the radon dose is about $4 \cdot 4.0\,\text{mSv} = 16\,\text{mSv}$ and a little more. The total dose is more than three times the average $5.9\,\text{mSv}$, so fixing the radon problem of the house would reduce the resident's dose more than any other measure.

## fy8-13-L3-03
**Given:** absorbed dose of the lungs from alpha radiation $D_\text{lungs} = 0.10\,\text{mGy}$, uniform absorbed dose of the whole body from gamma radiation $D_\gamma = 0.50\,\text{mGy}$; $w_\text{R} = 20$ for alpha and $1$ for gamma; $w_\text{T} = 0.12$ for the lungs
**Asked:** the effective dose $H_\text{E}$ from both sources together in millisieverts
**Principle:** Alpha radiation irradiates only the lungs, so its effective dose is the equivalent dose of the lungs multiplied by the weighting factor of the lungs. Gamma radiation irradiates the whole body uniformly, and the tissue weighting factors add up to $1$, so its effective dose is the same as the equivalent dose of the body. The effective doses are added together.
**Formula:** $H_\text{E} = w_\text{T} w_{\text{R},\alpha} D_\text{lungs} + w_{\text{R},\gamma} D_\gamma$
**Conversions:** Not needed: when the absorbed doses are in milligrays, the weighted doses come out in millisieverts.
**Substitution:** $H_\text{E} = 0.12 \cdot 20 \cdot 0.10\,\text{mGy} + 1 \cdot 0.50\,\text{mGy} = 0.24\,\text{mSv} + 0.50\,\text{mSv} = 0.74\,\text{mSv}$
**Answer:** $0.74\,\text{mSv}$, two significant figures like the doses $0.10\,\text{mGy}$ and $0.50\,\text{mGy}$.
**Reasonableness:** The absorbed dose from alpha radiation is a fifth of that from gamma radiation, but once weighted its share is almost half of the share of gamma, because $0.12 \cdot 20 = 2.4$. If the factor of the lungs were forgotten, the share of alpha would wrongly come out as $2.0\,\text{mSv}$.

## fy8-13-L1-06
**Asked:** which statement correctly describes the difference between the absorbed dose (gray) and the effective dose (sievert)
**Principle:** The absorbed dose $D = \tfrac{E}{m}$ only tells how much energy is absorbed per unit mass. In the equivalent dose it is multiplied by the radiation weighting factor $w_\text{R}$ and in the effective dose also by the tissue weighting factors $w_\text{T}$, so the sievert describes the health risk of radiation.
**Model answer:** The correct statement is the one according to which the gray tells the energy absorbed in tissue per unit mass and the sievert also takes into account the type of radiation and the sensitivity of the tissue. The units $\text{Gy}$ and $\text{Sv}$ both have the form $\tfrac{\text{J}}{\text{kg}}$, but the quantities are not the same: an absorbed dose of $0.30\,\text{mGy}$ from alpha radiation gives an equivalent dose of $6.0\,\text{mSv}$. The statement that the gray concerns only gamma radiation and the sievert only alpha radiation is wrong, because neither is limited to one type of radiation. The statement that the units describe the source is wrong, because the decay rate of a source is measured in becquerels. The statement that the quantities are the same is wrong, because the type of radiation affects the sieverts.

## fy8-13-L1-07
**Given:** equivalent dose of the liver $H_\text{liver} = 2.0\,\text{mSv}$ and weighting factor $w_\text{liver} = 0.04$, equivalent dose of the stomach $H_\text{stomach} = 1.0\,\text{mSv}$ and weighting factor $w_\text{stomach} = 0.12$
**Asked:** the effective dose $H_\text{E}$ in millisieverts
**Principle:** The effective dose is obtained by multiplying the equivalent dose of each irradiated tissue by its weighting factor and adding the products together. The other tissues receive no dose, so they add nothing to the sum.
**Formula:** $H_\text{E} = w_\text{liver} H_\text{liver} + w_\text{stomach} H_\text{stomach}$
**Conversions:** Not needed: when the equivalent doses are in millisieverts, the effective dose comes out in millisieverts, because the weighting factors are pure numbers.
**Substitution:** $H_\text{E} = 0.04 \cdot 2.0\,\text{mSv} + 0.12 \cdot 1.0\,\text{mSv} = 0.080\,\text{mSv} + 0.12\,\text{mSv} = 0.20\,\text{mSv}$
**Answer:** $0.20\,\text{mSv}$, two significant figures like the doses $2.0\,\text{mSv}$ and $1.0\,\text{mSv}$.
**Reasonableness:** The sum of the weighting factors is only $0.04 + 0.12 = 0.16$, so the effective dose is smaller than the equivalent dose of either organ ($2.0\,\text{mSv}$ and $1.0\,\text{mSv}$). It estimates the long-term cancer risk to the whole body for an average person, even though only two organs are irradiated.

## fy8-13-L1-08
**Given:** effective dose of the examination $H_1 = 0.10\,\text{mSv}$, average annual dose of a Finn $H_\text{avg} = 5.9\,\text{mSv}$
**Asked:** the share of the dose of the examination in the average annual dose as a percentage
**Principle:** The share is obtained by dividing the dose of the examination by the annual dose and expressing the ratio as a percentage. The doses are in the same unit, so the ratio is a pure number.
**Formula:** $\text{share} = \dfrac{H_1}{H_\text{avg}} \cdot 100\,\%$
**Conversions:** Not needed: both doses are in millisieverts.
**Substitution:** $\text{share} = \dfrac{0.10\,\text{mSv}}{5.9\,\text{mSv}} \cdot 100\,\% = 0.016949 \cdot 100\,\% = 1.6949\,\%$
**Answer:** $1.7\,\%$, two significant figures like the annual dose $5.9\,\text{mSv}$.
**Reasonableness:** The annual dose is $5.9 : 0.10 \approx 59$ times the dose of the examination, so the examination is about $\tfrac{1}{59} \approx 0.017$, or $1.7\,\%$, of the annual dose. One examination therefore hardly increases the annual dose.

## fy8-13-L2-05
**Given:** annual effective doses in the table: radon $4.0\,\text{mSv}$, other natural radiation $1.1\,\text{mSv}$, medical use $0.8\,\text{mSv}$
**Asked:** a) the sum of the doses $H_\text{tot}$, b) the share of radon in the total dose as a percentage
**Principle:** Effective doses from different sources are added together, because they estimate the same thing: the long-term cancer risk to the whole body for an average person. The share of radon is its dose divided by the total dose.
**Formula:** $H_\text{tot} = H_1 + H_2 + H_3$ and $\text{share} = \dfrac{H_\text{radon}}{H_\text{tot}} \cdot 100\,\%$
**Conversions:** Not needed: all doses are in millisieverts.
**Substitution:** a) $H_\text{tot} = 4.0\,\text{mSv} + 1.1\,\text{mSv} + 0.8\,\text{mSv} = 5.9\,\text{mSv}$; b) $\text{share} = \dfrac{4.0\,\text{mSv}}{5.9\,\text{mSv}} \cdot 100\,\% = 67.8\,\%$
**Answer:** $68\,\%$, two significant figures like the doses. The sum $5.9\,\text{mSv}$ agrees with the average in STUK-A263 (2020).
**Reasonableness:** The radon dose $4.0\,\text{mSv}$ is slightly more than two thirds of the sum, because two thirds would be $\tfrac{2}{3} \cdot 5.9\,\text{mSv} = 3.9\,\text{mSv}$. The other sources together are $1.1 + 0.8 = 1.9\,\text{mSv}$, less than a third.

## fy8-13-L2-06
**Given:** distances and dose rates from the table: $r = 0.50\,\text{m}$; $1.00\,\text{m}$; $1.50\,\text{m}$ and $2.00\,\text{m}$ and $\dot{H} = 410$; $98.0$; $44.0$ and $26.0\,\mu\text{Sv/h}$; new distance $r = 3.0\,\text{m}$
**Asked:** a) the products $\dot{H} r^2$, b) whether the measurement obeys the inverse-square law, c) the dose rate $\dot{H}$ at a distance of $3.0\,\text{m}$
**Principle:** If $\dot{H}_2 = \dot{H}_1 \left(\tfrac{r_1}{r_2}\right)^2$, then $\dot{H}_1 r_1^2 = \dot{H}_2 r_2^2$, so the product $\dot{H} r^2$ is the same at all distances. The measurements have small random variation, so the products are approximately equal.
**Reading the table:** The products are calculated for each row of the table. If the product increased or decreased systematically with distance, the law would not hold.
**Formula:** $k = \dot{H} r^2$ and $\dot{H}(r) = \dfrac{k_\text{avg}}{r^2}$
**Conversions:** Not needed: the distances are in metres and the dose rates in the unit $\mu\text{Sv/h}$.
**Substitution:** a) $k_1 = 410\,\mu\text{Sv/h} \cdot (0.50\,\text{m})^2 = 102.5\,\mu\text{Sv} \cdot \text{m}^2/\text{h}$, $k_2 = 98.0\,\mu\text{Sv/h} \cdot (1.00\,\text{m})^2 = 98.0\,\mu\text{Sv} \cdot \text{m}^2/\text{h}$, $k_3 = 44.0\,\mu\text{Sv/h} \cdot (1.50\,\text{m})^2 = 99.0\,\mu\text{Sv} \cdot \text{m}^2/\text{h}$ and $k_4 = 26.0\,\mu\text{Sv/h} \cdot (2.00\,\text{m})^2 = 104.0\,\mu\text{Sv} \cdot \text{m}^2/\text{h}$; b) the products are $98$–$104$ and show no trend: they vary by about $\pm 3\,\%$ around the mean, so the measurement obeys the inverse-square law; c) the sum of the products is $102.5 + 98.0 + 99.0 + 104.0 = 403.5$, so $k_\text{avg} = \dfrac{403.5}{4} = 100.875\,\mu\text{Sv} \cdot \text{m}^2/\text{h}$ and $\dot{H} = \dfrac{100.875\,\mu\text{Sv} \cdot \text{m}^2/\text{h}}{(3.0\,\text{m})^2} = 11.208\,\mu\text{Sv/h}$
**Answer:** $11\,\mu\text{Sv/h}$ (more precisely $11.2\,\mu\text{Sv/h}$), two significant figures like the distance $3.0\,\text{m}$.
**Reasonableness:** According to the inverse-square law, from a distance of $2.00\,\text{m}$ to $3.0\,\text{m}$ the dose rate decreases by the factor $\left(\tfrac{2.00}{3.0}\right)^2 = 0.444$, so $26.0\,\mu\text{Sv/h} \cdot 0.444 = 11.6\,\mu\text{Sv/h}$ (based on the outermost measurement alone; the mean method gives a slightly smaller value). The result $11.2\,\mu\text{Sv/h}$ is close to it and smaller than any measured value, as it should be at a greater distance.

## fy8-13-L2-07
**Given:** mass of the liver $m = 1.8\,\text{kg}$, absorbed energy $E = 0.63\,\text{mJ}$, weighting factor of alpha radiation $w_\text{R} = 20$
**Asked:** a) the student's error, b) the equivalent dose of the liver $H_\text{T}$ in millisieverts
**Principle:** The student's absorbed dose $0.35\,\text{mGy}$ is correct, but for the equivalent dose it must be multiplied by the radiation weighting factor. At the same absorbed dose, alpha radiation damages cells $20$ times more than gamma radiation.
**Formula:** $D = \dfrac{E}{m}$ and $H_\text{T} = w_\text{R} D$
**Conversions:** $E = 0.63\,\text{mJ} = 0.63 \cdot 0.001\,\text{J} = 0.00063\,\text{J}$; $1\,\tfrac{\text{J}}{\text{kg}} = 1\,\text{Gy} = 1000\,\text{mGy}$.
**Substitution:** $D = \dfrac{0.00063\,\text{J}}{1.8\,\text{kg}} = 0.00035\,\text{Gy} = 0.35\,\text{mGy}$ and $H_\text{T} = 20 \cdot 0.35\,\text{mGy} = 7.0\,\text{mSv}$
**Answer:** $7.0\,\text{mSv}$, two significant figures like the energy $0.63\,\text{mJ}$ and the mass $1.8\,\text{kg}$.
**Model answer on part a):** Gray and sievert are not the same thing, even though both have the form $\tfrac{\text{J}}{\text{kg}}$. The gray measures absorbed energy per unit mass, and the sievert takes into account the type of radiation. The weighting factor of alpha radiation is $20$, so the student should have multiplied the dose by $20$. Their answer $0.35\,\text{mSv}$ is $20$ times too small.
**Reasonableness:** The equivalent dose $7.0\,\text{mSv}$ is $20$ times the absorbed dose $0.35\,\text{mGy}$, as it should be for alpha radiation. From gamma radiation the same absorbed dose would give only $0.35\,\text{mSv}$.

## fy8-13-L3-04
**Given:** average concentration $c_\text{avg,Finland} = 94\,\tfrac{\text{Bq}}{\text{m}^3}$ and the resulting dose $H_\text{avg} = 4.0\,\text{mSv}$ per year; the resident's time at home $80\,\%$ of the average; reference level $300\,\tfrac{\text{Bq}}{\text{m}^3}$; measured concentrations winter $380$, spring $260$, summer $140$ and autumn $300\,\tfrac{\text{Bq}}{\text{m}^3}$; target dose $2.0\,\text{mSv}$
**Asked:** a) the mean concentration of the year, b) the radon dose, c) an explanation and a comparison with the reference level, d) the highest permitted mean concentration after remediation
**Principle:** The periods are of equal length, so the mean concentration of the year is their average. By assumption the radon dose is directly proportional to the concentration and to the time at home, so the dose is obtained by multiplying the average dose of Finns by the ratio of the concentrations and the ratio of the times. In part d) the same equation is solved for the concentration.
**Formula:** $c_\text{avg} = \dfrac{c_1 + c_2 + c_3 + c_4}{4}$, $H = H_\text{avg} \dfrac{c}{c_\text{avg,Finland}} \cdot f$ and $c = \dfrac{H}{H_\text{avg} f} c_\text{avg,Finland}$, where $f = 0.80$ is the ratio of the times at home
**Conversions:** Not needed: the concentrations are in the same unit and the doses in millisieverts; $80\,\% = 0.80$.
**Substitution:** a) The sum of the concentrations is $380 + 260 + 140 + 300 = 1080\,\tfrac{\text{Bq}}{\text{m}^3}$, so $c_\text{avg} = \dfrac{1080\,\tfrac{\text{Bq}}{\text{m}^3}}{4} = 270\,\tfrac{\text{Bq}}{\text{m}^3}$; b) $H = 4.0\,\text{mSv} \cdot \dfrac{270\,\tfrac{\text{Bq}}{\text{m}^3}}{94\,\tfrac{\text{Bq}}{\text{m}^3}} \cdot 0.80 = 4.0\,\text{mSv} \cdot 2.8723 \cdot 0.80 = 9.19\,\text{mSv}$; d) $c = \dfrac{2.0\,\text{mSv}}{4.0\,\text{mSv} \cdot 0.80} \cdot 94\,\tfrac{\text{Bq}}{\text{m}^3} = 0.625 \cdot 94\,\tfrac{\text{Bq}}{\text{m}^3} = 58.75\,\tfrac{\text{Bq}}{\text{m}^3}$
**Answer:** $59\,\tfrac{\text{Bq}}{\text{m}^3}$, two significant figures like the target dose $2.0\,\text{mSv}$. The dose in part b) is about $9.2\,\text{mSv}$.
**Model answer on part c):** The radon concentration is highest in winter, because warm indoor air rises and draws radon from the ground (the chimney effect) and the windows are closed. In this model the dose is determined by the mean concentration of the year, $270\,\tfrac{\text{Bq}}{\text{m}^3}$, so a dose calculated from the winter value $380\,\tfrac{\text{Bq}}{\text{m}^3}$ would be $\tfrac{380}{270} = 1.4$ times as large, or about $40\,\%$ too large. The official measurement is nevertheless made in the heating season, for at least two months, and the result is used as an estimate of the annual mean: it is slightly high but on the safe side. Here the mean concentration of the heating season (autumn, winter and spring) is $(300 + 380 + 260) : 3 \approx 313\,\tfrac{\text{Bq}}{\text{m}^3}$, that is, above the reference level $300\,\tfrac{\text{Bq}}{\text{m}^3}$, so radon remediation would be recommended. The mean concentration of the year, $270\,\tfrac{\text{Bq}}{\text{m}^3}$, is nevertheless below the reference level; it is still about three times the average of Finnish dwellings.
**Reasonableness:** Check: $4.0\,\text{mSv} \cdot \dfrac{58.75}{94} \cdot 0.80 = 4.0\,\text{mSv} \cdot 0.625 \cdot 0.80 = 2.0\,\text{mSv}$. The concentration must decrease by about $78\,\%$ (from $270$ to $58.75$), which is a large change but one that radon remediation can achieve.

## fy8-13-L3-05
**Given:** dose rate at a distance of $1.0\,\text{m}$ behind a concrete wall from the table (at thicknesses $0$, $4.0$, $8.0$ and $12.0\,\text{cm}$: $240$, $121$, $60.5$ and $29.8\,\mu\text{Sv/h}$), distance of the workstation $r_2 = 2.0\,\text{m}$, thickness of the wall $d = 10\,\text{cm}$, dose limit $H = 25\,\mu\text{Sv}$
**Asked:** a) the half-value thickness of concrete $d_{1/2}$, b) the dose rate at the workstation, c) the longest working time $t$ in hours, d) one assumption that may make the working time too long
**Principle:** Concrete halves the dose rate at every half-value thickness, and distance reduces it according to the inverse-square law. The two effects are independent, so their factors are multiplied. The dose rate at the workstation is constant, so the permitted time is the dose limit divided by the dose rate.
**Reading the table:** In the table $240 \to 121 \to 60.5 \to 29.8\,\mu\text{Sv/h}$: the dose rate halves every time the thickness increases by $4.0\,\text{cm}$ ($240 : 2 = 120 \approx 121$, $121 : 2 \approx 60.5$ and $60.5 : 2 \approx 30 \approx 29.8$). Therefore $d_{1/2} \approx 4.0\,\text{cm}$.
**Formula:** $\dot{H} = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2 \left(\dfrac{1}{2}\right)^{d/d_{1/2}}$ and $H = \dot{H} t$, so $t = \dfrac{H}{\dot{H}}$
**Conversions:** Not needed: the thickness and the half-value thickness are in centimetres, the distances in metres and the dose in microsieverts.
**Substitution:** b) $\dot{H} = 240\,\mu\text{Sv/h} \cdot \left(\dfrac{1.0\,\text{m}}{2.0\,\text{m}}\right)^2 \cdot \left(\dfrac{1}{2}\right)^{10\,\text{cm}/4.0\,\text{cm}} = 60\,\mu\text{Sv/h} \cdot 0.1768 = 10.61\,\mu\text{Sv/h}$; c) $t = \dfrac{25\,\mu\text{Sv}}{10.61\,\mu\text{Sv/h}} = 2.357\,\text{h}$
**Answer:** $2.4\,\text{h}$, two significant figures like the dose limit $25\,\mu\text{Sv}$ and the thickness of the wall $10\,\text{cm}$. The dose rate in part b) is about $11\,\mu\text{Sv/h}$.
**Model answer on part d):** The formula assumes that the photons hitting the concrete are either absorbed or pass through with the same proportion. In reality some of the gamma radiation scatters in the wall and the surroundings, and the scattered radiation can raise the dose rate at the workstation above the calculated value. The point-source assumption and the reading of the half-value thickness from the table are also approximate. Therefore the working time should be chosen shorter than the calculated one, for example half of it, and the dose should be monitored with a dosimeter.
**Reasonableness:** Behind the wall at a distance of $1.0\,\text{m}$ the dose rate would be $240 \cdot \left(\tfrac{1}{2}\right)^{2.5} = 42.4\,\mu\text{Sv/h}$, which lies between the table values $60.5$ and $29.8\,\mu\text{Sv/h}$, just as $10\,\text{cm}$ lies between the thicknesses $8.0\,\text{cm}$ and $12.0\,\text{cm}$. The distance $2.0\,\text{m}$ reduces it to a quarter, that is, to $10.6\,\mu\text{Sv/h}$, and $2.4\,\text{h} \cdot 10.6\,\mu\text{Sv/h} \approx 25\,\mu\text{Sv}$.
