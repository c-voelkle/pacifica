import sys,re
sys.path.insert(0,'/home/claude/work/merge')
from blocks import blocks,R
B={f:blocks(f) for f in ['CR-059','CR-060','CR-061','CR-062','CR-063','CR-064','CR-065','CR-067','CR-068']}
def q(f,n):
    k,t=B['CR-'+f][n]; assert k=='q',(f,n,t[:50]); return t
L=open('/home/claude/work/merge/canon_8_13.md',encoding='utf8').read().split('\n')
P={i:l for i,l in enumerate(L)}
def rep(i,old,new,cnt=1):
    assert P[i].count(old)==cnt,(i,old[:60],P[i].count(old)); P[i]=P[i].replace(old,new)
def span(i,a,b,new):
    s=P[i]; x=s.index(a); y=s.index(b,x)+len(b); P[i]=s[:x]+new+s[y:]
def after(i,*paras):  P[i]=P[i]+''.join('\n\n'+p for p in paras)
def before(i,*paras): P[i]=''.join(p+'\n\n' for p in paras)+P[i]
c066=[l[2:] for l in open(R+'CR-066.md',encoding='utf8').read().split('\n') if l.startswith('> **[PROPOSED — CR-066]** In December 1862')][0]
c060line=[l[2:] for l in open(R+'CR-060.md',encoding='utf8').read().split('\n') if l.startswith('> **[PROPOSED — CR-060]** In the Rockies the line follows')][0]
# ---------- §8
rep(34," **[OPEN]** Annual flows"," "+q('068',4)+" **[OPEN]** Annual flows")
after(62,'<!-- CR-059 -->\n'+q('059',3),q('059',4),q('059',5),q('059',6))
m=re.search(r"; Britain refuses to support a war of Californian expansion, and the London bondholders warn[^.;]*",P[86]); assert m
P[86]=P[86].replace(m.group(0),"; <!-- CR-068: no bondholders in 1860 -->Britain refuses to support a war of Californian expansion")
after(88,q('068',8))
# ---------- §9
after(99,''); P[99]=P[99].rstrip()+' '+q('068',10)
after(99,'<!-- CR-064 -->\n'+q('064',3))
sh="Sherman organizes readiness and reserves in the proposed office of Inspector-General, initially supporting protection while challenging the expanding objectives."
rep(107,' '+sh,'')
after(107,q('068',12),sh+' <!-- CR-067 -->'+q('067',2))
# ---------- §10
w="John Whiteaker negotiates civil protections without conceding a governor's right to transfer Oregon's allegiance."
assert w in q('059',9); rep(115,w,'<!-- CR-059 -->'+q('059',9))
after(121,'<!-- CR-059 -->\n'+q('059',12),q('068',14))
P[125]='<!-- CR-060 -->\n'+q('060',3)
idaho="Idaho's mining districts turn toward the Northwest in 1863, western Montana's camps toward Salt Lake and Walla Walla in 1863–1864."
assert idaho in P[127]
P[127]='\n\n'.join(['<!-- CR-061 -->\n'+q('061',3),q('061',4),q('061',5),q('061',6),q('061',7),'<!-- CR-066 -->\n'+c066,q('061',9),q('061',10),q('061',11),
   idaho+' <!-- CR-060 -->'+q('060',6)])
