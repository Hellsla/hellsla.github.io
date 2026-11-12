"""Ahjo's small starter files (teacher 2026-11-09): the 3D models a lesson starts from, the Arduino sketch of the serial
plotter guide and the measurement templates, written from this script so that every size is stated here and can be
checked. Run to (re)write assets/shared/ahjo/aloitus/; scripts/build.py publishes them as ahjo-aloitus/, scripts/ahjo.py
links them from the lessons (ahjo.json "starters"), and scripts/test_ahjo.py checks the files match this script.

None of these has been printed or run on Ahjo's own equipment yet, so ahjo.json says so beside every link.

  python scripts/ahjo_starters.py"""
import math, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "assets/shared/ahjo/aloitus"


# --- ASCII STL ----------------------------------------------------------------------------------------------------
def facet(a, b, c):
    """One triangle, counter-clockwise seen from outside, with its normal."""
    u = [b[i] - a[i] for i in range(3)]; v = [c[i] - a[i] for i in range(3)]
    nx, ny, nz = u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]
    ln = math.sqrt(nx * nx + ny * ny + nz * nz) or 1.0
    f = lambda p: " ".join(f"{x:.4f}" for x in p)
    return (f"  facet normal {nx / ln:.6f} {ny / ln:.6f} {nz / ln:.6f}\n    outer loop\n      vertex {f(a)}\n      vertex {f(b)}\n"
            f"      vertex {f(c)}\n    endloop\n  endfacet\n")


def quad(a, b, c, d): return facet(a, b, c) + facet(a, c, d)


def box(x0, y0, z0, dx, dy, dz):
    """A closed box, in mm."""
    p = lambda i, j, k: (x0 + i * dx, y0 + j * dy, z0 + k * dz)
    return (quad(p(0, 0, 0), p(0, 1, 0), p(1, 1, 0), p(1, 0, 0)) + quad(p(0, 0, 1), p(1, 0, 1), p(1, 1, 1), p(0, 1, 1))
            + quad(p(0, 0, 0), p(1, 0, 0), p(1, 0, 1), p(0, 0, 1)) + quad(p(1, 1, 0), p(0, 1, 0), p(0, 1, 1), p(1, 1, 1))
            + quad(p(0, 1, 0), p(0, 0, 0), p(0, 0, 1), p(0, 1, 1)) + quad(p(1, 0, 0), p(1, 1, 0), p(1, 1, 1), p(1, 0, 1)))


def cylinder(cx, cy, r, h, n=64):
    out = ""
    for i in range(n):
        a, b = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        p, q = (cx + r * math.cos(a), cy + r * math.sin(a)), (cx + r * math.cos(b), cy + r * math.sin(b))
        out += facet((cx, cy, 0), (q[0], q[1], 0), (p[0], p[1], 0)) + facet((cx, cy, h), (p[0], p[1], h), (q[0], q[1], h))
        out += quad((p[0], p[1], 0), (q[0], q[1], 0), (q[0], q[1], h), (p[0], p[1], h))
    return out


