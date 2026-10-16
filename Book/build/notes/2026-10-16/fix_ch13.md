# Fix report: ch13 (ফ্লোট সুইচ), stage 1

Files touched: `Book/build/ch13.py`, `Book/build/dia_ch13.py`.

## Items

- ✅ **Figure ১৩.১০ was wired COM–NO (a draining circuit) while the chapter teaches filling a roof tank.** The institute-slide images (h25/h26) were dropped. d09_single is now a hand-drawn figure with two panels:
  - Power: L/N → Q1 → KM1 1-2 / 3-4 → F2 → pump M 1~.
  - Control: L → F1 → F2 95-96 → FS COM → **NC** → KM1 A1; A2 → N.

  The new caption names it as the filling circuit (COM–NC). The note strip says that for draining the wire moves from NC to NO. The prose in ১৩.৬.৩ and ১৩.৬.৫ was rewritten to match, so the text no longer tells the reader to move a wire on a draining figure. The wire list is written in the `dia_ch13.py` comment block, and I traced the render once more after it was done.
- ✅ **Double condition (figure ১৩.১২)**: also redrawn as a ladder (d10_double), so that it includes F2 95-96. FS-1 is COM–NO in the reservoir and FS-2 is COM–NC in the roof tank. That is the same logic as the old slide and as সারণি ১৩.৫. Its power circuit is stated to be the same as ১৩.১০.
- ✅ **Syllabus gap "সিঙ্গেল/ডাবল কন্ডিশন অটো-মেনুয়াল"**: added a new section, **১৩.৬.৬ অটো-ম্যানুয়াল — সিলেক্টর সুইচসহ সংযোগ**. It contains:
  - A new figure, d13_automan, which shows a MAN–0–AUTO selector S1. The AUTO branch runs through FS-1 NO and FS-2 NC. The MAN branch is ch08's ৮.৯ latching (STOP, START, KM1 13-14). Both branches join at A1, and F2 95-96 sits before the split.
  - Prose explaining that MAN uses latching to satisfy BNBC ১.৩.২৭(ঘ), while AUTO falls under that clause's exception for automatic controllers. It also explains why AUTO does not latch: the back-path through 13-14 dead-ends at S1's open MAN contact.
  - How to make it single-condition: drop FS-1.
  - A state table (new সারণি ১৩.৭), a safety box on manual mode, a six-step wiring sequence that starts supply-off, and a new practical-table row.
  - Updated cross-links: ১৩.৭.২ now points back to the new section, and its "বাধ্যতামূলক" is now "রাখা উচিত". The objectives, subtitle, intro, summary, glossary (HOA switch), one short question and one essay question were updated to match.

  The helpers (`_nc`, `_no`, `_pb`, `fuse`, `thermal_sym`, `nc_tip`, `no_tip`, `coil_sym`) are imported from dia_ch09/dia_ch08, the same way other `dia_` files do it.
- ✅ **Pumps above 0.376 kW with no overload protection (contradicted ch09)**:
  - ১৩.৬.১ now cites ১.৩.২৭(গ) and ৯.১.১. It notes that 0.5 HP (0.373 kW) is just below the limit and 1 HP is above it, and says to use an MPCB set to the pump's FLC instead of a plain MCB.
  - d07_direct's MCB is now labelled MPCB, "মোটরের কারেন্টে সেট".
  - সারণি ১৩.৪'s action column now reads "কন্টাক্টর ও ওভারলোড রিলে" for 1.5 HP and up, and "MPCB, or contactor + relay" for 1 HP.
  - ১৩.৬.২ adds F2 after the contactor, with 95-96 in series ahead of the float. It refers to ৯.১০ (three poles in series) and to ৯.৪.৩ (use manual reset H, because auto-reset restarts the pump through the float).
  - The note to example ১৩.১ and the summary carry the same rule.
- ✅ **Unbalanced MCQ key (ক appeared once)**: reordered MCQ 5 (COM–NC first) and MCQ 10 (IP68 first). The key is now ১-ক ২-খ ৩-গ ৪-ঘ ৫-ক ৬-গ ৭-গ ৮-ঘ ৯-খ ১০-ক, i.e. ক3 খ2 গ3 ঘ2.
- ✅ **MCQ 4 and summary said the float goes to "A1 ও A2"**: the question now asks which terminal's line the float sits in series with (answer A1). The summary bullet and the d08 note strip now say the float is in the A1 line and A2 goes to N.
- ✅ **MCQ 1 ("পারদের ফোঁটা" could be defended)** → "রাবারের বল".
- ✅ **Contactor terminals were named L1/T1** (ch08 teaches 1/L1–2/T1): the prose now uses 1/L1, 3/L2, 5/L3 and 2/T1, 4/T2, 6/T3, and the d08 callouts read "ইনপুট 1 3 5" / "আউটপুট 2 4 6". The re-introduction of the contactor in ১৩.৬.২ is replaced by a one-sentence pointer to ch08.
- ✅ **House-wiring leftovers**: ১৩.২.৩ "টু-ওয়ে সুইচের গঠনের মতো" was removed; the changeover is described in its own terms. ১৩.৩ "হাউস ওয়্যারিংয়ে" was reframed.
- ✅ **Contradictions**:
  - ১৩.১ said the float never drives the pump, which contradicted ১৩.৬.১. Rewritten.
  - ১৩.৭.৩ (the differential section) said a short free cable makes the contact sit "আধা-লাগা", contradicting snap action. Rewritten.
  - ১৩.৮ said there was "মাত্র একটি" moving part. Rewritten.
