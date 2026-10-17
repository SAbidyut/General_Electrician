# fix_ch03 — stage 1 (factual / safety / consistency)

File touched: Book/build/ch03.py only (no diagram change). Backup of pre-edit source: scratchpad/bk345/ch03.py

## Items
- ✅ ৭.১ বজ্রপাত = স্থির বিদ্যুৎ (৩.১.২): rewritten — charge stored in the cloud is static; lightning is its sudden discharge to ground.
- ✅ ৭.২ ভোল্টেজ = "বিদ্যুৎচালক বল" (৩.৩ def + glossary): definition now "বিভব পার্থক্য"; EMF named separately as the source's property. Glossary row "Voltage" corrected.
- ✅ ৭.৩ গড় মান (৩.৭.১ formula box): now says full-cycle average is zero; 0.637 × Vm is the half-cycle average.
- ✅ ৭.৪ / ৩-এর ১৫ (৩.৪.১): "চারটি বিষয়… সম্মিলিত সম্পর্ক এই সূত্রে" → "নির্দিষ্ট তাপমাত্রায় প্রথম তিনটির সম্পর্ক" (R = ρL/A has no temperature term).
- ✅ ৭.৫ উদাহরণ ৩.৩: steps now 230 × 0.43 = 98.9 W = 0.0989 kW; E ≈ 23.7 kWh; answer 23.7 ইউনিট.
- ✅ ৭.৬ লাইন টেস্টার: practical row ৪ → "টু-পোল ভোল্টেজ টেস্টার বা মাল্টিমিটার"; ৩.৯.১ ⚠ box "টেস্টার দিয়ে মেপেই" → "টু-পোল ভোল্টেজ টেস্টার বা মাল্টিমিটার দিয়ে মেপে" (matches ch01 ১.৮.২).
- ✅ ৭.৮ সারণি ৩.৫ (power vs energy; review called it ৩.৭): energy unit cell now adds "SI একক জুল (J)".
- ✅ Contradiction found while checking (same as ch05 review item ৮): ৩.৬ "মনে রাখুন" box said bill calculation is "এই বইয়ের পরিসরের বাইরে" although উদাহরণ ৩.৪ and গাণিতিক প্রশ্ন ৪–৫ teach it. Replaced with: simple bill = units × rate; real bills add slab rates and other charges.
- ✅ ৬ (structure list) glossary "Phase / Line = জীবন্ত কারেন্ট-বহনকারী তার" (neutral also carries current) → "আর্থের সাপেক্ষে ভোল্টেজযুক্ত তার".
- ✅ ৬ practical row ২ (live socket measurement): added "(প্রশিক্ষকের তত্ত্বাবধানে)".
- ⏭ ৭.৭ BNBC 2012 vs 2020 — left as instructed by the brief.
- ⏭ ৭.৯ MCQ ১১ duplicated in ch04/ch05 — not an error (key balanced ক৪/খ৪/গ৪/ঘ৪, every answer unique). Left for stage 2 / dedup.
- ⏭ ৩-এর ২৬ fan-capacitor sentences belong in ৩.৮.১ — placement only, content is correct. Stage 2.
- ⏭ Math-answer key for গাণিতিক সমস্যা, glossary pruning, objectives merge, ৩.৯ split — structure/style, stage 2.
- Checked, no change needed: older review items for ch03 (definition of বিদ্যুৎ, run vs start capacitor, Insulator "প্রায় নেই") are already fixed in source. No forward chapter references.

## Sources
- No new number introduced that needed a source (all edits are corrections of definitions/arithmetic).

## Layout (layout.py 4.5)
- Before: 21 pp, one gap p9 4.78 cm (inherited). (Orchestrator baseline showed p8 4.60 + p9 4.78.)
- After: 21 pp, **zero gaps**. figures 8 / tables 10 unchanged. mathguard clean.

## Author decision
- None required.
