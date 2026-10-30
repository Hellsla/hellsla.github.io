# Ruukkilabra portal architecture

The durable summary of the teacher's master brief (2026-10-30). Short on purpose: read this, not the whole brief,
before working on portal structure. What is **implemented** is marked as such; the rest is the agreed design for
later phases, each its own reviewed pull request.

## Identity
Ruukkilabra is the teacher's independent open resource platform, used at Kiviruukin lukio but not the school's
website. Keep its own identity (forest green, terracotta, Fraunces + Plus Jakarta Sans, the arch logo). Motto
suggestion: *Tutki. Oivalla. Toteuta.* Folder and URL stay `fysiikkalabra/site/`. Physics only for now; new
student-facing content is Finnish first, without new translations until the teacher asks.

## Four main sections (long term)
| Section | What | State |
|---|---|---|
| A. Oppimateriaalit | national modules FY1–FY8 (LOPS 2019), `curriculum.json`, inquiry lessons | implemented |
| B. Lukiokohtaiset opintojaksot | school-specific optional courses: FY10 first, later e.g. Makerspace 1–2 | **registry + landing page implemented** |
| C. Ahjo Makerspace | open maker resources and, apart from them, Ahjo-specific local information | planned (phase G) |
| D. Opettajalle | public teacher guidance; nothing confidential in the public repo or site | planned |

Simulations stay inside the lessons that use them; Käsitetakomo (`../kasitetakomo.html`) is linked contextually,
not rebuilt. It reads no URL parameters today, so a topic deep link needs a small filter by `?aihe=` (phase H).

## National vs school-specific courses (implemented)
- `curriculum.json` holds only the national modules, their LOPS goals and lesson slots; `/new-course` validates
  those against `docs/lops2019/`. A local course never enters it and never borrows national goals.
- `local-courses.json` is the registry of school-specific courses (`scripts/local_courses.py` documents the
  fields): title, subtitle, school, status, description, goals, themes, ways of working, report sections and
  `prepare` (published chapters to study first, by lesson id). Finnish is the source; a translation would be
  `content/<lang>/local-courses.json`, and a course appears only in languages that have it (the others get a note
  at their front page's `#unavailable-<CODE>`, where the language menu points).
- `build.py` renders each course to `site/<CODE>.html` (same `page.html` template and module-page parts) and a row
  in the front page section *Lukiokohtaiset opintojaksot*, after the national modules and Tulossa, before the sample
  lesson. No code names FY10; a second course is a second entry in the registry.
- `status: "planning"` = the teacher's working version: the page says so and shows no credits, assessment or
  official goals. Add a status (and its `site.local_status_<status>` texts) only when a course needs it.
- Validation (build and `test_home.py`, in CI): codes unique and apart from national ones, required texts, known
  status, `prepare` ids are curriculum lessons and are linked only where published in that language.

## Shared resources (design for phases C–G)
- **One canonical resource, many pathways.** A course is a pathway through reusable resources; never copy a
  lesson, investigation, project or tutorial into a second course.
- Resource types: physics lesson (exists), experimental investigation, experimental-method unit, TVT skills guide,
  makerspace project, teacher resource, school-specific course (exists). Stable ids such as `fy3-6`,
  `fy10-jousivakio`, `tvt-ga-suoran-sovitus` (illustrative; extend `courses.py` minimally when a new id form arrives).
- Minimal metadata, only what real resources need: id, title, type, description, objectives, related modules,
  course memberships, prerequisites, F/E levels, support modes, equipment, safety, status, canonical URL/anchor.
- **Prerequisites** in three kinds (physics knowledge, experimental skills, TVT skills), each `essential`,
  `helpful` or `extension`, with a short reason and optionally the phase where it is needed. Shown as
  *Tässä työssä tarvitset näitä tietoja ja taitoja*; plus just-in-time *Tarvitsetko apua? →* links at the step that
  needs them. Concept explanations and software instructions stay separate resources, linked to each other.
- **Links from metadata, not hand-copied HTML.** A resolver checks that targets and anchors exist and are
  published, generates relative URLs and the reverse links (*Sovella kokeellisesti* on a theory chapter), and fails
  on duplicate ids. A reverse link never changes a lesson's reviewed content or hash. Unpublished target: no link,
  a short correct explanation and the missing dependency named.
- **TVT skills guides** are an internal category, not a homepage section. Each records software, version/edition,
  date verified, outcome, prerequisites, steps, common mistakes, related investigations. Instructions only after
  checking current official documentation; no invented menus or features. First: Vernier Graphical Analysis linear fit.
- **Ahjo projects**: Haaste → Suunnittele → Rakenna → Testaa ja kehitä → Dokumentoi ja arvioi; open tutorials apart
  from machine-specific local procedures, which need verified devices and never replace local training.

## Publication and review
The existing rule stays: a page is public only when its reviews pass for its current content hash; drafts go to
`preview/`. New resource types get an equivalent gate before any of them is published. A course landing page in
`planning` contains no teaching content and is labelled as a plan. Links to a national lesson never re-review it.
Confidential material (answer keys, student data, restricted assessment) never goes into served files or this
public repository: a hidden element is not access control.
