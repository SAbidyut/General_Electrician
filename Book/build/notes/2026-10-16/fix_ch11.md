# Stage-1 fixes — অধ্যায় ১১ (ATS)

Source changed: `Book/build/ch11.py` only (no diagram changes needed). Backup of the pre-edit file:
`/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/bak1112/ch11.py`

## Items (review/ch11.md §৭ + review_2026-09-23.md ch11 + caller's brief)

- ✅ **৮ / old-review CONSISTENCY ch11↔ch12 (main item)**: সারণি ১১.১ row 1 no longer claims the electrical interlock fails on welded contacts. It now lists the real failure modes (wire off, wrong terminal, armature pressed by hand). A new sentence after the table says that if the interlock NC is a **mirror contact** (IEC 60947-4-1; 21-22 on many contactors), a welded main contact keeps it open and the other contactor cannot pull in. This matches ch12 ১২.৪.২. Rows 2–3 were tightened (mechanical interlock: stuck coil can burn; "both together": no notable limitation). The fault-table row "দুই কন্টাক্টরই একসঙ্গে টানল" now says "কন্টাক্ট জোড়া লেগে গেছে, আর ইন্টারলকের NC মিরর কন্টাক্ট নয়". The summary bullet adds the mirror-contact clause.
- ✅ ১ (১১.৩.৩): the wrong "অধ্যায় ৮-এর ৮.৭" claim ("কন্টাক্টর সুরক্ষা-যন্ত্র নয়") was removed. ch08 says nothing about short circuits. The paragraph now stands on its own.
- ✅ ২ (১১.৪.১): reference changed from "অধ্যায় ৯-এর ৯.২.২" to "অধ্যায় ৭-এর ৭.৯.৩", which is where single phasing is explained (checked in ch07.py, line 580).
- ⏭ ৩ (উদাহরণ ১১.৪ → ৬.৭.১): already correct in the current source.
- ⏭ ৪ (সারণি ১১.৮ → ৮.১১): already correct in the current source.
- ⏭ ৫ (উদাহরণ ১১.৪ neutral explanation): already rewritten correctly in the current source (phase on VSS N gives 400 V; broken N gives zero or an unstable reading).
- ✅ ৬ (১১.৯.২, ১১.৯.৫): no fuse in the neutral. Only the three phases go through fuses/MCB; N goes direct.
- ✅ ৭ (CT ✔ box, ১১.৯.৩): the box now says to switch off load and supply before reversing a CT, or to swap S1/S2 at the meter.
- ✅ ৯ (সারণি ১১.৩, KA1 box): KA1 is now "কন্টাক্টর রিলে বা ছোট কন্টাক্টর". The box names all three bridging contacts (KA1, KM1, KM2 21-22) and says a plain plug-in relay is not used.
- ✅ ১০ (১১.১ vs ১১.৪.১): "ভোল্টেজ ঠিক আছে কি না" was removed from ATS function 1. "তিনটিই সমান জরুরি" contradicted the next sentence and was removed too. ১১.৪.১'s last paragraph now matches the 0.6 × UN threshold (it checks that each phase is above about 60 % of nominal, not ordinary fluctuations).
- ✅ ১১ (230 vs 231 V): সারণি ১১.৬ keeps "প্রায় ২৩০ V". উদাহরণ ১১.৪'s answer adds "নামমাত্র মান হিসেবে ২৩০ V". The summary reads "প্রায় ২৩০ V (হিসাবে ২৩১ V)". MCQ ৯ option খ reads "প্রায় ২৩০ V".
- ✅ ১২ (১১.৮.১ step 3): L3 added.
- ✅ ১৩ (১১.৮.২ step 7): rewritten as the hand test it actually is, done with both sources off. The meaningless "কন্টিনিউইটি মোডে" was dropped.
- ⏭ ১৪ (÷ in উদাহরণ ১১.৩): already "/" in the current source.
- ✅ ১৫ (১১.৯.১): moving-iron now reads "সাধারণ বিকৃত তরঙ্গেও মোটামুটি RMS মান দেখায়".
- ✅ ১৬ (১১.৯.৩): the CT secondary now reads "সাধারণত 5 A, কখনো 1 A" (summary bullet too).
- ✅ ১৭ (back-feed box): the unsourced "মারাত্মক অপরাধ এবং আত্মহত্যার শামিল" became "অত্যন্ত বিপজ্জনক; এ কাজ কখনোই করবেন না".
- ✅ ১৮ (১১.৭): the dead time is now "সাধারণত কয়েক সেকেন্ড থেকে আধা মিনিট" for auto-start, "হাতে চালু করলে আরও বেশি".
- ✅ ১৯ (উদাহরণ ১১.২): "স্টার-ডেল্টা স্টার্টার" (a ch14 topic) became "কম স্টার্টিং কারেন্টের স্টার্টার".
- ✅ ২০ / old [VERIFY] (সারণি ১১.২): PC now reads "শর্ট-সার্কিট অবস্থায় সংযোগ (make) করতে ও সহ্য করতে পারে, কিন্তু কাটতে পারে না". CC lost the unsourced "বিশ্রামের অবস্থান একটিই" and now reads "কন্টাক্টর দিয়ে তৈরি". The docstring was updated to match.
- ✅ ২১ (MCQ ৬, ১০): option wording fixed ("জেনারেটর গরম হওয়ার অপেক্ষা", "আর্থ থেকে বিচ্ছিন্ন থাকে"). The key is unchanged and balanced (ক৩ খ৩ গ২ ঘ২).
- ✅ ২২ (সারণি ১১.৮, ammeter row): the remedy is now "সঙ্গে সঙ্গে লোড বন্ধ করুন", with the open-secondary hazard stated.
- ✅ old [MINOR] (উদাহরণ ১১.৬ ρ unit): "0.0172 Ω·mm2/m" added in the question and in প্রদত্ত. The rendered page was checked visually.
- ✅ Glossary: the "ট্রান্সফার সময়" row was dropped because the term is not used in the text. "অনুপাত"'s meaning no longer just repeats the word.
- ✅ Book-wide rule (practicals touching wiring): a line before the practical table says both sources must be off and verified dead. The "ফেজ রিলে" row now says to wire the lamp with supply off, and the fault-finding row says to switch off. While rewriting those cells, the তুমি-forms in that table became করুন-forms and "ফেজ রিলে" became "ফেজ ফেইলিওর রিলে".
- ⏭ The rest of review §১–৬ (headings, word choice, dashes, objectives, summary length, box count) is stage-2 style.

