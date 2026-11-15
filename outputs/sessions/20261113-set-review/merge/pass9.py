import re
p='/home/claude/pacifica/outputs/sessions/20261113-set-review/merged-storyline-8-13.md'
t=open(p,encoding='utf8').read(); done=[];miss=[]
def R(o,nw,what):
    global t
    if t.count(o)==1: t=t.replace(o,nw); done.append(what)
    else: miss.append((what,t.count(o)))
R("At San Antonio in February he has the terms of the Richmond credit printed:","At San Antonio in February, where the Sunset articles are signed, he also has the terms of the Richmond credit printed:","San Antonio: the two tellings are tied as one visit")
R(" The convention that sets up the post also ends the scalp bounties in Sonora and Chihuahua.","","the end of the scalp bounties (kept in §12)")
R("In the East the armies fight from the Peninsula to the Wilderness, and the Overland campaign of 1864 costs the Union more than sixty thousand men in six weeks.","In the East the armies fight from the Peninsula to the Wilderness and on to Petersburg.","the Overland losses (kept in §12)")
R("Lincoln's last operations fail: east of Atlanta in November, where McPherson is killed, and in February at Petersburg and at Mobile.","Lincoln's last operations fail, before Atlanta, at Petersburg and at Mobile.","McPherson's death and the February failures (told in §11)")
R("The Republic's armistice is signed in May 1865, and on the last day of that month the Protectorship expires with its term.","On the last day of May 1865 the Protectorship expires with its term.","Pacifica's armistice (told once, in the armistice paragraph)")
R("It is signed in mid-May 1865, some weeks after Richmond's, by Elias as Protector; in the last week of May he signs the Treaty of Amity and Commerce with Richmond, his last act in that office.","It is signed in mid-May 1865, some weeks after Richmond's, by Elias as Protector.","the Treaty of Amity (told once)")
R("A Pacifica–Confederate Treaty of Amity and Commerce in spring 1865 supplies Pacifica's formal recognition.","A Pacifica–Confederate Treaty of Amity and Commerce in spring 1865 supplies Pacifica's formal recognition. <!-- CR-062 -->**[PROPOSED — CR-062]** Elias signs it in the last week of May, his last act as Protector.","")
R("a protocol signed with the treaty in December 1865 by Vallejo and Sherman, under the armistice and under the full powers of the office the Enabling Law has just created:","a protocol signed with the treaty by Vallejo and Sherman:","the powers under which the treaty is signed")
R(" Colorado's Western Slope, North, Middle and South Park, the upper Arkansas and the San Luis Valley are Pacifican; Denver, Boulder, Clear Creek, Gilpin and Pikes Peak stay Union.","","the Colorado line (kept in CR-060's paragraph)")
R("**[PROPOSED]** The surviving Puget Sound enclave is evacuated under the treaty, leaving the Union without a Pacific port. Pacifica pays","**[PROPOSED]** The evacuation of the Sound leaves the Union without a Pacific port. Pacifica pays","the evacuation of the Sound")
R(", so that Elias becomes creditor to the Union's bankers and not to its government.",".","Elias as creditor to the Union's bankers")
R("They choose Whiteaker, whom Oregon elected governor in 1858 for a state never admitted, to chair it. John Whiteaker negotiates civil protections","They choose John Whiteaker, whom Oregon elected governor in 1858 for a state never admitted, to chair it. He negotiates civil protections","Whiteaker's introduction")
R("A brigade stays to hold Pensacola, Fort Pickens and Ship Island.","A brigade stays to hold Fort Pickens and Ship Island.","Pensacola's garrison")
t=re.sub(r'\n{3,}','\n\n',t); open(p,'w',encoding='utf8').write(t)
print(len(done),'done; missing:',miss)
open('/home/claude/work/merge/log9.txt','w',encoding='utf8').write('\n'.join('- '+d for d in done if d))
