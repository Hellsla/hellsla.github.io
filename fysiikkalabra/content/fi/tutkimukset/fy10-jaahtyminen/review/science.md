VERDICT: PASS
CONTENT-HASH: 25ed7d65bd70f235

## Blocking
None.

## Polish
- With 1 dl of water, the vessel's heat capacity and evaporation matter relatively more. The page already states "astia lämpenee ja jäähtyy veden mukana" as a condition and excludes the initial transient, so this needs no change. teacher.md could mention it when the test run is done.

## Checked (revision from 148966f54c744215)
- All five earlier polish points are applied correctly:
  - The exponential fit is now $A\cdot e^{-Bt} + C$ to $T$, or $A\cdot e^{-Bt}$ to $T - T_\text{huone}$. The reason the pure form is wrong (it tends to $0\ {}^\circ\text{C}$) is right, and teacher.md lists it as a misconception.
  - The half-time test now says "sopusoinnussa".
  - The late points are now "suhteellisesti epätarkimpia".
  - The O plan measures until the difference falls to about a quarter, which is two half-times (teacher.md says so too). Reading half-times from several starting points is now possible.
  - The result notation no longer reuses $k$, and the half-time keeps $\bar{t}_{1/2} \pm \Delta t_{1/2}$.
- New maths prerequisite (exponential function and natural logarithm, helpful, with half-time as the fallback): correct and consistent with the theory block.
- Model figure: the difference bars are now green (#2b8a3e). That is not a force, velocity or acceleration colour, and no arrows are drawn. The figure is unchanged otherwise: the model curve only, bars at 1, ½ and ¼ one $t_{1/2}$ apart, no numbers on the axes and no data points. All four embedded SVGs match figures.py.
- Unchanged and still correct:
  - Newton's law, its derivation and its stated conditions. Linearity is called approximate, because radiation, natural convection and evaporation grow faster than linearly at large $\Delta T$.
  - The linearisation: slope $-k$, intercept $\ln(T_0 - T_\text{huone})$ and $t_{1/2} = \ln 2/k$, plus the Celsius/kelvin remark.
  - $\Delta(T - T_\text{huone}) = \Delta T + \Delta T_\text{huone}$, and the steepest/least-steep line and half-range methods.
  - Hot-water safety in investigation.json: no equipment-dependent value is invented, and the probe limits come "sen ohjeesta".
- The new sources sentence in mode I and the mode labels in Päätät itse make no physics claims.
