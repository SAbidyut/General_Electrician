# ch14 (স্টার-ডেল্টা স্টার্টার): stage-1 fixes

Files changed: `Book/build/ch14.py`, `Book/build/dia_ch14.py` (d14 label and docstring only). Backups of both files from before the pass: `/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/bak14/`.

## Review file, section ৭
1. ✅ **KM3 two-wire swap (১৪.৫.৩ safety box, fault table row).** I checked the review's analysis against সারণি ১৪.৩, and it is right. Swapping any two of KM3's wires puts the same phase on both ends of one coil, so that coil gets 0 V. The other two coils sit across the same two lines in opposite directions. The result is a single-phasing condition, not a reversal or plugging. Rewrote the box, removed the "প্লাগিং (অধ্যায় ১২-এর ১২.৮)" reference, and changed the fault row to "ডেল্টায় বদলের সময় জোরে ঝাঁকুনি, বড় কারেন্ট ও ট্রিপ / একটি কয়েল ভোল্টেজ পায় না". The same wrong claim in the dia_ch14 docstring is also corrected.
2. ✅ **A16 ≠ 16 A (১৪.৯, paragraph after সারণি ১৪.৫).** Now reads: the model number is not the rating; ABB A16's AC-3 rating at 400 V is 17 A (7.5 kW), close to the calculated 17.4 A; "নিজে কিনলে পরের মাপটি নেওয়া নিরাপদ" kept. Removed the unsourced explanation that "AC-3 depends on breaking current, star-delta breaks less". উদাহরণ ১৪.৩'s "18 A বা তার বড়" agrees with this rounding-up rule and is left as is.
3. ✅ **Fault row "কিছুক্ষণ চলার পর ওভারলোড ট্রিপ" (১৪.১২).** Cause is now "রিলে মূল লাইনে বসানো অথচ 0.58 × In-এ সেট করা, বা ট্রিপ ক্লাস ছোট". Remedy is now "রিলে ডেল্টার শাখায় (KM1-এর নিচে) সরান; …ক্লাস ২০". The tip after the table now says "মূলে একই ভুল: রিলের অবস্থান আর সেটিং মেলেনি".
4. ✅ **Step 3 "পাওয়ার তার আগে" vs the safety box (১৪.১০.২).** I went further than the review's "মোটরের তার" wording, because the box was also wrong on the physics. It claimed disconnecting the motor makes the control test safe. But the KM2+KM3 short runs only through the poles of KM3 and KM2, not through the motor. So the first test (table row 1 and the box) is now done **with Q1 off and 230 V fed only to the control circuit at F1**. The box now ends "…তবেই Q1 চালু করুন", which no longer contradicts step 3.
5. ✅ **Practical task 3 and the interlock row of সারণি ১৪.৬.** The test now runs with Q1 off, control supply only, in the delta state (after t1). An insulated tool presses KM2's armature, and KM3 should drop out. Then, with the supply off, a temporary jumper bypasses **KM2's** 21-22 and the test is repeated. The jumper is removed afterwards with the supply off.
6. ✅ **Starting-current multiple.** The intro now says "ফুল-লোড কারেন্টের ৬ থেকে ৮ গুণ". সারণি ১৪.৭ now gives DOL 6–8 গুণ and star-delta 2–2.7 গুণ. Also fixed in সারণি ১৪.৬: the "স্টারের কারেন্ট" row said "প্রায় দ্বিগুণ" and now says "চালুর মুহূর্তে … প্রায় ২ থেকে ২.৭ গুণ".
7. ✅ **"৫৮ / ৩৩ শতাংশ" of what (১৪.১ and ১৪.৯).** Both places now say "মোটরের ফুল-লোড কারেন্টের ৫৮ / ৩৩ শতাংশ (০.৫৮ গুণ / এক-তৃতীয়াংশ)".
8. ✅ **Mixed sources (১৪.৭.২).** The 50 ms value is credited to the CT-SDS.23 datasheet. The reason (it prevents arc short-circuits) is now credited to ABB's starting-combinations catalogue.
9. ✅ **Unverified "লিখিতভাবে নিষিদ্ধ" (১৪.৩.৩).** Softened to "সংযোগ নেওয়ার আগে বিতরণকারী প্রতিষ্ঠানের শর্ত জেনে নিন; কোনো কোনো প্রতিষ্ঠান … শর্ত দেয়".
10. ✅ **Coil start and end ends (১৪.২.১ tip).** Added: a continuity test does not show which end is U1 and which is U2. A coil connected backwards unbalances the motor. If the ends are unmarked, a separate polarity test is needed.
11. ⏭ **Cross-references: no change needed.** I checked 6.7.1, 7.10, 8.6, 8.9, 9.1.2 (which says ৬-৮ গুণ), 9.5.2, 9.6, 10.5.1, 12.4 and 12.4.2. All exist in earlier chapters. The 12.8 reference was removed under item 1.
12. ⏭ **"strúçture" in the credit.** This is the original Commons title, not an error. Adding "[sic]" is the author's call.

