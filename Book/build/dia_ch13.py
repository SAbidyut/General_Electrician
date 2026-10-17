# -*- coding: utf-8 -*-
"""অধ্যায় ১৩: ফ্লোট সুইচের ডায়াগ্রাম।

সার্কিট ও কানেকশন ডায়াগ্রাম ইনস্টিটিউটের নিজের ডেক থেকে হুবহু বসানো —
`HW Connection Diagram All.pptx` স্লাইড ২৫–২৮ (`assets_ch20.py`)।  হাতে
নতুন করে আঁকা হয়নি, কারণ হাতে আঁকলেই টপোলজি বদলে যাওয়ার ঝুঁকি
(অধ্যায় ৬-এর অভিজ্ঞতা)।

আলোকচিত্র উইকিমিডিয়া কমন্স থেকে।  যেটা কেটে খোলা সুইচের ভেতর দেখায়,
সেটাই এই অধ্যায়ের প্রধান ছবি — ইস্পাতের বল, লিভার আর মাইক্রোসুইচ,
তিনটিই এক ফ্রেমে।

যা সোর্সে নেই — ঘরের পানির ব্যবস্থায় সুইচটা কোথায় বসে, ভাসা-ডোবার
সঙ্গে কোন কন্টাক্ট বদলায়, মাল্টিমিটার দিয়ে COM চেনার নিয়ম, আর ডাবল
কন্ডিশনের দুই ট্যাংক — এগুলো নতুন আঁকা।

লেবেলের নিয়ম (অধ্যায় ১৫ থেকে কড়া):  প্যানেলের শিরোনাম বিশেষ্য,
যন্ত্রাংশের লেবেল এক-দুই শব্দ, নিচে এক লাইনের একটি নোট-পটি।  কারণ,
পরামর্শ ও সতর্কবাণী সবই বইয়ের লেখায় — ছবিতে নয়।

কালপুরুষে `Ω`, `∞`, `°` নেই — তাই কন্টিনিউইটির ফল লেখা হয়েছে
"বিপ" আর "নীরব" বলে, রোধের মান দিয়ে নয়।  `÷` কালপুরুষে `+` হয়ে
আঁকে, তাই ছবির লেবেলেও কখনো নয়।
"""
import os

from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, wrap, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch13")
IMG = os.path.join(HERE, "assets", "ch13")

T_TITLE = 34
T_NODE = 28
T_NAME = 24.5
T_BODY = 21.5
T_SMALL = 20
T_CALL = 24
T_TINY = 18.5

SYM = "#12324D"
SW = 3.4
LIVE = "#D42A1F"
NEUT = "#1F2933"
EARTH = "#1B6E47"
WATER = "#BFDCEF"
WATER_E = "#5E9EC8"
BOXG = "#E7ECF1"
METAL = "#8D9AA8"
PLATE = "#F4F7FA"
DEAD = "#9AA6B2"
FLOATC = "#F2C230"          # ফ্লোটের খোলস — বাজারে হলুদই বেশি


# ── shared helpers ──────────────────────────────────────────────────────
def panel(s, x, y, w, h, title, col=STEEL):
    """প্যানেলের শিরোনাম — কেবল নাম, কোনো মন্তব্য নয়।"""
    s.rect(x, y, w, h, "#FCFDFE", LINE, 1.8, 13)
    s.box_auto(x + w / 2, y + 12, title, T_BODY, fill=col, stroke=col,
               tcolor="#FFFFFF", pad_x=22, pad_y=9)


def note_strip(s, y, text, x=46, w=1148, fill="#EAF2FA", stroke=STEEL,
               tcolor=NAVY, size=T_NAME):
    """এক লাইনের তথ্য-পটি।  দুই লাইনে গড়ালে লেখাটা ছোট করতে হবে —
    ছবির নিচে অনুচ্ছেদ বসানো এই বইয়ের নিয়ম নয়।"""
    if tw(text, size, 700) > w - 60:
        raise ValueError(f"note_strip এক লাইনে ধরে না: {text!r}")
    s.rect(x, y, w, 58, fill, stroke, 2, 11)
    s.text(x + w / 2, y + 36, text, size, tcolor, 700, "middle")
    return y + 58


def callout(s, x, y, text, tx, ty, anchor="end", size=T_CALL, col=NAVY):
    """লেবেল ও লিডার — লেখার যে পাশে লক্ষ্য, সেই কিনারা থেকেই বেরোয়।"""
    s.text(x, y + size * 0.32, text, size, col, 700, anchor)
    w = tw(text, size, 700)
    x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle"
                                      else x - w)
    x1 = x0 + w
    # লিডার থামে বৃত্তের কিনারায়, আর ডগার চিহ্নটি ফাঁপা বৃত্ত — ভরাট
    # বিন্দু দিলে যে জিনিসটি দেখানো হচ্ছে সেটিই ঢাকা পড়ে যায়।
    start = x1 + 10 if tx > x1 else x0 - 10
    R = 6.0
    d = ((tx - start) ** 2 + (ty - y) ** 2) ** 0.5 or 1.0
    ex, ey = tx - (tx - start) / d * R, ty - (ty - y) / d * R
    s.path(f"M {start} {y} L {ex} {ey}", STEEL, 2.2)
    s.circle(tx, ty, R, "none", STEEL, 2.2)


def img_panel(s, x, y, w, h, title, img, col=STEEL):
    panel(s, x, y, w, h, title, col)
    s.image_fit(x + 16, y + 64, w - 32, h - 78, f"{IMG}/{img}", 6)


