"""Kirjaa opettajan päätös: python docs/illustration-audit/decide.py <tunniste> "<päätös>" [<tunniste> "<päätös>" ...]"""
import pathlib, sys, datetime, subprocess
HERE = pathlib.Path(__file__).resolve().parent
day = datetime.date.today().isoformat(); done = set()
for fid, dec in zip(sys.argv[1::2], sys.argv[2::2]):
    hit = False
    for p in (HERE / "data").glob("*.tsv"):
        L = p.read_text().splitlines()
        for k, l in enumerate(L):
            if l.split("|")[0] == fid:
                f = (l.split("|") + [""] * 9)[:9]; f[8] = f"{dec} (opettaja {day})"; L[k] = "|".join(f); hit = True; done.add(p.stem)
        p.write_text("\n".join(L) + "\n")
    print(fid, "kirjattu" if hit else "EI LÖYDY")
subprocess.run([sys.executable, str(HERE / "build.py"), *sorted(done)], check=True)
