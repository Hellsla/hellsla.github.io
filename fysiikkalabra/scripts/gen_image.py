"""Placeholder for the image-creator agent: plug in your image API here (set IMAGE_API_KEY).
Usage: python scripts/gen_image.py "<prompt>" assets/<id>/hero.png"""
import sys, os, pathlib
prompt, out = sys.argv[1], pathlib.Path(sys.argv[2]); out.parent.mkdir(parents=True, exist_ok=True)
if not os.environ.get("IMAGE_API_KEY"):
    out.with_suffix(".svg").write_text(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 630'><rect width='1200' height='630' fill='#eef'/><text x='60' y='330' font-size='48' font-family='sans-serif'>{prompt[:60]}</text></svg>")
    print("no IMAGE_API_KEY: wrote SVG placeholder", out.with_suffix(".svg")); sys.exit(0)
raise SystemExit("TODO: call your image API here and write", out)
