# -*- coding: utf-8 -*-
"""qc2.py — the overlaps qc.py is structurally blind to.

qc.py compares *text runs* against the shapes svgkit happens to record, and
it exempts any text that sits wholly inside a rect.  Three whole classes of
defect fall through that net, and they are the ones a reader actually sees:

  A. box-over-drawing — a label box (chip / box_auto / callout / note strip)
     drawn on top of wiring or a device body.  qc.py never compares a box
     against anything, only text.
  B. text-over-poly   — `poly()` records no geometry at all, so an arrowhead,
     a motor body or a tank drawn with poly() is invisible to the gate.
  C. box-over-box     — two filled boxes partly covering each other.

This module monkey-patches svgkit's primitives to keep fill-aware geometry
with draw order, so "who is on top of whom" is answerable.  It changes
nothing in svgkit.py itself — that engine is shared with ../HW All.
"""
import importlib
import sys

import svgkit as K

NONE = ("none", "None", "", None)


# ── geometry ───────────────────────────────────────────────────────────
def _seg_in_box(x1, y1, x2, y2, b):
    """Length of segment (x1,y1)-(x2,y2) lying inside box b — Liang-Barsky."""
    bx0, by0, bx1, by1 = b
    dx, dy = x2 - x1, y2 - y1
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x1 - bx0), (dx, bx1 - x1), (-dy, y1 - by0), (dy, by1 - y1)):
        if p == 0:
            if q < 0:
                return 0.0
            continue
        t = q / p
        if p < 0:
            if t > t1:
                return 0.0
            t0 = max(t0, t)
        else:
            if t < t0:
                return 0.0
            t1 = min(t1, t)
    if t0 > t1:
        return 0.0
    return ((t1 - t0) ** 2 * (dx * dx + dy * dy)) ** 0.5


def _pt_in_poly(px, py, pts):
    inside = False
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            xi = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < xi:
                inside = not inside
    return inside


