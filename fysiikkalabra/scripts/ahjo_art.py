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

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, f in ART.items(): (OUT / f"{name}.svg").write_text(f())
    print("wrote", len(ART), "illustrations to", OUT)
