from sites import *
import os
name="Jordan Ellis"
nav=[("About Me","home",[("About Me","home")]),
     ("MILE Portfolio","mile",[("MILE Portfolio","mile")]),
     ("Math Ed Portfolio","med",[("Letters & goals","med-letters"),("Teaching philosophy","med-phil"),("Year 1","med-y1"),("Year 2 (in progress)","med-y2"),("Year 3","med-y3"),("Year 4","med-y4"),("Feedback log","med-log")]),
     ("Concluding Reflection","concl",[("Concluding Reflection","concl")])]

home='''<p class="lead">Sophomore · Adolescent/Young Adult Integrated Mathematics · Class of 2029 · Last updated October 2026</p>
<p>I'm from Columbus, and I'm the first person in my family to go to college. I picked math education because my high-school geometry teacher, Mr. Abara, made proofs feel like a game, and I want to do that for someone else. I'm also on the club ultimate team, which is where most of my Sundays go.</p>
<p>This site is a year and a half old. I made it in UNV 101 in August 2025 with two pages and an About Me that I have already rewritten twice. Right now the Year 1 page is done, Year 2 is half-built, and Years 3 and 4 are empty on purpose — my mentor said leave the placeholders up so I can see what's coming. Reading Priya's finished site in a Methods I workshop is what made me realize mine was going to look like that eventually, and also that mine currently doesn't.</p>
<div class="mile"><b>MILE note.</b> One ASC artifact is in (Quantitative Reasoning, from MTH 231). Advanced Writing, two more ASCs, and Capstone are still to come. Concluding Reflection: senior year.</div>'''

mile='''<p class="lead">Started in UNV 101, August 2025 · in progress</p>
<table><tr><th>Requirement</th><th>Artifact</th><th>Course</th><th>Status</th></tr>
<tr><td>About Me</td><td>About Me page</td><td>UNV 101</td><td>Done (revised twice)</td></tr>
<tr><td>ASC · Quantitative reasoning</td><td>Sum of the first n odd numbers is n², three ways</td><td>MTH 231</td><td>Done · S26</td></tr>
<tr><td>ASC · Oral communication</td><td>Lesson plan, taught — planned for EDT 313</td><td>EDT 313 Methods I</td><td>In progress · F26</td></tr>
<tr><td>ASC · (third)</td><td>—</td><td>TBD</td><td>Year 3</td></tr>
<tr><td>Advanced Writing</td><td>Teaching philosophy v3</td><td>EDT 401W</td><td>Year 3</td></tr>
<tr><td>Capstone</td><td>—</td><td>EDT 419</td><td>Year 4</td></tr>
<tr><td>Concluding reflection</td><td>—</td><td>EDT 419</td><td>Year 4</td></tr></table>
<h3>Sum of the first n odd numbers is n², three ways<span class="tag">MILE · ASC Quantitative Reasoning</span></h3>
<h4>Artifact</h4>''' + embed("Ellis_MTH231_OddNumbers_ThreeWays.pdf","Google Drive · 4 pages · MTH 231, March 2026") + '''
<div class="card math">1 + 3 + 5 + ⋯ + (2n−1) = n².&nbsp; By induction (p. 1). By the L-shaped picture — each odd number is an L wrapped around an (n−1)×(n−1) square (p. 2). By pairing terms from the outside in (p. 3).</div>
<h4>Reflection</h4>
<p><b>Process.</b> The assignment was one proof. I did the induction, got it, and felt nothing. Then I drew the squares and actually laughed. I asked Dr. Okafor if I could turn in all three and reflect on which one I'd show a ninth grader. Page 4: the picture, obviously, and then I'd ask them to find the induction in it.</p>
<p><b>Outcomes.</b> I can prove this three ways. The thing I learned isn't the theorem — it's that the proof I'd teach and the proof I was asked for are different, and I should know both.</p>
<p><b>Integration.</b> Mr. Abara used to say "a proof you can't draw is a proof you don't own yet." I put that in Letter 1 without knowing why. Now it's on this page with evidence.</p>
<h4>Feedback &amp; reply</h4>''' + comment("Dr. Okafor","faculty mentor","Apr 3, 2026","Which of the three would a student who hates proofs believe? Not 'understand' — believe.") + comment(name,"student","Apr 6, 2026","The picture. And that bothers me, because it's the least rigorous. I don't know what to do with that yet.",True) + comment("Dr. Okafor","faculty mentor","Apr 7, 2026","Good. Leave it on the page. Come back to it in Methods.") + '''
<h4>Next step</h4><p>Methods I, fall 2026: plan a lesson where the picture comes first and the rigor second, and see if it holds up with real ninth graders.</p>'''