def plate_with_hole(x0, y0, w, d, h, cx, cy, r, n=64):
    """A rectangular plate w x d x h with one round hole of radius r through it at (cx, cy). The plate is star-shaped
    from the hole's centre, so every ray from it meets the outline once: the faces are strips between the hole and the
    outline along those rays, with rays through the four corners so the outline stays straight. Closed and manifold."""
    corners = [(x0, y0), (x0 + w, y0), (x0 + w, y0 + d), (x0, y0 + d)]
    angs = sorted({round(2 * math.pi * i / n, 9) for i in range(n)} | {round(math.atan2(y - cy, x - cx) % (2 * math.pi), 9) for x, y in corners})

    def edge(t):
        dx, dy = math.cos(t), math.sin(t); best = None
        for x, y in ((x0, None), (x0 + w, None), (None, y0), (None, y0 + d)):
            s = ((x - cx) / dx if abs(dx) > 1e-12 else None) if x is not None else ((y - cy) / dy if abs(dy) > 1e-12 else None)
            if s is None or s <= 0: continue
            px, py = cx + s * dx, cy + s * dy
            if x0 - 1e-6 <= px <= x0 + w + 1e-6 and y0 - 1e-6 <= py <= y0 + d + 1e-6 and (best is None or s < best[0]): best = (s, px, py)
        return best[1], best[2]

    ins = [(cx + r * math.cos(t), cy + r * math.sin(t)) for t in angs]; outs = [edge(t) for t in angs]
    out = ""
    for i in range(len(angs)):
        j = (i + 1) % len(angs)
        a, b, c, e = ins[i], outs[i], outs[j], ins[j]
        out += quad((a[0], a[1], h), (b[0], b[1], h), (c[0], c[1], h), (e[0], e[1], h))          # top
        out += quad((a[0], a[1], 0), (e[0], e[1], 0), (c[0], c[1], 0), (b[0], b[1], 0))          # bottom
        out += quad((b[0], b[1], 0), (c[0], c[1], 0), (c[0], c[1], h), (b[0], b[1], h))          # outer wall
        out += quad((a[0], a[1], 0), (a[0], a[1], h), (e[0], e[1], h), (e[0], e[1], 0))          # the hole's wall
    return out


def stl(name, body): return f"solid {name}\n{body}endsolid {name}\n"


# --- the files ----------------------------------------------------------------------------------------------------
FIT_CLEARANCES = (0.1, 0.2, 0.3, 0.4, 0.5)      # mm, hole diameter minus pin diameter
PIN = 10.0                                       # mm, the pin's diameter
FIT_HEIGHTS = (3, 4, 5, 6, 7)                    # mm: a ring's height tells its clearance (3 mm = 0.1 mm ... 7 mm = 0.5 mm)


def files():
    out = {}
    # Ahjo 1, lesson 3: a key fob to start from, 50 x 25 x 3 mm with a 5 mm hole for the ring
    out["avaimenpera-pohja.stl"] = stl("avaimenpera_pohja", plate_with_hole(0, 0, 50, 25, 3, 7, 12.5, 2.5))
    # Ahjo 1, lesson 4: five rings 16 x 16 mm with holes 10.1-10.5 mm, told apart by height, and a 10.0 mm pin
    body = "".join(plate_with_hole(i * 20, 0, 16, 16, hgt, i * 20 + 8, 8, (PIN + c) / 2) for i, (c, hgt) in enumerate(zip(FIT_CLEARANCES, FIT_HEIGHTS)))
    out["sovitekoe.stl"] = stl("sovitekoe", body + cylinder(110, 8, PIN / 2, 15))
    # Ahjo 1, lesson 5: a beam 120 x 12 x 6 mm for the load test (span 100 mm between the supports)
    out["palkki.stl"] = stl("palkki", box(0, 0, 0, 120, 12, 6))
    # Ahjo 1, lesson 6: a 20 mm cube for a print that is ready within the lesson
    out["kalibrointikuutio.stl"] = stl("kalibrointikuutio", box(0, 0, 0, 20, 20, 20))
    out["sarjaplotteri.ino"] = SKETCH
    out["robotti-testi.ino"] = ROBOT
    out["airbit-ohjain.ts"] = AIRBIT          # Dronelabra, lesson 5
    out["lentoanalyysi.py"] = ANALYSIS        # Dronelabra, lessons 8, 11, 12 and 15
    out["lentodata-esimerkki.csv"] = EXAMPLE_DATA
    for name, head in TEMPLATES.items():
        out[name] = head + "\n" + "\n".join(";" * head.count(";") for _ in range(8)) + "\n"
    return out


SKETCH = """// Valoanturi sarjaplotteriin (Ruukkilabra, Ahjo 1, tunti 10)
// Kytkenta: 5V -> valovastus -> A0 -> 10 kohm vastus -> GND
// Avaa Tools -> Serial Plotter ja valitse 9600 baud.
// Light sensor to the serial plotter: 5V -> LDR -> A0 -> 10 kohm -> GND, 9600 baud.

const int SENSOR_PIN = A0;      // jannitteenjaon keskikohta / the divider's middle point

void setup() {
  Serial.begin(9600);           // sama nopeus kuin plotterissa / the same speed as the plotter
}

void loop() {
  int value = analogRead(SENSOR_PIN);   // 0...1023 vastaa 0...5 V / 0...1023 means 0...5 V
  Serial.print("valo:");                // nimi kayralle / the curve's name
  Serial.println(value);
  delay(50);                            // 20 lukemaa sekunnissa / 20 readings a second
}
"""

