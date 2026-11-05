VERDICT: PASS
CONTENT-HASH: 561ea006852fe64e

Science review of the Selkeä suomi translation of fy9-kokeellisuus (source content/fi/units/fy9-kokeellisuus/, already PASS).

Method: `check_i18n.py` (fi-easy: 0 errors); every string of unit.json, inquiry.json, exit-ticket.json and sovella/tasks.json compared to source.json (translate_kit extract) for `$…$` tokens and numbers; unit.md, teacher.md and sovella/solutions.md compared the same way, with identical ```latex blocks. The only difference is the added step numbers 1)–3) in the Ryhmän jousimittaus prompt (activities.7). Every number was recomputed in one Python call: ε = 2,29 %, k = 24,7 N/m, θ₀ = −275,1 °C, s_min = 14 m, Δρ = 0,24 g/cm³, the spring table (keskiarvo 21,8 N/m; with the 1,0 cm offset removed and the bad row left out, the fit gives ≈ 25 N/m), t = 160 s, g = (9,7 ± 0,9) m/s², the pendulum T² values and fit (k = 4,02 s²/m, g = 9,82 m/s², r ≈ 2,5 cm, l = 0,25 m gives 8,9 m/s²), the stone (2677 kg/m³ ± 78), and the bicycle (a = 4,17 m/s², μ₀ ≥ 0,425, 3,78 m/s², 0,39). All of them agree.

## Blocking
None.

## Polish
1. sovella/solutions.md, s6 d) **Annettu** keeps the source phrase "kaikissa ajoissa", but the task text (tasks.json tasks.5.parts.3.text) now says "kaikilla ajokerroilla". Use "kaikilla ajokerroilla" in both places.
2. unit.json key_concepts "mittausepävarmuus": "kuinka paljon tulos voi olla väärin" is loose. Write "kuinka paljon tulos voi poiketa oikeasta arvosta". unit.md does it better: "kuinka suuri virhe voi olla".
3. Several added plain-language glosses change no physics and are correct: "syrjäyttää eli työntää pois tieltään", "lukkiutuneet eli eivät lakanneet pyörimästä", "levosta eli liikkeelle paikaltaan", "tiivistyisi" made into "muuttuisi nesteeksi" and "Öljy ei siis kiehu". Keep them.

## Shared issues
None.