letters='''<p class="lead">One letter each fall. Letter 2 grades the goals in Letter 1.</p>
<h3>Letter 1 · September 2025 (UNV 101)</h3>
<div class="card"><p>Dear Jordan next fall,</p><p>You are a first-gen freshman who picked this major because of one teacher, and you're a little worried that isn't enough of a reason. You want to make proofs feel like a game. You don't know what a lesson plan looks like. You're most looking forward to the first time you're in front of a class and most worried about the first time a kid is smarter than you.</p>
<p>Mr. Abara said "a proof you can't draw is a proof you don't own yet." Write that down somewhere.</p>
<p>Goals: (1) Pass MTH 151 and MTH 231 with B or better. (2) Go to one Howe Center workshop on this portfolio thing. (3) Find out what a lesson plan looks like.</p></div>
<h3>Letter 2 · September 2026</h3>
<div class="card"><div class="goal"><span class="b">✓</span><span>151: B+. 231: A. The A is the odd-numbers proof.</span></div><div class="goal"><span class="b">✓</span><span>Went to two. The second one showed a senior's site (Priya's) and I went home and rebuilt mine.</span></div><div class="goal"><span class="b">✓</span><span>Saw one in a Methods I preview. It has a table of what students will say wrong. I did not know that was a thing.</span></div>
<p style="margin-top:12px">What I got wrong a year ago: "a kid smarter than me" is not the thing to worry about. The odd-numbers page taught me that the proof I'd show a kid isn't the one I'd show a professor, and I'm not sure yet which one is smarter.</p>
<p>Goals: (1) Teach one lesson in EDT 313 with the picture first. (2) Write the wrong-answers table before the lesson, not after. (3) Reply to feedback within a week — right now I'm at about two.</p></div>
<div class="empty">Letter 3 · September 2027 — not yet written</div>
<div class="empty">Letter 4 · September 2028 — not yet written</div>'''

phil='''<p class="lead">Two versions so far. Both kept.</p>
<div class="two">
<div class="v"><h4>v1 · Fall 2025</h4><p>I believe math should feel like a game — the way Mr. Abara taught proofs. Students learn when they're curious, and the teacher's job is to make them curious and then explain things clearly so the curiosity pays off. I want every student to have the moment I had in geometry.</p></div>
<div class="v"><h4>v2 · Fall 2026</h4><p>A proof you can't draw is a proof you don't own yet, and I think that's true for most of mathematics. Students learn when they have a picture before they have the rule. My job is to find the picture (<a data-go href="#mile">odd numbers, p. 2</a>), put it first, and then make them find the rule in it. I'm less sure than I was that "explain clearly" is the job. Dr. Okafor's question — which proof would a student <i>believe</i> — is the one I'm carrying into Methods.</p><p><i>What changed since v1:</i> "make them curious" got replaced by "give them the picture," which is a thing I can actually plan.</p></div></div>
<div class="empty">v3 · Fall 2027 (Advanced Writing) — not yet written</div>
<div class="empty">v4 · Spring 2029 — not yet written</div>'''

y1=f'''<p class="lead">2025–26 · UNV 101, MTH 151, MTH 231, EDT 190 · Complete</p>
<ul><li><a data-go href="#mile">Sum of the first n odd numbers, three ways</a> — MILE ASC artifact, with the "believe" question I'm still carrying.</li>
<li><b>Observation notes · Talawanda High School, Mr. Fields, Geometry · April 2026</b><br>{embed("Ellis_Observation_Fields_Apr2026.gdoc","Google Docs · 2 pages","DOC")}
<p>One visit, 50 minutes. He put a diagram on the board with no words and waited. It took a student almost a minute to say "is that supposed to be congruent?" and then the whole lesson came out of that question. I timed the wait: 52 seconds. I could not have done that. I don't know if I'll be able to.</p></li></ul>
<h3>Muddiest point · Year 1</h3><p>"How do you know which picture to put first?"</p>
<h3>Goal check-in</h3><p>See <a data-go href="#med-letters">Letter 2</a>. All three met, one of them by accident.</p>'''

