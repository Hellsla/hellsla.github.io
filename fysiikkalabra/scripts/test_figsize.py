"""figsize.py: an inline figure is never drawn larger than its viewBox; the hero and sized svgs are left alone.

  python scripts/test_figsize.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import figsize

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

n = figsize.natural
out = n('<svg data-fig="kone" viewBox="0 0 420 470" role="img" style="max-width:100%;font-size:20px"><g/></svg>')
check("a narrow figure gets its own width", out.startswith('<svg width="420" data-fig="kone"'), out[:60])
out = n('<svg viewBox="0 0 380 596" style="max-width:min(100%,440px)">')
check("a hand-set cap above the natural size gives way", 'width="380"' in out, out)
for name, src in [("the hero", '<svg class="fig-hero" viewBox="0 0 1200 600" style="max-width:100%">'),
                  ("a sized svg", '<svg viewBox="0 0 24 24" width="24" style="max-width:100%">'),
                  ("an icon without a max-width", '<svg class="ahjo-icon" viewBox="0 0 24 24" height="24">')]:
    check(f"{name} is left alone", n(src) == src, n(src))
check("idempotent", n(n('<svg viewBox="0 0 600 340" style="max-width:100%">')) == '<svg width="600" viewBox="0 0 600 340" style="max-width:100%">')
sys.exit(1 if fails else 0)
