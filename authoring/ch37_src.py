from lib import Chapter

POINTS = {
169: [
 "Heading RETINAL DETACHMENT; definition: separation of neurosensory retina from retinal pigment epithelium and collection of subretinal fluid",
 "Investigations: Indirect ophthalmoscopy: IOC",
 "Investigations: Optical coherence tomography (OCT); B-scan ultrasonography",
 "Figure Normal vs Retinal Detachment: NSR, subretinal space, RPE, fluid",
 "Types: Retinal detachment (RD) -> Primary/Rhegmatogenous RD; Secondary RD -> Tractional, Exudative",
 "Heading: Primary/Rhegmatogenous Retinal Detachment (RRD); Pathogenesis: Syneresis (liquefaction of vitreous) -> Posterior vitreous detachment (PVD)",
 "Pathogenesis: dynamic vitreoretinal traction from attached parts of vitreous",
 "Pathogenesis: retinal breaks develop -> fluid enters subretinal space",
 "Figure: retina, detached parts of retina, attached parts of retina, vitreoretinal traction",
 "Causes: pathological myopia (m/c)",
 "Causes: blunt trauma",
 "Causes: cataract surgery (aphakia)",
 "Causes: lattice degeneration of retina",
 "Symptoms: photophobia: flashes of light (stretching of nerve fibers -> ectopic neural impulses to brain)",
 "Symptoms: floaters: small black flying dots (d/t vitreal opacities)",
 "Symptoms: curtain falling in front of eye",
 "Symptoms: loss of vision: sudden & painless",
],
170: [
 "Signs 1: detached retina: gray/opaque, convex shaped",
 "Signs 2: extent of RD till ora serrata",
 "Signs 3: Shafer's sign - tobacco-dust appearance",
 "Shafer's sign d/t deposition of brown pigmented cells at the anterior surface of vitreous",
 "Eye diagram labels: RD, Shafer's sign",
 "Photograph caption: RD",
 "Photograph caption: U shaped retinal tear; m/c location: superotemporal quadrant",
 "OCT caption 'Longstanding RRD' labels: RD, subretinal fluid, intraretinal cysts",
 "Lincoff rules: rules to locate breaks in retina",
 "Signs 4: RAPD (relative afferent pupillary defect)",
 "Signs 5: in chronic RD - retinal atrophy",
 "Chronic RD: subretinal demarcation lines k/a high water marks (> 3 months)",
 "Chronic RD: intraretinal cysts (> 1 year)",
 "Management - Prophylaxis: laser photocoagulation to seal breaks (usually superotemporal quadrant)",
 "Treatment flowchart: mobile retina -> tamponade -> internal / external",
 "Internal 1. Pneumatic retinopexy: uses SF6 or C3F8 (propane)",
 "Pneumatic retinopexy: done in superior breaks",
 "Internal 2. Silicone oil: injected into vitreous cavity",
 "Silicone oil: removed after 8-12 weeks",
 "Silicone oil complication: hyperoleon -> oil leaks into anterior chamber and collects superiorly (inverse hypopyon)",
 "External tamponade: scleral buckling (scleral weight pushes RPE anteriorly)",
 "Immobile retina: in proliferative vitreo-retinopathy (causes membrane formation & scarring) -> vitrectomy + subretinal fluid drainage",
 "Note: Lincoff rules -> used to locate breaks in retina",
],
171: [
 "Heading: Secondary Retinal Detachment; table columns Tractional RD | Exudative RD",
 "Pathology - tractional: static vitreoretinal traction",
 "Pathology - exudative: exudation into subretinal space",
 "Etiology tractional: diabetic retinopathy (m/c)",
 "Etiology tractional: retinopathy of prematurity",
 "Etiology tractional: penetrating trauma",
 "Etiology tractional: sickle cell retinopathy (Roth spots (+): hemorrhage with clear centre) - circled",
 "Etiology exudative: choroidal melanoma (m/c)",
 "Etiology exudative: toxemia of pregnancy",
 "Etiology exudative: Coat's disease (idiopathic retinal telengiectasia)",
 "Etiology exudative: VKH syndrome",
 "Etiology exudative: central serous retinopathy",
 "Clinical features tractional: loss of vision: gradual & painless",
 "Tractional: shape of RD: concave",
 "Tractional: photopsia, floaters, extension of RD till ora serrata - bracket (-)",
 "Clinical features exudative: loss of vision: sudden, painless",
 "Exudative: shape of RD: convex",
 "Exudative: hallmark feature: shifting fluid (with shifting head position)",
 "Treatment (both): treat the cause",
],
}

