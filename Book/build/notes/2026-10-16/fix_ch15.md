# ch15 — stage-1 fixes (factual / technical / safety / syllabus)

Files touched: `Book/build/ch15.py`, `Book/build/dia_ch15.py` (+ regenerated `diagrams/ch15/*`).
qc.py: 0 problems (15 diagrams). mathguard: clean. Deliverables in `Book/` not re-copied (brief: touch own sources only).

## Items

### Syllabus gap (review ch15 §7.1; old review "SYLLABUS GAP")
- ✅ **New section ১৫.১০ "স্টার-ডেল্টা মোটর কন্ট্রোল প্র্যাকটিস"** (before সারসংক্ষেপ; summary/glossary/exercises renumbered ১৫.১১/১৫.১২/১৫.১৩):
  - ১৫.১০.১ বাসবার থেকে স্টার্টারে সাপ্লাই: L1–L3 bar → own Q1 → split point → KM1/F2 → U1V1W1 and KM3 → W2U2V2, KM2 on the same nodes. Two rules: KM3 must be fed from Q1's output, never a separate busbar tap (else live after Q1 is off, outside Q1's protection, phase order to be matched in two places → plugging at changeover, ref ১৪.৫.৩); conductor up to the split carries full In, branches 0.58 In, KM2 In/3 (ref ১৪.৯). Control return to N bar, never PE; bodies to PE bar.
  - New diagram **d15_sd** (dia_ch15.py): 5-bar set in BNBC colours, three starters tapped off, M1 opened up with In / 0.58 In / In/3 labels, PE to motor body; no wire crossings except tap stubs over lower bars (standard bus convention).
  - ১৫.১০.২ sizing with this chapter's method + **উদাহরণ ১৫.৫**: 72+30+44 = 146 A (motor currents from ch14's ABB table rows 37/15/22 kW), demand factor 1 for motors that run together, +20 % → 175.2 A, closed panel J = 1.2 → 146 mm² → 30 × 5 (150 mm², 180 A at J 1.2); KM1/KM3/F2 = 0.58 × 72 = 41.8 A. Note shows the trap: table 15.3's capacity column is at J 1.6, so 25 × 5 would look fine (200 A) but carries only 150 A at 1.2. Starting current explicitly does not size the bar (star = ⅓ of DOL, few seconds).
  - ১৫.১০.৩ eight practice steps (LOTO + Prove–Test–Prove with two-pole tester; bar ID; tap-off lugs one per hole with spring washer; Q1→KM1/KM3; rest per ১৪.১০.১, F2 at 0.58 In per ১৪.৯.১; N/PE; dead continuity checks; control-only run then supply off before connecting motor) + measurement table (tap-off In, branch ≈0.58×, star start ≈⅓ DOL, bus phase balance, IR joint check per ১৫.৮.৩) + safety box (clamp meter only on live panel; any wire change only after isolate/lock/verify).
  - Also: subtitle line + new 14th objective; intro's false claim "সিলেবাসেও ঠিক ওই দুটিই" replaced with the three-part description; 2 summary bullets; MCQ ১৩ (answer গ: In); short question ১৩ (why KM3 from Q1); maths problem ৯; practical-table row "স্টার-ডেল্টা প্র্যাকটিস".
  - All ch14 refs checked against ch14.py headings: ১৪.৩, ১৪.৫, ১৪.৫.৩, ১৪.৭, ১৪.৯, ১৪.৯.১, ১৪.১০, ১৪.১০.১, ১৪.১০.২ exist with that content.

### Older review (review_2026-09-23.md)
- ✅ **TN-C-S N/PE** (১৫.৪.২ safety box, সারণি ১৫.৯ row, summary, MCQ ৮): now "never joined in any DB/SDB/sub-panel; whether a single N–PE link exists at the origin is set by the earthing system — required once in TN-C-S, absent in TT — engineer's decision; rejoining downstream puts load current on PE". Fault-table remedy now "remove the link inside the DB" instead of "never joined after the meter". MCQ ৮ reworded to "কোনো ডিবির ভেতরে…".
- ✅ **Diversity vs demand factor** (১৫.৬.৩ prose, উদাহরণ ১৫.২ & ১৫.৪ question+given, glossary, docstring): → ডিমান্ড ফ্যাক্টর (≤1, multiply); one sentence added that diversity factor is ≥1 and is divided by; glossary now has both rows, worded exactly as ch06's glossary.
- ✅ 4P vs TP&N (১৫.৪), copper oxide (১৫.২.১), "সিসা" (১৫.৮.১), "দেশজুড়ে এক" (১৫.৪.১) — see below.
- ⏭ BNBC clause numbers — left as instructed (handled separately).

