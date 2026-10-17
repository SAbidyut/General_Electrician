# ch08 (ম্যাগনেটিক কন্টাক্টর) — stage 1 fixes

Files touched: `Book/build/ch08.py`, `Book/build/dia_ch08.py`, `Book/build/assets_ch08.py`,
`Book/build/assets/ch08/credits.json`. Backups of the pre-edit sources:
`/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/ch08_bak/`.
Rebuilt `out/অধ্যায়-০৮ — ম্যাগনেটিক কন্টাক্টর.docx` and the PDF. The copies in `Book/` and
`Book/অধ্যায়-08/` were **not** updated (the brief did not ask for it).

## Review section 7 items

| # | Item | Result |
|---|---|---|
| 1 | Intro: forward ref to ch13 | ✅ Removed "অধ্যায় ১৩-এ…" and replaced it with a standalone line: float-switch pump panels also use this contactor. No chapter number. |
| 2 | ৮.২.১(২): "অধ্যায় ৭-এ মোটরের কোর…" | ⏭ Not in the current source. The sentence already reads "মোটরের স্টেটর আর ট্রান্সফরমারের কোরও একই কারণে…" with no chapter reference. |
| 3 | Forward refs to ch9 (৮.৪.২, ৮.৭, ৮.১০-৭) | ✅ All three rewritten to stand alone. ৮.১০(৭) now says that a motor over 0.376 kW needs overcurrent protection such as an overload relay, as required by BNBC 1.3.27(গ). |
| 4 | Back refs (ex 7.4, ৬.৭, ch05, ch01) | ⏭ Re-checked and all are correct (ch07 example 4 = 7.37 A; ch06 ৬.৭.২; ch05 continuity; ch01 ১.৮ LOTO). |
| 5 | Table 8.3 lists incandescent lamps under AC-1; ৮.৫.১ uses "বাতি" | ✅ AC-1 example is now "হিটার, রেজিস্ট্যান্স ফার্নেস". ৮.৫.১ says হিটার instead of বাতি (lamps are AC-5b). |
| 6 | ৮.২.৩: arc chute explanation was backwards | ✅ Rewritten: the arc splits into short arcs in series, each with its own voltage drop, so the total arc voltage exceeds the supply voltage. The plates also absorb heat, and the arc goes out at current zero. |
| 7 | "Electrically separate" (৮.১.২, summary, fig 8.1) | ✅ The text now says there is no wire between the coil and the main contacts, but the control supply is usually a phase and neutral from the same line. Only a control transformer (সারণি ৮.৫) isolates the two. Summary bullet 2, the fig 8.1 caption and the d01 title are reworded to match. |
| 8 | Table 8.4 HP column vs the chapter's kW rule | ✅ The column header now says "(প্রায়)". A note after উদাহরণ ৮.৩ explains that HP figures are trade names (7.5 HP = 5.6 kW, but the nameplate says 5.5 kW). Students should match the nameplate kW and take the next size up if it exceeds the contactor's kW. |
| 9 | উদাহরণ ৮.৪ note: "৩.৭ kW", "চার গুণেরও বেশি" | ✅ Now reads "4 kW (AC-3) … প্রায় 15 kW; তফাত প্রায় চার গুণ". |
| 10 | ৮.৬: "230 V-এ ৪ kW, 400 V-এ ৭.৫ kW" (18 A figures) | ✅ Replaced with the 9 A contactor actually under discussion: LC1D09 is 2.2 kW at 230 V and 4 kW at 400 V. |
| 11 | ৮.৫.৩ modular contactor: pump in the list; AC-7b | ✅ Pump removed. AC-7b (small household motors) is mentioned, with the iCT example (AC-7a 25 A against AC-7b 8.5 A). The unverified "ছ'মাসের মাথায়" is softened. Summary now says "কারখানার মোটরের জন্য নয়". |
| 12 | ৮.৮.৩ box ("pumps, even convenient") vs BNBC 1.3.27(ঘ) | ✅ The box now quotes the clause's real exception: an automatic control device starting a motor at intervals is allowed if other adequate precautions are taken (wording taken from ch13's verified quote). It states that a hand-operated selector is not such a device. In সারণি ৮.৭ the "কোথায় চলে" entry now reads "বাতির গ্রুপ; স্বয়ংক্রিয় নিয়ন্ত্রকে চলা পাম্প (শর্তসাপেক্ষে)". The docstring records the clause. |
| 13 | "একশো বছর", "পৃথিবীর প্রতিটি মোটর-প্যানেলে" | ✅ Both removed (intro and ৮.৯). |
| 14 | ৮.২.১ box: "পোল দেরিতে বন্ধ হলে সিঙ্গেল ফেজিং" | ✅ Now "কোনো একটি পোলের কন্টাক্ট ক্ষয়ে গেলে বা ঠিকমতো না লাগলে". |
| 15 | ৮.১০(৪): wrong reason for a separate control fuse | ✅ Now: the control wiring is thin and can burn before the large power breaker trips. |
| 16 | সারণি ৮.২ rows 5-6 / 7-8 named only the overload relay | ✅ Now "টাইমারের বিলম্বিত NC (55-56), ওভারলোড রিলের ট্রিপ (95-96)" and the NO equivalent. |
| 17 | Terminal-marking standard cited as IEC 60947-5-1 | ✅ Could not verify the exact part or annex (IEC is paywalled and search was inconclusive), so the text now says "IEC 60947 সিরিজ" in ৮.৪ and in the সারণি ৮.২ caption. |
| 18 | 10×/8× Ie read as every-operation duty (উদাহরণ ৮.২, ৮.৫.২) | ✅ These are now called making and breaking capacity test conditions. The text adds that in normal AC-3 duty the contactor makes the starting current and breaks roughly Ie. উদাহরণ ৮.২ (question, answer, note) and গাণিতিক সমস্যা ৪ are reworded to "ক্ষমতা". This also removes the ch08 vs ch12 "AC-3 breaks 8×" vs "AC-4 breaks 6×" clash. |
| 19 | "পুশ বাটন দিয়ে ৫০ অশ্বশক্তির মোটর", argued from a 9 A coil | ✅ Softened. The claim is now limited to this size of contactor, with a note that big contactors draw much more VA, so the button and fuse should be checked against the datasheet. |
| 20 | ৮.৯.২ box contradicted itself | ✅ Rewritten with the single correct outcome when the two are swapped: START does nothing, and holding STOP runs the motor (traced). |
| 21 | ৮.৯.১ definition grammatically broken | ✅ Rewritten ("…বোতাম ছেড়ে দেওয়ার পরও কন্টাক্টরের কয়েলে সরবরাহ চালু রাখে…"). |
| 22 | "সবুজ ছেঁড়া রেখা" | ✅ Now "সবুজ ড্যাশ রেখা" in both the text and the d14 note strip (the lines are dashed). |
| 23 | "সারণির শেষ সারিটি" pointed at the wrong row | ✅ Now names the "মোটর চালানো যায়" row. The odd "(সবই অক্সিলিয়ারি)" for a relay is now "সবই ছোট মাপের". |
| 24 | ৮.২.১(৩): armature is "the only moving part" | ✅ Now: the magnet pulls the armature, and the carrier and contact bridge move with it. |

