# -*- coding: utf-8 -*-
"""অধ্যায় ১৬-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮–১৪-এর মতোই।  ডাউনলোডারটি
`assets_ch14.py`-র কপি;  বদলেছে কেবল ছবির তালিকা।

এই অধ্যায়ে কমন্স অস্বাভাবিক রকমের উদার — আগের ছয় অধ্যায়ে যেখানে
কন্ট্রোল-গিয়ারের একটা-দুটো ছবির বেশি মেলেনি, সেখানে সোলারের ছবি
প্রচুর, এবং দুটি **বাংলাদেশেরই**:

  ph_roof_bd    খুলনা জেলার ছাদে বসানো সোলার অ্যারে (Helena Wright,
                CC BY 2.0)।  বিদেশি ছাদের ছবি দিয়ে বাংলাদেশের বই
                শুরু করার দরকার নেই যখন খুলনারটাই পাওয়া যায়।
  ph_hatil      হাতিল কারখানার ছাদের সারি — শিল্প-ছাদের মাপ বোঝাতে।

যেগুলো নেমপ্লেট ও টার্মিনাল পড়ার কাজে লাগে — এই অধ্যায়ের আসল
সম্পদ, কারণ ১৬.৩ পুরোটাই "গায়ের লেখা পড়া" নিয়ে:

  ph_back       ১৬৫ W প্যানেলের পিছন — জাংশন বক্স, স্পেসিফিকেশন
                স্টিকার ও গুটিয়ে রাখা তার একসঙ্গে দেখা যায়।
  ph_jbox       একই প্যানেলের জাংশন বক্সের কাছ থেকে তোলা ছবি।
  ph_jbox_open  খোলা জাংশন বক্স — ভেতরের বাইপাস ডায়োড দেখা যায়।
  ph_edge       মডিউলের কিনারার প্রস্থচ্ছেদ — ফ্রেম, ব্যাকশিট, বাস
                রিবন ও ডায়োডের সংযোগ।  ১২৩০x৮০৩, তাই বড় করে
                বসানো যাবে না;  ৮ সেমিতেই পড়া যায়।
  ph_growatt    Growatt MOD 4000TL3-X গ্রিড-টাই ইনভার্টারের গায়ের
                ডেটা প্লেট।  অন-গ্রিড ইনভার্টারের প্রতিটি ঘর —
                DC ইনপুট রেঞ্জ, MPPT সংখ্যা, AC আউটপুট — আসল
                যন্ত্রের গা থেকে পড়ানো যায়।
  ph_label      ওই একই ছবির স্টিকারটুকু কেটে বড় করে —  Phaesun
                Sun Plus 165 P:  Pmax 165 Wp, Vmp 19.4 V, Imp 8.51 A,
                Voc 23.5 V, Isc 8.80 A, সহনশীলতা +/-3 %, সর্বোচ্চ
                সিস্টেম ভোল্টেজ 1000 V, কাজের তাপমাত্রা -40 থেকে
                +85, আর নিচে লেখা "Certified according CEI/IEC 61215
                and CEI/IEC 61730" — নেট মিটারিং নির্দেশিকা-২০২৫
                যে দুটি স্ট্যান্ডার্ড বাধ্যতামূলক করেছে, ঠিক সেই
                দুটি।  ১৬.৩ পুরোটাই এই স্টিকার পড়া।  ছোট টুকরো,
                তাই ২৫৬০ চওড়া থাম্ব থেকে কাটা।
  ph_mc4        MC4 কানেক্টরের সামনে ও উপর থেকে (CC0)।  ছবির
                বর্ণনাতেই লেখা আছে কোনটা পুরুষ আর কোনটা মেয়ে —
                এটি গুরুত্বপূর্ণ, কারণ সোলারে **উল্টো**:  পজিটিভ
                কেবলের মাথায় মেয়ে খোল, ভেতরে পুরুষ পিন।

  ph_array      সিরিজে জোড়া চারটি মনোক্রিস্টালাইন প্যানেল (হোমস,
                সিরিয়া) — ছবির নিজের বর্ণনায় লেখা "connected in
                series ... optimized for a hybrid MPPT charge
                controller", অর্থাৎ ১৬.৪-এর স্ট্রিং ঠিক এটাই।
  ph_install    ছাদে বসানোর কাজ চলছে — মাউন্টিং স্ট্রাকচার ও
                কাত করে বসানোর ছবি।

চালানোর নিয়ম:  python assets_ch16.py     (Book/build/ থেকে)
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
OUT = os.path.join(HERE, "assets", "ch16")
CACHE = os.path.join(HERE, ".commons")
os.makedirs(OUT, exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

UA = {"User-Agent": "rapti-book/1.0 (textbook figure prep)"}
API = "https://commons.wikimedia.org/w/api.php"

# নাম → (কমন্সের ফাইলনাম, প্রত্যাশিত মাপ, ক্রপ-বক্স ভগ্নাংশে,
#        সর্বোচ্চ চওড়া, কনট্রাস্ট, ঘূর্ণন ডিগ্রিতে, থাম্বের চওড়া)
# ঘূর্ণন **আগে** হয়, ক্রপ **পরে** — তাই ক্রপ-বক্সটা ঘোরানো ছবির হিসাবে।
# শেষ ঘরটি ঐচ্ছিক:  ছবির ছোট একটি টুকরো কেটে বড় করে বসাতে হলে
# ১২৮০-র বদলে বড় থাম্ব লাগে (ph_label — স্পেসিফিকেশন স্টিকার)।
PHOTOS = {
    "ph_roof_bd":   ("Solar on the Rooftop (18868464374).jpg",
                     (4672, 2628), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
    "ph_hatil":     ("Hatil rooftop solar panels.jpg",
                     (4032, 3024), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
    "ph_back":      ("165W solar panel, back.jpg",
                     (3000, 4000), (0.0, 0.0, 1.0, 1.0), 1280, 1.06, 0),
    "ph_jbox":      ("Solar panel junction box.jpg",
                     (4000, 3000), (0.0, 0.0, 1.0, 1.0), 1280, 1.06, 0),
    "ph_jbox_open": ("Junction box of solar panel.JPG",
                     (2350, 2190), (0.0, 0.0, 1.0, 1.0), 1280, 1.06, 0),
    "ph_edge":      ("Edge and termination of a PV module.jpg",
                     (1230, 803), (0.0, 0.0, 1.0, 1.0), 1230, 1.04, 0),
    "ph_growatt":   ("Growatt MOD 4000TL3-X inverter data sheet.jpg",
                     (3456, 5184), (0.0, 0.0, 1.0, 1.0), 1280, 1.08, 0),
    "ph_label":     ("165W solar panel, back.jpg",
                     (3000, 4000), (0.700, 0.113, 1.000, 0.452), 1700,
                     1.12, 0, 2560),
    # কেবল উপরের সারি — সামনের দুই মুখ, যেখানে + ও - চিহ্ন আর
    # ভেতরের সকেট-পিনের পার্থক্য দেখা যায়।  পুরো ছবিটা ২ x ২ গ্রিড,
    # অত লম্বা ছবি পাতায় বসালে প্রায় ১২ সেমি খেয়ে ফেলে।
    "ph_mc4":       ("MC4 Connector Front and Top View.jpg",
                     (2985, 4599), (0.02, 0.005, 0.98, 0.40), 1280,
                     1.06, 0),
    "ph_array":     ("Residential rooftop photovoltaic array of four "
                     "panels in Syria.jpg",
                     (4608, 3456), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
    "ph_install":   ("Solar Installation in Kenya.jpg",
                     (3024, 4032), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
}

# নাম → কোন অধ্যায়ের ফোল্ডার থেকে;  ছবি আর কৃতজ্ঞতা একসঙ্গে আসে
REUSE = {}


def _get(url):
    for _ in range(9):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=300).read()
        except Exception as exc:                 # ৪২৯ এলে থেমে আবার চেষ্টা
            print("   … আবার চেষ্টা:", exc, flush=True)
            time.sleep(30)
    raise SystemExit("✗ নামানো গেল না: " + url)


# কমন্সের নিজস্ব নিয়ম — মূল ফাইল বারবার টানলে ৪২৯, আর থাম্বের চওড়াও
# তাদের তালিকার মাপ হতে হয় (নইলে ৪০০:  "Use thumbnail sizes listed
# on https://w.wiki/GHai")।  ১২৮০ ওই তালিকার একটি মাপ।
THUMB_W = 1280


def _meta(fname, thumb=None):
    """কমন্সের ফাইলনাম → থাম্বের URL, আসল মাপ, শিরোনাম, লেখক, লাইসেন্স।
    একই ফাইল দুই মাপে লাগতে পারে, তাই ক্যাশের চাবিতে মাপও আছে।"""
    thumb = thumb or THUMB_W
    cache = os.path.join(CACHE, "ch16_meta.json")
    db = json.load(open(cache)) if os.path.exists(cache) else {}
    key = f"{fname}@{thumb}"
    if key not in db:
        q = urllib.parse.urlencode({
            "action": "query", "format": "json", "titles": "File:" + fname,
            "prop": "imageinfo", "iiprop": "url|size|extmetadata",
            "iiurlwidth": thumb})
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

        db[key] = {"url": info.get("thumburl") or info["url"],
                     "size": [info["width"], info["height"]],
                     "title": field("ObjectName"), "author": field("Artist"),
                     "licence": field("LicenseShortName")}
        json.dump(db, open(cache, "w"), ensure_ascii=False, indent=1)
        time.sleep(6)
    return db[key]


def fetch(fname, thumb=None):
    """ডাউনলোড করে ক্যাশে রাখা — বারবার কমন্সে হিট করলে ৪২৯ আসে।"""
    thumb = thumb or THUMB_W
    fn = os.path.join(CACHE,
                      f"ch16_{thumb}_" + re.sub(r"[^\w.-]", "_", fname))
    if not os.path.exists(fn) or os.path.getsize(fn) < 4096:
        open(fn, "wb").write(_get(_meta(fname, thumb)["url"]))
        time.sleep(6)
    return open(fn, "rb").read()


def main():
    credits = {}
    for name, spec in PHOTOS.items():
        fname, size, box, wmax, contrast, rot = spec[:6]
        thumb = spec[6] if len(spec) > 6 else THUMB_W
        m = _meta(fname, thumb)
        if tuple(m["size"]) != size:
            raise SystemExit(f"✗ {name}: {fname}-এর মাপ {tuple(m['size'])}, "
                             f"হওয়ার কথা {size} — কমন্সে ছবিটি বদলেছে, "
                             f"ক্রপ-বক্স আবার মিলিয়ে নিতে হবে")
        im = ImageOps.exif_transpose(
            Image.open(io.BytesIO(fetch(fname, thumb)))).convert("RGB")
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
        print(f"✓ {name:14s} {str(im.size):12s} {m['licence']:14s} {fname}",
              flush=True)

    for name, src in REUSE.items():
        d = os.path.join(HERE, "assets", src)
        shutil.copy(os.path.join(d, name + ".jpg"), OUT)
        credits[name] = json.load(open(os.path.join(d, "credits.json"),
                                       encoding="utf-8"))[name]
        print(f"✓ {name:14s} (অধ্যায় {src[2:]} থেকে)", flush=True)

    json.dump(credits, open(os.path.join(OUT, "credits.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n✓ credits.json —", len(credits), "টি ছবি")


if __name__ == "__main__":
    main()
