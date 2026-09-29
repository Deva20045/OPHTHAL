from lib import Chapter

POINTS = {
164: [
 "Chapter title: RETINAL VASCULAR DISORDERS : PART 2; heading 'Hypertensive retinopathy'",
 "Phases: Vasoconstriction phase -> Sclerotic phase (Atherosclerosis) -> Exudative phase",
 "Sub-heading 'Clinical features' / 'Keith-Wagner classification' (table: Grade | Characteristics)",
 "Grade 1: Arteriolar attenuation; A:V (diameter) ratio = 1:3 (Normal 2:3)",
 "Grade 2: Salus sign - deflection of blood vessel",
 "Grade 3: Bonnet sign - banking of blood vessel",
 "Grade 3: Gunn sign - tapering of blood vessel",
 "Grade 3: Flame shaped hemorrhages with cotton wool spots",
 "Bracket beside Grades 2 and 3: signs are 'At AV crossings in veins'",
 "Grade 4: Copper wiring of arterioles",
 "Grade 4: Silver wiring of arterioles",
 "Grade 4: Papilledema",
 "Figure 'Grade 4 HTN retinopathy' labels: 1 Cotton wool spots; 2 Swelling of optic disc; 3 Exudates: macular star appearance: malignant HTN",
 "Figure 'Grade 3 Hypertensive retinopathy' labels: cotton wool spots, AV change, hemorrhages (flame shaped)",
],
165: [
 "Heading: Central Retinal Artery Occlusion (CRAO); CAUSES",
 "Cause: Atherosclerosis: m/c",
 "Cause: Emboli - Hollenhorst plaque: cholesterol emboli originating from bifurcation of CCA",
 "Cause: Giant cell arteritis",
 "Clinical feature: sudden, painless loss of vision",
 "Clinical feature: optic atrophy (Consecutive)",
 "Clinical feature: RAPD or Marcus Gunn pupil",
 "Fundus: pale fundus d/t retinal edema",
 "Fundus: cattle tracking fundus d/t segmentation of blood column",
 "Fundus: cherry red spot at macula d/t collection of fluid in ganglion cell layers (GCL) of retina except at foveola",
 "Figure caption: Cherry red spot (arrow at macula)",
 "Figure caption: CRAO with macular cilioretinal artery sparing",
 "Figure caption: Dye filling cilioretinal artery in FFA",
 "Note 'Cherry red spots at macula' - mnemonic: Cherry trees never grow tall in sand, mud & grime",
 "List item: CRAO",
 "List item: Trauma-blunt",
 "List item: Niemann Picks disease",
 "List item: Gangliosidosis Type 1",
 "List item: Tay Sachs disease (bracket: Gangliosidosis Type 2)",
 "List item: Sandhoffs disease (bracket: Gangliosidosis Type 2)",
 "List item: metachromatic leukodystrophy",
 "List item: Gaucher's disease: Type 2",
],
166: [
 "TREATMENT: Ocular emergency: Rx within 4 hrs",
 "24-48 hrs: Complete occlusion",
 "Ocular massage: dislodge emboli",
 "Vasodilatation - sublingual isosorbide nitrate",
 "Carbogen: 95% O2 + 5% CO2 -> hypercarbia -> raised PCO2 -> lowered pH -> vasodilatation (respiratory acidosis)",
 "Decrease IOP - IV mannitol",
 "Decrease IOP - paracentesis: aspiration of aqueous",
 "Rx of cause",
 "Heading: Central retinal vein occlusion (CRVO); m/c cause: hypertension",
 "1. Non-ischemic stage: d/t stasis of blood -> hypoxia; and raised vascular permeability -> macular edema -> loss of vision",
 "Rx: intravitreal triamcinolone",
 "Rx: 0.7 mg dexamethasone intravitreal implants (Geneva study)",
 "Rx: anti VEGF drugs",
 "2. Ischemic stage: severe hypoxia -> capillary endothelium damage",
 "Clinical feature: severe flame shaped hemorrhages",
 "Figure caption: Tomato ketchup/splash appearance",
 "Clinical feature: rubeosis iridis (neovascularisation of iris) d/t oxygen demand by posterior segment",
 "Blood leak into anterior chamber -> blocks trabecular meshwork -> neovascular glaucoma AKA 100 day glaucoma: glaucoma progression of 3 months in CRVO",
 "Rx: panretinal photocoagulation",
 "Note: m/c cause of neovascular glaucoma: diabetic retinopathy",
],
167: [
 "BRANCHED RETINAL VEIN OCCLUSION (BRVO): superior part of central retinal vein occluded",
 "BRVO: m/c site: AV crossings",
 "BRVO: m/c quadrant: superotemporal",
 "Figure caption: BRVO",
 "Heading: Retinopathy of prematurity (ROP) - occurs in: age at birth <= 32 weeks",
 "ROP occurs in: birth weight <= 1750 grams",
 "Age of screening table row 1: age at birth >= 28 wks, birth weight >= 1200 g -> 4 weeks after birth",
 "Age of screening table row 2: age at birth < 28 wks, birth weight < 1200 g -> 2-3 weeks after birth",
 "Stage 1: demarcating line between vascularized retina & peripheral avascular retina",
 "Stage 2: ridge formation at demarcating line",
 "Stage 3: extra retinal neovascularization on the ridge moving into vitreous",
 "Stage 4: partial retinal detachment (RD)",
 "Stage 5: total RD",
 "Figure captions: Stage 2 ROP; Stage 3 ROP",
],
168: [
 "Treatment: laser photocoagulation",
 "Indication: pre-threshold ROP type 1 (ETROP study)",
 "Zone 1 + any stage + plus disease (or)",
 "Zone 1 + stage 3 (or)",
 "Zone 2 + stage 2/3 + plus disease (or)",
 "Plus disease: venous tortuosity & dilatation in >= 2 quadrants",
 "Pars plana vitrectomy: if RD +",
 "Figure 'Zones of retina': nasal, temporal, clock hours (12/3/6/9), zone I, II, III, macula, optic nerve, ora serrata",
 "Heading: Miscellaneous",
 "EALES' DISEASE triangle: Occlusion; Periphlebitis; Neovascularisation of retina -> recurrent vitreous hemorrhage",
 "Eales' disease Rx: panretinal photocoagulation",
 "COATS' DISEASE: idiopathic retinal telengiectasia",
 "Coats': m > F",
 "Coats': unilateral",
 "Coats' clinical features: painless loss of vision",
 "Coats' clinical features: strabismus",
 "Coats' clinical features: leukocoria",
 "Coats' clinical features: exudative retinal detachment",
],
}