def photo_callouts(fname, title, img, left, right, note,
                   iw=430, top=104, gap=36, size=T_CALL, w=1240):
    """একটি আলোকচিত্র মাঝখানে, দুই পাশে লেবেল ও লিডার।

    অধ্যায় ১৯-এ শেখা তিনটি ফাঁদ এখানেই বাঁধা আছে:  (ক) ছবিটা আগে আঁকো,
    লিডার পরে — উল্টো করলে ছবিই লিডার ঢেকে দেয়;  (খ) লিডারের ডগা
    ছাপা লেখার পাশে রাখো, লেখার উপরে নয়;  (গ) প্রতিটি লেবেল তার
    নিজের লক্ষ্যের সমান উচ্চতায় বসে, নইলে একটি লিডার গোটা ছবি
    কোনাকুনি চিরে যায়।
    """
    from PIL import Image as _Im
    with _Im.open(f"{IMG}/{img}") as im:
        pw, ph = im.size
    ih = round(iw * ph / pw)
    ix = (w - iw) / 2
    s = SVG(w, top + ih + 130)
    s.title(title, T_TITLE)

    def place(items, side):
        if not items:
            return
        minsep = size * 2.0
        ys = [top + fy * ih for (_t, _fx, fy) in items]
        for i in range(1, len(ys)):
            ys[i] = max(ys[i], ys[i - 1] + minsep)
        over = ys[-1] - (top + ih - 12)
        if over > 0:
            ys = [y - over for y in ys]
        under = (top + 12) - ys[0]
        if under > 0:
            ys = [y + under for y in ys]
        for (text, fx, fy), ly in zip(items, ys):
            tx, ty = ix + fx * iw, top + fy * ih
            if side == "left":
                callout(s, ix - gap, ly, text, tx, ty, "end", size)
            else:
                callout(s, ix + iw + gap, ly, text, tx, ty, "start", size)

    s.image(ix, top, iw, ih, f"{IMG}/{img}")
    place(left, "left")
    place(right, "right")
    y = note_strip(s, top + ih + 30, note)
    s.fit(y, 24)
    return s.save(f"{OUT}/{fname}.svg")


def two_panel(fname, title, left, right, note, pw=560, gap=28, top=96,
              lcol=STEEL, rcol=GREEN, rw=None, ph=None):
    """দুই ছবির শিট — বাঁয়ে-ডানে দুটি প্যানেল, নিচে এক লাইনের নোট।"""
    from PIL import Image as _Im
    rw = rw or pw
    if ph is None:
        hs = []
        for w_, (_h, img) in ((pw, left), (rw, right)):
            with _Im.open(f"{IMG}/{img}") as im:
                iw_, ih_ = im.size
            hs.append(round((w_ - 32) * ih_ / iw_) + 78)
        ph = max(hs)
    s = SVG(1240, top + ph + 112)
    s.title(title, T_TITLE)
    total = pw + gap + rw
    x0 = (1240 - total) / 2
    img_panel(s, x0, top, pw, ph, left[0], left[1], lcol)
    img_panel(s, x0 + pw + gap, top, rw, ph, right[0], right[1], rcol)
    y = note_strip(s, top + ph + 26, note)
    s.fit(y, 24)
    return s.save(f"{OUT}/{fname}.svg")


# ── circuit / block helpers ─────────────────────────────────────────────
def node(s, x, y, col=SYM, r=6.5):
    s.circle(x, y, r, col)


def blk(s, cx, cy, text, w=None, h=64, fill="#FFFFFF", stroke=STEEL,
        size=T_BODY, tcol=NAVY, sw=2.6):
    w = w or tw(text, size, 700) + 46
    x, y = cx - w / 2, cy - h / 2
    s.rect(x, y, w, h, fill, stroke, sw, 10)
    s.text(cx, cy + size * 0.34, text, size, tcol, 700, "middle")
    return x, y, w, h


def chip(s, cx, cy, text, fill=LIGHT, stroke=STEEL, tcol=NAVY,
         size=T_SMALL):
    w = tw(text, size, 700) + 30
    s.rect(cx - w / 2, cy - 19, w, 38, fill, stroke, 2, 19)
    s.text(cx, cy + size * 0.34, text, size, tcol, 700, "middle")
    return w


def ground_hatch(s, y, x0, x1, col=GREY):
    """মাটির রেখা ও তার নিচের তির্যক দাগ।"""
    s.line(x0, y, x1, y, col, 3.2)
    x = x0 + 12
    while x < x1:
        s.path(f"M {x} {y} L {x - 14} {y + 16}", col, 2.0)
        x += 26


def water(s, x, y, w, h):
    s.rect(x, y, w, h, WATER, WATER_E, 2.2, 0)


def float_body(s, cx, cy, ang=0.0, r=26):
    """ফ্লোটের খোলস — কাত হলে ang ডিগ্রি ঘোরে (কেবল-ফ্লোট)।"""
    s.ellipse(cx, cy, r * 1.15, r * 0.86, FLOATC, "#8A6D14", 2.6)


def micro_contact(s, x, y, closed_nc, wlen=150):
    """ছোট কন্টাক্ট-চিত্র:  COM থেকে লিভার, উপরে NC নিচে NO।

    যেটি বন্ধ, সেটিতেই লিভার ঠেকে থাকে; অন্যটি ধূসর।
    """
    s.text(x - 14, y + 7, "COM", T_SMALL, NAVY, 700, "end")
    node(s, x, y)
    ty, by = y - 46, y + 46
    tip = (x + wlen * 0.78, ty if closed_nc else by)
    s.path(f"M {x} {y} L {tip[0]:.0f} {tip[1]:.0f}",
           LIVE if closed_nc else DEAD, 3.6)
    for yy, name, on in ((ty, "NC", closed_nc), (by, "NO", not closed_nc)):
        col = LIVE if on else DEAD
        node(s, x + wlen * 0.78, yy, col, 6)
        s.path(f"M {x + wlen * 0.78:.0f} {yy} L {x + wlen:.0f} {yy}", col, 3.2)
        s.text(x + wlen + 12, yy + 7, name, T_SMALL, col, 700, "start")


