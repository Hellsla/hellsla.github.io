VERDICT: FAIL
CONTENT-HASH: dfb3675133290f7c

## Blocking
- [Major] #tarvitset, "Lähdejännite ja sisäinen resistanssi" (page-390-2, page-1280-2, preview/fy10-paristo.html) — visual verification incomplete: the changed item renders as plain text "Lähdejännite ja sisäinen resistanssi (FY6, luku tulossa)" with no link. The build took the `not_published` fallback ("luku tulossa") for target fy6-8, so the link, its styling and its wrapping could not be judged at 390 or 1280 px — the change under review is not visible — recapture with fy6-8 resolving as published (or confirm in the build that the link will render once fy6-8 is on the site), then re-review. If the fallback is the intended pre-publication look, the item also reads as unfinished to a student: "luku tulossa" for a chapter that exists.

## Polish
- (none; the rest of the section is unchanged: the other items, tags, spacing and the 390/1280 layout match the earlier PASS, no overflow seen)

## Checked
- page-390-1, page-390-2, page-1280-1, page-1280-2 (opening, #tarvitset at both widths). Other widths/captures not opened; diff is limited to this one item.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
