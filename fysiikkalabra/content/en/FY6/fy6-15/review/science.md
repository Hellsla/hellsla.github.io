VERDICT: PASS
CONTENT-HASH: 13c7836cee33b3d3

## Blocking

## Polish

## Checked
- Delta 45327c18: figures.json maps "v" to "E". Both figures now show I_E: the fault current along PE in the earthing figure, and the current through the person with I_L − I_N = I_E in the RCD figure. This is physically correct: both are earth-fault currents, and the text calls both "fault current". I_E no longer clashes with I_f, the fuse's rated current, which was my earlier notation concern about I_f. The RCD alt text now names I_E.
- The earthing figure's alt text says "fault current" without the symbol. This is harmless.
- The numbers in lesson.md, inquiry.json, exit-ticket.json, exercises.json and solutions.md were compared by script with the Finnish and are identical (multisets match).
- The prose was read against the Finnish for the safety statements, and each one survives:
  - fuse vs person (protects only together with protective earthing);
  - RCD principle, the 30 mA limit, and the L–N contact it misses;
  - colours only in new installations, and never trusting a colour;
  - class III at 50 V AC or 120 V DC;
  - the shoe conditions and "shoes must not be regarded as protection";
  - IEC 60479-1 thresholds with the caveats;
  - step voltage (short steps, feet together) and 112;
  - the Tukes register and the layperson list.
- The worked example (19.6 A, about 20 A, trips only if the load continues long enough) and the misconception text match the Finnish.
