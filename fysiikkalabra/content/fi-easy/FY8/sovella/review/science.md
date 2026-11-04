VERDICT: PASS
CONTENT-HASH: 49d7cb0c881119b3

## Blocking
None. The round-1 item is fixed. The s2 e task text now explains the radiation weighting factor (how many times more the radiation type damages cells than gamma radiation) and the tissue weighting factor (how sensitive the tissue is) separately. The solution Periaate adds that w_T tells how large a share of the whole-body risk comes from the tissue. Both are correct and match fy8-13.

## Polish
- **s2 e w_R wording.** It could add "samalla absorboituneella annoksella", because the comparison only holds at the same absorbed dose. Strictly, the reference is photon radiation (gamma and X-rays). At this level, "gammasäteily" is acceptable (C).
- **s2 e task text, w_T wording.** It could include the same "eli kuinka suuri osa koko kehon riskistä tulee siitä" phrase as the solution. That is optional.
- Carried over, s1 a: "Fotoni on valon hiukkanen". Suggestion: "sähkömagneettisen säteilyn energiakvantti", because the 296 nm photon is UV.
- Carried over, s1 d: add "joiden välissä on energia-aukko; johtavuusvyöllä elektronit voivat liikkua".
- Carried over, s5 b: "Kasvukerroin kertoo, kuinka monta uutta fissiota yksi fissio aiheuttaa". Add "keskimäärin".
- Carried over, s5 a: "eri massa". Better: "eri määrä neutroneja".
- Carried over, s1 a Vastaus: "296 nm, koska … kolme merkitsevää numeroa". Suggestion: "tarkkuus on kolme merkitsevää numeroa, koska…".
- Carried over, s2 e: "aiheuttaman haitan". More precise: "haitan riskin".
- Carried over, s5 c: the typo "uraani-235:tä, Tämä" (editorial).

## Checked
Hash 49d7cb0c881119b3 at start and end.
- **Diff HEAD~1.** It changes only the s2 e task text and its Periaate. No number, answer, tolerance or point value changed. practice.py check reports OK.
- **s2 e chain is unchanged.** E = AtQ = 2.83·10⁻⁴ J, D = 2.36·10⁻⁴ Gy, H_T = 4.71 mSv, H_E = 0.566 mSv, about 10 % of 5.9 mSv.
- **Sanity scan.** The answers.py values still match the solutions: 296 nm, 1193, 5.594 MeV, 3.52 kg / 83 %, 1791 W, 36.2 cm, 0.23 µSv/h, 7.16, 135 s, 3.67 %, 3.49 a.
- **Round-1 checks still hold.** These cover the added explanations, the sentence splits, the criteria and the alt texts ("r miinus kahdesta").
