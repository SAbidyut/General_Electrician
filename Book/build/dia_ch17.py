# -*- coding: utf-8 -*-
"""অধ্যায় ১৭ — CC ক্যামেরা : ডায়াগ্রাম।

সহায়কগুলো আগের অধ্যায় থেকে আমদানি করা (CLAUDE.md-র নিয়ম):
`panel`, `note_strip`, `node`, `blk`, `chip`, `callout` অধ্যায় ৮ থেকে;
`fuse`, `lamp` অধ্যায় ৯ থেকে;  `earth` অধ্যায় ১১ থেকে;  `dev` অধ্যায়
১৬ থেকে (যন্ত্র-বাক্স — নাম উপরে, রেটিং নিচে)।  `photo_callouts`
অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই `_use_ch17_images()` দিয়ে
বদলে নেওয়া হয়েছে।

**সংখ্যা কোথা থেকে** — ছবির প্রতিটি সংখ্যা আসল ডেটাশিটের, একটিও
বানানো নয়।  পুরো লেখাটি `notes/ch17_datasheets.txt`-এ আছে:

  অ্যানালগ ক্যামেরা  Dahua DH-HAC-HFW1200T-A — 1/2.7 ইঞ্চি CMOS,
        1920x1080, লেন্স 3.6 mm (2.8 ও 6 ঐচ্ছিক), দৃশ্যকোণ যথাক্রমে
        87.5 / 103 / 54.7 ডিগ্রি, IR 30 m, IR LED একটিই, সর্বনিম্ন
        আলো 0.02 lux (IR জ্বললে 0), 12 V DC +/-30 %, সর্বোচ্চ 3.6 W,
        IP67, আউটপুট এক চ্যানেল BNC (HD/CVBS বদলানো যায়)।
        d05, d06, d07 ও d13 এই ক্যামেরার।
  IP ক্যামেরা      Dahua DH-IPC-HFW1230S-S5 — 1/2.8 ইঞ্চি CMOS,
        1920x1080, লেন্স মাউন্ট M12, 2.8 mm (102 ডিগ্রি) ও 3.6 mm
        (84 ডিগ্রি), IR 30 m, 18টি IR LED, H.265/H.264, বিট রেট
        12 kbps থেকে 6144 kbps, RJ-45 10/100, ONVIF Profile S,
        12 V DC বা PoE (802.3af), খরচ 2.3 W (PoE, সাধারণ) থেকে
        5.5 W (PoE, সর্বোচ্চ), IP67।  d04, d09, d10 ও d14-এ।
  DVR (XVR)        Dahua DH-XVR5108HS-4KL-X — 8 চ্যানেল BNC,
        HDCVI/AHD/TVI/CVBS/IP পাঁচ রকম, বিট রেট 32 থেকে 6144 kbps
        প্রতি চ্যানেল, এক SATA পোর্ট 10 TB পর্যন্ত, 12 V DC 2 A,
        HDD ছাড়া 10 W-র কম, RS485 দিয়ে PTZ।  d08 ও d13-এ।
  NVR              Dahua DHI-NVR4108HS-8P-4KS2 — 8টি PoE পোর্ট
        (802.3at/af), **প্রতি পোর্টে সর্বোচ্চ 25.5 W, কিন্তু মোট
        মাত্র 80 W**, ইনকামিং ব্যান্ডউইথ 80 Mbps, বিট রেট 16 kbps
        থেকে 20 Mbps প্রতি চ্যানেল, এক SATA III 6 TB পর্যন্ত,
        48 V DC 2 A, HDD ছাড়া 8.3 W-র কম, ডিকোডিং 2 চ্যানেল 4K বা
        8 চ্যানেল 1080P।  d08, d10 ও d14-এ।
  ভিডিও বালুন      Hikvision DS-1H18S/E(C) — এক চ্যানেল প্যাসিভ,
        UTP CAT5/5E/6, দূরত্ব সর্বোচ্চ 250 m (PoC ক্যামেরায় 150 m),
        **BNC দিকে 75 ohm, UTP দিকে 100 ohm** — d11-এর পুরো যুক্তি
        এই দুটি সংখ্যার উপরে;  720P থেকে 8MP, অ্যান্টি-ইন্টারফেরেন্স
        60 dB-র বেশি, ESD IEC 61000-4-2 লেভেল ৩, সার্জ 2 kV
        IEC 61000-4-5।  d11 ও d12-এ।

**DORI (d06) — সংখ্যাগুলো দুই জায়গা থেকে মিলিয়ে নেওয়া।**  পিক্সেল
ঘনত্বের চারটি সীমা IEC/EN 62676-4-এর:  উপস্থিতি বোঝা 25, পর্যবেক্ষণ 63,
চেনা 125, শনাক্তকরণ 250 পিক্সেল প্রতি মিটারে (মানুষের মুখ গড়ে 16
সেন্টিমিটার চওড়া ধরে)।  আর দূরত্বগুলো Dahua-র ডেটাশিটের, যার নিজের
পাদটীকায় লেখা "calculated ... according to EN 62676-4"।  **জ্যামিতির
সূত্রে হাতে কষলে দূরত্ব সবসময় ডেটাশিটের চেয়ে কম আসে** — 6 mm লেন্সে
প্রায় 8 শতাংশ, 2.8 mm-এ প্রায় 25 শতাংশ, কারণ চওড়া লেন্সের ব্যারেল
ডিস্টরশন হিসাবের বাইরে।  অর্থাৎ হাতের হিসাব নিরাপদ দিকে ভুল করে।
d06-এ দুটোই পাশাপাশি দেখানো, যাতে পাঠক নিজেই মিলিয়ে নিতে পারে।

**PoE-র পিনআউট (d09) নিয়ে সতর্কতা।**  Mode A (Alternative A,
সাধারণত এন্ডস্প্যান) ডেটা-জোড়া 1-2 ও 3-6 দিয়ে পাওয়ার পাঠায়;  Mode B
(Alternative B, সাধারণত মিডস্প্যান) অব্যবহৃত জোড়া 4-5 ও 7-8 দিয়ে।
IEEE 802.3-এ এন্ডস্প্যান যেকোনো মোড ব্যবহার করতে পারে, তাই "সাধারণত"।  ছবিতে
জোড়ার রং TIA-568B-র ক্রমে, কারণ ph_rj45 ছবিটিও সেই ক্রমের — দুটো
মিলিয়ে দেখলে যেন না ঠকে।

**বালুনের ছবি (d11) কেন এভাবে আঁকা।**  বালুন আসলে একটি ট্রান্সফরমার,
তাই প্রতীকটাও ট্রান্সফরমারের — এক দিকে এক প্রান্ত-ভূমিসহ কুণ্ডলী
(আনব্যালান্সড, 75 ohm), অন্য দিকে মাঝ-বিন্দুহীন কুণ্ডলী
(ব্যালান্সড, 100 ohm)।  নয়েজ কেন কাটে তা দেখাতে দুই তারে **একই
দিকের** তীর আঁকা হয়েছে — কমন-মোড নয়েজ দুই তারে সমান, তাই পার্থক্য
নেওয়ার সময় বাদ পড়ে।  এটাই বালুনের পুরো যুক্তি, আর ছবিটা সেটাই
দেখায়।

**d13 ও d14-এর তারের তালিকা নিজ নিজ ফাংশনের ডকস্ট্রিংয়ে।**  অধ্যায়
১৪-এর শিক্ষা:  কন্ট্রোল বা সংযোগের ছবি আঁকার **আগে** টার্মিনাল ধরে
ধরে তারের তালিকা লিখতে হয় — দেখতে ঠিক লাগা ছবিও ভুল নোডে জোড়া
থাকতে পারে, আর তালিকাতেই সেটা ধরা পড়ে।

**ক্রসিং।**  d13 ও d14 দুটোতেই শূন্য ক্রসিং — ক্যামেরাগুলো বাঁ পাশে
উপর থেকে নিচে সাজানো, রেকর্ডারের পোর্টও উপর থেকে নিচে একই ক্রমে,
তাই তারগুলো নেস্ট করে।  `qc.py` ক্রসিং দেখে না;  কোনো তার সরালে
চোখে মিলিয়ে নিতে হবে।

কালপুরুষের সীমা আগের অধ্যায়গুলোর মতোই — টার্মিনাল, রেটিং ও মডেল
নম্বর ল্যাটিন অঙ্কে;  `÷`, `Ω`, `°` ছবিতে নেই ("ohm" ও "ডিগ্রি"
লেখা হয়)।
"""
import math
import os

import dia_ch08 as C8
from dia_ch08 import (panel, note_strip, node, blk, chip, callout,
                      T_TITLE, T_NODE, T_NAME, T_BODY, T_SMALL, T_CALL,
                      T_TINY, SYM, SW, DEAD, PLATE)
from dia_ch09 import fuse, lamp
from dia_ch11 import earth
from dia_ch16 import dev
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch17")
IMG = os.path.join(HERE, "assets", "ch17")

# ── এই অধ্যায়ের রঙের নিয়ম ─────────────────────────────────────────────
# সংকেতের ধরন অনুযায়ী রং, পুরো অধ্যায়ে এক:
VID = "#9A5B12"           # ভিডিও — কোঅক্স / BNC
VIDBG = "#FDF2E0"
NET = "#1D5B8F"           # নেটওয়ার্ক — Cat 6 / RJ45
NETBG = "#E9F1F9"
PWR = "#C0392B"           # পাওয়ার — DC ১২ V
PWRBG = "#FDECEA"
POE = "#6B3FA0"           # PoE — পাওয়ার ও ডেটা একই তারে
POEBG = "#F2ECF9"
IRC = "#8E44AD"           # ইনফ্রারেড আলো
LENS = "#2C3E50"
BODY = "#E7ECF1"          # ক্যামেরার খোল
BODY2 = "#CFD8E0"
SCREEN = "#16283C"


def _use_ch17_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch17_images()
    return C8.photo_callouts(*a, **k)


# ── সাধারণ প্রতীক ──────────────────────────────────────────────────────
def bullet_cam(s, x, y, w=150, h=62, col=BODY, edge="#7C8894", ir=True,
               tag=None, face="right", bracket=True):
    """বুলেট ক্যামেরা — পাশ থেকে দেখা।  `face` লেন্স কোন দিকে।
    ফেরত দেয় লেন্সের কেন্দ্র (cx, cy), যাতে দৃশ্যকোণ আঁকা যায়।"""
    s.rect(x, y, w, h, col, edge, 3, h / 2)
    if face == "right":
        lx = x + w
        s.rect(x + w - 16, y - 5, 22, h + 10, BODY2, edge, 2.6, 6)
        cx = x + w + 6
    else:
        lx = x
        s.rect(x - 6, y - 5, 22, h + 10, BODY2, edge, 2.6, 6)
        cx = x - 6
    cy = y + h / 2
    s.circle(cx, cy, h * 0.30, LENS, "#0E1A24", 2.6)
    s.circle(cx, cy, h * 0.14, "#31465C")
    if ir:                                   # চারপাশে IR LED-র বলয়
        for i in range(8):
            a = 2 * math.pi * i / 8
            s.circle(cx + h * 0.42 * math.cos(a), cy + h * 0.42 * math.sin(a),
                     4.4, "#F3E9FB", IRC, 1.8)
    if bracket:
        bx = x + w * 0.34
        s.path(f"M {bx} {y + h} L {bx} {y + h + 26}", edge, 4)
        s.rect(bx - 26, y + h + 26, 52, 12, edge, edge, 1, 3)
    if tag:
        s.text(x + w / 2, y - 18, tag, T_SMALL, NAVY, 700, "middle")
    return cx, cy