ROBOT = """// Robotin testiohjelma (Ruukkilabra, Ahjo 1, tunnit 12-13)
// Arduino Uno, kaksi DC-moottoria ja kaksikanavainen moottorinohjain (L298N-tyyppinen: ENA/IN1/IN2 ja ENB/IN3/IN4).
// Testaamaton luonnos: Ahjon robottialustaa ei ole viela valittu. Tarkista pinnit oman moottorinohjaimesi mukaan.
// Moottorit saavat virran omasta paristosta moottorinohjaimen kautta, ei Arduinon 5V-pinnista. GND-pinnit yhteen.
// Nosta robotti ensin pyorat ilmassa telineen paalle ja kokeile vasta sitten lattialla.
// Robot test sketch: Arduino Uno, two DC motors, an L298N-type driver. Untested draft: check the pins for your driver.
// The motors take their power from their own battery through the driver, never from the 5V pin. Join the GNDs.

const int ENA = 5, IN1 = 7, IN2 = 8;    // vasen moottori / left motor (ENA: nopeus PWM / speed)
const int ENB = 6, IN3 = 9, IN4 = 10;   // oikea moottori / right motor

const int SPEED = 160;                  // 0...255; aloita pienella / start low
const int DRIVE_MS = 1000;              // ajoaika / driving time
const int TURN_MS = 400;                // kaannos, saada niin etta kulma on 90 astetta / adjust until the turn is 90 degrees

void motor(int en, int a, int b, int speed) {   // speed -255...255
  digitalWrite(a, speed > 0); digitalWrite(b, speed < 0);
  analogWrite(en, abs(speed));
}

void drive(int left, int right, int ms) {
  motor(ENA, IN1, IN2, left); motor(ENB, IN3, IN4, right);
  delay(ms);
  motor(ENA, IN1, IN2, 0); motor(ENB, IN3, IN4, 0);
  delay(500);                           // tauko / pause
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int p : pins) pinMode(p, OUTPUT);
  delay(3000);                          // aikaa laskea robotti alas / time to put the robot down
  drive(SPEED, SPEED, DRIVE_MS);        // eteen / forwards
  drive(-SPEED, -SPEED, DRIVE_MS);      // taakse / backwards
  drive(SPEED, -SPEED, TURN_MS);        // kaannos oikealle / turn right
  drive(-SPEED, SPEED, TURN_MS);        // kaannos vasemmalle / turn left
}

void loop() {
  // Tunti 13: ajakaa nelio toistamalla neljasti drive(SPEED, SPEED, DRIVE_MS) ja drive(SPEED, -SPEED, TURN_MS).
  // Lesson 13: drive a square by repeating forwards and a right turn four times.
}

// Tunti 13, anturikokeilu: painike robotin keulaan pinnin 2 ja GND:n valiin. Lisaa setup()-osaan
//   pinMode(2, INPUT_PULLUP);
// ja aja eteenpain vain, kun painike ei ole painettuna (painettuna digitalRead(2) on LOW):
//   if (digitalRead(2) == HIGH) { motor(ENA, IN1, IN2, SPEED); motor(ENB, IN3, IN4, SPEED); }
//   else { motor(ENA, IN1, IN2, 0); motor(ENB, IN3, IN4, 0); }
// Lesson 13, sensor trial: a push button on the robot's front between pin 2 and GND, pinMode(2, INPUT_PULLUP),
// and drive forwards only while digitalRead(2) is HIGH (the button is not pressed); otherwise stop.
"""

