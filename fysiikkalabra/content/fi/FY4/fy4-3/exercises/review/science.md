VERDICT: FAIL
CONTENT-HASH: 9afe1ad795180985

## Blocking
- solutions.md:265–279 (L3-04, both `voimakuvio` blocks; renderer scripts/fbdspec.py `draw`) — A. The forward arrows are cut off: in the cart diagram $\overline{T}$ (450 N) and in the horse diagram $\overline{F}_\text{t}$ (480 N) run from x = 342 to a head at x = 642, but the figure's viewBox is 0–600, so both arrows end in a bare line at the right edge with no head (checked with `fbdspec.py show` and the SVG coordinates). The two forces that drive the paradox show no direction, so the diagram cannot be checked against "eteenpäin" in the text. — Fix the crop in `draw` so that every arrow head and label lies inside the viewBox (or lower the scale for a one-body figure whose horizontal forces are this long), then re-render and confirm all six heads are visible.

## Polish
- solutions.md:265–279 (L3-04) — the diagrams show only horizontal forces; the first one says `pinta 0` but draws no surface, and the horse stands on a road with no normal force. The slot says "ei vielä täydellisiä voimakuvioita", so this is not an error, but write in the Voimakuvio step "pystysuorat voimat (paino ja tien tukivoima) kumoavat toisensa eikä niitä piirretä", as L1-04 does.
- solutions.md:227 (L1-08) — the moved sentence reads correctly and its physics is right (the rope pulls the child back towards the sled; the child's force on the rope is not in the child's diagram). "eli lasta vastaan" is still unclear (carried); "(köysi vetää lasta taaksepäin)" is clearer.
- Carried from the previous round: L3-05 "kärry vetää köyttä ja oppilasta" (solutions.md:290, 296); L2-06 b) asks for 6,0 s against a 0–5 s table; L3-04 c) does not say why the cart starts.

## Checked
- Full review: I recomputed every numeric answer in one script (18, 850, 90, 240, 6,4, 13, 65, 830, 8,9, 0,27, 0,60, 1,9, 38, 4,8, 3,0, 480, 3,4). All agree with answers.py and exercises.json.
- L3-04 diagram physics: cart T 450 forward against F_r 410 + F_k 40; horse F_t 480 forward (friction at the hooves, from the bottom corner) against T 450 + F_h 30. Each sum is zero, matching a = 0 and the Kaava step. The third-law pair T is on two different diagrams.
- The developer's working-tree edit (uncommitted, in this hash) fixes the symbols. The rolling resistance is now F_r, which no longer renders as "ilmanvastus" in the alt text and matches the F_r of L1-04. The two bodies are now separate diagrams, so neither one's arrows run into the other's box.
- MC L1-06, L1-07, L2-07: exactly one correct option each.
- The other 13 drawn diagrams match their texts and sum to zero along a.
- The hash at the end is 9afe1ad795180985. It changed during the review because of the edit above, and this report judges that version.