# ── ১. ঘরের পানির ব্যবস্থায় ফ্লোট সুইচ ─────────────────────────────────
def d01_system():
    """পাম্প, রিজার্ভার, ছাদের ট্যাংক আর ডিবি — একই ছবিতে।

    তারের পথগুলো হিসাব করে বসানো, যাতে কোনোটাই আরেকটাকে না কাটে:
    সাপ্লাই পাইপ ওঠে x = ২৫০ বরাবর, কন্ট্রোল কেবল নামে x = ৬৯০ বরাবর,
    আর পাম্পের পাওয়ার কেবল যায় y = ৪৯০ বরাবর — তিনটির কোনো মিল নেই।
    """
    s = SVG(1240, 780)
    s.title("ঘরের পানির ব্যবস্থায় ফ্লোট সুইচ", T_TITLE)

    # ছাদের ট্যাংক ও তার পায়া
    s.rect(700, 128, 450, 140, "#FFFFFF", NAVY, 3.0, 6)
    water(s, 704, 200, 442, 64)
    s.text(990, 172, "ছাদের ট্যাংক", T_NAME, NAVY, 700, "middle")
    for lx in (740, 1110):
        s.path(f"M {lx} 268 L {lx} 470", METAL, 5.0)
    s.path("M 700 268 L 1150 268", METAL, 5.0)

    # সাপ্লাই পাইপ:  পাম্প → উপরে → ট্যাংকের মাথা
    s.path("M 200 367 L 200 84 L 940 84 L 940 128", WATER_E, 5.0)
    s.text(222, 240, "সাপ্লাই পাইপ", T_BODY, WATER_E, 700, "start")

    # ফ্লোট সুইচ ট্যাংকের ভেতর
    s.rect(757, 137, 26, 26, METAL, GREY, 2, 4)
    s.path("M 770 163 L 850 214", "#3B3B3B", 3.0)
    float_body(s, 866, 224, r=22)
    s.text(1010, 232, "ফ্লোট সুইচ", T_BODY, NAVY, 700, "middle")

    # কন্ট্রোল কেবল:  ট্যাংক → ডিবি
    s.path("M 700 150 L 610 150 L 610 320", "#3B3B3B", 3.0, dash="10 7")
    s.text(598, 240, "কন্ট্রোল ক্যাবল", T_BODY, GREY, 700, "end")

    # ডিবি
    s.rect(520, 320, 180, 140, PLATE, NAVY, 2.8, 8)
    s.text(610, 358, "DB", T_NAME, NAVY, 700, "middle")
    chip(s, 610, 398, "MCB")
    chip(s, 610, 438, "KM1")

    # ডিবি → পাম্প (পাওয়ার কেবল)
    s.path("M 520 396 L 318 396", NEUT, 3.2)
    s.text(419, 368, "পাওয়ার ক্যাবল", T_BODY, GREY, 700, "middle")

    # পাম্প
    blk(s, 230, 396, "পাম্প", 176, 58, "#FFFFFF", STEEL, T_NAME, STEEL, 3.0)

    # মাটি ও রিজার্ভার
    ground_hatch(s, 470, 40, 1200)
    s.rect(80, 490, 300, 150, "#FFFFFF", NAVY, 2.8, 4)
    water(s, 84, 552, 292, 84)
    s.text(230, 672, "আন্ডারগ্রাউন্ড রিজার্ভার", T_BODY, NAVY, 700, "middle")
    s.path("M 280 425 L 280 490", WATER_E, 5.0)

    y = note_strip(s, 700, "ফ্লোট সুইচ কয়েল চালায়; পাম্পের কারেন্ট "
                           "যায় কন্টাক্টরের ভেতর দিয়ে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_system.svg")


# ── ২. বাইরের অংশ ───────────────────────────────────────────────────────
def d02_parts():
    return photo_callouts(
        "d02_parts", "ক্যাবল-ফ্লোট সুইচের অংশ", "ph_cable.jpg",
        # লক্ষ্যের উচ্চতার ক্রমেই তালিকা — উল্টো থাকলে দুই লিডার
        # ফ্লোটের গা বেয়ে একে অন্যকে কাঁচি করে কাটে
        left=[("ক্যাবলের মুখ", 0.44, 0.12), ("ফ্লোট বডি", 0.18, 0.66)],
        right=[("কাউন্টার-ওয়েট", 0.66, 0.24), ("তিন-কোর ক্যাবল", 0.84, 0.76)],
        note="ওজনটি যেখানে বাঁধা, ফ্লোট তার চারপাশেই ওঠানামা করে",
        iw=720)


# ── ৩. ভেতরের অংশ ───────────────────────────────────────────────────────
def d03_inside():
    return photo_callouts(
        "d03_inside", "ফ্লোট সুইচের ভেতরে", "ph_cut_on.jpg",
        left=[("ক্যাবল", 0.14, 0.30), ("মাইক্রোসুইচ", 0.45, 0.40)],
        right=[("ইস্পাতের বল", 0.63, 0.42), ("লিভার", 0.76, 0.55)],
        note="বল গড়িয়ে লিভারকে ঠেলে, লিভার মাইক্রোসুইচের পিন চাপে",
        iw=760)


# ── ৪. দুই অবস্থা ───────────────────────────────────────────────────────
def d04_states():
    return two_panel(
        "d04_states", "কেটে খোলা সুইচের দুই অবস্থা",
        ("অফ অবস্থা", "ph_cut_off.jpg"),
        ("অন অবস্থা", "ph_cut_on.jpg"),
        "একই সুইচ; শুধু বলের অবস্থান বদলেছে",
        lcol=GREY, rcol=GREEN)


