# Fix brief — stage 1: factual / technical / safety errors only

Project: Bangla textbook "জেনারেল ইলেকট্রিশিয়ান", repo /home/user/General_Electrician.
Read /home/user/General_Electrician/CLAUDE.md first (Architecture, Commands, Conventions,
Constraints sections are binding). The book is GENERATED: each chapter's text lives in
Book/build/chNN.py, its diagrams in Book/build/dia_chNN.py. Never hand-edit .docx.

The author approved a review. THIS STAGE fixes only the errors — wrong facts, wrong
numbers, unsafe instructions, wrong/forward cross-references, contradictions,
syllabus gaps, ambiguous/double-answer MCQs, unbalanced MCQ keys. Do NOT do the general
language/style rewrite yet (that is stage 2) — but where you must rewrite a sentence to
fix it, write it in plain, formal, student-friendly Bangla (impersonal voice or "করুন";
no তুমি-forms, no em-dash-glued clauses, no dramatic phrasing).

## Your input
1. Section "### ৭." (and any factual items elsewhere) of your chapter's review file:
   /tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/review/chNN.md
2. Your chapter's items in Book/build/notes/review_2026-09-23.md (an older review;
   take only factual/safety/consistency items; ch01–03 items there were already fixed).
3. Book-wide decisions that touch facts (apply inside your chapter):
   - Motor starting current (DOL) is written everywhere as "ফুল-লোড কারেন্টের ৬ থেকে ৮ গুণ".
   - No reference to a chapter the reader has not reached yet (later chapter number) —
     remove or make the sentence self-standing. References back to earlier chapters must
     point to a section that really contains that content (open that chapter's chNN.py
     and check).
   - House-wiring-book leftovers (গৃহওয়্যারিং, হাউস ওয়্যারিংয়ে, series board / switch
     board / two-way-switch chapters that do not exist in this book) are reframed for a
     general electrician.
   - Every practical task that touches wiring must say the supply is OFF (and verified
     dead) before wires are removed/changed.
   - MCQ answer key balanced across ক/খ/গ/ঘ (difference ≤1) and every MCQ has exactly
     one defensible answer.
   - "বিএনবিসি ২০১২" citations: leave as they are in this stage (handled separately).

## How to work
- Verify before you change. Every number or rule you introduce must be checkable: use
  web search (WebSearch/WebFetch via ToolSearch) for datasheets/standards when the review
  marks something "to verify" or when you are not certain. If you cannot verify a claim,
  soften or remove it — never invent a number, clause or standard. If you decide a review
  item is NOT actually an error, skip it and say why.
- If a figure (diagram) is wrong, fix dia_chNN.py, then from Book/build:
    python3 dia_chNN.py && python3 render.py 'diagrams/chNN/*.svg' && python3 qc.py dia_chNN
  (qc must report 0 problems) and look at the changed PNG with the Read tool.
  If a figure number appears hard-typed in prose, keep it right.
- Syllabus gaps (only where the review names one for your chapter) are filled with a real
  section in the chapter's existing style (heading, prose, a table or steps, practical
  task), reusing existing diagrams/helpers where possible.
- Run `python3 mathguard.py chNN.py` if you touched maths.
- Build and check layout. ALWAYS use these env vars (several builds run in parallel):
    export CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
    export LO_PROFILE=/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/lo_chNN
    cd /home/user/General_Electrician/Book/build
    python3 chNN.py && python3 layout.py "out/<the chapter file>.docx" 4.5
  Record the layout result BEFORE your first edit (baseline), and at the end. No new
  page-foot gap > 4.5 cm may remain that was not in the baseline; close gaps by
  reordering content (CLAUDE.md), never by shrinking figures.
- Touch only your own chNN.py / dia_chNN.py / assets. Do NOT edit bookkit.py, svgkit.py,
  render.py, layout.py, mkbook.py, CLAUDE.md, or other chapters' files. Do NOT run git.
  Do NOT load or use any skill.

## Output
Write /tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/review/fix_chNN.md:
  - each item: ✅ fixed (what changed, in one line, with section no.) / ⏭ skipped (why)
  - sources used for any verified number (URL)
  - layout before → after (pages, gaps)
  - anything that needs the author's decision.
Reply with a 5-line summary only.
