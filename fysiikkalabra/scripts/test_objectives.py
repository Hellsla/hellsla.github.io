"""objectives.py accepts goals that complete "Tällä tunnilla opit" / "In this lesson, you will learn to" and catches
the forms that do not (teacher 2026-10-29). Module goals are not lesson goals: their grammar is never checked.

  python scripts/test_objectives.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import objectives as O, reviews

fails = 0
def check(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f": {detail}")); fails += not ok

def errs(g, lang): return O.check(g, lang)[0]
def warns(g, lang): return O.check(g, lang)[1]

GOOD = {
    "fi": ["laskemaan polttoaineesta vapautuvan energian lämpöarvon ja massan avulla.",                         # one verb
           "vertailemaan polttoaineita ja ruokaa energiasisällön perusteella sekä selittämään, miten ruoan energiasisältö eroaa lämpöarvosta.",   # parallel verbs
           "erottamaan vapautuneen energian hyötyenergiasta hyötysuhteen avulla.",
           "laskemaan tehon kaavalla $P = E : t$.", "lukemaan $(t, s)$-kuvaajasta nopeuden ja alkupaikan."],
    "fi-easy": ["laskemaan kappaleen painon massan avulla.", "selittämään, miksi kappaleen paino riippuu taivaankappaleesta.",
                "erottamaan massan ja painon toisistaan.",
                "käyttämään Boylen lakia. Isotermisessä tilanmuutoksessa paineen ja tilavuuden tulo pysyy vakiona."],   # a second sentence may explain
    "en": ["calculate the energy released from a fuel using its heat of combustion and mass.",
           "compare fuels and food by energy content and explain how food energy differs from the heat of combustion.",
           "tell released energy apart from useful energy using efficiency.", "use Boyle's law.", "assess the result."],
}
for lang, goals in GOOD.items():
    for g in goals:
        check(f"{lang} accepts: {g[:50]}", not errs([g], lang) and not warns([g], lang), O.check([g], lang))

BAD = {   # certainly wrong under the heading: errors
    "fi": ["Osaat laskea polttoaineesta vapautuvan energian.", "Opit laskemaan tehon.", "Sinä osaat selittää paineen.",
           "Tunnistat neljä perusvuorovaikutusta.", "Laskemaan tehon.", "laskea tehon kaavalla $P = E : t$."],
    "fi-easy": ["Osaat laskea painon.", "osaat erottaa massan ja painon."],
    "en": ["You can calculate power.", "You recognise the four interactions.", "to calculate power.", "Calculate power.", "can explain why."],
}
for lang, goals in BAD.items():
    for g in goals:
        check(f"{lang} rejects: {g}", bool(errs([g], lang)), O.check([g], lang))

SUSPECT = {   # broken parallel form: a warning for a person to look at
    "fi": ["laskemaan tehon ja selittää, miksi lasku riippuu ajasta.", "laskemaan tehon ja osaat selittää sen."],
    "fi-easy": ["vertailemaan polttoaineita energiasisällön perusteella. Opit myös selittämään, miten ruoka eroaa."],   # caught by the 2026-10-29 review
    "en": ["calculate power and can explain why.", "calculates the power."],
}
for lang, goals in SUSPECT.items():
    for g in goals:
        check(f"{lang} flags: {g}", not errs([g], lang) and bool(warns([g], lang)), O.check([g], lang))

# module goals and Pohjatiedot use their own grammar and are not lesson goals: never passed to the check
cur = json.loads((reviews.ROOT / "curriculum.json").read_text())
check("module goals keep \"osaa …\" (curriculum.json is not rewritten)", any(g.startswith("osaa ") for g in cur["FY1"]["tavoitteet"]))

# a goal rephrased with its formulas and numbers kept is the review category objective-form; a changed formula is not
old = json.dumps({"learn": ["Osaat laskea tehon kaavalla $P = E : t$.", "Osaat selittää 2 asiaa."], "x": 1}, ensure_ascii=False)
new = json.dumps({"learn": ["laskemaan tehon kaavalla $P = E : t$.", "selittämään 2 asiaa."], "x": 1}, ensure_ascii=False)
check("objective-form: rephrased goals", reviews.objective_form(old, new) is not None and json.loads(reviews.objective_form(old, new)) == json.loads(new))
check("objective-form: a changed formula is not a rephrasing", reviews.objective_form(old, new.replace("E : t", "W : t")) is None)
check("objective-form: a changed number is not a rephrasing", reviews.objective_form(old, new.replace("2 asiaa", "3 asiaa")) is None)
check("objective-form: a goal added is not a rephrasing", reviews.objective_form(old, json.dumps({"learn": json.loads(new)["learn"] + ["kuvaamaan …"], "x": 1})) is None)
check("objective-form rule: science none, pedagogy delta", reviews.RULES["objective-form"] == ("none", "delta"))

# every lesson now passes
import subprocess
r = subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / "objectives.py")], capture_output=True, text=True)
check("every lesson's goals pass", r.returncode == 0 and "WARNING" not in r.stdout, r.stdout[-800:])
print(f"{fails} failure(s)"); sys.exit(1 if fails else 0)
