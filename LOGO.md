# AlephB logo

The monogram is the Hebrew letter Aleph (א) from **Noto Serif Hebrew** (weight 650)
and a Latin **B** from **Playfair Display** (weight 700), turned into outlines. Both
letters share one ink height and one baseline. No font is needed to show it.

| File | What |
|---|---|
| `logo.svg` | master, `fill="currentColor"` |
| `logo.png` | 512 px tall, transparent |
| `favicon.svg` | square, dark ink or light ink per the browser's theme |
| `favicon-32.png`, `apple-touch-icon.png` | on white |
| `avatar.png` | 1024 px square on white (GitHub, Google, Chrome Web Store) |

## Regenerate

```sh
pip install fonttools resvg-py pillow
curl -LO "https://github.com/google/fonts/raw/main/ofl/notoserifhebrew/NotoSerifHebrew%5Bwdth,wght%5D.ttf"
curl -LO "https://github.com/google/fonts/raw/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"
python tools/logo.py "NotoSerifHebrew[wdth,wght].ttf" 650 "PlayfairDisplay[wght].ttf" 700 > logo.svg
python tools/export.py
```

The fonts are not in this repo. If you change `logo.svg`, paste the new `<svg>` into the `<h1>` of `index.html` and `privacy.html` too.

## Licences

Both fonts are under the SIL Open Font License 1.1, which allows logos made from them:
Noto Serif Hebrew © The Noto Project Authors, and Playfair Display © The Playfair Project Authors.
