from sites import *
import os
name="Marcus Bell"
nav=[("About Me","home",[("About Me","home")]),
     ("MILE Portfolio","mile",[("Overview","mile"),("Artifacts","mile-art")]),
     ("Math Ed Portfolio","med",[("Then / now letter","med-letter"),("Teaching philosophy","med-phil"),("Junior fall · Reconstruct","med-s1"),("Junior spring","med-s2"),("Senior year","med-s3"),("Feedback log","med-log")]),
     ("Concluding Reflection","concl",[("Concluding Reflection","concl")])]

home='''<p class="lead">Senior · Middle Childhood Education, Mathematics &amp; Science · Transferred from Sinclair Community College, fall 2025 · Class of 2027</p>
<p>I'm from Dayton. I did two years at Sinclair while working at a tire shop, mostly gen-eds and math through Calc I, planning to go into engineering. I coached my little brother's rec basketball team for three of those years, and somewhere in there I noticed I was better at explaining a pick-and-roll to eleven-year-olds than I was at wanting to be an engineer. I transferred to Miami as a Middle Childhood major with a math concentration.</p>
<p>I started this site in August 2025, my first semester here, so I didn't have a UNV 101 shell to build on. The Math Ed pages start with a "then / now" letter instead of a first-year letter, and the first artifacts are things I already had from Sinclair, reflected on looking back. My mentor, Dr. Lin, calls it building backward. Everything from spring 2026 on is built forward like everyone else's.</p>
<div class="mile"><b>MILE note.</b> MILO confirmed that my Sinclair ENG 1201 transfers as Advanced Writing-equivalent but that I still owe the artifact and reflection, which is on the MILE page. The three ASC artifacts and Capstone are from Miami courses.</div>'''

mile='''<p class="lead">Started August 2025 (transfer intake) · submitted to MILO through Capstone, spring 2027</p>
<table><tr><th>Requirement</th><th>Artifact</th><th>Course</th><th>Added</th></tr>
<tr><td>About Me</td><td>About Me page + then/now letter</td><td>Transfer intake, EDT 190</td><td>F25</td></tr>
<tr><td>ASC · Quantitative reasoning</td><td>Related-rates problem from Calc I, re-explained for a sixth grader</td><td>Sinclair MAT 2270 (retrospective) — <i>counts per MILO</i></td><td>F25</td></tr>
<tr><td>ASC · Teamwork</td><td>Lesson-study plan: fractions on a number line, grade 6, written with two classmates</td><td>EDT 313 Methods I</td><td>F25</td></tr>
<tr><td>ASC · Problem solving</td><td>Analysis of student work: "Is 3/8 closer to 0, 1/2, or 1?"</td><td>EDT 424 placement</td><td>S26</td></tr>
<tr><td>Advanced Writing</td><td>Teaching philosophy v3 with evidence</td><td>EDT 401W</td><td>F26</td></tr>
<tr><td>Capstone</td><td>Classroom video with commentary</td><td>EDT 419 Student Teaching</td><td>S27</td></tr>
<tr><td>Concluding reflection</td><td>Concluding Reflection page</td><td>EDT 419</td><td>S27</td></tr></table>'''

mile_art=f'''{artifact_page("Related rates, re-explained for a sixth grader","MILE · ASC Quantitative Reasoning · retrospective",
  embed("Bell_Sinclair_MAT2270_RelatedRates_Rewrite.pdf","Google Drive · original problem set (2024) + 2-page rewrite (Sept 2025)"),
  "My Calc I problem set from Sinclair, spring 2024: a ladder sliding down a wall. In September 2025 Dr. Lin asked me to pick one piece of old math and explain it to a hypothetical sixth grader in two pages, then reflect on both versions.",
  '''<p><b>Then.</b> The 2024 solution is correct and I could not tell you today what I was thinking. It's symbols. I got a 9/10 and the one point off was a sign error I didn't understand at the time.</p>