## Other factual and consistency items (section 6, old review, brief)

- ✅ **Starting current**: ৮.১.১ and ৮.৫.১ both now say "ফুল-লোড কারেন্টের ৬ থেকে ৮ গুণ".
- ✅ **Practical tasks**: every wiring row now says to switch the supply off and verify it dead with a tester before wiring or removing wires. "পাওয়ার সার্কিট" is now under teacher supervision. "ল্যাচিং সার্কিট" now lists a fuse or MCB. The whole table was moved from তুমি to করুন.
- ✅ **MCQ 1** now asks about the "মেইন কন্টাক্ট". Without that, NC auxiliaries close by spring and "স্প্রিং" was arguable.
- ✅ **MCQ 10**: "নয়" is bold.
- ✅ **MCQ key**: unchanged and balanced (ক3 খ2 গ2 ঘ3), one answer each.
- ✅ **Glossary**: স্থির কোর → "মাঝের বাহুতে"; শেডিং রিং → "তামা বা পিতলের"; সিঙ্গেল ফেজিং → "গরম হয়ে পুড়ে যেতে পারে"; বর্তনী → সার্কিট in two definitions.
- ✅ **Photo credit**: "Julo (talk · contribs)" is now "Julo" in `credits.json`. `assets_ch08.py` now strips that pattern in both the metadata reader and the credits writer, so a re-run (even from the old metadata cache) cannot bring it back. The merged book's চিত্রসূত্র reads the same JSON.
- ⏭ **Figure placement** (move চিত্র ৮.১৩ / ৮.১৯ right photo): this is structure, not an error. Left for stage 2.

## Diagram fixes (dia_ch08.py)

