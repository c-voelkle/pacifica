"""Enter CR-059 to CR-070's persons into the character bible and registry
(adoption of 15 November 2026).

The prose bible is the authored source: new persons are added there as short
profiles (Lincoln as a dossier), additions to existing persons are appended to
their entries, and the registry's narrative_profile copies are then refreshed
from the bible, as validate_character_docs.py requires.

  python3 outputs/sessions/20261115-integration/characters_integration.py
  python3 book-agent/revision/validate_character_docs.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "book-agent" / "revision"
BIBLE = BASE / "character_bible.md"
REGISTRY = BASE / "character_registry.json"
DATE = "15 November 2026"
ST = f"APPROVED {DATE}, local labels retained"

# (id, display name, CR, tier, profile text, links)
NEW = [
    # CR-059: Oregon and the Northwest
    ("CT-JOHN-WHITEAKER", "John Whiteaker, chair of Oregon's civil compact", "CR-059", "supporting",
     "Elected governor of Oregon in June 1858 for a state never admitted (*hist.* election; here admission fails). After Portland falls in 1861 the territorial legislature and county commissioners choose him to chair the civil compact with the occupation command; he negotiates civil protections without conceding a governor's right to transfer Oregon's allegiance.", []),
    ("CT-JOSEPH-LANE", "Joseph Lane, Oregon's senator-elect", "CR-059", "supporting",
     "Chosen senator in 1858 in anticipation of admission; he advised Oregon to act as a state without waiting for Congress, and his name sinks the admission bill in 1859 (§8). In August 1866 he declines an invitation to Richmond and speaks for accession at Roseburg.", []),
    ("CT-JAMES-NESMITH", "James W. Nesmith, leader of Oregon's Douglas Democrats", "CR-059", "supporting",
     "The Douglas Democrats' leader in Oregon. He calls the entrenched charter of 1866 a charter no cabinet can touch, and answers Lane's Roseburg speech that Oregon is not voting for Lane.", []),
    ("CT-MATTHEW-DEADY", "Matthew P. Deady, the compact's court", "CR-059", "supporting",
     "A territorial justice who becomes the court of Oregon's and the Puget Sound counties' compacts. In the Willamette flood of December 1861 he orders a seized relief steamer released, and the command refuses until Victoria makes compliance Hawaii's price for renewing the Protectorship. In July and August 1866 the delegates Oregon elected in June 1861 meet at last at Salem under him.", []),
    ("CT-JOHN-MULLAN", "John Mullan, builder of the Mullan Road", "CR-059", "supporting",
     "The army engineer who built the road over the Bitterroots (*hist.*). He guides the regulars east on it under the Walla Walla convention of July 1862, resigns his commission in the spring of 1863 and comes back to his property at Walla Walla to carry Pacifica's mail on his road.", []),
    # CR-060: Deseret, the Basin and the Rockies
    ("CT-BRIGHAM-YOUNG", "Brigham Young, governor of Deseret", "CR-060", "supporting",
     "Elected governor of the unrecognized State of Deseret in March 1862. After the Morrill Act he asks for protection through the old San Bernardino channel; his counsellors sign the working articles of December 1862, and he will sign no compact the Protector has not signed. On 24 July 1863 he and Elias sign the Compact of Association. He surrenders John D. Lee at the signing (APPROVED — CR-015) and obtains protection at a price he resents. In 1864, on Deseret's own decision, he sends Lot Smith's cavalry to Bannack (APPROVED — CR-060). In December 1866 his General Assembly approves the charter of accession.", [("signs the Compact of Association with", "CT-ELIAS")]),
    ("CT-JOHN-D-LEE", "John D. Lee", "CR-060", "minor",
     "Surrendered by Brigham Young in 1863 and hanged by Pacifica for Mountain Meadows (APPROVED — CR-015); he is the one man given up, at the signing of the Compact, and the others are not found (PROPOSED — CR-060).", []),
    ("CT-LOT-SMITH", "Lot Smith, the Legion's cavalry commander", "CR-060", "supporting",
     "His Mormon cavalry guards the Salt Lake road for the Union in 1862 (*hist.*) and is bound by the Compact of 1863 to the common defence of the roads and the valley. In the summer of 1864 Young sends it north to Bannack on Deseret's own decision; it is there first, the Union's regulars turn back at the Sun River without a fight, and after the peace Pacifica pays the Legion in gold for that summer, the only pay it ever has from Pacifica (APPROVED — CR-060).", []),
    ("CT-JEFFERSON-HUNT", "Jefferson Hunt of the Mormon Battalion", "CR-060", "minor",
     "The old Mormon Battalion captain of San Bernardino (*hist.*); in October 1862 he goes up the Salt Lake road with Hays to speak for the Republic to Brigham Young.", []),
    ("CT-EDWARD-BEALE", "Edward Fitzgerald Beale, commissioner to the nations of the road", "CR-060", "supporting",
     "In October 1862 he goes up the Salt Lake road with Hays to speak for the Republic to the nations of the road (the Box Elder compact of 1863 follows). His part in the Owyhee prosecution of 1866 is OPEN.", []),
    ("CT-BEAR-HUNTER", "Bear Hunter, Northwestern Shoshone leader", "CR-060", "minor",
     "In January 1863 his men fight Hays's column for a morning from the ravine on the Bear River and draw off into the hills with their families; the column does not follow, and that summer the bands sign the Box Elder compact.", []),
    ("CT-WASHAKIE", "Washakie, Eastern Shoshone leader", "CR-060", "minor",
     "His Eastern Shoshone make their own terms for passage at Fort Bridger and keep their distance from both armies; his agreement's terms are OPEN.", []),
    ("CT-JAMES-NYE", "James W. Nye, Lincoln's governor of Nevada Territory", "CR-060", "minor",
     "His territorial volunteers at Fort Churchill eat California's flour through 1863, their only road to the Union through Deseret; when Pacifica retakes Washoe in the spring of 1864 those who will not stay march east by Deseret's road, fed at Pacifica's charge, and he goes with them.", []),
    ("CT-HENRY-PLUMMER", "Henry Plummer, sheriff of Bannack", "CR-060", "minor",
     "Once a city marshal at Nevada City in California; in January 1864 the Alder Gulch committee hangs him, and its members say that Pacifica's courts sent him to them.", []),
    # CR-061: New Mexico, Arizona and Texas
    ("CT-EDWARD-CANBY", "Edward R. S. Canby, the Union's commander in New Mexico", "CR-061", "supporting",
     "He does not give up the river: through the summer of 1862 he stocks Fort Craig and pickets the Jornada, fights the column at the second Valverde in October, accepts Carson's resignation, keeps the fort through the winter and, offered evacuation with arms and colours by Caleb, marches out in April 1863, fed by Pacifica on the road to Fort Union.", []),
    ("CT-JAMES-CARLETON", "James H. Carleton", "CR-061", "minor",
     "At Fort Union with too few wagons to empty Santa Fe; Canby makes him the department's acting commander there in January 1863.", []),
    ("CT-HENRY-SIBLEY", "Henry H. Sibley", "CR-061", "minor",
     "His Texans come up the Rio Grande in the winter of 1861–62 for the road to their Pacific supplier and lose it at Glorieta Pass at the end of March 1862.", []),
    ("CT-HENRY-HALLECK", "Henry W. Halleck, the Union's general in chief", "CR-061, CR-063, CR-064", "supporting",
     "A San Francisco lawyer who takes the first Panama steamer after Sumter in May 1861 and refuses the Republic's commissions (PROPOSED — CR-064). As general in chief he refuses Canby's request to go east and orders Fort Craig held, because while its flag flies the Union still claims the river; in the West his engineer McPherson talks him out of a mistake before he is called to Washington in July 1862.", []),
    ("CT-JOSEPH-WEST", "Joseph R. West, Caleb's deputy", "CR-061", "minor",
     "Colonel of the column's infantry, commanding in Caleb's absence. In January 1863 the Pinos Altos miners bring him Mangas Coloradas, seized under a flag of truce; he reads them Caleb's standing order, refuses to hold him and sends him home with a written safe-conduct.", [("deputy to", "CT-CALEB")]),
    ("CT-EDWARD-EYRE", "Edward E. Eyre, the column's cavalry officer", "CR-061", "minor",
     "Commands the advance cavalry at Mesilla in July 1862; asked by the alcalde to guard the flour they bought, his men fire when Sibley's rear guard comes to requisition it.", []),
    ("CT-MARSHALL-HOWE", "Marshall S. Howe", "CR-061", "minor",
     "Holds Fort Craig with seven hundred men at the second Valverde and strikes the entrenchment from the south; in April 1863 he marches out of Fort Craig to move the Mescalero onto a reserve at Bosque Redondo with too few men, and the attempt fails.", []),
    ("CT-JOHN-CHIVINGTON", "John M. Chivington", "CR-061", "minor",
     "His Coloradans try a ford against the light column at the narrows in October 1862; he falls back up the river and fires the Albuquerque depot.", []),
    ("CT-JAMES-REILY", "James Reily, Richmond's commissioner at San Antonio", "CR-061", "minor",
     "Carried Sibley's letters to the governors of Chihuahua and Sonora in 1862 (*hist.*); signs the Sunset articles for Richmond at San Antonio in February 1863 and is killed in Louisiana in April (*hist.* death).", []),
    ("CT-JOHN-MAGRUDER", "John B. Magruder", "CR-061", "minor",
     "Signs the Sunset articles for the military district at San Antonio in February 1863.", []),
    ("CT-HENRY-CONNELLY", "Henry Connelly, the Union's governor of New Mexico", "CR-061", "minor",
     "Too sick to govern, he withdraws to Las Vegas with the territorial government; his secretary, William Arny, claims the territory in his name.", []),
    ("CT-JOSE-MANUEL-GALLEGOS", "José Manuel Gallegos, speaker of the compact's House", "CR-061", "supporting",
     "The priest Bishop Lamy suspended, who wanted New Mexico a state and wanted no Texan in it. He keeps the speaker's chair at Santa Fe through January 1863 against the acting governor's order, signs the Rio Grande compact when the San Antonio articles are read in the plaza, and in December 1865 casts the speaker's vote that passes the abolition ordinance.", [("rival of", "CT-MIGUEL-A-OTERO")]),
    ("CT-MIGUEL-A-OTERO", "Miguel Antonio Otero (1829–1882)", "CR-061", "minor",
     "His name stands first on the Rio Grande compact, signed at Santa Fe in the spring of 1863, with Gallegos's beside it, though the two have been rivals since he took Gallegos's seat in Congress; his members keep Gallegos in the speaker's chair. Distinct from his son, the later governor.", []),
    ("CT-DIEGO-ARCHULETA", "Diego Archuleta", "CR-061", "minor",
     "In April 1866 he talks half of Rio Arriba's patrones out of the revolt against the abolition ordinance.", []),
    ("CT-JEAN-BAPTISTE-LAMY", "Jean-Baptiste Lamy, Bishop of Santa Fe", "CR-061", "minor",
     "Preaches abolition from the captive article on; the ordinance of December 1865 passes on the vote of the priest he suspended, Gallegos.", []),
    ("CT-MANUEL-CHAVES", "Manuel Antonio Chaves", "CR-061", "minor",
     "Guided Chivington's flank march at Glorieta (*hist.*); from the spring of 1863 he leads the Union's New Mexicans against the carretas in the Galisteo country.", []),
    ("CT-JOSE-FRANCISCO-CHAVES", "José Francisco Chaves", "CR-061", "minor",
     "Stays with the Union's territorial government at Las Vegas and with Francisco Perea publishes the protest against New Mexico's charter that goes to Washington in 1866.", []),
    ("CT-FRANCISCO-PEREA", "Francisco Perea", "CR-061", "minor",
     "Stays with the Union's territorial government at Las Vegas and with José Francisco Chaves publishes the protest of 1866.", []),
    ("CT-BARBONCITO", "Barboncito, Navajo leader", "CR-061", "supporting",
     "In December 1862 he and Delgadito come to Santa Fe to ask for peace, and he will speak of nothing else until the New Mexican slaving raids stop; the Cubero agreement follows in May 1863. With Manuelito he negotiates the homeland treaty of 1865, with Kit Carson across from him as the compact's commissioner.", [("negotiates across from", "CT-KIT-CARSON")]),
    ("CT-DELGADITO", "Delgadito, Navajo leader", "CR-061", "minor",
     "Comes to Santa Fe with Barboncito in December 1862 to ask for peace.", []),
    ("CT-MANUELITO", "Manuelito, Navajo leader", "CR-061", "minor",
     "Negotiates the Navajo homeland treaty of 1865 with Barboncito.", []),
    ("CT-MANGAS-COLORADAS", "Mangas Coloradas, Chihenne Apache leader", "CR-061", "supporting",
     "Seized by the Pinos Altos miners under a flag of truce in January 1863 and sent home by Joseph West with a safe-conduct; his Chihenne keep a truce from that winter. At Santa Rita del Cobre, where he met Kearny twenty years before, he brings his son-in-law Cochise to the table; the end of the scalp bounties is his price, and the copper mine is leased with a royalty to his people. He dies in his own country in the winter of 1866–67 and is buried by his people.", [("father-in-law of", "CT-COCHISE")]),
    ("CT-COCHISE", "Cochise, Chiricahua Apache leader", "CR-061", "supporting",
     "His Chiricahua fight the column for the springs at Apache Pass in July 1862 and raid the road now and then afterwards; at Santa Rita del Cobre in 1865 he comes to the table with Mangas, and the Chiricahua take passage money from the Sunset road's customs.", []),
    ("CT-BENITO-JUAREZ", "Benito Juárez, President of Mexico", "CR-061", "supporting",
     "Pacifica recognises his government as France withdraws and lends to it on the Sonora customs (APPROVED — CR-058). From the autumn of 1865 until June 1866 his government sits at Paso del Norte, where the rifles cross from New Mexico at a customs post agreed with Mexico. His words of 15 July 1867 become the continent's common language, and he would rather have a weak Confederacy on the Rio Grande than a reunited giant.", []),
    # CR-062: the Western treaty and Alaska
    ("CT-JOHN-SHERMAN", "John Sherman of Ohio", "CR-059, CR-062", "supporting",
     "William Sherman's brother (CT-SHERMAN is William; never merge). In 1859 he moves for the correspondence that helps keep Oregon out of the Union (PROPOSED — CR-059). In 1867, with Fessenden, he checks the gold in the New York Subtreasury and tells the Senate that Oregon can be ceded because it was never admitted, and that he helped keep it out; Wade and Chandler call the Western treaty one negotiated by one Sherman and ratified by the other.", [("brother of", "CT-SHERMAN")]),
    ("CT-EDUARD-STOECKL", "Eduard de Stoeckl, Russia's minister at Washington", "CR-062", "minor",
     "Home from Washington in 1866, he reports that the Union is ceding its only Pacific ports, could neither use Russian America nor defend it, and that a Senate selling the West will vote no money for land beyond it.", []),
    ("CT-ALEXANDER-GORCHAKOV", "Alexander Gorchakov, Russia's foreign minister", "CR-062", "minor",
     "Asks Pacifica's envoy whether selling Russian America to Pacifica would strengthen Britain, and is answered with the Republic's history.", []),
    ("CT-CHARLES-SUMNER", "Charles Sumner", "CR-062", "supporting",
     "In April 1867 he reads Oregon's returns and the article on colour, denounces Oregon's exclusion clause and speaks for the Western treaty: it cannot reach a citizen of any member state, Oregon's Black residents may choose their citizenship, and the Union's own Enabling Act never got the clause removed. His Alabama speech of 13 April 1869 (APPROVED — CR-058) is the Union's claim against Canada.", []),
    # CR-063 and CR-064: the Gulf and the West
    ("CT-FRANKLIN-BUCHANAN", "Franklin Buchanan, the Tennessee's admiral", "CR-063", "minor",
     "Commands the Confederate squadron in Mobile Bay; his *Tennessee* engages when the Union column breaks under Fort Morgan's fire in February 1865. Distinct from CT-JAMES-BUCHANAN.", []),
    ("CT-BENJAMIN-BUTLER", "Benjamin F. Butler", "CR-063", "minor",
     "His army of 15,000 waits at Ship Island in 1862 for a squadron that has gone to repair; ordered to Fort Monroe after the Seven Days, he goes home with no city to govern and no victory.", []),
    ("CT-DAVID-PORTER", "David D. Porter", "CR-063", "minor",
     "Bypasses Vicksburg's batteries with Grant in 1863; with Welles he wants Wilmington, Lee's last port, in the winter of 1864–65.", []),
    ("CT-GIDEON-WELLES", "Gideon Welles, the Union's Navy Secretary", "CR-063", "minor",
     "Wants Wilmington rather than Mobile in the winter of 1864–65.", []),
    ("CT-JOHN-PEMBERTON", "John C. Pemberton, Vicksburg's commander", "CR-063", "minor",
     "Keeps the telegram, fights at Champion Hill and loses; on 17 May 1863 he stays in the works with the beaten divisions and the heavy guns, because he will not be the Northern-born general who gave up Vicksburg, and surrenders the city at the turn of June and July.", []),
    ("CT-ALFRED-TERRY", "Alfred H. Terry", "CR-063", "minor",
     "His men sail from Hampton Roads for Mobile in January 1865 and cannot stay on Dauphin Island while the bay is Confederate.", []),
    ("CT-GEORGE-THOMAS", "George H. Thomas", "CR-064", "supporting",
     "Given the West by Grant over McPherson in 1864 because the Army of the Cumberland will serve under no younger man; he moves on Johnston in May 1864 with about a hundred thousand men on one railroad, flanks only toward the line behind his enemy, blockhouses every mile and, pressed by telegraph, answers that he will move when he is ready. He cannot spare Indiana's soldiers for the election.", []),
    ("CT-JAMES-MCPHERSON", "James B. McPherson", "CR-064", "supporting",
     "Halleck's engineer, who talks him out of a mistake in 1862; Grant's army commander from October 1863, at Jackson, Chattanooga and Knoxville. Grant gives him the West in November 1864, and days later he is shot from his horse in a wood between two of his own corps east of Atlanta.", []),
    ("CT-GREELEY", "Horace Greeley", "CR-065", "supporting",
     "On 2 September 1864 he and two other editors ask the governors whether Lincoln should withdraw, and his *Tribune* then endorses Lincoln without enthusiasm. He defeats Grant in 1872 and dies before the electors meet (canon §13).", []),
    # CR-067: the Republic's officers
    ("CT-CHARLES-STONE", "Charles Pomeroy Stone, acting chief of the General Staff", "CR-067", "supporting",
     "West Point 1845; the builder of the Benicia arsenal and surveyor of Sonora (*hist.*). He resigns early, builds Benicia for the Republic, joins Marcus's General Staff and runs it as acting chief while Marcus is abroad, late 1862 to 1864: the man history blamed for Ball's Bluff keeps the Department of the Rio Grande supplied (approved by the author, 9 November 2026).", [("acting chief for", "CT-MARCUS-I")]),
    ("CT-EDWARD-ORD", "Edward O. C. Ord, a fighting general", "CR-067", "supporting",
     "Approved by the author as a fighting general (9 November 2026); his recommended post is the field division of the Department of the Columbia under Naglee from late 1862, in the country where he campaigned in the 1850s (*hist.*). Naglee's vanity beside his steadiness is the department's working tension.", [("serves under", "CT-HENRY-NAGLEE")]),
    ("CT-HENRY-NAGLEE", "Henry Morris Naglee, Marcus's Northwestern deputy", "CR-067", "supporting",
     "A California volunteer of 1846–47, banker and San Jose brandy-maker (*hist.*). Brigadier general and Marcus's deputy in the Columbia from late 1862 (approved by the author, 9 November 2026), holding it against Silas Casey on the Sound; brave, vain and quarrelsome, good material for Sherman's inspections.", []),
    ("CT-JAMES-DENVER", "James W. Denver, commander of the Great Basin", "CR-067", "supporting",
     "A Californian of the 1850s, Commissioner of Indian Affairs and governor of Kansas Territory (*hist.*). Brigadier general commanding the Department of the Great Basin from October 1862 (approved by the author with the post, 9 November 2026), with Hays as his colonel on the Salt Lake road and Beale as commissioner; a department of politics as much as war.", []),
    ("CT-JAMES-ALDEN", "James Alden Jr., the commodore", "CR-067, CR-070", "supporting",
     "Wilkes Expedition officer and Pacific coast surveyor (*hist.*). He surveys California's coast for the Republic from 1849, heads its coast survey to 1861 with Davidson lent to it in 1850, knows every harbour from San Diego to Puget Sound and commands the fleet and chairs the Navy Board in the war (approved by the author, 9 November 2026).", []),
    ("CT-GEORGE-A-JOHNSON", "George Alonzo Johnson, captain of the Colorado flotilla", "CR-067", "minor",
     "The pioneer of Colorado River steam navigation (*hist.*); his boats are taken into confederal service in 1862 and he commands them, supplying the Department of the Rio Grande from Fort Yuma (approved by the author, 9 November 2026).", []),
    ("CT-JAMES-T-WATKINS", "James T. Watkins, captain of the Northwestern transports", "CR-067", "minor",
     "Pacific Mail captain, honoured for the rescue of the *San Francisco*'s troops in 1854 (*hist.*); he commands the chartered steamers that carry the Northwestern expedition (approved by the author, 9 November 2026).", []),
    # CR-069: the coin and the bank
    ("CT-JOSEPH-DONOHOE", "Joseph A. Donohoe, Ralston's partner", "CR-069", "minor",
     "Ralston's partner in Donohoe, Ralston & Co. (1861–64; *hist.*). He wants the firm's future in New York; they quarrel in private and part in public as friends in 1864. Distinct from Peter Donahue of the workshops (CT-DONAHUE). Dates OPEN.", [("partner of", "CT-RALSTON")]),
    ("CT-DARIUS-MILLS", "Darius Ogden Mills", "CR-069", "minor",
     "Opens the Bank of California with Ralston on 4 July 1864, its capital paid in gold coin, as its president (*hist.*).", [("bank founder with", "CT-RALSTON")]),
    ("CT-EUGENE-KELLY", "Eugene Kelly, Ralston's partner in New York", "CR-069", "minor",
     "A founding partner of Donohoe, Ralston & Co. (1861; *hist.*), in New York through the war (PROPOSED). Distinct from Kelly of the steel experiments (CT-KELLY).", [("partner of", "CT-RALSTON")]),
    # CR-070: the north
    ("CT-KOWEE", "Kowee (Kawa.ée), Auk Tlingit leader", "CR-070", "supporting",
     "In 1872 he brings ore from Gastineau Channel to the assay office at Sitka and will not show its source until the Commission has agreed his people's share: the first finder's compact. When the prospectors he guides, Harris and Juneau, come back with too little, he tells the assayer to send them out again; the town takes Juneau's name, not his. Dates OPEN.", []),
    ("CT-RICHARD-HARRIS", "Richard Harris, prospector", "CR-070", "minor",
     "One of the two prospectors Kowee guides to the Gastineau gold in 1872.", [("guided by", "CT-KOWEE")]),
    ("CT-JOE-JUNEAU", "Joe Juneau, prospector", "CR-070", "minor",
     "One of the two prospectors Kowee guides to the Gastineau gold in 1872; the town on the gold belt takes his name.", [("guided by", "CT-KOWEE")]),
    ("CT-NICOLAI-AHTNA", "Nicolai, Ahtna leader of Taral", "CR-070", "minor",
     "In 1885 he shows the Commission's party the copper of the Chitina and makes a finder's compact for it, so that he never has to trade its whereabouts for food.", []),
    ("CT-GEORGE-DAVIDSON", "George Davidson, coast surveyor and Northern Commissioner", "CR-070", "supporting",
     "Historical person (1825–1911) in an alternate role: lent by Bache to Alden's survey in 1850, head of the Republic's coast survey from 1861 and the second Northern Commissioner, succeeding Pablo de la Guerra in 1873. Kohklux drew him a map of the Chilkat road when he was a guest in 1869 and will not open it to him as Commissioner.", [("succeeds", "CT-PABLO-DE-LA-GUERRA")]),
    ("CT-KOHKLUX", "Kohklux, Chilkat leader of Klukwan", "CR-070", "minor",
     "Davidson's host in August 1869 and, with two of his wives, the maker of the map of the Chilkat road; in 1880 the Chilkat refuse the Commission a compact, and their pass stays theirs and closed.", []),
    ("CT-DANIEL-LIBBY", "Daniel B. Libby, prospector of the Seward Peninsula", "CR-070", "minor",
     "Found gold on the Niukluk with the telegraph survey in 1866 and kept it to himself (*hist.* find); from 1876 he leads the Northern Commission's parties on the Seward Peninsula, supplied by the whalers at Norton Sound.", []),
]

LINCOLN = ("CT-ABRAHAM-LINCOLN", "Abraham Lincoln, Elias's antagonist", "CR-065, CR-068", "principal_or_developed", """**Status:** Historical person in alternate history; CR-065 and CR-068, {st}.

