# fix_ch02 — অধ্যায় ২ (ইলেকট্রিক্যাল টুলস), stage 1

Files touched: Book/build/ch02.py, Book/build/dia_ch02.py (d02, d06 re-rendered; qc 0 problems). Backups of the pre-edit files: scratchpad/bak01/.

## Items (review ch02.md §৭ and the relevant §৬ points)
- ✅ §৭-1 BNBC vs tool safety: objective 5 now reads "পাওয়ার টুল ব্যবহারের নিরাপত্তাবিধি (IEC 62841) মেনে চলতে পারবে"; BNBC removed from the intro; the ২.৬ sentence now says that IEC 62841 governs tool safety and that BNBC Part 8 Ch 1 is the installation code, not a tool-use code. (BNBC edition left as is, as the brief instructs.)
- ✅ §৭-2 Class III/SELV written one way everywhere: "৫০ V AC-এর বেশি নয়" (table ২.১০, summary, glossary).
- ✅ §৭-3 MCQ 9: option গ "স্পিরিট লেভেল" → "ফিশ ওয়্যার", so only one answer is defensible (key ক).
- ✅ §৭-4 SWG vs mm²: the wire-gauge row in সারণি ২.৬ now says it measures a single strand's diameter (SWG) and that cable size is written in mm² (1.5 / 2.5 mm²). The glossary row reads "একক তারের". MCQ 10 → "একক তারের SWG নম্বর সরাসরি নির্ণয় করা হয় কী দিয়ে?" Micrometer and vernier were replaced with clearly wrong options (প্লাম্ব বব, ট্রাই স্কয়ার), since a micrometer also measures diameter (key গ).
- ✅ §৭-5 Toolkit (২.৮, now 18 rows): added digital multimeter, clamp meter, ferrule crimper, adjustable wrench + Allen key set, and a slim 3 mm flat terminal screwdriver in the screwdriver set. Removed cold chisel, spirit level and wire gauge. Diagonal cutter now also covers cable ties. Chapter 5 is not named anywhere.
- ✅ §৭-6 Cold chisel: "মাথা ছড়িয়ে গেলে ঘষে ঠিক করতে হবে, ফেটে গেলে বাতিল করতে হবে".
- ✅ §৭-7 Insulated Tools glossary → "IEC 60900 মানের টুল; লাইভ অংশের কাছে কাজের উপযোগী". d02 labels "জীবন্ত লাইনে ব্যবহারের উপযোগী" / "…জীবন্ত লাইনে কাজ করা যাবে না" were changed to "লাইভ অংশের কাছে…".
- ✅ §৭-8 BS 7671 522.6.202: the second sentence of ২.৬.২ now says that outside the zones a cable needs a depth greater than 50 mm or *earthed* metal conduit or covering. It also says that cables inside the zones at less than 50 mm need 30 mA RCD additional protection, unless they have an earthed metal covering.
- ✅ §৭-9 Key unchanged and balanced: ক4 খ4 গ4 ঘ3.
- ⏭ §৭-10 MCQ 2: the review itself says it is fine.
- ⏭ §৭-11 d01/d02 terminology (অন্তরক) and the Bangla vs Latin digits of the size example: stage 2.
- ✅ §৬ The four categories are now named in ২.২, with the section where each is covered. The NCV detector was moved from the power-tool photo row and table into ২.৩.১ (its photo row is now 5-up, captioned "…স্ক্রু ড্রাইভার ও টেস্টার"), so it matches d06, which lists it under safety tools. The power-tool row is now 8 photos, 4 per row.
- ✅ Forward reference found in a figure: d06 said "মাল্টিমিটার (অধ্যায় ৫)", now "মাল্টিমিটার, ক্ল্যাম্প মিটার".
- ✅ House-wiring framing: the star screwdriver row now reads "সুইচ বোর্ড, প্যানেল ও যন্ত্রপাতির…" (ফ্যান dropped).
- ✅ Practical task 5 (drilling near concealed cable) now starts "সংশ্লিষ্ট সার্কিটের সাপ্লাই বন্ধ রেখে…". The other tasks do not touch live wiring.
- ⏭ §৬ intro-less subsections, glossary trimming, double numbering, "মনে রাখুন" box → prose, and objective (8) wording: stage 2.

## Sources
- BS 7671 522.6.202 (zones; under 50 mm needs a 30 mA RCD unless there is an earthed metal covering or conduit): https://electrical.theiet.org/media/1445/cables-in-walls.pdf ; https://www.voltimum.co.uk/articles/rcds-and-concealed-cable ; https://professional-electrician.com/?p=13406
- SELV/ELV limits of 50 V AC and 120 V ripple-free DC (IEC 61140 band): standard value. Only the AC figure is used in the text.

## Layout
- Before: 23 pp, no gap > 4.5 cm. After: **24 pp, no gap > 4.5 cm**, 15 figures and 13 tables.
- The added text opened three gaps, closed by reordering. d03 (stripping) now comes before সারণি ২.২, d02 (IEC 60900 marking) right after the ২.৫ intro paragraph, and in ২.৭ the bullet list now comes before d07.

## Needs the author's decision
- The toolkit removals (chisel, spirit level, wire gauge) are a judgement call. The chapter still teaches those tools; the kit was just refocused on panel and motor work.
