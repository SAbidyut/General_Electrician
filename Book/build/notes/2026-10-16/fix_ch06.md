# fix_ch06 — stage 1 (factual / technical / consistency)

## Items
- ✅ উদাহরণ ৬.২ ব্রেকার (review ৭.১): ১৬A রাখা হয়েছে, কারণ স্পষ্ট করা হলো ("১০A-তে ব্রেকার প্রায় পূর্ণ লোডে চলবে"), আর মন্তব্যে লেখা হলো যে ১৬A নিলে মেইন তারও অন্তত ১৬A বহনক্ষম হতে হবে। ৬.৪-এর ৫.৮ A → ১০A-এর সঙ্গে আর অসংগতি নেই (একটির ব্রেকার প্রায় পূর্ণ লোডে, অন্যটির নয়)।
- ✅ ডাইভার্সিটি ফ্যাক্টরের সংজ্ঞা (৭.২; পুরোনো রিভিউ A7): পারিভাষিক শব্দে সঠিক সংজ্ঞা দেওয়া হলো (আলাদা সর্বোচ্চ চাহিদার যোগফল / মোট সর্বোচ্চ চাহিদা, মান ≥ ১) এবং নতুন সারি Demand Factor যোগ হলো (সর্বোচ্চ চাহিদা / সংযুক্ত লোড, ≤ ১)। সারণি ৬.৫-এর সারিটি এখন "কোন লোড একসঙ্গে চলে তা বিবেচনা করে সর্বোচ্চ চাহিদা ধরতে হবে (ডিমান্ড ফ্যাক্টর)"।
- ✅ জেনারেটরের রেটিং (৬.৫, পুরোনো রিভিউ): "kW-এ লেখা থাকে না" কথাটি সরানো হলো। এখন লেখা আছে: মূল রেটিং kVA-তে দেওয়া হয়; নেমপ্লেটে kW-ও থাকে, তবে একটি নির্দিষ্ট পাওয়ার ফ্যাক্টরে (সাধারণত ০.৮)।
- ✅ MCQ ৮ "জেনারেটরের রেটিং কোন এককে লেখা থাকে?" প্রশ্নটির দুটি উত্তর সমর্থনযোগ্য ছিল (kW ও kVA), তাই এখন "ট্রান্সফরমারের রেটিং…" (উত্তর গ, kVA)। সংক্ষিপ্ত প্রশ্ন ৮-ও সেই অনুযায়ী বদলানো হলো।
- ✅ সারণি ৬.৫ "মোটরের kVA" (৭.৩): সারির লেখা আগেই জেনারেটর ছিল। ব্যবহারিক কাজ ৪ বদলে করা হলো "জেনারেটর বা ইউপিএসের নেমপ্লেট পড়ে kVA থেকে kW নির্ণয়"।
- ✅ সারণি ৬.২-এ এলইডি (৭.৪): ০.৯ → "০.৫–০.৯", ধরন "ইলেকট্রনিক (ড্রাইভারভেদে)"। ইলেকট্রনিক ব্যালাস্টের সারিতে আগেই "ইলেকট্রনিক" লেখা ছিল।
- ✅ ৬.৪.১ "অর্ধেক লোডে বিদ্যুৎ টানে বেশি" (৭.৫): নতুন লেখা: হালকা লোডে পাওয়ার ফ্যাক্টর ও দক্ষতা কমে যায়, তাই একই কাজে লাইনে বেশি কারেন্ট লাগে।
- ✅ MCQ উত্তরমালা ক২ খ৪ গ৩ ঘ১ থেকে ক২ খ৩ গ৩ ঘ২: প্রশ্ন ৪-এর বিকল্প (খ) ১.৭৩২ ও (ঘ) ৩.০ অদলবদল করা হলো, তাই উত্তর এখন ঘ।
- ✅ MCQ ১০: (ঘ) "কিছুই বদলায় না" (যা (ক)-এর প্রায় একই কথা) বদলে "ব্রেকার ছোট হয়ে যায়"।
- ✅ চিত্র ৬.৬ (d06_steps) লেখার সঙ্গে সাংঘর্ষিক ছিল: "বিএনবিসি গুণক" আর "পাওয়ার ফ্যাক্টর" দুটি পরপর ধাপ হিসেবে আঁকা ছিল, অথচ ৬.৮ বলে দুটি একসঙ্গে বসানো যাবে না। এখন ধাপগুলো: তালিকা → মোট ওয়াট → "১.৬৫ গুণক বা cos φ" → কারেন্ট → ব্রেকারের মাপ, আর নোট-স্ট্রিপে লেখা "যেকোনো একটি; দুটি একসঙ্গে নয়"। qc ০, PNG চোখে দেখে যাচাই করা হয়েছে।
- ✅ উদাহরণ ৬.১-এর প্রদত্ত অংশে "cos φ = 1" আগাম এসে পড়ছিল (৬ অংশ)। এখন লেখা আছে "লোড খাঁটি রেজিস্টিভ"।
- ⏭ ৭.৬ (≈৭ A) এবং ৭.৭ (১.৭৪ গুণ): লেখায় আগেই ঠিক করা ছিল।
- ⏭ ৭.৮ বিএনবিসির উল্লেখের ধরন: এই পর্যায়ে বাদ রাখার কথা (ব্রিফ)।
- ⏭ পারিভাষিক শব্দ থেকে Frequency, RMS, Peak, Impedance বাদ দেওয়া, শিখনফল, বাক্সের ধরন, ভূমিকা: এগুলো কাঠামো বা ভাষার বিষয়, ভুল নয়। দ্বিতীয় পর্যায়ের জন্য রাখা হলো।
- ⏭ MCQ সংখ্যা ১০টি (অন্য অধ্যায়ে ১৫–১৬টি): কাঠামোর বিষয়।

## Sources
- Diversity/demand factor: https://en.wikipedia.org/wiki/Diversity_factor ; https://electrical-engineering-portal.com/demand-factor-diversity-factor-utilization-factor-load-factor ; https://www.ecmag.com/section/codes-standards/diversity-vs-demand-dont-be-confused-these-terms
- LED PF 0.5–0.6 in low-cost lamps (EPA/ENERGY STAR docs): https://cmadmin.energystar.gov/sites/default/files/NRDC%20Comments_2.pdf ; https://blog.1000bulbs.com/home/power-factor-explained
- Generator kVA/kW at 0.8 pf: https://kirloskaroilengines.com/products/power-gen/200-kva---250-kva ; https://generatorsource.com/power-insights/understanding-diesel-generator-specifications-kw/
(Proxy blocks direct page fetches in this session, so these were checked through search-result extracts only.)

## Layout
Before: 20 pages, no gap > 4.5 cm. After: 20 pages, no gap > 4.5 cm.

## Author decisions
- Ex ৬.২ keeps 16A (with a stated reason). If you prefer 10A for a 9.2 A load, change the answer only, since no other text depends on it.
