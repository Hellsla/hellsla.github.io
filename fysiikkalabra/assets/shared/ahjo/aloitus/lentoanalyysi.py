# Mittaussarjojen analyysi (Ruukkilabra, Dronelabra)
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
