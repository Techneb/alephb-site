"""Make the PNG/favicon set from logo.svg. usage: python tools/export.py"""
import io
import re
import resvg_py
from PIL import Image

INK, NIGHT, PAPER = "#15191b", "#eef2f3", "#ffffff"
svg = open("logo.svg").read()
w, h = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
path = re.search(r'<path d="[^"]+"/>', svg).group()


def render(height, color=INK):
    s = svg.replace("currentColor", color)
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=s, height=height))))


def square(size, share, bg=PAPER):
    """The monogram centred on a solid square, `share` of its width."""
    im = render(round(size * share * h / w))
    sq = Image.new("RGBA", (size, size), bg)
    sq.paste(im, ((size - im.width) // 2, (size - im.height) // 2), im)
    return sq


render(512).save("logo.png", optimize=True)
square(32, 0.94).save("favicon-32.png", optimize=True)
square(180, 0.72).save("apple-touch-icon.png", optimize=True)
square(1024, 0.66).save("avatar.png", optimize=True)

# favicon.svg: square viewBox, ink follows the browser's theme
pad = (w - h) / 2
open("favicon.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-pad:.2f} {w} {w}">'
    f"<style>path{{fill:{INK}}}@media (prefers-color-scheme:dark){{path{{fill:{NIGHT}}}}}</style>"
    f"{path}</svg>\n")
