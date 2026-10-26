"""Assemble this forward review from explicitly authored records, without old case data."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import subprocess
from rdflib import Graph, Namespace, RDF, RDFS, Literal, URIRef, XSD

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PC = Namespace('urn:pacifica:ontology:review:')
V = Namespace('urn:pacifica:vocab:review:')
N = Namespace('urn:pacifica:review:forward-gold-20261026:')
PROV = Namespace('http://www.w3.org/ns/prov#')
G = Graph()
for prefix, ns in [('pc', PC), ('v', V), ('fg', N), ('prov', PROV)]: G.bind(prefix, ns)
BASE = '4ea16e3a739c807a5f20bbb8ffb98450b84215c7'

def add(s,p,o): G.add((s,p,o))
def lit(s,p,t): add(s,p,Literal(t))
def record(id,kind,label):
    u = N[id]; add(u,RDF.type,PC[kind]);lit(u,RDFS.label,label);return u
def ent(id,label,kind='Resource',registry=None):
    u = URIRef('urn:pacifica:character:'+registry) if registry else N[id]
    add(u,RDF.type,PC.Entity);lit(u,RDFS.label,label);add(u,PC.entityKind,V[kind])
    if registry:lit(u,PC.registryId,registry)
    return u

sources = {
 'master': ('book-agent/revision/master_storyline.md','NarrativeSource','LFNormalizedText'),
 'approvals': ('book-agent/revision/change_requests.json','NarrativeSource','LFNormalizedText'),
 'registry': ('book-agent/revision/character_registry.json','RegistrySource','LFNormalizedText'),
 'bible': ('book-agent/revision/character_bible.md','RegistrySource','LFNormalizedText'),
 'history': ('book-agent/revision/historical_background.md','ReviewSource','LFNormalizedText'),
 'finance': ('finance/CR-031-review.md','ReviewSource','LFNormalizedText'),
 'rent': ('finance/CR-027-handoff.md','ReviewSource','LFNormalizedText'),
 'dossier': ('docs/power-review/ontology/inputs/evidence.md','ReviewSource','ExactBytes'),
 'inherited-finance': ('docs/power-review/ontology/inputs/financial-analysis.json','CalculationSource','ExactBytes'),
 'calculation': ((OUT/'diagnostic.py').relative_to(ROOT).as_posix(),'CalculationSource','LFNormalizedText'),
 'diagnostic': ((OUT/'financial-diagnostic.json').relative_to(ROOT).as_posix(),'CalculationSource','LFNormalizedText'),
}
files = {}
for key,(path,kind,basis) in sources.items():
    content=(ROOT/path).read_bytes()
    if basis=='LFNormalizedText':content=content.replace(b'\r\n',b'\n')
    sha=hashlib.sha256(content).hexdigest();files[path]={'sha256':sha,'hash_basis':basis}
    u=record('D-'+key,'SourceDocument',path)
    lit(u,PC.documentPath,path);lit(u,PC.sha256,sha);add(u,PC.hashBasis,V[basis]);add(u,PC.sourceKind,V[kind]);add(u,PC.retrievalStatus,V.LocalPinned)

def passage(id,doc,locator):
    u=record(id,'SourcePassage',locator);add(u,PROV.specializationOf,N['D-'+doc]);lit(u,PC.locator,locator);return u

for key,loc in {
 'P01':'lines 117, 125: October 1847 find and delayed official confirmation, locally PROPOSED CR-028',
 'P02':'lines 127-131: inherited mining rules, 1849 royalty, 1850 mint and separate private claims',
 'P03':'lines 137-139, 183-189: 1852 office, legislative obstruction and technical-contract network',
 'P04':'lines 213-219, 333-339: constitutional enabling procedure, life office and lapse',
 'P05':'lines 483-505: Realm constitution, charters, appointment limits and negotiated succession',
 'P06':'lines 520-530: independent estates and unwritten Crown bargain, proposed personnel and compact',
 'P07':'lines 630-642: contested succession, Act, independent crowns, accession and retained charter',
 'P08':'lines 664-668: ordinances, Senate resistance and distinct Japanese government',
 'P09':'lines 678-691: approved credit mechanism, MODEL allocations and proposed 1918 halt',
 'P10':'lines 701, 739-750: short funding, earthquake, Japanese own capital and FX facility',
 'P11':'lines 752-762: loan/treaty distinction, illegal application, legal cure and common offices',
 'P12':'lines 782-792, 806-808: Reserve Bank actions, distress, renewal, conditional command',
 'P13':'lines 818-828: proposed Union settlement and authored endpoint, independent Union',
 'P14':'line 840: Crown-estates arrangement tested in 1887, 1913 and 1915-1917; Altai report breaks it in 1921',
 'P15':'lines 590, 596, 727: foreign gold purchased against credit, sector-specific Crown shares, private management and no banking Crown equity',
}.items():passage(key,'master',loc)
passage('PA','approvals','$.requests[?(@.id=="CR-014")].requirements; CR-021 requirements (subject to later CR-027), CR-024/025 requirements[0], CR-027 requirements[20:23], CR-028 requirements[0] and open[0], CR-029 requirements')
passage('PI','registry','$.people[?(@.id in ["CT-ELIAS","CT-KAIULANI","CT-JULIAN","CT-SOBERANES"])]; stable IDs and narrative_profile')
passage('PH','history','lines 29-30, 96, 174, 309-321: mining law boundaries, bullion not sole war cause, local CR-028/029 qualifications')
passage('PF','finance','sections Saved Story-case reference values; Narrative commitments and accounting boundaries; Source discrepancies retained for the author')
passage('PR','rent','Puʻuloa lease and Victoria estate bullets; unprovided rent and estate values')
passage('PD','diagnostic','financial-diagnostic.json: output_musd; baseline_5pct_90pct_gross_musd; sensitivity; checks; endpoint_1932_power_delta')
passage('PCALC','calculation','diagnostic.py: output=sum(baseline_rows 1849-1852); gross=output*rate*collection; baseline=.05*.9*output')
passage('PIN','inherited-finance','$.baseline_rows; $.break_even; $.debt_timing; $.mechanism_boundary; supplied cached values and original check flags, not rerun here')

hist = [
 ('H1','US Mint historical overview','https://www.usmint.gov/learn/history/overview','ReportedByDossier','California Gold Rush section; inherited dossier H1, access reported 26 October 2026; not retrieved anew'),
 ('H2','Director of the Mint report, 30 January 1855','https://www.govinfo.gov/content/pkg/SERIALSET-00788_00_00-004-0062-0000/pdf/SERIALSET-00788_00_00-004-0062-0000.pdf','ReportedByDossier','House Executive Document 62, 33rd Congress 2nd Session, printed pp.2-3; inherited dossier H2; text retrieved by prior analyst, page-image request failed'),
 ('H3','Manuel Payno Mexican debt compilation','https://www.letrasmexicanas.mx/obra-visor/mexico-y-sus-cuestiones-financieras-con-la-inglaterra-la-espana-y-la-francia-memoria-que-por-orden-del-supremo-gobierno-constitucional-de-la-republica-escribe-el-c-manuel-payno--0/html/1f955a22-2cb3-4714-9ce2-9ffc1fdf0c92_9.html','ReportedByDossier','appendix document 17, accepted 4 June 1846, printed pp.31-33, Articles 3,5,7; edition publication date unestablished; inherited dossier H3 paraphrases'),
 ('H4','Smithsonian assay-office catalogue lead','https://collections.si.edu/search/detail/edanmdm%3Anmah_1101903?print=yes','Unretrieved','inherited dossier H4; search lead only, full record retrieval failed; no verified contracting evidence'),
]
for key,title,url,retrieval,loc in hist:
    u=record('D-'+key,'SourceDocument',title);add(u,PC.sourceKind,V.HistoricalSource);add(u,PC.retrievalStatus,V[retrieval]);add(u,PC.sourceURL,URIRef(url));add(u,PROV.wasDerivedFrom,N['D-dossier']);passage(key,key,loc)

E={}
for id,label,kind,reg in [
 ('elias','Elias Thorne','Person','CT-ELIAS'),('victoria','Victoria Kamāmalu','Person','CT-KAIULANI'),('julian','Julian Thorne','Person','CT-JULIAN'),
 ('california','Republic of California','Jurisdiction',None),('realm','Pacifica Realm','Jurisdiction',None),('concord-scope','Common Concord matters','Jurisdiction',None),('japan','Japan','Jurisdiction',None),('union-scope','Sovereign Union','Jurisdiction',None),
 ('treasury','Public Treasury','Institution',None),('superintendent','Superintendent of Mines and Public Revenue','Office',None),('providentor','Life Providentor','Office',None),('sovereign','Sovereign of Pacifica','Office',None),('regent','Regent of the Realm','Office',None),('polytechnic','Polytechnic chartered estate','Institution',None),('estates','Chartered estates including measures and technical establishments','Collective',None),('crown','Crown as an enduring institution','Institution',None),('creditors','London bondholders','Collective',None),('investors','Foreign and Pacifican private subscribers','Collective',None),('syndicates','San Francisco syndicates','Institution',None),('japan-banks','Japanese international banks','Institution',None),('reservebank','Pacifica Reserve Bank','Institution',None),('concord','Two-party Pacific Concord','Institution',None),('union','Union government','Institution',None),
 ('gold','California gold and official processing flow','Resource',None),('royalty','5% royalty entitlement','Resource',None),('royalty3','Candidate 3% royalty entitlement','Resource',None),('cash','Public royalty receipts','Resource',None),('private-claims','Elias private mining property','Resource',None),('revenues','Customs and prospective mineral revenues pledged to debt','Resource',None),('network','Skills, suppliers, transport and public contractors','Resource',None),('delegation','1865 Enabling Law delegation','Instrument',None),('constitution','1887 constitutional appointment and regency provisions','Instrument',None),('act','1914 Act of Settlement and 1915 accession','Instrument',None),('charter','Polytechnic charter','Instrument',None),('bargain','Unwritten Crown-estates reciprocal restraint','Instrument',None),('shares','Crown champion shares with distribution boundaries','Resource',None),('capacity','Estate-held force, money, communications and statistics','Resource',None),('minister-appointments','Minister appointment and ordinance power','Resource',None),('entente','Entente loan claims','Resource',None),('newissues','New Entente syndicate issues','Resource',None),('shortfunding','Short foreign funding obligations','Resource',None),('facility','Japan FX rescue credit','Resource',None),('loanvote','Senate vote for rescue loan and guarantee/on-loan scheme','Instrument',None),('common-policy','Common Foreign Affairs, Navy and Finance decisions','Resource',None),('consent','1928 Senate consent, indemnity and Concord instruments','Instrument',None),('overseas-command','Japan overseas commands in common command','Resource',None),('renewal','1932 renewal ratified by both crowns and delegations','Instrument',None),('bank-resources','Gold lending, bank recapitalization and debt restructuring','Resource',None),('bank-gap','Reserve Bank mandate and access boundaries not detailed here','Instrument',None),('association','Union monetary/arbitration association and diplomatic concessions','Resource',None),('collection-service','Staged assay/remittance collection service','Institution',None),('assay-service','Assay, stamped bars or other settlement/remittance services','Resource',None),('crisis-protocol','Candidate reciprocal accession/crisis coordination protocol','Instrument',None),('coordinated-response','Time-limited coordination of estate and Treasury action','Resource',None)]: E[id]=ent(id,label,kind,reg)

for id,label,kind in [('private-firms','Private firms retaining management and competition','Collective'),('management','Firm management and competitive decisions','Resource'),('bank-equity','Equity ownership in private banking','Resource'),('purchased-gold','Foreign concession gold purchased against credit','Resource'),('fund','Development Fund','Institution'),('surplus','Public surplus subject to Fund claim','Resource')]: E[id]=ent(id,label,kind)

def case(id,label,kind,description,divergence,downstream):
    u=record(id,'ComparisonCase',label);lit(u,PC.sourceRevision,BASE);add(u,PC.interventionKind,V[kind]);lit(u,PC.changeDescription,description);lit(u,PC.earliestDivergence,divergence);lit(u,PC.heldAssumptions,'Matched inherited sources and external shocks; no new historical retrieval; no workbook reading or century-long rerun; all local authorial labels preserved.');lit(u,PC.downstreamStatus,downstream);lit(u,PC.endpointYear,1932)
    if id!='B':add(u,PC.baselineCase,N.B)
case('B','Retain authored baseline','Baseline','Retain the current narrative and its local proposals, gaps and MODEL numbers.','No new divergence; earliest reviewed proposed mechanism October 1847.','Authored 1932 outcome retained as a narrative consequence, not proof of marginal early-policy effects.')
case('C','Minimal gold/revenue clarification','Exposition','Explain entitlement, throughput, receipts, pledge and public/private boundaries without assigning new outcomes or collection efficacy.','None: exposition only.','World trajectory unchanged by definition; support improves only where it restates existing mechanisms.')
case('S','Candidate staged assay and remittance collection service','WorldChange','Start with an assay/remittance service and clear receipts/audit; commission coinage only after equipment, supplies and operators are demonstrated; retain 5% subject to author choice.','Possible 1848-1850 collection and commissioning changes; dates conditional.','Later credit, investment, survival and succession are not replayed; no retained alternative endpoint asserted.')
case('R','Candidate 3% royalty','WorldChange','Replace 5% with 3%; diagnose fixed output at explicit collection fractions, without predicting behavioral gains.','Mining Law of 1849, unless a distinct earlier law is authorized.','Only 1849-1852 gross fiscal diagnostic calculated; later authored outcomes not assumed to survive.')
case('AC','Clarify accession and crisis cooperation','Exposition','Show how known charter safeguards, nomination rules, ministerial offices and reciprocal legitimacy work; state the unprovided syndicate decision instrument as a gap.','None: exposition only.','Does not create an inherited life delegation, estate subordination or new syndicate powers.')
case('AD','Candidate substantive coordination bargain','WorldChange','Negotiate a reciprocal accession/crisis protocol: who requests action, which estate decisions and new issues are covered, independent assent, costs, reporting and expiry.','At 1914-1915 accession or a separately authorized later crisis; date is an author choice.','Reassess Senate, estate and investor resistance plus later finance; no endpoint rerun.')

def claim(id,label,sub,pred,obj,years,passages,status='Unspecified',basis='NarrativeStatement',state='Known',case='B',truth=True,missing=None,control=None):
    u=record(id,'Claim',label);add(u,PC.subject,E[sub]);add(u,PC.predicate,PC[pred]);add(u,PC.case,N[case]);lit(u,PC.period,f'{years[0]}–{years[1]} (inclusive review coverage)');lit(u,PC.startYear,years[0]);lit(u,PC.endYear,years[1]);add(u,PC.jurisdiction,E['concord-scope' if id in ['C22','C23'] else 'realm' if years[0]>=1856 else 'california']);add(u,PC.authorialStatus,V[status]);add(u,PC.claimBasis,V[basis]);add(u,PC.valueState,V[state]);
    if obj:add(u,PC.object,E[obj])
    if state=='Known':lit(u,PC.truthValue,truth)
    else:lit(u,PC.missingReason,missing)
    for p in passages:add(u,PROV.wasDerivedFrom,N[p])
    if control:
        office,instrument,gap,conditions,refusal,expiry,burdens=control;add(u,PC.actingThrough,E[office])
        if instrument:add(u,PC.controlInstrument,E[instrument])
        else:lit(u,PC.instrumentGap,gap)
        for p,t in [(PC.conditions,conditions),(PC.refusalTerms,refusal),(PC.expiryTerms,expiry),(PC.burdens,burdens)]:lit(u,p,t)
    return u

claim('C01','Proposed discovery and secrecy before public announcement','elias','establishes','gold',(1847,1848),['P01','PA'],'Proposed')
claim('C02','Law sets a public 5% entitlement at mint and trade choke points','treasury','hasClaimOn','royalty',(1849,1852),['P02'])
claim('C03','Narrative says the state begins receiving gold and other revenues','treasury','receives','cash',(1850,1852),['P02'])
claim('C04','Registered private claims belong to Elias and remain separate','elias','owns','private-claims',(1848,1887),['P02'])
claim('C05','Proposed recognition debt pledges customs and mining revenue','creditors','hasClaimOn','revenues',(1848,1852),['P01','P03','PA'],'Proposed')
claim('C06','1852 Superintendent controls collections, credit and works subject to legislators','elias','hasAuthorityOver','cash',(1852,1855),['P03'],control=('superintendent',None,'Precise statutes and expenditure controls remain unprovided.','Collection and investment mandate; public office, not private property.','Legislators can frustrate taxes, loans, subsidies and ports.','Later offices reorganize authority; this office is not automatically inherited.','Contractor payments, debt service, courts, staff and contested rights.'))
claim('C07','Public contracts and careers preserve an expanding technical network','treasury','retains','network',(1852,1887),['P03'])
claim('C08','1865 constitutional amendment concentrates agenda and appointments in Elias','elias','hasAuthorityOver','minister-appointments',(1865,1887),['P04','PA'],'Approved',control=('providentor','delegation',None,'Two-thirds both chambers and founding-state ratification; protected Hawaiian institutions.','Ministers retain expertise and constituencies; courts enforce ordinary property; protected provisions remain binding.','Life Providentorship; delegation lapses with 1887 regency.','Reconstruction, war debt, patronage obligations and protected revenues.'))
claim('C09','Life enabling delegation expires at the regency','elias','expires','delegation',(1887,1887),['P04','P06','PA'],'Approved')
claim('C10','Polytechnic retains charter, nominations and Senate-protected removal','polytechnic','retains','charter',(1887,1932),['P05','P07'],'Approved')
claim('C11','Victoria coordinates independent estates by reciprocal legitimacy and restraint','victoria','cooperatesWith','estates',(1887,1915),['P06','PA'],'Approved')
claim('C12','Crown holds champion shares, without a free purse','crown','owns','shares',(1887,1932),['P06'],'Approved')
claim('C13','Julian accedes through settlement and distinct crown consents','julian','holdsOffice','sovereign',(1915,1932),['P07','PI','PA'],'Approved')
claim('C14','Julian appoints ministers and uses reviewable ordinances through sovereign office','julian','hasAuthorityOver','minister-appointments',(1915,1932),['P05','P08','PA'],'Approved',control=('sovereign','constitution',None,'Realm powers and charter protections survive accession; ordinances laid before next session.','Senate resists; Polytechnic nominees and Senate removal consent constrain estate chief.','Office follows succession law; enabling delegation is not revived.','Support coalitions, court/legislative conflict, grant obligations and official continuity.'))
claim('C15','Unresolved detailed means for Julian to obtain estate resources during a Crown-estate conflict','julian','canMobilize','capacity',(1915,1932),['P06','P07','P08','P14'],'AuthorialNotApplicable','AnalystInference','Unknown',missing='Reciprocal bargain establishes cooperation, but this bounded source set does not give the request, authorization and refusal procedure in a charter-threatening crisis.',control=('sovereign',None,'No universal command instrument follows from accession; specific estate requests, sanctions and fallback remain unprovided.','Dependable cooperation could suffice; preserve charters, appointments and Development Fund.','Estates have their own mandates and the Crown must not touch protected structures; response to breach needs specification.','Different offices and generations survive 1915; unwritten bargain tested and breaks in 1921 according to character summary.','Coordination, distribution restrictions, factional trust and integrity of statistics.'))
claim('C16','Treasury participates in Entente credit through syndicates','treasury','hasClaimOn','entente',(1914,1918),['P09','PA'],'Approved')
claim('C17','Private subscribers retain their own Entente claims and risk','investors','owns','entente',(1914,1932),['P09','PF'],'Approved')
claim('C18','Proposed 1918 halt to new syndicate issues is an action with an instrument gap','julian','haltsNewIssues','newissues',(1918,1918),['P09'],'Proposed',control=('sovereign',None,'The passage states that he stops new issues; it does not specify law, syndicate undertaking, collateral gate or a coordinating decision.','Treasury can withhold its own future money; private new issues require a distinct effective channel.','Private lenders retain claims, risk, overseas alternatives and potential refusal.','New issues at the proposed autumn 1918 decision; not confiscation of old claims.','Loss of credit income/orders; continued war before halt, food provision and allied bargaining.'))
claim('C19','Japanese banks retain short foreign obligations against long industrial assets','japan-banks','owes','shortfunding',(1917,1927),['P09','P10','PA'],'Approved')
claim('C20','Julian assembles authorized public/private rescue FX facility','julian','canMobilize','facility',(1927,1933),['P10','P11','PF'],'Approved',control=('sovereign','loanvote',None,'Treasury one-third, private lenders two-thirds; Japan guarantee and agency on-lending; draws as needed.','Private lenders must subscribe; Japanese banks and government retain domestic authority; no blanket confiscation.','Repayment schedule 1929-1933; commitment is not full drawing.','Public exposure, private risk, import buffer and potential losses; lending protects Pacifican creditors too.'))
claim('C21','Rescue loan and Ka Lōkahi endorsement do not authorize refused treaty','julian','hasAuthorityOver','common-policy',(1927,1927),['P11','PA'],'Approved',truth=False,control=('sovereign',None,'Senate refused treaty; provisional application is illegal in substance.','Political endorsement gives no substitute legal consent.','Senate refuses; Japan can lapse if Pacifica fails to secure consent.','1927 illegal interval before 1928 cure.','Domestic legitimacy and treaty-lapse risk.'))
claim('C22','1928 legal settlement permits bounded common executive action','julian','commands','common-policy',(1928,1932),['P11','PA'],'Approved',control=('concord','consent',None,'Two-thirds Senate consent and indemnity; three ministers with Japanese PM countersign; at least one Japanese.','Japan retains national government and home army except Concord war; western squadron reserved until renewal.','Five-year trust; quota and delegation review, audit, renewal required.','65% Pacifican common cost share; audit and divided delegation; rural distress under gold policy.'))
claim('C23','1932 consent extends common overseas command to 1937','julian','commands','overseas-command',(1932,1937),['P12'],'Approved',control=('concord','renewal',None,'Coup defeated through Emperor, navy and loyal Japanese units; ratification by both crowns and delegations.','Home army remains national except Concord war; Japan can refuse in 1937.','Renewal to 1937; no unlimited or permanent mandate.','Navy ministry bargain, shared costs, security exposure and partner domestic legitimacy.'))
claim('C24','Reserve Bank supplies gold and bank support through its institutional operations','reservebank','canMobilize','bank-resources',(1931,1932),['P12'],control=('reservebank',None,'Detailed mandate, liquidity authorization and Julian access procedure are not provided here.','Gold reserves and borrowing; recapitalization and restructuring instead of forced liquidation.','Bank and creditor holders retain claims; overseas debtors may stop paying.','Moratorium and restructuring are dated; indefinite gold support is not established.','Reserve depletion, credit losses, exports slump and Japan rural distress.'))
claim('C25','Proposed Union settlement exchanges rescue for cooperation while retaining Union sovereignty','union','cooperatesWith','concord',(1932,1932),['P13'],'Proposed')
claim('C26','Private firms retain management and competition despite Crown shares','private-firms','retains','management',(1887,1932),['P15'])
claim('C27','Crown does not own equity in private banking','crown','owns','bank-equity',(1887,1932),['P15'],truth=False)
claim('C28','Reserve Bank receives foreign concession gold through purchase against credit','reservebank','receives','purchased-gold',(1897,1932),['P15'])
claim('C29','Development Fund has a claim on every surplus','fund','hasClaimOn','surplus',(1887,1932),['P06'],'Approved')

# Alternative claims are analyst proposals; no authorial approval is implied.
claim('C30','Clarification preserves distinct public receipt, private wealth and debt claims','treasury','retains','cash',(1849,1932),['P02','P03'],'AuthorialNotApplicable','AnalystInference',case='C')
claim('C31','Candidate staged service could attract declared bullion through useful settlement','collection-service','establishes','assay-service',(1848,1852),['H1','H2','P02'],'Proposed','AnalystInference',case='S')
claim('C32','Candidate collection improvement remains unestimated','collection-service','receives','cash',(1849,1852),['H1','H2','PIN'],'Proposed','AnalystInference','Unknown',case='S',missing='No defensible policy-to-collection response, commissioning capacity, cost or avoidance elasticity in fixed source set.')
claim('C33','3% candidate creates a lower statutory entitlement','treasury','hasClaimOn','royalty3',(1849,1852),['P02','PD'],'Proposed','AnalystInference',case='R')
claim('C34','Accession clarification retains existing offices and independence','julian','holdsOffice','sovereign',(1915,1932),['P05','P06','P07'],'AuthorialNotApplicable','AnalystInference',case='AC')
claim('C35','Candidate new reciprocal crisis protocol could obtain specified coordinated action','julian','canMobilize','coordinated-response',(1915,1932),['P06','P09','P11'],'Proposed','AnalystInference','Unknown',case='AD',missing='No author-approved protocol or evidence of independent estate/syndicate acceptance; action and negotiated scope are candidates.',control=('sovereign','crisis-protocol',None,'Define triggering request, estate assents, new-issue perimeter, protected charters, reporting and financing in negotiation.','Estates, Senate, syndicates and counterparties retain specified consent/refusal; no universal cash sweep.','Time-limited crisis activation and review, rather than revived life delegation.','Negotiation costs, legitimacy concessions, reporting, creditor remedies and foregone discretion, all unestimated.'))

def quantity(id,label,case,sub,years,val,state,quantbasis,unit,accounting,passages,reason=None,kind='Flow',status='AuthorialNotApplicable'):
    # QuantityClaims are explicitly Claims: inference is disabled in validation.
    u=record(id,'Claim',label);add(u,RDF.type,PC.QuantityClaim);add(u,PC.subject,E[sub]);add(u,PC.predicate,PC.measures);add(u,PC.case,N[case]);lit(u,PC.period,f'{years[0]}–{years[1]}');lit(u,PC.startYear,years[0]);lit(u,PC.endYear,years[1]);add(u,PC.jurisdiction,E['california' if years[0]<1856 else 'realm']);add(u,PC.authorialStatus,V[status]);add(u,PC.claimBasis,V.ModelAssumption if quantbasis in ['InheritedParameter','InheritedResult'] else V.Calculation if val is not None else V.AnalystInference);add(u,PC.valueState,V[state]);add(u,PC.quantityKind,V[kind]);lit(u,PC.unit,unit);lit(u,PC.accountingBasis,accounting);add(u,PC.quantitativeBasis,V[quantbasis]);
    if val is None:lit(u,PC.missingReason,reason)
    else:add(u,PC.numericValue,Literal(Decimal(str(val)),datatype=XSD.decimal))
    for p in passages:add(u,PROV.wasDerivedFrom,N[p])
quantity('Q01','Inherited fixed gold output total, replayed','B','gold',(1849,1852),'237','Known','InheritedParameter','Period USD millions','Aggregate production value; not public receipts',['PIN','PD'],status='Model')
quantity('Q02','5% at 90% gross royalty replay','B','treasury',(1849,1852),'10.665','Known','IndependentlyChecked','Period USD millions','Fixed output gross before costs and further receipt adjustments',['PIN','PD','PCALC'])
quantity('Q03','3% at full collection gross royalty','R','treasury',(1849,1852),'7.110','Known','IndependentlyChecked','Period USD millions','Fixed output gross at hypothetical 100% collection; no behavioral prediction',['PD','PCALC'])
quantity('Q04','3% full capture gross shortfall','R','treasury',(1849,1852),'-3.555','Known','IndependentlyChecked','Period USD millions','Delta versus 5% at 90%; before all collection costs',['PD','PCALC'])
quantity('Q05','Maximum gross room from 90% to full collection at 5%','S','treasury',(1849,1852),'1.185','Known','ConditionalCalculation','Period USD millions','Conditional extra gross from ten-point capture gain, not a forecast',['PD','PCALC'])
quantity('Q06','Candidate staged service net receipts','S','treasury',(1849,1852),None,'Unmodeled','QuantitativeUnmodeled','Period USD millions','Net policy difference including costs, leakage and output response',['PD','PIN'],reason='Service cost, capture gain and output/avoidance response unavailable; not zero.')
quantity('Q07','Candidate 1932 mobilizable resource difference','S','julian',(1932,1932),None,'Unmodeled','QuantitativeUnmodeled','Period USD millions','Endpoint resource difference after obligations and transmission',['PD','PIN'],reason='No intermediate investment, institutional or endpoint rerun; no numerical power inference.')
quantity('Q08','Required capture at 3% fixed output','R','treasury',(1849,1852),'1.5','Known','IndependentlyChecked','Fraction of fixed taxable output','Required fraction to match 5% times 90%; infeasible above one',['PD','PCALC'],kind='Rate')
quantity('Q09','Inherited approximate public Japanese rescue drawing','B','treasury',(1927,1927),'165.620','Known','InheritedResult','Period USD millions','Public drawing only; 600 commitment and private 331.241 distinct',['PF','P10'],status='Model')
quantity('Q10','New coordination bargain net burden','AD','crown',(1915,1932),None,'Unmodeled','QuantitativeUnmodeled','Period USD millions','Negotiation, reporting, contingent claims and financing costs',['P06','P09','P11'],reason='Candidate legal/political terms and financing shares unapproved; costs unprovided.')

def link(id,label,fr,to,stage,relation,support,explanation,passages,case='B',conditions='Applicable offices, resources and dated conditions of the linked claims.',refusal='Independent institutions and counterparties retain the refusal points stated in linked claims.',burdens='Costs and obligations stated in linked claims; no automatic net gain.'):
    u=record(id,'MechanismLink',label)
    for c in fr:add(u,PC.fromClaim,N[c])
    for c in to:add(u,PC.toClaim,N[c])
    add(u,PC.case,N[case]);add(u,PC.stage,V[stage]);add(u,PC.relationKind,V[relation]);add(u,PC.narrativeSupport,V[support]);lit(u,PC.explanation,explanation);lit(u,PC.conditions,conditions);lit(u,PC.refusalTerms,refusal);lit(u,PC.burdens,burdens)
    for p in passages:add(u,PROV.wasDerivedFrom,N[p])

link('L01','Discovery to fiscal organization',['C01'],['C02'],'Creation','Enables','Asserted','Secrecy buys proposed diplomatic/administrative time; it does not show how dispersed gold is captured.',['P01','P02'])
link('L02','Entitlement to actual receipt',['C02','C05'],['C03'],'Creation','Enables','Missing','Mint and trade choke points plus useful coinage are named; capture fraction, enforcement coverage, leakage, timing and costs are not explained. Pledged receipts are not free cash.',['P02','P03','H1','H2'])
link('L03','Receipts to an administered treasury',['C03'],['C06'],'Creation','Enables','Explained','1852 convention vests collections, credit and works in an office; legislators still obstruct.',['P03'])
link('L04','Public procurement to reproducible capacity',['C06'],['C07'],'Accumulation','Enables','Explained','Paid trials, works, careers and private contracts create teams and repeat demand; costs and independent owners prevent total personal ownership.',['P03'])
link('L05','Productive constituency and lawful concentration',['C07'],['C08'],'Transmission','Enables','Explained','Dependence on grants and contracts supports a bargaining coalition, while constitutional amendment supplies the legal instrument. The network is neither a sufficient nor necessary cause of the law.',['P03','P04'])
link('L06','Life authority ends rather than being inherited',['C08'],['C09'],'Preservation','Constrains','Explained','Explicit lapse removes the enabling delegation while ordinary establishments survive.',['P04','P06'])
link('L07','Establishments survive through charters and balance',['C07','C09'],['C10','C11'],'Preservation','Preserves','Explained','Separate chartered capacities, Regent legitimacy and reciprocal restraint preserve institutions through the life-office interruption. Personnel details and proposed Truce/compact dates are not all approved.',['P05','P06'])
link('L08','Institutions and negotiated legitimacy transmit office',['C10','C11'],['C13','C14'],'Transmission','Transmits','Explained','Kiyoshi coalition fails; separate crown and legislative consents establish accession. Retained charter and Senate participation constrain the new sovereign.',['P07','P05'])
link('L09','Accession does not fully explain crisis compliance',['C13','C14','C12'],['C15'],'Transmission','Enables','Missing','Shared legitimacy and appointments can secure dependable cooperation, but no detailed instruction/refusal procedure covers a ruler threatening charter safeguards. Ownership of Crown shares is not ownership of estate resources.',['P06','P07','P08'])
link('L10','Mixed wartime lending to new-issue halt',['C16','C17'],['C18'],'Exercise','Enables','Asserted','Narrative states Julian stops private syndicate new issues. Treasury future lending is separable; the private coordination instrument is unspecified.',['P09'])
link('L11','Wartime gains also create later financial liabilities',['C16','C19'],['C20'],'Accumulation','Enables','Explained','Japanese long assets and short funding, peace, earthquake and lender nonrenewal create rescue dependence; friendship, naval risk and Pacifican claims jointly motivate offer. Early royalty is not established as its marginal cause.',['P09','P10'])
link('L12','Financial rescue is distinct from treaty consent',['C20'],['C21'],'Exercise','Constrains','Explained','Senate authorizes rescue loan but refuses treaty; endorsement by other crowns supplies political weight, no legal authority.',['P11'])
link('L13','A restraint preserves a lawful common executive',['C21'],['C22'],'Preservation','Preserves','Explained','1928 consent and indemnity with shorter term, audit and quota review cure illegality at cost of discretion.',['P11'])
link('L14','Renewal converts some partner command to common control',['C22'],['C23'],'Accumulation','Transmits','Explained','1932 renewal after loyal Japanese cooperation consolidates overseas command for a fixed term; domestic army and 1937 refusal remain national.',['P12'])
link('L15','Reserve support to Union bargaining',['C24'],['C25'],'Exercise','Enables','Asserted','Rescue helps obtain proposed association; Union chooses stability and privileges while remaining sovereign. Detailed acceptance mechanisms stay proposed; Reserve Bank assets are not Julian private wealth.',['P12','P13'])
link('L16','Share and surplus boundaries limit descendant mobilization',['C12','C26','C27','C29'],['C15'],'Transmission','Constrains','Explained','Sector-specific share interests do not confer firm management or bank equity; Fund claim on surplus constrains free resources. Distribution and crisis decision procedures remain separate gaps.',['P06','P15'])
link('L17','Foreign purchases widen reserves without creating ownership of foreign mines',['C28'],['C24'],'Preservation','Enables','Explained','Purchased foreign concession gold adds a reserve supply channel against credit. It is not a royalty on Pacifican territory, free gold, foreign GDP under Julian control or proof of the marginal contribution of 1849 receipts.',['P15','P12'])
link('L30','Staged service to greater declared collection',['C31'],['C32'],'Creation','Enables','Missing','Settlement usefulness is a historical analogy, not an estimated capture response; processing and remittance stages require capacity and cost.',['H1','H2','H4','PD'],case='S')
link('L31','Gross collection room to spendable service gain',['Q05','C32'],['Q06','Q07'],'Accumulation','Enables','Missing','No unconditional net gain or endpoint conclusion follows until costs, output and institutional transmission are supplied.',['PD','PIN'],case='S')
link('L32','Lower rate under a fixed-output accounting control',['C33'],['Q03','Q04','Q08'],'Creation','Constrains','Explained','At fixed 237m output, even full 3% capture falls below the inherited 5%/90% diagnostic. Does not establish behavioral or political response.',['PD','PCALC'],case='R')
link('L33','New bargain to negotiated crisis action',['C35'],['Q10'],'Transmission','Enables','Missing','Scope, assent, sanctions, financing and expiry require a new author decision and counterpart acceptance; no claim of current canonical existence.',['P06','P09','P11'],case='AD')

def evidence(id,target,p,relation,historical,boundary,group=None):
    u=record(id,'EvidenceApplication',f'{p} applied to {target}');add(u,PC.target,N[target]);add(u,PC.sourcePassage,N[p]);add(u,PC.evidenceRelation,V[relation]);add(u,PC.historicalSupport,V[historical]);lit(u,PC.applicability,boundary)
    if group:lit(u,PC.independenceGroup,group)
for i,(target,p) in enumerate([('C01','P01'),('C02','P02'),('C03','P02'),('C04','P02'),('C05','P01'),('C06','P03'),('C08','P04'),('C09','P04'),('C10','P05'),('C11','P06'),('C12','P06'),('C13','P07'),('C14','P05'),('C15','P06'),('C16','P09'),('C17','P09'),('C18','P09'),('C19','P10'),('C20','P10'),('C21','P11'),('C22','P11'),('C23','P12'),('C24','P12'),('C25','P13')],1):
    evidence(f'E{i:02}',target,p,'Supports','HistoricalNotApplicable','Authored fictional statement or bounded analytic extraction; local qualifications retained. Does not prove historical feasibility or supply omitted instrument.','current-master')
evidence('E30','L02','H1','Analogy','Analogous','Prior dossier reports Mint retrospective: local settlement reduces eastward shipping delays/risks; actual branch 1854. Cannot validate Pacifica 1850 staffing, costs or 90% capture.','Mint-history')
evidence('E31','C31','H1','Analogy','Analogous','Useful settlement is a candidate participation incentive; no collection elasticity or earlier commissioning proof.','Mint-history')
evidence('E32','L30','H2','Analogy','Analogous','Prior analyst retrieved text, page-image request failed; April 1854 supplies/parting-acid constraint demonstrates an operating risk, not a Pacifican schedule or output calibration. No OCR quantities used.','Mint-1855-report')
evidence('E33','C05','H3','Analogy','Analogous','1846 Mexican instrument has a coupon and pledged revenues. It neither proves counterfactual recognition/transfer nor applicable Pacifican maturity, arrears or due dates.','Payno-doc17')
evidence('E34','L30','H4','EvidenceUnavailable','Unavailable','Search snippet/full retrieval failure cannot establish Moffat operator, Treasury contract, public/private structure or local commissioning date.','Smithsonian-lead')
evidence('E35','L02','PH','Challenges','HistoricalNotApplicable','Historical background explicitly leaves claims, tribal territory and exact royalty system unsettled; inherited rules do not establish collection coverage. No fresh source retrieval.','project-history')
evidence('E36','C18','P09','Challenges','HistoricalNotApplicable','The approved mixed-ownership credit mechanism blocks counting all subscriber claims as Treasury assets; the halt is locally proposed and lacks the specific compliance channel.','current-master')
evidence('E37','Q02','PD','Supports','HistoricalNotApplicable','Arithmetic replay of supplied JSON with fixed output; parameters remain inherited and empirically unvalidated.','bounded-JSON-replay')
evidence('E38','C12','PR','Challenges','HistoricalNotApplicable','No Puʻuloa rent or estate total supplied; shares/land cannot be converted into a free cash balance or assigned zero.','project-finance-notes')
evidence('E39','C26','P15','Supports','HistoricalNotApplicable','Narrative distinguishes private management from sector-specific Crown equity and a golden share against foreign sale; no operational command inferred.','current-master')
evidence('E40','C27','P15','Supports','HistoricalNotApplicable','Explicit negative statement about Crown bank equity; Reserve Bank regulation is a distinct relation, not ownership.','current-master')
evidence('E41','C28','P15','Supports','HistoricalNotApplicable','Foreign concession gold reaches reserves by sale against credit; no foreign production or mine ownership added to domestic resources.','current-master')
evidence('E42','C29','P06','Supports','HistoricalNotApplicable','Development Fund claim on surplus and Crown commitment to protect it limit discretionary resources; amount and distribution procedure not quantified.','current-master')

def judgment(id,case,verdict,basis,dimensions,deps,explanation,sensitivity,conditional=True,against='B'):
    u=record(id,'Judgment',explanation.split('.')[0]);add(u,PC.comparesCase,N[case]);add(u,PC.againstCase,N[against]);add(u,PC.verdict,V[verdict]);add(u,PC.verdictBasis,V[basis]);
    for d in dimensions:add(u,PC.targetDimension,V[d])
    lit(u,PC.conditional,conditional);lit(u,PC.endpointYear,1932);lit(u,PC.explanation,explanation);lit(u,PC.sensitivity,sensitivity)
    for d in deps:add(u,PC.dependsOn,N[d])
    for p in ['P02','P06','P09','P11','PD']:add(u,PROV.wasDerivedFrom,N[p])
judgment('J01','C','Improves','ExplanatorySupport',['Explanation'],['L02','C04','C05','C06'],'Minimal clarification improves inspectability of collection and ownership but supplies no extra world power.','If clarification introduces new collection machinery or powers it becomes a world-change case.',False)
judgment('J02','S','Unresolved','WorldPower',['MobilizableResources','Implementation'],['C31','C32','L30','L31','Q05','Q06','Q07','L09'],'Staged assay/remittance service is a conditional development priority, not an established endpoint improvement.','Capture response, commissioning, enforcement/avoidance, cost and preservation through succession could reverse the case.')
judgment('J03','R','Weakens','FiscalDiagnostic',['GrossReceipts'],['Q02','Q03','Q04','Q08','L32'],'A 3% rate weakens gross receipts in the declared fixed-output control even at full collection.','Higher output, reduced costs or different baseline capture could reverse real net results; no such response is estimated.',False)
judgment('J04','R','Unresolved','WorldPower',['MobilizableResources','Leverage','FreedomToAct'],['Q04','C33','L09'],'The 3% alternative has no established 1932 power effect; better consent or output must be shown rather than assumed.','A defensible behavioral gain and complete transmission path could outweigh foregone gross revenue.')
judgment('J05','AC','Improves','ExplanatorySupport',['Explanation'],['L06','L08','L09','L10','C14','C18'],'Accession/crisis clarification is recommended now because it preserves valid offices and makes instrument gaps explicit.','A supposed clarification that creates an enforceable command bargain is substantive development.',False)
judgment('J06','AD','Unresolved','WorldPower',['Implementation','Leverage','FreedomToAct'],['C35','Q10','L33','L09','L10'],'A new reciprocal coordination bargain could make crisis action dependable but might reduce discretion or provoke refusal.','Estate legitimacy, Senate acceptance, investor alternatives, real cost and behavior after breach determine whether it helps.')
judgment('J07','B','Unresolved','WorldPower',['MobilizableResources','Implementation','Leverage','FreedomToAct'],['Q02','Q03','Q04','C06','C08','C09','C13','C15','C18','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','L02','L09','L10','L16','L17'],'Retaining baseline rather than adopting the 3% candidate preserves a larger gross fixed-output take and an authored path to bounded command; the relative net 1932 power effect is unmodeled.','Rate-driven output/participation gains, collection costs, estate/creditor refusal, succession breach, Japanese nonconsent or gold-support failure could reverse the preference.',against='R')

manifest={'review':'forward-gold-20261026','baseline_commit':BASE,'source_origin':'Matched local storyline/approval/identity/history/finance notes and inherited dossier/JSON; no new external retrieval.','files':files}
(OUT/'input-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
G.serialize(destination=OUT/'review.ttl',format='turtle')

def hash_file(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
skill_paths=['AGENTS.md','.agents/skills/aegis/SKILL.md','.agents/skills/aegis/references/success-contract.md','.agents/skills/aegis/references/ontology-workflow.md','.agents/skills/clio/SKILL.md','.agents/skills/chryseis/SKILL.md','.agents/skills/chryseis/references/quantity-methods.md']
profile_paths=['docs/power-review/ontology/'+p for p in ['README.md','ontology.ttl','vocabularies.ttl','shapes.ttl','queries.rq','validate.py']]
baseline_checks={}
for path in ['book-agent/revision/master_storyline.md','book-agent/revision/change_requests.json','book-agent/revision/character_registry.json','book-agent/revision/historical_background.md','finance/CR-031-review.md']:
    previous=subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT).replace(b'\r\n',b'\n')
    baseline_checks[path]=hashlib.sha256(previous).hexdigest()==files[path]['sha256']
run={'review_id':'forward-gold-20261026','evaluation_date':'2026-10-26','contract_version':'0.1.1','profile_version':'0.1.0','narrative_baseline_commit':BASE,'local_checkout_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'remote_ref_status':'No fresh remote lookup; explicitly a pinned local matched-source test.','baseline_source_hash_comparisons':baseline_checks,'source_manifest':'input-manifest.json','skills_exact_byte_hashes':{p:hash_file(p) for p in skill_paths},'profile_exact_byte_hashes':{p:hash_file(p) for p in profile_paths},'methods':['Separate assessment pass; no old review read','Dated case-scoped RDF propositions; independent authority/evidence/quantity schemes','Inherited historical dossier with retrieval limitations preserved','Decimal fixed-output 1849-1852 royalty calculation from supplied JSON only','Explicit --data/--manifest validation plus all five SPARQL views; no old graph merge'],'coverage':['1847-1852 creation and collection','1865 constitutional concentration','1887 expiry and independent estates','1914-1915 accession','1914-1918 mixed-owner finance and proposed halt','1927-1928 credit/consent/cure','1932 renewal and gold rescue','creation, preservation, transmission, exercise, accumulation','baseline, minimal clarification, staged service, 3% alternative, accession clarification, substantive bargain'],'exclusions':['No canon, skill or profile edits; no delegation by reviewer','No publish, commit, install or workbook read/recalculation','No new web retrieval or author source request; prior No preference checkpoint honored','No prior assessment, gold-review.ttl, test_ontology.py or earlier power-review outputs read','No century-long scenario outputs or marginal power score','README case-specific What the pilot demonstrates section skipped'],'independence_limits':'Independent reasoning pass by a separate agent; profile tailored around earlier needs and inherited evidence/finance conclusions constrain independence. Not a controlled benchmark.','record_counts':{k:len(set(G.subjects(RDF.type,PC[k]))) for k in ['Entity','Claim','QuantityClaim','MechanismLink','EvidenceApplication','ComparisonCase','Judgment','SourceDocument','SourcePassage']},'review_triples':len(G)}
(OUT/'run-manifest.json').write_text(json.dumps(run,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'triples':len(G),'counts':run['record_counts'],'baseline_hash_checks':baseline_checks},indent=2))
