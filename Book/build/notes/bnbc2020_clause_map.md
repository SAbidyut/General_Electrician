# BNBC 2012 → BNBC 2020 clause map (Part 8, Chapter 1) — verified

Done 2026-10-16 from the gazetted BNBC 2020 PDF (Bangladesh Gazette, extraordinary,
11 Feb 2021, S.R.O. 55-Law/2020), Part 8 Chapter 1. Extracted text:
`notes/bnbc2020_part8_ch1.txt` (`<<PAGE n>>` = 0-based PDF page index).
"PDF idx" below is that index; "gaz." is the gazette page printed on the sheet
(gaz. = idx + 2548). Every 2020 quote was read in the gazette text, not inferred.
The 2012 wording the book relied on is in the chNN.py docstrings and
`notes/ch17_bnbc.txt`. The older unverified attempt is `notes/2026-10-16/bnbc2020_map.md`.

Bangla sub-clause letters follow the book's existing convention:
(a)ক (b)খ (c)গ (d)ঘ (e)ঙ (f)চ (g)ছ (h)জ (i)ঝ (o)ণ (p)ত.

## Result in one line

The 2020 chapter is renumbered almost throughout. Every provision the book cites survives
**with the same content except one: the cable colour code**, which 2020 changes from
red/yellow/blue + black neutral to the IEC code (brown/black/grey + blue neutral).
2020 also adds a CCTV clause (1.3.38) that the book now cites. No citation had to be removed.

## Table

