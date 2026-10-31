VERDICT: PASS
CONTENT-HASH: f5a520209b17a828

## Blocking
None.

## Polish
None open. The four points from the review of hash 90dca00ab4f7fc9e are fixed:
1. Equipment is now only "jänniteanturi ja tiedonkeruuohjelma". It agrees with the tuki and teacher.md, which say a multimeter is too slow.
2. The page now says why the sensor draws almost no current: its resistance is megaohms, much larger than the coil's.
3. $U_\text{max}$ is now the largest absolute value of the first (entry) pulse. The page warns that with reversed wiring the "max" tool finds the exit pulse, which depends on the exit speed.
4. The sign change is now explained by the sign of $\Delta\Phi$, and the minus sign gives the direction by Lenz's law.

The other edits (Käsittele Q2 neutral with the line questions in O OO, extension controls moved to O OO, hero with two coils of the same size) add no physics error. The hero shows no method.

## Checked
- Definitions: $\Phi = BA$, Wb, $e = -N\,\Delta\Phi/\Delta t$ with $\Phi$ per turn, no flux change gives no voltage, Lenz. All correct.
- $U_\text{max} = c\,v$ with its conditions stated. I recomputed it with a point dipole (coil radius 1.5 cm, length 2 cm). The entry peak lies within about 1 mm of the coil's top edge, so measuring $h$ there is justified. $U_\text{max}/\sqrt{2gh}$ is constant within 1 % for $h$ from 0.10 m to 0.80 m.
- $S = N\Delta\Phi$: integrating up to the first zero crossing gives $N\Phi_\text{max}$, which does not depend on $v$ (within 0.3 %).
- The pulse figure is marked as a model and is computed from the dipole model. The pulses have opposite signs, and the exit pulse is taller and narrower. Matches the model answer. No invented data.
- Flux figure: field lines pass through the turns, $\overline{v}$ is blue, and the magnet has no pole letters. Setup figure: $h$ is drawn as in the tuki.
- Uncertainty: $\Delta v/v = \tfrac12\,\Delta h/h$, the half range and the slope error are correct.
- Safety: pinching and chipping, keeping magnets away from devices, a pacemaker reported to the teacher, and no power supply on the coil. No values are invented, and the eddy-current warning about metal tubes is correct.
- Scope: the page briefly explains FY7 induction (fy7-4 and fy7-5 are unpublished).