def dome_cam(s, cx, cy, r=46, col=BODY, edge="#7C8894", vandal=False,
             tag=None):
    """ডোম ক্যামেরা — সিলিং থেকে ঝোলানো, অর্ধগোলক।"""
    s.rect(cx - r - 10, cy - 16, 2 * r + 20, 18, col, edge, 3, 6)
    s.path(f"M {cx - r} {cy + 2} A {r} {r} 0 0 0 {cx + r} {cy + 2} Z",
           "#2B3B4B", 3, fill="#3C5063")
    s.circle(cx, cy + r * 0.34, r * 0.26, LENS, "#0E1A24", 2.4)
    if vandal:                               # ভ্যান্ডাল-প্রুফ ধাতব বলয়
        # মোটা ঢালাই-বলয়, চারটি স্ক্রু আর পুরু কাচ — সাধারণ ডোমের
        # সঙ্গে পার্থক্যটা ছবিতে দেখা না গেলে অনুচ্ছেদটাই অর্থহীন।
        s.rect(cx - r - 18, cy - 20, 2 * r + 36, 24, "#8A96A2", "#5A6470",
               3, 6)
        for dx in (-r - 6, -r * 0.34, r * 0.34, r + 6):
            s.circle(cx + dx, cy - 8, 4.4, "#5A6470")
        s.path(f"M {cx - r + 4} {cy + 2} A {r - 4} {r - 4} 0 0 0 "
               f"{cx + r - 4} {cy + 2}", "#94A3B0", 3.4)
    if tag:
        s.text(cx, cy + r + 34, tag, T_SMALL, NAVY, 700, "middle")
    return cx, cy + r * 0.34


def ptz_cam(s, cx, cy, r=44, tag=None):
    """PTZ — উপরে মোটর-আবাস, নিচে ঘূর্ণায়মান গোলক।"""
    s.rect(cx - r - 6, cy - 44, 2 * r + 12, 30, BODY, "#7C8894", 3, 8)
    s.rect(cx - r + 4, cy - 16, 2 * r - 8, 16, BODY2, "#7C8894", 2.6, 4)
    s.circle(cx, cy + r * 0.42, r * 0.80, "#3C5063", "#2B3B4B", 3)
    s.circle(cx, cy + r * 0.42, r * 0.30, LENS, "#0E1A24", 2.4)
    ar = s.arrow_defs(STEEL, "arPT", 11)
    s.path(f"M {cx - r - 22} {cy - 29} A 26 26 0 0 1 {cx + r + 22} {cy - 29}",
           STEEL, 2.6, marker=ar)
    if tag:
        s.text(cx, cy + r + 52, tag, T_SMALL, NAVY, 700, "middle")
    return cx, cy + r * 0.42


def box_cam(s, x, y, w=140, h=58, tag=None):
    """বক্স ক্যামেরা — আলাদা লেন্স লাগানো যায়, তাই লেন্সটা বাইরে।"""
    s.rect(x, y, w, h, BODY, "#7C8894", 3, 7)
    s.rect(x + w, y + h * 0.20, 40, h * 0.60, BODY2, "#7C8894", 2.6, 5)
    s.circle(x + w + 40, y + h / 2, h * 0.24, LENS, "#0E1A24", 2.4)
    bx = x + w * 0.5
    s.path(f"M {bx} {y + h} L {bx} {y + h + 24}", "#7C8894", 4)
    s.rect(bx - 24, y + h + 24, 48, 11, "#7C8894", "#7C8894", 1, 3)
    if tag:
        s.text(x + w / 2, y - 16, tag, T_SMALL, NAVY, 700, "middle")
    return x + w + 40, y + h / 2


def rec_box(s, x, y, w, h, title, sub, col=NAVY, ports=None,
            rports=None):
    """রেকর্ডার (DVR বা NVR) — সামনে নাম, পিছনে পোর্টের সারি।
    `ports` বাঁ কিনারায়, `rports` ডান কিনারায় — দুটোরই (x, y)
    ফেরত আসে, তার জোড়ার জন্য।  **মনিটর ও রাউটারের তার সবসময় ডান
    পাশ দিয়ে** বের করতে হয়;  বাঁ পাশ দিয়ে বের করলে তারটা বাক্সের
    ভেতরের লেখার উপর দিয়ে যায়।"""
    s.rect(x, y, w, h, "#FCFDFE", col, 3.2, 12)
    s.rect(x, y, w, 46, col, col, 1, 12)
    s.text(x + w / 2, y + 32, title, T_NAME, "#FFFFFF", 700, "middle")
    s.text(x + w / 2, y + 78, sub, T_SMALL, GREY, 700, "middle")
    out = []
    if ports:
        n = len(ports)
        y0, y1 = y + 112, y + h - 26
        step = (y1 - y0) / max(n - 1, 1)
        for i, (lab, pc) in enumerate(ports):
            py = y0 + i * step
            s.rect(x - 14, py - 13, 28, 26, "#FFFFFF", pc, 2.6, 4)
            s.text(x + 26, py + T_TINY * 0.34, lab, T_TINY, pc, 700,
                   "start")
            out.append((x - 14, py))
    rout = []
    if rports:
        n = len(rports)
        y0, y1 = y + 112, y + h - 26
        step = (y1 - y0) / max(n + 1, 1)
        for i, (lab, pc) in enumerate(rports):
            py = y0 + (i + 1) * step
            s.rect(x + w - 14, py - 13, 28, 26, "#FFFFFF", pc, 2.6, 4)
            s.text(x + w - 26, py + T_TINY * 0.34, lab, T_TINY, pc, 700,
                   "end")
            rout.append((x + w + 14, py))
    return (out, rout) if rports else out


def rj45(s, cx, cy, w=34, h=28, col=NET):
    """RJ45 প্লাগের ছোট প্রতীক — উপরে ক্লিপ।"""
    s.rect(cx - w / 2, cy - h / 2, w, h, "#FFFFFF", col, 2.4, 3)
    s.rect(cx - 6, cy - h / 2 - 7, 12, 8, "#FFFFFF", col, 2.2, 2)


def bnc(s, cx, cy, r=13, col=VID):
    """BNC কানেক্টরের ছোট প্রতীক — বাইরে বলয়, ভেতরে পিন।"""
    s.circle(cx, cy, r, "#FFFFFF", col, 2.6)
    s.circle(cx, cy, r * 0.32, col)


def cone(s, cx, cy, ang, reach, col=AMBER, bg=AMBERBG, op=0.55, up=0.0):
    """ক্যামেরার দৃশ্যকোণ — লেন্স থেকে ছড়ানো কীলক।  `ang` ডিগ্রিতে,
    `up` কীলকের অক্ষ কত ডিগ্রি উপরে হেলানো।"""
    a0 = math.radians(-ang / 2 - up)
    a1 = math.radians(ang / 2 - up)
    x0, y0 = cx + reach * math.cos(a0), cy + reach * math.sin(a0)
    x1, y1 = cx + reach * math.cos(a1), cy + reach * math.sin(a1)
    s.path(f"M {cx:.1f} {cy:.1f} L {x0:.1f} {y0:.1f} "
           f"A {reach} {reach} 0 0 1 {x1:.1f} {y1:.1f} Z",
           col, 2.2, fill=bg, opacity=op)
    return (x0, y0), (x1, y1)


def person(s, x, y, h=64, col="#3A4652"):
    """দাঁড়ানো মানুষ — মাপের তুলনা বোঝাতে।"""
    r = h * 0.14
    s.circle(x, y - h + r, r, col)
    s.path(f"M {x} {y - h + 2 * r} L {x} {y - h * 0.38}", col, 3.4)
    s.path(f"M {x - h * 0.17} {y - h * 0.62} L {x + h * 0.17} "
           f"{y - h * 0.62}", col, 3.2)
    s.path(f"M {x} {y - h * 0.38} L {x - h * 0.15} {y}", col, 3.2)
    s.path(f"M {x} {y - h * 0.38} L {x + h * 0.15} {y}", col, 3.2)


def monitor(s, x, y, w=210, h=140, tiles=(2, 2), col=NAVY):
    """মনিটর — পর্দায় কয়েকটি ভাগ।"""
    s.rect(x, y, w, h, SCREEN, col, 3.2, 7)
    r, c = tiles
    gx = (w - 14) / c
    gy = (h - 14) / r
    for i in range(r):
        for j in range(c):
            s.rect(x + 7 + j * gx + 2, y + 7 + i * gy + 2, gx - 4, gy - 4,
                   "#26415E", "#3C5F86", 1.4, 3)
    s.rect(x + w / 2 - 34, y + h, 68, 12, col, col, 1, 3)
    s.rect(x + w / 2 - 52, y + h + 12, 104, 10, col, col, 1, 3)


def cable_run(s, d, col, sw=3.6, dash=None, marker=None, label=None,
              lx=None, ly=None, tcol=None):
    """একটি তার — রং দিয়েই বোঝা যায় কোন সংকেত।"""
    s.path(d, col, sw, dash=dash, marker=marker)
    if label:
        s.text(lx, ly, label, T_TINY, tcol or col, 700, "middle")


