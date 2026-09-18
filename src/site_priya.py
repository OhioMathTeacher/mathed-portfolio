from sites import *
import os
name="Priya Natarajan"
nav=[("About Me","home",[("About Me","home")]),
     ("MILE Portfolio","mile",[("Overview","mile"),("Advanced Writing","mile-aw"),("ASC artifacts","mile-asc"),("Capstone","mile-cap")]),
     ("Math Ed Portfolio","med",[("Letters & goals","med-letters"),("Teaching philosophy","med-phil"),("Year 1","med-y1"),("Year 2","med-y2"),("Year 3","med-y3"),("Year 4","med-y4"),("Feedback log","med-log")]),
     ("Concluding Reflection","concl",[("Concluding Reflection","concl")])]

home=f'''<p class="lead">Senior · Adolescent/Young Adult Integrated Mathematics · Class of 2027 · Student teaching at Talawanda High School, Oxford</p>
<p>I grew up in Mason, Ohio, and came to Miami thinking I would major in actuarial science. A semester of tutoring at the Rinella Learning Center changed that: I liked the moment when someone who "wasn't a math person" got a hard idea more than I liked the math itself. I switched to math education my second semester.</p>
<p>This site holds my MILE portfolio and my Math Ed portfolio. Every artifact has a reflection, and every reflection points at a specific place in the artifact. I started it in UNV 101 in fall 2023 and have added to it every semester since. The old versions of things are still here on purpose — the teaching philosophy page shows all four.</p>
<h3>Who I want to be in a classroom</h3>
<p>A teacher whose students argue about mathematics with each other instead of waiting for me. Someone who plans for the wrong answers, not just the right ones. (That sentence is from my Year 3 philosophy; the Year 1 version said "make math fun," which I now think is the wrong goal.)</p>
<div class="mile"><b>MILE note.</b> This is my About Me page. The MILE artifacts are on the MILE Portfolio page; the Concluding Reflection was submitted through the MILO form in April 2027.</div>'''

mile=f'''<p class="lead">Miami Integrated Learning Experience · started in UNV 101, fall 2023 · submitted to MILO through Capstone (EDT 419), spring 2027</p>
<table><tr><th>Requirement</th><th>Artifact</th><th>Course</th><th>Added</th></tr>
<tr><td>About Me</td><td>About Me page</td><td>UNV 101</td><td>F23</td></tr>
<tr><td>ASC · Quantitative reasoning</td><td>Proof that √2 is irrational, with commentary</td><td>MTH 231 Elements of Discrete Math</td><td>S24</td></tr>
<tr><td>ASC · Oral communication</td><td>Lesson plan, taught: Proportional reasoning, grade 7</td><td>EDT 313 Methods I</td><td>F25</td></tr>
<tr><td>ASC · Problem solving</td><td>Analysis of student work on the "Which is steeper?" task</td><td>EDT 424 field placement</td><td>S26</td></tr>
<tr><td>Advanced Writing</td><td>Teaching philosophy v3, with evidence</td><td>EDT 401W</td><td>F26</td></tr>
<tr><td>Capstone</td><td>Classroom video with time-stamped commentary</td><td>EDT 419 Student Teaching</td><td>S27</td></tr>
<tr><td>Concluding reflection</td><td>Concluding Reflection page</td><td>EDT 419</td><td>S27</td></tr></table>
<p>Each artifact below has its reflection on the same page, as MILE requires. The Math Ed pages hold the same artifacts with more context and the feedback I got on them.</p>'''

