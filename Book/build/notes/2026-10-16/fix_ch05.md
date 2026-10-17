# fix_ch05 — stage 1 (factual / safety / consistency)

Files touched: Book/build/ch05.py, Book/build/dia_ch05.py (d01 note strip only; regenerated, rendered, qc.py 0 problems, PNG checked by eye). Backup: scratchpad/bk345/

## Items
- ✅ ৭.১ "লাইভ–ডেড–লাইভ" (৫.১২ box) → "Prove–Test–Prove" with pointer back to ch01 ১.৮.২; tool now "টু-পোল ভোল্টেজ টেস্টার বা উপযুক্ত CAT রেটিংয়ের মাল্টিমিটার"; "ধাপ তিনটি" now really has three items (the 4th bullet folded into the lead text); মরা/জীবন্ত → ডেড/চালু (ch01 terms).
- ⏭ ৭.২ Filament box far from উদাহরণ ৫.২ — the box itself names "উদাহরণ ৫.২", so the reference is not ambiguous; move is structural (stage 2). Box content checked (hot R ≈ 15 × cold, 100 W → 529 Ω hot) — correct.
- ✅ ৭.৩ উদাহরণ ৫.১: lamp type stated (ফিলামেন্ট), current measured with the multimeter in series instead of a clamp meter (clamp is poor at 0.15 A, per the chapter's own সারণি ৫.৫), value changed to 0.17 A → 39.1 W ≈ 40 W bulb (old 34.5 W was called "স্বাভাবিক" for a 40 W lamp — 14 % low). Note now says P = V × I holds only for resistive loads; LED/CFL/fan give V × I above the real watts.
- ✅ ৭.৪ A-port ambiguity: সারণি ৫.৪ "A পোর্ট" row notes many meters have separate 10A and mA jacks; ৫.৭.১ step ৪ rewritten (choose jack and range; start on 10A if unknown; overcurrent in the mA jack blows the internal fuse). The figure (single A port, simplified meter face) stays consistent.
- ✅ ৭.৫ সারণি ৫.৬ "বারবার ব্রেকার ট্রিপ → ক্ল্যাম্পে L+N": row now "বারবার RCCB ট্রিপ করে | লিকেজ ক্ল্যাম্প মিটারে… | … (MCB বারবার ট্রিপ করলে সাধারণত ওভারলোড বা শর্ট সার্কিট)". ৫.৫ note box adds that mA-level leakage needs a leakage clamp meter.
- ✅ ৭.৬ CAT categories standard: ৫.১১ ⚠ box, summary and glossary now cite IEC 61010-2-030 (measurement categories moved out of 61010-1 in the 2010 edition).
- ✅ ৭.৭ "বাধ্যতামূলক" (৫.৯): now "IEC 60364-6 অনুযায়ী নতুন ওয়্যারিং চালুর আগে যে যাচাই করতে হয়, এই পরীক্ষা তার অংশ"; ৫.৯ note box's "পরিসরের বাইরে" sentence replaced with the verified minimum: circuits up to 500 V tested at 500 V DC, insulation resistance ≥ 1 MΩ.
- ✅ ৭.৮ ৫.১০ box "বিল হিসাব… পরিসরের বাইরে" (contradicts ch03) → points back to ch03 ৩.৬ / উদাহরণ ৩.৪ (checked: present). Same contradiction also fixed inside ch03.
- ✅ ৭.৯ Megger: ৫.৯ now introduces "ইনসুলেশন রেজিস্ট্যান্স টেস্টার", says Megger is a company name, test voltages ২৫০/৫০০/১০০০ V DC; glossary row adjusted.
- ✅ ৭.১০ ৫.৮ ⚠ body resistance "যোগ হয়ে" → body is in parallel, reading comes out low; "মিটার নষ্ট হয়ে যাবে" → "নষ্ট হতে পারে".
- ✅ ৭.১১ সারণি ৫.৩ "ডিজিটাল: তুলনামূলক দামি" → "দাম মান অনুযায়ী; ভালো মানের মিটার টেকসই".
- ✅ ৭.১২ ৫.৫ list "উপযুক্ত মানের ব্রেকার নির্বাচন" → "ব্রেকারের রেটিংয়ের সঙ্গে মিলিয়ে দেখা".
- ✅ House-wiring leftovers: "ওয়্যারিং কর্মীর ব্যাগে" → "ইলেকট্রিশিয়ানের ব্যাগে"; summary "ওয়্যারিংয়ের প্রতিটি সিদ্ধান্ত" → "বৈদ্যুতিক কাজের…"; diagram d01 note strip "হাউস ওয়্যারিংয়ের কাজে" → "বৈদ্যুতিক কাজে".
- ✅ Safety on practicals: ৫.৭.১ step ১ adds two-pole dead check before opening the circuit; practical table row ২ (live socket) "(প্রশিক্ষকের তত্ত্বাবধানে)", row ৩ "সরবরাহ বন্ধ ও ডেড যাচাই করে…", row ৫ "বাতির ফিলামেন্টের (ঠান্ডা অবস্থায়)", row ৭ "সরবরাহ বিচ্ছিন্ন করে মেগার দিয়ে…".
- ⏭ ৭.১৩ MCQ key already balanced (ক৪/খ৪/গ৪/ঘ৪); all single-answer. No change.
- ⏭ ৭.১৪ "আগের অধ্যায়ে" → "অধ্যায় ৪-এ": correct as is; wording only, stage 2.
- ⏭ Missing গাণিতিক সমস্যা section, glossary merges, box-type changes, objectives — structure, stage 2.

## Sources
- IEC 61010-2-030 holds the measurement categories (moved from IEC 61010-1:2010): https://webstore.iec.ch/publication/75915 ; HBM note GN610/GN611 https://www.Hbm.com/fileadmin/mediapool/files/GN610_GN611_Isolation_and_type_testing.pdf
- IEC 60364-6 Table 6.1 (≤500 V circuits: 500 V DC test, ≥1 MΩ) — secondary sources agree: https://uk.rs-online.com/web/content/discovery/ideas-and-advice/insulation-resistance-testing , https://nen.sulerr.com/en/guides/nen-3140/isolatieweerstandsmeting , https://community.se.com/t5/Expert-on-Demand-for-Standards/Perhitungan-Tahanan-Isolasi/td-p/361359 (the primary IEC text is paywalled; the VDE preview could not be fetched through the proxy). Only the ≤500 V row is quoted in the book.

## Layout (layout.py 4.5)
- Before: 21 pp, zero gaps.
- After: 21 pp, zero gaps; figures 11 / tables 8 unchanged; mathguard clean; qc.py dia_ch05 0 problems.

## Author decision
- The IEC 60364-6 1 MΩ figure is from consistent secondary sources; confirm against the standard if the institute holds a copy.
