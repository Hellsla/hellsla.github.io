VERDICT: PASS
CONTENT-HASH: ba12e1046bac1b9e

## Blocking
None. The blocking issue from the previous review (68b46f0db8623883) is fixed. A steady tilt is now said to change only the deceleration and the slope. The line still passes through the origin, so the tilt does not show in the graph. It is checked with a spirit level or by braking in both directions. This now reads the same in the Teoria tuki, in "Miksi juuri nämä akselit?" (the tilt is explicitly not a cause of a constant term) and in teacher.md ($a = \mu g\cos\theta \pm g\sin\theta$).

## Polish
- "noin $6\ \%$ asteen kallistusta kohti" (student page and teacher.md): this holds only near $\mu = 0.3$. One degree adds about $0.017$ to the apparent $\mu$, which is $\tan 1^\circ$. The relative error is therefore about $1.7\ \%/\mu$: 3.5 % at $\mu = 0.5$, 12 % at $\mu = 0.15$. Suggested wording: "noin 0,02 kitkakertoimessa asteen kallistusta kohti".

## Checked (full page at f3d9677dccfae0f5)
- Energy model: $-\mu m g s = 0 - \tfrac{1}{2}mv_0^2 \Rightarrow \tfrac{1}{2}v_0^2 = \mu g\cdot s$, a line through the origin with slope $\mu g$ (m/s²). With $v_0^2$ on the axis the slope is $2\mu g$, and with the axes swapped it is the reciprocal. $s(v_0)$ curves upward. Speed-dependent friction bends the points. A constant term comes from a push still acting or from $v_0$ and $x_0$ read at different moments.
- Reading: $v_0$ and $x_0$ are now read at the same moment just after the peak, with smoothing. This is correct and consistent with the extension's fit-window hint.
- Brake caveat: with wheels carrying weight or a spring brake, the result is $F_\mu/G$. teacher.md now says correctly that the mass cancels only when the weight presses the brake, and that with a spring brake a heavier cart slides farther. The new Ennusta Q3 (added load) is an open prediction and fits this.
- Force diagram (figures.py unchanged): rectangle body. $\overline{G}$ starts at the centre and $\overline{N}$ at the bottom surface, 34 px apart and of equal length. $\overline{F}_\mu$ starts at the surface, points backwards and is 0.30 of $G$. $\overline{v}$ (blue) and $\overline{a}$ (orange) are drawn beside the body.
- Extension: $ma = \mu mg$, $a = \mu g$, and the $v(t)$ slope is $-\mu g$ (the cart moves away from the sensor). Overlapping intervals are read as "sopusoinnussa".
- Uncertainty: $\Delta(\tfrac{1}{2}v_0^2) \approx v_0\Delta v_0$, $\Delta\mu/\mu = \Delta k/k$, and the rounding rule is correct.
- Hero, setup and model figures: consistent with the physics. House rules: \overline vectors, \cdot, LaTeX labels and colours are followed. No invented data or sensor ranges.
- Revision to ba12e1046bac1b9e checked: the tilt effect now reads "mitattu kitkakerroin muuttuu noin $0{,}02$ asteen kallistusta kohti" in both investigation.md and teacher.md. This is correct ($\tan 1^\circ \approx 0.017$) and holds for any $\mu$, so the polish point is resolved.
