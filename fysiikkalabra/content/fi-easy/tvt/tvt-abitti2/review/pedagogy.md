VERDICT: PASS
CONTENT-HASH: 16fa2a30a29a80d1

## Blocking
None. The S2 guide has the same seven steps, table, links, dates, 60 min, mistakes, gap section and sources as the Finnish guide. No step or fact is lost or added. The known gaps (formula editor, graph steps, attaching a file) are stated in the same way in both versions and in step 6.

## Polish
- Explain these words the first time, inside the sentence, as NOTES.md §12 req. 3 asks:
  - "varmuuskopioidaan" (step 5): "tallentuvat toiseen paikkaan varmuuden vuoksi".
  - "avotehtävä" (step 6): "tehtävä, johon kirjoitat oman vastauksen".
  - "oheisohjelma" (step 6 and sources).
  - "lisenssi" (step 2): "käyttölupa".
  - "asennuskoodi".
  - "symbolinen laskenta" and "vektorigrafiikka" (table): add a short gloss or an example.
- Intro: "koejärjestelmä" is not explained. Add "eli tietokoneohjelma, jolla koe tehdään".
- "Mihin tarvitset tätä": the sentence "Ohje on koottu ... Lähteet ja lukupäivä ovat ohjeen lopussa" has several ideas. Split it into two sentences.
- Step 2 ends with "Kaikkia ei tarvitse osata" and "Valitse siis yksi ohjelma ja opettele se kunnolla". The second is the clear instruction; the first is slightly repetitive and could go.
- Practice section: "Ne kuvaavat koulun Graphical Analysis Proa. Sen Abitti 2:n versio ... ei ole verrattu toisiinsa" is hard for S2 readers. Rewrite: "Ohjeet on tehty koulun Graphical Analysis Pro -versiolle. Abitti 2:n versio voi näyttää erilaiselta."
- The `[[ohje:...]]` links in the practice section are kept, which is correct.

## Checked
- Same physics and content as fi/tvt/tvt-abitti2/guide.md, compared sentence by sentence. The formula $60\,\text{min}$ is intact.
- One action per step: yes. Steps 1-7 are in a clear order, and the bold UI names (Siirry tarkastelemaan vastauksiasi, Päätä koe) are kept.
- Difficult words: "päivittyy eli muuttuu uudemmaksi" and "vastauskenttä eli kenttä, johon vastaus kirjoitetaan" are explained well. The words in Polish are not.
- Natural Finnish with whole sentences, and no childish tone.
- Uncertainty in the sources is stated openly, as in the Finnish version. This is honest and correct.
- Not run: `reviews.py hash` does not work for a guide (no lesson folder). I used the hash you supplied, 16fa2a30a29a80d1. I did not open guide.json.
