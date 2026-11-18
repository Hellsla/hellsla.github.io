VERDICT: PASS
CONTENT-HASH: 8f2ecbbabde652e0
SCOPE: delta added-exercise from 613d454f2b784ce1 base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md:75 (L2-07) — the Kaava now ends in $v = c\sin\alpha_\text{r} : n_2$, but the Sijoitus still goes through $n$ and then $v$; substitute into the last form, or end the Kaava at $v = c : n$.
- solutions.md:183 (L3, acceptance angle) — $\theta_\text{max} = \sin^{-1}\sqrt{n_1^2 - n_2^2}$ uses $n_0 = 1$; write $n_0 = 1{,}00$ (air) at the row where $n_0$ is dropped.

## Checked
- Delta: only Kaava steps rewritten as aligned blocks (L1-01, L1-02, L1-03, L1-06, L2-01, L2-02, L2-04, L2-05, L2-06, L1-07, L1-08, L3-01, L3-02, L3-03, L1-09) plus paragraph splits; no number, answer, unit or tolerance changed.
- Each rajakulma Kaava now starts from Snell's law $n_1\sin\alpha_\text{r} = n_2\sin 90^\circ$ and solves for the asked quantity ($\alpha_\text{r}$, $n_2$, $n$); algebra right, and the $n_1 > n_2$ condition is in each Periaate.
- L2-04 (lamp): $r = h\tan\alpha_\text{r}$ from the right triangle; $2{,}05\,\text{m}$ recomputed.
- L2-06 zigzag: $t_2 = L : (v\sin\alpha_\text{r})$, $\Delta t = \dfrac{n_1 L}{c}\left(\dfrac{n_1}{n_2} - 1\right)$ derived right; $67{,}6\,\text{ns}$ recomputed.
- L3-02: $\varphi_\text{max} = 90^\circ - \alpha_\text{r}$, $n_1\cos\alpha_\text{r} = \sqrt{n_1^2 - n_2^2}$; $17{,}37^\circ$, $14{,}03^\circ$, $9{,}82^\circ$ recomputed.
- L3-03 bend: $(R-a):(R+a) = n_2 : n_1$ gives $R_\text{min} = a(n_1+n_2):(n_1-n_2) = 16{,}06\,\text{mm}$; algebra right.
- All other changed substitutions recomputed in one script (48,75°, 24,41°, 61,04°, 1,456, 1,414, 2,007·10⁵ km/s, 1,217 ms, 63,20°, 103,4 km, 1,493): unchanged and right.
- Hash 8f2ecbbabde652e0 at the start and at the end.
