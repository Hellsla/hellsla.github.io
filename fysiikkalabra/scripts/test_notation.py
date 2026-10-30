"""Vector notation everywhere (project rule 14, teacher 2026-10-29): a vector is \\overline{F}, never \\vec{F},
\\mathbf{F}, \\boldsymbol{F} or \\overrightarrow{F}. lint_lesson.py checks a lesson's maths; this test covers every
source a student can see, in every language: lesson and exercise texts, inquiry and Sovella files, figures.py and the
figure texts, the simulations (sim.js) and the interface strings (lang/*.json). Bold numbers (\\mathbf{12}) in a
readout are not vectors and pass. Reviews and packets are reports about the text, not the text, and are skipped.
Usage: python scripts/test_notation.py   (exit 1 with file:line for each finding)"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
BAD = re.compile(r"\\{1,2}(?:vec|overrightarrow|boldsymbol)\s*\{|\\{1,2}mathbf\s*\{\s*[A-Za-z\\]")
SOURCES = [("content", "*.md"), ("content", "*.json"), ("lessons", "*.md"), ("lessons", "*.json"), ("lessons", "*.py"),
           ("lessons", "*.js"), ("assets/sims", "*.js"), ("lang", "*.json")]


def findings():
    out = []
    for top, pat in SOURCES:
        for f in sorted((ROOT / top).rglob(pat)):
            if "review" in f.parts: continue
            for i, line in enumerate(f.read_text(errors="replace").splitlines(), 1):
                for m in BAD.finditer(line):
                    out.append(f"{f.relative_to(ROOT)}:{i}: {line[max(0, m.start() - 20):m.end() + 20].strip()}")
    return out


if __name__ == "__main__":
    assert BAD.search(r"$\vec{F}$") and BAD.search(r"'$\\mathbf{v}$'") and BAD.search(r"\overrightarrow{AB}")
    assert not BAD.search(r"$\overline{F}_\mu$") and not BAD.search(r"\\mathbf{${Math.round(W)}}") and not BAD.search(r"\mathbf{12}")
    bad = findings()
    for b in bad: print(b)
    print(f"{len(bad)} vector symbols not written with an overline" if bad else "ok   every vector is written \\overline{…} (rule 14)")
    sys.exit(1 if bad else 0)
