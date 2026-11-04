VERDICT: FAIL
CONTENT-HASH: 7c190a2fcc2fb406

## Blocking
- B (internal consistency) — content/fi-easy/FY2/fy2-8/inquiry.json:63 — the retrieval feedback still says "Ilman luonnollista kasvihuoneilmiötä keskilämpötila olisi noin $-18\,{}^\circ\text{C}$ todellisen $+15\,{}^\circ\text{C}$:n sijaan. Se on noin $33\,\text{K}$ alempi." The corrected lesson now says the $-18\,{}^\circ\text{C}$ value is the effective radiating temperature of a simple radiative-balance model, "ei tarkka ennuste pinnan lämpötilasta ilman kasvihuonekaasuja". — Fix: "Maan yksinkertainen säteilytasapainomalli antaa efektiiviseksi säteilylämpötilaksi noin $-18\,{}^\circ\text{C}$, mutta maanpinnan keskilämpötila on noin $+15\,{}^\circ\text{C}$. Ero, noin $33\,\text{K}$, näyttää kasvihuoneilmiön merkityksen."
- B (internal consistency, rubric) — content/fi-easy/FY2/fy2-8/inquiry.json:497 — the criterion "luonnollinen ilmiö nostaa keskilämpötilan noin $-18\,{}^\circ\text{C}$:sta noin $+15\,{}^\circ\text{C}$:een" still presents −18 °C as the surface temperature without greenhouse gases, while the model answer under it (l. 501) was corrected. — Fix: "Mainitsin, että maanpinta on noin $+15\,{}^\circ\text{C}$, vaikka yksinkertainen säteilytasapainomalli antaa vain noin $-18\,{}^\circ\text{C}$."

(The fi version has the same two lines. Outside this review's hash: exercises/exercises.json:69 says "keskilämpötila on noin $+15\,{}^\circ\text{C}$ eikä noin $-18\,{}^\circ\text{C}$"; align it with the model-answer wording when the exercise set is next edited.)

## Polish
- lesson.md: "Ilman sitä merien vesi olisi jäässä" stays acceptable (C), but since the −18 °C is now hedged, "olisi todennäköisesti jäässä" would match the new caution.

## Checked
batch delta review: lesson theory, misconception, Tiivistelmä, sim model box and ennuste feedback now carry the effective-radiating-temperature wording; GISTEMP 2025 anomaly map caption (base 1951–1980, grey = no data, not a photo) correct; numbers unchanged.
