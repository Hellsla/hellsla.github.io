"""Small decorative illustrations for the tip pages (Kuuntele ja katso, Kirjavinkit; teacher 2026-11-18, 4c).
Inline SVG, 48 x 48, the module-icon family: thin forest-green outlines, one terracotta accent, no text, aria-hidden.
They wait for the teacher's approval like every new figure (docs/teacher-figures.tsv; nobody marks them approved but the teacher)."""
G, A, T = "#1a4d2e", "#b8532f", "#ecf5ee"
_S = f'fill="none" stroke="{G}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
_L = f'stroke="{G}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
_ACC = f'fill="none" stroke="{A}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"'
_DOT = f'fill="{A}" stroke="none"'


def _atom(cx, cy, rx, ry, nucleus=2.6, orbits=(0, 60, 120)):
    o = "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({a} {cx} {cy})"/>' for a in orbits)
    return f'<g {_S}>{o}</g><circle cx="{cx}" cy="{cy}" r="{nucleus}" {_DOT}/>'


ART = {
    "FY1": (f'<circle cx="22" cy="18" r="8" fill="{T}" {_L}/><ellipse cx="22" cy="18" rx="15" ry="4.5" transform="rotate(-20 22 18)" {_ACC}/>'
            f'<circle cx="40" cy="8" r="1.6" {_DOT}/><circle cx="7" cy="9" r="1.2" {_DOT}/>'
            f'<g {_S}><rect x="5" y="35" width="38" height="7" rx="1.5" fill="{T}"/><path d="M11 35v3.5M17 35v5M23 35v3.5M29 35v5M35 35v3.5"/></g>'),
    "FY2": (f'<g {_S}><path d="M24 22v20M17 42h14"/><circle cx="24" cy="20" r="2.4" fill="{T}"/></g>'
            f'<g {_ACC}><path d="M24 17.6V5M26.1 21.2l11.3 6.5M21.9 21.2l-11.3 6.5"/></g>'
            f'<path d="M39 8l-4 7h5l-4 7" {_ACC} stroke-width="1.8"/>'),
    "FY3": (f'<g {_S}><rect x="9" y="5" width="9" height="28" rx="4.5" fill="{T}"/><circle cx="13.5" cy="37" r="6" fill="{T}"/></g>'
            f'<circle cx="13.5" cy="37" r="3" {_DOT}/><path d="M13.5 37V16" {_ACC}/>'
            f'<circle cx="34" cy="22" r="6" fill="{T}" {_L}/><g {_ACC}><path d="M34 10v3M34 31v3M22 22h3M43 22h3M25.5 13.5l2 2M40.5 28.5l2 2M42.5 13.5l-2 2M27.5 28.5l-2 2"/></g>'),
    "FY4": (f'<path d="M24 4c6 7 7 16 5 26H19c-2-10-1-19 5-26z" fill="{T}" {_L}/><circle cx="24" cy="16" r="3.2" {_S}/>'
            f'<path d="M19 24l-6 8 6-1M29 24l6 8-6-1" {_S}/><path d="M21 33l3 10 3-10" {_ACC} fill="{A}" fill-opacity=".25"/>'),
    "FY5": (f'<path d="M3 24h42" {_S} stroke-width="1" stroke-dasharray="2 3"/>'
            f'<path d="M4 24c5-14 9-14 14 0s9 14 14 0 7-9 12 0" {_ACC} stroke-width="2.6"/>'
            f'<g {_S}><path d="M6 38c3-4 5-4 8 0s5 4 8 0 5-4 8 0 5 4 8 0" opacity=".6"/></g>'),
    "FY6": (f'<g {_S}><path d="M24 5L16 43M24 5l8 38M19.5 25h9M17.5 34h13M11 14h26M11 14l13-6 13 6M18 43h12"/></g>'
            f'<g {_ACC}><path d="M2 20q4 3 9-6M46 20q-4 3-9-6"/></g><circle cx="11" cy="14" r="1.8" {_DOT}/><circle cx="37" cy="14" r="1.8" {_DOT}/>'),
    "FY7": (f'<path d="M12 6v21a12 12 0 0 0 24 0V6" {_S} stroke-width="5" stroke="{G}"/><path d="M12 6v8M36 6v8" {_ACC} stroke-width="5" stroke-linecap="butt"/>'
            f'<g {_S} stroke-width="1.5"><path d="M17 8q7-5 14 0"/></g>'
            f'<g {_ACC} stroke-width="1.8"><path d="M24 42v3M17 41l-2 2.5M31 41l2 2.5"/></g>'),
    "FY8": _atom(24, 24, 19, 7) + f'<g {_DOT}><circle cx="43" cy="24" r="2.2"/><circle cx="14.5" cy="7.5" r="2.2"/><circle cx="14.5" cy="40.5" r="2.2"/></g>',
    # the page tops
    "listen": (f'<path d="M9 29v-5a15 15 0 0 1 30 0v5" {_S} stroke-width="2.6"/>'
               f'<rect x="5" y="27" width="10" height="15" rx="4" fill="{T}" {_L}/><rect x="33" y="27" width="10" height="15" rx="4" fill="{T}" {_L}/>'
               + _atom(24, 33, 7, 2.8, 2.2, (0, 60, 120))),
    "read": (f'<path d="M5 38q9-4 19 0 10-4 19 0v6q-9-4-19 0-10-4-19 0z" fill="{T}" {_L}/><path d="M24 38v6" {_S}/>'
             + _atom(24, 17, 12, 4.5, 2.4, (0, 60, 120)) + f'<path d="M6 12q3-3 6 0M36 8q3-3 6 0" {_ACC} stroke-width="1.8"/>'),
}


def svg(key, size, label=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true" focusable="false"'
    return f'<svg class="page-art" viewBox="0 0 48 48" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg" {a}>{ART[key]}</svg>'


if __name__ == "__main__":
    import sys
    for k in ART: print(k, len(svg(k, 64)))
