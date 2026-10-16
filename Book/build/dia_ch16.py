# -*- coding: utf-8 -*-
"""অধ্যায় ১৬ — সোলার : ডায়াগ্রাম।

সহায়কগুলো অধ্যায় ৮, ৯ ও ১১ থেকে আমদানি করা (CLAUDE.md-র নিয়ম):
`panel`, `note_strip`, `node`, `blk`, `chip`, `callout` অধ্যায় ৮ থেকে;
`fuse`, `lamp` অধ্যায় ৯ থেকে;  `earth`, `meter` অধ্যায় ১১ থেকে।
`photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই এখানে
`_use_ch16_images()` দিয়ে বদলে নেওয়া হয়েছে।

**সংখ্যা কোথা থেকে** — ছবির প্রতিটি বৈদ্যুতিক সংখ্যা আসল ডেটাশিটের,
কোনোটাই বানানো নয়:

  বড় মডিউল  Trina TSM-500 DE18M.08 — Vmp 42.8, Imp 11.69, Voc 51.7,
           Isc 12.28, দক্ষতা 20.7 %, NOCT 43 সেলসিয়াস, Pmax -0.34 %,
           Voc -0.25 %, Isc +0.04 % প্রতি ডিগ্রিতে, সর্বোচ্চ সিস্টেম
           ভোল্টেজ 1500 V, সর্বোচ্চ সিরিজ ফিউজ 20 A।  d05 ও ১৬.৭-এর
           অন-গ্রিড হিসাব দুটোই এই মডিউলের।
  ছোট মডিউল Phaesun Sun Plus 165 P — Pmax 165, Vmp 19.4, Imp 8.51,
           Voc 23.5, Isc 8.80, সর্বোচ্চ সিস্টেম ভোল্টেজ 1000 V।
           সংখ্যাগুলো `assets_ch16.py`-র ph_label ছবির স্টিকার থেকে
           পড়া — d04, d06, d08 ও ১৬.৮-এর অফ-গ্রিড হিসাব এই মডিউলের।
  কন্ট্রোলার EPEVER Tracer4210AN — 40 A, 520 W/12 V, 1040 W/24 V,
           সর্বোচ্চ PV Voc 100 V (সর্বনিম্ন তাপমাত্রায়) / 92 V
           (25 সেলসিয়াসে), বুস্ট 14.4, ফ্লোট 13.8, LVD 11.1 V।

**বক্ররেখা গুণগত, কিন্তু প্রান্তবিন্দু আসল** — Voc, Isc,
Vmp, Imp ওই ডেটাশিটেরই, আর তাপমাত্রার সরণটুকু -0.25 %/ডিগ্রি ধরে
হিসাব করে আঁকা।  তাই ছবি দেখে সংখ্যা মেলানো যায়।

**তিনটি সিস্টেম এক ছবিতে (d09)** — আলাদা তিন ছবি না করে একটাই লম্বা
ছবি, কারণ তুলনাটাই পাঠ:  অন-গ্রিডে ব্যাটারি নেই, অফ-গ্রিডে গ্রিড
নেই, হাইব্রিডে দুটোই।  পাশাপাশি না থাকলে পার্থক্যটা চোখে পড়ে না।

**সংযোগের ছবিতে ধনাত্মক তার লাল, ঋণাত্মক কালো, AC ইস্পাতরঙা** —
পুরো অধ্যায়ে এক নিয়ম।  DC আর AC এক ছবিতে থাকলে মাঝখানে ইনভার্টারের
সীমানা টানা আছে, যাতে কোন দিকটা DC তা নিয়ে সন্দেহ না থাকে।

কালপুরুষের সীমা আগের অধ্যায়গুলোর মতোই — টার্মিনাল, রেটিং, মডেল
নম্বর ল্যাটিন অঙ্কে;  `÷`, `Ω`, `°` ছবিতে নেই ("ডিগ্রি" লেখা হয়)।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, blk, chip, callout,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, LIVE, NEUT, DEAD, PLATE, CU)
from dia_ch09 import fuse, lamp
from dia_ch11 import earth, meter
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch16")
IMG = os.path.join(HERE, "assets", "ch16")

SUN = "#E3A008"           # সূর্য ও আলো
SUNBG = "#FDF3DA"
GLASS = "#1D4E7C"         # মডিউলের কাচ
GLASS2 = "#2C6EA8"
CELL = "#173C5E"
DCP = "#C0392B"           # DC ধনাত্মক
DCN = "#1F2933"           # DC ঋণাত্মক
ACW = "#1D5B8F"           # AC
BATT = "#2F7D4F"
BATTBG = "#E7F3EC"


def _use_ch16_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch16_images()
    return C8.photo_callouts(*a, **k)


# ── সাধারণ প্রতীক ──────────────────────────────────────────────────────
def sun(s, cx, cy, r=34, rays=12, col=SUN):
    """সূর্য — গোল চাকতি আর চারদিকে রশ্মি।"""
    s.circle(cx, cy, r, SUNBG, col, 3.2)
    for i in range(rays):
        a = 2 * math.pi * i / rays
        x0, y0 = cx + (r + 9) * math.cos(a), cy + (r + 9) * math.sin(a)
        x1, y1 = cx + (r + 24) * math.cos(a), cy + (r + 24) * math.sin(a)
        s.path(f"M {x0:.1f} {y0:.1f} L {x1:.1f} {y1:.1f}", col, 3)


def ray(s, x0, y0, x1, y1, col=SUN, sw=3.2, marker=None):
    """আলোর তীর — সবসময় একই ধাঁচে।"""
    s.path(f"M {x0} {y0} L {x1} {y1}", col, sw, dash="13 8", marker=marker)


def pv_module(s, x, y, w, h, cols=6, rows=10, frame="#8A98A5",
              glass=GLASS, cell=CELL, label=None, size=T_SMALL):
    """সোলার মডিউল — ফ্রেম, কাচ আর সেলের জাল।  `cols`/`rows` সেলের
    সারি-কলাম;  ছবি ছোট হলে কমিয়ে দিতে হয়, নইলে জাল কালো দেখায়।"""
    s.rect(x, y, w, h, glass, frame, 3.4, 6)
    gx, gy = 5.0, 5.0
    cw = (w - 2 * gx - (cols - 1) * 3.2) / cols
    ch = (h - 2 * gy - (rows - 1) * 3.2) / rows
    for r in range(rows):
        for c in range(cols):
            s.rect(x + gx + c * (cw + 3.2), y + gy + r * (ch + 3.2),
                   cw, ch, cell, "none", 0, 1.5)
    if label:
        s.text(x + w / 2, y + h + size + 10, label, size, NAVY, 700,
               "middle")
    return x, y, w, h


def jbox(s, cx, cy, w=54, h=34, col="#3A4652"):
    """মডিউলের পিছনের জাংশন বক্স।"""
    s.rect(cx - w / 2, cy - h / 2, w, h, "#2E3842", col, 2.4, 4)


def dev(s, x, y, w, h, name, sub=None, col=STEEL, fill="#FCFDFE",
        size=T_NAME, subsize=T_SMALL):
    """সিস্টেম ডায়াগ্রামের যন্ত্র-বাক্স — নাম উপরে, রেটিং নিচে।"""
    s.rect(x, y, w, h, fill, col, 3, 11)
    if sub:
        s.text(x + w / 2, y + h / 2 - 6, name, size, col, 700, "middle")
        s.text(x + w / 2, y + h / 2 + 26, sub, subsize, GREY, 700, "middle")
    else:
        s.text(x + w / 2, y + h / 2 + size * 0.34, name, size, col, 700,
               "middle")
    return x, y, w, h


def battery(s, x, y, w, h, tag=None, col=BATT):
    """ব্যাটারি — দুটি খোপ আর উপরে দুই টার্মিনাল।"""
    s.rect(x, y, w, h, BATTBG, col, 3, 7)
    s.rect(x + w * 0.16, y - 11, w * 0.14, 11, col, "none", 0, 2)
    s.rect(x + w * 0.70, y - 11, w * 0.14, 11, col, "none", 0, 2)
    s.text(x + w * 0.23, y - 18, "+", T_BODY, DCP, 700, "middle")
    s.text(x + w * 0.77, y - 18, "-", T_BODY, DCN, 700, "middle")
    s.line(x + w / 2, y + 8, x + w / 2, y + h - 8, col, 2, dash="6 6")
    if tag:
        s.text(x + w / 2, y + h / 2 + T_BODY * 0.34, tag, T_BODY, col,
               700, "middle")
    return x + w * 0.23, x + w * 0.77          # + আর - টার্মিনালের x


def batt_sym(s, x, ytop, ybot, col=SYM, sw=3.2, cells=2):
    """ব্যাটারির প্রতীক — লম্বা-খাটো দাগ।  সার্কিট ডায়াগ্রামে।"""
    n = cells * 2
    step = (ybot - ytop) / (n - 1)
    for i in range(n):
        wdt = 26 if i % 2 == 0 else 14
        yy = ytop + i * step
        s.path(f"M {x - wdt} {yy} L {x + wdt} {yy}", col, sw)


def dcbreak(s, x, y, w, h, y1, y2, tag="DC আইসোলেটর", col=STEEL):
    """DC আইসোলেটর — দুই পোল একসঙ্গে ছেঁড়ে।  y1/y2 দুই পোলের উচ্চতা;
    নামটি বাক্সের নিচে বসে, ভেতরে নয় — ভেতরে বসালে তারের সঙ্গে
    লেগে যায়।"""
    s.rect(x, y, w, h, "#FFFFFF", col, 2.8, 9)
    for yy in (y1, y2):
        s.circle(x + w * 0.28, yy, 5.5, col)
        s.circle(x + w * 0.72, yy, 5.5, col)
        s.path(f"M {x + w * 0.28} {yy} L {x + w * 0.72} {yy - 18}", col, 3)
    s.path(f"M {x + w * 0.5} {y1 - 9} L {x + w * 0.5} {y2 - 9}", col, 2.2,
           dash="6 5")
    s.text(x + w / 2, y + h + 28, tag, T_SMALL, col, 700, "middle")
    return x, y, w, h


# ── ১. আলো পড়লেই বিদ্যুৎ ───────────────────────────────────────────────
def d01_idea():
    s = SVG(1240, 700)
    s.title("সোলার মডিউল: আলো থেকে বিদ্যুৎ", T_TITLE)
    ar = s.arrow_defs(SUN, "arS", 15)
    ad = s.arrow_defs(DCP, "arD", 14)

    sun(s, 158, 190, 40)
    s.text(158, 290, "সূর্যের আলো", T_BODY, SUN, 700, "middle")

    MX, MY, MW, MH = 356, 116, 300, 216
    pv_module(s, MX, MY, MW, MH, cols=8, rows=5)
    for i in range(3):
        ray(s, 214, 150 + i * 46, MX - 14, 158 + i * 60, marker=ar)
    s.text(MX + MW / 2, MY + MH + 36, "সোলার মডিউল", T_NAME, NAVY, 700,
           "middle")

    # দুই তার — ধনাত্মক উপরে (লাল), ঋণাত্মক নিচে (কালো)
    PY_, NY_ = MY + 62, MY + 154
    s.path(f"M {MX + MW} {PY_} L 754 {PY_}", DCP, 4)
    s.path(f"M 846 {PY_} L 1010 {PY_} L 1010 {MY + 86}", DCP, 4)
    s.path(f"M {MX + MW} {NY_} L 1010 {NY_} L 1010 {MY + 138}", DCN, 4)
    s.text(700, PY_ - 20, "+", T_NODE, DCP, 700, "middle")
    s.text(700, NY_ + 36, "-", T_NODE, DCN, 700, "middle")

    meter(s, 800, PY_, 46, "A", NAVY)
    lamp(s, 1010, MY + 112, 26, True, AMBER)
    s.text(1010, MY + 182, "DC লোড", T_BODY, NAVY, 700, "middle")

    panel(s, 46, 420, 1148, 170, "যা মনে রাখতে হবে")
    for i, t in enumerate(("ঘোরে এমন কোনো অংশ নেই",
                           "উৎপাদন সরাসরি DC",
                           "আলো কমলে কারেন্ট কমে")):
        chip(s, 236 + i * 384, 500, t, size=T_BODY)
    s.text(620, 560, "ভোল্টেজ প্রায় একই থাকে, বদলায় কারেন্ট",
           T_SMALL, GREY, 700, "middle")

    y = note_strip(s, 610, "সোলার মডিউল নিজেই বিদ্যুতের উৎস, আর "
                           "এর আউটপুট DC")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. সেলের ভেতরে কী ঘটে ──────────────────────────────────────────────
def d02_cell():
    s = SVG(1240, 760)
    s.title("সোলার সেলের কার্যনীতি", T_TITLE)
    ar = s.arrow_defs(SUN, "arC", 15)
    ae = s.arrow_defs(RED, "arE", 13)

    X0, X1 = 150, 830
    layers = [("কাচ ও EVA", 118, 34, "#DCE9F3", "#9FB6C8"),
              ("সামনের গ্রিড ও ARC", 152, 22, "#B9C6D2", "#7E8C99"),
              ("N-টাইপ সিলিকন", 174, 66, "#8FB8DC", "#3C7FB5"),
              ("P-টাইপ সিলিকন", 240, 92, "#2D5F8A", "#1B3F5E"),
              ("পেছনের ধাতব স্তর", 332, 26, "#9AA6B2", "#6B7783"),
              ("ব্যাকশিট", 358, 28, "#E7ECF1", "#A9B4BF")]
    for name, y, h, fill, stroke in layers:
        s.rect(X0, y, X1 - X0, h, fill, stroke, 2.2, 3)
        callout(s, X1 + 190, y + h / 2, name, X1 + 8, y + h / 2,
                "end", T_BODY)

    # জংশন
    s.path(f"M {X0} 240 L {X1} 240", RED, 3.4, dash="11 7")
    s.text(X0 + 14, 232, "P-N জংশন", T_SMALL, RED, 700, "start")

    # ফোটন
    for i in range(3):
        ray(s, 250 + i * 150, 62, 302 + i * 150, 112, marker=ar)
    s.text(232, 74, "ফোটন", T_BODY, SUN, 700, "end")

    # ইলেকট্রন ও হোল
    for cx, cy, sym, col in ((430, 206, "-", RED), (500, 206, "-", RED),
                             (430, 290, "+", NAVY), (500, 290, "+", NAVY)):
        s.circle(cx, cy, 15, "#FFFFFF", col, 2.6)
        s.text(cx, cy + 8, sym, T_BODY, col, 700, "middle")
    s.path("M 560 206 L 640 206", RED, 3, marker=ae)
    s.path("M 400 290 L 330 290", NAVY, 3, marker=s.arrow_defs(NAVY, "arH", 13))
    s.text(660, 200, "ইলেকট্রন", T_SMALL, RED, 700, "start")
    s.text(310, 284, "হোল", T_SMALL, NAVY, 700, "end")

    # বাইরের সার্কিট — দুই তারই স্তরের নিচ দিয়ে, যাতে ডান দিকের
    # লেবেলগুলোর গায়ে না লাগে
    s.path(f"M {X0 + 44} 152 L 96 152 L 96 512 L 470 512", DCN, 3.6)
    s.path(f"M 610 512 L 760 512 L 760 345 L {X1 - 44} 345", DCP, 3.6)
    lamp(s, 540, 512, 28, True, AMBER)
    s.text(540, 570, "বাইরের সার্কিট", T_BODY, NAVY, 700, "middle")
    s.text(96, 544, "-", T_NODE, DCN, 700, "middle")
    s.text(786, 462, "+", T_NODE, DCP, 700, "middle")

    panel(s, 46, 590, 1148, 96, "একটি সেলের মাপ")
    for i, t in enumerate(("ওপেন সার্কিট ভোল্টেজ 0.6 থেকে 0.7 V",
                           "MPP-তে ভোল্টেজ প্রায় 0.5 থেকে 0.58 V")):
        chip(s, 330 + i * 580, 652, t, size=T_BODY)

    y = note_strip(s, 706, "ভোল্টেজ নির্ভর করে পদার্থের উপর; কারেন্ট নির্ভর করে "
                           "সেলের ক্ষেত্রফল ও আলোর তীব্রতার উপর")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_cell.svg")


# ── ৩. সেল থেকে অ্যারে ─────────────────────────────────────────────────
def d03_hierarchy():
    s = SVG(1240, 700)
    s.title("সেল, মডিউল, স্ট্রিং ও অ্যারে", T_TITLE)
    ar = s.arrow_defs(STEEL, "arH", 15)

    CY = 220
    xs = (46, 342, 638, 934)
    CW = 260
    for x in xs:
        s.rect(x, 120, CW, 250, "#FCFDFE", LINE, 1.8, 13)

    # ১. সেল
    s.rect(xs[0] + 88, CY - 44, 84, 84, CELL, "#8A98A5", 2.6, 4)
    for i in range(3):
        s.path(f"M {xs[0] + 92 + i * 26} {CY - 42} L {xs[0] + 92 + i * 26} "
               f"{CY + 38}", "#9FB6C8", 1.8)
    # ২. মডিউল
    pv_module(s, xs[1] + 76, CY - 56, 108, 112, cols=4, rows=6)
    # ৩. স্ট্রিং — তিন মডিউল সিরিজে
    for i in range(3):
        pv_module(s, xs[2] + 26 + i * 72, CY - 50, 58, 100, cols=2, rows=5)
    for i in range(2):
        s.path(f"M {xs[2] + 84 + i * 72} {CY} L {xs[2] + 98 + i * 72} {CY}",
               DCP, 3.4)
    # ৪. অ্যারে — দুই স্ট্রিং
    for r in range(2):
        for i in range(3):
            pv_module(s, xs[3] + 26 + i * 72, CY - 48 + r * 72, 58, 58,
                      cols=2, rows=3)
    s.path(f"M {xs[3] + 14} {CY - 19} L {xs[3] + 14} {CY + 53}", DCP, 3.4)
    s.path(f"M {xs[3] + 14} {CY - 19} L {xs[3] + 26} {CY - 19}", DCP, 3.4)
    s.path(f"M {xs[3] + 14} {CY + 53} L {xs[3] + 26} {CY + 53}", DCP, 3.4)

    names = ("সেল", "মডিউল", "স্ট্রিং", "অ্যারে")
    subs = ("Voc প্রায় 0.69 V", "55 সেল সিরিজে", "3 মডিউল সিরিজে",
            "2 স্ট্রিং প্যারালালে")
    vals = ("Isc প্রায় 18.5 A", "Voc 37.9 V · 550 W",
            "Voc 113.7 V · 1650 W", "113.7 V · 3300 W")
    for x, n, sb, v in zip(xs, names, subs, vals):
        s.text(x + CW / 2, 160, n, T_NAME, NAVY, 700, "middle")
        s.text(x + CW / 2, 322, sb, T_SMALL, STEEL, 700, "middle")
        s.text(x + CW / 2, 354, v, T_SMALL, GREY, 700, "middle")
    for x in xs[:-1]:
        s.path(f"M {x + CW + 6} {CY} L {x + CW + 28} {CY}", STEEL, 3.6,
               marker=ar)

    panel(s, 46, 400, 1148, 176, "কোনটি কীভাবে বাড়ে")
    for i, t in enumerate(("সিরিজে: ভোল্টেজ যোগ হয়, কারেন্ট একই",
                           "প্যারালালে: কারেন্ট যোগ হয়, ভোল্টেজ একই")):
        chip(s, 330 + i * 580, 486, t, size=T_BODY)
    s.text(620, 548, "বাজারে মডিউলকে প্যানেল বলা হয়", T_SMALL, GREY, 700, "middle")

    y = note_strip(s, 596, "অ্যারের ভোল্টেজ একটি স্ট্রিংয়ের ভোল্টেজের সমান; "
                           "মোট কারেন্ট স্ট্রিংগুলোর কারেন্টের যোগফল")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_hierarchy.svg")


# ── I-V বক্ররেখার সাধারণ হিসাব ─────────────────────────────────────────
def _ivcurve(voc, isc, vmp, imp, n=140):
    """এক-ডায়োড আদলের কাছাকাছি বক্ররেখা, যা চার প্রান্তবিন্দুর
    চারটিতেই ঠিক বসে — তাই ছবি দেখে ডেটাশিটের সংখ্যা মেলানো যায়।"""
    c2 = (vmp / voc - 1) / math.log(1 - imp / isc)
    c1 = (1 - imp / isc) * math.exp(-vmp / (c2 * voc))
    pts = []
    for k in range(n + 1):
        v = voc * k / n
        i = isc * (1 - c1 * (math.exp(v / (c2 * voc)) - 1))
        pts.append((v, max(i, 0.0)))
    return pts


def _graph(s, X0, Y0, XW, YH, xmax, ymax, xstep, ystep, xlab, ylab,
           ydec=0, col=NAVY):
    """অক্ষ ও জাল।  px/py ফেরত দেয়, যাতে বিন্দু বসানো যায়।"""
    px = lambda v: X0 + v / xmax * XW
    py = lambda i: Y0 - i / ymax * YH
    k = 0
    while k * ystep <= ymax + 1e-9:
        s.line(X0, py(k * ystep), X0 + XW, py(k * ystep), "#E3E9EF", 1.4)
        lab = f"{k * ystep:.{ydec}f}"
        s.text(X0 - 12, py(k * ystep) + 7, lab, T_BODY, GREY, 700, "end")
        k += 1
    k = 0
    while k * xstep <= xmax + 1e-9:
        s.text(px(k * xstep), Y0 + 32, f"{k * xstep:g}", T_BODY, GREY, 700,
               "middle")
        k += 1
    s.path(f"M {X0} {Y0 - YH - 10} L {X0} {Y0} L {X0 + XW + 10} {Y0}",
           col, 2.8)
    s.text(X0 + XW / 2, Y0 + 68, xlab, T_BODY, col, 700, "middle")
    s.text(X0 - 6, Y0 - YH - 26, ylab, T_BODY, col, 700, "start")
    return px, py


def _legend(s, x, y, items, dy=30, w=104):
    """লেখচিত্রের ছোট সূচি — রঙের দাগ আর পাশে সংখ্যা।  পেছনে সাদা
    পটভূমি, নইলে বক্ররেখার উপর বসে পড়ে।"""
    s.rect(x - 14, y - 24, w, (len(items) - 1) * dy + 44, "#FFFFFF",
           LINE, 1.6, 8, opacity=0.92)
    for i, (lab, col) in enumerate(items):
        s.path(f"M {x} {y + i * dy} L {x + 30} {y + i * dy}", col, 3.6)
        s.text(x + 40, y + i * dy + 7, lab, T_BODY, col, 700, "start")


def _plot(s, px, py, pts, col, sw=3.8, dash=None):
    d = "M " + " L ".join(f"{px(v):.1f} {py(i):.1f}" for v, i in pts)
    s.path(d, col, sw, dash=dash)


# ── ৪. I-V ও P-V বক্ররেখা ──────────────────────────────────────────────
def d04_iv():
    """Phaesun Sun Plus 165 P-এর নিজের স্টিকারের চারটি সংখ্যা —
    Voc 23.5, Isc 8.80, Vmp 19.4, Imp 8.51 — থেকেই বক্ররেখা।"""
    s = SVG(1240, 780)
    s.title("I-V ও P-V বক্ররেখা এবং সর্বোচ্চ পাওয়ারের বিন্দু", T_TITLE)
    VOC, ISC, VMP, IMP = 23.5, 8.80, 19.4, 8.51

    X0, Y0, XW, YH = 150, 560, 800, 400
    px, py = _graph(s, X0, Y0, XW, YH, 25, 10, 5, 2, "ভোল্টেজ (V)",
                    "কারেন্ট (A)")
    pts = _ivcurve(VOC, ISC, VMP, IMP)
    _plot(s, px, py, pts, DCP)

    # পাওয়ার বক্ররেখা — ডান দিকের অক্ষে, 250 W = সম্পূর্ণ উচ্চতা।
    # ২৫০ রাখা হয়েছে যাতে P-V আর I-V লেখাগুলো একে অন্যের ঘাড়ে না ওঠে।
    ppy = lambda p: Y0 - p / 250.0 * YH
    d = "M " + " L ".join(f"{px(v):.1f} {ppy(v * i):.1f}" for v, i in pts)
    s.path(d, STEEL, 3.4, dash="12 7")
    for p in (50, 100, 150, 200, 250):
        s.text(X0 + XW + 16, ppy(p) + 7, f"{p}", T_BODY, STEEL, 700, "start")
    s.text(X0 + XW + 14, Y0 - YH - 26, "পাওয়ার (W)", T_BODY, STEEL, 700,
           "start")

    # প্রান্তবিন্দু
    node(s, px(0), py(ISC), DCP, 8)
    node(s, px(VOC), py(0), DCP, 8)
    node(s, px(VMP), py(IMP), NAVY, 9)
    node(s, px(VMP), ppy(VMP * IMP), STEEL, 8)
    s.text(X0 + 14, py(ISC) - 22, "Isc 8.80 A", T_CALL, DCP, 700, "start")
    s.text(px(VOC) - 16, py(0) - 56, "Voc 23.5 V", T_CALL, DCP, 700, "end")
    s.path(f"M {px(VMP)} {py(IMP)} L {px(VMP)} {Y0}", NAVY, 2.2, dash="7 6")
    s.path(f"M {X0} {py(IMP)} L {px(VMP)} {py(IMP)}", NAVY, 2.2, dash="7 6")
    s.text(px(VMP) + 14, py(IMP) - 30, "MPP", T_NAME, NAVY, 700, "start")
    s.text(px(VMP) + 14, py(IMP) + 4, "19.4 V · 8.51 A", T_SMALL, NAVY,
           700, "start")
    s.text(px(VMP) - 16, ppy(VMP * IMP) - 18, "165 W", T_NAME, STEEL, 700,
           "end")

    y = note_strip(s, 660, "MPPT কন্ট্রোলার ও গ্রিড-টাই ইনভার্টার মডিউলকে "
                           "MPP-র কাছাকাছি চালিয়ে রাখে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_iv.svg")


# ── ৫. আলোর তীব্রতা ও তাপমাত্রার প্রভাব ────────────────────────────────
def d05_effects():
    """Trina TSM-500 DE18M.08-এর নিজের ডেটাশিট থেকে — Voc 51.7,
    Isc 12.28, Vmp 42.8, Imp 11.69, আর সহগ Voc -0.25 %, Isc +0.04 %,
    Pmax -0.34 % প্রতি ডিগ্রিতে।  এই মডিউলটিই ১৬.৭-এর অন-গ্রিড
    হিসাবে ব্যবহার হয়েছে, তাই সংখ্যাগুলো মেলে।"""
    s = SVG(1240, 800)
    s.title("আলোর তীব্রতা ও তাপমাত্রার প্রভাব", T_TITLE)
    VOC, ISC, VMP, IMP = 51.7, 12.28, 42.8, 11.69

    # ── বাঁ দিক:  আলোর তীব্রতা
    X0, Y0, XW, YH = 132, 452, 400, 306
    px, py = _graph(s, X0, Y0, XW, YH, 60, 15, 20, 5, "ভোল্টেজ (V)",
                    "কারেন্ট (A)")
    legL = []
    for g, col in ((1000, DCP), (800, "#D2763A"), (600, "#C9A000"),
                   (400, "#9AA6B2")):
        k = g / 1000.0
        # Voc আলো কমলে লগারিদমিক নিয়মে সামান্য কমে (55 সেল, n = 1.2)
        voc = VOC + 75 * 1.2 * 0.02585 * math.log(k)
        _plot(s, px, py, _ivcurve(voc, ISC * k, VMP + (voc - VOC),
                                  IMP * k), col, 3.4)
        legL.append((f"{g}", col))
    _legend(s, X0 + 40, Y0 - YH + 26, legL)
    s.text(X0 + XW / 2, Y0 + 104, "আলোর তীব্রতা W/m2 (সেল 25 সেলসিয়াস)",
           T_BODY, GREY, 700, "middle")

    # ── ডান দিক:  তাপমাত্রা
    X1 = 700
    px2, py2 = _graph(s, X1, Y0, XW, YH, 60, 15, 20, 5, "ভোল্টেজ (V)",
                      "কারেন্ট (A)")
    legR = []
    for t, col in ((15, "#1F5FBF"), (25, DCP), (45, "#D2763A"),
                   (65, "#B5321F")):
        voc = VOC * (1 - 0.0025 * (t - 25))
        isc = ISC * (1 + 0.0004 * (t - 25))
        _plot(s, px2, py2, _ivcurve(voc, isc, VMP * (1 - 0.0030 * (t - 25)),
                                    IMP * (1 + 0.0004 * (t - 25))), col, 3.4)
        legR.append((f"{t}", col))
    _legend(s, X1 + 40, Y0 - YH + 26, legR)
    s.text(X1 + XW / 2, Y0 + 104, "সেলের তাপমাত্রা সেলসিয়াসে "
                                  "(আলো 1000 W/m2)", T_BODY, GREY, 700,
           "middle")

    panel(s, 46, 592, 1148, 100, "Trina TSM-500 DE18M.08-এর সহগ")
    for i, t in enumerate(("Voc কমে 0.25 % প্রতি ডিগ্রিতে",
                           "Isc বাড়ে 0.04 %", "Pmax কমে 0.34 %")):
        chip(s, 250 + i * 370, 656, t, size=T_BODY)

    y = note_strip(s, 712, "স্ট্রিংয়ের হিসাব করতে হয় বছরের সবচেয়ে "
                           "ঠান্ডা সকালের Voc দিয়ে, STC-র Voc দিয়ে নয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_effects.svg")


# ── ৬. সিরিজ ও প্যারালাল ───────────────────────────────────────────────
def d06_series():
    """Phaesun 165 P — সিরিজে তিনটি, প্যারালালে তিনটি, মিশ্রে চারটি।
    মোট Pmax মডিউলের সংখ্যা দিয়ে গুণ, Voc x Isc দিয়ে নয়।"""
    s = SVG(1240, 860)
    s.title("মডিউল জোড়ার তিন উপায়: সিরিজ, প্যারালাল ও মিশ্র", T_TITLE)
    MW, MH, GAP = 84, 96, 30

    def scol(x, ytop, n):
        """n মডিউল উল্লম্বভাবে সিরিজে।  উপরের + আর নিচের - ফেরত দেয়।"""
        px_, nx_ = x + MW * 0.27, x + MW * 0.73
        for i in range(n):
            pv_module(s, x, ytop + i * (MH + GAP), MW, MH, cols=3, rows=5)
        for i in range(n - 1):
            yb = ytop + i * (MH + GAP) + MH
            s.path(f"M {nx_} {yb} L {nx_} {yb + GAP / 2} L {px_} "
                   f"{yb + GAP / 2} L {px_} {yb + GAP}", DCN, 3.2)
        return px_, ytop, nx_, ytop + (n - 1) * (MH + GAP) + MH

    CARD_Y, CARD_H = 104, 500
    for x, nm in ((46, "সিরিজ: 3টি"), (440, "প্যারালাল: 3টি"),
                  (834, "মিশ্র: 2 সিরিজ, 2 প্যারালাল")):
        s.rect(x, CARD_Y, 360, CARD_H, "#FCFDFE", LINE, 1.8, 13)
        s.text(x + 180, CARD_Y + 42, nm, T_NAME, NAVY, 700, "middle")

    # ক. সিরিজ — তিনটি এক কলামে
    p1, t1, n1, b1 = scol(184, 200, 3)
    s.path(f"M {p1} {t1} L {p1} {t1 - 34} L 120 {t1 - 34} L 120 {b1 + 30}",
           DCP, 3.4)
    s.path(f"M {n1} {b1} L {n1} {b1 + 30} L 120 {b1 + 30}", DCN, 3.4)

    # খ. প্যারালাল — তিনটি পাশাপাশি, উপরে + বাস, নিচে - বাস
    PY0 = 300
    xs = [478 + i * 106 for i in range(3)]
    for x in xs:
        pv_module(s, x, PY0, MW, MH, cols=3, rows=5)
        s.path(f"M {x + MW * 0.27} {PY0} L {x + MW * 0.27} {PY0 - 52}",
               DCP, 3.2)
        s.path(f"M {x + MW * 0.73} {PY0 + MH} L {x + MW * 0.73} "
               f"{PY0 + MH + 52}", DCN, 3.2)
    s.path(f"M {xs[0] + MW * 0.27} {PY0 - 52} L {xs[2] + MW * 0.27} "
           f"{PY0 - 52}", DCP, 3.4)
    s.path(f"M {xs[0] + MW * 0.73} {PY0 + MH + 52} L {xs[2] + MW * 0.73} "
           f"{PY0 + MH + 52}", DCN, 3.4)

    # গ. মিশ্র — দুই কলামে দুটি করে, কলাম দুটি প্যারালালে
    tops, bots = [], []
    for c in range(2):
        px_, ty, nx_, by = scol(898 + c * 148, 256, 2)
        s.path(f"M {px_} {ty} L {px_} {ty - 44}", DCP, 3.2)
        s.path(f"M {nx_} {by} L {nx_} {by + 44}", DCN, 3.2)
        tops.append(px_); bots.append(nx_)
        ty0, by0 = ty - 44, by + 44
    s.path(f"M {tops[0]} {ty0} L {tops[1]} {ty0}", DCP, 3.4)
    s.path(f"M {bots[0]} {by0} L {bots[1]} {by0}", DCN, 3.4)

    rows = [("সিরিজ: 3টি", "3 x 23.5 = 70.5 V", "8.80 A", "495 W"),
            ("প্যারালাল: 3টি", "23.5 V", "3 x 8.80 = 26.4 A", "495 W"),
            ("মিশ্র: 4টি", "2 x 23.5 = 47 V", "2 x 8.80 = 17.6 A",
             "660 W")]
    panel(s, 46, 624, 1148, 180, "Phaesun 165 P দিয়ে হিসাব")
    hx = (216, 520, 800, 1070)
    for j, h in enumerate(("সংযোগ", "অ্যারের Voc", "অ্যারের Isc",
                           "মোট Pmax")):
        s.text(hx[j], 690, h, T_BODY, STEEL, 700, "middle")
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            s.text(hx[j], 724 + i * 28, v, T_SMALL,
                   NAVY if j == 0 else INK, 700 if j == 0 else 400,
                   "middle")

    y = note_strip(s, 824, "মোট পাওয়ার = মডিউলের সংখ্যা x একটি মডিউলের Pmax; "
                           "Voc ও Isc গুণ করে নয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_series.svg")


# ── ৭. তিন ধরনের সোলার সিস্টেম ─────────────────────────────────────────
def d07_systems():
    """তিনটি আলাদা ছবি না করে একটাই — তুলনাটাই পাঠ।"""
    s = SVG(1240, 1000)
    s.title("অন-গ্রিড, অফ-গ্রিড ও হাইব্রিড সিস্টেম", T_TITLE)
    ar = s.arrow_defs(STEEL, "arY", 14)
    ad = s.arrow_defs(DCP, "arDd", 14)

    BW, BH = 168, 78

    def row(oy, name, chain, tail):
        s.rect(46, oy - 34, 1148, 250, "#FCFDFE", LINE, 1.8, 13)
        s.box_auto(140, oy - 20, name, T_BODY, fill=NAVY, stroke=NAVY,
                   tcolor="#FFFFFF", pad_x=20, pad_y=8)
        xs = [316 + i * 210 for i in range(len(chain))]
        for x, (nm, sub, col) in zip(xs, chain):
            dev(s, x, oy + 56, BW, BH, nm, sub, col)
        for i, x in enumerate(xs[:-1]):
            c = DCP if i < 1 else STEEL
            s.path(f"M {x + BW} {oy + 56 + BH / 2} L {x + 206} "
                   f"{oy + 56 + BH / 2}", c, 3.6,
                   marker=(ad if i < 1 else ar))
        s.text(140, oy + 100, tail, T_SMALL, GREY, 700, "middle")
        return xs

    # ক. অন-গ্রিড
    xs = row(96, "অন-গ্রিড",
             [("সোলার অ্যারে", "DC", GLASS2),
              ("গ্রিড-টাই ইনভার্টার", "DC থেকে AC", STEEL),
              ("নেট মিটার", "দুই দিকে মাপে", NAVY),
              ("লোড ও গ্রিড", "230 V AC", GREEN)],
             "ব্যাটারি নেই")
    s.text(620, 276, "গ্রিড চলে গেলে ইনভার্টার বন্ধ হয় (অ্যান্টি-আইল্যান্ডিং)",
           T_BODY, RED, 700, "middle")

    # খ. অফ-গ্রিড
    xs = row(376, "অফ-গ্রিড",
             [("সোলার অ্যারে", "DC", GLASS2),
              ("চার্জ কন্ট্রোলার", "PWM বা MPPT", AMBER),
              ("ব্যাটারি ব্যাংক", "12 বা 24 V", BATT),
              ("ইনভার্টার ও লোড", "230 V AC", GREEN)],
             "গ্রিড নেই")
    s.text(620, 556, "রাতে লোড চলে ব্যাটারি থেকে", T_BODY, NAVY, 700, "middle")

    # গ. হাইব্রিড
    xs = row(656, "হাইব্রিড",
             [("সোলার অ্যারে", "DC", GLASS2),
              ("হাইব্রিড ইনভার্টার", "MPPT ভেতরে", STEEL),
              ("ব্যাটারি ব্যাংক", "ব্যাকআপ", BATT),
              ("লোড ও গ্রিড", "230 V AC", GREEN)],
             "দুটোই আছে")
    s.text(620, 836, "হাইব্রিড ইনভার্টার সোলার, ব্যাটারি ও গ্রিড "
                     "তিনটি উৎসই নিয়ন্ত্রণ করে", T_BODY, NAVY, 700, "middle")

    y = note_strip(s, 898, "নেট মিটারিং হয় শুধু অন-গ্রিড ও হাইব্রিড "
                           "সিস্টেমে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_systems.svg")


# ── ৮. PWM না MPPT ─────────────────────────────────────────────────────
def d08_pwm():
    """একই Phaesun 165 P, একই 12 V ব্যাটারি — দুই কন্ট্রোলারে কত।
    PWM মডিউলকে ব্যাটারির ভোল্টেজে টেনে নামায়, তাই কাজের বিন্দু
    14.4 V-এ;  MPPT মডিউলকে 19.4 V-এ রেখে আউটপুট নামিয়ে আনে।"""
    s = SVG(1240, 780)
    s.title("PWM ও MPPT: একই মডিউলে পাওয়ারের তুলনা", T_TITLE)
    VOC, ISC, VMP, IMP = 23.5, 8.80, 19.4, 8.51

    X0, Y0, XW, YH = 150, 540, 740, 380
    px, py = _graph(s, X0, Y0, XW, YH, 25, 10, 5, 2, "ভোল্টেজ (V)",
                    "কারেন্ট (A)")
    pts = _ivcurve(VOC, ISC, VMP, IMP)
    _plot(s, px, py, pts, DCP)

    VB, IB = 14.4, 8.79           # বক্ররেখা এখানে প্রায় Isc-তেই সমতল
    # PWM-এর আয়তক্ষেত্র
    s.rect(px(0), py(IB), px(VB) - px(0), Y0 - py(IB), "#E9EDF1",
           "none", 0, 0)
    s.rect(px(0), py(IMP), px(VMP) - px(0), Y0 - py(IMP), "#FBE7E4",
           "none", 0, 0, opacity=0.55)
    node(s, px(VB), py(IB), STEEL, 9)
    node(s, px(VMP), py(IMP), DCP, 9)
    s.path(f"M {px(VB)} {py(IB)} L {px(VB)} {Y0}", STEEL, 2.2, dash="7 6")
    s.path(f"M {px(VMP)} {py(IMP)} L {px(VMP)} {Y0}", DCP, 2.2, dash="7 6")
    s.text(px(VB) - 18, py(IB) + 60, "PWM", T_NAME, STEEL, 700, "end")
    s.text(px(VB) - 18, py(IB) + 94, "14.4 V x 8.79 A", T_SMALL, STEEL,
           700, "end")
    s.text(px(VMP) + 16, py(IMP) - 66, "MPPT", T_NAME, DCP, 700, "start")
    s.text(px(VMP) + 16, py(IMP) - 32, "19.4 V x 8.51 A", T_SMALL, DCP,
           700, "start")

    cards = [("PWM", "127 W", "মডিউল চলে ব্যাটারির ভোল্টেজে", STEEL),
             ("MPPT", "165 W", "মডিউল চলে MPP-তে", DCP)]
    for i, (nm, big, sub, col) in enumerate(cards):
        x = 946
        yy = 150 + i * 170
        s.rect(x, yy, 248, 146, "#FCFDFE", col, 2.8, 12)
        s.text(x + 124, yy + 44, nm, T_NAME, col, 700, "middle")
        s.text(x + 124, yy + 92, big, T_TITLE, NAVY, 700, "middle")
        s.text(x + 124, yy + 126, sub, T_TINY, GREY, 700, "middle")
    s.text(1070, 510, "একই রোদে প্রায় 30 % বেশি", T_BODY, GREEN, 700,
           "middle")

    y = note_strip(s, 646, "Vmp 19.4 V-এর মডিউলে 12 V সিস্টেমে PWM ব্যবহার "
                           "করলে প্রায় এক-চতুর্থাংশ শক্তি কাজে লাগে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_pwm.svg")


# ── ৯. চার্জ কন্ট্রোলারের টার্মিনাল ও সংযোগের ক্রম ─────────────────────
def d09_scc():
    """EPEVER Tracer4210AN-এর মাপ ও সেটিং ব্যবহার করা হয়েছে।
    সংযোগের ক্রম ম্যানুয়ালের নিজের বাক্য থেকে (Tracer-AN Manual EN
    V2.6, Step 2):  ব্যাটারি → লোড → PV অ্যারে, আর খোলার সময় ঠিক
    উল্টো ক্রমে।  ব্যাটারি আগে, কারণ কন্ট্রোলার ব্যাটারির ভোল্টেজ
    দেখেই বুঝে নেয় সিস্টেম 12 না 24 V।"""
    s = SVG(1240, 800)
    s.title("চার্জ কন্ট্রোলারের টার্মিনাল ও সংযোগের ক্রম", T_TITLE)
    ar = s.arrow_defs(GREEN, "arG", 15)

    BX, BY, BW_, BH_ = 420, 130, 400, 330
    s.rect(BX, BY, BW_, BH_, "#FCFDFE", NAVY, 3.4, 14)
    s.text(BX + BW_ / 2, BY + 54, "MPPT চার্জ কন্ট্রোলার", T_NAME, NAVY,
           700, "middle")
    s.text(BX + BW_ / 2, BY + 90, "Tracer4210AN · 40 A", T_SMALL, GREY,
           700, "middle")
    s.rect(BX + 70, BY + 112, BW_ - 140, 86, "#1B2A38", "#0F1A24", 2.4, 8)
    s.text(BX + BW_ / 2, BY + 150, "14.4 V", T_NODE, "#7FE0A0", 700,
           "middle")
    s.text(BX + BW_ / 2, BY + 182, "8.9 A", T_BODY, "#7FE0A0", 700,
           "middle")

    pairs = [(BX + 66, "PV", GLASS2), (BX + 200, "BAT", BATT),
             (BX + 334, "LOAD", AMBER)]
    for x, tag, col in pairs:
        for dx, sym, c in ((-24, "+", DCP), (24, "-", DCN)):
            s.rect(x + dx - 17, BY + BH_ - 6, 34, 30, "#E7ECF1", col,
                   2.4, 5)
            s.text(x + dx, BY + BH_ + 16, sym, T_BODY, c, 700, "middle")
        s.text(x, BY + BH_ - 16, tag, T_BODY, col, 700, "middle")

    # ধাপের ক্রম
    # ক্রমটি EPEVER Tracer-AN ম্যানুয়ালের নিজের বাক্য:  "Connect the
    # system in the order of battery - load - PV array ... and
    # disconnect the system in the reverse order."
    steps = [("3", "সোলার অ্যারে", GLASS2, pairs[0][0], 120),
             ("1", "ব্যাটারি", BATT, pairs[1][0], 520),
             ("2", "DC লোড", AMBER, pairs[2][0], 920)]
    for n, nm, col, tx, sx in steps:
        s.rect(sx, 560, 200, 120, "#FCFDFE", col, 2.8, 12)
        s.badge(sx + 30, 560 + 30, n, 20, col, "#FFFFFF", 19)
        s.text(sx + 100, 560 + 78, nm, T_BODY, col, 700, "middle")
        s.path(f"M {sx + 100} 556 L {sx + 100} 520 L {tx} 520 L {tx} "
               f"{BY + BH_ + 76}", col, 3, dash="9 7")

    panel(s, 860, 130, 334, 330, "কেন এই ক্রম")
    s.textlines(884, 206, ["ব্যাটারি আগে জুড়লে কন্ট্রোলার",
                           "এর ভোল্টেজ দেখে বোঝে সিস্টেম",
                           "12 V না 24 V।",
                           "",
                           "খোলার ক্রম উল্টো:",
                           "সোলার, তারপর লোড, সবশেষে",
                           "ব্যাটারি।"], T_BODY, INK, 400, lh=1.5)

    y = note_strip(s, 706, "ব্যাটারি, তারপর লোড, সবশেষে সোলার; খোলার "
                           "সময় উল্টো ক্রমে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_scc.svg")


# ── ১০. পিক সান আওয়ার ──────────────────────────────────────────────────
def d10_sunhours():
    """বাংলাদেশে দৈনিক গড় GHI প্রায় 5 kWh/m2 (বিশ্বব্যাংক/গ্লোবাল
    সোলার অ্যাটলাস) — অর্থাৎ 1000 W/m2 তীব্রতায় 5 ঘণ্টার সমান।"""
    s = SVG(1240, 720)
    s.title("পিক সান আওয়ার: দিনের মোট আলো ঘণ্টায় প্রকাশ", T_TITLE)

    X0, Y0, XW, YH = 140, 480, 1000, 340
    px, py = _graph(s, X0, Y0, XW, YH, 14, 1200, 2, 200,
                    "দিনের সময় (ভোর 6টা থেকে ঘণ্টা)", "তীব্রতা W/m2")
    # ঘণ্টাভিত্তিক তীব্রতা — সাইন আকৃতি, শীর্ষ প্রায় 950 W/m2,
    # মোট ক্ষেত্রফল প্রায় 5 kWh/m2
    def g(t):
        if t < 0.6 or t > 13.4:
            return 0.0
        return 950 * math.sin(math.pi * (t - 0.6) / 12.8) ** 1.35
    pts = [(t / 10.0, g(t / 10.0)) for t in range(0, 141)]
    d = ("M " + " L ".join(f"{px(t):.1f} {py(v):.1f}" for t, v in pts) +
         f" L {px(14)} {Y0} L {px(0)} {Y0} Z")
    s.path(d, SUN, 3.4, fill="#FBEFD2")
    s.text(px(7), 300, "দিনের মোট আলো", T_NAME, "#B8860B", 700, "middle")
    s.text(px(7), 340, "প্রায় 5 kWh প্রতি বর্গমিটারে", T_BODY,
           "#B8860B", 700, "middle")

    # সমতুল্য আয়তক্ষেত্র — 1000 W/m2 x 5 ঘণ্টা
    s.rect(px(4.5), py(1000), px(9.5) - px(4.5), Y0 - py(1000),
           "none", DCP, 3.2, 0, dash="12 8")
    s.text(px(7), py(1060), "1000 W/m2 x 5 ঘণ্টা = একই ক্ষেত্রফল",
           T_BODY, DCP, 700, "middle")

    panel(s, 46, 566, 1148, 96, "বাংলাদেশের হিসাব")
    for i, t in enumerate(("বছরের গড় 4.5 থেকে 5 ঘণ্টা",
                           "শীতে কম, গ্রীষ্মে বেশি",
                           "অন-গ্রিডে 4.5, অফ-গ্রিডে 4")):
        chip(s, 250 + i * 370, 630, t, size=T_BODY)

    y = note_strip(s, 686, "নকশার হিসাবে 1 kW অ্যারে দিনে প্রায় 3.6 ইউনিট "
                           "দেয় (4.5 x 0.8), লস বাদ দেওয়ার পরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_sunhours.svg")


# ── ১১. অফ-গ্রিড সিস্টেমের সংযোগ ───────────────────────────────────────
def d11_offgrid_wiring():
    """তারের তালিকা (ছবি আঁকার আগে লেখা — অধ্যায় ১৪-এর শিক্ষা):

        1  অ্যারে +       → DC আইসোলেটর → F1 → কন্ট্রোলার PV +
        2  অ্যারে -       → DC আইসোলেটর → কন্ট্রোলার PV -
        3  কন্ট্রোলার BAT + → F2 → ব্যাটারি +
        4  কন্ট্রোলার BAT - → ব্যাটারি -
        5  ব্যাটারি +      → F3 → ইনভার্টার DC +
        6  ব্যাটারি -      → ইনভার্টার DC -
        7  ইনভার্টার AC L  → ডিবির MCB → লোড
        8  ইনভার্টার AC N  → ডিবির নিউট্রাল বার → লোড
        9  অ্যারের ফ্রেম, কন্ট্রোলার ও ইনভার্টারের বডি → আর্থ বার

    ৫ ও ৬ নম্বর তার ব্যাটারির পোস্টেই T হয়ে বেরোয় — ছবিতে বিন্দু
    দেওয়া আছে।  ইনভার্টারের ধনাত্মক তারটি নিচের পথে (y 412) আর
    ঋণাত্মকটি উপরের পথে (y 400):  উল্টো করলে দুটো কেটে যেত।
    F2 ও F3 আলাদা, কারণ দুটো শাখাকে আলাদাভাবে রক্ষা করতে হয়, আর
    দুটোই ব্যাটারির কাছে — শর্ট হলে সবচেয়ে বড় কারেন্ট ব্যাটারিই দেয়।"""
    s = SVG(1240, 880)
    s.title("অফ-গ্রিড সিস্টেমের সংযোগ", T_TITLE)
    PY_, NY_ = 200, 268

    # ── অ্যারে:  দুটি মডিউল সিরিজে
    pv_module(s, 62, 150, 78, 76, cols=3, rows=3)
    pv_module(s, 62, 252, 78, 76, cols=3, rows=3)
    s.path("M 118 226 L 118 239 L 84 239 L 84 252", DCN, 3.0)
    s.path("M 84 150 L 84 124 L 212 124 L 212 200", DCP, 3.4)
    s.path("M 118 328 L 118 348 L 212 348 L 212 268", DCN, 3.4)
    s.text(108, 380, "সোলার অ্যারে", T_BODY, NAVY, 700, "middle")
    s.text(230, 188, "+", T_BODY, DCP, 700, "start")
    s.text(230, 292, "-", T_BODY, DCN, 700, "start")

    # ── DC আইসোলেটর ও F1
    dcbreak(s, 270, 160, 120, 150, PY_, NY_)
    s.path(f"M 212 {PY_} L 270 {PY_}", DCP, 3.4)
    s.path(f"M 212 {NY_} L 270 {NY_}", DCN, 3.4)
    s.path(f"M 390 {PY_} L 408 {PY_}", DCP, 3.4)
    fuse(s, 430, PY_, 44, 30, "F1")
    s.path(f"M 452 {PY_} L 480 {PY_}", DCP, 3.4)
    s.path(f"M 390 {NY_} L 480 {NY_}", DCN, 3.4)

    # ── চার্জ কন্ট্রোলার
    dev(s, 480, 152, 220, 156, "চার্জ কন্ট্রোলার", "MPPT 40 A", AMBER)
    s.text(496, PY_ - 8, "PV +", T_TINY, DCP, 700, "start")
    s.text(496, NY_ - 8, "PV -", T_TINY, DCN, 700, "start")
    s.text(540, 288, "BAT -", T_TINY, DCN, 700, "middle")
    s.text(660, 288, "BAT +", T_TINY, DCP, 700, "middle")

    # ── ব্যাটারি ব্যাংক;  ঋণাত্মক বাঁয়ে, ধনাত্মক ডানে
    s.path("M 540 308 L 540 430", DCN, 3.4)
    s.path("M 660 308 L 660 330", DCP, 3.4)
    fuse(s, 660, 352, 30, 44, None, vertical=True)
    s.text(684, 358, "F2", T_TINY, NAVY, 700, "start")
    s.path("M 660 374 L 660 430", DCP, 3.4)
    s.rect(500, 430, 200, 120, BATTBG, BATT, 3, 7)
    s.rect(526, 419, 28, 11, BATT, "none", 0, 2)
    s.rect(646, 419, 28, 11, BATT, "none", 0, 2)
    s.text(516, 414, "-", T_NODE, DCN, 700, "end")
    s.text(684, 414, "+", T_NODE, DCP, 700, "start")
    s.text(600, 500, "24 V ব্যাটারি ব্যাংক", T_BODY, BATT, 700, "middle")
    s.text(600, 612, "2 x 12 V সিরিজে", T_SMALL, GREY, 700, "middle")

    # ── ব্যাটারি → ইনভার্টার (T সংযোগ, বিন্দু দেওয়া)
    s.path("M 660 412 L 730 412", DCP, 3.4)
    fuse(s, 752, 412, 44, 30, None)
    s.text(752, 442, "F3", T_TINY, NAVY, 700, "middle")
    s.path("M 774 412 L 840 412 L 840 430", DCP, 3.4)
    s.path("M 540 400 L 900 400 L 900 430", DCN, 3.4)
    node(s, 660, 412, DCP)
    node(s, 540, 400, DCN)

    # ── ইনভার্টার ও ডিবি
    dev(s, 790, 430, 190, 150, "ইনভার্টার", "24 V থেকে 230 V", STEEL)
    s.text(840, 462, "DC +", T_TINY, DCP, 700, "middle")
    s.text(900, 462, "DC -", T_TINY, DCN, 700, "middle")
    s.path("M 980 478 L 1024 478", ACW, 3.4)
    s.path("M 980 534 L 1024 534", ACW, 3.4)
    s.text(1002, 464, "L", T_TINY, ACW, 700, "middle")
    s.text(1002, 562, "N", T_TINY, ACW, 700, "middle")
    dev(s, 1024, 430, 170, 150, "AC ডিবি", "MCB ও RCCB", GREEN)
    s.text(1109, 612, "বাতি · ফ্যান · সকেট", T_SMALL, GREEN, 700, "middle")

    # ── আর্থিং
    s.path("M 130 700 L 1150 700", GREEN, 3.4)
    for x, y0 in ((180, 392), (452, 330), (886, 592), (1109, 628)):
        s.path(f"M {x} {y0} L {x} 700", GREEN, 2.6, dash="9 7")
        node(s, x, 700, GREEN, 5.5)
    s.path("M 480 306 L 452 330", GREEN, 2.6, dash="9 7")
    earth(s, 130, 700)
    s.text(130, 784, "আর্থ ইলেকট্রোড", T_SMALL, GREEN, 700, "middle")

    y = note_strip(s, 806, "F2 ও F3 ব্যাটারির কাছে বসানো, কারণ শর্ট হলে "
                           "সবচেয়ে বেশি কারেন্ট দেয় ব্যাটারি")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_offgrid_wiring.svg")


# ── ১২. অন-গ্রিড (নেট মিটারিং) সংযোগ ───────────────────────────────────
def d12_ongrid_wiring():
    """তারের তালিকা:

        1  স্ট্রিং ১ ও ২ → DC আইসোলেটর → ইনভার্টার DC +/-
        2  ইনভার্টার AC   → সোলার MCB → হাউস ডিবির বাসবার
        3  গ্রিড          → নেট মিটার → মেইন ব্রেকার → হাউস ডিবি
        4  হাউস ডিবি      → লোড
        5  অ্যারের ফ্রেম ও ইনভার্টারের বডি → আর্থ বার

    সোলার ঢোকে **নেট মিটারের লোডের দিকে** (মিটার ও মেইন ব্রেকারের
    পরে) — তাই উদ্বৃত্ত বিদ্যুৎ
    মিটার দিয়েই ফিরে যায় এবং গোনা হয়।  ক্রসিং নেই।"""
    s = SVG(1240, 940)
    s.title("অন-গ্রিড সিস্টেমের সংযোগ (নেট মিটারিং)", T_TITLE)

    # ── এক স্ট্রিং, চার মডিউল সাপের মতো সিরিজে (A-B-D-C)
    for x, y in ((62, 140), (154, 140), (154, 248), (62, 248)):
        pv_module(s, x, y, 82, 86, cols=3, rows=4)
    s.path("M 144 183 L 154 183", DCN, 3.0)          # A - → B +
    s.path("M 195 226 L 195 248", DCN, 3.0)          # B - → D +
    s.path("M 154 291 L 144 291", DCN, 3.0)          # D - → C +
    s.path("M 85 140 L 85 116 L 300 116 L 300 220 L 330 220", DCP, 3.4)
    s.path("M 85 334 L 85 366 L 282 366 L 282 270 L 330 270", DCN, 3.4)
    s.text(146, 398, "এক স্ট্রিং: মডিউলগুলো সিরিজে", T_SMALL, NAVY, 700,
           "middle")
    s.text(104, 108, "+", T_BODY, DCP, 700, "middle")
    s.text(70, 360, "-", T_BODY, DCN, 700, "end")

    # ── DC আইসোলেটর
    dcbreak(s, 330, 176, 130, 132, 220, 270)
    s.path("M 300 200 L 300 220 L 330 220", DCP, 3.4)
    s.path("M 460 220 L 510 220", DCP, 3.4)
    s.path("M 460 270 L 510 270", DCN, 3.4)

    # ── গ্রিড-টাই ইনভার্টার
    dev(s, 510, 160, 220, 170, "গ্রিড-টাই ইনভার্টার",
        "MOD 4000TL3-X · 4000 W", STEEL)  # noqa: নেমপ্লেট ph_growatt
    s.text(504, 208, "PV +", T_TINY, DCP, 700, "end")
    s.text(504, 258, "PV -", T_TINY, DCN, 700, "end")
    s.text(620, 316, "AC আউট", T_TINY, ACW, 700, "middle")

    # ── সোলার MCB
    s.path("M 620 330 L 620 420", ACW, 3.4)
    dev(s, 530, 420, 180, 104, "সোলার MCB", "ও AC আইসোলেটর", ACW)
    s.path("M 620 524 L 620 672 L 740 672", ACW, 3.4)

    # ── গ্রিড → নেট মিটার → মেইন ব্রেকার
    s.path("M 1145 140 L 1145 190", ACW, 3.6)
    s.circle(1145, 128, 14, "#FFFFFF", ACW, 3)
    s.text(1145, 104, "গ্রিড", T_BODY, ACW, 700, "middle")
    dev(s, 950, 190, 200, 140, "নেট মিটার", "আমদানি ও রপ্তানি kWh", NAVY)
    s.path("M 1050 330 L 1050 420", ACW, 3.6)
    dev(s, 960, 420, 180, 104, "মেইন ব্রেকার", None, NAVY)
    s.path("M 1050 524 L 1050 672 L 940 672", ACW, 3.6)

    # ── হাউস ডিবি ও লোড
    dev(s, 740, 610, 200, 124, "হাউস ডিবি", "বাসবার ও MCB", GREEN)
    s.path("M 840 734 L 840 786", ACW, 3.4)
    s.box_auto(840, 786, "বাতি · ফ্যান · ফ্রিজ · এসি", T_BODY,
               fill=GREENBG, stroke=GREEN, tcolor=GREEN, pad_x=24, pad_y=11)

    # ── আর্থিং
    s.path("M 150 560 L 600 560", GREEN, 3.4)
    # ইনভার্টারের বডি-আর্থ বাঁ পাশ দিয়ে নামে, যাতে সোলার MCB-র
    # বাক্সের লেখার উপর দিয়ে না যায়
    s.path("M 200 410 L 200 560", GREEN, 2.6, dash="9 7")
    node(s, 200, 560, GREEN, 5.5)
    s.path("M 510 300 L 490 300 L 490 560", GREEN, 2.6, dash="9 7")
    node(s, 490, 560, GREEN, 5.5)
    earth(s, 150, 560)
    s.text(150, 644, "আর্থ", T_SMALL, GREEN, 700, "middle")

    y = note_strip(s, 850, "সোলার যুক্ত হয় নেট মিটারের লোডের দিকে, তাই "
                           "বাড়তি বিদ্যুৎ মিটার দিয়েই গ্রিডে যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d12_ongrid_wiring.svg")


# ── ১৩. কোণ, দিক ও ছায়া ────────────────────────────────────────────────
def d13_tilt():
    """বাংলাদেশের অক্ষাংশ প্রায় 20.5 থেকে 26.5 ডিগ্রি উত্তর, তাই স্থির
    কাঠামোয় দক্ষিণমুখী ও অক্ষাংশের সমান কাত — মোটা দাগে 23 ডিগ্রি।"""
    s = SVG(1240, 780)
    s.title("কাত, দিক ও সারির ফাঁক", T_TITLE)
    ar = s.arrow_defs(SUN, "arT", 15)

    # ── বাঁ দিক:  পাশ থেকে দেখা
    s.rect(46, 96, 700, 420, "#FCFDFE", LINE, 1.8, 13)
    s.text(396, 138, "পাশ থেকে: কাত", T_NAME, NAVY, 700, "middle")
    GY = 420
    s.path(f"M 96 {GY} L 700 {GY}", GREY, 3.4)
    # প্যানেলের নিচু কিনারা দক্ষিণে (ডানে), উঁচু কিনারা উত্তরে (বাঁয়ে) —
    # তাই মুখ দক্ষিণ-আকাশের দিকে, আর সূর্য ডান দিকে।
    ang = math.radians(23)
    L = 260
    x0, y0 = 488, GY                                  # নিচু কিনারা
    x1, y1 = x0 - L * math.cos(ang), GY - L * math.sin(ang)
    s.path(f"M {x0} {y0} L {x1:.1f} {y1:.1f}", GLASS, 12, cap="butt")
    s.path(f"M {x0} {y0} L {x0 - 130} {y0}", NAVY, 2.4, dash="8 6")
    s.path(f"M {x0 - 86} {y0} A 86 86 0 0 1 "
           f"{x0 - 86 * math.cos(ang):.1f} {y0 - 86 * math.sin(ang):.1f}",
           RED, 2.8)
    s.text(446, 396, "23 ডিগ্রি", T_BODY, RED, 700, "start")
    s.path(f"M {x1:.1f} {y1:.1f} L {x1:.1f} {GY}", GREY, 3)
    sun(s, 596, 196, 30)
    for a, b, c, d in ((556, 232, 420, 392), (536, 214, 372, 372),
                       (516, 196, 324, 352)):
        ray(s, a, b, c, d, marker=ar)
    s.text(150, GY + 38, "উত্তর", T_BODY, NAVY, 700, "middle")
    s.text(660, GY + 38, "দক্ষিণ", T_BODY, NAVY, 700, "middle")
    s.text(396, GY + 76, "ছাদের সমতল", T_SMALL, GREY, 700, "middle")

    # ── ডান দিক:  সারির ফাঁক
    s.rect(776, 96, 418, 420, "#FCFDFE", LINE, 1.8, 13)
    s.text(985, 138, "উপর থেকে: সারির ফাঁক", T_NAME, NAVY, 700, "middle")
    for r in range(2):
        yy = 210 + r * 150
        s.rect(830, yy, 300, 56, GLASS, "#8A98A5", 2.6, 5)
        s.text(980, yy + 36, f"সারি {r + 1}", T_SMALL, "#DCE9F3", 700,
               "middle")
    s.rect(830, 266, 300, 62, "#CBD5DE", "none", 0, 0, opacity=0.8)
    s.text(1036, 306, "শীতের সকালের ছায়া", T_SMALL, GREY, 700, "middle")
    s.path("M 856 266 L 856 360", RED, 2.6)
    s.path("M 848 266 L 864 266", RED, 2.6)
    s.path("M 848 360 L 864 360", RED, 2.6)
    s.text(872, 306, "ফাঁক", T_SMALL, RED, 700, "start")

    panel(s, 46, 548, 1148, 130, "মূল নিয়ম")
    for i, t in enumerate(("দক্ষিণমুখী, কাত প্রায় 23 ডিগ্রি",
                           "সারির ফাঁক শীতের ছায়া মেপে",
                           "সেলে ছায়া পড়লে স্ট্রিংয়ের কারেন্ট কমে")):
        chip(s, 236 + i * 384, 622, t, size=T_BODY)

    y = note_strip(s, 700, "ছাদে ট্যাংক বা প্যারাপেটের ছায়া সকাল-বিকেলে "
                           "কোথায় পড়ে, বসানোর আগে দেখে নিন")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_tilt.svg")


# ── ১৪. ব্যাটারি ব্যাংক ────────────────────────────────────────────────
def d14_battbank():
    s = SVG(1240, 800)
    s.title("ব্যাটারি ব্যাংক: সিরিজ, প্যারালাল ও ব্যবহারযোগ্য ক্ষমতা",
            T_TITLE)

    BW_, BH_ = 130, 92

    def cell(x, y, tag="12 V · 200 AH"):
        s.rect(x, y, BW_, BH_, BATTBG, BATT, 3, 7)
        s.rect(x + 18, y - 10, 22, 10, BATT, "none", 0, 2)
        s.rect(x + BW_ - 40, y - 10, 22, 10, BATT, "none", 0, 2)
        s.text(x + BW_ / 2, y + BH_ / 2 + 7, tag, T_TINY, BATT, 700,
               "middle")
        return x + 29, x + BW_ - 29

    # ── সিরিজ
    s.rect(46, 100, 360, 340, "#FCFDFE", LINE, 1.8, 13)
    s.text(226, 142, "সিরিজ", T_NAME, NAVY, 700, "middle")
    p1, n1 = cell(80, 210)
    p2, n2 = cell(250, 210)
    s.path(f"M {n1} 200 L {n1} 180 L {p2} 180 L {p2} 200", SYM, 3.2)
    s.path(f"M {p1} 200 L {p1} 160", DCP, 3.2)
    s.path(f"M {n2} 200 L {n2} 160", DCN, 3.2)
    s.text(p1, 150, "+", T_BODY, DCP, 700, "middle")
    s.text(n2, 150, "-", T_BODY, DCN, 700, "middle")
    s.text(226, 356, "24 V · 200 AH", T_NAME, BATT, 700, "middle")
    s.text(226, 396, "ভোল্টেজ যোগ, AH একই", T_SMALL, GREY, 700, "middle")

    # ── প্যারালাল
    s.rect(440, 100, 360, 340, "#FCFDFE", LINE, 1.8, 13)
    s.text(620, 142, "প্যারালাল", T_NAME, NAVY, 700, "middle")
    p3, n3 = cell(474, 210)
    p4, n4 = cell(644, 210)
    s.path(f"M {p3} 200 L {p3} 172 L {p4} 172 L {p4} 200", DCP, 3.2)
    s.path(f"M {n3} 200 L {n3} 186 L {n4} 186 L {n4} 200", DCN, 3.2)
    s.text(p3 - 22, 166, "+", T_BODY, DCP, 700, "end")
    s.text(n4 + 22, 180, "-", T_BODY, DCN, 700, "start")
    s.text(620, 356, "12 V · 400 AH", T_NAME, BATT, 700, "middle")
    s.text(620, 396, "AH যোগ, ভোল্টেজ একই", T_SMALL, GREY, 700, "middle")

    # ── DoD
    s.rect(834, 100, 360, 340, "#FCFDFE", LINE, 1.8, 13)
    s.text(1014, 142, "কতটুকু ব্যবহার করা যায়", T_NAME, NAVY, 700,
           "middle")
    BX, BY_, BW2, BH2 = 906, 186, 96, 166
    for i, (frac, col, lab, sub) in enumerate((
            (0.50, "#C8892A", "লিড-অ্যাসিড", "DoD 50 %"),
            (0.80, GREEN, "LiFePO4", "DoD 80 %"))):
        x = BX + i * 160
        s.rect(x, BY_, BW2, BH2, "#EDF1F5", GREY, 2.4, 6)
        s.rect(x, BY_ + BH2 * (1 - frac), BW2, BH2 * frac, col, "none",
               0, 6)
        s.text(x + BW2 / 2, BY_ + BH2 - BH2 * frac / 2 + 8,
               f"{int(frac * 100)} %", T_NAME, "#FFFFFF", 700, "middle")
        s.text(x + BW2 / 2, BY_ + BH2 + 32, lab, T_BODY, col, 700,
               "middle")
        s.text(x + BW2 / 2, BY_ + BH2 + 62, sub, T_SMALL, GREY, 700,
               "middle")
    s.text(1014, 172, "200 AH ব্যাটারির", T_SMALL, GREY, 700, "middle")

    panel(s, 46, 472, 1148, 170, "প্যারালালে জোড়ার আগে")
    for i, t in enumerate(("একই মডেল, একই AH",
                           "একই বয়স ও একই চার্জ অবস্থা",
                           "সমান দৈর্ঘ্যের তার")):
        chip(s, 236 + i * 384, 548, t, size=T_BODY)
    s.text(620, 612, "দুটি ব্যাটারির অবস্থা আলাদা হলে একটি অন্যটিকে "
                     "অনবরত চার্জ করে, আর দুটিরই ক্ষতি হয়", T_SMALL, GREY,
           700, "middle")

    y = note_strip(s, 662, "ব্যাকআপের হিসাবে AH-এর পুরোটা ধরা যায় না; "
                           "DoD ও ইনভার্টারের দক্ষতা দিয়ে গুণ করতে হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d14_battbank.svg")


ALL = [d01_idea, d02_cell, d03_hierarchy, d04_iv, d05_effects,
       d06_series, d07_systems, d08_pwm, d09_scc, d10_sunhours,
       d11_offgrid_wiring, d12_ongrid_wiring, d13_tilt, d14_battbank]

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