# ══════════════════════════════════════════════════════════════════════
# ১. সিস্টেমের পাঁচটি অংশ
# ══════════════════════════════════════════════════════════════════════
def d01_system():
    s = SVG(1240, 700)
    s.title("CC ক্যামেরা সিস্টেম — পাঁচটি অংশ", T_TITLE)
    ar = s.arrow_defs(STEEL, "arS", 15)
    ap = s.arrow_defs(PWR, "arP", 13)

    Y = 190
    # ── ক্যামেরা
    bullet_cam(s, 62, Y + 18, 132, 54)
    s.text(128, Y + 132, "১. ক্যামেরা", T_NAME, NAVY, 700, "middle")
    s.text(128, Y + 166, "দৃশ্য থেকে সংকেত", T_SMALL, GREY, 700, "middle")

    # ── ট্রান্সমিশন
    s.path(f"M 216 {Y + 45} L 330 {Y + 45}", STEEL, 4, marker=ar)
    s.rect(348, Y - 4, 214, 152, LIGHT, STEEL, 2.8, 12)
    s.text(455, Y + 42, "২. ট্রান্সমিশন", T_NAME, NAVY, 700, "middle")
    s.text(455, Y + 82, "কোঅক্স + বালুন", T_SMALL, VID, 700, "middle")
    s.text(455, Y + 116, "অথবা Cat 6", T_SMALL, NET, 700, "middle")

    # ── রেকর্ডার
    s.path(f"M 562 {Y + 72} L 640 {Y + 72}", STEEL, 4, marker=ar)
    s.rect(658, Y - 4, 214, 152, "#FCFDFE", NAVY, 3, 12)
    s.text(765, Y + 42, "৩. রেকর্ডার", T_NAME, NAVY, 700, "middle")
    s.text(765, Y + 82, "DVR বা NVR", T_SMALL, GREY, 700, "middle")
    s.text(765, Y + 116, "+ হার্ড ডিস্ক", T_SMALL, GREY, 700, "middle")

    # ── ডিসপ্লে
    s.path(f"M 872 {Y + 72} L 950 {Y + 72}", STEEL, 4, marker=ar)
    monitor(s, 968, Y + 6, 200, 132)
    s.text(1068, Y + 190, "৪. ডিসপ্লে", T_NAME, NAVY, 700, "middle")

    # ── পাওয়ার — নিচে, সবার তলায়
    s.rect(62, 512, 1106, 96, PWRBG, PWR, 2.8, 13)
    s.text(620, 552, "৫. পাওয়ার সাপ্লাই", T_NAME, PWR, 700, "middle")
    s.text(620, 588, "ক্যামেরায় 12 V DC অথবা PoE  ·  রেকর্ডারে "
                     "নিজস্ব অ্যাডাপ্টার", T_SMALL, NAVY, 700, "middle")
    for x in (128, 455, 765, 1068):
        s.path(f"M {x} 470 L {x} 512", PWR, 3, dash="8 6", marker=ap)

    y = note_strip(s, 630, "পাঁচটির যেকোনো একটি দুর্বল হলে পুরো "
                           "সিস্টেম দুর্বল — সবচেয়ে বেশি অবহেলা হয় "
                           "পাঁচ নম্বরটিতে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_system.svg")


# ══════════════════════════════════════════════════════════════════════
# ২. ক্যামেরার ভেতরে
# ══════════════════════════════════════════════════════════════════════
def d02_inside():
    """বাঁ থেকে ডানে আলোর পথ:  দৃশ্য → লেন্স → ICR ফিল্টার → সেন্সর →
    DSP → আউটপুট।  IR LED আলাদা পথে, কারণ ওটা আলো **পাঠায়**।"""
    s = SVG(1240, 790)
    s.title("ক্যামেরার ভেতরে — আলো থেকে সংকেত", T_TITLE)
    al = s.arrow_defs(AMBER, "arL", 14)
    ao = s.arrow_defs(STEEL, "arO", 14)
    ai = s.arrow_defs(IRC, "arI", 13)

    s.rect(58, 140, 1124, 368, "#FBFCFD", LINE, 2.4, 14)
    s.text(1152, 176, "ক্যামেরার খোলের ভেতর", T_SMALL, GREY, 700, "end")

    CY = 310
    # ── দৃশ্য
    s.rect(70, CY - 82, 118, 164, GREENBG, GREEN, 2.6, 10)
    person(s, 129, CY + 52, 84, GREEN)
    s.text(129, CY - 96, "দৃশ্য", T_SMALL, GREEN, 700, "middle")
    for dy in (-34, 0, 34):
        s.path(f"M 196 {CY + dy} L 252 {CY + dy * 0.45}", AMBER, 3,
               dash="10 7", marker=al)

    # ── লেন্স
    s.path(f"M 268 {CY - 66} A 90 90 0 0 1 268 {CY + 66} "
           f"A 90 90 0 0 1 268 {CY - 66} Z", LENS, 3, fill="#BCD6EA")
    s.text(268, CY + 108, "লেন্স", T_SMALL, NAVY, 700, "middle")
    s.text(268, CY + 140, "ফোকাল লেংথ", T_TINY, GREY, 700, "middle")

    # ── ICR ফিল্টার
    s.rect(370, CY - 62, 26, 124, "#E8F0F7", STEEL, 2.8, 4)
    s.path(f"M 383 {CY - 62} L 383 {CY + 62}", STEEL, 2, dash="7 6")
    s.text(383, CY + 108, "ICR ফিল্টার", T_SMALL, NAVY, 700, "middle")
    # দ্বিতীয় সারিতে, কারণ লেখাটা চওড়া — পাশের দুটোর সঙ্গে লেগে যায়
    s.text(383, CY + 176, "দিনে ঢোকে, রাতে সরে", T_TINY, GREY, 700,
           "middle")
    s.path(f"M 340 {CY} L 366 {CY}", AMBER, 3.4, marker=al)

    # ── সেন্সর
    s.rect(470, CY - 66, 92, 132, "#2B3B4B", "#16222E", 3, 6)
    for i in range(6):
        for j in range(4):
            s.rect(478 + j * 20, CY - 58 + i * 20, 15, 15, "#3E5568",
                   "none", 0, 2)
    s.text(516, CY + 108, "ইমেজ সেন্সর", T_SMALL, NAVY, 700, "middle")
    s.text(516, CY + 140, "CMOS · 1920 x 1080", T_TINY, GREY, 700,
           "middle")
    s.path(f"M 400 {CY} L 466 {CY}", AMBER, 3.4, marker=al)

    # ── DSP
    s.rect(640, CY - 62, 150, 124, LIGHT, STEEL, 3, 10)
    s.text(715, CY - 18, "DSP বোর্ড", T_BODY, NAVY, 700, "middle")
    s.text(715, CY + 20, "H.265 / H.264", T_SMALL, STEEL, 700, "middle")
    s.text(715, CY + 50, "এনকোডিং", T_TINY, GREY, 700, "middle")
    s.path(f"M 566 {CY} L 636 {CY}", STEEL, 3.4, marker=ao)

    # ── আউটপুট — দুই রকম
    s.path(f"M 794 {CY - 26} L 866 {CY - 26}", VID, 3.4, marker=ao)
    bnc(s, 886, CY - 26)
    s.text(916, CY - 20, "BNC — অ্যানালগ", T_SMALL, VID, 700, "start")
    s.path(f"M 794 {CY + 26} L 866 {CY + 26}", NET, 3.4, marker=ao)
    rj45(s, 886, CY + 26)
    s.text(916, CY + 32, "RJ45 — IP", T_SMALL, NET, 700, "start")
    s.text(946, CY + 74, "একই ক্যামেরায় দুটো থাকে না —", T_TINY, GREY,
           700, "middle")
    s.text(946, CY + 100, "যেকোনো একটি", T_TINY, GREY, 700, "middle")

    # ── IR LED
    s.rect(240, 168, 200, 60, "#F7EEFC", IRC, 2.6, 10)
    s.text(340, 206, "IR LED", T_BODY, IRC, 700, "middle")
    s.path(f"M 340 228 L 340 {CY - 96}", IRC, 3, dash="9 7", marker=ai)
    s.text(470, 200, "রাতে নিজেই আলো পাঠায়", T_SMALL, IRC, 700, "start")

    y = note_strip(s, 538, "অ্যানালগে এনকোডিং হয় DVR-এ, আর IP "
                           "ক্যামেরায় এনকোডিং হয় ক্যামেরার ভেতরেই")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_inside.svg")


# ══════════════════════════════════════════════════════════════════════
# ৩. আকৃতি অনুযায়ী ধরন
# ══════════════════════════════════════════════════════════════════════
def d03_types():
    s = SVG(1240, 690)
    s.title("আকৃতি অনুযায়ী ক্যামেরার ধরন", T_TITLE)

    Y = 210
    # ── বুলেট
    s.rect(52, 130, 268, 372, "#FBFCFD", LINE, 2.2, 13)
    bullet_cam(s, 88, Y, 142, 56)
    s.text(186, Y + 148, "বুলেট", T_NAME, NAVY, 700, "middle")
    for i, t in enumerate(["বাইরে, দেয়ালে", "কোন দিকে তাকিয়ে",
                           "দূর থেকে বোঝা যায়"]):
        s.text(186, Y + 186 + i * 30, t, T_TINY, GREY, 700, "middle")

    # ── ডোম
    s.rect(336, 130, 268, 372, "#FBFCFD", LINE, 2.2, 13)
    dome_cam(s, 470, Y + 40, 52)
    s.text(470, Y + 148, "ডোম", T_NAME, NAVY, 700, "middle")
    for i, t in enumerate(["ভেতরে, ছাদে", "কোন দিকে তাকিয়ে",
                           "বাইরে থেকে বোঝা যায় না"]):
        s.text(470, Y + 186 + i * 30, t, T_TINY, GREY, 700, "middle")

    # ── ভ্যান্ডাল ডোম
    s.rect(620, 130, 268, 372, "#FBFCFD", LINE, 2.2, 13)
    dome_cam(s, 754, Y + 40, 52, vandal=True)
    s.text(754, Y + 148, "ভ্যান্ডাল ডোম", T_NAME, NAVY, 700, "middle")
    for i, t in enumerate(["ধাতব খোল, মোটা কাচ", "ভাঙচুর ঠেকায়",
                           "সিঁড়ি, লিফট, গেট"]):
        s.text(754, Y + 186 + i * 30, t, T_TINY, GREY, 700, "middle")

    # ── PTZ
    s.rect(904, 130, 284, 372, "#FBFCFD", LINE, 2.2, 13)
    ptz_cam(s, 1046, Y + 36, 46)
    s.text(1046, Y + 148, "PTZ", T_NAME, NAVY, 700, "middle")
    for i, t in enumerate(["ঘোরে, কাত হয়, জুম করে", "অপারেটর চালায়",
                           "RS485 বা নেটওয়ার্কে"]):
        s.text(1046, Y + 186 + i * 30, t, T_TINY, GREY, 700, "middle")

    y = note_strip(s, 528, "বুলেট দেখানোর জন্য, ডোম লুকানোর জন্য, "
                           "ভ্যান্ডাল ডোম টেকার জন্য, PTZ খোঁজার জন্য")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_types.svg")


