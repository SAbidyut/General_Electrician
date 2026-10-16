# CLAUDE.md

## Purpose

Authoring an original **Bangla textbook: "জেনারেল ইলেকট্রিশিয়ান" (General
Electrician)** for Resonance Automation Professional Training Institute
(RAPTI) — a second, separate book from the "ইলেকট্রিক্যাল হাউস ওয়্যারিং"
project. **This is a sibling project, not a continuation.** The house-wiring
book's own project lives at `../HW All` (its own git repo, its own CLAUDE.md)
and is not touched from here — if the user needs to edit the house-wiring
book they work in that folder, not this one. This folder was set up on
2026-09-14 by copying the house-wiring book's engine and conventions across
so the two books share one visual identity, one DOCX/SVG toolchain, and one
set of house-style rules; the *content* is new and chapter-by-chapter from
here on.

Delivered **one chapter at a time as a .docx**, built by the same Python
pipeline as the house-wiring book. The user is the institute's course
developer and reviews each chapter before the next is started.

## Status

The user supplied this 17-chapter syllabus verbatim on 2026-09-14. Nine
chapters overlapped in subject with chapters already built for the
house-wiring book; those nine were **adapted and delivered on 2026-09-14**
rather than rebuilt from scratch (renumbered, cross-references fixed — see
"Reused-content — how the nine adapted chapters were done" below for exactly
what changed). The remaining eight have no house-wiring equivalent and are
still unstarted.