<p><b>Now.</b> The rewrite (page 3) uses a ruler sliding down a book. Doing it for a sixth grader forced me to say what "rate" means before I could use it, and I realized I had never said it out loud. That's the connection to everything I'm learning about middle-school math: kids get stuck on "per" — miles per hour, cups per batch — and I was stuck on it too, I just had the notation to hide it.</p>
<p><b>Integration.</b> Coaching. I could always break a play into steps for a kid. I never did it for myself in math. The rewrite is the first time.</p>''',
  comment("Dr. Lin","faculty mentor","Sep 28, 2025","This is exactly what a retrospective should do. One question to carry forward: where in the ruler explanation does the sixth grader get to do something, rather than watch you?")+
  comment(name,"student","Oct 1, 2025","Nowhere. It's a lecture with a ruler. I'll fix that in the fractions lesson.",True),
  '<a data-go href="#med-letter">Then / now letter</a> · <a data-go href="#med-s1">Junior fall</a>',
  "Write a lesson where the kid does the thing.")}
{artifact_page("Lesson-study plan: fractions on a number line, grade 6","MILE · ASC Teamwork",
  embed("Bell_Chen_Ortiz_LessonStudy_Fractions_Gr6.pdf","Google Drive · 6 pages · team of three · taught by each of us, Nov 2025"),
  "Methods I lesson study: three of us wrote one plan, each taught it in a different placement, then revised together. Task: place 3/8, 5/4, and 7/8 on a number line from 0 to 2 and explain.",
  '''<p><b>Process.</b> First draft (page 1) had me explaining the number line for eight minutes. Chen cut it to two and put the ruler-sliding move from my retrospective in reverse: students build the line themselves with paper strips. Ortiz added the anticipated-responses table — I'd never seen one; it's now on every plan I write.</p>
<p><b>Outcomes.</b> When I taught it (page 4, my notes), two students put 5/4 to the left of 1 "because 4 is bigger than 5 upside down." That's in the anticipated table because Ortiz predicted it. I had the move ready: "show me 4/4 first." Ready moves are the thing I did not have in the ruler explanation.</p>
<p><b>Teamwork.</b> I was the one who pushed back on cutting my explanation, and I was wrong. Page 6 is our revision log, including the argument.</p>''',
  comment("Dr. Lin","EDT 313 instructor","Dec 2, 2025","The revision log is the artifact. Most teams hide the disagreement.")+
  comment(name,"student","Dec 5, 2025","Kept it in. Also kept the 8-minute version on page 1 so the difference is visible.",True),
  '<a data-go href="#mile-art">Ruler retrospective</a> (the lecture I stopped giving) · <a data-go href="#med-s2">Junior spring student-work analysis</a> (same standard, real sorting)',
  "Collect the work next time instead of just teaching.")}
<h3>Analysis of student work · Advanced Writing · Capstone</h3><p>See <a data-go href="#med-s2">Junior spring</a>, <a data-go href="#med-phil">Teaching philosophy v3</a>, and <a data-go href="#med-s3">Senior year</a>.</p>'''

letter='''<p class="lead">Written September 2025, my first month at Miami. Two columns, both dated now: who I was when I started college, and who I am today. Then goals.</p>
<div class="two">
<div class="v"><h4>Then · August 2023, starting at Sinclair</h4><p>I thought math was something you were good at or not, and I was, so I'd be an engineer. I thought teaching was what you did if you couldn't do the thing. I'd have said learning happens when someone explains it right. I was coaching 11-year-olds and did not think of that as teaching.</p></div>
<div class="v"><h4>Now · September 2025, starting at Miami</h4><p>I think coaching was the most teaching I've ever done and I was decent at it because I never explained a play — I ran it slow, then faster. I don't know yet how to do that with fractions. I'm worried that being 22 and starting the program in Year 3 means I'll always be a step behind people who've had two years of methods. I'm looking forward to a real classroom by October.</p></div></div>
<h3>Goals for junior year</h3>
<div class="goal"><span class="b"></span><span>Write one lesson where I explain for less than three minutes total.</span></div>
<div class="goal"><span class="b"></span><span>Find out whether "run it slow, then faster" has a name in math education.</span></div>
<div class="goal"><span class="b"></span><span>Reply to every piece of feedback on this site within a week.</span></div>
<h3>Letter 2 · January 2026 (start of junior spring)</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>Fractions lesson: two minutes. Chen made me.</span></div><div class="goal"><span class="b">✓</span><span>It sort of does: "concrete–representational–abstract." Paper strips, then a drawn line, then the fraction. I'd been doing CRA with a basketball.</span></div><div class="goal"><span class="b">✓</span><span>Average 3 days. Coming from a job where you answer the customer the same day, this one's easy.</span></div>
<p style="margin-top:12px">Goals: (1) Collect and sort student work before planning. (2) Write a philosophy that doesn't mention basketball. (3) Ask Dr. Lin the question I'm avoiding: am I behind?</p></div>
<h3>Letter 3 · August 2026 (start of senior year)</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>"Is 3/8 closer to 0, 1/2, or 1?" — 26 responses sorted. Junior spring.</span></div><div class="goal"><span class="b">✗</span><span>v2 mentions basketball. I've decided that's fine.</span></div><div class="goal"><span class="b">✓</span><span>Asked. She said: "Behind on what? You've taught more hours than most of them." Logged on the feedback page.</span></div>
<p style="margin-top:12px">Goals for student teaching: (1) Film a lesson and time my own explanations. (2) Keep the anticipated-responses table under one page. (3) Write to myself at the end of my first year teaching.</p></div>
<h3>Letter 4 · April 2027 — to myself at the end of my first year teaching</h3>
<div class="card"><p>You started this two years late and finished it on time. The thing you were afraid of in September 2025 — being a step behind — turned out to be backwards. You'd already been teaching for three years; you just hadn't been reflecting. Reread the then/now letter once a year. Keep the revision log with the argument in it. And when a kid puts 5/4 to the left of 1, you already know what to say.</p></div>'''