c = Chapter(37, "Retinal Detachment", 169, 171, POINTS)

# ------------------------------------------------------------ p169
c.unit("Retinal detachment: definition, investigations, types and pathogenesis", "Retina",
       "RD definition neurosensory retina RPE subretinal fluid; indirect ophthalmoscopy IOC OCT B-scan; figure normal vs RD; primary rhegmatogenous vs secondary tractional exudative; pathogenesis syneresis PVD vitreoretinal traction retinal breaks.")
c.q(169, "fillup", "Retinal detachment is the separation of the neurosensory retina from the ___ with collection of subretinal fluid.",
    "Retinal pigment epithelium",
    ["Choroid", "Bruch's membrane", "Internal limiting membrane"],
    "RD: separation of neurosensory retina from retinal pigment epithelium and collection of subretinal fluid.",
    [1], "Definition")
c.q(169, "management", "Which investigation is the investigation of choice (IOC) for retinal detachment in the book?",
    "Indirect ophthalmoscopy",
    ["Optical coherence tomography", "B-scan ultrasonography", "Fundus fluorescein angiography"],
    "Investigations: Indirect ophthalmoscopy: IOC; also OCT and B-scan ultrasonography.",
    [2], "Investigations")
c.q(169, "oddoneout", "Which of the following is NOT listed among the investigations for retinal detachment?",
    "Fundus fluorescein angiography",
    ["Optical coherence tomography (OCT)", "B-scan ultrasonography", "Indirect ophthalmoscopy"],
    "Listed investigations: indirect ophthalmoscopy (IOC), OCT and B-scan ultrasonography.",
    [3], "Investigations")
c.q(169, "recall", "In the 'Normal' diagram beside the investigations, the labelled layers from top to bottom are:",
    "NSR, subretinal space, RPE",
    ["RPE, subretinal space, NSR", "NSR, RPE, subretinal space", "Subretinal space, NSR, RPE"],
    "Normal: NSR / Subretinal space / RPE. In the retinal detachment diagram the space is filled with Fluid between NSR and RPE.",
    [4], "Investigations")
c.q(169, "recall", "How does the book classify retinal detachment?",
    "Primary/Rhegmatogenous RD, and Secondary RD (tractional and exudative)",
    ["Primary RD (tractional), and Secondary RD (rhegmatogenous and exudative)",
     "Rhegmatogenous RD, tractional RD, and Secondary RD (exudative only)",
     "Primary/Rhegmatogenous RD (exudative), and Secondary RD (tractional)"],
    "Types: RD -> Primary/Rhegmatogenous RD; Secondary RD -> Tractional and Exudative.",
    [5], "Types")
c.q(169, "fillup", "The pathogenesis of rhegmatogenous RD begins with ___ (liquefaction of vitreous), followed by posterior vitreous detachment.",
    "Syneresis",
    ["Dynamic vitreoretinal traction", "Formation of retinal breaks", "Entry of fluid into the subretinal space"],
    "Pathogenesis: Syneresis (liquefaction of vitreous) -> posterior vitreous detachment (PVD).",
    [6], "Pathogenesis")
c.q(169, "recall", "Which sequence follows posterior vitreous detachment in the pathogenesis of RRD?",
    "Dynamic vitreoretinal traction from attached vitreous, retinal breaks develop, fluid enters subretinal space",
    ["Retinal breaks develop, dynamic vitreoretinal traction, fluid enters subretinal space",
     "Fluid enters subretinal space, retinal breaks develop, dynamic vitreoretinal traction",
     "Dynamic vitreoretinal traction, fluid enters subretinal space, retinal breaks develop"],
    "PVD -> dynamic vitreoretinal traction from attached parts of vitreous -> retinal breaks develop -> fluid enters subretinal space.",
    [7, 8], "Pathogenesis")
