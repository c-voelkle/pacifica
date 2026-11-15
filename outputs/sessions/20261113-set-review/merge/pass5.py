import re
p='/home/claude/pacifica/outputs/sessions/20261113-set-review/merged-storyline-8-13.md'
t=open(p,encoding='utf8').read(); n=0
def R(o,nw,cnt=1):
    global t,n
    assert t.count(o)==cnt,(o[:70],t.count(o)); t=t.replace(o,nw); n+=1
def para(start):
    i=t.index(start); i=t.rfind('\n\n',0,i)+2; j=t.index('\n\n',i); return i,j
def take(start):
    global t
    i,j=para(start); s=t[i:j]; t=t[:i]+t[j+2:]; return s
def put_before(start,s):
    global t
    i,_=para(start); t=t[:i]+s+'\n\n'+t[i:]
# ---- §9 1861
R("to bind itself by treaty to amnesty and the writ of habeas corpus for the inhabitants of the Columbia,","to bind itself by treaty to prosecute no inhabitant of the Columbia for trading or corresponding with the Republic and to keep the writ of habeas corpus open to them,")
R("and his message of 4 July answers them:","and his message of 4 July, which reaches Monterey in August, answers them:")
# ---- §10
R("that October the posts east of the Cascades, cut off from the sea, are ordered out as well, and Fort Churchill's regulars","and Fort Churchill's regulars")
R("leaves the city to the Legion.","leaves the city to the Nauvoo Legion, Deseret's militia.")
# Rio Grande order: the January 1863 paragraph before San Antonio
s=take("**[APPROVED — CR-061]** In January 1863, with Caleb on the road to Texas")
put_before("**[PROPOSED]** Richmond renounces its Arizona claim",s)
R("**[APPROVED — CR-015]** In Navajo country the government chooses a different course. **[APPROVED — CR-061]** In December 1862","**[APPROVED — CR-015]** In Navajo country the government chooses a different course. **[APPROVED — CR-061]** It makes no campaign. In December 1862")
# Washoe sentence order
R("Washoe is retaken in 1863–1864. **[PROPOSED — CR-060]** Pacifica retakes it in the spring of 1864, without a fight: Elias moves in the first weeks the Sierra roads allow.","Pacifica retakes it in the spring of 1864, without a fight: Elias moves in the first weeks the Sierra roads allow.")
R("<!-- CR-060 -->**[PROPOSED — CR-060]** Through 1863 Nye's volunteers","Washoe is retaken in 1863–1864. <!-- CR-060 -->**[PROPOSED — CR-060]** Through 1863 Nye's volunteers")
# ---- §11
R("the armistice offer, the Proclamation, the answer at Honolulu, the officer kept and the terms of passage","the armistice offer of 1862 and the widened credit")
R("**[APPROVED — CR-068]** On 1 January 1863 Lincoln proclaims","<!-- CR-068: the Proclamation, the account of the nations, the answer at Honolulu and the terms of passage --> **[APPROVED — CR-068]** On 1 January 1863 Lincoln proclaims")
R("Pacifica's government replies with a published account,","In the spring Pacifica's government replies with a published account,")
R("days after Hawaii's legislature, which has read the San Antonio terms, has put","days after Hawaii's legislature, with the Proclamation, the account and the San Antonio articles all before it, has put")
R("the renewal passes in the last week of the term. That spring the Republic also prints terms of passage for men leaving the Union's draft, and Lincoln answers in a public letter.","the renewal passes in the last week of the term, and the second turret ship comes out to Honolulu that year, as promised in 1861. That spring the Republic also prints terms of passage for men leaving the Union's draft, under Lincoln's own sentence from Peoria that no man is good enough to govern another without that other's consent, and Lincoln answers in a public letter.")
R("**[APPROVED — CR-068]** At San Antonio in February he has the terms","<!-- CR-068: the terms of the credit -->**[APPROVED — CR-068]** At San Antonio in February he has the terms")
R("A preface addressed to the people of the United States answers Lincoln's Lyceum address of 1838 and cites","A preface addressed to the people of the United States says that the Protector can be dismissed every twelvemonth by either legislature, answers Lincoln's Lyceum address of 1838 and cites")
# ---- §12
R("After Lincoln's refusal in February he makes no statement,","After Lincoln's public refusal of *Two Houses* that February he makes no further statement,")
R("as it printed in 1863.","as it published in 1862.")
R("In 1865 Elias secures the Enabling Law through constitutional amendment: two-thirds of both confederal chambers and ratification by both founding states.","The Enabling Law is a constitutional amendment, secured by two-thirds of both confederal chambers and ratification by both founding states.")
# orphan comment
R("<!-- CR-062 -->\n\n<!-- CR-059 -->","<!-- CR-059 -->")
R("**[PROPOSED — CR-062]** The Western treaty is signed at Washington","<!-- CR-062 -->\n**[PROPOSED — CR-062]** The Western treaty is signed at Washington")
# moved paragraphs: before "The interior consents", Navajo join repaired
bh=take("**[PROPOSED — CR-060]** In April 1865, after a starving winter")
ow=take("**[PROPOSED — CR-060]** In the Owyhee country")
nv=take("**[APPROVED — CR-015]** Barboncito and Manuelito negotiate that settlement.")
pe=take("**[APPROVED — CR-061]** The captive article brings")
nv=nv.replace("**[APPROVED — CR-015]** Barboncito and Manuelito negotiate that settlement.","**[APPROVED — CR-015]** In 1865 a treaty recognizes the Navajo homeland. Barboncito and Manuelito negotiate that settlement.",1)
nv=nv.replace("East of the line the Union tries in 1863","East of the armistice line at Glorieta the Union had tried in 1863",1).replace("who marched out of Fort Craig in April with","who marched out of Fort Craig in April 1863 with",1)
ow=ow.replace("In the Owyhee country the Republic's mounted police on the Snake road, posted from the camp at Boise, are a dozen men","In the Owyhee country the Republic keeps mounted police on the Snake road, posted from the camp at Boise since 1863 to bring the emigrant trains through. They are a dozen men",1).replace("the Snake raids are real","the Shoshone and Paiute raids on the road are real",1)
i,_=para("**[PROPOSED — CR-060]** The interior consents in its own ways.")
# keep the CR-060 comment line that precedes "The interior consents"
k=t.rfind("<!-- CR-060 -->\n",0,i+1)
blk="<!-- CR-061 -->\n"+nv+"\n\n"+pe+"\n\n<!-- CR-060 -->\n"+bh+"\n\n"+ow+"\n\n"
t=t[:k]+blk+t[k:]
R("**[PROPOSED — CR-060]** The interior consents in its own ways.","**[PROPOSED — CR-060]** By these agreements and by votes the interior consents in its own ways.")
# ---- §13 writ
R("a fugitive held for return under the new treaties' rendition clause petitions a court at","a fugitive who has reached San Francisco is detained under the controls the association treaties have just extended to the ports, and Richmond's consul claims him. He petitions a court at")
R("to rest the case on Pacifica's own prohibition of slavery, on the San Antonio article of 1863, under which no one who reached its soil was ever given up, and on the terms","to rest the case on Pacifica's own prohibition of slavery, with the San Antonio article of 1863 as evidence that no one who reached its soil was ever given up, and on the terms")
R("By a convention of that year a ransom article replaces the rendition clause: a person","By a convention of that year the agreement gains a ransom article in place of the rendition Richmond had asked for and been refused: a person")
R("Over the winter of 1871–1872 the cabinet sets travel-paper controls that refuse entry at Texas, the railway and Gulf ports,","Over the winter of 1871–1872 the cabinet tightens the travel-paper controls of the Texas line, which the treaties have extended to the railway and the Gulf ports,")
# mid-sentence comment in §8
R("; <!-- CR-068: no bondholders in 1860 -->Britain refuses to support a war of Californian expansion","; **[APPROVED — CR-068]** Britain refuses to support a war of Californian expansion <!-- CR-068: no bondholders in 1860 -->")
t=re.sub(r'\n{3,}','\n\n',t)
open(p,'w',encoding='utf8').write(t); print(n)