def _poly_box(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def _overlap(a, b):
    return (min(a[2], b[2]) - max(a[0], b[0]), min(a[3], b[3]) - max(a[1], b[1]))


def _nested(a, b):
    return (a[0] >= b[0] - .6 and a[1] >= b[1] - .6
            and a[2] <= b[2] + .6 and a[3] <= b[3] + .6)


# ── recording ──────────────────────────────────────────────────────────
_ORIG = {}


def install():
    S = K.SVG
    for n in ("rect", "line", "path", "circle", "poly", "image", "text"):
        _ORIG[n] = getattr(S, n)

    def g(self):
        if not hasattr(self, "g2"):
            self.g2 = []
        return self.g2

    def rect(self, x, y, w, h, fill="none", stroke="none", sw=1.5, rx=8,
             dash=None, opacity=None):
        g(self).append(dict(k="rect", b=(x, y, x + w, y + h), fill=fill,
                            op=opacity, i=len(self.g2), txt=[]))
        return _ORIG["rect"](self, x, y, w, h, fill, stroke, sw, rx, dash, opacity)

    def line(self, x1, y1, x2, y2, stroke=K.NAVY, sw=2, dash=None,
             cap="round", marker=None):
        g(self).append(dict(k="seg", p=[(x1, y1), (x2, y2)], i=len(self.g2)))
        return _ORIG["line"](self, x1, y1, x2, y2, stroke, sw, dash, cap, marker)

    def path(self, d, stroke=K.NAVY, sw=2, fill="none", dash=None, marker=None,
             cap="round", join="round", opacity=None):
        pts = K._path_points(d)
        if pts:
            g(self).append(dict(k="seg", p=pts, i=len(self.g2)))
        return _ORIG["path"](self, d, stroke, sw, fill, dash, marker, cap, join,
                             opacity)

    def circle(self, cx, cy, r, fill="none", stroke="none", sw=2, opacity=None):
        g(self).append(dict(k="circle", c=(cx, cy, r),
                            b=(cx - r, cy - r, cx + r, cy + r), fill=fill,
                            i=len(self.g2)))
        return _ORIG["circle"](self, cx, cy, r, fill, stroke, sw, opacity)

    def poly(self, pts, fill="none", stroke="none", sw=2):
        g(self).append(dict(k="poly", p=list(pts), b=_poly_box(pts), fill=fill,
                            i=len(self.g2)))
        return _ORIG["poly"](self, pts, fill, stroke, sw)

    def image(self, x, y, w, h, path, rx=0):
        g(self).append(dict(k="image", b=(x, y, x + w, y + h), fill="#img",
                            i=len(self.g2), txt=[]))
        return _ORIG["image"](self, x, y, w, h, path, rx)

    def text(self, x, y, s, size=16, fill=K.INK, weight=400, anchor="start",
             family=K.FAMILY, opacity=None, ls=None):
        if s.strip():
            w = K.tw(s, size, weight, family)
            x0 = x if anchor == "start" else (
                x - w / 2 if anchor == "middle" else x - w)
            g(self).append(dict(k="text", b=(x0, y - size * .80, x0 + w,
                                             y + size * .26), s=s,
                                i=len(self.g2)))
        return _ORIG["text"](self, x, y, s, size, fill, weight, anchor, family,
                             opacity, ls)

    S.rect, S.line, S.path, S.circle = rect, line, path, circle
    S.poly, S.image, S.text = poly, image, text


def uninstall():
    for n, f in _ORIG.items():
        setattr(K.SVG, n, f)


# ── the three checks ───────────────────────────────────────────────────
def analyse(svg):
    G = getattr(svg, "g2", [])
    texts = [e for e in G if e["k"] == "text"]
    filled = [e for e in G
              if e["k"] in ("rect", "image") and e.get("fill") not in NONE
              and not e.get("op")]
    polys = [e for e in G if e["k"] == "poly" and e.get("fill") not in NONE]

    # which filled boxes carry text (a label box, as opposed to a device body)
    for bx in filled:
        bx["txt"] = [t["s"] for t in texts
                     if t["i"] > bx["i"] and _nested(t["b"], bx["b"])]

    hits = []

    # A. a text-bearing box drawn over earlier wiring / device geometry
    for bx in filled:
        if not bx["txt"]:
            continue
        lab = bx["txt"][0][:34]
        inner = (bx["b"][0] + 3, bx["b"][1] + 3, bx["b"][2] - 3, bx["b"][3] - 3)
        for e in G:
            if e["i"] >= bx["i"]:
                continue
            if e["k"] == "seg":
                run = 0.0
                for a, b in zip(e["p"], e["p"][1:]):
                    run = max(run, _seg_in_box(a[0], a[1], b[0], b[1], inner))
                # a wire that merely lands on the box edge is fine; a wire
                # that runs across its face is covered up
                if run > max(16.0, .34 * (inner[2] - inner[0])):
                    hits.append(("A box covers wire", lab, round(run)))
                    break
            elif e["k"] == "poly" and e.get("fill") not in NONE:
                ox, oy = _overlap(inner, e["b"])
                if ox > 6 and oy > 6 and not _nested(inner, e["b"]):
                    hits.append(("A box covers shape", lab, round(min(ox, oy))))
                    break

    # B. text sitting on a filled polygon (poly() is invisible to qc.py)
    for t in texts:
        tb = t["b"]
        cx, cy = (tb[0] + tb[2]) / 2, (tb[1] + tb[3]) / 2
        own = any(_nested(tb, b["b"]) and b["i"] < t["i"] and b["i"] > 0
                  for b in filled)
        for p in polys:
            if p["i"] > t["i"]:
                continue
            ox, oy = _overlap(tb, p["b"])
            if ox <= 2 or oy <= 2:
                continue
            corners = [(tb[0], tb[1]), (tb[2], tb[1]), (tb[0], tb[3]),
                       (tb[2], tb[3]), (cx, cy)]
            n_in = sum(_pt_in_poly(x, y, p["p"]) for x, y in corners)
            if n_in and not (own and n_in == 5):
                hits.append(("B text on poly", t["s"][:34], n_in))
                break

    # C. two filled boxes partly covering each other
    for i, a in enumerate(filled):
        for b in filled[i + 1:]:
            if not (a["txt"] or b["txt"]):
                continue
            ox, oy = _overlap(a["b"], b["b"])
            if ox > 5 and oy > 5 and not _nested(a["b"], b["b"]) \
                    and not _nested(b["b"], a["b"]):
                la = (a["txt"] or ["·"])[0][:22]
                lb = (b["txt"] or ["·"])[0][:22]
                hits.append(("C box × box", f"{la} × {lb}", round(min(ox, oy))))
    return hits


def run(mods):
    total = 0
    install()
    try:
        for name in mods:
            mod = importlib.import_module(name)
            K.COLLECT = True
            for f in mod.ALL:
                try:
                    f()
                except Exception:
                    pass
            K.COLLECT = False
            K.flush()
            print(f"\n── {name} ──")
            for f in mod.ALL:
                saved = {}

                def cap(self, path, _o=K.SVG.save, _s=saved):
                    _s["svg"] = self
                    return _o(self, path)
                K.SVG.save, old = cap, K.SVG.save
                try:
                    f()
                finally:
                    K.SVG.save = old
                svg = saved.get("svg")
                if svg is None:
                    continue
                h = analyse(svg)
                if h:
                    print(f"  ✗ {f.__name__:22s} {len(h)}")
                    for kind, lab, n in h[:10]:
                        print(f"       {kind:22s} '{lab}'  ({n})")
                total += len(h)
    finally:
        uninstall()
    print(f"\ntotal: {total}")
    return total


if __name__ == "__main__":
    sys.exit(1 if run(sys.argv[1:]) else 0)