c = Chapter(36, "Retinal Vascular Disorders : Part 2", 164, 168, POINTS)

# ------------------------------------------------------------------ p164
c.unit("Hypertensive retinopathy: phases and Keith-Wagner grades", "Retina",
       "Hypertensive retinopathy phases vasoconstriction sclerotic exudative Keith-Wagner grades 1-4 A:V ratio Salus Bonnet Gunn signs flame hemorrhages cotton wool spots copper silver wiring papilledema macular star.")
c.q(164, "recall", "In hypertensive retinopathy, the book lists the phases in which order?",
    "Vasoconstriction phase, then sclerotic phase (atherosclerosis), then exudative phase",
    ["Sclerotic phase (atherosclerosis), then vasoconstriction phase, then exudative phase",
     "Vasoconstriction phase, then exudative phase, then sclerotic phase (atherosclerosis)",
     "Exudative phase, then sclerotic phase (atherosclerosis), then vasoconstriction phase"],
    "Hypertensive retinopathy runs Vasoconstriction phase -> Sclerotic phase (Atherosclerosis) -> Exudative phase.",
    [1, 2], "Hypertensive retinopathy")
c.q(164, "fillup", "Keith-Wagner grade 1 shows arteriolar attenuation, with an A:V (diameter) ratio of ___ (normal ___).",
    "1:3 ; normal 2:3",
    ["2:3 ; normal 1:3", "1:2 ; normal 3:4", "1:4 ; normal 1:2"],
    "Grade 1: arteriolar attenuation; A:V (diameter) ratio = 1:3, whereas normal is 2:3.",
    [3, 4], "Keith-Wagner classification")
c.q(164, "match", "Match each sign of the Keith-Wagner table with its meaning — 1) Salus sign  2) Bonnet sign  3) Gunn sign  … A) Tapering of blood vessel  B) Deflection of blood vessel  C) Banking of blood vessel",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Salus sign = deflection of blood vessel (grade 2); Bonnet sign = banking of blood vessel and Gunn sign = tapering of blood vessel (both grade 3).",
    [5, 6, 7], "Keith-Wagner classification")