mile_aw=artifact_page("Teaching Philosophy v3 — Advanced Writing artifact","MILE · Advanced Writing",
  embed("Natarajan_Philosophy_v3_F26.pdf","Google Drive · 2 pages · EDT 401W, December 2026"),
  "EDT 401W asked for a philosophy statement in which every claim is supported. I rewrote v2 from scratch and then went back through the site linking each sentence that makes a claim to an artifact that shows it.",
  '''<p><b>Outcomes.</b> The assignment was to write something a hiring principal could check. The clearest example is paragraph 2: "I plan for the answers students are likely to give, not just the one I want." That sentence links to the <a data-go href="#med-y2">anticipated-responses table in my Year 2 lesson plan</a> (page 2), and to the <a data-go href="#med-y3">Year 3 student-work analysis</a>, where four of the six strategies I predicted actually showed up.</p>
<p><b>Development.</b> Reading v1 next to v3 is uncomfortable. v1 says "I want to make math fun and accessible." v3 doesn't use the word fun. What replaced it is "students argue about mathematics with each other," which is something I saw happen in the proportional-reasoning lesson and could not have described before I taught it.</p>''',
  comment("Dr. Ayers","EDT 401W instructor","Dec 12, 2026","Paragraph 4 still makes a claim without evidence: \"I use assessment to change what I teach the next day.\" Do you have an artifact for that?")+
  comment(name,"student","Dec 14, 2026","Yes — the Year 3 assessment page. I added the link and a sentence about the re-teach on linear vs. proportional. Thank you; I'd read past it three times.",True),
  '<a data-go href="#med-phil">All four philosophy versions</a> · <a data-go href="#med-y3">Year 3 assessment</a>',
  "Write v4 during student teaching with the video as evidence for the discourse claims.")

mile_asc=f'''<h3>Proof that √2 is irrational, with commentary<span class="tag">MILE · ASC Quantitative Reasoning</span></h3>
<h4>Artifact</h4>{embed("MTH231_sqrt2_proof_annotated.pdf","Google Drive · 3 pages · MTH 231, April 2024","PDF")}
<div class="card math">Suppose √2 = a/b in lowest terms. Then 2b² = a², so a² is even, so a is even; write a = 2k. Then 2b² = 4k², so b² = 2k², so b is even. Both even contradicts lowest terms. ∎</div>
<h4>Reflection</h4>
<p><b>Process.</b> I had seen this proof before and thought I understood it. What I had actually memorized was the shape. The annotated version (page 2) shows the place I got stuck when I tried to write it from nothing: why does a² even imply a even? I had to prove the contrapositive separately, and that is the sentence I now think of as the actual proof.</p>
<p><b>Integration.</b> Two years later, in the proportional-reasoning lesson, a seventh grader said "it's the same because you add 3 to both." That is the same mistake I made here — believing the shape of an argument without checking the step that carries the weight. I did not see the connection until I wrote this reflection in Year 3 for the ASC requirement.</p>
<h3 style="margin-top:36px">Lesson plan, taught: Proportional reasoning, grade 7<span class="tag">MILE · ASC Oral Communication</span></h3>
<p>Full page with anticipated responses, feedback, and reply: <a data-go href="#med-y2">Year 2 → Lesson plan</a>.</p>
<h3 style="margin-top:36px">Analysis of student work: "Which is steeper?"<span class="tag">MILE · ASC Problem Solving</span></h3>
<p>Full page with sorted strategies and what I did next: <a data-go href="#med-y3">Year 3 → Student work analysis</a>.</p>'''

mile_cap=f'''<p class="lead">Capstone artifact · EDT 419 Student Teaching · Talawanda High School, Algebra I, period 4 · March 2027</p>
<p>Full page with the time-stamped commentary and supervisor feedback: <a data-go href="#med-y4">Year 4 → Classroom video</a>.</p>
<p>The Concluding Reflection required by MILE is on its <a data-go href="#concl">own page</a>. I submitted this site's link through the MILO form on April 21, 2027.</p>'''

