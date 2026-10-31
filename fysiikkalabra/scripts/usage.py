"""Token and cost accounting per lesson in review/usage.tsv, measured from Claude Code's own transcripts.

  python scripts/usage.py collect <id>[,<id>...] [--session <id | path.jsonl>] [--round n] [--since 2026-10-26T07:00:00Z]
      reads the session transcript (~/.claude/projects/<project>/<session>.jsonl; the current session by default,
      $CLAUDE_CODE_SESSION_ID) and every subagent transcript beside it (<session>/subagents/agent-*.jsonl) and writes
      one row per agent run of this lesson and one for the main session's part (the /lesson orchestrator, from the
      "Run lesson <id>" message on, or from --since when the steps were run without the command). Run it again and
      the rows are replaced, never added twice (column ref).
  python scripts/usage.py log <id> --agent A --model M --effort E --mode M --round n --context N --seconds S --calls C --verdict V
      a manual row, for a run without a transcript (source=reported)
  python scripts/usage.py report <id | FY4 | --all> [--by agent]
      the rows, measured totals, the list-price cost, and what is not measured

What is measured. Every assistant turn in a transcript carries the API's usage: input (uncached), cache_write
(5-minute and 1-hour), cache_read and output tokens, and the model that served it. A turn appears on several lines
(one per content block) with one message id, so turns are counted once. `tokens` is the sum of the four over all
turns: what the run processed. `context` is the last turn's prompt plus output: what the harness reports as an
agent's "tokens" at the end, the run's final context size. They differ by a factor of 2–10, because every turn
re-reads the context (mostly as cheap cache reads). Rows logged before this script read transcripts have only
`context` (source=notification); their consumption is unknown and the report says so. No transcript text is
written anywhere: only counts, model ids and a hash of the session and agent id (ref).

Cost: list prices per million tokens (the claude-api skill, cached 2026-10-06; check the pricing page). Input, output
and cache read are per model; a cache write costs 1.25× input (5 min) or 2× (1 h). Claude Haiku 5.5 bills a turn
whose prompt exceeds 100 000 tokens at 0.50 / 2.50. On a subscription the cost is what the same work would cost on
the API: a comparison figure, not a bill."""
import argparse, collections, datetime, hashlib, json, os, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

COLS = ["date", "lesson", "course", "agent", "stage", "model", "effort", "mode", "round", "tokens", "input", "output", "cache_read",
        "cache_write", "context", "turns", "seconds", "calls", "verdict", "cost_usd", "source", "ref"]
OLD_COLS = ["date", "lesson", "agent", "model", "effort", "mode", "round", "tokens", "input", "output", "cache_read", "cache_write", "seconds", "calls", "verdict"]
PRICES = {"fable": (10.0, 50.0, 0.25), "opus": (4.0, 20.0, 0.20), "sonnet": (2.0, 10.0, 0.20), "haiku": (0.10, 0.50, 0.01)}   # $/MTok in, out, cache read
HAIKU_LONG = (0.50, 2.50, 0.05)          # Haiku 5.5 turns with a prompt over 100 000 tokens
BASELINE = 473632                       # fy3-9, 25 Oct 2026, before packets and delta reviews: a sum of final contexts, compare with `context`
LESSON = re.compile(r"\b([a-z]+\d+-(?:[0-9][0-9a-z]*|[a-z]+(?:-[a-z]+)*)|tvt-[a-z]+(?:-[a-z]+)*)\b")   # a lesson, an investigation (fy10-jousivakio) or a TVT guide


def course_of(pid):
    """The course of a lesson; FY10 for an investigation, TVT for a guide (the local course that lists them)."""
    if pid.startswith("tvt-"): return "TVT"
    try: return courses.course_of(pid)
    except (SystemExit, ValueError, KeyError): return pid.split("-")[0].upper()


def review_folder(pid):
    """review/ of a lesson, an investigation or a TVT guide: where its usage.tsv lives."""
    import guides, investigations
    if pid in investigations.ids(): return investigations.folder(pid) / "review"
    if pid in guides.ids(): return guides.folder(pid) / "review"
    return courses.find_lesson(pid) / "review"
PACKET = re.compile(r"review/packet-(science|pedagogy|visual|developer)\.md")


def family(model):
    return next((f for f in PRICES if f in (model or "")), None)


