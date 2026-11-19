#!/usr/bin/env python3
"""Writes the installable-site icons (work queue 17a PR 2) into assets/shared/brand/ from ruukkilabra-symboli.svg:
ruukkilabra-192.png and -512.png (the symbol on the site's page colour, 12 % margin) and ruukkilabra-maskable-512.png
(26 % margin, inside the maskable safe zone). The logo is not redrawn; run again only when the symbol changes.
Needs Playwright with Chromium (PW_CHROMIUM, see _browser.py)."""
import base64, pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _browser import launch
from playwright.sync_api import sync_playwright

BRAND = pathlib.Path(__file__).resolve().parents[1] / "assets/shared/brand"
BG = "#f7f3ec"                                   # the theme-color of the pages
ICONS = (("ruukkilabra-192.png", 192, 0.12), ("ruukkilabra-512.png", 512, 0.12), ("ruukkilabra-maskable-512.png", 512, 0.26))


def main():
    svg = base64.b64encode((BRAND / "ruukkilabra-symboli.svg").read_bytes()).decode()
    with sync_playwright() as p:
        b = launch(p)
        for name, size, margin in ICONS:
            pg = b.new_page(viewport={"width": size, "height": size}, device_scale_factor=1)
            m = round(size * margin)
            pg.set_content(f'<body style="margin:0;background:{BG}"><img src="data:image/svg+xml;base64,{svg}" '
                           f'style="position:absolute;left:{m}px;top:{m}px;width:{size - 2 * m}px;height:{size - 2 * m}px">')
            pg.wait_for_function("document.images[0].complete")
            pg.screenshot(path=str(BRAND / name))
            pg.close()
        b.close()


if __name__ == "__main__":
    main()