letters=f'''<p class="lead">One letter each fall, addressed to myself a year later. Each one starts by grading the goals in the one before it.</p>
<h3>Letter 1 · September 2023 (UNV 101)</h3>
<div class="card"><p>Dear Priya-in-a-year,</p><p>You just switched to math ed and you are worried you did it because tutoring felt good and not because you can actually teach. You want to learn how to explain things so people get them the first time. You are looking forward to being in a real classroom and terrified of a kid asking why.</p>
<p>Goals: (1) Get through Calc II with an A. (2) Learn to explain one hard idea three different ways. (3) Observe a real math class before spring.</p></div>
<h3>Letter 2 · September 2024</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>Calc II, A−. Close enough.</span></div><div class="goal"><span class="b">~</span><span>"Three ways" — I can do it for slope. I cannot do it for why a negative times a negative is positive. Half credit.</span></div><div class="goal"><span class="b">✓</span><span>Observed Ms. Reyes's 8th-grade class at Talawanda Middle, twice.</span></div>
<p style="margin-top:12px">What I got wrong a year ago: "explain so people get it the first time." Ms. Reyes almost never explained. She asked. I don't know how to do that yet.</p>
<p>Goals: (1) Teach one full lesson in Methods I without lecturing for more than 5 minutes. (2) Write down the wrong answers I expect before every lesson. (3) Rewrite my philosophy without the word "fun."</p></div>
<h3>Letter 3 · September 2025</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>Lesson taught; 4 minutes of me talking at the start, then groups. It was a mess in a way I could learn from — see Year 2.</span></div><div class="goal"><span class="b">✓</span><span>Anticipated-responses table is now the first thing I write.</span></div><div class="goal"><span class="b">✓</span><span>v2 has no "fun" in it.</span></div>
<p style="margin-top:12px">Goals: (1) Collect real student work and sort it before deciding what to teach next. (2) Reply to every piece of feedback within a week. (3) Ask a question in placement that I don't know the answer to.</p></div>
<h3>Letter 4 · September 2026</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>"Which is steeper?" — sorted 27 responses into five strategies. Year 3.</span></div><div class="goal"><span class="b">~</span><span>Averaged 9 days. Working on it.</span></div><div class="goal"><span class="b">✓</span><span>"Is a vertical line steeper than every other line, or is it not a slope at all?" A student asked this and I said I didn't know and we spent ten minutes on it. Best ten minutes of the semester.</span></div>
<p style="margin-top:12px">Goals for student teaching: (1) Film myself and count my own questions. (2) Have a real re-teach day based on an assessment. (3) Write v4 with the video as evidence.</p></div>
<h3>Letter 5 · April 2027 — to myself at the end of my first year teaching</h3>
<div class="card"><p>You have a classroom now. Reread letter 1. You were afraid of a kid asking why. By now you know that is the whole job. The thing to be afraid of is a room where nobody asks. Keep the anticipated-responses table. Keep replying to feedback within a week — your mentor teacher is your new Dr. Ayers. And rewrite the philosophy in May; v5 is going to disagree with v4, and that is the evidence you are still learning.</p></div>'''

phil=f'''<p class="lead">Four versions, one per year. Nothing was edited in place; each one was rewritten and dated.</p>
<div class="two">
<div class="v"><h4>v1 · Fall 2023</h4><p>I want to make math fun and accessible for every student. Too many people think they are "not math people," and I believe a good teacher can change that with clear explanations, patience, and real-world examples. My goal is for students to leave my class feeling confident.</p></div>
<div class="v"><h4>v4 · Spring 2027</h4><p>Students learn mathematics by doing it in front of each other and defending it. My job is to choose tasks worth arguing about, predict the arguments, and ask the question that moves the argument forward — not to settle it. I plan for the answers students are likely to give (<a data-go href="#med-y2">Y2 lesson plan, p. 2</a>), I sort what they actually give (<a data-go href="#med-y3">Y3 analysis</a>), and I change tomorrow based on it (<a data-go href="#med-y3">Y3 assessment</a>). In the <a data-go href="#med-y4">March 2027 video</a>, students talk for 31 of 48 minutes. That number is the philosophy.</p></div>
</div>
<h3>v2 · Fall 2024</h3><div class="card"><p>Students learn math by doing it, not by watching me do it. My job is to pick good problems and then get out of the way — but not too far out of the way. I watched a teacher this year who almost never explained anything and her students learned more than I did in most lectures. I want to know how she decides when to speak.</p><p><i>What changed since v1:</i> I removed "fun" and "clear explanations." Observation notes from Ms. Reyes's class made me doubt that explaining is the main thing a teacher does.</p></div>
<h3>v3 · Fall 2026 (Advanced Writing artifact)</h3><div class="card"><p>Every claim in this version links to an artifact. <a data-go href="#mile-aw">Read it on the MILE page</a>, with the instructor comment that caught the one claim I hadn't supported.</p></div>'''

