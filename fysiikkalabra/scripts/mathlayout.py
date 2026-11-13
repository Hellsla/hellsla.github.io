"""Layout of the maths in a solution (teacher's brief 2026-10-27, "pitkien laskuratkaisujen luettavuus").

A solution is written as the house rules say (NOTES.md §3 "Complete solutions"): one line per step, its bold label
first, the calculation as inline LaTeX: `**Sijoitus:** $Q = 4190 \\cdot 0{,}20 \\cdot 70\\,\\text{J} = 58\\,660\\,\\text{J}$`.
The source stays that way, so check_solutions.py, lint_lesson.py and the reviews read what they always read. This
module only decides how it shows:

- `chain_rows(tex)` splits a chain of relations at its top-level `=`, `\\approx`, `<`, `>` (never inside braces,
  `\\left…\\right`, `\\text{}` or an environment) into rows. The tokens are kept exactly, so every row is balanced
  LaTeX and the chain means what it meant. Anything it is not sure of (an `&`, a `\\\\`, `\\begin`, unbalanced braces)
  is left as it was. No other splitting is ever done.
- `display_chains(md)` shows a long chain (two relations or more, or one with a long side) as the rows of a
  calculation (`chain_html`, site.css .eq-chain): the relation signs in one column like an `aligned` block, but each
  side is inline maths that wraps after an operator on a narrow phone, never inside a number or a unit. A short
  formula stays inside its sentence.
- `align_equals(tex)` aligns a display `aligned` block written with every row starting at `&` at its equals signs,
  when that does not make it wider.
- `solution_md` / `steps_html` give each step of a solution a block of its own (.sol-step, its label on a line of
  its own) and set the answer apart (.sol-answer) from the reasons for its precision.
"""
import re

RELS = ("\\approx", "\\neq", "=", "<", ">", "\\le", "\\ge")
ALIGN_FIT = 28       # visible characters an aligned block may have, even when aligning makes it wider than as written (equals signs aligned, teacher 2026-11-13; fy4-2 overflowed a 360 px phone at 33)
LONG = 38            # raw LaTeX characters: a chain at least this long is shown as rows of its own
DISPLAY_STEPS = ("Kaava", "Muunnokset", "Sijoitus", "Järkevyys", "Kuvaajan lukeminen",   # solutions.md labels
                 "Yksikkömuunnokset", "Tulos", "Kaava ratkaistuna")                          # worked example stages


