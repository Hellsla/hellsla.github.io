VERDICT: PASS
CONTENT-HASH: 364d8e22b9c0ae39

## Blocking

None.

## Polish

- Open item for Lauri: the Analysointi steps 1–3 cannot name menus because frame-by-frame marking in GA Pro is unverified (it may live in Vernier Video Analysis). The guide handles this honestly; once the tool is decided, give steps 1–3 concrete menu names like the other guides.
- Move "(opettaja kertoo, kumpaa käytetään: Graphical Analysis Pro vai Vernier Video Analysis)" from step 3 to step 1, where the student first opens "koulun videoanalyysiohjelma".
- Ilman analyysiohjelmaa: "Laske, monenko kuvan päästä tapahtuma on edellisestä tapahtumasta" is clumsy; e.g. "Laske, montako kuvaa kahden tapahtuman välillä on".
- Mistake "Ohjelma käytti väärää kuvataajuutta": "monikertaisia" → "moninkertaisia".
- Ohjelmakohtaisia vinkkejä, Kuvataajuus repeats Kuvaaminen step 6 and Analysointi step 1; one mention is enough.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. No invented GA menu paths; the video-sync tip is a verified Pro feature; CSV transfer to GA Pro is verified.
- Filming steps are concrete, each with a reason (tripod, perpendicular, distance, scale in the plane, light, true frame rate). Figure (top view, scale in the right and wrong place) supports step 4.
- Goals (film usable video; get position vs time by program or by counting frames) match both parts; checklist covers filming, scale, frame rate and consistent marking.
- Frame-count method: $t = \tfrac{N}{f}$ displayed with symbols named, example 36 : 240 1/s = 0,15 s, timing uncertainty one frame.
- Mistakes are real ones (camera moved, scale off-plane, wrong fps, inconsistent point, blur), each with symptom and fix; the off-plane scale mistake rightly notes the fit will not reveal it.
- Cross-links to kuvaaja, suoran-sovitus, nopeus-datasta sensible; investigation titles exist. No Tracker leftovers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- No screenshot in this guide (not needed); guides.py check: ok. Rendered preview checked: no leftover markdown or {{ga:}} markers.
- The grammar fix is correct Finnish. Nothing else changed.

## Delta 5 (2026-10-31)

- Analysointi now names Vernier Video Analysis for steps 1–3 and GA Pro for step 4; *opettaja kertoo, kumpaa* is gone; no menu names invented; the GA Pro video-sync tip in *Ohjelmakohtaisia vinkkejä* is a separate sensor-sync feature and does not contradict. Matches fy10-muotokerroin.
- Polish: step 4 *Siirrä Video Analysisista* — the clipped name inflects awkwardly; prefer *Siirrä Video Analysis -sovelluksesta*. Step 1 mixes *sovellus* and *ohjelma* (*Tarkista ensin, että ohjelma …*) — *sovellus* throughout would be tidier. Step 3 repeats the app name already given in step 1 (harmless).