| Ch | Title | Scope (user's own bullets) | Source | State |
|---|---|---|---|---|
| 01 | কর্মক্ষেত্রে নিরাপত্তা | নিরাপত্তার গুরুত্ব · দুর্ঘটনার কারণ ও প্রতিকার · নিরাপত্তা বিধি · সতর্কতা · PPE · ফার্স্ট এইড | = HW ch01 (same number, same scope) | ✅ delivered — 32 pp, 13/12 figures/tables |
| 02 | ইলেকট্রিক্যাল টুলস | হ্যান্ড টুলস · পাওয়ার টুলস · রক্ষণাবেক্ষণ ও নিরাপদ ব্যবহার | = HW ch02 (same number, same scope) | ✅ delivered — 23 pp, 15/13 |
| 03 | ইলেকট্রিসিটি বা বিদ্যুৎ | ইলেকট্রিসিটি · ইলেকট্রন · কারেন্ট · ভোল্টেজ · রেজিস্ট্যান্স · পাওয়ার · এনার্জি · ফ্রিকুয়েন্সি | ← HW ch04, renumbered 4→3 | ✅ delivered — 21 pp, 8/10, one pre-existing 4.78 cm gap (p9, inherited from HW) |
| 04 | ইলেকট্রিক্যাল সার্কিট | সংজ্ঞা · প্রকারভেদ · সিরিজ/প্যারালাল বৈশিষ্ট্য · ৩ লোড সিরিজ/প্যারালাল যাচাই (ব্যবহারিক) · মিশ্র সার্কিট যাচাই | ← HW ch07, renumbered 7→4 (its own §৭.৯ practical work was already exactly this chapter's three named exercises — no need to reach into HW ch03) | ✅ delivered — 24 pp, 10/9, zero gaps |
| 05 | মেজারিং ইন্সট্রুম্যান্ট | পরিচিতি · প্রকারভেদ ও ব্যবহার · V/I/R পরিমাপ পদ্ধতি · অ্যামিটার-ভোল্টমিটার সংযোগ | ← HW ch08, renumbered 8→5 | ✅ delivered — 21 pp, 11/8, zero gaps |
| 06 | পাওয়ার ফরমুলা | সিঙ্গেল/থ্রি-ফেজ · A/V/W সূত্র · ক্যালকুলেশন | ← HW ch16, renumbered 16→6 | ✅ delivered — 20 pp, 6/7, one 4.56 cm gap (p11, pre-existing) |
| 07 | মটর | DP সুইচে মটর সংযোগ · মটরের অ্যাম্পিয়ার ক্যালকুলেশন · কয়েল ও ক্যাপাসিটর পরিচিতি · ক্যাপাসিটর ক্যালকুলেশন ও সংযোগ | ← HW ch18, renumbered 18→7 | ✅ delivered — 27 pp, 9/10, zero gaps |
| 08 | ম্যাগনেটিক কন্টাক্টর | পরিচিতি ও কাজ · সিলেক্টর সুইচ + কন্টাক্টর দিয়ে লোড কন্ট্রোল · পুশ বাটন + কন্টাক্টর দিয়ে লেচিং সার্কিট | none — written from scratch; photos from Wikimedia Commons | ✅ delivered — 34 pp, 19/10, zero gaps |
| 09 | DOL Starter | কী ও কেন · ওভারলোড রিলে পরিচিতি ও ক্যালকুলেশন · রিলে+স্টার্টার দিয়ে লোড কন্ট্রোল | none — written from scratch; photos from Wikimedia Commons | ✅ delivered — 33 pp, 17/10, zero gaps |
| 10 | টাইমার | টাইমার আলোচনা · টাইমার লজিকে লোড কন্ট্রোল · Automatic Motor Off/Stop | none — written from scratch; photos from Wikimedia Commons | ✅ delivered — 27 pp, 16/9, zero gaps |
| 11 | ATS | পরিচিতি · কন্ট্রোল+পাওয়ার সার্কিট দিয়ে লোড কন্ট্রোল · প্যানেল মিটার সংযোগ | none — written from scratch; photos from Wikimedia Commons | ✅ delivered — 30 pp, 15/10, zero gaps |
| 12 | Forward-Reverse Starter | আলোচনা · কন্ট্রোল সার্কিট সংযোগ · পাওয়ার সার্কিট দিয়ে মটর কন্ট্রোল | none — written from scratch; one new photo from Wikimedia Commons, rest reused from ch08 | ✅ delivered — 27 pp, 13/8, zero gaps |
| 13 | ফ্লোট সুইচ | পরিচিতি ও কাজ · সংযোগ · সিঙ্গেল/ডাবল কন্ডিশন অটো-মেনুয়াল | ← HW ch20, renumbered 20→13 | ✅ delivered — 24 pp, 13/10, zero gaps |
| 14 | Star-Delta Starter | আলোচনা · কন্ট্রোল সার্কিট সংযোগ · পাওয়ার সার্কিট দিয়ে মটর কন্ট্রোল | none — written from scratch; ch07's ৭.১০ introduces the terminal-box side, one new photo from Wikimedia Commons, rest reused from ch08/09/10 | ✅ delivered — 35 pp, 19/9, zero gaps |
| 15 | বাসবার | ব্যবহার · ক্যালকুলেশন · Star-Delta ব্যবহার করে মটর কন্ট্রোল প্র্যাকটিস | ← HW ch21, renumbered 21→15 | ✅ delivered — 29 pp, 14/6, zero gaps |
| 16 | Solar | পরিচিতি ও আলোচনা · ক্যালকুলেশন · ব্যাটারি ব্যাকআপ ক্যালকুলেশন · সংযোগ | none reused in the end — written from scratch off primary sources; `Solar System.docx` supplied the section order only | ✅ delivered — 48 pp, 20/18, zero gaps |
| 17 | CC Camera | পরিচিতি ও ক্যামেরার ধরন · NVR/DVR/POE/Video Balun ব্যবহার ও সংযোগ · CC ক্যামেরা সংযোগ | none — written from scratch off Dahua/Hikvision datasheets and BNBC; photos from Wikimedia Commons | ✅ delivered — 56 pp, 25/16, zero gaps |

**Legend:** ✅ delivered — `.docx` in `Book/`, preview PDF + SVG source in
`Book/অধ্যায়-NN/`, source in `Book/build/chNN.py` · ⏳ not started, no
house-wiring equivalent exists.

## Diagram marking & terminology pass, 2026-09-21 (partial — 6 of 17)

User reported three things in the diagrams: overlapping text, callout markings
that point at the wrong place, and technical terms translated too literally into
Bangla. **`qc.py` reported 0 problems on all 190 diagrams throughout** — it
measures text-box vs recorded-shape intersections, so it is structurally blind to
both real defects: a leader whose endpoint is geometrically fine but lands on the
wrong feature, and two leaders that cross (crossing lines produce no text
collision). Treat a clean `qc.py` as evidence about `qc.py`, not about the figure.

**Two cheap mechanical checks found everything**, and are worth re-running before
any future diagram delivery:

- **Sort-order invariant.** In `photo_callouts()` the label list is auto-spaced
  down one side, so a list *not* sorted by its target's `fy` forces the leaders to
  cross. A short script parsing `left=[…]/right=[…]` out of the `dia_*.py` sources
  and flagging non-monotonic `fy` found 4 real crossings in one pass
  (ch08 d09, ch11 d10, ch13 d02, ch15 d08). ch11 d10's is a false positive — five
  dial symbols at nearly equal `fy`, deliberately fanned.
- **Grid overlay + pixel sampling.** For callouts onto photographs, render the
  source photo with a 0.05 fractional grid and the current targets marked, then
  read the correct fraction off it. Wrong values were all round numbers
  (0.20, 0.58, 0.72); correct ones are not. Where a label names a colour, sample
  the pixel under the endpoint — that is how "নীল নিউট্রাল" was caught pointing at
  grey wall. Tool kept at `/tmp/.../gridcheck.py`; recreate it, it is ~30 lines.

**Fixed and delivered (ch08, 09, 13, 14, 15, 16 — rebuilt, `qc.py` clean,
page counts and gap sets unchanged: 34/33/24/35/29/48, zero gaps):**

- **ch08 d09_modular** — the worst of them. "কয়েল A1" pointed at terminal 5's
  screw, "কয়েল A2" and "আউটপুট 2 4 6 8" both at empty black shadow below the body,
  "IEC 61095" at the middle of the wiring schematic instead of the printed
  `IEC 61095 / EN 61095` line. All re-measured; IEC moved to the left column
  because its target is on the left.
- **ch08 d02_outside** — "নেমপ্লেট" pointed at blank grey moulding and
  "কয়েল A1 — উল্টো পাশে" at the nameplate text, i.e. the two were effectively
  swapped. Input/aux-13/output nudged onto their actual holes.
- **ch08 d04_inside** — five left-hand leaders scissoring. The file's own comment
  already said the order must follow target height; "পুশ রড" broke it and *cannot*
  be fixed by reordering (its target is far right but mid-height, so it crosses
  স্থির কন্টাক্ট or ক্যারিয়ার প্লেট in every arrangement). Moved to the right
  column. **স্থির কোর's label must stay at y=496** — raising it makes its leader
  cut through the coil's "A1" text, which `qc.py` *does* catch.
- **ch13 d02_parts**, **ch13 d08_contactor**, **ch15 d08_earth** — ordering fixed,
  targets re-measured onto real terminals/wires.
- **Over-translated terms** (the user's own example was ১৪.৩): **তারা-বিন্দু →
  নিউট্রাল পয়েন্ট** everywhere (17 hits across `ch14.py`/`dia_ch14.py`; the
  inflected forms তারা-বিন্দুর/-তে/-কে need their own replacements or you get
  "নিউট্রাল পয়েন্টর"). Also টার্মিনাল পট্টি → টার্মিনাল ব্লক, ঠেলা-দণ্ড → পুশ রড
  (ch09 d04), বর্তনী → সার্কিট in the ch08/ch16 diagram labels only (ch08 d10 had
  "কন্ট্রোল সার্কিট … আলাদা বর্তনী" in one sentence), খোলা-বর্তনী ভোল্টেজ →
  ওপেন সার্কিট ভোল্টেজ, চুম্বকীয় টান → ম্যাগনেটিক টান.
  **Left alone deliberately:** রোধ, বর্তনী and পাওয়ার ত্রিভুজ in ch01–ch06 — those
  are standard Bangla textbook terms, used consistently within the inherited
  chapters; the defect was mixing registers inside one figure, not the word.

**Not done — the user stopped the sweep here.** Chapters 10, 11, 12, 17 were
never reviewed, and only the photo-callout figures plus a handful of drawn ones
were checked in the six that were. Known-suspect, noted but unfixed:
**ch08 d14_wiring** and **ch14 d14_wiring** have wire crossings drawn with neither
a dot nor a hop (ch12's `hop_line()` convention exists for exactly this);
**ch08 d15_faults**'s "রুপোর টিপ ক্ষয়ে গেছে" points at copper rather than the
silver pad. Resume by running the sort-order script over all `dia_*.py` first.

## Editorial pass, 2026-09-21

User asked for (1) no cross-references to chapters the reader has not reached yet, and (2) prose that reads as human-written. Done in `chNN.py`, all 17 rebuilt, `layout.py` gap set unchanged (ch03 4.78 cm, ch06 4.56 cm only):

- **Forward chapter pointers removed or made self-standing** (ch03, 04, 07-11, 16); ch16's "অধ্যায় ১৯" and ch03's "পরিশিষ্ট ঘ" pointed at things that do not exist in this book. ch06's "অধ্যায় ৪-এ পাওয়ার" was wrong (power is ch03).
- **Stale house-wiring numbers fixed**: ch13 said চিত্র ২০.x, ch15 said সারণি/উদাহরণ/চিত্র ২১.x, ch07 said চিত্র ১৮.৮ - all now this book's own numbers. Lesson: renumbering must cover hard-typed `চিত্র/সারণি/উদাহরণ N.M` in prose, not only headings.
- **Source-slide talk removed** from ch13/ch15 prose ("ইনস্টিটিউটের পুরোনো স্লাইডে..."). ch12 spelled মটর, rest মোটর; now মোটর throughout (dia_ch12 regenerated).
- Prose: the book already had few connective tics. Reflexive "X নয়, Y" antitheses and a few chatty hooks (সুখবর/গল্প) were rewritten by hand. A mechanical em-dash-to-comma pass was tried and reverted - it made list/explanation dashes ambiguous.
- ch09 needed a small reorder-by-wording (E4 line kept at original length) to keep zero gaps.
- **Not done**: a line-by-line read of all ~1 MB of Bangla prose.

## Institute/hotline moved from header to footer, 2026-09-15

Same-day follow-up to the header work below: the user clarified that
"Resonance Automation" and the phone number belong in the **footer**, not
as a second header line — matching the merged house-wiring book's own
`mkbook.fill_footer()` exactly (`../HW All/Book/build/mkbook.py`), not
something new invented for this book. Fixed in `bookkit.py`:

- **Header is one line again**: book title (left) · `অধ্যায় N · chapter
  title` (centre) · `rapti.net` (right) — the institute/phone line that had
  been added below it is gone.
- **Footer is now three columns**, built by a new `Book._fill_footer()`
  helper applied to both `sec.footer` and `sec.first_page_footer` (so the
  chapter-opener page gets it too, since a per-chapter file has no separate
  "cover" section the way the merged book does): `Resonance Automation`
  (left, plain grey) · page number (centre, bold navy `PAGE` field) ·
  `01617-345534` (right) — same tab-stop-on-"Normal"-style technique as the
  header, same reason (the built-in `Header`/`Footer` style's own tab stops
  would otherwise merge with the paragraph's and misplace the columns).
  `INSTITUTE_SHORT = "Resonance Automation"` added next to the existing
  `WEB`/`PHONE` constants for this.
- **This undid the one page-count side effect from the header change**:
  since the footer's line count never changed (still one line, just
  reformatted from centre-only to three columns), removing the header's
  second line brought every chapter back to exactly its original page
  count and gap set. Verified on all nine: 32/23/21/24/21/20/27/24/29
  pages, gaps unchanged (ch03 4.78 cm, ch06 4.56 cm, both exactly matching
  the pre-header-change numbers). ch05's content reorder from the entry
  below (troubleshooting table moved after its two worked examples) is no
  longer load-bearing for layout, but was left in place — it reads fine
  and there's no reason to revert a harmless change.
- All nine delivered `.docx` + preview PDFs in `Book/` rebuilt and
  re-copied again after this fix.

## Running header customised for this book, 2026-09-15

`bookkit.py` here is a copy of the house-wiring engine, and its
`build_header_footer()`/`Book.__init__()` defaults still said "ইলেকট্রিক্যাল
হাউস ওয়্যারিং" — every one of the nine delivered chapters was silently
carrying the *other* book's title in its running header. The user asked for
this book's own header, matching the shape the merged house-wiring book uses
(see `../HW All`'s own CLAUDE.md, "Merged book — running header lost its
chapter number" and the `mkbook.py` header code) but applied per-chapter
here rather than only at merge time, since this book has no merge yet:

- `Book.__init__()`'s `book_title` default → **`"General Electrician"`**
  (English, matching the syllabus's own use of English course/topic names —
  DOL Starter, ATS, Star-Delta Starter). `institute` default →
  **`"Resonance Automation Professional Training Institute (RAPTI)"`**
  (was Bangla, unused by any code before this change).
- `build_header_footer()` rebuilt as a **two-line header**: line 1 is the
  three-column tab-stop layout copied from `mkbook.py`'s merged-book header
  — book title (left) · `অধ্যায় N · chapter title` (centre, bold) ·
  `rapti.net` (right) — including the same "paragraph style must be
  `Normal`, never the built-in `Header` style" fix, because `Header` carries
  its own tab stops that OOXML merges with the paragraph's own and pushes
  the right-aligned text off its mark. Line 2, centred below the divider:
  `{institute}  ·  ☎ {PHONE}`. `WEB = "rapti.net"` and
  `PHONE = "01617-345534"` are new module-level constants next to the other
  colour tokens.
- **This is a per-chapter header**, unlike the house-wiring book's merged
  header — no STYLEREF is involved, since there's no merged book yet for
  this project to need one. When this book does get its own `mkbook.py`
  pass, that merge code should read `self.institute`/the phone constant
  from here rather than re-typing them.
- **The added header line cost real body space on every page** — roughly
  0.3–0.4 cm, since the header area grows to fit two lines plus the divider
  instead of one. Re-running `layout.py` on all nine chapters after the
  change found it reopened a page-foot gap in exactly one: **ch05
  (measuring instruments) grew 21→22 pages with two new gaps** (a
  worked-example pair got stranded right after সারণি ৫.৬, the
  "two-worked-examples-and-a-table-don't-share-a-page" pattern this
  project's CLAUDE.md already knows). Fixed the standing way — **reordered,
  not shrunk**: the troubleshooting table moved from *before* the two
  worked examples to *after* them, and উদাহরণ ৫.১'s two-line `steps=`
  merged to one. Back to 21 pages, zero gaps. **ch03's and ch06's
  pre-existing gaps shifted by ~0.03 cm (4.78→4.75, 4.56→4.54) — noise, not
  a new problem.** The other six chapters (01, 02, 04, 07, 13, 15) were
  unaffected. **If a future header/footer change touches every page again,
  re-run `layout.py` on all delivered chapters before calling it done — a
  small per-page cost can silently tip over one already-tight chapter even
  when every other one absorbs it fine.**
- All nine delivered `.docx` + preview PDFs in `Book/` were rebuilt and
  re-copied after this fix.

## Reused-content — how the nine adapted chapters were done, 2026-09-14

The user's instruction was explicit: take the topic-matching house-wiring
chapters, edit the chapter numbering, and drop them straight into this
project's normal `Book/build/` — the same way chapters 1 and 2 were handled,
not left in a holding folder. All nine are now done and delivered; the
`_hwbook_reference/` staging folder used while doing this work has been
deleted.

**Chapters 1 and 2 needed no renumbering** — house-wiring's own chapter
number and topic happen to match this book's exactly (ch01 নিরাপত্তা, ch02
টুলস) — but they were **not** untouched copies either: both had prose that
pointed at other house-wiring chapters with no equivalent here (ch01's
"আর্থিং ও সুরক্ষা ডিভাইস… অধ্যায় ২২ ও ২৮-এ", ch02's SWG/Conduit glossary
rows pointing at "অধ্যায় ২৩"/"২৬") and were rebuilt after those were fixed
(see below). Page counts unchanged (32, 23).

**Seven more were renumbered and content-fixed**: ch03←HW04, ch04←HW07,
ch05←HW08, ch06←HW16, ch07←HW18, ch13←HW20, ch15←HW21. For each: the source
(`chNN.py`, `dia_chNN.py`, `assets_chNN.py` where one exists), photo assets,
and rendered diagram PNG/SVG pairs were copied in under the **new** number;
`Book(N, …)`, the `D`/`A` path setup, the docstring header and the
`os.path.join(OUT, "অধ্যায়-NN — …")` save path were all updated to the new
number; every hand-typed section-number string in `b.h1()/h2()/h3()` calls
(which carry the chapter number as their leading digit, e.g. `"১৮.৯.৩"`) was
renumbered with a quote-anchored find/replace — auto-numbered things
(চিত্র/সারণি captions, worked-example numbers) needed no touching since
`bookkit.py` derives those from the `Book(N, …)` chapter number itself, not
from hand-typed strings.

**The harder part was the prose itself: every house-wiring chapter freely
cross-references *other* house-wiring chapters by number, and this book's
chapter list is a different, shorter set** — of the four candidate chapters,
only two (safety=1, motor=7↔float-switch=13's mutual references) share a
number with this book. A per-chapter mapping was applied by hand, reading
full surrounding context before each edit (never a blind
digit-for-digit substitution, since section numbers of the *same* chapter
and cross-references to a *different* chapter can share a leading digit by
coincidence):

- **Renumbered in place** where the target chapter is also reused here:
  `৪`→`৩` (electricity), `৭`→`৪` (circuits), `৮`→`৫` (measuring), `১৬`→`৬`
  (power formula), `১৮`→`৭` (motor), `২০`→`১৩` (float switch), `২১`→`১৫`
  (busbar). Included dotted cross-section refs like "অধ্যায় ১৬-এর ১৬.৭
  অনুচ্ছেদ" → "অধ্যায় ৬-এর ৬.৭ অনুচ্ছেদ".
- **Redirected forward** to a chapter this book will still write, where the
  content genuinely belongs there: ch13 (float switch)'s "কন্টাক্টর,
  ওভারলোড রিলে … বিস্তারিত অধ্যায় ২২-এ" (HW's breaker chapter, no GE
  equivalent) became "অধ্যায় ৮ ও ৯-এ" — GE's own ম্যাগনেটিক কন্টাক্টর and
  DOL Starter chapters, which really will cover contactors and overload
  relays. ch03 (electricity)'s capacitor-voltage-rating aside pointing at
  HW's fan chapter (no GE equivalent) was redirected to "অধ্যায় ৭ দ্রষ্টব্য"
  (GE's own motor chapter, which does cover capacitor voltage ratings).
- **Softened or dropped** where the target chapter has no GE equivalent at
  all and no reasonable substitute exists yet — house-wiring's fan (12),
  switch board (15), bill (17), two-way switch (13, a different HW chapter
  than GE's float-switch 13), joints (11), cable (23), breaker (22), conduit
  (26) and earthing (28) chapters. These sentences were reworded to stand on
  their own (e.g. "ক্যাবল সাইজ নির্বাচনের বিস্তারিত হিসাব এই বইয়ের পরিসরের
  বাইরে" instead of naming a chapter that isn't in this book) rather than
  deleted outright, so no factual content was lost — only the dangling
  pointer.
- **Left untouched, deliberately**: `বিএনবিসি ২০১২ পার্ট ৮ অধ্যায় ১`
  citations (that "অধ্যায় ১" names the *standard's own* Part 8 Chapter 1,
  never this book's chapter numbering — a real trap, since GE's own চ্যাপ্টার
  ১ is also safety, so a careless regex could have "fixed" a citation that
  was never broken); code comments recording historical layout fixes (e.g.
  `# … (অধ্যায় ১৫-এর শিক্ষা)`) since they're dev notes, not rendered text and
  not worth rewriting for a chapter that no longer exists under that number
  here.

**Every one of the nine was then rebuilt and verified** with the borrowed
`../HW All/Book/build/venv` (`python chNN.py` then `python layout.py
"out/…docx" 4.5`) — figures/tables/page counts all match the original
house-wiring chapter exactly, and every pre-existing page-foot gap carried
over unchanged (ch03's 4.78 cm, ch06's 4.56 cm); the content edits opened
no new one. `mathguard.py` is clean on all nine. Diagrams were **not**
regenerated — the copied PNG/SVG pairs are byte-identical to the delivered
house-wiring ones, since no `dia_chNN.py` content changed, only its own
`D`/`A` path constants (for if it's ever re-run).

**`Book/build/.textcache.json` was copied over too** (the house-wiring
book's ~2000 measured-string cache) — harmless for new content, which just
appends to it.

**The remaining chapters have no house-wiring equivalent at all** — ৮
ম্যাগনেটিক কন্টাক্টর (now written, 2026-09-16), ৯ DOL Starter, ১০ টাইমার,
১১ ATS, ১২ Forward-Reverse Starter, ১৪ Star-Delta Starter (all now
written), ১৬ Solar, ১৭ CC Camera — industrial control-panel wiring and low-voltage/security topics the
house-wiring book never covers. They start from a blank `chNN.py`/`dia_chNN.py` the normal way
(see Workflow below); the house-wiring `Motor.docx`/`Solar System.docx`
source files at `../HW All` root and `assets_hwbook.py`'s already-extracted
institute photos are worth checking for reusable facts/figures before
hand-drawing anything new, and the CLAUDE.md source-mining habits below
still apply — root out real market components, verify every standard by web
search, never invent a clause number.

## Chapter 17 — what it established, 2026-09-20

- **BNBC is the chapter's spine, and it names CC ক্যামেরা outright.**  Part 8
  Chapter 1 §1.1.1 lists "CCTV monitoring System" among the installations the
  code governs, which settles that this is an electrician's job and not an
  aside.  Two clauses then give the chapter its two halves, and they disagree
  by 60 mm on purpose: **§1.3.40.1** (RF and video cable) says video cable
  running parallel to power conduit keeps **at least 350 mm**, and
  **§1.3.41** (data) says Cat 6 keeps **at least 410 mm** — which maps exactly
  onto coax+balun versus IP.  §1.3.40.1 also specifies the coax construction
  (solid copper centre, foamed polythene, aluminium foil, copper braid), which
  is precisely what `ph_coax`'s cross-section shows, and §1.3.41 forbids any
  joint between patch panel and socket.  Full extracts in
  `notes/ch17_bnbc.txt`.  Both clauses open with the same sentence — never in
  the same conduit as power cable — and that is the line to quote.
- **Five datasheets carry every number, and one of them prints the standard
  itself.**  Dahua **DH-HAC-HFW1200T-A**'s datasheet contains a full DORI
  table *and* names EN 62676-4 in its own footnote, so the four pixel-density
  thresholds (25 / 63 / 125 / 250 px/m) could be checked from two directions
  instead of taken on trust.  It also gives three lens angles for one camera
  (103 / 87.5 / 54.7 degrees), which is what makes d05 possible.  The others:
  **IPC-HFW1230S-S5** (PoE 5.5 W max, M12 mount, ONVIF Profile S),
  **XVR5108HS-4KL-X** (800 m at 1080P over coax), **NVR4108HS-8P-4KS2**, and
  Hikvision **DS-1H18S/E(C)** (75 ohm BNC / 100 ohm UTP, 250 m).  Text in
  `notes/ch17_datasheets.txt`.
- **The chapter's best moment is one line of a datasheet.**  The NVR's spec
  reads "Max 25.5w for single port, 80w in total".  Multiply and you get
  204 W, a number that appears nowhere and that the box cannot deliver;
  the total runs out first.  d10 and উদাহরণ ১৭.৪–৫ are built on that, and
  ১৭.৫ deliberately fails (6 × 5.5 + 2 × 25.5 = 84 W > 80 W), which is the
  ch12 AC-3/AC-4 move again.
- **The hand calculation is honestly worse than the datasheet, and the book
  says so.**  Deriving DORI distance geometrically gives ~8 % short at 6 mm
  and ~25 % short at 2.8 mm, because barrel distortion is outside the
  formula.  Rather than hide it, ১৭.৪.৩ prints both and notes that the hand
  figure errs toward safety.  The px/m formula itself (`D = N_H / W`) *is*
  exact and needs no lens data — that is what the three worked examples use.
- **Hikvision's site is behind a JS bot challenge**; `curl` and WebFetch both
  return a script, not the PDF.  `assets.hikvision.com` (their document CDN)
  serves the same files straight.  Dahua's own `dahuasecurity.com` and
  `material.dahuasecurity.com` are open — prefer Dahua when a fact can come
  from either.
- **Two Commons files were rejected for lying about themselves**, the ch11 CT
  lesson twice over.  `CCTV Surveillance Notice bn.svg` is filed as Bengali
  but its own description says *Hindi*, and its text is unreadable without
  the font — so the Bangla notice in d15 was drawn instead, where the wording
  is ours.  `Coaxial cable.JPG` looks like a coax cross-section but its
  description reads "High voltage power cable".  A third, a Planet PoE
  switch, was dropped only because its description is in Chinese script and
  Kalpurush has no CJK glyphs (ch10's lesson).
- **`\text{...}` and `\;` are not in the math DSL** and print literally;
  `_MATH_CMD` has only `\quad`/`\qquad` for spacing.  Worse, `\text{}` is how
  Bangla sneaks into `steps=` — `mathguard.py` caught ten of them.  And a
  `\quad` immediately before a unit renders as a visible hole ("= 4.2    Ω");
  the house form is a plain space, as in ch03.
- **SVG text has no markdown.**  `**সমান**` printed with the asterisks in
  d11's first render.  Emphasis in a diagram is colour or a separate line.
- **Gaps: eleven on the first build, closed in eight passes, 56 pages.**  Nine
  of the eleven were a worked example or a tall figure that would not share a
  page.  What worked was ch14's move (explanation and tables *before* the
  tall figure) plus ch11's (a photo row bridging two examples).  Two examples
  were converted to prose because their arithmetic was a single operation and
  the real content was the conclusion — that removes a tall block *and*
  shortens the chapter, and is worth reaching for before shuffling a fifth
  time.  The last gap was filled with a fact the chapter genuinely lacked:
  PoE does not extend the 100 m limit.
- **A cross-reference was wrong and got caught by opening the chapter.**  The
  draft said the DC marking on the NVR's 48 V inlet was "পড়া অধ্যায় ৩-এ" —
  but ch03's ৩.১.৩ covers AC vs DC with a waveform figure and never shows the
  marking.  Reference dropped.  ch03's `R = ρL/A` and Ohm's law *are* there
  (৩.৪.১, ৩.৫), ch04's series-parallel is ৪.৪/৪.৫, ch06's power formula ৬.৩.
- **Not written, because it could not be verified:** any clause number from
  inside IEC 62676-4 or IEEE 802.3 (both paywalled — only the numbers Dahua's
  datasheet itself prints are cited); prices; hard-disk life or warranty
  hours; H.265+ saving percentages as our own figure (the manufacturer's
  claim is quoted as theirs); and any Bangladeshi statute on surveillance and
  personal data — ১৭.১২ therefore presents the notice as professional
  practice, not as law, and says to check current rules before working
  somewhere sensitive.

## Chapter 16 — what it established, 2026-09-20

- **The institute's own `Solar System.docx` was mined and then mostly set
  aside.** Its section order (সেল → মডিউল → প্যানেল → অ্যারে, তিন ধরনের
  সিস্টেম, পাঁচ-ধাপের অন-গ্রিড ও অফ-গ্রিড হিসাব) is sound and the chapter
  follows it, but almost none of its numbers survived: it quotes the ৭০
  শতাংশ net-metering limit (repealed in 2025), uses `÷` throughout (which
  Kalpurush renders as `+`), and its battery step divides Wh by 12 V with
  no DoD term at all, which under-sizes the bank by half. **Treat that file
  as an outline, not a source.**
- **Bangladesh's rule changed under the book's feet, and the current text is
  primary-source verified.** `NET METERING GUIDELINE – 2025` (SREDA) was
  downloaded whole and read clause by clause; its text is kept at
  `Book/build/notes/nm2025.txt` so the next edit does not have to re-fetch
  it. What changed from 2018: single-phase consumers are now eligible
  (3.3 A), the cap is 100 % of sanctioned load instead of 70 % (3.3 B),
  settlement is quarterly instead of annual (3.4 F), and 10 % of exported
  energy is kept as a Distribution System Maintenance Charge (3.4 M) —
  that last clause is what উদাহরণ ১৬.৫ is built on. Separately, the Power
  Division's **21 December 2025 circular** makes rooftop solar mandatory
  for new connections on roofs of 1000 sq ft or more.
  **powerdivision.gov.bd fails TLS verification** — the guideline's actual
  PDF lives on their Oracle object store, linked from the page HTML.
- **Two real nameplates carry the whole chapter, and one of them came out of
  a photograph.** Commons' "165W solar panel, back.jpg" has a fully legible
  Phaesun Sun Plus 165 P sticker; `assets_ch16.py` crops it a second time at
  a 2560-px thumb (`ph_label`) so every field can be read, and ১৬.৩ is
  taught straight off it. Its footer even reads "Certified according
  CEI/IEC 61215 and CEI/IEC 61730" — exactly the two standards the 2025
  guideline mandates. The other is Growatt MOD 4000TL3-X's data plate
  (`ph_growatt`). **`assets_ch16.py` now takes a per-photo thumb width** as
  an optional 7th tuple field, and the metadata cache is keyed by
  `fname@width`; copy that file, not ch14's.
- **A Commons photo was rejected for lying about itself.** "SUOER SOLAR
  CHARGE CONTROLLER.jpg" (CC0) is not a charge controller at all — the
  markings read `SPEC CATV BN-18-MS`, "Optical Input +2 to -12 dBm",
  "Input Wavelength 1200-1600 nm". It is a CATV optical node with a battery
  backup. Same lesson as ch11's CT: **read the nameplate in the photo before
  captioning it.** The chapter therefore has a drawn charge controller (d09)
  and no photograph of one.
- **The Trina 550 W was dropped mid-chapter because it does not fit the
  inverter.** Its Isc is 18.52 A and the MOD 4000TL3-X's plate says
  `PV Isc 16 A × 2` — incompatible however the string is arranged, since
  series count does not change Isc. Swapped to **TSM-500 DE18M.08**
  (Isc 12.28 A, Voc 51.7, Vmp 42.8, Imp 11.69), which passes all four
  checks. The near-miss became ১৬.৭.২'s safety box, the chapter's
  selection lesson — the ch12 AC-3/AC-4 move again.
- **EPEVER's Tracer-AN manual settled three things the field argues about**,
  all quoted verbatim in `ch16.py`'s docstring: connect **battery → load →
  PV** and disconnect in reverse (d09 was drawn with the wrong order first
  and corrected); a fast-acting fuse of 1.25–2 × the controller's rated
  current within **150 mm** of the battery; and "connect the inverter
  directly to the battery, **not** to the load side of the controller" —
  which is why d11 shows the inverter tapped at the battery posts.
- **d11's battery taps are the ch14 planarity problem again.** Two wires
  leaving the battery to both the controller and the inverter cannot be
  drawn crossing-free unless the positive leaves on the lower path (y 412)
  and the negative on the upper (y 400); swapping them cuts both. The wire
  list was written into the docstring before the picture, and that is what
  caught it.
- **`given=` / `find=` do not go through the math DSL** — `V_{oc}` printed
  literally as `V_{oc}` in the first build. Brace subscripts belong only in
  `steps=`. Write `Voc`, `P(array)`, `I(MCB)` in the two rich-text fields.
  Also `÷` had crept into two `formula` boxes; Kalpurush prints it as `+`.
- **LibreOffice ignores a table column narrower than about 2 cm** and
  redistributes it. A three-column wire list with `widths=[1.4, 5.0, 9.0]`
  came out with a 5 cm first column and cramped text beside it. Both wire
  lists were rebuilt as two columns with the number folded into the first
  cell.
- **Gaps: ten on the first build, closed in three passes, 48 pages.** What
  worked was ch14's move — the explanation and the summary table **before**
  the tall figure (d07, d08, d09), photo rows moved ahead of the drawn
  figure they support, and the DoD definition moved from ১৬.১০.১ up to
  ১৬.৯.৩ where it is first used. Four gaps were filled with content the
  chapter genuinely lacked rather than by shuffling: the three-stage
  charging table, the roof-area calculation, the C-rate rule for charging
  current, and what a net meter's display actually shows.
- **Not written, because it could not be verified:** any clause number from
  inside IEC 61215 or 61730 (paywalled — only the standard numbers the 2025
  guideline names are cited), prices of any kind (ch19's reasoning), cycle
  counts for any named battery brand, and fixed efficiency bands for
  mono/poly/thin-film — সারণি ১৬.১ gives the qualitative difference and
  lets the two datasheets in hand supply the only percentages.

## Chapter 14 — what it established, 2026-09-19

- **The control-ladder bug it nearly shipped.** The first `_ladder14()`
  branched the timer and the two state rungs off **STOP 12** instead of off
  the latched node. Electrically that means the timer starts counting the
  moment the panel is energised and KM2 pulls in without anyone pressing
  START. Caught only while writing d14's wire list — the list said
  "STOP : 12 → KT : 2" and the sentence read wrong out loud. **Rule: write
  the terminal-to-terminal wire list for every control circuit; a ladder
  that looks right can still be feeding the wrong node, and the list is
  where it shows.** The four rungs now branch at x = 632, the same node as
  KM1's A1.
- **Three hops in the power circuit are unavoidable, and it is provable.**
  The three bottom-row nodes each carry three wires (motor lead, KM2, KM3),
  so the routing is non-planar however you arrange it. Every alternative was
  tried on paper — KM2 left / KM2 below / KM3 left / staggered entry
  depths / reordering KM2's poles — and each one just moves the three
  crossings somewhere else. Both sides of the planar argument are written
  out in `dia_ch14.py`'s docstring so the next person doesn't redo it.
  `hop_line()` draws them with ch12's convention (dot = joint, hop = pass).
- **What *is* crossing-free, and why:** KM3's poles carry **L3, L2, L1 left
  to right**. That makes its three output links order-reversing, which
  nests, so KM3 → motor has zero crossings. The supply rails are the
  ordinary full-width three-rail bus, and drops cross rails without dots —
  the standard schematic convention (ch11's d12 precedent), not a hop.
- **The rotation proof belongs in the book, not just the code.** Star puts
  winding U across L1–N, delta across L1–L2; the line voltage leads the
  phase voltage by 30 degrees, and **all three windings shift by the same
  30 degrees**, so the sequence — and the direction — cannot change. ১৪.৫.৩
  says this in prose, and the safety box immediately warns that swapping two
  of KM3's wires reverses the delta and turns the changeover into plugging.
- **`_power14(s, state)` and `_ladder14(s, oy, state)`** each draw all their
  states from one function, so d06/d07/d08 and d10/d11 cannot disagree —
  the ch12 lesson applied again. State colouring runs `live()`/`DEAD` walks.
- **Sources checked for the numbers** (full quotes in `ch14.py`'s
  docstring): ABB's starting-combinations catalogue **1SBC009500R1002** for
  the one-third current *and* one-third torque, the "at least 80% of nominal
  speed" rule, "motor nominal voltage in delta connection must be equal to
  that of the mains" with the 380/660 V example and the six-terminal
  requirement, the KM1/KM2/KM3 naming, the 6–10 s star time, the 50 ms
  transition that "prevents arc short-circuits", and — the single most
  useful line — "connect in the 'delta' circuit. The setting current value
  of the thermal O/L relay must be equal to motor rated current In x 0.58".
  Table ১৪.৫ is that catalogue's kit-form selection rows verbatim. ABB
  **CT-SDS.23** datasheet 2CDC111128D0201 for the dedicated timer (17-18
  star, 17-28 delta, fixed 50 ms ± 2 ms, seven ranges 0.05 s–10 min,
  ± 6 % of full scale, AC-15 3 A, 22.5 mm). ANLY **TRD** for the market
  alternative (30 S / 60 S, Y-to-Δ 0.1–0.5 s). Schneider **LC3D** for a real
  factory-built star-delta starter (3 × 3P, 9/12/18/32 A).
- **The 0.58 / 0.33 split is the chapter's selection lesson** and it lands
  because ABB's own table agrees: at 30 A / 15 kW the catalogue gives A 16,
  A 12, A 16 while the hand calculation gives 17.4, 10, 17.4 A. The book
  shows both and says to round up when calculating by hand — do **not**
  attribute a reason to the manufacturer that the catalogue does not state
  (the first draft did, and it was rewritten).
- **Photos: Commons has exactly one usable star-delta image**, and it is not
  a contactor panel — `Star delta starter internal strúçture.jpg` (CC0) is a
  manual drum switch. That turned out better than a contactor photo would
  have: its terminal strip reads L1, A2, C1, L2, C2, B1, L3, B2, A1, which
  is three lines plus six winding ends, so ১৪.১১ got a real "how it was done
  before contactors" section out of it. It needs `rot=-90` (shot portrait,
  device is landscape) and a crop that removes the photographer's watermark.
  **Rejected on purpose:** the two `Transitionresistors-star-delta switch`
  photos — genuine and striking, but they are *closed-transition* hardware,
  which is outside this syllabus; a photo whose subject you cannot explain
  is worse than no photo (ch11's CT lesson).
- **Commons now rejects arbitrary thumbnail widths** with `400: Use
  thumbnail sizes listed on https://w.wiki/GHai`. ch08–ch12 asked for 1700
  and 3200 px and got away with it; that no longer works. `assets_ch14.py`
  uses **1280**, which is on their list. Copy that file, not the older ones.
- **Page-foot gaps took three reorder passes** (11 gaps → 0, 36 → 35 pages).
  What worked was ch12's move again: **the explanation goes before the
  picture** when the picture is tall — done for d02, d03, d04, d08, d09 and
  d14, rewording "চিত্র ১৪.N-এ" to "নিচের ছবিতে". Also: the summary table
  moved *ahead* of the power circuit it summarises, and ১৪.১০ gained a real
  opening about panel layout (it had none — a genuine hole, not filler).
  **A late one-sentence reword re-opened two gaps and added a page**; trim
  the replacement to the same line count as what it replaces, then re-run
  `layout.py`.
- **Not written, because it could not be verified:** any IEC 60947-4-1
  clause number (paywalled — only ABB's "in compliance with IEC 947-4-1"
  is quoted), any resistor value for closed transition, and any BNBC rule
  about when star-delta becomes mandatory. BNBC 1.3.27 says nothing about
  starter type, so ১৪.৩.৩'s "৭.৫ kW" is written as field practice, exactly
  as ch09 did.

## Chapter 12 — what it established, 2026-09-18

- **The topology bug this chapter nearly shipped.** The first draft of
  `d05_power` crossed *both* link sets — inputs `1→5, 3→3, 5→1` **and**
  outputs `2↔6, 4↔4, 6↔2`. Each picture looked plausible (every wire was
  one continuous phase colour) but the two crossings cancelled and KM2
  delivered the *same* phase order as KM1 — the reversal was gone. Caught
  only by tracing the render by eye, exactly as CLAUDE.md's "parallel drawn
  as series" rule warns. **Rule for ১৪/১৬/১৭: after any power-circuit
  render, trace one phase from the supply to the motor terminal and say out
  loud what it proves.**
- **Only one of the two link sets can be crossing-free.** Connecting two
  equal rows of three terminals in order-*reversing* fashion nests (planar,
  zero crossings); doing it order-*preserving* is provably non-planar —
  three crossings, always. So `join_bus()` draws the output links with
  **semicircular hops** at each crossing: filled dot = joint, hop =
  crossing, and the two can never be confused. Reuse it in ১৪ (star-delta
  has the same shape at the delta links).
- **`_ladder12(s, oy, state)`** is ch09's `_ladder()` doubled with the two
  rungs cutting each other. Both `d07_fwd` and `d08_rev` come from it, so
  the two pictures cannot disagree. The colour walk must treat a NO that is
  *bypassed by a closed latch* as passing — the first version greyed out the
  whole rung downstream of the released FWD button.
- **Button contacts of the two rungs are deliberately at the same x**
  (FWD's NO at 540 in rung 1, FWD's NC at 540 in rung 2), so each two-element
  push button's mechanical link is one straight dashed line. That forced
  rung 2's order to be `FWD 21-22 → [REV 13-14 ‖ KM2 13-14] → KM1 21-22`,
  which is also the electrically correct order (the opposite button's NC
  must sit *before* the latch, or it cannot break it).
- **Why 21-22 and no other NC**: Schneider's FAQ FA142116 states "LC1D09 to
  LC1D95: The 21-22 NC auxiliary contact is a mirror contact", and IEC
  60947-4-1's mirror contact cannot close while the NO main contacts are
  closed — welded contacts included. LC1D09M7's datasheet carries the same
  line. This is the whole argument for layer two of the interlock.
- **The interlock argument runs on two datasheet numbers**: LC1D09M7 closes
  in 12–22 ms and opens in 4–19 ms, so worst case the incoming contactor is
  in before the outgoing one is out. That is why button interlock alone is
  not enough, and it is checkable rather than asserted.
- **AC-3 vs AC-4 is the chapter's selection lesson.** ABB's contactor guide
  (1SAC200017M0002 D) prints AC-3 as "starting, switching off motors during
  running, **reversing**" — so reversing *after the motor has stopped* is
  ordinary AC-3. AC-4 (plugging/inching) breaks **6 × Ie**, and the same
  LC1D09M7 drops from 4 kW to **2.2 kW** at 400 V. Worked example ১২.২ makes
  the ch08 choice of LC1D09 fail, which is the most useful moment in the
  chapter.
- **Three cross-references were wrong on the first pass and had to be
  checked against the actual chapters**: the rotating field is *not* in ch07
  (no section covers it — the reference was dropped, not redirected);
  star/delta is ৭.১০, not ৭.৬; utilization categories are ৮.৫.১, not ৮.৬.
  Worse, the first worked example invented a "১.২৫ গুণ" contactor factor and
  credited it to ৮.৬ — ch08's actual rule is *FLC → AC-3 rating → kW rating
  at the same voltage*, no factor. **Open the referenced chapter and read
  the section before citing it, every time.**
- **MCQ key was ক0/খ4/গ5/ঘ1 on the first draft** — exactly the skew
  CLAUDE.md warns about. Fixed by reordering options to ক3/খ2/গ3/ঘ2. Read
  the key as a string before shipping.
- **Page-foot gaps took five reorder passes** (8 gaps → 0). Every one came
  from a 11–13 cm figure meeting a page with less than that left. What
  worked: explanation *before* the picture rather than after, and moving
  tables/worked examples/boxes to sit ahead of the figure they support.
  **A widening experiment was tried and abandoned** — pushing d05/d07/d08/d10
  from ~13 cm to ~14.4 cm for bigger type reopened three gaps that would not
  close, because `d07`/`d08` have aspect ratio 0.92 (13 cm tall at 14.4 cm
  wide). Instead `d05_power`'s *canvas* was compressed 1160→1040 px, which
  made it both wider (12.4→13.8 cm) and shorter. Compressing a canvas is not
  the same as shrinking a figure, and it is the move to reach for first.
- **Photos: Commons has nothing usable for "reversing contactor"** (same
  finding as ch11). Only one new file was worth taking — a bridge-crane
  pendant. A promising-looking hit, "Mafelec modular industrial contactors
  and wiring", turns out to be an aircraft relay harness, not a motor panel;
  rejected. Everything else came from ch08 via `REUSE`, which also avoids
  another 429 from Wikimedia.
- **Not written, because it could not be verified**: any IEC 60204-1 clause
  number (paywalled), and any specific dwell time before reversing — that
  depends on inertia, so ১২.৯ gives a measuring method instead of a number.

## Chapter 11 — what it established, 2026-09-18

- **The ATS control circuit keeps the two sources electrically separate.**
  Everything on the mains side runs off the mains L and N, everything on the
  generator side off the generator's own L and N; the only things bridging
  them are *contactor* auxiliary contacts (KA1 21-22, KM1 21-22, KM2 21-22),
  whose rated insulation voltage is 690 V (Siemens 3RT2016 datasheet). A
  timer contact was deliberately **not** used as the bridge: no AH3 datasheet
  states the insulation between its two contact sets, so that number could
  not be verified. This is why the extra auxiliary relay **KA1** exists —
  without it, "mains is back" cannot reach the generator-side circuit and the
  two contactors deadlock.
- **Break-before-make falls out of the topology**: KT1 times out → KA1 pulls
  in → KA1 21-22 opens → KM2 drops → KM2 21-22 closes → only then KM1 pulls
  in. d07's timing chart draws that gap (KM1 rises at 12.3, KM2 falls at 12)
  so the picture cannot disagree with the prose.
- **`dia_ch11.py` imports from ch08/ch09/ch10** (`panel`, `note_strip`,
  `fuse`, `lamp`, `_nc`, `_no`, `timer_coil`, `dno`, `timing`, `dim_arrow`)
  and adds `earth()` and `meter()`, which ১২/১৪/১৬/১৭ can reuse.
- **d12 (three CTs + ammeter selector) has three deliberate crossings** —
  connecting three S1 leads one way and all three S2 to a common bus is not
  planar. No dots at the crossings, and the S1 wires are drawn in phase
  colours against a black S2, so they stay readable. qc.py cannot see this;
  check by eye if a wire moves.
- **Sources checked for the numbers** (all in `ch11.py`'s docstring): BNBC
  2012 Part 8 Ch 1 §1.3.24.4 re-read from the law.resource.org PDF and quoted
  verbatim — generator connects after the energy meter and main breaker,
  through a changeover rated at least **1.25 ×** the main incoming breaker,
  of a type where "there is no chance that the generator will be connected"
  in the mains position; contactor-type automatic changeover is explicitly
  allowed. IEC 60947-6-1 classes PC/CB/CC. ABB CM-PFE datasheet for every
  phase-relay number (3 × 208-440 V, threshold 0.6 × UN, 11-12/14 on the
  closed-circuit principle, fixed 500 ms start-up and trip, AC-12 4 A,
  22.5 mm). Schneider LC1D65004P7 for a real 4-pole AC-1 80 A contactor.
  IEC 61869-2 for P1/P2/S1/S2 and the open-secondary hazard; IEC 61554 for
  96 × 96 (cutout 92 × 92); IEC 60051 for the dial marks (star-2 = 2 kV test
  voltage, class 1.5 = ±1.5 % of full scale).
- **A rejected photo worth remembering**: Commons' "DIP current
  transformer.jpg" looks like a CT but its own label reads *4–20 mA DC
  output* — it is a transducer, not a 5 A CT. Replaced with ITL-Family.jpg
  (public domain). Always read the nameplate in the photo before captioning
  it.
- **Page-foot gaps took six reorder passes** and every one came from the same
  two shapes: a tall figure, or two worked examples that will not share a
  page. What finally worked in ১১.৯.৩ was bridging the two CT examples with
  the CT photo row and moving the burden example (১১.৬) to the end of the
  ammeter section. 30 pages, zero gaps.
- **Not written, because it could not be verified**: nothing from the
  paywalled IEC 60947-6-1 text beyond the class definitions, and no transfer-
  time figures for a specific ATSE model.

## Chapter 10 — what it established, 2026-09-17

- **`dia_ch10.py` adds the timer symbol helpers** that ১১, ১২ and ১৪ will
  need: `timer_coil()` (crossed box = on-delay, filled box = off-delay),
  `dnc()`/`dno()` (a ch09 `_nc`/`_no` with the IEC "parachute": ∩ for
  on-delay, ∪ for off-delay on a horizontal rung), `vcontact()` for
  vertical IEC symbols, and `timing()`/`dim_arrow()` for timing charts.
  `timing()` draws no false edge at either end of the chart: a pulse that
  starts at 0 or runs to `tmax` stays high at that edge.
- **The IEC symbol list at qelectrotech has one row mislabelled** ("Make
  contact, delayed opening" is drawn as an NC). The drawings follow the
  consistent rule: an arc opening toward the blade (∈) is on-delay, and an
  arc bulging toward the blade (⊃) is off-delay.
- **8-pin timer pinout (ANLY AH3, verified from the ANLY AH3-R and Alion
  AH3 datasheet timing charts):** 2-7 supply, 8-5 delayed NC, 8-6 delayed
  NO, 1-4/1-3 delayed in Mode A and instantaneous in Mode B. The AH3-NC
  ranges are 6S/60S/6M/60M on a 0–6 scale. Contacts are rated 250 VAC 5 A
  resistive, with ±10 % setting error and ±1 % repeat error. **The Commons
  AH3 photo is a 110 VAC unit**, and the chapter warns about exactly that.
- **The auto-stop topology (`_autostop()`):** KT1 8-5 sits after STOP and
  before the START ‖ 13-14 pair. KT1's coil is in parallel with KM1's coil
  from the same node, so when t expires the latch breaks and the timer
  resets itself. The wiring diagram d13 has no crossings; KT1-2 runs over
  the top to A1.
- **Page-foot gaps took five reorder passes.** Every one came from a worked
  example or tall figure that could not share a page. Examples were moved
  to where they fit the argument (energy saving in 10.7, tank filling in
  10.8) and renumbered to stay in order. **The DIN time-switch photo is
  very tall (1026×2244)**, so its `figure_row` uses `width_cm=5.5`, which
  is also its natural size.
- **Commons titles in CJK script render as boxes** (Kalpurush has no CJK
  glyphs). `ch10.py`'s credits block replaces them with "Time relay".
  Reuse that regex if a future photo credit has a non-Latin title.
- **Not verified, so not written:** the IEC 61812-1 function letter codes
  (the standard is paywalled), and the exact TeSys LADT/LADR catalogue
  ranges beyond LADT2's 0.1–30 s from se.com.

## Chapter 9 — what it established, 2026-09-17

- **`dia_ch09.py` imports its helpers from `dia_ch08.py`** (`panel`,
  `note_strip`, `chip`, `callout`, `coil_sym`, `photo_callouts`, the type
  scale and wire colours) instead of copying them. `photo_callouts` reads
  `dia_ch08.IMG`/`OUT` at call time, so ch09 re-points them in
  `_use_ch09_images()` first. Chapters ১০–১৪ should import the same way.
- **The DOL control ladder is `_ladder(s, oy, state)`** — F1 → F2 95-96 →
  STOP → START ‖ KM1 13-14 → coil, run lamp H1 across the coil, trip lamp H2
  through 97-98. d09 ("run") and d10 ("trip") are one function with two
  states, so the two pictures can't disagree. Timer/F-R/star-delta ladders
  can grow from it.
- **d11 (connection diagram) has zero wire crossings** — buttons in a
  vertical column on the left, and KM1's 13/14 and F2's 95/96 both on the
  left face. qc.py doesn't check crossings; if a wire moves, look again.
- **`assets_ch09.py` asks Commons for 3200-px thumbs** (ch08 used 1700),
  because three of its photos are one panel cut from a 4-panel collage.
  `REUSE = ["ph_starter"]` copies a ch08 photo *and* its credit together.
- **Sources checked for the numbers** (all in `ch09.py`'s docstring):
  BNBC 1.3.27(a),(c),(d) re-read from the law.resource.org PDF — the
  clause says nothing about starter types or a DOL size limit, so the
  "≈৭.৫ kW" figure is written as field practice, not a rule. Trip classes
  (10A 2–10 s, 10 4–10 s, 20 6–20 s, 30 9–30 s at 7.2×; 120/240/480/720 s at
  1.5×) and the 1.05×/1.2× rule from ABB's thermal-OLR catalogues quoting
  IEC 60947-4-1, agreeing with Schneider TeSys. The LRD range and back-up-fuse
  table is the TeSys catalogue verbatim. From the Siemens 3RU2/3RB3 manual:
  wire all three poles in series for single-phase loads, the phase-loss
  acceleration, the warning about auto-reset restarts, 3RB recovery = 3 min
  on auto reset, and no setting outside the scale. 3RV2011-0HA10 (0.55–0.8 A,
  CLASS 10, 10 A instantaneous trip) is from its datasheet.
- **Worked-example numbers carry across chapters**: ৯.১/৯.৪ use ch07's 7.37 A
  5 HP motor and ch08's LC1D09; ৯.৩'s 10 HP 14.2 A matches ch08's exercise.
- **Two Commons files were rejected on purpose**: `Dol starter.jpg` and
  `Auto DOL starter.jpg` are hand-drawn circuits with no overload relay in them.
- **Watch for this in ch10**: 5-6/7-8 second digits aren't only for
  protection devices — timer contacts use them too. The d05 note strip was
  corrected for exactly this before delivery.

## Chapter 8 — what it established, 2026-09-16

First chapter of this book written from scratch. Three things it settled that
chapters ৯–১৪ should follow, since all of them are contactor circuits:

- **`assets_chNN.py` now pulls Commons *thumbnails*, not originals.** Asking
  for the full file 16 times in a row gets a `429` from Wikimedia (their own
  error text says to use the thumbnail sizes instead). `assets_ch08.py`
  requests `iiurlwidth=1700` and keeps the size-guard honest by checking the
  API's reported *original* size, not the downloaded thumb. Copy that file
  for the next chapter rather than `../HW All`'s older ones.
- **Figure numbers are never hand-typed any more.** Adding one photo row late
  in the edit shifted every later `চিত্র N.M` and silently broke three
  cross-references in the practical-work table. Fixed by capturing
  `bn(b.fig_n)` straight after the `b.figure()` call and interpolating it.
  **And no figure number goes inside an SVG** — `qc.py` can't see a stale one
  there, and `d10_power`'s note strip had exactly that bug.
- **The two syllabus items are one lesson, not two.** সিলেক্টর সুইচ = দুই
  তারের কন্ট্রোল = low-voltage *release* (motor restarts by itself when the
  line comes back); পুশ বাটন ল্যাচিং = তিন তারের কন্ট্রোল = low-voltage
  *protection* (it does not). BNBC 2012 Part 8 Ch 1 §1.3.27(d) is what makes
  the second one mandatory, and its exact wording is quoted in `ch08.py`'s
  docstring. Chapters ১০–১৪ all build on the same latching circuit, so they
  can refer back to ৮.৯ instead of re-explaining it.

Verified sources it leans on (all re-checked against the primary document,
not from memory): Siemens 3RT2016-1AP01 datasheet for every coil and rating
number; CHiNT NXC catalogue for the selection table and the 10×Ie/8×Ie
making-breaking rule; IEC 60947-4-1/-5-1 and IEC 61095; BNBC §1.3.27(a),(c),(d)
from the law.resource.org PDF.

## Architecture

Chapters are **generated, never hand-edited** — identical three-stage
pipeline to the house-wiring book:

```
dia_chNN.py  ──► diagrams/chNN/*.svg ──(render.py, headless Chrome)──► *.png
                                                    │
chNN.py ──(bookkit.py)──► out/অধ্যায়-NN — <title>.docx  ◄── assets/chNN/*.png
                                                    │
                              layout.py / qc.py  ──► verification
```

| File | Responsibility |
|---|---|
| `bookkit.py` | DOCX engine: page setup, styles, headings, boxes, tables, figures, OMML math, worked examples. Identical copy of the house-wiring book's engine — **do not fork it**; a fix that belongs in the engine belongs in both projects. |
| `svgkit.py` | Measured-layout SVG builder (Chrome text measurement, auto-sizing, collision geometry). |
| `dia_chNN.py` | Chapter NN's diagrams. Exports `ALL = [...]`. |
| `chNN.py` | Chapter NN's content. Exports `build()` → `(path, Book)`. |
| `render.py` | SVG → high-DPI PNG via headless Chrome. |
| `qc.py` | Diagram quality gate — text/text, text/graphic, off-canvas. |
| `layout.py` | DOCX→PDF, reports blank bands at page feet. |
| `tune.py` | Optional auto-shrink of figures (rarely used). |
| `mkbook.py` | Merges the per-chapter `.docx` into one delivered book — cover, PPE poster, imprint page, clickable সূচিপত্র, the seven back-of-book parts (পরিভাষা · five question types · চিত্রসূত্র), book-wide header/footer. Rewritten for this book on 2026-09-22; see "Merged book" below. |
| `dia_cover.py` / `assets_cover.py` | Cover artwork + RAPTI's logo (from `rapti.net`), copied verbatim — same institute, same visual identity. |
| `mathguard.py` | Flags Bangla text inside `b.math()`/`steps=` (OMML breaks on it). Run before building any maths-heavy chapter. |

## Directory map

| Path | Contents |
|---|---|
| `CLAUDE.md` | This file. |
| `Book/` | Deliverables: one `.docx` per chapter + `Kalpurush.ttf` + the Bangla handbook. |
| `Book/অধ্যায়-NN/` | Per chapter: preview PDF + SVG source, once a chapter ships. |
| `Book/build/` | The pipeline — same Python sources as `../HW All/Book/build/`, plus this book's own `chNN.py`/`dia_chNN.py` for chapters ১–৭, ১৩, ১৫. |
| `Book/build/out/`, `Book/build/diagrams/` | Generated; regenerable; not shipped. |
| `../HW All/` | The sibling house-wiring project. Its own git repo, its own CLAUDE.md. Go there to edit that book; nothing here should reach back into it except one-time copies like this setup. |

## Tech stack

Identical to the house-wiring project: Python 3 + `python-docx`, `lxml`,
`pymupdf`, `python-pptx`, `Pillow`. External: headless Google Chrome (text
measurement + SVG raster), LibreOffice `soffice` (DOCX→PDF), ImageMagick.

**No venv ships with this project either** — create one the same way:

```bash
python3 -m venv venv && ./venv/bin/pip install python-docx python-pptx pillow lxml pymupdf
```

## Commands

Run from `Book/build/` — identical invocation to the house-wiring project:

```bash
python dia_chNN.py                      # generate chapter NN's SVGs
python render.py 'diagrams/chNN/*.svg'  # rasterise to PNG
python qc.py dia_chNN                   # MUST report 0 problems
python mathguard.py chNN.py             # MUST report clean, if the chapter has maths
python chNN.py                          # build the .docx
python layout.py "out/<file>.docx" 4.5  # report page-foot gaps
```

Merging the delivered chapters into one book (`mkbook.py` is already set up
for this book — 17 chapters, this book's own title and cover):

```bash
python assets_cover.py && python dia_cover.py && python render.py 'diagrams/cover/cover.svg'
python mkbook.py --pdf
```

The full merge takes roughly half an hour, most of it LibreOffice resolving
fields on a 177 MB document. For anything that only touches the front matter,
`MKBOOK_ONLY=6,8 python mkbook.py` builds a two-chapter subset in about a
minute and reproduces front-matter pagination exactly.

## Conventions

Same house style as the house-wiring book — carried over so the two books
read as one series:

- **Formal Bangla book prose**, same register settled for the house-wiring
  book from chapter 12 onward (see "Voice" below).
- **All diagrams are pictures** (vector SVG + PNG fallback), never native
  Word-table diagrams.
- **When a source file already has the matching circuit/wiring diagram,
  embed that image directly** rather than hand-redrawing it — crop at high
  DPI, autocrop white margin, place via `SVG.image_fit()`. This matters even
  more here: contactor/starter/timer/ATS panel wiring is exactly the kind of
  diagram a manufacturer datasheet or a real panel photograph already draws
  correctly, and hand-drawn control-circuit ladders are where topology
  errors are easiest to introduce by accident (see the house-wiring book's
  ch06 "parallel drawn as series" incident in its own CLAUDE.md history —
  the lesson applies doubly to contactor/interlock wiring here).
- **All data tables are real Word tables**, never images.
- Numbering: `চিত্র N.M`, `সারণি N.M`, equations `(N.M)`.
- **No `§` sign anywhere** — write cross-references plainly
  (`৭.৩-এর বিভাগ`, not `§৭.৩`).
- Every chapter ends with সারসংক্ষেপ → পারিভাষিক শব্দ → অনুশীলনী (MCQ with
  answer key + short + essay + practical, plus maths where relevant).
- **MCQ answer keys must be balanced across ক/খ/গ/ঘ** — read the key as a
  string before shipping; the house-wiring book shipped several chapters
  with the key skewed hard to one option and had to fix it after the fact.
  Don't repeat that here.
- **Maths in textbook style** via `Book.math()` (OMML fractions) and
  `Book.worked_example()` → প্রশ্ন → প্রদত্ত → নির্ণেয় → সমাধান → উত্তর.
  `steps=` goes through the math DSL; `given=`/`find=` go through `_rich`
  (no `\times`, no Bangla words, no `_{…}` subscripts — see Constraints).
- **Numerals: Bangla in prose, Latin inside equations.**
- Cite **IEC** and **BNBC** (or the relevant control-gear standard — IEC
  60947 for contactors/starters, IEC 61439 for panels, etc.) wherever a rule
  has a standard behind it — verify the number by web search, never from
  memory.
- Diagram type sizing: a `W`-px canvas placed `P` cm wide renders `N`-px type
  at `N × P(pt) / W` points — keep the smallest label ≥ ~7.5 pt.

## Constraints — do NOT change

Identical hard constraints to the house-wiring book (its CLAUDE.md has the
full incident history behind each one — read it if a rule here looks
arbitrary):

- **Never modify any source `.docx`/`.pptx`/`.pdf`** the institute supplied.
- Do not hand-edit generated `.docx` — change `chNN.py` and rebuild.
- Body font is **Kalpurush**; do not switch fonts.
- Kalpurush lacks `÷` (renders as `+`) — use `\frac` or `/`, in SVG labels too.
- Kalpurush has **no Unicode subscript digits** — write plain `R1`, `I1`;
  real subscripts only via the math DSL's `_{…}`.
- **No Bangla words inside `b.math()` or `steps=`**, not even in backticks —
  OMML drops spaces and splits conjuncts. Write the equation with Latin
  symbols and put the Bangla key in the following `formula` box.
- A fraction's numerator must stay wrapped in
  `<m:eqArr><m:e>…</m:e></m:eqArr>` (both `m:num` and `m:den`) — a bare
  `m:num` left-aligns in LibreOffice.
- The math DSL knows only the commands in `README.md` — `\cos`, `\phi` etc.
  are not among them; write `` `cos φ` `` as upright text instead.
- `svgkit` path parsing must honour **relative** SVG commands.
- Page-foot gaps are fixed by **reordering content**, never by shrinking
  figures.
- **`qc.py` only sees what `svgkit` records in `shapes`** (`rect`, `line`,
  `path`, `circle`) — `poly()` and `image()` interiors are invisible to it;
  check those by eye.
- Bengali `৪` renders like a Latin `8` in Kalpurush — Latin digits wherever
  the digit *is* the identity of a thing (a size, a rating, a gauge number),
  not just where a fraction's numerator needs a straight `4`.
- **A "parallel" circuit hand-drawn from a source diagram can render in
  series if the shared node is drawn as one chained wire instead of two
  independent drops to a common bus** — verify every "প্যারালালে" claim in
  the prose against the actual wire routing, in both the schematic and any
  pictorial panel. This is the single most relevant inherited lesson for
  this book: contactor/starter/ATS/timer control circuits live and die on
  correct interlock and parallel/series wiring, more so than anything in
  house wiring.

## Voice

Same target as the house-wiring book's chapters 12+: an experienced
electrician who has actually wired contactors and starters, not a textbook
voice. Ground claims in the field — real relay/contactor part numbers, real
faults ("কন্টাক্টর কয়েল বার্ন করে যখন…"), what a technician actually checks
first. Vary sentence rhythm; avoid formulaic scaffolding, empty
intensifiers, and threes-for-the-sake-of-threes. Full detail (what to keep,
what to file off) is in `../HW All/CLAUDE.md`'s own "Voice" section — same
rules, new content.

## Workflow for a new chapter

Identical to the house-wiring book:

1. Mine any available source material for facts/photos (this project's own
   root has none yet — check `../HW All`'s `Motor.docx`/`Solar System.docx`
   for chapters 07/16, and the open web for control-gear datasheets/
   manufacturer photos for chapters 08–12, 14).
2. Verify any standard/number by web search before citing it.
3. Write `dia_chNN.py`, then `chNN.py`, copying an existing chapter's shape.
4. `qc.py` must be clean, then look at every diagram PNG by eye.
5. Build, run `layout.py`, reorder to close gaps > ~4.5 cm.
6. Read the produced PDF page by page before delivering.
7. Copy the `.docx`, preview PDF and SVGs into `Book/`, update the status
   table here.
8. After the user approves the chapter, ask before backing it up to git —
   this project has no remote configured yet; set one up (or confirm reusing
   a repo under the same GitHub account) before the first push.

## Merged book — what the merge pass settled, 2026-09-22

The user asked for the full book, merged the way the house-wiring book is
merged, plus four specific things. All four are done; `python mkbook.py --pdf`
now produces **`Book/জেনারেল ইলেকট্রিশিয়ান — সম্পূর্ণ বই (অধ্যায় ১–১৭).docx`**
and its PDF — **526 pages**, cover + PPE poster + imprint + সূচিপত্র, the 17
chapter cores, then the seven back-of-book parts.

- **`mkbook.py` is now this book's own.** `DEST`, the chapter-range assert
  (`NCHAP = 17`), the imprint prose, the কোর্স line and the সূচিপত্র's part
  list were all rewritten. `BOOK_BN`/`BOOK_EN` are new module constants; the
  running header's left column reads **জেনারেল ইলেকট্রিশিয়ান** (the user asked
  for the Bangla name on the top-left of every page, not the English one).
  Everything else in the engine is untouched and still shared with `../HW All`.
- **চিত্রসূত্র is now one back-of-book part, built from `credits.json`, not
  from the printed paragraphs.** `strip_credits()` removes each chapter's own
  Heading-4 block (verified: always Heading 4 + one Normal paragraph, right
  before the অনুশীলনী Heading 1) and `build_credits_part()` reprints the lot at
  the end. Doing it from the JSON rather than by lifting text is what fixed a
  real, pre-existing gap: **chapters 7, 13, 15 and 17 use Commons photographs
  under CC BY / CC BY-SA and never printed a credit block at all** — 81 entries
  across 11 chapters now, where only 7 chapters had any.
  - A key counts as used when its name, or any name in its `files` list,
    appears in `chNN.py` or `dia_chNN.py`. **`assets_chNN.py` is deliberately
    not scanned** — it names every file downloaded, including the rejected
    ones (ch08 `ph_burn2`, ch16 `ph_jbox`, ch13 `ph_barrel`), and crediting a
    photograph the book does not print would be wrong. Cross-checked against
    ch08's own hand-written `used` list: identical, 15 of 16.
  - Two entry shapes exist and both are handled: `{title, author, licence}`
    (grouped so one photographer's several pictures make one line) and
    `{source, licence}` with no author, which is how ch07's and the `rapti_*`
    institute entries are written. English licence strings are normalised to
    Bangla (`CRED_LIC`).
- **The PPE poster was already wired.** `FRONT_PPE_PNG` and the page-2
  full-bleed placement came across with the engine; the file the user supplied
  is byte-identical (md5 `5cc850af…`) to `assets/front/ppe_poster.png`. Nothing
  needed changing — check before rebuilding anything if this comes up again.
- **Cover rebuilt in `dia_cover.py`.** Sheet, blueprint grid, gold frame and
  the whole text stack are kept from the house-wiring cover on purpose (one
  visual identity), with gold corner marks added. The title is Bangla over
  `GENERAL ELECTRICIAN`, and the motif is a full **DOL starter** — control
  ladder left (STOP NC → START NO ‖ holding contact → coil), power circuit
  right (three-phase bus → MCB → contactor poles → overload relay → motor).
  The contact symbols are `dia_ch09._nc`/`_no` reproduced, so the cover uses
  the book's own notation.
  - **Two things went wrong drawing it and are worth not repeating.** A ladder
    drawn with its two rails *joined* top and bottom renders as one big empty
    rectangle — rails end in terminal dots instead. And a holding branch only
    lines up with the contact it parallels if both use the same symbol width;
    they share `NOW = 92` for exactly that reason.

**Two pagination findings from the merge:**

- **The imprint has to end on one page, and it nearly didn't.** Three body
  paragraphs (17 lines) pushed স্বত্ব onto a near-empty page 4. Folded back to
  two paragraphs and a two-line copyright notice. If a future edit lengthens
  the imprint, re-check page 3 — the subset build (`MKBOOK_ONLY=6,8`) reproduces
  front-matter pagination exactly and takes about a minute, so use it.
- **The চিত্রসূত্র part was 4 pages with one orphan credit line on the last.**
  Closed by tightening it (heading `space_before` 9→6 pt, entry
  `line_spacing` 1.18→1.13, `space_after` 2→1.5 pt) to a filled 3 pages
  (524–526), which also took the book from 527 to 526 pages.
  `/tmp/credtest.py`'s trick — build **only** that part into a standalone
  `.docx` and convert it — reproduces its pagination exactly in ~30 s, against
  ~25 min for the full merge. Recreate it if the part is ever retuned.

**Known, not fixed:** the last bullet of ch16's সারসংক্ষেপ orphans onto page
385 of the merged book. Page 384 is completely full (ink to y=812 of 842), so
it is a genuine one-line overflow, not a page-foot gap — and it exists only in
the merged book, because the merge cuts each chapter core at পারিভাষিক শব্দ and
so ends ch16 in a different place than the standalone chapter does. Fixing it
means shortening a summary bullet in `ch16.py`, which changes the delivered
standalone chapter too; left for the user to decide. Everything else is clean —
a full scan found exactly these two near-blank pages, and the second is now
gone.

## Correction pass, 2026-09-23 — chapters 1–3 only

A full-book review (`Book/build/notes/review_2026-09-23.md`) listed factual,
consistency and AI-style problems in all 17 chapters. The user then asked for
**only chapters 1–3 to be fixed** and the merged book rebuilt with those; ch04–17
are untouched and their items in the review file are still open.

- ch01: body-resistance figures per IEC 60479-1 (hand-to-hand 1,000–2,000 Ω at
  230 V, table rows redone); reflective *vest* (not apron — also dia_ch01 d05);
  Prove–Test–Prove needs a two-pole tester (IEC 61243-3), neon ruled out; ELCB,
  gloves and let-go wording; unverified clearance numbers removed.
- ch02: house-wiring framing → electrician; two-pole tester added to the kit
  table; Class III, drilling-zone heading, ferrule glossary fixed.
- ch03: definition of বিদ্যুৎ rewritten (energy of charge; static vs current);
  run vs start capacitor.
- All three: objectives end in "পারবে", em-dashes thinned, "নয়, বরং" removed.
- Rebuilt: 32/23/21 pages, gaps unchanged (only ch03's inherited 4.78 cm).
- Edit tool: `scratchpad/rep.py` + pair files (exact-count find/replace); backups
  of every ch*.py/dia_ch*.py from before the pass are in the session scratchpad.

## Full-book revision, 2026-10-16 — DONE (stages 1–3)

The user approved a three-stage revision of the whole book (review in
`Book/build/notes/language_review_2026-10-16.md`; the 15 book-wide decisions in
its first table and the proposed headings were all approved and applied):

1. **Stage 1 — factual/safety errors**, all 17 chapters (reports in
   `notes/2026-10-16/fix_chNN.md`, brief `fixbrief.md`). New sections: ch13
   ১৩.৬.৬ auto-manual, ch15 ১৫.১০ star-delta practice.
2. **Stage 2 — language, headings, decisions**, all 17 chapters (brief
   `notes/2026-10-16/s2brief.md`). Prose is impersonal, instructions "করুন";
   em-dashes only as labels; terms সার্কিট/রেজিস্ট্যান্স/প্যারালাল/বাটন/ক্যাবল/HP;
   objectives 7–9 ending "পারবে", summaries 9–12 bullets. Exercise headings
   ("ক. বহুনির্বাচনী প্রশ্ন" …) were deliberately kept — mkbook.py matches them.
   Chapter titles changed: ch05 "মেজারিং ইনস্ট্রুমেন্ট", ch15 "বাসবারের ব্যবহার ও
   ক্যালকুলেশন". **Three-phase supply/motor leads drawn joined by one bar (a
   phase-to-phase short) were found and fixed in ch06 d01, ch08 d01/d10/d14,
   ch09 d08/d11, ch10 d13, ch12 d05, ch14 Q1 poles** — check any new power
   circuit for this.
3. **Stage 3** — all 17 rebuilt with zero page-foot gaps (pages: 33 23 21 24 22
   20 28 34 33 29 31 27 27 36 34 49 53), copied into `Book/`, merged book rebuilt:
   **536 pages**.

Environment notes: `CHROME` and `LO_PROFILE` env vars (render.py, svgkit.py,
layout.py); render.py pads the viewport and crops (headless Chromium clipped
the bottom ~86 px); svgkit's measure file is per-process. LibreOffice needs
`libreoffice-math` or equations come out blank, and LibreOffice 24.2 printed a
bare "(" in OMML as "\(", so `_math_tokens` emits matched brackets as `<m:d>`.
mkbook needs `pip install docxcompose`; the full merge took ~5 min here.
BNBC 2020 text could not be reached (`notes/2026-10-16/bnbc2020_map.md`), so
citations stay "২০১২" and the imprint says so. LibreOffice can silently drop a
table's body rows when its header lands at a page foot (seen once in ch16) —
`layout.py` does not catch it.

## Next step

**All seventeen chapters are written and the full book is merged.** What is
left is housekeeping:

1. **`Book/পড়ুন — বই তৈরির নির্দেশিকা.md` is still the house-wiring book's
   guide, verbatim** — its title, its 28 chapters, its cable and earthing
   chapters. It was never rewritten when this folder was set up and it ships in
   the delivery folder. Rewrite it for this book or delete it.
2. **No git repository has been initialized in this folder yet.** Worth doing
   now that there is a merged book to version, mirroring `../HW All`'s own
   private-repo setup — ask the user which GitHub account and repo name.

**Chapter 17 is the longest in the book — 56 pages standalone (49 in the
merged book, where its glossary and exercises move to the back), against
ch16's 48 and ch14's 35.** The length is earned (three syllabus items, nine
worked examples, 25 figures, 16 tables, and a BNBC spine that no generic CCTV
text has), but if the user wants the series evened out, the cheapest cuts in
order are:

- **১৭.১৫ পারিভাষিক শব্দ** — 33 rows, the longest glossary in the book; ~2 pp.
- **১৭.১৩-র ত্রুটি-সারণি** — 12 rows; trimming to the 8 most common saves ~1 pp.
- **one of the two photo rows in ১৭.৮.৩** (ph_rack / ph_ctrl) — decorative
  rather than load-bearing; ~0.5 pp.
- **উদাহরণ ১৭.৯ (মোশন রেকর্ডিং)** could fold into a note box; ~0.7 pp.

Do **not** cut ১৭.৪.৩ (DORI), ১৭.৭.৪ (PoE budget) or ১৭.৯.২ (ভোল্টেজ ড্রপ) —
those three are the chapter's reason to exist, and each one is a calculation
the field gets wrong.
