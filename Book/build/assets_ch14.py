# -*- coding: utf-8 -*-
"""অধ্যায় ১৪-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮–১২-এর মতোই।  ডাউনলোডারটি
`assets_ch12.py`-র কপি;  বদলেছে দুটো জিনিস — ছবির তালিকা, আর `REUSE`
এখন অভিধান, কারণ এই অধ্যায় ৮, ৯ ও ১০ — তিন জায়গা থেকেই ছবি নেয়।

  ph_manual      হাতে-চালানো স্টার-ডেল্টা সুইচের ভেতর।  কমন্সে
                 স্টার-ডেল্টা খুঁজে কাজে লাগার মতো একটিই ছবি আছে, আর
                 সেটি কন্টাক্টরের নয় — পুরোনো ড্রাম সুইচের।  তাতে
                 অসুবিধা নেই, উল্টো সুবিধা:  টার্মিনাল পট্টিতে
                 L1-L2-L3 আর কয়েলের ছয় প্রান্ত A1-A2, B1-B2, C1-C2
                 স্পষ্ট পড়া যায়, আর ১৪.১১-এর "আগে যেভাবে হতো" অংশটা
                 ওই ছবিতেই দাঁড়িয়ে আছে।  ছবিটি ৯০ ডিগ্রি ঘুরিয়ে নিতে
                 হয় (তোলা হয়েছে লম্বালম্বি, যন্ত্রটি আড়াআড়ি), আর
                 নিচের আলোকচিত্রীর জলছাপটুকু ক্রপে বাদ যায়।

যা নেওয়া হয়নি, ইচ্ছে করেই — "Transitionresistors-star-delta switch"
নামের দুটি ছবি (৩০০ কিলোওয়াট মোটরের পুড়ে যাওয়া ট্রানজিশন রেজিস্টর)।
ছবি দুটি আসল ও ভালো, কিন্তু ওগুলো **ক্লোজড ট্রানজিশন** স্টার-ডেল্টার
জিনিস, যা এই সিলেবাসে নেই;  রেজিস্টর কী করছে তা না বুঝিয়ে ছবিটা
বসালে শিক্ষার্থী বিভ্রান্ত হবে (অধ্যায় ১১-এর CT-ছবির শিক্ষা —
ক্যাপশন লেখার আগে নেমপ্লেট পড়ো, আর যা ব্যাখ্যা করা যাবে না তা
বসিও না)।  ক্লোজড ট্রানজিশনের কথা ১৪.১২-এ এক অনুচ্ছেদে আছে, ছবি ছাড়া।

আগের অধ্যায় থেকে আসা (`REUSE`):  অধ্যায় ৮ থেকে ph_starter,
ph_contactor, ph_modular, ph_pb_green, ph_pb_red, ph_burn;  অধ্যায় ৯
থেকে ph_olr, ph_mounted;  অধ্যায় ১০ থেকে ph_ah3, ph_ah3_base।

চালানোর নিয়ম:  python assets_ch14.py     (Book/build/ থেকে)
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
OUT = os.path.join(HERE, "assets", "ch14")
CACHE = os.path.join(HERE, ".commons")
os.makedirs(OUT, exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

UA = {"User-Agent": "rapti-book/1.0 (textbook figure prep)"}
API = "https://commons.wikimedia.org/w/api.php"

# নাম → (কমন্সের ফাইলনাম, প্রত্যাশিত মাপ, ক্রপ-বক্স ভগ্নাংশে,
#        সর্বোচ্চ চওড়া, কনট্রাস্ট, ঘূর্ণন ডিগ্রিতে)
# ঘূর্ণন **আগে** হয়, ক্রপ **পরে** — তাই ক্রপ-বক্সটা ঘোরানো ছবির হিসাবে।
# মাপটা পাহারাদার — কমন্সে ছবি বদলালে ক্রপ-বক্স ভুল জায়গায় বসবে,
# আর সেটা এখানেই ধরা পড়বে।
PHOTOS = {
    "ph_manual": ("Star delta starter internal strúçture.jpg",
                  (2308, 3916), (0.075, 0.025, 0.995, 0.985), 1500, 1.08,
                  -90),
}

# নাম → কোন অধ্যায়ের ফোল্ডার থেকে;  ছবি আর কৃতজ্ঞতা একসঙ্গে আসে
REUSE = {
    "ph_starter": "ch08", "ph_contactor": "ch08", "ph_modular": "ch08",
    "ph_pb_green": "ch08", "ph_pb_red": "ch08", "ph_burn": "ch08",
    "ph_olr": "ch09", "ph_mounted": "ch09",
    "ph_ah3": "ch10", "ph_ah3_base": "ch10",
}


def _get(url):
    for _ in range(7):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=300).read()
        except Exception as exc:                 # ৪২৯ এলে থেমে আবার চেষ্টা
            print("   … আবার চেষ্টা:", exc)
            time.sleep(20)
    raise SystemExit("✗ নামানো গেল না: " + url)


# কমন্সের নিজস্ব নিয়ম — মূল ফাইল বারবার টানলে ৪২৯, আর থাম্বের চওড়াও
# তাদের তালিকার মাপ হতে হয় (নইলে ৪০০:  "Use thumbnail sizes listed
# on https://w.wiki/GHai")।  ১২৮০ ওই তালিকার একটি মাপ।
THUMB_W = 1280


def _meta(fname):
    """কমন্সের ফাইলনাম → থাম্বের URL, আসল মাপ, শিরোনাম, লেখক, লাইসেন্স।"""
    cache = os.path.join(CACHE, "ch14_meta.json")
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
    fn = os.path.join(CACHE, "ch14_" + re.sub(r"[^\w.-]", "_", fname))
    if not os.path.exists(fn) or os.path.getsize(fn) < 4096:
        open(fn, "wb").write(_get(_meta(fname)["url"]))
        time.sleep(3)
    return open(fn, "rb").read()


def main():
    credits = {}
    for name, (fname, size, box, wmax, contrast, rot) in PHOTOS.items():
        m = _meta(fname)
        if tuple(m["size"]) != size:
            raise SystemExit(f"✗ {name}: {fname}-এর মাপ {tuple(m['size'])}, "
                             f"হওয়ার কথা {size} — কমন্সে ছবিটি বদলেছে, "
                             f"ক্রপ-বক্স আবার মিলিয়ে নিতে হবে")
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

    for name, src in REUSE.items():
        d = os.path.join(HERE, "assets", src)
        shutil.copy(os.path.join(d, name + ".jpg"), OUT)
        credits[name] = json.load(open(os.path.join(d, "credits.json"),
                                       encoding="utf-8"))[name]
        print(f"✓ {name:14s} (অধ্যায় {src[2:]} থেকে)")

    json.dump(credits, open(os.path.join(OUT, "credits.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n✓ credits.json —", len(credits), "টি ছবি")


if __name__ == "__main__":
    main()
