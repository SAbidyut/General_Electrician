# Stage-1 fixes — অধ্যায় ১২ (Forward-Reverse Starter)

Source changed: `Book/build/ch12.py` only (no diagram changes needed). Backup of the pre-edit file:
`/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/bak1112/ch12.py`

## Items (review/ch12.md §৭ + review_2026-09-23.md ch12 + caller's brief)

- ✅ **৫ / old CONSISTENCY ch08↔ch12 (caller's item)**: সারণি ১২.৬'s column now reads "স্বাভাবিক কাজে যে কারেন্ট ভাঙতে হয়". One sentence after the table explains the difference. ch08 ৮.৫.২'s AC-3 "৮ × Ie" is the breaking-capacity test value, for occasional extreme conditions. Ie and 6 × Ie here are normal everyday-duty values. The bases differ, so the numbers do not contradict each other.
- ✅ **৩ (caller's item, duplicated paragraph after চিত্র ১২.১৩)**: this was already gone in the current source. I checked the built .docx: only one paragraph follows চিত্র ১২.১৩, and "সে আলোচনা ১২.৯-এ" no longer appears anywhere.
- ✅ **৪ (caller's item, "একই কোড থেকে আঁকা")**: removed. The paragraph after চিত্র ১২.১১ now just says the motor is running in reverse and the live path goes through the lower rung to KM2.
- ✅ ১ (১২.৬.২, wrong claim that the NC must sit before the latch): the bullet now says the opposite button's NC is in series with the coil, outside the holding-contact parallel branch, so before or after works. Summary bullet ৮ was corrected. **MCQ ৯** had two defensible answers. It now asks how the NC connects to its own coil, and the answer is (ক) সিরিজে. MCQ ৭'s correct option moved to (খ). New key: ক৩ খ৩ গ২ ঘ২.
- ⏭ ২ ("বন্ধনীর এই কথাটাই আসল"): the current source already reads "শেষের এই কথাটাই আসল", which is a style point for stage 2.
- ✅ ৬ (plastic vs metal lever): ১২.৪.৩ now reads "ছোট যন্ত্রাংশ… যান্ত্রিক দোলনা লিভার", and ১২.৪.৪ reads "কেবল যান্ত্রিক লিভারটাই". In the ✔ box, the unverified claim "যত ভেতরের… তত দেরিতে কাজ করে" was removed and "ধাতু দিয়ে" became "যান্ত্রিকভাবে". The box was kept only as one line, because the page layout needed it.
- ✅ ৭ (✔ box ১২.৯): stopping time is now measured with the load coupled ("লোডসহ"). Uncoupling removes the load's inertia and gives too short a time.
- ✅ ৮ / old [UNVERIFIED] (উদাহরণ ১২.২): "দুই ধাপ বড়" was removed. The answer now says to pick a contactor whose catalogue AC-4 rating is at least 3.7 kW. প্রদত্ত/নির্ণেয় are in Bangla, as are উদাহরণ ১২.১'s.
- ✅ ৯ (সারণি ১২.২ and the mirror box): (ক) LAD9R1V was verified as a full reversing kit: LAD9V2 mechanical interlock, LAD9V1 electrical interlock, and parallel and reverser power bars. The row now says so. (খ) 3RA2913-2AA1 was left as is, since the docstring quotes Siemens: "Wiring kit … Electrical and mechanical, Including mechanical interlocking for reversing starter". (গ) "31-32 বা 41-42" became "সামনে লাগানো বাড়তি অক্সিলিয়ারি ব্লকের NC-তে নয়"; Schneider's FAQ recommends the built-in NC over front add-on blocks.
- ✅ ১০ (১২.৩ "স্বয়ংক্রিয়"): now reads "বোতাম চেপে দিক বদলানোর জন্য দুটি কন্টাক্টর ব্যবহার করা হয়".
- ✅ ১১ (counts): ১২.৬.১ "চারটি জিনিস" was reworded as a list. The panel-door paragraph now names its five items. ১২.৫ "একটি তারই" became "তিনটি তার". Terminal numbers in ১২.৫ are now Latin digits.
- ✅ ১২ (সারণি ১২.৪ step ৫): REV's NO is closed from the moment of pressing, and KM2's coil gets supply once KM1 21-22 closes.
- ✅ ১৩ (সারণি ১২.৭): "কন্টাক্টর ও রিলে AC-4" became "কন্টাক্টর AC-4 অনুযায়ী বাছুন". Overload relays have no AC-4 rating.
- ✅ ১৪ (১২.৮ slip): now defined and qualified ("স্টার্টের মুহূর্তের প্রায় দ্বিগুণ", current "সমান বা কিছুটা বেশি").
- ✅ ১৫ ("তিনটিই বদলালে কিছুই হয় না"): the ১২.২ box, summary bullet ১ and short question ২ now say "চক্রাকারে এক ঘর করে সরালে দিক বদলায় না".
- ⏭ ১৬: cross-references were already verified correct. No forward references.
- ✅ ১৭ (math problem ৪): uses টানতে/ছাড়তে for the contactor and "মেইন কন্টাক্ট একসঙ্গে বন্ধ" for the contact. Latin ms. ১২.৪.৪ and essay ৫ also use টানা/ছাড়া for the 12–22 / 4–19 ms figures.
- ✅ ১৮ (math problem ৩): "ধরে নিন" added for the half-rating assumption.
- ✅ Old [SAFETY] (practical ৫): Q1 must now be off and proven dead, with the motor disconnected and control supply only. The task also warns not to hold the button more than a few seconds, because a blocked coil heats, and says to switch control supply off before refitting the wire. A line before the practical list says to switch off and prove dead before any wiring change.
- ✅ Old [MINOR] (সারণি ১২.৫ "মোটরের দুই তার বদলান" vs "line leads, not motor leads"): now "টার্মিনাল ব্লকে দুই তার বদলান". The ✔ box below it adds "সরবরাহ বন্ধ করে".
- ⏭ Old [FORMAT] (MCQ key without box, practicals as a list) and the rest of §১–৬: stage-2 style.

## Sources
- Schneider FAQ FA142116 (LC1D09–LC1D95 21-22 is a mirror contact; prefer the built-in NC to add-on blocks): https://www.se.com/uk/en/faqs/FA142116
- IEC 60947-4-1 Annex F = mirror contact: https://cache.industry.siemens.com/dl/files/261/109758261/att_1019182/v1/Positivelydriven_mirror_contact_V3_0_en.pdf
- LAD9R1V contents (mechanical LAD9V2 + electrical LAD9V1 + LAD9V5/LAD9V6 bars): https://eezee.sg/product/schneider-electric-lad9r1v-kit-for-assembling-3p-reversing-contactors-lc1d09-d38-with-screw-clamp-terminals-with-electrical-interlock-0cc72c5c12 ; https://www.steinerelectric.com/Product/Schneider-Electric-LAD9R1V-Reversing-Contactor-Kit-With-Interlock32-A-Max-Load3-Poles-57156
- AC-3 breaks Ie / AC-4 6 × Ie (normal duty): ABB 1SAC200017M0002, already quoted in the ch12 docstring. ch08's 10 × / 8 × Ie (capacity test): CHiNT NXC, already quoted in ch08.

## Layout
- Before: 27 pages, no gap > 4.5 cm.
- After: 27 pages, no gap > 4.5 cm. The first build after the edits had two gaps (p10 4.95 cm, p17 7.27 cm). They were closed by reordering, not shrinking: চিত্র ১২.১২ (panel layout) and its paragraph moved up to the start of ১২.৭, right after the paragraph that describes that layout; the ✔ box in ১২.৪.৪ was kept as one line.
- mathguard: clean.

## Needs the author's decision
- Diagram d09 (চিত্র ১২.৭, panel ১) says the button's NC and NO act "একসঙ্গে, তাই একটির আগে অন্যটি হয় না". The text in ১২.৪.১ says the NC opens first, then the NO closes, and ১২.৪.৪ says "প্রায় একই মুহূর্তে". This is a minor inconsistency that the review did not raise, and I did not touch it. Real push-button blocks are usually break-before-make; if the author agrees, the diagram label should change.
- MCQ key format ("১—ক" paragraph vs ch11's ✔ box) was left for stage 2.
