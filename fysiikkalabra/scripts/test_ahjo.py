"""Ahjo Makerspace pages (teacher 2026-11-08, scripts/ahjo.py) in the built site/: the three pages, the two course pages (Ahjo 1, Ahjo 2) and
every guide with a page (a draft marked "Luonnos" first, the twelve sections, its figures drawn) and every lesson's own page
(teacher 2026-11-09: start now first, levels, materials, safety, previous/next) in every language,
the original logo on each, every internal link resolving to a built file or an anchor on it, no equipment the school will
not have, the safety page marked as a draft until a topic is approved, the front page's row, and in a browser no
sideways scroll at 360, 768 and 1280 px and a keyboard path through the section's navigation.

  python scripts/test_ahjo.py"""
import os, re, sys, pathlib, subprocess, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import ahjo, i18n

SITE = ROOT / "site"
fails = []
def expect(name, ok, got=None):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  ({got!r})"[:300]))
    if not ok: fails.append(name)


for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    d = ahjo.load(lang)
    guides = ahjo.ready_guides(d)
    for name in (ahjo.PAGE, ahjo.BANK, ahjo.SAFETY, ahjo.PROJECTS) + tuple(ahjo.course_page(c["code"]) for c in d["courses"]) + tuple(f"{g}.html" for g in guides) \
            + tuple(ahjo.lesson_page(c["code"], i) for c in d["courses"] for i in range(1, len(c.get("lessons", [])) + 1)):
        f = out / name
        expect(f"{lang} {name}: built", f.is_file())
        if not f.is_file(): continue
        html = f.read_text()
        main = html[html.find("<main"):html.find("</main>")]
        head = html[:html.find("</head>")]
        expect(f"{lang} {name}: Ahjo's mark as the tab icon, not Ruukkilabra's", "ruukkilabra-32.png" not in head and "ruukkilabra-symboli.svg" not in head
               and all(re.search(rf'href="(?:\.\./)*{re.escape(i)}"', head) and (SITE / i).is_file() for i in ahjo.TAB_ICONS.values()))
        lesson = re.search(r"-tunti-\d+\.html$", name) is not None   # a lesson's page has Ahjo's mark in its top bar instead
        expect(f"{lang} {name}: the original logo with its name as alt", lesson and 'class="ahjo-ltop-home"' in main and 'alt="' in main or re.search(r'<img class="ahjo-logo[^"]*" src="(?:\.\./)?brand/ahjo-makerspace-logo\.svg" alt="[^"]+"', main) is not None)
        expect(f"{lang} {name}: the section's navigation marks this page", lesson or (f'aria-current="page"' in main and 'class="ahjo-nav"' in main))
        expect(f"{lang} {name}: no laser cutter or CNC anywhere", not ahjo.FORBIDDEN.search(re.sub(r"<[^>]+>", " ", main)))
        bad = []
        for href in re.findall(r'href="([^"]+)"', main):
            if re.match(r"[a-z]+:", href):      # Ahjo links only inside Ruukkilabra, but for a project card's inspiration (a known site)
                ext = re.match(r"https://([^/]+)/", href)
                official = name[:-5] in guides and ext and ext.group(1) in ahjo.OFFICIAL_HOSTS   # a guide's sources: the authority's rules, the maker's documents (Dronelabra, 2026-11-12)
                if not (name == ahjo.PROJECTS and ext and ext.group(1) in ahjo.SOURCE_HOSTS) and not official: bad.append(href)
                continue
            path, _, frag = href.partition("#"); path = path.split("?")[0]   # a guide opened from a lesson: ?tunti=... (ahjo.js)
            target = (out / path).resolve() if path else f
            if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text()): bad.append(href)
        expect(f"{lang} {name}: every link resolves to a built page (and its anchor)", not bad, bad)
    pr = (out / ahjo.PROJECTS).read_text() if (out / ahjo.PROJECTS).is_file() else ""
    cards = re.findall(r'<article class="ahjo-proj( approved)?" id="([^"]+)".*?</article>', pr, re.S)
    expect(f"{lang}: the project bank shows every card once", [c[1] for c in cards] == [p["id"] for p in sorted(d["projects"], key=lambda p: p["status"] != "hyvaksytty")], [c[1] for c in cards])
    expect(f"{lang}: a card is approved only where the teacher marked it (approved_by, date)",
           all(bool(a) == (p["status"] == "hyvaksytty" and bool(p.get("approved_by"))) for a, pid in cards for p in d["projects"] if p["id"] == pid))
    card = {pid: x for x, pid in ((mm.group(0), mm.group(1)) for mm in re.finditer(r'<article class="ahjo-proj[^"]*" id="([^"]+)".*?</article>', pr, re.S))}
    expect(f"{lang}: every card has its status badge and a measure of success, and an inspiration link marked external when a page inspired it (a project of our own has none, 2026-11-12)",
           all(re.search(rf'ahjo-badge.*?{re.escape(ahjo.esc(d["ui"]["proj_success"]))}', card.get(p["id"], ""), re.S)
               and bool(p.get("inspiration")) == bool(re.search(r'rel="external noopener".*?ahjo-ext', card.get(p["id"], ""), re.S)) for p in d["projects"]))
    drone = [p for p in d["projects"] if p["id"].startswith("drone-")]
    expect(f"{lang}: Dronelabra's eight project cards each show steps, safety limits and what the project needs",
           len(drone) == 8 and all(p.get("steps") and p.get("safety") and p.get("need") and ahjo.esc(p["safety"]) in card.get(p["id"], "") and ahjo.esc(d["ui"]["proj_steps"]) in card.get(p["id"], "")
                                   and ahjo.esc(d["ui"]["lesson_status"][p["need"]]) in card.get(p["id"], "") for p in drone), len(drone))
    expect(f"{lang}: the project page says the cards are proposals", ahjo.esc(d["ui"]["projects_note"]) in pr)
    expect(f"{lang}: a project card shows its picture, name, line, level and length first and opens for the rest (teacher 2026-11-09)",
           all(re.search(rf'<article class="ahjo-proj[^"]*" id="{p["id"]}"[^>]* data-level="{p["level"]}"><div class="ahjo-pcard-art"><svg.*?<h3[^>]*>{re.escape(ahjo.esc(p["title"]))}</h3>'
                         rf'.*?class="ahjo-proj-sum">{re.escape(ahjo.esc(p["summary"]))}</p><p class="ahjo-proj-meta">.*?<details class="ahjo-open"><summary>.*?<dl class="ahjo-proj-dl">.*?</dl></details></article>', pr, re.S)
               for p in d["projects"]))
    expect(f"{lang}: the projects can be filtered by level (hidden until the script runs)", re.search(r'<div class="ahjo-filter" data-key="level"[^>]*hidden>', pr) is not None)
    bank = (out / ahjo.BANK).read_text() if (out / ahjo.BANK).is_file() else ""
    chal = re.findall(r'<article class="ahjo-proj ahjo-chal" id="([^"]+)".*?</article>', bank, re.S)
    expect(f"{lang}: the bank shows every small challenge once (10–15, teacher 2026-11-08), each with its three levels", 10 <= len(chal) <= 15
           and sorted(chal) == sorted(x["id"] for x in d.get("challenges", [])) and bank.count('class="ahjo-levels ahjo-chal-levels"') == len(chal), chal)
    expect(f"{lang}: the bank jumps to every topic, and the small challenges can be filtered by time",
           all(f'<a href="#{c["id"]}">' in bank for c in d["categories"]) and re.search(r'<div class="ahjo-filter" data-key="time"[^>]*hidden>', bank) is not None
           and all(re.search(rf'id="{x["id"]}"[^>]* data-time="{"short" if x["minutes"] <= 20 else "long"}"', bank) for x in d.get("challenges", [])))
    guided = [x for x in d.get("challenges", []) if x.get("guide")]
    expect(f"{lang}: the three small challenges with a full guide (teacher 2026-11-08) link to it from their card", len(guided) == 3
           and all(re.search(rf'id="{x["id"]}".*?class="ahjo-chal-guide"><a href="{x["guide"]}.html"', bank, re.S) and (out / f'{x["guide"]}.html').is_file() for x in guided), [x["id"] for x in guided])
    expect(f"{lang}: each small challenge is linked from its Ahjo 1 lesson page", all(f'href="{ahjo.BANK}#{x["id"]}"' in ((out / ahjo.lesson_page("AHJO1", x["lesson"])).read_text()
           if (out / ahjo.lesson_page("AHJO1", x["lesson"])).is_file() else "") for x in d.get("challenges", [])))
    for g in guides:
        r = next(r for r in d["resources"] if r.get("id") == g)
        f = out / f"{g}.html"; html = f.read_text() if f.is_file() else ""
        art = re.search(r'<article class="ahjo-guide">(.*?)</article>', html, re.S)
        heads = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", art.group(1))] if art else []
        expect(f"{lang} {g}: the quick start, Learn more and the twelve guide sections in order", heads == [d["ui"]["guide_quick"], d["ui"]["guide_more"]] + d["ui"]["guide_sections"], heads)
        quick = re.search(r'<section class="ahjo-quick".*?</section>', art.group(1), re.S) if art else None
        expect(f"{lang} {g}: the quick start comes first, with try, modify and challenge yourself", quick is not None and art.group(1).startswith('<section class="ahjo-quick"')
               and [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h3[^>]*>(.*?)</h3>", quick.group(0))] == d["ui"]["lesson_levels"])
        expect(f"{lang} {g}: a draft says so before the guide, and the bank links it with its badge",
               r["status"] != "draft" or (html.find('class="ahjo-draft"') != -1 and html.find('class="ahjo-draft"') < html.find('class="ahjo-guide"')
                                         and re.search(rf'href="{g}\.html".*?{re.escape(ahjo.esc(d["ui"]["res_draft"]))}', bank, re.S) is not None))
        placeholders = len(ahjo.FIG_REF.findall(ahjo.guide_file(g, lang).read_text()))
        expect(f"{lang} {g}: every figure drawn ({placeholders})", art is not None and art.group(1).count('class="fig ahjo-fig"><svg') == placeholders and not ahjo.FIG_REF.search(art.group(1)))
    safety = (out / ahjo.SAFETY).read_text() if (out / ahjo.SAFETY).is_file() else ""
    approved = any(s.get("status") == "hyvaksytty" for s in d["safety"])
    expect(f"{lang}: the safety page is marked as a draft while nothing is approved", approved or ('class="ahjo-draft"' in safety and ahjo.esc(d["ui"]["safety_draft_note"].split(".")[0]) in safety))
    expect(f"{lang}: every safety topic is listed", all(f'id="{s["id"]}"' in safety for s in d["safety"]))
    start = (out / ahjo.PAGE).read_text() if (out / ahjo.PAGE).is_file() else ""
    expect(f"{lang}: the equipment heading follows equipment_status", ahjo.esc(d["ui"]["equipment_h_" + d["equipment_status"]]) in start)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 on the start page", all(f'id="{c["code"].lower()}"' in start for c in d["courses"]))
    for c in d["courses"]:
        card = re.search(rf'<article class="ahjo-course" id="{c["code"].lower()}".*?</article>', start, re.S)
        expect(f"{lang} {c['code']}: the start page's card links its own course page", card is not None and f'href="{ahjo.course_page(c["code"])}"' in card.group(0))
        cp = (out / ahjo.course_page(c["code"])).read_text() if (out / ahjo.course_page(c["code"])).is_file() else ""
        m = cp[cp.find("<main"):cp.find("</main>")]
        u = d["ui"]; ls = c.get("lessons", []); st = c.get("start")
        # the course page for the student (teacher 2026-11-09): the banner says what you get to do and has one button to the first task
        hd = m[m.find('<header class="ahjo-hero'):m.find("</header>", m.find('<header class="ahjo-hero'))]
        cta = re.search(r'<a class="ahjo-cta" href="([^"]+)">(.*?)</a>', hd, re.S)
        first = "#aloitushaaste" if st else ahjo.lesson_page(c["code"], 1)
        expect(f"{lang} {c['code']}: the banner has the course's logo, a one-sentence pitch and one button to the first task ({first})",
               'class="ahjo-logo ahjo-course-logo"' in hd and ahjo.esc(c["pitch"]) in hd and cta is not None and cta.group(1) == first
               and (not st or ahjo.esc(st["title"]) in cta.group(2)), cta.group(1) if cta else None)
        lessons_h = [h for h in re.findall(r'href="([a-z0-9-]+-tunti-\d+\.html)"', m)]
        order = list(dict.fromkeys(lessons_h))
        expect(f"{lang} {c['code']}: every lesson opens its own page, in order", order[:16] == [ahjo.lesson_page(c["code"], i) for i in range(1, 17)] and len(ls) == 16, order[:5])
        expect(f"{lang} {c['code']}: the old lesson anchors (#tunti-N) and the back links' anchors (#kortti-N) are on the page",
               all(f'id="tunti-{i}"' in m and f'id="kortti-{i}"' in m for i in range(1, 17)))
        expect(f"{lang} {c['code']}: no lesson's levels, start or materials on the course page (they are on the lesson's page)",
               'class="ahjo-steps"' not in m and 'class="ahjo-levels"' not in m and not any(l.get("start") and ahjo.esc(l["start"]) in m for l in ls))
        if c["code"] == "AHJO1":
            units = re.findall(r'<section class="ahjo-unit" id="kokonaisuus-(\d)".*?</section>', m, re.S)
            cards = re.findall(r'<a class="ahjo-lcard" id="kortti-(\d+)" href="([^"]+)">(.*?)</a>', m, re.S)
            expect(f"{lang} AHJO1: the 16 lessons in five parts ({len(units)}), each a card with its number, picture, what you make and a link",
                   len(units) == len(c["units"]) == 5 and len(cards) == 16 and all('class="ahjo-art"' in x and 'class="ahjo-lcard-t"' in x and 'class="ahjo-lcard-x"' in x for _, _, x in cards)
                   and [int(n) for n, _, _ in cards] == list(range(1, 17)), len(cards))
            expect(f"{lang} AHJO1: each part names its lessons (1–2, 3–6, 7–11, 12–13, 14–16)", [x["lessons"] for x in c["units"]] == [[1, 2], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13], [14, 15, 16]])
        elif c["code"] == "DRONELABRA":   # Ahjo's third course (teacher 2026-11-12): the same cards in parts as Ahjo 1
            cards = re.findall(r'<a class="ahjo-lcard" id="kortti-(\d+)" href="([^"]+)">(.*?)</a>', m, re.S)
            expect(f"{lang} DRONELABRA: the 16 lessons in five parts, each a card with a picture",
                   len(c["units"]) == 5 and m.count('<section class="ahjo-unit"') == 5 and len(cards) == 16 and all('class="ahjo-art"' in x for _, _, x in cards), len(cards))
            expect(f"{lang} DRONELABRA: every lesson says what it needs beyond the present equipment, what goes into the diary and the teacher's timing and preparation",
                   all(l.get("status") in u["lesson_status"] and l.get("diary") and l.get("teacher") for l in ls)
                   and all(ahjo.esc(u["lesson_status"][l["status"]]) in (out / ahjo.lesson_page("DRONELABRA", i)).read_text() and ahjo.esc(l["teacher"]["prep"]) in (out / ahjo.lesson_page("DRONELABRA", i)).read_text() for i, l in enumerate(ls, 1)))
            fly = [l for l in ls if any(x in l.get("safety", []) for x in ("drone-lentoalue", "drone-fpv"))]
            expect(f"{lang} DRONELABRA: every lesson with flying needs the teacher's safety approval and has something to do while waiting or a peer task",
                   len(fly) >= 8 and all(l["status"] == "hyvaksynta" and l.get("safety_note") and (l.get("wait") or l.get("peer")) for l in fly), len(fly))
        else:
            path = re.search(r'<ol class="ahjo-path">(.*)</ol>', m, re.S)
            steps = re.findall(r'<li class="ahjo-path-step">', m)
            hand = [l["milestone"] for l in ls if l.get("milestone")]
            expect(f"{lang} AHJO2: the project path in seven stages with the lessons under them and the five hand-ins marked",
                   len(steps) == len(c["units"]) == 7 and path is not None and len(hand) == 5 and path.group(1).count('class="ahjo-path-m"') == 5
                   and all(ahjo.esc(h) in path.group(1) for h in hand), len(steps))
            expect(f"{lang} AHJO2: the opening challenge with all its steps on the course page and on lesson 1 (teacher 2026-11-08)",
                   st is not None and 'id="aloitushaaste"' in m and all(ahjo.esc(x) in m for x in st["steps"])
                   and 'id="aloitushaaste-tunti"' in (out / ahjo.lesson_page("AHJO2", 1)).read_text())
            sn = c.get("snacks")
            expect(f"{lang} AHJO2: the optional maker snacks follow the path, and the own pace is said with it (teacher 2026-11-08)",
                   sn and c.get("flex") and 'id="maker-valipalat"' in m and m.find('id="oppitunnit"') < m.find('id="maker-valipalat"')
                   and all(ahjo.esc(x["title"]) in m for x in sn["items"]) and ahjo.esc(c["flex"]) in m)
        about = re.search(r'<details class="ahjo-about" id="opintojaksosta">(.*?)</details>', m, re.S)
        ab = about.group(1) if about else ""
        expect(f"{lang} {c['code']}: the goals, the topics and the optional deepening are folded at the end of the page",
               about is not None and m.find('id="oppitunnit"') < m.find('id="opintojaksosta"') and (not c.get("goals") or 'id="tavoitteet"' in ab)
               and all(ahjo.esc(t) in ab for t in c["topics"]) and bool(c.get("deepening")) == ('id="syventavat"' in ab))
        expect(f"{lang} {c['code']}: the Makerspace licence only where the teacher said so (Ahjo 1), with its parts and its status (still being prepared)",
               bool(c.get("license")) == ('id="ajokortti"' in ab) and (not c.get("license") or (all(ahjo.esc(t) in ab for t, _ in u["license_parts"]) and ahjo.esc(u["license_status"]) in ab)))
        expect(f"{lang} {c['code']}: the lesson structure A–E is in the folded details where the lessons have levels",
               not any(l.get("levels") for l in ls) or ('id="nain-edetaan"' in ab and 'type="A"' in ab and ahjo.esc(u["approach_note"]) in ab))
        expect(f"{lang} {c['code']}: what is assessed is in the folded details (teacher 2026-11-09)",
               'id="arviointi"' in ab and all(ahjo.esc(x) in ab for x in c["assessment"]["items"]) and ahjo.esc(c["assessment"]["note"]) in ab)
        expect(f"{lang} {c['code']}: the licence's skills checklist only on Ahjo 1", bool(c.get("license")) == ('class="ahjo-check"' in ab)
               and (not c.get("license") or all(ahjo.esc(x) in ab for x in u["license_check"])))
        fin = c.get("final")
        nfin = next((i for i, l in enumerate(ls, 1) if l.get("final")), 14)   # Ahjo 1: lesson 14; Dronelabra: its last lesson
        l14 = (out / ahjo.lesson_page(c["code"], nfin)).read_text() if (out / ahjo.lesson_page(c["code"], nfin)).is_file() else ""
        expect(f"{lang} {c['code']}: the mini project options are on lesson 14's page (teacher 2026-11-08)",
               not fin or ('id="miniprojekti"' in l14 and all(ahjo.esc(t) in l14 for t, _ in fin["options"])))
        expect(f"{lang} {c['code']}: the course page reaches Ahjo's materials, projects and safety by the section's navigation, not by big cards",
               all(f'href="{h}"' in m[m.find('class="ahjo-nav"'):m.find("</nav>", m.find('class="ahjo-nav"'))] for h in (ahjo.BANK, ahjo.PROJECTS, ahjo.SAFETY))
               and 'class="ahjo-sec ahjo-shared"' not in m and 'ahjo-safety-teaser' not in m)
        # each lesson's own page (teacher 2026-11-09)
        for i, l in enumerate(ls, 1):
            f = out / ahjo.lesson_page(c["code"], i)
            h = f.read_text() if f.is_file() else ""
            lm = h[h.find("<main"):h.find("</main>")]
            tag = f"{lang} {f.name}"
            body = lm[lm.find('class="ahjo-lmain"'):]
            expect(f"{tag}: built, with the lesson's title, picture and its number of 16", f.is_file() and f"<h1>{ahjo.esc(l.get('make') or l['title'])}</h1>" in lm
                   and 'class="ahjo-lhead-art"><svg' in lm and ahjo.esc(u["lesson_of"].replace("{n}", str(i)).replace("{m}", "16")) in lm)
            now = re.search(r'<section class="ahjo-now".*?</section>', body, re.S)
            start_first = body.find('class="ahjo-now"') == min(x for x in (body.find('class="ahjo-now"'), body.find('class="ahjo-steps"'), body.find('class="ahjo-lsec ahjo-done"')) if x >= 0)
            if l.get("levels"):
                expect(f"{tag}: 'Aloita heti' first, then the three levels and what you made at the basic level and the optional challenge",
                       now is not None and ahjo.esc(l["start"]) in now.group(0) and start_first and body.count('class="ahjo-level-n"') == 3
                       and all(ahjo.esc(l["levels"][k]) in body for k in ("try", "modify", "challenge")) and ahjo.esc(l["output"]) in body
                       and (not l.get("output_plus") or 'class="ahjo-done-row ahjo-done-plus"' in body))
            else:
                expect(f"{tag}: what the project does now, the next task first, what to save and the hand-in",
                       ahjo.esc(l["text"]) in lm and now is not None and ahjo.esc(l["example"]) in now.group(0) and (i == 1 or start_first)
                       and ahjo.esc(l["output"]) in body and (not l.get("milestone") or ahjo.esc(l["milestone"]) in body)
                       and "ahjo-projektipaivakirja.html" in lm)
            expect(f"{tag}: what you need, and the lesson's safety topics linked with their status still being prepared",
                   all(ahjo.esc(x) in lm for x in l["needs"]) and all(f'href="{ahjo.SAFETY}#{s}"' in lm for s in l.get("safety", []))
                   and (not l.get("safety") or ahjo.esc(u["lesson_safety_note"]) in lm) and (l.get("safety") or l.get("safety_note") or ahjo.esc(u["lesson_safety_none"]) in lm))
            expect(f"{tag}: the lesson's own safety note is shown, and 'no devices' only where the lesson has neither topics nor a note (teacher 2026-11-09)",
                   (not l.get("safety_note") or f'<p class="ahjo-lside-own">{ahjo.esc(l["safety_note"])}</p>' in lm)
                   and ((ahjo.esc(u["lesson_safety_none"]) in lm) == (not l.get("safety") and not l.get("safety_note"))))
            peer = re.search(r'<section class="ahjo-lsec ahjo-peer".*?</section>', lm, re.S)
            expect(f"{tag}: the together part (peers) is shown where the lesson has one, and it is not a hand-in",
                   bool(peer) == bool(l.get("peer")) and (not peer or (ahjo.esc(l["peer"]) in peer.group(0) and "ahjo-milestone" not in peer.group(0)
                                                                      and not (l.get("milestone") and ahjo.esc(l["milestone"]) in peer.group(0)))))
            sts = [x for x in d.get("starters", []) if x["id"] in l.get("starters", [])]
            expect(f"{tag}: its starter files are linked with their note (untested, the teacher prints or tries them first)",
                   all(re.search(rf'href="(?:\.\./)?{ahjo.STARTERS_PUB}/{re.escape(x["file"])}" download', lm) and ahjo.esc(x["note"]) in lm and (SITE / ahjo.STARTERS_PUB / x["file"]).is_file() for x in sts))
            hd = lm[lm.find('<header class="ahjo-lhead"'):lm.find("</header>", lm.find('<header class="ahjo-lhead"'))]
            expect(f"{tag}: the goal is in the header, so the work still starts first (teacher 2026-11-09)", f'{ahjo.esc(l["goal"])}</p>' in hd)
            expect(f"{tag}: 'If you have to wait' where the lesson has one", bool(l.get("wait")) == ('class="ahjo-lsec ahjo-wait"' in lm) and (not l.get("wait") or ahjo.esc(l["wait"]) in lm))
            expect(f"{tag}: a hand-in asks for each member's own part (teacher 2026-11-09)", not l.get("milestone") or ahjo.esc(u["lesson_own"]) in lm)
            if c["code"] == "AHJO2":
                expect(f"{tag}: says that the lesson guides the project and does not bind every group (teacher 2026-11-09)", ahjo.esc(u["lesson_pace"]) in lm)
            pager = re.search(r'<nav class="ahjo-pager".*?</nav>', lm, re.S)
            pg = pager.group(0) if pager else ""
            expect(f"{tag}: back to the course and to the previous and next lesson",
                   f'href="{ahjo.course_page(c["code"])}#kortti-{i}"' in pg and (i == 1 or f'href="{ahjo.lesson_page(c["code"], i - 1)}" rel="prev"' in pg)
                   and (i == 16 or f'href="{ahjo.lesson_page(c["code"], i + 1)}" rel="next"' in pg))
    home = (out / "index.html").read_text()
    plan = re.search(r'<ul class="mod-list plan-list"[^>]*>(.*?)</ul>', home, re.S)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 are not in the front page's planned list (teacher 2026-11-08)",
           not plan or not any(f'{c["code"].lower()}.svg' in plan.group(1) for c in d["courses"]))
    rows = re.search(r'<ul class="mod-list ahjo-list">(.*?)</ul>', home, re.S)
    expect(f"{lang}: the front page lists Ahjo 1 and Ahjo 2, each linking its course page with its icon (teacher 2026-11-08)",
           rows is not None and [h for h in re.findall(r'href="([^"]+)"', rows.group(1))] == [ahjo.course_page(c["code"]) for c in d["courses"]]
           and all(f'module-icons/{c["code"].lower()}.svg' in rows.group(1) for c in d["courses"]))
