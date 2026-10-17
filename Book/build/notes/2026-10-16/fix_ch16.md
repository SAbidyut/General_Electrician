# Chapter 16 (সোলার সিস্টেম): stage-1 fixes

Files changed: `Book/build/ch16.py` and `Book/build/dia_ch16.py` (d10, d12 and d13 were re-rendered; qc reports 0 problems; the PNGs were checked by eye).
Backups of the files before this pass: `scratchpad/ch16.py.orig` and `scratchpad/dia_ch16.py.orig`.

## Net-metering 10% charge (the main item)

I re-checked the rule against `notes/nm2025.txt`. Clause **3.4 M** says: "10% of the **net exported** electricity during a billing period shall be taken as Distribution System Maintenance Charge". Annex-5(a) adds: "Since export is less than import, his net export is Enet = 0, hence no maintenance charge applies". Annex-5(a) gives BU = I − E − C, and Annex-5(b) gives Eadj = 0.9 × Enet, with credit carried = Eadj + C. **Confirmed: the charge applies only to net export.** The sub-clause letter is M (the 13th letter), not ঝ.

Note: most of the text the review quotes had already been corrected in the committed `ch16.py`. The 16.8.2 prose, the summary and MCQ 9 already said "নিট রপ্তানি", and Example 16.5 already used a net-export month. I fixed what was still wrong:

- ✅ **উদাহরণ ১৬.৫**: the answer is unchanged (280 net, 252 credit). I changed the inputs from 150/430 to 120/400 so a closed shop's daytime self-use is plausible. The "normal month" in the note used 600/132, which contradicts the shop's 480 units a month. It is now 180/132, giving a bill of 48 units with no charge, plus the previous credit. Check: 480 = 180 + 432 − 132.
- ✅ **১৬.৮.২ prose**: now reads "ধারা ৩.৪-এর উপধারা M", with a new sentence "আমদানি বেশি হলে এই চার্জ কাটা হয় না।"
- ✅ **New formula box in ১৬.৮.২**: monthly accounting for both cases (net exporter / net importer), taken exactly from 3.4C, 3.4D, 3.4M and Annex-5. This is real content, and it also closed a page-foot gap.
- ✅ **"মনে রাখুন" box, summary, MCQ 9**: already said "নিট রপ্তানি". Checked, no change needed.
- ✅ **Maths problem 6**: the first part's answer is 640, no charge. I added a second part (import 300, export 520 → credit 0.9 × 220 = 198) so that both cases are practised.
- ✅ **Docstring** (developer notes): clause letters changed to 3.3A/B/C, 3.4F, 3.4M and 3.5(b). The stale "রপ্তানি 132, ক্রেডিট 118.8" note is updated, the "অধ্যায় ১৯" pointer is removed, and the Annex-5 quote is added.
- No diagram repeats the 10% figure (checked by grep).

## Other review items (section ৭)

1. ✅ সারণি ১৬.১১, frequency row: now "গ্রিড ৫০ হার্জের ±১ শতাংশে; ইনভার্টার ±৪ শতাংশে চলবে", per guideline 4.3.2.
2. ✅ AFCI box (১৬.৬.২): "শব্দতরঙ্গ" replaced with "high-frequency electrical noise in the current".
3. ✅ Solar cable (১৬.৬.৩): the insulation rating is now explained by string voltage, not by "DC".
4. ✅ (partly reframed) PSH 4.5:
   - ১৬.৭: on-grid uses 4.5 (any winter shortfall comes from the grid); off-grid uses the winter value of about 4.
   - উদাহরণ ১৬.৮ recomputed with PSH 4: 835 W × 1.2 = 1002 W, so about 1000 W. Six 165 W modules = 990 W is unchanged, and the note explains the 1% difference.
   - Also changed: summary bullet, MCQ 7 (now asks about on-grid; answer still ক), d10 chip ("অন-গ্রিডে 4.5, অফ-গ্রিডে 4").
   - d10's note strip said "1 kW gives 4–4.5 units a day", which contradicts the chapter's own 4.5 × 0.8 = 3.6. It now says 3.6.
   - I could not open profilesolar.com (blocked), so I could not confirm whether the 4.06/5.98 figures include losses. The causal claim "4.5 is safe, otherwise there is a shortfall in winter" was therefore removed rather than defended.
