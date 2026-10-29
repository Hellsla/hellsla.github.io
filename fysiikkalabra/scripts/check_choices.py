"""Where the correct option sits on the built pages, per course. Usage: python scripts/check_choices.py [<id> | <course> | --all] [--site]

Options are shown in a seeded order (inquiry.choice_order), so the check reads what students see: every
`<ul class="choices">` of each lesson page in preview/ (or site/ with --site, or when there is no preview), the
position of the option marked data-correct="1", and the number of options. For each course it compares the count
in each position with what a fair shuffle gives (an item with k options adds 1/k to each of its k positions):

  FAIL  20 or more items and one position holds more than 45 % of the correct answers, or a position is used
        more than 3 standard deviations more or less than a fair shuffle would (positions expected at least 5 times)
  WARN  6–19 items and one position holds more than 60 %; fewer items say nothing either way
  WARN  a lesson with 4 or more items has every correct answer in the same position
  WARN  the correct option is the longest one (visible text, formulas counted by their content) in more than 40 % of a
        course's 10 or more items, or in one item more than 20 % longer than every distractor: a student can pick the
        longest, most careful-sounding option without the physics (teacher 2026-10-29); shorten it or give the
        distractors the same detail, a content change that needs the reviews
  WARN  competing explanations ("Aino: …") where one speaker is right in more than 60 % of 6 or more items:
        the shuffle moves the option, not the name, so a student can still guess; rename speakers in the next
        content round (a content change, so it needs the reviews)

A FAIL that a fair shuffle produced by chance is fixed without touching any lesson: set "shuffle_salt" in the
course's entry in curriculum.json (scripts/courses.py), which re-seeds that course's order. Exit status 1 on FAIL."""
import collections, json, math, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

SPEAKER = re.compile(r"\s*\**([A-ZÅÄÖ][a-zåäö]+)\**\s*:")


def positions(page_html):
    """[(position of the first correct option, number of options)] in page order."""
    out = []
    for ul in re.findall(r'<ul class="choices">(.*?)</ul>', page_html, re.S):
        flags = re.findall(r'data-correct="([01])"', ul)
        if "1" in flags: out.append((flags.index("1"), len(flags)))
    return out


def speakers(folder):
    """Names of the speakers whose explanation is the correct option, in competing-explanation items of inquiry.json."""
    data = json.loads((folder / "inquiry.json").read_text()) if (folder / "inquiry.json").exists() else {}
    names = []
    def walk(x):
        if isinstance(x, dict):
            ch = x.get("choices")
            if isinstance(ch, list) and len(ch) > 1 and all(isinstance(c, dict) and SPEAKER.match(c.get("text", "")) for c in ch):
                names.extend(SPEAKER.match(c["text"]).group(1) for c in ch if c.get("correct"))
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(data)
    return names


def _visible(text):
    return len(re.sub(r"\\[a-zA-Z]+|[{}$*_^\\]", "", text))


def longest(folder):
    """[(activity id, correct is strictly longest, correct is more than 20 % longer than every distractor)] of the
    choice items in inquiry.json and exit-ticket.json."""
    out = []
    for name in ("inquiry.json", "exit-ticket.json"):
        f = folder / name
        if not f.exists(): continue
        def walk(x, owner=""):
            if isinstance(x, dict):
                owner = x.get("id", owner)
                ch = x.get("choices")
                if isinstance(ch, list) and len(ch) > 1 and all(isinstance(c, dict) and "text" in c for c in ch):
                    right = [_visible(c["text"]) for c in ch if c.get("correct")]
                    wrong = [_visible(c["text"]) for c in ch if not c.get("correct")]
                    if len(right) == 1 and wrong:
                        out.append((owner, right[0] > max(wrong), right[0] > 1.2 * max(wrong)))
                for v in x.values(): walk(v, owner)
            elif isinstance(x, list):
                for v in x: walk(v, owner)
        walk(json.loads(f.read_text()))
    return out


