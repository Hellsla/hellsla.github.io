VERDICT: PASS
CONTENT-HASH: 4a1e0daa19b91386

Delta review (solution practice, 2026-11-12) of the version passed before.

## Blocking
None. Built fy9-voimat (en) with ?ratkaisut=1, every details element opened, at 390 and 1280 px. No .katex-error, no script errors; the changed Sijoitus, Kaava and Vastaus lines render with upright subscripts and units, thin spaces and \cdot (no x, no \times); decimal comma in fi and fi-easy, decimal point in en; the new symbol definitions ("missä ...") read naturally and the sentences are in the right language.

## Polish
1. Page-level horizontal overflow at 390 px when all details are open (167 px): long inline-math Sijoitus or answer lines in .reveal or .answer blocks do not wrap or scroll. Verified in the previous version (git 761b6673) for energia, voimat, sahkokentta and mittaaminen, so it is not a regression of this change (mittaaminen is about 40 px wider now). Fix when convenient: break such a substitution into a display line (\begin{aligned}) or let .reveal/.answer have overflow-x:auto.