# ══════════════════════════════════════════════════════════════════════
# ৪. অ্যানালগ বনাম IP
# ══════════════════════════════════════════════════════════════════════
def d04_analog_ip():
    """দুই সারি।  পার্থক্যের জায়গাটা একটাই — **এনকোডিং কোথায় হয়**।
    অ্যানালগে ক্যামেরা কাঁচা ভিডিও পাঠায়, DVR এনকোড করে;  IP-তে
    ক্যামেরা নিজেই এনকোড করে, NVR কেবল জমা রাখে।"""
    s = SVG(1240, 760)
    s.title("অ্যানালগ HD বনাম IP — পার্থক্য কোথায়", T_TITLE)
    av = s.arrow_defs(VID, "arV", 14)
    an = s.arrow_defs(NET, "arN", 14)

    def row(y, col, bg, title, cam_lab, cable, rec, rec_sub, enc,
            arrow, note):
        s.rect(52, y, 1136, 218, bg, col, 2.6, 14)
        # শিরোনাম তারের উপরে, বাঁ কোণে নয় — বাঁ কোণে বসালে
        # নিচের লাল E-র সঙ্গে লেগে যায়।
        s.box_auto(400, y + 14, title, T_BODY, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=22, pad_y=9)
        bullet_cam(s, 96, y + 96, 122, 50, ir=False)
        s.text(157, y + 204, cam_lab, T_TINY, NAVY, 700, "middle")
        s.path(f"M 240 {y + 121} L 560 {y + 121}", col, 4, marker=arrow)
        s.text(400, y + 100, cable, T_SMALL, col, 700, "middle")
        s.rect(596, y + 62, 216, 118, "#FCFDFE", col, 3, 11)
        s.text(704, y + 112, rec, T_NAME, col, 700, "middle")
        s.text(704, y + 150, rec_sub, T_TINY, GREY, 700, "middle")
        s.path(f"M 812 {y + 121} L 900 {y + 121}", col, 4, marker=arrow)
        monitor(s, 918, y + 60, 150, 100, (2, 2), col)
        # এনকোডিং কোথায় — লাল E, যন্ত্রের গায়েই।  লেখা নেই ইচ্ছে
        # করে;  নিচের পটিতে একবারই বোঝানো আছে, তাতে জায়গাও বাঁচে
        # আর দুই সারিতে একই কথা দুবার লিখতে হয় না।
        ex, ey = enc
        s.circle(ex, ey, 18, "#FFFFFF", RED, 3.2)
        s.text(ex, ey + 8, "E", T_BODY, RED, 700, "middle")
        s.text(1108, y + 196, note, T_TINY, GREY, 700, "end")

    row(120, VID, VIDBG, "অ্যানালগ HD", "HDCVI / AHD / TVI",
        "কোঅক্স — কাঁচা ভিডিও", "DVR", "এখানেই এনকোডিং হয়",
        (642, 212), av,
        "ক্যামেরা সস্তা, তার দুটো — ভিডিও ও পাওয়ার আলাদা")
    row(382, NET, NETBG, "IP", "নেটওয়ার্ক ক্যামেরা",
        "Cat 6 — এনকোড করা ডেটা", "NVR", "কেবল জমা রাখে",
        (157, 458), an,
        "ক্যামেরা দামি, PoE হলে তার একটাই")

    y = note_strip(s, 626, "লাল E যেখানে, ছবির মান সেখানেই ঠিক হয় — "
                           "তাই IP-তে লম্বা তারেও মান পড়ে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_analog_ip.svg")


# ══════════════════════════════════════════════════════════════════════
# ৫. ফোকাল লেংথ ও দৃশ্যকোণ
# ══════════════════════════════════════════════════════════════════════
def d05_fov():
    """Dahua DH-HAC-HFW1200T-A-র তিনটি লেন্স, ডেটাশিটের নিজের সংখ্যা:
    2.8 mm — 103 ডিগ্রি, 3.6 mm — 87.5 ডিগ্রি, 6 mm — 54.7 ডিগ্রি।

    **কীলকের দৈর্ঘ্য এখানে মাপে আঁকা** — প্রতিটি ওই লেন্সের *চেনা*
    (Recognize, 125 পিক্সেল প্রতি মিটার) দূরত্ব পর্যন্ত, অর্থাৎ
    যথাক্রমে 8, 11 ও 16 মিটার;  তিনটিই ডেটাশিটের DORI সারণির।
    প্রথম খসড়ায় দৈর্ঘ্যগুলো আন্দাজে নেওয়া হয়েছিল আর নিচে একটা
    মিটার-স্কেল আঁকা ছিল — ছবি দেখে কেউ মাপ মেলাতে গেলে ঠকত।

    কীলক মাপে আঁকলে চওড়াগুলো খুব লম্বা হয়ে ক্যানভাস ছাড়িয়ে যায়
    (103 ডিগ্রি কোণে 372 পিক্সেল পাল্লা মানে উপরে-নিচে 291 পিক্সেল)।
    তাই পুরোটা একটা আয়তক্ষেত্রে **ক্লিপ** করা — যা বাস্তবেও ঠিক,
    কারণ ঘরের দেয়ালেই দৃশ্য শেষ হয়।"""
    s = SVG(1240, 950)
    s.title("একই ক্যামেরা, তিন লেন্স — চওড়া না দূর", T_TITLE)

    X0, PW, PY, PH = 186, 930, 148, 476     # ছকের চৌহদ্দি
    PPM = PW / 20.0                          # ২০ মিটার = ৯৩০ পিক্সেল
    CY = PY + PH / 2

    s.rect(X0, PY, PW, PH, "#FBFCFD", LINE, 2.2, 8)

    # (লেখা-মাপ, কোণ ডিগ্রিতে, চেনার দূরত্ব মিটারে, রং, পটভূমি)
    lenses = [("2.8", 103.0, "103", 8, "#B36B00", "#FFF1D8"),
              ("3.6", 87.5, "87.5", 11, "#1D5B8F", "#E4EFF9"),
              ("6", 54.7, "54.7", 16, "#1B6E47", "#E6F4EC")]

    # বড় কীলক আগে, ছোট পরে — নইলে সবচেয়ে বড়টি উপরে বসে বাকি দুটোকে
    # ঝাপসা করে দেয়।
    s.clip_begin(X0, PY, PW, PH, 8)
    for f, ang, angs, m, col, bg in reversed(lenses):
        cone(s, X0, CY, ang, m * PPM, col, bg, 0.40)
    s.clip_end()

    # ── ক্যামেরা ছকের বাঁ কিনারায়, লেন্স ঠিক শীর্ষবিন্দুতে
    bullet_cam(s, X0 - 124, CY - 26, 112, 52, ir=False)

    # ── প্রতিটি কীলকের ডগা থেকে অক্ষ পর্যন্ত টান, উপরে মিটার
    for f, ang, angs, m, col, bg in lenses:
        x = X0 + m * PPM
        s.path(f"M {x:.1f} {CY} L {x:.1f} 660", col, 2.4, dash="8 6")
        s.circle(x, CY, 6, col)
        # লেবেল টানের ডান পাশে — মাঝখানে বসালে টানটাই লেখার উপর দিয়ে যায়
        s.text(x + 12, 640, f"{m} m", T_SMALL, col, 700, "start")

    # ── অক্ষ ও দাগ
    s.path(f"M {X0} 660 L {X0 + PW} 660", GREY, 2.4)
    for m in (0, 5, 10, 15, 20):
        x = X0 + m * PPM
        s.path(f"M {x:.1f} 652 L {x:.1f} 668", GREY, 2.4)
        s.text(x, 700, f"{m}", T_TINY, GREY, 700, "middle")
    s.text(X0 + PW / 2, 734, "লেন্স থেকে দূরত্ব, মিটারে", T_SMALL, GREY,
           700, "middle")

    # ── মানুষ, মাপের তুলনায় — ছকের ভেতরে, নিচের দিকে
    for m in (8, 16):
        person(s, X0 + m * PPM, 606, 58)

    # ── নিচে তিনটি ঘর
    for i, (f, ang, angs, m, col, bg) in enumerate(lenses):
        x = 62 + i * 388
        s.rect(x, 756, 360, 96, bg, col, 2.6, 11)
        s.text(x + 180, 796, f"{f} mm  —  {angs} ডিগ্রি", T_BODY, col, 700,
               "middle")
        s.text(x + 180, 832, f"চেনা যায় {m} মিটার পর্যন্ত", T_SMALL,
               GREY, 700, "middle")

    y = note_strip(s, 874, "চওড়া লেন্স বেশি জায়গা দেখায়, কিন্তু "
                           "চেনা যায় কাছেরটুকুই — দূরের মুখ চিনতে "
                           "সরু লেন্স")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_fov.svg")


# ══════════════════════════════════════════════════════════════════════
# ৬. পিক্সেল ঘনত্ব ও DORI
# ══════════════════════════════════════════════════════════════════════
def d06_dori():
    """IEC/EN 62676-4-র চারটি সীমা, আর তার পাশে Dahua-র ডেটাশিটের
    দূরত্ব (3.6 mm লেন্স, 2 MP)।  দুই কলাম পাশাপাশি রাখার কারণ:
    সীমাটা স্ট্যান্ডার্ডের, দূরত্বটা যন্ত্রের — গুলিয়ে ফেলা যাবে না।"""
    s = SVG(1240, 780)
    s.title("DORI — কত পিক্সেল পেলে কী বোঝা যায়", T_TITLE)

    rows = [("উপস্থিতি বোঝা", "Detect", 25, "মানুষ আছে কি নেই", 53, GREY,
             "#F2F4F6"),
            ("পর্যবেক্ষণ", "Observe", 63, "কতজন, কী পোশাক", 21, AMBER,
             AMBERBG),
            ("চেনা", "Recognize", 125, "আগে দেখা লোক কি না", 11, STEEL,
             LIGHT),
            ("শনাক্তকরণ", "Identify", 250, "কে, তা বলা যায়", 5, GREEN,
             GREENBG)]

    s.rect(52, 128, 1136, 58, "#EEF2F6", LINE, 2, 10)
    for x, t, an in ((104, "স্তর", "start"), (392, "পিক্সেল প্রতি মিটারে",
                                              "middle"),
                     (700, "কী বোঝা যায়", "middle"),
                     (1136, "3.6 mm লেন্সে দূরত্ব", "end")):
        s.text(x, 166, t, T_SMALL, NAVY, 700, an)

    y = 194
    for bn_, en, ppm, what, dist, col, bg in rows:
        s.rect(52, y, 1136, 122, bg, col, 2.4, 11)
        s.text(104, y + 50, bn_, T_NAME, col, 700, "start")
        s.text(104, y + 88, en, T_TINY, GREY, 700, "start")
        s.text(392, y + 66, str(ppm), T_TITLE, col, 700, "middle")
        s.text(700, y + 70, what, T_BODY, NAVY, 700, "middle")
        s.text(1136, y + 70, f"{dist} m", T_NAME, col, 700, "end")
        # মুখের পিক্সেল — ঘনত্ব যত বেশি, খোপ তত ছোট
        n = {25: 2, 63: 4, 125: 6, 250: 10}[ppm]
        bx, by, bw = 860, y + 24, 76
        cw = bw / n
        for i in range(n):
            for j in range(n):
                sh = "#FFFFFF" if (i + j) % 2 else col
                s.rect(bx + j * cw, by + i * cw, cw, cw, sh, "none", 0, 0)
        s.rect(bx, by, bw, bw, "none", col, 2, 2)
        y += 132

    s.text(620, y + 34, "মুখের চওড়া গড়ে 16 সেন্টিমিটার ধরে "
                        "স্ট্যান্ডার্ড সংখ্যাগুলো বের করা", T_SMALL,
           GREY, 700, "middle")

    y2 = note_strip(s, y + 58, "সীমা চারটি IEC 62676-4-র, আর দূরত্ব "
                               "যন্ত্রের নিজের ডেটাশিটের — দুটো এক নয়")
    s.fit(y2, 24)
    return s.save(f"{OUT}/d06_dori.svg")