# ── ৫. কাজের নীতি ───────────────────────────────────────────────────────
def d05_action():
    """পানি নিচে ও পানি উপরে — কোন কন্টাক্ট বন্ধ থাকে।"""
    s = SVG(1240, 660)
    s.title("পানির উচ্চতা ও কন্টাক্টের অবস্থা", T_TITLE)

    PW, PH, PY = 564, 440, 96
    for i, (title_, low, col) in enumerate(
            (("পানি নিচে", True, STEEL), ("পানি উপরে", False, GREEN))):
        px = 46 + i * (PW + 20)
        panel(s, px, PY, PW, PH, title_, col)

        # ট্যাংক
        tx, ty, tw_, th = px + 46, PY + 62, PW - 92, 200
        s.rect(tx, ty, tw_, th, "#FFFFFF", NAVY, 2.6, 4)
        wh = 44 if low else 140
        water(s, tx + 3, ty + th - wh, tw_ - 6, wh - 3)

        # কেবলের বাঁধন ও ফ্লোট
        ax, ay = tx + 70, ty + 26
        s.rect(ax - 13, ay - 13, 26, 26, METAL, GREY, 2, 4)
        if low:
            s.path(f"M {ax} {ay} L {ax + 12} {ay + 118}", "#3B3B3B", 3.0)
            float_body(s, ax + 14, ay + 138)
        else:
            s.path(f"M {ax} {ay} L {ax + 118} {ay + 52}", "#3B3B3B", 3.0)
            float_body(s, ax + 142, ay + 62)

        # কোন কন্টাক্ট বন্ধ
        micro_contact(s, px + 128, PY + 352, low, 150)

    y = note_strip(s, 562, "ফ্লোট নিচে নামলে NC বন্ধ, উপরে উঠলে NO বন্ধ")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_action.svg")


# ── ৬. মাল্টিমিটারে COM চেনা ────────────────────────────────────────────
def d06_test():
    """তিন তারের কোনটি COM — কন্টিনিউইটি টেস্টে বেরিয়ে আসে।"""
    s = SVG(1240, 700)
    s.title("কন্টিনিউইটি টেস্টে COM, NO ও NC শনাক্তকরণ", T_TITLE)

    # বাঁয়ে ফ্লোট সুইচ ও তিন তার
    fx, fy = 210, 250
    float_body(s, fx, fy, r=44)
    s.text(fx, fy + 92, "ফ্লোট সুইচ", T_BODY, NAVY, 700, "middle")
    for i, (nm, dy) in enumerate((("তার ১", -66), ("তার ২", 0),
                                  ("তার ৩", 66))):
        s.path(f"M {fx + 52} {fy} L {fx + 120} {fy + dy} "
               f"L {fx + 196} {fy + dy}", "#3B3B3B", 3.0)
        node(s, fx + 196, fy + dy)
        s.text(fx + 210, fy + dy + 7, nm, T_BODY, NAVY, 700, "start")

    # ডানে ফলের ছক।  ডান কিনারা ১১৮০ — নোট-পটির ১১৯৪ পেরোয় না।
    gx, gy, lw = 610, 148, 150
    cw, rh = 140, 62
    gw = lw + 3 * cw
    heads = ["১–২", "১–৩", "২–৩"]
    rows = [("ফ্লোট নিচে", ["বিপ", "নীরব", "নীরব"]),
            ("ফ্লোট উপরে", ["নীরব", "বিপ", "নীরব"])]
    s.rect(gx, gy, gw, rh * 3, "#FFFFFF", LINE, 2, 8)
    for c, h in enumerate(heads):
        s.text(gx + lw + c * cw + cw / 2, gy + rh * 0.64, h, T_NAME, NAVY,
               700, "middle")
    s.line(gx, gy + rh, gx + gw, gy + rh, LINE, 2)
    for r, (nm, vals) in enumerate(rows):
        ry = gy + rh * (r + 1)
        s.text(gx + lw / 2, ry + rh * 0.64, nm, T_BODY, NAVY, 700, "middle")
        for c, v in enumerate(vals):
            col = GREEN if v == "বিপ" else GREY
            s.text(gx + lw + c * cw + cw / 2, ry + rh * 0.64, v, T_BODY,
                   col, 700, "middle")
        if r:
            s.line(gx, ry, gx + gw, ry, LINE, 2)
    for c in range(4):
        s.line(gx + lw + c * cw, gy, gx + lw + c * cw, gy + rh * 3, LINE, 2)

    # ফল — বাক্য নয়, কেবল মিল
    for i, (a, b) in enumerate((("তার ১", "COM"), ("তার ২", "NC"),
                                ("তার ৩", "NO"))):
        cx = gx + 100 + i * 200
        chip(s, cx, 400, f"{a} = {b}", GREENBG, GREEN, GREEN, T_NAME)

    y = note_strip(s, 466, "মিটার বিপ মোডে; সুইচ সরবরাহ থেকে বিচ্ছিন্ন")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_test.svg")