| Book location | 2012 | 2020 | 2020 text (verbatim, short) | PDF idx (gaz.) | Change made |
|---|---|---|---|---|---|
| ch06 ৬.২ note box, summary | 1.3.3 | **1.1.4** | "The nominal voltage in Bangladesh is 230 volts AC single phase and 400 volts AC 3 phase." (scope: "not exceeding 415 V AC between conductors") | 1969 (4517) | number + year |
| ch06 ৬.৮ box, উদাহরণ ৬.৪ given, summary, glossary, MCQ 6, short Q; ch13 docstring | 1.3.7.4 | **1.3.2.4** | "…of the small inductive loads (up to 1.0 kW) the ratings are to be multiplied by a factor of 1.65 to take care of the power factor and the starting current situation. The factor shall be higher for higher rated motors." (same for fluorescent lamps and ceiling/table/pedestal/exhaust fans) | 1998 (4546) | number |
| ch06 ৬.১০ table caption, maths exercise | Table 8.1.17 | **Table 8.1.17** (via 1.3.2.5) | "the minimum load densities to be considered are those shown in Table 8.1.17." All 12 rows the book prints are identical (2020 also lists barber shops 32/75, not printed). | 1998–2000 (4546–4548) | none (year only where stated) |
| ch15 উদাহরণ note (২০% spare) | 1.3.9.3.8 | **1.3.4.3(h) = (জ)** | "Each branch circuit … must have spare capacity to permit at least 20% increase in load…" | 2009 (4557) | number |
| ch15 tip box, fault table | 1.3.9.3.9 | **1.3.4.3(i) = (ঝ)** | "At least one spare circuit must be allowed in the distribution board for each five circuits in use." | 2010 (4558) | number |
| ch03 ৩.১০ safety box, fig caption, objective, summary; ch06 ৬.২.১ para, table ৬.১, summary, MCQ 7; ch15 ১৫.৪.১ para, fig d07, summary, MCQ 4, practical row; dia_ch06/dia_ch15 comments | 1.3.9.3.15 + Table 8.1.2 | **1.3.4.3(o) = (ণ) + Table 8.1.21** (also 1.3.42.3(i)) | "Previously, for a three phase circuit red colour was used for the live (L1), Yellow … (L2), Blue … (L3) cable and the black colour for the neutral … This colour code of cables shall now be replaced by the current IEC cable colour code standards, Table 8.1.21 and Figure 8.1.1." Table 8.1.21 "Current IEC": PE green/yellow, N blue, L/L1 brown, L2 black, L3 grey. 1.3.42.3(i): "For three phase, Brown for L1, Black for L2, Grey for L3, Blue for [neutral]". | 2010–2011 (4558–4559); 2067 (4615) | **SUBSTANCE CHANGED** — book rewritten: BNBC 2020 = IEC code; red/yellow/blue/black kept only as the old code still seen in existing installations. ch06 table gains an "আগের কোডে" column; ch06 adds one sentence that the book's diagrams use the old colours to tell phases apart. ch15 d07 redrawn (old vs 2020 side by side). MCQ keys unchanged (options rewritten: ch06 Q7 answer খ = কালো, ch15 Q4 answer ক = কালো). |
| ch06 ৬.৯ box, fault table, summary; ch15 ১৫.৪.৩, fault table | 1.3.9.3.16 | **1.3.4.3(p) = (ত)** | "After completing the installation balancing should be checked by clamp meter current measurement of each phase." | 2011 (4559) | number |
| ch06 ৬.৯ box | 1.3.10.3 | **1.3.5.3** | "Balancing of circuits in three phase installations shall be arranged in the drawing and also must be done during physical connection." | 2012 (4560) | number |
| ch15 ১৫.৪.২ | 1.3.14.1.6 | **1.3.9.1(f) = (চ)** | "A Switch Board Metal Box must have a small Copper / Brass earthing busbar for terminating the ECCs." | 2019 (4567) | number |
| ch15 tip box, ১৫.৬.৫ | 1.3.17.2 | **1.3.12.2** | "…the size will depend on … the size of the busbars and the type of insulators used for the busbars." | 2022 (4570) | number |
| ch13 practical bullet | 1.3.17.3 | **1.3.12.3** | "These boards shall never be located on water soaked or damp walls." | 2023 (4571) | number |
| ch15 ১৫.৭ | 1.3.17.4(c) | **1.3.12.4(c)** | "Cables shall be connected to terminals only by soldered or welded lugs, unless the terminals are of such form that it is possible to securely clamp them without cutting away the cable strands." | 2023 (4571) | number |
| ch17 ১৭.৮.৫ bullet | 1.3.18.1 | **1.3.13.1** | "For buildings over six-storey or 20 m high … one vertical electrical service shaft of (200 mm x 400 mm) size for every 1500 m2 … (f) CCTV cables" | 2023 (4571) | number |
| ch15 ১৫.৩.৩ (sandwich trunking) | 1.3.18.2 | **1.3.13.2(d) = (ঘ)** | "For more than 9 storied building Busbar preferably sandwiched copper busbar trunking should be used for safety reasons." | 2024 (4572) | number + letter |
| ch15 ১৫.৩.৩ (riser protection) | 1.3.18.2 | **1.3.13.2(g) = (ছ)** | "Each riser cable must have appropriate fuse or circuit breaker protection at the source busbar junction and also at the tap off point." | 2024 (4572) | number + letter |
| ch15 ১৫.৩.৩ | 1.3.18.3(a) | **1.3.13.3(a)** | "…shall be copper of solid rectangular cross-section. The copper bars are insulated. … 200 amperes to 3000 amperes" | 2025 (4573) | number |
| ch15 ১৫.৩.৩ | 1.3.18.3(c) | **1.3.13.3(c)** | "Busbar trunking shall be placed in a dry place and must not be installed in a place which is even slightly exposed to weather/moisture/ spray or sprinkle of water." | 2025 (4573) | number |
| ch15 ১৫.২.১, ১৫.৩.৩ | 1.3.18.4 | **1.3.13.4** | "The busbars shall be copper." (LT busducts) | 2025 (4573) | number |
| ch11 ১১.২ | 1.3.24.1 | **1.3.19.1** | "Provision should be made for standby power supply, in buildings, where interruption … would cause significant discomfort, … cause panic." | 2033 (4581) | number |
| ch11 ১১.২ | 1.3.24.2 | **1.3.19.2** | "…essential light load, … essential lift (s), one or all water pumps…" | 2034 (4582) | number |
| ch11 docstring | 1.3.24.3 | **1.3.19.3** | "Generator room" | 2034 (4582) | number |
| ch11 ১১.২, উদাহরণ ১১.১ note, summary, MCQ 2, short Q | 1.3.24.4 | **1.3.19.4** | "…connected at the supply input point after the energy meter and after the main incoming switch … The rating of such a switch shall be at least 1.25 times the rating of the main incoming circuit breaker. … there is no chance that the generator will be connected and vice versa. … manual … or … automatic type with magnetic contactors." | 2035 (4583) | number (1.25 unchanged) |
| ch07, ch08, ch09, ch10, ch12, ch13, ch14 (all motor citations, incl. boxes, tables, summaries, questions, dia_ch13 comments) | 1.3.27 (a), (c), (d) | **1.3.22 (a), (c), (d)** "Precautions regarding Rotating Machines" | (a) "…shall be suitable for a current at least equal to the full load current rating of the motor…"; (c) "Every electric motor having a rating exceeding 0.376 kW shall be provided with control equipment incorporating means of protection against overcurrent."; (d) "Every motor shall be provided with means to prevent automatic restarting after a stoppage due to drop in voltage or failure. … does not preclude arrangements for starting a motor at intervals by an automatic control device…" | 2040 (4588) | number (0.376 kW and exemptions unchanged; still nothing on starter type, so ch14's statement stands) |
| ch15 ১৫.২.১, ১৫.৪.২, summary | 1.3.37.3.5 | **1.3.32.9** "Earthing busbars" | "A copper earthing busbar shall be provided inside the LT Panel or MDB/DB … Copper earthing busbar shall also be provided inside the DBs, FDBs, SDBs and BDBs. Hexagonal head brass screw, nuts and washers…" | 2053 (4601) | number |
| ch17 ১৭.৮.৫ bullet | 1.3.39.2 | **1.3.34.2** | "A clearance of at least 40 percent must be maintained inside the PVC conduits." | 2062 (4610) | number |
| ch17 ১৭.৫ (coax build), table ১৭.x, safety box, fault table, summary, MCQ 6 | 1.3.40.1 | **1.3.35.1** | "These cables must not be placed in the same conduit with power cables. A distance of at least 350 mm must be maintained if a portion runs in parallel with the power cable conduits." + same coax construction sentence | 2063 (4611) | number |
| ch17 ১৭.৪ choice list, ১৭.৮, table, summary, short Q | 1.3.41 | **1.3.36** | "…the cable shall be in one piece i.e., no joints will be allowed. … at least a distance of 410 mm between these two." | 2063–2064 (4611–4612) | number |
| ch17 ১৭.৮.৫ opening para, safety box, summary | — (none in 2012) | **1.3.38** "CCTV System inside a Building" (new) | "Installation of cable network for CCTV System inside a Building shall be done following the guidelines given for cable work for television antennas/cable television system earlier in this document." | 2066 (4614) | **new citation**; the old sentence "CC ক্যামেরার তার টানার জন্য আলাদা কোনো নিয়ম নেই" was no longer true and was rewritten |
| ch07 ৭.৮ para, summary bullet, docstring | 1.3.47.8.2 (d), (e) | **1.3.42.3**, "Inspection of Low Tension (LT) Installation" list (unlettered bullets) | "Suitable linked switch or circuit breaker or lockable push button is provided near the motors/apparatus … in an easily accessible location; Two separate and distinct earth connections are provided for the motor apparatus;" | 2071 (4619) | number; sub-letters (ঘ)/(ঙ) dropped because the 2020 list is unlettered — cited as "ধারা ১.৩.৪২.৩-এর এলটি পরিদর্শন-তালিকা" |
| ch17 ১৭.১ para (scope names CCTV) | 1.1.1 | **1.1.1 (g)** | "(g) Burglar alarm/CCTV monitoring/security." | 1963 (4511) | year only |
| ch02 ২.৬ para, glossary, MCQ (BNBC Part 8 Ch 1 title) | Part 8 Ch 1 | Part 8 Ch 1 | "PART VIII - BUILDING SERVICES / Chapter 1 / Electrical and Electronic Engineering Services for Buildings" | 1963 (4511) | none (no year or clause printed) |
| mkbook.py imprint ("বইটি সম্পর্কে") | "ধারা নম্বরগুলো ২০১২ সংস্করণের…" | — | — | — | replaced with: book follows বিএনবিসি ২০২০ (পার্ট ৮, অধ্যায় ১; গেজেট ১১ ফেব্রুয়ারি ২০২১) — shorter than before, so the imprint still fits one page |

## Not changed, deliberately

- The book's own diagrams in ch06 and ch08–ch15 still draw L1/L2/L3 red/yellow/blue and
  N black. They were not redrawn (that is most of the book's figures); ch06 ৬.২.১ now says
  in one sentence that these are the old code's colours used to tell phases apart.
  ch15 d07 is the one figure that labelled a colour code as BNBC's, and it was redrawn.
- ch14's "BNBC says nothing about starter type" and the ~7.5 kW DOL figure as field
  practice: still true in 2020 (1.3.22 has no starter-type rule).
- ch17's 40 % conduit clearance is still cited to the telecom-cable clause (1.3.34.2), as
  the book did with 2012's 1.3.39.2.
