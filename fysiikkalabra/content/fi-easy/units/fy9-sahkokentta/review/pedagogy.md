VERDICT: PASS
CONTENT-HASH: 894eada2c0c82540
SCOPE: delta: new tasks s7 (Alfahiukkanen levyjen välissä) and s8 (Vihreä merkkivalo) and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- s8 d: the prompt asks "Mitä tulokset kertovat LEDistä ja Ohmin laista?", but the communication criterion (1 p) rewards explaining why an LED cannot be connected straight to a source and what the series resistor does. Add "Miksi LEDin kanssa tarvitaan etuvastus?" to the prompt, or fold the point into the concept criterion.
- s7 b: "Painovoima on niin pieni, ettei sillä ole merkitystä" is required unprompted in the scored text; justified only in Järkevyys.
- s7 c: the $v^2 = 2as$ route under "Hyväksytään myös" skips the energy point; say how it is scored.
- Intro: "Ratkaise kysytty suure symboleilla" is simple, but "symboleilla" may puzzle an easy-language reader; "kirjaimilla" or "kaavalla" is easier.

## Checked
- Read the fi-easy packet's s7 and s8 (tasks.json, solutions, answers.py lines) and the intro.
- Language level: short sentences, one idea each (the long fi sentences are split: "Kaksi suurta metallilevyä on rinnakkain tyhjiössä. Niiden välissä on ..."); terms unchanged (potentiaali, potentiaaliero, ominaiskäyrä, etuvastus, Ohmin laki), so the lesson's vocabulary still matches. Criteria are worded as in fi without losing a step.
- Fidelity: same data and numbers as fi (5,0 kV/m, 1,602·10^-19 C, 6,645·10^-27 kg, 4,0 and 2,0 cm, 6,0 V, 220 Ω, 30 mA, 5 and 20 mA); answer fields identical; rubric points sum to part points; the new d prompt in s7 ("aiemmin negatiiviselle") keeps the meaning.
- Text names no method; results rounded to two significant figures; aligned calculation rows; units neutral.
- Intro: eight tasks, matches the set. practice.py check OK. Layout captures in shots.md for the current hash; hash unchanged at the end.
