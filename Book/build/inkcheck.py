#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""inkcheck.py — does any lettering actually land on top of a drawing?

`qc.py` answers that question from svgkit's *recorded* boxes, and its text box
is `size*0.80` above the baseline by `size*0.26` below.  Latin type fits that;
Bangla does not — the matra, the ref and the য-ফলা all sit outside it — so a
label can be measured clean and still print on top of a wire.  `poly()` records
no geometry at all, and text inside any rect is exempt by construction, which
hides a third class.

This tool does not measure boxes.  It renders each diagram twice — once with
the lettering removed, once with only the lettering — and intersects the two
ink masks.  What it reports is literally the pixels where a letter and a
drawing are printed on the same spot.

Both masks use a darkness threshold, which is what keeps the obvious
non-defects out:

  * dark text on a pale label box — the box is nowhere near the threshold, so
    it never enters the graphics mask;
  * white text on a navy chip — the lettering is lighter than the threshold,
    so it never enters the text mask.

So a hit means dark lettering printed over dark drawing ink, which is the
defect the reader complains about.

    python inkcheck.py diagrams/ch08/*.svg
"""
import glob
import os
import re
import subprocess
import sys

from PIL import Image, ImageChops

import render as R

SCRATCH = os.environ.get(
    "INK_TMP",
    "/private/tmp/claude-501/-Users-saron-Downloads-General-Electrician/"
    "c4289576-3d41-4401-90cd-2c67ed2457fe/scratchpad/ink")
DARK = 150          # 0-255 luminance; below this counts as ink
MIN_PX = 26         # ignore a few stray antialiased pixels
SCALE = 2           # 2x is plenty to see a collision and renders quickly

TEXT_RE = re.compile(r"<text\b.*?</text>", re.S)


def _variants(svg_path, tmp):
    body = open(svg_path, encoding="utf-8").read()
    base = os.path.splitext(os.path.basename(svg_path))[0]
    # graphics only — every <text> element taken out
    g = os.path.join(tmp, base + ".g.svg")
    open(g, "w", encoding="utf-8").write(TEXT_RE.sub("", body))
    # text only — keep the <text> elements and the white page under them
    head = body[:body.index(">") + 1]
    tail = "</svg>"
    keep = "".join(TEXT_RE.findall(body))
    w, h = R.svg_size(svg_path)
    t = os.path.join(tmp, base + ".t.svg")
    open(t, "w", encoding="utf-8").write(
        f'{head}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{keep}{tail}')
    return g, t


def _mask(png):
    """Ink mask: 255 where the pixel is darker than DARK, else 0."""
    im = Image.open(png).convert("L")
    return im.point(lambda v: 255 if v < DARK else 0)


CELL = 8            # coarse grid used to group hits into blobs


def _blobs(both, w, h):
    """Group hit pixels into blobs on a coarse grid.

    Clustering raw pixels is quadratic enough to hang on a diagram with a
    photograph under the lettering (ch14 d03 stalled the first version for
    over ten minutes).  Reducing to CELL-sized cells first leaves a few
    hundred points to flood-fill, which is instant, and a collision is never
    so small that an 8 px cell misses it.
    """
    small = both.reduce(CELL)
    sw, sh = small.size
    px = small.load()
    live = {(x, y) for y in range(sh) for x in range(sw) if px[x, y]}
    out = []
    while live:
        stack = [live.pop()]
        cells = []
        while stack:
            c = stack.pop()
            cells.append(c)
            cx, cy = c
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    q = (cx + dx, cy + dy)
                    if q in live:
                        live.discard(q)
                        stack.append(q)
        xs = [c[0] for c in cells]
        ys = [c[1] for c in cells]
        box = (min(xs) * CELL, min(ys) * CELL,
               min((max(xs) + 1) * CELL, w), min((max(ys) + 1) * CELL, h))
        n = both.crop(box).histogram()[255]
        if n >= MIN_PX:
            out.append(dict(n=n, x=box[0] // SCALE, y=box[1] // SCALE,
                            x1=box[2] // SCALE, y1=box[3] // SCALE))
    out.sort(key=lambda d: -d["n"])
    return out


def check(svg_path, tmp):
    g, t = _variants(svg_path, tmp)
    gp = R.render(g, os.path.join(tmp, "g.png"), scale=SCALE)
    tp = R.render(t, os.path.join(tmp, "t.png"), scale=SCALE)
    if not gp or not tp:
        return None
    gm, tm = _mask(gp), _mask(tp)
    if gm.size != tm.size:
        return None
    w, h = gm.size
    both = ImageChops.multiply(gm, tm)      # ink in BOTH layers
    # getbbox/histogram are C-level; iterating getdata() in Python cost
    # minutes per diagram on the big canvases.
    if not both.getbbox() or both.histogram()[255] < MIN_PX:
        return []
    return _blobs(both, w, h)


def main(args):
    files = []
    for a in args:
        files.extend(sorted(glob.glob(a)) if any(c in a for c in "*?[") else [a])
    os.makedirs(SCRATCH, exist_ok=True)
    total = 0
    for f in files:
        r = check(f, SCRATCH)
        if r is None:
            print(f"  ?  {f}  (render failed)")
            continue
        if not r:
            continue
        name = os.path.relpath(f)
        print(f"  ✗ {name}", flush=True)
        for d in r[:8]:
            print(f"       {d['n']:6d} px  at ({d['x']},{d['y']})-"
                  f"({d['x1']},{d['y1']})")
        total += len(r)
    print(f"\ncollisions: {total}")
    return total


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