def length_warns(code, by_lesson):
    items = [(lid, it) for lid, its in by_lesson.items() for it in its]
    warns = [f"{lid} {aid}: the correct option is over 20 % longer than every distractor" for lid, (aid, _, much) in items if much]
    n, k = len(items), sum(1 for _, (_, longer, _) in items if longer)
    if n >= 10 and k / n > 0.40:
        warns.insert(0, f"{code}: the correct option is the longest in {k} of {n} items ({100 * k / n:.0f} %, limit 40 %)")
    return warns


def course_report(code, items_by_lesson, names):
    """(fails, warns, summary line) for one course."""
    fails, warns = [], []
    items = [it for its in items_by_lesson.values() for it in its]
    n = len(items)
    kmax = max((k for _, k in items), default=0)
    obs = [sum(1 for p, _ in items if p == i) for i in range(kmax)]
    exp = [sum(1 / k for _, k in items if k > i) for i in range(kmax)]
    var = [sum((1 / k) * (1 - 1 / k) for _, k in items if k > i) for i in range(kmax)]
    shares = [o / n for o in obs] if n else []
    dist = " / ".join(f"{o}" for o in obs)
    summary = f"{code}: {n} choice item(s) in {len(items_by_lesson)} lesson(s), correct option in positions 1–{kmax}: {dist} (fair shuffle ≈ {' / '.join(f'{e:.1f}' for e in exp)})"
    if n >= 20:
        for i, s in enumerate(shares):
            if s > 0.45: fails.append(f"{code}: position {i + 1} holds {obs[i]}/{n} = {100 * s:.0f} % of the correct answers (limit 45 %)")
        for i in range(kmax):
            if exp[i] >= 5 and var[i] > 0 and abs(obs[i] - exp[i]) > 3 * math.sqrt(var[i]):
                fails.append(f"{code}: position {i + 1} has {obs[i]} correct answers, a fair shuffle gives {exp[i]:.1f} ± {math.sqrt(var[i]):.1f}")
    elif n >= 6:
        for i, s in enumerate(shares):
            if s > 0.60: warns.append(f"{code}: position {i + 1} holds {obs[i]}/{n} of the correct answers (too few items to fail on)")
    for lid, its in items_by_lesson.items():
        if len(its) >= 4 and len({p for p, _ in its}) == 1:
            warns.append(f"{lid}: every one of its {len(its)} correct answers is in position {its[0][0] + 1}")
    cnt = collections.Counter(names)
    if len(names) >= 6 and cnt and cnt.most_common(1)[0][1] / len(names) > 0.60:
        who, k = cnt.most_common(1)[0]
        warns.append(f"{code}: in competing explanations {who} is right in {k} of {len(names)} items; the shuffle moves the option, not the name (rename speakers in the next content round)")
    return fails, warns, summary


def main(args):
    site = "--site" in args; args = [a for a in args if a != "--site"]
    out = courses.ROOT / ("site" if site or not (courses.ROOT / "preview" / "index.html").exists() else "preview")
    target = args[0] if args else "--all"
    lessons = courses.lessons()
    if target != "--all":
        code = courses.course_of(target) if target.lower() != target.upper() and "-" in target else target.upper()
        lessons = [f for f in lessons if courses.course_of(f.name) == code]
    by_course = collections.defaultdict(dict); names = collections.defaultdict(list); lengths = collections.defaultdict(dict)
    for folder in lessons:
        page = out / f"{folder.name}.html"
        if not page.exists(): continue
        code = courses.course_of(folder.name)
        items = positions(page.read_text())
        if items: by_course[code][folder.name] = items
        names[code] += speakers(folder)
        lengths[code][folder.name] = longest(folder)
    bad = 0
    if not by_course: print(f"no choice items on the pages in {out.name}/ for {target}")
    for code in sorted(by_course):
        fails, warns, summary = course_report(code, by_course[code], names[code])
        print(("FAIL " if fails else "ok   ") + summary)
        for f in fails: print("  FAIL " + f)
        for w in warns + length_warns(code, lengths[code]): print("  WARN " + w)
        bad += bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
