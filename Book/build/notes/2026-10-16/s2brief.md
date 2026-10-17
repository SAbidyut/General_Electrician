# Stage 2 brief — language, headings and structure (whole chapter)

Project: Bangla textbook "জেনারেল ইলেকট্রিশিয়ান", repo /home/user/General_Electrician.
Read /home/user/General_Electrician/CLAUDE.md first (Architecture, Commands, Conventions,
Constraints are binding). Chapter text lives in Book/build/chNN.py, diagram text in
Book/build/dia_chNN.py. Never hand-edit .docx. Do NOT load or use any skill. Do NOT run git.
Touch only your own chNN.py / dia_chNN.py.

The author is publishing this book. Their complaint: it reads as AI-written, many words are
needlessly hard, many sentences are awkward, and headings are unattractive. Stage 1 (factual
fixes) is DONE — the current source is the truth for every fact, number, circuit and
calculation. Do not change any technical content, number, formula, `steps=`, table value,
answer key, or reintroduce anything stage 1 removed. Your job is to rewrite the WORDING.

## Your guide
Your chapter's review: /tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/review/chNN.md
 - §১ headings: apply the proposed headings (keep section numbers; keep "ঠিক আছে" ones).
   Make the same kind of section carry the same name pattern, e.g. every fault section is
   "<যন্ত্র>-এর সাধারণ ত্রুটি ও প্রতিকার". Headings: short formal noun phrases, no
   question form, no em-dash, no metaphor, include the technical term.
 - §২ hard words → simple words.  §৩ sentence rewrites.  §৪ AI patterns.  §৫ consistency.
   §৬ structure.
 Stage 1 changed some text, so a quoted "বর্তমান" may no longer match exactly — rewrite the
 current text in the same spirit. Also read /tmp/.../review/fix_chNN.md to know what stage 1
 changed (do not undo it).
 Go through the WHOLE chapter, not only the quoted items: every paragraph, box, caption,
 table cell with prose, objective, summary bullet, glossary row, question and practical step.

## Book-wide decisions (approved by the author — apply everywhere in your chapter)
1. Register: running prose impersonal ("করতে হয়", "করা হয়", "দেখা যায়"); instructions
   in boxes, steps and practical tasks use আপনি-form ("করুন", "দেখুন", "মাপুন"). No তুমি-forms
   (করো/দেখো/নাও/লেখো/রাখো/বসাও…), no first person (আমরা, করব, বসাই, দিই, করা যাক).
2. Em-dash (—): do not glue clauses or make dramatic reveals with it. Split into two
   sentences, or use comma/colon/বন্ধনী. A dash may remain only as a label separator in a
   list/table/caption ("কয়েল — এনামেল করা তার"). Target: most dashes in prose gone.
3. No dramatic or chatty phrasing: remove teasers, "সবচেয়ে দামি কথা", "যন্ত্রটির ভাষা",
   "ব্যাকরণ", "এক সুতোয় বাঁধা", "জেদি", "স্বভাব", "মজার ব্যাপার", "খারাপ খবর", "ফাঁদ",
   personification of devices, rhetorical questions answered at once, closing moral lines,
   "X নয়, (বরং) Y" antitheses (state Y plainly; keep a contrast only when the wrong idea
   is a real common mistake), "একটিই/এইটুকুই/মাত্র" emphasis, "এক… দুই… তিন" scaffolding
   for rhythm, filler "ঠিক/আসলে/অর্থাৎ/মানে". Use "সবচেয়ে" only for a true comparison.