c.q(164, "scenario", "A fundus examination in a hypertensive patient shows flame shaped hemorrhages together with cotton wool spots. Which Keith-Wagner grade does the book assign to this finding?",
    "Grade 3",
    ["Grade 2", "Grade 4", "Grade 1"],
    "Grade 3 in the Keith-Wagner table: Bonnet sign, Gunn sign and flame shaped hemorrhages with cotton wool spots.",
    [8], "Keith-Wagner classification")
c.q(164, "recall", "The bracket drawn beside grades 2 and 3 of the Keith-Wagner table states that the Salus, Bonnet and Gunn signs are seen:",
    "At AV crossings in veins",
    ["At the optic disc margin in arterioles", "Around the macula in capillaries", "Only in the peripheral retina in arteries"],
    "The bracket beside grades 2 and 3 reads 'At AV crossings in veins'.",
    [9], "Keith-Wagner classification")
c.q(164, "oddoneout", "Per the Keith-Wagner table, all of the following belong to grade 4 EXCEPT:",
    "Salus sign",
    ["Copper wiring of arterioles", "Silver wiring of arterioles", "Papilledema"],
    "Grade 4: copper wiring of arterioles, silver wiring of arterioles and papilledema. Salus sign belongs to grade 2.",
    [10, 11, 12], "Keith-Wagner classification")
c.q(164, "match", "In the 'Grade 4 HTN retinopathy' photograph, match arrow 1, 2 and 3 with the book's labels — A) Swelling of optic disc  B) Exudates: macular star appearance  C) Cotton wool spots",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Labels: 1 Cotton wool spots, 2 Swelling of optic disc, 3 Exudates: macular star appearance: malignant HTN.",
    [13], "Figures")
c.q(164, "truefalse", "True or false — 'In the grade 4 photograph, the exudates forming a macular star appearance indicate benign hypertension.' Choose the correct verdict:",
    "False - the book links the macular star exudates to malignant HTN",
    ["True - macular star exudates mark benign hypertension",
     "False - the macular star is a sign of cotton wool spots alone",
     "True - the macular star is the sign of papilledema alone"],
    "Label 3 in the grade 4 figure: Exudates: macular star appearance: malignant HTN.",
    [13], "Figures")
c.q(164, "recall", "The 'Grade 3 Hypertensive retinopathy' photograph is annotated with which set of labels?",
    "Cotton wool spots, AV change and hemorrhages (flame shaped)",
    ["Cotton wool spots, swelling of optic disc and exudates",
     "AV change, copper wiring and hemorrhages (flame shaped)",
     "Cotton wool spots, Salus sign and macular star"],
    "The grade 3 figure is labelled: cotton wool spots, AV change and hemorrhages (Flame shaped).",
    [14], "Figures")

# ------------------------------------------------------------------ p165
c.unit("CRAO: causes and clinical features", "Retina",
       "CRAO causes atherosclerosis m/c Hollenhorst plaque cholesterol emboli CCA giant cell arteritis; sudden painless loss consecutive optic atrophy RAPD Marcus Gunn pupil pale fundus cattle tracking cherry red spot cilioretinal sparing; cherry red spot mnemonic and list.")
c.q(165, "recall", "Which is the most common cause of central retinal artery occlusion according to the book?",
    "Atherosclerosis",
    ["Giant cell arteritis", "Hypertension", "Cholesterol emboli from a Hollenhorst plaque"],
    "CRAO causes: Atherosclerosis (m/c), emboli (Hollenhorst plaque) and giant cell arteritis. Hypertension is the m/c cause of CRVO (p166).",
    [1, 2], "CRAO - causes")
c.q(165, "fillup", "A Hollenhorst plaque consists of cholesterol emboli originating from the bifurcation of the ___.",
    "Common carotid artery (CCA)",
    ["Internal carotid artery siphon", "Aortic arch", "Ophthalmic artery"],
    "Emboli: Hollenhorst plaque - cholesterol emboli originating from bifurcation of CCA.",
    [3], "CRAO - causes")
c.q(165, "oddoneout", "All of the following are listed as causes of CRAO in the book EXCEPT:",
    "Hypertension",
    ["Atherosclerosis", "Emboli", "Giant cell arteritis"],
    "The listed causes of CRAO are atherosclerosis (m/c), emboli (Hollenhorst plaque) and giant cell arteritis. Hypertension is the m/c cause of CRVO.",
    [4], "CRAO - causes")
