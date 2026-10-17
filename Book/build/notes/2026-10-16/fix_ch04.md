# fix_ch04 — stage 1 (factual / safety / consistency)

File touched: Book/build/ch04.py only (diagrams unchanged — none contained an error). Backup: scratchpad/bk345/ch04.py

## Items
- ✅ ৭.১ Mixed-circuit rule "আগে প্যারালাল, পরে সিরিজ" (wrong for the chapter's own চিত্র of বাতি ৩–৪ in series inside a branch): fixed in ৪.৬ bullet ("সবচেয়ে ভেতরের অংশ থেকে ধাপে ধাপে"; series inside a branch added first), ৪.৬.১ steps ১–২, সারণি ৪.৬ cell, and ৪.১০ summary.
- ⏭ ৭.২ Door-bell transformer output as DC — source already says "মোবাইল চার্জারের আউটপুট" (correct DC example); nothing to fix.
- ✅ ৭.৩ Indicator lamp as a series example: removed from সারণি ৪.৫ (the "সিরিজ বোর্ড" row). The tip box and সারণি ৪.৬ did not actually mention indicator lamps.
- ✅ **সারণি ৪.৫ (series test board drawn as parallel) + house-wiring rows**: "সিরিজ বোর্ড" row replaced by "ডিস্ট্রিবিউশন বোর্ড | মেইন সুইচ বা মেইন MCB | প্রতিটি শাখা সার্কিট"; "পুরো বাসার ওয়্যারিং" replaced by "মোটর কন্ট্রোল প্যানেল | কন্ট্রোল ফিউজ ও STOP বাটন | কন্টাক্টরের কয়েল ও তার ইন্ডিকেটর বাতি" (matches ch09's ladder, H1 across the coil; no chapter number cited). মাল্টিপ্লাগ and সুইচ বোর্ড rows are factually right and kept. Lead-in sentence no longer says "পরবর্তী অধ্যায়গুলোতে আসা".
- ✅ ৭.৪ "কমপক্ষে চারটি অংশ" vs "পাঁচটি অংশ" (৪.১): now "কমপক্ষে তিনটি অংশ: উৎস, পরিবাহী ও লোড; ব্যবহারিক সার্কিটে নিয়ন্ত্রণ ও সুরক্ষা যন্ত্রও থাকে". সারণি ৪.১ caption → "একটি ব্যবহারিক বর্তনীর অংশসমূহ"; summary bullet ১ matched.
- ✅ ৭.৫ উদাহরণ ৪.২ "প্রায় 25 W": note now says R is assumed constant; really the filament R falls at low voltage, so power is somewhat above 25 W (no forward ref to ch05).
- ✅ ৭.৬ House-wiring leftovers: গৃহওয়্যারিং ×9 → "ভবনের ওয়্যারিং" (objective, tip box, সারণি ৪.৬, h2 ৪.৭.১, summary, MCQ ১০, short Q৮, essay Q৪); "ওয়্যারিং কর্মী" → "ইলেকট্রিশিয়ান"; ৪.২.২ "হাউস ওয়্যারিংয়ের প্রায় সব কাজই" → "ভবন ও কারখানার প্রায় সব বিদ্যুৎ সার্কিটই এসি".
- ✅ ৭.৭ Forward reference in ৪.৮ IEC 60051-2 box ("পরের অধ্যায়ে") — sentence removed. Section ৪.৮ itself kept (only fixed, not cut, per instruction).
- ✅ ৭.৮ BNBC overclaim (৪.৭.১ box) "এই কোড অনুসারেই লোড প্যারালালে… সুইচ ফেজে": claim removed; box now only says BNBC sets the minimum standard for building wiring. Citation text "বিএনবিসি ২০১২" left untouched.
- ✅ ৭.৯ সারণি ৪.৭ voltmeter in series: "কারেন্ট প্রায় বন্ধ, পাঠ ভুল" → "লোড চলে না; মিটারে প্রায় পুরো সরবরাহ ভোল্টেজ দেখায়".
- ✅ ৭.১০ গাণিতিক প্রশ্ন ৭: unverifiable fuse part ("প্রচলিতভাবে 5–6 A") removed; question now asks total current only (উত্তর 1 A).
- ✅ ৭.১১ / ৩-এর ৩৯ Practicals ৪.৯.১–৪.৯.৩: each now starts with supply OFF + two-pole tester dead check; lamps are removed only with supply OFF, then supply restored; switching on only after showing the instructor. End safety box item ১ now says supply off and verified dead with a two-pole tester before connecting, removing a lamp or changing wiring.
- ✅ ৩-এর ৪৩ Summary last bullet ("ব্যতিক্রম করলে মিটার নষ্ট হয়" — false for a voltmeter in series) → ammeter in parallel = short circuit, may destroy meter.
- ✅ ৬ Practical table row ৪ "অ্যামিটার/ক্ল্যাম্প মিটার… সিরিজে" (clamp meter is never in series) → "অ্যামিটার বা মাল্টিমিটার".
- ✅ Old review [LOGIC] সারণি ৪.৩ listed "ফিউজ, সুইচ ও অ্যামিটার সিরিজেই বসাতে হয়" as an *advantage* → replaced with a real advantage: "সার্কিটের কারেন্ট সীমিত রাখা যায় (যেমন সিরিজ টেস্ট ল্যাম্প)".
- ✅ MCQ ১৩ (ammeter resistance) had a near-second answer "রোধ থাকে না" (ideal ammeter) → distractor changed to "লোডের রোধের সমান". Key unchanged and balanced: ক৪/খ৪/গ৪/ঘ৪.
- ⏭ MCQ ১১–১২ duplicate ch03/ch05, weak distractors (Q৩/৫/৭), glossary pruning, objectives rewrite, moving সারণি ৪.৭ to ch05, deleting IEC 60051-2 box — duplication/style/structure, stage 2.

## Sources
- No new number introduced. The ladder fact (indicator lamp parallel to the coil) is from this book's own ch09 `_ladder()`.

## Layout (layout.py 4.5)
- Before: 24 pp, zero gaps.
- After: **25 pp, zero gaps**; figures 10 / tables 9 unchanged; mathguard clean. The extra page carries the last 3 rows of the practical table (সারণি ৪.৯, page 25 ink ends ~y207). Shortening my own additions did not pull it back (earlier pages absorb the slack), so it was left; stage 2's planned trims (e.g. dropping duplicate MCQs / IEC 60051-2 box) will recover it.

## Author decision
- সারণি ৪.৫: the series test board was dropped rather than corrected, because it is all-series and so is not an example of a *mixed* circuit. If the author wants the test board in the book, it fits better as a correct all-series example in ৪.৪.৩.
- The ammeter/voltmeter section ৪.৮ still overlaps ch05 (syllabus item belongs to ch05); left in place per instruction.
