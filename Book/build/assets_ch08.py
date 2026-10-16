# -*- coding: utf-8 -*-
"""অধ্যায় ৮-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**।  ইনস্টিটিউটের কোনো ফাইলে কন্টাক্টরের ছবি
নেই (`../HW All`-এর দুটো ডেকেই খুঁজে দেখা হয়েছে; অধ্যায় ২০-এর জন্য
নামানো `JLC1-D09-10.jpg`-ই একমাত্র কন্টাক্টরের ছবি ছিল, আর সেটি
শুধু বাইরের চেহারা দেখায়)।

এই অধ্যায়ের ভার যে ছবিগুলো টানে:

  ph_exploded   গোটা কন্টাক্টর খুলে ফেলা — কয়েল, কুলাটা (স্থির কোর),
      আর্মেচার, রিটার্ন স্প্রিং, মেইন ও অক্সিলিয়ারি কন্টাক্ট, সবগুলো
      এক ফ্রেমে ছড়ানো।  ভেতরে কী আছে তার গোটা পাঠটা এই এক ছবিতে।
      মূল ছবির স্প্যানিশ লেবেলগুলো `dia_ch08.py` বাংলা পটি দিয়ে
      ঢেকে দেয় — ছবিটি CC0, বদলানোয় বাধা নেই।
  ph_contactor  IEK KMИ-11810 — টার্মিনালের ছাপা নম্বর (1/L1 3/L2 5/L3,
      2/T1 4/T2 6/T3, 13-14, A1-A2) খালি চোখেই পড়া যায়।  ৮.৪-এর
      টার্মিনাল-মানচিত্র এই ছবির উপরেই বসানো।
  ph_modular    CHiNT NCH8-63 — মডুলার (হাউসহোল্ড) কন্টাক্টর, DIN
      রেলে বসে।  গায়ে IEC 61095 লেখা, AC-3 নয় AC-7a — অর্থাৎ এটি
      মোটরের কন্টাক্টর নয়।  বাজারে এই ভুলটাই সবচেয়ে বেশি হয়, তাই
      ছবিটি ইচ্ছে করে রাখা।
  ph_starter    বাস্তবে বসানো একটি DOL স্টার্টারের ভেতর — উপরে
      ওভারলোড রিলে (২০-৩২ A ডায়াল), নিচে MAHENDRA 25A-440V-AC
      কন্টাক্টর।  উপমহাদেশের বাজারে জিনিসটা ঠিক এভাবেই দেখায়।
  ph_burn       পুড়ে যাওয়া মেইন কন্টাক্ট — ৮.১১-এর ত্রুটির ছক
      এই ছবির উপরেই দাঁড়ানো।

সব ছবিরই কৃতজ্ঞতা `credits.json`-এ লেখা হয়, আর সেটি কমন্সের নিজের
extmetadata থেকে আসে — হাতে টোকা নয়, তাই লেখক বা লাইসেন্স ভুল হওয়ার
সুযোগ নেই।  CC BY ও CC BY-SA-তে কৃতজ্ঞতা স্বীকার আইনি শর্ত।

চালানোর নিয়ম:  python assets_ch08.py     (Book/build/ থেকে)
"""
import io
import json
import os
import re
import time
import urllib.parse
import urllib.request

