"""Ahjo Makerspace illustrations (teacher 2026-11-08, "piirrä kuvitukset"): flat vector scenes in Kiviruukin lukio's
colours, no text, decorative (the heading beside each says what it is). One per course (480 x 240) and one per resource
bank category (240 x 150). Run to (re)write assets/shared/ahjo/<name>.svg; scripts/ahjo.py inlines them.

  python scripts/ahjo_art.py"""
import pathlib
OUT = pathlib.Path(__file__).resolve().parents[1] / "assets/shared/ahjo"
N, N2, M, L = "#012169", "#2a4a9b", "#8fa3d1", "#d9dfe9"     # navy, mid navy, soft blue, light grey-blue
P, PD, PS, W, BG = "#fca5c7", "#e0679f", "#fde4ee", "#ffffff", "#f3f5f9"
S = f'stroke="{N}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
s2 = f'stroke="{N}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"'


def svg(w, h, body, bg=True):
    back = f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="ahjo-art" aria-hidden="true" focusable="false">'
            f'{back}{body}</svg>\n')


def rays(cx, cy, r1, r2, n=7, a0=200, a1=340, col=P, w=4):
    import math
    out = ""
    if n < 2: return out
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        out += f'<path d="M{cx + r1 * math.cos(a):.1f} {cy + r1 * math.sin(a):.1f}L{cx + r2 * math.cos(a):.1f} {cy + r2 * math.sin(a):.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
    return out


def bench(x0, x1, y, h=240):
    return (f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="12" rx="3" fill="{N}"/>'
            f'<rect x="{x0 + 14}" y="{y + 12}" width="10" height="{h - y - 12}" fill="{N2}"/><rect x="{x1 - 24}" y="{y + 12}" width="10" height="{h - y - 12}" fill="{N2}"/>')


def printer(x, y, s=1.0, part=True):
    """A 3D printer: frame, gantry, nozzle, bed and a printed part (pink) half done."""
    def t(v): return v * s
    g = (f'<g transform="translate({x} {y}) scale({s})">'
         f'<rect x="0" y="0" width="100" height="112" rx="6" fill="{W}" {S}/>'
         f'<rect x="10" y="10" width="80" height="84" rx="3" fill="{PS}"/>'
         f'<path d="M10 30H90" {S}/><rect x="40" y="24" width="20" height="14" rx="2" fill="{N}"/>'
         f'<path d="M50 38l-4 6h8z" fill="{N}"/>'
         f'<rect x="18" y="86" width="64" height="6" rx="1" fill="{N2}"/>')
    if part: g += (f'<path d="M38 86h24l-3-20h-18z" fill="{P}" stroke="{PD}" stroke-width="1.5"/>'
                   f'<path d="M40 79h20M41 72h18" stroke="{PD}" stroke-width="1.2"/>')
    g += (f'<rect x="0" y="100" width="100" height="12" rx="3" fill="{N}"/><circle cx="84" cy="106" r="3" fill="{P}"/>'
          f'<path d="M100 20c14 0 18 10 18 22" {s2} fill="none"/><circle cx="118" cy="50" r="10" fill="{W}" {s2}/><circle cx="118" cy="50" r="4" fill="{P}"/></g>')
    return g


def board(x, y, led=True):
    """A microcontroller board on a breadboard with an LED and a resistor."""
    g = (f'<g transform="translate({x} {y})">'
         f'<rect x="0" y="22" width="120" height="44" rx="4" fill="{W}" {s2}/>'
         + "".join(f'<circle cx="{10 + 8 * i}" cy="{34 + 10 * j}" r="1.6" fill="{M}"/>' for i in range(14) for j in range(3))
         + f'<rect x="-6" y="-26" width="70" height="44" rx="4" fill="{N2}" {s2}/>'
         f'<rect x="4" y="-16" width="22" height="14" rx="1" fill="{L}"/><rect x="34" y="-14" width="18" height="18" rx="1" fill="{N}"/>'
         + "".join(f'<rect x="{2 + 6 * i}" y="-30" width="3" height="5" fill="{N}"/>' for i in range(10))
         + f'<path d="M30 -26C30 -40 74 -40 74 30" stroke="{PD}" stroke-width="2.5" fill="none"/>'
         f'<path d="M58 18C58 10 88 6 88 30" stroke="{N}" stroke-width="2.5" fill="none"/>'
         f'<rect x="90" y="40" width="22" height="8" rx="3" fill="#e9c46a" {s2}/><path d="M93 40v8M98 40v8M104 40v8" stroke="{PD}" stroke-width="1.5"/>')
    if led:
        g += (f'<path d="M74 30v-8M80 30v-8" {s2}/><path d="M70 22v-10a7 7 0 0 1 14 0v10z" fill="{P}" {s2}/>'
              + rays(77, 6, 14, 24, n=5, a0=210, a1=330, col=P, w=3))
    return g + '</g>'


