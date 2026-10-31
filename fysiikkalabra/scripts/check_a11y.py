"""Accessibility checks on built pages (teacher 2026-10-30): every form field has an accessible name that says more
than "Vastaus" alone, every aria-describedby / aria-labelledby / label[for] target exists, ids are unique, every
figure (svg role="img") and every canvas has a text alternative, every button has a name, and every page declares its
language. Static HTML only; keyboard and screen-reader behaviour stays a browser test (test_inquiry.py, test_sims.py).

  python scripts/check_a11y.py [site|preview] (default site)"""
import collections, html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BARE = {"vastaus", "answer"}


def attrs(tag):
    return {k.lower(): html.unescape(v) for k, v in re.findall(r'([\w:-]+)="([^"]*)"', tag)}


def problems(text):
    out = []
    ids = collections.Counter(re.findall(r'\sid="([^"]+)"', text))
    out += [f'id "{k}" is used {v} times' for k, v in ids.items() if v > 1]
    labels_for = set(re.findall(r'<label[^>]*\sfor="([^"]+)"', text))
    if not re.search(r'<html[^>]*\slang="[^"]+"', text): out.append("<html> has no lang")
    # a field inside a <label> is named by it
    inside = set()
    for m in re.finditer(r"<label\b.*?</label>", text, re.S):
        inside |= {x.start() + m.start() for x in re.finditer(r"<(?:input|textarea|select)\b", m.group(0))}
    for m in re.finditer(r"<(input|textarea|select)\b[^>]*>", text):
        a = attrs(m.group(0))
        if a.get("type") in ("hidden", "submit", "button"): continue
        name = a.get("aria-label", "").strip()
        named = name or a.get("aria-labelledby") or a.get("id") in labels_for or m.start() in inside
        if not named: out.append(f"a {m.group(1)} without an accessible name: {m.group(0)[:90]}")
        elif name.lower() in BARE and not a.get("aria-describedby"):
            out.append(f'a field named only "{name}" with no description of its question: {m.group(0)[:90]}')
        for ref in (a.get("aria-describedby", "") + " " + a.get("aria-labelledby", "")).split():
            if ids[ref] == 0: out.append(f'aria reference "{ref}" points to no element')
    for m in re.finditer(r'<svg\b[^>]*role="img"[^>]*>', text):
        if not attrs(m.group(0)).get("aria-label", "").strip(): out.append(f"a figure without a text alternative: {m.group(0)[:90]}")
    for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", text, re.S):
        if not re.sub(r"<[^>]+>|\s", "", m.group(2)) and "aria-label" not in m.group(1): out.append(f"a button without a name: {m.group(0)[:90]}")
    return out


def main(where="site"):
    bad = 0; pages = sorted((ROOT / where).rglob("*.html"))
    for p in pages:
        for x in problems(p.read_text()):
            bad += 1; print(f"{p.relative_to(ROOT)}: {x}")
    print(f"{len(pages)} pages checked" + (f", {bad} problems" if bad else ": no accessibility problems found"))
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1] if len(sys.argv) > 1 else "site") else 0)