from PIL import Image, ImageEnhance, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "ch08")
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
    # ── ভেতরের গঠন ─────────────────────────────────────────────────
    # খুলে ফেলা কন্টাক্টর (Telemecanique LC1 D09)।  স্প্যানিশ লেবেল
    # ছবির গায়েই আছে; ক্রপ পুরোটাই রাখে, বাংলা পটি ছবির উপরে বসে।
    "ph_exploded":  ("Despiece contactor.jpg",
                     (1192, 709), (0.000, 0.000, 1.000, 1.000), 1192, 1.04, 0),
    # খোলা ফ্রেমের পুরনো কন্টাক্টর — E-কোর, কয়েল আর আর্মেচার খোলা চোখে
    "ph_frame":     ("Stycznik przemyslowy.jpg",
                     (1276, 1696), (0.040, 0.020, 0.965, 0.900), 1100, 1.06, 0),
    # মুভিং কন্টাক্ট ব্রিজ — দুই প্রান্তে রুপোর টিপ
    "ph_bridge":    ("Schützkontakt 1.jpg",
                     (1404, 1578), (0.030, 0.080, 0.975, 0.930), 1000, 1.05, 0),
    # ব্রিজ ও স্থির কন্টাক্ট একসঙ্গে, সিরামিক আর্ক-চেম্বারসহ
    "ph_contacts":  ("Schützkontakt 2.jpg",
                     (3275, 2183), (0.030, 0.060, 0.975, 0.960), 1400, 1.05, 0),

    # ── বাইরের চেহারা ও টার্মিনাল ───────────────────────────────────
    # IEK KMИ-11810 — সব টার্মিনাল-নম্বর পড়া যায়
    "ph_contactor": ("Contactor DIN IEK.jpg",
                     (2113, 2505), (0.115, 0.095, 0.870, 0.815), 1500, 1.05, 0),
    # CHiNT NCH8-63 — মডুলার, IEC 61095, চার পোলই NO
    "ph_modular":   ("Contactor NCH8-63.JPG",
                     (2560, 1920), (0.280, 0.080, 0.720, 0.960), 1200, 1.10, 0),

    # ── প্যানেলে বসানো অবস্থায় ─────────────────────────────────────
    # DOL স্টার্টারের ভেতর — উপরে ওভারলোড রিলে, নিচে কন্টাক্টর
    "ph_starter":   ("Inside 3 phase motor starter.jpg",
                     (3000, 4000), (0.045, 0.020, 0.960, 0.960), 1200, 1.08, 0),

    # ── কন্ট্রোল ডিভাইস ────────────────────────────────────────────
    # সবুজ স্টার্ট পুশ বাটন — সঙ্গে পেছনের কন্টাক্ট ব্লক
    "ph_pb_green":  ("Push button switch Green.jpg",
                     (3024, 4032), (0.150, 0.250, 0.880, 0.790), 1100, 1.06, 0),
    # লাল স্টপ বাটন — গায়ে রেটিং ছাপা
    "ph_pb_red":    ("Push button switch.jpg",
                     (1654, 1335), (0.020, 0.030, 0.980, 0.970), 1100, 1.05, 0),
    # অ্যাকচুয়েটর আর কন্টাক্ট ব্লক আলাদা — দুই টুকরোর গড়ন
    "ph_pb_parts":  ("Push button switch PB switch.jpg",
                     (3024, 4032), (0.130, 0.300, 0.900, 0.700), 1300, 1.06, 0),
    # প্যানেলের গায়ে বসানো রোটারি সিলেক্টর সুইচ
    "ph_sel":       ("Selector switch.jpg",
                     (2448, 3264), (0.150, 0.150, 0.880, 0.900), 1100, 1.05, 0),
    # সিলেক্টর সুইচের পেছন — দুই তলা কন্টাক্ট ব্লক, নম্বরসহ
    "ph_sel_back":  ("Selector switch DPDT.jpg",
                     (3024, 4032), (0.200, 0.150, 0.930, 0.880), 1200, 1.06, 0),
    # ইমার্জেন্সি স্টপ — মাশরুম মাথা, ঘুরিয়ে ছাড়াতে হয়
    "ph_estop":     ("Not-Aus Betätiger.jpg",
                     (2580, 1932), (0.120, 0.060, 0.900, 0.960), 1100, 1.05, 0),

    # ── ত্রুটি ─────────────────────────────────────────────────────
    # পুড়ে যাওয়া মেইন কন্টাক্ট, দুই কোণ থেকে
    "ph_burn":      ("Burned Contactor-01ASD.jpg",
                     (3468, 4624), (0.060, 0.230, 0.960, 0.780), 1400, 1.05, 0),
    "ph_burn2":     ("Burned Contactor-02ASD.jpg",
                     (3468, 4624), (0.060, 0.230, 0.960, 0.780), 1400, 1.05, 0),
    # রুপোর কন্টাক্টে আর্ক-ক্ষয় — ছোট ছবি, ছোট মাপেই বসবে
    "ph_erosion":   ("Silver contacts arc erosion failure.jpg",
                     (403, 403), (0.020, 0.020, 0.980, 0.980), 403, 1.12, 0),
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


# ছবি এত বড়ই নামানো হয়।  সব ক্রপের `wmax` এর চেয়ে ছোট, তাই আসল
# ফাইল টানার দরকার নেই — কমন্স নিজেই মূল ফাইলের বদলে থাম্বনেইল
# ব্যবহার করতে বলে, আর আসল ফাইল বারবার টানলে ৪২৯ দেয়।
THUMB_W = 1700


def _meta(fname):
    """কমন্সের ফাইলনাম → থাম্বের URL, আসল মাপ, শিরোনাম, লেখক, লাইসেন্স।"""
    cache = os.path.join(CACHE, "ch08_meta.json")
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
    fn = os.path.join(CACHE, "ch08_" + re.sub(r"[^\w.-]", "_", fname))
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

    json.dump(credits, open(os.path.join(OUT, "credits.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n✓ credits.json —", len(credits), "টি ছবি")


if __name__ == "__main__":
    main()
