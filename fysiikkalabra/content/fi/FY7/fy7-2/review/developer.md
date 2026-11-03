VERDICT: DONE

inquiry.json: koe-1/koe-2 velocity unit is now "Mm/s" (value 1; koe-1 intro explains 1 Mm/s = 10^6 m/s), table headers "v lopussa (Mm/s)", "F_m (fN)", "F_s (fN)" (new sim keys Fm15/Fs15; koe-2 intro and johtopaatos model use fN); koe-1 B shown as $0{,}20\,\text{T}$ through `values`; ennuste-2 says r and d = 2r; pohdi "sama vauhti" now "(nopeusvalitsimen jälkeen)"; tarkistus-4 criterion 4 rewritten.
lesson.md: "noin 0,1 %"; sentence before r-graph says it shows r while the sim shows d = 2r; figures regenerated.
figures.py: r-graph proton label off the line, aria says r not 2r; spectrometer labels "kevyempi"/"raskaampi" at the detector (radii 106/126, schematic, height 410), 2r label moved; track-sign crosses skip the dashed track.
sim.js: arrow labels avoid B marks and sit on a plate; adapter unit Mm/s; Fm15/Fs15 keys. lang/fi.json: sims.fy7-2.nopeus = "Animaation nopeus". glossary.json: massaspektrometri "samalla varauksella".
Tests unchanged. check_lesson.py all ok.