Born 1809. A first-term Whig member for Illinois who votes for Ashmun's amendment and asks the President to show the spot where the war began (1848); his opponents revive that vote in 1860, the war that ended with California outside the Union. President 1861–1865: he refuses Seward's foreign war, offers release and an inquiry over the dead sailor in June 1861, answers the bankers with the Legal Tender Act, proclaims emancipation on 1 January 1863, answers the Republic's terms of passage and *Two Houses* in public letters and refuses both, and offers the people of Pacifica his terms in the spring of 1864. He expects to lose, keeps the memorandum's pledge and loses the election of November 1864 to McClellan (PROPOSED — CR-065). Afterwards a private citizen at Springfield with Herndon: he writes to Oregon's Union men in the *Oregonian* in June 1866 and to the Senate in the *Chicago Tribune* in 1867, advising it to take the purchase money and refuse the separate loan. In 1869 he comes west by sea at Elias's invitation, paying his own passage, and the two men meet once; no record of what was said survives. He dies at Springfield in November 1872.

**Function:** Elias's agonal counterpart, the keeper of the law against the founder by law. He reads Elias first as the eagle of his own Lyceum address and then as a man who binds himself in public and will give up anything but power (CR-068 MD3, MD4). His stratagems are his historical ones.

**Voice:** Plain, exact, biblical cadence, humour as a weapon, reticence ("terribly reticent, secretive, shut-mouth", Herndon). Never a saint and never a fanatic. His words on the page are his own; invented words only in marked in-world documents.""".format(st=ST), [("agonal counterpart of", "CT-ELIAS"), ("defeated in 1864 by", "CT-MCCLELLAN")])

ADD = {
    "CT-ELIAS": "**CR-059 to CR-070 ({st}):** He governs the war as Protector from 1 June 1861 to 31 May 1865 and annexes nothing by decree: Oregon, Washington Territory, Deseret, Washoe, western Montana and New Mexico are held under compacts and come in by their own votes and charters of 1866, members on the exchange of 1867. In the winter of 1862–63 he goes by Santa Fe and Taos to Texas (the Sunset articles at San Antonio and the printed terms of the Richmond credit), and on 24 July 1863 he signs the Compact of Association with Brigham Young. CR-068 adds his reading of Lincoln, first as the Whig of 1848 and from the winter of 1862–63 as a man who does whatever the law can bear; his costly misjudgment of Lincoln's hour in the autumn of 1862; the seven reasons of 1861, the armistice offer of 1862, the answer at Honolulu, *Two Houses*, the Terms of Monterey and their preface, the blind vote of November 1864 and the answer to Oregon of 1866, all in the open; and his annotated copies of Lincoln's speeches. He lets the Protectorship lapse with its term in May 1865, governs six months as Chancellor and lays the heads of the Enabling Law before the Council himself. He brings the Northern Commission's charter to the chambers as a bill, because the compacts need a ratifier that will outlive him.",
    "CT-KAIULANI": "**CR-059 to CR-070 ({st}):** She is the judge of the contest's heavy beats before 1865, and her prices are Hawaii's: Honolulu's batteries and frigates and the second turret ship (1861), Deady's relief steamer released (1861), control of entry and quarantine at Hawaiian ports and the Carson guarantees for the third renewal (1864), and the end of the renewals with a lawful settlement that protects Hawaii's institutions (November 1864), which she negotiates into the Enabling Law at Monterey in 1865, voting with the King's letter and keeping her reservations about its reach. The Proclamation does not move her. In 1866 she has Oregon's exclusion article limited to people who are not citizens of a member state, and Hawaii's legislature ratifies Oregon's charter on her message; she keeps the Hawaiian sailor's family's claim before the claims commission and will not have the Alaska treaty dispose of the nations' lands. In 1871–72 she supports the border controls, by the government's standing instructions to Hawaii's delegation. In 1876 she remembers that Elias brought the Northern Commission's charter to the chambers as a bill.",
    "CT-SHERMAN": "**CR-059 to CR-070 ({st}):** Major general and Inspector-General, reporting to the Protector and the Council (CR-067). With Victoria he says in 1862 that a garrison on the Salt Lake road needed the Council's vote; after his refusal of 1862 Elias keeps him in office. In 1864 he insists that the Washoe garrison leave with its arms and tells the cabinet that Lincoln will not unsay the Proclamation. At Monterey in 1865 he tells the committee that an office for life has its date too and is not answered. In December 1865 he signs the Western treaty and the Oregon protocol at Washington beside Vallejo; his brother John votes on it (CT-JOHN-SHERMAN). He keeps silent over the Union's campaign of 1864.",
    "CT-CHRONICLER": "**CR-068 ({st}):** His Lincoln is adversarial in judgment and never in fact; he judges by declared terms; his blind spot is consent as procedure. He writes the Comparison of Thorne and Lincoln.",
    "CT-RALSTON": "**CR-069 ({st}):** Ohio-born, he takes the Republic's oath in July 1861, with his family in Ohio and his partner Eugene Kelly in New York. In the run of January 1862 he pays every depositor in gold, and on 1 March he brings Elias the houses' Steamer Day Agreement in place of a ban on the export of coin, and keeps it at a cost to his own firm. He brings the houses to take the Republic's war bonds in coin (PROPOSED). In 1864 he and Joseph Donohoe quarrel in private and part in public as friends, and on 4 July he and Darius Ogden Mills open the Bank of California. In 1867 his bank is the Republic's agent for the loan the Senate declined, taking a share of its own. His later fate stays OPEN.",
    "CT-CALEB": "**CR-061 and CR-067 ({st}):** Brigadier general commanding the Department of the Rio Grande from 1862, reporting to the Protector through the General Staff. His standing order is that a chief who comes in under a flag goes home under one. He goes with Elias to Texas in January–February 1863, leaving Joseph West in command, and on his return offers Canby evacuation with arms and colours; Fort Craig marches out in April 1863.",
    "CT-PABLO-DE-LA-GUERRA": "**CR-061, CR-062 and CR-070 ({st}):** Elias's civil commissioner in New Mexico, who carries on the Rio Grande compact after Elias leaves for Texas and signs the Cubero agreement with the Navajo in May 1863; Pacifica's envoy at St Petersburg in 1866–67 (CR-062 K3; the storyline leaves the envoy unnamed); the first Northern Commissioner, 1867–1873, succeeded by George Davidson.",
    "CT-ANDRES-PICO": "**CR-061 and CR-067 ({st}):** Raises the Californio lancers of the autumn campaign of 1862, and as brigadier general commands the Department of California, through which the others are reinforced and supplied.",
    "CT-HAYS": "**CR-060 and CR-067 ({st}):** Colonel with a regular commission, commanding on the Salt Lake road from October 1862 under Denver. In January 1863 he marches on the Bear River winter camp with warrants for the men who killed the Bannack miners and orders not to touch the lodges; Bear Hunter's men fight him for a morning and draw off, and he does not follow.",
    "CT-MARCUS-I": "**CR-060 and CR-067 ({st}):** Major general, the army's senior officer and chief of the General Staff, commanding the Northwestern expedition in person in 1861–62; his military mission in the Confederacy from late 1862 to late 1863 advises but cannot order, while Charles Stone runs the General Staff. He retakes Washoe in the spring of 1864 and commands the Columbia again from mid-1864.",
    "CT-FARRAGUT": "**CR-063 ({st}):** He goes home to New York worn out in December 1864, argues for Mobile, goes back by the mail steamer by his own insistence, and is killed when *Hartford* strikes one of Logan's torpedoes in February 1865; the Western treaty charges his death to no one.",
    "CT-FREMONT": "**CR-065 ({st}):** In 1864 he stands as the radicals' candidate and withdraws to keep McClellan out.",
    "CT-MCCLELLAN": "**CR-062 and CR-065 ({st}):** He defeats Lincoln on 8 November 1864 (about 120 electoral votes to 103, MODEL), takes the oath on 4 March 1865, signs the armistice conventions of March–June, puts the signed Western treaty in his safe in December 1865 and sends it to the Senate in April 1867 with Oregon's certified returns.",
    "CT-VALLEJO": "**CR-062 ({st}):** In the third week of December 1865 he signs the Western treaty at Washington, the instrument that ends the convention he signed in the same city in 1848, and with Sherman the protocol on Oregon's choice.",
    "CT-LOGAN-TURNER": "**CR-062 ({st}):** When the technical mission is dissolved under the armistice of 1865 he stays in New Orleans on his own account, and in 1866 turns down a contract from Richmond's navy for a better offer from the Gulf's merchants.",
    "CT-DONAHUE": "**CR-069 ({st}):** Distinct from Joseph A. Donohoe, Ralston's partner (CT-JOSEPH-DONOHOE).",
    "CT-KELLY": "**CR-069 ({st}):** Distinct from Eugene Kelly, Ralston's partner in New York (CT-EUGENE-KELLY).",
    "CT-DAVID-KALAKAUA": "**CR-067 ({st}):** Hawaiian member of the Navy Board from 1863 (approved by the author, 9 November 2026).",
}


def section_text() -> str:
    out = [f"## CR-059 to CR-070 — the Civil War, the West and the north ({DATE})", "",
           "Historical persons in alternate history unless marked; no invented persons are added. "
           "Each profile keeps the local label of the storyline passage it rests on.", ""]
    cid, name, cr, _tier, text, _links = LINCOLN
    out += [f"### {cid} — {name}", "", text, ""]
    for cid, name, cr, _tier, text, _links in NEW:
        out += [f"**{cid} — {name}.** Historical person in alternate history; {cr}, {ST}. {text}", ""]
    return "\n".join(out).rstrip() + "\n"


def bible_profiles(bible: str) -> dict[str, str]:
    """The validator's own chunking, reproduced."""
    starts = []
    for m in re.finditer(r"^### (CT-[A-Z0-9-]+) — [^\n]+$|^\*\*(CT-[A-Z0-9-]+) — [^\n]+?\*\*", bible, re.M):
        starts.append((m.start(), m.group(1) or m.group(2), "dossier" if m.group(1) else "short"))
    breaks = sorted(m.start() for m in re.finditer(r"^## |^### |^\*\*CT-[A-Z0-9-]+ — ", bible, re.M))
    out = {}
    for pos, cid, kind in starts:
        after = next((q for q in breaks if q > pos), len(bible))
        chunk = bible[pos:after].strip()
        if kind == "dossier":
            chunk = chunk.split("\n", 1)[1].strip()
        else:
            chunk = re.sub(r"^\*\*CT-[A-Z0-9-]+ — [^\n]+?\*\*\s*", "", chunk)
        out[cid] = (pos, after, chunk)
    return out


