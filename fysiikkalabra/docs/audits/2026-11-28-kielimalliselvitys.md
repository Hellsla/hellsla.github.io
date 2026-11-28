# FY9: paikallisen kielimallin selvitys (työjono 11b PR 10)

Vain selvitys, ei toteutusta. Suunnitelma: `docs/FY9_ADAPTIVE_PLAN.md` rivi K, PR 10, P12. Ehdoton rajoitus: opiskelijoiden
käyttö ei saa aiheuttaa jatkuvia kielimallikuluja; ei palvelinta, avaimia, tunnuksia eikä oppilastietojen keruuta.
Mikään muu ominaisuus ei saa riippua tästä. Lähteet luettiin 2026-11-28; "tarkistamatta" = ei luettu tässä sessiossa.

## 1. Mitä malli tekisi, mitä nykyinen palaute ei

Nykyinen palaute on deterministinen (tarkistus ±2 %, kiinteät vihjeet, valmentajan lokit). Paikallinen malli voisi
vain selittää vapaamuotoista vastausta tai muotoilla vihjeen uudelleen. Se ei saa arvioida oikeellisuutta: numeerisen
vastauksen tarkistaa `answers.py`, ja malli korvaisi sen epävarmalla arvauksella.

## 2. Tekniikka (tarkistettu)