P[129]='\n\n'.join(['<!-- CR-060 -->\n'+q('060',9),q('060',13),q('060',10),'<!-- CR-061 -->\n'+q('061',15),q('061',16),q('061',17)])
# ---------- §11
span(133,"Federal wooden ships withdraw from exposed positions","rather than a fixed alternate date.",'<!-- CR-064 -->'+q('064',6))
rep(135,"The difficulty lies in delivering suitable armored ships to the right theatre in time.","The difficulty lies in delivering suitable armored ships to the right theatre in time. <!-- CR-063 -->"+q('063',17))
P[137]='<!-- CR-064 -->\n'+q('064',9)
rep(139,"Logan brings testing, machinery and gun-handling lessons learned with Ericsson.","Logan brings testing, machinery and gun-handling lessons learned with Ericsson. <!-- CR-063 -->"+q('063',3))
rep(139,"Pensacola, Ship Island and Key West sustain the Gulf blockade.","Pensacola, Ship Island and Key West sustain the Gulf blockade. "+q('063',6))
rep(139,"Pacifican supplies and credit travel around Cape Horn to neutral Matamoros and overland into Texas, under the working supply plan.",q('063',9))
rep(141,"leaves late in 1862 with a small staff.","leaves late in 1862 with a small staff. <!-- CR-067 -->"+q('067',4))
after(141,P[147],q('068',16)); P[147]=None
span(143,"Richmond authorizes preservation","before adding an escape.",'<!-- CR-063 -->'+q('063',12)+'\n\n'+q('063',13))
after(143,q('068',18),'<!-- CR-064 -->\n'+q('064',12))
P[155]="The consequences of the altered armored fleet continue along the Atlantic and Gulf coasts. <!-- CR-064 -->"+q('064',15)+" The 1863 Charleston assault requires different timing or composition; the historical failures do not become additional Confederate victories merely because the same attacks are not mounted. The rapid Union capture of Atlanta at Wassaw Sound cannot be assumed without an equivalent to the historical Weehawken. **[OPEN]** Whether the Charleston and Wassaw operations occur, alternative ships, outcomes and the wider blockade effects."
before(157,'<!-- CR-064 -->\n'+q('064',18))
span(157,"**[PROPOSED]** Logan's reduced mission","as a real limit.",'<!-- CR-063 -->'+q('063',19))
rep(157,"Mobile's rail connections help sustain Johnston at Atlanta.",q('064',21))
after(157,'<!-- CR-065 -->\n'+q('065',2))
rep(159,"In December 1864–January 1865 the Union assembles a seaborne force of broadside ironclads of the New Ironsides type and troops at Pensacola.",'<!-- CR-063 -->'+q('063',21))
rep(159,"Farragut is killed.","Farragut is killed. "+q('063',24))
rep(159,"re-embarks the Dauphin Island troops.","re-embarks the Dauphin Island troops. "+q('063',26))
span(161,"**[PROPOSED]** Johnston, retained","casualty totals remain **[OPEN]**.",q('064',24))
# ---------- §12 (reordered)
order12=[]
def take(i): 
    s=P[i]; P[i]=None; return s
p187=take(187); p187=p187.replace(" **[OPEN]** Exact dissolution"," "+q('068',20)+" <!-- CR-065 -->"+q('065',11)+" **[OPEN]** Exact dissolution")
p191='<!-- CR-065 -->\n'+'\n\n'.join([q('065',5),q('065',6),q('065',7),q('065',8)])+'\n\n<!-- CR-062 -->\n'+q('062',2)
p193=take(193).replace("New Mexico runs east to 103°W.","New Mexico runs east to 103°W.")
p205=take(205); x=p205.index("Lot supports the bargain"); y=p205.index("Constitutional critics warn"); p205=p205[:x]+p205[y:]
seq=[(189,None),('t',p191),(197,None),(199,None),('t',q('068',22)),(201,None),(203,None),('t',q('068',23)),('t',p205),(207,None),(209,None),
     ('t',p193),('t','<!-- CR-060 -->\n'+c060line),('t','<!-- CR-062 -->\n'+q('062',5)),('t','<!-- CR-059 -->\n'+q('059',15)),('t','<!-- CR-060 -->\n'+q('060',18)),
     (195,None),('t','<!-- CR-062 -->\n'+q('062',8)),('t',q('062',9)),('t',q('062',10)),('t','<!-- CR-061 -->\n'+q('061',20)),('t',q('068',25)),(211,None),(213,None)]
out12=[p187]
for k,v in seq:
    out12.append(take(k) if v is None else v)
