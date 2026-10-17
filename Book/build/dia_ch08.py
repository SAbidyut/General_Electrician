# -*- coding: utf-8 -*-
"""অধ্যায় ৮ — ম্যাগনেটিক কন্টাক্টর : ডায়াগ্রাম।

এই অধ্যায়ের কোনো সার্কিট ইনস্টিটিউটের ডেকে নেই — কন্টাক্টর, সিলেক্টর
সুইচ আর পুশ বাটনের ছবি বা সার্কিট দুটো পিপিটির একটিতেও নেই।  তাই
সব সার্কিট এখানে নতুন আঁকা, আর আলোকচিত্র উইকিমিডিয়া কমন্স থেকে
(`assets_ch08.py`)।

**টপোলজি যাচাই — অধ্যায় ৬-এর শিক্ষা এই অধ্যায়ে দ্বিগুণ খাটে।**
ল্যাচিং সার্কিটের হোল্ডিং কন্টাক্ট START বোতামের **সমান্তরালে**
বসে, সিরিজে নয় — আর দুটোর পার্থক্য আঁকায় মাত্র একটা তারের।  তাই
d12 ও d13-এ হোল্ডিং কন্টাক্টের শাখাটি START-এর দুই প্রান্তের ঠিক
দুটি নোড থেকেই নামে, অন্য কোথাও থেকে নয়; নোড দুটি আলাদা করে আঁকা
(`node()`) যাতে চোখেই ধরা পড়ে।  d13-এর তিন অবস্থায় লাল রঙে যে পথটি
দেখানো হয়েছে, সেটিও একই জ্যামিতি থেকে আঁকা — অর্থাৎ ছবি আর কথা
আলাদা হয়ে যেতে পারে না।

**d03-এর স্প্যানিশ লেবেল** — মূল ছবিটির (CC0) গায়ে যন্ত্রাংশের নাম
স্প্যানিশে ছাপা।  লেবেলগুলো বাংলা পটি দিয়ে ঢেকে দেওয়া হয়েছে;
পটির মাপ স্প্যানিশ লেখার বাক্সের চেয়ে ছোট হতে পারে না — `_cover()`
সেটাই নিশ্চিত করে।

**কালপুরুষের সীমা** — `÷` লিখলে `+` আঁকে, `Ω` ও `°` নেই।  তাই ছবির
লেবেলে ভগ্নাংশ `/` দিয়ে, রোধের একক লেখা হয়নি।  বাংলা `৪` ল্যাটিন
`8`-এর মতো দেখায়, তাই টার্মিনাল-নম্বর, রেটিং ও মডেল নম্বর সর্বত্র
ল্যাটিন অঙ্কে — ওগুলোতে অঙ্কটাই জিনিসটার পরিচয়।

লেবেলের নিয়ম (অধ্যায় ১৫ থেকে কড়া):  প্যানেলের শিরোনাম বিশেষ্য,
যন্ত্রাংশের লেবেল এক-দুই শব্দ, নিচে এক লাইনের একটি নোট-পটি।
পরামর্শ ও সতর্কবাণী সবই বইয়ের লেখায় — ছবিতে নয়।
"""
import os

from svgkit import (SVG, NAVY, STEEL, LIGHT, RED, REDBG, GREEN, GREENBG,
                    AMBER, AMBERBG, GREY, LINE, INK, wrap, tw)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "ch08")
IMG = os.path.join(HERE, "assets", "ch08")

T_TITLE = 34
T_NODE = 28
T_NAME = 24.5
T_BODY = 21.5
T_SMALL = 20
T_CALL = 24
T_TINY = 18.5

SYM = "#12324D"
SW = 3.4
LIVE = "#D42A1F"          # লাইভ / সক্রিয় পথ
NEUT = "#1F2933"          # নিউট্রাল
DEAD = "#9AA6B2"          # বিদ্যুৎহীন পথ
COILC = "#C8892A"         # কয়েলের তামা
IRON = "#7C8894"          # কোরের ইস্পাত
IRON_D = "#5B6672"
PLATE = "#F4F7FA"
BOXG = "#E7ECF1"
SILVER = "#B9C2CB"
CU = "#B5762F"
FLUX = "#2E7DBE"          # চৌম্বক ফ্লাক্স


# ── ভাগাভাগি করা সহায়ক ─────────────────────────────────────────────────
def panel(s, x, y, w, h, title, col=STEEL, fill="#FCFDFE"):
    """প্যানেলের শিরোনাম — কেবল নাম, কোনো মন্তব্য নয়।"""
    s.rect(x, y, w, h, fill, LINE, 1.8, 13)
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


def node(s, x, y, col=SYM, r=6.5):
    s.circle(x, y, r, col)


def blk(s, cx, cy, text, w=None, h=64, fill="#FFFFFF", stroke=STEEL,
        size=T_BODY, tcol=NAVY, sw=2.6, rx=10):
    w = w or tw(text, size, 700) + 46
    x, y = cx - w / 2, cy - h / 2
    s.rect(x, y, w, h, fill, stroke, sw, rx)
    s.text(cx, cy + size * 0.34, text, size, tcol, 700, "middle")
    return x, y, w, h


def chip(s, cx, cy, text, fill=LIGHT, stroke=STEEL, tcol=NAVY,
         size=T_SMALL, pad=30):
    w = tw(text, size, 700) + pad
    s.rect(cx - w / 2, cy - 19, w, 38, fill, stroke, 2, 19)
    s.text(cx, cy + size * 0.34, text, size, tcol, 700, "middle")
    return w


def callout(s, x, y, text, tx, ty, anchor="end", size=T_CALL, col=NAVY,
            lead=STEEL):
    """লেবেল ও লিডার — লেখার যে পাশে লক্ষ্য, সেই কিনারা থেকেই বেরোয়।"""
    s.text(x, y + size * 0.32, text, size, col, 700, anchor)
    w = tw(text, size, 700)
    x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
    x1 = x0 + w
    start = x1 + 10 if tx > x1 else x0 - 10
    # লিডার থামে বৃত্তের কিনারায়, আর ডগার চিহ্নটি ফাঁপা বৃত্ত — ভরাট
    # বিন্দু দিলে যে জিনিসটি দেখানো হচ্ছে সেটিই ঢাকা পড়ে যায়।  ১১
    # অধ্যায়ের ডায়ালের চিহ্নগুলো ছাপা অক্ষরের চেয়ে ছোট, ওখানে ভরাট
    # বিন্দু পাঁচটি চিহ্নের একটিও দেখতে দিত না।
    R = 6.0
    d = ((tx - start) ** 2 + (ty - y) ** 2) ** 0.5 or 1.0
    ex, ey = tx - (tx - start) / d * R, ty - (ty - y) / d * R
    s.path(f"M {start} {y} L {ex} {ey}", lead, 2.2)
    s.circle(tx, ty, R, "none", lead, 2.2)


def spring(s, x, y0, y1, w=22, turns=5, col=IRON_D, sw=2.8):
    """রিটার্ন স্প্রিং — জিগজ্যাগ।"""
    step = (y1 - y0) / (turns * 2)
    d = f"M {x} {y0}"
    for i in range(turns * 2):
        d += f" L {x + (w / 2 if i % 2 == 0 else -w / 2):.1f} {y0 + step * (i + 0.5):.1f}"
    d += f" L {x} {y1}"
    s.path(d, col, sw)


def coil_sym(s, x, y, w, h, tag=None, live=False):
    """সার্কিট ডায়াগ্রামের কয়েল — IEC-র খালি আয়তক্ষেত্র।  প্রস্থচ্ছেদের
    `coil_block()` থেকে আলাদা, আর সেটাই নিয়ম:  ছবি বাস্তব হলে পাক
    আঁকা হয়, প্রতীক হলে কেবল বাক্স।"""
    s.rect(x, y, w, h, "#FFFFFF", SYM, 3.2, 5)
    if tag:
        s.text(x + w / 2, y + h / 2 + T_BODY * 0.34, tag, T_BODY, NAVY,
               700, "middle")


def coil_block(s, x, y, w, h, turns=6):
    """কয়েলের প্রস্থচ্ছেদ — ভেতরে পাক-রেখা।"""
    s.rect(x, y, w, h, "#F7E9CF", COILC, 2.4, 5)
    for i in range(turns):
        yy = y + h * (i + 0.5) / turns
        s.line(x + 4, yy, x + w - 4, yy, COILC, 1.9)


def photo_callouts(fname, title, img, left, right, note,
                   iw=430, top=104, gap=36, size=T_CALL, w=1240, pad=26):
    """একটি আলোকচিত্র মাঝখানে, দুই পাশে লেবেল ও লিডার।

    অধ্যায় ১৯-এ শেখা তিনটি ফাঁদ এখানেই বাঁধা:  (ক) ছবিটা আগে আঁকো,
    লিডার পরে;  (খ) লিডারের ডগা ছাপা লেখার পাশে রাখো, উপরে নয়;
    (গ) প্রতিটি লেবেল তার নিজের লক্ষ্যের সমান উচ্চতায় বসে।
    """
    from PIL import Image as _Im
    with _Im.open(f"{IMG}/{img}") as im:
        pw, ph = im.size
    ih = round(iw * ph / pw)
    ix = (w - iw) / 2
    s = SVG(w, top + ih + 130)
    s.title(title, T_TITLE)
    s.image(ix, top, iw, ih, f"{IMG}/{img}", 8)

    def place(items, side):
        if not items:
            return
        minsep = size * 2.0
        ys = [top + fy * ih for (_t, _fx, fy) in items]
        for i in range(1, len(ys)):
            ys[i] = max(ys[i], ys[i - 1] + minsep)
        over = ys[-1] - (top + ih + 6)
        if over > 0:
            ys = [y - over for y in ys]
        under = (top + 10) - ys[0]
        if under > 0:
            ys = [y + under for y in ys]
        for (t, fx, fy), y in zip(items, ys):
            tx, ty = ix + fx * iw, top + fy * ih
            lx = ix - gap if side == "L" else ix + iw + gap
            callout(s, lx, y, t, tx, ty, "end" if side == "L" else "start", size)

    place(left, "L")
    place(right, "R")
    y = note_strip(s, top + ih + pad, note)
    s.fit(y, 24)
    return s.save(f"{OUT}/{fname}.svg")