c.q(165, "scenario", "A patient reports sudden, painless loss of vision in one eye from CRAO. Which type of optic atrophy does the book say follows?",
    "Consecutive optic atrophy",
    ["Primary optic atrophy", "Secondary optic atrophy", "Glaucomatous optic atrophy"],
    "Clinical features of CRAO: sudden, painless loss of vision; optic atrophy (Consecutive).",
    [5, 6], "CRAO - clinical features")
c.q(165, "fillup", "In CRAO, RAPD is also called the ___ pupil.",
    "Marcus Gunn",
    ["Argyll Robertson", "Adie's tonic", "Hutchinson"],
    "Clinical features: RAPD or Marcus Gunn pupil.",
    [7], "CRAO - clinical features")
c.q(165, "match", "Match the fundus appearance in CRAO with its cause — 1) Pale fundus  2) Cattle tracking fundus  3) Cherry red spot at macula  … A) Segmentation of blood column  B) Retinal edema  C) Collection of fluid in ganglion cell layers except at foveola",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "Pale fundus d/t retinal edema; cattle tracking fundus d/t segmentation of blood column; cherry red spot at macula d/t collection of fluid in the GCL of retina except at foveola.",
    [8, 9, 10], "CRAO - clinical features")
c.q(165, "fillup", "The fundus photograph placed beside the CRAO clinical features carries the caption '___', with an arrow pointing at the macular spot.",
    "Cherry red spot",
    ["Cattle tracking", "Tomato ketchup/splash appearance", "Macular star"],
    "Figure caption: Cherry red spot. ('Tomato ketchup/splash appearance' is the CRVO figure on p166.)",
    [11], "CRAO - figures")
c.q(165, "scenario", "A CRAO fundus photograph shows the macula spared, and the fluorescein angiogram shows dye filling one arterial channel. Which vessel do the book's captions name?",
    "Cilioretinal artery",
    ["Central retinal vein", "Long posterior ciliary artery", "Superior temporal branch of the central retinal artery"],
    "Captions: 'CRAO with macular cilioretinal artery sparing' and 'Dye filling cilioretinal artery in FFA'.",
    [12, 13], "CRAO - figures")
c.q(165, "recall", "'Cherry trees never grow tall in sand, mud & grime' is the book's mnemonic for the causes of:",
    "Cherry red spot at macula",
    ["Cattle tracking fundus", "Consecutive optic atrophy", "Tomato ketchup appearance of the fundus"],
    "Note: Cherry red spots at macula - mnemonic: Cherry trees never grow tall in sand, mud & grime.",
    [14], "Cherry red spot - mnemonic")
c.q(165, "oddoneout", "Which of the following is NOT among the conditions the book lists for cherry red spot at macula?",
    "Eales' disease",
    ["Blunt trauma", "Niemann Picks disease", "CRAO"],
    "The list begins CRAO, Trauma-blunt, Niemann Picks disease ... Eales' disease is a separate condition (p168).",
    [15, 16, 17], "Cherry red spot - list")
c.q(165, "recall", "In the book's cherry red spot list, which gangliosidosis is written on its own line, NOT bracketed with Tay Sachs and Sandhoffs disease?",
    "Gangliosidosis Type 1",
    ["Gangliosidosis Type 2", "Gangliosidosis Type 3", "Gaucher's disease Type 1"],
    "The list gives Gangliosidosis Type 1 separately; Tay Sachs and Sandhoffs disease are bracketed together as Gangliosidosis Type 2.",
    [18], "Cherry red spot - list")
c.q(165, "fillup", "Tay Sachs disease and Sandhoffs disease are bracketed in the cherry red spot list as Gangliosidosis Type ___.",
    "2",
    ["1", "3", "4"],
    "Tay Sachs disease and Sandhoffs disease are bracketed together as Gangliosidosis Type 2.",
    [19, 20], "Cherry red spot - list")
c.q(165, "truefalse", "True or false — 'Any type of Gaucher's disease is listed for cherry red spot at macula.' Choose the correct verdict:",
    "False - the book lists Gaucher's disease: Type 2 (after metachromatic leukodystrophy)",
    ["True - the list names Gaucher's disease without specifying a type",
     "False - the book lists Gaucher's disease: Type 1",
     "False - Gaucher's disease is bracketed with Tay Sachs disease as Type 2 gangliosidosis"],
    "The list ends with metachromatic leukodystrophy and Gaucher's disease: Type 2.",
    [21, 22], "Cherry red spot - list")

