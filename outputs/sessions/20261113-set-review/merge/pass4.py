p='/home/claude/pacifica/outputs/sessions/20261113-set-review/merged-storyline-8-13.md'
t=open(p,encoding='utf8').read(); n=0
def R(o,nw):
    global t,n
    assert t.count(o)==1,(o[:60],t.count(o)); t=t.replace(o,nw); n+=1
R("Candidate changed assignments are the 11th and 13th Iowa, followed as organization permits by the 15th and 16th, transported through Panama to the Sound.","The 11th and 13th Iowa, followed by the 15th and 16th, are sent through Panama to the Sound.")
R("Four Iowa regiments raised that autumn are on the Panama road to the Sound.","The four Iowa regiments sent to the Sound are missing from the field.")
R("On the news Fort Garland falls to the Rio Grande garrison in 1863 without an assault: in May its Colorado garrison","On the news Fort Garland falls to the Rio Grande garrison without an assault: in May 1863 its Colorado garrison")
R("is signed at Cubero with Elias's commissioner, Pablo de la Guerra;","is signed at Cubero with de la Guerra;")
R("The Union keeps a squadron and a garrison at Pensacola, and no Union army comes","No Union army comes")
R("Grant drives Johnston out of Jackson and halts","Grant sends McPherson, who drives Johnston's relief army, stronger by the men who escaped the city, out of Jackson in July and halts")
R(" McPherson drives Johnston's relief army, stronger by the men who escaped the city, out of Jackson in July.","")
R("After it, the Fort Union garrison marches out under arms by Raton Pass with a Pacifican escort to the Colorado line, and Fort Union is evacuated in 1867 with its stores sold at valuation.","After it, in 1867, the Fort Union garrison marches out under arms by Raton Pass with a Pacifican escort to the Colorado line, and its stores are sold at valuation.")
R(" The treaty the Senate ratifies in 1867 records Oregon's choice and cedes it with the rest of the Northwest.","")
R("is soon in Washington, and from July 1862 he is its general in chief.","is soon in Washington.")
R("Victoria uses it to win her conditions for the third renewal, among them Hawaii's control of entry at its own ports.","Victoria uses it to win her conditions for the third renewal.")
# Oregon paragraph: terms introduced
R("Elias could soften the Native article's rule on testimony while the charter is open, and does not.","The charter's Native article sends killings and land disputes to confederal courts and admits Native testimony, against Oregon's own law. Elias could soften it while the charter is open, and does not.")
R("The Chinese floor and the Native article he insisted on nearly cost him the south.","The Native article and the charter's floor for Chinese residents, one licence and one court for all, which he insisted on, nearly cost him the south.")
R("The returns commission voids","The returns commission, one member from each government and a president chosen by both, voids")
i=t.index("Nesmith"); 
t=t[:i]+"James Nesmith, the Douglas Democrats' leader in Oregon,"+t[i+len("Nesmith"):]; n+=1
# labels on Lincoln's letters
R("That month Lincoln, a private citizen at Springfield,","**[APPROVED — CR-068]** That month Lincoln, a private citizen at Springfield,")
R("and says that what Oregon can hold him to is its charter.","and says that what Oregon can hold him to is its charter. **[PROPOSED — CR-059]**")
R("While the Senate debates, Lincoln writes from Springfield","**[APPROVED — CR-068]** While the Senate debates, Lincoln writes from Springfield")
R("The Senate consents on 9 April and,","**[PROPOSED — CR-062]** The Senate consents on 9 April and,")
open(p,'w',encoding='utf8').write(t); print(n)