phil='''<p class="lead">Three versions. v1 is retrospective — what I believed when I started college, written in 2025.</p>
<div class="two">
<div class="v"><h4>v1 · retrospective, written Sept 2025 about Aug 2023</h4><p>Learning happens when someone explains it clearly and you practice. Some people are math people. The teacher's job is to know the material cold and present it in order.</p></div>
<div class="v"><h4>v3 · Fall 2026 (Advanced Writing artifact)</h4><p>Students learn mathematics the way kids learn a play: slow with something in their hands, then faster with a drawing, then fast with the symbols — and they have to run it, not watch it. My job is to build the sequence (<a data-go href="#mile-art">fractions lesson, p. 2–3</a>), predict where it breaks (<a data-go href="#mile-art">anticipated responses, p. 3</a>), and have the next move ready (<a data-go href="#med-s2">"3/8" analysis, strategy 4</a>). There are no math people. There are people who got to run it slow first and people who didn't.</p></div></div>
<h3>v2 · January 2026</h3><div class="card"><p>Explaining is the smallest part of teaching. I coached for three years without explaining a play once — we ran it. The fractions lesson worked when we cut my explanation to two minutes and gave the kids paper strips. I think the teacher's job is to build the thing students run, and to know where they'll trip. (Yes, this mentions basketball.)</p><p><i>What changed since v1:</i> everything except "know the material cold," which I still think is true and which the ruler retrospective showed I hadn't done for "rate."</p></div>'''

s1=f'''<p class="lead">Fall 2025 · Transfer intake, EDT 190, EDT 313 Methods I · Placement: Kramer Elementary, grade 6</p>
<p>The reconstruction semester. Site shell created in August (no UNV 101 shell to inherit). Then/now letter and retrospective philosophy written in September. Two artifacts pulled from prior work, reflected on looking back. Then the first forward artifact: the lesson-study plan.</p>
<h3>Reconstructed artifacts</h3>
<ul><li><a data-go href="#mile-art">Related rates, re-explained for a sixth grader</a> — Sinclair Calc I, retrospective reflection (MILE · ASC Quantitative Reasoning)</li>
<li><b>Coaching practice plan, 2023–24 season</b> — {embed("Bell_RecBasketball_PracticePlans_2023.pdf","Google Drive · 12 pages · not a MILE artifact, but the earliest evidence I have of me teaching anything","PDF").replace('<div class="embed">','<div class="embed" style="margin:8px 0">')}
<p>Retrospective reflection: every practice starts with the same drill at walking speed, then game speed. I wrote "walk it first" on 9 of 12 plans. I didn't know it was pedagogy. Dr. Lin's intake question — "where does the sixth grader get to do something?" — has the same answer as the practice plans: everywhere, or it doesn't work.</p></li></ul>
<h3>First forward artifact</h3>
<p><a data-go href="#mile-art">Lesson-study plan: fractions on a number line</a> (MILE · ASC Teamwork), taught November 2025.</p>
<h3>Mentor intake conversation · September 12, 2025</h3>
{comment("Dr. Lin","faculty mentor","Sep 12, 2025","Read your then/now letter. My one question: you say you're worried about being behind. Behind on what, specifically?")}
{comment(name,"student","Sep 15, 2025","Methods vocabulary, I think. Everyone in EDT 313 says 'anticipated responses' and 'CRA' like they were born knowing it. I didn't have words for what I was doing with the team.",True)}
{comment("Dr. Lin","faculty mentor","Sep 16, 2025","Then the site's job this semester is to give you the words for things you already do. Keep the practice plans on here.")}
<p>Muddiest point, junior fall: "How do you 'walk it first' with a fraction?"</p>'''

