# -*- coding: utf-8 -*-
"""অধ্যায় ১২ — ফরওয়ার্ড-রিভার্স স্টার্টার : ডায়াগ্রাম।

সহায়কগুলো অধ্যায় ৮, ৯, ১০ ও ১১ থেকে আমদানি করা (CLAUDE.md-র নিয়ম)।
`photo_callouts` অধ্যায় ৮-এর ছবির ফোল্ডার ধরে রাখে, তাই এখানে
`_use_ch12_images()` দিয়ে বদলে নেওয়া হয়েছে।

**পাওয়ার সার্কিটের টপোলজি (d05, d06)** — দুই কন্টাক্টরের ইনপুট দিকে
ক্রম উল্টে জোড়া, আর আউটপুট দিক সরাসরি সমান্তরাল:

    KM1 1←L1   3←L2   5←L3          KM2 1←L3   3←L2   5←L1
    KM1 2 ─┬─ KM2 2 ─→ F2 ─→ U      (4 ও 6 একইভাবে V ও W-তে)

অর্থাৎ দুই কন্টাক্টরের 2 নম্বর টার্মিনাল একই নোডে।  **এখানেই বিপদ** —
দুটো একসঙ্গে টানলে L1 আর L3 ওই নোডে মিলে যায়, অর্থাৎ ফেজ-টু-ফেজ শর্ট
(d04)।  ওভারলোড রিলে দুই কন্টাক্টরের **পরে**, একটাই — দুই দিকের
কারেন্ট একই পথ দিয়ে যায় বলে একটিই যথেষ্ট।

**কন্ট্রোল সার্কিটের টপোলজি (`_ladder12`)** — অধ্যায় ৯-এর `_ladder()`-এর
দুই কপি, পরস্পরের পথ কেটে:

    L → F1 → F2 95-96 → STOP → P
    P → [FWD 13-14 ‖ KM1 13-14] → REV 21-22 → KM2 21-22 → KM1 কয়েল → N
    P → [REV 13-14 ‖ KM2 13-14] → FWD 21-22 → KM1 21-22 → KM2 কয়েল → N

লক্ষণীয় — বোতামের NC ল্যাচের **পরে** বসে, ফলে উল্টো বোতাম চাপলে চলন্ত
দিকের ল্যাচ আগে ভাঙে।  আর কন্টাক্টরের NC 21-22 কয়েলের ঠিক আগে, যাতে
পথটা সবচেয়ে ছোট হয়।

**২১-২২ কেন, অন্য কোনো NC কেন নয়** — Schneider-এর নিজস্ব নথি (FAQ
FA142116):  "LC1D09 to LC1D95: The 21-22 NC auxiliary contact is a
mirror contact", আর মিরর কন্টাক্টের সংজ্ঞা IEC 60947-4-1-এ — "a NC
auxiliary contact which reflects the state of the NO main contact",
মেইন কন্টাক্ট ওয়েল্ড হয়ে আটকে গেলেও এটি বন্ধ হতে পারে না।  LC1D09M7-এর
ডেটাশিটেও লেখা:  "type mirror contact 1 NC conforming to IEC
60947-4-1"।  তাই ইন্টারলকের তারটা 21-22-এ, 31-32-এ নয়।

**সময়ের হিসাব (১২.৪-এর যুক্তি)** — একই LC1D09M7-এর ডেটাশিট:  বন্ধ হতে
12–22 ms, খুলতে 4–19 ms।  বোতামের NO আর NC প্রায় একসঙ্গে কাজ করে, তাই
কেবল বোতামের ইন্টারলকে ভরসা করলে একটি কন্টাক্টর ছাড়ার আগেই অন্যটি
ধরে ফেলতে পারে।

**ক্রসিং কোথায়, আর কেন এড়ানো যায়নি** — উপরের দিকের তিন লিঙ্ক
(1→5, 3→3, 5→1) ক্রম উল্টে দেয় বলে ওগুলো নেস্টেড হয়, একটিও ক্রসিং
লাগে না।  নিচের দিকের তিন লিঙ্ক (2-2, 4-4, 6-6) ক্রম বজায় রাখে, আর
সমান দুই সারি বিন্দু ক্রম বজায় রেখে জুড়তে গেলে সমতলে ক্রসিং হবেই —
তিনটি।  তাই `join_bus()` ওখানে **আধা-বৃত্তের লাফ** আঁকে;  জোড়ার
জায়গায় ভরাট বিন্দু, ক্রসিংয়ে লাফ — দুটো কখনো এক দেখায় না।

**d10 `poly()` দিয়ে আঁকা** — qc ওটার ভেতর দেখে না, চোখে দেখে নিতে হবে।

কালপুরুষের সীমা আগের অধ্যায়গুলোর মতোই — টার্মিনাল, রেটিং, মডেল
নম্বর ল্যাটিন অঙ্কে;  `÷`, `Ω`, `°` ছবিতে নেই।
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
from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch12")
IMG = os.path.join(HERE, "assets", "ch12")

# তিন ফেজের রঙ — ছবিজুড়ে এক (বাংলাদেশের বাজারে লাল-হলুদ-নীল প্রচলিত,
# কিন্তু ছাপায় হলুদ পড়া যায় না, তাই গাঢ় অ্যাম্বার)
PH1 = "#C0392B"
PH2 = "#B47500"
PH3 = "#1D5B8F"
PHC = (PH1, PH2, PH3)

FWDC = GREEN              # সামনের দিক
REVC = "#7A4FA3"          # পেছনের দিক
MECH = "#4A5560"          # যান্ত্রিক অংশ


def _use_ch12_images():
    C8.IMG = IMG
    C8.OUT = OUT


def photo_callouts(*a, **k):
    _use_ch12_images()
    return C8.photo_callouts(*a, **k)


# ── ছোট সহায়ক ───────────────────────────────────────────────────────────
def motor_sym(s, cx, cy, r=48, arrow=None, col=SYM):
    """মোটরের বৃত্ত;  arrow = "cw" / "ccw" হলে ভেতরে ঘোরার তির।"""
    s.circle(cx, cy, r, "#FFFFFF", col, 3.6)
    s.text(cx, cy - 2, "M", T_NODE, col, 700, "middle")
    s.text(cx, cy + 26, "3 ~", T_SMALL, col, 700, "middle")
    if not arrow:
        return
    rr = r + 26
    if arrow == "cw":
        s.path(f"M {cx - rr} {cy} A {rr} {rr} 0 0 1 {cx} {cy - rr}",
               FWDC, 3.4)
        s.path(f"M {cx - 13} {cy - rr + 3} L {cx} {cy - rr} "
               f"L {cx - 4} {cy - rr + 14}", FWDC, 3.4)
    else:
        s.path(f"M {cx + rr} {cy} A {rr} {rr} 0 0 0 {cx} {cy - rr}",
               REVC, 3.4)
        s.path(f"M {cx + 13} {cy - rr + 3} L {cx} {cy - rr} "
               f"L {cx + 4} {cy - rr + 14}", REVC, 3.4)


def pole_set(s, x0, gap, ytop, ybot, closed, col=SYM, tags=True):
    """কন্টাক্টরের তিন পোল — ঢালু ব্লেড, বন্ধ হলে সোজা।
    ফেরত দেয় তিনটি পোলের x।"""
    xs = [x0 + i * gap for i in range(3)]
    for i, x in enumerate(xs):
        node(s, x, ytop, col)
        node(s, x, ybot, col)
        if closed:
            s.path(f"M {x} {ytop} L {x} {ybot}", col, SW)
        else:
            s.path(f"M {x} {ytop} L {x + 34} {ybot}", col, SW)
        if tags:
            s.text(x - 14, ytop + 34, str(2 * i + 1), T_TINY, NAVY, 700,
                   "end")
            s.text(x - 14, ybot + 26, str(2 * i + 2), T_TINY, NAVY, 700,
                   "end")
    return xs


def chev(s, x, y, dx, dy, col=RED, sz=15, sw=3.8):
    """তির-মুখ — (dx, dy) দিকে মুখ করা।"""
    px, py = -dy, dx
    s.path(f"M {x - dx * sz + px * sz} {y - dy * sz + py * sz} "
           f"L {x} {y} "
           f"L {x - dx * sz - px * sz} {y - dy * sz - py * sz}", col, sw)


def join_bus(s, pairs, yterm, col=SYM, sw=3.6, labels=("U", "V", "W"),
             lab_dx=18):
    """দুই কন্টাক্টরের একই নম্বরের টার্মিনাল জোড়া দেয়।

    সমান দুই সারি টার্মিনাল সোজা জুড়তে গেলে সমতলে ক্রসিং হয়ই — এ
    ছবিগুলোতে তিনটি।  যেখানে ক্রসিং, সেখানে আধা-বৃত্তের লাফ (hop)
    আঁকা হয়, তাই জোড়া আর ক্রসিং কখনো এক দেখায় না।
    pairs = [(xa, xb, y), …]  y ছোট থেকে বড় ক্রমে।"""
    def hops_on(xa, xb, y):
        h = []
        for xa2, xb2, y2 in pairs:
            if y2 <= y:
                continue
            for xv in (xa2, xb2):
                if xa + 12 < xv < xb - 12:
                    h.append(xv)
        return sorted(h)

    for i, (xa, xb, y) in enumerate(pairs):
        s.path(f"M {xa} {yterm} L {xa} {y}", col, sw)
        s.path(f"M {xb} {yterm} L {xb} {y}", col, sw)
        d, cur = f"M {xa} {y}", xa
        for xv in hops_on(xa, xb, y):
            d += f" L {xv - 10} {y} A 10 10 0 0 1 {xv + 10} {y}"
            cur = xv + 10
        d += f" L {xb} {y}"
        s.path(d, col, sw)
        node(s, xa, y, col)
        node(s, xb, y, col)
        if labels:
            s.text(xa - lab_dx, y + 8, labels[i], T_BODY, NAVY, 700, "end")


def km_box(s, x, y, w, h, tag, col=SYM, sub=None):
    """নামটি বাক্সের ডান পাশে — উপরে বসালে ক্রস-লিঙ্কের তার কেটে যায়।"""
    s.rect(x, y, w, h, "#FCFDFE", col, 2.4, 9)
    s.text(x + w + 18, y + h / 2 - 4, tag, T_NAME, col, 700, "start")
    if sub:
        s.text(x + w + 18, y + h / 2 + 28, sub, T_SMALL, GREY, 400,
               "start")


# ── ১. কোথায় দিক বদলাতে হয় ──────────────────────────────────────────────
def d01_idea():
    s = SVG(1240, 620)
    s.title("দুই দিকে মোটর চালানোর প্রয়োগ", T_TITLE)

    cards = [("ক্রেন ও হয়েস্ট", "ওঠা ও নামা", FWDC),
             ("শাটার ও গেট", "খোলা ও বন্ধ", STEEL),
             ("লেদ ও ড্রিল", "কাটা ও প্যাঁচ ছাড়া", AMBER),
             ("কনভেয়র", "সামনে ও পেছনে", REVC)]
    W, GAP, X0, Y = 262, 24, 58, 130
    for i, (name, what, col) in enumerate(cards):
        x = X0 + i * (W + GAP)
        s.rect(x, Y, W, 330, "#FCFDFE", col, 2.4, 13)
        s.box_auto(x + W / 2, Y + 16, name, T_BODY, fill=col, stroke=col,
                   tcolor="#FFFFFF", pad_x=18, pad_y=9)

        cy = Y + 170
        # দুই দিকের তির — সব কার্ডে এক প্রতীক
        s.path(f"M {x + 56} {cy} L {x + W - 56} {cy}", col, 4)
        s.path(f"M {x + 78} {cy - 18} L {x + 56} {cy} L {x + 78} {cy + 18}",
               col, 4)
        s.path(f"M {x + W - 78} {cy - 18} L {x + W - 56} {cy} "
               f"L {x + W - 78} {cy + 18}", col, 4)
        s.circle(x + W / 2, cy, 28, "#FFFFFF", col, 3.2)
        s.text(x + W / 2, cy + 8, "M", T_NAME, col, 700, "middle")
        s.text(x + W / 2, Y + 268, what, T_BODY, NAVY, 700, "middle")

    y = note_strip(s, 500, "একই মোটর ও একই সরবরাহ; যেকোনো দুটি ফেজ "
                           "অদলবদল করলে মোটর উল্টো দিকে ঘোরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. ফেজ ক্রম ও ঘূর্ণায়মান ক্ষেত্র ────────────────────────────────────
def _waves(s, x0, y0, w, h, order, cols):
    """তিনটি সাইন — order = ফেজের কোণের ক্রম (ডিগ্রিতে)।"""
    s.rect(x0, y0, w, h, "#FFFFFF", LINE, 1.6, 8)
    mid = y0 + h / 2
    s.line(x0 + 6, mid, x0 + w - 6, mid, LINE, 1.6)
    for ph, col in zip(order, cols):
        pts = []
        for i in range(0, 145):
            t = i / 144
            ang = math.radians(t * 720 + ph)
            pts.append(f"{x0 + 10 + t * (w - 20):.1f} "
                       f"{mid - math.sin(ang) * (h / 2 - 16):.1f}")
        s.path("M " + " L ".join(pts), col, 3)


def _rotor(s, cx, cy, r, cw, cols, labels):
    """তিন কয়েলের বৃত্ত — ভেতরে ঘোরার তির।"""
    s.circle(cx, cy, r, "#FFFFFF", GREY, 2.4)
    for i, (col, lab) in enumerate(zip(cols, labels)):
        a = math.radians(-90 + i * 120)
        px, py = cx + math.cos(a) * r, cy + math.sin(a) * r
        s.circle(px, py, 20, "#FFFFFF", col, 3.2)
        s.text(px, py + 7, lab, T_SMALL, col, 700, "middle")
    rr = r - 44
    if cw:
        s.path(f"M {cx - rr} {cy} A {rr} {rr} 0 1 1 {cx + rr} {cy}",
               FWDC, 4)
        s.path(f"M {cx + rr - 14} {cy - 14} L {cx + rr} {cy} "
               f"L {cx + rr - 14} {cy + 14}", FWDC, 4)
    else:
        s.path(f"M {cx + rr} {cy} A {rr} {rr} 0 1 0 {cx - rr} {cy}",
               REVC, 4)
        s.path(f"M {cx - rr + 14} {cy - 14} L {cx - rr} {cy} "
               f"L {cx - rr + 14} {cy + 14}", REVC, 4)


def d02_sequence():
    s = SVG(1240, 760)
    s.title("ফেজ সিকোয়েন্স বদলালে চুম্বকক্ষেত্র উল্টো দিকে ঘোরে",
            T_TITLE)

    for k, (x0, ttl, order, cw, col) in enumerate(
            [(46, "সিকোয়েন্স L1 - L2 - L3", (0, -120, -240), True, FWDC),
             (646, "সিকোয়েন্স L1 - L3 - L2", (0, -240, -120), False, REVC)]):
        panel(s, x0, 92, 548, 520, ttl, col)
        _waves(s, x0 + 36, 158, 476, 200, order, PHC)
        for i, (nm, c) in enumerate(zip(("L1", "L2", "L3"), PHC)):
            s.text(x0 + 60 + i * 112, 392, nm, T_BODY, c, 700, "middle")
            s.line(x0 + 24 + i * 112, 384, x0 + 48 + i * 112, 384, c, 4)
        _rotor(s, x0 + 274, 510, 92, cw, PHC, ("U", "V", "W"))
        s.text(x0 + 274, 628, "ঘোরে " + ("ঘড়ির কাঁটার দিকে"
                                          if cw else "উল্টো দিকে"),
               T_BODY, col, 700, "middle")

    y = note_strip(s, 656, "যেকোনো দুটি ফেজ অদলবদল করলে ফেজ সিকোয়েন্স "
                           "উল্টে যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d02_sequence.svg")


# ── ৩. কোন দুটি তার বদলাতে হয় ───────────────────────────────────────────
def d03_swap():
    s = SVG(1240, 700)
    s.title("সরবরাহ লাইনে দুই ফেজ অদলবদল", T_TITLE)

    for k, (x0, ttl, feed, col, arrow) in enumerate(
            [(46, "সামনের দিক", ("L1", "L2", "L3"), FWDC, "cw"),
             (646, "পেছনের দিক (L1 ও L3 অদলবদল)", ("L3", "L2", "L1"),
              REVC, "ccw")]):
        panel(s, x0, 92, 548, 470, ttl, col)
        TY, BY = 180, 330
        for i in range(3):
            x = x0 + 130 + i * 112
            c = PHC[("L1", "L2", "L3").index(feed[i])]
            s.text(x, TY - 22, feed[i], T_BODY, c, 700, "middle")
            s.path(f"M {x} {TY} L {x} {BY}", c, SW)
            node(s, x, TY, c)
        # মোটরের টার্মিনাল পাত
        s.rect(x0 + 92, BY, 356, 62, PLATE, SYM, 2.4, 7)
        for i, nm in enumerate(("U", "V", "W")):
            x = x0 + 130 + i * 112
            node(s, x, BY, SYM)
            s.text(x, BY + 42, nm, T_BODY, NAVY, 700, "middle")
        s.text(x0 + 274, BY + 92, "মোটরের টার্মিনাল বাক্স", T_SMALL, GREY,
               400, "middle")
        motor_sym(s, x0 + 274, BY + 168, 42, arrow)

    y = note_strip(s, 594, "মোটরের ভেতরের স্টার বা ডেল্টা সংযোগ বদলানো "
                           "হয় না; অদলবদল হয় শুধু বাইরের তিন তারে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_swap.svg")


# ── ৪. দুটো একসঙ্গে লাগলে ───────────────────────────────────────────────
def d04_danger():
    s = SVG(1240, 840)
    s.title("দুই কন্টাক্টর একসঙ্গে চালু হলে ফেজ-টু-ফেজ শর্ট", T_TITLE)

    KT, KB, JOIN = 300, 420, 520
    A0, B0, GAP = 300, 700, 84

    # দোষের পথ সবার আগে — মোটা ফ্যাকাশে লাল পটি, বাকি তার এর উপরে বসে
    s.path(f"M {A0} 150 L {A0} {JOIN} L {B0} {JOIN} L {B0} 234",
           "#F1948A", 16)
    for ax, ay, dx, dy in ((A0, 246, 0, 1), (530, JOIN, 1, 0),
                           (B0, 300, 0, -1)):
        chev(s, ax, ay, dx, dy)

    # তিন ফেজের বাস — নেস্টেড, ক্রসিং ছাড়া
    spans = [(A0, B0 + 2 * GAP, 150), (A0 + GAP, B0 + GAP, 192),
             (A0 + 2 * GAP, B0, 234)]
    for i, (xl, xr, yy) in enumerate(spans):
        s.path(f"M {xl} {yy} L {xr} {yy}", PHC[i], 3.6)
        s.text(xl - 22, yy + 8, ("L1", "L2", "L3")[i], T_BODY, PHC[i],
               700, "end")
        s.path(f"M {xl} {yy} L {xl} {KT}", PHC[i], 3.6)
        s.path(f"M {xr} {yy} L {xr} {KT}", PHC[i], 3.6)
        node(s, xl, yy, PHC[i])
        node(s, xr, yy, PHC[i])

    km_box(s, A0 - 46, KT - 6, 2 * GAP + 92, KB - KT + 12, "KM1", FWDC,
           "চালু")
    km_box(s, B0 - 46, KT - 6, 2 * GAP + 92, KB - KT + 12, "KM2", REVC,
           "চালু")
    pole_set(s, A0, GAP, KT, KB, True, SYM, tags=False)
    pole_set(s, B0, GAP, KT, KB, True, SYM, tags=False)

    join_bus(s, [(A0 + i * GAP, B0 + i * GAP, JOIN + i * 44)
                 for i in range(3)], KB)

    s.path(f"M 942 {JOIN} L {B0 + 20} {JOIN}", RED, 2.2, dash="8 6")
    s.text(944, JOIN + 8, "শর্ট সার্কিট কারেন্ট", T_CALL, RED, 700, "start")
    s.text(600, JOIN + 148, "L1 ও L3 যুক্ত হয়েছে U বিন্দুতে; মাঝে শুধু "
                            "দুই জোড়া কন্টাক্ট", T_NAME, RED, 700, "middle")

    y = note_strip(s, 720, "মাঝের ফেজ দুই দিকেই একই থাকে; একসঙ্গে চালু "
                           "হলে বাইরের দুই ফেজ সরাসরি যুক্ত হয়",
                   fill=REDBG, stroke=RED, tcolor=RED)
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_danger.svg")


# ── ৫. পাওয়ার সার্কিট ───────────────────────────────────────────────────
def d05_power():
    s = SVG(1240, 1040)
    s.title("ফরওয়ার্ড-রিভার্স স্টার্টারের পাওয়ার সার্কিট", T_TITLE)

    SUP, Q_Y = 108, 190
    KT, KB = 344, 452
    JOIN, F_Y, MOT = 534, 692, 868
    A0, B0, GAP = 250, 690, 84
    QX = [A0, A0 + GAP, A0 + 2 * GAP]

    # সরবরাহ ও Q1
    # প্রতিটি ফেজের আলাদা টার্মিনাল — তিন ফেজকে এক দাগে জুড়লে সেটা
    # ফেজ-টু-ফেজ শর্ট বোঝায়
    s.text(A0 - 40, SUP + 9, "সরবরাহ", T_BODY, NAVY, 700, "end")
    for i, x in enumerate(QX):
        node(s, x, SUP, PHC[i])
        s.text(x, SUP - 22, ("L1", "L2", "L3")[i], T_BODY, PHC[i], 700,
               "middle")
        s.path(f"M {x} {SUP} L {x} {Q_Y - 40}", PHC[i], 3.6)
    s.rect(A0 - 52, Q_Y - 40, 2 * GAP + 104, 80, PLATE, NAVY, 2.6, 8)
    for x in QX:
        s.path(f"M {x} {Q_Y - 24} L {x} {Q_Y + 24}", NAVY, 3.4)
    s.path(f"M {QX[0]} {Q_Y} L {QX[2]} {Q_Y}", NAVY, 2.2, dash="7 5")
    s.text(A0 + 2 * GAP + 74, Q_Y - 6, "Q1 — MCCB", T_BODY, NAVY, 700,
           "start")
    s.text(A0 + 2 * GAP + 74, Q_Y + 24, "শর্ট সার্কিট সুরক্ষা", T_SMALL,
           GREY, 400, "start")

    # নেস্টেড বাস:  যে ফেজ সবচেয়ে ডানে যাবে, তার বাস সবচেয়ে নিচে
    bus_y = [302, 274, 246]                    # L1, L2, L3
    dest = [B0 + 2 * GAP, B0 + GAP, B0]        # L1→5, L2→3, L3→1
    for i, x in enumerate(QX):
        s.path(f"M {x} {Q_Y + 40} L {x} {bus_y[i]}", PHC[i], 3.6)
        s.path(f"M {x} {bus_y[i]} L {dest[i]} {bus_y[i]}", PHC[i], 3.6)
        node(s, x, bus_y[i], PHC[i])
        s.path(f"M {x} {bus_y[i]} L {x} {KT}", PHC[i], 3.6)
        s.path(f"M {dest[i]} {bus_y[i]} L {dest[i]} {KT}", PHC[i], 3.6)
        node(s, dest[i], bus_y[i], PHC[i])

    km_box(s, A0 - 46, KT - 6, 2 * GAP + 92, KB - KT + 12, "KM1",
           FWDC, "সামনের দিক")
    km_box(s, B0 - 46, KT - 6, 2 * GAP + 92, KB - KT + 12, "KM2",
           REVC, "পেছনের দিক")
    pole_set(s, A0, GAP, KT, KB, False, SYM)
    pole_set(s, B0, GAP, KT, KB, False, SYM)

    # আউটপুট — দুই কন্টাক্টরের একই নম্বরের টার্মিনাল একই নোডে
    # একই নম্বরের টার্মিনাল একই নোডে — 2-2, 4-4, 6-6।  নোডের রং কালচে,
    # কারণ কোন ফেজ আসবে তা নির্ভর করে কোন কন্টাক্টর টেনেছে তার উপর।
    joins = [(A0 + i * GAP, B0 + i * GAP, JOIN + i * 44) for i in range(3)]
    join_bus(s, joins, KB, labels=None)
    for i, (xa, _, yy) in enumerate(joins):
        s.path(f"M {xa} {yy} L {xa} {F_Y - 34}", SYM, 3.6)

    # F2 — ওভারলোড রিলে
    s.rect(A0 - 52, F_Y - 34, 2 * GAP + 104, 96, "#FFFBF2", AMBER, 2.4, 8)
    for i, x in enumerate(QX):
        thermal_sym(s, x, F_Y + 14, 38, 54, SYM, 3.4)
        s.path(f"M {x} {F_Y + 41} L {x} {F_Y + 62}", SYM, 3.6)
    s.text(A0 + 2 * GAP + 74, F_Y + 6, "F2 — ওভারলোড রিলে", T_BODY, AMBER,
           700, "start")
    s.text(A0 + 2 * GAP + 74, F_Y + 36, "দুই দিকের জন্য একটি", T_SMALL,
           GREY, 400, "start")

    # মোটর
    # তিনটি লিড মোটরের বৃত্তে তিনটি আলাদা বিন্দুতে ঢোকে — এক বিন্দুতে
    # মিললে ছবিটি তিন ফেজের শর্ট বোঝায়
    for i, (x, nm) in enumerate(zip(QX, ("U", "V", "W"))):
        s.path(f"M {x} {F_Y + 62} L {x} {MOT - 84}", SYM, 3.6)
        ex = QX[1] + (i - 1) * 30
        ey = MOT - (46 if i == 1 else 35)
        s.path(f"M {x} {MOT - 84} L {x} {MOT - 66} L {ex} {ey}"
               if i != 1 else f"M {x} {MOT - 84} L {x} {ey}", SYM, 3.6)
        s.text(x - 18, MOT - 92, nm, T_SMALL, NAVY, 700, "end")
    motor_sym(s, QX[1], MOT, 46)
    earth(s, QX[1] + 46, MOT)
    s.text(QX[1] + 108, MOT + 8, "PE", T_BODY, GREEN, 700, "start")

    s.path(f"M 892 {JOIN + 16} L {B0 + 2 * GAP + 8} {JOIN + 2}", STEEL, 2.2)
    s.textlines(900, JOIN + 26, ["দুই কন্টাক্টরের একই নম্বরের",
                                 "টার্মিনাল এক বিন্দুতে"], T_SMALL, NAVY, 700)

    y = note_strip(s, 942, "KM1 ফেজ সিকোয়েন্স না বদলে দেয়, KM2 বাইরের দুই "
                            "ফেজ অদলবদল করে; ওভারলোড রিলে দুটির পরে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_power.svg")


# ── ৬. ক্রস-লিঙ্ক টার্মিনাল স্তরে ───────────────────────────────────────
def d06_crosslink():
    s = SVG(1240, 780)
    s.title("টার্মিনাল পর্যায়ে ক্রস-লিংক সংযোগ", T_TITLE)

    KT, KB = 380, 520
    A0, B0, GAP = 250, 700, 92

    # নেস্টেড লিঙ্ক — বাইরেরটা উপরে, ভেতরেরটা নিচে;  একটিও ক্রসিং নেই
    links = [(A0, B0 + 2 * GAP, 200, PH1, "1 → 5"),
             (A0 + GAP, B0 + GAP, 258, PH2, "3 → 3"),
             (A0 + 2 * GAP, B0, 316, PH3, "5 → 1")]
    for xa, xb, yy, col, lab in links:
        s.path(f"M {xa} {KT} L {xa} {yy} L {xb} {yy} L {xb} {KT}", col, 4)
        node(s, xa, KT, col)
        node(s, xb, KT, col)
        s.text((xa + xb) / 2, yy - 14, lab, T_SMALL, col, 700, "middle")

    km_box(s, A0 - 50, KT, 2 * GAP + 100, KB - KT, "KM1", FWDC)
    km_box(s, B0 - 50, KT, 2 * GAP + 100, KB - KT, "KM2", REVC)
    for x0, col in ((A0, FWDC), (B0, REVC)):
        for i in range(3):
            x = x0 + i * GAP
            s.rect(x - 26, KT - 4, 52, 34, "#D7E2EC", STEEL, 2, 4)
            s.text(x, KT + 20, str(2 * i + 1), T_TINY, NAVY, 700, "middle")
            s.rect(x - 26, KB - 30, 52, 34, "#D7E2EC", STEEL, 2, 4)
            s.text(x, KB - 6, str(2 * i + 2), T_TINY, NAVY, 700, "middle")

    # নিচের দিক — সোজা:  2-2, 4-4, 6-6।  সমান দুই সারি টার্মিনাল সোজা
    # জুড়তে গেলে সমতলে তিনটি ক্রসিং হয়ই;  ক্রসিংয়ে বিন্দু নেই।
    outs = [(A0, B0, 596, "U"), (A0 + GAP, B0 + GAP, 646, "V"),
            (A0 + 2 * GAP, B0 + 2 * GAP, 696, "W")]
    join_bus(s, [(xa, xb, yy) for xa, xb, yy, _ in outs], KB, sw=4,
             labels=None)
    for i, (xa, xb, yy, lab) in enumerate(outs):
        s.path(f"M {xa} {yy} L {A0 - 120} {yy}", SYM, 4)
        s.text(A0 - 134, yy + 8, lab, T_BODY, NAVY, 700, "end")
        s.text(xb + 34, yy + 8, f"{2 * i + 2} - {2 * i + 2}", T_SMALL,
               GREY, 400, "start")

    s.text(620, 150, "ওপরের তিনটি লিংক একটির ভেতরে আরেকটি বসানো, "
                     "তাই কোনো তার অন্যটিকে কাটে না",
           T_BODY, GREY, 400, "middle")

    y = note_strip(s, 740, "ওপরে উল্টো ক্রমে, নিচে একই নম্বরে সোজা সংযোগ; "
                           "বাজারের তৈরি লিংক-বারও এভাবে বসে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_crosslink.svg")


# ── ৭-৮. কন্ট্রোল সার্কিট ───────────────────────────────────────────────
# রাং ১:  P → [FWD 13-14 ‖ KM1 13-14] → REV 21-22 → KM2 21-22 → KM1 কয়েল
# রাং ২:  P → FWD 21-22 → [REV 13-14 ‖ KM2 13-14] → KM1 21-22 → KM2 কয়েল
# দুই বোতামের NO ও NC একই x-এ, তাই যান্ত্রিক সংযোগের ছেঁড়া রেখা খাড়া।
BX1, BX2, IX = 540, 680, 820       # বোতাম ১, বোতাম ২, অক্সিলিয়ারি NC
CX, RX = 972, 1164                 # কয়েলের শুরু, ডান পাশের নিউট্রাল
TAP = CX - 28                      # বাতির শাখা যেখান থেকে নামে


def _rung(s, y, items, coil_tag, coil_on, lamp_y, lamp_tag, lamp_col,
          latch_x, latch_y, latch_tag, latch_on):
    """একটি দিকের রাং।  items = [(x, kind, closed, tag, tagpos, a, b), …]

    tagpos:  "top" — কন্টাক্টের মাথায়;  "low" — নিচে (বোতামের কন্টাক্টে,
    কারণ মাথা দিয়ে বোতামের ছেঁড়া যান্ত্রিক রেখা নামে)।"""
    cur, x = LIVE, 500
    for (ix, kind, closed, tag, tagpos, ta, tb) in items:
        s.path(f"M {x} {y} L {ix} {y}", cur, SW)
        if kind == "no":
            _no(s, ix, y, cur, closed=closed)
        else:
            _nc(s, ix, y, cur, opened=not closed)
        if tag and tagpos == "top":
            s.text(ix + 46, y - 58, tag, T_SMALL, NAVY, 700, "middle")
        elif tagpos == "low":
            s.text(ix + 46, y + 76, tag, T_SMALL, NAVY, 700, "middle")
        elif tag:
            s.text(ix - 10, y - 26, tag, T_SMALL, NAVY, 700, "end")
        s.text(ix + 10, y + 36, ta, T_TINY, NAVY, 700, "middle")
        s.text(ix + 82, y + 36, tb, T_TINY, NAVY, 700, "middle")
        # ল্যাচ যে NO-র সমান্তরালে, সেটি খোলা থাকলেও পথ চালু থাকে
        passes = closed or (ix == latch_x and latch_on)
        cur = cur if passes else DEAD
        x = ix + 92
    s.path(f"M {x} {y} L {CX} {y}", cur, SW)
    node(s, TAP, y, cur)
    coil_sym(s, CX, y - 32, 130, 64, coil_tag)
    s.text(CX - 6, y - 40, "A1", T_TINY, NAVY, 700, "end")
    s.text(CX + 136, y - 40, "A2", T_TINY, NAVY, 700, "start")
    s.path(f"M {CX + 130} {y} L {RX} {y}", NEUT, SW)
    node(s, RX, y, NEUT)

    # ল্যাচ — যে NO-র সমান্তরালে, তার দুই নোড থেকে
    lc = LIVE if latch_on else DEAD
    s.path(f"M {latch_x} {y} L {latch_x} {latch_y} L {latch_x + 6} "
           f"{latch_y}", lc, SW)
    _no(s, latch_x + 6, latch_y, lc, closed=latch_on, w=80)
    s.path(f"M {latch_x + 86} {latch_y} L {latch_x + 92} {latch_y} "
           f"L {latch_x + 92} {y}", lc, SW)
    s.text(latch_x + 46, latch_y + 42, latch_tag, T_SMALL,
           LIVE if latch_on else GREY, 700, "middle")

    # বাতি — কয়েলের সমান্তরালে
    s.path(f"M {TAP} {y} L {TAP} {lamp_y} L {CX + 41} {lamp_y}",
           LIVE if coil_on else DEAD, SW)
    lamp(s, CX + 65, lamp_y, 24, on=coil_on, col=lamp_col)
    s.path(f"M {CX + 89} {lamp_y} L {RX} {lamp_y}", NEUT, SW)
    node(s, RX, lamp_y, NEUT)
    s.text(CX + 65, lamp_y + 54, lamp_tag, T_SMALL, lamp_col, 700, "middle")


def _ladder12(s, oy, state):
    """state = "fwd" / "rev" — কোন দিক চলছে।"""
    fwd, rev = state == "fwd", state == "rev"
    LY = oy + 150
    RF = LY + 190
    HF, LF = RF + 98, RF + 180
    RR = LF + 160
    HR, LR = RR + 98, RR + 180
    NY = LR + 84

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
    s.path(f"M 482 {LY} L 500 {LY} L 500 {RR}", LIVE, SW)
    node(s, 500, RF, LIVE)
    node(s, 500, RR, LIVE)

    # রাং ১ — সামনের দিক
    _rung(s, RF,
          [(BX1, "no", False, None, None, "13", "14"),
           (BX2, "nc", True, None, None, "21", "22"),
           (IX, "nc", not rev, "KM2", "top", "21", "22")],
          "KM1", fwd, LF, "H1: সামনে", FWDC, BX1, HF, "KM1 13-14", fwd)
    # রাং ২ — পিছনের দিক
    _rung(s, RR,
          [(BX1, "nc", True, "FWD", "low", "21", "22"),
           (BX2, "no", False, "REV", "left", "13", "14"),
           (IX, "nc", not fwd, "KM1", "top", "21", "22")],
          "KM2", rev, LR, "H2: পেছনে", REVC, BX2, HR, "KM2 13-14", rev)

    # দুই বোতাম — উপরে ছবি, দুই রাংয়ে দুই কন্টাক্ট, মাঝে ছেঁড়া রেখা
    # FWD-এর রাং ১-এ NO (খোলা), রাং ২-এ NC (বন্ধ);  REV-এর উল্টোটা।
    # ড্যাশ-রেখা দুই রাংয়েই নিজের ব্লেড ছুঁয়ে থামে — একই বোতাম যে দুটি
    # কন্টাক্টকেই নাড়ায়, ছবিটা তবেই তা বলে।
    _pb(s, BX1 + 46, RF, FWDC, "#BFE3CE", "FWD",
        tip=no_tip(BX1, RF, BX1 + 46))
    _pb(s, BX2 + 46, RF, REVC, "#E3D5F0", "REV",
        tip=nc_tip(BX2, RF, BX2 + 46))
    for bx, ty in ((BX1 + 46, nc_tip(BX1, RR, BX1 + 46)),
                   (BX2 + 46, no_tip(BX2, RR, BX2 + 46))):
        s.path(f"M {bx} {RF + 20} L {bx} {ty}", "#3B3B3B", 2.2, dash="7 5")

    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    return NY


def d07_fwd():
    s = SVG(1240, 1120)
    s.title("কন্ট্রোল সার্কিট: মোটর সামনের দিকে চলছে", T_TITLE)
    ny = _ladder12(s, 70, "fwd")
    y = note_strip(s, ny + 48, "KM1 চালু, তাই KM1 21-22 খোলা; KM1 না "
                               "ছাড়া পর্যন্ত KM2 চালু হতে পারবে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_fwd.svg")


def d08_rev():
    s = SVG(1240, 1120)
    s.title("কন্ট্রোল সার্কিট: মোটর পেছনের দিকে চলছে", T_TITLE)
    ny = _ladder12(s, 70, "rev")
    y = note_strip(s, ny + 48, "KM2 চালু, তাই KM2 21-22 খোলা; KM1-এর "
                               "কয়েলে সরবরাহ যেতে পারে না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_rev.svg")


# ── ৯. তিন স্তরের ইন্টারলক ──────────────────────────────────────────────
def d09_interlock():
    s = SVG(1240, 780)
    s.title("ইন্টারলকের তিন স্তর", T_TITLE)

    W, X0, Y, H = 376, 40, 100, 470
    for k, (ttl, col) in enumerate([("১. পুশ বাটন ইন্টারলক", STEEL),
                                    ("২. অক্সিলিয়ারি NC", GREEN),
                                    ("৩. যান্ত্রিক ইন্টারলক", MECH)]):
        panel(s, X0 + k * (W + 24), Y, W, H, ttl, col)

    # ১ — দুই কন্টাক্টের বোতাম
    x = X0 + 74
    s.rect(x + 52, 190, 84, 26, "#E3D5F0", REVC, 2.4, 6)
    s.text(x + 94, 174, "REV বাটন", T_SMALL, REVC, 700, "middle")
    s.path(f"M {x + 94} 216 L {x + 94} 338", "#3B3B3B", 2.2, dash="7 5")
    s.path(f"M {x + 94} 374 L {x + 94} 420", "#3B3B3B", 2.2, dash="7 5")
    _nc(s, x + 20, 300, DEAD, opened=True)
    s.text(x + 66, 356, "21-22 খোলে", T_SMALL, NAVY, 700, "middle")
    _no(s, x + 20, 420, LIVE, closed=True)
    s.text(x + 66, 476, "13-14 বন্ধ হয়", T_SMALL, NAVY, 700, "middle")
    s.text(X0 + W / 2, 528, "আগে 21-22 খোলে,", T_SMALL, GREY, 400,
           "middle")
    s.text(X0 + W / 2, 556, "তারপর 13-14 বন্ধ হয়", T_SMALL, GREY, 400,
           "middle")

    # ২ — মিরর কন্টাক্ট
    x = X0 + W + 24 + 52
    s.text(x + 136, 178, "KM1 চালু হলে", T_SMALL, NAVY, 700, "middle")
    coil_sym(s, x + 60, 208, 150, 60, "KM1")
    s.path(f"M {x + 135} 268 L {x + 135} {nc_tip(x + 90, 320, x + 135, opened=True)}", "#3B3B3B", 2.2, dash="7 5")
    _nc(s, x + 90, 320, DEAD, opened=True)
    s.text(x + 136, 376, "21-22 খোলে", T_SMALL, NAVY, 700, "middle")
    s.path(f"M {x + 182} 320 L {x + 250} 320 L {x + 250} 420 "
           f"L {x + 210} 420", DEAD, SW)
    coil_sym(s, x + 60, 390, 150, 60, "KM2")
    s.text(x + 136, 486, "KM2 চালু হতে পারে না", T_SMALL, GREY, 400,
           "middle")
    s.text(X0 + W + 24 + W / 2, 528, "মিরর কন্টাক্ট: মেইন কন্টাক্ট",
           T_SMALL, GREY, 400, "middle")
    s.text(X0 + W + 24 + W / 2, 556, "জোড়া লেগে গেলেও এটি বন্ধ হয় না",
           T_SMALL, GREY, 400, "middle")

    # ৩ — যান্ত্রিক লিভার
    bx = X0 + 2 * (W + 24) + 54
    for i, (cx, pulled) in enumerate(((bx + 46, True), (bx + 216, False))):
        s.rect(cx - 46, 220, 92, 150, PLATE, MECH, 2.4, 8)
        s.text(cx, 200, ("KM1", "KM2")[i], T_SMALL, (FWDC, REVC)[i], 700,
               "middle")
        s.rect(cx - 26, 250 + (18 if pulled else 0), 52, 60, BOXG, IRON_D,
               2.2, 5)
        s.text(cx, 392, "চালু" if pulled else "আটকানো", T_SMALL,
               LIVE if pulled else RED, 700, "middle")
    s.poly([(bx + 46, 256), (bx + 216, 240), (bx + 216, 262),
            (bx + 46, 278)], "#C9D2DB", MECH, 2.6)
    s.circle(bx + 131, 259, 9, "#FFFFFF", MECH, 2.6)
    s.text(bx + 131, 428, "রকার লিভার", T_SMALL, MECH, 700, "middle")
    s.text(X0 + 2 * (W + 24) + W / 2, 528, "একটি টানলে লিভার ঘুরে",
           T_SMALL, GREY, 400, "middle")
    s.text(X0 + 2 * (W + 24) + W / 2, 556, "অন্যটির পথ আটকে দেয়",
           T_SMALL, GREY, 400, "middle")

    y = note_strip(s, 616, "বাটন ভুল চাপা ঠেকায়, 21-22 কয়েলের সরবরাহ "
                           "ঠেকায়, লিভার আর্মেচার আটকে রাখে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_interlock.svg")


# ── ১০. সরাসরি উল্টো বনাম থামার সময় দিয়ে ───────────────────────────────
def _curve(s, px, ytop, h, pts, col, tmax, vmin=-1.0, vmax=1.0, zero=False,
           sw=3.4):
    ys = lambda v: ytop + h * (vmax - v) / (vmax - vmin)
    if zero:
        s.line(px(0), ys(0), px(tmax), ys(0), LINE, 1.6)
    s.path("M " + " L ".join(f"{px(t):.1f} {ys(v):.1f}" for t, v in pts),
           col, sw)
    return ys


def d10_timing():
    s = SVG(1240, 1140)
    s.title("প্লাগিং ও বিরতিসহ দিক বদল", T_TITLE)
    TMAX = 12

    panels = [
        (92, "প্লাগিং: চলন্ত অবস্থায় REV চাপা হয়েছে", RED,
         [(0.2, 5.1)], [(5.2, TMAX)],
         [(0, 0), (0.2, 0), (2.2, 1), (5.1, 1), (5.7, 0), (6.8, -1),
          (TMAX, -1)],
         [(0, 0.2), (0.15, 6), (2.2, 1), (5.1, 1), (5.2, 6), (6.8, 6),
          (7.6, 1), (TMAX, 1)],
         "কারেন্ট 6 × Ie পর্যন্ত ওঠে, উল্টো দিকে ঘোরা শুরু না হওয়া পর্যন্ত থাকে"),
        (572, "বিরতিসহ: REV-এর আগে মোটর থেমেছে", GREEN,
         [(0.2, 5.0)], [(8.0, TMAX)],
         [(0, 0), (0.2, 0), (2.2, 1), (5.0, 1), (8.0, 0), (10.2, -1),
          (TMAX, -1)],
         [(0, 0.2), (0.15, 6), (2.2, 1), (5.0, 1), (5.05, 0), (7.95, 0),
          (8.1, 6), (10.2, 1), (TMAX, 1)],
         "শুধু স্বাভাবিক স্টার্টিং কারেন্ট; কন্টাক্ট ও গিয়ারবক্সে চাপ কম"),
    ]

    for (py, ttl, col, km1, km2, spd, cur, note) in panels:
        panel(s, 30, py, 1180, 452, ttl, col)
        px, lows = timing(s, 330, py + 58, 760,
                          [("KM1", km1, FWDC), ("KM2", km2, REVC)],
                          TMAX, RH=64)
        # গতি
        s.text(310, py + 242, "গতি", T_SMALL, NAVY, 700, "end")
        ys = _curve(s, px, py + 198, 88, spd, STEEL, TMAX, zero=True)
        s.text(316, ys(1) + 6, "+", T_SMALL, GREY, 400, "end")
        s.text(316, ys(-1) + 6, "−", T_SMALL, GREY, 400, "end")
        # কারেন্ট
        s.text(310, py + 352, "কারেন্ট", T_SMALL, NAVY, 700, "end")
        yc = _curve(s, px, py + 306, 92, cur, RED, TMAX, vmin=0, vmax=7)
        for v, lab in ((1, "Ie"), (6, "6 × Ie")):
            s.line(330, yc(v), 1090, yc(v), LINE, 1.4, dash="6 5")
            s.text(1104, yc(v) + 7, lab, T_TINY, GREY, 400, "start")
        s.text(700, py + 430, note, T_BODY, col, 700, "middle")

    y = note_strip(s, 1044, "দিক বদলের আগে কয়েক সেকেন্ডের বিরতি "
                            "কন্টাক্টরের আয়ু বাড়ায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_timing.svg")


# ── ১১. প্যানেল ─────────────────────────────────────────────────────────
def d11_panel():
    s = SVG(1240, 880)
    s.title("প্যানেলের ভেতর ও দরজা", T_TITLE)

    panel(s, 40, 92, 700, 700, "ভেতরের মাউন্টিং প্লেট")
    s.rect(74, 150, 632, 590, "#F4F6F8", STEEL, 3, 6)

    # ডিন রেল ১ — Q1 ও কন্ট্রোল ফিউজ
    s.rect(112, 184, 556, 24, BOXG, IRON_D, 2, 3)
    s.rect(140, 208, 150, 96, PLATE, NAVY, 2.4, 6)
    s.text(215, 260, "Q1", T_NAME, NAVY, 700, "middle")
    s.text(215, 330, "MCCB", T_SMALL, GREY, 400, "middle")
    s.rect(320, 208, 120, 96, PLATE, AMBER, 2.4, 6)
    s.text(380, 260, "F1", T_NAME, AMBER, 700, "middle")
    s.text(380, 330, "কন্ট্রোল ফিউজ", T_SMALL, GREY, 400, "middle")

    # ডিন রেল ২ — দুই কন্টাক্টর, মাঝে যান্ত্রিক ইন্টারলক
    s.rect(112, 372, 556, 24, BOXG, IRON_D, 2, 3)
    for cx, tag, col in ((216, "KM1", FWDC), (400, "KM2", REVC)):
        s.rect(cx - 74, 396, 148, 136, PLATE, col, 2.6, 6)
        s.text(cx, 450, tag, T_NAME, col, 700, "middle")
        s.text(cx, 492, "LC1D09", T_SMALL, GREY, 400, "middle")
    s.rect(290, 434, 36, 60, "#E7ECF1", MECH, 2.6, 4)
    s.text(308, 566, "যান্ত্রিক ইন্টারলক", T_SMALL, MECH, 700, "middle")
    s.rect(500, 396, 148, 136, "#FFFBF2", AMBER, 2.6, 6)
    s.text(574, 450, "F2", T_NAME, AMBER, 700, "middle")
    s.text(574, 492, "ওভারলোড", T_SMALL, GREY, 400, "middle")

    # টার্মিনাল ব্লক
    s.rect(112, 606, 556, 24, BOXG, IRON_D, 2, 3)
    for i in range(14):
        s.rect(122 + i * 39, 630, 30, 52, "#D7E2EC", STEEL, 1.8, 3)
    s.text(390, 714, "টার্মিনাল ব্লক: বাইরের সব তার এখানে আসে", T_SMALL,
           GREY, 400, "middle")

    # ── দরজা ───────────────────────────────────────────────────────
    panel(s, 764, 92, 436, 700, "দরজার বাইরের দিক")
    s.rect(800, 150, 364, 590, "#FBFCFD", STEEL, 3, 8)

    for cx, col, tag in ((892, FWDC, "H1: সামনে"),
                         (1072, REVC, "H2: পেছনে")):
        s.circle(cx, 226, 32, "#FFFFFF", col, 3.2)
        s.circle(cx, 226, 19, "#F5C542" if col is FWDC else "#FFFFFF",
                 col, 2.4)
        s.text(cx, 296, tag, T_SMALL, col, 700, "middle")

    for cx, col, bg, tag in ((892, FWDC, "#BFE3CE", "FWD"),
                             (1072, REVC, "#E3D5F0", "REV")):
        s.circle(cx, 408, 40, bg, col, 3.4)
        s.text(cx, 418, tag, T_BODY, col, 700, "middle")
    s.circle(982, 566, 48, "#F6C9C4", RED, 3.6)
    s.circle(982, 566, 32, "#F6C9C4", RED, 2.6)
    s.text(982, 576, "STOP", T_BODY, RED, 700, "middle")
    s.text(982, 662, "লাল মাশরুম হেড, হাতের তালু দিয়ে চাপা যায়",
           T_SMALL, GREY, 400, "middle")

    y = note_strip(s, 812, "দুই দিকের জন্য দুটি বাতি; বড় STOP বাটন সবার "
                           "নিচে, যাতে জরুরি অবস্থায় দ্রুত চাপা যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_panel.svg")


ALL = [d01_idea, d02_sequence, d03_swap, d04_danger, d05_power,
       d06_crosslink, d07_fwd, d08_rev, d09_interlock, d10_timing,
       d11_panel]


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fn in ALL:
        print("  ", fn())
