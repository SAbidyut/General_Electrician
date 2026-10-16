# ch17 (CC ক্যামেরা): stage-1 fixes

Files changed: `Book/build/ch17.py`, `Book/build/dia_ch17.py` (d06, d09 re-rendered). qc.py: 0 problems. mathguard: clean.
Backups from before the edit: `scratchpad/ch17.py.stage1bak`, `scratchpad/dia_ch17.py.stage1bak`. Edit script: `scratchpad/ch17fix/edits1.py`.

## Review section ৭ (and matching older-review items)

- ✅ **৭-ক DORI terms**: Detect = **উপস্থিতি বোঝা**, Observe = **পর্যবেক্ষণ**, Recognize = **চেনা**, Identify = **শনাক্তকরণ** (standard spelling). All 14 uses of "সনাক্ত" are now "শনাক্ত", and "শনাক্ত" no longer means Detect anywhere. Changed in সারণি ১৭.৬, ১৭.৪.৩ prose (Bangla names added next to D-O-R-I), examples ১৭.১–১৭.৩, ১৭.৫.২ ("কেবল উপস্থিতি বোঝা যাবে, চেনা যাবে না"), সারসংক্ষেপ, the glossary DORI row, MCQ ২–৩ and the d06 diagram labels.
- ✅ **৭-খ** ১৭.১২.১ ✔: the division had been written the wrong way round. It now reads: horizontal pixels (1920 for 2 MP) divided by the scene width.
- ✅ **৭-গ** ১৭.১১.১ ⚠: the text already said that daisy-chaining is still parallel and that the + to − link is the real series fault. I added "ওই টুকরোয়" and a pointer to উদাহরণ ১৭.৭. I checked d13 in the code: three separate drops from three nodes on the 12 V bus, so it is drawn as parallel.
- ✅ **৭-ঘ** CCA = তামার প্রলেপ দেওয়া অ্যালুমিনিয়াম. It has higher resistance and heats up (১৭.৭.৩ ❖).
- ✅ **৭-ঙ** ১৭.৮.১: "হুবহু" is replaced. The code lists centre conductor, foamed PE, Al foil, braid and PVC sheath. The photographed cable has no foil, and the text now says so. (The review said the code omits the sheath, but "PVC sheathed" is in 1.3.40.1, so the sheath is listed.)
- ✅ **৭-চ / old A13** PoE port vs LAN port: removed the false "power from both sides" claim from ১৭.৭.৩ ✔. In ১৭.১১.২ ⚠ the reason is now that the PoE ports form a separate network meant only for cameras connected directly, with a pointer to the ❖ box below.
- ✅ **৭-ছ** Mode A/B: endspan is "সাধারণত" Mode A and midspan is "সাধারণত" Mode B, in the prose, the d09 subtitles and the docstring. The glossary row (switch PoE vs injector) was already correct.
  - Extra fix in d09: the unpowered pins 4-5/7-8 under Mode A were labelled "কেবল ডেটা". That contradicts ১৭.৭.৩, which says those pairs are idle at 100 Mbps. Pins now read ডেটা + পাওয়ার / কেবল পাওয়ার / কেবল ডেটা / খালি, and the strip says "100 Mbps-এর হিসাব".
- ✅ **৭-জ** removed "একই দামের" from ১৭.৮.৪.
- ✅ **৭-ঝ / old A13 units**: everything is now decimal, matching how disks are labelled.
  - Formula: S = B × 86400 / (8 × 1000), so 1 Mbps = 10.8 GB per day.
  - উদাহরণ ১৭.৮: 21.6 / 172.8 / 5184 GB = 5.18 TB, about 5.2 TB. It still fits a 6 TB disk.
  - 4 TB = 4000 GB, which lasts about ২৩ days. One sentence explains that the recorder may show about 3.6 TB because it counts in 1024s. The 10 % tip now reads "২০ থেকে ২১ দিন".
  - উদাহরণ ১৭.৯: 1726 GB = 1.73 TB.
  - 4K note: 173 → 691 GB per day, about ২০.৭ TB.
  - Updated to match: the formula box, the summary bullet, MCQ ৮ (10.8 GB; key letter unchanged) and the docstring.
- ✅ **৭-ঞ** removed "মোটা" from the note in উদাহরণ ১৭.৭.
- ✅ **৭-ট** ১৭.১০.৩ ✔ rewritten without the "কাকতালীয় নয়" claim. It also now says correctly that data from cameras on the external switch does pass through the LAN port.
- ✅ **৭-ঠ** summary: "যেমন উদাহরণের NVR-এ 25.5 W ও 80 W". The 80 W is no longer stated as a general PoE rule.
- ✅ **৭-ড** last summary bullet now reads "সূর্য বা জানালার দিকে মুখ না করে".
- ✅ **৭-ঢ** four fixes:
  - The "১০১ মিটারে" overstatement is rewritten to say the camera may fail to start or drop data beyond 100 m.
  - BNBC 1.3.41 says "may be installed using Cat 6", so it is not a mandate. ১৭.৬.৪ and ১৭.৮.৩ now say the code "speaks of" Cat 6.
  - সারণি ১৭.২: "12 MP বা তার বেশিও পাওয়া যায়".
  - RS485: "সাধারণত DVR-এ থাকে".
