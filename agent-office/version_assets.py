#!/usr/bin/env python3
"""Refresh static asset URLs so browsers fetch matching office code after updates."""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = re.compile(r'((?:src|href)=")([^"?]+\.(?:js|css))(?:\?[^\"]*)?(")')


def version_assets():
    page = ROOT / 'index.html'

    def version(match):
        name = match[2]
        asset = (ROOT / name).resolve()
        if not asset.is_relative_to(ROOT):
            raise ValueError(f'Expected an office asset: {name}')
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
        return f'{match[1]}{name}?v={digest}{match[3]}'

    page.write_text(ASSETS.sub(version, page.read_text()))


if __name__ == '__main__':
    version_assets()