y1=f'''<p class="lead">2023–24 · UNV 101, MTH 151, MTH 231 · No placement yet</p>
{artifact_page("Proof that √2 is irrational","ASC Quantitative Reasoning",
  embed("MTH231_sqrt2_proof_annotated.pdf","Google Drive · 3 pages · MTH 231"),
  "Second-semester discrete math. We were asked to write a proof from memory and then annotate where we got stuck.",
  '<p>Full reflection on the <a data-go href="#mile-asc">MILE page</a>. The short version: I had memorized the shape of the proof and not the step that carries it.</p>',
  comment("Dr. Okafor","faculty mentor","May 2, 2024","Good catch on the contrapositive. Keep this page — you will want to come back to \"memorized the shape\" when you start watching students do the same thing.")+
  comment(name,"student","May 6, 2024","I don't totally see what you mean yet, but I'll leave it here.",True)+
  comment(name,"student","Nov 2, 2025","I see it now — see the Integration paragraph I added on the MILE page.",True),
  'Muddiest point, Year 1: "How do you explain something to someone who thinks they already get it?"',
  "Observe a real classroom before spring (goal 3, letter 1).")}
<h3>Observation notes · Talawanda Middle School, Ms. Reyes, 8th grade · March 2024</h3>
{embed("Observation_Reyes_Mar2024.gdoc","Google Docs · 2 pages","DOC")}
<p>Two visits. I counted: in 45 minutes she gave one explanation, lasting about 90 seconds. Everything else was questions. The moment I keep thinking about is a boy who said "the y-intercept is where it starts" and she said "starts what?" and waited eleven seconds. I would have jumped in at three.</p>'''

y2=f'''<p class="lead">2024–25 · EDT 313 Methods I, EDT 190 field experience · Talawanda Middle School</p>
{artifact_page("Lesson plan, taught: Proportional reasoning, grade 7","ASC Oral Communication",
  embed("Natarajan_LessonPlan_Proportional_Gr7.pdf","Google Drive · 4 pages · taught April 15, 2025 · Ohio Learning Standards 7.RP.2"),
  "Methods I required one lesson taught in placement. Ms. Reyes gave me period 3. The task: two mixtures of orange juice concentrate and water — 2 cups concentrate to 3 cups water, versus 3 cups to 5 cups. Which tastes more orange?",
  '''<p><b>Process.</b> I wrote the anticipated-responses table (page 2) the night before. I predicted four strategies: unit rate, scaling to a common amount of water, "add the same to both," and drawing it. Three of those showed up. The fourth thing that showed up I had not predicted: a group said the 3:5 mixture is "more orange because it has more concentrate." That is an absolute-versus-relative error and I had no move ready for it.</p>
<p><b>Outcomes.</b> I talked for 4 minutes at the start — timed by a classmate — then groups worked for 22. Goal 1 from letter 2 met. But the share-out at the end was me re-explaining each group's method, which is not what Ms. Reyes does. Page 4 has my post-lesson notes: "I summarized because I was afraid of the silence."</p>
<p><b>Integration.</b> The "more concentrate" group is my √2 proof: they had the shape of an argument (more stuff → more effect) and didn't check the step. I wrote that connection on the <a data-go href="#mile-asc">MILE page</a> a semester later.</p>''',
  comment("Dr. Okafor","EDT 313 instructor","Apr 20, 2025","Your anticipated-responses table is the best in the section. What would you have said to the \"more concentrate\" group if you'd predicted it?")+
  comment(name,"student","Apr 24, 2025","I think: \"Would 3 cups of concentrate in 100 cups of water be more orange?\" Push the same reasoning until it breaks. I've added it to the table as row 5, so the next version of this lesson has the move ready.",True)+
  comment("Ms. Reyes","cooperating teacher","Apr 16, 2025","The silence is where they think. Next time count to ten before you rescue them.")+
  comment(name,"student","Apr 18, 2025","Counted in my head during the video lesson two years later — see Year 4. I got to twelve.",True),
  '<a data-go href="#med-y1">Year 1 observation notes</a> (the eleven-second wait) · <a data-go href="#med-phil">Philosophy v2</a> · <a data-go href="#med-y3">Year 3 student-work analysis</a> (same standard, real sorting)',
  "Next time, collect the student work instead of just watching it. That became Year 3.")}