def robot(x, y):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M32 0v-14" {S}/><circle cx="32" cy="-18" r="6" fill="{P}" {s2}/>'
            f'<rect x="4" y="0" width="56" height="40" rx="10" fill="{W}" {S}/>'
            f'<rect x="14" y="10" width="36" height="16" rx="6" fill="{N}"/><circle cx="24" cy="18" r="4" fill="{P}"/><circle cx="40" cy="18" r="4" fill="{P}"/>'
            f'<rect x="0" y="40" width="64" height="30" rx="6" fill="{N2}" {S}/>'
            f'<circle cx="12" cy="74" r="11" fill="{N}"/><circle cx="12" cy="74" r="4" fill="{L}"/><circle cx="52" cy="74" r="11" fill="{N}"/><circle cx="52" cy="74" r="4" fill="{L}"/>'
            f'<path d="M64 52h14l6 -8" {S} fill="none"/></g>')


def pegboard(x, y):
    """A tool wall: a perforated board with a ruler, pliers and a screwdriver hanging on it."""
    holes = "".join(f'<circle cx="{x + 10 + 14 * i}" cy="{y + 10 + 14 * j}" r="1.8" fill="{M}"/>' for i in range(11) for j in range(4))
    return (f'<rect x="{x}" y="{y}" width="160" height="62" rx="4" fill="{L}"/>{holes}'
            f'<rect x="{x + 14}" y="{y + 14}" width="10" height="40" rx="2" fill="#e9c46a" {s2}/>'
            f'<path d="M{x + 52} {y + 12}l-6 26M{x + 60} {y + 12}l6 26" stroke="{N}" stroke-width="5" stroke-linecap="round"/><path d="M{x + 46} {y + 38}l-3 14M{x + 66} {y + 38}l3 14" stroke="{PD}" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="{x + 92}" y="{y + 10}" width="10" height="22" rx="4" fill="{P}" {s2}/><path d="M{x + 97} {y + 32}v20" stroke="{N}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M{x + 120} {y + 14}h26v8h-26z" fill="{N2}"/><path d="M{x + 126} {y + 22}v26" stroke="{N2}" stroke-width="5" stroke-linecap="round"/>')


def ahjo1():
    b = (bench(16, 464, 196) + printer(36, 84) + board(196, 160) + robot(366, 112)
         + pegboard(176, 22))
    return svg(480, 240, b)


def ahjo2():
    # sketch -> prototype -> test, joined by arrows, with a loop back (iterate)
    sketch = (f'<g transform="translate(36 70)"><rect x="0" y="0" width="100" height="120" rx="4" fill="{W}" {S} transform="rotate(-4 50 60)"/>'
              f'<path d="M22 84c10-30 30-40 56-36" stroke="{M}" stroke-width="3" fill="none" stroke-dasharray="5 5"/>'
              f'<rect x="22" y="56" width="46" height="30" rx="4" fill="none" stroke="{N2}" stroke-width="2.5"/><path d="M30 86l-6 10M60 86l6 10" stroke="{N2}" stroke-width="2.5"/>'
              f'<circle cx="70" cy="26" r="13" fill="{P}" {s2}/><path d="M65 40h10M66 45h8" {s2}/>' + rays(70, 26, 18, 26, n=5, a0=200, a1=340, col=PD, w=2.5)
              + f'<path d="M74 124l20-46 8 4-20 46-10 6z" fill="#e9c46a" {s2}/><path d="M94 78l8 4 4-8-8-4z" fill="{PD}" {s2}/></g>')
    proto = (f'<g transform="translate(196 92)"><path d="M0 30l44-22 44 22v54l-44 22-44-22z" fill="#d9b26a" stroke="{N}" stroke-width="3" stroke-linejoin="round"/>'
             f'<path d="M0 30l44 22 44-22M44 52v54" stroke="{N}" stroke-width="3" fill="none" stroke-linejoin="round"/>'
             f'<path d="M10 46l26 13M14 64l18 9" stroke="#a97a35" stroke-width="2.5"/>'
             f'<rect x="52" y="62" width="24" height="16" rx="3" fill="{N2}" transform="skewY(-26)"/>'
             f'<circle cx="64" cy="72" r="4" fill="{P}" transform="skewY(-26)"/></g>')
    test = (f'<g transform="translate(346 82)"><rect x="0" y="0" width="98" height="110" rx="8" fill="{W}" {S}/>'
            f'<path d="M14 92V18M14 92h72" {s2}/><path d="M18 80l16-14 14 6 16-22 18-14" stroke="{PD}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{N}"/>' for cx, cy in ((18, 80), (34, 66), (48, 72), (64, 50), (82, 36)))
            + f'<circle cx="84" cy="98" r="0"/></g><g transform="translate(424 70)"><circle r="16" fill="{N}"/><path d="M-7 0l5 5 9-10" stroke="{W}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    arrows = (f'<path d="M154 128h30M174 120l10 8-10 8" stroke="{N}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="M298 128h36M324 120l10 8-10 8" stroke="{N}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="M394 204C394 230 90 230 88 206" stroke="{P}" stroke-width="4" fill="none" stroke-dasharray="2 9" stroke-linecap="round"/>'
              f'<path d="M80 214l8-10 8 10" stroke="{PD}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return svg(480, 240, sketch + proto + test + arrows)


