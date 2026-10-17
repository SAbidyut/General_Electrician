# Fix report: ch10 (টাইমার), stage 1

Files touched: `Book/build/ch10.py`, `Book/build/dia_ch10.py` (d09, d10 note strips only).

## Items

- ✅ **Table 10.7, row 2 (technical error)**: the cause "8-5-এর বদলে 8-6 বা 1-এর সেটে তার" was wrong. With 8-6 the motor never starts. Cause is now "হোল্ডিং তার STOP 12-তে · timer coil has no supply (2 or 7 open)". The remedy now checks the ON lamp and 2-7 voltage. Added a new row: "START চাপলে মোটর চালুই হয় না | 8-5-এর বদলে 8-6-এ তার".
- ✅ **Table 10.7, rows where a wire is moved**: each remedy now starts with "সরবরাহ বন্ধ করে".
- ✅ **MCQ 7 (two defensible answers)**: "ওয়াটার হিটার" → "২ kW ওয়াটার হিটার". That heater draws about 8.7 A, which is over the 5 A contact, so it is wrong too. The key is unchanged and balanced: ক2 খ3 গ3 ঘ2.
- ✅ **Cross-refs**: in example 10.5, "অধ্যায় ৯-এর চিত্রে" → "চিত্র ৯.২" (checked: d02_current is the second figure in ch09 and shows the DOL current). In 10.7, "অধ্যায় ৯-এর চিত্রের মতোই" → "৯.৭-এর পাওয়ার সার্কিটের মতোই". In 10.4.1, "৯.৪.১" → "অধ্যায় ৮-এর সারণি ৮.২ ও অধ্যায় ৯-এর ৯.৪.১" (checked: table 8.2 is the auxiliary-contact numbering table).
- ✅ **10.3, the word "বন্ধ" used in two opposite senses**: the timing-chart sentence was rewritten. It now says high = signal present / contact closed (জোড়া লাগা), and low = absent / open. It also defines the chapter's convention: switches are "অন/অফ", contacts are "বন্ধ/খোলা". Following that convention, S1 is now "অন/অফ" in 10.6.1 (prose and the state table), in 10.6.3, and in the d09/d10 note strips.
- ✅ **10.5 "আদি নকশা"**: this claim had no source. It now reads "এই ধরনের একটি পরিচিত নকশা".
- ✅ **Example 10.4, ±10 % basis (older review)**: the AH3/Alion datasheets say "Setting error ±10 % max" but do not say what it is a percentage of. Omron, for its own timers, states setting error as a percentage of full scale (FS). The note now says this, and gives the full-scale case: ±6 min, up to 240 L overflow. The worked steps (on the set value) are unchanged.
- ✅ **10.7 "বসানো সময় চলে"** → "বসানো সময় পর্যন্ত চলে" (the older review flagged this as ambiguous).
- ✅ **Practical table**: added one line before the table: every wiring task is done with the supply off and verified dead with a tester. The "ভুল হোল্ডিং তার" row now says to switch the supply off before moving the wire and again before restoring it. Rows I rewrote use the করুন form; the other rows were left for stage 2.
- ⏭ **MCQ key**: already balanced (ক2 খ3 গ3 ঘ2).
- ⏭ **Inconsistency in ch07 ("৫–৭ গুণ")**: this belongs to another chapter. ch07 ৭.৯.৫ already reads "৬ থেকে ৮ গুণ" in the current source.
- ⏭ **Objectives, intro, summary trims, box re-titling, তুমি-forms**: these are style and structure, so they are left for stage 2.

## Sources

- Alion AH3 catalogue (setting error ±10 % max, repeat ±1 %): https://www.slideshare.net/slideshow/h3ba-series-multi-range-analogue-timer/116862156 (from search results; the page itself did not load)
- Goldsupplier AH3 listing (same figures): https://www.goldsupplier.com/provide/p131765075.html
- Omron, setting error as "% of FS": https://www.ia.omron.com/products/family/3486/specification.html and the H3DR manual https://manualmachine.com/omron/h3drm/15628334-user-manual/

## Layout

- Before: 27 pages, no gaps.
- After: 27 pages, no gaps. One intermediate build went to 28 pages, with a single table row spilling over. I fixed it by shortening the new safety line and the rewritten row, not by shrinking anything.
- `qc.py dia_ch10`: 0 problems.

## Environment problem found (affects every chapter)

`render.py` with this Chromium (`/opt/pw-browsers/chromium-1194`) clips the bottom ~86 px of every SVG, so the note strip at the foot of a diagram comes out blank in the PNG. `qc.py` cannot see this. All ch10 and ch13 PNGs were re-rendered with `/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/render_fix.py`. It renders with extra viewport height and then crops back to the exact size; `render.py` itself is untouched.

## Needs the author's decision

- Nothing from ch10.
