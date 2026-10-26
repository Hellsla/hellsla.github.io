VERDICT: PASS
CONTENT-HASH: 710ecceebfa61815

## Blocking

## Polish
- lesson.md `## Kaava: Kaasun työ ja hyötysuhde`: the section also defines the heat pump's lämpökerroin ε, which is not a hyötysuhde. A name like "Kaasun työ, hyötysuhde ja lämpökerroin" would cover all of it. Optional.

## Checked
batch delta review: `## Kaava: Kaasun työ ja hyötysuhde` fits what the section holds (Wk = pΔV, ΔU = Q − Wk, W = Q1 − Q2, η = W/Q1, heat-pump ε). I compared the old and new text by script with fill/stroke/opacity attributes and the heading masked: the lesson.md diff is only figure recolouring (geometry, coordinates, numbers and labels identical). No prose refers to a figure colour. inquiry.json: the sim activity's text is split into text/howto/model/calc with every sentence kept word for word (only the order changed), and no other activity changed, so the model's stated limits are still there. The physics did not change.
