VERDICT: PASS
CONTENT-HASH: e657e0ce17df22e3

## Blocking
None.

## Polish
- Epävarmuus: "jokaisessa mittauspisteessä, vähintään parhaassa pisteessä ja sen naapuripisteissä" asks for both every point and a minimum in one sentence. The physics is right; only the wording is unclear (pedagogy's call).

## Re-check of the previous polish (hash 146866d913c81e90 to e657e0ce17df22e3)
- Swept figure: all three velocity arrows now run from 330 to 454, so they are equal. They are blue #1971c2 with $\overline{v}$ and clear the hub nose.
- AC clause: on the AC range the meters show effective values, and for a resistive load $P = UI$ is the mean power. This is correct.
- Density: "riippuu lämpötilasta ja ilmanpaineesta" is correct. The page now estimates $\Delta\rho$ from the room's temperature and pressure (table or calculation), which is a sound method and invents no values. 1,2 is right for room air, and 1,25 in fy4-15 is a "noin" value for cooler air, so there is no conflict.
- $v = \sqrt[3]{\overline{v^3}}$ is the speed that makes $\tfrac12\rho A v^3$ equal to the mean power, so $3\cdot\Delta v/v$ applies to it. Using the relative uncertainty of $\overline{v^3}$ directly in place of that term is equivalent and correct.
- $P$ against $v^3$ is a straight line only if $\eta$ does not change with $v$. This is correct, and it covers the cut-in speed and the changing tip-speed ratio.
- $\Delta P$ at the points: needed to compare differences with the uncertainty, and consistent with the error bars in the graph tuki.
- The removed "double each step" hint for the load leaves no gap in the physics.

## Checked (unchanged from the previous review)
- $P = UI$ with its units. Circuit: the ammeter is in series, and the voltmeter is across the load only.
- $P_\text{tuuli} = \tfrac12\rho A v^3$ with its conditions; $\eta = P/P_\text{tuuli}$; averaging $v^3$ over the area.
- $\Delta\eta/\eta = \Delta P/P + \Delta\rho/\rho + 2\Delta r/r + 3\Delta v/v$ and $\Delta P/P = \Delta U/U + \Delta I/I$.
- Betz is about 59 % for an ideal rotor, with the cause given; it matches fy4-15.
- Nothing is invented: no data, no kit limits, no menu names. The hero uses no physics colours.
