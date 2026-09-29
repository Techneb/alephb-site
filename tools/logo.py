"""Draw the AlephB monogram (א + B) as SVG outlines.

usage: python tools/logo.py ALEPH_FONT ALEPH_WGHT B_FONT B_WGHT > logo.svg
Both glyphs are scaled to the same ink height and set on one baseline.
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

H = 100      # ink height of each letter, in viewBox units
GAP = 15     # space between the letters (original: 12 px at 82 px tall)


def glyph(path, wght, char):
    font = TTFont(path)
    if "fvar" in font:
        axes = {a.axisTag: a.defaultValue for a in font["fvar"].axes}
        axes["wght"] = float(wght)
        font = instantiateVariableFont(font, axes)
    gs = font.getGlyphSet()
    g = gs[font.getBestCmap()[ord(char)]]
    bp = BoundsPen(gs)
    g.draw(bp)
    return gs, g, bp.bounds


def main(af, aw, bf, bw):
    x, paths = 0, []
    for f, w, c in ((af, aw, "א"), (bf, bw, "B")):
        gs, g, (x0, y0, x1, y1) = glyph(f, w, c)
        k = H / (y1 - y0)
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        # flip y, scale to H, move ink to (x, 0)
        g.draw(TransformPen(pen, (k, 0, 0, -k, x - x0 * k, y1 * k)))
        paths.append(pen.getCommands())
        x += (x1 - x0) * k + GAP
    wdt = round(x - GAP, 2)
    print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {wdt} {H}" fill="currentColor">'
          f'<path d="{" ".join(paths)}"/></svg>')


if __name__ == "__main__":
    main(*sys.argv[1:5])