def cat_3d():
    layers = "".join(f'<rect x="{88 - i * 0}" y="{112 - i * 7}" width="64" height="6" rx="2" fill="{P if i % 2 else PD}"/>' for i in range(6))
    return svg(240, 150, f'<rect x="60" y="120" width="120" height="10" rx="2" fill="{N2}"/>{layers}'
               f'<rect x="96" y="24" width="48" height="30" rx="4" fill="{N}"/><path d="M110 54h20l-6 12h-8z" fill="{N}"/><path d="M120 66v8" stroke="{PD}" stroke-width="3"/>'
               f'<path d="M30 39H210" stroke="{N}" stroke-width="5" stroke-linecap="round"/><circle cx="30" cy="39" r="6" fill="{M}"/><circle cx="210" cy="39" r="6" fill="{M}"/>'
               f'<path d="M180 82l14-8 14 8v16l-14 8-14-8z" fill="{W}" {s2}/><path d="M180 82l14 8 14-8M194 90v16" {s2} fill="none"/>')


def cat_elec():
    return svg(240, 150, board(64, 64))


def cat_robot():
    arm = (f'<rect x="40" y="118" width="70" height="14" rx="4" fill="{N}"/><circle cx="75" cy="112" r="12" fill="{N2}"/>'
           f'<path d="M75 112L112 62" stroke="{N2}" stroke-width="14" stroke-linecap="round"/><circle cx="112" cy="62" r="9" fill="{P}" {s2}/>'
           f'<path d="M112 62L160 72" stroke="{N2}" stroke-width="11" stroke-linecap="round"/><circle cx="160" cy="72" r="6" fill="{W}" {s2}/>'
           f'<path d="M164 66l14-6M164 78l14 6" {S}/><rect x="176" y="70" width="14" height="14" rx="2" fill="{P}" {s2}/>')
    return svg(240, 150, arm + f'<rect x="168" y="112" width="40" height="20" rx="3" fill="{PS}" {s2}/>')


def cat_vr():
    return svg(240, 150, f'<path d="M40 60c0-12 10-18 22-18h116c12 0 22 6 22 18v34c0 10-8 18-18 18h-38l-12-14h-24l-12 14h-38c-10 0-18-8-18-18z" fill="{N}"/>'
               f'<path d="M54 64h52v28h-46c-4 0-6-2-6-6zM134 64h52v22c0 4-2 6-6 6h-46z" fill="{N2}"/>'
               f'<path d="M62 84l14-12 10 8 12-12M142 84l10-8 12 6 14-12" stroke="{P}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
               f'<path d="M40 70H22M200 70h18" stroke="{N}" stroke-width="8" stroke-linecap="round"/>'
               + rays(120, 40, 10, 22, n=5, a0=230, a1=310, col=P, w=3))


def cat_textile():
    shirt = (f'<path d="M70 40l26-12h48l26 12 22 26-20 14-12-10v62H80V70l-12 10-20-14z" fill="{W}" {S}/>'
             f'<path d="M104 28c4 10 28 10 32 0" {s2} fill="none"/>'
             f'<path d="M106 94l14-22 14 22z" fill="{N}"/><path d="M100 76h40" stroke="{P}" stroke-width="4" stroke-linecap="round"/>'
             + rays(120, 98, 22, 30, n=5, a0=200, a1=340, col=P, w=3))
    sc = (f'<g transform="translate(188 98) rotate(30)"><circle cx="-10" cy="22" r="8" fill="none" stroke="{PD}" stroke-width="3.5"/><circle cx="10" cy="22" r="8" fill="none" stroke="{PD}" stroke-width="3.5"/>'
          f'<path d="M-6 15L6 -18M6 15L-6 -18" stroke="{N}" stroke-width="4" stroke-linecap="round"/></g>'
          f'<path d="M24 120c12-16 24 0 36-14" stroke="{N2}" stroke-width="2.5" fill="none" stroke-dasharray="4 4"/><circle cx="24" cy="120" r="3" fill="{N}"/>')
    return svg(240, 150, shirt + sc)


def cat_tools():
    return svg(240, 150, f'<rect x="28" y="116" width="184" height="10" rx="2" fill="{N}"/>'
               + "".join(f'<path d="M{40 + 8 * i} 116v{-6 if i % 5 else -11}" stroke="{W}" stroke-width="2"/>' for i in range(21))
               + f'<g transform="rotate(-35 120 70)"><rect x="60" y="62" width="100" height="14" rx="7" fill="{N2}"/>'
               f'<circle cx="166" cy="69" r="15" fill="{N2}"/><rect x="168" y="63" width="16" height="12" fill="{BG}"/><rect x="60" y="62" width="34" height="14" rx="7" fill="{P}"/></g>'
               f'<g transform="rotate(35 120 70)"><rect x="62" y="64" width="54" height="16" rx="6" fill="{PD}"/><rect x="116" y="68" width="56" height="8" rx="2" fill="{M}"/><path d="M172 68l10 4-10 4z" fill="{N}"/></g>')


