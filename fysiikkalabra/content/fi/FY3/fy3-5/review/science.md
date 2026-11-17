VERDICT: PASS
CONTENT-HASH: 0673a9b71c836baf

## Blocking

## Polish
- `prior` still lists the gas micro-model as the retrieved prior knowledge, but the retrieval now asks about work, W = Fs. The first item (Työ W = Fs, Joule) already covers the new choice, so this is a consistency note only.

## Checked
batch delta review: the new retrieval choice `pr-mikromalli` is recomputed: W = Fs = 90 N · 0,10 m = 9,0 J, the only correct option. The distractors are wrong and their feedback right: 900 J is F/s, 90 J is the force's number, 90,1 J is F + s. The choice asks only the size of the work and does not say where the energy goes. It therefore does not give away Ennuste 1 (Bea: work raises the internal energy) or Ennuste 2 (ΔU = W in the insulated cylinder). The transfer task's numbers are now in LaTeX and its answer is unchanged: 75 N · 0,080 m − 0,60 J = 5,4 J. The new `learn` lines (objective-form) say the same as before. The furnace photo caption ("sisäenergia kasvaa" when heated) is correct. The worked-example edit is a paragraph split. lesson-answers.py agrees with my own values.