# contradictions in the data (teacher 2026-11-09): deterministic, so they cannot come back
import ahjo_starters
expect("the starter files are what scripts/ahjo_starters.py writes", all((ahjo.STARTERS / n).is_file() and (ahjo.STARTERS / n).read_text() == t for n, t in ahjo_starters.files().items()))
for lang in i18n.languages():
    d = ahjo.load(lang); u = d["ui"]
    expect(f"{lang}: every starter file says it is untested or a template, never approved",
           all(re.search(r"testaamaton|untested|pohja|template|kokeillut|tried", x["note"], re.I) and not re.search(r"hyväksytty|approved|\btestattu\b|\btested\b", x["note"], re.I) for x in d["starters"]))
    WORK = re.compile(r"prototyyp|prototype|tulost|print|arduino|robot|servo|moottor|motor|parist|batter|\bled|pahvi|cardboard|sakse|scissor|työkalu|tool|laitte|device|kuorm|load|juot|solder", re.I)
    for c in d["courses"]:
        for i, l in enumerate(c["lessons"], 1):
            said = " ".join([l.get("start", ""), l.get("example", ""), l.get("output", "")] + list(l.get("levels", {}).values()) + l.get("needs", []))
            expect(f"{lang} {c['code']} lesson {i}: a lesson that builds or tests something does not say 'no devices' (it has safety topics or its own note)",
                   not WORK.search(said) or bool(l.get("safety") or l.get("safety_note")), WORK.search(said).group(0) if WORK.search(said) else None)
    a1 = {i: l for i, l in enumerate(d["courses"][0]["lessons"], 1)}
    expect(f"{lang} AHJO1: lessons 7, 10 and 11 start from their own wiring guide (LED from 5V, serial plotter, servo), not from a measuring program's page",
           [a1[n]["guides"][0] for n in (7, 10, 11)] == ["ahjo-led-piiri", "ahjo-sarjaplotteri", "ahjo-servo"])
    expect(f"{lang} AHJO1 lesson 7: two LEDs and two resistors in the materials, as each parallel branch has its own resistor",
           re.search(r"(kaksi|two) 330 Ω", " ".join(a1[7]["needs"])) is not None and re.search(r"(kaksi|two) LED", " ".join(a1[7]["needs"])) is not None)
    expect(f"{lang} AHJO1 lessons 4, 5, 6, 8: the fit test, load test, before/after and battery estimate are in the basic level",
           all(re.search(k, a1[n]["levels"]["try"], re.I) for n, k in ((4, "sovitekoe|sovitekok|fit test"), (5, "kuorma|kolik|load|coin"), (8, "arvio|estimate"))) and re.search(r"ennen ja jälkeen|before.and.after", a1[6]["output"], re.I))
    expect(f"{lang} AHJO1 lesson 15: build, test, change and test again, and a failed change is accepted", re.search(r"testaa uudelleen|test again|uusi testi|new test", a1[15]["output"] + a1[15]["levels"]["modify"], re.I)
           and re.search(r"ei tarvitse onnistua|epäonnist|ei onnistunut|does not have to succeed|fail|did not", a1[15]["output"] + a1[15]["levels"]["modify"], re.I))
    # brief 3 (teacher 2026-11-09 19.42): robotics on a ready base, a correct multimeter, the light sensor's direction, waiting options
    expect(f"{lang} AHJO1 lessons 12–13: the basic level runs on a ready robot base, building it is the challenge, and the sensor starts with a simple trial",
           re.search(r"valmiiksi koottu|valmis|ready", a1[12]["start"] + " ".join(a1[12]["needs"]), re.I) is not None and re.search(r"kokoa|assemble", a1[12]["levels"]["challenge"], re.I) is not None
           and re.search(r"painike|button", a1[13]["levels"]["modify"], re.I) is not None and "mekaaninen" not in a1[12]["safety"])
    expect(f"{lang} AHJO1 lesson 8: voltage in parallel, current in series, and never a current range across the battery",
           all(re.search(w, a1[8]["levels"]["try"] + a1[8].get("safety_note", ""), re.I) for w in (r"rinnan|parallel", r"sarjaan|series")) and re.search(r"sulak|fuse", a1[8].get("safety_note", ""), re.I))
    expect(f"{lang} AHJO1 lesson 10: more light raises the buzzer's pitch (a covering hand lowers it, as the sketch maps light to pitch)",
           not re.search(r"käsi lähestyy|hand comes closer", a1[10]["levels"]["modify"]))
    expect(f"{lang} AHJO1 lesson 1: the coin cell's hazard is said", re.search(r"niel|swallow", a1[1].get("safety_note", ""), re.I) is not None)
    expect(f"{lang}: every lesson that prints in class, or shares a robot, says what to do while waiting (lessons 4, 5, 6, 12, 13, 15; Ahjo 2: 8, 14)",
           all(a1[n].get("wait") for n in (4, 5, 6, 12, 13, 15)) and all(d["courses"][1]["lessons"][n - 1].get("wait") for n in (8, 14)))
    expect(f"{lang}: every lesson has a short goal (what you learn), at most 140 characters", all(l.get("goal") and len(l["goal"]) <= 140 for c in d["courses"] for l in c["lessons"]),
           [l["title"] for c in d["courses"] for l in c["lessons"] if not l.get("goal") or len(l["goal"]) > 140])
    expect(f"{lang}: the licence's skills checklist covers coin cells, the multimeter, the printer's hot parts, tools and robots, and testing, and says it does not replace a device permit",
           all(any(re.search(w, x, re.I) for x in u["license_check"]) for w in (r"nappiparist|coin cell", r"rinnan|parallel", r"kuum|hot", r"robot", r"testaa|test")) and re.search(r"lupa|permit", u["license_check_note"], re.I))
    expect(f"{lang}: both courses list what is assessed, and say a failed prototype or attempt can show excellent skills",
           [len(c["assessment"]["items"]) for c in d["courses"]] == [6, 7, 7] and all(re.search(r"epäonnist|ei onnistunut|ei toiminut|fail", c["assessment"]["note"], re.I) for c in d["courses"]))
    hand = [l for c in d["courses"] for l in c["lessons"] if l.get("milestone")]
    expect(f"{lang}: the peer practices add no hand-ins (still five, all in Ahjo 2)", len(hand) == 5 and all(not l.get("milestone") for l in d["courses"][0]["lessons"]))
    for g in ("ahjo-led-piiri", "ahjo-sarjaplotteri", "ahjo-servo"):
        t = ahjo.guide_file(g, lang).read_text()
        expect(f"{lang} {g}: the guide has code or wiring, and troubleshooting", "<svg data-fig=" in t and t.count("\n| ") >= 4)
    t = ahjo.guide_file("ahjo-led-piiri", lang).read_text()
    expect(f"{lang} ahjo-led-piiri: no program is needed, and each parallel branch has its own resistor", "```" not in t and re.search(r"oma \$330|own \$330", t) is not None)
    t = ahjo.guide_file("ahjo-sarjaplotteri", lang).read_text()
    expect(f"{lang} ahjo-sarjaplotteri: the program in the guide is the starter sketch's, at the plotter's speed", "Serial.begin(9600)" in t and "9600" in ahjo_starters.SKETCH
           and "analogRead(SENSOR_PIN)" in t and "analogRead(SENSOR_PIN)" in ahjo_starters.SKETCH and "Vernier" not in t)