# ══════════════════════════════════════════════════════════════════════
# ৭. দিন ও রাত — ICR ও IR
# ══════════════════════════════════════════════════════════════════════
def d07_night():
    s = SVG(1240, 700)
    s.title("দিনে রঙিন, রাতে সাদা-কালো — ভেতরে কী বদলায়", T_TITLE)
    al = s.arrow_defs(AMBER, "arD", 13)
    ai = s.arrow_defs(IRC, "arN", 13)

    def half(x, w, title, col, bg, sun_day):
        s.rect(x, 128, w, 420, bg, col, 2.8, 14)
        s.box_auto(x + w / 2, 142, title, T_BODY, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=24, pad_y=9)
        return x + w / 2

    # ── দিন
    cx = half(52, 556, "দিন — আলো আছে", AMBER, AMBERBG, True)
    s.circle(cx - 190, 236, 30, "#FDF3DA", AMBER, 3)
    for i in range(10):
        a = 2 * math.pi * i / 10
        s.path(f"M {cx - 190 + 38 * math.cos(a):.1f} "
               f"{236 + 38 * math.sin(a):.1f} L "
               f"{cx - 190 + 52 * math.cos(a):.1f} "
               f"{236 + 52 * math.sin(a):.1f}", AMBER, 2.6)
    s.rect(cx - 30, 210, 24, 112, "#E8F0F7", STEEL, 3, 4)
    s.text(cx - 18, 350, "ICR ফিল্টার", T_SMALL, STEEL, 700, "middle")
    s.text(cx - 18, 380, "ঢোকানো", T_SMALL, STEEL, 700, "middle")
    s.path(f"M {cx - 130} 266 L {cx - 40} 266", AMBER, 3.4, marker=al)
    s.rect(cx + 60, 206, 90, 120, "#2B3B4B", "#16222E", 3, 6)
    s.path(f"M {cx - 2} 266 L {cx + 56} 266", AMBER, 3.4, marker=al)
    s.text(cx + 105, 350, "সেন্সর", T_SMALL, NAVY, 700, "middle")
    s.text(cx, 430, "IR আলো আটকে দেয়, তাই রং ঠিক থাকে",
           T_SMALL, NAVY, 700, "middle")
    s.text(cx, 470, "ছবি রঙিন", T_BODY, AMBER, 700, "middle")
    s.text(cx, 510, "0.02 lux পর্যন্ত চলে", T_TINY, GREY, 700, "middle")

    # ── রাত
    cx = half(632, 556, "রাত — আলো নেই", IRC, "#F7EEFC", False)
    for i in range(7):
        a = 2 * math.pi * i / 7
        s.circle(cx - 190 + 34 * math.cos(a), 236 + 34 * math.sin(a),
                 8, "#EDDCF7", IRC, 2.2)
    s.text(cx - 190, 320, "IR LED", T_SMALL, IRC, 700, "middle")
    s.rect(cx - 30, 210, 24, 112, "#F2F4F6", "#9AA6B2", 2.6, 4,
           dash="8 6")
    s.path(f"M {cx - 34} 206 L {cx - 2} 326", "#9AA6B2", 3)
    s.path(f"M {cx - 2} 206 L {cx - 34} 326", "#9AA6B2", 3)
    s.text(cx - 18, 352, "ICR ফিল্টার", T_SMALL, GREY, 700, "middle")
    s.text(cx - 18, 382, "সরিয়ে নেওয়া", T_SMALL, GREY, 700, "middle")
    s.path(f"M {cx - 130} 266 L {cx - 40} 266", IRC, 3.4, dash="9 6",
           marker=ai)
    s.rect(cx + 60, 206, 90, 120, "#2B3B4B", "#16222E", 3, 6)
    s.path(f"M {cx - 2} 266 L {cx + 56} 266", IRC, 3.4, dash="9 6",
           marker=ai)
    s.text(cx + 105, 350, "সেন্সর", T_SMALL, NAVY, 700, "middle")
    s.text(cx, 430, "IR ঢুকতে দেয়, তাই অন্ধকারেও ছবি ওঠে",
           T_SMALL, NAVY, 700, "middle")
    s.text(cx, 470, "ছবি সাদা-কালো", T_BODY, IRC, 700, "middle")
    s.text(cx, 510, "0 lux-এও চলে, পাল্লা 30 m", T_TINY, GREY, 700,
           "middle")

    y = note_strip(s, 574, "রাতে ছবি সাদা-কালো হওয়া দোষ নয়, নকশা — "
                           "IR আলোর রং হয় না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_night.svg")


# ══════════════════════════════════════════════════════════════════════
# ৮. DVR ও NVR পাশাপাশি
# ══════════════════════════════════════════════════════════════════════
def d08_recorders():
    """দুই রেকর্ডারের পোর্ট-তালিকা আসল ডেটাশিটের।  সবচেয়ে বড়
    পার্থক্য দুটো, আর দুটোই ছবিতে আছে:  DVR-এ ক্যামেরার সংখ্যা
    = BNC পোর্টের সংখ্যা, আর তার দুটো;  NVR-এ এক তারে দুটোই, কিন্তু
    PoE-র মোট বাজেট আছে।"""
    s = SVG(1240, 820)
    s.title("DVR ও NVR — পিছনের দিক থেকে দেখা", T_TITLE)

    def unit(x, title, model, col, bg, rows, foot):
        s.rect(x, 128, 552, 560, bg, col, 2.8, 14)
        s.box_auto(x + 276, 144, title, T_NAME, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=26, pad_y=10)
        s.text(x + 276, 222, model, T_SMALL, GREY, 700, "middle")
        yy = 262
        for lab, val, pc in rows:
            s.rect(x + 26, yy, 500, 52, "#FFFFFF", LINE, 1.8, 8)
            s.text(x + 46, yy + 34, lab, T_SMALL, NAVY, 700, "start")
            s.text(x + 506, yy + 34, val, T_SMALL, pc, 700, "end")
            yy += 60
        s.rect(x + 26, 612, 500, 58, "#FFFFFF", col, 2.4, 9)
        s.text(x + 276, 648, foot, T_SMALL, col, 700, "middle")

    unit(52, "DVR (XVR)", "Dahua DH-XVR5108HS-4KL-X", VID, VIDBG,
         [("ক্যামেরা ইনপুট", "8 চ্যানেল BNC", VID),
          ("সংকেতের ধরন", "HDCVI / AHD / TVI / CVBS / IP", VID),
          ("বিট রেট প্রতি চ্যানেল", "32 থেকে 6144 kbps", NAVY),
          ("হার্ড ডিস্ক", "1 SATA · 10 TB পর্যন্ত", NAVY),
          ("পাওয়ার", "12 V DC 2 A · 10 W-র কম", PWR)],
         "ক্যামেরায় পাওয়ার আলাদা টানতে হয়")

    unit(636, "NVR", "Dahua DHI-NVR4108HS-8P-4KS2", NET, NETBG,
         [("ক্যামেরা ইনপুট", "8 চ্যানেল · 8টি PoE পোর্ট", NET),
          ("PoE", "802.3at/af · পোর্টে 25.5 W", POE),
          ("মোট PoE বাজেট", "80 W — যোগফল নয়", RED),
          ("হার্ড ডিস্ক", "1 SATA III · 6 TB পর্যন্ত", NAVY),
          ("পাওয়ার", "48 V DC 2 A · 8.3 W-র কম", PWR)],
         "এক তারেই পাওয়ার ও ডেটা")

    y = note_strip(s, 706, "DVR-এ প্রতি ক্যামেরায় দুটো তার, NVR-এ "
                           "একটা — কিন্তু NVR-এর PoE বাজেট গুনে নিতে হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_recorders.svg")


# ══════════════════════════════════════════════════════════════════════
# ৯. PoE — কোন জোড়ায় পাওয়ার
# ══════════════════════════════════════════════════════════════════════
def d09_poe():
    """TIA-568B-র আট পিন, আর দুই মোডে পাওয়ার কোন জোড়ায় যায়।
    Mode A — ডেটা-জোড়া 1-2 ও 3-6;  Mode B — অব্যবহৃত জোড়া 4-5 ও 7-8।
    100BASE-TX-এ ডেটা চলে কেবল 1-2 ও 3-6-তে, তাই Mode B-তে ডেটা ও
    পাওয়ার আলাদা তারে থাকে;  Mode A-তে একই তারে দুটোই — তাতে অসুবিধা
    নেই, কারণ পাওয়ার DC আর ডেটা উচ্চ কম্পাঙ্কে।"""
    s = SVG(1240, 800)
    s.title("PoE — আট পিনের কোনটিতে পাওয়ার", T_TITLE)

    PINS = [(1, "সাদা-কমলা", "#E8933A"), (2, "কমলা", "#D9730D"),
            (3, "সাদা-সবুজ", "#5FB07E"), (4, "নীল", "#2F6FB5"),
            (5, "সাদা-নীল", "#7FA9D8"), (6, "সবুজ", "#1B6E47"),
            (7, "সাদা-বাদামি", "#B08968"), (8, "বাদামি", "#7A5C42")]

    def plug(x, y, powered, title, sub, col, bg):
        s.rect(x, y, 512, 470, bg, col, 2.8, 14)
        s.box_auto(x + 256, y + 14, title, T_BODY, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=24, pad_y=9)
        s.text(x + 256, y + 92, sub, T_SMALL, GREY, 700, "middle")
        yy = y + 126
        for n, name, pc in PINS:
            on = n in powered
            s.rect(x + 28, yy, 456, 36, "#FFFFFF" if not on else "#F6F0FD",
                   POE if on else LINE, 2.6 if on else 1.6, 6)
            s.rect(x + 38, yy + 7, 22, 22, pc, "#4A5560", 1.6, 3)
            s.text(x + 74, yy + 26, str(n), T_SMALL, NAVY, 700, "start")
            s.text(x + 104, yy + 26, name, T_TINY, GREY, 700, "start")
            # 100 Mbps-এ ডেটা চলে কেবল 1-2 ও 3-6-এ;  4-5, 7-8 খালি
            data = n in (1, 2, 3, 6)
            if on:
                s.text(x + 474, yy + 26,
                       "ডেটা + পাওয়ার" if data else "কেবল পাওয়ার",
                       T_TINY, POE, 700, "end")
            else:
                s.text(x + 474, yy + 26,
                       "কেবল ডেটা" if data else "খালি",
                       T_TINY, GREY, 700, "end")
            yy += 42

    plug(52, 128, {1, 2, 3, 6}, "Mode A  ·  Alternative A",
         "ডেটা-জোড়াতেই পাওয়ার  —  সাধারণত সুইচের PoE (এন্ডস্প্যান)",
         POE, POEBG)
    plug(676, 128, {4, 5, 7, 8}, "Mode B  ·  Alternative B",
         "অব্যবহৃত জোড়ায় পাওয়ার  —  সাধারণত ইনজেক্টর (মিডস্প্যান)",
         STEEL, LIGHT)

    s.rect(52, 620, 1136, 82, "#FBFCFD", LINE, 2.2, 12)
    s.text(620, 656, "ক্যামেরা দুটো মোডই বোঝে — কোনটি এসেছে তা নিজে "
                     "ঠিক করে নেয়", T_SMALL, NAVY, 700, "middle")
    s.text(620, 688, "তাই সুইচ আর ইনজেক্টর মিলিয়ে ভাবার দরকার নেই, "
                     "কিন্তু দুটো একসঙ্গে দেওয়া যাবে না", T_TINY, RED,
           700, "middle")

    y = note_strip(s, 720, "100 Mbps-এর হিসাব। Gigabit-এ চারটি জোড়াতেই "
                           "ডেটা চলে, খালি জোড়া থাকে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_poe.svg")


