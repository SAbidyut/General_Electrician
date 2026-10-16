# -*- coding: utf-8 -*-
"""অধ্যায় ১০-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮ ও ৯-এর মতোই।  ডাউনলোডারটি
`assets_ch09.py`-র হুবহু কপি;  বদলেছে কেবল ছবির তালিকা।

  ph_ah3 / ph_ah3_base   ANLY AH3-NC — এ অঞ্চলের বাজারে সবচেয়ে চেনা
      ৮-পিনের টাইমারের ঘরানা।  পিন-মানচিত্র (2-7 সরবরাহ, 8-5/8-6
      বিলম্বিত, 1-4/1-3 দ্বিতীয় সেট) ANLY-র AH3-R ও Alion AH3-এর
      ডেটাশিটের সংযোগ-চিত্র ও টাইমিং চার্ট থেকে মেলানো।
  ph_motor / ph_pneu     গঠনভেদের উদাহরণ।
  ph_ts_digital / ph_ts_analog   টাইম সুইচ।

চালানোর নিয়ম:  python assets_ch10.py     (Book/build/ থেকে)
"""
import io
import json
import os
import re
import shutil
import time
import urllib.parse
import urllib.request

from PIL import Image, ImageEnhance, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "ch10")
CACHE = os.path.join(HERE, ".commons")
os.makedirs(OUT, exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

UA = {"User-Agent": "rapti-book/1.0 (textbook figure prep)"}
API = "https://commons.wikimedia.org/w/api.php"

# নাম → (কমন্সের ফাইলনাম, প্রত্যাশিত মাপ, ক্রপ-বক্স ভগ্নাংশে,
#        সর্বোচ্চ চওড়া, কনট্রাস্ট, ঘূর্ণন ডিগ্রিতে)
# মাপটা পাহারাদার — কমন্সে ছবি বদলালে ক্রপ-বক্স ভুল জায়গায় বসবে,
# আর সেটা এখানেই ধরা পড়বে (অধ্যায় ২০-এর শিক্ষা)।
PHOTOS = {
    # ── বাজারের অ্যানালগ টাইমার ─────────────────────────────────────
    # ANLY AH3-NC — ৮-পিনের মাল্টি-রেঞ্জ টাইমার, 6S/60S/6M/60M
    "ph_ah3":       ("限時繼電器AH3-NC.jpg",
                     (1840, 3264), (0.265, 0.285, 0.905, 0.740), 1100, 1.05, 0),
    # একই টাইমারের পেছন — আট পিন, মাঝে চাবি-খাঁজ
    "ph_ah3_base":  ("限時繼電器AH3-NC-01.jpg",
                     (1840, 3264), (0.170, 0.305, 0.800, 0.720), 1000, 1.05, 0),
    # ── টাইমারের নানা গঠন ──────────────────────────────────────────
    # মোটরচালিত (সিনক্রোনাস) টাইমার — Crouzet, পুরনো ল্যাব যন্ত্র
    "ph_motor":     ("Crouzet-timer1 hg.jpg",
                     (8272, 6200), (0.0, 0.0, 1.0, 1.0), 1100, 1.0, 0),
    # বায়ুচালিত (নিউমেটিক) সিঁড়ির বাতির সুইচ
    "ph_pneu":      ("Pneumatic pushbutton timer switch.jpg",
                     (621, 716), (0.0, 0.0, 1.0, 1.0), 621, 1.05, 0),
    # ── টাইম সুইচ ──────────────────────────────────────────────────
    "ph_ts_digital": ("Programmable switch clock for DIN rail.JPG",
                     (3600, 5100), (0.110, 0.015, 0.395, 0.455), 1100, 1.04, 0),
    "ph_ts_analog": ("Timer Quadro elettrico.jpg",
                     (2448, 3264), (0.185, 0.335, 0.640, 0.605), 1100, 1.04, 0),
}


REUSE = []


def _get(url):
    for _ in range(7):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=300).read()
        except Exception as exc:                 # ৪২৯ এলে থেমে আবার চেষ্টা
            print("   … আবার চেষ্টা:", exc)
            time.sleep(20)
    raise SystemExit("✗ নামানো গেল না: " + url)


# ছবি এত বড়ই নামানো হয় (অধ্যায় ৮-এ ১৭০০ ছিল;  এখানে চার-ছবির
# কোলাজ থেকে এক টুকরো কাটতে হয়, তাই বড়)।  সব ক্রপের `wmax` এর চেয়ে ছোট, তাই আসল
# ফাইল টানার দরকার নেই — কমন্স নিজেই মূল ফাইলের বদলে থাম্বনেইল
# ব্যবহার করতে বলে, আর আসল ফাইল বারবার টানলে ৪২৯ দেয়।
THUMB_W = 3200


