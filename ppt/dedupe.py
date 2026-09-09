"""Sama taustakuva upotettiin kerran kalvoa kohti - yhdistetään ne yhdeksi osaksi."""
import hashlib, re, shutil, sys, zipfile

src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
names = zin.namelist()
data = {n: zin.read(n) for n in names}
zin.close()

media = [n for n in names if n.startswith("ppt/media/") and not n.endswith("/")]
first, drop = {}, {}
for n in sorted(media):
    h = hashlib.sha256(data[n]).hexdigest()
    if h in first:
        drop[n] = first[h]
    else:
        first[h] = n

for n, keep in drop.items():
    print("  %s -> %s" % (n.split('/')[-1], keep.split('/')[-1]))
    del data[n]

if drop:
    sub = {n.split("/")[-1]: keep.split("/")[-1] for n, keep in drop.items()}
    pat = re.compile("|".join(re.escape(k) for k in sorted(sub, key=len, reverse=True)))
    for n in list(data):
        if n.endswith(".rels"):
            x = data[n].decode("utf-8")
            y = pat.sub(lambda m: sub[m.group(0)], x)
            if y != x:
                data[n] = y.encode("utf-8")

with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for n in names:
        if n in data:
            z.writestr(n, data[n])
print("yhdistetty %d kuvaa" % len(drop))