P[187]='\n\n'.join(out12); P[191]=None
# ---------- §13
rep(226,"go south through Paso del Norte from New Mexico.","go south through Paso del Norte from New Mexico. <!-- CR-061 -->"+q('061',23))
span(242,"**[PROPOSED]** Travel-paper controls","that use of delegated constitutional power.",q('068',27))
P[238]=P[238]+' '+q('068',32)
P[236]=P[236]+' '+q('068',30)
txt='\n'.join(P[i] for i in range(len(L)) if P[i] is not None)
txt=re.sub(r'\n{3,}','\n\n',txt)
head="""# Merged storyline text, §§8–13 (candidate)

**Status:** CANDIDATE for the author's reading, composed on 13 November 2026 from current canon (`master_storyline.md` §§8–13) and the storyline texts of the nine drafts CR-059 to CR-065, CR-067 and CR-068, with CR-066 Part E. It is not canon and nothing is integrated: `master_storyline.md` is unchanged. Labels are each draft's own; a sentence labelled APPROVED for one CR may rest on rows that are PROPOSED in another. Built by `outputs/sessions/20261113-set-review/merge/assemble.py`, then edited by hand where two drafts told the same event (listed at the end).

"""
open('/home/claude/work/merge/merged.md','w',encoding='utf8').write(head+txt+'\n')
print(len(txt))

# ================= hand edits where two drafts tell the same event =================
t=open('/home/claude/work/merge/merged.md',encoding='utf8').read()
edits=[]
def E(old,new,why):
    global t
    assert t.count(old)==1,(old[:70],t.count(old)); t=t.replace(old,new); edits.append(why)
# §10
E(" are ordered out as well (CR-059 I2), and"," are ordered out as well, and","§10: a draft reference removed from the prose (CR-060).")
E("The Owyhee country is where the doctrine fails before it holds. The mounted police are a dozen men","The Owyhee country is where the friendship doctrine fails before it holds. The Republic's mounted police on the Snake road, posted from the camp at Boise, are a dozen men","§10: the Owyhee paragraph names the doctrine and the police it relies on (CR-060 against CR-059).")
E("Washoe is retaken in 1863–1864. Pacifica retakes it in the spring of 1864,","Pacifica retakes Washoe in the spring of 1864,","§10: canon's \"Washoe is retaken in 1863–1864\" and CR-060's dated sentence are one sentence.")
# §12 dissolution
a="Elias uses the dissolution provision before the threatened revocation is enacted, calling an election within the prescribed interval. He campaigns on security, paid contracts, unfinished works and the costs of interruption. The administration's economic constituency helps him secure a more favorable Assembly. "
E(a,"","")
E("The news of Lincoln's defeat arrives afterwards. Elias then dissolves the Assembly. A force staged on the Sound to take Port Townsend is stood down in March 1865, when McClellan's inaugural shows that he will treat. <!-- CR-065 -->**[PROPOSED — CR-065]** Once the news of the Union's vote has reached the Pacific, Elias dissolves the Assembly. He asks Pacifica's voters,",
  "The news of Lincoln's defeat arrives afterwards. Elias uses the dissolution provision before the threatened revocation is enacted, calling an election within the prescribed interval. <!-- CR-065 -->**[PROPOSED — CR-065]** He asks Pacifica's voters,","§12: the dissolution is told once, after the blind vote, with canon's sentences kept (CR-065 against CR-068).")