c.q(169, "recall", "The pathogenesis figure with arrows on the curved retina is labelled with:",
    "Retina, detached parts of retina, attached parts of retina and vitreoretinal traction",
    ["Retina, posterior vitreous face, subretinal fluid and vitreoretinal traction",
     "Retina, detached parts of retina, attached parts of retina and retinal break",
     "Neurosensory retina, RPE, attached parts of retina and vitreoretinal traction"],
    "Figure labels: Retina, Detached parts of retina, Attached parts of retina, Vitreoretinal traction.",
    [9], "Pathogenesis")

c.unit("RRD: causes and symptoms", "Retina",
       "RRD causes pathological myopia m/c blunt trauma cataract surgery aphakia lattice degeneration; symptoms flashes of light floaters curtain sudden painless loss.")
c.q(169, "recall", "What is the most common cause of rhegmatogenous retinal detachment?",
    "Pathological myopia",
    ["Lattice degeneration of retina", "Cataract surgery (aphakia)", "Blunt trauma"],
    "Causes: Pathological myopia (m/c), blunt trauma, cataract surgery (aphakia), lattice degeneration of retina.",
    [10], "RRD - causes")
c.q(169, "oddoneout", "All of the following are listed causes of primary/rhegmatogenous RD EXCEPT:",
    "Diabetic retinopathy",
    ["Blunt trauma", "Cataract surgery (aphakia)", "Lattice degeneration of retina"],
    "RRD causes: pathological myopia, blunt trauma, cataract surgery (aphakia), lattice degeneration. Diabetic retinopathy is the m/c cause of tractional RD (p171).",
    [11, 12, 13], "RRD - causes")
c.q(169, "fillup", "The book explains the 'flashes of light' of RRD (written as photophobia) by stretching of ___, which sends ectopic neural impulses to the brain.",
    "Nerve fibers",
    ["Vitreal opacities", "Retinal pigment epithelial cells", "Subretinal fluid layers"],
    "Photophobia: Flashes of light (Stretching of nerve fibers -> Ectopic neural impulses to brain).",
    [14], "RRD - symptoms")
c.q(169, "recall", "In RRD, small black flying dots (floaters) are due to:",
    "Vitreal opacities",
    ["Stretching of nerve fibers", "Membrane formation and scarring", "Shifting subretinal fluid"],
    "Floaters: Small black flying dots (d/t vitreal opacities).",
    [15], "RRD - symptoms")
c.q(169, "scenario", "A patient reports floaters and flashes, then a curtain falling in front of the eye with sudden, painless loss of vision. Which diagnosis fits the book's symptom list?",
    "Primary/rhegmatogenous retinal detachment",
    ["Tractional retinal detachment", "Coats' disease", "Eales' disease"],
    "RRD symptoms: flashes of light, floaters, curtain falling in front of eye, loss of vision sudden & painless.",
    [16, 17], "RRD - symptoms")

# ------------------------------------------------------------ p170
c.unit("RRD: signs", "Retina",
       "RRD signs gray opaque convex detached retina extent to ora serrata Shafer's sign tobacco-dust; U shaped tear superotemporal; OCT labels; Lincoff rules; RAPD; chronic RD retinal atrophy high water marks intraretinal cysts.")
c.q(170, "recall", "How is the detached retina described in RRD?",
    "Gray/opaque and convex shaped",
    ["Gray/opaque and concave shaped", "Red and convex shaped", "Pale and flat with cherry red spot"],
    "Signs: Detached retina: Gray/opaque, convex shaped. (Concave shape belongs to tractional RD, p171.)",
    [1], "RRD - signs")
c.q(170, "fillup", "In RRD the extent of the detachment goes up to the ___.",
    "Ora serrata",
    ["Optic disc", "Macula", "Equator"],
    "Signs: Extent of RD till ora serrata.",
    [2], "RRD - signs")
