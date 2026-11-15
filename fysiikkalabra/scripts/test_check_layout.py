"""Test of the clipped-formula check in scripts/check_layout.py (work queue 5b, teacher 2026-11-15).

A calculation row or an inline formula that has to be scrolled to is cut off in a screenshot, and the visual reviewer
rejected three rounds of fy8-1 and fy8-2 solutions for it ("m/s" cut to "m/") while check_layout.py said OK. This builds
fixture pages from a real built page and the formulas of those findings (fy8-2 L2-09 and L3-06, #593; fy8-1 L2-08, #590),
opened as a solution at 360 px, and checks that
  - each clipped formula fails, in a calculation row and as an inline formula;
  - the same calculations broken into rows, and short formulas, pass (no false alarm);
  - the check is not tied to a language (the same formula with a decimal comma and a decimal point).
Usage: python scripts/test_check_layout.py"""
import pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent / "site"
failures = []


def expect(name, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"  -> {detail}"))
    if not ok: failures.append(name)


def chain(*rows):
    """A calculation set as rows, as mathlayout.chain_html writes it: (left side, right side) per row."""
    return '<div class="eq-chain">' + "".join(f'<div class="eq-row"><span class="eq-l">{l}</span><span class="eq-r">{r}</span></div>' for l, r in rows) + "</div>"


def solution(*blocks):
    return ('<details class="level"><summary>Taso 2</summary><ol><li><div class="numeric"><details class="solution"><summary>Näytä ratkaisu</summary><div class="steps"><div class="sol-step"><p class="sol-label">Substitution</p>'
            + "".join(blocks) + "</div></div></details></div></li></ol></details>")


FIXTURES = {
    # fy8-2 L2-09 (#593): the row ends "... 10^8 m/s" and was cut to "m/"
    "fx-bad-row": solution(chain(("$hc$", r"$= 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} \cdot 1{,}000 \cdot 10^{0}$"))),
    # fy8-2 L3-06: the denominator "405 nm · 1,602·10^-19 J/eV" ran out of the box
    "fx-bad-denominator": solution(chain((r"$E_\text{viol}$", r"$= \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{405 \cdot 10^{-9}\,\text{m} \cdot 1{,}602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}} \cdot 1{,}000}$"))),
    # fy8-2 L2-09 Järkevyys: an inline formula that cannot wrap, scrolled on its own line, "eV" cut
    "fx-bad-inline": solution(r"<p>Likiarvo $1240\,\text{eV}\,\text{nm} : 436\,\text{nm} \approx 2{,}84\,\text{eV} \approx 2{,}8\,\text{eV}$ antaa saman tuloksen kuin laskettu arvo.</p>"),
    # fy8-1 L2-08 (#590, en, round 1): the unit Hz at the end of the chain cut off
    "fx-bad-hz": solution(chain((r"$E_\text{k,max}$", r"$= 0.4136\,\tfrac{\text{eV}}{10^{14}\,\text{Hz}} \cdot (12 - 5.56) \cdot 10^{14}\,\text{Hz} = 2.66\,\text{eV}$"))),
    # the same calculations broken into rows, and short formulas: nothing to report
    "fx-good-rows": solution(chain(("$hc$", r"$= 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$"), ("", r"$\cdot 2{,}998 \cdot 10^{8}\,\text{m/s}$"), ("", r"$= 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$")),
                             chain((r"$E_\text{viol}$", r"$= \dfrac{hc}{\lambda}$"), ("", r"$= \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{405 \cdot 10^{-9}\,\text{m}}$"), ("", r"$= 4{,}905 \cdot 10^{-19}\,\text{J}$"))),
    "fx-good-short": solution(r"<p>Likiarvo $E = hc/\lambda \approx 2{,}84\,\text{eV} \approx 2{,}8\,\text{eV}$ antaa saman tuloksen.</p>", chain(("$E$", r"$= 2{,}84\,\text{eV}$"))),
}


def main():
    base = (SITE / "fy8-2.html")
    if not base.is_file(): sys.exit("site/fy8-2.html is needed as the base page of the fixtures")
    page = base.read_text()
    tmp = pathlib.Path(tempfile.mkdtemp())
    try:
        for f in SITE.iterdir():
            if f.suffix != ".html" and not f.name.startswith("."): (tmp / f.name).symlink_to(f)   # styles, scripts, fonts, KaTeX
        for name, html in FIXTURES.items():
            (tmp / f"{name}.html").write_text(re.sub(r"(<main[^>]*>).*(</main>)", lambda m: f'{m.group(1)}<article class="inquiry"><section class="stage"><div class="activity act-theory">{html}</div></section></article>{m.group(2)}', page, count=1, flags=re.S))
        for width in (360, 390):
            for name in FIXTURES:
                r = subprocess.run([sys.executable, str(HERE / "check_layout.py"), name, "--width", str(width), "--dir", str(tmp)], capture_output=True, text=True)
                out = r.stdout + r.stderr
                if name.startswith("fx-bad"):
                    expect(f"{name} at {width} px: a clipped formula fails the layout check", r.returncode == 1 and "clipped" in out, out)
                else:
                    expect(f"{name} at {width} px: formulas that fit give no alarm", r.returncode == 0 and "clipped" not in out, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{len(failures)} FAILED: " + ", ".join(failures) if failures else "\nall check_layout tests passed")
    sys.exit(1 if failures else 0)


main()
