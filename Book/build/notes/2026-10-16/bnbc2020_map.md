# BNBC 2012 → BNBC 2020, Part 8 Chapter 1: clause map

Researched 2026-10-16.

## Result: the BNBC 2020 text could not be obtained in this session

No primary 2020 text was read, so **no 2020 clause number or wording below is verified.**

Why nothing could be read:

- **Shell downloads were refused.** The egress proxy returned `403 CONNECT` for every host tried. That includes the official sources (hbri.gov.bd, rajuk.gov.bd, mohpw.gov.bd, dpp.gov.bd, bgpress.gov.bd, bdlaws.minlaw.gov.bd) and the mirrors (law.resource.org, scribd.com, compliancebangladesh.com, blog.dil.com.bd, socebd.com, eab.com.bd). It also includes www.google.com. Only package registries (pypi.org) answered.
- **WebFetch failed on every URL** with `getaddrinfo ENOTFOUND`, even example.com and en.wikipedia.org.
- **WebSearch was the only tool that worked.** It returns a model-written summary of the search hits, not the documents themselves. Across about 15 queries (English and Bangla, clause numbers, distinctive phrases such as "0.376 kW", "1.65", "350 mm", "410 mm", "CCTV monitoring System"), every clause-level hit came from the **2012** PDF at law.resource.org. No search surfaced 2020 Part 8 Chapter 1 text for any of the listed clauses.

As a result, **nothing was downloaded to `scratchpad/bnbc_dl/`.**

## Table

"2020 clause" is **unverified** in every row. Where a secondary source hints at something, the row says so.

| 2012 clause | 2020 clause | same content? | quote of 2020 text | source URL |
|---|---|---|---|---|
| 1.1.1 (scope list incl. CCTV) | not verified | not verified. A secondary Bangla summary of the "BNBC-2020 electrical part" (ElectroAID) lists the same scope items, including security/CCTV, and paraphrases the same opening ("The provisions of the Code presented in this Chapter, cover the Electrical and Electronic Engineering Services for Buildings"), but gives no clause number. | none (secondary paraphrase only) | https://eab.com.bd/scope-and-structures-bnbc-2020-electrical-part-in-bangla/ (could not open; seen as a search snippet only) |
| 1.3.3 (nominal voltages) | not verified | not verified | none | — |
| 1.3.7.4 (1.65 factor for fluorescent lamps, fans, small inductive loads ≤1 kW) | not verified | not verified. Search returned the 1.65 wording only from the 2012 PDF. | none | https://law.resource.org/pub/bd/bnbc.2012/gov.bd.bnbc.2012.08.01.pdf (2012 only) |
| 1.3.9.3.8 (20 % spare capacity) | not verified | not verified | none | — |
| 1.3.9.3.9 (spare way per five circuits) | not verified | not verified | none | — |
| 1.3.9.3.15 + Table 8.1.2 (colour code: R-Y-B / black N / green-yellow E) | not verified | not verified. Search returned only the 2012 table. | none | 2012 PDF only |
| 1.3.9.3.16 | not verified | not verified | none | — |
| 1.3.10.3 (phase balancing) | not verified | not verified | none | — |
| 1.3.17.3 (no board on damp wall) | not verified | not verified | none | — |
| 1.3.17.4(c) (lugs soldered/welded) | not verified | not verified | none | — |
| 1.3.18.2 (sandwich busbar trunking above 9 storeys) | not verified | not verified. **Warning:** see the note on 1.3.18.1 below. | none | — |
| 1.3.18.4 (busduct bars copper) | not verified | not verified (same warning) | none | — |
| 1.3.24.2 | not verified | not verified | none | — |
| 1.3.24.4 (generator changeover, ≥1.25 × main incoming breaker) | not verified | not verified. Search returned the changeover wording only from the 2012 PDF. | none | 2012 PDF only |
| 1.3.27 (a), (c) (overcurrent protection for motors >0.376 kW), (d) (restart prevention) | not verified | not verified. "0.376 kW" returned no BNBC hit at all. | none | — |
| 1.3.37.3.5 (copper earth bar in LT panel/MDB/DB) | not verified | not verified | none | — |
| 1.3.40.1 (RF/video cable ≥350 mm from power) | not verified | not verified | none | — |
| 1.3.41 (data cable ≥410 mm) | not verified | not verified | none | — |
| 1.3.47.8.2 (d) | not verified | not verified | none | — |
| Table 8.1.17 (minimum load density) and Table 8.1.2 (colour code), i.e. the "8.1.x" references | not verified | not verified. A secondary hint (below) suggests table numbers may not line up. | none | — |

