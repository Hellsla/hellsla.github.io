VERDICT: PASS
CONTENT-HASH: 4f138c5ae82e3d40

## Blocking
None.

## Polish
All carried over from the last PASS; none touches this change.
- **s2 e w_R wording.** Could add "samalla absorboituneella annoksella"; strictly the reference is photon radiation, but "gammasäteily" is acceptable at this level (C).
- **s2 e task text, w_T wording.** Could include the solution's "eli kuinka suuri osa koko kehon riskistä tulee siitä". Optional.
- s1 a: "Fotoni on valon hiukkanen". Suggestion: "sähkömagneettisen säteilyn energiakvantti", because the 296 nm photon is UV.
- s1 d: add "joiden välissä on energia-aukko; johtavuusvyöllä elektronit voivat liikkua".
- s5 b: "Kasvukerroin kertoo, kuinka monta uutta fissiota yksi fissio aiheuttaa". Add "keskimäärin".
- s5 a: "eri massa". Better: "eri määrä neutroneja".
- s1 a Vastaus: "296 nm, koska … kolme merkitsevää numeroa". Suggestion: "tarkkuus on kolme merkitsevää numeroa, koska…".
- s2 e: "aiheuttaman haitan". More precise: "haitan riskin".
- s5 c: the typo "uraani-235:tä, Tämä" (editorial).

## Checked
Hash 4f138c5ae82e3d40 at start and end.
- **Diff HEAD~1 (fd2e54e95).** In this set it touches only solutions.md, two lines: s1 a Sijoitus (E_v, λ₃) and s1 d Sijoitus (λ_max, E of the 1500 nm photon). Four expressions change from `\dfrac{h·c}{X}` to `h · \dfrac{c}{X}`. No number, unit, answer, tolerance or point value changed. practice.py check reports OK.
- **Values identical.** a·b/c = a·(b/c). Recomputed both forms: 3,562·10⁻¹⁹ J, 2,959·10⁻⁷ m, 1,107·10⁻⁶ m, 1,324·10⁻¹⁹ J, matching the stated results (2,22 eV, 296 nm, 1110 nm, 0,83 eV).
- **Typesetting.** Each new expression has balanced braces, `\cdot` between h and the fraction, units kept with their numbers, and decimal commas `{,}`. The denominator is unchanged, so units still reduce to J or m. The text is identical to fi in these expressions.
- Everything else is unchanged since the last PASS and still agrees.
