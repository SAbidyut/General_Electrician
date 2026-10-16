# -*- coding: utf-8 -*-
"""অধ্যায় ১১ — ATS : ডায়াগ্রাম।

সহায়কগুলো অধ্যায় ৮, ৯ ও ১০ থেকে আমদানি করা (CLAUDE.md-র নিয়ম)।
`photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই এখানে
`_use_ch11_images()` দিয়ে বদলে নেওয়া হয়েছে।

**কন্ট্রোল সার্কিটের টপোলজি (d06)** — দুই দিকের কন্ট্রোল সরবরাহ
আলাদা:  মেইন দিকের সবকিছু মেইনের L ও N থেকে, জেনারেটর দিকের সবকিছু
জেনারেটরের L ও N থেকে।  দুই দিক জোড়া লাগে কেবল কন্টাক্টরের
অক্সিলিয়ারি কন্টাক্ট দিয়ে (KA1 21-22, KM1 21-22, KM2 21-22) — যাদের
ইনসুলেশন রেটিং 690 V (Siemens 3RT2016-এর ডেটাশিট)।  টাইমারের ছোট
কন্টাক্ট দুই উৎসের মাঝে রাখা হয়নি, কারণ AH3-এর দুই কন্টাক্ট সেটের
মাঝের ইনসুলেশনের কোনো সংখ্যা ডেটাশিটে পাওয়া যায়নি।

    মেইন:  L → F1 → F3 11-14 → P
           P → KT1 (2-7) → N
           P → KT1 8-6 → KA1 কয়েল → N
           P → KA1 13-14 → KM2 21-22 → Q → KM1 কয়েল → N;  Q → H2 → N
    জেন.:  L → F2 → G
           G → KT2 (2-7) → N
           G → KT2 8-6 → KA1 21-22 → KM1 21-22 → R → KM2 কয়েল → N;
           R → H3 → N

মেইন ফিরলে:  KT1 গোনে → KA1 টানে → KA1 21-22 খোলে → KM2 ছাড়ে →
KM2 21-22 বন্ধ হয় → তবেই KM1 টানে।  অর্থাৎ ভাঙা আগে, জোড়া পরে —
d07-এর টাইমিং চার্টে KM2-এর পতন আর KM1-এর ওঠার মাঝের ফাঁকটুকু এই।

**d12-এ তিনটি ক্রসিং ইচ্ছাকৃত** — তিনটি CT-র S1 একদিকে আর S2 একই
সারিতে জুড়তে হলে সমতলে ক্রসিং এড়ানো যায় না।  ক্রসিংয়ে বিন্দু নেই,
আর S1 তারগুলো ফেজের রঙে, S2 কালোয় — চোখে আলাদা থাকে।

**ব্যাক-ফিড (d02)** — 11 kV / 0.4 kV ট্রান্সফরমার উল্টো দিক থেকে
খাওয়ালে একই অনুপাতে ভোল্টেজ বাড়ায়;  তাই ছবিতে কেবল "হাজার ভোল্ট"
জাতীয় কথা, নির্দিষ্ট সংখ্যা নয়।

কালপুরুষের সীমা আগের অধ্যায়গুলোর মতোই — টার্মিনাল, রেটিং, মডেল
নম্বর ল্যাটিন অঙ্কে;  `÷`, `Ω`, `°` ছবিতে নেই।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, chip, callout, coil_sym,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, LIVE, NEUT, DEAD, PLATE, CU)
from dia_ch09 import fuse, lamp, _nc, _no
from dia_ch10 import timer_coil, dno, timing, dim_arrow, TIMEC, TIMEBG
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch11")
IMG = os.path.join(HERE, "assets", "ch11")

MAINC = STEEL             # মেইনের দিক
GENC = AMBER              # জেনারেটরের দিক
PH_R, PH_Y, PH_B = "#C0392B", "#C9A000", "#1F5FBF"


def _use_ch11_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch11_images()
    return C8.photo_callouts(*a, **k)


def earth(s, x, y, col=GREEN):
    """আর্থের প্রতীক — (x, y) থেকে নিচে।"""
    s.path(f"M {x} {y} L {x} {y + 18}", col, 3)
    for i, w in enumerate((26, 17, 8)):
        s.path(f"M {x - w} {y + 18 + i * 8} L {x + w} {y + 18 + i * 8}",
               col, 3)


def meter(s, cx, cy, r, sym, col=NAVY):
    s.circle(cx, cy, r, "#FFFFFF", col, 3.2)
    s.text(cx, cy + T_NODE * 0.36, sym, T_NODE, col, 700, "middle")


# ── ১. ATS-এর ধারণা ────────────────────────────────────────────────────
def d01_idea():
    s = SVG(1240, 660)
    s.title("দুই উৎস ও একটি লোডের মধ্যে ATS", T_TITLE)
    ar = s.arrow_defs(NAVY, "arA", 15)

    def src(y, name, sub, col, bg):
        s.rect(46, y, 300, 120, bg, col, 2.8, 12)
        s.text(196, y + 52, name, T_NAME, col, 700, "middle")
        s.text(196, y + 92, sub, T_SMALL, NAVY, 700, "middle")

    src(110, "মেইন সরবরাহ", "মিটার ও মেইন ব্রেকারের পরে", MAINC, LIGHT)
    src(310, "জেনারেটর", "স্ট্যান্ডবাই উৎস", GENC, AMBERBG)

    # ATS বাক্স
    s.rect(480, 110, 300, 320, "#FBFCFD", NAVY, 3, 14)
    s.text(630, 158, "ATS", T_TITLE, NAVY, 700, "middle")
    A, B, C = (600, 230), (600, 330), (700, 280)
    s.path(f"M 346 170 L 560 170 L 560 {A[1]} L {A[0]} {A[1]}", MAINC, 4)
    s.path(f"M 346 370 L 560 370 L 560 {B[1]} L {B[0]} {B[1]}", GENC, 4)
    node(s, *A, MAINC)
    node(s, *B, GENC)
    node(s, *C, NAVY)
    s.path(f"M {C[0]} {C[1]} L {A[0] + 6} {A[1] + 4}", NAVY, 5)
    s.path(f"M {C[0]} {C[1]} L 894 {C[1]}", NAVY, 4, marker=ar)
    s.text(640, 400, "একবারে একটি উৎস যুক্ত", T_SMALL, GREY, 700, "middle")

    s.rect(894, 220, 300, 120, GREENBG, GREEN, 2.8, 12)
    s.text(1044, 272, "লোড", T_NAME, GREEN, 700, "middle")
    s.text(1044, 312, "বাসবার ও DB", T_SMALL, NAVY, 700, "middle")

    panel(s, 46, 462, 1148, 124, "ATS-এর তিন কাজ")
    for i, t in enumerate(("মেইন যাচাই করে", "উৎস বদলায়",
                           "দুই উৎস আলাদা রাখে")):
        chip(s, 236 + i * 384, 546, t, size=T_BODY)
    y = note_strip(s, 610, "লোড যেকোনো সময় শুধু একটি উৎসের সঙ্গে "
                           "যুক্ত থাকে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. ব্যাক-ফিডের বিপদ ─────────────────────────────────────────────────
def d02_backfeed():
    s = SVG(1240, 640)
    s.title("ইন্টারলক ছাড়া জেনারেটর সংযোগে ব্যাক-ফিড", T_TITLE)
    ar = s.arrow_defs(RED, "arB", 15)
    Y = 250
    # খুঁটি ও লাইনম্যান
    s.rect(150, Y - 20, 14, 290, "#8A6A45", "#6B5033", 2, 2)
    s.path(f"M 60 {Y} L 420 {Y}", NAVY, 4)
    s.text(300, Y - 18, "11 kV লাইন", T_SMALL, NAVY, 700, "middle")
    hx, hy = 206, Y + 40
    s.circle(hx, hy, 16, "#F2C9A0", NAVY, 2.4)
    s.path(f"M {hx} {hy + 16} L {hx} {hy + 86}", NAVY, 4)
    s.path(f"M {hx} {hy + 36} L {hx - 34} {hy + 8} L {hx - 40} {hy - 30}",
           NAVY, 4)
    s.path(f"M {hx} {hy + 36} L {hx + 30} {hy + 60}", NAVY, 4)
    s.path(f"M {hx} {hy + 86} L {hx - 24} {hy + 130}", NAVY, 4)
    s.path(f"M {hx} {hy + 86} L {hx + 20} {hy + 130}", NAVY, 4)
    s.text(206, Y + 220, "মেরামতরত", T_SMALL, RED, 700, "middle")
    s.text(206, Y + 248, "লাইনম্যান", T_SMALL, RED, 700, "middle")

    # ট্রান্সফরমার
    s.circle(466, Y, 34, "#FFFFFF", NAVY, 3)
    s.circle(510, Y, 34, "#FFFFFF", NAVY, 3)
    s.text(488, Y + 70, "ট্রান্সফরমার", T_SMALL, NAVY, 700, "middle")
    s.text(488, Y + 98, "11 / 0.4 kV", T_SMALL, GREY, 700, "middle")
    s.path(f"M 544 {Y} L 780 {Y}", NAVY, 4)
    s.text(662, Y - 18, "0.4 kV লাইন", T_SMALL, NAVY, 700, "middle")

    # বাড়ি
    s.path("M 780 190 L 980 100 L 1180 190", NAVY, 3)
    s.rect(780, 190, 400, 320, "#FBFCFD", NAVY, 3, 4)
    s.rect(810, Y - 30, 110, 60, PLATE, NAVY, 2.4, 6)
    s.text(865, Y + 8, "DB", T_BODY, NAVY, 700, "middle")
    s.path(f"M 780 {Y} L 810 {Y}", NAVY, 4)
    s.path(f"M 920 {Y} L 1060 {Y} L 1060 {Y + 86}", RED, 4)
    s.circle(1060, Y + 130, 44, AMBERBG, GENC, 3.4)
    s.text(1060, Y + 140, "G", T_NODE, GENC, 700, "middle")
    s.text(1060, Y + 210, "জেনারেটর", T_SMALL, GENC, 700, "middle")
    s.text(990, Y + 36, "সরাসরি যুক্ত", T_SMALL, RED, 700, "middle")

    # উল্টো প্রবাহের তীর
    s.path("M 760 150 L 300 150", RED, 3.6, marker=ar)
    s.text(530, 136, "বিদ্যুৎ উল্টো পথে", T_BODY, RED, 700, "middle")

    y = note_strip(s, 560, "ট্রান্সফরমার উল্টো দিকেও ভোল্টেজ বাড়ায়; "
                           "বিদ্যুৎহীন ভাবা লাইনে হাজার ভোল্ট",
                   fill=REDBG, stroke=RED, tcolor=RED)
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_backfeed.svg")


# ── ৩. হাতে চালানো চেঞ্জওভার ────────────────────────────────────────────
def d03_manual():
    s = SVG(1240, 560)
    s.title("ম্যানুয়াল চেঞ্জওভার সুইচের তিন অবস্থান", T_TITLE)
    for i, (pos, lab, col) in enumerate((
            ("I", "অবস্থান I — মেইন", MAINC),
            ("0", "অবস্থান 0 — অফ", GREY),
            ("II", "অবস্থান II — জেনারেটর", GENC))):
        x = 46 + i * 390
        panel(s, x, 92, 368, 360, f"অবস্থান {pos}", col)
        A, B, C = (x + 110, 200), (x + 110, 330), (x + 250, 265)
        s.path(f"M {x + 30} {A[1]} L {A[0]} {A[1]}", MAINC, 4)
        s.path(f"M {x + 30} {B[1]} L {B[0]} {B[1]}", GENC, 4)
        s.text(x + 30, A[1] - 16, "মেইন", T_SMALL, MAINC, 700, "start")
        s.text(x + 30, B[1] + 34, "জেন.", T_SMALL, GENC, 700, "start")
        node(s, *A, MAINC)
        node(s, *B, GENC)
        node(s, *C, NAVY)
        if pos == "I":
            end = (A[0] + 6, A[1] + 4)
        elif pos == "II":
            end = (B[0] + 6, B[1] - 4)
        else:
            end = (x + 150, C[1])
        s.path(f"M {C[0]} {C[1]} L {end[0]} {end[1]}", col if pos != "0"
               else NAVY, 5)
        s.path(f"M {C[0]} {C[1]} L {x + 340} {C[1]}", NAVY, 4)
        s.text(x + 300, C[1] - 16, "লোড", T_SMALL, GREEN, 700, "middle")
        chip(s, x + 184, 410, lab, size=T_SMALL)
    y = note_strip(s, 476, "0 পার না হয়ে এক উৎস থেকে অন্য উৎসে যাওয়া যায় না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_manual.svg")


# ── ৪. ফেজ ফেইলিওর রিলে ─────────────────────────────────────────────────
def _changeover(s, cx, ybot, to14, col):
    """খাড়া চেঞ্জওভার — নিচে কমন 11, উপরে বাঁয়ে 12, ডানে 14।"""
    piv = (cx, ybot - 50)
    s.path(f"M {cx} {ybot} L {cx} {piv[1]}", col, 3.2)
    node(s, *piv, col)
    t12, t14 = (cx - 46, ybot - 150), (cx + 46, ybot - 150)
    for (tx, ty), n in ((t12, "12"), (t14, "14")):
        s.path(f"M {tx} {ty} L {tx} {ty - 40}", col, 3.2)
        node(s, tx, ty, col)
        s.text(tx, ty - 52, n, T_SMALL, NAVY, 700, "middle")
    tgt = t14 if to14 else t12
    s.path(f"M {piv[0]} {piv[1]} L {tgt[0]} {tgt[1] + 6}", LIVE, 4)
    s.text(cx + 24, ybot - 6, "11", T_SMALL, NAVY, 700, "start")


def d04_pfr():
    s = SVG(1240, 700)
    s.title("ফেজ ফেইলিওর রিলের দুই অবস্থা", T_TITLE)

    panel(s, 46, 92, 380, 500, "DIN-রেলের মডিউল")
    bx, by, bw, bh = 146, 170, 180, 360
    s.rect(bx, by, bw, bh, "#F1F4F7", STEEL, 3, 10)
    for i, t in enumerate(("L1", "L2", "L3")):
        x = bx + 36 + i * 54
        s.rect(x - 18, by + 16, 36, 30, "#D7E2EC", STEEL, 2, 4)
        s.text(x, by + 76, t, T_TINY, NAVY, 700, "middle")
    for i, t in enumerate(("11", "12", "14")):
        x = bx + 36 + i * 54
        s.rect(x - 18, by + bh - 46, 36, 30, "#D7E2EC", STEEL, 2, 4)
        s.text(x, by + bh - 58, t, T_TINY, NAVY, 700, "middle")
    s.circle(bx + bw / 2, by + 150, 14, "#F5C542", AMBER, 2.4)
    s.text(bx + bw / 2, by + 196, "LED R (হলুদ)", T_TINY, GREY, 700, "middle")
    s.text(bx + bw / 2, by + 246, "F3", T_NAME, STEEL, 700, "middle")

    for i, (ttl, ok, col, l1, l2) in enumerate((
            ("তিন ফেজ ঠিক", True, GREEN, "রিলে টানা", "11-14 বন্ধ"),
            ("ফেজ নেই বা ক্রম উল্টো", False, RED, "রিলে ছাড়া",
             "11-12 বন্ধ"))):
        x = 456 + i * 374
        panel(s, x, 92, 352, 500, ttl, col)
        _changeover(s, x + 176, 430, ok, SYM)
        s.text(x + 176, 488, l1, T_BODY, col, 700, "middle")
        s.text(x + 176, 526, l2, T_BODY, NAVY, 700, "middle")
    y = note_strip(s, 616, "তিন ফেজ ঠিক থাকলে রিলে টানা থাকে; রিলে বিকল "
                           "হলে 11-14 খুলে যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_pfr.svg")


# ── ৫. পাওয়ার সার্কিট ──────────────────────────────────────────────────
def _pole_col(s, x0, col, qtag, ktag, Q_Y, KM_Y):
    xs = [x0 + 60 * i for i in range(4)]
    # ব্রেকার
    s.rect(xs[0] - 30, Q_Y - 30, 240, 60, PLATE, NAVY, 2.6, 8)
    for x in xs:
        s.path(f"M {x} {Q_Y - 18} L {x} {Q_Y + 18}", NAVY, 3.4)
    s.path(f"M {xs[0]} {Q_Y} L {xs[3]} {Q_Y}", NAVY, 2.2, dash="7 5")
    # কন্টাক্টর — চার পোল, খোলা অবস্থায়
    s.rect(xs[0] - 30, KM_Y - 44, 240, 88, "#FBFCFD", col, 2.4, 8)
    for x in xs:
        node(s, x, KM_Y - 26, col)
        s.path(f"M {x} {KM_Y + 26} L {x - 22} {KM_Y - 18}", col, 4)
        node(s, x, KM_Y + 26, col)
    for x in xs:
        s.path(f"M {x} 150 L {x} {Q_Y - 30}", col, 4)
        s.path(f"M {x} {Q_Y + 30} L {x} {KM_Y - 44}", col, 4)
    return xs


def d05_power():
    s = SVG(1240, 1000)
    s.title("চার পোল কন্টাক্টরসহ ATS-এর পাওয়ার সার্কিট", T_TITLE)
    Q_Y, KM_Y = 200, 400
    BUS = [540, 570, 600, 630]
    names = ["L1", "L2", "L3", "N"]
    s.text(260, 104, "মেইন সরবরাহ", T_NAME, MAINC, 700, "middle")
    s.text(980, 104, "জেনারেটর", T_NAME, GENC, 700, "middle")
    for x0, col in ((170, MAINC), (890, GENC)):
        for i, n in enumerate(names):
            s.text(x0 + 60 * i, 140, n, T_TINY, col, 700, "middle")
    mx = _pole_col(s, 170, MAINC, "Q1", "KM1", Q_Y, KM_Y)
    gx = _pole_col(s, 890, GENC, "Q2", "KM2", Q_Y, KM_Y)
    s.text(392, Q_Y + 8, "Q1 — ব্রেকার", T_BODY, NAVY, 700, "start")
    s.text(848, Q_Y + 8, "Q2 — ব্রেকার", T_BODY, NAVY, 700, "end")
    s.text(392, KM_Y - 8, "KM1", T_BODY, MAINC, 700, "start")
    s.text(848, KM_Y - 8, "KM2", T_BODY, GENC, 700, "end")

    # যান্ত্রিক ইন্টারলক
    IY = KM_Y + 22
    s.path(f"M 392 {IY} L 848 {IY}", NAVY, 2.4, dash="10 6")
    for x, d in ((392, 1), (848, -1)):
        s.poly([(x, IY - 12), (x, IY + 12), (x + d * 18, IY)], NAVY)
    s.text(620, IY + 36, "যান্ত্রিক ইন্টারলক", T_SMALL, NAVY, 700, "middle")

    # ফেজ ফেইলিওর রিলের ট্যাপ
    FB = (430, 250, 170, 70)
    for i, x in enumerate(mx[:3]):
        ty = 262 + i * 22
        node(s, x, ty, MAINC)
        s.path(f"M {x} {ty} L {FB[0]} {ty}", MAINC, 2.4)
    s.rect(*FB, "#F1F4F7", STEEL, 2.6, 8)
    s.text(FB[0] + FB[2] / 2, FB[1] + 44, "F3", T_NAME, STEEL, 700, "middle")
    s.text(FB[0] + FB[2] / 2, FB[1] + 100, "ফেজ ফেইলিওর রিলে", T_TINY,
           GREY, 700, "middle")
    # কন্ট্রোল সরবরাহের ট্যাপ
    node(s, mx[0], 300, MAINC)
    s.path(f"M {mx[0]} 300 L 100 300", MAINC, 2.4)
    s.text(96, 290, "F1", T_SMALL, MAINC, 700, "end")
    node(s, gx[0], 300, GENC)
    s.path(f"M {gx[0]} 300 L 800 300", GENC, 2.4)
    s.text(792, 290, "F2", T_SMALL, GENC, 700, "end")

    # লোড বাসবার
    for i, (y, n) in enumerate(zip(BUS, names)):
        s.path(f"M 150 {y} L 1090 {y}", NAVY, 4.4)
        s.text(1104, y + 7, n, T_TINY, NAVY, 700, "start")
        for xs, col in ((mx, MAINC), (gx, GENC)):
            s.path(f"M {xs[i]} {KM_Y + 44} L {xs[i]} {y}", col, 4)
            node(s, xs[i], y, NAVY)
    # লোডের ফিডার, CT ও মিটারের ট্যাপ
    FX = [560, 620, 680, 740]
    for i, (x, y) in enumerate(zip(FX, BUS)):
        node(s, x, y, NAVY)
        s.path(f"M {x} {y} L {x} 800", NAVY, 4)
    for x in FX[:3]:
        s.ellipse(x, 720, 20, 12, "none", GREEN, 3.4)
    s.text(772, 728, "CT × 3 — অ্যামিটারে", T_SMALL, GREEN, 700, "start")
    for x in FX:
        node(s, x, 670, NAVY)
    s.rect(540, 652, 220, 36, "none", NAVY, 2, 8, dash="6 5")
    s.text(526, 678, "ভোল্টমিটারে চার তার", T_SMALL, NAVY, 700, "end")
    s.rect(480, 800, 340, 72, GREENBG, GREEN, 2.8, 10)
    s.text(650, 846, "লোড (DB)", T_NAME, GREEN, 700, "middle")
    s.text(150, 672, "লোড বাসবার", T_SMALL, NAVY, 700, "start")

    y = note_strip(s, 900, "নিউট্রালসহ চারটি পোলই বদলায়; দুই কন্টাক্টর "
                           "একসঙ্গে চালু হয় না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_power.svg")


# ── ৬. কন্ট্রোল সার্কিট ─────────────────────────────────────────────────
RX, P, CX = 1150, 400, 880       # ডানের নিউট্রাল, বাস, কয়েলের x


def _rail(s, LY, NY, fuse_tag):
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", SYM, SW)
    fuse(s, 154, LY, 72, 42, fuse_tag)
    s.path(f"M 190 {LY} L 230 {LY}", SYM, SW)
    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    s.path(f"M {RX} {LY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)


def _coil(s, y, tag, kind=None, pins=("A1", "A2")):
    if kind:
        timer_coil(s, CX, y - 32, 150, 64, tag, kind)
        s.path(f"M {CX + 150} {y} L {RX} {y}", NEUT, SW)
    else:
        coil_sym(s, CX, y - 32, 130, 64, tag)
        s.path(f"M {CX + 130} {y} L {RX} {y}", NEUT, SW)
    s.text(CX - 6, y - 40, pins[0], T_TINY, NAVY, 700, "end")
    s.text(CX + (156 if kind else 136), y - 40, pins[1], T_TINY, NAVY, 700,
           "start")
    node(s, RX, y, NEUT)


def _contact(s, x, y, kind, tag, a, b, col=SYM):
    if kind == "no":
        _no(s, x, y, col)
    else:
        _nc(s, x, y, col)
    s.text(x + 46, y - 58, tag, T_SMALL, NAVY, 700, "middle")
    s.text(x + 10, y + 36, a, T_TINY, NAVY, 700, "middle")
    s.text(x + 82, y + 36, b, T_TINY, NAVY, 700, "middle")


def _lamp_rung(s, xfrom, y, tag, col):
    s.path(f"M {xfrom} {y} L 921 {y}", SYM, SW)
    lamp(s, 945, y, 24)
    s.path(f"M 969 {y} L {RX} {y}", NEUT, SW)
    node(s, RX, y, NEUT)
    s.text(915, y + 44, tag, T_SMALL, col, 700, "end")


def d06_control():
    s = SVG(1240, 1240)
    s.title("ATS-এর কন্ট্রোল সার্কিট", T_TITLE)

    # ── মেইন দিক ─────────────────────────────────────────────
    panel(s, 30, 92, 1180, 566, "মেইন অংশ: সরবরাহ মেইনের L ও N", MAINC)
    LY = 230
    R2, R3, R4, NY = LY + 120, LY + 240, LY + 320, LY + 400
    _rail(s, LY, NY, "F1")
    _contact(s, 230, LY, "no", "F3", "11", "14")
    s.path(f"M 322 {LY} L {CX} {LY}", SYM, SW)
    node(s, P, LY)
    _coil(s, LY, "KT1", "on", ("2", "7"))
    s.text(560, LY - 16, "মেইন ঠিক থাকলে", T_TINY, GREY, 700, "middle")

    s.path(f"M {P} {LY} L {P} {R3}", SYM, SW)
    node(s, P, R2)
    node(s, P, R3)
    # রাং ২: KT1 8-6 → KA1
    s.path(f"M {P} {R2} L 500 {R2}", SYM, SW)
    dno(s, 500, R2, SYM, "on")
    s.text(560, R2 - 70, "KT1", T_SMALL, TIMEC, 700, "start")
    s.text(510, R2 + 36, "8", T_TINY, NAVY, 700, "middle")
    s.text(584, R2 + 36, "6", T_TINY, NAVY, 700, "middle")
    s.path(f"M 592 {R2} L {CX} {R2}", SYM, SW)
    _coil(s, R2, "KA1")
    # রাং ৩: KA1 13-14 → KM2 21-22 → KM1
    s.path(f"M {P} {R3} L 470 {R3}", SYM, SW)
    _contact(s, 470, R3, "no", "KA1", "13", "14")
    s.path(f"M 562 {R3} L 630 {R3}", SYM, SW)
    _contact(s, 630, R3, "nc", "KM2", "21", "22", GENC)
    s.path(f"M 722 {R3} L {CX} {R3}", SYM, SW)
    Q = 800
    node(s, Q, R3)
    _coil(s, R3, "KM1")
    s.path(f"M {Q} {R3} L {Q} {R4}", SYM, SW)
    _lamp_rung(s, Q, R4, "H2 — লোড মেইনে", MAINC)

    # ── জেনারেটর দিক ─────────────────────────────────────────
    panel(s, 30, 688, 1180, 450, "জেনারেটর অংশ: সরবরাহ জেনারেটরের L ও N",
          GENC)
    LY = 826
    G2, G3, NY = LY + 120, LY + 200, LY + 280
    _rail(s, LY, NY, "F2")
    s.path(f"M 230 {LY} L {CX} {LY}", SYM, SW)
    node(s, P, LY)
    _coil(s, LY, "KT2", "on", ("2", "7"))
    s.path(f"M {P} {LY} L {P} {G2}", SYM, SW)
    node(s, P, G2)
    s.path(f"M {P} {G2} L 430 {G2}", SYM, SW)
    dno(s, 430, G2, SYM, "on")
    s.text(490, G2 - 70, "KT2", T_SMALL, TIMEC, 700, "start")
    s.text(440, G2 + 36, "8", T_TINY, NAVY, 700, "middle")
    s.text(514, G2 + 36, "6", T_TINY, NAVY, 700, "middle")
    s.path(f"M 522 {G2} L 580 {G2}", SYM, SW)
    _contact(s, 580, G2, "nc", "KA1", "21", "22", MAINC)
    s.path(f"M 672 {G2} L 700 {G2}", SYM, SW)
    _contact(s, 700, G2, "nc", "KM1", "21", "22", MAINC)
    s.path(f"M 792 {G2} L {CX} {G2}", SYM, SW)
    Rn = 836
    node(s, Rn, G2)
    _coil(s, G2, "KM2")
    s.path(f"M {Rn} {G2} L {Rn} {G3}", SYM, SW)
    _lamp_rung(s, Rn, G3, "H3 — লোড জেনারেটরে", GENC)

    y = note_strip(s, 1162, "দুই অংশের সংযোগ শুধু কন্টাক্টরের NC দিয়ে; "
                            "একটি চালু হলে অন্যটির পথ খোলা")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_control.svg")


# ── ৭. ঘটনার ক্রম ──────────────────────────────────────────────────────
def d07_timing():
    s = SVG(1240, 780)
    s.title("মেইন বিচ্ছিন্ন হওয়া থেকে ফিরে আসা পর্যন্ত ATS-এর টাইমিং চার্ট", T_TITLE)
    px, lows = timing(s, 330, 96, 860,
                      [("মেইন", [(0, 3), (9, 16)], MAINC),
                       ("জেনারেটর", [(4, 14.5)], GENC),
                       ("KA1", [(0, 3), (12, 16)], TIMEC),
                       ("KM1 · লোড মেইনে", [(0, 3), (12.3, 16)], LIVE),
                       ("KM2 · লোড জেনারেটরে", [(6, 12)], GREEN)],
                      16, RH=92)
    for t in (3, 4, 6, 9, 12):
        s.path(f"M {px(t)} {lows[0] - 44} L {px(t)} {lows[4] + 16}", GREY,
               1.6, dash="6 5")
    dim_arrow(s, px(4), px(6), lows[4] + 48, "t2", RED, below=True)
    dim_arrow(s, px(9), px(12), lows[4] + 48, "t1", RED, below=True)
    s.text(px(4.5), lows[4] + 110, "লোড বিদ্যুৎহীন: 3 থেকে 6", T_SMALL, RED,
           700, "middle")
    y = note_strip(s, lows[4] + 140, "মেইন ফেরার পর t1 সময় লোড জেনারেটরেই থাকে, "
                                     "তারপর বদল হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_timing.svg")


# ── ৮. প্যানেলের ভেতর ও দরজা ─────────────────────────────────────────────
def d08_panel():
    s = SVG(1240, 1000)
    s.title("ATS প্যানেলের ভেতরের বিন্যাস ও দরজা", T_TITLE)

    panel(s, 46, 92, 720, 820, "ভেতরের মাউন্টিং প্লেট")
    s.rect(80, 150, 652, 690, "#F4F6F8", STEEL, 3, 6)

    def duct(y):
        s.rect(100, y, 612, 30, "#DDE3E9", "#AEB8C2", 1.6, 3)

    def dev(x, y, w, h, tag, sub, col=STEEL, bg="#FFFFFF"):
        s.rect(x, y, w, h, bg, col, 2.6, 8)
        s.text(x + w / 2, y + h / 2 + 2, tag, T_NAME, col, 700, "middle")
        s.text(x + w / 2, y + h / 2 + 34, sub, T_TINY, GREY, 700, "middle")

    dev(110, 180, 250, 110, "Q1", "মেইন ব্রেকার", MAINC)
    dev(450, 180, 250, 110, "Q2", "জেন. ব্রেকার", GENC)
    duct(310)
    dev(110, 360, 130, 130, "KM1", "4 পোল", MAINC)
    dev(260, 360, 130, 130, "KM2", "4 পোল", GENC)
    dev(430, 360, 110, 130, "KA1", "রিলে", STEEL)
    dev(580, 360, 120, 130, "F3", "ফেজ রিলে", STEEL)
    s.path("M 240 380 L 260 380", NAVY, 3)
    duct(510)
    dev(110, 560, 130, 130, "KT1", "মেইন টাইমার", TIMEC, TIMEBG)
    dev(260, 560, 130, 130, "KT2", "জেন. টাইমার", TIMEC, TIMEBG)
    dev(430, 560, 110, 130, "F1 F2", "কন্ট্রোল", NAVY, PLATE)
    dev(580, 560, 120, 130, "F4", "মিটার", NAVY, PLATE)
    duct(710)
    s.rect(110, 760, 590, 50, "#E9EEF3", NAVY, 2.4, 4)
    for i in range(20):
        s.line(130 + i * 29, 766, 130 + i * 29, 804, "#9AA6B2", 1.6)
    s.text(405, 870, "X1 টার্মিনাল ব্লক · নিচ দিয়ে তিনটি ক্যাবল", T_SMALL, NAVY,
           700, "middle")

    panel(s, 796, 92, 398, 820, "দরজায়")
    s.rect(830, 150, 330, 690, "#EEF1F4", NAVY, 3, 8)
    for i, (sym, col) in enumerate((("V", NAVY), ("A", NAVY), ("Hz", NAVY))):
        cx = 885 + i * 110
        s.rect(cx - 45, 180, 90, 90, "#FFFFFF", col, 2.6, 4)
        s.text(cx, 236, sym, T_NAME, col, 700, "middle")
    s.text(995, 300, "মিটার 96 × 96", T_SMALL, GREY, 700, "middle")
    for i, t in enumerate(("VSS", "ASS")):
        cx = 885 + i * 110
        s.circle(cx, 360, 28, "#FFFFFF", NAVY, 2.6)
        s.path(f"M {cx} 360 L {cx + 16} {344}", NAVY, 5)
        s.text(cx, 418, t, T_SMALL, NAVY, 700, "middle")
    for row, (lab, yy) in enumerate((("মেইন R Y B", 490),
                                     ("জেনারেটর R Y B", 590))):
        for j, c in enumerate((PH_R, PH_Y, PH_B)):
            s.circle(900 + j * 60, yy, 20, c, NAVY, 2)
        s.text(995, yy + 52, lab, T_SMALL, NAVY, 700, "middle")
    s.circle(900, 700, 24, "#57B87A", NAVY, 2)
    s.circle(900, 780, 24, "#F2B544", NAVY, 2)
    s.text(940, 708, "H2 — মেইনে", T_SMALL, MAINC, 700, "start")
    s.text(940, 788, "H3 — জেনারেটরে", T_SMALL, GENC, 700, "start")

    y = note_strip(s, 936, "বড় যন্ত্র উপরে, ছোট যন্ত্র মাঝে, টার্মিনাল "
                           "সবার নিচে; ক্যাবল ঢোকে নিচ দিয়ে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_panel.svg")


# ── ৯. ভোল্টমিটার ও সিলেক্টর সুইচ ───────────────────────────────────────
def d09_vss():
    s = SVG(1240, 700)
    s.title("ভোল্টমিটার সিলেক্টর সুইচের সংযোগ", T_TITLE)
    XS = [200, 280, 360, 440]
    for x, n, c in zip(XS, ("R", "Y", "B", "N"), (PH_R, PH_Y, PH_B, NEUT)):
        s.text(x, 118, n, T_NODE, c, 700, "middle")
        s.path(f"M {x} 134 L {x} 300", c, 3.6)
        node(s, x, 134, c)
        if n != "N":
            fuse(s, x, 210, 60, 30, None, vertical=True)
    s.text(150, 216, "F4", T_SMALL, NAVY, 700, "end")

    BX, BY, BW, BH = 140, 300, 360, 280
    s.rect(BX, BY, BW, BH, "#F7F9FB", NAVY, 3, 12)
    cx, cy = 320, 452
    s.circle(cx, cy, 58, "#FFFFFF", NAVY, 3)
    pos = [("OFF", 90), ("RY", 45), ("YB", 0), ("BR", -45),
           ("RN", -135), ("YN", 180), ("BN", 135)]
    for t, a in pos:
        r = 96
        tx = cx + r * math.cos(math.radians(a))
        ty = cy - r * math.sin(math.radians(a))
        s.text(tx, ty + 7, t, T_SMALL, NAVY if t != "RY" else RED, 700,
               "middle")
    a = math.radians(45)
    s.path(f"M {cx} {cy} L {cx + 50 * math.cos(a)} {cy - 50 * math.sin(a)}",
           RED, 7)
    s.circle(cx, cy, 10, NAVY)

    # আউটপুট → মিটার
    s.path(f"M {BX + BW} 400 L 780 400 L 780 {452 - 64}", NAVY, 3.4)
    s.path(f"M {BX + BW} 510 L 780 510 L 780 {452 + 64}", NAVY, 3.4)
    meter(s, 780, 452, 64, "V")
    s.text(870, 460, "0 – 500 V", T_BODY, NAVY, 700, "start")
    s.text(620, 386, "মিটারের দুই তার", T_SMALL, GREY, 700, "middle")
    s.text(320, 628, "VSS (7 অবস্থান)", T_BODY, NAVY, 700, "middle")

    y = note_strip(s, 660, "তিনটি লাইন ভোল্টেজ, তিনটি ফেজ ভোল্টেজ এবং "
                           "একটি OFF অবস্থান")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_vss.svg")


# ── ১০. প্যানেলের অ্যামিটার ─────────────────────────────────────────────
def d10_ammeter():
    return photo_callouts(
        "d10_ammeter", "প্যানেল অ্যামিটারের ডায়ালের চিহ্ন",
        "ph_ammeter.jpg",
        left=[("মুভিং-আয়রন যন্ত্র", 0.175, 0.515),
              ("AC (~)", 0.232, 0.537),
              ("অ্যাকুরেসি ক্লাস 1.5", 0.290, 0.537),
              ("খাড়া করে বসাতে হবে (⊥)", 0.342, 0.530),
              ("পরীক্ষা-ভোল্টেজ 2 kV", 0.392, 0.527)],
        right=[("স্কেল 0 – 10 A", 0.855, 0.280),
               ("মডেল নম্বর", 0.695, 0.537),
               ("জিরো অ্যাডজাস্টমেন্ট স্ক্রু", 0.497, 0.820)],
        note="অ্যাকুরেসি ক্লাস 1.5: ত্রুটি পূর্ণ স্কেলের ±1.5 শতাংশের মধ্যে",
        iw=470)


# ── ১১. কারেন্ট ট্রান্সফরমার ────────────────────────────────────────────
def d11_ct():
    s = SVG(1240, 720)
    s.title("কারেন্ট ট্রান্সফরমারের (CT) সংযোগ ও শর্টিং লিংক", T_TITLE)
    ar = s.arrow_defs(RED, "arC", 14)

    panel(s, 46, 92, 640, 520, "সংযোগ")
    X, CY = 250, 330
    s.path(f"M {X} 150 L {X} 560", LIVE, 7)
    s.text(X - 22, 186, "P1", T_BODY, NAVY, 700, "end")
    s.text(X - 22, 548, "P2", T_BODY, NAVY, 700, "end")
    s.text(X + 20, 176, "সরবরাহের দিক", T_TINY, GREY, 700, "start")
    s.text(X + 20, 560, "লোডের দিক", T_TINY, GREY, 700, "start")
    s.path(f"M {X - 30} 230 L {X - 30} 280", RED, 3, marker=ar)
    s.text(X - 42, 262, "Ip", T_SMALL, RED, 700, "end")
    s.ellipse(X, CY, 70, 30, "none", GREEN, 12)
    s.text(X - 90, CY + 8, "CT", T_NAME, GREEN, 700, "end")
    # সেকেন্ডারি
    S1, S2 = (X + 70, CY - 8), (X + 70, CY + 22)
    MX, MY, MR = 560, CY + 30, 56
    s.path(f"M {S1[0]} {S1[1]} L 480 {S1[1]} L 480 250 L {MX} 250 "
           f"L {MX} {MY - MR}", GREEN, 3.4)
    s.path(f"M {S2[0]} {S2[1]} L 420 {S2[1]} L 420 470 L {MX} 470 "
           f"L {MX} {MY + MR}", GREEN, 3.4)
    s.text(348, S1[1] - 14, "S1", T_SMALL, NAVY, 700, "start")
    s.text(348, S2[1] + 30, "S2", T_SMALL, NAVY, 700, "start")
    meter(s, MX, MY, MR, "A")
    node(s, 420, 470, GREEN)
    earth(s, 420, 470)
    s.text(452, 530, "S2 আর্থে", T_SMALL, GREEN, 700, "start")
    s.text(300, 220, "100 / 5 A", T_BODY, GREEN, 700, "start")

    panel(s, 716, 92, 478, 520, "মিটার খোলার আগে", RED)
    for i, t in enumerate(("S1", "S2")):
        x = 880 + i * 150
        s.rect(x - 40, 220, 80, 70, "#D7E2EC", STEEL, 2.4, 6)
        s.text(x, 266, t, T_BODY, NAVY, 700, "middle")
        s.circle(x, 330, 12, "#FFFFFF", NAVY, 2.4)
        s.path(f"M {x} 290 L {x} 318", NAVY, 3)
    s.rect(868, 318, 174, 24, "#E0A43A", AMBER, 2.4, 6)
    s.text(955, 392, "শর্টিং লিংক", T_BODY, AMBER, 700, "middle")
    s.text(955, 460, "আগে S1-S2 শর্ট করুন,", T_BODY, NAVY, 700, "middle")
    s.text(955, 500, "তারপর মিটার খুলুন", T_BODY, NAVY, 700, "middle")

    y = note_strip(s, 636, "চালু লাইনে CT-র সেকেন্ডারি খোলা থাকলে "
                           "বিপজ্জনক উঁচু ভোল্টেজ ওঠে",
                   fill=REDBG, stroke=RED, tcolor=RED)
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_ct.svg")


# ── ১২. তিন CT, অ্যামিটার সিলেক্টর সুইচ ─────────────────────────────────
def d12_ass():
    s = SVG(1240, 720)
    s.title("তিন CT, অ্যামিটার সিলেক্টর সুইচ ও একটি অ্যামিটার", T_TITLE)
    ar = s.arrow_defs(NAVY, "arD", 13)
    XS = [220, 340, 460]
    COLS = [PH_R, PH_Y, PH_B]
    BUSY = 580
    BX, BY, BW, BH = 660, 330, 220, 170
    for i, (x, c, n) in enumerate(zip(XS, COLS, ("R", "Y", "B"))):
        s.text(x, 114, n, T_NODE, c, 700, "middle")
        s.path(f"M {x} 130 L {x} 300", c, 5, marker=ar)
        s.ellipse(x, 210, 40, 16, "none", GREEN, 8)
        # S1 — ডানে, ফেজের রঙে
        y1 = 380 + i * 40
        s.path(f"M {x + 18} 226 L {x + 18} {y1} L {BX} {y1}", c, 3.2)
        # S2 — বাঁয়ে, কালো
        s.path(f"M {x - 18} 226 L {x - 18} {BUSY}", NEUT, 3.2)
        node(s, x - 18, BUSY, NEUT)
        s.text(x + 26, 256, "S1", T_TINY, NAVY, 700, "start")
        s.text(x - 26, 256, "S2", T_TINY, NAVY, 700, "end")
    s.text(530, 300, "লোডে", T_SMALL, GREY, 700, "middle")

    s.rect(BX, BY, BW, BH, "#F7F9FB", NAVY, 3, 12)
    s.text(BX + BW / 2, BY + 62, "ASS", T_NAME, NAVY, 700, "middle")
    s.text(BX + BW / 2, BY + 104, "OFF · R · Y · B", T_SMALL, NAVY, 700,
           "middle")
    s.text(BX + BW / 2, BY + 142, "4 অবস্থান", T_TINY, GREY, 700, "middle")
    s.path(f"M {BX + BW} 380 L 1040 380 L 1040 {430 - 56}", NAVY, 3.4)
    meter(s, 1040, 430, 56, "A")
    s.path(f"M 1040 {430 + 56} L 1040 {BUSY} L {XS[0] - 18} {BUSY}", NEUT,
           3.2)
    node(s, 1040, BUSY, NEUT)
    s.text(1110, 438, "0 – 100 A", T_SMALL, NAVY, 700, "start")
    earth(s, XS[0] - 18, BUSY)
    s.text(540, BUSY + 36, "S2-এর সাধারণ তার, এক জায়গায় আর্থ করা", T_SMALL,
           NAVY, 700, "start")

    y = note_strip(s, 648, "যে ফেজ দেখানো হচ্ছে না, তার CT সুইচের ভেতরে "
                           "শর্ট থাকে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d12_ass.svg")


ALL = [d01_idea, d02_backfeed, d03_manual, d04_pfr, d05_power, d06_control,
       d07_timing, d08_panel, d09_vss, d10_ammeter, d11_ct, d12_ass]


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