c.q(170, "scenario", "Slit-lamp examination of the anterior vitreous shows a tobacco-dust appearance in a patient with RD. Which sign is this?",
    "Shafer's sign",
    ["Salus sign", "Gunn sign", "Marcus Gunn sign"],
    "Signs 3: Shafer's sign - tobacco-dust appearance.",
    [3], "RRD - signs")
c.q(170, "fillup", "Shafer's sign is due to deposition of brown pigmented cells at the ___ surface of the vitreous.",
    "Anterior",
    ["Posterior", "Lateral", "Basal retinal"],
    "Shafer's sign: d/t deposition of brown pigmented cells at the anterior surface of vitreous.",
    [4], "RRD - signs")
c.q(170, "recall", "The eye diagram drawn beside the signs list is labelled with:",
    "RD and Shafer's sign",
    ["RD and Lincoff rules", "RD and high water marks", "Shafer's sign and intraretinal cysts"],
    "The eye diagram's labels: RD and Shafer's sign.",
    [5], "RRD - signs")
c.q(170, "recall", "Under the photograph captioned 'U shaped retinal tear', the book gives which m/c location?",
    "Superotemporal quadrant",
    ["Inferonasal quadrant", "Superonasal quadrant", "Inferotemporal quadrant"],
    "U shaped retinal tear - m/c location: Superotemporal quadrant. (The photograph before it is captioned RD.)",
    [6, 7], "RRD - signs")
c.q(170, "scenario", "An OCT scan captioned 'Longstanding RRD' is annotated with which features?",
    "RD, subretinal fluid and intraretinal cysts",
    ["RD, subretinal fluid and Shafer's sign", "RD, high water marks and intraretinal cysts", "Retinal breaks, subretinal fluid and RPE"],
    "OCT of longstanding RRD labels: RD, Subretinal fluid, Intraretinal cysts.",
    [8], "RRD - signs")
c.q(170, "recall", "What are Lincoff rules used for?",
    "To locate breaks in the retina",
    ["To decide the duration of silicone oil tamponade", "To grade proliferative vitreo-retinopathy", "To time prophylactic laser photocoagulation"],
    "Lincoff rules: Rules to locate breaks in retina (repeated in the note at the end of the page).",
    [9, 23], "RRD - signs")
c.q(170, "fillup", "Sign 4 of RRD in the book is ___ (relative afferent pupillary defect).",
    "RAPD",
    ["Argyll Robertson pupil", "Adie's pupil", "Relative efferent pupillary defect"],
    "Signs 4: RAPD (Relative afferent pupillary defect).",
    [10], "RRD - signs")
c.q(170, "fillup", "In chronic RD, subretinal demarcation lines known as 'high water marks' (and retinal atrophy) appear after more than ___.",
    "3 months",
    ["1 month", "6 months", "1 year"],
    "In chronic RD: retinal atrophy; subretinal demarcation lines K/a high water marks (> 3 months).",
    [11, 12], "RRD - chronic RD")
c.q(170, "numeric", "Intraretinal cysts appear in chronic RD after more than:",
    "1 year",
    ["3 months", "6 weeks", "5 years"],
    "Intraretinal cysts (> 1 year).",
    [13], "RRD - chronic RD")

c.unit("RRD: prophylaxis and treatment", "Retina",
       "RRD prophylaxis laser to seal breaks; mobile retina tamponade internal external; pneumatic retinopexy SF6 C3F8 superior breaks; silicone oil 8-12 weeks hyperoleon inverse hypopyon; scleral buckling; immobile retina PVR vitrectomy subretinal fluid drainage.")
c.q(170, "management", "What prophylaxis does the book give for retinal breaks?",
    "Laser photocoagulation to seal the breaks (usually superotemporal quadrant)",
    ["Pneumatic retinopexy with SF6 in the inferior quadrant", "Scleral buckling with silicone oil", "Vitrectomy with subretinal fluid drainage"],
    "Prophylaxis: Laser photocoagulation to seal breaks (usually superotemporal quadrant).",
    [14], "RRD - management")