- ✅ **Unsourced or over-strong claims**:
  - "ইম্পেলারের সিল" → "পাম্পের সিল"; the "আধ ঘণ্টা" dry-run times were removed (intro and ১৩.১.১).
  - "আইসোলেটর থাকতেই হবে" → "রাখা জরুরি".
  - The ১৩.৬.৫ tip ("some floats become drain switches when hung upside down") was removed because it could not be verified.
- ✅ **Colour tip (blue = neutral per IEC 60445)**: now recommends numbered ferrules, and says to avoid blue and green-yellow tape.
- ✅ **সারণি ১৩.৪ vs সারণি ৭.৬ currents**: added a line saying that table assumes 0.70 efficiency for every size, and points to সারণি ৭.৬.
- ✅ **Fault table**:
  - Row 1 now lists an overload trip as a cause. Its remedy checks the control MCB, F2 95-96, wiring and float when A1–A2 has no voltage, and the coil and pump power line when it has.
  - The last row no longer shorts the float leads live. The supply is switched off, an insulated jumper is fitted on the board, then the supply is restored.
- ✅ **Cross-refs**:
  - "অধ্যায় ৭-এর সেই পাম্প" → "উদাহরণ ৭.৩".
  - Maths problem 5 → "৭.৯.৫".
  - Every hard-typed চিত্র ১৩.N that the new figures would shift is now a captured number (`n_direct`, `n_single`, `n_double`, `n_am`).
  - The forward "বিস্তারিত অধ্যায় ৮ ও ৯-এ" sentence was replaced.
- ✅ **Practical table**: added the supply-off-and-verify line; the contactor row now cites the COM–NC figure and lists the overload relay; added an auto-manual row.
- ⏭ **d11_levels inset (small block sketch FS-1–FS-2–KM1)**: only the label changed (MC → KM1, also on the d01 chip). It is a location sketch, not a working circuit; F2 is in d10/d13.
- ⏭ **Stage-2 items**: কেবল → ক্যাবল, তুমি-forms in rows I did not touch, objectives 12 → 8, em-dashes, box re-titling. Left untouched.

## Sources

- BNBC 1.3.27(গ) wording: already quoted verbatim in `ch09.py`'s docstring, taken from the law.resource.org PDF. "Every electric motor having a rating exceeding 0.376 kW shall be provided with control equipment incorporating means of protection against overcurrent."
- 0.5 HP = 0.373 kW: arithmetic (0.5 × 746 W).
- Overload relay on single phase (three poles in series), reset behaviour with float control, and MPCB: ch09 ৯.১০, ৯.৪.৩ and ৯.১১, which cite the Siemens 3RU2/3RB3 manual.
- **Not verified, so not written**: how the poles of an MPCB should be wired for single phase. I could not find a manufacturer statement, so the text says to follow the maker's connection diagram.

## Layout

- Before: 24 pages, no gaps.
- After: 27 pages, no gaps. The +3 pages come from the new ১৩.৬.৬ section, its figure and table, and the larger drawn figures.
- The first build had one 7.04 cm gap on p19 (worked example ১৩.৩). I closed it by reordering: "লেভেল কন্ট্রোলার ও ম্যানুয়াল মোড" is now ১৩.৭.২ and "ডিফারেনশিয়াল ঠিক করা" is ১৩.৭.৩. The forward pointer in ১৩.২.১ was updated to ১৩.৭.৩.
- `qc.py dia_ch13`: 0 problems. `mathguard.py ch13.py`: clean.

## Needs the author's decision

- **The institute's slides 25–28 are no longer used** for figures ১৩.১০ and ১৩.১২; both are now hand-drawn schematics. The slides' photo-style connection diagrams were lost with them. If the author wants a photo-style connection view back, it has to be redrawn with COM–NC and an overload relay.
- **Label size**: the new figures follow ch09's ladder convention (T_TINY terminal numbers). At 15.4 cm that is about 6.5 pt, under the 7.5 pt house guideline. ch09 has the same issue.
- **Power circuit**: it switches both L and N through two KM1 poles. The old text said one pole; both are common practice.
