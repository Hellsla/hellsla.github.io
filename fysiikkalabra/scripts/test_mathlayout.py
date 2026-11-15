"""A sentence mark after display maths belongs to the formula's last row (work queue 5e): `$$a = b$$.` never leaves
the full stop alone at the start of the next line. Usage: python scripts/test_mathlayout.py"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mathlayout as ml


def stash(text):
    """What build.render_md swaps each formula of text for (the same substitution), with the rest of the text kept."""
    def f(m):
        return ml.display_html(m.group(1), m.group(2) or "") if m.group(0).startswith("$$") else m.group(0)
    return re.sub(ml.DISPLAY_OR_INLINE, f, text, flags=re.S)


def check(got, want, name):
    ok = got == want
    print("OK  " if ok else "FAIL", name, "" if ok else f"\n  got  {got!r}\n  want {want!r}")
    return ok


results = [
    check(stash("$$a = b$$."), "$$a = b\\text{.}$$", "full stop moves into the formula"),
    check(stash("$$a=b$$, joten c"), "$$a=b\\text{,}$$ joten c", "comma moves in, the text continues"),
    check(stash("$$a = b$$.\n\nSeuraava"), "$$a = b\\text{.}$$\n\nSeuraava", "end of paragraph"),
    check(stash("$$a = b$$ ja c."), "$$a = b$$ ja c.", "no mark right after: unchanged"),
    check(stash("$$x$$.5"), "$$x$$.5", "a mark inside a number is not moved"),
    check(stash("Inline $a = b$. ja $c$, ok"), "Inline $a = b$. ja $c$, ok", "inline maths is unchanged"),
    check(stash("$$\\begin{aligned}a &= b \\\\ &= c\\end{aligned}$$."),
          "$$\\begin{aligned}a &= b \\\\ &= c\\text{.}\\end{aligned}$$", "aligned: the last row gets the mark"),
    check(stash("$$\\begin{aligned}a &= b \\\\ &\\quad = c\\end{aligned}$$;"),
          '<span class="mj-wide">$$\\begin{aligned}a &= b = c\\text{;} \\end{aligned}$$</span>'
          '<span class="mj-narrow">$$\\begin{aligned}a &= b \\\\ &\\quad = c\\text{;}\\end{aligned}$$</span>',
          "a hand-split chain: the mark in both the wide and the narrow form"),
]
sys.exit(0 if all(results) else 1)
