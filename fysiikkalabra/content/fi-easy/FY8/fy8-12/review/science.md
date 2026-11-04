VERDICT: PASS
CONTENT-HASH: 65587e36f7083d7a

## Blocking

## Polish
- lesson.md:144 (aria-label of figure jaljet) — carried over: "Se irrottaa elektronin, ja se ionisoi lyhyellä matkalla muutaman molekyylin": the second "se" can be read as the gamma photon; it is the released electron that ionises — write "ja tämä elektroni ionisoi".
- lesson.md (Yleinen virhekäsitys) — carried over: true for sterilisation and diagnostics; 15–18 MV radiotherapy makes some photoneutrons. C at this level.

## Checked
- Only change since the last PASS: lessons/FY8/fy8-12/figures.py:208 `tuntematon` d-axis labels every 6 mm instead of every 4 mm; grid (2 mm × 50 /min) and curve (800 /min, d½ = 12 mm) unchanged.
- Rendered SVG: d labels 6, 12, …, 48 at their grid lines; y labels 200–800. The curve meets 400 /min exactly at the labelled 12 mm line, so reading d½ = 12 mm still works; the solution's checks 24 mm → 200 and 48 mm → 50 are on labelled values too.
- figures.json alt text "Ruudukon viivat ovat 2 millimetrin välein vaakasuunnassa ja 50 pulssin välein pystysuunnassa ... 0–48 mm ... 800 pulssia minuutissa" is still true; it says nothing about label spacing.
- inquiry.json:390–411 (Tarkista 2): answer 12, tolerance 0,06, mistakes 24 and 400, hints and solution unchanged and still correct; nothing refers to 4 mm labels.
- review/shots/fy8-12-fig-14-390.png shows the new labels without overlap.
- Content hash 65587e36f7083d7a at start and end, equal to the packet.
- Earlier checks (numbers equal the Finnish source, sim model and `simState` unchanged) stand.