## Sources
- Electropedia / IEC 62683, class PC definition (make and withstand, not break): https://electropedia.org/cdd/iec62683/iec62683.nsf/0/7A9DF13982EDC113C1258D15005AE692
- IEC 60947-4-1 scope (contactors not normally designed to interrupt short-circuit current), via search summary of the standard's scope
- Mirror contact, Schneider FAQ FA142116: https://www.se.com/uk/en/faqs/FA142116
- Annex F = mirror contacts: Siemens "Positively driven / mirror contact": https://cache.industry.siemens.com/dl/files/261/109758261/att_1019182/v1/Positivelydriven_mirror_contact_V3_0_en.pdf

## Layout
- Before: 30 pages, no gap > 4.5 cm.
- After: 30 pages, no gap > 4.5 cm. The first build after the edits gave 31 pages with three gaps. These were closed by shortening the new interlock wording to about its original line count. Nothing was shrunk. The sentence "কন্টাক্টরের ক্যাটালগে এই ব্লক আলাদা যন্ত্রাংশ হিসেবে পাওয়া যায়…" was dropped to make room.
- mathguard: clean.

## Needs the author's decision
- **LC1D65004P7 may have no built-in auxiliary contacts.** A reseller listing says it ships "without built-in auxiliary contact"; I could not reach Schneider's datasheet. Worked example ১১.১ names it as KM1/KM2, yet the whole control circuit uses KM1/KM2 21-22. If the reseller is right, the book should either name a 4-pole contactor that has a built-in NC (mirror) contact, or say that an add-on auxiliary block is needed (its terminal numbers would differ from 21-22). I left the text as is, apart from making the mirror-contact statement conditional ("NC যদি মিরর কন্টাক্ট হয়").
- IEC 60947-6-1 class CC: I could not get the standard's own wording. "কন্টাক্টর দিয়ে তৈরি, শর্ট-সার্কিট কাটে না" rests on the IEC 60947-4-1 scope plus common usage.