<h3>Goal check-in</h3><p>See <a data-go href="#med-letters">Letter 3</a>. Muddiest point, Year 2: "When do you speak?" — still muddy, but I have a number now: not before ten seconds.</p>'''

y3=f'''<p class="lead">2025–26 · EDT 424 Methods II, EDT 401W · Placement: Talawanda High School, Algebra I</p>
{artifact_page("Analysis of student work: “Which is steeper?”","ASC Problem Solving",
  embed("Natarajan_StudentWork_Steeper_27responses.pdf","Google Drive · 9 pages · 27 anonymized responses, sorted · February 2026")+
  '''<div class="work">Task: Line A goes through (0,0) and (4,6). Line B goes through (1,2) and (3,5). Which is steeper? Convince someone who disagrees.</div>
<table><tr><th>Strategy</th><th>n</th><th>Example (student's words)</th><th>Predicted?</th></tr>
<tr><td>Compute slope, compare 3/2 vs 3/2</td><td>9</td><td>"They're both 1.5 so neither"</td><td>Yes</td></tr>
<tr><td>Rise only</td><td>6</td><td>"A goes up 6, B only goes up 3, so A"</td><td>Yes</td></tr>
<tr><td>Subtract instead of divide</td><td>5</td><td>"A: 6−4=2. B: 5−3=2. Same."</td><td>Yes</td></tr>
<tr><td>Graph and eyeball</td><td>4</td><td>"I drew them and B looks steeper"</td><td>Yes</td></tr>
<tr><td>Ratio of y to x at one point</td><td>3</td><td>"B: 2/1 = 2, A: 6/4 = 1.5, so B"</td><td>No</td></tr></table>''',
  "Methods II asked us to give a task in placement, collect every response, and sort before planning the next lesson. Mr. Delgado let me use his second-period Algebra I.",
  '''<p><b>Outcomes.</b> Nine students got it right, and the interesting thing is that 18 didn't, in four different ways. The "subtract" group (page 5) is additive reasoning again — the same error as "add 3 to both" in the seventh-grade juice lesson. I now think this is the misconception, the one that shows up everywhere from grade 6 to Algebra I.</p>
<p><b>Process.</b> The strategy I didn't predict — ratio at one point, which gives the right answer for A and the wrong answer for B — was the most useful, because it's <i>almost</i> slope. I built the next lesson around a student from that group: "Why did your method work for line A?" Page 8 has the lesson that came out of it.</p>
<p><b>Integration.</b> This is the first time I have sorted before deciding what to teach. Goal 1, letter 3. It is also the first time I've had evidence for a philosophy claim rather than a belief — which is why v3 links here.</p>''',
  comment("Mr. Delgado","cooperating teacher","Feb 19, 2026","The kid in the 'ratio at one point' group is the one to build on. Also: 5 of your 6 'rise only' students are the ones who sit by the window. Coincidence?")+
  comment(name,"student","Feb 22, 2026","Not a coincidence — that group had been working together all week and one strong voice. I re-mixed the groups for the follow-up and the rise-only strategy dropped to 2. Added a note on page 9.",True)+
  comment("Dr. Okafor","faculty mentor","Mar 3, 2026","This is the artifact I'd show a principal. One push: your table says 'Predicted?' — what would a table that also tracked 'what I said to them' look like?")+
  comment(name,"student","Mar 8, 2026","Added a fourth column on page 7. Half the cells are empty, which is the honest answer.",True),
  '<a data-go href="#med-y2">Year 2 lesson plan</a> (same misconception, different grade) · <a data-go href="#mile-asc">√2 proof</a> ("memorized the shape") · <a data-go href="#med-phil">Philosophy v3</a>',
  "Design an assessment that catches additive reasoning on purpose, and re-teach based on it.")}
{artifact_page("Assessment I designed: Linear vs. proportional","Methods II",
  embed("Natarajan_Quiz_LinearVsProportional_results.xlsx","Google Sheets · 24 students · March 2026","XLS"),
  "A six-item quiz written to distinguish students who can compute slope from students who understand it as a rate. Items 3 and 5 are deliberately additive traps.",
  '''<p><b>Outcomes.</b> 19 of 24 got item 1 (compute slope from two points). 8 of 24 got item 5 ("A plant grows 3 cm every 2 days. Another plant is 3 cm taller on day 2. Are they the same?"). That gap is the whole point of the quiz. Item 5 became the next day's warm-up — the re-teach Dr. Ayers asked me for evidence of in <a data-go href="#mile-aw">philosophy v3</a>.</p>
<p><b>Process.</b> I graded item 5 wrong for two students who were right — their explanation was correct and their final answer was mis-copied. Rubric revised to weight the reasoning; results sheet has both scorings.</p>''',
  comment("Mr. Delgado","cooperating teacher","Mar 18, 2026","Good quiz. Item 5 is the only one I'd keep on a real test — the others tell you what you already know from homework.")+
  comment(name,"student","Mar 20, 2026","Fair. Next version has three item-5s and one item-1.",True),
  '<a data-go href="#med-y3">Student-work analysis</a> (the misconception this quiz was built to catch)',
  "Film a lesson and count my own questions (goal 1, letter 4).")}'''

y4=f'''<p class="lead">2026–27 · EDT 419 Student Teaching · Talawanda High School, Algebra I, periods 2 and 4 · Mr. Delgado</p>
{artifact_page("Classroom video with commentary: Introducing slope as a rate","MILE · Capstone",
  '<div class="video"><span>Natarajan_Algebra1_P4_Mar2027.mp4 · 48:12 · district consent on file · shared, not published</span></div>',
  "Period 4, March 11, 2027. The lesson opens with the plant-growth item from my Year 3 quiz as a warm-up and builds to defining slope as a rate. Twenty-three students.",
  '''<p><b>Time-stamped commentary</b> (full version, 3 pages, in the Drive folder):</p>
<p><span class="ts">02:10</span> I ask "Are the plants growing the same?" and wait. Twelve seconds. Ms. Reyes said ten, two years ago. A student says "no, because one is 3 taller but the other is 3 per 2 days." That is the whole lesson in one sentence and I didn't say it.</p>
<p><span class="ts">09:45</span> I ask a question I already know the answer to — "so what's the slope?" — and get silence, the bad kind. I should have asked "what does 3 over 2 mean here?"</p>
<p><span class="ts">17:30</span> Group at the back is subtracting. Additive reasoning, again. Instead of correcting, I ask the group next to them to explain their method to the subtracting group. It takes four minutes and it works, and I am not in the conversation.</p>
<p><span class="ts">31:00–41:00</span> Share-out. I counted afterward: students speak for 31 of the 48 minutes. I speak for 14. Goal 1, letter 4.</p>
<p><b>Development.</b> In the Year 2 lesson, I summarized every group's method because I was afraid of silence. Here I don't summarize once. That change is the difference between v2 and v4 of the philosophy, and I can point to the minute where it shows.</p>''',
  comment("Dr. Okafor","university supervisor","Mar 15, 2027","09:45 is the honest moment in this commentary. You noticed it. Now: how many of your 14 minutes were questions you already knew the answer to?")+
  comment(name,"student","Mar 19, 2027","Rewatched and counted: 11 of 19 questions. Worse than I thought. Added a tally to page 3 of the commentary and a goal to the last letter.",True)+
  comment("Mr. Delgado","cooperating teacher","Mar 12, 2027","17:30 — that's teaching. Also you have a period-2 version of this lesson that went worse. Put that one up too.")+
  comment(name,"student","Mar 14, 2027","Period 2 video added to the Drive folder with a one-page comparison. Short version: I rescued them at 6 seconds in period 2. Twelve in period 4. Same lesson, same day.",True),
  '<a data-go href="#med-y2">Year 2 lesson</a> (the summarizing I stopped doing) · <a data-go href="#med-y3">Year 3 quiz</a> (the warm-up) · <a data-go href="#med-phil">Philosophy v4</a>',
  "Count known-answer questions every time I film myself. Letter 5 has the goal.")}
