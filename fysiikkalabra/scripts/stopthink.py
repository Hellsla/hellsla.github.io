"""Pysähdy ja mieti (```pysahdy fence; teacher 2026-11-17, pilot fy4-3, fy4-4, fy4-6): one short question after a theory
subsection that the student can answer from the paragraph just read, and an openable answer. No field, lock, checklist or storage.

    ```pysahdy
    Question text.
    ---
    Answer text (1-2 sentences).
    ```
"""
import html, re

STOP = re.compile(r"```pysahdy\n(.*?)```", re.S)


def parts(body):
    """(question, answer) of a fence body: the question, a line `---`, the answer."""
    q, _, a = body.partition("\n---\n")
    return " ".join(q.split()), " ".join(a.split())


def as_html(text, label, answer):
    """Each fence as <aside class="stop-think">: a small heading, the question, <details><summary>Vastaus</summary>. Its
    maths stays $...$ for build.py's stash."""
    def one(m):
        q, a = parts(m.group(1))
        return (f'\n\n<aside class="stop-think"><p class="stop-think-label">{html.escape(label)}</p><p class="stop-think-q">{q}</p>'
                f'<details class="stop-think-a"><summary>{html.escape(answer)}</summary><p>{a}</p></details></aside>\n\n')
    return STOP.sub(one, text)


def n_blocks(text):
    return len(STOP.findall(text))