s2=f'''<p class="lead">Spring 2026 · EDT 424 Methods II · Placement: Kramer Elementary, grade 6, Mrs. Hadley</p>
{artifact_page("Analysis of student work: “Is 3/8 closer to 0, 1/2, or 1?”","MILE · ASC Problem Solving",
  embed("Bell_StudentWork_ThreeEighths_26responses.pdf","Google Drive · 8 pages · 26 anonymized responses, sorted · March 2026")+
  '''<div class="work">Task: Is 3/8 closer to 0, to 1/2, or to 1? Show how you know. Then do 7/12.</div>
<table><tr><th>Strategy</th><th>n</th><th>Example (student's words)</th><th>Predicted?</th><th>What I said</th></tr>
<tr><td>Benchmark: 4/8 is 1/2, 3/8 is one less</td><td>10</td><td>"Half of 8 is 4 so 3/8 is just under half"</td><td>Yes</td><td>"Do 7/12 the same way."</td></tr>
<tr><td>Whole-number thinking: 3 is small</td><td>6</td><td>"3 is close to 0"</td><td>Yes</td><td>"Is 3/4 close to 0?"</td></tr>
<tr><td>Gap reasoning: 8−3=5, big gap</td><td>4</td><td>"It's 5 away from 8 so it's far from 1"</td><td>Yes</td><td>—</td></tr>
<tr><td>Built it with strips</td><td>4</td><td>(drawing, correct)</td><td>Yes</td><td>"Now do it without the strip."</td></tr>
<tr><td>Decimal: 3÷8=0.375</td><td>2</td><td>"0.375 is closer to 0.5"</td><td>No</td><td>"Where did you learn that?"</td></tr></table>''',
  "Methods II: give a task, collect everything, sort before planning. Mrs. Hadley gave me a full period. This is the same standard as the fall lesson-study, five months later, with the work actually collected.",
  '''<p><b>Outcomes.</b> The "gap reasoning" group is the one I couldn't answer (empty cell). 8−3=5 is right, and it's the wrong kind of right — it's the difference, not the ratio. I've since learned this is additive reasoning and it's everywhere in grades 6–8. The follow-up lesson (page 7) was built on it: 1/2 vs. 50/100, both "far from the top."</p>
<p><b>Process.</b> Four students built it with strips without being told to. They were the four who'd been in my November lesson. That's the only evidence I have that the paper strips stuck, and it's not nothing.</p>
<p><b>Integration.</b> "Walk it first" with a fraction — the muddiest point from the fall — turns out to be a paper strip. Answered, sort of. New muddiest point: how do you get them to stop needing the strip?</p>''',
  comment("Mrs. Hadley","cooperating teacher","Mar 20, 2026","The two decimal kids are the ones with the tutor. Don't build the class around them.")+
  comment(name,"student","Mar 22, 2026","Noted — I'd been planning to have them present. Follow-up lesson leads with the strips group instead.",True)+
  comment("Dr. Lin","faculty mentor","Apr 1, 2026","'What I said' column with an empty cell is the most honest table I've seen this year. Fill it in when you know.")+
  comment(name,"student","Apr 3, 2026","Filled in on page 7 after the follow-up: \"Is 5 away from 8 the same as 5 away from 100?\" It worked on two of the four.",True),
  '<a data-go href="#mile-art">Fall lesson study</a> (same standard) · <a data-go href="#mile-art">Ruler retrospective</a> ("per" was my gap too) · <a data-go href="#med-phil">Philosophy v2</a>',
  "Design the assessment that catches additive reasoning on purpose — senior fall.")}'''

s3=f'''<p class="lead">2026–27 · EDT 401W (fall), EDT 419 Student Teaching (spring) · Talawanda Middle School, grade 7, Mr. Nowak</p>
<h3>Senior fall</h3>
<ul><li><a data-go href="#med-phil">Teaching philosophy v3</a> — Advanced Writing artifact, every claim linked (MILE).</li>
<li><b>Assessment: ratio vs. difference, grade 7</b> — {embed("Bell_Quiz_RatioVsDifference_results.xlsx","Google Sheets · 28 students · November 2026","XLS")}<p>Five items; items 2 and 4 are additive traps ("Team A won 6 of 10, Team B won 8 of 14 — who did better?"). 22/28 correct on the plain ratio item, 9/28 on item 4. The next day's lesson was item 4. This is the "re-teach based on evidence" claim in v3, and the reason it links here.</p></li></ul>
<h3>Senior spring</h3>
{artifact_page("Classroom video with commentary: Comparing ratios","MILE · Capstone",
  '<div class="video"><span>Bell_Grade7_P3_Feb2027.mp4 · 44:30 · district consent on file · shared, not published</span></div>',
  "Period 3, February 24, 2027. Warm-up is item 4 from the fall quiz. Twenty-six students, paper strips available but not required.",
  '''<p><span class="ts">00:00–02:40</span> I explain the task. 2 minutes 40 seconds. Fall 2025 me would have taken eight. Goal 1 from the then/now letter, on film.</p>
<p><span class="ts">06:15</span> Group 4 says Team B did better "because 8 is more than 6." Whole-number thinking — strategy 2 from the 3/8 analysis. I ask "did Team B play more games?" and leave. They get there in about a minute without me.</p>
<p><span class="ts">14:50</span> Group 1 says "A because they lost less" — 4 losses vs. 6. Gap reasoning, the empty cell from last spring. This time I have the move: "Team C won 90 of 100 and lost 10. Better or worse than A?" It takes them four minutes and they argue with each other, not me. This is the minute I'd show a principal.</p>
<p><span class="ts">30:00–40:00</span> Share-out. Two groups present; I ask the room to say whether they agree and why, and don't say whether I agree. Mr. Nowak's note afterward: "you never gave the answer." I didn't notice.</p>
<p><b>Development.</b> Junior fall: the ruler lecture. Senior spring: 2:40 of explaining, and a ready move for the error I couldn't answer a year ago. Both are on this site with dates.</p>''',
  comment("Mr. Nowak","cooperating teacher","Feb 25, 2027","You never gave the answer. Some of them left not sure. Is that OK?")+
  comment(name,"student","Feb 27, 2027","I think it's OK for a day, not for a week. The exit ticket the next day (added to the Drive folder) shows 21/26 got item 4 — up from 9/28 in the fall. The five who didn't get the strips back and me for ten minutes.",True)+
  comment("Dr. Lin","university supervisor","Mar 2, 2027","14:50 is the whole portfolio in four minutes. For the presentation: put the empty cell from last spring next to this clip.")+
  comment(name,"student","Mar 4, 2027","That's the presentation. Slide 1 is the empty cell.",True),
  '<a data-go href="#med-s2">3/8 analysis</a> (the empty cell) · <a data-go href="#med-s1">Ruler retrospective</a> · <a data-go href="#med-phil">Philosophy v3</a>',
  "Letter 4 has the goals for year one. Keep the revision log.")}'''

log=f'''<p class="lead">Every comment on this site, with reply time. Goal: under 7 days. Average so far: 2.9.</p>
<table><tr><th>Date</th><th>From</th><th>On</th><th>Reply in</th><th>What I changed</th></tr>
<tr><td>Sep 2025</td><td>Dr. Lin</td><td>Then/now letter (intake)</td><td>3 days</td><td>Kept the practice plans on the site.</td></tr>
<tr><td>Sep 2025</td><td>Dr. Lin</td><td><a data-go href="#mile-art">Ruler retrospective</a></td><td>3 days</td><td>Next lesson: kids do the thing.</td></tr>
<tr><td>Dec 2025</td><td>Dr. Lin</td><td><a data-go href="#mile-art">Lesson study</a></td><td>3 days</td><td>Kept the 8-minute draft visible.</td></tr>
<tr><td>Mar 2026</td><td>Mrs. Hadley</td><td><a data-go href="#med-s2">3/8 analysis</a></td><td>2 days</td><td>Led with the strips group.</td></tr>
<tr><td>Apr 2026</td><td>Dr. Lin</td><td>3/8 analysis</td><td>2 days</td><td>Filled the empty cell.</td></tr>
<tr><td>Feb 2027</td><td>Mr. Nowak</td><td><a data-go href="#med-s3">Video</a></td><td>2 days</td><td>Added exit-ticket data.</td></tr>
<tr><td>Mar 2027</td><td>Dr. Lin</td><td>Video</td><td>2 days</td><td>Presentation structure.</td></tr>
<tr><td>Apr 14, 2027</td><td>Portfolio panel</td><td>Presentation</td><td>4 days</td><td>See below.</td></tr></table>
<h3>"Am I behind?" · August 2026</h3>
{comment(name,"student","Aug 28, 2026","The question I'd been avoiding: I started in Year 3. Am I behind?",True)}
{comment("Dr. Lin","faculty mentor","Aug 29, 2026","Behind on what? You've taught more hours than most of the cohort, you just called it coaching. The site shows it. Stop asking.")}
<h3>Presentation feedback · April 14, 2027</h3>
{comment("Dr. Lin, Dr. Okafor, Dr. Ayers","portfolio panel","Apr 14, 2027","The empty cell → 14:50 clip is the clearest single piece of evidence of growth we saw this year. Push: your reflections are all about the mathematics. Where's the student who isn't doing the math for a non-math reason?")}
{comment(name,"student","Apr 18, 2027","Same note Priya got, I hear. Honest answer: I coached those kids for three years and never wrote anything about them either. Goal 1 in letter 4.",True)}'''

concl='''<p class="lead">MILE Concluding Reflection · submitted via the MILO form, April 20, 2027 · EDT 419</p>
<p>I came to Miami as a transfer in fall 2025 with a Calc I problem set, twelve basketball practice plans, and a belief that some people are math people. The MILE prompt asks how my experiences connect. For me the connection was retroactive: the portfolio made me reflect on things I'd already done, and the practice plans turned out to be the most important artifact on the site even though they aren't a MILE requirement. "Walk it first" was pedagogy. I just didn't have the word.</p>
<p>What I can do now, with the link: explain for under three minutes (<a data-go href="#med-s3">video, 0:00–2:40</a>); predict the errors and have a move ready (<a data-go href="#med-s2">the filled-in cell</a>, <a data-go href="#med-s3">14:50</a>); and change tomorrow based on what students actually did (<a data-go href="#med-s3">fall quiz → February warm-up</a>). What I can't do yet, per the panel, is write about a student who isn't doing math for reasons that aren't mathematical. Letter 4, goal 1.</p>
<p>Two years late, on time. The habit I'm keeping is the then/now column. Every August: what did I believe a year ago, what do I believe now, and what on this site shows the difference.</p>
<p><i>— M. B., Oxford, Ohio, April 2027</i></p>'''

pages=[("home","home","About Me",home),("mile","mile","MILE Portfolio",mile),("mile-art","mile","MILE artifacts",mile_art),
       ("med-letter","med","Then / now letter & goals",letter),("med-phil","med","Teaching philosophy",phil),("med-s1","med","Junior fall · Reconstruct",s1),("med-s2","med","Junior spring · Teach and analyze",s2),("med-s3","med","Senior year · Placement and student teaching",s3),("med-log","med","Feedback log",log),
       ("concl","concl","Concluding Reflection",concl)]
out=site("Marcus Bell Teaching Portfolio",name,"Teaching Portfolio · Middle Childhood Mathematics · Miami University · transfer 2025–2027",pages,nav,"Shared with faculty mentor and cooperating teachers; not published","",theme="bold")
open(os.path.join(OUT_DIR,'marcus.html'),'w').write(out); print(len(out))
