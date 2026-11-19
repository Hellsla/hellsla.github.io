VERDICT: PASS
CONTENT-HASH: 2383749f923e783e

## Blocking
(none)

## Polish
(none)

## Checked
- Diff origin/main...HEAD (excluding review/): one line in inquiry.json, a long text field in which two paragraph breaks (\n\n) were inserted; words, maths and figures unchanged. The same change is in all three languages.
- Read the earlier Sovella visual report (en, PASS) as evidence.
- Opened review/shots: contact-1.png and fy9-lampo-stage-sovella-1280-2.png (fi, en), contact-1.png (fi-easy). Layout, maths and reading column are intact; no clipping or overflow.
- Not opened: the changed field is a long explanatory text (apparently the model / "Mallin oletukset" box, closed by default), which I did not find in an opened-state capture. Judged from the diff: the split follows the sentence boundaries, with the display formula staying in the middle paragraph, so the presentation can only improve.