fi, easy = ahjo.load(), ahjo.load("fi-easy")
key = lambda d: [(l.get("start"), l.get("example"), l.get("peer"), l.get("safety_note"), tuple(l.get("levels", {}).values())) for c in d["courses"] for l in c["lessons"]]
diff = sum(a != b for a, b in zip(key(fi), key(easy)))
expect("fi-easy: the key student instructions are rewritten in selkosuomi (not the Finnish text copied)", ahjo.data_file("fi-easy") != ahjo.SOURCE and diff == 48, diff)   # 32 lessons of Ahjo 1 and 2, and Dronelabra's 16 (2026-11-12)
expect("fi-easy: shorter sentences than the Finnish in the lessons' instructions",
       (lambda w: w(easy) < w(fi))(lambda d: sum(len(s.split()) for x in key(d) for v in x for s in re.split(r"[.?!]", " ".join(v) if isinstance(v, tuple) else (v or "")) if s.strip())
                                    / max(1, sum(1 for x in key(d) for v in x for s in re.split(r"[.?!]", " ".join(v) if isinstance(v, tuple) else (v or "")) if s.strip()))))

import module_icons
expect("Ahjo 1's and Ahjo 2's icons are the teacher's choice (1a, 2a), drawn on the logo's anvil", all(module_icons.file(c).read_text() == ahjo.course_icon_svg(c) for c in ahjo.COURSE_ICON_TITLES))
expect("the header's Ruukkilabra symbol in Kiviruukin lukio's colours is up to date", ahjo.SITE_MARK_KR.is_file() and ahjo.SITE_MARK_KR.read_text() == ahjo.site_mark_kiviruukki())
for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    h = (out / ahjo.PAGE).read_text()
    expect(f"{lang}: the Ahjo pages' header symbol is in Kiviruukin lukio's colours", "ruukkilabra-symboli-kiviruukki.svg" in h[:h.find("</header>")] and 'brand-mark" src="brand/ruukkilabra-symboli.svg' not in h)
