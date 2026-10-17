# ch09 (DOL স্টার্টার): stage 1 fixes

File touched: `Book/build/ch09.py` only. `dia_ch09.py` was not changed. d13 was checked by eye and is correct.

## Review ch09.md, section ৭

1. ✅ **৯.১.১, আধা অশ্বশক্তি:** "আধা অশ্বশক্তির একটি পাম্পও এই সীমার উপরে" is now "এক অশ্বশক্তির (০.৭৫ kW) একটি ছোট পাম্পও এই সীমার উপরে". Half a horsepower is 0.37 kW, which is below 0.376 kW, so the old sentence was wrong.
2. ⏭ **Starting current 5–7 vs 6–8:** ch09 already used 6–8, which is the book-wide value, so the mismatch has to be fixed in ch07. Inside ch09 the wording was made uniform as "ফুল-লোড কারেন্টের ৬ থেকে ৮ গুণ" in ৯.১.২, সারণি ৯.১, ৯.২.১ and সারসংক্ষেপ. MCQ 2's option "৬–৮" was left alone because it is an answer option. The duration ("এক-দুই সেকেন্ড" here, "এক সেকেন্ডেরও কম" in ch07) was not changed. Both describe small motors, so the ch07 fixer should make that choice.
3. ✅ **৯.২.১, breaker vs ch07's 1.25× rule:** the paragraph now gives the ch07 ৭.৯.৫ result first: the breaker must be at least ৯.২৫ A, so the shop size is ১০ A, and ১৬ or ২০ A is still often seen on site. The next paragraph now says a ১০ A breaker will not trip at ১০ A either, because under IEC 60898-1 an MCB does not trip within one hour at 1.13 × In.
4. ✅ **৯.৯.২ safety box and সারণি ৯.৮, 97-98 logic:** the box now describes "95-96 বাইপাস হয়ে থাকলে (জাম্পার রয়ে গেলে বা ফিউজ থেকে তার সরাসরি STOP-এ গেলে)". In the table row "রিলে কখনো ট্রিপ করে না", the cause "97-98-এ তার লাগানো" is now "95-96 বাইপাস করা".
5. ✅ **উদাহরণ ৯.৬:** the answer is now 5.45 A, with LRD10 and the dial at "5.45 A (প্রায় 5.5)". It now also says LRD12's lowest mark (5.5 A) is above the motor current, so LRD12 cannot be used. This removes the conflict with the "never set outside the scale" rule.
6. ✅ **৯.৩.১:** ইনভার is now "লোহা-নিকেলের সংকর" (was "নিকেল-ইস্পাতের").
7. ✅ **Forward references:**
   - In ৯.১.৩, "যা এই বইয়ের একটু পরের বিষয়" is removed. The sentence now says star-delta reduces starting current and points back to ৭.১০ (checked: ৭.১০ is "থ্রি-ফেজ মোটরের স্টার ও ডেল্টা সংযোগ").
   - The last intro sentence is now self-standing: "মোটর নিয়ন্ত্রণের প্রায় প্রতিটি সার্কিটে এই স্টার্টারটিই কোনো না কোনো রূপে থাকে।"
8. ✅ **Back-references now name the section** (each one checked in ch07.py / ch08.py):
   - ৯.৪.৩ now says "অধ্যায় ৮-এর ৮.৯.৪".
   - ৯.২.২ now says "অধ্যায় ৭-এর ৭.৯.৩-এর সিঙ্গেল ফেজিং" (the safety box is in ৭.৯.৩).
   - উদাহরণ ৯.৬'s note now says "অধ্যায় ৭-এর ৭.৯.৪-এর সারণি". I cited the section rather than "সারণি ৭.৬" so the reference still holds if the ch07 fixer adds a table.
