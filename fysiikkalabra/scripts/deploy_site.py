#!/usr/bin/env python3
"""Assemble the public copy of Ruukkilabra for https://ruukkilab.fi/ (teacher 2026-11-04).

The source stays in this repository; the workflow .github/workflows/ruukkilabra-deploy.yml runs this script after the
fysiikkalabra-ci run of an approved main commit has passed, and pushes the result to the separate public repository
that GitHub Pages serves at the domain. The published root is the committed site/ folder, so the front page is
https://ruukkilab.fi/ and every relative link works as it does under site/.

    python scripts/deploy_site.py OUT [--models DIR]

OUT is a checkout of the publishing repository: everything in it except .git is replaced. --models is a checkout of
the read-aloud model repository; its folders supertonic3-v1/ and ort/ are published under models/ (same origin as
the pages, so no CORS). Without --models the models/ folder already in OUT is kept as it is.

Added beside the pages: CNAME (the custom domain), .nojekyll (serve the files as they are), robots.txt and
sitemap.xml. Then two gates, and the script exits 1 (nothing is pushed) if either fails:
- privacy: no published text file may name the teacher's other sites (hellsla.github.io, github.com/Hellsla);
  Ruukkilabra must never lead to them (teacher 2026-11-04);
- links: every relative href/src in the pages and every url() in the stylesheets resolves to a file inside the
  published root (font fallbacks .woff/.ttf of KaTeX, which browsers never fetch beside .woff2, are only counted).
"""
import argparse, os, pathlib, re, shutil, sys, urllib.parse

DOMAIN = "ruukkilab.fi"
BASE = f"https://{DOMAIN}/"
ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
MODEL_DIRS = ("supertonic3-v1", "ort")
FORBIDDEN = re.compile(r"hellsla\.github\.io|github\.com/hellsla", re.I)
TEXT = {".html", ".js", ".mjs", ".css", ".json", ".svg", ".txt", ".md", ".xml", ".webmanifest"}
REF = re.compile(r"""\s(?:href|src|poster)\s*=\s*["']([^"']+)["']""")
CSS_URL = re.compile(r"""url\(\s*["']?([^"')]+?)["']?\s*\)""")


def clear(out):
    for p in out.iterdir():
        if p.name == ".git" or p.name == "models":
            continue
        shutil.rmtree(p) if p.is_dir() and not p.is_symlink() else p.unlink()


def copy_models(src, out):
    dest = out / "models"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir()
    for d in MODEL_DIRS:
        if not (src / d).is_dir():
            sys.exit(f"deploy_site: {src / d} is missing")
        shutil.copytree(src / d, dest / d)


def pages(out):
    return sorted(p for p in out.rglob("*.html") if ".git" not in p.parts and "models" not in p.relative_to(out).parts)


def write_extras(out):
    (out / "CNAME").write_text(DOMAIN + "\n")
    (out / ".nojekyll").write_text("")
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    urls = []
    for p in pages(out):
        rel = p.relative_to(out).as_posix()
        if rel.split("/")[-1] == "index.html":
            rel = rel[: -len("index.html")]
        urls.append(f"  <url><loc>{BASE}{urllib.parse.quote(rel)}</loc></url>")
    (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
                                     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + "\n".join(urls) + "\n</urlset>\n")
    return len(urls)


def check_privacy(out):
    bad = []
    for p in out.rglob("*"):
        if ".git" in p.parts or not p.is_file() or p.suffix.lower() not in TEXT:
            continue
        for n, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
            m = FORBIDDEN.search(line)
            if m:
                bad.append(f"{p.relative_to(out)}:{n}: {m.group(0)}")
    return bad


def check_links(out):
    missing, fallback = [], 0
    root = out.resolve()
    files = pages(out) + sorted(p for p in out.rglob("*.css") if ".git" not in p.parts)
    for f in files:
        text = f.read_text(errors="ignore")
        refs = REF.findall(text) if f.suffix == ".html" else []
        refs += CSS_URL.findall(text)
        for r in refs:
            r = r.strip()
            if not r or r.startswith(("#", "data:", "mailto:", "javascript:", "blob:", "tel:")) or "${" in r or "{{" in r:
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", r, re.I) or r.startswith("//"):
                continue
            path = urllib.parse.unquote(r.split("#")[0].split("?")[0])
            if not path:
                continue
            target = (root / path.lstrip("/")) if path.startswith("/") else (f.resolve().parent / path)
            target = pathlib.Path(os.path.normpath(target))
            if target != root and root not in target.parents:
                missing.append(f"{f.relative_to(out)} -> {r} (outside the site)")
            elif not target.exists():
                if f.suffix == ".css" and target.suffix in (".woff", ".ttf") and target.with_suffix(".woff2").exists():
                    fallback += 1
                else:
                    missing.append(f"{f.relative_to(out)} -> {r}")
    return missing, fallback


def check_canonical(out):
    bad = []
    for p in pages(out):
        m = re.search(r'<link rel="canonical" href="([^"]+)"', p.read_text(errors="ignore"))
        if m and not m.group(1).startswith(BASE):
            bad.append(f"{p.relative_to(out)}: canonical {m.group(1)}")
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("out", type=pathlib.Path)
    ap.add_argument("--models", type=pathlib.Path)
    ap.add_argument("--site", type=pathlib.Path, default=SITE)
    a = ap.parse_args()
    out = a.out
    out.mkdir(parents=True, exist_ok=True)
    clear(out)
    for p in a.site.iterdir():
        (shutil.copytree if p.is_dir() else shutil.copy2)(p, out / p.name)
    if a.models:
        copy_models(a.models, out)
    n = write_extras(out)
    privacy, canon = check_privacy(out), check_canonical(out)
    missing, fallback = check_links(out)
    print(f"deploy_site: {n} pages, models/ {'from ' + str(a.models) if a.models else 'kept as it was'}"
          f"; {fallback} KaTeX font fallbacks (.woff/.ttf beside .woff2) not published, as before")
    for title, items in (("names another site of the teacher (privacy rule 2026-11-04)", privacy),
                         ("canonical address is not on " + DOMAIN, canon), ("broken relative link", missing)):
        for i in items[:50]:
            print(f"FAIL {title}: {i}")
        if len(items) > 50:
            print(f"FAIL ... and {len(items) - 50} more")
    if privacy or canon or missing:
        sys.exit(1)
    print("deploy_site: PASS")


if __name__ == "__main__":
    main()
