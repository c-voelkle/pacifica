import re
src=open('/home/claude/work/merge/merged.md',encoding='utf8').read()
body=src[src.index('## 8. '):src.index('\n---\n\n## Notes on the merge')]
notes=src[src.index('## Notes on the merge'):]
L=body.split('\n'); off=5   # body line 0 == file line 5
P={i+off:l for i,l in enumerate(L)}
log=[]
def R(i,old,new,why=None,cnt=1):
    assert P[i].count(old)==cnt,(i,old[:60],P[i].count(old)); P[i]=P[i].replace(old,new)
    if why: log.append(why)
def pop(i):
    s=P[i]; P[i]=None; return s
def com(i):  # take a paragraph together with a comment line two above, if any
    c=''
    if P.get(i-2,'') and P[i-2].startswith('<!--') and len(P[i-2])<130: c=pop(i-2)+'\n'
    return c+pop(i)
# ---------------- §8
R(72,"The Senate passes the bill in May.","The Senate had passed the bill in May 1858.","§8: the Senate's vote on Oregon is dated.")
for i in (72,74,76): P[i]="**[PROPOSED — CR-059]** "+P[i]
log.append("Labels: new paragraphs that began without a label carry one (CR-059 in §8, CR-063 and CR-062 later).")
# ---------------- §9
R(126," Washington eventually offers a route to release and investigation in exchange for withdrawal. Elias demands broader strategic guarantees and protection for collaborators; a limited crisis becomes a territorial war through choices rather than inevitability."," A limited crisis becomes a territorial war through choices rather than inevitability.","§9: canon's summary of the offer and the reply is cut; CR-068's paragraph tells both.")
R(130,"in the proposed office of Inspector-General","as Inspector-General","§9: Sherman's office is no longer \"proposed\".")
# ---------------- §10
R(132,"## 10. The Northwestern campaign and occupation (1861–1862)","## 10. The Northwestern campaign, the interior and the Rio Grande (1861–1864)","§10 is kept to 1861–1864 and ordered by theatre (the Columbia; the Basin and Deseret; the Rio Grande; Montana and Washoe), as the author approved; Black Hawk, the Owyhee, the Navajo treaty and the end of peonage (1865–66) stand in §12 after the interior's consent.")
R(138,"**[OPEN]** Local officeholders, succession, compacts, boundaries and accession dates.","**[OPEN]** Local officeholders, succession and boundaries.")
R(147,"Mullan resigns his commission in the spring and","Mullan resigns his commission in the spring of 1863 and")
R(147," Lewiston stands on a townsite","\n\n**[PROPOSED — CR-059]** Lewiston stands on a townsite")
R(154," The regiments that might have come back to Utah were to be raised in California.","","Memo language removed (the regiments \"that might have come back\", the \"friendship doctrine\", the pointer to letters \"told above\").")
R(154,", while Elias is at Santa Fe, his commissioners",", while Elias is in New Mexico, his commissioners")
R(154," In December 1862, while Elias","\n\n**[PROPOSED — CR-060]** In December 1862, while Elias")
R(154,"and promise nothing against the Union's law. Young will not sign","and promise nothing against the Union's law. Lincoln's governor leaves by Fort Bridger in the spring of 1863, and Utah's legislature goes on sitting without him.\n\n**[PROPOSED — CR-060]** Young will not sign")
R(154," Lincoln's governor had left by Fort Bridger in the spring of 1863, under the articles, and Utah's legislature goes on sitting without him.","")
R(154,"none within a day's ride of the city, and Young signs.","none within a day's ride of the city.","§10: the Deseret paragraph is three (1861–62; the articles; the Compact), and the signing is told once.")
R(168,"**[PROPOSED — CR-066]** In December 1862, on his way to Texas, Elias rides up from Santa Fe to Taos,","**[PROPOSED — CR-061]** In November 1862 Elias leaves Monterey by the southern stage road, through Yuma, Tucson and Mesilla, and comes up the Rio Grande to Santa Fe in December, on his way to Texas. **[APPROVED — CR-066]** From Santa Fe he rides up to Taos,","§10: Elias's arrival in New Mexico is stated before Taos; the Taos paragraph is labelled APPROVED, as the project rules record it.")
R(172,"At San Antonio in February 1863 the Confederacy gets the use of the road but no right to march on it.","At San Antonio in February 1863, where Elias has come from Santa Fe, the Sunset articles give the Confederacy the use of the southern road, the Sunset road, but no right to march on it.","§10: the Sunset articles and the Sunset road are named where they are made.")
R(181,"The Owyhee country is where the friendship doctrine fails before it holds. The Republic's mounted police on the Snake road, posted from the camp at Boise, are","In the Owyhee country the Republic's mounted police on the Snake road, posted from the camp at Boise, are")
# Washoe paragraph rebuilt in order
p=P[176]; a=p.index("Pacifica retakes Washoe in the spring of 1864"); mont=p[:a].rstrip()
def cut(s,start,end):
    x=s.index(start); y=s.index(end,x)+len(end); return s[x:y]
