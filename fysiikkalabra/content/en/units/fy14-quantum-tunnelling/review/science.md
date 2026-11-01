VERDICT: FAIL
CONTENT-HASH: d2a9fd877ad07dac

Science review of fy14-quantum-tunnelling, 2026-11-01 (full review: unit.md, inquiry.json, teacher.md, figures.py).

## Blocking
1. **B, causality and consistency across chapters.** `unit.md` *Tunnelling and the Sun* says two protons within a few femtometres are where "the **strong nuclear force** can hold them together". For two protons this is not true: the diproton is unbound and falls apart at once. Fusion succeeds only when one proton turns into a neutron during the encounter (weak interaction) and a deuteron forms. The same section then gives the 9-billion-year wait right after "Each meeting has only a tiny chance [to tunnel]", and `check-3`'s correct feedback does the same. A student will read the wait as a result of tunnelling alone. Wikipedia *Proton–proton chain* (checked 2026-11-01) and this course's own `fy14-fusion-reactions` give the weak interaction as the reason for the slowness. Fix, in as few words as possible:
   - (a) "… within a few femtometres, where the strong nuclear force acts" (also the sunbarrier aria-label "where the strong nuclear force can join the protons" → "acts");
   - (b) after "fusion goes on all the time": "Even after tunnelling, one of the two protons must turn into a neutron at that moment, a slow process of the weak interaction (chapter *The Energy of the Stars*). So an average proton waits about 9 billion years …";
   - (c) `check-3` correct feedback: "… An average proton still waits about 9 billion years, also because the first step needs the weak interaction."

## Polish
2. `unit.md` Sun section: "In 1928 Gamow's tunnelling solved the puzzle." In 1928 Gamow explained alpha decay; Atkinson and Houtermans (1929) applied it to stars. Write "Gamow's tunnelling (1928) solved the puzzle".
3. `unit.md` *Electrons one at a time*: Merli, Missiroli and Pozzi used an electron biprism, the electron version of two slits. "a two-slit device" could say "an electron biprism, which acts like two slits".
4. The classical turning distance (about 1000 fm) treats one proton as fixed, with 1.35 keV. That is fine as an order of magnitude ("of the order of" is already said for k_BT). Optionally add "roughly" in check-explain's model answer.

## Checked
- Recomputed: k_BT at 15.7 MK = 1.353 keV; k e² / 2 fm = 720 keV (×533); turning point 1.440 MeV·fm : 1.353 keV = 1064 fm (figure 1060); proton λ at 1.35 keV = 779 fm (mistakes 24 630, 1102, 33 380; m_p/m_e = 1836); electron at 100 V: p = 5.40·10⁻²⁴ kg·m/s, λ = 0.123 nm, v = 5.9·10⁶ m/s = 2.0 % of c; tennis ball 2.3·10⁻³⁴ m. Tunnelling table = exp(−2κL) with κ = √(2m_e·1 eV)/ħ = 5.12 nm⁻¹: 7.7 %, 0.60 %, 0.046 %, 0.0035 % (labelled approximate model values: fine); factor 12.8 ≈ 13 per 0.25 nm, 171 for doubling.
- Figures: `barrier` schematic and labelled so; same wavelength on both sides is right; `slits` sampled from a two-slit intensity and labelled simulated; `sunbarrier` line and crossing correct.
- Every choice has exactly one correct option; the distractor feedback is correct.
- Facts: Young 1801–03, Taylor 1909, Davisson–Germer and G. P. Thomson–Reid 1927, Merli et al. 1974, Born 1926, Gamow / Gurney–Condon 1928, STM 1981 / Nobel 1986, de Broglie (Dieppe 1892–1987, history degree 1910, thesis 1924, Nobel 1929 with that motivation), Sun core 15.7 MK and age 4.6 Gyr, the 9 Gyr wait (WebFetch, *Proton–proton chain*, 2026-11-01).