def cat_safety():
    return svg(240, 150, f'<path d="M40 70c0-14 18-22 80-22s80 8 80 22v18c0 14-12 22-28 22-20 0-24-16-52-16s-32 16-52 16c-16 0-28-8-28-22z" fill="{PS}" {S}/>'
               f'<path d="M58 66c18-4 44-4 52 0M130 66c18-4 44-4 52 0" stroke="{W}" stroke-width="5" stroke-linecap="round"/>'
               f'<path d="M40 70H22M200 70h18" stroke="{N}" stroke-width="6" stroke-linecap="round"/>'
               f'<g transform="translate(176 104)"><rect x="-22" y="-18" width="44" height="36" rx="6" fill="{W}" {S}/><path d="M-4-10h8v6h6v8h-6v6h-8v-6h-6v-8h6z" fill="{PD}"/></g>')


def cat_doc():
    return svg(240, 150, f'<rect x="44" y="26" width="100" height="108" rx="6" fill="{W}" {S}/>'
               + "".join(f'<circle cx="44" cy="{40 + 14 * i}" r="4" fill="{BG}" {s2}/>' for i in range(7))
               + f'<path d="M62 112V48M62 112h68" {s2}/><path d="M66 102l16-14 14 4 14-22 14-12" stroke="{PD}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
               f'<path d="M68 42h40" stroke="{L}" stroke-width="5" stroke-linecap="round"/>'
               f'<g transform="translate(176 92)"><rect x="-28" y="-18" width="56" height="40" rx="6" fill="{N}"/><rect x="-12" y="-26" width="20" height="10" rx="2" fill="{N}"/>'
               f'<circle cx="0" cy="2" r="13" fill="{N2}" stroke="{W}" stroke-width="3"/><circle cx="0" cy="2" r="5" fill="{P}"/><circle cx="18" cy="-10" r="3" fill="{P}"/></g>')


ART = {"ahjo1": ahjo1, "ahjo2": ahjo2, "3d": cat_3d, "elektroniikka": cat_elec, "robotiikka": cat_robot, "vr": cat_vr,
       "tekstiilit": cat_textile, "tyokalut": cat_tools, "turvallisuus": cat_safety, "dokumentointi": cat_doc}


# --- one small scene per lesson (teacher 2026-11-08, "haluan kuvat tunneille"): 240 x 150, the lesson's topic at a glance
def sc(body): return svg(240, 150, body)
Y = "#e9c46a"     # wood, resistor, pencil
C = "#d9b26a"     # cardboard


def person(x, y, col):
    """An abstract person (head and shoulders), never a real one."""
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{col}"/><path d="M{x - 20} {y + 40}c0-18 9-24 20-24s20 6 20 24z" fill="{col}"/>'


def screen(x, y, w, h, inner=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{N}"/><rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="3" fill="{W}"/>'
            f'<path d="M{x + w / 2} {y + h}v10M{x + w / 2 - 22} {y + h + 12}h44" stroke="{N}" stroke-width="5" stroke-linecap="round"/>{inner}')


def cube_wire(cx, cy, r):
    return (f'<path d="M{cx} {cy - r}l{r} {r * .5}v{r}l{-r} {r * .5}l{-r} {-r * .5}v{-r}z" fill="{PS}" stroke="{N}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<path d="M{cx - r} {cy - r * .5}l{r} {r * .5}l{r} {-r * .5}M{cx} {cy}v{r}" stroke="{N}" stroke-width="2.5" fill="none"/>'
            f'<path d="M{cx} {cy - r}v{r}M{cx - r} {cy + r * .5}l{r} {-r * .5}l{r} {r * .5}" stroke="{M}" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>')


def gear(cx, cy, r, col):
    import math
    pts = []
    for i in range(16):
        a = math.pi * 2 * i / 16; rr = r if i % 2 == 0 else r * .78
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/><circle cx="{cx}" cy="{cy}" r="{r * .3}" fill="{BG}"/>'