AIRBIT = """// Air:bit 2 -ohjaimen aloitusohjelma (Ruukkilabra, Dronelabra, tunti 5)
// MakeCode (makecode.microbit.org): vaihda JavaScript-nakymaan, liita ohjelma ja palaa lohkoihin.
// Testaamaton luonnos. Kokeile aina ensin ILMAN POTKUREITA: kaynnistyvatko ja pysahtyvatko moottorit hallitusti?
// Ohjain lahettaa viisi arvoa (valmistajan ohjeen "PARTY"): P = pitch, A = arm, R = roll, T = throttle, Y = yaw.
// Starter for the Air:bit 2 hand controller. Untested draft: always try it first WITHOUT PROPELLERS.

let radioGroup = 7      // vaihda ryhmasi omaksi numeroksi; dronessa pitaa olla sama / your group's own number, the same on the drone
let arm = 0             // 0 = moottorit eivat kay, 1 = kaynnistyslupa / 1 = the motors may run
let throttle = 0        // kaasu 0...100
let pitch = 0           // kallistus eteen ja taakse, asteina / forwards and backwards, degrees
let roll = 0            // kallistus sivulle, asteina / sideways, degrees

radio.setGroup(radioGroup)
basic.showNumber(radioGroup)

// A pienentaa kaasua, B kasvattaa. Yli 40:n askel on 1, jotta leijunnan saato on tarkkaa.
// A lowers the throttle, B raises it. Above 40 the step is 1 for a finer hover.
input.onButtonPressed(Button.A, function () {
    throttle = Math.max(0, throttle - (throttle > 40 ? 1 : 5))
})
input.onButtonPressed(Button.B, function () {
    throttle = Math.min(100, throttle + (throttle >= 40 ? 1 : 5))
})

// A+B yhta aikaa: kaynnistyslupa paalle tai pois. Kaasu nollataan aina samalla.
// A+B together: arm or disarm. The throttle always returns to zero.
input.onButtonPressed(Button.AB, function () {
    arm = arm == 0 ? 1 : 0
    throttle = 0
})

// Hatapysaytys: ravista ohjainta. / Emergency stop: shake the controller.
input.onGesture(Gesture.Shake, function () {
    arm = 0
    throttle = 0
})

basic.forever(function () {
    pitch = Math.constrain(input.rotation(Rotation.Pitch), -45, 45)
    roll = Math.constrain(input.rotation(Rotation.Roll), -45, 45)
    radio.sendValue("P", pitch)
    radio.sendValue("A", arm)
    radio.sendValue("R", roll)
    radio.sendValue("T", throttle)
    radio.sendValue("Y", 0)          // kaanto on jatkotehtava / yaw is an extra task

    // Naytto: vasen ylakulma = kaynnistyslupa, vasen sarake = kaasu, piste = kallistus
    // Display: top left = armed, left column = throttle, the dot = tilt
    basic.clearScreen()
    if (arm == 1) {
        led.plot(0, 0)
    }
    led.plot(0, 4 - Math.idiv(throttle, 25))
    led.plot(Math.round(Math.map(roll, -45, 45, 0, 4)), Math.round(Math.map(pitch, -45, 45, 0, 4)))
})

// Tarkista ilman potkureita, etta kallistuksen suunta vastaa dronen liiketta. Jos suunta on vaarin pain,
// vaihda arvon etumerkki (esimerkiksi radio.sendValue("P", -pitch)).
// Check without propellers that the tilt direction matches the drone. If it is reversed, change the sign.
"""

EXAMPLE_DATA = """# Keksitty harjoitusaineisto, ei mitattu oikealla dronella / Invented practice data, not measured with a real drone
sarja;toisto;etaisyys_cm
lahto 2 m;1;12,5
lahto 2 m;2;18,0
lahto 2 m;3;9,5
lahto 2 m;4;22,0
lahto 2 m;5;15,5
lahto 4 m;1;21,0
lahto 4 m;2;30,5
lahto 4 m;3;17,5
lahto 4 m;4;26,0
lahto 4 m;5;34,5
"""

