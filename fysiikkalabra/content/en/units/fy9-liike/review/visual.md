VERDICT: PASS
CONTENT-HASH: 7cc0b8b8dfcd46c3
SCOPE: delta (old-content fixes, git diff origin/main)
Checked: fy9-liike (en): rendered preview page at 390 and 1280 px with every details/solution open (DOM check: no page overflow, no KaTeX error, no clipped or scrolling display formula); captures review/shots/*stage-sovella-*, *stage-exercises-*, *teacher-*, intro and stage-selita/tarkista tiles, with sample tiles opened at readable size (aallot fi sovella-1280-5 and 390-6, liike en sovella-390-9, ympyraliike fi-easy sovella-390-8, energia fi teacher-1280-1); changed numbers and units diffed against the source for decimal comma/point and \, thin space.

1. Blocking: none.
2. Typography: changed numbers and units are LaTeX with thin space, decimal comma in fi and fi-easy, decimal point in en; aligned blocks and inline formulas fit at 390 px; no layout regressions from the changed lines.
3. Language: changed lines read naturally and consistently with the glossary terms; no wording defect found.
4. Polish: known drawing issues (kone-kuva W arrow, kalteva.webp, geo-kuva ray, kartta label, sahkokentta formula map E vs W) are known to the teacher, not re-judged here.