4. No talk about the book or chapter itself ("এই অধ্যায়ের মেরুদণ্ড", "অধ্যায়টি তিন ভাগে
   সাজানো", "নিচের ছবিতে" without a number, "এই বইয়ের সব ছবিতে"). Refer to a figure as
   "চিত্র N.M" (use the existing bn(b.fig_n) capture pattern, never a hand-typed number that
   could drift; "নিচের চিত্রে" is acceptable only when the figure follows immediately).
   A one- or two-sentence chapter intro that says what the chapter teaches is fine.
5. Terms (one word each, whole chapter, prose + tables + diagrams):
   সার্কিট (not বর্তনী) · রেজিস্ট্যান্স (not রোধ; ch03 may introduce it once as
   "রেজিস্ট্যান্স (রোধ)") · প্যারালাল (not সমান্তরাল) · সিরিজ · বাটন (not বোতাম) ·
   HP (write "অশ্বশক্তি (HP)" only at first use) · লাইভ / ডেড (not জীবন্ত/মরা) ·
   ক্যাবল for cable (never কেবল/কেব্‌ল for cable; কেবল may mean "only" — prefer "শুধু") ·
   ইন্ডাক্টিভ · ফ্রিকোয়েন্সি · ইনস্ট্রুমেন্ট · নেমপ্লেট · আর্থিং.
6. "বন্ধ" ambiguity: switches/breakers are অন/অফ (চালু/বন্ধ for a machine is fine);
   contacts are "বন্ধ (closed)/খোলা (open)" or simply NO/NC. Never let "বন্ধ করুন" be read
   either way.
7. Spelling (Bangla Academy standard): পুরোনো, রুপা, রং, হিসাব, বেয়ারিং, জংশন, পেছন,
   অনুভূমিক, ইচ্ছা, শনাক্ত, সারণি, ক্যাপাসিটর, কন্টাক্টর, ইলেকট্রোম্যাগনেট.
8. Digits: Latin digits for ratings, sizes, model numbers, terminal numbers, units and all
   maths; Bangla digits for ordinary counting words in prose. Never mix the two for the same
   kind of quantity in one sentence.
9. Learning objectives: 7–9 bullets, every one ending "…পারবে।", covering what the chapter
   actually teaches (keep the box's lead-in text as it is).
10. সারসংক্ষেপ: 9–12 bullets, one plain fact each.
11. ⚠ / সতর্কতা boxes only for real safety points. Others become a normal note box or plain
    prose. Box titles: plain nouns ("সতর্কতা", "লক্ষ করুন", "মাঠের অভিজ্ঞতা" is OK).
12. Glossary rows (পারিভাষিক শব্দ): definitions in one plain sentence; trim duplicates.
13. Diagram text (dia_chNN.py): apply 2, 3, 5, 6, 7 to titles, note strips and labels
    (titles: plain noun phrases, no dash slogans like "— একটাও বাদ দেওয়া চলে না"). After
    editing: python3 dia_chNN.py && python3 render.py 'diagrams/chNN/*.svg' &&
    python3 qc.py dia_chNN (0 problems) and look at each changed PNG with Read. No figure
    numbers inside SVGs.
14. Kalpurush rules from CLAUDE.md still hold (no ÷, no Unicode subscripts, no Bangla inside
    b.math()/steps=).

## Voice target
Like a good BTEB/NCTB technical textbook written by an experienced electrician: plain,
formal চলিত Bangla; short-to-medium sentences; one idea per sentence; common words; concrete
field detail kept (part numbers, real faults, what a technician checks) — but stated plainly,
not dramatised. Read every rewritten paragraph back: it must sound like a person wrote it for
students, not like a list of punchlines.

## Build and layout
    export CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
    export LO_PROFILE=/tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/lo_chNN
    cd /home/user/General_Electrician/Book/build
    python3 mathguard.py chNN.py; python3 chNN.py && python3 layout.py "out/<chapter file>.docx" 4.5
Never kill other processes (no pkill). At the end the chapter must have NO page-foot gap
> 4.5 cm. Close gaps by reordering content or by tightening/expanding wording — never by
shrinking figures (CLAUDE.md). Equations now render in this environment.

## Output
Write /tmp/claude-0/-home-user-General-Electrician/18fbdde2-fb8e-587c-8f07-2d25ce0064b8/scratchpad/review/s2_chNN.md:
counts before → after (em-dashes in prose, তুমি-forms, সবচেয়ে, "নয়, বরং"), headings changed,
objectives/summary counts, diagrams changed, layout before → after, anything for the author.
Then run a final self-check: grep your chNN.py for — ; তুমি-verbs ; বর্তনী ; সমান্তরাল ;
বোতাম ; কেব্‌ল ; পুরনো ; রুপো — and fix what remains. Reply with a 5-line summary only.

## One extra diagram check (found in ch08 during stage 1)
ch08 had three figures where L1, L2, L3 (or the motor's three leads, or 2/4/6) were drawn
joined by ONE horizontal bar — electrically a phase-to-phase short. Look at every PNG of your
chapter that shows a three-phase supply, bus or motor feed. Separate phase rails (one line per
phase) are fine; a single line touching all three phase dots is not. Fix any you find in
dia_chNN.py (separate leads), re-render, qc, look again, and list it in your report.