def _meta(fname):
    """কমন্সের ফাইলনাম → থাম্বের URL, আসল মাপ, শিরোনাম, লেখক, লাইসেন্স।"""
    cache = os.path.join(CACHE, "ch10_meta.json")
    db = json.load(open(cache)) if os.path.exists(cache) else {}
    if fname not in db:
        q = urllib.parse.urlencode({
            "action": "query", "format": "json", "titles": "File:" + fname,
            "prop": "imageinfo", "iiprop": "url|size|extmetadata",
            "iiurlwidth": THUMB_W})
        d = json.loads(_get(API + "?" + q))
        page = next(iter(d["query"]["pages"].values()))
        if "imageinfo" not in page:
            raise SystemExit(f"✗ কমন্সে পাওয়া গেল না: {fname}")
        info = page["imageinfo"][0]
        em = info["extmetadata"]

        def field(key):
            v = str(em.get(key, {}).get("value", "")).strip()
            v = re.sub(r"<[^>]+>", "", v)          # লেখকের ঘরে HTML থাকে
            return re.sub(r"\s+", " ", v).strip()

        db[fname] = {"url": info.get("thumburl") or info["url"],
                     "size": [info["width"], info["height"]],
                     "title": field("ObjectName"), "author": field("Artist"),
                     "licence": field("LicenseShortName")}
        json.dump(db, open(cache, "w"), ensure_ascii=False, indent=1)
        time.sleep(2)
    return db[fname]


def fetch(fname):
    """ডাউনলোড করে ক্যাশে রাখা — বারবার কমন্সে হিট করলে ৪২৯ আসে।"""
    fn = os.path.join(CACHE, "ch10_" + re.sub(r"[^\w.-]", "_", fname))
    if not os.path.exists(fn) or os.path.getsize(fn) < 4096:
        open(fn, "wb").write(_get(_meta(fname)["url"]))
        time.sleep(3)
    return open(fn, "rb").read()


def main():
    credits = {}
    for name, (fname, size, box, wmax, contrast, rot) in PHOTOS.items():
        m = _meta(fname)
        # পাহারাদার — মাপ মেলে কমন্সে যা আছে তার সঙ্গে, নামানো থাম্বের
        # সঙ্গে নয়।  ছবিটি কেউ বদলে দিলে ক্রপ-বক্স ভুল জায়গায় বসবে,
        # আর সেটা এখানেই ধরা পড়বে (অধ্যায় ২০-এর শিক্ষা)।
        if tuple(m["size"]) != size:
            raise SystemExit(f"✗ {name}: {fname}-এর মাপ {tuple(m['size'])}, "
                             f"হওয়ার কথা {size} — কমন্সে ছবিটি বদলেছে, "
                             f"ক্রপ-বক্স আবার মিলিয়ে নিতে হবে")
        # EXIF-এর ওরিয়েন্টেশন আগে মেলানো — কমন্সের পাতায় ছবিটি যেভাবে
        # দেখায়, ক্রপ-বক্সও সেই হিসাবেই লেখা
        im = ImageOps.exif_transpose(
            Image.open(io.BytesIO(fetch(fname)))).convert("RGB")
        if rot:
            im = im.rotate(rot, expand=True)
        w, h = im.size
        im = im.crop((int(w * box[0]), int(h * box[1]),
                      int(w * box[2]), int(h * box[3])))
        if im.width > wmax:
            im = im.resize((wmax, round(im.height * wmax / im.width)),
                           Image.LANCZOS)
        if contrast != 1.0:
            im = ImageEnhance.Contrast(im).enhance(contrast)
        im.save(os.path.join(OUT, name + ".jpg"), quality=92)

        credits[name] = {"title": m["title"] or os.path.splitext(fname)[0],
                         "author": m["author"], "licence": m["licence"],
                         "source": "উইকিমিডিয়া কমন্স"}
        print(f"✓ {name:14s} {str(im.size):12s} {m['licence']:14s} {fname}")

    # আগের অধ্যায়ের ছবি লাগলে ছবি আর কৃতজ্ঞতা একসঙ্গে কপি হয়
    src = os.path.join(HERE, "assets", "ch08")
    for name in REUSE:
        shutil.copy(os.path.join(src, name + ".jpg"), OUT)
        credits[name] = json.load(open(os.path.join(src, "credits.json"),
                                       encoding="utf-8"))[name]
        print(f"✓ {name:14s} (অধ্যায় ৮ থেকে)")

    json.dump(credits, open(os.path.join(OUT, "credits.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n✓ credits.json —", len(credits), "টি ছবি")


if __name__ == "__main__":
    main()