# ------------------------------------------------------------------ p166 (CRAO treatment)
c.unit("CRAO treatment", "Retina",
       "CRAO ocular emergency Rx within 4 hrs; 24-48 hrs complete occlusion; ocular massage; sublingual isosorbide nitrate; carbogen 95% O2 + 5% CO2 respiratory acidosis; IV mannitol; paracentesis; Rx of cause.")
c.q(166, "management", "How quickly must treatment be started for CRAO, which the book calls an ocular emergency?",
    "Within 4 hrs",
    ["Within 24 hrs", "Within 48 hrs", "Within 1 week"],
    "TREATMENT: Ocular emergency: Rx within 4 hrs.",
    [1], "CRAO - treatment")
c.q(166, "numeric", "After how long does the book say CRAO becomes complete occlusion?",
    "24-48 hrs",
    ["4 hrs", "1-2 hrs", "72-96 hrs"],
    "24-48 hrs: Complete occlusion.",
    [2], "CRAO - treatment")
c.q(166, "recall", "What is the purpose of ocular massage in CRAO?",
    "To dislodge emboli",
    ["To lower IOP by aspirating aqueous", "To cause vasodilatation through hypercarbia", "To treat the underlying cause"],
    "Ocular massage: Dislodge emboli.",
    [3], "CRAO - treatment")
c.q(166, "fillup", "For vasodilatation in CRAO, the book lists sublingual ___.",
    "Isosorbide nitrate",
    ["Mannitol", "Triamcinolone", "Dexamethasone"],
    "Vasodilatation - sublingual isosorbide nitrate.",
    [4], "CRAO - treatment")
c.q(166, "numeric", "Carbogen, used for vasodilatation in CRAO, is a mixture of:",
    "95% O2 + 5% CO2",
    ["5% O2 + 95% CO2", "50% O2 + 50% CO2", "100% O2"],
    "Carbogen: 95% O2 + 5% CO2 -> hypercarbia -> raised PCO2 -> lowered pH -> vasodilatation.",
    [5], "CRAO - treatment")
c.q(166, "truefalse", "True or false — 'Carbogen causes vasodilatation through respiratory alkalosis with a raised pH.' Choose the correct verdict:",
    "False - hypercarbia raises PCO2 and lowers pH (respiratory acidosis), which causes vasodilatation",
    ["True - hypercarbia lowers PCO2 and raises pH",
     "False - carbogen acts by lowering PCO2 and lowering pH",
     "True - respiratory alkalosis with raised pH causes the vasodilatation"],
    "The book's chain: Hypercarbia -> raised PCO2 -> lowered pH -> vasodilatation, labelled respiratory acidosis.",
    [5], "CRAO - treatment")
c.q(166, "management", "To lower IOP in CRAO, the book lists IV mannitol and:",
    "Paracentesis - aspiration of aqueous",
    ["Ocular massage to dislodge emboli", "Sublingual isosorbide nitrate", "Carbogen inhalation"],
    "Decrease IOP: IV mannitol and paracentesis (aspiration of aqueous).",
    [6, 7], "CRAO - treatment")
c.q(166, "management", "After massage, vasodilators and IOP lowering, what is the last item in the book's CRAO treatment list?",
    "Rx of cause",
    ["Panretinal photocoagulation", "Pars plana vitrectomy", "Intravitreal triamcinolone"],
    "The CRAO treatment list ends with 'Rx of cause'.",
    [8], "CRAO - treatment")

# ------------------------------------------------------------------ p166 (CRVO)
c.unit("Central retinal vein occlusion (CRVO)", "Retina",
       "CRVO m/c cause hypertension; non-ischemic stage stasis hypoxia macular edema Rx triamcinolone 0.7 mg dexamethasone implant Geneva anti VEGF; ischemic stage flame hemorrhages tomato ketchup rubeosis iridis neovascular glaucoma 100 day glaucoma PRP; m/c cause of NVG diabetic retinopathy.")
c.q(166, "recall", "What is the most common cause of central retinal vein occlusion per the book?",
    "Hypertension",
    ["Atherosclerosis", "Diabetic retinopathy", "Giant cell arteritis"],
    "Central retinal vein occlusion (CRVO): m/c cause: Hypertension.",
    [9], "CRVO")
c.q(166, "fillup", "In the non-ischemic stage of CRVO, stasis of blood causes hypoxia and raised vascular permeability, leading to ___ and loss of vision.",
    "Macular edema",
    ["Rubeosis iridis", "Neovascular glaucoma", "Capillary endothelium damage"],
    "Non-ischemic stage: d/t stasis of blood -> hypoxia and raised vascular permeability -> macular edema -> loss of vision.",
    [10], "CRVO - non-ischemic stage")
