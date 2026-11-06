VERDICT: PASS
CONTENT-HASH: caaeaa93666bca57

## Blocking

## Polish

## Checked
- Round 2 (commit 4ff432a8f), checked against the text only, not renders. The correct choice's feedback is now just "Oikein. Valitse seuraavaksi perustelu, joka selittää vastauksesi.", so it gives away neither the ratio nor the reason. The ratio 24,0 s : 8,0 s = 3 moved to the correct reason's feedback, where it belongs.
- "noin" dropped from the correct choice, the answer and the solution. That is right, because the model (constant vP and vS on the whole path) gives exactly d_B/d_A = Δt_B/Δt_A = 3. There is no longer a hedge cue.
- The correct reason, shortened to "Aallot kulkevat saman matkan tasaisilla nopeuksilla, joten aikaero on verrannollinen matkaan." (about 93 characters against 85–90), is right because Δt = d(1/vS − 1/vP). It is no longer clearly the longest.
- Recomputed values unchanged: 8,4 km/s; dA ≈ 67 km, dB ≈ 2,0·10² km. Exactly one choice and one reason are correct. The solution's wording of the reason matches the option.
- answers.py is unchanged, and running it with python3 -I gives the same 16 numeric answers. The rest of the set is unchanged.