### Review file §7
1. ✅ Syllabus gap — above.
2. ✅ উদাহরণ ১৫.২ note: 20 % margin → 223 mm² → **30 × 8 (240 mm², 384 A)**, not 50 × 5. (Maths problem ৭, 25 %: 371.5 A → 232 mm² → 30 × 8; no answer key exists, nothing to change.)
3. ✅ J inconsistency: উদাহরণ ১৫.২ now states the main panel has ventilation; ১৫.৬.১ says J 1.6 applies to ventilated panels and 1.2 to closed ones (new example 15.5 uses 1.2); summary bullet updated.
4. ✅ "ফোর পোল চাইতে হয়, থ্রি পোল নয়" → TP&N = three phase poles + neutral link; 4P only when the neutral must be switched too; design decides.
5. ✅ "সব সাদা তার" → "সব নিউট্রাল তার" (১৫.১).
6. ✅ Copper "সবচেয়ে ভালো" → "রুপা বাদ দিলে…"; oxide "নিজেও মোটামুটি পরিবাহী" → not a hard insulating layer like Al₂O₃, thin and soft (also সারণি ১৫.১ row).
7. ✅ SPD (১৫.৫.৪): connects from L and N, earth end to the PE bar; short earth lead. Also fixed in the same paragraph block: RCCB-neutral error claimed the RCCB might "sit silently and not trip" — unsupported; now: wrong neutral landing trips the RCCB as soon as load runs (and the reverse mistake likewise).
8. ✅ Comb bar (১৫.৭): each MCB's own terminal screw must be tightened.
9. ✅ "সিসা মেশানো" → "অন্য ধাতু মেশানো থাকতে পারে"; "খরচ প্রায় দ্বিগুণ" → "অকারণে বড় ও দামি"; "ক্রমটিও দেশজুড়ে এক" → "প্রচলিত ক্রম" (prose, summary, and d07 note strip "ক্রম সব প্যানেলে এক" → "এটিই প্রচলিত ক্রম").
10. ✅ Current density: definition box now the physics one (current per unit cross-section that flows; unit A/mm²); opening sentence says the *design* value is what is chosen; "তাকে বাধা দেয় বারের কাটা মুখের ক্ষেত্রফল" → the cross-section is the current-carrying area; glossary meaning fixed.
11. ⏭ Formula-box/kVA order: checked the source — the two OMML formulas precede the explanatory box, and the kVA formulas follow "সূত্র নিচেরটি". Not an error.
12. ✅ চিত্র ১৫.৫ (d14_trunk) caption vs text: photo is a ceiling-hung horizontal run, which the text calls বাসডাক্ট. Diagram title → "বাসবার ট্রাংকিং (বাসডাক্ট)", note strip → "কারখানার ছাদ বরাবর আনুভূমিক রান — একে বাসডাক্টও বলা হয়" (old note "উঁচু ভবনে রাইজার কেবলের বদলে — বিএনবিসি ১.৩.১৮.৩" described a vertical riser, which the photo is not; the BNBC citation therefore left the figure — it is still in the prose). Book caption kept ("ছাদ থেকে ঝোলানো বাসবার ট্রাংকিং…"), now consistent with the figure title.
13. ✅ "সবুজ তার" → "সবুজ-হলুদ তার" (১৫.৫.১).
14. ✅ MCQ key: now 13 questions, ক৩ খ৩ গ৪ ঘ৩ (added ১৩-গ). MCQ ১০ weak options replaced (answer unchanged, খ); MCQ ৮ "কিছুই হয় না" → "আরসিসিবির সংবেদনশীলতা বাড়ে" (answer unchanged, ঘ).
15. ✅ Cross-refs: only backward (ch06, ch14) — all checked.

### Book-wide decisions
- ✅ Supply OFF/verified dead added to practical rows that touch wiring (রঙের কোড, টার্মিনাল বার বসানো, ভারসাম্য যাচাই — measure live, rearrange dead, ত্রুটি খোঁজা) and one sentence before the faults table (every remedy only after isolating and testing dead). Practical-table rows rewritten from তুমি-form to impersonal.
- No DOL starting multiplier appears in ch15 except via "⅓ of DOL" (no number given), so nothing to align.
- No forward chapter references; no house-wiring leftovers found beyond "ঘরের ডিবি" phrasing (style, stage 2).

## Layout reorders made to close gaps (content unchanged)
- ১৫.৬.১: the two temperature paragraphs ("চারপাশের তাপমাত্রা", "ধাতুর নিজের ধর্ম") moved after উদাহরণ ১৫.১ (still inside ১৫.৬.১).
- d04_dims figure moved after the formula box/maths, before উদাহরণ ১৫.১.
- d15_sd figure placed after its explanation ("নিচের ছবির…").

## Sources
- TN-C-S split, no rejoin downstream: ETI/Eplan, "TN Earthing System Regarding Grounding and Fault Protection" — https://eplan.etigroup.eu/media-center/eti-blog/tn-earthing-system-regarding-grounding-and-fault-protection
- Demand factor (max demand / connected load, <1) vs diversity factor (sum of individual max demands / max demand of whole, >1): https://www.ecmag.com/section/codes-standards/diversity-vs-demand-dont-be-confused-these-terms ; https://electrical-engineering-portal.com/8-important-definitions-to-quantify-load-diversity ; consistent with ch06.py glossary.
- Star-delta numbers (0.58 In in KM1/KM3/F2, KM2 ⅓, star start ⅓ of DOL, motor currents 30/44/72 A for 15/22/37 kW) taken from ch14.py (ABB 1SBC009500R1002, already verified there) — no new numbers introduced.

## Layout
- Before: 29 pages, no gap > 4.5 cm.
- After: 34 pages, no gap > 4.5 cm. (+5 pages = new section ≈ 4 pp with an 11 cm figure, example, 8 steps, table; plus longer safety box / glossary row / questions.)

## For the author
- Chapter grew 29 → 34 pages; the new section is ~4 pages. If that is too long, the measurement table or the third (maths) question could go.
- MCQ ১২ still asks students to memorise a BNBC clause number — left (citation stage).
- dia_ch15 d14: the BNBC 1.3.18.3 citation was dropped from the figure's note strip because the old note described a riser, not the pictured ceiling run.
