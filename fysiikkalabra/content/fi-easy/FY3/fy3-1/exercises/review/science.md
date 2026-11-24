VERDICT: PASS
CONTENT-HASH: ca97d56eea315b06

## Blocking

## Polish
- exercises.json (fy3-1-L1-10): the stored 316,2 N still carries one figure more than the solution's 316 N. This is carried over and is inside the tolerance.

## Checked
- solutions.md:224 (fy3-1-L3-04): I read the Kaava block on disk as an aligned block. The note now reads $(c = x/F)$, the stretch per newton. With $F = G = mg$ this gives $x/m = c\,g$, so the first row is now defined correctly. Round 1's naming issue ("jousen vakio") is resolved.
- L3-04: dividing the two rows cancels $c$. The last symbolic row is the form the Sijoitus uses.
- L3-04 recomputed: $\sum x/\sum m = 21{,}8/2{,}10 = 10{,}38\,\text{cm/kg}$. Then $g_\text{X} = 9{,}81 \cdot 3{,}8/10{,}38 = 3{,}59\,\text{m/s}^2$, so $3{,}6\,\text{m/s}^2$, which is Mars. The answer is unchanged.
- The diff changes nothing else. The rest of my previous checks still hold.
- The hash was the same at the start and the end.