All diagrams were regenerated and rendered. `qc.py dia_ch08` reports 0 problems, and every changed PNG was checked by eye.

- **d14_wiring** was redrawn with a wire list in its docstring. It now has **zero crossings**, so neither dots nor hops are needed. (ch12's `join_bus` and ch14's `hop_line` import `dia_ch08`, so importing them back would be circular.) The redraw also fixed three real errors in the old drawing:
  1. L1, L2 and L3 were joined by one horizontal bar, which is a phase-to-phase short. The same was true of 2, 4 and 6.
  2. The control L landed on the STOP box, not on terminal 11.
  3. The STOP 12 → START 13 wire ran through START 14's riser with no dot, which reads as START bridged.

  The button terminals now face the contactor. Traced: L → 11; 12 → START 13 ← KM1 13; START 14 ← KM1 14; START 14 → A1; A2 → N.
- **d10_power** and **d01_idea** (not in the brief, found while checking): both drew the three phases joined by one horizontal line. In d10 this was the supply rail and the motor feed; in d01 it was the motor feed. Both are dead shorts. They now use separate leads to separate motor terminals and three separate supply leads. d01's title no longer claims the circuits are "আলাদা".
- **d15_faults**: re-measured on a 0.05 grid overlay.
  - "রুপোর টিপ ক্ষয়ে গেছে" now points at the pitted silver pad on the left pole's bridge (0.20, 0.46). It used to point at the copper edge (0.24, 0.62).
  - "তামা কালো হয়ে গেছে" used to point at grey moulding. It now points at the blackened copper around the right pole's lower screw hole and moved to the right column.
  - "ধাতু ছিটকে জমেছে" now points at the white spatter (0.775, 0.327).
  - "অক্সিলিয়ারি ব্লক" used to point at shadow under the block (0.90, 0.45). It now points onto the LADN body (0.93, 0.36).
  - Labels are sorted by target height, so no leaders cross.

## Sources for verified numbers

Only web search was available; WebFetch and curl were blocked by DNS or proxy 403, so these were checked through search-result text.

- LC1D09: AC-3 2.2 kW at 220–230 V, 4 kW at 380–400 V. Schneider datasheets, e.g. https://www.ottofischer.ch/pim/aa8f0735-464b-4b72-b13d-9b9d0bfbd562/LC1D09FD.pdf and https://docs.rs-online.com/bae4/A700000015228758.pdf
- Acti9 iCT 25 A: AC-7a 25 A, AC-7b 8.5 A, IEC/EN 61095. https://eshop.se.com/id/acti-9-ict-25a-2nc-230-240v-50hz-contactor-a9c20736.html
- AC-3 making/breaking capacity 10/8 × Ie versus normal duty about 6 × Ie make and 1 × Ie break; AC-5b = incandescent lamps:
  - Fuji AEH281a (IEC 60947-4-1 table) https://www.th.fujielectric.com/en/products/AEH281a.pdf
  - Asbeam https://asbeam.com/news/528-cn.html
  - Lowag https://www.lowag.com.tr/en/2026/10/03/contactor-utilization-categories-ac1-ac3-ac4/
- BNBC 1.3.27(ঘ) exception text: taken from ch13.py's docstring (verified there against the law.resource.org PDF).
- Terminal-marking standard (IEC 60947-1 Annex L?): **not verified**, so it is written only as "IEC 60947 সিরিজ".

## Layout

- Before: 34 pages, no gap > 4.5 cm.
- After: **34 pages, no gap > 4.5 cm**.
- The first build after the edits was 36 pages with 8 gaps. They were closed by keeping the intro at its old length (a standalone float-switch line replaced the ch13 reference), condensing the arc-chute text, and moving the HP note from after সারণি ৮.৪ to after উদাহরণ ৮.৩.

## For the author

1. **The diagram shorts.** d01, d10 and d14 had all three phases drawn on one common wire. This was a real error in the shipped figures, not a style issue, and it may also exist in other chapters that copied the shape. The ch08 versions are fixed; other chapters were not checked.
2. **Headings and register.** The heading "৮.১.২ দুই বর্তনীর ভাগাভাগি" and the তুমি steps in ৮.৬ were left for stage 2 (style). Only the practical table was converted, because every row there needed a safety edit anyway.
3. **Delivery copies.** `Book/অধ্যায়-০৮ — ….docx` and `Book/অধ্যায়-08/` (PDF and SVGs) still hold the old version. Copy the new build across once all stage-1 work is accepted.