def turn_cost(model, u):
    """$ for one turn's usage, or None for a model without a known price."""
    f = family(model)
    if f is None: return None
    cw = u.get("cache_creation") or {}
    w5, w1 = cw.get("ephemeral_5m_input_tokens"), cw.get("ephemeral_1h_input_tokens")
    if w5 is None and w1 is None: w5, w1 = u.get("cache_creation_input_tokens", 0), 0
    prompt = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + (w5 or 0) + (w1 or 0)
    i, o, r = HAIKU_LONG if f == "haiku" and prompt > 100_000 else PRICES[f]
    return (u.get("input_tokens", 0) * i + (w5 or 0) * 1.25 * i + (w1 or 0) * 2 * i + u.get("cache_read_input_tokens", 0) * r + u.get("output_tokens", 0) * o) / 1e6


def read_transcript(path, start=None, end=None):
    """Measured totals of one transcript (optionally only the lines from index start to end) and its first user text."""
    turns, models, calls, times, prompt, last_text = {}, collections.Counter(), 0, [], None, ""
    lines = path.read_text().splitlines()[start:end]
    for line in lines:
        try: r = json.loads(line)
        except json.JSONDecodeError: continue
        if r.get("timestamp"): times.append(r["timestamp"])
        m = r.get("message") or {}
        content = m.get("content")
        if r.get("type") == "user" and prompt is None:
            prompt = content if isinstance(content, str) else " ".join(c.get("text", "") for c in content or [] if isinstance(c, dict) and c.get("type") == "text")
        if r.get("type") != "assistant" or not m.get("usage"): continue
        turns[m.get("id") or r.get("uuid")] = (m.get("model"), m["usage"])
        for c in content if isinstance(content, list) else []:
            if c.get("type") == "tool_use": calls += 1
            if c.get("type") == "text" and c.get("text"): last_text = c["text"]
    tot = collections.Counter(); cost, priced = 0.0, True
    for model, u in turns.values():
        if model == "<synthetic>": continue
        models[model] += 1
        tot["input"] += u.get("input_tokens", 0); tot["output"] += u.get("output_tokens", 0)
        tot["cache_read"] += u.get("cache_read_input_tokens", 0); tot["cache_write"] += u.get("cache_creation_input_tokens", 0)
        c = turn_cost(model, u); cost += c or 0; priced &= c is not None
    last = next((u for model, u in reversed(list(turns.values())) if model != "<synthetic>"), {})
    context = sum(last.get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens"))
    secs = 0
    if len(times) > 1:
        t = sorted(datetime.datetime.fromisoformat(x.replace("Z", "+00:00")) for x in times); secs = int((t[-1] - t[0]).total_seconds())
    return {"tot": tot, "models": models, "calls": calls, "turns": sum(models.values()), "context": context, "seconds": secs,
            "cost": cost if priced else None, "prompt": prompt or "", "last_text": last_text}


def session_file(session):
    base = pathlib.Path(os.environ.get("CLAUDE_CONFIG_DIR") or pathlib.Path.home() / ".claude") / "projects"
    if session and session.endswith(".jsonl"): return pathlib.Path(session)
    sid = session or os.environ.get("CLAUDE_CODE_SESSION_ID")
    found = sorted(base.glob(f"*/{sid}.jsonl")) if sid else sorted(base.glob("*/*.jsonl"), key=lambda p: p.stat().st_mtime)[-1:]
    if not found: sys.exit(f"no transcript for session {sid or '(latest)'} under {base}; pass --session <id or path>")
    return found[-1]


def read_rows(f):
    if not f.exists(): return []
    lines = f.read_text().splitlines()
    head = lines[0].split("\t") if lines else COLS
    rows = [dict(zip(head, l.split("\t"))) for l in lines[1:] if l.strip()]
    if head != COLS:                                   # rows from before transcripts: the number was the final context
        for r in rows:
            r["context"], r["tokens"] = r.get("tokens", ""), ""
            r["source"] = r.get("source") or "notification"
            r["course"] = r.get("course") or course_of(r["lesson"])
    return rows


def write_rows(f, rows):
    f.parent.mkdir(exist_ok=True)
    f.write_text("\t".join(COLS) + "\n" + "".join("\t".join(str(r.get(c, "")) for c in COLS) + "\n" for r in rows))


def row_of(lid, agent, stage, s, ref, **extra):
    models = s["models"]
    model = ", ".join(m for m, _ in models.most_common()) or "?"
    t = s["tot"]
    return {"date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "lesson": lid, "course": course_of(lid),
            "agent": agent, "stage": stage, "model": model, "tokens": sum(t.values()), "input": t["input"], "output": t["output"],
            "cache_read": t["cache_read"], "cache_write": t["cache_write"], "context": s["context"], "turns": s["turns"], "seconds": s["seconds"],
            "calls": s["calls"], "cost_usd": "" if s["cost"] is None else f"{s['cost']:.4f}", "source": "transcript", "ref": ref, **extra}


def scaled(s, k):
    """A transcript summary times k: a batch run's share of one lesson."""
    s = dict(s); s["tot"] = collections.Counter({x: round(v * k) for x, v in s["tot"].items()}); s["context"] = round(s["context"] * k)
    if s["cost"] is not None: s["cost"] *= k
    return s


def collect(lid, session=None, rnd="", since=None, batch=()):
    """batch: the lessons of one batch run (a comma list on the command line). A batch agent ("Lessons: a, b, c" in its
    prompt) and the orchestrator's part are shared equally among its lessons, so a course total counts each once."""
    sf = session_file(session); sid = sf.stem
    f = review_folder(lid) / "usage.tsv"
    rows = read_rows(f); by_ref = {r.get("ref"): i for i, r in enumerate(rows) if r.get("ref")}
    new = []
    for t in sorted((sf.parent / sid / "subagents").glob("agent-*.jsonl")):
        if since and (json.loads(t.read_text().splitlines()[0]).get("timestamp") or "") < since: continue   # an agent from before this run
        s = read_transcript(t)
        lessons = set(LESSON.findall(s["prompt"])); share = None
        if "Lessons:" in s["prompt"] and lid in lessons: share = len(lessons); s = scaled(s, 1 / share)
        elif lid not in lessons or (len(lessons) > 1 and f"Lesson: {lid}" not in s["prompt"]): continue
        meta_f = t.with_suffix(".meta.json"); meta = json.loads(meta_f.read_text()) if meta_f.exists() else {}
        role = PACKET.search(s["prompt"])
        agent = meta.get("agentType", "agent")
        if role and agent in ("general-purpose", "agent", "claude"): agent = {"science": "science-reviewer", "pedagogy": "pedagogy-reviewer", "visual": "visual-editorial-reviewer"}.get(role.group(1), role.group(1))
        mode = re.search(r"\bMode:\s*(\w+)", s["prompt"]); r_ = re.search(r"\bRound:\s*(\d+)", s["prompt"])
        verdict = re.search(r"VERDICT:\s*(PASS|FAIL|DONE|BLOCKED)", s["last_text"])
        stage = "review" if "reviewer" in agent else "develop" if agent == "developer" else "other"
        new.append(row_of(lid, agent, stage, s, hashlib.sha1(f"{sid}:{t.stem}".encode()).hexdigest()[:12],
                          effort=meta.get("effort", ""), mode=(f"batch/{share}" if share else mode.group(1) if mode else ""), round=r_.group(1) if r_ else rnd,
                          verdict=verdict.group(1) if verdict else ""))
    lines = sf.read_text().splitlines(); start = end = None
    for i, line in enumerate(lines):                    # the orchestrator's share: from "Run lesson <id>" to the next /lesson run
        if "Run lesson " not in line: continue
        try: r = json.loads(line)
        except json.JSONDecodeError: continue
        c = (r.get("message") or {}).get("content")
        text = c if isinstance(c, str) else " ".join(b.get("text", "") for b in c or [] if isinstance(b, dict) and b.get("type") == "text")
        if r.get("type") != "user" or r.get("isSidechain") or not text: continue   # the command's own message, not a tool result quoting it
        m = re.search(r"Run lesson ([a-z]+\d+-[0-9][0-9a-z]*)", text)
        if m and m.group(1) == lid and start is None: start = i
        elif m and start is not None and m.group(1) != lid: end = i; break
    if start is None and since:                          # no /lesson message: the orchestration started at a known time
        start = next((i for i, line in enumerate(lines) if (json.loads(line).get("timestamp") or "") >= since), len(lines))
        mode = "since"
    else: mode = "session" if start is None else "lesson-run"
    s = read_transcript(sf, start, end)
    if len(batch) > 1: s = scaled(s, 1 / len(batch)); mode = f"{mode}/{len(batch)}"
    new.append(row_of(lid, "orchestrator", "orchestrate", s, hashlib.sha1((f"{sid}:main:{lid}" + (f":{since}" if since else "")).encode()).hexdigest()[:12], mode=mode, round=rnd))
    for r in new:
        if r["ref"] in by_ref: rows[by_ref[r["ref"]]] = r
        else: rows.append(r)
    write_rows(f, rows)
    for r in new: print(f"{r['agent']:18} {r['model']:22} {int(r['tokens']):>9} tokens processed, context {int(r['context']):>7}, ${r['cost_usd'] or '?'}")
    if mode == "session": print("note: no 'Run lesson' message in this session; the orchestrator row holds the whole main session")


def log(a):
    f = review_folder(a.id) / "usage.tsv"
    rows = read_rows(f)
    rows.append({"date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "lesson": a.id, "course": course_of(a.id),
                 "agent": a.agent, "stage": a.stage, "model": a.model, "effort": a.effort, "mode": a.mode, "round": a.round, "context": a.context,
                 "seconds": a.seconds, "calls": a.calls, "verdict": a.verdict, "source": "reported"})
    write_rows(f, rows); print("logged", a.agent, a.model, a.context)


def report(target, by=None):
    if target == "--all": folders = courses.lessons()
    elif courses.LESSON_ID.match(target) or LESSON.fullmatch(target): folders = [review_folder(target).parent]
    else: folders = courses.lessons(target.upper())
    rows = [r for f in folders for r in read_rows(f / "review" / "usage.tsv")]
    if not rows: sys.exit(f"{target}: no review/usage.tsv rows")
    num = lambda r, k: int(r.get(k) or 0)
    measured = [r for r in rows if r.get("source") == "transcript"]; other = [r for r in rows if r.get("source") != "transcript"]
    if by:
        g = collections.defaultdict(lambda: collections.Counter())
        for r in rows:
            k = (r["agent"], r["model"], r.get("mode", ""), r.get("source", ""))
            g[k]["runs"] += 1; g[k]["context"] += num(r, "context"); g[k]["tokens"] += num(r, "tokens"); g[k]["cost"] += float(r.get("cost_usd") or 0)
        print(f"{'agent':18} {'model':22} {'mode':9} {'source':12} {'runs':>4} {'context sum':>12} {'processed':>11} {'cost $':>8}")
        for k, c in sorted(g.items(), key=lambda kv: -kv[1]["context"]):
            print(f"{k[0]:18} {k[1][:22]:22} {k[2]:9} {k[3]:12} {c['runs']:>4} {c['context']:>12} {c['tokens'] or '':>11} {c['cost'] or '':>8}")
    else:
        print(f"{'lesson':8} {'agent':18} {'model':22} {'mode':8} {'rnd':>3} {'processed':>10} {'in':>7} {'out':>7} {'c.read':>9} {'c.write':>8} {'context':>8} {'calls':>5} {'verdict':7} {'cost $':>8} source")
        for r in rows:
            print(f"{r['lesson']:8} {r['agent']:18} {r['model'][:22]:22} {r.get('mode', ''):8} {r.get('round', ''):>3} {r.get('tokens', ''):>10} {r.get('input', ''):>7} {r.get('output', ''):>7} "
                  f"{r.get('cache_read', ''):>9} {r.get('cache_write', ''):>8} {r.get('context', ''):>8} {r.get('calls', ''):>5} {r.get('verdict', ''):7} {r.get('cost_usd', ''):>8} {r.get('source', '')}")
    print()
    if measured:
        t = {k: sum(num(r, k) for r in measured) for k in ("tokens", "input", "output", "cache_read", "cache_write")}
        cost = sum(float(r.get("cost_usd") or 0) for r in measured)
        print(f"measured ({len(measured)} runs, from transcripts): {t['tokens']} tokens processed = {t['input']} input + {t['cache_write']} cache write + "
              f"{t['cache_read']} cache read + {t['output']} output; ${cost:.2f} at API list prices")
    if other:
        print(f"not measured ({len(other)} runs, source {', '.join(sorted({r.get('source', '') for r in other}))}): only the final context size per run "
              f"(sum {sum(num(r, 'context') for r in other)}); what they processed and cost is unknown")
    if len(folders) == 1:
        ctx = sum(num(r, "context") for r in rows)
        print(f"context sum {ctx} = {100 * ctx / BASELINE:.0f} % of the fy3-9 baseline ({BASELINE}, the same measure: a sum of final contexts)")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("collect"); c.add_argument("id"); c.add_argument("--session"); c.add_argument("--round", default=""); c.add_argument("--since")
    l = sub.add_parser("log"); l.add_argument("id")
    for k in ("agent", "model", "effort", "mode", "verdict"): l.add_argument(f"--{k}", required=True)
    l.add_argument("--stage", default="")
    for k in ("round", "context", "seconds", "calls"): l.add_argument(f"--{k}", type=int, required=True)
    r = sub.add_parser("report"); r.add_argument("target"); r.add_argument("--by", choices=["agent"])
    a = p.parse_args()
    if a.cmd == "collect":
        ids = a.id.split(",")
        for i in ids: collect(i, a.session, a.round, a.since, batch=ids)
    elif a.cmd == "log": log(a)
    else: report(a.target, a.by)