def chart(x, y, w, h, pts, col=PD):
    path = "M" + "L".join(f"{x + 8 + px * (w - 16)} {y + h - 8 - py * (h - 16)}" for px, py in pts)
    return (f'<path d="M{x} {y}v{h}h{w}" {s2} fill="none"/><path d="{path}" stroke="{col}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            + "".join(f'<circle cx="{x + 8 + px * (w - 16)}" cy="{y + h - 8 - py * (h - 16)}" r="3.5" fill="{N}"/>' for px, py in pts))


def bubble(x, y, w, h, col=W, tail=1):
    t = f'<path d="M{x + 18} {y + h}l-4 14 16-14z" fill="{col}" {s2}/>' if tail > 0 else f'<path d="M{x + w - 18} {y + h}l4 14-16-14z" fill="{col}" {s2}/>'
    return f'{t}<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{col}" {s2}/><path d="M{x + 12} {y + h - 2}h20" stroke="{col}" stroke-width="4"/>'


A1 = {
 1: lambda: sc(f'<path d="M60 136V64a60 60 0 0 1 120 0v72z" fill="{PS}" {S}/>' + rays(120, 64, 66, 84, n=7, a0=200, a1=340, col=P, w=5)
              + f'<path d="M84 136V78a36 36 0 0 1 72 0v58" fill="{W}" {S}/><rect x="96" y="104" width="48" height="10" rx="2" fill="{N}"/>'
              + f'<path d="M100 104l8-16h24l8 16" fill="{N2}"/><circle cx="148" cy="112" r="3" fill="{P}"/><path d="M20 136h200" {S}/>'),
 2: lambda: sc(f'<path d="M64 40l44 78H20z" fill="#ffd166" stroke="{N}" stroke-width="4" stroke-linejoin="round"/><path d="M64 66v26" stroke="{N}" stroke-width="7" stroke-linecap="round"/><circle cx="64" cy="104" r="4.5" fill="{N}"/>'
              + f'<path d="M126 70c0-10 14-16 48-16s48 6 48 16v12c0 10-8 16-20 16-12 0-14-10-28-10s-16 10-28 10c-12 0-20-6-20-16z" fill="{PS}" {S}/><path d="M138 66c10-3 22-3 28 0M182 66c10-3 22-3 28 0" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'),
 3: lambda: sc(screen(50, 22, 140, 90, cube_wire(120, 62, 26) + f'<path d="M62 34h20M62 42h14" stroke="{L}" stroke-width="4" stroke-linecap="round"/><path d="M168 96l-12-4 4 12z" fill="{PD}"/>')),
 4: lambda: sc(f'<rect x="30" y="56" width="180" height="22" rx="3" fill="{M}"/>' + "".join(f'<path d="M{40 + 8 * i} 56v{8 if i % 5 else 14}" stroke="{N}" stroke-width="1.5"/>' for i in range(21))
              + f'<path d="M40 56V24h18v32M140 56V24h18v32" fill="{N2}" stroke="{N}" stroke-width="2"/><rect x="130" y="50" width="38" height="34" rx="3" fill="{N}"/><rect x="136" y="56" width="26" height="12" rx="2" fill="{P}"/>'
              + f'<rect x="58" y="98" width="82" height="34" rx="4" fill="{P}" {s2}/><path d="M58 92v-6M140 92v-6M58 89h82" stroke="{PD}" stroke-width="2"/><path d="M64 89l-5-3v6zM134 89l5-3v6z" fill="{PD}"/>'),
 5: lambda: sc(printer(78, 20, 1.0)),
 6: lambda: sc(f'<ellipse cx="78" cy="122" rx="50" ry="10" fill="{N2}"/><path d="M48 118V74h60v44z" fill="{P}" {s2}/><path d="M48 90h60M48 104h60" stroke="{PD}" stroke-width="1.5"/>'
              + f'<path d="M104 74c6 4 6 10 4 16" stroke="{PD}" stroke-width="3" fill="none" stroke-linecap="round"/>'
              + f'<rect x="132" y="30" width="92" height="16" rx="2" fill="{M}" {s2}/>' + "".join(f'<path d="M{140 + 8 * i} 30v{6 if i % 5 else 10}" stroke="{N}" stroke-width="1.5"/>' for i in range(11))
              + f'<path d="M140 46v40h12V46M196 46v40h12V46" fill="{N2}" stroke="{N}" stroke-width="2"/>'
              + f'<g transform="translate(178 112)"><circle r="16" fill="{N}"/><path d="M-7 0l5 5 10-11" stroke="{W}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'),
 7: lambda: sc(f'<path d="M50 44h140v70H50z" fill="none" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
              + f'<rect x="36" y="64" width="28" height="34" rx="3" fill="{N}"/><rect x="44" y="58" width="12" height="6" fill="{N}"/><path d="M44 74h12M50 84v-14" stroke="{W}" stroke-width="3"/>'
              + f'<rect x="96" y="36" width="44" height="16" rx="6" fill="{Y}" {s2}/><path d="M106 36v16M114 36v16M124 36v16" stroke="{PD}" stroke-width="2.5"/>'
              + f'<path d="M180 70a12 12 0 0 1 20 0v20h-20z" fill="{P}" {s2}/>' + rays(190, 70, 18, 28, n=5, a0=-60, a1=60, col=P, w=3)
              + f'<path d="M120 114l-8-6v12z" fill="{N}"/>'),
 8: lambda: sc(f'<rect x="76" y="20" width="76" height="112" rx="10" fill="#ffd166" {S}/><rect x="88" y="32" width="52" height="26" rx="3" fill="{N}"/><path d="M96 48h8M108 48h8M120 48h8" stroke="{P}" stroke-width="4"/>'
              + f'<circle cx="114" cy="86" r="18" fill="{W}" {s2}/><path d="M114 86l10-10" {S}/><circle cx="96" cy="118" r="5" fill="{N}"/><circle cx="132" cy="118" r="5" fill="{PD}"/>'
              + f'<path d="M96 118c-20 10-40 0-56-20M132 118c20 10 40 6 54-14" stroke-width="3" fill="none" stroke="{N}"/><path d="M134 120c20 10 40 6 54-14" stroke="{PD}" stroke-width="3" fill="none"/>'
              + f'<path d="M36 94l8-6M182 98l8-8" stroke="{N}" stroke-width="5" stroke-linecap="round"/>'),
 9: lambda: sc(board(60, 70) + f'<g transform="translate(150 22)"><rect width="74" height="44" rx="6" fill="{N}"/><path d="M14 14l-6 8 6 8M60 14l6 8-6 8" stroke="{P}" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M24 16h22M24 24h14M24 32h18" stroke="{W}" stroke-width="3" stroke-linecap="round"/></g>'),
 10: lambda: sc(f'<rect x="26" y="60" width="54" height="30" rx="4" fill="{N2}" {s2}/><circle cx="62" cy="75" r="9" fill="{W}" {s2}/><circle cx="62" cy="75" r="4" fill="{N}"/><circle cx="40" cy="75" r="9" fill="{W}" {s2}/><circle cx="40" cy="75" r="4" fill="{N}"/>'
              + "".join(f'<path d="M{88 + 14 * i} {62 - 4 * i}a{14 + 6 * i} {14 + 6 * i} 0 0 1 0 {26 + 8 * i}" stroke="{P}" stroke-width="3" fill="none" stroke-linecap="round"/>' for i in range(4))
              + f'<rect x="170" y="36" width="20" height="80" rx="3" fill="{M}"/><path d="M60 112v-22" {s2}/><circle cx="100" cy="122" r="8" fill="{P}" {s2}/><circle cx="130" cy="122" r="8" fill="{L}" {s2}/><circle cx="160" cy="122" r="8" fill="{L}" {s2}/>'),
 11: lambda: sc(f'<circle cx="200" cy="34" r="16" fill="#ffd166"/>' + rays(200, 34, 22, 30, n=6, a0=100, a1=250, col="#ffd166", w=3)
              + f'<g transform="rotate(-20 110 70)"><rect x="60" y="50" width="100" height="44" rx="3" fill="{N}"/>' + "".join(f'<path d="M{60 + 25 * i} 50v44" stroke="{N2}" stroke-width="2"/>' for i in range(1, 4)) + f'<path d="M60 72h100" stroke="{N2}" stroke-width="2"/></g>'
              + f'<path d="M110 90v30" stroke="{N}" stroke-width="6"/><rect x="92" y="118" width="36" height="20" rx="3" fill="{PD}" {s2}/><circle cx="110" cy="112" r="6" fill="{W}" {s2}/>'),
 12: lambda: sc(gear(76, 70, 34, N2) + gear(128, 98, 24, PD) + robot(156, 54).replace(f"translate(156 54)", "translate(160 52) scale(0.85)")),
 13: lambda: sc(f'<path d="M20 120C60 120 60 50 120 50S180 110 222 110" stroke="{N}" stroke-width="10" fill="none" stroke-linecap="round"/>'
              + robot(100, 40).replace("translate(100 40)", "translate(98 18) scale(0.55)")
              + f'<path d="M150 22l10 12M164 18l2 14M178 24l-6 12" stroke="{P}" stroke-width="3" stroke-linecap="round"/>'),
 14: lambda: sc(f'<rect x="26" y="20" width="110" height="114" rx="4" fill="{W}" {S}/><path d="M40 40h60M40 52h44" stroke="{L}" stroke-width="5" stroke-linecap="round"/>'
              + f'<path d="M44 108l22-30 18 16 26-34" stroke="{PD}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="110" cy="60" r="5" fill="{PD}"/>'
              + "".join(f'<rect x="156" y="{30 + 32 * i}" width="16" height="16" rx="3" fill="{W}" {s2}/><path d="M180 {38 + 32 * i}h36" stroke="{L}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))
              + f'<path d="M159 38l4 5 8-9M159 70l4 5 8-9" stroke="{PD}" stroke-width="3" fill="none" stroke-linecap="round"/>'
              + f'<path d="M126 136l42-42 8 8-42 42-12 4z" fill="{Y}" {s2}/>'),
 15: lambda: sc(f'<path d="M78 136l-8-50h80l-8 50z" fill="{PD}" {s2}/><rect x="66" y="80" width="88" height="10" rx="3" fill="{P}" {s2}/>'
              + f'<path d="M110 80c0-30-20-40-36-44 6 18 18 30 36 44zM110 80c0-34 22-44 40-46-6 20-20 32-40 46z" fill="#3f8f5a"/><path d="M110 80V40" stroke="#2d6b42" stroke-width="3"/>'
              + f'<path d="M150 104h20v-60" stroke="{N}" stroke-width="3" fill="none"/><rect x="164" y="24" width="44" height="28" rx="4" fill="{N2}" {s2}/><circle cx="176" cy="38" r="5" fill="{P}"/><path d="M186 38h14" stroke="{W}" stroke-width="3"/>'
              + f'<path d="M140 100v26" stroke="{L}" stroke-width="4"/><path d="M134 126h12" stroke="{N}" stroke-width="3"/>'),
 16: lambda: sc(screen(26, 18, 120, 76, chart(42, 30, 88, 50, [(0, .1), (.3, .35), (.6, .5), (1, .9)])) + robot(170, 66).replace("translate(170 66)", "translate(168 54) scale(0.75)")
              + f'<path d="M30 132h184" {S}/>'),
}

A2 = {
 1: lambda: sc(person(60, 64, N2) + person(120, 52, N) + person(180, 64, PD) + f'<path d="M20 124h200" {S}/>'
              + f'<g transform="translate(120 20)"><circle r="11" fill="#ffd166" {s2}/><path d="M-5 13h10" {s2}/></g>'),
 2: lambda: sc(bubble(24, 22, 92, 40) + f'<path d="M38 36h56M38 46h40" stroke="{L}" stroke-width="5" stroke-linecap="round"/>'
              + person(54, 104, N2) + f'<circle cx="160" cy="76" r="30" fill="{PS}" stroke="{N}" stroke-width="6"/><path d="M182 98l26 26" stroke="{N}" stroke-width="10" stroke-linecap="round"/><path d="M150 76h20M160 66v20" stroke="{PD}" stroke-width="4" stroke-linecap="round"/>'),
 3: lambda: sc("".join(f'<rect x="{x}" y="{y}" width="46" height="40" rx="2" fill="{c}" transform="rotate({r} {x + 23} {y + 20})"/>'
                         + f'<path d="M{x + 8} {y + 14}h28M{x + 8} {y + 24}h18" stroke="{N}" stroke-width="2.5" stroke-linecap="round" opacity=".55" transform="rotate({r} {x + 23} {y + 20})"/>'
                         for x, y, c, r in ((24, 24, P, -6), (82, 18, "#ffd166", 4), (140, 26, PS, -3), (186, 40, P, 6), (40, 82, PS, 5), (100, 80, P, -4), (158, 88, "#ffd166", 3)))),
 4: lambda: sc(f'<g transform="translate(76 22)"><path d="M0 30l44-22 44 22v54l-44 22-44-22z" fill="{C}" stroke="{N}" stroke-width="3" stroke-linejoin="round"/><path d="M0 30l44 22 44-22M44 52v54" stroke="{N}" stroke-width="3" fill="none"/>'
              f'<path d="M58 40l18-9v10l-18 9z" fill="{N2}"/><path d="M10 50l24 12" stroke="#a97a35" stroke-width="2.5"/><path d="M-12 24l14 6M100 24l-14 6" stroke="{M}" stroke-width="3" stroke-linecap="round"/></g>'
              f'<rect x="24" y="118" width="30" height="8" rx="2" fill="{L}" transform="rotate(-20 39 122)"/><path d="M184 106l14-14 6 6-14 14z" fill="{PD}"/>'),
 5: lambda: sc(bubble(20, 20, 84, 44, PS) + f'<path d="M50 42h24M62 30v24" stroke="{PD}" stroke-width="5" stroke-linecap="round"/>'
              + bubble(136, 30, 84, 44, W, tail=-1) + f'<path d="M166 52h24" stroke="{N}" stroke-width="5" stroke-linecap="round"/>'
              + person(60, 104, N2) + person(180, 108, PD) + f'<path d="M98 110c14-16 32-16 46 0" stroke="{M}" stroke-width="3" fill="none" stroke-dasharray="4 5"/>'),
 6: lambda: sc(f'<path d="M30 30v96h184" {s2} fill="none"/>' + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="4" fill="{c}"/>' for x, y, w, c in ((40, 38, 50, N2), (80, 60, 60, PD), (130, 82, 44, N2), (160, 104, 46, P)))
              + f'<path d="M150 30v96" stroke="{PD}" stroke-width="2.5" stroke-dasharray="5 4"/><path d="M144 26l6 8 6-8z" fill="{PD}"/>'),
 7: lambda: sc(f'<rect x="20" y="18" width="200" height="116" rx="4" fill="#e9f0fb" {s2}/>' + "".join(f'<path d="M{20 + 20 * i} 18v116" stroke="#cfdcf1" stroke-width="1"/>' for i in range(1, 10)) + "".join(f'<path d="M20 {18 + 20 * j}h200" stroke="#cfdcf1" stroke-width="1"/>' for j in range(1, 6))
              + f'<path d="M60 104V52h70l30 30v22z" fill="none" stroke="{N}" stroke-width="3" stroke-linejoin="round"/><circle cx="96" cy="80" r="10" fill="none" stroke="{N}" stroke-width="2.5"/>'
              + f'<path d="M60 118h100M60 114v8M160 114v8" stroke="{PD}" stroke-width="2"/><path d="M174 52v52M170 52h8M170 104h8" stroke="{PD}" stroke-width="2"/><path d="M98 116h24" stroke="{PD}" stroke-width="4"/>'),
 8: lambda: sc(bench(20, 220, 104, 150) + f'<path d="M40 104l20-30h40l10 30z" fill="{C}" {s2}/><rect x="124" y="78" width="40" height="26" rx="3" fill="{P}" {s2}/><path d="M144 78v26" stroke="{PD}" stroke-width="2"/>'
              + f'<g transform="rotate(-30 190 60)"><rect x="168" y="54" width="44" height="12" rx="5" fill="{N2}"/><rect x="204" y="44" width="14" height="32" rx="3" fill="{N}"/></g>'),
 9: lambda: sc(chart(30, 24, 120, 100, [(0, .15), (.25, .3), (.5, .55), (.75, .6), (1, .85)]) + f'<circle cx="190" cy="80" r="30" fill="{W}" {S}/><path d="M190 80V60M190 80l14 8" {S}/><rect x="182" y="40" width="16" height="8" rx="2" fill="{N}"/><path d="M212 56l6-6" {S}/>'),
 10: lambda: sc(person(54, 64, N2) + f'<rect x="80" y="86" width="64" height="40" rx="4" fill="{C}" {s2}/><circle cx="128" cy="100" r="6" fill="{P}" {s2}/><path d="M90 98h20" stroke="#a97a35" stroke-width="3"/>'
              + f'<path d="M66 96l24 6" stroke="{N2}" stroke-width="8" stroke-linecap="round"/>' + person(190, 58, PD)
              + f'<rect x="158" y="86" width="40" height="50" rx="3" fill="{W}" {s2}/><path d="M166 98h24M166 108h18M166 118h22" stroke="{L}" stroke-width="3" stroke-linecap="round"/>'
              + f'<path d="M30 136h180" {S}/><path d="M118 40a8 8 0 1 1 10 8v6" stroke="{PD}" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="128" cy="64" r="3" fill="{PD}"/>'),
 11: lambda: sc(f'<rect x="22" y="56" width="70" height="56" rx="4" fill="{C}" {s2}/><path d="M36 76h26" stroke="#a97a35" stroke-width="3"/><circle cx="74" cy="96" r="6" fill="{L}" {s2}/>'
              + f'<path d="M104 84h30" stroke="{PD}" stroke-width="5" stroke-linecap="round"/><path d="M130 72l14 12-14 12z" fill="{PD}"/>'
              + f'<rect x="150" y="48" width="70" height="64" rx="8" fill="{W}" {S}/><circle cx="200" cy="96" r="7" fill="{P}" {s2}/><rect x="162" y="62" width="30" height="16" rx="2" fill="{N}"/><path d="M167 70h8M179 70h8" stroke="{P}" stroke-width="3"/>'
              + f'<path d="M30 126h60M156 126h60" stroke="{M}" stroke-width="5" stroke-linecap="round"/><path d="M40 30h16M188 22v16M180 30h16" stroke="{P}" stroke-width="4" stroke-linecap="round"/>'),
 12: lambda: sc(board(36, 74, led=True) + f'<path d="M172 38c18 4 30 22 30 46s-14 40-30 46c-12-8-18-26-18-46s4-40 18-46z" fill="{PS}" {s2}/><path d="M164 70h30M162 86h34M164 102h30" stroke="{P}" stroke-width="3"/>'),
 13: lambda: sc(f'<path d="M30 128h184" {S}/><rect x="52" y="78" width="40" height="50" rx="3" fill="{M}"/><rect x="104" y="40" width="40" height="88" rx="3" fill="{PD}"/>'
              + f'<path d="M160 70h44M160 70v58" stroke="{N}" stroke-width="0"/><path d="M60 64l84-34" stroke="{N}" stroke-width="3" stroke-dasharray="6 5"/><path d="M144 30l-12-1 6 10z" fill="{N}"/>'
              + f'<g transform="translate(184 74)"><circle r="20" fill="{N}"/><path d="M-9 0l6 6 12-13" stroke="{W}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'),
 14: lambda: sc(f'<g transform="translate(40 44)"><path d="M0 24l50-22 50 22v50l-50 22-50-22z" fill="{W}" stroke="{N}" stroke-width="3" stroke-linejoin="round"/><path d="M0 24l50 22 50-22M50 46v50" stroke="{N}" stroke-width="3" fill="none"/>'
              f'<path d="M64 56l26-12v18l-26 12z" fill="{N}"/>' + f'<circle cx="77" cy="58" r="5" fill="{P}"/><path d="M12 56l26 12v14l-26-12z" fill="{P}"/></g>'
              f'<path d="M176 36l20 20-34 34-20-20z" fill="{PS}" {s2}/><path d="M142 70l-14 14 4 4 14-14" fill="{N}" {s2}/>' + rays(200, 30, 8, 18, n=4, a0=-120, a1=-20, col=P, w=3)),
 15: lambda: sc(cat_doc().split('<rect width="240" height="150" rx="14" fill="#f3f5f9"/>', 1)[1].rsplit("</svg>", 1)[0]),
 16: lambda: sc(f'<path d="M20 120h200v18H20z" fill="{N}"/>' + screen(64, 14, 112, 70, cube_wire(120, 46, 16) + f'<path d="M80 30h18M80 38h12" stroke="{L}" stroke-width="4" stroke-linecap="round"/>')
              + person(40, 82, PD).replace("40 82", "40 82")
              + "".join(f'<circle cx="{x}" cy="132" r="7" fill="{M}"/>' for x in (150, 170, 190, 210))),
}
for k, f in A1.items(): ART[f"ahjo1-{k}"] = f
for k, f in A2.items(): ART[f"ahjo2-{k}"] = f


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, f in ART.items(): (OUT / f"{name}.svg").write_text(f())
    print("wrote", len(ART), "illustrations to", OUT)
    import ahjo                                   # the front page's icon: the logo's mark, cut from the original
    ahjo.MARK.write_text(ahjo.mark_svg()); print("wrote", ahjo.MARK)
