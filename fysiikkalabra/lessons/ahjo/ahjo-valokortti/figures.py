"""Figure of the Ahjo guide Valokortti paperipiirillä (scripts/figlib.py): one inside half of the opened card, drawn for
this guide after nobody's picture. The copper tracks are orange, the corner that folds over the coin cell is marked
with a dashed line, and its end lands on the cell when folded (the pad is the mirror image of the cell in the fold)."""
from figlib import Fig, INK, MUTED, WHITE, RULE, HOT, ALUMINIUM, METAL_EDGE, n

TAPE = "#e8873a"    # copper tape
LEAD = "#868e96"    # the LED's legs


def track(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{TAPE}" '
          'stroke-width="12" stroke-linejoin="miter" stroke-linecap="square"/>')


def kortti():
    f = Fig("ahjo-valo-kortti", 380, "Piirros avatun kortin toisesta sisäpuoliskosta, ei mittakaavassa. Kortille on liimattu "
            "kaksi oranssia kuparinauharataa. Miinusrata alkaa oikeasta alakulmasta pariston alta, kulkee vasemmalle ja "
            "nousee ylös LEDin lyhyen jalan eli katodin kohdalle. Plusrata alkaa LEDin pitkän jalan eli anodin kohdalta, "
            "kulkee alas ja oikealle kortin oikeaan alakulmaan, joka on rajattu katkoviivalla taitettavaksi kulmaksi. "
            "Nappiparisto on miinusradan päässä plusnapa ylöspäin. Kaareva nuoli näyttää, että kun kulma taitetaan "
            "katkoviivaa pitkin, plusradan pää osuu pariston yläpintaan ja piiri sulkeutuu. Radat eivät kosketa toisiaan.")
    f.rect(40, 30, 520, 320, WHITE, RULE, 2.5, rx=4)
    # the corner that folds over the cell: below the line x + y = 750
    f.path("M420,350 L560,210 L560,350 Z", "#fbf4e9")
    f.line(420, 350, 560, 210, MUTED, 2.5, dash="8 6")
    bx, by, px, py = 445, 225, 525, 305                     # the cell and its mirror image in the fold, the pad
    lx, ly = 210, 120                                       # the LED
    track(f, (bx, by), (270, by), (270, ly))                # minus: under the cell, left and up to the cathode
    track(f, (150, ly), (150, py), (px, py))                # plus: from the anode down and right into the corner
    f.rect(px - 18, py - 18, 36, 36, TAPE, rx=4)            # the end of the plus track that lands on the cell
    # LED seen from above, legs bent sideways onto the tracks
    f.line(lx - 10, ly, 150, ly, LEAD, 4, cap="round"); f.line(lx + 10, ly, 270, ly, LEAD, 4, cap="round")
    f.circle(lx, ly, 22, HOT, INK, 2)
    f.tex(lx, ly + 44, r"\text{LED}", "middle", size=22)
    f.tex(150, ly - 30, r"\text{pitkä jalka}", "middle", size=18)
    f.tex(278, ly - 30, r"\text{lyhyt jalka}", "middle", size=18)
    # the coin cell on the end of the minus track, + up
    f.circle(bx, by, 34, ALUMINIUM, METAL_EDGE, 2.5)
    f.circle(bx, by, 25, "#d5dbe1", METAL_EDGE, 1.5)
    f.tex(bx, by, r"+", "middle", size=26)
    f.tex(bx, by - 58, r"\text{nappiparisto, + ylöspäin}", "middle", size=18)
    # labels
    f.tex(300, by + 24, r"\text{miinusrata}", "start", size=20)
    f.tex(160, 270, r"\text{plusrata}", "start", size=20)
    f.tex(552, 368, r"\text{taitettava kulma}", "end", MUTED, size=18)
    # the fold: the pad turns over onto the cell
    f.path(f"M{px - 4},{py - 24} Q{px + 30},{by - 30} {bx + 38},{by - 14}", "none", INK, 2.5)
    f.path(f"M{bx + 38},{by - 14} l14,-2 l-6,12 Z", INK)
    return f.svg()


FIGURES = {"kortti": kortti}