# ══════════════════════════════════════════════════════════════════════
# ১০. PoE-র পাওয়ার বাজেট
# ══════════════════════════════════════════════════════════════════════
def d10_budget():
    """অধ্যায়ের সবচেয়ে কাজের ছবি।  NVR4108HS-8P-4KS2-র ডেটাশিটে
    দুটো সংখ্যা আলাদা আলাদা লেখা:  "Max 25.5w for single port,
    80w in total"।  গুণ করলে 204 W, কিন্তু পাওয়া যাবে 80 W — এই
    ফাঁদেই বেশির ভাগ লোক পড়ে।"""
    s = SVG(1240, 760)
    s.title("PoE বাজেট — পোর্টের হিসাব আর মোটের হিসাব এক নয়", T_TITLE)

    # ── বাঁ দিকে: ভুল হিসাব
    s.rect(52, 128, 540, 300, REDBG, RED, 2.8, 14)
    s.box_auto(322, 144, "যেভাবে ভুল হয়", T_BODY, fill=RED, stroke=RED,
               tcolor="#FFFFFF", pad_x=24, pad_y=9)
    s.text(322, 232, "8 পোর্ট  x  25.5 W", T_NODE, NAVY, 700, "middle")
    s.text(322, 292, "=  204 W", T_TITLE, RED, 700, "middle")
    s.text(322, 348, "\"আটটা ক্যামেরা তো ধরেই যাবে\"", T_SMALL, GREY,
           700, "middle")
    s.text(322, 390, "— ডেটাশিট তা বলে না", T_SMALL, RED, 700, "middle")

    # ── ডান দিকে: আসল বাজেট
    s.rect(648, 128, 540, 300, GREENBG, GREEN, 2.8, 14)
    s.box_auto(918, 144, "ডেটাশিট যা বলে", T_BODY, fill=GREEN,
               stroke=GREEN, tcolor="#FFFFFF", pad_x=24, pad_y=9)
    s.text(918, 218, "প্রতি পোর্টে সর্বোচ্চ  25.5 W", T_BODY, NAVY, 700,
           "middle")
    s.text(918, 292, "মোট  80 W", T_TITLE, GREEN, 700, "middle")
    s.text(918, 348, "দুটো শর্তই একসঙ্গে মানতে হবে", T_SMALL, GREY, 700,
           "middle")
    s.text(918, 390, "মোটটাই আগে ফুরায়", T_SMALL, GREEN, 700, "middle")

    # ── নিচে: আটটি ক্যামেরা, খরচের পটি
    s.text(620, 478, "আটটি IPC-HFW1230S-S5 — প্রতিটির সর্বোচ্চ খরচ "
                     "5.5 W (PoE)", T_BODY, NAVY, 700, "middle")
    x0, bw, gap = 118, 110, 16
    for i in range(8):
        x = x0 + i * (bw + gap)
        s.rect(x, 512, bw, 74, POEBG, POE, 2.6, 9)
        s.text(x + bw / 2, 544, f"ক্যাম {i + 1}", T_TINY, NAVY, 700,
               "middle")
        s.text(x + bw / 2, 574, "5.5 W", T_SMALL, POE, 700, "middle")
    s.text(620, 628, "মোট  8  x  5.5  =  44 W", T_NODE, GREEN, 700,
           "middle")
    s.text(620, 672, "80 W বাজেটের ভেতরেই — তাই আটটিই চলবে", T_SMALL,
           GREEN, 700, "middle")

    y = note_strip(s, 696, "কিন্তু ক্যামেরা যদি PTZ বা হিটারওয়ালা হয়, "
                           "তিনটিতেই বাজেট ফুরিয়ে যেতে পারে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_budget.svg")


# ══════════════════════════════════════════════════════════════════════
# ১১. ভিডিও বালুন
# ══════════════════════════════════════════════════════════════════════
def d11_balun():
    """বালুন = **bal**anced-**un**balanced ট্রান্সফরমার।  ছবির দুই
    অর্ধে দুটো কথা:  উপরে **কী বদলায়** (75 ohm আনব্যালান্সড থেকে
    100 ohm ব্যালান্সড), নিচে **কেন লাভ** (কমন-মোড নয়েজ দুই তারে
    সমান পড়ে, তাই বিয়োগে বাদ যায়)।"""
    s = SVG(1240, 820)
    s.title("ভিডিও বালুন — কোঅক্সের সংকেত মোচড়ানো জোড়ায়", T_TITLE)
    av = s.arrow_defs(VID, "arB", 13)

    # ── উপরের অর্ধ: কী বদলায়
    s.rect(52, 122, 1136, 300, "#FBFCFD", LINE, 2.4, 14)

    # কোঅক্সের দিক
    s.text(210, 166, "কোঅক্স দিক", T_BODY, VID, 700, "middle")
    s.text(210, 200, "আনব্যালান্সড  ·  75 ohm", T_SMALL, GREY, 700,
           "middle")
    s.path("M 86 264 L 420 264", VID, 4.2)
    s.path("M 86 330 L 420 330", "#2E3842", 3.4)
    s.text(96, 246, "ভেতরের পরিবাহী", T_TINY, VID, 700, "start")
    s.text(96, 356, "ব্রেইড — আর্থে", T_TINY, "#2E3842", 700, "start")
    earth(s, 330, 330)
    bnc(s, 420, 264, 14)

    # ট্রান্সফরমার
    s.rect(500, 216, 240, 170, LIGHT, STEEL, 3.2, 12)
    s.text(620, 190, "বালুন", T_NAME, STEEL, 700, "middle")
    for i in range(4):                       # প্রাথমিক কুণ্ডলী
        s.path(f"M 556 {248 + i * 26} A 13 13 0 1 1 556 {274 + i * 26}",
               SYM, 3)
    for i in range(4):                       # গৌণ কুণ্ডলী
        s.path(f"M 684 {248 + i * 26} A 13 13 0 1 0 684 {274 + i * 26}",
               SYM, 3)
    s.path("M 612 240 L 612 372", SYM, 2.4)
    s.path("M 628 240 L 628 372", SYM, 2.4)
    s.path("M 440 264 L 556 264", VID, 3.6)
    s.path("M 440 330 L 500 330 L 500 352 L 556 352", "#2E3842", 3)

    # UTP দিক
    s.path("M 684 264 L 1000 264", "#2F6FB5", 3.8)
    s.path("M 684 352 L 1000 352", "#7FA9D8", 3.8)
    s.text(1010, 270, "জোড়ার এক তার", T_TINY, "#2F6FB5", 700, "start")
    s.text(1010, 358, "জোড়ার অন্য তার", T_TINY, "#7FA9D8", 700, "start")
    s.text(1030, 166, "UTP দিক", T_BODY, NET, 700, "middle")
    s.text(1030, 200, "ব্যালান্সড  ·  100 ohm", T_SMALL, GREY, 700,
           "middle")

    # ── নিচের অর্ধ: কেন নয়েজ কাটে
    s.rect(52, 444, 1136, 268, NETBG, NET, 2.6, 14)
    s.box_auto(196, 458, "নয়েজ কেন কাটে", T_BODY, fill=NET, stroke=NET,
               tcolor="#FFFFFF", pad_x=24, pad_y=9)
    # সতর্কতা:  SVG-র লেখায় মার্কডাউন চলে না — `**...**` হুবহু ছাপা হয়।
    # জোর দিতে হলে রং বা আলাদা লাইন, তারা-চিহ্ন নয়।
    s.text(470, 528, "বাইরের নয়েজ দুই তারে সমান পড়ে", T_SMALL, RED,
           700, "middle")
    s.path("M 112 590 L 700 590", "#2F6FB5", 4)
    s.path("M 112 652 L 700 652", "#7FA9D8", 4)
    an = s.arrow_defs(RED, "arNz", 12)
    for x in (240, 380, 520):                # নয়েজ — দুই তারে একই দিকে
        s.path(f"M {x} 546 L {x} 580", RED, 2.8, marker=an)
        s.path(f"M {x} 608 L {x} 642", RED, 2.8, marker=an)
    s.rect(730, 576, 200, 96, "#FFFFFF", NET, 2.8, 10)
    s.text(830, 614, "রিসিভার", T_SMALL, NAVY, 700, "middle")
    s.text(830, 650, "পার্থক্য নেয়", T_SMALL, NET, 700, "middle")
    s.path("M 700 590 L 730 590", "#2F6FB5", 3.4)
    s.path("M 700 652 L 730 652", "#7FA9D8", 3.4)
    s.path("M 930 624 L 998 624", GREEN, 3.6, marker=s.arrow_defs(
        GREEN, "arG", 13))
    s.text(1082, 608, "সংকেত থাকে,", T_SMALL, GREEN, 700, "middle")
    s.text(1082, 644, "নয়েজ বাদ যায়", T_SMALL, GREEN, 700, "middle")

    y = note_strip(s, 730, "বালুন জোড়ায় জোড়ায় লাগে — দুই মাথায় দুটি, "
                           "নইলে কিছুই কাজ করবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_balun.svg")