expect("the mark is cut from the original logo unchanged (scripts/ahjo_art.py writes it)", ahjo.MARK.is_file() and ahjo.MARK.read_text() == ahjo.mark_svg())

# browser: widths and keyboard
from playwright.sync_api import sync_playwright
port = 8799
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port)], cwd=SITE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": os.environ["CHROMIUM_PATH"]} if os.environ.get("CHROMIUM_PATH") else {}))
        gpages = [f"{g}.html" for g in ahjo.ready_guides(ahjo.load())]
        for name in ["ahjo.html", "ahjo-1.html", "ahjo-2.html", "ahjo-materiaalit.html", "ahjo-turvallisuus.html", "ahjo-projektit.html", "en/ahjo.html", "en/ahjo-1.html", "en/ahjo-projektit.html",
                     "ahjo-1-tunti-1.html", "ahjo-1-tunti-3.html", "ahjo-1-tunti-9.html", "ahjo-1-tunti-14.html", "ahjo-2-tunti-1.html", "ahjo-2-tunti-5.html",
                     "ahjo-2-tunti-16.html", "en/ahjo-2.html", "en/ahjo-1-tunti-7.html", "en/ahjo-2-tunti-9.html", "fi-easy/ahjo-1-tunti-12.html", "fi-easy/ahjo-1-tunti-5.html", "fi-easy/ahjo-2-tunti-9.html"] + gpages + ["en/" + g for g in gpages]:
            for w in (360, 768, 1280):
                pg = b.new_page(viewport={"width": w, "height": 900}); pg.goto(f"http://localhost:{port}/{name}")
                ov = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                expect(f"{name} @ {w}: no sideways scroll", ov <= 0, ov)
                small = pg.evaluate("""[...document.querySelectorAll('main a')].filter(a => { if (a.closest('.ahjo-guide p, .ahjo-guide li, .ahjo-guide td, .ahjo-proj dd')) return false; const r = a.getBoundingClientRect();
                    return r.width > 0 && r.height < 24; }).map(a => a.textContent.trim()).slice(0, 5)""")
                expect(f"{name} @ {w}: links are at least 24 px high", not small, small)
                pg.close()
        pg = b.new_page(viewport={"width": 1280, "height": 900}); pg.goto(f"http://localhost:{port}/ahjo.html")
        seen = []
        for _ in range(40):
            pg.keyboard.press("Tab")
            seen.append(pg.evaluate("(() => { const a = document.activeElement; return a.closest('.ahjo-nav') ? a.getAttribute('href') : null })()"))
        nav = [h for h in seen if h]
        expect("keyboard: Tab reaches every link of Ahjo's navigation in order", nav[:6] == ["ahjo.html", "ahjo.html#opintojaksot", "ahjo-materiaalit.html", "ahjo-projektit.html", "ahjo.html#laitteisto", "ahjo-turvallisuus.html"], nav)
        # old links keep working (ahjo.js): a lesson's anchor on the course page opens its page, #miniprojekti opens lesson 14,
        # a folded section's anchor unfolds it; the back link goes to the course page and stays there
        pg = b.new_page(viewport={"width": 390, "height": 844})
        for old, new in (("ahjo-1.html#tunti-3", "/ahjo-1-tunti-3.html"), ("ahjo-2.html#tunti-12", "/ahjo-2-tunti-12.html"), ("ahjo-1.html#miniprojekti", "/ahjo-1-tunti-14.html"),
                         ("ahjo-1.html#kortti-3", "/ahjo-1.html"), ("en/ahjo-1.html#tunti-5", "/en/ahjo-1-tunti-5.html")):
            pg.goto(f"http://localhost:{port}/{old}"); pg.wait_for_load_state()
            expect(f"old link {old} opens {new}", pg.url.split("#")[0].endswith(new), pg.url)
        pg.goto(f"http://localhost:{port}/ahjo-1.html#ajokortti")
        expect("an anchor under the folded details (#ajokortti) unfolds them", pg.evaluate("document.getElementById('opintojaksosta').open"))
        pg.goto(f"http://localhost:{port}/ahjo-1-tunti-9.html"); pg.click(".ahjo-now .ahjo-cta"); pg.wait_for_load_state()
        back = pg.locator(".ahjo-from a")
        expect("a guide opened from a lesson shows the way back to that lesson", back.is_visible() and back.get_attribute("href") == "ahjo-1-tunti-9.html", pg.url)
        pg.goto(f"http://localhost:{port}/ahjo-1-tunti-9.html"); pg.click(".ahjo-pager-next"); pg.wait_for_load_state()
        expect("Next lesson goes from lesson 9 to lesson 10", pg.url.endswith("/ahjo-1-tunti-10.html"), pg.url)
        pg.click(".ahjo-pager-up"); pg.wait_for_load_state()
        expect("Back to the course stays on the course page", pg.url.split("#")[0].endswith("/ahjo-1.html"), pg.url)
        pg.goto(f"http://localhost:{port}/ahjo-projektit.html")
        d0 = ahjo.load()
        pg.click('.ahjo-filter[data-key="level"] .ahjo-fbtn[data-v="3"]')
        vis = pg.evaluate("[...document.querySelectorAll('article.ahjo-proj')].filter(a => a.offsetParent).map(a => a.id)")
        expect("project bank: the level filter shows only that level's cards", sorted(vis) == sorted(p["id"] for p in d0["projects"] if p["level"] == 3) and vis, vis)
        pg.click('.ahjo-filter[data-key="level"] .ahjo-fbtn[data-v=""]')
        expect("project bank: All shows every card again", pg.evaluate("[...document.querySelectorAll('article.ahjo-proj')].filter(a => a.offsetParent).length") == len(d0["projects"]))
        pg.goto(f"http://localhost:{port}/ahjo-materiaalit.html")
        pg.click('.ahjo-filter[data-key="time"] .ahjo-fbtn[data-v="short"]')
        vis = pg.evaluate("[...document.querySelectorAll('article.ahjo-chal')].filter(a => a.offsetParent).map(a => a.id)")
        expect("material bank: the time filter shows only the short challenges", sorted(vis) == sorted(x["id"] for x in d0["challenges"] if x["minutes"] <= 20) and vis, vis)
        pg.goto(f"http://localhost:{port}/ahjo-1.html")
        top = pg.evaluate("document.querySelector('.ahjo-course-hero .ahjo-cta').getBoundingClientRect().bottom")
        expect("phone: the button to the first task is in the first screen", top <= 844, top)
        pg.close()
        b.close()
finally:
    srv.terminate()

print(f"\n{len(fails)} failure(s)" if fails else "\nall Ahjo checks passed")
sys.exit(1 if fails else 0)
