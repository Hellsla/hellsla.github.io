"""Recorded read-aloud for Finnish lessons (teacher 2026-11-15, work queue 5c): ElevenLabs "Oskari - Finnish".
Usage:
  python scripts/readaloud_audio.py <page-id> --dry            list the blocks to record, their speech text and its characters
  python scripts/readaloud_audio.py <page-id> --formulas       list the page's formulas as "TeX → puheteksti"
  python scripts/readaloud_audio.py <page-id> [--limit N]      record every block that has no current recording

Opens the built page (site/<page-id>.html), asks readaloud.js (window.flSpeech.blocks) for the blocks the Kuuntele button
reads, and records each block once: one mp3 per block and the start and end time of every word (ElevenLabs'
with-timestamps text-to-speech), in <audio repository>/fi/<page-id>/<hash>.mp3 and assets/audio/fi/<page-id>.json, which
build.py copies to site/audio/. The hash is of the block's speech text (the same function as readaloud.js textHash), so a
block that changed is read by the other voices until it is recorded again, and a block that did not change is never paid
for twice. This runs in a developer session, never in a student's browser. The key is the environment's network secret
for api.elevenlabs.io (the proxy adds xi-api-key; the placeholder below is never a real key) and is never written anywhere.
The mp3 files go to a checkout of Hellsla/ruukkilabra-audio (beside this repository, or RUUKKILABRA_AUDIO_DIR) as
fi/<page-id>/<hash>.mp3; only the manifest, assets/audio/fi/<page-id>.json, is kept here.
The text sent is the block's speech text made easier to say: numbers and lone symbols written out in words
(`spoken()`); the page's own wording is not changed, and every word of the page keeps one timing."""
import base64, json, os, pathlib, re, sys, urllib.error, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

VOICE_ID = "nJ8YqEenIxs18T0Hu4QE"            # Oskari - Finnish (teacher 2026-11-15)
VOICE_NAME = "Oskari - Finnish"
MODEL = "eleven_multilingual_v2"
AUDIO = ROOT / "assets" / "audio" / "fi"        # the manifests (block hashes and word times): in this repository, published in site/audio/fi/
# The mp3 files are not in this repository (teacher 2026-11-15): they live in Hellsla/ruukkilabra-audio as fi/<page-id>/<hash>.mp3
# (the way the read-aloud models live in Hellsla/ruukkilabra-models) and the deploy workflow copies them to the published site.
# A checkout of it beside this repository, or RUUKKILABRA_AUDIO_DIR, is where a recording is written.
MP3_ROOT = pathlib.Path(os.environ.get("RUUKKILABRA_AUDIO_DIR") or ROOT.parent.parent / "ruukkilabra-audio")
API = "https://api.elevenlabs.io/v1/text-to-speech/{}/with-timestamps?output_format=mp3_44100_64"


def text_hash(t):
    """FNV-1a over the UTF-16 code units + the length: the same as textHash in templates/readaloud.js."""
    h = 0x811C9DC5
    u = t.encode("utf-16-le")
    for i in range(0, len(u), 2):
        h ^= u[i] | (u[i + 1] << 8)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return f"{h:08x}{len(u) // 2:04x}"


# ---- Finnish words for what a voice reads badly --------------------------------------------------------------------
ONES = ["nolla", "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän"]
TEENS = ["kymmenen", "yksitoista", "kaksitoista", "kolmetoista", "neljätoista", "viisitoista", "kuusitoista", "seitsemäntoista",
         "kahdeksantoista", "yhdeksäntoista"]
TENS = {2: "kaksikymmentä", 3: "kolmekymmentä", 4: "neljäkymmentä", 5: "viisikymmentä", 6: "kuusikymmentä", 7: "seitsemänkymmentä",
        8: "kahdeksankymmentä", 9: "yhdeksänkymmentä"}
LETTERS = {"a": "aa", "b": "bee", "c": "see", "d": "dee", "e": "ee", "f": "äf", "g": "gee", "h": "hoo", "i": "ii", "j": "jii",
           "k": "koo", "l": "äl", "m": "äm", "n": "än", "o": "oo", "p": "pee", "q": "kuu", "r": "är", "s": "äs", "t": "tee",
           "u": "uu", "v": "vee", "w": "kaksoisvee", "x": "äks", "y": "yy", "z": "tset", "å": "oo", "ä": "ää", "ö": "öö"}