c.q(166, "oddoneout", "Which is NOT listed as treatment for the non-ischemic stage of CRVO with macular edema?",
    "Panretinal photocoagulation",
    ["Intravitreal triamcinolone", "Dexamethasone intravitreal implant", "Anti VEGF drugs"],
    "Non-ischemic Rx: intravitreal triamcinolone, 0.7 mg dexamethasone intravitreal implants and anti VEGF drugs. Panretinal photocoagulation is listed for the ischemic stage's neovascular glaucoma.",
    [11, 12, 13], "CRVO - non-ischemic stage")
c.q(166, "numeric", "The dexamethasone intravitreal implant of the Geneva study is given in a dose of:",
    "0.7 mg",
    ["0.07 mg", "7 mg", "1.5 mg"],
    "Rx: 0.7 mg dexamethasone intravitreal implants (Geneva study).",
    [12], "CRVO - non-ischemic stage")
c.q(166, "fillup", "The ischemic stage of CRVO arises from severe hypoxia causing damage to the ___.",
    "Capillary endothelium",
    ["Ganglion cell layer", "Trabecular meshwork", "Foveola"],
    "Ischemic stage: Severe hypoxia -> Capillary endothelium damage.",
    [14], "CRVO - ischemic stage")
c.q(166, "scenario", "A fundus shows severe flame shaped hemorrhages that give a 'tomato ketchup/splash appearance'. Which stage of CRVO is this in the book?",
    "Ischemic stage",
    ["Non-ischemic stage", "Grade 3 hypertensive retinopathy stage", "Cattle tracking stage"],
    "Ischemic stage clinical features: severe flame shaped hemorrhages; figure caption Tomato ketchup/splash appearance.",
    [15, 16], "CRVO - ischemic stage")
c.q(166, "fillup", "Rubeosis iridis (neovascularisation of iris) in ischemic CRVO is due to the oxygen demand by the ___.",
    "Posterior segment",
    ["Anterior chamber", "Trabecular meshwork", "Cornea"],
    "Rubeosis iridis (Neovascularisation of iris) d/t oxygen demand by posterior segment.",
    [17], "CRVO - ischemic stage")
c.q(166, "scenario", "In ischemic CRVO, blood leaks into the anterior chamber and blocks the trabecular meshwork. Which glaucoma results, and by what other name is it known?",
    "Neovascular glaucoma, also called 100 day glaucoma",
    ["Neovascular glaucoma, also called 90 day glaucoma", "Angle-closure glaucoma, also called 100 day glaucoma", "Neovascular glaucoma, also called cattle tracking glaucoma"],
    "Blood leak into AC -> blocks trabecular meshwork -> neovascular glaucoma: AKA 100 day glaucoma.",
    [18], "CRVO - ischemic stage")
c.q(166, "numeric", "The '100 day glaucoma' name refers to glaucoma progression of ___ in CRVO.",
    "3 months",
    ["1 month", "6 months", "100 weeks"],
    "100 day glaucoma: Glaucoma progression of 3 months in CRVO.",
    [18], "CRVO - ischemic stage")
c.q(166, "management", "Which treatment does the book give for the neovascular changes of ischemic CRVO?",
    "Panretinal photocoagulation",
    ["Intravitreal triamcinolone", "Paracentesis", "Pars plana vitrectomy"],
    "Rx: Panretinal photocoagulation.",
    [19], "CRVO - ischemic stage")
c.q(166, "recall", "What is the most common cause of neovascular glaucoma, per the book's note?",
    "Diabetic retinopathy",
    ["CRVO", "Retinopathy of prematurity", "CRAO"],
    "Note: m/c cause of neovascular glaucoma: Diabetic retinopathy.",
    [20], "CRVO - ischemic stage")

# ------------------------------------------------------------------ p167
c.unit("BRVO and retinopathy of prematurity (screening and stages)", "Retina",
       "BRVO superior part of central retinal vein AV crossings superotemporal; ROP age at birth <=32 weeks weight <=1750 g; screening table 28 weeks 1200 g; stages 1-5 demarcating line ridge extraretinal neovascularization partial and total RD.")
c.q(167, "fillup", "In branched retinal vein occlusion, the ___ part of the central retinal vein is occluded.",
    "Superior",
    ["Inferior", "Nasal", "Temporal"],
    "BRVO: Superior part of central retinal vein occluded.",
    [1], "BRVO")
