# -*- coding: utf-8 -*-
"""dia_cover.py — বইয়ের প্রচ্ছদ (full-bleed A4 আর্টওয়ার্ক)।

ক্যানভাস ১২৪০ × ১৭৫৪ px = A4-এর অনুপাত (১:১.৪১৪২), পূর্ণ পৃষ্ঠাজুড়ে বসে।
১২৪০ px ২১০ মিমি চওড়া হলে ১ px = ০.৪৮ pt — তাই ১০০ px শিরোনাম ছাপে ৪৮ pt।

ভাবনা — **একটি ড্রয়িং শিট**।  পুরো পৃষ্ঠা এক টানা গাঢ় নীল; তার উপর খুব
হালকা ব্লুপ্রিন্ট-গ্রিড, সোনালি কিনারার রেখা, আর নিচের অর্ধে ম্লান রেখায়
একটি কন্ট্রোল প্যানেলের নকশা।  সহোদর বই ‘ইলেকট্রিক্যাল হাউস ওয়্যারিং’-এর
প্রচ্ছদের সঙ্গে এক চেহারা রাখার জন্য শিট, গ্রিড, সোনালি কিনারা ও লেখার
বিন্যাস হুবহু একই — বদলেছে কেবল শিরোনাম আর মাঝের মোটিফ, কারণ এই বইয়ের
বিষয় ঘরের ওয়্যারিং নয়, শিল্পকারখানার মোটর কন্ট্রোল।

মোটিফ = একটি পূর্ণ **DOL স্টার্টার** — ডান দিকে পাওয়ার সার্কিট (তিন ফেজ
বাস → MCB → কন্টাক্টরের তিন পোল → ওভারলোড রিলে → মোটর), বাঁ দিকে তারই
কন্ট্রোল ল্যাডার (STOP NC → START NO ‖ হোল্ডিং কন্টাক্ট → কয়েল), আর দুইয়ের
মাঝে কয়েল থেকে কন্টাক্টে যাওয়া ছেঁড়া-রেখার যান্ত্রিক সংযোগ।  অর্থাৎ বইয়ের
অধ্যায় ৮ ও ৯-এর ছবিটাই প্রচ্ছদে — সাজানো, কিন্তু বানানো নয়: ল্যাচিং
প্যারালালে, ওভারলোড রিলে কয়েলের আগে, হোল্ডিং কন্টাক্ট START-এর পাশে।

প্রচ্ছদটি বইয়ে **PNG হিসেবেই** বসে, SVG নয় — যার কম্পিউটারে কালপুরুষ নেই তার
কাছেও প্রচ্ছদ হুবহু একই দেখাবে।
"""
import os
from svgkit import SVG, tw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "diagrams", "cover")
IMG = os.path.join(HERE, "assets", "cover")

W, H = 1240, 1754
CX = W / 2
INSET = 40                       # শিটের কিনারার রেখা

GOLD    = "#C8A64B"
GOLD_L  = "#DFC57E"
WHITE   = "#FFFFFF"
NEARW   = "#E9F1F8"
PALE    = "#A9C8E4"
PALE2   = "#8AAECD"
SUB     = "#C0D6EA"
NAVY_D  = "#0A2440"
MOTIF   = "#6FA8DC"
LATIN   = "Helvetica Neue"