# ══════════════════════════════════════════════════════════════════════
# ১২. দূরত্বের তুলনা
# ══════════════════════════════════════════════════════════════════════
def d12_distance():
    """চারটি দণ্ড, চারটিই ডেটাশিটের সংখ্যা — একটিও আন্দাজ নয়।  সবচেয়ে
    দরকারি পাঠ:  IP-র 100 m সবচেয়ে ছোট, অথচ IP-ই সবচেয়ে আধুনিক।
    দূরত্ব বেশি দরকার হলে অ্যানালগ এখনো হারেনি।"""
    s = SVG(1240, 700)
    s.title("কোন তারে কত দূর — ডেটাশিটের সংখ্যা", T_TITLE)

    X0, XW, MAX = 300, 800, 850
    rows = [("Cat 6 — IP ক্যামেরা", "IEEE 802.3 · এক হপে", 100, NET,
             NETBG),
            ("UTP + প্যাসিভ বালুন", "Hikvision DS-1H18S/E(C)", 250, VID,
             VIDBG),
            ("কোঅক্স — HDCVI 1080P", "Dahua XVR5108HS-4KL-X", 800, AMBER,
             AMBERBG),
            ("কোঅক্স — HDCVI 720P", "একই রেকর্ডার", 1200, GREEN,
             GREENBG)]

    y = 168
    for name, src, m, col, bg in rows:
        s.text(280, y + 34, name, T_BODY, NAVY, 700, "end")
        s.text(280, y + 68, src, T_TINY, GREY, 700, "end")
        w = XW * min(m, MAX) / MAX
        s.rect(X0, y + 12, w, 58, bg, col, 2.8, 8)
        if m > MAX:                          # বাজেট ছাড়িয়ে গেলে ছেঁড়া প্রান্ত
            s.path(f"M {X0 + w - 18} {y + 12} L {X0 + w - 4} {y + 41} "
                   f"L {X0 + w - 18} {y + 70}", col, 3)
            s.text(X0 + w + 18, y + 50, f"{m} m", T_NAME, col, 700,
                   "start")
        else:
            s.text(X0 + w + 18, y + 50, f"{m} m", T_NAME, col, 700,
                   "start")
        y += 104

    # ── স্কেল
    s.path(f"M {X0} {y + 4} L {X0 + XW} {y + 4}", GREY, 2.4)
    for m in (0, 200, 400, 600, 800):
        x = X0 + XW * m / MAX
        s.path(f"M {x} {y - 4} L {x} {y + 12}", GREY, 2.4)
        s.text(x, y + 42, f"{m}", T_TINY, GREY, 700, "middle")
    s.text(X0 + XW / 2, y + 76, "মিটার", T_SMALL, GREY, 700, "middle")

    s.rect(52, y + 100, 1136, 64, REDBG, RED, 2.4, 11)
    s.text(620, y + 140, "100 মিটারের বেশি IP চালাতে হলে মাঝখানে "
                         "সুইচ বসাতে হয় — প্রতিটি হপে আবার 100 মিটার",
           T_SMALL, RED, 700, "middle")

    y2 = note_strip(s, y + 184, "দূরত্বই যেখানে মূল সমস্যা, সেখানে "
                                "অ্যানালগ এখনো সহজ সমাধান")
    s.fit(y2, 24)
    return s.save(f"{OUT}/d12_distance.svg")


# ══════════════════════════════════════════════════════════════════════
# ১৩. অ্যানালগ সিস্টেমের সম্পূর্ণ সংযোগ
# ══════════════════════════════════════════════════════════════════════
def d13_analog_wiring():
    """তারের তালিকা — ছবি আঁকার আগে লেখা (অধ্যায় ১৪-এর নিয়ম):

        1  ক্যাম ১ BNC      → কোঅক্স → DVR VIDEO IN 1
        2  ক্যাম ২ BNC      → কোঅক্স → DVR VIDEO IN 2
        3  ক্যাম ৩ BNC      → বালুন → UTP → বালুন → DVR VIDEO IN 3
        4  ক্যাম ১/২/৩ DC   → পাওয়ার বক্সের 12 V DC আউট (প্যারালালে)
        5  পাওয়ার বক্স AC   → 230 V সাপ্লাই
        6  DVR DC 12V       → নিজস্ব অ্যাডাপ্টার → 230 V সাপ্লাই
        7  DVR HDMI         → মনিটর
        8  DVR LAN          → রাউটার (দূর থেকে দেখার জন্য)
        9  DVR ভেতরে        → SATA হার্ড ডিস্ক

    **৪ নম্বর তারটি প্যারালাল, সিরিজ নয়** — তিনটি ক্যামেরা একই
    12 V বাসে আলাদা আলাদা ড্রপে জোড়া।  CLAUDE.md-র সবচেয়ে পুরোনো
    সতর্কতা এটাই:  সিরিজে আঁকলে ছবিটা দেখতে প্রায় একই লাগে, অথচ
    তিনটে ক্যামেরা 4 V করে পেত।  ছবিতে তাই বাসবার থেকে **তিনটি
    আলাদা ড্রপ** আঁকা, আর প্রতিটির গোড়ায় নোড-বিন্দু।

    ক্রসিং শূন্য:  ক্যামেরা উপর থেকে নিচে ১, ২, ৩ — DVR-এর পোর্টও
    উপর থেকে নিচে ১, ২, ৩।"""
    s = SVG(1240, 900)
    s.title("অ্যানালগ সিস্টেম — সম্পূর্ণ সংযোগ", T_TITLE)

    # ── তিনটি ক্যামেরা, বাঁ দিকে
    cams = []
    for i, y in enumerate((172, 320, 468)):
        bullet_cam(s, 62, y, 124, 50, ir=False, face="right")
        s.text(124, y - 16, f"ক্যামেরা {i + 1}", T_SMALL, NAVY, 700,
               "middle")
        cams.append(y + 25)

    # ── DVR
    ports, rports = rec_box(
        s, 780, 158, 250, 420, "DVR", "8 চ্যানেল · XVR", VID,
        [("VIDEO IN 1", VID), ("VIDEO IN 2", VID), ("VIDEO IN 3", VID)],
        [("HDMI", NAVY), ("LAN", NET)])

    # ── ১ ও ২: সরাসরি কোঅক্স
    for i in (0, 1):
        px, py = ports[i]
        s.path(f"M 196 {cams[i]} L {px - 40} {cams[i]} "
               f"L {px - 40} {py} L {px} {py}", VID, 3.6)
        bnc(s, 212, cams[i], 11)
        s.text(400, cams[i] - 18, "কোঅক্স RG59", T_TINY, VID, 700,
               "middle")

    # ── ৩: বালুন জোড়া
    px3, py3 = ports[2]
    s.path(f"M 196 {cams[2]} L 268 {cams[2]}", VID, 3.6)
    bnc(s, 212, cams[2], 11)
    s.rect(268, cams[2] - 24, 76, 48, LIGHT, STEEL, 2.6, 8)
    s.text(306, cams[2] + 6, "বালুন", T_TINY, STEEL, 700, "middle")
    s.path(f"M 344 {cams[2] - 8} L 616 {cams[2] - 8}", "#2F6FB5", 3.2)
    s.path(f"M 344 {cams[2] + 8} L 616 {cams[2] + 8}", "#7FA9D8", 3.2)
    s.text(480, cams[2] - 30, "UTP — Cat 6-র এক জোড়া", T_TINY, NET, 700,
           "middle")
    s.rect(616, cams[2] - 24, 76, 48, LIGHT, STEEL, 2.6, 8)
    s.text(654, cams[2] + 6, "বালুন", T_TINY, STEEL, 700, "middle")
    s.path(f"M 692 {cams[2]} L {px3 - 40} {cams[2]} "
           f"L {px3 - 40} {py3} L {px3} {py3}", VID, 3.6)

    # ── মনিটর ও রাউটার — তার ডান পাশ দিয়ে, বাক্সের ভেতর দিয়ে নয়
    pxh, pyh = rports[0]
    monitor(s, 1074, 214, 140, 96, (2, 2), NAVY)
    s.path(f"M {pxh} {pyh} L 1052 {pyh} L 1052 262 L 1074 262", NAVY, 3.2)
    s.text(1144, 352, "মনিটর", T_SMALL, NAVY, 700, "middle")
    pxl, pyl = rports[1]
    s.rect(1074, 400, 140, 74, NETBG, NET, 2.6, 10)
    s.text(1144, 446, "রাউটার", T_SMALL, NET, 700, "middle")
    s.path(f"M {pxl} {pyl} L 1052 {pyl} L 1052 437 L 1074 437", NET, 3.2)

    # ── পাওয়ার বক্স ও 12 V বাস — প্যারালাল ড্রপ
    s.rect(62, 640, 300, 116, PWRBG, PWR, 2.8, 12)
    s.text(212, 682, "পাওয়ার বক্স", T_BODY, PWR, 700, "middle")
    s.text(212, 722, "230 V AC থেকে 12 V DC", T_TINY, GREY, 700, "middle")
    # AC-র প্রবেশ পাওয়ার বক্সের ডান কোণে।  বাঁ কোণে রাখলে লেবেলটা
    # ক্যামেরা ৩-র ব্র্যাকেটের উপর পড়ে, আর মাঝখানে রাখলে ১২ V-র
    # তৃতীয় ড্রপের (y = 539) উপর।
    s.path("M 330 580 L 330 640", NAVY, 3.4)
    s.text(330, 562, "230 V AC", T_TINY, NAVY, 700, "middle")

    s.path("M 400 698 L 700 698", PWR, 4.2)          # 12 V বাসবার
    s.path("M 362 698 L 400 698", PWR, 4.2)
    s.text(550, 736, "12 V DC বাস — তিনটি আলাদা ড্রপ, প্যারালালে",
           T_SMALL, PWR, 700, "middle")
    for i, x in enumerate((440, 550, 660)):
        node(s, x, 698, PWR, 6)
        s.path(f"M {x} 698 L {x} {cams[i] + 46} L 196 {cams[i] + 46}",
               PWR, 3, dash="8 6")
        s.circle(196, cams[i] + 46, 5.5, PWR)

    # ── DVR-এর নিজস্ব পাওয়ার
    s.rect(830, 640, 200, 84, PWRBG, PWR, 2.6, 10)
    s.text(930, 690, "12 V অ্যাডাপ্টার", T_SMALL, PWR, 700, "middle")
    s.path("M 930 578 L 930 640", PWR, 3.4)

    # ── হার্ড ডিস্ক
    s.rect(1074, 560, 140, 74, LIGHT, NAVY, 2.6, 9)
    s.text(1144, 594, "হার্ড ডিস্ক", T_TINY, NAVY, 700, "middle")
    s.text(1144, 622, "SATA, ভেতরে", T_TINY, GREY, 700, "middle")
    s.path("M 1030 560 L 1052 560 L 1052 597 L 1074 597", NAVY, 3,
           dash="7 5")

    y = note_strip(s, 786, "তিনটি ক্যামেরা 12 V বাসে প্যারালালে — "
                           "সিরিজে জুড়লে প্রতিটি 4 V পাবে, ছবিই উঠবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_analog_wiring.svg")