5. ✅ উদা ১৬.১১ note: the "২০ শতাংশ বাড়তি" contradiction is removed. It now says charge time (4.6 h) roughly equals the sun hours (4.5, about 4 in winter), so there is no margin and the customer should be told to reduce load in winter.
6. ✅ ১৬.৯.৫ tip and উদা ১৬.৯:
   - The current is now calculated at the nominal 24 V: 990 × 0.97 / 24 = 40 A, exactly at the controller's 40 A limit.
   - The tip says that dividing by 28.8 V under-states the current, and that an MPPT controller limits itself to its rated current.
   - The note derives the typical 33 A as 40 / 1.2, using the chapter's own 20% derate. That keeps ১৬.১০.৩'s "৩৩ অ্যাম্পিয়ার" and উদা ১৬.১১ (4.6 h) valid.
   - Maths problem 7 is rewritten to use nominal voltage (answer 48.5 A, so a 40 A controller is not enough).
7. ✅ উদা ১৬.৪: the MCB is now sized on the inverter's maximum output current, 6.7 A × 1.25 = 8.4 A → 10 A four-pole. I added "follow the inverter manual if it recommends a size", because I could not find Growatt's own breaker recommendation online.
8. ✅ উদা ১৬.৬: the "পরের মাপ 1000 VA" / "৬০০ VA-তেও চলত" contradiction is removed (the note is also shorter).
9. ✅ Summary bullet 1: আয়তন → ক্ষেত্রফল.
10. ✅ ১৬.১২: the latitude was already 20.5–26.5. "সূর্য সারা বছর দক্ষিণ আকাশে" is now "বছরের বেশির ভাগ সময়, বিশেষ করে শীতে, দুপুরের সূর্য দক্ষিণ আকাশে". The d13 docstring latitude is updated too.
11. ✅ Row spacing (১৬.১২ bullet, summary, d13 label):
    - The rule is now: no shading from 9 am to 3 pm on 21–22 December.
    - Simple method added: at Dhaka's latitude the gap should be about 1.5 × the height of the front row's upper edge, a little more in the north.
    - Computed by standard solar geometry: shadow/height ratio at 9 am on the solstice is 1.30 at 20.9°N, 1.44 at 23.7°N and 1.60 at 26.4°N.
    - d13 label changed from "শীতের দুপুরের ছায়া" to "শীতের সকালের ছায়া".
12. ✅ ১৬.৩.৩ bypass tip: added the landscape vs portrait sentence.
13. ✅ Paragraph after the I-V figure: MPP tracking is now credited to MPPT controllers and grid-tie inverters only, with "PWM does not do this (১৬.৬.১)".
14. ✅ ১৬.৬.১ opening: "20 V খাওয়ালে" is replaced by uncontrolled overcharge as the real risk.
15. ✅ ১৬.১: "ব্যাটারি চার্জ হবে না" → "খুব কম চার্জ হবে".
16. ✅ ১৬.৫ back-feed box: "হাজার ভোল্ট" → "২৩০ V থেকে উপরের লাইনে প্রায় ১১ হাজার ভোল্ট". This matches ch11 line 189, and the ch11 reference is kept.
17. ✅ Intro: the mandatory-solar sentence now gives the 1000 sq ft condition precisely and the single-phase residential exception.
18. ✅ Counts:
    - ১৬.১ now says two needs, and points to hybrid in ১৬.৫.
    - ১৬.৫: "একটি প্রশ্ন" → "দুটি প্রশ্ন".
    - ১৬.৯.৪ now names the fourth loss (dust and heat on the module).
    - ১৬.১৩: "তিনটি" → "চারটি".
19. ✅ ১৬.৯.৩: now says the battery holds one full day's energy (one day of autonomy), not "রাতের শক্তি".
20. ✅ উদা ১৬.৯ note: the Phaesun datasheet I found does not give a temperature coefficient. The note now says so and assumes −0.35%/°C: 47 × 1.0525 = 49.5 V, still ≤ 92 V.
21. ✅ সারণি ১৬.৫ (EPEVER): all "কী মেলাতে হবে" cells now use one form, "X ≤ এই মান".
22. ✅ Off-grid step 8: switch off the inverter and AC loads first, then disconnect in reverse order.
23. ✅ Practical 2 (Isc):
    - use a module with Isc under 10 A;
    - cover the module before connecting and before disconnecting the 10 A range;
    - prefer a DC clamp meter.
    Practicals 3 and 8 now refer to this method.
