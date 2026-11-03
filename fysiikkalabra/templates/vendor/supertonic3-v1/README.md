# Supertonic 3 voice (read aloud)

Teacher 2026-11-03: the read-aloud voice of Ruukkilabra ("Nainen" = voice 0 = F1, "Mies" = voice 5 = M1), run in the
student's browser by `templates/readaloud.js` with onnxruntime-web (vendor/ort). 31 languages, Finnish and English
included.

- Model: Supertonic 3 by Supertone Inc., https://huggingface.co/Supertone/supertonic-3
- These files: the sherpa-onnx conversion as packaged in the npm packages @3sln/donki-lle-voice-multi(-2, -3)@0.1.1
  (decoded from their base64 chunks, byte sizes in manifest.json).
- Model licence: BigScience OpenRAIL-M (https://huggingface.co/Supertone/supertonic-3/blob/main/LICENSE). The licence's
  use restrictions apply to everyone who uses this voice; Ruukkilabra uses it only to read its own learning materials
  aloud.
- The folder name carries a version: a changed model goes in a new folder, so the browsers' cached copies
  (Cache Storage "fl-tts-supertonic3-v1") never mix two models.
