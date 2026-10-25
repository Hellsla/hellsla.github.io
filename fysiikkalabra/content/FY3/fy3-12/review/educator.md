VERDICT: FAIL
CONTENT-HASH: c4e06f33e1001537

## Blocking
1. exercises.json:99, :82, :90; lesson.md:52; meta.json prerequisites — L3-03 needs the lämpökerroin (fy3-11) and L3-01/L3-02 need Q = cmΔT and lämpökapasiteetti (fy3-6), but meta lists only fy3-5 and lesson.md never names either formula; a student with only fy3-5 cannot start L3-03. — Add `"fy3-6", "fy3-11"` to `prerequisites`, and in lesson.md:52 add a recall sentence: "Muista, että lämpömäärä on $Q = cm\Delta T$ ja että lämpöpumpun lämpökerroin on sen luovuttaman lämpötehon ja käyttämän sähkötehon suhde."
2. exercises.json:14, :22 — L1-02 (solve U) and L1-03 (solve ΔT) are rearrangements, which the CLAUDE.md rubric puts at level 2; published lessons keep level 1 forward-only. — Make them forward uses, e.g. L1-02: "Vanhan ulko-oven U-arvo on 1,2 W/(m²·K) ja pinta-ala 2,0 m². Sisällä on 21 °C ja ulkona −19 °C. Kuinka suuri lämpöteho johtuu oven läpi?" (96 W); L1-03: "Lämmityskaudella kerrostaloasunnon ulkoseinän läpi johtuu keskimäärin 210 W. Kuinka monta kilowattituntia lämpöä karkaa 30 vuorokaudessa?" (151 kWh). Update answers.py and solutions.md.

## Polish
1. lesson.md:3 — the "vaikka … yhtä paljon energiaa kuin saa" clause presupposes energy balance before it is taught and states no real paradox. — E.g. "Miksi pilvinen talviyö on lauhempi kuin kirkas, ja miksi Maan keskilämpötila on +15 °C eikä pakkasella?"
2. lesson.md:31 — the step from "maanpinta saa enemmän energiaa" to a *higher equilibrium* relies on line 6's last sentence without saying so. — Add: "Lämpimämpi pinta säteilee enemmän, joten se lämpenee vain siihen asti, että lähtevä teho taas on yhtä suuri kuin tuleva." Optionally add that sunlight is short-wave because the Sun is very hot.
3. lesson.md:114 — kWh is never defined in FY3 but is used in the example and four exercises. — Add after E = Pt: "Kun teho on kilowatteina ja aika tunteina, energia saadaan kilowattitunteina: 1 kWh = 3,6 MJ."
4. exercises.json:82 — L3-01 asks how shiny surfaces stop radiation; the lesson never says that surfaces reflect thermal radiation. — Add to lesson.md:6: "Kiiltävä tai vaalea pinta heijastaa säteilyä, tumma imee ja säteilee sitä hyvin."
5. lesson.md:52 — the ethics goal is a single assertion. — Make it concrete: "Meriin varastoitunut energia pitää lämpenemisen käynnissä vuosikymmeniä, joten nykyiset päästöt vaikuttavat ihmisiin, jotka eivät ole niitä aiheuttaneet." The L3-03 neighbour question could also ask whose emissions shrink.

## Checked
- Lint: 0 errors, 0 warnings; L2-04 albedo framing is already with the fixer (not repeated).
- Figures: two in Ydinajatus (lines 8, 33), one in Kaava (line 61), each next to its paragraph; longest paragraph 96 words.
- Example: 5 `<!-- vaihe -->` stages, bold lead-ins, symbolic first row in every display.
- No exercise repeats the example (L2-01 inverse, L2-02 cost, L2-03 difference).
- Level 2 and level 3 fit the rubric; level 3 combines two ideas with reasoning.
- Exit ticket Q3 tests the core idea (energy balance, greenhouse effect), not a detail.
- Goals covered: heat transfer modes, U-value and home energy, climate change.
- fy3-5 (energy conservation) and fy3-2 (P = W/t) are used consistently.
- All six meta glossary terms exist in glossary.json.