24. ✅ Practical 3: "চলন্ত অবস্থায়" removed (cell covered with cardboard). Summary "চলন্ত অবস্থায় MC4" → "কারেন্ট চলা অবস্থায়".
25. ✅ চিত্র ১৬.১৯ caption and the d12 note strip: "ভেতরের দিক" → "লোডের দিক (মিটার ও মেইন ব্রেকারের পরে)". The prose's "বাইরের দিকে" → "গ্রিডের দিকে (মিটারের আগে)".
26. ✅ সারণি ১৬.৭, PF row: now states the condition, "৪.২.৩-এর শর্ত (০.৮৫-এর বেশি লিডিং বা ল্যাগিং) পূরণ করে".

## Older review (review_2026-09-23.md)

- ✅ Practical 2 safety: same fix as item 23.
- ✅ Back-feed 11 kV: same fix as item 16.
- ✅ Phaesun coefficient assumption: same fix as item 20.
- ✅ VERIFY-DATE: ১৬.৮ now says "নিয়ম বদলায়, তাই কাজের আগে সর্বশেষ সংস্করণ মিলিয়ে নিন।"
- ⏭ [MATH-RENDER] "V(ব্যাটারি)": skipped. That line is in a `box("formula")`, which goes through `_rich` as plain text, not OMML, so Bangla is safe. mathguard is clean.
- ⏭ তুমি-form in the short and essay questions: skipped as a register item (stage 2). Only maths problem 7, which I had to rewrite anyway, now uses "লিখুন".

## Book-wide checks

- No rendered forward chapter reference. The only one, "অধ্যায় ১৯", was in the docstring and is removed.
- No house-wiring leftovers. "হাউস ডিবি" is the solar consumer DB and is correct.
- No DOL starting-current statement in this chapter.
- The MCQ key is unchanged and balanced at 3/3/3/3. MCQ 7 is reworded, so it has one defensible answer.
- Wiring practicals 4 and 5 now say to work with everything OFF and the modules covered. Practical 5 also says to check voltage before every connection.
- mathguard: clean.

## Sources

- `Book/build/notes/nm2025.txt` (SREDA Net Metering Guideline 2025): 3.4 C/D/M, Annex-5(a)(b), 4.2.3(i), 4.3.2.
- Phaesun Sun Plus 165 P datasheet (no temperature coefficient listed): https://static.mercateo.com/50/49a13191334c4d0c9ae6f68a2851612c/pdf/datablad-2256124-phaesun-sun-plus-165-p-polykristallijn-zonnepaneel-165-wp-12-v.pdf
- Dhaka seasonal per-kW figures (search snippet only; the site itself is blocked by the proxy): https://profilesolar.com/locations/Bangladesh/Dhaka/
- Growatt recommended AC breaker: not found, so the text tells the reader to follow the manual.

## Layout

- **Before:** 48 pages, no page-foot gap.
- **After:** **50 pages, no page-foot gap above 4.5 cm.**

The text additions shifted the chain of tall worked examples (16.5 to 16.11 each start at the top of a page), which opened gaps at p19 and p26. I closed them by reordering, without shrinking anything:

- The Growatt photo now comes before its data-plate table, and its caption no longer starts with "ওই".
- The net-metering formula box was added in ১৬.৮.২.
- The Ex 16.6 note was shortened by one line.

## Needs the author's decision

- **The chapter grew from 48 to 50 pages.** Most of the growth is the new safety and clarification text.
- **Off-grid design PSH changed from 4.5 to the winter value of 4.** This follows the review's suggestion. Ex 16.8 now gives about 1000 W, and the same 6 × 165 W array is kept. If the author prefers 4.5 throughout, Ex 16.8, ১৬.৭, the summary and d10 need reverting together.
- **Row-spacing rule of thumb ("about 1.5 × height at Dhaka").** This is my own solar-geometry calculation, not a cited source.
- **d12 has an old overlap.** The green dashed earth line from the inverter runs through the "সোলার MCB ও AC আইসোলেটর" box text. qc does not catch it. Not fixed here because it is a layout issue, not a factual one.
- **Delivery copies are not updated.** The `.docx` and preview PDF in `Book/` were not re-copied; per the brief, only `out/` was rebuilt.
