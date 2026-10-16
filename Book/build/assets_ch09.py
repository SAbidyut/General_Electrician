# -*- coding: utf-8 -*-
"""অধ্যায় ৯-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮-এর মতোই।  ডাউনলোডারটি
`assets_ch08.py`-র হুবহু কপি (থাম্বনেইল টানে, পূর্ণ ফাইল নয় — নইলে
কমন্স ৪২৯ দেয়);  বদলেছে কেবল ছবির তালিকা।

যে ছবিগুলো এই অধ্যায়ের ভার টানে:

  ph_olr        Allen-Bradley EA ঘরানার ওভারলোড রিলে — 95 N.C. 96,
      97 N.O. 98, 2 T1 4 T2 6 T3, TEST, TRIPPED, PUSH TO RESET সব
      গায়ে ছাপা।  ৯.৪-এর টার্মিনাল-মানচিত্র এর উপরে।  (আপলোডারের
      বিবরণে রিলেটি ইলেকট্রনিক;  সামনের দিক থার্মালের মতোই, তাই
      বইয়ের লেখায় "থার্মাল" বলে দাবি করা হয়নি।)
  ph_mounted    একই ঘরানার রিলে কন্টাক্টরের নিচে সরাসরি বসানো।
  ph_bimetal / ph_ra20_open / ph_inside — বাইমেটাল ও ভেতরের গঠন।
  ph_mpcb       Siemens 3RV2011 — বাংলাদেশি আপলোডারের তোলা, গায়ে
      CLASS 10 পড়া যায়।
  ph_starter    অধ্যায় ৮ থেকে আবার ব্যবহার (`REUSE`)।

কমন্সে `Dol starter.jpg` ও `Auto DOL starter.jpg` নামে দুটি ছবি আছে,
কিন্তু দুটোই হাতে আঁকা সার্কিট আর তাতে ওভারলোড রিলেই নেই — ইচ্ছে
করে বাদ।

চালানোর নিয়ম:  python assets_ch09.py     (Book/build/ থেকে)
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
OUT = os.path.join(HERE, "assets", "ch09")
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
    # ── ওভারলোড রিলে — সামনের দিক ──────────────────────────────────
    # Allen-Bradley EA — প্রতিটি টার্মিনালের নাম (95 N.C. 96, 97 N.O. 98,
    # 2 T1 …) আর TEST, TRIPPED, Man/Trip, PUSH TO RESET গায়ে পড়া যায়।
    # ৯.৪-এর টার্মিনাল-মানচিত্র এই ছবির উপরেই।
    "ph_olr":       ("Swiss AB MSR Motorschutzrelais.jpg",
                     (1324, 1324), (0.040, 0.000, 0.880, 1.000), 1200, 1.04, 0),
    # একই ঘরানার রিলে কন্টাক্টরের ঠিক নিচে বসানো — তিনটি পিন সোজা
    # কন্টাক্টরের 2/4/6-এ ঢুকেছে।  আপলোডারের আঁকা রঙিন দাগগুলো
    # ক্রপে বাদ:  উপরের লাল-হলুদ পটি (y < ০.১২), ডানের লাল টুকরো
    # (x > ০.৯৩) আর নিচের নীল পটি (y > ০.৮৩)।
    "ph_mounted":   ("Motorschutzrelais.jpg",
                     (645, 1001), (0.000, 0.125, 0.930, 0.828), 645, 1.04, 0),
    # GE MTO3N — থার্মাল রিলে, ডায়াল 7.5–10.5 A, H/A রিসেট
    "ph_ge":        ("GE MTO3N.JPG",
                     (3648, 2736), (0.260, 0.060, 0.790, 0.870), 1100, 1.05, 0),
    # RA-20 — বাজারের চেনা চীনা ঘরানার রিলে (চার ছবির উপরে-বাঁ)
    "ph_ra20":      ("SHERNDIAN ELECTRIC RA-20.JPG",
                     (7300, 5470), (0.130, 0.020, 0.430, 0.345), 1200, 1.06, 0),

    # ── ভেতরের গঠন ─────────────────────────────────────────────────
    # RA-20 খোলা অবস্থায় (চার ছবির নিচে-ডানে)
    "ph_ra20_open": ("SHERNDIAN ELECTRIC RA-20.JPG",
                     (7300, 5470), (0.780, 0.520, 0.990, 0.985), 1100, 1.06, 0),
    # একটি বাইমেটাল স্ট্রিপ, গায়ে হিটারের পাক (চার ছবির উপরে-বাঁ)
    "ph_bimetal":   ("Bimetallic strip from RA-20 overload relay.JPG",
                     (7300, 5470), (0.100, 0.090, 0.405, 0.370), 1300, 1.06, 0),
    # পুরনো একটি থার্মাল রিলের ভেতর — তিনটি বাইমেটাল পাশাপাশি
    "ph_inside":    ("Relé térmico.jpg",
                     (3000, 4000), (0.000, 0.000, 1.000, 1.000), 1100, 1.05, 0),

    # ── মোটর প্রোটেকশন সার্কিট ব্রেকার ─────────────────────────────
    # Siemens 3RV2011 — গায়ে CLASS 10 আর 0.55–0.8 A ডায়াল
    "ph_mpcb":      ("Siemens MPCB.jpg",
                     (1328, 2288), (0.000, 0.000, 1.000, 1.000), 1000, 1.04, 0),
}


REUSE = ["ph_starter"]


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
    cache = os.path.join(CACHE, "ch09_meta.json")
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
    fn = os.path.join(CACHE, "ch09_" + re.sub(r"[^\w.-]", "_", fname))
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

    # অধ্যায় ৮-এর DOL স্টার্টারের ছবিটি এখানেও লাগে — ছবি আর তার
    # কৃতজ্ঞতা একসঙ্গে কপি হয়, যাতে দুটো কখনো আলাদা না হয়
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
