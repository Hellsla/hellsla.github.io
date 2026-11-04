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
**Reasonableness:** The thyroid's own dose of $30\,\text{mSv}$ is large, but because only a small and fairly insensitive organ is irradiated, the effective dose, which describes the risk to the whole body, is only $4\,\%$ of it.

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
**Reasonableness:** Five halvings in a row: $96 \to 48 \to 24 \to 12 \to 6 \to 3\,\mu\text{Sv/h}$. Three centimetres of lead is a typical thickness for the shield of a gamma source.

## fy8-13-L3-01
**Given:** dose rate $\dot{H}_1 = 80\,\mu\text{Sv/h}$ at distance $r_1 = 1.0\,\text{m}$ without a shield, working time $t = 30\,\text{min}$; A: $r = 2.0\,\text{m}$ without a shield; B: $r = 1.0\,\text{m}$ and lead $d = 18\,\text{mm}$, $d_{1/2} = 6.0\,\text{mm}$
**Asked:** the difference of the doses $H_\text{A} - H_\text{B}$ in microsieverts, with its sign
**Principle:** In method A the dose rate is reduced by distance according to the inverse-square law, in method B by lead according to the half-value thickness. The working time is the same in both, so the doses are obtained by multiplying each dose rate by the same time.
**Formula:** $H_\text{A} = \dot{H}_1 \left(\dfrac{r_1}{r_\text{A}}\right)^2 t$ and $H_\text{B} = \dot{H}_1 \left(\tfrac{1}{2}\right)^{d/d_{1/2}} t$, so $H_\text{A} - H_\text{B} = \dot{H}_1 t \left[\left(\dfrac{r_1}{r_\text{A}}\right)^2 - \left(\tfrac{1}{2}\right)^{d/d_{1/2}}\right]$
**Conversions:** $t = 30\,\text{min} = 30 \cdot \tfrac{1}{60}\,\text{h} = 0.50\,\text{h}$
**Substitution:** $H_\text{A} = 80\,\mu\text{Sv/h} \cdot \left(\tfrac{1.0\,\text{m}}{2.0\,\text{m}}\right)^2 \cdot 0.50\,\text{h} = 20\,\mu\text{Sv/h} \cdot 0.50\,\text{h} = 10\,\mu\text{Sv}$ and $H_\text{B} = 80\,\mu\text{Sv/h} \cdot \left(\tfrac{1}{2}\right)^{3} \cdot 0.50\,\text{h} = 10\,\mu\text{Sv/h} \cdot 0.50\,\text{h} = 5.0\,\mu\text{Sv}$, so $H_\text{A} - H_\text{B} = 10\,\mu\text{Sv} - 5.0\,\mu\text{Sv} = 5.0\,\mu\text{Sv}$
**Answer:** $H_\text{A} - H_\text{B} = +5.0\,\mu\text{Sv}$, so method B gives the smaller dose; two significant figures like the distances and the half-value thickness.
**Reasonableness:** Doubling the distance reduces the dose rate to a quarter, but three half-value thicknesses reduce it to an eighth, so B is better and the difference should be positive.

## fy8-13-L3-02
**Given:** radon concentration of the home $400\,\tfrac{\text{Bq}}{\text{m}^3}$, average concentration $94\,\tfrac{\text{Bq}}{\text{m}^3}$ and the resulting dose $4.0\,\text{mSv}$ per year, other sources $1.9\,\text{mSv}$ per year
**Asked:** the resident's annual effective dose $H$ from all sources in millisieverts
**Principle:** Effective doses from different sources can be added together, because they describe the same risk to the whole body. The radon dose is by assumption directly proportional to the concentration, and the other sources give the average dose.
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
