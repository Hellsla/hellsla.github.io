VERDICT: FAIL
CONTENT-HASH: 6e3fb1b8a584919f

## Blocking
- exercises/solutions.md:221 (L2-06, Kuvaajan lukeminen) — **A**, the round-1 finding fixed in only two of its three places: the slopes of the $E_\text{k,max}(f)$ lines are still called "likimain $\tfrac{h}{e} = 4{,}14 \cdot 10^{-15}\,\tfrac{\text{eV}}{\text{Hz}}$" ($h/e$ has the unit V s; the slope of $E_\text{k,max}(f)$ is $h$) — fix: write $h = 4{,}14 \cdot 10^{-15}\,\text{eV}\,\text{s}$, as L2-07 and L2-08 now do; numbers unchanged.

## Polish
- exercises/solutions.md:251 — L2-07 still gives "three significant figures like the energies in the data" for $W = 2{,}14\,\text{eV}$; $0{,}55\,\text{eV}$ has two; the reason is that $W$ is known to the hundredth of an eV.

## Checked
- L2-07 Järkevyys: slope $4{,}133 \cdot 10^{-15}\,\text{eV/Hz}$ is $h$ in eV s; correct ($h/e = 4{,}136 \cdot 10^{-15}$ numerically, as eV s).
- L2-08: $E_\text{k,max} = h(f - f_0)$ correct; $h = 4{,}136 \cdot 10^{-15}\,\text{eV}\,\text{s}$ = $0{,}4136\,\text{eV}$ per $10^{14}\,\text{Hz}$; $0{,}4136 \cdot 6{,}44 = 2{,}66\,\text{eV}$.
- L2-09: $c/f_0 = 2{,}998 \cdot 10^8 / 7{,}0 \cdot 10^{14} = 428\,\text{nm}$; two significant figures justified by the read frequency; answer 428 with tolerance 4 % accepts $4{,}3 \cdot 10^2\,\text{nm}$.
- L1-10 hyphen fix and the caption-marker removal and chain re-breaks change no number.
- Hash identical at start and end.