# ── ৭. সরাসরি সংযোগ ─────────────────────────────────────────────────────
def d07_direct():
    """ছোট পাম্পে কন্টাক্টর ছাড়া সংযোগ — পুরো কারেন্ট সুইচের ভেতর দিয়ে।"""
    s = SVG(1240, 560)
    s.title("ছোট পাম্পে সরাসরি সংযোগ", T_TITLE)

    LY, NY = 190, 400
    s.text(96, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(96, NY + 9, "N", T_NODE, NEUT, 700, "end")

    # লাইভ লাইন:  MPCB → ফ্লোট সুইচ → মোটর।  ০.৩৭৬ kW-এর বেশি পাম্পে
    # বিএনবিসি ১.৩.২২(গ)-র ওভারলোড সুরক্ষা MPCB-ই দেয় (অধ্যায় ৯-এর ৯.১১)।
    s.path(f"M 112 {LY} L 300 {LY}", LIVE, SW)
    # MCB
    s.rect(300, LY - 44, 96, 88, PLATE, NAVY, 2.6, 8)
    s.text(348, LY - 56, "MPCB", T_BODY, NAVY, 700, "middle")
    s.path(f"M 348 {LY - 26} L 348 {LY + 26}", NAVY, 3.0)
    s.path(f"M 396 {LY} L 560 {LY}", LIVE, SW)

    # ফ্লোট সুইচের প্রতীক
    node(s, 560, LY, LIVE)
    s.path(f"M 560 {LY} L 648 {LY - 40}", LIVE, SW)
    node(s, 664, LY, LIVE)
    s.path(f"M 664 {LY} L 880 {LY}", LIVE, SW)
    s.text(612, LY - 62, "ফ্লোট সুইচ", T_BODY, NAVY, 700, "middle")
    s.path(f"M 596 {LY + 18} L 596 {LY + 60}", "#3B3B3B", 2.6)
    float_body(s, 596, LY + 82, r=20)

    # মোটর
    s.path(f"M 880 {LY} L 880 {LY + 52}", LIVE, SW)
    s.circle(880, 295, 52, "#FFFFFF", SYM, SW)
    s.text(880, 307, "M", T_NODE, SYM, 700, "middle")
    s.text(966, 302, "পাম্প মোটর", T_BODY, NAVY, 700, "start")
    s.text(348, LY + 76, "মোটরের কারেন্টে সেট", T_SMALL, GREY, 700,
           "middle")
    s.path(f"M 880 {295 + 52} L 880 {NY}", NEUT, SW)

    # নিউট্রাল
    s.path(f"M 112 {NY} L 1000 {NY}", NEUT, SW)
    node(s, 880, NY, NEUT)

    y = note_strip(s, 462, "পাম্পের পুরো কারেন্ট ফ্লোট সুইচের কন্টাক্টের "
                           "ভেতর দিয়েই যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_direct.svg")


# ── ৮. কন্টাক্টরের টার্মিনাল ────────────────────────────────────────────
def d08_contactor():
    return photo_callouts(
        "d08_contactor", "ম্যাগনেটিক কন্টাক্টরের টার্মিনাল",
        "ph_contactor.jpg",
        left=[("কয়েল A1", 0.35, 0.13), ("ইনপুট 1 3 5", 0.505, 0.305)],
        right=[("কয়েল A2", 0.70, 0.11), ("অক্সিলিয়ারি 13-14", 0.845, 0.305),
               ("আউটপুট 2 4 6", 0.615, 0.80)],
        note="ফ্লোট সুইচ বসে কয়েলের A1-এর লাইনে; A2 যায় নিউট্রালে",
        iw=560)


# ── ৯–১০ ও ১৩. পাম্প কন্ট্রোলের সার্কিট (হাতে আঁকা) ───────────────────
# আগের d09/d10 ছিল ইনস্টিটিউটের স্লাইড ২৫–২৮ হুবহু।  দুটি কারণে সেগুলো
# বাদ:  (ক) সিঙ্গেল কন্ডিশনের স্লাইড COM–NO দিয়ে আঁকা, অর্থাৎ খালি করার
# সংযোগ, অথচ অধ্যায়ের মূল কাজ ছাদের ট্যাংক ভরা (COM–NC);  (খ) কোনো
# স্লাইডেই ওভারলোড রিলে নেই, অথচ বিএনবিসি ১.৩.২২(গ) ০.৩৭৬ kW-এর বেশি
# মোটরে ওভারকারেন্ট সুরক্ষা চায় (অধ্যায় ৯-এর ৯.১.১)।  নাম অধ্যায় ৯-এর
# রীতিতে:  Q1 মেইন ব্রেকার, F1 কন্ট্রোল ফিউজ/এমসিবি, F2 ওভারলোড রিলে,
# KM1 কন্টাক্টর।
#
# তারের তালিকা (ছবি আঁকার আগে লেখা, অধ্যায় ১৪-এর নিয়মে):
#   সিঙ্গেল কন্ডিশন  L → F1 → F2:95;  F2:96 → FS:COM;  FS:NC → KM1:A1;
#                     KM1:A2 → N।
#   ডাবল কন্ডিশন     L → F1 → F2:95;  F2:96 → FS-1:COM;  FS-1:NO →
#                     FS-2:COM;  FS-2:NC → KM1:A1;  KM1:A2 → N।
#   অটো-ম্যানুয়াল     L → F1 → F2:95;  F2:96 → S1 (AUTO ও MAN দুই
#                     কন্টাক্টের ইনপুট);  S1 AUTO → FS-1:COM;  FS-1:NO →
#                     FS-2:COM;  FS-2:NC → KM1:A1;  S1 MAN → STOP:11;
#                     STOP:12 → START:13 ও KM1:13;  START:14 ও KM1:14 →
#                     KM1:A1;  KM1:A2 → N।
#   AUTO-তে MAN শাখার দিকে উল্টো পথ খোঁজা হয়েছে:  A1 → KM1 13-14 → STOP
#   → S1 MAN (খোলা) — থামে।  তাই AUTO-তে ল্যাচ হয় না, ট্যাংক ভরলে কয়েল
#   ছাড়ে।  MAN-এ উল্টো পথ A1 → FS-2 → FS-1 → S1 AUTO (খোলা) — থামে।
#   পাওয়ার:  L → Q1 → KM1 1-2 → F2 (তিন পোল সিরিজে, ৯.১০) → পাম্প;
#             N → Q1 → KM1 3-4 → পাম্প।
from dia_ch08 import coil_sym                                    # noqa: E402
from dia_ch09 import (fuse, thermal_sym, _nc, _no, _pb, nc_tip,  # noqa: E402
                      no_tip)

CW = SYM          # স্থির ছবি — তারের এক রং; লাইভ-নিউট্রাল লেবেলে


def float_act(s, cx, blade_y, top, name, sub=None):
    """ফ্লোটের প্রতীক — ব্লেড থেকে ড্যাশ-রেখা উপরে একটি ভাসমান খোলস।"""
    s.path(f"M {cx} {blade_y:.0f} L {cx} {top + 14}", "#3B3B3B", 2.2,
           dash="7 5")
    float_body(s, cx, top, r=16)
    s.text(cx, top - 30, name, T_SMALL, NAVY, 700, "middle")
    if sub:
        s.text(cx, top - 56, sub, T_TINY, GREY, 700, "middle")


def f2_contact(s, x, LY):
    """F2-এর 95-96 (NC), উপরে থার্মাল প্রতীক।"""
    _nc(s, x, LY, CW)
    s.path(f"M {x + 40} {nc_tip(x, LY, x + 40):.0f} L {x + 40} {LY - 64}",
           SYM, 2, dash="6 5")
    thermal_sym(s, x + 40, LY - 88, 34, 40, SYM, 2.4)
    s.text(x + 66, LY - 112, "F2", T_SMALL, AMBER, 700, "start")
    s.text(x + 10, LY + 36, "95", T_TINY, NAVY, 700, "middle")
    s.text(x + 92, LY + 36, "96", T_TINY, NAVY, 700, "middle")


def fs_contact(s, x, LY, kind, name, sub=None):
    """ফ্লোট সুইচের কন্টাক্ট:  kind = "NC" বা "NO" (ফ্লোট নিচে অবস্থায়)।"""
    if kind == "NC":
        _nc(s, x, LY, CW)
        tip = nc_tip(x, LY, x + 46)
    else:
        _no(s, x, LY, CW)
        tip = no_tip(x, LY, x + 46)
    float_act(s, x + 46, tip, LY - 92, name, sub)
    s.text(x + 4, LY + 36, "COM", T_TINY, NAVY, 700, "middle")
    s.text(x + 92, LY + 36, kind, T_TINY, NAVY, 700, "middle")


def coil13(s, x, LY):
    coil_sym(s, x, LY - 40, 116, 80, "KM1")
    s.text(x - 10, LY - 50, "A1", T_TINY, NAVY, 700, "end")
    s.text(x + 126, LY - 50, "A2", T_TINY, NAVY, 700, "start")


def _power13(s, x0, y0):
    """সিঙ্গেল ফেজ পাম্পের পাওয়ার সার্কিট, খাড়া করে।"""
    XL, XN = x0 + 120, x0 + 240
    s.text(XL, y0, "L", T_NODE, LIVE, 700, "middle")
    s.text(XN, y0, "N", T_NODE, NEUT, 700, "middle")
    Q, K, F, M = y0 + 70, y0 + 180, y0 + 292, y0 + 404
    for x in (XL, XN):
        s.path(f"M {x} {y0 + 16} L {x} {Q - 34}", CW, SW)
    # Q1
    s.rect(XL - 34, Q - 34, XN - XL + 68, 68, PLATE, NAVY, 2.6, 8)
    for x in (XL, XN):
        s.path(f"M {x} {Q - 20} L {x} {Q + 20}", NAVY, 3.2)
    s.path(f"M {XL} {Q} L {XN} {Q}", NAVY, 2.0, dash="7 5")
    s.text(XL - 46, Q + 8, "Q1", T_BODY, NAVY, 700, "end")
    for x in (XL, XN):
        s.path(f"M {x} {Q + 34} L {x} {K - 34}", CW, SW)
    # KM1 মেইন কন্টাক্ট (খোলা)
    for x, a, b in ((XL, "1", "2"), (XN, "3", "4")):
        node(s, x, K - 34, CW)
        s.path(f"M {x} {K - 34} L {x + 30} {K + 20}", DEAD, SW)
        node(s, x, K + 34, CW)
        s.text(x - 14, K - 26, a, T_TINY, NAVY, 700, "end")
        s.text(x - 14, K + 46, b, T_TINY, NAVY, 700, "end")
    s.path(f"M {XL + 16} {K - 4} L {XN + 16} {K - 4}", GREEN, 2.0,
           dash="7 5")
    s.text(XL - 46, K + 8, "KM1", T_BODY, GREEN, 700, "end")
    s.path(f"M {XL} {K + 34} L {XL} {F - 34}", CW, SW)
    # F2 — থার্মাল উপাদান, কেবল L পথে আঁকা (তিন পোল সিরিজে, ৯.১০)
    s.rect(XL - 40, F - 46, 80, 92, "#FFFBF2", AMBER, 2.2, 8, dash="7 5")
    s.path(f"M {XL} {F - 34} L {XL} {F - 28}", CW, SW)
    thermal_sym(s, XL, F, 34, 56, CW, 3.0)
    s.path(f"M {XL} {F + 28} L {XL} {F + 34}", CW, SW)
    s.text(XL - 46, F + 8, "F2", T_BODY, AMBER, 700, "end")
    # মোটর
    s.path(f"M {XL} {F + 34} L {XL} {M - 40} L {XL + 34} {M - 40}", CW, SW)
    s.path(f"M {XN} {K + 34} L {XN} {M - 40} L {XN - 34} {M - 40}", CW, SW)
    cx = (XL + XN) / 2
    s.circle(cx, M, 44, "#FFFFFF", SYM, 3.4)
    s.text(cx, M - 2, "M", T_NODE, SYM, 700, "middle")
    s.text(cx, M + 26, "1 ~", T_TINY, SYM, 700, "middle")
    s.text(cx + 58, M + 8, "পাম্প", T_BODY, NAVY, 700, "start")
    return M + 44


def d09_single():
    s = SVG(1240, 760)
    s.title("সিঙ্গেল কন্ডিশনে ছাদের ট্যাংক ভরার সার্কিট", T_TITLE)
    panel(s, 46, 96, 420, 560, "পাওয়ার সার্কিট", STEEL)
    _power13(s, 76, 186)
    panel(s, 486, 96, 708, 560, "কন্ট্রোল সার্কিট", GREEN)

    LY, NY, RX = 380, 560, 1150
    s.text(528, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(528, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 540 {LY} L 562 {LY}", CW, SW)
    fuse(s, 598, LY, 72, 42, "F1")
    s.path(f"M 634 {LY} L 660 {LY}", CW, SW)
    f2_contact(s, 660, LY)
    s.path(f"M 752 {LY} L 800 {LY}", CW, SW)
    fs_contact(s, 800, LY, "NC", "FS")
    s.path(f"M 892 {LY} L 960 {LY}", CW, SW)
    coil13(s, 960, LY)
    s.path(f"M 1076 {LY} L {RX} {LY} L {RX} {NY}", NEUT, SW)
    s.path(f"M 540 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)

    y = note_strip(s, 680, "ভরার সংযোগ COM–NC; খালি করার কাজে তারটি "
                           "NC থেকে NO-তে যাবে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d09_single.svg")


def d10_double():
    s = SVG(1240, 460)
    s.title("ডাবল কন্ডিশনের কন্ট্রোল সার্কিট", T_TITLE)
    LY, NY, RX = 250, 350, 1130
    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", CW, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 260 {LY}", CW, SW)
    f2_contact(s, 260, LY)
    s.path(f"M 352 {LY} L 440 {LY}", CW, SW)
    fs_contact(s, 440, LY, "NO", "FS-1", "রিজার্ভার")
    s.path(f"M 532 {LY} L 640 {LY}", CW, SW)
    fs_contact(s, 640, LY, "NC", "FS-2", "ছাদের ট্যাংক")
    s.path(f"M 732 {LY} L 860 {LY}", CW, SW)
    coil13(s, 860, LY)
    s.path(f"M 976 {LY} L {RX} {LY} L {RX} {NY}", NEUT, SW)
    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    y = note_strip(s, 386, "দুই সুইচ সিরিজে; দুটির কন্টাক্টই বন্ধ হলে "
                           "কয়েলে সরবরাহ যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_double.svg")


def d13_automan():
    """অটো-ম্যানুয়াল:  S1 (MAN–0–AUTO) দুই শাখার একটি বেছে নেয়।"""
    s = SVG(1240, 760)
    s.title("অটো-ম্যানুয়াল সিলেক্টর সুইচসহ কন্ট্রোল সার্কিট", T_TITLE)
    LY = 250                 # AUTO শাখা
    MY = LY + 180            # MAN শাখা
    HB = MY + 96             # হোল্ডিং শাখা
    NY = HB + 104
    RX = 1150
    P = 400                  # শাখা যেখানে ভাগ হয়
    SX = 432                 # S1-এর দুই কন্টাক্ট
    X = 1000                 # কয়েলের আগের নোড
    AX, BX = 780, 900        # START-এর দুই নোড

    s.text(70, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(70, NY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 82 {LY} L 118 {LY}", CW, SW)
    fuse(s, 154, LY, 72, 42, "F1")
    s.path(f"M 190 {LY} L 236 {LY}", CW, SW)
    f2_contact(s, 236, LY)
    s.path(f"M 328 {LY} L {SX} {LY}", CW, SW)
    node(s, P, LY, CW)
    s.path(f"M {P} {LY} L {P} {MY} L {SX} {MY}", CW, SW)

    # S1 — দুই কন্টাক্ট, এক হাতল (অবস্থান 0-তে দুটিই খোলা)
    _no(s, SX, LY, CW)
    _no(s, SX, MY, CW)
    kx = SX + 46
    s.path(f"M {kx} {no_tip(SX, LY, kx):.0f} L {kx} {LY - 70}", GREY, 2.2,
           dash="6 4")
    s.path(f"M {kx} {no_tip(SX, MY, kx):.0f} L {kx} {LY + 26}", GREY, 2.2,
           dash="6 4")
    s.circle(kx, LY - 84, 13, "#FFFFFF", GREY, 2.4)
    s.text(kx, LY - 112, "S1  MAN–0–AUTO", T_SMALL, NAVY, 700, "middle")
    s.text(SX + 92, LY + 36, "AUTO", T_TINY, STEEL, 700, "middle")
    s.text(SX + 92, MY + 36, "MAN", T_TINY, STEEL, 700, "middle")

    # AUTO শাখা — দুই ফ্লোট সিরিজে
    s.path(f"M {SX + 92} {LY} L 600 {LY}", CW, SW)
    fs_contact(s, 600, LY, "NO", "FS-1", "রিজার্ভার")
    s.path(f"M 692 {LY} L 800 {LY}", CW, SW)
    fs_contact(s, 800, LY, "NC", "FS-2", "ছাদের ট্যাংক")
    s.path(f"M 892 {LY} L 1020 {LY}", CW, SW)
    node(s, X, LY, CW)
    coil13(s, 1020, LY)
    s.path(f"M 1136 {LY} L {RX} {LY} L {RX} {NY}", NEUT, SW)

    # MAN শাখা — অধ্যায় ৮-এর ল্যাচিং
    s.path(f"M {SX + 92} {MY} L 620 {MY}", CW, SW)
    _nc(s, 620, MY, CW)
    _pb(s, 666, MY, RED, "#F6C9C4", "STOP")
    s.path(f"M 712 {MY} L {AX} {MY}", CW, SW)
    _no(s, AX, MY, CW, w=BX - AX)
    _pb(s, (AX + BX) / 2, MY, GREEN, "#BFE3CE", "START",
        tip=no_tip(AX, MY, (AX + BX) / 2, BX - AX))
    s.path(f"M {AX} {MY} L {AX} {HB} L {AX + 20} {HB}", CW, SW)
    _no(s, AX + 20, HB, CW, w=80)
    s.path(f"M {AX + 100} {HB} L {BX} {HB} L {BX} {MY}", CW, SW)
    s.text((AX + BX) / 2, HB + 40, "KM1 13-14", T_SMALL, GREEN, 700,
           "middle")
    s.path(f"M {BX} {MY} L {X} {MY} L {X} {LY}", CW, SW)

    s.path(f"M 82 {NY} L {RX} {NY}", NEUT, SW)
    node(s, RX, NY, NEUT)
    y = note_strip(s, NY + 40, "AUTO-তে ফ্লোট চালায়, MAN-এ START-STOP; "
                               "F2 দুই মোডেই পাম্প থামায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_automan.svg")


# ── ১১. ডাবল কন্ডিশনের দুই ট্যাংক ───────────────────────────────────────
def d11_levels():
    """কোন সুইচ কোথায় বসে আর কোন কন্টাক্ট ব্যবহার হয়।"""
    s = SVG(1240, 700)
    s.title("ডাবল কন্ডিশনে দুই ট্যাংকের দুই ফ্লোট সুইচ", T_TITLE)

    # ছাদের ট্যাংক (ডানে, উপরে)
    s.rect(806, 108, 344, 150, "#FFFFFF", NAVY, 2.8, 5)
    water(s, 810, 190, 336, 64)
    s.text(978, 96, "ছাদের ট্যাংক", T_NAME, NAVY, 700, "middle")
    s.rect(867, 128, 22, 22, METAL, GREY, 2, 4)
    s.path("M 878 150 L 900 208", "#3B3B3B", 2.8)
    float_body(s, 916, 224, r=22)
    s.text(1132, 150, "FS-2 · COM–NC", T_BODY, GREEN, 700, "end")
    s.path("M 806 262 L 1150 262", METAL, 5.0)          # ছাদ

    # রিজার্ভার (বাঁয়ে, নিচে)
    ground_hatch(s, 352, 40, 470)
    s.rect(96, 372, 320, 154, "#FFFFFF", NAVY, 2.8, 4)
    water(s, 100, 438, 312, 84)
    s.text(256, 556, "আন্ডারগ্রাউন্ড রিজার্ভার", T_NAME, NAVY, 700, "middle")
    s.rect(157, 390, 22, 22, METAL, GREY, 2, 4)
    s.path("M 168 412 L 190 458", "#3B3B3B", 2.8)
    float_body(s, 206, 472, r=22)
    s.text(96, 604, "FS-1 · COM–NO", T_BODY, STEEL, 700, "start")

    # পাম্প ও পাইপ
    blk(s, 590, 316, "পাম্প", 176, 60, "#FFFFFF", STEEL, T_NAME, STEEL, 3.0)
    s.path("M 416 428 L 470 428 L 470 316 L 502 316", WATER_E, 5.0)
    s.path("M 678 316 L 730 316 L 730 148 L 806 148", WATER_E, 5.0)

    # কন্ট্রোল সার্কিট — দুই সুইচ সিরিজে
    s.rect(430, 512, 620, 108, LIGHT, STEEL, 2.2, 10)
    s.text(740, 500, "কন্ট্রোল সার্কিট", T_BODY, STEEL, 700, "middle")
    bx = 470
    s.text(bx - 12, 592, "L", T_BODY, LIVE, 700, "end")
    s.path(f"M {bx} 585 L {bx + 56} 585", LIVE, 3.0)
    for i, nm in enumerate(("FS-1", "FS-2")):
        x = bx + 56 + i * 168
        node(s, x, 585, LIVE)
        s.path(f"M {x} 585 L {x + 62} 561", LIVE, 3.0)
        node(s, x + 78, 585, LIVE)
        s.text(x + 39, 540, nm, T_TINY, NAVY, 700, "middle")
        s.path(f"M {x + 78} 585 L {x + 168} 585", LIVE, 3.0)
    s.rect(870, 561, 96, 48, "#FFFFFF", NAVY, 2.6, 8)
    s.text(918, 593, "KM1", T_BODY, NAVY, 700, "middle")
    s.path("M 966 585 L 1020 585", NEUT, 3.0)
    s.text(1032, 592, "N", T_BODY, NEUT, 700, "start")

    y = note_strip(s, 640, "রিজার্ভারে পানি আছে এবং ছাদের ট্যাংক ভরেনি, "
                           "তখনই পাম্প চলে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_levels.svg")


# ── ১২. বাস্তবে বসানো বোর্ড ─────────────────────────────────────────────
def d12_panel():
    return photo_callouts(
        "d12_panel", "বোর্ডে বসানো লেভেল কন্ট্রোলার", "ph_panel.jpg",
        left=[("MCB", 0.21, 0.44), ("ইন্ডিকেটর", 0.27, 0.90)],
        right=[("লেভেল কন্ট্রোলার", 0.63, 0.16),
               ("AUTO / MANUAL", 0.71, 0.42),
               ("কন্ট্রোল তার", 0.62, 0.80)],
        note="ম্যানুয়াল মোডে ফ্লোট নষ্ট হলেও পাম্প চালানো যায়",
        iw=760)


ALL = [d01_system, d02_parts, d03_inside, d04_states, d05_action, d06_test,
       d07_direct, d08_contactor, d09_single, d10_double, d11_levels,
       d12_panel, d13_automan]


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
