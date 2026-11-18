#!/usr/bin/env python3
"""Render the QuietBabyGear favicon set from the site's SVG mark.

The mark (site/public/favicon.svg) on a 64-unit grid:
  - rounded rect (0,0,64,64), rx=12, fill #fbf7ef (paper)
  - baseline: line (14,42)-(50,42), ink #293733, width 4, round cap
  - curve: M20 38 c 2-9 8-14 17-14 5 0 8 2 10 5 (two cubic segments), ink, width 4
  - two clay dots: (25,44) r4, (43,44) r4, fill #d95d39
  - sage stem: line (32,16)-(32,24), #79a99a, width 4, round cap

Drawn full-bleed on an opaque paper canvas, supersampled 4x, LANCZOS downscale.
Outputs into site/public/: favicon-16x16.png, favicon-32x32.png,
apple-touch-icon.png (180), icon-192.png, icon-512.png, favicon.ico (16/32/48),
site.webmanifest.
"""
import json
import struct
from PIL import Image, ImageDraw

OUT = "/home/hatch/workspace/quietbabygear/site/public"
PAPER = (251, 247, 239, 255)   # #fbf7ef
INK = (41, 55, 51, 255)        # #293733
CLAY = (217, 93, 57, 255)      # #d95d39
SAGE = (121, 169, 154, 255)    # #79a99a


def cubic(p0, p1, p2, p3, n=24):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def render_mark(size: int) -> Image.Image:
    ss = 4
    canvas = size * ss
    img = Image.new("RGBA", (canvas, canvas), PAPER)
    d = ImageDraw.Draw(img)
    u = canvas / 64.0  # one SVG unit in supersampled pixels
    w = 4 * u
    # rounded rect background
    d.rounded_rectangle([0, 0, canvas - 1, canvas - 1], radius=12 * u, fill=PAPER)
    # sage stem
    d.line([(32 * u, 16 * u), (32 * u, 24 * u)], fill=SAGE, width=int(round(w)))
    # curve (two cubic segments)
    seg1 = cubic((20, 38), (22, 29), (28, 24), (37, 24))
    seg2 = cubic((37, 24), (42, 24), (45, 26), (47, 29))
    pts = [(x * u, y * u) for x, y in seg1 + seg2[1:]]
    d.line(pts, fill=INK, width=int(round(w)), joint="curve")
    # baseline
    d.line([(14 * u, 42 * u), (50 * u, 42 * u)], fill=INK, width=int(round(w)))
    # clay dots
    for cx, cy in [(25, 44), (43, 44)]:
        r = 4 * u
        d.ellipse([cx * u - r, cy * u - r, cx * u + r, cy * u + r], fill=CLAY)
    return img.resize((size, size), Image.LANCZOS)


def write_ico(pngs: dict, path: str) -> None:
    entries = sorted(pngs.items())
    count = len(entries)
    header = struct.pack("<HHH", 0, 1, count)
    offset = 6 + 16 * count
    directory = b""
    data = b""
    for size, blob in entries:
        directory += struct.pack(
            "<BBBBHHII", size if size < 256 else 0, size if size < 256 else 0,
            0, 0, 1, 32, len(blob), offset + len(data))
        data += blob
    with open(path, "wb") as f:
        f.write(header + directory + data)


def save_png(img: Image.Image, path: str) -> bytes:
    import io
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    blob = buf.getvalue()
    with open(path, "wb") as f:
        f.write(blob)
    return blob


def main() -> None:
    pngs = {}
    for size, name in [(16, "favicon-16x16.png"), (32, "favicon-32x32.png"),
                       (48, "favicon-48x48.png"), (180, "apple-touch-icon.png"),
                       (192, "icon-192.png"), (512, "icon-512.png")]:
        img = render_mark(size)
        blob = save_png(img, f"{OUT}/{name}")
        if size in (16, 32, 48):
            pngs[size] = blob
        print(f"wrote {name} {size}x{size}")
    write_ico(pngs, f"{OUT}/favicon.ico")
    print("wrote favicon.ico (16/32/48)")
    manifest = {
        "name": "QuietBabyGear",
        "short_name": "QuietBabyGear",
        "description": "Baby gear tested for the hour nobody designs for.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#fbf7ef",
        "theme_color": "#26332f",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    with open(f"{OUT}/site.webmanifest", "w") as f:
        json.dump(manifest, f, indent=2)
    print("wrote site.webmanifest")


if __name__ == "__main__":
    main()