| Asia | Tieto | Lähde |
|---|---|---|
| WebLLM | "Everything runs inside the browser with no server support and is accelerated with WebGPU." | [README](https://raw.githubusercontent.com/mlc-ai/web-llm/HEAD/README.md) |
| WebLLM-mallit (VRAM-arvio) | Qwen2.5-1.5B-Instruct q4f16_1: 1,6 Gt; gemma3-1b-it q4f16_1: 711 Mt; Llama-3.2-1B-Instruct q4f16_1: 879 Mt; gemma-2-2b-it q4f16_1: 1,9 Gt (konteksti 4K). "Memory requirements are estimates." | [mallilista](https://webllm.mlc.ai/models/) |
| Transformers.js | ONNX Runtime; selaimessa oletus CPU (WASM), WebGPU valittavissa; "WebGPU API is still experimental in many browsers" | [README](https://github.com/huggingface/transformers.js) |
| WebGPU, tietokone | Chrome/Edge 113 (Windows, macOS, ChromeOS); Linux "in progress"; Firefox Windows 141, macOS ARM64 145 | [web.dev 2025-11-25](https://web.dev/blog/webgpu-supported-major-browsers) |
| WebGPU, puhelin | Android: Chrome 121, Android 12+ ja Qualcomm/ARM-GPU; Safari: iOS 26 ja iPadOS 26; Firefox Android "in progress" | sama |
| Chromen sisäinen tekoäly | Vaatii yli 4 Gt VRAM tai 16 Gt RAM + 4 ydintä, vähintään 22 Gt tilaa; ei mobiilissa; Chrome 149:n kielet: en, es, ja, de, fr (suomea ei listattu) | [Chrome-ohje](https://developer.chrome.com/docs/ai/get-started) |
| Lisenssit | Qwen2.5-1.5B-Instruct: apache-2.0, 1,54 Mrd parametria, "over 29 languages" (suomea ei nimetty). Gemma 3 1B: lisenssi "gemma", 1,0 Mrd parametria, "over 140 languages", käyttöehdot hyväksyttävä kirjautuneena | [Qwen](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct), [Gemma](https://huggingface.co/google/gemma-3-1b-it) |
| Ennakkotapaus | `templates/readaloud.js`: Supertonic 3 (OpenRAIL-M), noin 145 Mt, onnxruntime-web, välimuistissa; oletus puhelimessa ja ilman WebGPU:ta laitteen oma ääni | tämä repositorio |

Tarkistamatta: Gemman käyttöehtojen jakelu- ja käyttörajoitukset (`ai.google.dev/gemma/terms` ohjasi osoitteeseen,
jota ei voitu lukea); WebLLM-projektin lisenssi (README ei sano); mallien suomen laatu (ei luettua mittausta);
todelliset latausajat ja akunkulutus lukiolaisten laitteilla; WebGPU-osuus oppilaiden laitteista.

## 3. Sopiiko lukiolaisten koneille ja Abittiin

- **Puhelimet:** WebGPU on vasta tietyillä Android-laitteilla (Android 12+, Qualcomm/ARM) ja iOS 26:ssa. Sivuston
  oma linja on jo, että puhelimessa ja ilman WebGPU:ta käytetään kevyttä vaihtoehtoa. Malli (0,7–1,9 Gt VRAM-arvio) on
  moninkertaisesti ääneenluvun 145 Mt:tä; lataus ja akku tarkistamatta.
- **Koulun koneet:** vaatimukset (selain, WebGPU, muisti) tarkistamatta; koulun laitekanta on tuntematon.
- **Abitti:** Abitti-sivun mukaan ylioppilaskokeessa kokeen tekemiseen käytetään vain koejärjestelmää
  ("et voi ... käyttää tietokonettasi muuhun kuin kokeen tekemiseen"; macOS: ei pääsyä tiedostoihin eikä sovelluksiin;
  [kokeeseen liittyminen](https://www.abitti.fi/kokelaalle/kokeeseen-liittyminen/),
  [tekninen valvonta](https://www.abitti.fi/kokelaalle/tekninen-valvonta-kokelassovelluksessa/)). Paikallinen malli
  toimisi siis vain harjoitellessa Abitin ulkopuolella, ei itse kokeessa. Internet-yhteyden täsmällinen sääntö kokeessa:
  tarkistamatta.

## 4. Fysiikan tarkkuus (arvio, ei lähdeväite)

Pieni malli (1–2 Mrd parametria) voi kirjoittaa uskottavan mutta väärän ratkaisun: väärä yksikkö, virheellinen
kaava, laskuvirhe tai keksitty perustelu. Opiskelija ei välttämättä tunnista virhettä, koska hän kysyy juuri siksi, ettei osaa itse.
Palaute näyttäisi arvioinnilta, vaikka se ei sitä ole ("arvioinnin näennäinen luotettavuus"). Suomen laatu on
tarkistamatta, ja pienet mallit ovat yleensä heikompia pienillä kielillä (tämä on oletus, ei tarkistettu). Sivuston
sääntö (`physics-guardrails.md`, katselmoinnit) edellyttää tieteellistä tarkistusta; mallin vapaa tuotos ei kulje
sen läpi. Lisäksi Gemma-lisenssin ehdot pitäisi lukea ennen mallin jakamista omalta sivustolta.

## 5. Suositus opettajalle: odotetaan

Ei toteuteta nyt. Perustelut:
1. Hyöty on kapea: deterministinen palaute kattaa tarkistuksen; malli lisäisi vain selitystä, ja siinä virheriski on suurin.
2. Puhelinkattavuus on vajaa (WebGPU rajattu), ja mallien VRAM-arviot ovat noin 5–13 kertaa ääneenluvun mallin koko (tiedostokoot tarkistamatta).
3. Suomen laatu, Gemman ehdot ja Abitti-sääntö ovat tarkistamatta; ilman niitä päätös olisi arvaus.
4. Kulurajoitus täyttyisi (kaikki ajettaisiin asiakkaan koneella), mutta oikeellisuusriski ei poistu.

Kun halutaan arvioida uudelleen: (a) mittaa suomen laatu kymmenellä oikealla FY9-tehtävällä ja kirjaa virheet,
(b) lue Gemman ehdot, (c) kysy koululta laitteet ja WebGPU-tuki, (d) vasta sitten pieni kokeilu, jossa malli vain
selittää jo tarkistetun mallivastauksen, ei arvioi opiskelijan vastausta.