E("Pacifica's war has been paid for in gold, and its voters give him the Assembly he asked for.","Pacifica's war has been paid for in gold. He campaigns on security, paid contracts, unfinished works and the costs of interruption. The administration's economic constituency helps him secure a more favorable Assembly. **[APPROVED — CR-068]** A force staged on the Sound to take Port Townsend is stood down in March 1865, when McClellan's inaugural shows that he will treat.","")
E("seven of Hawaii's, on Victoria's condition that","seven of Hawaii's, on Hawaii's condition that","§12: the condition of November 1864 is Hawaii's government's (CR-068 revision 32).")
E("Thomas, in contact with Johnston on the Chattahoochee, cannot spare them.","Thomas, in contact with Johnston before Atlanta, cannot spare them.","§12: the front on election day as CR-064 has it.")
E("which McClellan will grant in a month,","which McClellan will grant within two months,","")
E("In the same weeks his last winter operations fail, at Petersburg and at Mobile. Lincoln opens no talks with Monterey; the West is not his to sell.","His last operations fail: east of Atlanta in November, where McPherson is killed, and in February at Petersburg and at Mobile. His annual message of December 1864 says that the Executive has no power to cede the West and will not treat for it, and he opens no talks with Monterey.","§12: Lincoln's last winter is one passage: the failed attack of 22 November (CR-064) and the annual message (CR-068) join CR-065's sentence.")
E("**[APPROVED — CR-068]** Lincoln's annual message of December 1864 says that the Executive has no power to cede the West and will not treat for it, and he opens no talks with Monterey before he leaves office. He goes home to Springfield","**[APPROVED — CR-068]** Lincoln goes home to Springfield","")
# Enabling Law order
m1=t.index("In 1865 Elias secures the Enabling Law through constitutional amendment"); m1e=t.index("\n\n",m1)+2
para=t[m1:m1e]; t=t[:m1]+t[m1e:]
m2=t.index("Constitutional critics warn that institutional survival"); t=t[:m2]+para+t[m2:]
edits.append("§12: order is the armistices, the lapse and the six months, the bargain of the summer, then canon's sentence that the law is secured.")
# Lincoln's letters told once
E("and took another for life; and who dismisses him now?","and took another for life; who dismisses him now, and in which country would they rather be able to lose an election?","§12: Lincoln's Oregon letter of June 1866 is told once, in the Oregon paragraph (CR-059 and CR-068).")
E(" In June 1866 he writes to Oregon's Union men in the *Oregonian* and asks in which country they would rather be able to lose an election. Elias answers over his own name that the office was voted in public and that Oregon's hold on him is its charter. In the spring of 1867, while the Senate debates the paid cession, he answers it in a public letter that advises taking the purchase money and refusing the loan; the Senate ratifies."," His letters to Oregon in 1866 and to the Senate in 1867 are told above.","§12: Lincoln's letter of 1867 is told once, in the ratification paragraph (CR-062 and CR-068).")
E("**[PROPOSED — CR-062]** Oregon votes in October 1866, and in the winter both governments","**[PROPOSED — CR-062]** In the winter after Oregon's vote both governments","")
E("Port Townsend's garrison sails, Fort Union's marches north over Raton Pass, and the surveyors take the field.","Port Townsend's garrison sails, and the surveyors take the field.","§12: Fort Union's evacuation is told once, in CR-061's paragraph.")
edits=[e for e in edits if e]
t+="\n---\n\n## Notes on the merge\n\n**Where two drafts told the same event, the candidate tells it once:**\n\n"+'\n'.join('- '+e for e in edits)+"""

**Placed by the merge map (`review-5-merged-storyline.md`):** §10's paragraph on the California column is three runs (the Rio Grande with CR-066's Taos paragraph; the Columbia, Idaho and the Port Townsend convention; Montana and Washoe). Canon's CR-022 paragraph on the Texas journey stands before CR-068's paragraph that uses it. §12 runs: the home front of 1864; the Union's election; the armistices and the lines; the lapse and the Enabling Law; the treaty of December 1865; Oregon and the interior in 1866; Alaska and the Senate in 1867; Lincoln afterwards.

**Not in this candidate, because they fall outside §§8–13:** CR-068's sentence for §4 (Lincoln's vote of 1848); CR-062's sentence for §14 (Sitka, October 1867); CR-060's sentences for §19 and §25.

**Not done:** no sentence was rewritten for style; forward references inside a draft's own paragraph stand as the draft has them; labels are each draft's own and have not been reconciled with the register; ledger quotes have not been re-checked against this text; no fresh reviewer has read it.
"""
open('/home/claude/work/merge/merged.md','w',encoding='utf8').write(t)
print(len(t),len(edits))