nye=cut(p,"Through 1863 Nye's volunteers","Elias leaves them there.")
votes=cut(p,"In January 1864 Washoe's voters","lock the Basin into the Union.")
rest=cut(p,"Washington closes the overland wire","there is no State of Nevada.").replace("Carson's guarantees kept","the Carson Convention's guarantees kept")
washoe=("<!-- CR-060 -->**[PROPOSED — CR-060]** "+nye+" The Terms of Monterey, printed in August 1863 and adopted by the Council in September, say that Pacifica asks no state of the Union and holds itself free to occupy any territory Congress acts to make one. "+votes+
 " Washoe is retaken in 1863–1864. **[PROPOSED — CR-060]** Pacifica retakes it in the spring of 1864, without a fight: Elias moves in the first weeks the Sierra roads allow. "+rest+" **[OPEN]** Exact forces and routes; civilian and Native authority require their own agreements.")
P[176]=mont
log.append("§10: Washoe is told once and in order (1863, the votes of January and March 1864, the retaking, the conditions), and canon's sentence \"Washoe is retaken in 1863–1864.\", which the ledger quotes, is restored.")
order10=[132,134,136,138,140,142,144]
seq=[P[i] for i in order10]
seq+= [com(147), pop(151), com(154), com(179)]
seq+= [com(157)]+[pop(i) for i in (159,161,163,165)]+[com(168)]+[pop(i) for i in (170,172,174)]+[com(186)]
seq+= [pop(176), washoe, pop(149)]
later=[com(183), pop(181), pop(188), pop(190)]
for i in order10+[146,153,156,167,178,185]: P[i]=None
P[132]='\n\n'.join(seq)
# ---------------- §11
R(203,"He meets Logan in a New Orleans repair yard","Marcus meets Logan in a New Orleans repair yard")
p=P[207]; k=p.index(" In January 1863 Lincoln answers")
pA=p[:k]; pB="**[APPROVED — CR-068]** "+p[k+1:]
P[207]=pB; P[199]=P[199]+"\n\n"+pA
log.append("§11: the armistice offer of spring 1862 and the widened credit stand in 1862, before New Orleans; the exchanges of 1863 follow the Texas journey.")
P[194]=P[194]+"\n\n"+pop(226)
log.append("§11: Drewry's Bluff (May 1862) follows Hampton Roads.")
east=cut(P[238],"**[PROPOSED — CR-064]** In the East the armies fight","western campaign of 1864.")
P[238]=P[238].replace(" "+east,"")
P[229]="**[PROPOSED — CR-064]** In the East the armies fight from the Peninsula to the Wilderness, and the Overland campaign of 1864 costs the Union more than sixty thousand men in six weeks. **[OPEN]** Casualty totals of the western campaign of 1864.\n\n"+P[229]
log.append("§11: the summary of the Eastern war stands before the Atlanta campaign, and Early's raid is told once.")
R(236,"while Johnston holds the Chattahoochee","while Johnston holds Atlanta")
P[211]="**[PROPOSED — CR-063]** "+P[211]
# ---------------- §12
R(264,"on terms it printed two years ago","on the terms it printed in 1863")
R(266,"The war's political decision comes when Lincoln loses the election of 1864. ","")
R(273,"and the conference fails over separation. His last operations fail:","and the conference fails over separation. Lincoln's last operations fail:")
R(275,"Sherman's brother John in the Senate provides a possible negotiating channel.","Sherman's brother John sits in the Senate that must consent to any treaty.")
R(282,"Wartime alliance clauses and exact treaty drafting remain **[OPEN]** within this selected postwar structure.","The treaty carries no military clause; its exact drafting remains **[OPEN]**.","§12: the Amity treaty's sentence is amended as decided (CR-062 CT3).")
R(284,"He reads his pledge of 1864 against himself","He reads the condition he accepted in 1864 against himself")
R(288,"the list of provisions the cabinet may not legislate around","the list of protected provisions that cabinet legislation may not touch")
R(288,"the two members of the mission party vote against","the two members of Hawaii's delegation from the American mission families vote against")
R(298,"Colorado's Western Slope, North and Middle Park and the San Luis Valley are Pacifican; Denver, the Front Range, Pikes Peak and Leadville stay Union.","Colorado's Western Slope, North, Middle and South Park, the upper Arkansas and the San Luis Valley are Pacifican; Denver, Boulder, Clear Creek, Gilpin and Pikes Peak stay Union.","§12: canon's Colorado sentence follows CR-060's line (South Park and the upper Arkansas Pacifican).")
R(324," His letters to Oregon in 1866 and to the Senate in 1867 are told above.","")
P[317]="**[PROPOSED — CR-062]** "+P[317]; P[319]="**[PROPOSED — CR-062]** "+P[319]
blind=pop(264); fin=pop(266); marcus=pop(286); treaty=com(304)
P[271]=P[271]+"\n\n"+fin
P[273]=P[273]+"\n\n"+blind
log.append("§12: the blind vote and the dissolution follow the Union's election and Lincoln's last winter.")
P[296]=P[296]+"\n\n"+marcus
P[298]=treaty+"\n\n"+P[298]
log.append("§12: the treaty's signing stands before the description of its line.")
P[310]=P[310]+"\n\n"+'\n\n'.join(later)
# ---------------- §13
s="Free navigation of the Mississippi is Pacifica's condition for guaranteeing the treaty of the spring of 1871."
m=re.search(r" <!-- CR-068: the river --> \*\*\[APPROVED — CR-068\]\*\* "+re.escape(s),P[351]); assert m
P[351]=P[351].replace(m.group(0),"")
R(345,"Richmond restores free Mississippi navigation; Pacifica guarantees Confederate independence.","Richmond restores free Mississippi navigation; Pacifica guarantees Confederate independence. <!-- CR-068: the river -->**[APPROVED — CR-068]** Free navigation of the Mississippi is Pacifica's condition for that guarantee.","§13: the Mississippi condition stands with the treaty that ends Grant's war, and Lincoln's death with 1872.")
m=re.search(r" <!-- CR-068: Lincoln's death --> \*\*\[APPROVED — CR-068\]\*\* Lincoln dies at Springfield in November 1872\. Pacifica pays him no official honour\.",P[353]); assert m
P[353]=P[353].replace(m.group(0),"")
R(353,"then dies before the electors meet.","then dies before the electors meet. <!-- CR-068: Lincoln's death -->**[APPROVED — CR-068]** Lincoln dies at Springfield in November 1872. Pacifica pays him no official honour.")
out='\n'.join(P[i] for i in sorted(P) if P[i] is not None); out=re.sub(r'\n{3,}','\n\n',out)
open('/home/claude/work/merge/merged2.md','w',encoding='utf8').write(out.rstrip()+'\n')
open('/home/claude/work/merge/log2.txt','w',encoding='utf8').write('\n'.join('- '+x for x in log))
print(len(out),len(log))
