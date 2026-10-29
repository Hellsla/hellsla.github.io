# Pictures and simulations

One folder per course, created by `python scripts/new_course.py <FY4>` (`/new-course FY4`); paths come from
`scripts/courses.py`, so a lesson never names another course's folder by accident.

- `pics/<course>/<file>`: pictures of the course. Lesson text refers to them as `pics/fy4/<file>`; the build
  publishes each referenced picture at the same path under `site/`.
- `sims/<course>/<name>/`: one simulation per folder (`sim.js`, its own `sim.css` and images). `meta.json`
  `"sim": true` is the lesson's own folder (`<name>` = lesson id); `"sim": "fy4-2"` reuses another one of the
  course; `python scripts/courses.py deps` lists who uses what. Published at `sims/<course>/<name>/`.
- `shared/pics/`, `shared/sims/<name>/`: only what genuinely serves several courses (`"sim": "shared/<name>"`).
- `shared/brand/`: the Ruukkilabra logos (teacher 2026-10-29), published as `site/brand/`: the arch symbol (also the favicon and
  `ruukkilabra-180.png` touch icon), the wordmark, and the wordmark with each language's subtitle (`lang/<lang>.json` `site.logo`).
  `scripts/brand_logos.py` writes the wordmarks from the symbol and Plus Jakarta Sans; edit the symbol by hand.

FY3's simulations predate these folders and stay as `sim.js` in their lesson folders (`lesson_folder_sims` in
curriculum.json), so their URLs and review hashes are unchanged.
