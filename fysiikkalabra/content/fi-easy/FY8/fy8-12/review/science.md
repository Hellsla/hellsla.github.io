VERDICT: PASS
CONTENT-HASH: a59616042b279e74

## Blocking

## Polish
- lesson.md:144 (aria-label of figure jaljet) — "Se irrottaa elektronin, ja se ionisoi lyhyellä matkalla muutaman molekyylin": the second "se" can be read as the gamma photon; it is the released electron that ionises — write "ja tämä elektroni ionisoi" (wording; the figure itself is right).
- lesson.md (Yleinen virhekäsitys) — carried over: true for sterilisation and diagnostics; 15–18 MV radiotherapy makes some photoneutrons. C at this level.

## Checked
- Rewritten figure descriptions (hero, energia, jaljet, lapaisy, gm, vaimeneminen, tarkistus figure) in figures.json and lesson.md: every number kept (1,7–3,3 eV, 12,6 eV, 60 keV, 662 keV, 0,1 mm, 5 mm, 5 cm, 500 V, 5,5 / 11 / 16,5 mm, 0,6 at 25 mm, 0–48 mm, 2 mm × 50 /min, 800 /min); scripted comparison of keys and values.
- Physics of the rewrites correct: the photon threshold is the ionisation energy of water; the GM avalanche is caused by the electron accelerated towards the positive wire; "pulssitaajuus ilman taustasäteilyä" is the net rate; the attenuation curve halves every 5,5 mm in lead (μ_Pb ≈ 1,29 1/cm → 5,4 mm) and Al gives ≈ 0,59 at 25 mm.
- assets/sims/fy8/fy8-12/sim.js:149 label from lang key, fi-easy.json "GM-putki" as before; model and `simState` unchanged.
- lesson.md, inquiry.json, exit-ticket.json numbers equal the Finnish source; inquiry difference is only ½ written out as \tfrac{1}{2} (10 mm lead → 0,29 ≈ ¼, correct).
