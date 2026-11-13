VERDICT: PASS
CONTENT-HASH: e3a9ded2e50a2046

## Blocking

## Polish
- lesson.md "Ytimen energiatasot ja gammaspektri" — "jää tasosta alle 0,1 keV" but 2505,8 - (1173,2 + 1332,5) = 0,1 keV exactly, not less. Fix: "noin 0,1 keV".
- lesson.md same paragraph — the recoil of about 0,03 keV checks out (E^2/(2Mc^2) per photon, about 0,013 and 0,017 keV), but the student cannot see where it comes from; "pyöristystä" for the remainder is fine. Optional: say "pyöristyksen ja rekyylin yhteisvaikutus on noin 0,1 keV" to keep the paragraph short.
- Earlier polish items not addressed in this diff (electron-capture scope, prediction prompts, "Mallin tiedot", sim chart height) remain optional and non-blocking.

## Checked
- Scale sentence now reads "kymmeniätuhansia tai satojatuhansia kertoja enemmän": consistent with tens of keV to hundreds of keV versus a few eV; fixes my earlier polish item.
- Recoil figure (0,03 keV) is physically correct for Co-60 and the explanation of the sum gap is a sound, short correction.
- Misconception paragraph now says the element changes when the proton number changes (alpha, beta, electron capture): consistent with the text, gamma claim unchanged.
- inquiry.json feedback for the caesium option: shorter, still names the actual error (photon carries no proton), Z stays 56.
- Nothing in the diff discloses an answer early or alters figures, task order or workload.
