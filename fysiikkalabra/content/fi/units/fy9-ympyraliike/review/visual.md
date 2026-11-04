VERDICT: PASS
CONTENT-HASH: 678dc353273487b6

Round 2 (delta review of round 1 fixes; round 1 hash fc0aa5da26550049). Visual and editorial review of fy9-ympyraliike.

## Round 1 Blocking: verified fixed
- sovella/tasks.json s3 d: "Mikä on lyhin kierrosaika, jolla alustaa saa pyörittää tällä kärryllä ja etäisyydellä?". It is clear and in good Finnish, and it renders in the preview.
- inquiry.json lumilapio, Sijoitus: "takakäden suhteen". It renders in the built page at 390 and 1280.

## Polish: verified
- Figure tilanteet, captured at 390 (2x):
  - $\overline{N}$ sits above the arrow tip, clear of the block;
  - the panel-title fractions are display size and legible;
  - "Maa" and the ground arc are grey, so blue is now used only for velocity;
  - force red, velocity blue and acceleration orange hold.
- The new unit.md sentence renders cleanly at 390 with inline $\tfrac{v^2}{r}$.
- The s2 d model answer and the tarkistus-1 feedback are in correct Finnish with LaTeX units.

## Build check
`build.py fy9-ympyraliike` at 390 and 1280:
- 0 `.katex-error`;
- no raw `$`;
- no console errors;
- no horizontal overflow (scrollWidth equals the viewport).

## Still open (Polish, not blocking)
- s1 a: the Järkevyys inline fractions are kept as house style.
- Shared: the catalog figures fy5-6/vr and fy5-4/kuvaaja have 13 px labels at 390.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