- ✅ **৭-ণ** removed "রাতে বেশি" from ১৭.৮.৫ ⚠.
- ✅ **৭-ত** "দূরত্ব ১০০ মিটারের মধ্যে হলে PoE-ই সহজ উত্তর".
- ✅ **৭-থ** ρ = 0.0175 Ω·mm²/m in ১৭.৯.২ and in the প্রদত্ত line of উদাহরণ ১৭.৬.
- ✅ **৭-দ** উদাহরণ ১৭.৩ note: "প্রায় দ্বিগুণ".
- ✅ **৭-ধ / old ONVIF** date rewritten exactly: no new Profile S conformance after 31 March 2027. It adds that installed Profile S devices keep working and that buyers should choose Profile T for new devices.
- ⏭ **৭-ন, ৭-প** confirmed correct, so no change.

## Other factual items

- ✅ **Found in this pass** (১৭.৪.২ ⚠): the box said a 2.8 mm lens "cannot recognise a face at 4 m". The chapter's own DORI table gives 2.8 mm Recognize = 8 m and Identify = 4 m. It now reads "ডেটাশিট অনুযায়ী চার মিটারের বেশি দূরের মুখ শনাক্ত করা যায় না".
- ✅ **Old-review "IR LED-র আলো পোকা টানে"** (unverified): replaced with the checkable mechanism. Insects or spider webs in front of the lens light up under IR and set off motion detection.
- ⏭ **Old-review BNBC shaft numbers** (200 × 400 mm, one per 1500 m²): skipped because they match the stored extract `notes/ch17_bnbc.txt` (1.3.18.1).
- ✅ **MCQ ৪** reworded: "সব পোর্ট মিলিয়ে NVR সর্বোচ্চ কত ওয়াট দিতে পারবে?"
- ✅ **MCQ ৬** now says "কোঅক্সিয়াল ভিডিও কেব্‌ল", so 410 mm can no longer be argued as a second answer.
- ✅ **MCQ ৯** option গ is now "রাতে লেন্স বন্ধ হয়ে যায় বলে". The old option was partly defensible.
- ✅ **MCQ key** is still ১-খ ২-ঘ ৩-ক ৪-খ ৫-গ ৬-ঘ ৭-গ ৮-ক ৯-ক ১০-ঘ ১১-খ ১২-গ, which is ক3/খ3/গ3/ঘ3.
- ✅ **Short question ১৩** now says "চিত্র ১৭.N অনুযায়ী" (an auto number), because BNBC lists five layers.
- ✅ **Math problem ৩** adds "(পোর্টের সংখ্যা যথেষ্ট ধরে নিন)".
- ✅ **Supply OFF**:
  - ১৭.১১ intro: the 230 V supply to the power box, adapters and PoE switch stays off until all wiring is done.
  - Practical ৫ and ৮: supply off while connecting.
  - Practical ৬: supply off, and the 12 V output is checked at 0 V on a multimeter before connecting.
  - Practical ৭: connect with the supply off, then switch on to measure.
- ⏭ **Practical ৪** "ধারাবাহিকতা → কন্টিনিউইটি": terminology, left for stage 2.
- ⏭ **Cross-references** checked: ch03 R = ρL/A and V = IR, ch04 ৪.৪/৪.৫, ch06 P = V × I all exist. There are no forward references (this is the last chapter) and no house-wiring leftovers.

## Sources

- ONVIF Profile S Deprecation Q&A: https://www.onvif.org/?p=8591
- Press release: https://www.securityinfowatch.com/video-surveillance/press-release/55322371/onvif-onvif-to-phase-out-support-for-profile-s-promotes-profile-t-as-successor
- BNBC 1.3.40.1 and 1.3.41 wording ("may be installed using Cat 6", "PVC sheathed … Alluminium foil"): `Book/build/notes/ch17_bnbc.txt` (law.resource.org PDF extract)
- Storage arithmetic uses SI units: 1 Mbps × 86400 s ÷ 8 = 10 800 MB = 10.8 GB.

## Layout

- Before: 56 pages, 0 gaps above 4.5 cm.
- After: 56 pages, 0 gaps.

## For the author

1. **Equations do not show in PDFs converted in this environment.** OMML equations render blank in every PDF that `layout.py` produces here, with their space still reserved. The ch06 PDF from another build shows the same thing, so it is an environment or LibreOffice issue, not the chapter. Page count and gaps are unaffected, but check the maths visually on a normal machine before delivery.
2. **Storage convention.** I chose option (ক) from the review: decimal throughout, 10.8 GB per day. If you prefer to keep 10.55 with a footnote, every number listed under ৭-ঝ changes back.
3. **Not re-copied to the delivery folder.** The rebuilt chapter was not copied into `Book/` or `Book/অধ্যায়-১৭/`.
