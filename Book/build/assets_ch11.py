# -*- coding: utf-8 -*-
"""অধ্যায় ১১-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮–১০-এর মতোই।  ডাউনলোডারটি
`assets_ch10.py`-র হুবহু কপি;  বদলেছে কেবল ছবির তালিকা।

  ph_genset      সাইলেন্ট ডিজেল জেনারেটর (Kirloskar, ভারত) — এ অঞ্চলের
                 বাজারের চেনা চেহারা।
  ph_atse        তৈরি ATS (Cummins Onan OTPC) — IEC 60947-6-1-এর ATSE।
  ph_phasesel    স্বয়ংক্রিয় ফেজ সিলেক্টর — কমন্সের বিবরণে লেখা, L1 গেলে
                 L2-তে, L2 গেলে L3-তে সরে।
  ph_ammeter     প্যানেলের মুভিং-আয়রন অ্যামিটার।
  ph_ct          LV কারেন্ট ট্রান্সফরমারের পরিবার — রিং ও কেস ধরনের।
  ph_ad16        AD16-22 ধরনের V/A/Hz পাইলট-মিটার ও তার নিজস্ব CT (CC0)।
  ph_cam         ক্যাম সুইচ — সিলেক্টর সুইচের ভেতরের গঠন।

চালানোর নিয়ম:  python assets_ch11.py     (Book/build/ থেকে)
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
OUT = os.path.join(HERE, "assets", "ch11")
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
    "ph_genset":   ("Kirloskar - Silent Diesel Generator Set - Mathura 2013-02-24 6663.JPG",
                    (4288, 2848), (0.140, 0.080, 0.785, 0.930), 1100, 1.0, 0),
    "ph_atse":     ("Cummins Onan Transfer Switch Model No. OTPCB-4494345.JPG",
                    (2816, 2112), (0.270, 0.000, 0.880, 0.960), 1100, 1.0, 0),
    "ph_phasesel": ("Transfer switching relay.JPG",
                    (3648, 2736), (0.370, 0.400, 0.870, 1.000), 1100, 1.0, 0),
    "ph_ammeter":  ("Moving iron ammeter.jpg",
                    (1608, 1393), (0.0, 0.0, 1.0, 1.0), 1100, 1.0, 0),
    # ITL-এর রিং ও প্লাস্টিক-কেস LV CT-র সারি (পাবলিক ডোমেইন)।  কমন্সের
    # "DIP current transformer.jpg" দেখতে CT হলেও আসলে 4-20 mA-এর
    # ট্রান্সডিউসার (গায়ে লেখা) — তাই বাদ।
    "ph_ct":       ("ITL-Family.jpg",
                    (600, 401), (0.02, 0.04, 0.98, 0.96), 600, 1.0, 0),
    "ph_ad16":     ("Type AD16-22 indicator meter with stock current transformer (4).jpg",
                    (2400, 2400), (0.040, 0.020, 0.960, 0.980), 1100, 1.0, 0),
    "ph_cam":      ("Cam Switch.jpg",
                    (4155, 2376), (0.360, 0.130, 0.960, 0.950), 1100, 1.0, 0),
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
    cache = os.path.join(CACHE, "ch11_meta.json")
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
    fn = os.path.join(CACHE, "ch11_" + re.sub(r"[^\w.-]", "_", fname))
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