# ── ১. কেন কন্টাক্টর — দুই সার্কিটের ভাগাভাগি ────────────────────────────
def d01_idea():
    """চাবিকাঠি ছবি:  ছোট কারেন্টের কন্ট্রোল সার্কিট বড় কারেন্টের
    পাওয়ার সার্কিটকে চালায়।  কয়েল আর মেইন কন্টাক্টের মাঝে কোনো তার
    নেই, যোগটা চুম্বকের — কিন্তু কন্ট্রোল সাপ্লাই সাধারণত একই
    সরবরাহের একটি ফেজ থেকে নেওয়া, তাই "দুটি সার্কিট বৈদ্যুতিকভাবে
    আলাদা" বলা যায় না (কন্ট্রোল ট্রান্সফরমার থাকলে তবেই আলাদা)।

    মোটরে তিন ফেজ তিনটি আলাদা তারে ঢোকে;  আগের সংস্করণে তিনটি একটি
    আড়াআড়ি রেখায় জোড়া ছিল, যার মানে ফেজে-ফেজে শর্ট সার্কিট।"""
    s = SVG(1240, 700)
    s.title("কয়েল কন্ট্রোল সার্কিটে, মেইন কন্টাক্ট পাওয়ার সার্কিটে", T_TITLE)
    ar = s.arrow_defs(STEEL, "ar", 15)

    # ── বাঁ পাশ:  কন্ট্রোল সার্কিট ──────────────────────────────────
    panel(s, 46, 92, 520, 396, "কন্ট্রোল সার্কিট", STEEL, "#F7FAFD")
    CLY, CNY = 226, 400
    s.text(96, CLY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(96, CNY + 9, "N", T_NODE, NEUT, 700, "end")
    s.path(f"M 104 {CLY} L 210 {CLY}", LIVE, 2.4)
    # সুইচ বা বোতাম
    node(s, 210, CLY, LIVE)
    s.path(f"M 210 {CLY} L 286 {CLY - 38}", LIVE, 2.4)
    node(s, 300, CLY, LIVE)
    s.text(255, CLY - 56, "সুইচ", T_BODY, NAVY, 700, "middle")
    s.path(f"M 300 {CLY} L 396 {CLY}", LIVE, 2.4)
    # কয়েল
    coil_sym(s, 396, CLY - 42, 104, 84)
    s.text(448, CLY - 58, "কয়েল", T_BODY, NAVY, 700, "middle")
    s.text(382, CLY - 52, "A1", T_SMALL, NAVY, 700, "end")
    s.text(514, CLY - 52, "A2", T_SMALL, NAVY, 700, "start")
    s.path(f"M 500 {CLY} L 524 {CLY} L 524 {CNY}", NEUT, 2.4)
    s.path(f"M 104 {CNY} L 524 {CNY}", NEUT, 2.4)
    node(s, 524, CNY, NEUT)
    chip(s, 306, 452, "সরু তার · কম কারেন্ট", AMBERBG, AMBER, AMBER, T_SMALL)

    # ── ডান পাশ:  পাওয়ার সার্কিট ────────────────────────────────────
    panel(s, 674, 92, 520, 396, "পাওয়ার সার্কিট", NAVY, "#FBF8F4")
    for xx, nm in ((762, "L1"), (852, "L2"), (942, "L3")):
        s.text(xx, 156, nm, T_BODY, LIVE, 700, "middle")
        s.path(f"M {xx} 168 L {xx} 214", LIVE, 4.2)
        # মেইন কন্টাক্ট — খোলা
        node(s, xx, 214, LIVE)
        s.path(f"M {xx} 214 L {xx + 32} 270", LIVE, 4.2)
        node(s, xx, 280, LIVE)
        s.path(f"M {xx} 280 L {xx} 322", LIVE, 4.2)
    s.text(1004, 250, "মেইন", T_BODY, NAVY, 700, "start")
    s.text(1004, 280, "কন্টাক্ট", T_BODY, NAVY, 700, "start")
    # মোটর
    # তিন ফেজ তিনটি আলাদা তারে মোটরের বৃত্তে — কোথাও একসঙ্গে জোড়া নয়
    s.path("M 762 322 L 826 354", LIVE, 4.2)
    s.path("M 852 322 L 852 344", LIVE, 4.2)
    s.path("M 942 322 L 878 354", LIVE, 4.2)
    s.circle(852, 380, 36, "#FFFFFF", SYM, 3.4)
    s.text(852, 392, "M", T_NODE, SYM, 700, "middle")
    s.text(904, 388, "মোটর", T_BODY, NAVY, 700, "start")
    chip(s, 934, 452, "মোটা তার · বড় কারেন্ট", REDBG, RED, RED, T_SMALL)

    # ── মাঝের যোগ:  চুম্বক ──────────────────────────────────────────
    s.path("M 500 226 L 640 226 L 640 268 L 744 268", FLUX, 3.2, dash="10 7",
           marker=ar)
    s.text(620, 196, "ম্যাগনেটিক টান", T_BODY, FLUX, 700, "middle")

    y = note_strip(s, 516, "কয়েলের ছোট কারেন্ট চুম্বক বানায়, চুম্বক "
                           "মেইন কন্টাক্ট টেনে বন্ধ করে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d01_idea.svg")


# ── ২. বাইরের চেহারা ও টার্মিনাল ───────────────────────────────────────
def d02_outside():
    return photo_callouts(
        "d02_outside", "কন্টাক্টরের টার্মিনাল ও ছাপা নম্বর",
        "ph_contactor.jpg",
        # ভগ্নাংশ ছবির উপর মেপে বসানো — প্রতিটি ডগা তার নিজের
        # ছিদ্র বা ছাপা লেখার উপরে, আর তালিকা fy-র ক্রমে সাজানো
        left=[("ইনপুট 1/L1 3/L2 5/L3", 0.285, 0.245),
              ("কয়েল A1 (উল্টো পাশে)", 0.10, 0.38),
              ("নেমপ্লেট", 0.335, 0.58),
              ("DIN রেল ক্লিপ", 0.30, 0.90)],
        right=[("অক্সিলিয়ারি 13", 0.43, 0.115),
               ("অক্সিলিয়ারি 14", 0.80, 0.295),
               ("আউটপুট 2/T1 4/T2 6/T3", 0.665, 0.465),
               ("কয়েল A2", 0.88, 0.61)],
        note="বিজোড় নম্বর ইনপুট, জোড় নম্বর আউটপুট; সব কন্টাক্টরে একই নিয়ম",
        iw=500)


# ── ৩. খুলে ফেলা কন্টাক্টর ─────────────────────────────────────────────
# মূল ছবির (CC0) গায়ে যন্ত্রাংশের নাম স্প্যানিশে ছাপা।  আগে সেই লেখার
# উপরে সাদা পটি বসানো হতো, কিন্তু পটিগুলো স্প্যানিশ বাক্সের মাপে বাঁধা
# ছিল বলে দু-লাইনের লেবেলের জায়গায় বিশাল হয়ে যন্ত্রাংশের গায়ে উঠে
# যেত।  এখন স্প্যানিশ লেখাটাই ছবি থেকে মুছে ফেলা হয় (`_clean_photo()` —
# আশপাশের পটভূমির রং থেকে চার কোণে নমুনা নিয়ে দ্বি-রৈখিক মিশ্রণ, সামান্য
# দানা ও নরম কিনারা), আর বাংলা নাম বসে লেখার মাপের ছোট পটিতে, সঙ্গে
# যন্ত্রাংশ পর্যন্ত একটি সরু লিডার।  ফলে কোনো পটি আর কোনো যন্ত্রাংশ
# ঢাকে না, আর কোন নামটি কার — সেটাও আন্দাজ করতে হয় না।
#
# প্রতিটি সারি:  (স্প্যানিশ লেখার বাক্স, বাংলা নাম, পটির কেন্দ্র,
# লিডারের ডগা) — চারটিই ছবির ভগ্নাংশে মাপা।
_ES = [
    ((0.000, 0.028, 0.310, 0.178), "অক্সিলিয়ারি ব্লকের খোল",
     (0.152, 0.082), (0.165, 0.420)),
    ((0.386, 0.028, 0.484, 0.112), "স্থির কোর",
     (0.437, 0.068), (0.440, 0.180)),
    ((0.586, 0.028, 0.694, 0.112), "কয়েল",
     (0.645, 0.068), (0.633, 0.255)),
    ((0.841, 0.028, 0.969, 0.112), "মূল খোল",
     (0.902, 0.068), (0.890, 0.190)),
    ((0.204, 0.438, 0.346, 0.572), "কন্টাক্ট ব্রিজ",
     (0.288, 0.508), (0.221, 0.421)),
    ((0.034, 0.623, 0.182, 0.752), "অক্সিলিয়ারি কন্টাক্ট",
     (0.118, 0.694), (0.128, 0.568)),
    ((0.419, 0.511, 0.564, 0.645), "রিটার্ন স্প্রিং",
     (0.478, 0.578), (0.588, 0.600)),
    ((0.324, 0.798, 0.436, 0.882), "টার্মিনাল স্ক্রু",
     (0.380, 0.846), (0.392, 0.768)),
    ((0.558, 0.798, 0.796, 0.927), "মুভিং আর্মেচার",
     (0.678, 0.862), (0.669, 0.684)),
    ((0.814, 0.798, 0.976, 0.927), "মেইন কন্টাক্ট",
     (0.902, 0.862), (0.895, 0.692)),
]


def _clean_photo(src, dst):
    """স্প্যানিশ লেবেলগুলো ছবি থেকে মুছে দেয় (একবারই, তারপর ক্যাশ)।

    পটভূমিতে মৃদু গ্রেডিয়েন্ট আছে, তাই সমতল রং বসালে তালি বোঝা যায়।
    প্রতিটি বাক্সের চার কোণের বাইরে থেকে নমুনা নিয়ে (উজ্জ্বলতম ৫৫%
    পিক্সেল — তাতে কালো লেখা বা যন্ত্রাংশ নমুনায় ঢোকে না) দ্বি-রৈখিক
    মিশ্রণে তালিটা বোনা হয়, ছবির দানার সমান সামান্য নয়েজ মেশানো হয়,
    আর কিনারা ঝাপসা মুখোশ দিয়ে মেলানো হয়।"""
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    import random
    from PIL import Image as _Im, ImageDraw as _Dr, ImageFilter as _Fl

    def bg_at(im, cx, cy, r=18):
        W, H = im.size
        box = (max(0, cx - r), max(0, cy - r),
               min(W, cx + r), min(H, cy + r))
        px = list(im.crop(box).getdata())
        px.sort(key=lambda q: -(q[0] + q[1] + q[2]))
        keep = px[: max(1, len(px) * 55 // 100)]
        n = len(keep)
        return tuple(sum(q[k] for q in keep) / n for k in range(3))

    im = _Im.open(src).convert("RGB")
    W, H = im.size
    rnd = random.Random(7)
    for (a, b, c, d), _n, _cc, _tt in _ES:
        m, off = 6, 14
        x0, y0 = max(0, int(a * W) - m), max(0, int(b * H) - m)
        x1, y1 = min(W, int(c * W) + m), min(H, int(d * H) + m)
        w, h = x1 - x0, y1 - y0
        c00 = bg_at(im, x0 - off, y0 - off)
        c10 = bg_at(im, x1 + off, y0 - off)
        c01 = bg_at(im, x0 - off, y1 + off)
        c11 = bg_at(im, x1 + off, y1 + off)
        patch = _Im.new("RGB", (w, h))
        put = patch.load()
        for j in range(h):
            v = j / max(1, h - 1)
            for i in range(w):
                u = i / max(1, w - 1)
                col = []
                for k in range(3):
                    top = c00[k] * (1 - u) + c10[k] * u
                    bot = c01[k] * (1 - u) + c11[k] * u
                    col.append(int(max(0, min(255, top * (1 - v) + bot * v
                                              + rnd.gauss(0, 2.1)))))
                put[i, j] = tuple(col)
        mask = _Im.new("L", (w, h), 0)
        _Dr.Draw(mask).rectangle([4, 4, w - 5, h - 5], fill=255)
        im.paste(patch, (x0, y0), mask.filter(_Fl.GaussianBlur(3.5)))
    im.save(dst, quality=94)
    return dst


def _tag(s, cx, cy, text, tx, ty, size=T_NAME):
    """ছবির উপরে নামের পটি + যন্ত্রাংশ পর্যন্ত লিডার।

    লিডারটি পটির কেন্দ্র থেকে লক্ষ্যের দিকে যে কিনারা, সেখান থেকেই
    বেরোয় — তাই লেখার উপর দিয়ে যায় না।  ছবির গায়ে সরু রেখা হারিয়ে
    যায় বলে নিচে সাদা ছায়া।"""
    w = tw(text, size, 700) + 34
    h = size * 1.78
    x, y = cx - w / 2, cy - h / 2
    dx, dy = tx - cx, ty - cy
    if dx or dy:
        sx = (w / 2) / abs(dx) if dx else 1e9
        sy = (h / 2) / abs(dy) if dy else 1e9
        t = min(sx, sy)
        ex, ey = cx + dx * t, cy + dy * t
        gap = 7 / max(1.0, (dx * dx + dy * dy) ** 0.5)
        ex, ey = ex + dx * gap, ey + dy * gap
        s.path(f"M {ex:.1f} {ey:.1f} L {tx:.1f} {ty:.1f}", "#FFFFFF", 5.2,
               opacity=0.85)
        s.path(f"M {ex:.1f} {ey:.1f} L {tx:.1f} {ty:.1f}", STEEL, 2.2)
        s.circle(tx, ty, 6.5, "#FFFFFF", STEEL, 2.2)
        s.circle(tx, ty, 2.6, NAVY)
    s.rect(x, y, w, h, "#FFFFFF", STEEL, 2, 10)
    s.text(cx, cy + size * 0.34, text, size, NAVY, 700, "middle")
    return x, y, w, h


def d03_exploded():
    """খুলে ফেলা কন্টাক্টর — স্প্যানিশ লেখা মুছে বাংলা নামের পটি।"""
    from PIL import Image as _Im
    photo = _clean_photo(f"{IMG}/ph_exploded.jpg",
                         f"{IMG}/ph_exploded_clean.jpg")
    with _Im.open(photo) as im:
        pw, ph = im.size
    iw = 1152
    ih = round(iw * ph / pw)
    ix, iy = (1240 - iw) / 2, 96
    s = SVG(1240, iy + ih + 120)
    s.title("খুলে ফেলা কন্টাক্টরের অংশ", T_TITLE)
    s.image(ix, iy, iw, ih, photo, 8)

    for _box, name, (fx, fy), (tx, ty) in _ES:
        _tag(s, ix + fx * iw, iy + fy * ih, name,
             ix + tx * iw, iy + ty * ih)

    y = note_strip(s, iy + ih + 26,
                   "কয়েল, স্থির কোর ও মুভিং আর্মেচার মিলে কন্টাক্টরের "
                   "ইলেকট্রোম্যাগনেট")
    s.fit(y, 24)
    return s.save(f"{OUT}/d03_exploded.svg")


# ── ৪. ভেতরের প্রস্থচ্ছেদ ──────────────────────────────────────────────
# একটিমাত্র পোলের প্রস্থচ্ছেদ আঁকা হয়েছে, তিনটির নয় — তিনটি আঁকলে
# স্থির কন্টাক্টের লিড, পুশ রড আর ক্যারিয়ার একে অন্যের উপর পড়ে যায়,
# আর ছবিটা পড়াই যায় না।  তিন পোলের কথাটা লেখায় ও d06-এর প্রতীকে।
#
# জ্যামিতির শর্ত:  gap = 0 মানে কন্টাক্টর টানা — তখন আর্মেচারের পা
# ঠিক কোরের গায়ে লাগে আর ব্রিজের রুপোর টিপ ঠিক স্থির কন্টাক্টের
# টিপে বসে।  gap বাড়লে গোটা চলমান অংশটাই একসঙ্গে উপরে ওঠে, অর্থাৎ
# দুটোই একসঙ্গে খোলে — বাস্তবে যা ঘটে।
def _magnet(s, cx, oy, gap, live=False):
    """এক পোলের প্রস্থচ্ছেদ।  ফেরত দেয় মাপ, যাতে লেবেল বসানো যায়।"""
    FY = oy + 120                      # স্থির কন্টাক্টের সারি
    KTOP = oy + 330                    # স্থির কোরের মাথা (কখনো নড়ে না)
    BY = FY - 36 - gap                 # মুভিং ব্রিজ
    AY = KTOP - 74 - gap               # আর্মেচারের মাথা
    CP = AY - 18                       # ক্যারিয়ার প্লেট

    # খোল
    s.rect(cx - 212, oy, 424, 424, "#FBFCFD", "#9AA6B2", 2.6, 12)

    # স্থির কন্টাক্ট দুটি — L আকৃতি, টিপ ভেতরে, লিড বাইরে ও উপরে
    for sx, tn in ((-1, "1/L1"), (1, "2/T1")):
        x = cx + sx * 70
        s.rect(x - 26, FY, 52, 20, CU, "#7A4E1E", 2.2, 3)
        # ভেতরের টিপ (উপরমুখী)
        s.rect(x - 18, FY - 10, 36, 10, SILVER, "#8E99A4", 1.8, 2)
        # বাইরের বাহু ও উপরের লিড
        s.rect(min(x, cx + sx * 124), FY + 6, abs(sx * 54), 14, CU,
               "#7A4E1E", 2.2, 3)
        s.path(f"M {cx + sx * 124} {FY + 6} L {cx + sx * 124} {oy + 20}", CU, 8)
        s.text(cx + sx * 124, oy - 8, tn, T_SMALL, NAVY, 700, "middle")

    # মুভিং কন্টাক্ট ব্রিজ — টিপ নিচের দিকে
    s.rect(cx - 100, BY, 200, 16, CU, "#7A4E1E", 2.2, 3)
    for sx in (-1, 1):
        s.rect(cx + sx * 70 - 18, BY + 16, 36, 10, SILVER, "#8E99A4", 1.8, 2)

    # পুশ রড — দুই স্থির কন্টাক্টের ফাঁক দিয়েই নামে
    s.rect(cx - 14, BY + 16, 28, CP - BY - 16, "#E3E9EF", "#9AA6B2", 2.2, 4)

    # ক্যারিয়ার প্লেট ও আর্মেচার
    s.rect(cx - 140, CP, 280, 18, "#E3E9EF", "#9AA6B2", 2.2, 5)
    s.rect(cx - 100, AY, 200, 30, IRON, IRON_D, 2.4, 3)
    for lx in (cx - 100, cx - 15, cx + 70):
        s.rect(lx, AY + 30, 30, 44, IRON, IRON_D, 2.4, 2)

    # স্থির কোর — E, পা উপরে
    for lx in (cx - 100, cx - 15, cx + 70):
        s.rect(lx, KTOP, 30, 48, IRON, IRON_D, 2.4, 2)
    s.rect(cx - 100, KTOP + 48, 200, 30, IRON, IRON_D, 2.4, 3)

    # কয়েল — মাঝের পায়ের দুই পাশে
    coil_block(s, cx - 66, KTOP + 2, 46, 44, 4)
    coil_block(s, cx + 20, KTOP + 2, 46, 44, 4)
    ccol = LIVE if live else COILC
    s.path(f"M {cx - 66} {KTOP + 24} L {cx - 176} {KTOP + 24}", ccol, 3.2)
    s.path(f"M {cx + 66} {KTOP + 24} L {cx + 176} {KTOP + 24}", ccol, 3.2)
    s.text(cx - 182, KTOP + 31, "A1", T_SMALL, NAVY, 700, "end")
    s.text(cx + 182, KTOP + 31, "A2", T_SMALL, NAVY, 700, "start")

    # রিটার্ন স্প্রিং — ক্যারিয়ার প্লেট আর কোরের বেসের মাঝে
    for sx in (-1, 1):
        spring(s, cx + sx * 118, CP + 18, KTOP + 48, 22, 5)

    return dict(FY=FY, BY=BY, CP=CP, AY=AY, KTOP=KTOP, cx=cx, oy=oy)


def d04_inside():
    """বড় প্রস্থচ্ছেদ, পুরো লেবেলসহ — কয়েল বিদ্যুৎহীন অবস্থায়।"""
    s = SVG(1240, 800)
    s.title("ম্যাগনেটিক কন্টাক্টরের ভেতরের গঠন (এক পোলের প্রস্থচ্ছেদ)",
            T_TITLE)

    g = _magnet(s, 620, 118, 40)
    cx = g["cx"]

    # লেবেলের উচ্চতা হাতে বসানো, আর ক্রমটা লক্ষ্যের উচ্চতার ক্রমেই —
    # নইলে লিডারগুলো একে অন্যকে কাঁচি করে কেটে যায়
    # পুশ রডের ডগা (cx, BY+16 … CP) বাঁ পাশের বাকি পাঁচটি লক্ষ্যের
    # চেয়ে ডানে, অথচ উচ্চতায় তাদের মাঝামাঝি — বাঁ কলামে রাখলে তার
    # লিডার স্থির কন্টাক্ট ও ক্যারিয়ার প্লেটের লিডারকে কাঁচি করে কাটে
    # (কোনো ক্রমেই এড়ানো যায় না)।  তাই ওটি ডান কলামে, আর দুই কলামই
    # লক্ষ্যের উচ্চতার ক্রমে সাজানো।
    for y, t, tx, ty in ((176, "কন্টাক্ট ব্রিজ", cx - 100, g["BY"] + 8),
                         (252, "রুপার টিপ", cx - 70, g["BY"] + 21),
                         (328, "স্থির কন্টাক্ট", cx - 88, g["FY"] + 10),
                         (404, "ক্যারিয়ার প্লেট", cx - 140, g["CP"] + 9),
                         # ৪৯৬-ই থাকুক:  এর উপরে উঠলে লিডারটি কয়েলের
                         # A1 লেখাটির উপর দিয়ে চলে যায়
                         (496, "স্থির কোর", cx - 100, g["KTOP"] + 60)):
        callout(s, 372, y, t, tx, ty, "end")

    for y, t, tx, ty in ((176, "টার্মিনাল লিড", cx + 124, g["oy"] + 44),
                         (234, "খোল", cx + 212, g["oy"] + 96),
                         (292, "পুশ রড", cx + 14, g["CP"] - 46),
                         (350, "মুভিং আর্মেচার", cx + 100, g["AY"] + 16),
                         (408, "রিটার্ন স্প্রিং", cx + 118, g["CP"] + 52),
                         (466, "এয়ার গ্যাপ", cx + 85, g["AY"] + 96),
                         (524, "কয়েল", cx + 66, g["KTOP"] + 24)):
        callout(s, 872, y, t, tx, ty, "start")

    # এয়ার গ্যাপের চিহ্ন — আর্মেচারের পা আর কোরের মাথার মাঝের ফাঁক
    for sx in (-1, 1):
        s.path(f"M {cx + sx * 85} {g['AY'] + 74} L {cx + sx * 85} {g['KTOP']}",
               RED, 3.0, dash="7 5")

    chip(s, 620, 590, "কয়েলে বিদ্যুৎ নেই: স্প্রিং সবকিছু উপরে ঠেলে "
                      "রেখেছে, কন্টাক্ট খোলা", REDBG, RED, RED, T_BODY, 44)

    y = note_strip(s, 644, "স্প্রিং উপরে ঠেলে, চুম্বক নিচে টানে; এতেই "
                           "কন্টাক্ট খোলে ও বন্ধ হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d04_inside.svg")


# ── ৫. কাজের নীতি — দুই অবস্থা ─────────────────────────────────────────
def d05_action():
    """কয়েল বন্ধ বনাম কয়েল চালু — পাশাপাশি, একই জ্যামিতি।"""
    s = SVG(1240, 840)
    s.title("কয়েলে বিদ্যুৎ দেওয়ার আগে ও পরে", T_TITLE)
    ar = s.arrow_defs(RED, "arr", 15)

    for px, ttl, gap, on in ((30, "কয়েল বিদ্যুৎহীন: কন্টাক্ট খোলা", 40, False),
                             (622, "কয়েল সক্রিয়: কন্টাক্ট বন্ধ", 0, True)):
        panel(s, px, 92, 588, 618, ttl, RED if not on else GREEN,
              "#FDFBFA" if not on else "#F8FCFA")
        g = _magnet(s, px + 294, 182, gap, on)
        chip(s, px + 294, 668,
             "A1-A2-তে 230 V আছে, আর্মেচার নিচে নেমেছে" if on else
             "A1-A2-তে ভোল্টেজ নেই, স্প্রিং উপরে ঠেলে রেখেছে",
             GREENBG if on else REDBG, GREEN if on else RED,
             GREEN if on else RED, T_BODY, 40)
        # টানের দিক — খোলের ভেতর ডান পাশের ফাঁকা করিডরে, যেটুকু
        # জায়গা আছে তাতে এক শব্দের বেশি ধরে না;  পুরো কথাটা চিপে
        ax = px + 294 + 172
        if on:
            s.path(f"M {ax} {g['AY'] - 70} L {ax} {g['AY'] - 6}", RED, 3.4,
                   marker=ar)
            s.text(ax, g["AY"] - 86, "টান", T_SMALL, RED, 700, "middle")
        else:
            s.path(f"M {ax} {g['KTOP'] - 6} L {ax} {g['KTOP'] - 70}", RED, 3.4,
                   marker=ar)
            s.text(ax, g["KTOP"] - 84, "ঠেলা", T_SMALL, RED, 700, "middle")

    y = note_strip(s, 738, "বিদ্যুৎ চলে গেলে কন্টাক্টর নিজে থেকেই "
                           "ছেড়ে দেয় এবং কন্টাক্ট খুলে যায়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d05_action.svg")


# ── ৬. প্রতীক ও টার্মিনাল-নম্বরের নিয়ম ─────────────────────────────────
def d06_symbols():
    s = SVG(1240, 800)
    s.title("কন্টাক্টরের প্রতীক ও টার্মিনাল নম্বর", T_TITLE)

    # ── উপরের সারি:  চারটি প্রতীক ─────────────────────────────────
    panel(s, 46, 92, 1148, 310, "সার্কিট ডায়াগ্রামে যেভাবে আঁকা হয়")

    def coil_sym(cx, cy):
        s.path(f"M {cx} {cy - 58} L {cx} {cy - 34}", SYM, 3)
        s.rect(cx - 38, cy - 34, 76, 68, "#FFFFFF", SYM, 3.2, 4)
        s.path(f"M {cx} {cy + 34} L {cx} {cy + 58}", SYM, 3)
        s.text(cx - 48, cy - 42, "A1", T_SMALL, NAVY, 700, "end")
        s.text(cx - 48, cy + 56, "A2", T_SMALL, NAVY, 700, "end")

    def no_sym(cx, cy, tn=("1", "2"), closed=False):
        s.path(f"M {cx} {cy - 58} L {cx} {cy - 30}", SYM, 3)
        node(s, cx, cy - 30)
        if closed:
            s.path(f"M {cx} {cy - 30} L {cx} {cy + 30}", SYM, 3.4)
        else:
            s.path(f"M {cx} {cy - 30} L {cx + 40} {cy + 24}", SYM, 3.4)
        node(s, cx, cy + 30)
        s.path(f"M {cx} {cy + 30} L {cx} {cy + 58}", SYM, 3)
        s.text(cx - 14, cy - 36, tn[0], T_SMALL, NAVY, 700, "end")
        s.text(cx - 14, cy + 44, tn[1], T_SMALL, NAVY, 700, "end")

    def nc_sym(cx, cy, tn=("21", "22")):
        s.path(f"M {cx} {cy - 58} L {cx} {cy - 30}", SYM, 3)
        node(s, cx, cy - 30)
        s.path(f"M {cx} {cy - 30} L {cx + 40} {cy + 24}", SYM, 3.4)
        s.path(f"M {cx + 40} {cy + 24} L {cx + 40} {cy - 14}", SYM, 3.4)
        node(s, cx, cy + 30)
        s.path(f"M {cx} {cy + 30} L {cx} {cy + 58}", SYM, 3)
        s.text(cx - 14, cy - 36, tn[0], T_SMALL, NAVY, 700, "end")
        s.text(cx - 14, cy + 44, tn[1], T_SMALL, NAVY, 700, "end")

    CY = 232
    coil_sym(186, CY)
    s.text(186, 372, "কয়েল", T_BODY, NAVY, 700, "middle")

    for i, cx in enumerate((400, 466, 532)):
        no_sym(cx, CY, (str(2 * i + 1), str(2 * i + 2)))
    # যান্ত্রিক যোগ — তিনটি কন্টাক্ট আর কয়েল একসঙ্গেই নড়ে
    s.path(f"M 186 {CY + 34} L 186 {CY + 76} L 532 {CY + 76}", SYM, 2.2,
           dash="7 5")
    for cx in (400, 466, 532):
        s.path(f"M {cx} {CY + 40} L {cx} {CY + 76}", SYM, 2.2, dash="7 5")
    s.text(466, 372, "তিনটি মেইন কন্টাক্ট (NO)", T_BODY, NAVY, 700, "middle")

    no_sym(790, CY, ("13", "14"))
    s.text(800, 372, "অক্সিলিয়ারি NO", T_BODY, NAVY, 700, "middle")

    nc_sym(1024, CY, ("21", "22"))
    s.text(1034, 372, "অক্সিলিয়ারি NC", T_BODY, NAVY, 700, "middle")

    # ── নিচের সারি:  নম্বরের নিয়ম ─────────────────────────────────
    panel(s, 46, 424, 1148, 250, "দুই অঙ্কের নম্বর যেভাবে পড়তে হয় "
                                 "(IEC 60947 সিরিজ)")
    s.text(310, 510, "13", 62, NAVY, 700, "middle")
    s.path("M 284 536 L 214 582", STEEL, 2.4)
    s.path("M 336 536 L 406 582", STEEL, 2.4)
    s.text(196, 616, "প্রথম অঙ্ক = ক্রম", T_BODY, NAVY, 700, "middle")
    s.text(196, 646, "কন্টাক্টটি কত নম্বর", T_SMALL, GREY, 400, "middle")
    s.text(424, 616, "দ্বিতীয় অঙ্ক = কাজ", T_BODY, NAVY, 700, "middle")
    s.text(424, 646, "খোলা না বন্ধ", T_SMALL, GREY, 400, "middle")

    for i, (pair, what, col, bg) in enumerate((
            ("1 – 2", "NC", RED, REDBG),
            ("3 – 4", "NO", GREEN, GREENBG),
            ("5 – 6", "বিশেষ NC", AMBER, AMBERBG),
            ("7 – 8", "বিশেষ NO", STEEL, LIGHT))):
        cx = 652 + i * 142
        s.rect(cx - 62, 476, 124, 58, bg, col, 2.2, 9)
        s.text(cx, 516, pair, T_NAME, col, 700, "middle")
        s.text(cx, 568, what, T_BODY, NAVY, 700, "middle")
    s.text(865, 630, "উদাহরণ:  21-22 মানে দ্বিতীয় কন্টাক্ট, আর সেটি NC",
           T_BODY, GREY, 400, "middle")

    y = note_strip(s, 700, "কয়েলের দুই প্রান্তের নাম সব সময় "
                           "A1 ও A2")
    s.fit(y, 24)
    return s.save(f"{OUT}/d06_symbols.svg")


# ── ৭. নেমপ্লেট পড়া ────────────────────────────────────────────────────
def d07_nameplate():
    """বাজারচলতি একটি মোটর-কন্টাক্টরের গায়ের লেখা, বাংলা ব্যাখ্যাসহ।
    সংখ্যাগুলো IEK KMИ-11810 আর CHiNT NXC-18-এর ডেটাশিট থেকে —
    দুটোতেই 18 A / 4-7.5-10 kW, অর্থাৎ এটি একটি বাস্তব ঘরানার প্লেট।"""
    s = SVG(1240, 700)
    s.title("কন্টাক্টরের নেমপ্লেটের অর্থ", T_TITLE)

    PX, PY, PW, PH = 118, 110, 470, 400
    s.rect(PX, PY, PW, PH, "#F2F4F6", "#8894A0", 3, 10)
    s.text(PX + 26, PY + 54, "NXC-18", 40, NAVY, 700, "start")
    s.text(PX + PW - 26, PY + 52, "CHiNT", T_NAME, STEEL, 700, "end")
    s.line(PX + 20, PY + 72, PX + PW - 20, PY + 72, "#AEB8C2", 2)

    rows = [("Ue", "690 V"), ("Ui", "690 V"), ("Uimp", "6 kV"),
            ("AC-1  Ie", "32 A"), ("AC-3  Ie", "18 A"),
            ("AC-3  380/400 V", "7.5 kW"), ("কয়েল", "230 V  50 Hz"),
            ("IEC 60947-4-1", "")]
    for i, (a, b) in enumerate(rows):
        yy = PY + 112 + i * 36
        s.text(PX + 26, yy, a, T_BODY, INK, 400, "start")
        s.text(PX + PW - 26, yy, b, T_BODY, INK, 700, "end")

    # ব্যাখ্যা — ডান পাশে
    notes = [
        ("Ue", "কাজের ভোল্টেজের সর্বোচ্চ সীমা", PY + 112, STEEL),
        ("Uimp", "ইম্পালস সহ্য করার ক্ষমতা", PY + 184, STEEL),
        ("AC-1", "রেজিস্টিভ লোডে চলবে 32 A পর্যন্ত", PY + 220, AMBER),
        ("AC-3", "মোটরে চলবে 18 A পর্যন্ত", PY + 256, RED),
        ("kW", "400 V-এ সর্বোচ্চ 7.5 kW মোটর", PY + 292, RED),
        ("কয়েল", "কন্ট্রোল সার্কিটের ভোল্টেজ", PY + 328, GREEN),
    ]
    for tag, txt, yy, col in notes:
        s.path(f"M {PX + PW + 12} {yy - 7} L {PX + PW + 58} {yy - 7}", col, 2.2)
        s.circle(PX + PW + 12, yy - 7, 5, col)
        s.text(PX + PW + 70, yy, txt, T_BODY, NAVY, 700, "start")

    chip(s, 620, 552, "একই কন্টাক্টরের রেটিং লোডের ধরন অনুযায়ী আলাদা",
         AMBERBG, AMBER, AMBER, T_BODY, 44)

    y = note_strip(s, 594, "মোটরের জন্য AC-3 ঘরের মান ধরতে হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d07_nameplate.svg")


# ── ৮. ইউটিলাইজেশন ক্যাটাগরি ───────────────────────────────────────────
def d08_categories():
    """একই কন্টাক্টরে তিন ক্যাটাগরির তিন রেটিং — Siemens 3RT2016-1AP01
    ডেটাশিট থেকে (AC-1 22 A, AC-3 9 A, AC-4 4.1 A @ 400 V)।"""
    s = SVG(1240, 640)
    s.title("লোডের ধরন অনুযায়ী একই কন্টাক্টরের রেটিং", T_TITLE)

    panel(s, 46, 92, 1148, 366, "3RT2016: 400 V-এ রেটিং")
    X0, BARW = 380, 700
    MAXA = 26.5
    bars = [("AC-1", "রেজিস্টিভ: হিটার, ফার্নেস", 22.0, GREEN, GREENBG),
            ("AC-3", "মোটর চালু ও বন্ধ", 9.0, AMBER, AMBERBG),
            ("AC-4", "ইঞ্চিং, প্লাগিং, ঘন ঘন উল্টানো", 4.1, RED, REDBG)]
    for i, (cat, what, amps, col, bg) in enumerate(bars):
        yy = 176 + i * 96
        s.text(X0 - 26, yy + 8, cat, T_NAME, col, 700, "end")
        s.text(X0 - 26, yy + 38, what, T_SMALL, GREY, 400, "end")
        w = BARW * amps / MAXA
        s.rect(X0, yy - 22, BARW, 46, "#F3F6F9", LINE, 1.6, 6)
        s.rect(X0, yy - 22, w, 46, bg, col, 2.6, 6)
        s.text(X0 + w + 16, yy + 9, f"{amps:g} A", T_NAME, col, 700, "start")

    s.text(620, 424, "কন্টাক্ট একই, শুধু লোডের ধরন আলাদা",
           T_BODY, GREY, 400, "middle")

    y = note_strip(s, 486, "মোটরের হিসাব সব সময় AC-3 ধরে; AC-1 দেখে "
                           "মোটর বাছলে কন্টাক্ট পুড়বে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d08_categories.svg")


# ── ৯. মডুলার কন্টাক্টর ────────────────────────────────────────────────
def d09_modular():
    return photo_callouts(
        "d09_modular", "মডুলার কন্টাক্টর (IEC 61095)",
        "ph_modular.jpg",
        # A1 ও A2-র স্ক্রু দুটি উপরে-নিচে মাঝবরাবর, টার্মিনাল 5-এ নয়;
        # IEC 61095 ছাপা আছে বাঁ পাশের রেটিং-ব্লকে, তাই লেবেলটিও বাঁয়ে
        left=[("ইনপুট 1 3 5 7", 0.245, 0.205),
              ("মডেল ও রেটিং", 0.28, 0.42),
              ("IEC 61095 (গৃহস্থালি)", 0.235, 0.505)],
        right=[("কয়েল A1", 0.485, 0.115),
               ("চারটি পোলই NO", 0.76, 0.445),
               ("আউটপুট 2 4 6 8", 0.72, 0.655),
               ("কয়েল A2", 0.485, 0.745)],
        note="গায়ে AC-7a লেখা, AC-3 নেই; এটি আলো ও হিটারের কন্টাক্টর",
        iw=430)


# ── ১০. পাওয়ার সার্কিট ─────────────────────────────────────────────────
def d10_power():
    """থ্রি-ফেজ পাওয়ার সার্কিট — MCB, কন্টাক্টরের মেইন কন্টাক্ট, মোটর।"""
    s = SVG(1240, 760)
    s.title("কন্টাক্টরের থ্রি-ফেজ পাওয়ার সার্কিট", T_TITLE)

    PH = [(430, "L1"), (570, "L2"), (710, "L3")]
    TOP, MCB_Y, KM_Y, MOT_Y = 118, 210, 380, 560

    # সরবরাহ
    # তিন ফেজ তিনটি আলাদা তার — একটি আড়াআড়ি রেখায় জোড়া দিলে সেটি
    # ফেজে-ফেজে শর্ট সার্কিট বোঝায় (আগের সংস্করণের ভুল)
    s.text(380, TOP + 9, "সরবরাহ", T_BODY, NAVY, 700, "end")
    for x, nm in PH:
        node(s, x, TOP, LIVE)
        s.text(x, TOP - 22, nm, T_BODY, LIVE, 700, "middle")
        s.path(f"M {x} {TOP} L {x} {MCB_Y - 42}", LIVE, 4)

    # MCB — তিন পোল, যান্ত্রিকভাবে জোড়া
    s.rect(390, MCB_Y - 42, 360, 84, PLATE, NAVY, 2.6, 8)
    for x, _ in PH:
        s.path(f"M {x} {MCB_Y - 26} L {x} {MCB_Y + 26}", NAVY, 3.4)
    s.path("M 430 {0} L 710 {0}".format(MCB_Y), NAVY, 2.2, dash="7 5")
    s.text(772, MCB_Y + 9, "MCB / MCCB", T_BODY, NAVY, 700, "start")
    for x, _ in PH:
        s.path(f"M {x} {MCB_Y + 42} L {x} {KM_Y - 54}", LIVE, 4)

    # কন্টাক্টরের মেইন কন্টাক্ট — তিনটি, যান্ত্রিকভাবে জোড়া
    s.rect(386, KM_Y - 54, 368, 112, "#FBFCFD", STEEL, 2.4, 8)
    for i, (x, _) in enumerate(PH):
        node(s, x, KM_Y - 34, LIVE)
        s.path(f"M {x} {KM_Y - 34} L {x + 36} {KM_Y + 20}", LIVE, 4)
        node(s, x, KM_Y + 34, LIVE)
        s.text(x - 16, KM_Y - 32, str(2 * i + 1), T_SMALL, NAVY, 700, "end")
        s.text(x - 16, KM_Y + 46, str(2 * i + 2), T_SMALL, NAVY, 700, "end")
    s.path(f"M 430 {KM_Y} L 710 {KM_Y}", STEEL, 2.2, dash="7 5")
    s.text(772, KM_Y - 14, "KM1 কন্টাক্টর", T_BODY, STEEL, 700, "start")
    s.text(772, KM_Y + 18, "মেইন কন্টাক্ট", T_SMALL, GREY, 400, "start")

    for x, _ in PH:
        s.path(f"M {x} {KM_Y + 58} L {x} {MOT_Y - 68}", LIVE, 4)

    # মোটর
    # তিনটি তার আলাদাভাবে মোটরের তিন টার্মিনালে (U, V, W)
    s.path(f"M 430 {MOT_Y - 68} L 537 {MOT_Y - 33}", LIVE, 4)
    s.path(f"M 570 {MOT_Y - 68} L 570 {MOT_Y - 46}", LIVE, 4)
    s.path(f"M 710 {MOT_Y - 68} L 603 {MOT_Y - 33}", LIVE, 4)
    s.circle(570, MOT_Y, 46, "#FFFFFF", SYM, 3.6)
    s.text(570, MOT_Y - 4, "M", T_NODE, SYM, 700, "middle")
    s.text(570, MOT_Y + 26, "3 ~", T_SMALL, SYM, 700, "middle")
    s.text(646, MOT_Y + 8, "থ্রি-ফেজ মোটর", T_BODY, NAVY, 700, "start")

    # বাঁ পাশের টীকা
    s.rect(64, 210, 252, 214, LIGHT, STEEL, 2, 10)
    s.text(190, 250, "এই তিনটি তার", T_BODY, NAVY, 700, "middle")
    s.text(190, 284, "মোটা হতে হবে,", T_BODY, NAVY, 700, "middle")
    s.text(190, 318, "কারণ মোটরের", T_BODY, NAVY, 700, "middle")
    s.text(190, 352, "পুরো কারেন্ট এদের", T_BODY, NAVY, 700, "middle")
    s.text(190, 386, "ভেতর দিয়ে যায়", T_BODY, NAVY, 700, "middle")

    y = note_strip(s, 640, "কন্ট্রোল সার্কিট আলাদা, তাই এই "
                           "ছবিতে দেখানো হয়নি")
    s.fit(y, 24)
    return s.save(f"{OUT}/d10_power.svg")


# ── ১১. সিলেক্টর সুইচ দিয়ে কন্ট্রোল ────────────────────────────────────
def d11_selector():
    """দুই তারের কন্ট্রোল — সুইচ যতক্ষণ ON, কয়েল ততক্ষণ টানা।"""
    s = SVG(1240, 700)
    s.title("সিলেক্টর সুইচ দিয়ে কন্টাক্টর নিয়ন্ত্রণ", T_TITLE)

    LY, NY = 244, 452
    s.text(84, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(84, NY + 9, "N", T_NODE, NEUT, 700, "end")

    # লাইভ → ফিউজ → সিলেক্টর → কয়েল → নিউট্রাল
    s.path(f"M 96 {LY} L 236 {LY}", LIVE, SW)
    s.rect(236, LY - 26, 84, 52, PLATE, NAVY, 2.6, 6)
    s.path(f"M 278 {LY - 26} L 278 {LY + 26}", NAVY, 3)
    s.text(278, LY - 44, "ফিউজ", T_BODY, NAVY, 700, "middle")
    s.path(f"M 320 {LY} L 474 {LY}", LIVE, SW)

    # সিলেক্টর সুইচ — মেইনটেইনড কন্টাক্ট
    node(s, 474, LY, LIVE)
    s.path(f"M 474 {LY} L 562 {LY - 48}", LIVE, SW)
    s.path(f"M 518 {LY - 24} L 518 {LY - 76}", GREY, 2.2, dash="6 4")
    s.circle(518, LY - 88, 13, "#FFFFFF", GREY, 2.4)
    node(s, 586, LY, LIVE)
    s.text(530, LY - 140, "সিলেক্টর সুইচ", T_BODY, NAVY, 700, "middle")
    s.text(530, LY - 112, "ON রাখলে ON-ই থাকে", T_SMALL, GREY, 400, "middle")
    s.path(f"M 586 {LY} L 760 {LY}", LIVE, SW)

    # কয়েল
    coil_sym(s, 760, LY - 44, 128, 88, "KM1")
    s.text(824, LY - 62, "কয়েল", T_BODY, NAVY, 700, "middle")
    s.text(748, LY - 54, "A1", T_SMALL, NAVY, 700, "end")
    s.text(900, LY - 54, "A2", T_SMALL, NAVY, 700, "start")
    s.path(f"M 888 {LY} L 1030 {LY} L 1030 {NY}", NEUT, SW)
    s.path(f"M 96 {NY} L 1030 {NY}", NEUT, SW)
    node(s, 1030, NY, NEUT)

    # ব্যাখ্যার পটি
    s.rect(236, 520, 380, 92, GREENBG, GREEN, 2.2, 10)
    s.text(426, 556, "সুইচ ON → কয়েল টানা", T_BODY, GREEN, 700, "middle")
    s.text(426, 590, "সুইচ OFF → কয়েল ছাড়া", T_BODY, GREEN, 700, "middle")
    s.rect(650, 520, 400, 92, REDBG, RED, 2.2, 10)
    s.text(850, 556, "বিদ্যুৎ ফিরলে মোটর", T_BODY, RED, 700, "middle")
    s.text(850, 590, "নিজে থেকেই চালু হবে", T_BODY, RED, 700, "middle")

    y = note_strip(s, 630, "দুই তারের কন্ট্রোল সহজ, কিন্তু লাইন "
                           "ফিরলে মোটর নিজে চালু হয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d11_selector.svg")


# ── ১২. পুশ বাটন ল্যাচিং সার্কিট ───────────────────────────────────────
def _pb_cap(s, cx, LY, col, bg, name, tip=None):
    """IEC পুশ বাটন — আড়াআড়ি পাত ও দণ্ড, ড্যাশ-রেখা ব্লেড পর্যন্ত।

    বোতামের মাথা কন্টাক্টের **উপরে** — নিচে নয়।  নিচে আঁকলে হোল্ডিং
    শাখার সঙ্গে জড়িয়ে যায়, আর ছবিটাই পড়া যায় না।  আগে এখানে কেবল
    একটি রঙিন বড়ি বসত আর ড্যাশ-রেখাটি ব্লেডের অনেক উপরে থেমে যেত;
    ওতে কোন কন্টাক্টটি বোতামের সঙ্গে বাঁধা তা বোঝাই যেত না।
    """
    if tip is None:
        tip = LY - 16
    PY = LY - 86
    s.rect(cx - 23, PY - 21, 46, 21, bg, col, 2.4, 4)
    s.path(f"M {cx - 34} {PY} L {cx + 34} {PY}", col, 3.6)
    s.path(f"M {cx} {PY} L {cx} {tip}", "#3B3B3B", 2.4, dash="7 5")
    s.text(cx, PY - 32, name, T_BODY, col, 700, "middle")


def _latch(s, LY, NY, live=None, pressed=None):
    """ল্যাচিং কন্ট্রোল সার্কিট।

    `live` — সক্রিয় পথের নাম:  None (নিভু), "start" (START চাপা),
    "hold" (হোল্ডিং কন্টাক্ট ধরে রেখেছে)।

    হোল্ডিং কন্টাক্ট START বোতামের **দুই প্রান্তের নোড দুটি থেকেই**
    নামে — সমান্তরাল, সিরিজ নয়।  এটাই এই ছবির একমাত্র জটিল কথা,
    আর ভুল হলে গোটা অধ্যায়টাই ভুল হয়ে যায়।
    """
    hot = LIVE if live else DEAD
    AX, BX, HB = 560, 700, LY + 110
    s.text(84, LY + 9, "L", T_NODE, LIVE, 700, "end")
    s.text(84, NY + 9, "N", T_NODE, NEUT, 700, "end")

    # লাইভ → ফিউজ
    s.path(f"M 96 {LY} L 200 {LY}", hot, SW)
    s.rect(200, LY - 24, 72, 48, PLATE, NAVY, 2.4, 6)
    s.path(f"M 236 {LY - 24} L 236 {LY + 24}", NAVY, 2.8)
    s.text(236, LY - 40, "ফিউজ", T_SMALL, NAVY, 700, "middle")

    # STOP — NC, চাপলে খোলে
    s.path(f"M 272 {LY} L 360 {LY}", hot, SW)
    stop_open = pressed == "stop"
    scol = DEAD if (stop_open or not live) else LIVE
    node(s, 360, LY, scol)
    s.path(f"M 452 {LY} L 452 {LY - 32}", scol, SW)     # ডান টার্মিনালের ঠেস
    if stop_open:
        s.path(f"M 360 {LY} L 436 {LY - 50}", DEAD, SW)
    else:
        s.path(f"M 360 {LY} L 464 {LY - 32}", scol, SW)  # ব্লেড ঠেসের উপরে
    node(s, 452, LY, scol)
    _pb_cap(s, 406, LY, RED, "#F6C9C4", "STOP  (NC)",
            tip=LY - (50 * 46 / 76 if stop_open else 32 * 46 / 104))

    # START — NO, চাপলে বন্ধ হয়।  দুই প্রান্তের নোড AX ও BX।
    s.path(f"M 452 {LY} L {AX} {LY}", LIVE if live else DEAD, SW)
    node(s, AX, LY, LIVE if live else DEAD)
    if pressed == "start":
        s.path(f"M {AX} {LY} L {BX} {LY}", LIVE, SW)
    else:
        s.path(f"M {AX} {LY} L {BX - 16} {LY - 50}", DEAD, SW)
    node(s, BX, LY, LIVE if live else DEAD)
    _pb_cap(s, 630, LY, GREEN, "#BFE3CE", "START  (NO)",
            tip=LY if pressed == "start" else LY - 50 * (630 - AX) / (BX - 16 - AX))

    # হোল্ডিং কন্টাক্ট — START-এর সমান্তরালে, নোড AX ও BX থেকেই
    hcol = LIVE if live == "hold" else DEAD
    s.path(f"M {AX} {LY} L {AX} {HB} L 600 {HB}", hcol, SW)
    node(s, 600, HB, hcol)
    if live:
        s.path(f"M 600 {HB} L 660 {HB}", hcol, SW)
    else:
        s.path(f"M 600 {HB} L 652 {HB - 42}", DEAD, SW)
    node(s, 660, HB, hcol)
    s.path(f"M 660 {HB} L {BX} {HB} L {BX} {LY}", hcol, SW)
    s.text(630, HB + 46, "হোল্ডিং কন্টাক্ট 13-14", T_BODY,
           LIVE if live == "hold" else GREY, 700, "middle")

    # কয়েল — প্রতীক, তাই খালি আয়তক্ষেত্র
    s.path(f"M {BX} {LY} L 840 {LY}", LIVE if live else DEAD, SW)
    coil_sym(s, 840, LY - 42, 124, 84, "KM1")
    s.text(828, LY - 52, "A1", T_SMALL, NAVY, 700, "end")
    s.text(976, LY - 52, "A2", T_SMALL, NAVY, 700, "start")
    # A2-এর দিকটা নিউট্রাল — কয়েল চালু থাকলেও ওটি লাল নয়
    s.path(f"M 964 {LY} L 1092 {LY} L 1092 {NY}", NEUT, SW)
    s.path(f"M 96 {NY} L 1092 {NY}", NEUT, SW)
    node(s, 1092, NY, NEUT)


def d12_latch():
    s = SVG(1240, 780)
    s.title("পুশ বাটন দিয়ে ল্যাচিং সার্কিট", T_TITLE)
    _latch(s, 290, 552, live="hold", pressed=None)
    s.rect(150, 600, 940, 72, LIGHT, STEEL, 2.2, 10)
    s.text(620, 646, "START ছেড়ে দিলেও 13-14 দিয়ে কয়েলে সরবরাহ থাকে",
           T_NAME, NAVY, 700, "middle")
    y = note_strip(s, 690, "হোল্ডিং কন্টাক্ট START-এর প্যারালালে বসে, "
                           "কখনো সিরিজে নয়")
    s.fit(y, 24)
    return s.save(f"{OUT}/d12_latch.svg")


# ── ১৩. ল্যাচিংয়ের তিন অবস্থা ──────────────────────────────────────────
def d13_latch_steps():
    """তিনটি অবস্থা, প্রতিবার সক্রিয় পথ লাল রঙে।"""
    s = SVG(1240, 1130)
    s.title("ল্যাচিং সার্কিটের তিন অবস্থা", T_TITLE)

    steps = [("বিশ্রামে: কোনো বাটন চাপা নেই", None, None,
              "কয়েলে ভোল্টেজ নেই, মোটর বন্ধ"),
             ("START চাপা", "start", "start",
              "কয়েল বিদ্যুৎ পায়, 13-14 সঙ্গে সঙ্গে বন্ধ হয়"),
             ("START ছেড়ে দেওয়ার পর", "hold", None,
              "13-14 দিয়ে কয়েলে কারেন্ট যেতে থাকে")]
    for i, (ttl, live, pressed, sub) in enumerate(steps):
        oy = 92 + i * 330
        s.rect(46, oy, 1148, 300, "#FCFDFE", LINE, 1.8, 12)
        # শিরোনামের বাক্স ব্যাজের ডান পাশ থেকে শুরু হয় — কেন্দ্রটা
        # তাই মাপ থেকে হিসাব করে বসাতে হয়, নইলে ব্যাজ ঢাকা পড়ে
        bw = tw(ttl, T_BODY, 600) + 44
        s.box_auto(126 + bw / 2, oy + 12, ttl, T_BODY, fill=STEEL,
                   stroke=STEEL, tcolor="#FFFFFF", pad_x=22, pad_y=9)
        s.badge(80, oy + 33, "কখগ"[i], 21, NAVY, "#FFFFFF", T_BODY)
        # ছোট মাপে আঁকতে হলে জায়গা কম — তাই কেবল দরকারি অংশ
        _latch_mini(s, oy, live, pressed)
        s.text(1150, oy + 288, sub, T_SMALL,
               LIVE if live else GREY, 700, "end")

    y = note_strip(s, 1092, "তিন তারের কন্ট্রোল: বিদ্যুৎ গেলে ল্যাচ "
                            "খুলে যায়, ফিরলে মোটর নিজে চালু হয় না")
    s.fit(y, 24)
    return s.save(f"{OUT}/d13_latch_steps.svg")


def _latch_mini(s, oy, live, pressed):
    """d13-এর ছোট সংস্করণ — একই টপোলজি, কম লেবেল।"""
    LY, NY = oy + 118, oy + 250
    hot = LIVE if live else DEAD
    AX, BX, HB = 520, 660, LY + 74

    s.text(96, LY + 8, "L", T_NAME, LIVE, 700, "end")
    s.text(96, NY + 8, "N", T_NAME, NEUT, 700, "end")
    s.path(f"M 106 {LY} L 250 {LY}", hot, 3)

    # STOP (NC) — কোনো ধাপেই চাপা হয় না
    scol = LIVE if live else DEAD
    node(s, 250, LY, scol)
    s.path(f"M 250 {LY} L 330 {LY - 26}", scol, 3)
    s.path(f"M 330 {LY - 26} L 330 {LY - 2}", scol, 3)
    node(s, 330, LY, scol)
    s.text(290, LY - 50, "STOP", T_SMALL, RED, 700, "middle")
    s.path(f"M 330 {LY} L {AX} {LY}", scol, 3)

    # START (NO)
    node(s, AX, LY, LIVE if live else DEAD)
    if pressed == "start":
        s.path(f"M {AX} {LY} L {BX} {LY}", LIVE, 3)
    else:
        s.path(f"M {AX} {LY} L {BX - 14} {LY - 44}", DEAD, 3)
    node(s, BX, LY, LIVE if live else DEAD)
    s.text((AX + BX) / 2, LY - 58, "START", T_SMALL, GREEN, 700, "middle")

    # হোল্ডিং কন্টাক্ট — সমান্তরাল শাখা
    hcol = LIVE if live == "hold" else DEAD
    s.path(f"M {AX} {LY} L {AX} {HB}", hcol, 3)
    node(s, AX + 40, HB, hcol)
    if live:
        s.path(f"M {AX + 40} {HB} L {AX + 120} {HB}", hcol, 3)
    else:
        s.path(f"M {AX + 40} {HB} L {AX + 112} {HB - 38}", DEAD, 3)
    node(s, AX + 120, HB, hcol)
    s.path(f"M {AX} {HB} L {AX + 40} {HB}", hcol, 3)
    s.path(f"M {AX + 120} {HB} L {BX} {HB} L {BX} {LY}", hcol, 3)
    s.text(AX + 80, HB + 34, "13-14", T_SMALL,
           LIVE if live == "hold" else GREY, 700, "middle")

    # কয়েল
    s.path(f"M {BX} {LY} L 790 {LY}", LIVE if live else DEAD, 3)
    coil_sym(s, 790, LY - 34, 108, 68, "KM1")
    s.path(f"M 898 {LY} L 1000 {LY} L 1000 {NY}", NEUT, 3)
    s.path(f"M 106 {NY} L 1000 {NY}", NEUT, 3)
    node(s, 1000, NY, NEUT)


# ── ১৪. কানেকশন ডায়াগ্রাম ──────────────────────────────────────────────
# টার্মিনাল থেকে টার্মিনাল — বোর্ডে ঠিক এভাবেই তার যাবে।
#
# তারের পথ হাতে বসানো, যাতে ক্রসিং প্রায় থাকেই না।  যেটুকু আছে
# (A2-এর তার আর A1-এর তার) সেটি নিরুপায় — A2 ব্লকের নিচে-ডানে আর
# A1 উপরে-বাঁয়ে, দুটোকেই ডান পাশের বোতামে যেতে হয়।  কনভেনশন
# অনুযায়ী ডট ছাড়া ক্রসিং মানে জোড়া নয়; জোড়া কেবল সেখানেই যেখানে
# ডট আঁকা।
def d14_wiring():
    """কানেকশন ডায়াগ্রাম — কোন তার কোন স্ক্রুতে।

    তারের তালিকা (ছবির আগে লেখা, অধ্যায় ১৪-এর নিয়মে):
      কন্ট্রোল L  → STOP 11
      STOP 12     → START 13          (নোড P)
      KM1 13      → START 13          (হোল্ডিং, সবুজ ড্যাশ)
      KM1 14      → START 14          (হোল্ডিং, সবুজ ড্যাশ)
      START 14    → KM1 A1            (নোড Q)
      KM1 A2      → কন্ট্রোল N
      সরবরাহ L1, L2, L3 → 1, 3, 5;  2, 4, 6 → মোটরের U, V, W — তিনটি
      আলাদা তার, কোথাও একসঙ্গে জোড়া নয়।

    বোতামের টার্মিনাল বোতামের বাঁ পাশে রাখায় কোনো তার অন্য তারকে
    কাটে না — ক্রসিং শূন্য, তাই ডট বা হপ কোনোটিরই দরকার পড়েনি।
    A1-এর তার নিচ দিয়ে ঘুরে আসে, মোটরের তিন তারের প্রান্তের নিচে।
    """
    s = SVG(1240, 900)
    s.title("ল্যাচিং সার্কিটের কানেকশন ডায়াগ্রাম", T_TITLE)

    def term(x, y, t, w=44, h=26):
        s.rect(x - w / 2, y, w, h, "#D7E2EC", STEEL, 2, 4)
        s.text(x, y + h / 2 + 6.5, t, T_TINY, NAVY, 700, "middle")

    # ── কন্টাক্টর ────────────────────────────────────────────────
    KX, KY, KW, KH = 260, 290, 340, 230
    s.rect(KX, KY, KW, KH, "#EEF3F8", STEEL, 3, 12)
    s.text(KX + KW / 2, KY + 118, "KM1", 44, STEEL, 700, "middle")
    s.text(KX + KW / 2, KY + 156, "ম্যাগনেটিক কন্টাক্টর", T_BODY, GREY,
           400, "middle")

    MAIN = [370, 435, 500]
    for i, x in enumerate(MAIN):
        term(x, KY - 26, str(2 * i + 1))
        s.path(f"M {x} {KY - 26} L {x} 196", LIVE, 3.6)
        s.text(x, 184, f"L{i + 1}", T_SMALL, LIVE, 700, "middle")
        term(x, KY + KH, str(2 * i + 2))
        s.path(f"M {x} {KY + KH + 26} L {x} 604", LIVE, 3.6)
        s.text(x, 634, "UVW"[i], T_SMALL, LIVE, 700, "middle")
    s.text(435, 146, "সরবরাহ", T_BODY, LIVE, 700, "middle")
    s.text(344, 634, "মোটরে", T_SMALL, LIVE, 700, "end")

    term(300, KY - 26, "A1")                  # উপরে-বাঁয়ে
    term(565, KY + KH, "A2")                  # নিচে-ডানে
    T13, T14 = 333, 489                       # KM1-এর 13 ও 14-এর মাঝরেখা
    term(KX + KW + 18, T13 - 13, "13", 30)    # ডানে — অক্সিলিয়ারি
    term(KX + KW + 18, T14 - 13, "14", 30)
    KR = KX + KW + 33                         # ডান টার্মিনালের বাইরের কিনারা

    # ── দুই বোতাম — টার্মিনাল বাঁ পাশে, কন্টাক্টরের দিকে মুখ করে ─────
    BX = 806                                  # বোতামের টার্মিনালের কেন্দ্র
    BL = BX - 22                              # টার্মিনালের বাঁ কিনারা

    def button(top, name, sub, col, bg, t1, t2):
        s.rect(BX + 22, top, 190, 112, bg, col, 2.8, 10)
        s.text(BX + 117, top + 46, name, T_NAME, col, 700, "middle")
        s.text(BX + 117, top + 82, sub, T_SMALL, GREY, 400, "middle")
        term(BX, top + 10, t1, h=34)
        term(BX, top + 68, t2, h=34)

    button(196, "STOP", "NC — লাল", RED, REDBG, "11", "12")
    button(416, "START", "NO — সবুজ", GREEN, GREENBG, "13", "14")
    S11, S12 = 196 + 27, 196 + 85             # STOP-এর তার ঢোকার উচ্চতা
    S13a, S13b = 416 + 17, 416 + 37           # START 13 — উপরে P, নিচে হোল্ডিং
    S14a, S14b = 484 + 5, 484 + 25            # START 14 — উপরে হোল্ডিং, নিচে A1

    # ── কন্ট্রোল সার্কিটের তার ───────────────────────────────────
    s.path(f"M 1150 160 L 770 160 L 770 {S11} L {BL} {S11}", LIVE, 3)
    s.text(1150, 140, "কন্ট্রোল সাপ্লাই L", T_SMALL, LIVE, 700, "end")

    # STOP 12 → START 13
    s.path(f"M {BL} {S12} L 750 {S12} L 750 {S13a} L {BL} {S13a}", NAVY, 3)

    # START 14 → A1:  নিচ দিয়ে ঘুরে, মোটরের তারের প্রান্তের নিচে
    s.path(f"M {BL} {S14b} L 770 {S14b} L 770 700 L 200 700 L 200 277 "
           f"L 278 277", NAVY, 3)
    s.text(485, 732, "START 14 → A1 (কয়েল)", T_SMALL, NAVY, 700, "middle")

    # A2 → N
    s.path(f"M 565 {KY + KH + 26} L 565 604 L 600 604", NEUT, 3)
    s.text(610, 611, "কন্ট্রোল N", T_SMALL, NEUT, 700, "start")

    # ── হোল্ডিং তার — KM1-এর 13 ও 14 START-এর দুই প্রান্তে ───────
    s.path(f"M {KR} {T13} L 700 {T13} L 700 {S13b} L {BL} {S13b}", GREEN, 3,
           dash="9 6")
    s.path(f"M {KR} {T14} L {BL} {S14a}", GREEN, 3, dash="9 6")
    s.text(686, 300, "হোল্ডিং তার", T_SMALL, GREEN, 700, "middle")

    y = note_strip(s, 790, "সবুজ ড্যাশ রেখার দুটি তার হোল্ডিং কন্টাক্টের; "
                           "না দিলে বাটন ছাড়লেই মোটর থামে")
    s.fit(y, 24)
    return s.save(f"{OUT}/d14_wiring.svg")


# ── ১৫. পুড়ে যাওয়া কন্টাক্ট ────────────────────────────────────────────
def d15_faults():
    return photo_callouts(
        "d15_faults", "পুড়ে যাওয়া মেইন কন্টাক্ট",
        "ph_burn.jpg",
        # লক্ষ্যগুলো গ্রিড বসিয়ে মাপা:  রুপোর টিপ = বাঁ পোলের ব্রিজের
        # ডান প্রান্তের ক্ষয়ে যাওয়া রুপোর প্যাড;  কালো তামা = ডান পোলের
        # স্থির কন্টাক্ট, নিচের স্ক্রু-ছিদ্রের চারপাশে;  ছিটকে জমা ধাতু =
        # ডান পোলের সাদা ছিটে;  অক্সিলিয়ারি ব্লক = LADN-এর গা।
        # তালিকা লক্ষ্যের উচ্চতা (fy) অনুযায়ী সাজানো, নইলে লিডার কাটাকাটি।
        left=[("রুপার টিপ ক্ষয়ে গেছে", 0.20, 0.46)],
        right=[("তাপে প্লাস্টিক গলেছে", 0.62, 0.22),
               ("ধাতু ছিটকে জমেছে", 0.775, 0.327),
               ("অক্সিলিয়ারি ব্লক", 0.93, 0.36),
               ("তামা কালো হয়ে গেছে", 0.72, 0.755)],
        note="বেশি কারেন্ট, ঢিলে স্ক্রু বা কম ভোল্টেজে চ্যাটারিংয়ের "
             "ফলে কন্টাক্ট এভাবে পোড়ে",
        iw=640)


ALL = [d01_idea, d02_outside, d03_exploded, d04_inside, d05_action,
       d06_symbols, d07_nameplate, d08_categories, d09_modular, d10_power,
       d11_selector, d12_latch, d13_latch_steps, d14_wiring, d15_faults]


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