c.q(170, "management", "In the treatment flowchart, a mobile retina is managed by:",
    "Tamponade, either internal or external",
    ["Vitrectomy plus subretinal fluid drainage", "Laser photocoagulation alone", "Treating the underlying cause only"],
    "Treatment: mobile retina -> Tamponade -> Internal / External. Immobile retina -> vitrectomy + subretinal fluid drainage.",
    [15], "RRD - management")
c.q(170, "fillup", "Pneumatic retinopexy uses ___ gas.",
    "SF6 or C3F8 (propane)",
    ["SF6 or CO2", "C3F8 or silicone oil", "Carbogen (95% O2 + 5% CO2)"],
    "Internal tamponade 1. Pneumatic retinopexy: uses SF6 or C3F8 (Propane).",
    [16], "RRD - management")
c.q(170, "management", "Pneumatic retinopexy is done for breaks in which location?",
    "Superior breaks",
    ["Inferior breaks", "Macular breaks only", "Breaks at the ora serrata only"],
    "Pneumatic retinopexy: Done in superior breaks.",
    [17], "RRD - management")
c.q(170, "recall", "Silicone oil tamponade is injected into the ___ and removed after ___.",
    "Vitreous cavity ; 8-12 weeks",
    ["Subretinal space ; 8-12 weeks", "Vitreous cavity ; 3 months", "Anterior chamber ; 1 year"],
    "Silicone oil: injected into vitreous cavity; removed after 8-12 weeks.",
    [18, 19], "RRD - management")
c.q(170, "scenario", "After silicone oil tamponade, oil leaks into the anterior chamber and collects superiorly, forming an inverse hypopyon. What is this complication called?",
    "Hyperoleon",
    ["Shafer's sign", "Hypopyon uveitis", "Proliferative vitreo-retinopathy"],
    "Silicone oil complication: Hyperoleon -> oil leaks into anterior chamber and collects superiorly (inverse hypopyon).",
    [20], "RRD - management")
c.q(170, "fillup", "In scleral buckling, the scleral weight pushes the ___ anteriorly.",
    "RPE",
    ["Neurosensory retina", "Vitreous base", "Silicone oil bubble"],
    "External tamponade: Scleral buckling (Scleral weight pushes RPE anteriorly).",
    [21], "RRD - management")
c.q(170, "scenario", "An RD has an immobile retina due to proliferative vitreo-retinopathy, which causes membrane formation and scarring. Which treatment does the flowchart give?",
    "Vitrectomy plus subretinal fluid drainage",
    ["Pneumatic retinopexy", "Scleral buckling alone", "Laser photocoagulation to seal breaks"],
    "Immobile retina: in proliferative vitreo-retinopathy (causes membrane formation & scarring) -> Vitrectomy + subretinal fluid drainage.",
    [22], "RRD - management")

# ------------------------------------------------------------ p171
c.unit("Secondary retinal detachment: tractional vs exudative", "Retina",
       "Tractional RD static vitreoretinal traction diabetic retinopathy m/c ROP penetrating trauma sickle cell Roth spots concave gradual; exudative RD subretinal exudation choroidal melanoma m/c toxemia Coat's VKH CSR sudden convex shifting fluid; treat the cause.")
c.q(171, "match", "Match the secondary RD with its pathology — 1) Tractional RD  2) Exudative RD  … A) Exudation into subretinal space  B) Static vitreoretinal traction  C) Dynamic vitreoretinal traction",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-C"],
    "Pathology: tractional RD - static vitreoretinal traction; exudative RD - exudation into subretinal space. (RRD has dynamic traction, p169.)",
    [1, 2, 3], "Secondary RD - pathology")
c.q(171, "recall", "What is the most common cause of tractional retinal detachment?",
    "Diabetic retinopathy",
    ["Retinopathy of prematurity", "Penetrating trauma", "Sickle cell retinopathy"],
    "Tractional RD etiology: Diabetic retinopathy (m/c), ROP, penetrating trauma, sickle cell retinopathy.",
    [4], "Tractional RD")