def _top_relations(tex):
    """Positions (start, end) of the relation signs at the top level of tex, or None when unsure."""
    if re.search(r"&|\\\\|\\begin|\\end", tex): return None
    out, depth, lr, i = [], 0, 0, 0
    while i < len(tex):
        c = tex[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", tex[i:])
            name = m.group(1)
            if name == "left": lr += 1
            elif name == "right": lr -= 1
            if depth == 0 and lr == 0 and "\\" + name in RELS and not re.match(r"[A-Za-z]", tex[i + len(m.group(0)):i + len(m.group(0)) + 1] or " "):
                out.append((i, i + len(m.group(0))))
            i += len(m.group(0)); continue
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0: return None
        elif c in "=<>" and depth == 0 and lr == 0: out.append((i, i + 1))
        i += 1
    return out if depth == 0 and lr == 0 else None


def chain_rows(tex):
    """`a = b \\approx c` -> [("a", "= b"), ("", "\\approx c")]: the rows of a calculation, each relation sign starting
    the row it belongs to, or None when tex is not a chain to split. Every part is balanced LaTeX on its own."""
    rels = _top_relations(tex)
    if not rels: return None
    first = tex[:rels[0][0]].strip()
    if not first: return None
    rows = []
    for k, (r0, r1) in enumerate(rels):
        end = rels[k + 1][0] if k + 1 < len(rels) else len(tex)
        rhs = tex[r1:end].strip()
        if not rhs: return None                                     # a relation with nothing after it
        rows.append(("" if k else first, tex[r0:r1] + " " + rhs))
    return rows


def vis_len(tex):
    """About how many characters wide tex renders: commands and braces dropped, a fraction as wide as its wider part."""
    t = re.sub(r"\\[dt]?frac\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}", lambda m: "x" * max(vis_len(m.group(1)), vis_len(m.group(2))), tex)
    t = re.sub(r"\\text\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\[,;:!]|\\quad|\\left|\\right|[{}]|\^|_", "", t)
    t = re.sub(r"\\[A-Za-z]+", "x", t)
    return len(t.replace(" ", ""))


def align_equals(tex):
    """An aligned block written with every row starting at `&` (left-aligned rows, `&Q = cm\\Delta T`, `&= 4190 …`):
    the `&` of each row that names its quantity moves to that row's first top-level relation, so the equals signs
    of the whole calculation stand in one column. Rows are not split or joined; a block with any other `&` stays."""
    m = re.fullmatch(r"(\s*\\begin\{aligned\}\s*)(.*?)(\s*\\end\{aligned\}\s*)", tex, re.S)
    if not m: return tex
    rows = re.split(r"(\\\\(?:\[[^\]]*\])?\s*)", m.group(2))
    cells = rows[0::2]
    if not all(r.lstrip().startswith("&") and r.count("&") == 1 for r in cells if r.strip()): return tex
    out, left, right = [], [0], [0]
    for r in cells:
        body = r.lstrip()[1:]
        rels = _top_relations(body)
        if rels and body[:rels[0][0]].strip():
            left.append(vis_len(body[:rels[0][0]])); right.append(vis_len(body[rels[0][0]:]))
            r = body[:rels[0][0]].rstrip() + " &" + body[rels[0][0]:]
        else: right.append(vis_len(body))
        out.append(r)
    if max(left) + max(right) > max(ALIGN_FIT, 1.05 * max(vis_len(c) for c in cells)): return tex   # aligned it would be wider than a phone (and than the block as written): as written
    rows[0::2] = out
    return m.group(1) + "".join(rows) + m.group(3)


WIDE_LHS = 20        # visible characters: a left side up to this long shares the column with its relations on a wide screen
WIDE_MAX = 40        # visible characters (vis_len) a row joined for a wide screen may have: it must fit a 768 px task card (fy5-6 overflowed at 62, fy8-11 at 46)


def join_wide(tex):
    """An aligned block whose chains the source split by hand (`&a \\\\ &\\quad = b`, teacher 2026-11-13, fy3-6; `&\\rho g h
    \\\\ &= 1000 \\\\ &\\quad \\cdot 9{,}81`, fy3-4): the same block with the pieces of one side joined, as long as the
    joined row stays within WIDE_MAX, or None when nothing joins. A row starting `&\\quad` or `&\\qquad` (a continuation of
    the row before) joins it; a row starting with a relation joins a row that is still only a left side, so `left =
    right` is one row. Each further relation of the chain keeps its own row, and a row break with a gap (`\\\\[6pt]`)
    ends the chain. The source is never changed; build.py shows this form on a wide screen and the form as written on a
    phone (.mj-wide / .mj-narrow in site.css)."""
    m = re.fullmatch(r"(\s*\\begin\{aligned\}\s*)(.*?)(\s*\\end\{aligned\}\s*)", tex, re.S)
    if not m: return None
    parts = re.split(r"(\\\\(?:\[[^\]]*\])?\s*)", m.group(2))
    cells, seps = parts[0::2], parts[1::2] + [""]
    out, out_seps, joined = [], [], False
    for cell, sep in zip(cells, seps):
        body = cell.lstrip()[1:].strip() if cell.lstrip().startswith("&") and cell.count("&") == 1 else None
        piece = None
        if out and body is not None and re.fullmatch(r"\\\\(?:\[[^\]]*\])?\s*", out_seps[-1]) and out_seps[-1].strip() == "\\\\":
            q = re.match(r"\\q?quad\s*(.*)", body, re.S)
            if q and q.group(1).strip(): piece = q.group(1).strip()
            elif re.match(r"(=|\\approx)\s", body):
                prev = out[-1].lstrip()[1:]
                if _top_relations(prev) == []: piece = body        # the row before is only a left side
        if piece and vis_len(out[-1]) + vis_len(piece) + 2 <= WIDE_MAX:
            out[-1] = out[-1].rstrip() + " " + piece + " "; out_seps[-1] = sep; joined = True
        else: out.append(cell); out_seps.append(sep)
    if not joined: return None
    return m.group(1) + "".join(c + s for c, s in zip(out, out_seps)) + m.group(3)


def wide_narrow_html(tex):
    """Display maths `tex` as both forms when join_wide changes it: `<span class="mj-wide">$$…$$</span><span
    class="mj-narrow">$$…$$</span>`; site.css shows one of them by the width of the screen. Otherwise just `$$tex$$`."""
    wide = join_wide(tex)
    if not wide: return None
    return f'<span class="mj-wide">$${align_equals(wide)}$$</span><span class="mj-narrow">$${align_equals(tex)}$$</span>'


def split_list(tex):
    """An inline list of values, `p = 203;\\ 159;\\ 134\\,\\text{kPa}`, as one formula per item ("$p = 203$; $159$;
    …") so a phone can wrap between the items; the semicolons are the list's punctuation, so the meaning is unchanged.
    Returns the inline maths with its dollars, or None when there is no top-level `;` list."""
    depth, cuts = 0, []
    for i, c in enumerate(tex):
        if c == "{": depth += 1
        elif c == "}": depth -= 1
        elif c == ";" and depth == 0 and (i == 0 or tex[i - 1] != "\\") and re.match(r";\s*\\[ ,;:]?", tex[i:i + 3]): cuts.append(i)
    if not cuts: return None
    items, last = [], 0
    for c in cuts:
        items.append(tex[last:c].strip()); last = c + 1 + len(re.match(r"\s*(\\[ ,;:])?\s*", tex[c + 1:]).group(0))
    items.append(tex[last:].strip())
    if any(not x for x in items): return None
    return "; ".join(f"${x}$" for x in items)


def is_long(tex):
    """A formula that does not read well inside a sentence: a chain of two relations or more, or one relation with a
    long side (a big fraction, a product of values with units)."""
    rels = _top_relations(tex)
    if not rels: return False
    return len(rels) >= 2 and len(tex) >= LONG or len(tex) >= 2 * LONG or (re.search(r"\\d?frac", tex) and len(tex) >= LONG)


def chain_html(rows, gap_before=(), force=False, narrow=False):
    """A calculation as rows (site.css .eq-chain): the left side, then the relation and the right side. The relation
    signs stand in one column, like an aligned block, but each side is inline maths that can wrap after an operator
    on a narrow phone, so a long row never runs off the screen and no number or unit is cut. A long left side (a sum
    of terms) stands on a line of its own, and its relations follow indented under it; one that is not very long does so
    only on a phone, and on a wide screen shares the column (a second chain with `mj-wide`/`mj-narrow`)."""
    lead = any(lhs and vis_len(lhs) > 10 for lhs, _ in rows)
    if lead and not force and max(vis_len(lhs) for lhs, _ in rows) <= WIDE_LHS:
        # a long left side stands on a line of its own only on a phone; on a wide screen it is one column with the
        # relations after it, `left = right` on one row (teacher 2026-11-13, fy3-6 reasonableness check)
        return (chain_html(rows, gap_before, True, False).replace('class="eq-chain', 'class="eq-chain mj-wide', 1)
                + chain_html(rows, gap_before, True, True).replace('class="eq-chain', 'class="eq-chain mj-narrow', 1))
    lead = lead and (force is not True or narrow)
    out = []
    for i, (lhs, rhs) in enumerate(rows):
        gap = " gap" if i in gap_before else ""
        if lead and lhs: out.append(f'<div class="eq-lead{gap}">${lhs}$</div>'); lhs, gap = "", ""
        out.append(f'<div class="eq-row{gap}"><span class="eq-l">' + (f"${lhs}$" if lhs else "") + f'</span><span class="eq-r">${rhs}$</span></div>')
    return f'<div class="eq-chain{" lead" if lead else ""}">' + "".join(out) + "</div>"


JOIN = r"\s*(?:ja|sekä|and|,)?\s*"


def _short_chain(p):
    """The rows of an inline formula `$a = b$` that has a left side, else None."""
    if not (p.startswith("$") and p.endswith("$")) or p.startswith("$$"): return None
    rows = chain_rows(p[1:-1])
    return rows if rows and rows[0][0] else None


def display_chains(text):
    """Every long inline formula of a step's text on lines of its own, as the rows of a calculation (chain_html); the
    text before and after it stays a sentence. Two calculations joined only by "ja" form one block, also when the
    first of them is short (it would otherwise end the sentence in a dangling "ja"). Display maths
    already written as $$…$$ is left alone."""
    parts = re.split(r"(\$\$.*?\$\$|\$[^$\n]+?\$)", text, flags=re.S)
    out, pending, gaps = [], [], []
    def flush():
        if pending: out.append("\n\n" + chain_html(pending, set(gaps)) + "\n\n"); pending.clear(); gaps.clear()
    for p in parts:
        rows = chain_rows(p[1:-1]) if p.startswith("$") and not p.startswith("$$") and is_long(p[1:-1]) else None
        if rows:   # a formula with no left side ("= 5 J" after "ja") stays inline (2026-10-28, fy2-5, fy2-6)
            if not pending and len(out) >= 2 and re.fullmatch(JOIN, out[-1]) and (short := _short_chain(out[-2])):
                # "$a = b$ ja $c = d = e$": the short calculation joins the block instead of a sentence ending in "ja"
                # (teacher 2026-11-03, fy2-6 Yksikkömuunnokset)
                out[-2:] = []; pending.extend(short)
            if pending: gaps.append(len(pending))
            pending.extend(rows)
        elif pending and re.fullmatch(JOIN, p): continue                  # "… ja …" between two calculations
        else: flush(); out.append(p)
    flush()
    s = "".join(out)
    s = re.sub(r"\n\n[,;.]\s*(?=\S)", "\n\n", s)                 # a comma or full stop right after the block would only dangle
    s = re.sub(r"\n\n[,;.]\s*$", "", s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


STEP_RE = re.compile(r"^\*\*([^*\n]+?)([:.])\*\*\s*", re.M)


def solution_md(text, display_steps=DISPLAY_STEPS):
    """A solutions.md block (or an inquiry numeric task's solution) as markdown with each step a paragraph group:
    `<!--step:Label-->` markers that steps_html turns into blocks, long chains in display rows."""
    chunks = STEP_RE.split(text.strip())
    if len(chunks) < 4: return text                                 # not a stepwise solution: as written
    out = [chunks[0].strip()] if chunks[0].strip() else []
    for k in range(1, len(chunks), 3):
        label, body = chunks[k].strip(), chunks[k + 2].strip()
        if label in display_steps: body = display_chains(body)
        out.append(f"<!--step:{label}-->\n\n{body}")
    return "\n\n".join(out)


def steps_html(html, answer_label="Vastaus"):
    """The rendered markers -> one block per step: `<div class="sol-step"><p class="sol-label">Sijoitus</p>…</div>`.
    The Vastaus step shows its first formula as the answer (.sol-answer) and the reasons for its precision after it."""
    pieces = re.split(r"(?:<p>)?<!--step:(.*?)-->(?:</p>)?", html)
    if len(pieces) < 3: return html
    out = pieces[0]
    for k in range(1, len(pieces), 2):
        label, body = pieces[k], pieces[k + 1].strip()
        key = re.sub(r"\W+", "-", label.lower()).strip("-")
        if label == answer_label:
            m = re.match(r"<p>(\$[^$]+\$)\s*[,.]?\s*(.*?)</p>", body, re.S)
            if m:
                rest = m.group(2).strip()
                body = (f'<p class="sol-answer">{m.group(1)}</p>' + (f"<p>{rest[0].upper() + rest[1:]}</p>" if rest else "")
                        + body[m.end():])
        out += f'<div class="sol-step" data-step="{key}"><p class="sol-label">{label}</p>{body}</div>'
    return out


if __name__ == "__main__":                                          # quick self-test
    assert chain_rows(r"Q = cm\Delta T = 4190 \cdot 0{,}20 = 58\,660\,\text{J}") == [("Q", "= cm\\Delta T"), ("", "= 4190 \\cdot 0{,}20"), ("", "= 58\\,660\\,\\text{J}")]
    assert chain_rows(r"\left(a = b\right)") is None and chain_rows(r"a & = b") is None
    assert "chain" not in display_chains(r"ja $= 4190 \cdot 0{,}20 \cdot 1000 \cdot 3600 \cdot 7{,}5 \cdot 10^{6}\,\text{J} \approx 1\,\text{J}$ eli")
    assert chain_rows(r"T = \dfrac{x = 1}{2} \approx 3") == [("T", "= \\dfrac{x = 1}{2}"), ("", "\\approx 3")]
    assert vis_len(r"4190\,\tfrac{\text{J}}{\text{kg}}") == 6
    assert _top_relations(r"\left. a \right|_{x=1} = 2") == [(len(r"\left. a \right|_{x=1} "), len(r"\left. a \right|_{x=1} ") + 1)]
    assert _top_relations(r"a \leq b") == [] and _top_relations(r"a \le b")
    assert align_equals("\\begin{aligned}\n&Q = c m \\\\\n&= 4 \\\\[6pt]\n&\\quad + 1\n\\end{aligned}") == "\\begin{aligned}\nQ &= c m \\\\\n&= 4 \\\\[6pt]\n&\\quad + 1\n\\end{aligned}"
    assert split_list(r"p = 203;\ 159;\ 66\,\text{kPa}") == r"$p = 203$; $159$; $66\,\text{kPa}$" and split_list(r"\{a;b\}") is None
    j = join_wide("\\begin{aligned}\n&a b \\\\\n&\\quad = c d \\\\[6pt]\n&e = f\n\\end{aligned}")
    assert j == "\\begin{aligned}\n&a b = c d \\\\[6pt]\n&e = f\n\\end{aligned}", j                 # a hand-split chain joins, the gap stays
    assert join_wide("\\begin{aligned}\n&a \\\\\n&\\quad \\cdot b\n\\end{aligned}") == "\\begin{aligned}\n&a \\cdot b \n\\end{aligned}"   # a continuation joins
    h = join_wide("\\begin{aligned}\n&\\rho g h \\\\\n&= 1000\\,\\tfrac{\\text{kg}}{\\text{m}^3} \\\\\n&\\quad \\cdot 9{,}81 \\\\\n&\\quad \\cdot 12 \\\\\n&= 117\\,720 \\\\[6pt]\n&p = p_0 \\\\\n&= 1 \\\\\n&\\quad + 2\n\\end{aligned}")
    assert h.count("\\\\") == 3 and "&\\rho g h = 1000" in h and "\\cdot 12 \\\\\n&= 117" in h and "&= 1 + 2" in h, h   # left = right on one row, each further = on its own
    assert join_wide("\\begin{aligned}\n&" + "x" * 50 + " \\\\\n&\\quad = " + "y" * 20 + "\n\\end{aligned}") is None   # too wide stays two rows
    assert wide_narrow_html("\\begin{aligned}\n&a \\\\\n&\\quad = b\n\\end{aligned}").count("$$") == 4
    assert align_equals("\\begin{aligned}\n&\\Delta U = Q + W \\\\\n&= -40\\,\\text{J} + 150\\,\\text{J} \\\\\n&= 110\\,\\text{J}\n\\end{aligned}").count("&=") == 3   # equals signs always in one column, also when it widens the block
    c = display_chains(r"Tarkistus: $0{,}300\,\text{kg} \cdot 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} = 1257\,\tfrac{\text{J}}{\text{K}}$ ja $0{,}200\,\text{kg} \cdot 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \approx 75\,\tfrac{\text{J}}{\text{K}}$.")
    assert c.count("eq-chain mj-wide") == 1 and c.count("eq-chain mj-narrow lead") == 1, c      # a short chain, also with \approx: one row on a wide screen
    w = chain_html([("c_\\text{v} m_\\text{v} (T_\\text{v} - T)", "= x")]); assert "mj-wide" not in w   # a short left side needs no second form
    j3 = join_wide("\\begin{aligned}\n&c_\\text{v} m_\\text{v} (T_\\text{v} - T) \\\\\n&\\quad = c_\\text{j} m_\\text{j} \\Delta T_\\text{j} + s m_\\text{j} \\\\\n&\\qquad + c_\\text{v} m_\\text{j} T\n\\end{aligned}")
    assert j3 and j3.count("\\\\") == 0, j3                                                     # the three rows of an energy balance: one equation, one row
    b = display_chains(r" $14\,\text{GWh} = {14 \cdot 10^{6}}\,\text{kWh}$ ja $5{,}0\,\text{MW} = 5{,}0 \cdot 1000\,\text{kW} = 5000\,\text{kW}$.")
    assert b.startswith('<div class="eq-chain') and "ja" not in b and b.count("eq-row") == 3 and "eq-row gap" in b, b
    print("ok")