c.q(167, "match", "Match the BRVO feature with its m/c location — 1) m/c site  2) m/c quadrant  … A) Superotemporal  B) AV crossings  C) Optic disc margin  D) Inferonasal",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-D"],
    "BRVO: m/c site: AV crossings; m/c quadrant: superotemporal.",
    [2, 3], "BRVO")
c.q(167, "recall", "The fundus photograph placed beside the BRVO description is captioned:",
    "BRVO",
    ["CRVO", "CRAO", "Coats' disease"],
    "Figure caption: BRVO.",
    [4], "BRVO")
c.q(167, "numeric", "Per the book, retinopathy of prematurity occurs in infants with an age at birth of:",
    "32 weeks or less",
    ["28 weeks or less", "36 weeks or less", "40 weeks or less"],
    "ROP occurs in: age at birth <= 32 weeks.",
    [5], "ROP")
c.q(167, "numeric", "Per the book, retinopathy of prematurity occurs in infants with a birth weight of:",
    "1750 grams or less",
    ["1200 grams or less", "2500 grams or less", "1500 grams or less"],
    "ROP occurs in: birth weight <= 1750 grams.",
    [6], "ROP")
c.q(167, "scenario", "A baby born at 30 weeks weighing 1500 g is at risk of ROP. When does the book's screening table say to screen?",
    "4 weeks after birth",
    ["2-3 weeks after birth", "At birth", "8 weeks after birth"],
    "Age at birth >= 28 wks and birth weight >= 1200 g: screen 4 weeks after birth.",
    [7], "ROP - screening")
c.q(167, "scenario", "A baby born at 26 weeks weighing 1000 g needs ROP screening. According to the table, screening should be done:",
    "2-3 weeks after birth",
    ["4 weeks after birth", "1 week after birth", "6 weeks after birth"],
    "Age at birth < 28 wks and birth weight < 1200 g: screen 2-3 weeks after birth.",
    [8], "ROP - screening")
c.q(167, "match", "Match the ROP stage with its feature — 1) Stage 1  2) Stage 2  … A) Ridge formation at demarcating line  B) Demarcating line between vascularized retina & peripheral avascular retina  C) Partial RD  D) Total RD",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-C", "1-C, 2-A"],
    "Stage 1: demarcating line between vascularized retina & peripheral avascular retina. Stage 2: ridge formation at demarcating line.",
    [9, 10], "ROP - stages")
c.q(167, "recall", "Which ROP stage shows extra retinal neovascularization on the ridge moving into the vitreous?",
    "Stage 3",
    ["Stage 2", "Stage 4", "Stage 1"],
    "Stage 3: Extra retinal neovascularization on the ridge moving into vitreous.",
    [11], "ROP - stages")
c.q(167, "match", "Match the ROP stages with their retinal detachment status — 1) Stage 4  2) Stage 5  … A) Total RD  B) Partial RD  C) Ridge formation  D) Demarcating line",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-D"],
    "Stage 4: partial retinal detachment (RD). Stage 5: total RD.",
    [12, 13], "ROP - stages")
c.q(167, "recall", "The two ROP fundus photographs at the foot of the page are captioned:",
    "Stage 2 ROP and Stage 3 ROP",
    ["Stage 1 ROP and Stage 2 ROP", "Stage 3 ROP and Stage 4 ROP", "Stage 4 ROP and Stage 5 ROP"],
    "Figure captions: Stage 2 ROP and Stage 3 ROP.",
    [14], "ROP - stages")

# ------------------------------------------------------------------ p168
c.unit("ROP treatment, Eales' disease and Coats' disease", "Retina",
       "ROP laser photocoagulation pre-threshold type 1 ETROP zone 1 zone 2 plus disease >=2 quadrants pars plana vitrectomy if RD; zones of retina figure; Miscellaneous: Eales' disease triangle PRP; Coats' disease telengiectasia M>F unilateral painless loss strabismus leukocoria exudative RD.")
c.q(168, "management", "Laser photocoagulation in ROP is indicated in which category, per the ETROP study?",
    "Pre-threshold ROP type 1",
    ["Stage 1 ROP", "Threshold stage 5 ROP", "Pre-threshold ROP type 2"],
    "Laser photocoagulation - Indication: Pre-threshold ROP type 1 (ETROP study).",
    [1, 2], "ROP - treatment")