y2=f'''<p class="lead">2026–27 · EDT 313 Methods I (fall), EDT 190 field experience · Placement: Talawanda High School, Geometry · <b>In progress — last updated October 14, 2026</b></p>
<h3>Lesson plan (draft 2 of ?) · Triangle inequality, grade 9<span class="tag">MILE · ASC Oral Communication · planned</span></h3>
<h4>Artifact</h4>{embed("Ellis_LessonPlan_TriangleInequality_draft2.gdoc","Google Docs · draft · to be taught November 2026","DOC")}
<h4>Context</h4><p>Methods I requires one lesson taught in placement. Mr. Fields offered period 5. Task: students get straws cut to 3, 5, 9 cm and try to make a triangle — they can't — and then figure out the rule. Picture first, rule second (philosophy v2, on purpose).</p>
<h4>Anticipated responses — draft</h4>
<table><tr><th>What students might say</th><th>What I'll say</th></tr>
<tr><td>"It's a triangle if you bend the straw"</td><td>"Can we agree straws stay straight? What if they were metal?"</td></tr>
<tr><td>"3 + 5 = 8, and 8 &lt; 9, so no" (right, fast)</td><td>"Does 3, 5, 8 work?" — the equality case, which I think is the interesting one</td></tr>
<tr><td>"The big one has to be less than the other two together"</td><td>"Say that as an inequality"</td></tr>
<tr><td>?</td><td>Dr. Okafor says there's always a fourth one I haven't thought of. Leaving this row empty until after I teach it.</td></tr></table>
<h4>Reflection — not yet written</h4><div class="empty">Reflection goes here after November 12. I've already decided the Process paragraph will be about the wait time. Goal: 20 seconds. Mr. Fields did 52.</div>
<h4>Feedback &amp; reply</h4>
{comment("Dr. Okafor","EDT 313 instructor","Oct 9, 2026","Draft 2 is much better than draft 1 — you cut the 6-minute intro to 2. Question: the 3-5-8 case. Do you want students to decide it's a triangle or not, or do you want to tell them? Your plan does both.")}
{comment(name,"student","Oct 14, 2026","I want them to decide, and then I want to tell them, which I think means I don't trust them to decide. Working on draft 3. (Five days on this reply — under a week. Goal 3.)",True)}
<h3>Goal check-in · mid-fall</h3>
<div class="goal"><span class="b">~</span><span>Picture-first lesson: planned, not yet taught.</span></div>
<div class="goal"><span class="b">✓</span><span>Wrong-answers table written before the lesson. Three rows and an honest fourth.</span></div>
<div class="goal"><span class="b">~</span><span>Reply time: 5 days, 6 days, 5 days this semester. Down from two weeks.</span></div>
<div class="empty">Second Year 2 artifact (observation notes from EDT 190, spring 2027) — not yet added</div>'''

y3='''<div class="empty"><p><b>Year 3 · 2027–28 · Not started</b></p><p>Planned: second lesson plan (different grade band) · analysis of student work · an assessment I design · teaching philosophy v3 for EDT 401W (MILE · Advanced Writing) · third ASC artifact.</p><p>Placeholder left up on purpose so I can see what's coming.</p></div>'''
y4='''<div class="empty"><p><b>Year 4 · 2028–29 · Not started</b></p><p>Planned: classroom video with commentary (MILE · Capstone) · philosophy v4 beside v1 · growth record · concluding reflection · submit through the MILO form · portfolio presentation.</p></div>'''

log='''<p class="lead">Every comment so far, with reply time. Goal: under 7 days. Year 1 average: 11 days. This fall so far: 5.3.</p>
<table><tr><th>Date</th><th>From</th><th>On</th><th>Reply in</th><th>What I changed</th></tr>
<tr><td>Oct 2025</td><td>Howe Center workshop</td><td>About Me (first draft)</td><td>16 days</td><td>Rewrote it. Then rewrote it again in Sept 2026.</td></tr>
<tr><td>Apr 2026</td><td>Dr. Okafor</td><td><a data-go href="#mile">Odd numbers proof</a></td><td>3 days</td><td>Nothing yet. Carrying the question into Methods.</td></tr>
<tr><td>Sep 2026</td><td>Dr. Okafor</td><td><a data-go href="#med-phil">Philosophy v2</a></td><td>6 days</td><td>Replaced "make them curious" with "give them the picture."</td></tr>
<tr><td>Oct 2026</td><td>Dr. Okafor</td><td><a data-go href="#med-y2">Lesson plan draft 2</a></td><td>5 days</td><td>Draft 3 in progress: decide, don't tell.</td></tr></table>'''

concl='''<div class="empty"><p><b>Concluding Reflection · Spring 2029 · Not yet written</b></p><p>MILE requires this in Capstone. I'm leaving the page here so the site has the same shape as a finished one. When I write it, I want it to start with the "believe" question from April 2026 and say whether I ever answered it.</p></div>'''

pages=[("home","home","About Me",home),("mile","mile","MILE Portfolio",mile),
       ("med-letters","med","Letters & goals",letters),("med-phil","med","Teaching philosophy",phil),("med-y1","med","Year 1 · Begin the record",y1),("med-y2","med","Year 2 · First classroom evidence (in progress)",y2),("med-y3","med","Year 3",y3),("med-y4","med","Year 4",y4),("med-log","med","Feedback log",log),
       ("concl","concl","Concluding Reflection",concl)]
out=site("Jordan Ellis Teaching Portfolio",name,"Teaching Portfolio · Mathematics Education · Miami University · 2025– (in progress)",pages,nav,"Shared with faculty mentor; not published","",theme="playful")
open(os.path.join(OUT_DIR,'jordan.html'),'w').write(out); print(len(out))
