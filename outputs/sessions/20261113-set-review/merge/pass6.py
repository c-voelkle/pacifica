import re,sys
sys.path.insert(0,'/home/claude/work')
from lib import *
p='/home/claude/pacifica/outputs/sessions/20261113-set-review/merged-storyline-8-13.md'
t=open(p,encoding='utf8').read(); n=0
def R(o,nw,cnt=1):
    global t,n
    assert t.count(o)==cnt,(o[:70],t.count(o)); t=t.replace(o,nw); n+=1
def para(start):
    i=t.index(start); i=t.rfind('\n\n',0,i)+2; j=t.index('\n\n',i); return i,j
def take(start,with_comment=False):
    global t
    i,j=para(start)
    if with_comment:
        k=t.rfind('\n\n',0,i-2)+2
        if t[k:i-2].startswith('<!--') and '\n' not in t[k:i-2]: i=k
    s=t[i:j]; t=t[:i]+t[j+2:]; return s
def put_before(start,s):
    global t
    i,_=para(start)
    k=t.rfind('\n\n',0,i-2)+2
    if t[k:i-2].startswith('<!--') and '\n' not in t[k:i-2]: i=k
    t=t[:i]+s+'\n\n'+t[i:]
def put_after(start,s):
    global t
    _,j=para(start); t=t[:j]+'\n\n'+s+t[j:]
# ---- §9
R("**[APPROVED — CR-068]** The offer of release and investigation is Lincoln's own, made in public through Baker in June, before any soldier has crossed into Oregon.","**[APPROVED — CR-068]** In June Lincoln, in public and through Baker, offers release, an inquiry and compensation for the dead sailor's family if the expedition gathering at San Francisco stands down. The offer is his own.")
s=" Pacifica's papers have already printed his first inaugural's sentence on the perpetual Union beside his speech of 1848 on the right of revolution, without comment, and his message of 4 July, which reaches Monterey in August, answers them: the right belongs to a people who can use it themselves and can name their wrong."
R(s,""); R(" Baker goes east and is killed at Ball's Bluff in October.",s+" Baker goes east and is killed at Ball's Bluff in October.")
# ---- §10
R(", and sends its Iowa regiments to Casey on the Sound.",".")
R("The second undertaking sustains the gains through finance and transport.","Finance and transport sustain the gains.")
R("Elias sends a garrison first and terms afterwards.","Elias sends a garrison first and terms afterwards. Sherman and Victoria say that a garrison on a new road needed the Council's vote; Elias calls it an invited guard and asks for none.")
R("In January 1863 the road's commander marches","In January 1863 Hays, the road's commander, marches")
R("signs when the Sunset articles are read in the plaza","signs when the San Antonio articles are read in the plaza")
R("is signed at Cubero with de la Guerra; and in 1865 a treaty recognizes a homeland and avoids the Long Walk.","is signed at Cubero with de la Guerra.")
R("In March regulars with Ute guides march up the San Luis Valley","In March the column's regulars with Ute guides march up the San Luis Valley")
R("Through 1863 Nye's volunteers at Fort Churchill","Through 1863 the territorial volunteers of James Nye, Lincoln's governor of Nevada Territory, at Fort Churchill")
pt=take("<!-- CR-068: the Port Townsend convention -->")
put_after("**[PROPOSED — CR-059]** Lewiston stands on a townsite",pt)
# ---- §11
R("lent on the terms printed in Texas,","lent on terms it prints the next year,")
R(" Without a Union New Orleans base there is no Red River campaign in 1864.","")
R("Steele's corps bridging the river","Frederick Steele's XV Corps bridging the river")
# ---- §12
R("By August the North has had sixty thousand casualties","By August 1864 the North has had sixty thousand casualties")
R("**[OPEN]** His cabinet. After taking office in March 1865,","**[OPEN]** His cabinet. **[PROPOSED]** After taking office in March 1865,")
R("striking the protocol's terms for a Union Oregon","striking the terms the protocol of 1865 set for a Union Oregon")
R("which he insisted on, nearly cost him the south","which Elias insisted on, nearly cost him the south")
R("The Union is to evacuate Port Townsend and Fort Union after the exchange.","The Union is to evacuate Port Townsend and Fort Union after the exchange, and Pacifica is to pay a vendor credit of $40 million in gold in six instalments from the exchange.")
# blind-vote paragraph split: the 1864 home front part goes back before the election
i,j=para("In the 1864–1865 consolidation struggle"); pv=t[i:j]
cutp=pv.index(" After the Union has voted on 8 November")
home=pv[:cutp]; vote="**[APPROVED — CR-068]**"+pv[cutp:]
t=t[:i]+vote+t[j:]
put_before("**[PROPOSED — CR-065]** By August 1864 the North",home); n+=1
# Victoria 1865–66 paragraphs to before Oregon
v1=take("**[APPROVED — CR-027]** Victoria keeps a kahuna",with_comment=False)
v2=take("**[APPROVED — CR-035]** That summer she sails to San Francisco",with_comment=True)
# Oregon after the nations, before the interior
og=take("**[PROPOSED — CR-059]** The peace transfers Idaho outright.",with_comment=True)
put_before("**[PROPOSED — CR-060]** By these agreements and by votes",v1+"\n\n"+v2.replace("That summer she sails","In the summer of 1866 she sails",1)+"\n\n"+og); n+=1
# enclave/credit paragraph after the Senate
en=take("**[PROPOSED]** The surviving Puget Sound enclave is evacuated")
put_before("**[PROPOSED — CR-061]** Until the exchange the armistice line at Glorieta",en); n+=1
# ---- §13
R("The same convention ends the scalp bounties","The convention that sets up the post also ends the scalp bounties")
t=re.sub(r'\n{3,}','\n\n',t)
open(p,'w',encoding='utf8').write(t); print(n)