## Older review (review_2026-09-23.md)
- ✅ **KM3 feed order (১৪.১০.১ steps 3 and 5).** Step 5 read literally said "2→W2", which contradicted the figure. The steps now give the mapping explicitly. KM3's 1, 3, 5 take L3, L2, L1, in reverse order as in চিত্র ১৪.N (the number is interpolated, not typed). KM3's 2, 4, 6 go to V2, U2, W2. The step also restates L1→W2, L2→U2, L3→V2. I checked this against the d08 render.
- ✅ **Overclaim (১৪.৪).** "নেমপ্লেটে … সবসময় দুটি সংখ্যায়" is now "ছয় প্রান্তের মোটরের নেমপ্লেটে … সাধারণত দুটি সংখ্যায়".
- A16, practical 3, and the 6-7 vs 6-8 items are covered above.

## Additional errors found while reading
- ✅ **১৪.৭ note box.** It said wiring the timer rungs off STOP 12 would "not be dangerous". Corrected: in that case KM3 would also pull in after t1 and put voltage on all six terminals of a motor that is standing still.
- ✅ **১৪.৮.২ tip.** It said a CT-SDS.23 drops in and "everything else stays identical". But the CT-SDS.23 needs a 380-440 V AC supply, and this chapter's control circuit runs L-N at 230 V. Added that a 230 V control circuit needs the CT-SDS.22 (24-240 V AC).
- ✅ **১৪.৩.১ note box.** The 80 % speed note claimed that switching early gives current "সরাসরি চালুর সমানই". Softened to "প্রায় … কাছাকাছি", and "প্রায় থেমে থাকা" became "কম গতিতেই".
- ✅ **১৪.১১.১.** It said "this circuit" opens for 50 ms, but the chapter's AH3 circuit has no fixed gap. Now reads "অল্প সময়ের জন্য (CT-SDS.23-এ ৫০ মিলিসেকেন্ড)".
- ✅ **Fault table row "সঙ্গে সঙ্গে Q1 ট্রিপ".** Changed to "বদলের মুহূর্তে Q1 ট্রিপ". A missing interlock shows up at changeover, not when START is pressed.
- ✅ **Supply OFF in practicals.** Tasks 1, 2 and 4 now say the supply is off (and verified dead) before wiring work. Task 3 is covered above. Tasks 5 and 6 only measure or turn a dial.
- ✅ **MCQ and short questions.** MCQ 1 now asks "কত গুণ পায়" instead of "কত অংশ পায়". Short question 4 no longer says "অর্ধেকে নয়". The MCQ key is unchanged and balanced: ক3 খ3 গ2 ঘ2.

## Diagram: d14_wiring crossings (CLAUDE.md open item)
- ⏭ **No crossings to fix.** d14_wiring draws no wires at all: just device boxes on the back-plate, the door, and the 11-row wire list. So there is nowhere a dot or a hop could go. The CLAUDE.md note does not match the current figure. The power-circuit figures (d06/d07/d08) already use `hop_line()` at all three unavoidable crossings, and I checked the d08 render by eye.
- ✅ **d14 timer label.** The KT box was labelled "স্টার-ডেল্টা টাইমার", but the wire list uses AH3 pins (2, 7, 8-5, 8-6). Relabelled "অন-ডিলে টাইমার".
- `dia_ch14.py` was regenerated and d14 re-rendered. `qc.py dia_ch14` reports 0 problems, and I looked at the d14 PNG. `mathguard.py ch14.py` is clean.

## Sources
- ABB A16-30-10, AC-3 17 A / 7.5 kW at 380-400 V: https://shop.in.abb.com/1sbl181001r8610/a16-30-10-400-415v-50hz-415-440v-60hz-contactor.html and https://www.radiolocman.com/datasheet/data.html?di=67538 (I saw these in search results; the ABB shop host could not be resolved from this sandbox.)
- ABB CT-SDS.23 supply 380-440 V AC: https://empower.abb.com/ecatalog/ec/EN_NA/p/1SVR730211R2300 and https://uk.rs-online.com/web/p/timer-relays/7467037
- ABB CT-SDS.22 supply 24-48 V DC / 24-240 V AC: https://library.e.abb.com/public/f994091a552b84f8c125771f00410b32/2CDC111093D0201.pdf and https://kvc.com.my/Products/Automation-and-Control/Relays/Timing-Relay/CT-SDS22S-TIME-RELAY-STAR-DELTA-2NO-24-48VDC-24-240VAC-zid2264461

## Layout
- Before: 35 pages, no gaps.
- After: 36 pages, no gaps over 4.5 cm (`layout.py` ✓). The added safety and polarity text pushed the last exercise items onto page 36.

## For the author
- The book now prescribes testing the control circuit with Q1 off and a separate 230 V control feed at F1. If your training panels take control L from after Q1, they need a temporary control supply for this test. Please confirm this suits your workshop.
- The chapter went from 35 to 36 pages. If the page count matters, stage 2's prose tightening should bring it back.
