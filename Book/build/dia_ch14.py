# -*- coding: utf-8 -*-
"""অধ্যায় ১৪ — স্টার-ডেল্টা স্টার্টার : ডায়াগ্রাম।

সহায়কগুলো অধ্যায় ৮–১২ থেকে আমদানি করা (CLAUDE.md-র নিয়ম) —
`panel`, `note_strip`, `node`, `chip`, `callout`, `coil_sym` অধ্যায় ৮;
`fuse`, `lamp`, `thermal_sym`, `_pb`, `_nc`, `_no` অধ্যায় ৯;
`timer_coil`, `dnc`, `dno`, `timing`, `dim_arrow` অধ্যায় ১০;
`earth` অধ্যায় ১১;  `motor_sym`, `pole_set`, `km_box`, `chev`,
`join_bus` অধ্যায় ১২।  `photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে
রাখে, তাই `_use_ch14_images()` দিয়ে বদলে নেওয়া হয়েছে।

**পাওয়ার সার্কিটের টপোলজি (d06, d07, d08)** — মোটরের ছয় প্রান্ত দুই
সারিতে, ঠিক যেভাবে টার্মিনাল বাক্সে বসে (অধ্যায় ৭-এর ৭.১০-এর ছবি):

    উপরের সারি :  U1   V1   W1     ← KM1 → F2 → এখানে
    নিচের সারি  :  W2   U2   V2     ← KM3 এখানে,  KM2 এই তিনটিকে জোড়ে

একই খাড়া কলামের দুই প্রান্ত ডেল্টার একই কোণ — U1+W2 = L1, V1+U2 = L2,
W1+V2 = L3।  তাই টার্মিনাল বাক্সের পিতলের পাত যা করত, এখানে KM3-এর
কন্টাক্ট সেটাই করে।

**ঘোরার দিক স্টার আর ডেল্টায় এক — যাচাই করা** (CLAUDE.md-র "এক ফেজ
ধরে হেঁটে দেখো" নিয়ম):

    স্টারে   —  U কয়েল  U1(L1) → U2(নিউট্রাল পয়েন্ট)  =  V(L1-N)
    ডেল্টায় —  U কয়েল  U1(L1) → U2(L2)           =  V(L1-L2)

তিন কয়েলেই একই রকম:  V কয়েল V(L2-N) → V(L2-L3), W কয়েল V(L3-N) →
V(L3-L1)।  লাইন ভোল্টেজ ফেজ ভোল্টেজের চেয়ে ৩০ ডিগ্রি আগে থাকে —
**তিনটিই সমান ৩০ ডিগ্রি**, তাই ক্রম বদলায় না, ঘোরার দিকও বদলায় না।
KM3-এর দুটি তার উল্টে বসালে ডেল্টার ক্রম উল্টে যায়, আর বদলের মুহূর্তে
চলন্ত মোটরে প্লাগিং হয় — d09-এর বিপদ।

**ক্রসিং কোথায়, আর কেন এড়ানো যায়নি** — সরবরাহের তিন রেল নেস্টেড
(L1 সবচেয়ে চওড়া, L3 সবচেয়ে সরু), তাই KM1 ও KM3-এর দিকে নামা কোনো
তার আরেকটাকে কাটে না।  KM3-এর আউটপুট তিনটিও ক্রম উল্টে বসে বলে
নেস্টেড — ওখানেও ক্রসিং নেই।  কিন্তু নিচের সারির তিনটি নোডে **তিনটি
করে তার** এসে মেলে (মোটর, KM2, KM3);  এই আকৃতি সমতলে আঁকা যায় না —
তিনটি ক্রসিং হবেই।  তাই সেখানে `join_bus`-এর মতো **আধা-বৃত্তের লাফ**:
ভরাট বিন্দু = জোড়া, লাফ = কেবল পেরিয়ে যাওয়া।

**কন্ট্রোল সার্কিটের টপোলজি (`_ladder14`)** — অধ্যায় ৯-এর `_ladder()`
আর অধ্যায় ১০-এর টাইমার একসঙ্গে:

    L → F1 → F2 95-96 → STOP → [START ‖ KM1 13-14] → P
    P → KM1 কয়েল → N
    P → KT কয়েল (2-7) → N
    P → KT 8-5 (বিলম্বে খোলে) → KM3 21-22 → KM2 কয়েল → N     [স্টার]
    P → KT 8-6 (বিলম্বে বন্ধ হয়) → KM2 21-22 → KM3 কয়েল → N   [ডেল্টা]

দুই দিকের NC 21-22 কয়েলের ঠিক আগে — অধ্যায় ১২-এর ১২.৪.২-এর একই
মিরর কন্টাক্টের যুক্তি।  AH3-এর 8-5/8-6 চেঞ্জওভারে ফাঁক প্রায় নেই,
তাই **ফাঁকটা আসলে ওই দুটো NC থেকেই আসে** — এটাই এই অধ্যায়ের সবচেয়ে
জরুরি কথা, আর d13-এর উৎসর্গীকৃত স্টার-ডেল্টা টাইমারের ৫০ ms স্থির
ট্রানজিশন তারই কারখানা-সংস্করণ।

সংখ্যাগুলো যাচাই করা (মূল নথি থেকে, মুখস্থ থেকে নয়) — ABB-র
স্টার্টিং কম্বিনেশন ক্যাটালগ 1SBC009500R1002 আর ABB CT-SDS.23-এর
ডেটাশিট 2CDC111128D0201;  পূর্ণ উদ্ধৃতি `ch14.py`-র ডকস্ট্রিংয়ে।

**d05 ও d15 `poly()` দিয়ে আঁকা অংশ আছে** — qc ওটার ভেতর দেখে না,
চোখে দেখে নিতে হবে।

কালপুরুষের সীমা আগের অধ্যায়গুলোর মতোই — টার্মিনাল, রেটিং, মডেল
নম্বর ল্যাটিন অঙ্কে;  `÷`, `Ω`, `°`, `√` ছবিতে নেই।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, chip, callout, coil_sym,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, LIVE, NEUT, DEAD, PLATE, CU, IRON,
                      IRON_D, SILVER, BOXG)
from dia_ch09 import (fuse, lamp, thermal_sym, _pb, _nc, _no,
                      nc_tip, no_tip)
from dia_ch10 import timer_coil, dnc, dno, timing, dim_arrow, TIMEC, TIMEBG
from dia_ch11 import earth
from dia_ch12 import motor_sym, pole_set, km_box, chev, PH1, PH2, PH3, PHC
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch14")
IMG = os.path.join(HERE, "assets", "ch14")

STARC = "#1D6FA8"          # স্টার অবস্থার রং
DELC = "#B5541F"           # ডেল্টা অবস্থার রং
MECH = "#4A5560"           # যান্ত্রিক অংশ


def _use_ch14_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch14_images()
    return C8.photo_callouts(*a, **k)


# ── ছোট সহায়ক ───────────────────────────────────────────────────────────
def hop_line(s, x0, x1, y, hops, col=SYM, sw=3.6, r=10):
    """x0 → x1 পর্যন্ত রেখা;  `hops`-এর প্রতিটি x-এ আধা-বৃত্তের লাফ।

    অধ্যায় ১২-এর `join_bus()`-এর একই নিয়ম — লাফ মানে কেবল পেরিয়ে
    যাওয়া, জোড়া নয়;  জোড়ার জায়গায় ভরাট বিন্দু বসে।"""
    step = 1 if x1 > x0 else -1
    inside = sorted([h for h in hops if min(x0, x1) + r < h < max(x0, x1) - r],
                    reverse=step < 0)
    d = f"M {x0} {y}"
    for h in inside:
        d += (f" L {h - step * r} {y} "
              f"A {r} {r} 0 0 {1 if step > 0 else 0} {h + step * r} {y}")
    d += f" L {x1} {y}"
    s.path(d, col, sw)


def wind_sym(s, x, ytop, ybot, col=SYM, sw=3.4, turns=4):
    """কয়েলের প্রতীক — খাড়া, IEC-র অর্ধবৃত্তের সারি।"""
    h = (ybot - ytop) / turns
    d = f"M {x} {ytop}"
    for i in range(turns):
        y0 = ytop + i * h
        d += f" A {h / 2} {h / 2} 0 0 1 {x} {y0 + h}"
    s.path(d, col, sw)


def term(s, x, y, tag, w=44):
    """মোটরের টার্মিনাল — ছোট চৌকো, ভেতরে নাম।  ভরাট বিন্দু বসে না,
    নইলে নামের উপর পড়ে (qc ধরেছিল)।"""
    s.rect(x - w / 2, y - 16, w, 32, "#D7E2EC", STEEL, 2, 4)
    s.text(x, y + 8, tag, T_TINY, NAVY, 700, "middle")


def star_point(s, x, y, col=SYM):
    """নিউট্রাল পয়েন্টের চিহ্ন।"""
    node(s, x, y, col, 9)
    for a in (90, 210, 330):
        s.path(f"M {x} {y} L {x + 26 * math.cos(math.radians(a))} "
               f"{y + 26 * math.sin(math.radians(a))}", col, 3)


def ratio_card(s, x, y, w, h, head, big, sub, col):
    s.rect(x, y, w, h, "#FCFDFE", col, 2.6, 12)
    s.box_auto(x + w / 2, y + 14, head, T_BODY, fill=col, stroke=col,
               tcolor="#FFFFFF", pad_x=18, pad_y=8)
    s.text(x + w / 2, y + h * 0.62, big, T_TITLE, col, 700, "middle")
    s.text(x + w / 2, y + h - 30, sub, T_SMALL, GREY, 400, "middle")


# ── ১. সমস্যাটা কোথায় ───────────────────────────────────────────────────
def d01_idea():
    s = SVG(1240, 660)
    s.title("বড় মোটর সরাসরি চালু করলে যা ঘটে", T_TITLE)

    cards = [("লাইনের ভোল্টেজ পড়ে যায়",
              "একই ট্রান্সফরমারের অন্য সব বাতি\nএক পলকের জন্য নিভু নিভু",
              STEEL),
             ("তার ও ব্রেকার বড় লাগে",
              "স্টার্টিং কারেন্ট ৬–৭ গুণ,\nব্রেকার বারবার ট্রিপ করে", AMBER),
             ("যন্ত্রে ঝাঁকুনি লাগে",
              "বেল্ট পিছলায়, কাপলিং খোলে,\nগিয়ারবক্স ক্ষয়ে যায়", RED)]
    W, GAP, X0, Y, H = 366, 26, 46, 132, 300
    for i, (name, what, col) in enumerate(cards):
        x = X0 + i * (W + GAP)
        s.rect(x, Y, W, H, "#FCFDFE", col, 2.4, 13)
        s.box_auto(x + W / 2, Y + 16, name, T_BODY, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=16, pad_y=9)
        for k, ln in enumerate(what.split("\n")):
            s.text(x + W / 2, Y + 150 + k * 40, ln, T_SMALL, NAVY, 400,
                   "middle")
        s.text(x + W / 2, Y + 254, ("৩", "২", "১")[2 - i], T_TITLE,
               "#E7EDF3", 700, "middle")

    s.text(620, 500, "সমাধান — চালুর সময়টুকুতে কয়েলে কম ভোল্টেজ দাও, "
                     "গতি উঠলে পুরো ভোল্টেজ", T_NAME, NAVY, 700, "middle")
    s.text(620, 542, "স্টার-ডেল্টা স্টার্টার ঠিক এই কাজটাই করে — "
                     "মোটরের সংযোগ বদলে", T_BODY, GREY, 400, "middle")

    y = note_strip(s, 578, "চালুর সময় কারেন্ট কমাতে হলে টর্কও কমবে — "
                           "এই দুটো একসঙ্গে চলে, আলাদা করা যায় না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. এক কয়েলে কত ভোল্ট ────────────────────────────────────────────────
def limb(s, x0, y0, x1, y1, tag, col=SYM, sw=3.4, gap=26):
    """কয়েলের ঘর — রেখার ঠিক মাঝে ছোট বাক্স, ভেতরে কয়েলের নাম।

    রেখাটা বাক্সের জায়গায় **ভেঙে** আঁকা হয়;  ভেতর দিয়ে টেনে দিলে
    qc ওটাকে "line crosses" ধরে, আর ছাপাতেও লেখার গায়ে দাগ পড়ে।"""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    d = math.hypot(x1 - x0, y1 - y0) or 1
    ux, uy = (x1 - x0) / d, (y1 - y0) / d
    s.path(f"M {x0} {y0} L {mx - ux * gap} {my - uy * gap}", col, sw)
    s.path(f"M {mx + ux * gap} {my + uy * gap} L {x1} {y1}", col, sw)
    s.rect(mx - 21, my - 17, 42, 34, "#FFFFFF", col, 2.4, 5)
    s.text(mx, my + 8, tag, T_TINY, col, 700, "middle")


def d02_voltage():
    s = SVG(1240, 740)
    s.title("একই কয়েল — ডেল্টায় ৪০০ ভোল্ট, স্টারে ২৩১ ভোল্ট", T_TITLE)

    for k, (ttl, col, vv, note) in enumerate(
            [("স্টার সংযোগ", STARC, "231 V", "লাইন ভোল্টেজের 0.58 গুণ"),
             ("ডেল্টা সংযোগ", DELC, "400 V", "পুরো লাইন ভোল্টেজ")]):
        X0 = 46 + k * 600
        panel(s, X0, 100, 570, 420, ttl, col)
        cx, cy = X0 + 285, 352

        if k == 0:                      # স্টার — তিন কয়েল এক বিন্দুতে
            R, RL, RT = 112, 138, 168
            for i, ang in enumerate((270, 30, 150)):
                ca = math.cos(math.radians(ang))
                sa = math.sin(math.radians(ang))
                limb(s, cx, cy, cx + R * ca, cy + R * sa, ("U", "V", "W")[i],
                     SYM, gap=22)
                s.path(f"M {cx + R * ca} {cy + R * sa} "
                       f"L {cx + RL * ca} {cy + RL * sa}", PHC[i], 3.6)
                node(s, cx + RL * ca, cy + RL * sa, PHC[i])
                s.text(cx + RT * ca, cy + RT * sa + 8, ("L1", "L2", "L3")[i],
                       T_BODY, PHC[i], 700, "middle")
            star_point(s, cx, cy, SYM)
            s.text(cx, cy + 58, "নিউট্রাল পয়েন্ট", T_SMALL, GREY, 400, "middle")
        else:                           # ডেল্টা — তিন কয়েল ত্রিভুজে
            pts = [(cx, cy - 118), (cx + 128, cy + 86), (cx - 128, cy + 86)]
            for i in range(3):
                p0, p1 = pts[i], pts[(i + 1) % 3]
                limb(s, p0[0], p0[1], p1[0], p1[1], ("U", "V", "W")[i], SYM)
            for i, (px, py) in enumerate(pts):
                node(s, px, py, PHC[i])
                dx, dy = (0, -42) if i == 0 else ((50, 34) if i == 1
                                                  else (-50, 34))
                s.path(f"M {px} {py} L {px + dx} {py + dy}", PHC[i], 3.6)
                s.text(px + dx * 1.5, py + dy * 1.5 + 8,
                       ("L1", "L2", "L3")[i], T_BODY, PHC[i], 700, "middle")

        s.box_auto(X0 + 285, 552, f"এক কয়েলে  {vv}", T_NAME, fill="#FFFFFF",
                   stroke=col, tcolor=col, pad_x=26, pad_y=11)
        s.text(X0 + 285, 634, note, T_SMALL, GREY, 400, "middle")

    y = note_strip(s, 666, "৪০০ ভোল্টে কয়েল পায় 400 / 1.73 = 231 V — "
                           "এই সংখ্যা থেকেই বাকি সব হিসাব আসে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_voltage.svg")


# ── ৩. এক-তৃতীয়াংশের হিসাব ──────────────────────────────────────────────
def d03_ratio():
    s = SVG(1240, 760)
    s.title("কারেন্ট আর টর্ক — দুটোই এক-তৃতীয়াংশে নামে", T_TITLE)
    ar = s.arrow_defs(STEEL, "arR", 14)

    steps = [("কয়েলের ভোল্টেজ", "0.58 গুণ", "400 → 231 V", STARC),
             ("কয়েলের কারেন্ট", "0.58 গুণ", "ভোল্টেজের সঙ্গে সঙ্গে", STEEL),
             ("লাইন কারেন্ট", "0.33 গুণ", "স্টারে লাইন = কয়েল", AMBER),
             ("টর্ক", "0.33 গুণ", "ভোল্টেজের বর্গের সঙ্গে", RED)]
    W, GAP, X0, Y, H = 272, 34, 46, 128, 214
    for i, (a, b, c, col) in enumerate(steps):
        x = X0 + i * (W + GAP)
        ratio_card(s, x, Y, W, H, a, b, c, col)
        if i < 3:
            s.path(f"M {x + W + 6} {Y + H / 2} L {x + W + GAP - 6} "
                   f"{Y + H / 2}", STEEL, 3.4, marker=ar)

    s.text(620, 414, "কেন লাইন কারেন্ট আরও কমে", T_NAME, NAVY, 700,
           "middle")
    s.text(620, 456, "ডেল্টায় লাইন কারেন্ট কয়েলের কারেন্টের 1.73 গুণ, "
                     "স্টারে ঠিক সমান।", T_BODY, GREY, 400, "middle")
    s.text(620, 494, "তাই কয়েলে 0.58 গুণ হলেও লাইনে দাঁড়ায় "
                     "0.58 / 1.73 = 0.33 গুণ।", T_BODY, GREY, 400, "middle")

    for k, (ttl, val, col) in enumerate(
            [("সরাসরি (DOL) চালু", "6 × Ie", RED),
             ("স্টারে চালু", "2 × Ie", STARC)]):
        x = 300 + k * 400
        s.rect(x - 150, 540, 300, 96, "#FCFDFE", col, 2.6, 11)
        s.text(x, 576, ttl, T_SMALL, GREY, 400, "middle")
        s.text(x, 616, val, T_NAME, col, 700, "middle")

    y = note_strip(s, 664, "৬ গুণের বদলে ২ গুণ — কিন্তু টর্কও এক-"
                           "তৃতীয়াংশ, তাই ভারী লোড নিয়ে চালু করা যাবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_ratio.svg")


# ── ৪. কারেন্ট ও টর্কের লেখচিত্র ────────────────────────────────────────
def _axes(s, x0, y0, w, h, xlab, ylab, ymax):
    s.path(f"M {x0} {y0 - h} L {x0} {y0} L {x0 + w} {y0}", NAVY, 2.6)
    for i in range(1, 6):
        xx = x0 + w * i / 5
        s.path(f"M {xx} {y0} L {xx} {y0 + 8}", NAVY, 2)
        s.text(xx, y0 + 32, str(i * 20), T_TINY, GREY, 400, "middle")
    for v in range(1, ymax + 1):
        yy = y0 - h * v / ymax
        s.path(f"M {x0 - 8} {yy} L {x0 + w} {yy}", "#E7EDF3", 1.4)
        s.text(x0 - 16, yy + 7, str(v), T_TINY, GREY, 400, "end")
    s.text(x0 + w / 2, y0 + 66, xlab, T_SMALL, NAVY, 700, "middle")
    s.text(x0 - 16, y0 - h - 18, ylab, T_SMALL, NAVY, 700, "middle")


def d04_curves():
    s = SVG(1240, 820)
    s.title("গতি বাড়ার সঙ্গে কারেন্ট ও টর্ক", T_TITLE)

    X0, W, H = 130, 470, 380
    for k in range(2):
        x0 = X0 + k * 560
        y0 = 516
        ymax = 7 if k == 0 else 3
        _axes(s, x0, y0, W, H, "গতি (শতকরা)",
              "I / Ie" if k == 0 else "T / Tn", ymax)
        px = lambda p: x0 + W * p / 100
        py = lambda v: y0 - H * v / ymax

        if k == 0:                       # কারেন্ট
            dol = [(0, 6.2), (20, 6.1), (40, 5.9), (60, 5.5), (75, 4.9),
                   (85, 4.0), (92, 2.9), (97, 1.6), (100, 1.0)]
            sta = [(p, v / 3) for p, v in dol]
        else:                            # টর্ক
            dol = [(0, 1.9), (20, 1.7), (40, 1.7), (60, 1.9), (75, 2.4),
                   (85, 2.6), (92, 2.2), (97, 1.2), (100, 0.0)]
            sta = [(p, v / 3) for p, v in dol]
        for pts, col, lab in ((dol, DELC, "ডেল্টা"), (sta, STARC, "স্টার")):
            d = "M " + " L ".join(f"{px(p)} {py(v)}" for p, v in pts)
            s.path(d, col, 3.8)
            s.text(px(pts[0][0]) + 16, py(pts[0][1]) - 16, lab, T_SMALL,
                   col, 700, "start")
        if k == 1:                       # লোডের টর্ক
            ld = [(0, 0.25), (40, 0.32), (70, 0.45), (100, 0.62)]
            s.path("M " + " L ".join(f"{px(p)} {py(v)}" for p, v in ld),
                   GREY, 3, dash="9 6")
            s.text(px(22), py(0.30) - 42, "লোডের টর্ক", T_SMALL, GREY, 700,
                   "middle")
        s.path(f"M {px(80)} {y0} L {px(80)} {y0 - H}", GREEN, 2.4,
               dash="8 6")
        s.text(px(80) + 10, y0 - H + 24, "৮০%", T_SMALL, GREEN, 700,
               "start")

    s.text(620, 644, "ABB-র ক্যাটালগের নিয়ম — অন্তত ৮০ শতাংশ গতি না উঠলে "
                     "ডেল্টায় ফেলা যাবে না", T_BODY, NAVY, 700, "middle")
    s.text(620, 682, "তার আগে ফেললে কারেন্ট আবার লাফিয়ে ওঠে, "
                     "আর স্টারে চালানোর সুবিধাটাই থাকে না", T_SMALL, GREY,
           400, "middle")

    y = note_strip(s, 714, "স্টারের টর্ক সবসময় লোডের টর্কের উপরে থাকতে "
                           "হবে — না থাকলে মোটর গতি তুলতেই পারবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_curves.svg")


# ── ৫. ছয় প্রান্ত ও ডেল্টার তিন কোণ ─────────────────────────────────────
def d05_terminals():
    s = SVG(1240, 810)
    s.title("ছয় প্রান্ত — কোন দুটি এক কোণে", T_TITLE)

    # ── বাঁয়ে:  টার্মিনাল ব্লক, পিতলের পাত বসানো ──────────────────────
    XS = [300, 430, 560]
    TOP, BOT = 244, 394
    s.rect(206, 210, 458, 218, "#FCFDFE", STEEL, 2.4, 12)
    for i, x in enumerate(XS):
        s.rect(x - 22, TOP + 16, 44, BOT - TOP - 32, "#F3D9A4", "#B98B2E",
               2.4, 4)
        term(s, x, TOP, ("U1", "V1", "W1")[i])
        term(s, x, BOT, ("W2", "U2", "V2")[i])
        s.path(f"M {x} {TOP - 16} L {x} 168", PHC[i], 3.6)
        node(s, x, 168, PHC[i])
        s.text(x, 150, ("L1", "L2", "L3")[i], T_BODY, PHC[i], 700, "middle")
    s.text(435, 468, "মোটরের টার্মিনাল ব্লক — পিতলের পাত বসানো",
           T_BODY, NAVY, 700, "middle")
    s.text(435, 504, "অধ্যায় ৭-এর ৭.১০-এর ব্লক, উল্টো করে ধরা", T_SMALL, GREY,
           400, "middle")

    # ── ডানে:  ডেল্টার ত্রিভুজ, কোণে দুই প্রান্তের নাম ─────────────────
    panel(s, 706, 130, 488, 346, "ডেল্টার তিন কোণ", DELC)
    cx, cy = 950, 306
    pts = [(cx, cy - 80), (cx + 108, cy + 60), (cx - 108, cy + 60)]
    for i in range(3):
        p0, p1 = pts[i], pts[(i + 1) % 3]
        limb(s, p0[0], p0[1], p1[0], p1[1], ("U", "V", "W")[i], SYM, gap=24)
    tags = [(34, -6, "start"), (34, 38, "start"), (-34, 38, "end")]
    for i, ((px, py), (dx, dy, an)) in enumerate(zip(pts, tags)):
        node(s, px, py, PHC[i], 8)
        s.text(px + dx, py + dy, ("L1", "L2", "L3")[i], T_BODY, PHC[i],
               700, an)
        s.text(px + dx, py + dy + 30, ("U1 + W2", "V1 + U2", "W1 + V2")[i],
               T_SMALL, NAVY, 700, an)

    # ── নিচে:  তিন কোণের সারণি ─────────────────────────────────────────
    s.rect(46, 552, 1148, 152, "#F3F7FB", STEEL, 2, 12)
    heads = ["ডেল্টার কোণ", "উপরের প্রান্ত", "নিচের প্রান্ত", "যে ফেজে যায়"]
    cols = [190, 470, 750, 1030]
    for ccx, h in zip(cols, heads):
        s.text(ccx, 592, h, T_SMALL, NAVY, 700, "middle")
    body = [("প্রথম", "U1", "W2", "L1", PH1),
            ("দ্বিতীয়", "V1", "U2", "L2", PH2),
            ("তৃতীয়", "W1", "V2", "L3", PH3)]
    for i, (a1, b1, c1, d1, col) in enumerate(body):
        yy = 634 + i * 32
        for ccx, t in zip(cols, (a1, b1, c1, d1)):
            s.text(ccx, yy, t, T_SMALL, col if ccx == 1030 else NAVY,
                   700 if ccx == 1030 else 400, "middle")

    y = note_strip(s, 722, "একই কলামের উপর ও নিচের প্রান্ত ডেল্টার একই "
                           "কোণ — স্টার্টারে এই পাতের কাজ KM3 করে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_terminals.svg")


# ── ৬-৮. পাওয়ার সার্কিট ─────────────────────────────────────────────────
# রেল ও কলামের x — d06/d07/d08/d09 সবাই এখান থেকে নেয়, তাই ছবিগুলো
# কখনো পরস্পরবিরোধী হতে পারে না (অধ্যায় ১২-এর শিক্ষা)।
RY = (236, 268, 300)              # L1, L2, L3 — তিন রেলের উচ্চতা
CX = (380, 480, 580)              # মোটরের তিন কলাম
BX = (820, 920, 1020)             # KM3-এর তিন পোল — বাঁ থেকে L3, L2, L1
KT, KB = 360, 452                 # কন্টাক্টরের উপর ও নিচ
FY0, FY1 = 484, 564               # ওভারলোড রিলের বাক্স
MT, MB = 612, 740                 # মোটরের বাক্স
TR = (636, 716)                   # উপরের ও নিচের সারির টার্মিনাল
DY = (780, 812, 844)              # KM3 → কলাম ১, ২, ৩-এর রেল
SY = (876, 902, 928)              # কলাম ১, ২, ৩ → KM2-এর রেল
SX = (120, 200, 280)              # KM2-এর তিন পোল
ST, SB = 958, 1036                # KM2-এর উপর ও নিচ


def _power14(s, state):
    """state = "off" / "star" / "delta"।  সবটুকু এক জায়গা থেকে আঁকা হয়
    বলে তিনটি ছবি কখনো আলাদা কথা বলতে পারে না।"""
    star, delta = state == "star", state == "delta"
    on = star or delta
    live = lambda ok: (PHC if ok else (DEAD, DEAD, DEAD))

    # ── তিন রেল ও Q1 ──────────────────────────────────────────────────
    for i, yy in enumerate(RY):
        s.path(f"M 118 {yy} L 1080 {yy}", PHC[i], 3.6)
        s.text(96, yy + 8, ("L1", "L2", "L3")[i], T_BODY, PHC[i], 700, "end")
    s.rect(168, RY[0] - 40, 128, RY[2] - RY[0] + 80, PLATE, NAVY, 2.6, 8)
    for yy in RY:
        s.path(f"M 232 {yy - 22} L 232 {yy + 22}", NAVY, 3.2)
    s.path(f"M 232 {RY[0]} L 232 {RY[2]}", NAVY, 2, dash="6 5")
    s.text(232, RY[0] - 54, "Q1 — MCCB", T_SMALL, NAVY, 700, "middle")

    # ── KM1 (লাইন কন্টাক্টর) ও তার খাওয়ানো ─────────────────────────────
    for i, x in enumerate(CX):
        s.path(f"M {x} {RY[i]} L {x} {KT}", PHC[i], 3.6)
        node(s, x, RY[i], PHC[i])
    km_box(s, CX[0] - 46, KT - 6, CX[2] - CX[0] + 92, KB - KT + 12, "KM1",
           GREEN, "লাইন")
    pole_set(s, CX[0], CX[1] - CX[0], KT, KB, on, SYM)

    # ── F2 — ওভারলোড রিলে, ডেল্টার শাখায় ───────────────────────────────
    s.rect(CX[0] - 52, FY0, CX[2] - CX[0] + 104, FY1 - FY0, "#FFFBF2",
           AMBER, 2.4, 8)
    for i, x in enumerate(CX):
        s.path(f"M {x} {KB} L {x} {FY0 + 6}", live(on)[i], 3.6)
        thermal_sym(s, x, (FY0 + FY1) / 2, 34, 48, SYM, 3.2)
        s.path(f"M {x} {FY1 - 6} L {x} {TR[0] - 16}", live(on)[i], 3.6)
    s.text(CX[2] + 74, FY0 + 34, "F2 — ওভারলোড রিলে", T_SMALL, AMBER, 700,
           "start")
    s.text(CX[2] + 74, FY0 + 62, "সেটিং  0.58 × In", T_SMALL, GREY, 400,
           "start")

    # ── মোটর ──────────────────────────────────────────────────────────
    s.rect(CX[0] - 80, MT, CX[2] - CX[0] + 160, MB - MT, "#FCFDFE", SYM,
           2.6, 10)
    for i, x in enumerate(CX):
        term(s, x, TR[0], ("U1", "V1", "W1")[i])
        term(s, x, TR[1], ("W2", "U2", "V2")[i])
    s.text(CX[1], (TR[0] + TR[1]) / 2 + 8, "তিন কয়েল · ছয় প্রান্ত", T_SMALL,
           GREY, 400, "middle")
    motor_sym(s, CX[2] + 158, (MT + MB) / 2, 42)
    s.path(f"M {CX[2] + 80} {(MT + MB) / 2} L {CX[2] + 116} "
           f"{(MT + MB) / 2}", SYM, 3)
    earth(s, CX[2] + 158, MB - 6)

    # ── KM3 (ডেল্টা কন্টাক্টর) — পোল বাঁ থেকে L3, L2, L1 ────────────────
    for k, x in enumerate(BX):
        i = 2 - k                                   # 820←L3, 920←L2, 1020←L1
        s.path(f"M {x} {RY[i]} L {x} {KT}", PHC[i], 3.6)
        node(s, x, RY[i], PHC[i])
    km_box(s, BX[0] - 46, KT - 6, BX[2] - BX[0] + 92, KB - KT + 12, "KM3",
           DELC, "ডেল্টা")
    pole_set(s, BX[0], BX[1] - BX[0], KT, KB, delta, SYM)

    # ── KM3-এর আউটপুট → নিচের সারি।  ক্রম উল্টে বসে বলে নিজেদের মধ্যে
    # কোনো ক্রসিং নেই;  লাফ কেবল কলামের খাড়া তারের উপর দিয়ে ──────────
    dcol = live(delta)
    for k in range(3):
        xb, xc, yy = BX[k], CX[2 - k], DY[k]
        s.path(f"M {xb} {KB} L {xb} {yy}", dcol[2 - k], 3.6)
        hop_line(s, xb, xc, yy, [c for c in CX if c != xc], dcol[2 - k], 3.6)
        node(s, xc, yy, dcol[2 - k])

    # ── কলামের খাড়া তার:  নিচের সারি → KM3-এর রেল → KM2-এর রেল ────────
    for i, x in enumerate(CX):
        col = PHC[i] if delta else (SYM if star else DEAD)
        s.path(f"M {x} {TR[1] + 16} L {x} {SY[i]}", col, 3.6)

    # ── KM2 (স্টার কন্টাক্টর) ───────────────────────────────────────────
    scol = SYM if star else DEAD
    for i in range(3):
        s.path(f"M {CX[i]} {SY[i]} L {SX[i]} {SY[i]}", scol, 3.6)
        node(s, CX[i], SY[i], scol)
        s.path(f"M {SX[i]} {SY[i]} L {SX[i]} {ST}", scol, 3.6)
    km_box(s, SX[0] - 46, ST - 6, SX[2] - SX[0] + 92, SB - ST + 12, "KM2",
           STARC, "স্টার")
    pole_set(s, SX[0], SX[1] - SX[0], ST, SB, star, SYM)
    s.path(f"M {SX[0]} {SB} L {SX[2]} {SB}", scol, 3.6)
    for x in SX:
        node(s, x, SB, scol)
    # নিউট্রাল পয়েন্ট বারের নিচে, টার্মিনাল-নম্বরের নাগালের বাইরে
    s.path(f"M {SX[1]} {SB} L {SX[1]} {SB + 46}", scol, 3.6)
    star_point(s, SX[1], SB + 46, scol)
    s.text(SX[1] + 92, SB + 54, "নিউট্রাল পয়েন্ট", T_SMALL,
           STARC if star else GREY, 700, "start")
    return SB + 92


def d06_power():
    s = SVG(1240, 1180)
    s.title("স্টার-ডেল্টা স্টার্টারের পাওয়ার সার্কিট", T_TITLE)
    yb = _power14(s, "off")
    s.textlines(700, SY[2] + 34, ["তিনটি আধা-বৃত্তের লাফ — নিচের সারির",
                                  "তিন নোডে তিনটি করে তার মেলে বলে",
                                  "সমতলে ক্রসিং এড়ানো যায় না"],
                T_SMALL, GREY, 400)
    y = note_strip(s, yb + 16, "KM1 উপরের সারিতে, KM3 নিচের সারিতে, "
                               "KM2 নিচের তিনটিকে এক করে — এই তিনটিই সব")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_power.svg")


def d07_star():
    s = SVG(1240, 1180)
    s.title("স্টার অবস্থা — KM1 ও KM2 টেনেছে, KM3 ছাড়া", T_TITLE)
    yb = _power14(s, "star")
    s.textlines(700, SY[2] + 34, ["নিচের তিন প্রান্ত KM2-তে এক হয়ে",
                                  "নিউট্রাল পয়েন্ট হয়েছে;  প্রতিটি কয়েলে",
                                  "ভোল্টেজ 400 / 1.73 = 231 V"],
                T_SMALL, STARC, 700)
    y = note_strip(s, yb + 16, "কয়েলে 231 V, লাইন কারেন্ট সরাসরি চালুর "
                               "এক-তৃতীয়াংশ — কিন্তু টর্কও এক-তৃতীয়াংশ")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_star.svg")


def d08_delta():
    s = SVG(1240, 1180)
    s.title("ডেল্টা অবস্থা — KM1 ও KM3 টেনেছে, KM2 ছাড়া", T_TITLE)
    yb = _power14(s, "delta")
    s.textlines(700, SY[2] + 34, ["KM2 ছেড়ে দিয়েছে, KM3 নিচের সারিকে",
                                  "লাইনে জুড়েছে;  প্রতিটি কয়েলে এখন",
                                  "পুরো 400 V"], T_SMALL, DELC, 700)
    y = note_strip(s, yb + 16, "প্রতিটি কয়েলে পুরো লাইন ভোল্টেজ — "
                               "মোটর এখন স্বাভাবিক ডেল্টায় চলছে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_delta.svg")


# ── ৯. দুটো একসঙ্গে টানলে ───────────────────────────────────────────────
def d09_danger():
    s = SVG(1240, 800)
    s.title("KM2 আর KM3 একসঙ্গে টানলে — তিন ফেজ সরাসরি শর্ট", T_TITLE)

    XS = [380, 560, 740]
    TY, MY, BY = 214, 396, 560
    for i, x in enumerate(XS):
        s.path(f"M {x} {TY} L {x} {MY}", PHC[i], 4)
        node(s, x, TY, PHC[i])
        s.text(x, TY - 22, ("L1", "L2", "L3")[i], T_BODY, PHC[i], 700,
               "middle")
        s.text(x - 16, MY - 84, ("W2", "U2", "V2")[i], T_SMALL, NAVY, 700,
               "end")
    s.rect(XS[0] - 58, 268, XS[2] - XS[0] + 116, 86, "#FFF1EC", DELC, 2.4, 8)
    for x in XS:
        s.path(f"M {x} 286 L {x} 336", DELC, 3.6)
        node(s, x, 286, DELC)
        node(s, x, 336, DELC)
    s.text(XS[2] + 78, 304, "KM3 — টেনেছে", T_BODY, DELC, 700, "start")
    s.text(XS[2] + 78, 334, "নিচের সারি লাইনে", T_SMALL, GREY, 400, "start")

    for i, x in enumerate(XS):
        term(s, x, MY, ("W2", "U2", "V2")[i])
        s.path(f"M {x} {MY + 16} L {x} {BY - 46}", RED, 4)
    s.rect(XS[0] - 58, BY - 46, XS[2] - XS[0] + 116, 86, "#FDECEA", RED,
           2.4, 8)
    for x in XS:
        s.path(f"M {x} {BY - 28} L {x} {BY + 22}", RED, 3.6)
    s.text(XS[2] + 78, BY - 10, "KM2 — টেনেছে", T_BODY, RED, 700, "start")
    s.text(XS[2] + 78, BY + 20, "তিনটি এক নোডে", T_SMALL, GREY, 400, "start")
    s.path(f"M {XS[0]} {BY + 22} L {XS[2]} {BY + 22}", RED, 4.4)
    for x in XS:
        node(s, x, BY + 22, RED)
    star_point(s, XS[1], BY + 56, RED)

    for i in (0, 2):
        chev(s, XS[i], 250, 0, 1, RED, 13, 3.4)
    chev(s, XS[1], BY - 6, 0, -1, RED, 13, 3.4)
    s.textlines(880, 206, ["একই বিন্দুতে L1, L2 আর L3",
                           "— মাঝে কোনো কয়েল নেই,",
                           "কোনো লোড নেই"], T_BODY, RED, 700)
    s.text(880, 620, "কয়েক হাজার অ্যাম্পিয়ার", T_NAME, RED, 700, "start")
    s.text(880, 656, "Q1 না কাটলে আগুন", T_SMALL, GREY, 400, "start")

    y = note_strip(s, 700, "KM2 আর KM3-এর মাঝে ইন্টারলক তাই বাধ্যতামূলক — "
                           "একটি ছাড়ার আগে অন্যটি টানতে পারবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_danger.svg")


# ── ১০-১১. কন্ট্রোল সার্কিট ─────────────────────────────────────────────
# চারটি রাং, সবই এক জায়গা থেকে;  d10 আর d11 একই ফাংশনের দুই অবস্থা,
# তাই দুই ছবি কখনো আলাদা কথা বলতে পারে না।
TX, IX = 700, 846                  # টাইমারের কন্টাক্ট, অক্সিলিয়ারি NC
CCX, RRX = 972, 1164               # কয়েলের শুরু, ডান পাশের নিউট্রাল


def _coil_end(s, y, tag, kind=None):
    if kind:
        timer_coil(s, CCX, y - 32, 130, 64, tag, kind)
    else:
        coil_sym(s, CCX, y - 32, 130, 64, tag)
    s.text(CCX - 6, y - 40, "A1", T_TINY, NAVY, 700, "end")
    s.text(CCX + 136, y - 40, "A2", T_TINY, NAVY, 700, "start")
    s.path(f"M {CCX + 130} {y} L {RRX} {y}", NEUT, SW)
    node(s, RRX, y, NEUT)


def _ladder14(s, oy, state):
    """state = "star" / "delta"।"""
    star = state == "star"
    LY = oy + 150
    RA = LY + 180                       # KM1 — ল্যাচিং রাং
    HA = RA + 96                        # ল্যাচের কন্টাক্ট
    RB = RA + 206                       # KT — টাইমারের কয়েল
    RC = RB + 132                       # KM2 — স্টার
    RD = RC + 132                       # KM3 — ডেল্টা
    NY = RD + 84

    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")

    # উপরের রেল:  F1 → F2 95-96 → STOP
    s.path(f"M 82 {LY} L 118 {LY}", LIVE, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 250 {LY}", LIVE, SW)
    _nc(s, 250, LY, LIVE)
    s.path(f"M 290 {nc_tip(250, LY, 290)} L 290 {LY - 62}", SYM, 2,
           dash="6 5")
    thermal_sym(s, 290, LY - 86, 34, 40, SYM, 2.4)
    s.text(316, LY - 110, "F2", T_SMALL, AMBER, 700, "start")
    s.text(260, LY + 36, "95", T_TINY, NAVY, 700, "middle")
    s.text(334, LY + 36, "96", T_TINY, NAVY, 700, "middle")
    s.path(f"M 342 {LY} L 390 {LY}", LIVE, SW)
    _nc(s, 390, LY, LIVE)
    _pb(s, 436, LY, RED, "#F6C9C4", "STOP")
    s.text(400, LY + 36, "11", T_TINY, NAVY, 700, "middle")
    s.text(474, LY + 36, "12", T_TINY, NAVY, 700, "middle")
    s.path(f"M 482 {LY} L 500 {LY} L 500 {RA}", LIVE, SW)
    node(s, 500, RA, LIVE)

    # ── রাং ১ — KM1, ল্যাচিং (অধ্যায় ৮-এর ৮.৯-এর সেই সার্কিট) ──────────
    s.path(f"M 500 {RA} L 540 {RA}", LIVE, SW)
    _no(s, 540, RA, LIVE, closed=False)
    _pb(s, 586, RA, GREEN, "#BFE3CE", "START", tip=no_tip(540, RA, 586))
    s.text(550, RA + 36, "13", T_TINY, NAVY, 700, "middle")
    s.text(624, RA + 36, "14", T_TINY, NAVY, 700, "middle")
    s.path(f"M 632 {RA} L {CCX} {RA}", LIVE, SW)
    s.path(f"M 540 {RA} L 540 {HA} L 546 {HA}", LIVE, SW)
    _no(s, 546, HA, LIVE, closed=True, w=80)
    s.path(f"M 626 {HA} L 632 {HA} L 632 {RA}", LIVE, SW)
    s.text(562, HA + 42, "KM1 13-14", T_SMALL, LIVE, 700, "middle")
    _coil_end(s, RA, "KM1")

    # নিচের তিন রাং ল্যাচের **পরে** — তাই START না চাপলে টাইমারও চলে না
    s.path(f"M 632 {RA} L 632 {RD}", LIVE, SW)
    for yy in (RA, HA, RB, RC, RD):
        node(s, 632, yy, LIVE)

    # ── রাং ২ — টাইমারের কয়েল, KM1-এর সঙ্গেই ─────────────────────────
    s.path(f"M 632 {RB} L {CCX} {RB}", LIVE, SW)
    _coil_end(s, RB, "KT", "on")
    s.text(CCX + 40, RB + 56, "2 - 7", T_TINY, NAVY, 700, "middle")

    # ── রাং ৩ — স্টার:  KT 8-5 → KM3 21-22 → KM2 কয়েল ─────────────────
    s.path(f"M 632 {RC} L {TX} {RC}", LIVE, SW)
    dnc(s, TX, RC, LIVE, "on", opened=not star)
    s.text(TX + 52, RC - 82, "KT 8-5", T_SMALL, TIMEC, 700, "start")
    c1 = LIVE if star else DEAD
    s.path(f"M {TX + 92} {RC} L {IX} {RC}", c1, SW)
    _nc(s, IX, RC, c1, opened=not star)
    s.text(IX + 46, RC - 62, "KM3 21-22", T_SMALL, NAVY, 700, "middle")
    s.text(IX + 10, RC + 36, "21", T_TINY, NAVY, 700, "middle")
    s.text(IX + 82, RC + 36, "22", T_TINY, NAVY, 700, "middle")
    s.path(f"M {IX + 92} {RC} L {CCX} {RC}", c1, SW)
    _coil_end(s, RC, "KM2")

    # ── রাং ৪ — ডেল্টা:  KT 8-6 → KM2 21-22 → KM3 কয়েল ────────────────
    s.path(f"M 632 {RD} L {TX} {RD}", LIVE, SW)
    dno(s, TX, RD, LIVE, "on", closed=not star)
    s.text(TX + 52, RD - 82, "KT 8-6", T_SMALL, TIMEC, 700, "start")
    c2 = DEAD if star else LIVE
    s.path(f"M {TX + 92} {RD} L {IX} {RD}", c2, SW)
    _nc(s, IX, RD, c2, opened=star)
    s.text(IX + 46, RD - 62, "KM2 21-22", T_SMALL, NAVY, 700, "middle")
    s.text(IX + 10, RD + 36, "21", T_TINY, NAVY, 700, "middle")
    s.text(IX + 82, RD + 36, "22", T_TINY, NAVY, 700, "middle")
    s.path(f"M {IX + 92} {RD} L {CCX} {RD}", c2, SW)
    _coil_end(s, RD, "KM3")

    s.path(f"M 82 {NY} L {RRX} {NY}", NEUT, SW)
    node(s, RRX, NY, NEUT)
    for yy in (RA, RB, RC, RD):
        s.path(f"M {RRX} {yy} L {RRX} {NY}", NEUT, SW)
    return NY


def d10_control_star():
    s = SVG(1240, 1120)
    s.title("কন্ট্রোল সার্কিট — স্টার অবস্থা (সময় গোনা চলছে)", T_TITLE)
    ny = _ladder14(s, 60, "star")
    y = note_strip(s, ny + 44, "KT 8-5 এখনো বন্ধ, তাই KM2 টেনেছে;  "
                               "KM2 21-22 খুলে KM3-এর পথ আটকে রেখেছে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_control_star.svg")


def d11_control_delta():
    s = SVG(1240, 1120)
    s.title("কন্ট্রোল সার্কিট — ডেল্টা অবস্থা (সময় শেষ)", T_TITLE)
    ny = _ladder14(s, 60, "delta")
    y = note_strip(s, ny + 44, "সময় শেষে 8-5 খুলল, 8-6 বন্ধ হলো;  KM2 "
                               "ছাড়ার পরেই তার 21-22 KM3-কে পথ দিল")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_control_delta.svg")


# ── ১২. সময়ের ছক ────────────────────────────────────────────────────────
def _plot(s, x0, y0, w, h, pts, col, tmax, vmax, dash=None, sw=3.6):
    px = lambda t: x0 + w * t / tmax
    py = lambda v: y0 - h * v / vmax
    s.path("M " + " L ".join(f"{px(t)} {py(v)}" for t, v in pts), col, sw,
           dash=dash)
    return px, py


def d12_timing():
    s = SVG(1240, 1040)
    s.title("শুরু থেকে ডেল্টা পর্যন্ত — কে কখন টানে", T_TITLE)

    TMAX, X0, XW = 12.0, 236, 838
    rows = [("START বোতাম", [(1, 1.6)], GREEN),
            ("KM1  লাইন", [(1, TMAX)], GREEN),
            ("KT  টাইমার", [(1, TMAX)], TIMEC),
            ("KM2  স্টার", [(1, 6)], STARC),
            ("KM3  ডেল্টা", [(6.2, TMAX)], DELC)]
    px, lows = timing(s, X0, 116, XW, rows, TMAX, RH=72)
    # মাপের তির টিক-সংখ্যার উপরে — নিচে বসালে ছেঁড়া রেখা সংখ্যার গায়ে পড়ে
    dim_arrow(s, px(1), px(6), lows[-1] + 40, "t1 — স্টারে চলার সময়  "
              "(6 – 10 s)", STARC)
    s.path(f"M {px(6)} 128 L {px(6)} {lows[-1] + 40}", GREY, 1.8, dash="7 5")
    for t in range(0, 13, 2):
        s.text(px(t), lows[-1] + 88, str(t), T_TINY, GREY, 400, "middle")
    s.text(X0 + XW / 2, lows[-1] + 122, "সময় (সেকেন্ড)", T_SMALL, NAVY, 700,
           "middle")

    # বদলের মুহূর্তটা বড় করে — এই স্কেলে ৫০ ms দেখাই যায় না
    ZX, ZY, ZW, ZH = 262, 626, 578, 250
    s.rect(ZX, ZY, ZW, ZH, "#FCFDFE", STEEL, 2.4, 12)
    s.text(ZX + ZW / 2, ZY + 36, "বদলের মুহূর্তটা বড় করে দেখলে", T_BODY,
           NAVY, 700, "middle")
    zx = lambda ms: ZX + 96 + (ms + 20) * 4.0
    HI2, LO2 = ZY + 76, ZY + 110          # KM2-এর সারি
    HI3, LO3 = ZY + 176, ZY + 210         # KM3-এর সারি
    s.text(ZX + 80, LO2 - 8, "KM2", T_SMALL, STARC, 700, "end")
    s.text(ZX + 80, LO3 - 8, "KM3", T_SMALL, DELC, 700, "end")
    s.path(f"M {zx(-20)} {HI2} L {zx(0)} {HI2} L {zx(0)} {LO2} "
           f"L {zx(90)} {LO2}", STARC, 3.6)
    s.path(f"M {zx(-20)} {LO3} L {zx(50)} {LO3} L {zx(50)} {HI3} "
           f"L {zx(90)} {HI3}", DELC, 3.6)
    s.path(f"M {zx(0)} {LO2} L {zx(0)} {HI3 - 4}", GREY, 1.6, dash="6 5")
    s.path(f"M {zx(50)} {LO2 + 4} L {zx(50)} {HI3}", GREY, 1.6, dash="6 5")
    dim_arrow(s, zx(0), zx(50), ZY + 143, "t2 = 50 ms", RED)
    s.text(ZX + ZW / 2, ZY + 238, "এই ফাঁকটুকুতেই আর্ক নিভে যায়", T_SMALL,
           GREY, 400, "middle")

    s.textlines(872, ZY + 54, ["KM2 পুরোপুরি ছাড়ার আগে KM3",
                               "টানলে ওই মুহূর্তে দুই সেট",
                               "কন্টাক্ট একসঙ্গে বন্ধ থাকে —",
                               "মানে ফেজ-টু-ফেজ শর্ট।",
                               "",
                               "উৎসর্গীকৃত স্টার-ডেল্টা টাইমারে",
                               "এই 50 ms কারখানাতেই বসানো।"],
                T_SMALL, NAVY, 400)

    y = note_strip(s, 912, "t1 হাতে বসানো যায়, t2 নয় — ওটি টাইমারের "
                           "ভেতরেই স্থির, ABB CT-SDS.23-এ 50 ms")
    s.fit(y, 24)
    return s.save(f"{OUT}/d12_timing.svg")


# ── ১৩. উৎসর্গীকৃত স্টার-ডেল্টা টাইমার ──────────────────────────────────
def d13_sdtimer():
    s = SVG(1240, 780)
    s.title("স্টার-ডেল্টা টাইমার — দুটি আউটপুট, মাঝে স্থির ফাঁক", T_TITLE)

    # বাঁয়ে — যন্ত্রটির সামনের চেহারা
    panel(s, 46, 118, 336, 470, "সামনের দিক", TIMEC)
    s.rect(120, 196, 188, 330, PLATE, IRON_D, 2.6, 10)
    s.circle(214, 288, 62, "#FFFFFF", IRON_D, 3)
    for i in range(7):
        a = math.radians(-210 + i * 40)
        s.path(f"M {214 + 46 * math.cos(a)} {288 + 46 * math.sin(a)} "
               f"L {214 + 60 * math.cos(a)} {288 + 60 * math.sin(a)}",
               IRON_D, 2.2)
    s.path("M 214 288 L 186 248", TIMEC, 4)
    s.text(214, 372, "সময়ের পরিসর", T_SMALL, NAVY, 700, "middle")
    s.text(214, 400, "0.05 s – 10 min", T_SMALL, GREY, 400, "middle")
    for i, (lab, col) in enumerate((("U/T", GREEN), ("R1", STARC),
                                    ("R2", DELC))):
        s.circle(160 + i * 54, 446, 11, col, col)
        s.text(160 + i * 54, 480, lab, T_TINY, NAVY, 700, "middle")
    s.text(214, 512, "তিনটি LED", T_SMALL, GREY, 400, "middle")

    # মাঝে — টার্মিনাল
    panel(s, 402, 118, 336, 470, "টার্মিনাল", STEEL)
    tt = [("A1", "সরবরাহ", NAVY, 196), ("A2", "সরবরাহ", NAVY, 258),
          ("17", "দুই আউটপুটের কমন", STEEL, 330),
          ("18", "স্টার কন্টাক্টরে", STARC, 402),
          ("28", "ডেল্টা কন্টাক্টরে", DELC, 474)]
    for tag, what, col, yy in tt:
        s.rect(440, yy - 22, 66, 44, "#D7E2EC", STEEL, 2.2, 5)
        s.text(473, yy + 8, tag, T_SMALL, NAVY, 700, "middle")
        s.text(524, yy + 8, what, T_SMALL, col, 700, "start")
    s.text(570, 534, "17-18 আর 17-28 — দুটোই NO", T_SMALL, GREY, 400,
           "middle")

    # ডানে — কাজের ছক
    panel(s, 758, 118, 436, 470, "কাজের ছক", DELC)
    rows = [("A1-A2", [(0, 9)], NAVY), ("17-18", [(0, 4)], STARC),
            ("17-28", [(4.5, 9)], DELC)]
    px, lows = timing(s, 856, 190, 296, rows, 9.0, RH=88)
    dim_arrow(s, px(0), px(4), 456, "t1", STARC)
    dim_arrow(s, px(4), px(4.5), 510, "t2 = 50 ms", RED)
    s.text(976, 552, "t1 ডায়ালে বসে, t2 বসে না", T_SMALL, GREY, 400,
           "middle")

    y = note_strip(s, 620, "সরবরাহ পেলেই 17-18 বন্ধ হয়ে স্টার ধরে;  t1 "
                           "শেষে খোলে, 50 ms পরে 17-28 ডেল্টা ধরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_sdtimer.svg")


# ── ১৪. প্যানেলে যন্ত্রগুলো ও তারের তালিকা ───────────────────────────────
def _dev(s, x, y, w, h, name, sub=None, col=STEEL, fill="#FCFDFE"):
    s.rect(x, y, w, h, fill, col, 2.6, 8)
    s.text(x + w / 2, y + 30, name, T_BODY, col, 700, "middle")
    if sub:
        s.text(x + w / 2, y + 58, sub, T_TINY, GREY, 400, "middle")
    return x + w / 2


def d14_wiring():
    s = SVG(1240, 960)
    s.title("প্যানেলে কোনটা কোথায়, আর কোন তার কোথা থেকে কোথায়", T_TITLE)

    # ── বাঁয়ে:  ব্যাক-প্লেটের সামনের চেহারা ──────────────────────────────
    s.rect(46, 118, 660, 588, "#F3F7FB", STEEL, 2.6, 12)
    s.text(376, 148, "ব্যাক-প্লেট", T_SMALL, GREY, 400, "middle")

    # DIN রেল যন্ত্রের ঠিক উপরে — ভেতর দিয়ে গেলে নামের উপর দাগ পড়ে
    for ry in (168, 318, 570):
        s.rect(74, ry - 9, 604, 18, "#D7E2EC", "#9AAEBF", 1.8, 3)

    _dev(s, 90, 182, 150, 96, "Q1", "MCCB", NAVY)
    _dev(s, 262, 182, 132, 96, "F1", "কন্ট্রোল ফিউজ", NAVY)
    _dev(s, 416, 182, 244, 96, "X1", "টার্মিনাল স্ট্রিপ", GREY)

    _dev(s, 90, 332, 168, 116, "KM1", "লাইন", GREEN)
    _dev(s, 274, 332, 168, 116, "KM2", "স্টার", STARC)
    _dev(s, 458, 332, 168, 116, "KM3", "ডেল্টা", DELC)
    _dev(s, 90, 462, 168, 74, "F2", "ওভারলোড রিলে", AMBER, "#FFFBF2")
    s.path("M 174 448 L 174 462", AMBER, 3, dash="5 4")
    s.text(292, 484, "F2 বসে KM1-এর নিচেই —", T_TINY, GREY, 400, "start")
    s.text(292, 514, "ওই পথেই কয়েলের কারেন্ট যায়", T_TINY, GREY, 400,
           "start")

    _dev(s, 300, 584, 190, 96, "KT", "স্টার-ডেল্টা টাইমার", TIMEC)

    # দরজা
    s.rect(46, 726, 660, 122, "#FCFDFE", IRON_D, 2.6, 10)
    s.text(108, 790, "দরজা", T_SMALL, GREY, 400, "middle")
    for i, (lab, col, bg) in enumerate((("STOP", RED, "#F6C9C4"),
                                        ("START", GREEN, "#BFE3CE"))):
        cx = 254 + i * 132
        s.rect(cx - 42, 762, 84, 30, bg, col, 2.4, 6)
        s.text(cx, 822, lab, T_SMALL, col, 700, "middle")
    for i, (lab, col) in enumerate((("H1 স্টার", STARC), ("H2 ডেল্টা", DELC))):
        cx = 520 + i * 124
        lamp(s, cx, 780, 20, on=True, col=col)
        s.text(cx, 826, lab, T_TINY, col, 700, "middle")

    # ── ডানে:  তারের তালিকা ─────────────────────────────────────────────
    panel(s, 730, 118, 464, 588, "কন্ট্রোল তারের তালিকা", NAVY)
    wires = [("১", "L", "F1 ভেতরে"),
             ("২", "F1 বাইরে", "F2 : 95"),
             ("৩", "F2 : 96", "STOP : 11"),
             ("৪", "STOP : 12", "START : 13  ও  KM1 : 13"),
             ("৫", "START : 14", "KM1 : 14  ও  KM1 : A1"),
             ("৬", "KM1 : A1", "KT : 2  ও  KT : 8"),
             ("৭", "KT : 5", "KM3 : 21"),
             ("৮", "KM3 : 22", "KM2 : A1"),
             ("৯", "KT : 6", "KM2 : 21"),
             ("১০", "KM2 : 22", "KM3 : A1"),
             ("১১", "N", "KT : 7  ও  তিন কয়েলের A2")]
    s.text(772, 196, "নং", T_TINY, NAVY, 700, "middle")
    s.text(872, 196, "কোথা থেকে", T_TINY, NAVY, 700, "middle")
    s.text(1060, 196, "কোথায়", T_TINY, NAVY, 700, "middle")
    s.path("M 748 212 L 1176 212", "#C8D4DF", 1.8)
    for i, (n, a1, b1) in enumerate(wires):
        yy = 244 + i * 39
        s.text(772, yy, n, T_TINY, GREY, 400, "middle")
        s.text(872, yy, a1, T_TINY, NAVY, 700, "middle")
        s.text(1060, yy, b1, T_TINY, NAVY, 400, "middle")
    s.text(962, 684, "H1 বসে KM2-এর A1-এ, H2 বসে KM3-এর A1-এ",
           T_TINY, GREY, 400, "middle")

    y = note_strip(s, 872, "পাওয়ার তার আলাদা — Q1 → KM1 ও KM3, "
                           "আর KM1 → F2 → মোটরের উপরের সারি")
    s.fit(y, 24)
    return s.save(f"{OUT}/d14_wiring.svg")


# ── ১৫. কোন কন্টাক্টরে কত কারেন্ট ───────────────────────────────────────
def d15_sizing():
    s = SVG(1240, 760)
    s.title("কোন কন্টাক্টরে কত কারেন্ট যায়", T_TITLE)

    cards = [("KM1 — লাইন", "0.58 × In", "ডেল্টায় কয়েলের কারেন্ট", GREEN),
             ("KM2 — স্টার", "0.33 × In", "স্টারের লাইন কারেন্ট", STARC),
             ("KM3 — ডেল্টা", "0.58 × In", "ডেল্টায় কয়েলের কারেন্ট", DELC),
             ("F2 — সেটিং", "0.58 × In", "কয়েলের কারেন্টেই বসে", AMBER)]
    W, GAP, X0, Y, H = 272, 34, 46, 124, 206
    for i, (a, big, sub, col) in enumerate(cards):
        ratio_card(s, X0 + i * (W + GAP), Y, W, H, a, big, sub, col)

    # উদাহরণ — একটি চেনা মাপের মোটর
    s.rect(46, 374, 1148, 186, "#F3F7FB", STEEL, 2, 12)
    s.text(620, 414, "উদাহরণ — 15 kW মোটর, নেমপ্লেটে In = 30 A", T_NAME,
           NAVY, 700, "middle")
    ex = [("KM1", "30 × 0.58 = 17.4 A", "বাজারে 18 A", GREEN),
          ("KM2", "30 / 3 = 10 A", "বাজারে 12 A", STARC),
          ("KM3", "30 × 0.58 = 17.4 A", "বাজারে 18 A", DELC),
          ("F2", "সেট করুন 17.4 A", "পরিসর 13–19 A", AMBER)]
    for i, (nm, calc, buy, col) in enumerate(ex):
        cx = 180 + i * 290
        s.text(cx, 462, nm, T_BODY, col, 700, "middle")
        s.text(cx, 500, calc, T_SMALL, NAVY, 400, "middle")
        s.text(cx, 532, buy, T_SMALL, GREY, 400, "middle")

    s.text(620, 610, "লক্ষ করুন — তিনটির একটিও পুরো 30 A-এর নয়।  সরাসরি "
                     "চালুর স্টার্টারে একটিই কন্টাক্টর লাগত,", T_SMALL,
           GREY, 400, "middle")
    s.text(620, 644, "কিন্তু সেটি হতো পুরো 30 A-এর।  তিনটি ছোট কন্টাক্টর "
                     "মিলিয়ে দাম প্রায় সমানই পড়ে।", T_SMALL, GREY, 400,
           "middle")

    y = note_strip(s, 680, "0.58 আসে 1 / 1.73 থেকে, আর 0.33 আসে "
                           "0.58 / 1.73 থেকে — দুটোই একই হিসাব")
    s.fit(y, 24)
    return s.save(f"{OUT}/d15_sizing.svg")


ALL = [d01_idea, d02_voltage, d03_ratio, d04_curves, d05_terminals,
       d06_power, d07_star, d08_delta, d09_danger,
       d10_control_star, d11_control_delta, d12_timing,
       d13_sdtimer, d14_wiring, d15_sizing]

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
