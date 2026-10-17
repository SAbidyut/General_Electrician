# -*- coding: utf-8 -*-
"""অধ্যায় ৯ — DOL স্টার্টার : ডায়াগ্রাম।

অধ্যায় ৮-এর সহায়কগুলো (`panel`, `note_strip`, `node`, `chip`,
`callout`, `coil_sym`, `photo_callouts`) এখানে সরাসরি আমদানি করা —
একই বইয়ের একই চেহারা, আর একটি সংশোধন দুই জায়গায় করতে হয় না।
`photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই এখানে
`IMG` বদলে নেওয়া হয়েছে (`_use_ch09_images()`)।

**টপোলজি যাচাই — অধ্যায় ৮-এর নিয়ম এখানেও।**  কন্ট্রোল সার্কিটে
ওভারলোড রিলের 95-96 **সিরিজে** বসে, STOP-এর আগে;  97-98 আলাদা
শাখায়, ট্রিপ বাতির সঙ্গে সিরিজে।  হোল্ডিং কন্টাক্ট 13-14 আগের মতোই
START-এর দুই নোড থেকে নামে।  d09 ও d10 একই `_ladder()` থেকে আঁকা,
কেবল অবস্থা আলাদা — ফলে "চলছে" আর "ট্রিপ" ছবির তার কখনো আলাদা হতে
পারে না।

**d11-এর তার-বিন্যাস** হাতে বসানো, **একটিও ক্রসিং নেই** — বোতামগুলো
বাঁ পাশে উল্লম্ব সারিতে, আর কন্টাক্টরের 13/14 ও রিলের 95/96 দুটোই
বাঁ দিকে মুখ করে।  কোনো তার সরালে ক্রসিং আবার ফিরে আসতে পারে,
চোখে দেখে নিতে হবে (qc ক্রসিং ধরে না)।

**d04 (বাইমেটাল)** — উঁচু প্রসারণের পাত বাঁয়ে, তাই গরমে পাতটি
ডানে, কম প্রসারণের পাতের দিকে বাঁকে।  বাস্তবের নিয়মও তাই।  পুশ
রড আর কন্টাক্টের ব্লেডের জ্যামিতি একই `shift` থেকে হিসাব করা,
যাতে গরম ছবিতে দণ্ডের মাথা ঠিক ব্লেডের গায়েই লাগে।

**d06 ও d07-এর সংখ্যা** — ১.০৫ ও ১.২ গুণ (ABB ও Siemens-এর
ক্যাটালগ, IEC 60947-4-1);  ৭.২ গুণে ক্লাস 10A 2–10 s, 10 4–10 s,
20 6–20 s, 30 9–30 s (ABB-র ক্যাটালগে IEC 947-4-1-এর উদ্ধৃতি;
Schneider TeSys-এও একই)।  ডায়ালের 5.5–8 A পরিসর Schneider LRD12-এর।

কালপুরুষের সীমা অধ্যায় ৮-এর মতোই — টার্মিনাল নম্বর, রেটিং, মডেল
নম্বর সব ল্যাটিন অঙ্কে।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, chip, callout, coil_sym,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, LIVE, NEUT, DEAD, PLATE, CU)
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch09")
IMG = os.path.join(HERE, "assets", "ch09")

HEAT = "#C8892A"          # হিটারের তামা
BI_HI = "#C0392B"         # উঁচু প্রসারণের পাত
BI_LO = "#7C8894"         # কম প্রসারণের পাত (ইনভার)
LAMP_ON = "#F5C542"


def _use_ch09_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch09_images()
    return C8.photo_callouts(*a, **k)


def fuse(s, x, y, w=72, h=46, label=None, vertical=False):
    """ফিউজ — খোলা আয়তক্ষেত্র, মাঝে দাগ (IEC)।"""
    if vertical:
        s.rect(x - h / 2, y - w / 2, h, w, PLATE, NAVY, 2.4, 6)
        s.path(f"M {x} {y - w / 2} L {x} {y + w / 2}", NAVY, 2.8)
    else:
        s.rect(x - w / 2, y - h / 2, w, h, PLATE, NAVY, 2.4, 6)
        s.path(f"M {x - w / 2} {y} L {x + w / 2} {y}", NAVY, 2.8)
    if label:
        s.text(x, y - h / 2 - 16, label, T_SMALL, NAVY, 700, "middle")


def thermal_sym(s, cx, cy, w=46, h=56, col=SYM, sw=3):
    """থার্মাল ওভারলোড উপাদানের প্রতীক — বাক্সের ভেতর ধাপ-কাটা রেখা।"""
    s.rect(cx - w / 2, cy - h / 2, w, h, "#FFFFFF", col, sw, 3)
    s.path(f"M {cx} {cy - h / 2} L {cx} {cy - 12} L {cx + 13} {cy - 12} "
           f"L {cx + 13} {cy + 12} L {cx} {cy + 12} L {cx} {cy + h / 2}",
           col, sw)


def lamp(s, cx, cy, r=24, on=False, col=GREEN):
    s.circle(cx, cy, r, LAMP_ON if on else "#FFFFFF", SYM, 3)
    d = r * 0.707
    s.path(f"M {cx - d} {cy - d} L {cx + d} {cy + d}", SYM, 2.6)
    s.path(f"M {cx - d} {cy + d} L {cx + d} {cy - d}", SYM, 2.6)


# ── ১. DOL স্টার্টার এক নজরে ────────────────────────────────────────────
def d01_block():
    s = SVG(1240, 700)
    s.title("DOL স্টার্টারের অংশ", T_TITLE)
    ar = s.arrow_defs(RED, "arP", 15)
    ag = s.arrow_defs(STEEL, "arC", 14)

    blocks = [("সরবরাহ", "L1 · L2 · L3", "400 V থ্রি-ফেজ", LIGHT, STEEL),
              ("MCCB / MCB", "Q1", "শর্ট সার্কিট থেকে", LIGHT, NAVY),
              ("কন্টাক্টর", "KM1", "চালু ও বন্ধ করে", GREENBG, GREEN),
              ("ওভারলোড রিলে", "F2", "বেশি কারেন্ট থেকে", AMBERBG, AMBER),
              ("মোটর", "M 3~", "লোড", LIGHT, STEEL)]
    BW, BH, Y = 196, 150, 120
    xs = [46 + i * 238 for i in range(5)]
    for x, (name, tag, role, bg, col) in zip(xs, blocks):
        s.rect(x, Y, BW, BH, bg, col, 2.8, 12)
        s.text(x + BW / 2, Y + 46, name, T_NAME, col, 700, "middle")
        s.text(x + BW / 2, Y + 88, tag, T_NODE, NAVY, 700, "middle")
        s.text(x + BW / 2, Y + 128, role, T_SMALL, GREY, 400, "middle")
    for x in xs[:-1]:
        s.path(f"M {x + BW + 4} {Y + BH / 2} L {x + 234} {Y + BH / 2}",
               RED, 4.2, marker=ar)

    # স্টার্টারের সীমানা — কন্টাক্টর আর রিলে একই বাক্সে
    sx0, sx1 = xs[2] - 18, xs[3] + BW + 18
    s.path(f"M {sx0} {Y - 24} L {sx1} {Y - 24} L {sx1} {Y + BH + 232} "
           f"L {sx0} {Y + BH + 232} Z", GREEN, 2.4, dash="10 7")
    s.text((sx0 + sx1) / 2, Y + BH + 222, "DOL স্টার্টার", T_NAME, GREEN,
           700, "middle")

    # কন্ট্রোল — বোতাম কয়েল চালায়, রিলে কয়েল কাটে
    cy = Y + BH + 104
    blk_w = 250
    bx = sx0 + 16
    s.rect(bx, cy - 34, blk_w, 68, "#FFFFFF", STEEL, 2.4, 10)
    s.text(bx + blk_w / 2, cy + 8, "START / STOP বাটন", T_BODY, STEEL,
           700, "middle")
    s.path(f"M {xs[2] + BW / 2} {cy - 38} L {xs[2] + BW / 2} {Y + BH + 6}",
           STEEL, 2.8, dash="8 6", marker=ag)
    s.text(xs[2] + BW / 2 - 14, Y + BH + 44, "কয়েল", T_SMALL, STEEL, 700,
           "end")
    rx = xs[3] + BW / 2
    s.path(f"M {rx} {Y + BH + 4} L {rx} {cy} L {bx + blk_w + 8} {cy}",
           AMBER, 2.8, dash="8 6", marker=s.arrow_defs(AMBER, "arA", 14))
    s.text(rx + 14, Y + BH + 44, "95-96", T_SMALL, AMBER, 700, "start")

    y = note_strip(s, Y + BH + 262, "কন্টাক্টর মোটর চালু-বন্ধ করে, ওভারলোড "
                                     "রিলে মোটরকে বেশি কারেন্ট থেকে রক্ষা করে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_block.svg")


# ── ২. চালু হওয়ার মুহূর্তের কারেন্ট ─────────────────────────────────────
def d02_current():
    """গুণগত লেখচিত্র — সংখ্যা অধ্যায় ৮-এর ৬–৮ গুণের সঙ্গে মেলানো।"""
    s = SVG(1240, 700)
    s.title("DOL-এ চালু হওয়ার মুহূর্তে মোটরের কারেন্ট", T_TITLE)

    X0, Y0, XW, YH = 190, 520, 900, 380      # অক্ষের মূলবিন্দু ও মাপ
    YMAX, TMAX = 8.0, 6.0
    px = lambda t: X0 + t / TMAX * XW
    py = lambda m: Y0 - m / YMAX * YH

    # গ্রিড ও অক্ষ
    for m in range(0, 9, 2):
        s.line(X0, py(m), X0 + XW, py(m), "#E3E9EF", 1.4)
        s.text(X0 - 16, py(m) + 7, f"{m}", T_SMALL, GREY, 700, "end")
    for t in range(0, 7):
        s.text(px(t), Y0 + 34, f"{t}", T_SMALL, GREY, 700, "middle")
    s.path(f"M {X0} {Y0 - YH - 10} L {X0} {Y0} L {X0 + XW + 10} {Y0}",
           NAVY, 2.8)
    s.text(X0 + XW / 2, Y0 + 72, "সময় (সেকেন্ড)", T_BODY, NAVY, 700,
           "middle")
    s.text(X0 - 20, Y0 - YH - 26, "ফুল-লোড কারেন্টের কত গুণ", T_BODY,
           NAVY, 700, "start")

    # স্টার্টিং ব্যান্ড ৬–৮ গুণ
    s.rect(px(0), py(8), px(2.4) - px(0), py(6) - py(8), "#FDECEA",
           "none", 0, 0)
    # বক্ররেখা:  ০ থেকে ঝাঁপ, ত্বরণের সময় প্রায় সমান, তারপর নেমে ১-এ
    d = (f"M {px(0)} {py(0)} L {px(0.02)} {py(7.2)} "
         f"C {px(0.8)} {py(7.0)}, {px(1.6)} {py(6.6)}, {px(2.1)} {py(5.6)} "
         f"C {px(2.4)} {py(4.4)}, {px(2.5)} {py(1.3)}, {px(2.9)} {py(1.0)} "
         f"L {px(6)} {py(1.0)}")
    s.path(d, RED, 4.2)
    s.line(px(2.9), py(1.0), px(6), py(1.0), RED, 4.2)

    s.text(px(1.2), py(7.4), "৬–৮ গুণ", T_NAME, RED, 700, "middle")
    s.text(px(4.4), py(1.0) - 20, "ফুল-লোড কারেন্ট", T_BODY, NAVY, 700,
           "middle")
    # ত্বরণের সময় — নিচে দুই-মাথা তীর
    ya = py(3.2)
    s.path(f"M {px(0.06)} {ya} L {px(2.5)} {ya}", GREY, 2.2, dash="6 5")
    s.text(px(1.25), ya - 14, "ত্বরণের সময়", T_SMALL, GREY, 700, "middle")

    y = note_strip(s, Y0 + 96, "স্টার্টিং কারেন্ট কয়েক সেকেন্ড থাকে, তাই "
                               "ওভারলোড রিলে এতে ট্রিপ করে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_current.svg")


# ── ৩. ওভারলোড রিলের সামনের দিক ─────────────────────────────────────────
def d03_olr():
    # ভগ্নাংশগুলো ক্রপ করা ছবির (assets_ch09.py-র ph_olr) হিসাবে
    return photo_callouts(
        "d03_olr", "ওভারলোড রিলের সামনের দিক", "ph_olr.jpg",
        left=[("সেটিং ডায়াল", 0.306, 0.205),
              ("ট্রিপ কন্টাক্ট 95-96 (NC)", 0.169, 0.290),
              ("মোটরে যায় 2/T1 4/T2 6/T3", 0.262, 0.661)],
        right=[("কন্টাক্টরে ঢোকার পিন", 0.820, 0.250),
               ("TEST বাটন", 0.414, 0.297),
               ("ট্রিপ ইন্ডিকেটর", 0.504, 0.406),
               ("রিসেট (Man / Auto)", 0.659, 0.464),
               ("অ্যালার্ম কন্টাক্ট 97-98 (NO)", 0.511, 0.563)],
        note="ডায়ালে মোটরের নেমপ্লেটের কারেন্ট বসাতে হয়, "
             "ট্রিপের কারেন্ট নয়",
        iw=440)


# ── ৪. বাইমেটালের কাজ ───────────────────────────────────────────────────
def _bimetal(s, x0, top, shift, hot):
    """একটি বাইমেটাল, হিটার, পুশ রড আর 95-96 কন্টাক্ট।

    `shift` — গরমে ফালির নিচের মাথা কত সরে।  পুশ রড ফালির মাথা
    থেকেই শুরু, আর দণ্ডের ডান মাথা ব্লেডকে ঠিক সেই পরিমাণ ঠেলে।
    """
    L = 250                              # ফালির দৈর্ঘ্য
    bot = top + L
    tip = x0 + shift
    # স্থির প্রান্ত
    s.rect(x0 - 40, top - 26, 88, 26, "#D5DCE3", "#8894A0", 2.2, 3)
    # দুই পাত — বাঁয়ে উঁচু প্রসারণ, ডানে কম
    for off, col in ((-6, BI_HI), (6, BI_LO)):
        if shift:
            d = (f"M {x0 + off} {top} Q {x0 + off} {top + L * 0.62} "
                 f"{tip + off} {bot}")
        else:
            d = f"M {x0 + off} {top} L {x0 + off} {bot}"
        s.path(d, col, 11)
    # হিটার — ফালির উপরের অংশে পাক
    for i in range(6):
        yy = top + 34 + i * 20
        dx = shift * ((yy - top) / L) ** 2 * 0.9 if shift else 0
        s.ellipse(x0 + dx, yy, 26, 7, "none", HEAT, 3.2)
    # মোটরের কারেন্ট — হিটারে ঢোকে-বেরোয়
    s.path(f"M {x0 - 26} {top + 34} L {x0 - 110} {top + 34}",
           RED if hot else HEAT, 3.4)
    s.path(f"M {x0 - 26} {top + 134} L {x0 - 110} {top + 134}",
           RED if hot else HEAT, 3.4)

    # পুশ রড
    BAR_Y = bot + 20
    BX = x0 + 210                        # ঠান্ডায় ব্লেডের x
    s.path(f"M {tip} {bot} L {tip} {BAR_Y}", "#5B6672", 4)
    s.rect(tip - 4, BAR_Y - 8, BX - x0 - 4, 16, "#E3E9EF", "#8894A0", 2.2, 4)

    # 95-96 কন্টাক্ট — ব্লেড নিচে পিভটে, উপরে 95-এর টিপ
    PIV = BAR_Y + 70
    TOPC = BAR_Y - 70
    bx_top = BX + shift * 2              # দণ্ড উচ্চতার দ্বিগুণ দূরে
    ccol = DEAD if hot else LIVE
    s.path(f"M {BX} {PIV} L {bx_top} {TOPC}", ccol, 5)
    s.circle(BX, PIV, 8, "#FFFFFF", SYM, 3)
    s.rect(BX - 26, TOPC - 16, 26, 14, "#B9C2CB", "#8E99A4", 1.8, 2)
    s.path(f"M {BX - 26} {TOPC - 9} L {BX - 70} {TOPC - 9}", SYM, 3)
    s.path(f"M {BX} {PIV + 8} L {BX} {PIV + 40}", SYM, 3)
    return dict(bot=bot, BAR_Y=BAR_Y, BX=BX, PIV=PIV, TOPC=TOPC, tip=tip)


def d04_bimetal():
    s = SVG(1240, 860)
    s.title("গরমে বাইমেটালের বেঁকে যাওয়া ও কন্টাক্ট খোলা", T_TITLE)

    for px_, ttl, shift, hot in ((30, "স্বাভাবিক কারেন্ট: পাত সোজা",
                                  0, False),
                                 (636, "বেশি কারেন্ট: পাত বেঁকেছে",
                                  46, True)):
        panel(s, px_, 92, 574, 640, ttl, GREEN if not hot else RED,
              "#F8FCFA" if not hot else "#FDFBFA")
        x0 = px_ + 200
        g = _bimetal(s, x0, 196, shift, hot)
        s.text(g["BX"] - 76, g["TOPC"] - 2, "95", T_SMALL, NAVY, 700, "end")
        s.text(g["BX"] - 12, g["PIV"] + 30, "96", T_SMALL, NAVY, 700, "end")
        chip(s, px_ + 287, 682,
             "95-96 খোলা, কয়েল ছেড়ে দেয়" if hot else
             "95-96 বন্ধ, কয়েল টানা থাকে",
             REDBG if hot else GREENBG, RED if hot else GREEN,
             RED if hot else GREEN, T_BODY, 40)

    # লেবেল — কেবল বাঁ প্যানেলে, ডানে একই জিনিস
    x0 = 230
    s.text(x0 + 60, 184, "স্থির প্রান্ত", T_SMALL, NAVY, 700, "start")
    s.text(x0 - 118, 222, "মোটরের", T_SMALL, RED, 700, "end")
    s.text(x0 - 118, 248, "কারেন্ট", T_SMALL, RED, 700, "end")
    s.text(x0 + 44, 290, "হিটার", T_SMALL, HEAT, 700, "start")
    s.text(x0 - 30, 420, "বেশি প্রসারণ", T_SMALL, BI_HI, 700, "end")
    s.text(x0 + 30, 420, "কম প্রসারণ", T_SMALL, BI_LO, 700, "start")
    s.text(x0 + 100, 494, "পুশ রড", T_SMALL, GREY, 700, "middle")

    y = note_strip(s, 760, "দুই ধাতুর প্রসারণ আলাদা, তাই পাত কম "
                           "প্রসারণের ধাতুর দিকে বাঁকে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_bimetal.svg")


# ── ৪খ. খোলা RA-20 ─────────────────────────────────────────────────────
def d04b_open():
    return photo_callouts(
        "d04b_open", "খোলা ওভারলোড রিলের ভেতর", "ph_ra20_open.jpg",
        left=[("বাইমেটাল ও হিটার", 0.135, 0.330),
              ("মেইন টার্মিনাল", 0.090, 0.680)],
        right=[("অক্সিলিয়ারি কন্টাক্ট", 0.880, 0.330),
               ("আরেকটি বাইমেটাল", 0.500, 0.330),
               ("ট্রিপ মেকানিজম", 0.660, 0.440),
               ("রিসেট বাটন", 0.680, 0.780),
               ("টেস্ট লিভার", 0.860, 0.820)],
        note="তামার সরু পাকগুলোই হিটার; মোটরের পুরো কারেন্ট এর ভেতর দিয়ে যায়",
        iw=380)


# ── ৫. প্রতীক ও টার্মিনাল ────────────────────────────────────────────────
def d05_symbols():
    s = SVG(1240, 720)
    s.title("ওভারলোড রিলের প্রতীক ও টার্মিনাল-নম্বর", T_TITLE)

    panel(s, 46, 92, 1148, 340, "সার্কিট ডায়াগ্রামে যেভাবে আঁকা হয়")
    CY = 262
    # তিন পোলের থার্মাল উপাদান
    for i, cx in enumerate((214, 294, 374)):
        s.path(f"M {cx} {CY - 88} L {cx} {CY - 28}", SYM, 3)
        thermal_sym(s, cx, CY)
        s.path(f"M {cx} {CY + 28} L {cx} {CY + 88}", SYM, 3)
        s.text(cx - 12, CY - 62, str(2 * i + 1), T_SMALL, NAVY, 700, "end")
        s.text(cx - 12, CY + 82, f"{2 * i + 2}/T{i + 1}", T_SMALL, NAVY,
               700, "end")
    s.path(f"M 238 {CY} L 350 {CY}", SYM, 2, dash="6 5")
    s.text(294, 400, "থার্মাল উপাদান (পাওয়ার)", T_BODY, NAVY, 700, "middle")

    def contact(cx, nc, t1, t2):
        s.path(f"M {cx} {CY - 88} L {cx} {CY - 30}", SYM, 3)
        node(s, cx, CY - 30)
        s.path(f"M {cx} {CY - 30} L {cx + 40} {CY + 24}", SYM, 3.4)
        if nc:
            s.path(f"M {cx + 40} {CY + 24} L {cx + 40} {CY - 14}", SYM, 3.4)
        node(s, cx, CY + 30)
        s.path(f"M {cx} {CY + 30} L {cx} {CY + 88}", SYM, 3)
        s.text(cx - 14, CY - 40, t1, T_SMALL, NAVY, 700, "end")
        s.text(cx - 14, CY + 50, t2, T_SMALL, NAVY, 700, "end")
        # থার্মাল চালনা — ছেঁড়া রেখা, মাথায় ছোট থার্মাল চিহ্ন
        s.path(f"M {cx + 20} {CY - 3} L {cx + 96} {CY - 3}", SYM, 2,
               dash="6 5")
        thermal_sym(s, cx + 118, CY - 3, 34, 40, SYM, 2.4)

    contact(606, True, "95", "96")
    s.text(660, 400, "ট্রিপ কন্টাক্ট (NC)", T_BODY, NAVY, 700, "middle")
    contact(906, False, "97", "98")
    s.text(960, 400, "অ্যালার্ম কন্টাক্ট (NO)", T_BODY, NAVY, 700,
           "middle")

    panel(s, 46, 456, 1148, 150, "টার্মিনাল নম্বরের নিয়ম")
    for i, (pair, what, col, bg) in enumerate((
            ("1 · 3 · 5", "কন্টাক্টর থেকে আসে", STEEL, LIGHT),
            ("2/T1 · 4/T2 · 6/T3", "মোটরে যায়", STEEL, LIGHT),
            ("95 – 96", "বিশেষ NC (ট্রিপ)", RED, REDBG),
            ("97 – 98", "বিশেষ NO (অ্যালার্ম)", AMBER, AMBERBG))):
        cx = 190 + i * 286
        w = tw(pair, T_BODY, 700) + 40
        s.rect(cx - w / 2, 510, w, 44, bg, col, 2.2, 9)
        s.text(cx, 540, pair, T_BODY, col, 700, "middle")
        s.text(cx, 584, what, T_SMALL, NAVY, 700, "middle")

    y = note_strip(s, 630, "95 থেকে 98: ওভারলোড রিলের জন্য "
                           "প্রচলিত নম্বর")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_symbols.svg")


# ── ৬. ডায়াল সেটিং ─────────────────────────────────────────────────────
def d06_setting():
    """Schneider LRD12-এর পরিসর 5.5–8 A;  মোটর অধ্যায় ৭-এর 7.37 A।"""
    s = SVG(1240, 680)
    s.title("ডায়ালের সেটিং ও ট্রিপের সীমা", T_TITLE)

    panel(s, 46, 92, 440, 470, "ডায়াল (5.5 – 8 A)")
    cx, cy, R = 266, 350, 132
    s.circle(cx, cy, R + 26, "#EEF3F8", STEEL, 2.4)
    s.circle(cx, cy, R - 34, "#2E6DB4", "#1D4F86", 3)
    a0, a1 = 225, -45                    # ডিগ্রি, ঘড়ির উল্টো দিকে মাপা
    vmin, vmax = 5.5, 8.0

    def ang(v):
        return math.radians(a0 + (a1 - a0) * (v - vmin) / (vmax - vmin))

    for k in range(11):
        v = vmin + k * 0.25
        a = ang(v)
        r0 = R - 6 if k % 2 else R - 18
        s.line(cx + r0 * math.cos(a), cy - r0 * math.sin(a),
               cx + (R + 6) * math.cos(a), cy - (R + 6) * math.sin(a),
               NAVY, 2.6 if k % 2 == 0 else 1.6)
    for v in (5.5, 6.0, 6.5, 7.0, 7.5, 8.0):
        a = ang(v)
        rr = R + 48
        s.text(cx + rr * math.cos(a), cy - rr * math.sin(a) + 8,
               f"{v:g}", T_SMALL, NAVY, 700, "middle")
    a = ang(7.4)
    s.path(f"M {cx} {cy} L {cx + (R - 42) * math.cos(a)} "
           f"{cy - (R - 42) * math.sin(a)}", "#FFFFFF", 9)
    s.circle(cx, cy, 10, "#FFFFFF")
    s.text(cx, cy + 190, "তীর 7.4 A-এ", T_BODY, NAVY, 700, "middle")

    # ── ডানে সংখ্যারেখা ─────────────────────────────────────────
    panel(s, 516, 92, 678, 470, "7.4 A-এ বসালে রিলে কী করে")
    X0, X1, LY = 560, 1150, 330
    vmin2, vmax2 = 6.0, 10.0
    px = lambda v: X0 + (v - vmin2) / (vmax2 - vmin2) * (X1 - X0)
    s.rect(px(6.0), LY - 14, px(7.77) - px(6.0), 28, GREENBG, GREEN, 1.8, 4)
    s.rect(px(7.77), LY - 14, px(8.88) - px(7.77), 28, AMBERBG, AMBER, 1.8,
           4)
    s.rect(px(8.88), LY - 14, px(10) - px(8.88), 28, REDBG, RED, 1.8, 4)
    for v in range(6, 11):
        s.line(px(v), LY + 14, px(v), LY + 26, GREY, 2)
        s.text(px(v), LY + 54, f"{v} A", T_SMALL, GREY, 700, "middle")

    def mark(v, text, sub, col, up):
        x = px(v)
        if up:
            s.path(f"M {x} {LY - 16} L {x} {LY - 70}", col, 2.6)
            s.text(x, LY - 110, text, T_BODY, col, 700, "middle")
            s.text(x, LY - 80, sub, T_SMALL, col, 700, "middle")
        else:
            s.path(f"M {x} {LY + 60} L {x} {LY + 104}", col, 2.6)
            s.text(x, LY + 134, text, T_BODY, col, 700, "middle")
            s.text(x, LY + 164, sub, T_SMALL, col, 700, "middle")

    mark(7.4, "সেটিং 7.4 A", "= মোটরের কারেন্ট", NAVY, True)
    mark(7.77, "1.05 × = 7.77 A", "ট্রিপ করবে না", GREEN, False)
    mark(8.88, "1.2 × = 8.88 A", "2 ঘণ্টার মধ্যে ট্রিপ", RED, True)

    y = note_strip(s, 588, "ডায়ালে মোটরের কারেন্ট বসে; ট্রিপ শুরু হয় "
                           "এর ৫ থেকে ২০ শতাংশ উপরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_setting.svg")


# ── ৭. ট্রিপ ক্লাস ──────────────────────────────────────────────────────
def d07_classes():
    s = SVG(1240, 640)
    s.title("৭.২ গুণ কারেন্টে বিভিন্ন ট্রিপ ক্লাসের ট্রিপ-সময়", T_TITLE)

    X0, X1 = 250, 1150
    TMAX = 30
    px = lambda t: X0 + t / TMAX * (X1 - X0)
    rows = [("Class 10A", 2, 10), ("Class 10", 4, 10),
            ("Class 20", 6, 20), ("Class 30", 9, 30)]
    TOP = 150
    for t in range(0, 31, 5):
        s.line(px(t), TOP - 20, px(t), TOP + 4 * 78 - 10, "#E3E9EF", 1.4)
        s.text(px(t), TOP + 4 * 78 + 22, f"{t}", T_SMALL, GREY, 700,
               "middle")
    s.text((X0 + X1) / 2, TOP + 4 * 78 + 60, "সময় (সেকেন্ড), ঠান্ডা অবস্থা থেকে",
           T_BODY, NAVY, 700, "middle")
    for i, (name, lo, hi) in enumerate(rows):
        yy = TOP + i * 78
        s.text(X0 - 24, yy + 18, name, T_NAME, NAVY, 700, "end")
        col, bg = (AMBER, AMBERBG) if lo < 5 else (GREEN, GREENBG)
        s.rect(px(lo), yy - 6, px(hi) - px(lo), 36, bg, col, 2.4, 6)
        s.text(px(hi) + 12, yy + 20, f"{lo}–{hi} s", T_BODY, col, 700,
               "start")

    # ৫ সেকেন্ডে চালু হওয়া মোটর
    xm = px(5)
    s.path(f"M {xm} {TOP - 34} L {xm} {TOP + 4 * 78 - 10}", RED, 3,
           dash="9 6")
    s.text(xm + 10, TOP - 38, "মোটর চালু হতে লাগে 5 s", T_BODY, RED, 700,
           "start")

    y = note_strip(s, TOP + 4 * 78 + 92, "ক্লাস 10A ও 10-এর রিলে মোটর চালু "
                                         "হওয়ার আগেই ট্রিপ করতে পারে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_classes.svg")


# ── ৮. পাওয়ার সার্কিট ──────────────────────────────────────────────────
def d08_power():
    s = SVG(1240, 900)
    s.title("DOL স্টার্টারের পাওয়ার সার্কিট", T_TITLE)

    PH = [(470, "L1"), (590, "L2"), (710, "L3")]
    TOP, Q_Y, KM_Y, F_Y, MOT_Y = 130, 230, 400, 570, 740

    # প্রতিটি ফেজের আলাদা টার্মিনাল — তিন ফেজকে এক দাগে জুড়লে সেটা
    # ফেজ-টু-ফেজ শর্ট হয়ে যায়
    s.text(430, TOP + 9, "সরবরাহ", T_BODY, NAVY, 700, "end")
    for x, nm in PH:
        node(s, x, TOP, LIVE)
        s.text(x, TOP - 22, nm, T_BODY, LIVE, 700, "middle")
        s.path(f"M {x} {TOP} L {x} {Q_Y - 42}", LIVE, 4)

    # Q1 — MCCB
    s.rect(430, Q_Y - 42, 320, 84, PLATE, NAVY, 2.6, 8)
    for x, _ in PH:
        s.path(f"M {x} {Q_Y - 26} L {x} {Q_Y + 26}", NAVY, 3.4)
    s.path(f"M 470 {Q_Y} L 710 {Q_Y}", NAVY, 2.2, dash="7 5")
    s.text(780, Q_Y - 6, "Q1 — MCCB / MCB", T_BODY, NAVY, 700, "start")
    s.text(780, Q_Y + 24, "শর্ট সার্কিট সুরক্ষা", T_SMALL, GREY, 400,
           "start")
    for x, _ in PH:
        s.path(f"M {x} {Q_Y + 42} L {x} {KM_Y - 54}", LIVE, 4)

    # KM1 — মেইন কন্টাক্ট
    s.rect(426, KM_Y - 54, 328, 112, "#FBFCFD", GREEN, 2.4, 8)
    for i, (x, _) in enumerate(PH):
        node(s, x, KM_Y - 34, LIVE)
        s.path(f"M {x} {KM_Y - 34} L {x + 36} {KM_Y + 20}", LIVE, 4)
        node(s, x, KM_Y + 34, LIVE)
        s.text(x - 16, KM_Y - 30, str(2 * i + 1), T_SMALL, NAVY, 700, "end")
        s.text(x - 16, KM_Y + 48, str(2 * i + 2), T_SMALL, NAVY, 700, "end")
    s.path(f"M 470 {KM_Y} L 710 {KM_Y}", GREEN, 2.2, dash="7 5")
    s.text(780, KM_Y - 6, "KM1 — কন্টাক্টর", T_BODY, GREEN, 700, "start")
    s.text(780, KM_Y + 24, "চালু-বন্ধ", T_SMALL, GREY, 400, "start")
    for x, _ in PH:
        s.path(f"M {x} {KM_Y + 58} L {x} {F_Y - 50}", LIVE, 4)

    # F2 — থার্মাল উপাদান
    s.rect(426, F_Y - 50, 328, 100, "#FFFBF2", AMBER, 2.4, 8)
    for i, (x, _) in enumerate(PH):
        s.path(f"M {x} {F_Y - 50} L {x} {F_Y - 28}", LIVE, 4)
        thermal_sym(s, x, F_Y, 40, 56, LIVE, 3.4)
        s.path(f"M {x} {F_Y + 28} L {x} {F_Y + 50}", LIVE, 4)
        s.text(x - 12, F_Y + 80, f"{2 * i + 2}/T{i + 1}", T_TINY, NAVY, 700,
               "end")
    s.text(780, F_Y - 6, "F2 — ওভারলোড রিলে", T_BODY, AMBER, 700, "start")
    s.text(780, F_Y + 24, "95-96 যায় কন্ট্রোলে", T_SMALL, GREY, 400,
           "start")
    for x, _ in PH:
        s.path(f"M {x} {F_Y + 50} L {x} {MOT_Y - 90}", LIVE, 4)

    # মোটর
    # তিনটি লিড মোটরের বৃত্তে তিনটি আলাদা বিন্দুতে ঢোকে — এক বিন্দুতে
    # মিললে ছবিটি তিন ফেজের শর্ট বোঝায়
    for x, nm, ex in ((470, "U", 560), (590, "V", 590), (710, "W", 620)):
        ey = MOT_Y - (46 if ex == 590 else 35)
        s.path(f"M {x} {MOT_Y - 90} L {x} {MOT_Y - 50} L {ex} {ey}"
               if x != 590 else f"M 590 {MOT_Y - 90} L 590 {ey}",
               LIVE, 4)
        if x < 590:
            s.text(x - 12, MOT_Y - 52, nm, T_SMALL, NAVY, 700, "end")
        elif x > 590:
            s.text(x + 12, MOT_Y - 52, nm, T_SMALL, NAVY, 700, "start")
        else:
            s.text(x - 12, MOT_Y - 58, nm, T_SMALL, NAVY, 700, "end")
    s.circle(590, MOT_Y, 46, "#FFFFFF", SYM, 3.6)
    s.text(590, MOT_Y - 4, "M", T_NODE, SYM, 700, "middle")
    s.text(590, MOT_Y + 26, "3 ~", T_SMALL, SYM, 700, "middle")
    # আর্থ
    s.path(f"M 636 {MOT_Y} L 780 {MOT_Y}", GREEN, 3)
    s.text(792, MOT_Y + 8, "PE — মোটরের বডি আর্থে", T_BODY, GREEN, 700,
           "start")

    y = note_strip(s, 812, "প্রতিটি ফেজ Q1, KM1 ও F2-এর ভেতর দিয়ে "
                           "সিরিজে মোটরে যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_power.svg")


# ── ৯-১০. কন্ট্রোল সার্কিট ──────────────────────────────────────────────
# ব্লেডের জ্যামিতি এক জায়গায় — বোতামের ড্যাশ-রেখা ঠিক ব্লেডের গায়ে
# এসে থামাতে হলে এই মাপগুলোই লাগে।
NC_RUN, NC_RISE = 104, 34        # বন্ধ NC ব্লেড
NC_ORUN, NC_ORISE = 78, 48       # খোলা NC ব্লেড
NO_RISE = 44                     # খোলা NO ব্লেড


def nc_tip(x, LY, cx, opened=False):
    """`_nc`-এর ব্লেড cx বিন্দুতে যে উচ্চতায় আছে।"""
    run, rise = (NC_ORUN, NC_ORISE) if opened else (NC_RUN, NC_RISE)
    return LY - rise * min(max((cx - x) / run, 0.0), 1.0)


def no_tip(x, LY, cx, w=92, closed=False):
    """`_no`-এর ব্লেড cx বিন্দুতে যে উচ্চতায় আছে।"""
    if closed:
        return LY
    return LY - NO_RISE * min(max((cx - x) / (w - 14), 0.0), 1.0)


def _pb(s, cx, LY, col, bg, name, tip=None):
    """IEC পুশ বাটন — আড়াআড়ি পাত ও তার দণ্ড, ড্যাশ-রেখা ব্লেড পর্যন্ত।

    আগে এখানে কেবল একটি রঙিন বড়ি বসত আর ড্যাশ-রেখাটি ব্লেডের অনেক
    উপরে থেমে যেত।  ওভাবে আঁকলে প্রতীকটি বোতাম বোঝায় না, নিছক একটি
    রঙিন চিহ্ন মনে হয় — আর যান্ত্রিক সংযোগটি কোন কন্টাক্টকে নাড়ায়
    তা-ও বোঝা যায় না।  IEC 60617 বোতামকে আঁকে আড়াআড়ি পাত আর দণ্ড
    হিসেবে, আর সংযোগটি ড্যাশ-রেখায় কন্টাক্ট ছুঁয়ে তবেই থামে।
    """
    if tip is None:
        tip = LY - 15               # NC ব্লেড বোতামের নিচে যেখানে পড়ে
    PY = LY - 84                    # পাতের উচ্চতা
    s.rect(cx - 21, PY - 19, 42, 19, bg, col, 2.4, 4)
    s.path(f"M {cx - 31} {PY} L {cx + 31} {PY}", col, 3.4)
    s.path(f"M {cx} {PY} L {cx} {tip}", "#3B3B3B", 2.2, dash="7 5")
    s.text(cx, PY - 30, name, T_SMALL, col, 700, "middle")


def _nc(s, x, LY, col, opened=False):
    """IEC ব্রেক (NC) কন্টাক্ট।

    ডান টার্মিনাল থেকে একটি খাড়া ঠেস উঠে আসে, আর ব্লেড তার মাথার উপর
    এসে বসে — বন্ধ অবস্থায় পথটি তাই ব্লেড বেয়ে ঠেসে, ঠেস বেয়ে ডান
    নোডে নামে।  আগের ছবিতে ঠেসটি ডান নোড থেকে ১২ px বাঁয়ে আর রেলের ২ px
    উপরে ঝুলে থাকত, অর্থাৎ বন্ধ কন্টাক্টটিই আঁকা হতো খোলা পথ হিসেবে।
    ব্লেড ঠেসটিকে সামান্য পেরিয়ে যায়, নইলে ছবিটা কন্টাক্ট না বুঝিয়ে
    তারের বাঁক মনে হয়।
    """
    RX = x + 92                              # ডান নোড
    BY = LY - NC_RISE                        # ঠেসের মাথা
    node(s, x, LY, col)
    s.path(f"M {RX} {LY} L {RX} {BY}", col, SW)
    if opened:
        s.path(f"M {x} {LY} L {x + NC_ORUN} {LY - NC_ORISE}", DEAD, SW)
    else:
        s.path(f"M {x} {LY} L {x + NC_RUN} {BY}", col, SW)
    node(s, RX, LY, col)


def _no(s, x, LY, col, closed=False, w=92):
    """IEC মেক (NO) কন্টাক্ট — খোলা থাকলে ব্লেড ডান টার্মিনাল ছেড়ে ওঠে।"""
    node(s, x, LY, col)
    if closed:
        s.path(f"M {x} {LY} L {x + w} {LY}", col, SW)
    else:
        s.path(f"M {x} {LY} L {x + w - 14} {LY - NO_RISE}", DEAD, SW)
    node(s, x + w, LY, col)


def _ladder(s, oy, state):
    """state:  "run" — চলছে (হোল্ডিং ধরে রেখেছে);  "trip" — ট্রিপ।"""
    run = state == "run"
    LY = oy + 150
    HB = LY + 96            # হোল্ডিং শাখা
    RL = LY + 184           # চলার বাতির শাখা
    TL = LY + 262           # ট্রিপ বাতির শাখা
    NY = LY + 336
    RX = 1130               # ডান পাশের নিউট্রাল খাড়া
    T = 236                 # ট্রিপ শাখা যেখান থেকে নামে
    AX, BX = 596, 720       # START-এর দুই নোড
    C = 810                 # কয়েলের আগের নোড

    on = LIVE
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")

    # L → F1
    s.path(f"M 82 {LY} L 118 {LY}", on, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 280 {LY}", on, SW)
    node(s, T, LY, on)

    # F2 95-96 — সিরিজে, STOP-এর আগে
    after95 = on if run else DEAD
    _nc(s, 280, LY, on if run else DEAD, opened=not run)
    s.path(f"M 320 {nc_tip(280, LY, 320, opened=not run)} L 320 {LY - 64}", SYM, 2, dash="6 5")
    thermal_sym(s, 320, LY - 88, 34, 40, SYM, 2.4)
    s.text(346, LY - 112, "F2", T_SMALL, AMBER, 700, "start")
    s.text(290, LY + 36, "95", T_TINY, NAVY, 700, "middle")
    s.text(372, LY + 36, "96", T_TINY, NAVY, 700, "middle")

    # STOP — NC
    s.path(f"M 372 {LY} L 424 {LY}", after95, SW)
    _nc(s, 424, LY, after95)
    _pb(s, 470, LY, RED, "#F6C9C4", "STOP")
    s.path(f"M 516 {LY} L {AX} {LY}", after95, SW)

    # START — NO, আর তার সমান্তরালে 13-14
    _no(s, AX, LY, after95, closed=False, w=BX - AX)
    _pb(s, (AX + BX) / 2, LY, GREEN, "#BFE3CE", "START",
        tip=no_tip(AX, LY, (AX + BX) / 2, BX - AX))
    hcol = on if run else DEAD
    s.path(f"M {AX} {LY} L {AX} {HB} L {AX + 22} {HB}", hcol, SW)
    _no(s, AX + 22, HB, hcol, closed=run, w=80)
    s.path(f"M {AX + 102} {HB} L {BX} {HB} L {BX} {LY}", hcol, SW)
    s.text((AX + BX) / 2, HB + 40, "KM1 13-14", T_SMALL,
           LIVE if run else GREY, 700, "middle")

    # কয়েল
    s.path(f"M {BX} {LY} L 860 {LY}", hcol, SW)
    node(s, C, LY, hcol)
    coil_sym(s, 860, LY - 40, 116, 80, "KM1")
    s.text(850, LY - 50, "A1", T_TINY, NAVY, 700, "end")
    s.text(986, LY - 50, "A2", T_TINY, NAVY, 700, "start")
    s.path(f"M 976 {LY} L {RX} {LY} L {RX} {NY}", NEUT, SW)

    # চলার বাতি — কয়েলের সমান্তরালে
    s.path(f"M {C} {LY} L {C} {RL} L 916 {RL}", hcol, SW)
    lamp(s, 940, RL, 24, on=run)
    s.path(f"M 964 {RL} L {RX} {RL}", NEUT, SW)
    node(s, RX, RL, NEUT)
    s.text(940, RL - 38, "H1 — চলছে", T_SMALL, GREEN, 700, "middle")

    # ট্রিপ বাতি — 97-98 দিয়ে
    tcol = on if not run else DEAD
    s.path(f"M {T} {LY} L {T} {TL} L 440 {TL}", on, SW)
    _no(s, 440, TL, on if not run else DEAD, closed=not run, w=92)
    s.path(f"M 532 {TL} L 916 {TL}", tcol, SW)
    s.path(f"M 486 {no_tip(440, TL, 486, closed=not run)} L 486 {TL - 50}", SYM, 2, dash="6 5")
    s.text(450, TL + 36, "97", T_TINY, NAVY, 700, "middle")
    s.text(524, TL + 36, "98", T_TINY, NAVY, 700, "middle")
    s.text(496, TL - 50, "F2", T_SMALL, AMBER, 700, "start")
    lamp(s, 940, TL, 24, on=not run)
    s.path(f"M 964 {TL} L {RX} {TL}", NEUT, SW)
    node(s, RX, TL, NEUT)
    s.text(940, TL + 52, "H2 — ট্রিপ", T_SMALL, AMBER, 700, "middle")

    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    return NY


def d09_control():
    s = SVG(1240, 700)
    s.title("DOL স্টার্টারের কন্ট্রোল সার্কিট (মোটর চলছে)", T_TITLE)
    ny = _ladder(s, 70, "run")
    y = note_strip(s, ny + 40, "95-96 ও 13-14 বন্ধ, তাই কয়েল টানা এবং "
                               "সবুজ বাতি জ্বলছে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_control.svg")


def d10_trip():
    s = SVG(1240, 700)
    s.title("ওভারলোডে ট্রিপের পর কন্ট্রোল সার্কিট", T_TITLE)
    ny = _ladder(s, 70, "trip")
    y = note_strip(s, ny + 40, "95-96 খোলা, ল্যাচ ভাঙা, আর 97-98 বন্ধ "
                               "হয়ে ট্রিপ বাতি জ্বলছে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_trip.svg")


# ── ১১. কানেকশন ডায়াগ্রাম ──────────────────────────────────────────────
# বোতামের সারি বাঁ পাশে, কন্টাক্টর ও রিলের কন্ট্রোল টার্মিনাল বাঁ দিকে
# মুখ করা — ফলে কোনো তার অন্য তারকে কাটে না।  শিকল:
#   L → F1 → F2 95 → F2 96 → STOP 11 → STOP 12 → START 13 → START 14 → A1
#   A2 → N
#   হোল্ডিং:  KM1 13 → (STOP 12 = START 13),  KM1 14 → (START 14 = A1)
def d11_wiring():
    s = SVG(1240, 900)
    s.title("DOL স্টার্টারের কানেকশন ডায়াগ্রাম", T_TITLE)

    def term(x, y, t, w=44, h=26):
        """y = টার্মিনালের উপরের কিনারা।"""
        s.rect(x - w / 2, y, w, h, "#D7E2EC", STEEL, 2, 4)
        s.text(x, y + h - 7, t, T_TINY, NAVY, 700, "middle")

    def sterm(x, cy, t, w=40, h=26):
        """পাশের টার্মিনাল — cy কেন্দ্র।"""
        s.rect(x - w / 2, cy - h / 2, w, h, "#D7E2EC", STEEL, 2, 4)
        s.text(x, cy + 6, t, T_TINY, NAVY, 700, "middle")

    # ── কন্টাক্টর KM1 ────────────────────────────────────────────
    KX, KY, KW, KH = 440, 240, 330, 180
    s.rect(KX, KY, KW, KH, "#EEF3F8", STEEL, 3, 12)
    s.text(KX + KW / 2 + 20, KY + 92, "KM1", 40, STEEL, 700, "middle")
    s.text(KX + KW / 2 + 20, KY + 128, "কন্টাক্টর", T_BODY, GREY, 400,
           "middle")
    MAIN = [545, 610, 675]
    for i, x in enumerate(MAIN):
        term(x, KY - 26, str(2 * i + 1))
        s.path(f"M {x} {KY - 26} L {x} 170", LIVE, 3.6)
        s.text(x, 158, f"L{i + 1}", T_SMALL, LIVE, 700, "middle")
    # তিন ফেজ আলাদা লিড — এক দাগে জুড়লে ফেজ-টু-ফেজ শর্ট
    s.text(610, 112, "সরবরাহ", T_BODY, LIVE, 700, "middle")
    term(480, KY - 26, "A1")
    term(740, KY - 26, "A2")
    sterm(KX - 22, KY + 50, "14")
    sterm(KX - 22, KY + 110, "13")

    # ── ওভারলোড রিলে F2 — সরাসরি কন্টাক্টরের নিচে ────────────────
    FX, FY, FW, FH = 440, 470, 330, 160
    for x in MAIN:
        s.path(f"M {x} {KY + KH} L {x} {FY}", CU, 7)
    s.rect(FX, FY, FW, FH, "#FFF8EA", AMBER, 3, 12)
    s.text(FX + FW / 2 + 20, FY + 78, "F2", 40, AMBER, 700, "middle")
    s.text(FX + FW / 2 + 20, FY + 114, "ওভারলোড রিলে", T_BODY, GREY, 400,
           "middle")
    for i, x in enumerate(MAIN):
        term(x, FY + FH, f"{2 * i + 2}/T{i + 1}", 56)
        s.path(f"M {x} {FY + FH + 26} L {x} 710", LIVE, 3.6)
        s.text(x, 738, "UVW"[i], T_SMALL, LIVE, 700, "middle")
    s.text(525, 738, "মোটরে", T_BODY, LIVE, 700, "end")
    for t, cy in (("96", FY + 36), ("95", FY + 72), ("97", FY + 108),
                  ("98", FY + 144)):
        sterm(FX - 22, cy, t)
    s.text(300, FY + 196, "97-98: ট্রিপ বাতির জন্য", T_TINY, GREY,
           700, "start")

    # ── বোতাম ও ফিউজ — বাঁ পাশে খাড়া সারি ────────────────────────
    BXc = 200

    def button(top, h, name, sub, col, bg, t_top, t_bot, w=180):
        s.rect(BXc - w / 2, top, w, h, bg, col, 2.8, 10)
        s.text(BXc, top + h / 2 - 4, name, T_NAME, col, 700, "middle")
        s.text(BXc, top + h / 2 + 26, sub, T_TINY, GREY, 700, "middle")
        term(BXc, top - 26, t_top)
        term(BXc, top + h, t_bot)

    button(210, 84, "START", "NO — সবুজ", GREEN, GREENBG, "14", "13")
    button(390, 84, "STOP", "NC — লাল", RED, REDBG, "12", "11")
    button(600, 70, "F1", "কন্ট্রোল ফিউজ", NAVY, PLATE, "", "", w=130)

    # START 13 ↔ STOP 12, জোড় J13
    s.path("M 200 320 L 200 364", NAVY, 3)
    node(s, 200, KY + 110, NAVY)
    # STOP 11 → F2 96
    s.path(f"M 200 500 L 200 {FY + 36} L {FX - 42} {FY + 36}", NAVY, 3)
    # F1 → F2 95
    s.path(f"M 200 574 L 200 {FY + 72} L {FX - 42} {FY + 72}", NAVY, 3)
    # কন্ট্রোল সরবরাহ → F1
    s.path("M 60 730 L 200 730 L 200 696", LIVE, 3)
    s.text(60, 764, "কন্ট্রোল সরবরাহ L", T_SMALL, LIVE, 700, "start")
    # START 14 → A1, জোড় J14
    s.path("M 200 184 L 200 130 L 480 130 L 480 214", NAVY, 3)
    node(s, 330, 130, NAVY)
    s.text(300, 118, "START 14 → A1", T_SMALL, NAVY, 700, "middle")
    # A2 → N
    s.path("M 740 214 L 740 130 L 1150 130", NEUT, 3)
    s.text(1150, 114, "A2 → কন্ট্রোল N", T_SMALL, NEUT, 700, "end")

    # ── হোল্ডিং তার ─────────────────────────────────────────────
    s.path(f"M {KX - 42} {KY + 50} L 330 {KY + 50} L 330 130", GREEN, 3,
           dash="9 6")
    s.path(f"M {KX - 42} {KY + 110} L 200 {KY + 110}", GREEN, 3, dash="9 6")
    s.text(330, KY + 138, "হোল্ডিং তার", T_SMALL, GREEN, 700, "start")

    # ডান পাশের ব্যাখ্যা
    s.rect(830, 300, 350, 330, LIGHT, STEEL, 2, 10)
    for i, t in enumerate(("তারের ক্রম:", "L → F1 → 95 → 96",
                           "→ STOP → START → A1", "A2 → N", "",
                           "হোল্ডিং: KM1 13-14", "START-এর দুই মাথায়")):
        if t:
            s.text(1005, 346 + i * 40, t, T_SMALL,
                   NAVY if i not in (0, 5) else STEEL, 700, "middle")

    y = note_strip(s, 800, "রিলের 95-96 কয়েলের সার্কিটে সিরিজে; এটি বাদ "
                           "দিলে ওভারলোড সুরক্ষা থাকে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_wiring.svg")


# ── ১২. বাস্তব DOL স্টার্টার ────────────────────────────────────────────
def d12_starter():
    return photo_callouts(
        "d12_starter", "একটি বাস্তব DOL স্টার্টারের ভেতর", "ph_starter.jpg",
        left=[("ওভারলোড রিলে", 0.180, 0.120),
              ("কন্টাক্টরের টার্মিনাল", 0.270, 0.350),
              ("আর্ক-ঢাকনা", 0.200, 0.480),
              ("চুম্বক ও কয়েলের খাঁচা", 0.400, 0.640)],
        right=[("সেটিং স্কেল 20-32 A", 0.590, 0.150),
               ("ব্যাকআপ ফিউজ সর্বোচ্চ 63 A", 0.520, 0.195),
               ("রিলে-কন্টাক্টরের সংযোগ", 0.780, 0.260),
               ("কন্টাক্টর 25 A", 0.620, 0.770)],
        note="দেশের বাজারে প্রচলিত নকশা: উপরে রিলে, নিচে কন্টাক্টর, "
             "এক বাক্সে",
        iw=430)


# ── ১৩. সিঙ্গেল ফেজ মোটরে তিন পোল সিরিজে ─────────────────────────────
def d13_single():
    s = SVG(1240, 560)
    s.title("সিঙ্গেল ফেজ মোটরে ওভারলোড রিলের তিন পোল সিরিজে", T_TITLE)

    Y1, Y2 = 170, 350
    xs = [470, 590, 710]
    s.path(f"M 420 {Y1 + 36} L 760 {Y1 + 36} L 760 {Y1 + 144} "
           f"L 420 {Y1 + 144} Z", AMBER, 2.2, dash="8 6")
    s.text(790, Y1 + 96, "F2", T_NODE, AMBER, 700, "start")
    for i, x in enumerate(xs):
        s.text(x - 14, Y1 + 20, str(2 * i + 1), T_SMALL, NAVY, 700, "end")
        s.text(x - 14, Y2 - 2, f"{2 * i + 2}", T_SMALL, NAVY, 700, "end")
        s.path(f"M {x} {Y1} L {x} {Y1 + 62}", LIVE, 4)
        thermal_sym(s, x, Y1 + 90, 40, 56, LIVE, 3.4)
        s.path(f"M {x} {Y1 + 118} L {x} {Y2}", LIVE, 4)
    # সরবরাহ → 1
    s.path(f"M 250 {Y1 - 40} L 470 {Y1 - 40} L 470 {Y1}", LIVE, 4)
    s.text(236, Y1 - 32, "L (KM1 থেকে)", T_BODY, LIVE, 700, "end")
    # 2 → 3 ও 4 → 5 — জাম্পার
    s.path(f"M 470 {Y2} L 470 {Y2 + 40} L 530 {Y2 + 40} L 530 {Y1 - 20} "
           f"L 590 {Y1 - 20} L 590 {Y1}", AMBER, 4)
    s.path(f"M 590 {Y2} L 590 {Y2 + 40} L 650 {Y2 + 40} L 650 {Y1 - 20} "
           f"L 710 {Y1 - 20} L 710 {Y1}", AMBER, 4)
    s.text(560, Y2 + 76, "জাম্পার", T_SMALL, AMBER, 700, "middle")
    # 6 → মোটর → N
    s.path(f"M 710 {Y2} L 710 {Y2 + 60} L 900 {Y2 + 60} L 900 {Y1 + 118}",
           LIVE, 4)
    s.circle(900, Y1 + 80, 38, "#FFFFFF", SYM, 3.4)
    s.text(900, Y1 + 76, "M", T_NODE, SYM, 700, "middle")
    s.text(900, Y1 + 104, "1 ~", T_TINY, SYM, 700, "middle")
    s.path(f"M 900 {Y1 + 42} L 900 {Y1 - 40} L 1060 {Y1 - 40}", NEUT, 4)
    s.text(1072, Y1 - 32, "N", T_NODE, NEUT, 700, "start")

    y = note_strip(s, Y2 + 104, "তিনটি বাইমেটালই গরম হয়, তাই রিলে একে "
                                "ফেজ চলে যাওয়া হিসেবে ধরে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_single.svg")


# ── ১৪. মোটর প্রোটেকশন সার্কিট ব্রেকার ─────────────────────────────────
def d14_mpcb():
    return photo_callouts(
        "d14_mpcb", "মোটর প্রোটেকশন সার্কিট ব্রেকার (MPCB)", "ph_mpcb.jpg",
        left=[("সেটিং ডায়াল 0.55-0.8 A", 0.180, 0.370),
              ("CLASS 10", 0.200, 0.520),
              ("শর্ট সার্কিট ট্রিপ 10 A", 0.140, 0.565),
              ("TEST", 0.090, 0.610)],
        right=[("অক্সিলিয়ারি 13-14 (NO)", 0.800, 0.200),
               ("ট্রিপ-নির্দেশক", 0.440, 0.370),
               ("হাতল (ON / OFF)", 0.660, 0.400),
               ("মোটরে 2/T1 4/T2 6/T3", 0.720, 0.920)],
        note="Siemens 3RV2011: এক যন্ত্রে ওভারলোড ও শর্ট সার্কিট "
             "সুরক্ষা",
        iw=370)


ALL = [d01_block, d02_current, d03_olr, d04_bimetal, d04b_open,
       d05_symbols, d06_setting, d07_classes, d08_power, d09_control,
       d10_trip, d11_wiring, d12_starter, d13_single, d14_mpcb]


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