def main() -> int:
    bible = BIBLE.read_text(encoding="utf-8")
    if "CT-ABRAHAM-LINCOLN —" in bible:
        print("already applied")
        return 1
    # Kit Carson: the pending markers are now integrated
    bible = bible.replace("**Pending with CR-061 (draft):**", f"**APPROVED — CR-061 ({DATE}):**")
    bible = bible.replace(" **Pending with CR-061:** the compact's commissioner, not Pacifica's, across from Barboncito in 1865.", "")
    # additions to existing entries, from the bottom up
    prof = bible_profiles(bible)
    for cid in sorted(ADD, key=lambda k: -prof[k][0]):
        pos, after, _ = prof[cid]
        head = bible[:after].rstrip()
        bible = head + "\n\n" + ADD[cid].format(st=ST) + "\n\n" + bible[after:].lstrip("\n")
    bible = bible.rstrip() + "\n\n" + section_text()
    BIBLE.write_text(bible, encoding="utf-8")

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    have = {p["id"] for p in reg["people"]}
    new_ids = []
    for cid, name, cr, tier, _text, links in [LINCOLN] + NEW:
        if cid in have:
            raise SystemExit(f"{cid} exists")
        reg["people"].append({
            "id": cid, "display_name": name, "nature": "historical_person_in_alternate_history",
            "tier": tier, "identity_state": "approved_alternate_role_details_open",
            "story_bible_section": cid, "narrative_profile": "",
            "links": [{"relationship": r, "to": t} for r, t in links],
            "legacy_profile_indices": [], "legacy_conflicts": [],
            "source_authority": [c.strip() for c in cr.split(",")],
        })
        new_ids.append(cid)
    prof = bible_profiles(BIBLE.read_text(encoding="utf-8"))
    for p in reg["people"]:
        if p["id"] in prof:
            p["narrative_profile"] = prof[p["id"]][2]
    n = len(reg["people"])
    retired = reg["stats"].get("retired_identities", 0)
    reg["stats"]["canonical_dossiers"] = n
    reg["stats"]["active_or_provisional_identities"] = n - retired
    reg["updated_on"] = "2026-11-15"
    entry = {
        "request": "CR-059 to CR-070",
        "source": "CR-059 to CR-065 and CR-067 to CR-070; author approval of 15 November 2026 (\"I approve the crs\")",
        "status": "approved_integrated",
        "updated_ids": sorted(ADD) + ["CT-KIT-CARSON"],
        "new_ids": new_ids,
        "limits": "Only persons on the page or approved in CR-067 are registered; the others named in the CRs stay without entries. Dates of the Native leaders and of Donohoe OPEN; Sherman's fate after 1865 OPEN.",
    }
    reg["character_revision_history"].append(entry)
    reg["character_revision"] = entry
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added {len(new_ids)} persons, updated {len(ADD) + 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