c.q(171, "oddoneout", "Which of the following is NOT listed as an etiology of tractional RD?",
    "VKH syndrome",
    ["Retinopathy of prematurity", "Penetrating trauma", "Sickle cell retinopathy"],
    "Tractional RD: DR (m/c), ROP, penetrating trauma, sickle cell retinopathy. VKH syndrome is listed under exudative RD.",
    [5, 6], "Tractional RD")
c.q(171, "scenario", "A tractional RD cause shows Roth spots, described as hemorrhage with clear centre. Which cause is this?",
    "Sickle cell retinopathy",
    ["Diabetic retinopathy", "Retinopathy of prematurity", "Penetrating trauma"],
    "Sickle cell retinopathy (Roth spots (+): Hemorrhage with clear centre).",
    [7], "Tractional RD")
c.q(171, "recall", "What is the most common cause of exudative RD?",
    "Choroidal melanoma",
    ["Toxemia of pregnancy", "Central serous retinopathy", "Diabetic retinopathy"],
    "Exudative RD etiology: Choroidal melanoma (m/c).",
    [8], "Exudative RD")
c.q(171, "scenario", "A woman with toxemia of pregnancy develops a retinal detachment. Which type of secondary RD does the book list it under?",
    "Exudative RD",
    ["Tractional RD", "Primary/rhegmatogenous RD", "Chronic RD with high water marks"],
    "Exudative RD etiology: choroidal melanoma (m/c), toxemia of pregnancy, Coat's disease, VKH syndrome, central serous retinopathy.",
    [9], "Exudative RD")
c.q(171, "oddoneout", "Which is NOT listed as an etiology of exudative RD?",
    "Retinopathy of prematurity",
    ["Coat's disease (idiopathic retinal telengiectasia)", "VKH syndrome", "Central serous retinopathy"],
    "Exudative RD: choroidal melanoma, toxemia of pregnancy, Coat's disease, VKH syndrome, central serous retinopathy. ROP is a tractional RD cause.",
    [10, 11, 12], "Exudative RD")
c.q(171, "scenario", "A patient has gradual, painless loss of vision and the detachment is concave in shape. Which secondary RD is this?",
    "Tractional RD",
    ["Exudative RD", "Primary/rhegmatogenous RD", "Retinopathy of prematurity stage 5"],
    "Tractional RD clinical features: loss of vision gradual & painless; shape of RD concave.",
    [13, 14], "Tractional RD")
c.q(171, "truefalse", "True or false — 'Tractional RD is characterised by photopsia, floaters and extension of RD up to the ora serrata.' Choose the correct verdict:",
    "False - the bracket marks all three as absent (-) in tractional RD",
    ["True - all three features are present in tractional RD",
     "False - only photopsia is absent, floaters and ora serrata extension are present",
     "True - they are present in tractional RD but absent in exudative RD"],
    "For tractional RD, photopsia, floaters and extension of RD till ora serrata are grouped by a bracket with (-).",
    [15], "Tractional RD")
c.q(171, "recall", "Which pair gives the loss of vision and shape of RD in exudative RD?",
    "Sudden, painless ; convex",
    ["Gradual, painless ; concave", "Sudden, painless ; concave", "Gradual, painless ; convex"],
    "Exudative RD: loss of vision sudden, painless; shape of RD convex.",
    [16, 17], "Exudative RD")
c.q(171, "scenario", "In a patient with exudative RD, the subretinal fluid moves when the head position is changed. What does the book call this feature?",
    "The hallmark feature: shifting fluid",
    ["Shafer's sign", "High water marks", "Hyperoleon"],
    "Exudative RD hallmark features: Shifting fluid (with shifting head position).",
    [18], "Exudative RD")
c.q(171, "management", "What is the treatment of secondary (tractional or exudative) RD in the table?",
    "Treat the cause",
    ["Pneumatic retinopexy", "Scleral buckling", "Silicone oil injection"],
    "Treatment (spanning both columns): Treat the cause.",
    [19], "Secondary RD - treatment")

covered = c.finish()