ANALYSIS = """# Mittaussarjojen analyysi (Ruukkilabra, Dronelabra)
# Lukee CSV-tiedoston, jossa on sarakkeet sarja;toisto;arvo, laskee jokaiselle sarjalle keskiarvon,
# keskihajonnan ja vaihteluvalin ja piirtaa kuvaajan. Desimaalipilkku ja -piste kelpaavat molemmat.
# Reads a CSV file with the columns series;run;value, prints the mean, standard deviation and range of each
# series and draws a graph. Both a decimal comma and a decimal point are read.
#
# Kaytto / Use:   python lentoanalyysi.py lentodata-esimerkki.csv
import csv
import statistics
import sys

tiedosto = sys.argv[1] if len(sys.argv) > 1 else "lentodata-esimerkki.csv"

sarjat = {}          # sarjan nimi -> lista mittauksia / series name -> list of measurements
suure = "arvo"
with open(tiedosto, encoding="utf-8") as f:
    rivit = [r for r in csv.reader(f, delimiter=";") if r and not r[0].startswith("#")]
suure = rivit[0][2]                      # otsikkorivin kolmas sarake / the header's third column
for sarja, toisto, arvo in (r[:3] for r in rivit[1:]):
    if arvo.strip() == "":
        continue                         # tyhja rivi / an empty row
    sarjat.setdefault(sarja, []).append(float(arvo.replace(",", ".")))

for nimi, arvot in sarjat.items():
    ka = statistics.mean(arvot)
    kh = statistics.stdev(arvot) if len(arvot) > 1 else 0.0
    print(f"{nimi}: n = {len(arvot)}, keskiarvo = {ka:.1f}, keskihajonta = {kh:.1f}, "
          f"vaihteluvali = {min(arvot):.1f}...{max(arvot):.1f}")

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Kuvaajaa ei piirretty: asenna matplotlib (pip install matplotlib).")
    sys.exit()

for i, (nimi, arvot) in enumerate(sarjat.items()):
    plt.plot([i] * len(arvot), arvot, "o", alpha=0.6)                    # jokainen mittaus / every measurement
    plt.errorbar(i, statistics.mean(arvot), yerr=statistics.stdev(arvot) if len(arvot) > 1 else 0,
                 fmt="_", color="black", markersize=24, capsize=6)       # keskiarvo ja keskihajonta / mean and sd
plt.xticks(range(len(sarjat)), list(sarjat))
plt.xlim(-0.5, len(sarjat) - 0.5)
plt.ylabel(suure)
plt.title("Mittaukset, keskiarvo ja keskihajonta")
plt.savefig("lentoanalyysi.png", dpi=150)
print("Kuvaaja tallennettu tiedostoon lentoanalyysi.png")
plt.show()
"""

TEMPLATES = {   # semicolons and decimal commas open in a Finnish spreadsheet; the headers say both languages
    "kuormituskoe.csv": "Palkki tai rakenne / Beam or structure;Oma massa (g) / Own mass (g);Kuorma, jonka se kesti (g) / Load it held (g);Mitä tapahtui / What happened",
    "ennen-jalkeen.csv": "Mitattava kohta / What you measure;Malli (mm) / Model (mm);Ennen (mm) / Before (mm);Jälkeen (mm) / After (mm);Paraniko? / Better?",
    "pariston-kesto.csv": "Laite / Device;Jännite (V) / Voltage (V);Virta (mA) / Current (mA);Pariston kapasiteetti (mAh) / Capacity (mAh);Arvio (h) = mAh / mA / Estimate (h)",
    "lentopoytakirja.csv": "Lento / Flight;Drone;Lentäjä / Pilot;Tähystäjä tai turvavastaava / Observer or safety officer;Akku: täysi vai käytetty / Battery: full or used;Kesto (s) / Duration (s);Mitattu arvo ja yksikkö / Measured value and unit;Havainto / Note",
    "testisuunnitelma.csv": "Testi / Test;Mittari tai havainto / Measure or observation;Toisto 1 / Run 1;Toisto 2 / Run 2;Toisto 3 / Run 3;Havainto / Note",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, text in files().items():
        (OUT / name).write_text(text)
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
