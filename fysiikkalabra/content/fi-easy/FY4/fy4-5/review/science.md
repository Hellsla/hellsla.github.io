VERDICT: PASS
CONTENT-HASH: 599fe97ac3218029

## Blocking
- none

## Polish
- scripts/check_i18n.py does not list `detail` (a rubric criterion's specifics) in TEXT_KEYS, so it reports the simplified check-3 criteria details as errors; the translation is right and the checker needs `detail` added (outside this review's scope; the content hash does not change when it is fixed).

## Checked
- Checked (full review against the reviewed Finnish): every number, formula and figure of lesson.md, inquiry.json and exit-ticket.json unchanged (check_i18n, figures.py --lang fi-easy --check); the added explanations (vektorisumma, kohtisuora, komponentti, tukivoima, noste, jännitysvoima) are correct. Fixed: "Kitkavoima ... estää liukumista" now "vastustaa liukumista pinnan suhteen" (kinetic friction does not prevent sliding); "Pitkä nuoli tarkoittaa suurta voimaa" now comparative like the Finnish; the drag condition keeps "ja sen oletukset". The elevator options keep empty texts and the descriptions list only arrow lengths; buoyancy keeps F_noste in text and figure.
