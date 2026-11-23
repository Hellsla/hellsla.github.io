VERDICT: PASS
CONTENT-HASH: 17b69b240046c296
SCOPE: delta md-paragraphs,numbers,reflow,typography from 8b0863e6ddb36e3d base 64d4935

## Blocking
- none

## Polish
- solutions.md fy8-4-L3-04 Kaava — `d = c/(N/t)` has no sentence saying it is the distance between photons.
- solutions.md fy8-4 Mallivastaus (double slit) — 'Se ei myöskään kulje kuulan tavoin' follows a sentence about photon collisions, so 'Se' is unclear; write 'Fotoni ei myöskään kulje...'. The added line 'Se ei voi syntyä siitä, että fotoni kulkee vain toisen raon kautta ja sen voi tietää' is awkward; write 'Raitakuvio ei synny, jos fotonin reitti on tiedossa.'

## Checked
- 8g diff: the Kaava step now lists the basic laws first (E = hf, c = f\lambda), then the derived formula, symbolic until Sijoitus; each Kaava block is an aligned list, one equation per row (the packet diff shows it flattened). A student can follow the derivation; numbers, answers and levels unchanged.
- The added closing sentences in model answers and the split Vastaus/Sijoitus paragraphs close gaps in the explanations and read clearly.
- Method: delta text in packet plus the aligned Kaava blocks read in solutions.md; no captures needed.