ACRONYMS = {"SI": "es ii", "AU": "aa uu", "m/s": "metriä sekunnissa"}      # short words of the lesson that a voice would read as a word


def below_thousand(n):
    out = ""
    if n >= 100:
        out += ("" if n // 100 == 1 else ONES[n // 100]) + "sata"
        n %= 100
    if n >= 20:
        out += TENS[n // 10]
        n %= 10
        if n: out += ONES[n]
    elif n >= 10: out += TEENS[n - 10]
    elif n or not out: out += ONES[n]
    return out


def integer(n):
    """The nominative of a whole number, written out (up to 10^12)."""
    if n == 0: return "nolla"
    parts = []
    for size, one, many in ((10**9, "miljardi", "miljardia"), (10**6, "miljoona", "miljoonaa")):
        k, n = divmod(n, size)
        if k: parts.append(one if k == 1 else below_thousand(k) + " " + many)
    k, n = divmod(n, 1000)                         # thousands and the rest are one word: kaksituhattakaksikymmentäkaksi
    tail = ("tuhat" if k == 1 else below_thousand(k) + "tuhatta" if k else "") + (below_thousand(n) if n else "")
    if tail: parts.append(tail)
    return " ".join(parts)


def number(tok):
    """'1,7' → 'yksi pilkku seitsemän'; '93' → 'yhdeksänkymmentäkolme'; the digits after the comma one by one."""
    m = re.fullmatch(r"(\d+)(?:[,.](\d+))?", tok)
    if not m: return None
    out = integer(int(m[1]))
    if m[2]: out += " pilkku " + " ".join(ONES[int(c)] for c in m[2])
    return out


def spoken(token):
    """One word of the block's speech text as it is said; punctuation around it stays."""
    t = token.replace("\u2060", "").replace("\u00ad", "").replace("\u200b", "")   # word joiner, soft hyphen, zero-width space
    m = re.fullmatch(r"([(\"“]*)(.*?)([.,:;!?)\"”]*)", t)
    pre, core, post = m[1], m[2], m[3]
    if core in ACRONYMS: core = ACRONYMS[core]
    elif len(core) == 1 and core.lower() in LETTERS: core = LETTERS[core.lower()]
    elif number(core): core = number(core)
    elif core == "–": core = ","
    return pre + core + post


def spoken_text(text):
    """(the text sent to the voice, for each word of the page the (first, last) character of its spoken words)."""
    out, spans = "", []
    for tok in text.split():
        tok = tok.replace("\u2060", "").replace("\u00ad", "").replace("\u200b", "")
        if not tok: continue
        w = spoken(tok)
        glue = not out or w == "," or re.fullmatch(r"[.,:;!?)]+|:\w+", tok) is not None   # "metriä ." → "metriä.", "AU :n" → "AU:n"
        if out and not glue: out += " "
        a = len(out)
        out += w
        spans.append((a, max(a, len(out) - 1)))
    return out, spans


# ---- the page ---------------------------------------------------------------------------------------------------------
def page_blocks(page_id):
    from playwright.sync_api import sync_playwright
    from _browser import launch
    f = ROOT / "site" / f"{page_id}.html"
    if not f.is_file(): sys.exit(f"{f} is not built (python scripts/build.py --all && python scripts/build.py)")
    with sync_playwright() as pw:
        b = launch(pw)
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.goto(f.as_uri()); pg.wait_for_timeout(1500)
        blocks = pg.evaluate("window.flSpeech ? window.flSpeech.blocks() : null")
        pairs = pg.evaluate("""(() => { const seen = new Map();
            for (const el of window.flSpeech.elements()) for (const k of el.querySelectorAll('.katex')) {
              if (k.closest('[data-speech]')) continue;
              const a = k.querySelector('annotation[encoding="application/x-tex"]'); if (!a || seen.has(a.textContent)) continue;
              let w; try { w = (k.closest('.katex-display') && (a.textContent.length > 140 || /\\\\begin/.test(a.textContent))) ? 'kaava' : window.flSpeech.tex(a.textContent); } catch (e) { w = '(virhe)'; }
              seen.set(a.textContent, w); }
            return [...seen]; })()""")
        hashes = pg.evaluate("window.flSpeech.blocks().map((t) => window.flSpeech.hash(t))")
        b.close()
    if blocks is None: sys.exit("window.flSpeech is missing: readaloud.js did not start")
    return blocks, pairs, hashes


def record(text):
    text_out, spans = spoken_text(text)
    body = json.dumps({"text": text_out, "model_id": MODEL, "language_code": "fi", "seed": 1}).encode()
    req = urllib.request.Request(API.format(VOICE_ID), data=body, headers={"xi-api-key": "proxy-injected", "Content-Type": "application/json"})
    try: r = json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e: sys.exit(f"ElevenLabs {e.code}: {e.read()[:300]!r}")
    al = r["alignment"]
    starts, ends = al["character_start_times_seconds"], al["character_end_times_seconds"]
    if len(starts) != len(text_out): sys.exit(f"alignment has {len(starts)} characters for {len(text_out)} sent")
    words = [[round(starts[a], 3), round(max(ends[min(b, len(text_out) - 1)], starts[a]), 3)] for a, b in spans]
    for k in range(len(words) - 1): words[k][1] = max(words[k][1], words[k + 1][0])   # no dark gap between two words
    return text_out, base64.b64decode(r["audio_base64"]), words


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"): sys.exit(__doc__)
    page_id, flags = a[0], a[1:]
    blocks, pairs, hashes = page_blocks(page_id)
    if "--formulas" in flags:
        for tex, w in pairs: print(f"{tex} → {w}")
        return
    mf = AUDIO / f"{page_id}.json"
    man = json.loads(mf.read_text()) if mf.is_file() else {"voice": VOICE_NAME, "voice_id": VOICE_ID, "model": MODEL, "blocks": {}}
    todo, seen = [], set()
    for t, h in zip(blocks, hashes):
        if h in seen or h in man["blocks"]: continue          # recorded already: the manifest says so, whether or not the mp3 checkout is here
        seen.add(h); todo.append((t, h, spoken_text(t)[0]))
    print(f"{len(blocks)} blocks, {len(todo)} to record, {sum(len(sp) for _, _, sp in todo)} characters")
    if "--dry" in flags:
        for t, h, sp in todo: print(f"[{h}] {len(sp)}: {sp}")
        return
    limit = int(flags[flags.index("--limit") + 1]) if "--limit" in flags else len(todo)
    done = used = 0
    if todo and not MP3_ROOT.is_dir(): sys.exit(f"{MP3_ROOT} is missing: clone Hellsla/ruukkilabra-audio there (or set RUUKKILABRA_AUDIO_DIR); nothing was sent")
    (MP3_ROOT / "fi" / page_id).mkdir(parents=True, exist_ok=True) if todo else None
    AUDIO.mkdir(parents=True, exist_ok=True)
    for t, h, sp in todo[:limit]:
        text_out, mp3, words = record(t)
        (MP3_ROOT / "fi" / page_id / f"{h}.mp3").write_bytes(mp3)
        man["blocks"][h] = {"file": f"{page_id}/{h}.mp3", "words": words}
        used += len(text_out); done += 1
        mf.write_text(json.dumps(man, ensure_ascii=False, separators=(",", ":")) + "\n")   # after every block: a stopped run loses nothing paid for
    stale = [h for h in man["blocks"] if h not in set(hashes)]       # recordings of text that has since changed: dropped, never published
    for h in stale:
        (MP3_ROOT / "fi" / man["blocks"].pop(h)["file"]).unlink(missing_ok=True)
    if stale: mf.write_text(json.dumps(man, ensure_ascii=False, separators=(",", ":")) + "\n"); print(f"dropped {len(stale)} stale recordings")
    size = sum(p.stat().st_size for p in (MP3_ROOT / "fi" / page_id).glob("*.mp3"))
    print(f"recorded {done} blocks, {used} characters sent, {size / 1e6:.2f} MB of mp3 in {MP3_ROOT / 'fi' / page_id}")


if __name__ == "__main__":
    main()
