# -*- coding: utf-8 -*-
"""অধ্যায় ১৭-এর আলোকচিত্র প্রস্তুত করা।

উৎস — **উইকিমিডিয়া কমন্স**, অধ্যায় ৮–১৬-এর মতোই।  ডাউনলোডারটি
`assets_ch16.py`-র কপি (সবচেয়ে নতুনটি — প্রতি-ছবি থাম্বের চওড়া নেওয়া
যায়, আর মেটাডেটার ক্যাশের চাবিতে মাপও থাকে);  বদলেছে কেবল ছবির তালিকা।

এই অধ্যায়ে কমন্স ভালোই উদার — নজরদারি ক্যামেরার ছবি প্রচুর।  সমস্যা
উল্টোটা:  বেশির ভাগই রাস্তার খুঁটিতে বসানো ক্যামেরার দূর থেকে তোলা ছবি,
যেখান থেকে শেখার কিছু নেই।  যেগুলো রাখা হয়েছে, সবগুলোই কোনো-না-কোনো
অনুচ্ছেদের কাজে লাগে:

  ph_types      বুলেট আর ভ্যান্ডাল ডোম — একই ছবিতে দুটো, তাই ১৭.৩-এর
                ধরন-ভেদ শুরু করার জন্য আদর্শ।
  ph_ptz        PTZ ক্যামেরা — ঘোরানো-কাত করা-জুম করার মাথাটি স্পষ্ট।
  ph_sign       দোকানের বাইরে ভ্যান্ডাল ডোম, আর পাশেই "নজরদারি চলছে"
                লেখা সাইনবোর্ড।  ১৭.১২-এর নোটিশ দেওয়ার কথাটি এই
                ছবিতেই দেখানো যায়।
  ph_pole       খুঁটিতে একাধিক ক্যামেরা — মাউন্টিং ও ঢাকনার ব্যবস্থা।
  ph_cpplus     CP Plus ডোম ক্যামেরা, বেঙ্গালুরুতে তোলা — ভেতরের
                IR LED-র পুরো বলয়টি স্পষ্ট, তাই ১৭.৫-এর নাইট ভিশনের
                আলোচনায় এটিই ব্যবহার হয়েছে।  দক্ষিণ এশিয়ার বাজারে
                সত্যিই বিক্রি হয়, এমন ব্র্যান্ড।
  ph_inside     খোলা বক্স ক্যামেরার ভেতর — পাওয়ার বোর্ড, BNC বসানো
                মেইন বোর্ড, অটো-আইরিসের তারসহ ভ্যারিফোকাল লেন্স আর
                সেন্সর বোর্ড, চারটিই একসঙ্গে।
  ph_lens       M12 x 0.5 মাউন্টের তিনটি লেন্স — ১৬ mm, ৬ mm ও ৮ mm।
                Dahua-র IPC-HFW1230S-S5-এর ডেটাশিটেও "Lens Mount M12"
                লেখা, অর্থাৎ ছবির জিনিসটাই বাজারের জিনিস।  ১৭.৪-এর
                ফোকাল লেংথ বনাম দৃশ্যকোণের আলোচনা এই ছবি ধরে।

  ph_nvr        Annke-র PoE NVR — সামনের দিক।
  ph_nvr_back   একই NVR-এর **পিছনের প্যানেল** — এই অধ্যায়ের সবচেয়ে
                কাজের ছবি।  PoE পোর্টের সারি, আলাদা LAN পোর্ট, HDMI,
                VGA, USB আর DC ইনপুট একসঙ্গে দেখা যায়, অর্থাৎ ১৭.৬-এর
                পুরো সংযোগ-তালিকাটি আসল যন্ত্রের গা থেকে পড়ানো যায়।
  ph_nvr_ports  ওই একই ছবির পোর্ট-সারিটুকু কেটে বড় করে — গায়ের লেখা
                পড়ার জন্য (ch16-এর ph_label-এর কায়দা)।
  ph_hdd        3.5 ইঞ্চি SATA হার্ড ডিস্ক (WD40EFRX, 4 TB) — ১৭.৯-এর
                স্টোরেজ হিসাবের সঙ্গে।
  ph_ctrl       ১৫টি মনিটরে ১৭৬টি ক্যামেরা দেখার কন্ট্রোল রুম — ছবির
                নিজের বর্ণনায় সংখ্যা দুটি লেখা আছে, আর সেটাই ১৭.১০-এর
                "সব ক্যামেরা একসঙ্গে দেখা যায় না" কথাটির প্রমাণ।

  ph_bnc        BNC কানেক্টর (পাবলিক ডোমেইন) — কোঅক্সের মাথা।
  ph_coax       কোঅক্সিয়াল ক্যাবলের প্রস্থচ্ছেদ (LMR-195)।  ভেতরের
                পরিবাহী, ডাইইলেকট্রিক, ব্রেইড ও শিথ — চারটি স্তরই
                আলাদা করে চেনা যায়।  BNBC ১.৩.৪০.১-এ কোঅক্সের
                যে গঠন লেখা আছে, ছবিটি ঠিক তা-ই দেখায়।
  ph_rj45       Cat 6 কেবল লাগানো RJ45 সকেট, TIA-568B ক্রমে।
  ph_poe_sw     Cisco SG 200-08P — PoE সুইচের সামনের দিক।
  ph_rack       ১৯ ইঞ্চি র‍্যাকে সুইচ ও প্যাচ প্যানেল, Cat 6 প্যাচ
                কর্ড দিয়ে জোড়া — BNBC ১.৩.৪১-এর প্যাচ প্যানেলের কথা।

বাতিল করা ফাইল — কারণসহ
────────────────────────
  "CCTV Surveillance Notice bn.svg" (CC0)।  ফাইলনামে `bn`, অর্থাৎ
  বাংলা হওয়ার কথা।  কিন্তু কমন্সে ফাইলটির **নিজের বর্ণনায় লেখা**
  "SVG vector version of the CCTV Surveillance Notice sign in
  *Hindi*", আর ভেতরের লেখাটুকু স্থানীয়ভাবে রেন্ডার করেও পড়া গেল না
  (ফন্ট বাইরে থেকে আসে)।  কোন ভাষার সাইন তা নিশ্চিত না হয়ে ক্যাপশন
  লেখা যায় না — অধ্যায় ১১-এর CT আর অধ্যায় ১৬-এর "চার্জ কন্ট্রোলার"
  ছবির শিক্ষাই এখানে খাটে।  বদলে ph_sign নেওয়া হয়েছে, আর বাংলা
  নোটিশটি `dia_ch17.py`-তে নিজে আঁকা হয়েছে, যেখানে লেখাটা আমাদের
  নিয়ন্ত্রণে।

  "Coaxial cable.JPG"।  দেখতে কোঅক্সের প্রস্থচ্ছেদ, কিন্তু ছবির নিজের
  বর্ণনায় লেখা "High voltage power cable" — অর্থাৎ জিনিসটা কোঅক্স
  নয়।  ph_coax (LMR-195) নেওয়া হয়েছে, যার বর্ণনা ও চেহারা মেলে।

  "Planet Technology WGS-4215-8P2S"।  PoE সুইচের ভালো ছবি, কিন্তু
  বর্ণনা পুরোটাই চীনা হরফে — কালপুরুষে CJK গ্লিফ নেই, কৃতজ্ঞতার
  তালিকায় বাক্স হয়ে উঠত (অধ্যায় ১০-এর শিক্ষা)।  Cisco SG 200-08P
  নেওয়া হয়েছে, যার বর্ণনা ল্যাটিন হরফে।

চালানোর নিয়ম:  python assets_ch17.py     (Book/build/ থেকে)
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
OUT = os.path.join(HERE, "assets", "ch17")
CACHE = os.path.join(HERE, ".commons")
os.makedirs(OUT, exist_ok=True)
os.makedirs(CACHE, exist_ok=True)

UA = {"User-Agent": "rapti-book/1.0 (textbook figure prep)"}
API = "https://commons.wikimedia.org/w/api.php"

# নাম → (কমন্সের ফাইলনাম, প্রত্যাশিত মাপ, ক্রপ-বক্স ভগ্নাংশে,
#        সর্বোচ্চ চওড়া, কনট্রাস্ট, ঘূর্ণন ডিগ্রিতে, থাম্বের চওড়া)
# ঘূর্ণন **আগে** হয়, ক্রপ **পরে** — তাই ক্রপ-বক্সটা ঘোরানো ছবির হিসাবে।
# শেষ ঘরটি ঐচ্ছিক:  ছবির ছোট একটি টুকরো কেটে বড় করে বসাতে হলে
# ১২৮০-র বদলে বড় থাম্ব লাগে (ph_nvr_ports — পিছনের প্যানেলের সারি)।
PHOTOS = {
    # ── ক্যামেরা ────────────────────────────────────────────────
    "ph_types":     ("Bullet camera and Vandal Dome camera.jpg",
                     (3024, 4032), (0.0, 0.08, 1.0, 0.92), 1280, 1.06, 0),
    "ph_ptz":       ("PTZ (Pan Tilt Zoom) security camera.jpg",
                     (3024, 4032), (0.0, 0.10, 1.0, 0.90), 1280, 1.06, 0),
    "ph_sign":      ("Vandal dome-style security camera next to signage "
                     "on exterior of Target store.jpg",
                     (3059, 2127), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
    "ph_pole":      ("2020-04-05 17.18.01 Pole with surveillance cameras "
                     "in Saarbrücken.jpg",
                     (3456, 4608), (0.05, 0.02, 0.95, 0.62), 1280, 1.06, 0),
    "ph_cpplus":    ("CP Plus CCTV camera.jpg",
                     (1072, 1072), (0.0, 0.0, 1.0, 1.0), 1072, 1.06, 0),
    # মূল ফাইলটি পাঁচটি ছবির কোলাজ;  সবচেয়ে কাজেরটি নিচেরটি —
    # পাওয়ার বোর্ড, BNC-সহ মেইন বোর্ড, ভ্যারিফোকাল লেন্স আর সেন্সর
    # বোর্ড একসঙ্গে।  অধ্যায় ৯-এর কোলাজ-কাটার নিয়ম।
    "ph_inside":    ("Inside of an EverFocus CCTV camera 20110115.jpg",
                     (639, 900), (0.08, 0.53, 0.97, 1.0), 639, 1.08, 0),
    "ph_lens":      ("Three M12 lenses for board or CCTV cameras.jpg",
                     (4000, 2396), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),

    # ── রেকর্ডার ও স্টোরেজ ─────────────────────────────────────
    "ph_nvr":       ("Annke PoE Network Video Recorder (NVR).jpg",
                     (2000, 1500), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
    # উপরে-নিচে অনেকটা ফাঁকা সাদা;  প্যানেলটুকুই রাখা হয়েছে।
    "ph_nvr_back":  ("Annke PoE Network Video Recorder (NVR), back.jpg",
                     (2000, 1500), (0.0, 0.25, 1.0, 0.76), 1280, 1.05, 0),
    # পিছনের প্যানেলের পোর্ট-সারিটুকু — গায়ের লেখা পড়ার জন্য।
    "ph_nvr_ports": ("Annke PoE Network Video Recorder (NVR), back.jpg",
                     (2000, 1500), (0.06, 0.30, 0.97, 0.72), 1600,
                     1.14, 0, 2000),
    "ph_hdd":       ("Western Digital \"Red\" 4 TB SATA NAS-optimized "
                     "3.5-inch HDD.jpg",
                     (1024, 768), (0.0, 0.0, 1.0, 1.0), 1024, 1.06, 0),
    "ph_ctrl":      ("CCTV control room monitor wall.jpg",
                     (1217, 500), (0.0, 0.0, 1.0, 1.0), 1217, 1.06, 0),

    # ── তার, কানেক্টর ও নেটওয়ার্ক ──────────────────────────────
    "ph_bnc":       ("BNC connector 20050720 001.jpg",
                     (2272, 1704), (0.0, 0.05, 1.0, 0.95), 1280, 1.05, 0),
    "ph_coax":      ("Cross section of an LMR-195 coaxial cable.jpg",
                     (4032, 3024), (0.10, 0.10, 0.90, 0.90), 1280, 1.08, 0),
    "ph_rj45":      ("Ethernet socket with two cables connected "
                     "(TIA-568B) (CAT6).jpg",
                     (3024, 4032), (0.0, 0.12, 1.0, 0.88), 1280, 1.05, 0),
    "ph_poe_sw":    ("Cisco SG 200-08P front.jpg",
                     (4128, 2322), (0.0, 0.0, 1.0, 1.0), 1280, 1.06, 0),
    "ph_rack":      ("19-inch rackmount Ethernet switches and "
                     "patch panels.jpg",
                     (1280, 960), (0.0, 0.0, 1.0, 1.0), 1280, 1.05, 0),
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
    cache = os.path.join(CACHE, "ch17_meta.json")
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
                      f"ch17_{thumb}_" + re.sub(r"[^\w.-]", "_", fname))
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
