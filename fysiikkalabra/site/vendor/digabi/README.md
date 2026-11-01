# Digabi rich-text-editor (vendored)

The solution editor under the exercises (templates/lesson.js, "Kirjoita ratkaisu") is the Matriculation Examination
Board's own answer editor, the one students use in Abitti. lesson.js loads these files only when a student first
opens the editor, so a lesson page stays as light as before.

| File | Source | Licence |
|---|---|---|
| rich-text-editor-bundle.js | npm `rich-text-editor` 8.13.0, `dist/rich-text-editor-bundle.js` (React, jQuery and MathQuill inside) | MIT, LICENSE-rich-text-editor |
| mathquill.css, fonts/Symbola.woff2, fonts/Symbola.woff | npm `@digabi/mathquill` 0.10.12, `build/` (the @font-face list trimmed to woff2 and woff) | MPL-2.0 |
| tex-svg.js | npm `mathjax` 3.2.2, `es5/tex-svg.js` | Apache-2.0, LICENSE-mathjax |

Abitti draws each formula on its server (`/math.svg?latex=…`). This site has no server, so lesson.js gives the editor
an `onLatexUpdate` that draws the formula in the browser with MathJax into a self-contained SVG
(`data:image/svg+xml`, the LaTeX in `alt`). The editor and Abitti both read such an image back as an editable formula.

To update: `npm pack rich-text-editor@<version>` (and the two others), copy the same files, and check the editor with
`python scripts/test_writepad.py`.