The book also uses "৮.১.২" as one of its own section numbers (ch08.py:171, `b.h2(..., "৮.১.২")`). That is the book's numbering, not a BNBC reference. It needs no change.

## Two secondary hints. Both are unverified and point in the same direction.

Both come from a DIFE (Department of Inspection for Factories and Establishments) electrical safety assessment report that cites "BNBC 2020": https://lima.dife.gov.bd/uploads/rtm/assessment_file_path/4341/145_CP_2021_1170_TSS-FASHION_ESA_V00.pdf. I could not open it; what follows is from WebSearch's summary of it.

1. **It cites "article 1.3.18.1 of BNBC 2020" for a load-factor rule** (apply at least 80 % to the estimated load). In the 2012 text, 1.3.18.1 is "Vertical Service Shaft for Electrical Risers". This project's own extract in `Book/build/notes/ch17_bnbc.txt` confirms that. If the assessor quoted 2020 correctly, then **the 1.3.18.x block, and possibly the numbering around it, differs between 2012 and 2020.** The book cites 1.3.18.1, 1.3.18.2, 1.3.18.3(a)/(c) and 1.3.18.4 in ch15 and ch17. The assessor could also simply have mis-cited.
2. **It cites "Table 8.1.24" of BNBC 2020 for generator-room area and spacing** (1.0 m to the walls, 1.25 m between generators). In the 2012 text, Table 8.1.24 is the substation/transformer-room area table. This again suggests either renumbered tables or a mis-citation.

Neither hint is evidence that a particular clause the book cites has moved. They do mean that **"the numbers are the same" cannot be assumed** either.

## Verdict

- **Can the book say "বিএনবিসি ২০২০" with the same clause numbers?** Not on the evidence available. No 2020 clause text was read. The one secondary hint about Part 8 Chapter 1 numbering (DIFE's "1.3.18.1 = load factor") conflicts with the 2012 numbering.
- **Which numbers change:** unknown. The ones most at risk, from the hint above, are the 1.3.18.x busbar-trunking clauses (ch15, ch17) and the "Table 8.1.x" references (Table 8.1.2 in ch03/ch06/ch15, Table 8.1.17 in ch06).
- **Not verifiable here:** every row of the table.
- **Recommendation:**
  - Keep the citations as "বিএনবিসি ২০১২" for now. They are accurate, as citations of the 2012 text the book actually read.
  - Optionally add one line saying that BNBC 2020 (gazetted 11 Feb 2021) is now in force and its clause numbers should be checked.
  - Do the 2012 → 2020 renumbering only after reading the gazetted Volume 3 (Part 8 Chapter 1), from a session or machine that can reach hbri.gov.bd, dpp.gov.bd/bgpress.gov.bd (S.R.O. No. 55-Law/2020), or the uru.gov.bd training PDFs titled "BNBC 2020, Part 8 … Chapter 1" (http://www.uru.gov.bd/en/document/211 and /212).
  - Check 1.3.18.x and the Table 8.1.x numbers first.

## Context gathered from search summaries (secondary)

- BNBC 2020 was published in the Bangladesh Gazette on 11 Feb 2021 as S.R.O. No. 55-Law/2020 (Ministry of Housing and Public Works). Part 8 "Building Services" is in Volume 3. The RSC Technical Guidelines V1.0 state it applies to buildings constructed or occupied after 11 Feb 2021: https://rsc-bd.org/wp-content/uploads/2025/02/RSCTechnicalGuidelinesStandardV1.0.pdf
- The 2020 code was reportedly the 2015 final draft after vetting by the ministries. One secondary source says the gazetted PDF was raw, and a later "enhanced" re-typeset copy "used corrected information": https://blog.dil.com.bd/2021/04/download-gazetted-bnbc-2020-enhanced-file-with-table-of-contents-footers-bookmarkscover-page-etc/. So third-party copies may differ from the gazette; prefer the gazette itself.
- The Urban Resilience Project hosts two RAJUK training decks titled "BNBC 2020, Part 8 Building Services: Chapter 1 Electrical and Electronic Engineering Services for Buildings": http://www.uru.gov.bd/en/document/211 and http://www.uru.gov.bd/en/document/212. Neither could be opened here.