c.q(168, "fillup", "One indication for laser in ROP is Zone 1 + ___ + plus disease.",
    "Any stage",
    ["Stage 3 only", "Stage 2/3 only", "Stage 1 only"],
    "Zone 1 + any stage + plus disease (or). Stage 2/3 with plus disease is the Zone 2 criterion.",
    [3], "ROP - treatment")
c.q(168, "oddoneout", "Which combination is NOT among the book's laser indications for pre-threshold ROP type 1?",
    "Zone 2 + stage 1 without plus disease",
    ["Zone 1 + stage 3", "Zone 2 + stage 2/3 + plus disease", "Zone 1 + stage 2 + plus disease"],
    "Listed indications: Zone 1 + any stage + plus disease; Zone 1 + stage 3; Zone 2 + stage 2/3 + plus disease.",
    [4, 5], "ROP - treatment")
c.q(168, "numeric", "Plus disease in ROP means venous tortuosity and dilatation in at least how many quadrants?",
    "2 quadrants",
    ["1 quadrant", "3 quadrants", "4 quadrants"],
    "Plus disease: Venous tortuosity & dilatation in >= 2 quadrants.",
    [6], "ROP - treatment")
c.q(168, "management", "An ROP eye has retinal detachment. What additional procedure does the book list?",
    "Pars plana vitrectomy",
    ["Laser photocoagulation alone", "Panretinal photocoagulation", "Paracentesis"],
    "Pars plana vitrectomy: If RD +.",
    [7], "ROP - treatment")
c.q(168, "recall", "Which set of labels appears on the 'Zones of retina' diagram?",
    "Zones I, II and III, macula, optic nerve, ora serrata, clock hours, nasal and temporal",
    ["Zones I, II and III, fovea, optic nerve, vortex veins, clock hours, nasal and temporal",
     "Zones I and II, macula, optic nerve, ora serrata, clock hours, superior and inferior",
     "Zones I, II and III, macula, cilioretinal artery, ora serrata, superior and inferior"],
    "The zones of retina figure labels Nasal, Temporal, Clock hours, Zone I, Zone II, Zone III, Macula, Optic Nerve and Ora serrata.",
    [8], "ROP - figure")
c.q(168, "recall", "Under 'Miscellaneous', which disease does the triangle of Occlusion, Periphlebitis and Neovascularisation of retina leading to recurrent vitreous hemorrhage represent?",
    "Eales' disease",
    ["Coats' disease", "Retinopathy of prematurity", "Branched retinal vein occlusion"],
    "Miscellaneous - EALES' DISEASE: Occlusion, Periphlebitis, Neovascularisation of retina -> Recurrent vitreous hemorrhage.",
    [9, 10], "Eales' disease")
c.q(168, "management", "Which treatment does the book give for Eales' disease?",
    "Panretinal photocoagulation",
    ["Pars plana vitrectomy", "Intravitreal triamcinolone", "Paracentesis"],
    "Eales' disease Rx: Panretinal photocoagulation.",
    [11], "Eales' disease")
c.q(168, "fillup", "Coats' disease is idiopathic retinal ___.",
    "Telengiectasia",
    ["Neovascularisation", "Periphlebitis", "Detachment"],
    "COATS' DISEASE: Idiopathic retinal telengiectasia.",
    [12], "Coats' disease")
c.q(168, "recall", "Which pair correctly describes Coats' disease?",
    "Male predominance and unilateral",
    ["Female predominance and unilateral", "Male predominance and bilateral", "Female predominance and bilateral"],
    "Coats' disease: M > F; unilateral.",
    [13, 14], "Coats' disease")
c.q(168, "oddoneout", "All of the following are clinical features of Coats' disease in the book EXCEPT:",
    "Papilledema",
    ["Painless loss of vision", "Strabismus", "Leukocoria"],
    "Coats' clinical features: painless loss of vision, strabismus, leukocoria, exudative retinal detachment. Papilledema is a grade 4 hypertensive retinopathy sign.",
    [15, 16, 17], "Coats' disease")
c.q(168, "scenario", "A child with Coats' disease is found to have a retinal detachment. What type of detachment does the book list among its clinical features?",
    "Exudative retinal detachment",
    ["Partial detachment with a ridge at a demarcating line", "Total detachment as stage 5", "Detachment of the vitreous with recurrent hemorrhage"],
    "Coats' clinical features: exudative retinal detachment.",
    [18], "Coats' disease")

covered = c.finish()