# ══════════════════════════════════════════════════════════════════════
# ১৪. IP সিস্টেমের সম্পূর্ণ সংযোগ
# ══════════════════════════════════════════════════════════════════════
def d14_ip_wiring():
    """তারের তালিকা — আগের মতোই, ছবি আঁকার আগে:

        1  ক্যাম ১ RJ45  → Cat 6 → NVR PoE 1     (পাওয়ার ও ডেটা একসঙ্গে)
        2  ক্যাম ২ RJ45  → Cat 6 → NVR PoE 2
        3  ক্যাম ৩ RJ45  → Cat 6 → NVR PoE 3
        4  ক্যাম ৪ RJ45  → Cat 6 → PoE সুইচ → Cat 6 → NVR LAN
        5  NVR LAN      → রাউটার (দূর থেকে দেখা ও ইন্টারনেট)
        6  NVR HDMI     → মনিটর
        7  NVR DC 48V   → নিজস্ব অ্যাডাপ্টার → 230 V
        8  NVR ভেতরে    → SATA হার্ড ডিস্ক

    **৪ নম্বরটি ইচ্ছে করে রাখা।**  NVR-এ PoE পোর্ট আটটি, কিন্তু
    বাজেট 80 W;  বাজেট ফুরালে বা দূরত্ব বাড়লে বাইরের PoE সুইচ
    লাগে, আর তখন ক্যামেরা NVR-এর PoE পোর্টে নয়, **LAN পোর্টে**
    ঢোকে।  এই পার্থক্যটা না বুঝলে মাঠে সবচেয়ে বেশি ভুল হয়।

    ক্রসিং শূন্য:  ক্যামেরা ১-৪ উপর থেকে নিচে, পোর্টও একই ক্রমে।"""
    s = SVG(1240, 950)
    s.title("IP সিস্টেম — এক তারেই পাওয়ার ও ছবি", T_TITLE)

    cams = []
    for i, y in enumerate((168, 292, 416)):
        bullet_cam(s, 62, y, 124, 48, ir=False)
        s.text(124, y - 16, f"ক্যামেরা {i + 1}", T_SMALL, NAVY, 700,
               "middle")
        cams.append(y + 24)

    # ── চতুর্থ ক্যামেরা — দূরে, সুইচের মাধ্যমে
    bullet_cam(s, 62, 568, 124, 48, ir=False)
    s.text(124, 552, "ক্যামেরা 4 — দূরে", T_SMALL, NAVY, 700, "middle")
    c4 = 592

    ports, rports = rec_box(
        s, 800, 150, 240, 410, "NVR", "8 চ্যানেল · 8 PoE", NET,
        [("PoE 1", POE), ("PoE 2", POE), ("PoE 3", POE)],
        [("HDMI", NAVY), ("LAN", NET)])

    # ── ১-৩: সরাসরি PoE
    for i in range(3):
        px, py = ports[i]
        rj45(s, 208, cams[i], 30, 24, POE)
        s.path(f"M 226 {cams[i]} L {px - 46} {cams[i]} "
               f"L {px - 46} {py} L {px} {py}", POE, 4)
        s.text(470, cams[i] - 20, "Cat 6 — PoE", T_TINY, POE, 700,
               "middle")

    # ── ৪: সুইচ হয়ে LAN পোর্টে
    pxh, pyh = rports[0]
    pxl, pyl = rports[1]
    rj45(s, 208, c4, 30, 24, POE)
    s.path(f"M 226 {c4} L 400 {c4}", POE, 4)
    s.rect(400, c4 - 42, 200, 84, POEBG, POE, 2.8, 11)
    s.text(500, c4 - 6, "PoE সুইচ", T_SMALL, POE, 700, "middle")
    s.text(500, c4 + 26, "নিজস্ব পাওয়ার", T_TINY, GREY, 700, "middle")
    # LAN পোর্ট ডান পাশে, তাই তারটি সবকিছুর নিচ দিয়ে ঘুরে ডানে ওঠে।
    # x = 620-তে নামানো হয়েছে, সুইচের কিনারা ঘেঁষে নয়।
    s.path(f"M 600 {c4} L 620 {c4} L 620 744 L 1130 744 "
           f"L 1130 {pyl} L {pxl} {pyl}", NET, 4)
    s.text(700, c4 - 20, "Cat 6 — কেবল ডেটা", T_TINY, NET, 700, "middle")
    s.path("M 500 660 L 500 700", PWR, 3, dash="8 6")
    s.text(500, 726, "230 V AC", T_TINY, PWR, 700, "middle")

    # ── মনিটর — HDMI পোর্টের ঠিক সমান উচ্চতায়, তাই তার একেবারে
    # সোজা;  কোনো উল্লম্ব অংশ নেই বলে ডান পাশে আর কিছুর উপর পড়ে না।
    monitor(s, 1076, pyh - 46, 136, 92, (2, 2), NAVY)
    s.path(f"M {pxh} {pyh} L 1076 {pyh}", NAVY, 3.4)
    s.text(1144, pyh - 68, "মনিটর", T_SMALL, NAVY, 700, "middle")

    # ── NVR-এর পাওয়ার।  অ্যাডাপ্টারটি নিচের তারের (y = 744) উপরে
    # বসানো, তাই দুটো কোথাও কাটাকাটি করে না।
    s.rect(700, 620, 200, 84, PWRBG, PWR, 2.6, 10)
    s.text(800, 654, "48 V অ্যাডাপ্টার", T_SMALL, PWR, 700, "middle")
    s.text(800, 686, "PoE-র জন্য 48 V লাগে", T_TINY, GREY, 700, "middle")
    s.path("M 800 560 L 800 620", PWR, 3.4)
    # হার্ড ডিস্কের কথাটা বাক্সের নিচে, ডান পাশে নয় — ডান পাশে
    # LAN-র তার উঠে যায়, লেখাটা তার নিচে চাপা পড়ে।
    s.text(950, 596, "হার্ড ডিস্ক NVR-এর ভেতরেই (SATA)", T_TINY, GREY,
           700, "middle")


    s.rect(52, 782, 1136, 64, POEBG, POE, 2.4, 11)
    s.text(620, 822, "PoE পোর্টে ঢুকলে NVR নিজেই পাওয়ার দেয়;  বাইরের "
                     "সুইচ দিয়ে এলে ক্যামেরা ঢোকে LAN পোর্টে",
           T_SMALL, POE, 700, "middle")

    y = note_strip(s, 864, "বাইরের PoE সুইচের ক্যামেরা NVR-এর PoE "
                           "পোর্টে লাগালে দুই দিক থেকে পাওয়ার পড়ে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d14_ip_wiring.svg")


# ══════════════════════════════════════════════════════════════════════
# ১৫. বসানোর পরিকল্পনা
# ══════════════════════════════════════════════════════════════════════
def d15_layout():
    """উপর থেকে দেখা একটি দোকান।  চারটি ক্যামেরার জায়গা ইচ্ছে করে
    বাছা:  গেটে সরু লেন্স (মুখ চেনার জন্য), ভেতরে চওড়া (পুরো ঘর),
    ক্যাশ কাউন্টারে কাছে ও সরু, আর গুদামের দরজায় একটি।  নিচে
    বাংলায় নোটিশের নমুনা — কমন্সের সাইনটি কোন ভাষার তা নিশ্চিত না
    হওয়ায় নিজেরাই আঁকা।"""
    s = SVG(1240, 880)
    s.title("বসানোর পরিকল্পনা — উপর থেকে দেখা", T_TITLE)

    # ── দোকানের ছক
    s.rect(62, 132, 700, 500, "#FBFCFD", NAVY, 3.2, 10)
    s.rect(62, 132, 700, 500, "none", NAVY, 3.2, 10)
    s.rect(500, 132, 262, 220, "#F2F5F8", LINE, 2.4, 6)
    s.text(590, 330, "গুদাম", T_BODY, GREY, 700, "middle")
    s.rect(96, 500, 200, 100, LIGHT, STEEL, 2.4, 6)
    s.text(196, 558, "ক্যাশ কাউন্টার", T_SMALL, STEEL, 700, "middle")
    # গেট
    s.rect(300, 620, 160, 24, GREENBG, GREEN, 2.6, 4)
    s.text(380, 668, "গেট", T_SMALL, GREEN, 700, "middle")

    # ── চারটি ক্যামেরা, কীলকসহ
    # প্রতিটি কীলকের প্রান্তবিন্দু হাতে মিলিয়ে দেখা হয়েছে যেন
    # ছকের (62..762, 132..632) ভেতরেই থাকে — নইলে কীলক দেয়াল ভেদ
    # করে বেরিয়ে নিচের নোটিশের লেখার উপর গিয়ে পড়ে।
    specs = [(380, 400, 54.7, 210, -90, GREEN, GREENBG, "ক্যাম 1",
              "6 mm — গেটে, মুখ চেনার জন্য"),
             (110, 200, 103.0, 300, -45, AMBER, AMBERBG, "ক্যাম 2",
              "2.8 mm — পুরো ঘর"),
             (196, 468, 87.5, 150, -90, STEEL, LIGHT, "ক্যাম 3",
              "3.6 mm — ক্যাশ কাউন্টার"),
             (740, 172, 87.5, 190, -140, POE, POEBG, "ক্যাম 4",
              "3.6 mm — গুদামের দরজা")]
    for cx, cy, ang, reach, up, col, bg, tag, sub in specs:
        cone(s, cx, cy, ang, reach, col, bg, 0.38, up)
        s.circle(cx, cy, 13, "#FFFFFF", col, 3.2)
        s.circle(cx, cy, 5, col)

    # লেবেলগুলো ছকের বাইরে, ডান পাশে — ভেতরে বসালে কীলকের সঙ্গে লাগে
    yy = 168
    for cx, cy, ang, reach, up, col, bg, tag, sub in specs:
        s.rect(800, yy, 388, 92, bg, col, 2.6, 11)
        s.circle(838, yy + 46, 13, "#FFFFFF", col, 3)
        s.circle(838, yy + 46, 5, col)
        s.text(874, yy + 40, tag, T_BODY, col, 700, "start")
        s.text(874, yy + 74, sub, T_SMALL, GREY, 700, "start")
        yy += 104

    s.text(994, yy + 34, "গেটে সরু লেন্স, ঘরে চওড়া —", T_SMALL, NAVY,
           700, "middle")
    s.text(994, yy + 66, "উল্টোটা করলে কারও মুখ চেনা যাবে না",
           T_SMALL, RED, 700, "middle")

    # ── নোটিশের নমুনা
    s.rect(62, 696, 700, 108, AMBERBG, AMBER, 3, 12)
    s.rect(92, 718, 64, 64, "#FFFFFF", AMBER, 2.6, 8)
    bullet_cam(s, 102, 740, 36, 20, ir=False, bracket=False)
    s.text(184, 746, "সতর্কীকরণ — এই এলাকায় CC ক্যামেরায়", T_BODY,
           NAVY, 700, "start")
    s.text(184, 780, "নজরদারি ও ধারণ করা হচ্ছে", T_BODY, NAVY, 700,
           "start")
    s.text(412, 828, "নোটিশ দৃশ্যমান জায়গায় থাকা উচিত", T_SMALL, GREY,
           700, "middle")

    s.fit(834, 24)
    return s.save(f"{OUT}/d15_layout.svg")


ALL = [d01_system, d02_inside, d03_types, d04_analog_ip, d05_fov,
       d06_dori, d07_night, d08_recorders, d09_poe, d10_budget,
       d11_balun, d12_distance, d13_analog_wiring, d14_ip_wiring,
       d15_layout]


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in ALL:
        print("✓", f(), flush=True)