def _sheet(s):
    """পটভূমি — নীল গ্রেডিয়েন্ট, ব্লুপ্রিন্ট-গ্রিড, সোনালি কিনারা।

    গ্রিড দুটি `<pattern>`, `s.add()` দিয়ে সরাসরি বসানো — `s.rect()` দিয়ে নয়।
    কারণ `qc.py` প্রতিটি রেকর্ড করা রেখাকে লেখার সঙ্গে মিলিয়ে দেখে, আর
    পটভূমির গ্রিড তো লেখার নিচ দিয়েই যাবে — সেটিই নকশা, ত্রুটি নয়।
    """
    s.defs.append(
        '<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#0A2440"/>'
        '<stop offset="0.45" stop-color="#133D63"/>'
        '<stop offset="1" stop-color="#061829"/></linearGradient>')
    s.defs.append(
        '<pattern id="grid1" width="62" height="62" patternUnits="userSpaceOnUse">'
        '<path d="M 62 0 L 0 0 0 62" fill="none" stroke="#7FB3DD" '
        'stroke-width="1" opacity="0.07"/></pattern>')
    s.defs.append(
        '<pattern id="grid2" width="310" height="310" patternUnits="userSpaceOnUse">'
        '<path d="M 310 0 L 0 0 0 310" fill="none" stroke="#7FB3DD" '
        'stroke-width="1.5" opacity="0.13"/></pattern>')
    s.add(f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>')
    s.add(f'<rect width="{W}" height="{H}" fill="url(#grid1)"/>')
    s.add(f'<rect width="{W}" height="{H}" fill="url(#grid2)"/>')
    s.add(f'<rect x="{INSET}" y="{INSET}" width="{W - 2*INSET}" '
          f'height="{H - 2*INSET}" fill="none" stroke="{GOLD}" '
          f'stroke-width="1.5" opacity="0.38"/>')
    # চার কোণে ছোট সোনালি কোণ-রেখা — শিটটিকে সত্যিকারের ড্রয়িং শিটের মতো
    # বাঁধে, আর ভেতরের কিনারার রেখাটিকে একঘেয়ে আয়তক্ষেত্র হতে দেয় না।
    k, d = INSET + 16, 54
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x = k if sx > 0 else W - k
        y = k if sy > 0 else H - k
        s.add(f'<g opacity="0.55" stroke="{GOLD}" stroke-width="2.2" '
              f'fill="none" stroke-linecap="square">'
              f'<line x1="{x}" y1="{y}" x2="{x + sx*d}" y2="{y}"/>'
              f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + sy*d}"/></g>')


def _divider(s, y, half, sw=1.1, op=0.55):
    """মাঝখানে ছোট সোনালি হীরকসহ একটি সরু রেখা।"""
    s.add(f'<g opacity="{op}">'
          f'<line x1="{CX-half:.1f}" y1="{y}" x2="{CX-20:.1f}" y2="{y}" '
          f'stroke="{GOLD}" stroke-width="{sw}"/>'
          f'<line x1="{CX+20:.1f}" y1="{y}" x2="{CX+half:.1f}" y2="{y}" '
          f'stroke="{GOLD}" stroke-width="{sw}"/>'
          f'<polygon points="{CX:.1f},{y-6} {CX+6:.1f},{y} {CX:.1f},{y+6} '
          f'{CX-6:.1f},{y}" fill="{GOLD}"/></g>')


def _motif(s):
    """ম্লান রেখায় একটি DOL স্টার্টার — বাঁয়ে কন্ট্রোল ল্যাডার, ডানে
    পাওয়ার সার্কিট, মাঝে কয়েল থেকে কন্টাক্টে ছেঁড়া-রেখার যান্ত্রিক সংযোগ।

    গোটা মোটিফ একটি `<g opacity>`-এর ভেতরে।  `svgkit.line()`-এ opacity
    আর্গুমেন্ট নেই, তাই প্রতিটি আকৃতিতে আলাদা দিলে রেখা পুরো গাঢ় আর বৃত্ত
    হালকা হয়ে যেত।

    তারের সংযোগ-বিন্দুতে ভরাট বৃত্ত, আর কোথাও দুটি তার কাটাকাটি করেনি —
    বইয়ের নিজের নিয়ম প্রচ্ছদেও মানা।
    """
    sw = 2.6
    s.add('<g opacity="0.28">')

    def dot(x, y):
        s.circle(x, y, 5.0, MOTIF, "none", 0)

    # কন্টাক্টের প্রতীক দুটি হুবহু বইয়ের নিজের `dia_ch09._nc` / `_no` —
    # অনুভূমিক রাংয়ের উপর, দুই প্রান্তে জোড়-বিন্দু।  NC-র ব্লেড ডান
    # টার্মিনালের ঠেসের মাথায় গিয়ে বসে (বন্ধ), NO-র ব্লেড ডান নোড ছেড়ে
    # উঠে থাকে (খোলা)।
    NCW, NCRUN, NCRISE = 92.0, 104.0, 34.0
    NOW, NORISE = 92.0, 44.0

    def nc_h(x, y):
        dot(x, y)
        s.line(x + NCW, y, x + NCW, y - NCRISE, MOTIF, sw)
        s.line(x, y, x + NCRUN, y - NCRISE, MOTIF, sw)
        dot(x + NCW, y)
        return x + NCW

    def no_h(x, y):
        dot(x, y)
        s.line(x, y, x + NOW - 14, y - NORISE, MOTIF, sw)
        dot(x + NOW, y)
        return x + NOW

    # ── কন্ট্রোল ল্যাডার (বাঁ দিক) ─────────────────────────────────────
    # দুই খাড়া রেল — বাঁয়ে L, ডানে N।  উপরের রাং:  STOP → START → কয়েল।
    # নিচের রাং:  হোল্ডিং কন্টাক্ট, START-এর ঠিক সমান্তরালে — অর্থাৎ
    # অধ্যায় ৯-এর ল্যাচিং সার্কিটই, ছোট করে আঁকা।
    # রেল দুটি উপরে-নিচে জোড়া নয় — জোড়া দিলে গোটা ল্যাডার একটা ফাঁকা
    # আয়তক্ষেত্র হয়ে যায়, আর সেটাই প্রথম রেন্ডারে দেখা গিয়েছিল।  বদলে
    # চার প্রান্তে টার্মিনাল বিন্দু, অর্থাৎ L আর N বাইরে থেকে আসছে।
    LRX, NRX = 184.0, 624.0                  # L রেল, N রেল
    LT, LB = 1052.0, 1324.0
    R1, R2 = 1128.0, 1248.0                  # দুই রাং
    s.line(LRX, LT, LRX, LB, MOTIF, sw)
    s.line(NRX, LT, NRX, LB, MOTIF, sw)
    for xx in (LRX, NRX):
        for yy in (LT, LB):
            s.circle(xx, yy, 5.0, MOTIF, "none", 0)

    s.line(LRX, R1, 224, R1, MOTIF, sw)
    a = nc_h(224, R1)                        # STOP
    s.line(a, R1, a + 40, R1, MOTIF, sw)
    NA = a + 40                              # START-এর বাঁ নোড
    b = no_h(NA, R1)                         # START
    NB = b                                   # START-এর ডান নোড
    s.line(NB, R1, NB + 34, R1, MOTIF, sw)
    s.rect(NB + 34, R1 - 26, 96, 52, "none", MOTIF, sw, 5)     # কয়েল
    s.line(NB + 48, R1 - 13, NB + 116, R1 + 13, MOTIF, sw * 0.8)
    s.line(NB + 130, R1, NRX, R1, MOTIF, sw)

    # হোল্ডিং শাখা — দুই নোড থেকে নেমে দ্বিতীয় রাংয়ে, সেখানেই NO কন্টাক্ট
    s.line(NA, R1, NA, R2, MOTIF, sw)
    s.line(NB, R2, NB, R1, MOTIF, sw)
    no_h(NA, R2)
    dot(NA, R1); dot(NB, R1)

    # ── পাওয়ার সার্কিট (ডান দিক) ──────────────────────────────────────
    PX = (790.0, 890.0, 990.0)                                 # তিন ফেজ
    s.line(PX[0] - 44, LT, PX[2] + 44, LT, MOTIF, sw)          # সরবরাহ বাস
    for x in PX:
        dot(x, LT)
        s.line(x, LT, x, 1074, MOTIF, sw)
        s.rect(x - 19, 1074, 38, 48, "none", MOTIF, sw, 5)     # MCB
        s.line(x - 9, 1110, x + 9, 1086, MOTIF, sw * 0.8)
        s.line(x, 1122, x, 1146, MOTIF, sw)
        # কন্টাক্টরের পোল — খোলা NO, খাড়া করে আঁকা
        dot(x, 1146)
        s.line(x, 1146, x + 32, 1192, MOTIF, sw)
        dot(x, 1206)
        s.line(x, 1206, x, 1222, MOTIF, sw)
        s.rect(x - 19, 1222, 38, 48, "none", MOTIF, sw, 5)     # ওভারলোড রিলে
        for yy in (1234, 1246, 1258):
            s.line(x - 10, yy, x + 10, yy, MOTIF, sw * 0.8)

    # তিন ফেজ মোটরে — বাইরের দুটি ভেতরের দিকে বেঁকে, কোথাও কাটাকাটি নেই
    MY, MR = 1374.0, 58.0
    s.line(PX[0], 1270, PX[0], 1292, MOTIF, sw)
    s.line(PX[0], 1292, PX[1] - 32, 1328, MOTIF, sw)
    s.line(PX[1], 1270, PX[1], 1316, MOTIF, sw)
    s.line(PX[2], 1270, PX[2], 1292, MOTIF, sw)
    s.line(PX[2], 1292, PX[1] + 32, 1328, MOTIF, sw)
    s.circle(PX[1], MY, MR, "none", MOTIF, sw)
    s.text(PX[1], MY + 4, "M", 52, MOTIF, 700, "middle", family=LATIN)
    s.line(PX[1] - 22, MY + 22, PX[1] - 8, MY + 12, MOTIF, sw * 0.85)
    s.line(PX[1] - 8, MY + 12, PX[1] + 8, MY + 30, MOTIF, sw * 0.85)
    s.line(PX[1] + 8, MY + 30, PX[1] + 22, MY + 20, MOTIF, sw * 0.85)

    s.add("</g>")


def cover():
    s = SVG(W, H, bg=NAVY_D)
    _sheet(s)
    _motif(s)

    # ── প্রতিষ্ঠানের পরিচয় ─────────────────────────────────────────────
    # উৎস-ফাইল ৩৫৬ px চওড়া; ২৫০ px-এ বসালে ছাপে ≈২১৭ dpi — এর বেশি বড়
    # করলে ওয়ার্ডমার্ক নরম দেখাবে।
    lw, lh = 250.0, 91.3
    s.image(CX - lw / 2, 100, lw, lh, os.path.join(IMG, "logo_rapti_light.png"))
    s.text(CX, 252, "রেজোন্যান্স অটোমেশন প্রফেশনাল ট্রেনিং ইনস্টিটিউট",
           29, NEARW, 700, "middle")
    s.text(CX, 284, "RESONANCE  AUTOMATION  PROFESSIONAL  TRAINING  INSTITUTE",
           15, PALE2, 500, "middle", family=LATIN, ls=2.8)
    _divider(s, 326, 290)

    # ── শিরোনাম ────────────────────────────────────────────────────────
    s.text(CX, 424, "প্রশিক্ষণ পাঠ্যপুস্তক", 25, GOLD_L, 700, "middle", ls=13)
    s.text(CX, 564, "জেনারেল", 104, WHITE, 700, "middle")
    s.text(CX, 696, "ইলেকট্রিশিয়ান", 104, WHITE, 700, "middle")
    s.line(CX - 75, 754, CX + 75, 754, GOLD, 3)
    s.text(CX, 810, "GENERAL ELECTRICIAN", 24, PALE, 300, "middle",
           family=LATIN, ls=8)
    s.text(CX, 872, "কোর্স মডিউল অনুযায়ী প্রণীত পূর্ণাঙ্গ পাঠ্যপুস্তক",
           25, SUB, 400, "middle")

    chip = "প্রথম সংস্করণ  ·  ২০২৬  ·  অধ্যায় ১–১৭"
    cwid = tw(chip, 22, 600) + 80
    s.rect(CX - cwid / 2, 910, cwid, 52, "none", GOLD, 1.5, 26, opacity=0.55)
    s.text(CX, 943, chip, 22, GOLD_L, 600, "middle")

    # ── যোগাযোগ ────────────────────────────────────────────────────────
    _divider(s, 1448, 340, sw=1.0, op=0.45)
    s.text(CX, 1508, "অ্যাডমিশন হটলাইন   ০১৬১৭-৩৪৫৫৩৪", 26, WHITE, 700, "middle")
    s.text(CX, 1552, "raptibd@gmail.com     ·     rapti.net", 21, PALE, 400,
           "middle", family=LATIN)
    s.text(CX, 1594,
           "২১০১, ভুইঘর, রূপায়ণ টাউন, গেট-১ সংলগ্ন, ফতুল্লা, নারায়ণগঞ্জ-১৪২০",
           19, PALE2, 400, "middle")

    return s.save(f"{OUT}/cover.svg")


ALL = [cover]

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
