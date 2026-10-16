# -*- coding: utf-8 -*-
"""অধ্যায় ১০ — টাইমার : ডায়াগ্রাম।

সহায়কগুলো অধ্যায় ৮ ও ৯ থেকে আমদানি করা (CLAUDE.md-র নিয়ম)।
`photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই এখানে
`_use_ch10_images()` দিয়ে বদলে নেওয়া হয়েছে।

**বিলম্বিত কন্টাক্টের প্রতীক (IEC 60617)** — কন্টাক্টের ব্লেড থেকে
একটি জোড়া রেখা বেরিয়ে "প্যারাশুট" অর্ধবৃত্তে শেষ হয়।  খাড়া করে আঁকা
প্রতীকে অন-ডিলের অর্ধবৃত্ত ব্লেডের দিকে **মুখ খোলা** (∈ আকার), আর
অফ-ডিলের অর্ধবৃত্ত ব্লেডের দিকে **পিঠ ফেরানো** (⊃ আকার)।  অনুভূমিক
ল্যাডারে ব্লেড নিচে, তাই অন-ডিলে ∩ আর অফ-ডিলে ∪।  কয়েলের পাশে
ক্রস-দেওয়া ছোট বাক্স = অন-ডিলে (slow-operating), ভরাট কালো বাক্স =
অফ-ডিলে (slow-releasing)।  qelectrotech-এর IEC 60617 প্রতীক-তালিকা
থেকে মেলানো;  সেই তালিকার একটি সারির নাম ভুল ছাপা ("Make contact,
delayed opening" লেখা, আঁকা আসলে NC) — আঁকাটাই অনুসরণ করা হয়েছে,
কারণ বাকি চার সারির নিয়মের সঙ্গে সেটিই মেলে।

**AH3-এর পিন বিন্যাস** — ANLY AH3-R ও Alion AH3-এর ডেটাশিটের
টাইমিং চার্টে লেখা:  SOURCE (2-7), N.C. (8-5), N.O. (8-6),
N.C. (1-4), N.O. (1-3)।  Mode A-তে দুই সেটই বিলম্বিত, Mode B-তে
1-4/1-3 তাৎক্ষণিক।

**d11-এর টপোলজি** — KT1-এর 8-5 (বিলম্বিত NC) STOP-এর পরে, START ও
হোল্ডিং-এর প্যারালাল জোড়ের **আগে** সিরিজে।  KT1-এর কয়েল KM1-এর
কয়েলের **প্যারালালে**, একই নোড C থেকে।  ফলে 8-5 খুললে দুটি কয়েলই
ছাড়ে, ল্যাচ ভাঙে, আর টাইমার নিজে থেকেই শূন্যে ফেরে।  d12-এর টাইমিং
চার্ট আর d13-এর তার — তিনটিই এই একই তারের ক্রম।

**d13-এ ক্রসিং নেই** — বাটন, টাইমারের সকেট আর ফিউজ বাঁ পাশে এক খাড়া
সারিতে;  তারের ক্রমেই উপর থেকে নিচে সাজানো।  KT1-এর 2 নম্বর তার
সবার উপর দিয়ে A1-এ, 7 নম্বর বাঁ দিকে N-এ।  qc ক্রসিং ধরে না — কোনো
তার সরালে চোখে দেখে নিতে হবে।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, chip, callout, coil_sym,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, LIVE, NEUT, DEAD, PLATE, CU)
from dia_ch09 import (fuse, thermal_sym, lamp, _pb, _nc, _no,
                      nc_tip, no_tip)
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch10")
IMG = os.path.join(HERE, "assets", "ch10")

TIMEC = "#6A4FB3"          # টাইমারের রং
TIMEBG = "#EFEAF9"


def _use_ch10_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch10_images()
    return C8.photo_callouts(*a, **k)


# ── প্রতীক ──────────────────────────────────────────────────────────────
def chute_up(s, mx, my, top, kind, col=SYM):
    """অনুভূমিক ল্যাডারের বিলম্বিত কন্টাক্ট — ব্লেডের মাঝ (mx, my) থেকে
    জোড়া রেখা উপরে `top` পর্যন্ত, মাথায় অর্ধবৃত্ত।
    kind "on" → ∩ (মুখ ব্লেডের দিকে),  "off" → ∪ (পিঠ ব্লেডের দিকে)।"""
    r = 13
    s.path(f"M {mx - 3} {my} L {mx - 3} {top}", col, 2)
    s.path(f"M {mx + 3} {my} L {mx + 3} {top}", col, 2)
    if kind == "on":
        # কেন্দ্র (mx, top + r) — উপরের অর্ধেক;  রেখা কেন্দ্রের ভেতর দিয়ে
        s.path(f"M {mx - r} {top + r} A {r} {r} 0 0 1 {mx + r} {top + r}",
               col, 2.4)
        s.path(f"M {mx - 3} {top} L {mx - 3} {top + r}", col, 2)
        s.path(f"M {mx + 3} {top} L {mx + 3} {top + r}", col, 2)
    else:
        # কেন্দ্র (mx, top - r) — নিচের অর্ধেক, সবচেয়ে নিচের বিন্দুতে রেখা
        s.path(f"M {mx - r} {top - r} A {r} {r} 0 0 0 {mx + r} {top - r}",
               col, 2.4)


def dnc(s, x, LY, col, kind="on", opened=False):
    """বিলম্বিত NC (৯২ px চওড়া)।  ব্লেডের মাঝ থেকে প্যারাশুট।"""
    _nc(s, x, LY, col, opened=opened)
    mx = x + (38 if opened else 40)
    my = nc_tip(x, LY, mx, opened=opened)
    chute_up(s, mx, my, LY - 60, kind, SYM)


def dno(s, x, LY, col, kind="on", closed=False, w=92):
    _no(s, x, LY, col, closed=closed, w=w)
    if closed:
        mx, my = x + w / 2, LY
    else:
        mx, my = x + (w - 14) / 2, LY - 22
    chute_up(s, mx, my, LY - 60, kind, SYM)


def timer_coil(s, x, y, w, h, tag, kind="on"):
    """কয়েল + বাঁয়ে ছোট বাক্স:  on → ক্রস,  off → ভরাট।"""
    b = h * 0.62
    by = y + (h - b) / 2
    if kind == "on":
        s.rect(x, by, b, b, "#FFFFFF", SYM, 2.6, 0)
        s.path(f"M {x} {by} L {x + b} {by + b}", SYM, 2.2)
        s.path(f"M {x} {by + b} L {x + b} {by}", SYM, 2.2)
    else:
        s.rect(x, by, b, b, SYM, SYM, 2.6, 0)
    coil_sym(s, x + b, y, w - b, h, None)
    s.text(x + b + (w - b) / 2, y + h / 2 + T_BODY * 0.34, tag, T_BODY,
           NAVY, 700, "middle")


def vcontact(s, x, ytop, ybot, nc=False, delay=None, col=SYM):
    """খাড়া কন্টাক্ট (IEC ছক যেমন আঁকে)।  delay = None / "on" / "off"।"""
    ym = (ytop + ybot) / 2
    ya, yp = ym - 34, ym + 34
    s.path(f"M {x} {ytop} L {x} {ya}", col, 3)
    s.path(f"M {x} {yp} L {x} {ybot}", col, 3)
    if nc:
        s.path(f"M {x} {ya} L {x + 30} {ya}", col, 3)
        ex, ey = x + 34, ya - 6
    else:
        ex, ey = x - 30, ya - 4
    s.path(f"M {x} {yp} L {ex} {ey}", col, 3.2)
    if not delay:
        return
    mx, my = (x + ex) / 2, (yp + ey) / 2
    ax, r = mx - 58, 14
    s.path(f"M {mx} {my - 3} L {ax} {my - 3}", col, 2)
    s.path(f"M {mx} {my + 3} L {ax} {my + 3}", col, 2)
    if delay == "on":             # ∈ — বাঁয়ে বেঁকে, মুখ ব্লেডের দিকে
        cx = ax + r
        s.path(f"M {cx} {my - r} A {r} {r} 0 0 0 {cx} {my + r}", col, 2.4)
    else:                         # ⊃ — পিঠ ব্লেডের দিকে
        cx = ax - r
        s.path(f"M {cx} {my - r} A {r} {r} 0 0 1 {cx} {my + r}", col, 2.4)


# ── টাইমিং চার্ট ────────────────────────────────────────────────────────
def timing(s, X0, Y0, XW, rows, tmax, RH=78, label_w=None):
    """rows = [(নাম, [(শুরু, শেষ), …], রং)] — প্রতিটি সারি উঁচু/নিচু রেখা।
    ফেরত দেয় সময় → x রূপান্তর আর প্রতিটি সারির নিচু রেখার y।"""
    px = lambda t: X0 + t / tmax * XW
    lows = []
    for i, (name, pulses, col) in enumerate(rows):
        lo = Y0 + i * RH + 44
        hi = lo - 34
        lows.append(lo)
        s.text(X0 - 20, lo - 8, name, T_SMALL, NAVY, 700, "end")
        s.line(X0, lo + 12, X0 + XW, lo + 12, "#E3E9EF", 1.2)
        # চার্টের কিনারায় কোনো ধার আঁকা হয় না — শুরুতে উঁচু থাকলে উঁচু
        # থেকেই শুরু, শেষে উঁচু থাকলে উঁচুতেই শেষ
        d = f"M {X0} {hi if pulses and pulses[0][0] <= 0 else lo}"
        end_hi = False
        for a, b in pulses:
            if a > 0:
                d += f" L {px(a)} {lo} L {px(a)} {hi}"
            if b >= tmax:
                d += f" L {X0 + XW} {hi}"
                end_hi = True
            else:
                d += f" L {px(b)} {hi} L {px(b)} {lo}"
        if not end_hi:
            d += f" L {X0 + XW} {lo}"
        s.path(d, col, 3.6)
    return px, lows


HEAD = 12                 # মাপ-তিরের মাথার দৈর্ঘ্য


def dim_arrow(s, x1, x2, y, text, col=RED, below=False):
    """মাপ-তির — চওড়া ফাঁকে তির ভেতরমুখো, সরু ফাঁকে বাইরে থেকে ভেতরমুখো।

    ফাঁকটি দুই মাথার চেয়ে সরু হলে তির দুটি একটার উপর আরেকটা পড়ে একটা
    দলা হয়ে যায় — ১৪ অধ্যায়ের `t2 = 50 ms` ঠিক তা-ই হয়েছিল, পড়াই যেত
    না।  সরু ফাঁকে তাই আঁকার চলতি রীতি মানা হয়:  ফাঁকের দুই সীমায় খাড়া
    দাগ, আর তির দুটি বাইরে থেকে ভেতরের দিকে তাক করা।
    """
    span = abs(x2 - x1)
    if span >= 3 * HEAD:
        s.path(f"M {x1} {y} L {x2} {y}", col, 2.2)
        pairs = ((x1, 1), (x2, -1))
    else:
        lo, hi = min(x1, x2), max(x1, x2)
        s.path(f"M {lo - 30} {y} L {hi + 30} {y}", col, 2.2)
        for xx in (lo, hi):
            s.path(f"M {xx} {y - 9} L {xx} {y + 9}", col, 2.2)
        pairs = ((lo, -1), (hi, 1))
    for xx, sgn in pairs:
        s.path(f"M {xx + sgn * HEAD} {y - 7} L {xx} {y} L {xx + sgn * HEAD} {y + 7}",
               col, 2.2)
    s.text((x1 + x2) / 2, y + (28 if below else -10), text, T_SMALL, col, 700,
           "middle")


# ── ১. টাইমারের ধারণা ───────────────────────────────────────────────────
def d01_idea():
    s = SVG(1240, 680)
    s.title("টাইমারের কাজের ধাপ", T_TITLE)
    ar = s.arrow_defs(STEEL, "arI", 15)
    blocks = [("১. কয়েলে সরবরাহ", "A1-A2 বা 2-7", LIGHT, STEEL),
              ("২. সময় গোনা", "ডায়ালে বসানো t", TIMEBG, TIMEC),
              ("৩. কন্টাক্ট বদল", "NO বন্ধ · NC খোলা", AMBERBG, AMBER)]
    BW, BH, Y = 330, 128, 104
    xs = [46, 455, 864]
    for x, (a, b, bg, col) in zip(xs, blocks):
        s.rect(x, Y, BW, BH, bg, col, 2.8, 12)
        s.text(x + BW / 2, Y + 52, a, T_NAME, col, 700, "middle")
        s.text(x + BW / 2, Y + 96, b, T_BODY, NAVY, 700, "middle")
    for x in xs[:-1]:
        s.path(f"M {x + BW + 6} {Y + BH / 2} L {x + 404} {Y + BH / 2}",
               STEEL, 3.6, marker=ar)

    panel(s, 46, 270, 1148, 300, "অন-ডিলে টাইমারের এক চক্র")
    px, lows = timing(s, 330, 324, 820,
                      [("কয়েলে সরবরাহ", [(1, 9)], STEEL),
                       ("NO কন্টাক্ট", [(5, 9)], AMBER)], 10, RH=92)
    s.path(f"M {px(1)} {lows[0] - 40} L {px(1)} {lows[1] + 20}", GREY, 1.8,
           dash="6 5")
    s.path(f"M {px(5)} {lows[0] - 40} L {px(5)} {lows[1] + 20}", GREY, 1.8,
           dash="6 5")
    dim_arrow(s, px(1), px(5), lows[1] + 44, "বসানো সময় t", TIMEC, below=True)
    y = note_strip(s, 594, "কয়েল সঙ্গে সঙ্গে সরবরাহ পায়, কন্টাক্ট বদলায় "
                           "t সময় পরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. প্রকারভেদ ─────────────────────────────────────────────────────────
def d02_types():
    s = SVG(1240, 720)
    s.title("টাইমারের প্রকারভেদ", T_TITLE)
    cols = [("গঠন অনুযায়ী", STEEL,
             ["নিউমেটিক (বাতাসের)", "মোটরচালিত", "ইলেকট্রনিক অ্যানালগ",
              "ডিজিটাল"]),
            ("কাজ অনুযায়ী", TIMEC,
             ["অন-ডিলে", "অফ-ডিলে", "স্টার-ডেল্টা টাইমার",
              "সাইক্লিক (ফ্লিকার)", "মাল্টিফাংশন"]),
            ("ঘড়ি ধরে চলে", AMBER,
             ["দৈনিক টাইম সুইচ", "সাপ্তাহিক টাইম সুইচ"])]
    for i, (ttl, col, items) in enumerate(cols):
        x = 46 + i * 390
        panel(s, x, 92, 368, 520, ttl, col)
        for j, it in enumerate(items):
            cy = 180 + j * 84
            s.rect(x + 30, cy - 30, 308, 60, "#FFFFFF", col, 2.4, 12)
            s.text(x + 184, cy + 8, it, T_BODY, NAVY, 700, "middle")
    y = note_strip(s, 636, "টাইমার সংকেত আসার পর থেকে সময় গোনে; টাইম সুইচ "
                           "দিনের ঘড়ি ধরে চলে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_types.svg")


# ── ৩. AH3 — সামনের দিক ────────────────────────────────────────────────
def d03_ah3():
    # ভগ্নাংশগুলো assets_ch10.py-র ক্রপ-করা ph_ah3-এর হিসাবে
    return photo_callouts(
        "d03_ah3", "ANLY AH3-NC অ্যানালগ টাইমার",
        "ph_ah3.jpg",
        left=[("মোড সুইচ A / B", 0.148, 0.121),
              ("সেটিং নব ও কাঁটা", 0.470, 0.470),
              ("মডেল নম্বর", 0.211, 0.868)],
        right=[("UP ও ON বাতি", 0.781, 0.127),
               ("স্কেল 0 – 6", 0.758, 0.604),
               ("পরিসর বাছাইয়ের সুইচ", 0.727, 0.824),
               ("কয়েলের ভোল্টেজ", 0.484, 0.857)],
        note="স্কেলের সংখ্যা একই থাকে; সংখ্যাটি সেকেন্ড না মিনিট, তা "
             "পরিসর সুইচ ঠিক করে",
        iw=460)


# ── ৪. আট পিনের বিন্যাস ────────────────────────────────────────────────
PIN_ANG = {1: 247.5, 2: 202.5, 3: 157.5, 4: 112.5,
           5: 67.5, 6: 22.5, 7: -22.5, 8: -67.5}


def d04_pins():
    s = SVG(1240, 900)
    s.title("৮-পিন টাইমারের পিন বিন্যাস (AH3)", T_TITLE)

    panel(s, 46, 92, 560, 470, "ডেটাশিটের নকশা")
    cx, cy, R = 326, 330, 132
    s.circle(cx, cy, R + 52, "#F4F7FA", STEEL, 2.4)
    s.circle(cx, cy, 44, "#DCE3EA", STEEL, 2.2)
    s.rect(cx - 16, cy + R + 36, 32, 22, "#FFFFFF", STEEL, 2.2, 3)
    s.text(cx, cy + R + 90, "চাবির খাঁজ", T_SMALL, GREY, 700, "middle")
    colmap = {2: (LIVE, REDBG), 7: (LIVE, REDBG),
              8: (AMBER, AMBERBG), 5: (AMBER, AMBERBG), 6: (AMBER, AMBERBG),
              1: (GREEN, GREENBG), 4: (GREEN, GREENBG), 3: (GREEN, GREENBG)}
    for p, a in PIN_ANG.items():
        t = math.radians(a)
        x, y = cx + R * math.cos(t), cy - R * math.sin(t)
        col, bg = colmap[p]
        s.circle(x, y, 27, bg, col, 3)
        s.text(x, y + 9, str(p), T_NODE, col, 700, "middle")

    panel(s, 636, 92, 558, 470, "একই টাইমারের পেছন")
    ih = 396
    iw = ih * 1000 / 1168              # ph_ah3_base-এর মাপ 1000 × 1168
    s.image(915 - iw / 2, 146, iw, ih, f"{IMG}/ph_ah3_base.jpg", 8)

    panel(s, 46, 590, 1148, 212, "কোন পিন কী")
    items = [("2 – 7", "সরবরাহ (কয়েল)", LIVE, REDBG),
             ("8", "প্রথম সেটের কমন", AMBER, AMBERBG),
             ("8 – 5 · 8 – 6", "বিলম্বিত NC · NO", AMBER, AMBERBG),
             ("1", "দ্বিতীয় সেটের কমন", GREEN, GREENBG),
             ("1 – 4 · 1 – 3", "NC · NO (মোড অনুযায়ী)", GREEN, GREENBG)]
    for i, (pins, what, col, bg) in enumerate(items):
        c, r = divmod(i, 3)
        x = 100 + c * 560
        y = 676 + r * 50
        w = tw(pins, T_BODY, 700) + 30
        s.rect(x, y - 24, w, 40, bg, col, 2.2, 9)
        s.text(x + w / 2, y + 4, pins, T_BODY, col, 700, "middle")
        s.text(x + w + 14, y + 4, what, T_SMALL, NAVY, 700, "start")
    y = note_strip(s, 826, "Mode A-তে দুই সেটই বিলম্বিত; Mode B-তে "
                           "1-4 ও 1-3 তাৎক্ষণিক")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_pins.svg")


# ── ৫. অন-ডিলে টাইমিং ───────────────────────────────────────────────────
def d05_ondelay():
    s = SVG(1240, 560)
    s.title("অন-ডিলে টাইমারের টাইমিং চার্ট", T_TITLE)
    px, lows = timing(s, 290, 100, 900,
                      [("সরবরাহ 2 – 7", [(1, 7), (9, 11)], STEEL),
                       ("NO 8 – 6", [(4, 7)], AMBER),
                       ("NC 8 – 5", [(0, 4), (7, 14)], TIMEC)], 14, RH=96)
    for t in (1, 4):
        s.path(f"M {px(t)} {lows[0] - 44} L {px(t)} {lows[2] + 16}", GREY,
               1.8, dash="6 5")
    dim_arrow(s, px(1), px(4), lows[2] + 48, "t", RED, below=True)
    dim_arrow(s, px(9), px(11), lows[2] + 48, "t-এর কম", RED, below=True)
    y = note_strip(s, lows[2] + 104, "t পূর্ণ হওয়ার আগে সরবরাহ গেলে কন্টাক্ট "
                                     "বদলায় না, গোনা শূন্যে ফেরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_ondelay.svg")


# ── ৬. অফ-ডিলে টাইমিং ───────────────────────────────────────────────────
def d06_offdelay():
    s = SVG(1240, 560)
    s.title("অফ-ডিলে টাইমারের টাইমিং চার্ট", T_TITLE)
    px, lows = timing(s, 290, 100, 900,
                      [("সরবরাহ A1 – A2", [(0.2, 14)], STEEL),
                       ("নিয়ন্ত্রণ সংকেত", [(2, 5), (9, 10)], GREEN),
                       ("NO 15 – 18", [(2, 8), (9, 13)], AMBER)], 14, RH=96)
    for t in (5, 8):
        s.path(f"M {px(t)} {lows[1] - 44} L {px(t)} {lows[2] + 16}", GREY,
               1.8, dash="6 5")
    dim_arrow(s, px(5), px(8), lows[2] + 48, "t", RED, below=True)
    dim_arrow(s, px(10), px(13), lows[2] + 48, "t", RED, below=True)
    y = note_strip(s, lows[2] + 104, "সংকেত এলে কন্টাক্ট সঙ্গে সঙ্গে বদলায়; "
                                     "সংকেত যাওয়ার t পরে ফেরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_offdelay.svg")


# ── ৭. প্রতীক ও নম্বর ────────────────────────────────────────────────────
def d07_symbols():
    s = SVG(1240, 900)
    s.title("টাইমারের প্রতীক ও টার্মিনাল নম্বর (IEC)", T_TITLE)

    panel(s, 46, 92, 1148, 250, "কয়েল")
    for i, (kind, name) in enumerate(((None, "সাধারণ কয়েল"),
                                      ("on", "অন-ডিলে কয়েল"),
                                      ("off", "অফ-ডিলে কয়েল"))):
        cx = 240 + i * 380
        s.path(f"M {cx} 150 L {cx} 190", SYM, 3)
        s.path(f"M {cx} 246 L {cx} 280", SYM, 3)
        if kind:
            timer_coil(s, cx - 76, 190, 152, 56, "KT1", kind)
        else:
            coil_sym(s, cx - 58, 190, 116, 56, "KM1")
        s.text(cx, 318, name, T_BODY, NAVY, 700, "middle")

    panel(s, 46, 366, 1148, 300, "বিলম্বিত কন্টাক্ট")
    for i, (nc, dl, l1, l2) in enumerate((
            (False, "on", "অন-ডিলে NO", "দেরিতে বন্ধ হয়"),
            (True, "on", "অন-ডিলে NC", "দেরিতে খোলে"),
            (False, "off", "অফ-ডিলে NO", "দেরিতে খোলে"),
            (True, "off", "অফ-ডিলে NC", "দেরিতে বন্ধ হয়"))):
        x = 210 + i * 272
        vcontact(s, x, 420, 580, nc, dl)
        s.text(x - 20, 616, l1, T_BODY, NAVY, 700, "middle")
        s.text(x - 20, 648, l2, T_SMALL, GREY, 700, "middle")

    panel(s, 46, 690, 1148, 120, "টার্মিনাল নম্বর")
    for i, (pair, what, col, bg) in enumerate((
            ("15 · 16 · 18", "চেঞ্জওভার, 15 কমন", TIMEC, TIMEBG),
            ("55 – 56", "বিলম্বিত NC", RED, REDBG),
            ("67 – 68", "বিলম্বিত NO", AMBER, AMBERBG))):
        cx = 230 + i * 390
        w = tw(pair, T_BODY, 700) + 36
        s.rect(cx - w / 2, 738, w, 40, bg, col, 2.2, 9)
        s.text(cx + 0, 766, pair, T_BODY, col, 700, "middle")
        s.text(cx + w / 2 + 12, 766, what, T_SMALL, NAVY, 700, "start")
    y = note_strip(s, 834, "দ্বিতীয় অঙ্ক 5-6 বা 7-8 হলে বিশেষ কন্টাক্ট; "
                           "এখানে বিলম্বিত কন্টাক্ট")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_symbols.svg")


# ── ৮. ডায়াল সেটিং ─────────────────────────────────────────────────────
def d08_dial():
    s = SVG(1240, 660)
    s.title("45 সেকেন্ড বসানোর জন্য পরিসর ও ডায়াল", T_TITLE)

    panel(s, 46, 92, 460, 470, "ডায়াল (স্কেল 0 – 6)")
    cx, cy, R = 276, 350, 132
    s.circle(cx, cy, R + 26, "#EEF3F8", STEEL, 2.4)
    s.circle(cx, cy, R - 34, "#20344A", "#12324D", 3)
    a0, a1 = 225, -45
    ang = lambda v: math.radians(a0 + (a1 - a0) * v / 6.0)
    for k in range(31):
        a = ang(k * 0.2)
        r0 = R - 20 if k % 5 == 0 else R - 6
        s.line(cx + r0 * math.cos(a), cy - r0 * math.sin(a),
               cx + (R + 6) * math.cos(a), cy - (R + 6) * math.sin(a),
               NAVY, 2.6 if k % 5 == 0 else 1.5)
    for v in range(7):
        a = ang(v)
        rr = R + 48
        s.text(cx + rr * math.cos(a), cy - rr * math.sin(a) + 8,
               f"{v}", T_SMALL, NAVY, 700, "middle")
    a = ang(4.5)
    s.path(f"M {cx} {cy} L {cx + (R - 30) * math.cos(a)} "
           f"{cy - (R - 30) * math.sin(a)}", "#E8452C", 8)
    s.circle(cx, cy, 16, "#C9A24A", "#8C6D25", 2)
    s.text(cx, cy + 196, "কাঁটা 4.5-এ", T_BODY, NAVY, 700, "middle")

    panel(s, 536, 92, 658, 470, "পরিসর সুইচ ও স্কেলের মান")
    rows = [("6S", "0 – 6 সেকেন্ড", "স্কেল × 1 s", False),
            ("60S", "0 – 60 সেকেন্ড", "স্কেল × 10 s", True),
            ("6M", "0 – 6 মিনিট", "স্কেল × 1 min", False),
            ("60M", "0 – 60 মিনিট", "স্কেল × 10 min", False)]
    for i, (code, rng, mul, sel) in enumerate(rows):
        y = 170 + i * 74
        bg, col = (TIMEBG, TIMEC) if sel else ("#FFFFFF", STEEL)
        s.rect(572, y - 30, 586, 58, bg, col, 2.6 if sel else 1.8, 10)
        s.text(620, y + 8, code, T_NAME, col, 700, "middle")
        s.text(690, y + 8, rng, T_BODY, NAVY, 700, "start")
        s.text(1130, y + 8, mul, T_BODY, col, 700, "end")
    s.text(865, 500, "4.5 × 10 s = 45 s", T_NAME, TIMEC, 700, "middle")
    y = note_strip(s, 586, "আগে পরিসর বাছুন, তারপর ডায়াল ঘোরান; পরিসর ভুল "
                           "হলে সময় দশ গুণ বা তারও বেশি ভুল হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_dial.svg")


# ── ৯. টাইমার লজিকে দুই বাতি ────────────────────────────────────────────
def d09_lamps():
    s = SVG(1240, 620)
    s.title("টাইমার লজিকে দুটি বাতির নিয়ন্ত্রণ", T_TITLE)
    LY, R2, R3, NY, RX, T = 170, 300, 424, 510, 1130, 236
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", SYM, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 300 {LY}", SYM, SW)
    node(s, T, LY)
    # S1 — সিলেক্টর সুইচ
    _no(s, 300, LY, SYM)
    s.text(346, LY - 58, "S1", T_SMALL, NAVY, 700, "middle")
    s.path(f"M 392 {LY} L 830 {LY}", SYM, SW)
    timer_coil(s, 830, LY - 34, 170, 68, "KT1", "on")
    s.text(824, LY - 42, "2", T_TINY, NAVY, 700, "end")
    s.text(1006, LY - 42, "7", T_TINY, NAVY, 700, "start")
    s.path(f"M 1000 {LY} L {RX} {LY} L {RX} {NY}", SYM, SW)

    # 8 কমন — দুই শাখাই এক পিন থেকে
    s.path(f"M {T} {LY} L {T} {R3}", SYM, SW)
    s.path(f"M {T} {R2} L 440 {R2}", SYM, SW)
    node(s, T, R2)
    dno(s, 440, R2, SYM, "on")
    s.text(450, R2 + 34, "8", T_TINY, NAVY, 700, "middle")
    s.text(524, R2 + 34, "6", T_TINY, NAVY, 700, "middle")
    s.text(500, R2 - 70, "KT1", T_SMALL, TIMEC, 700, "start")
    s.path(f"M 532 {R2} L 916 {R2}", SYM, SW)
    lamp(s, 940, R2, 24)
    s.text(940, R2 - 38, "H1", T_SMALL, NAVY, 700, "middle")
    s.path(f"M 964 {R2} L {RX} {R2}", SYM, SW)
    node(s, RX, R2)

    s.path(f"M {T} {R3} L 440 {R3}", SYM, SW)
    dnc(s, 440, R3, SYM, "on")
    s.text(450, R3 + 34, "8", T_TINY, NAVY, 700, "middle")
    s.text(524, R3 + 34, "5", T_TINY, NAVY, 700, "middle")
    s.text(500, R3 - 70, "KT1", T_SMALL, TIMEC, 700, "start")
    s.path(f"M 532 {R3} L 916 {R3}", SYM, SW)
    lamp(s, 940, R3, 24)
    s.text(940, R3 - 38, "H2", T_SMALL, NAVY, 700, "middle")
    s.path(f"M 964 {R3} L {RX} {R3}", SYM, SW)
    node(s, RX, R3)

    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    y = note_strip(s, NY + 34, "S1 অন করার t সময় পরে H1 জ্বলে আর H2 নেভে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_lamps.svg")


# ── ১০. তিন বাতি পরপর ────────────────────────────────────────────────────
def d10_sequence():
    s = SVG(1240, 760)
    s.title("দুটি টাইমারে তিনটি বাতির ক্রমিক নিয়ন্ত্রণ", T_TITLE)
    LY, RX, B = 160, 1130, 330          # B = S1-এর পরের খাড়া বাস
    rungs = [LY, LY + 96, LY + 192, LY + 288, LY + 384]
    NY = LY + 470
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", SYM, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 222 {LY}", SYM, SW)
    _no(s, 222, LY, SYM)
    s.text(268, LY - 58, "S1", T_SMALL, NAVY, 700, "middle")
    s.path(f"M 314 {LY} L {B} {LY}", SYM, SW)
    s.path(f"M {B} {LY} L {B} {rungs[4]}", SYM, SW)
    for r in rungs[1:]:
        node(s, B, r)

    def load_lamp(y, tag):
        lamp(s, 940, y, 24)
        s.text(940, y - 36, tag, T_SMALL, NAVY, 700, "middle")
        s.path(f"M 964 {y} L {RX} {y}", SYM, SW)

    def load_coil(y, tag):
        timer_coil(s, 860, y - 30, 160, 60, tag, "on")
        s.path(f"M 1020 {y} L {RX} {y}", SYM, SW)

    # ১: H1 সরাসরি
    s.path(f"M {B} {rungs[0]} L 916 {rungs[0]}", SYM, SW)
    load_lamp(rungs[0], "H1")
    # ২: KT1 কয়েল
    s.path(f"M {B} {rungs[1]} L 860 {rungs[1]}", SYM, SW)
    load_coil(rungs[1], "KT1")
    # ৩: KT1 NO → H2,  আর সেই নোড থেকে ৪: KT2 কয়েল
    s.path(f"M {B} {rungs[2]} L 480 {rungs[2]}", SYM, SW)
    dno(s, 480, rungs[2], SYM, "on")
    s.text(540, rungs[2] - 70, "KT1", T_SMALL, TIMEC, 700, "start")
    s.path(f"M 572 {rungs[2]} L 916 {rungs[2]}", SYM, SW)
    load_lamp(rungs[2], "H2")
    J = 700
    node(s, J, rungs[2])
    s.path(f"M {J} {rungs[2]} L {J} {rungs[3]} L 860 {rungs[3]}", SYM, SW)
    load_coil(rungs[3], "KT2")
    # ৫: KT2 NO → H3
    s.path(f"M {B} {rungs[4]} L 480 {rungs[4]}", SYM, SW)
    dno(s, 480, rungs[4], SYM, "on")
    s.text(540, rungs[4] - 70, "KT2", T_SMALL, TIMEC, 700, "start")
    s.path(f"M 572 {rungs[4]} L 916 {rungs[4]}", SYM, SW)
    load_lamp(rungs[4], "H3")

    s.path(f"M {RX} {LY} L {RX} {NY}", NEUT, SW)
    for r in rungs:
        node(s, RX, r, NEUT)
    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    y = note_strip(s, NY + 34, "S1 অন করলে H1 সঙ্গে সঙ্গে, H2 t1 সময় পরে এবং "
                               "H3 আরও t2 সময় পরে জ্বলে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_sequence.svg")


# ── ১১. নির্দিষ্ট সময় পর মোটর নিজে থেমে যায় ─────────────────────────────
def _autostop(s, oy, live=True):
    LY = oy + 150
    HB, TC, RL, NY = LY + 96, LY + 184, LY + 268, LY + 346
    RX, T = 1150, 236
    AX, BX, C = 668, 778, 830
    on = LIVE if live else SYM
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", on, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 262 {LY}", on, SW)

    # F2 95-96
    _nc(s, 262, LY, on)
    s.path(f"M 302 {nc_tip(262, LY, 302)} L 302 {LY - 64}", SYM, 2,
           dash="6 5")
    thermal_sym(s, 302, LY - 88, 34, 40, SYM, 2.4)
    s.text(328, LY - 112, "F2", T_SMALL, AMBER, 700, "start")
    s.text(272, LY + 36, "95", T_TINY, NAVY, 700, "middle")
    s.text(354, LY + 36, "96", T_TINY, NAVY, 700, "middle")
    # STOP
    s.path(f"M 354 {LY} L 394 {LY}", on, SW)
    _nc(s, 394, LY, on)
    _pb(s, 440, LY, RED, "#F6C9C4", "STOP")
    # KT1 8-5 — বিলম্বিত NC, START জোড়ের আগে
    s.path(f"M 486 {LY} L 526 {LY}", on, SW)
    dnc(s, 526, LY, on, "on")
    s.text(586, LY - 76, "KT1", T_SMALL, TIMEC, 700, "start")
    s.text(536, LY + 36, "8", T_TINY, NAVY, 700, "middle")
    s.text(610, LY + 36, "5", T_TINY, NAVY, 700, "middle")
    s.path(f"M 618 {LY} L {AX} {LY}", on, SW)

    # START ‖ KM1 13-14
    _no(s, AX, LY, on, closed=False, w=BX - AX)
    _pb(s, (AX + BX) / 2, LY, GREEN, "#BFE3CE", "START",
        tip=no_tip(AX, LY, (AX + BX) / 2, BX - AX))
    s.path(f"M {AX} {LY} L {AX} {HB} L {AX + 15} {HB}", on, SW)
    _no(s, AX + 15, HB, on, closed=live, w=80)
    s.path(f"M {AX + 95} {HB} L {BX} {HB} L {BX} {LY}", on, SW)
    s.text((AX + BX) / 2, HB + 40, "KM1 13-14", T_SMALL,
           LIVE if live else NAVY, 700, "middle")

    # C থেকে তিন শাখা:  KM1 কয়েল, KT1 কয়েল, H1
    s.path(f"M {BX} {LY} L 890 {LY}", on, SW)
    node(s, C, LY, on)
    coil_sym(s, 890, LY - 34, 130, 68, "KM1")
    s.text(884, LY - 42, "A1", T_TINY, NAVY, 700, "end")
    s.text(1026, LY - 42, "A2", T_TINY, NAVY, 700, "start")
    s.path(f"M 1020 {LY} L {RX} {LY} L {RX} {NY}", NEUT, SW)

    s.path(f"M {C} {LY} L {C} {RL}", on, SW)
    node(s, C, TC, on)
    s.path(f"M {C} {TC} L 870 {TC}", on, SW)
    timer_coil(s, 870, TC - 34, 170, 68, "KT1", "on")
    s.text(864, TC - 42, "2", T_TINY, NAVY, 700, "end")
    s.text(1046, TC - 42, "7", T_TINY, NAVY, 700, "start")
    s.path(f"M 1040 {TC} L {RX} {TC}", NEUT, SW)
    node(s, RX, TC, NEUT)

    s.path(f"M {C} {RL} L 931 {RL}", on, SW)
    lamp(s, 955, RL, 24, on=live)
    s.path(f"M 979 {RL} L {RX} {RL}", NEUT, SW)
    node(s, RX, RL, NEUT)
    s.text(992, RL + 40, "H1 (চলার বাতি)", T_SMALL, GREEN, 700, "start")

    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    return NY


def d11_autostop():
    s = SVG(1240, 720)
    s.title("স্বয়ংক্রিয় মোটর বন্ধের কন্ট্রোল সার্কিট (মোটর চলছে)", T_TITLE)
    ny = _autostop(s, 70, live=True)
    y = note_strip(s, ny + 40, "t পূর্ণ হলে 8-5 খোলে; দুটি কয়েল ছেড়ে দেয়, ল্যাচ "
                               "ভাঙে এবং মোটর থামে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_autostop.svg")


# ── ১২. স্বয়ংক্রিয় বন্ধের টাইমিং ──────────────────────────────────────
def d12_stoptiming():
    s = SVG(1240, 760)
    s.title("স্বয়ংক্রিয় মোটর বন্ধের টাইমিং চার্ট", T_TITLE)
    px, lows = timing(s, 290, 96, 900,
                      [("START", [(1, 1.6), (9, 9.6)], GREEN),
                       ("STOP", [(11.5, 12.1)], RED),
                       ("KM1 · মোটর", [(1, 7), (9, 11.5)], LIVE),
                       ("KT1 কয়েল", [(1, 7), (9, 11.5)], STEEL),
                       ("KT1 8 – 5", [(0, 7), (7.15, 14)], TIMEC)], 14, RH=92)
    for t in (1, 7):
        s.path(f"M {px(t)} {lows[0] - 44} L {px(t)} {lows[4] + 16}", GREY,
               1.8, dash="6 5")
    dim_arrow(s, px(1), px(7), lows[4] + 48, "বসানো সময় t", RED, below=True)
    dim_arrow(s, px(9), px(11.5), lows[4] + 48, "t-এর আগে STOP", GREY,
              below=True)
    y = note_strip(s, lows[4] + 104, "8-5 অল্প সময়ের জন্য খোলে; কয়েল সরবরাহ হারালেই "
                                     "টাইমার শূন্যে ফেরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d12_stoptiming.svg")


# ── ১৩. কানেকশন ডায়াগ্রাম ──────────────────────────────────────────────
# তারের ক্রম:  L → F1 → F2 95 → 96 → STOP 11 → 12 → KT1 8 → 5 → START 13 → 14
#        → A1;  A2 → N
# হোল্ডিং: KM1 13 → (KT1 5 = START 13),  KM1 14 → (START 14 = A1)
# টাইমার:  KT1 2 → A1,  KT1 7 → N
def d13_wiring():
    s = SVG(1240, 1080)
    s.title("স্বয়ংক্রিয় বন্ধের স্টার্টারের কানেকশন ডায়াগ্রাম", T_TITLE)

    def term(x, y, t, w=44, h=26):
        s.rect(x - w / 2, y, w, h, "#D7E2EC", STEEL, 2, 4)
        if t:
            s.text(x, y + h - 7, t, T_TINY, NAVY, 700, "middle")

    def sterm(x, cy, t, w=40, h=26):
        s.rect(x - w / 2, cy - h / 2, w, h, "#D7E2EC", STEEL, 2, 4)
        s.text(x, cy + 6, t, T_TINY, NAVY, 700, "middle")

    # ── KM1 ─────────────────────────────────────────────────────
    KX, KY, KW, KH = 440, 290, 330, 250
    H14, H13 = 320, 350
    s.rect(KX, KY, KW, KH, "#EEF3F8", STEEL, 3, 12)
    s.text(KX + KW / 2 + 20, KY + 150, "KM1", 40, STEEL, 700, "middle")
    s.text(KX + KW / 2 + 20, KY + 186, "কন্টাক্টর", T_BODY, GREY, 400,
           "middle")
    MAIN = [545, 610, 675]
    for i, x in enumerate(MAIN):
        term(x, KY - 26, str(2 * i + 1))
        s.path(f"M {x} {KY - 26} L {x} 214", LIVE, 3.6)
        s.text(x, 202, f"L{i + 1}", T_SMALL, LIVE, 700, "middle")
    # তিন ফেজ আলাদা লিড — এক দাগে জুড়লে ফেজ-টু-ফেজ শর্ট
    s.text(610, 164, "সরবরাহ", T_BODY, LIVE, 700, "middle")
    term(480, KY - 26, "A1")
    term(740, KY - 26, "A2")
    sterm(KX - 22, H14, "14")
    sterm(KX - 22, H13, "13")

    # ── F2 ──────────────────────────────────────────────────────
    FX, FY, FW, FH = 440, 600, 330, 180
    P96, P95 = 716, 752
    for x in MAIN:
        s.path(f"M {x} {KY + KH} L {x} {FY}", CU, 7)
    s.rect(FX, FY, FW, FH, "#FFF8EA", AMBER, 3, 12)
    s.text(FX + FW / 2 + 20, FY + 70, "F2", 40, AMBER, 700, "middle")
    s.text(FX + FW / 2 + 20, FY + 106, "ওভারলোড রিলে", T_BODY, GREY, 400,
           "middle")
    for i, x in enumerate(MAIN):
        term(x, FY + FH, f"{2 * i + 2}/T{i + 1}", 56)
        s.path(f"M {x} {FY + FH + 26} L {x} 870", LIVE, 3.6)
        s.text(x, 898, "UVW"[i], T_SMALL, LIVE, 700, "middle")
    s.text(512, 898, "মোটরে", T_BODY, LIVE, 700, "end")
    sterm(FX - 22, P96, "96")
    sterm(FX - 22, P95, "95")

    # ── বাঁয়ের খাড়া সারি ────────────────────────────────────────
    BXc = 200

    def button(top, h, name, sub, col, bg, t_top, t_bot, w=180):
        s.rect(BXc - w / 2, top, w, h, bg, col, 2.8, 10)
        s.text(BXc, top + h / 2 - 4, name, T_NAME, col, 700, "middle")
        s.text(BXc, top + h / 2 + 26, sub, T_TINY, GREY, 700, "middle")
        term(BXc, top - 26, t_top)
        term(BXc, top + h, t_bot)

    button(210, 84, "START", "NO, সবুজ", GREEN, GREENBG, "14", "13")
    # টাইমারের সকেট
    SY, SH = 390, 120
    s.rect(BXc - 90, SY, 180, SH, TIMEBG, TIMEC, 2.8, 10)
    s.text(BXc + 10, SY + 52, "KT1", T_NAME, TIMEC, 700, "middle")
    s.text(BXc + 10, SY + 84, "টাইমারের সকেট", T_TINY, GREY, 700, "middle")
    term(BXc, SY - 26, "5")
    term(BXc, SY + SH, "8")
    P2, P7 = SY + 36, SY + 86
    sterm(BXc - 112, P2, "2")
    sterm(BXc - 112, P7, "7")
    button(590, 84, "STOP", "NC, লাল", RED, REDBG, "12", "11")
    button(790, 70, "F1", "কন্ট্রোল ফিউজ", NAVY, PLATE, "", "", w=130)

    # শিকলের খাড়া অংশ
    s.path(f"M {BXc} 320 L {BXc} {SY - 26}", NAVY, 3)      # START 13 → KT1 5
    node(s, BXc, H13, NAVY)
    s.path(f"M {BXc} {SY + SH + 26} L {BXc} 564", NAVY, 3)  # KT1 8 → STOP 12
    # STOP 11 → F2 96
    s.path(f"M {BXc} 700 L {BXc} {P96} L {FX - 42} {P96}", NAVY, 3)
    # F1 → F2 95
    s.path(f"M {BXc} 764 L {BXc} {P95} L {FX - 42} {P95}", NAVY, 3)
    # কন্ট্রোল সরবরাহ → F1
    s.path(f"M 60 940 L {BXc} 940 L {BXc} 886", LIVE, 3)
    s.text(60, 974, "কন্ট্রোল সরবরাহ L", T_SMALL, LIVE, 700, "start")
    # START 14 → A1
    s.path(f"M {BXc} 184 L {BXc} 130 L 480 130 L 480 {KY - 26}", NAVY, 3)
    node(s, 330, 130, NAVY)
    node(s, 480, 130, NAVY)
    # A2 → N
    s.path(f"M 740 {KY - 26} L 740 130 L 1150 130", NEUT, 3)
    s.text(1150, 114, "A2 → কন্ট্রোল N", T_SMALL, NEUT, 700, "end")
    # KT1 2 → A1 — সবার উপর দিয়ে
    s.path(f"M {BXc - 132} {P2} L 44 {P2} L 44 90 L 480 90 L 480 130",
           TIMEC, 3)
    s.text(275, 80, "KT1 2 → A1", T_SMALL, TIMEC, 700, "middle")
    # KT1 7 → N
    s.path(f"M {BXc - 132} {P7} L 20 {P7}", NEUT, 3)
    s.text(22, P7 + 34, "N", T_SMALL, NEUT, 700, "start")

    # হোল্ডিং তার
    s.path(f"M {KX - 42} {H14} L 330 {H14} L 330 130", GREEN, 3, dash="9 6")
    s.path(f"M {KX - 42} {H13} L {BXc} {H13}", GREEN, 3, dash="9 6")
    s.text(344, H14 - 14, "হোল্ডিং", T_SMALL, GREEN, 700, "start")

    # ডান পাশের ব্যাখ্যা
    s.rect(830, 330, 350, 420, LIGHT, STEEL, 2, 10)
    lines = ("তারের ক্রম:", "L → F1 → 95 → 96", "→ STOP → KT1 8 → 5",
             "→ START → A1", "A2 → N", "",
             "হোল্ডিং: KM1 13-14", "টাইমার: 2 → A1, 7 → N")
    for i, t in enumerate(lines):
        if t:
            s.text(1005, 380 + i * 46, t, T_SMALL,
                   STEEL if i in (0, 6, 7) else NAVY, 700, "middle")

    y = note_strip(s, 1000, "KT1-এর 8-5 বসে STOP-এর পরে ও START-এর আগে; "
                            "হোল্ডিং তার জোড়ে 8-5-এর পরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_wiring.svg")


# ── ১৪. দ্বিতীয় মোটর দেরিতে চালু ─────────────────────────────────────────
def d14_twomotor():
    s = SVG(1240, 760)
    s.title("দ্বিতীয় মোটর t সময় পরে চালুর কন্ট্রোল সার্কিট", T_TITLE)
    LY = 220
    HB, R2, R3, NY = LY + 96, LY + 190, LY + 290, LY + 380
    RX, AX, BX, C = 1160, 590, 700, 770
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", SYM, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 230 {LY}", SYM, SW)
    for x, tag in ((230, "F2"), (346, "F3")):
        _nc(s, x, LY, SYM)
        s.path(f"M {x + 40} {nc_tip(x, LY, x + 40)} L {x + 40} {LY - 64}",
               SYM, 2, dash="6 5")
        thermal_sym(s, x + 40, LY - 88, 34, 40, SYM, 2.4)
        s.text(x + 66, LY - 112, tag, T_SMALL, AMBER, 700, "start")
        s.path(f"M {x + 92} {LY} L {x + 116} {LY}", SYM, SW)
    _nc(s, 462, LY, SYM)
    _pb(s, 508, LY, RED, "#F6C9C4", "STOP")
    s.path(f"M 554 {LY} L {AX} {LY}", SYM, SW)
    _no(s, AX, LY, SYM, w=BX - AX)
    _pb(s, (AX + BX) / 2, LY, GREEN, "#BFE3CE", "START",
        tip=no_tip(AX, LY, (AX + BX) / 2, BX - AX))
    s.path(f"M {AX} {LY} L {AX} {HB} L {AX + 15} {HB}", SYM, SW)
    _no(s, AX + 15, HB, SYM, w=80)
    s.path(f"M {AX + 95} {HB} L {BX} {HB} L {BX} {LY}", SYM, SW)
    s.text((AX + BX) / 2, HB + 40, "KM1 13-14", T_SMALL, NAVY, 700,
           "middle")

    s.path(f"M {BX} {LY} L 950 {LY}", SYM, SW)
    node(s, C, LY)
    s.path(f"M {C} {LY} L {C} {R3}", SYM, SW)

    def coil_at(y, tag, kind=None):
        if kind:
            timer_coil(s, 950, y - 32, 150, 64, tag, kind)
        else:
            coil_sym(s, 950, y - 32, 150, 64, tag)
        s.path(f"M 1100 {y} L {RX} {y}", NEUT, SW)
        node(s, RX, y, NEUT)

    coil_at(LY, "KM1")
    s.text(1030, LY - 44, "মোটর ১", T_SMALL, NAVY, 700, "middle")
    node(s, C, R2)
    s.path(f"M {C} {R2} L 950 {R2}", SYM, SW)
    coil_at(R2, "KT1", "on")
    s.path(f"M {C} {R3} L 810 {R3}", SYM, SW)
    dno(s, 810, R3, SYM, "on")
    s.text(870, R3 - 70, "KT1", T_SMALL, TIMEC, 700, "start")
    s.text(820, R3 + 34, "8", T_TINY, NAVY, 700, "middle")
    s.text(894, R3 + 34, "6", T_TINY, NAVY, 700, "middle")
    s.path(f"M 902 {R3} L 950 {R3}", SYM, SW)
    coil_at(R3, "KM2")
    s.text(1030, R3 + 60, "মোটর ২", T_SMALL, NAVY, 700, "middle")

    s.path(f"M {RX} {LY} L {RX} {NY}", NEUT, SW)
    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    y = note_strip(s, NY + 40, "STOP চাপলে বা যেকোনো ওভারলোড রিলে ট্রিপ করলে দুটি মোটরই থামে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d14_twomotor.svg")


ALL = [d01_idea, d02_types, d03_ah3, d04_pins, d05_ondelay, d06_offdelay,
       d07_symbols, d08_dial, d09_lamps, d10_sequence, d11_autostop,
       d12_stoptiming, d13_wiring, d14_twomotor]


if __name__ == "__main__":
    import svgkit as K
    os.makedirs(OUT, exist_ok=True)
    K.COLLECT = True
    for f in ALL:
        try:
            f()
        except Exception as e:
            print("  (collect)", f.__name__, e)
    K.COLLECT = False
    K.flush()
    for f in ALL:
        print("✓", os.path.relpath(f()))
