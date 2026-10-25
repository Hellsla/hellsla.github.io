"""Token and cost accounting, one row per agent run, in review/usage.tsv.

  python scripts/usage.py log <id> --agent science-reviewer --model opus --effort medium --mode full --round 1 \\
         --tokens 96618 --seconds 113 --calls 14 --verdict PASS [--input N --output N --cache-read N --cache-write N]
  python scripts/usage.py report <id>     table, totals, list-price estimate and the comparison with the fy3-9 baseline

The harness reports one token total per agent run; the input, output and cache columns stay empty until it
reports them, and the cost is then an estimate (90 % input assumed, bounds given). Modes: draft, fix, full, delta."""
import argparse, datetime, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import find_lesson
COLS = ["date", "lesson", "agent", "model", "effort", "mode", "round", "tokens", "input", "output", "cache_read", "cache_write", "seconds", "calls", "verdict"]
PRICES = {"opus": (4.0, 20.0), "sonnet": (2.0, 10.0), "haiku": (0.1, 0.5), "fable": (10.0, 50.0)}   # $ per MTok in, out; list prices 2026-10
CACHE_READ = {"opus": 0.20, "sonnet": 0.20, "haiku": 0.01, "fable": 0.25}
BASELINE = 473632          # fy3-9, 25 Oct 2026: two full review rounds + one fix pass, before packets and delta reviews


def log(a):
    f = find_lesson(a.id) / "review" / "usage.tsv"; f.parent.mkdir(exist_ok=True)
    row = [datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), a.id, a.agent, a.model, a.effort, a.mode, a.round,
           a.tokens, a.input or "", a.output or "", a.cache_read or "", a.cache_write or "", a.seconds, a.calls, a.verdict]
    new = not f.exists()
    with open(f, "a") as fh:
        if new: fh.write("\t".join(COLS) + "\n")
        fh.write("\t".join(str(x) for x in row) + "\n")
    print("logged", "\t".join(str(x) for x in row[2:]))


def cost(model, tokens, inp, out, cr):
    i, o = PRICES.get(model, PRICES["sonnet"])
    if inp or out: return ((inp or 0) * i + (out or 0) * o + (cr or 0) * CACHE_READ.get(model, 0.2)) / 1e6, True
    return (0.9 * tokens * i + 0.1 * tokens * o) / 1e6, False


def report(lid):
    f = find_lesson(lid) / "review" / "usage.tsv"
    if not f.exists(): sys.exit(f"{lid}: no review/usage.tsv yet")
    rows = [dict(zip(COLS, l.rstrip("\n").split("\t"))) for l in f.read_text().splitlines()[1:] if l.strip()]
    total = measured = 0; est_total = 0.0; exact = True
    print(f"{'agent':18} {'model':7} {'effort':7} {'mode':6} {'rnd':>3} {'tokens':>8} {'in':>7} {'out':>6} {'cache':>7} {'s':>5} {'calls':>5} verdict")
    for r in rows:
        t = int(r["tokens"] or 0); total += t
        c, ex = cost(r["model"], t, int(r["input"] or 0), int(r["output"] or 0), int(r["cache_read"] or 0)); est_total += c; exact &= ex
        print(f"{r['agent']:18} {r['model']:7} {r['effort']:7} {r['mode']:6} {r['round']:>3} {t:>8} {r['input']:>7} {r['output']:>6} {r['cache_read']:>7} {r['seconds']:>5} {r['calls']:>5} {r['verdict']}")
    rounds = max((int(r["round"] or 0) for r in rows), default=0)
    print(f"\ntotal {total} tokens in {len(rows)} runs, {rounds} review round(s); {100 * total / BASELINE:.0f} % of the fy3-9 baseline ({BASELINE})")
    print(f"cost {'' if exact else '≈ '}${est_total:.2f} at list prices" + ("" if exact else " (one total per run from the harness; 90 % input assumed)"))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("log"); l.add_argument("id")
    for k in ("agent", "model", "effort", "mode", "verdict"): l.add_argument(f"--{k}", required=True)
    for k in ("round", "tokens", "seconds", "calls"): l.add_argument(f"--{k}", type=int, required=True)
    for k in ("input", "output", "cache-read", "cache-write"): l.add_argument(f"--{k}", type=int)
    r = sub.add_parser("report"); r.add_argument("id")
    a = p.parse_args()
    log(a) if a.cmd == "log" else report(a.id)