<h3>Growth record</h3><p>Every comment on this site, in order, with its reply, is on the <a data-go href="#med-log">Feedback log</a>. The last entry is from the portfolio presentation on April 16, 2027.</p>'''

log=f'''<p class="lead">Every piece of feedback I've received on this portfolio, with my reply and the days it took me. Goal: under 7.</p>
<table><tr><th>Date</th><th>From</th><th>On</th><th>Reply in</th><th>What I changed</th></tr>
<tr><td>May 2024</td><td>Dr. Okafor</td><td><a data-go href="#med-y1">√2 proof</a></td><td>4 days</td><td>Nothing then. Came back 18 months later.</td></tr>
<tr><td>Apr 2025</td><td>Ms. Reyes</td><td><a data-go href="#med-y2">Lesson plan</a></td><td>2 days</td><td>Started counting wait time.</td></tr>
<tr><td>Apr 2025</td><td>Dr. Okafor</td><td>Lesson plan</td><td>4 days</td><td>Row 5 in the anticipated-responses table.</td></tr>
<tr><td>Feb 2026</td><td>Mr. Delgado</td><td><a data-go href="#med-y3">Student work</a></td><td>3 days</td><td>Re-mixed groups; page 9 note.</td></tr>
<tr><td>Mar 2026</td><td>Dr. Okafor</td><td>Student work</td><td>5 days</td><td>Fourth column: "what I said."</td></tr>
<tr><td>Mar 2026</td><td>Mr. Delgado</td><td>Quiz</td><td>2 days</td><td>Rebalanced items.</td></tr>
<tr><td>Dec 2026</td><td>Dr. Ayers</td><td><a data-go href="#mile-aw">Philosophy v3</a></td><td>2 days</td><td>Linked the assessment claim.</td></tr>
<tr><td>Mar 2027</td><td>Mr. Delgado</td><td><a data-go href="#med-y4">Video</a></td><td>2 days</td><td>Added period-2 comparison.</td></tr>
<tr><td>Mar 2027</td><td>Dr. Okafor</td><td>Video</td><td>4 days</td><td>Known-answer question tally.</td></tr>
<tr><td>Apr 16, 2027</td><td>Portfolio panel</td><td>Presentation</td><td>3 days</td><td>See below.</td></tr></table>
<h3>Presentation feedback · April 16, 2027</h3>
{comment("Dr. Okafor, Dr. Ayers, Dr. Lin","portfolio panel","Apr 16, 2027","Strongest thread: additive reasoning traced from a seventh-grade juice problem to an Algebra I video. Weakest: we don't see much of you working with a student who is struggling for reasons that aren't mathematical. Where is that in the portfolio?")}
{comment(name,"student","Apr 19, 2027","It isn't. The honest answer is that I have avoided writing about it because I don't have a strategy yet, and the portfolio has trained me to only write claims I can point at. I've added it as the first goal in letter 5, and I'll start the Year 1 page of my first-year-teacher portfolio with it.",True)}'''

concl=f'''<p class="lead">MILE Concluding Reflection · submitted via the MILO form, April 21, 2027 · EDT 419</p>
<p>The MILE prompt asks how the pieces of my Miami education connect. My honest answer is that they didn't until this site made them. The √2 proof from MTH 231 and a seventh grader saying "add 3 to both" were two years and two buildings apart, and they are the same idea — believing the shape of an argument without checking the step that carries it. I only saw it because the ASC requirement made me write a reflection on the proof in Year 3, with the juice lesson open in another tab.</p>
<p>What I can do now that I couldn't in fall 2023, with the evidence: I can predict what students will say before a lesson (<a data-go href="#med-y2">Y2 plan, p. 2</a>); I can sort what they actually say and build the next day on it (<a data-go href="#med-y3">Y3 analysis</a>, <a data-go href="#med-y3">Y3 quiz</a>); and I can be quiet for twelve seconds (<a data-go href="#med-y4">Y4 video, 02:10</a>). I cannot yet tell the difference between a student who is stuck on the math and a student who is stuck on something else, and the panel was right to say so.</p>
<p>The habit I'm taking out of Miami is not any of the artifacts. It's the rule that a reflection has to point at something. Four letters, four philosophies, and forty comments later, I don't trust a claim about my teaching that I can't link.</p>
<p><i>— P. N., Oxford, Ohio, April 2027</i></p>'''

pages=[("home","home","About Me",home),("mile","mile","MILE Portfolio",mile),("mile-aw","mile","MILE · Advanced Writing",mile_aw),("mile-asc","mile","MILE · Applied Skills Courses",mile_asc),("mile-cap","mile","MILE · Capstone",mile_cap),
       ("med-letters","med","Letters & goals",letters),("med-phil","med","Teaching philosophy",phil),("med-y1","med","Year 1 · Begin the record",y1),("med-y2","med","Year 2 · First classroom evidence",y2),("med-y3","med","Year 3 · Teach and analyze",y3),("med-y4","med","Year 4 · Student teaching",y4),("med-log","med","Feedback log",log),
       ("concl","concl","Concluding Reflection",concl)]
out=site("Priya Natarajan Teaching Portfolio",name,"Teaching Portfolio · Mathematics Education · Miami University · 2023–2027",pages,nav,"Shared with faculty mentor and cooperating teachers; not published","",theme="editorial")
open(os.path.join(OUT_DIR,'priya.html'),'w').write(out); print(len(out))