9. ✅ **৯.১১, "দ্বিতীয় ও চতুর্থ সারি":** the rows are now named: 'কোন ত্রুটিতে কাটল' and 'আইসোলেশন'. I assumed the data rows were meant, with the header not counted.
10. ✅ **৯.৭ box:** "৯.৯-এর বাস্তব স্টার্টারের ছবিতে" is now "চিত্র ৯.১৫-এর বাস্তব স্টার্টারে". The number is computed in code (`n_real = fig_n + 4`), and an `assert` checks it after d12 is placed.
11. ✅ **৯.৯.২, supply OFF:**
   - Step 1: the motor leads are removed and insulated while the supply is still off.
   - Step 4: switch off and verify dead with the tester before connecting the motor, and again before swapping two phases.
12. ✅ **সারণি ৯.৬:** "বিশ্রামে" is now "চালুর আগে". The motor column says "চালু হয়" in the START rows and "চলছে" in the running row. I did not use "বন্ধ অবস্থা", because in this table "বন্ধ" already means a closed contact.
13. ✅ **৯.১২:** "প্রায় অর্ধেকই" was a figure with no source. It is now "অনেক ত্রুটিই".
14. ⏭ **গাণিতিক ৫:** the class numbers are already Latin (10, 20 ও 30) in the source. Nothing to change.

## Older review (review_2026-09-23.md, ch09)

- ✅ **[CLARITY] ৯.১০ jumpers:** the text now says which device each number belongs to. On a relay mounted on its own base: 2→3 and 4→5, line into 1, motor from 6. On a relay plugged under the contactor: relay 2/T1 → contactor 3, relay 4/T2 → contactor 5, line into contactor 1. d13 shows the separate-base case, and its labels match.
- ✅ **[SAFETY-minor] ৯.৯.২ step 4:** done, see item 11.
- ⏭ **[MINOR] উদাহরণ ৯.২, "6 s ≥ 5 s":** not wrong (6 ≥ 5 is true), and the note already calls the calculation সাবধানী. Left alone.
- ⏭ **[REGISTER] তুমি-forms:** these belong to stage 2. The four practical-table rows I had to rewrite are now in করুন form. The others (৯.৬ steps, the remaining practical rows) are still তুমি-form.

## Book-wide rules applied

- **Supply OFF in practical tasks:** the পাওয়ার সার্কিট, কন্ট্রোল সার্কিট, সিঙ্গেল ফেজ সংযোগ and ত্রুটি খোঁজা rows now each say to switch off and confirm dead with the tester before wiring. ৯.৯.১ step 1 already said this.
- **MCQ:** the key is ক3 খ2 গ2 ঘ3, which is balanced. Each question has one defensible answer.
- **MCQ 4's weak distractor** ("উপরের দিকে") is a quality issue, not a second correct answer, so it is left for stage 2.
- **বিএনবিসি citations:** not touched.

## Sources

- IEC 60898-1 MCB thresholds (1.13 × In does not trip, 1.45 × In trips, conventional time 1 h): Schneider Electric FAQ FA369327, https://www.se.com/nl/en/faqs/FA369327/
- ch07 ৭.৯.৩ / ৭.৯.৪ / ৭.৯.৫ / ৭.১০ and ch08 ৮.৯.৪: read directly from ch07.py and ch08.py.

## Checks and layout

- `mathguard.py`: clean. No diagram was changed, so `qc.py` was not run.
- Layout before: 33 pages, no gap above 4.5 cm.
- Layout after: 33 pages, no gap above 4.5 cm.

## For the author

- **ch07 vs ch09:** ch07 still says 5–7 times and "এক সেকেন্ডেরও কম". That is for the ch07 fixer.
- **BNBC 0.376 kW vs ch13:** ch09 says every motor above 0.376 kW must have overload protection, but ch13 runs ½–2 HP pumps without an overload relay. This is noted in the older review and needs a decision in ch13.
- **৯.১১ row names:** the two rows named as Siemens' comparison points assume that "second and fourth row" in the old text did not count the header row. Please check this against the Siemens 3RU2 manual if needed.
