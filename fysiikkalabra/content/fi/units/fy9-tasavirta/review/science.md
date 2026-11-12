VERDICT: PASS
CONTENT-HASH: 2a82521ac3173fae
Delta review (Johda itse, 2026-11-12) of the version passed at a1b8841afce01d90.

## Blocking
(none)

## Polish
1. `inquiry.json` activities[13] and [19], solution **Kaava:** states $U = E - R_\text{s} I$ without saying where it comes from; activities[15] uses $R = U^2/P$, i.e. the removed $P = U^2/R$. Fix (teacher's call): add "(Kirchhoffin 2. laki, ks. Johda itse)" or one derivation line.

## Checked
1. Johda itse *vastuksen teho*: $P = UI$ with Ohm's law gives $RI^2$ and $U^2/R$; the Ohmic-resistor condition is stated.
2. Johda itse *napajännite*: the loop $E - R_\text{s}I - RI = 0$ gives $I = E/(R+R_\text{s})$ and $U = RI = E - R_\text{s}I$; the model sentence defines $E$, $R_\text{s}$, $U$, $R$ with units and states constant $E$, $R_\text{s}$. The charging sentence (terminal voltage above the emf) is right.
3. New figure `piiri`: cell symbol with the long plate +, $R_\text{s}$ in series inside the battery box, current out of + through $R$, $U$ across the terminals. Concept map: only MAFY rows remain ($R_\text{kok} = \Sigma R$, $\Sigma\Delta V = 0$, $P = UI$, $P = W/\Delta t$).
4. No removed formula is used as given elsewhere in `unit.md`.
5. Every derivation starts from MAFY laws or a definition stated in the unit; every new symbol is defined with its unit; no removed formula is used as given in `unit.md`.
