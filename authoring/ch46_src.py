from lib import Chapter

# Transcribed from printed Book pp. 215-219; includes tear-flow diagrams and test algorithms.
POINTS = {
215: [
 "Chapter title: Lacrimal apparatus: anatomy, watering eye and dry eye; tears have secretion and drainage pathways",
 "Main lacrimal gland is divided by levator palpebrae superioris",
 "Orbital part of lacrimal gland is superior; palpebral part is inferior",
 "Main lacrimal gland has main excretory ducts; function is reflex tear secretion",
 "Accessory lacrimal glands of Krause and Wolfring lie in fornix between sclera and palpebral conjunctiva",
 "Krause and Wolfring accessory glands provide basal tear secretion",
 "Parasympathetic lacrimal secretomotor centre: superior salivatory nucleus in pons",
 "Preganglionic parasympathetic pathway: greater superficial petrosal nerve, branch of facial nerve",
 "Parasympathetic pathway synapses in pterygopalatine ganglion",
 "Postganglionic pathway: zygomatic nerve, branch of maxillary division of trigeminal, stimulates lacrimal gland secretion",
 "Sympathetic innervation of lacrimal gland has inhibitory function",
 "Lacrimal apparatus figure labels main gland, orbital part, palpebral part, excretory ducts and drainage structures",
],
216: [
 "Drainage: upper and lower puncta lead to upper and lower canaliculi, then lacrimal sac",
 "Lacrimal sac is surrounded by orbicularis oculi; blinking assists drainage",
 "Nasolacrimal duct opens into inferior meatus of nose",
 "Opening of nasolacrimal duct is guarded by valve of Hasner; commonest congenital dacryocystitis block",
 "Watering eye from hyperlacrimation: increased tear secretion due to emotional stress or inflammation",
 "Epiphora is watering due to blockage of tear drainage",
 "Testing watering eye instruments: Nettleship punctum dilator, 26-gauge bent needle cannula and Bowman's lacrimal probe",
 "Syringing: after punctal dilation, blunt 26-gauge needle enters punctum and canaliculus; saline is injected",
 "Fluid reaching nose and throat indicates patent drainage; consider hypersecretion, lacrimal pump failure or partial obstruction (Jones dye test)",
 "Regurgitation of fluid during syringing indicates obstruction/blockage; proceed to probing",
 "On probing, hard stop indicates nasolacrimal duct blockage",
 "On probing, soft stop indicates lacrimal sac or canalicular block",
],
217: [
 "Jones dye test I: 2% fluorescein is instilled into conjunctival sac; cotton is placed at opening of NLD",
 "Jones I: stained cotton bud is positive and indicates hypersecretion",
 "Jones I: no staining is negative; irrigate residual fluorescein and perform Jones dye test II",
 "Jones II: stained bud after irrigation is positive and indicates partial NLD obstruction",
 "Jones II negative with no staining: lacrimal pump failure or partial canalicular obstruction",
 "Dacryocystitis is inflammation of lacrimal sac",
 "Congenital dacryocystitis: watering since birth due to non-canalization of NLD; commonest obstruction at valve of Hasner",
 "Congenital dacryocystitis treatment: lacrimal sac massage and topical tobramycin/erythromycin",
 "Age-based congenital treatment: 9-12 months syringing; >1 year probing; >4 years dacryocystorhinostomy (DCR)",
 "Acquired dacryocystitis cause listed: Streptococcus hemolyticus",
 "Acquired dacryocystitis treatment: oral antibiotics; DCR if fistula is positive",
],
218: [
 "Lacrimal gland tumours: pleomorphic adenoma is benign",
 "Adenoid cystic carcinoma of lacrimal gland is malignant",
 "Both lacrimal gland tumour types displace the eye downward and medially due to gland location",
 "Tear film innermost layer: mucin from goblet cells",
 "Tear film middle layer: aqueous from lacrimal glands",
 "Tear film outermost layer: lipid from meibomian gland, prevents evaporation of aqueous",
 "Corneal epithelium with microvilli is labelled under the tear film layers",
 "Aqueous deficiency: keratoconjunctivitis sicca; example Sjögren syndrome",
 "Lipid deficiency: evaporative dry eye; examples meibomian gland disease and contact lens wearer",
 "Mucin deficiency example: vitamin A deficiency",
 "Schirmer test is quantitative measurement of tear production using Whatman's filter paper No. 41",
 "Schirmer procedure: filter strip inserted in lower fornix for 5 minutes; measure wet length",
 "Schirmer wetting >15 mm is normal; <10 mm indicates dry eye",
 "Schirmer test illustrations label Whatman's filter paper and test procedure",
],
219: [
 "TBUT: instill 2% fluorescein in conjunctival sac and illuminate with blue light",
 "TBUT is interval between a blink and appearance of first dry spot on cornea",
 "TBUT <10 seconds suggests mucin deficiency",
 "A dry spot at a particular location suggests corneal disease",
 "Phenol red thread test: thread impregnated with phenol red dye is yellow before tears and red after contact with tears",
 "Phenol red thread is placed in lower fornix",
 "Phenol red thread test <6 mm indicates dry eye; >15 mm is normal",
 "Phenol red thread test diagram labels thread placement in lower fornix",
],
}

c = Chapter(46, "Lacrimal apparatus : Anatomy, Watering eye and Dry eye", 215, 219, POINTS)

c.unit("Tear secretion and lacrimal gland anatomy", "Adnexa",
       "The main gland is divided by levator into superior orbital and inferior palpebral parts and secretes reflex tears. Krause/Wolfring provide basal secretion. Parasympathetic secretomotor route: superior salivatory nucleus → greater superficial petrosal → pterygopalatine ganglion → zygomatic nerve; sympathetic is inhibitory.")
c.q(215, "match", "Match the lacrimal gland part with its position — 1) Orbital part  2) Palpebral part … A) Inferior  B) Superior",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Tears have secretion and drainage pathways; levator palpebrae superioris divides the main gland, with orbital part superior and palpebral part inferior.", [1, 2, 3], "Lacrimal gland anatomy")
c.q(215, "recall", "The main lacrimal gland is primarily responsible for ___ tear secretion.", "Reflex",
    ["Basal", "Mucin", "Lipid"], "The main lacrimal gland produces reflex tears; accessory Krause and Wolfring glands provide basal secretion.", [4, 5, 6], "Lacrimal gland anatomy")
c.q(215, "fillup", "Krause and Wolfring accessory glands are located in the conjunctival ___.", "Fornix",
    ["Limbus", "Caruncle", "Lacrimal sac"], "Accessory glands of Krause and Wolfring are located in the fornix between sclera and palpebral conjunctiva.", [5], "Accessory lacrimal glands")
c.q(215, "match", "Which pathway correctly carries parasympathetic secretomotor fibres to the lacrimal gland?", "Superior salivatory nucleus → greater superficial petrosal nerve → pterygopalatine ganglion → zygomatic nerve",
    ["Edinger-Westphal nucleus → oculomotor nerve → ciliary ganglion → nasociliary nerve", "Inferior salivatory nucleus → glossopharyngeal nerve → otic ganglion → auriculotemporal nerve", "Facial nucleus → chorda tympani → submandibular ganglion → lingual nerve"], "Parasympathetic route: superior salivatory nucleus in pons, greater superficial petrosal nerve (VII), pterygopalatine ganglion, then zygomatic nerve (V2) to stimulate lacrimal secretion.", [7, 8, 9, 10], "Lacrimal innervation")
c.q(215, "truefalse", "Sympathetic innervation of the lacrimal gland has an inhibitory function.", "True",
    ["False", "It is the main secretomotor pathway", "It has no function"], "The page labels sympathetic innervation as inhibitory; parasympathetic innervation is secretomotor.", [11], "Lacrimal innervation")
c.q(215, "recall", "The lacrimal apparatus anatomy figure labels the excretory ducts of the:", "Main lacrimal gland",
    ["Meibomian glands", "Canaliculi", "Nasolacrimal duct"], "The main gland's orbital and palpebral parts drain through main excretory ducts, as shown in the lacrimal apparatus diagram.", [12], "Lacrimal gland anatomy")

c.unit("Lacrimal drainage and evaluation of watering eye", "Adnexa",
       "Tears pass puncta → canaliculi → lacrimal sac → nasolacrimal duct → inferior meatus; orbicularis-assisted blinking pumps tears. Distinguish hyperlacrimation (over-secretion) from epiphora (drainage obstruction), and interpret syringing, probing and Jones tests.")
c.q(216, "match", "Put the tear drainage structures in the correct order.", "Puncta → canaliculi → lacrimal sac → nasolacrimal duct → inferior meatus",
    ["Canaliculi → puncta → nasolacrimal duct → sac → inferior meatus", "Puncta → sac → canaliculi → inferior meatus → nasolacrimal duct", "Puncta → canaliculi → inferior meatus → lacrimal sac → nasolacrimal duct"], "The drainage sequence is upper/lower puncta, canaliculi, lacrimal sac, nasolacrimal duct and inferior meatus.", [1, 3], "Lacrimal drainage")
c.q(216, "fillup", "The lacrimal sac is surrounded by orbicularis oculi; ___ assists drainage.", "Blinking",
    ["Accommodation", "Convergence", "Mydriasis"], "The lacrimal sac is surrounded by orbicularis oculi, and blinking assists tear drainage.", [2], "Lacrimal drainage")
c.q(216, "recall", "The nasolacrimal duct opens into which part of the nose?", "Inferior meatus",
    ["Middle meatus", "Superior meatus", "Sphenoethmoidal recess"], "The NLD opens into the inferior meatus; its opening is guarded by the valve of Hasner.", [3, 4], "Lacrimal drainage")
c.q(216, "scenario", "A newborn has congenital dacryocystitis from the commonest site of obstruction. Which structure is implicated?", "Valve of Hasner",
    ["Valve of Rosenmüller", "Plica semilunaris", "Punctum of the upper canaliculus"], "Non-canalization of the NLD, most commonly at the valve of Hasner, is listed in congenital dacryocystitis.", [4], "Lacrimal drainage")
c.q(216, "match", "Match the type of watering eye with its mechanism — 1) Hyperlacrimation  2) Epiphora … A) Blockage of drainage  B) Increased tear secretion",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Hyperlacrimation is increased secretion, for example with emotional stress or inflammation; epiphora is drainage blockage.", [5, 6], "Watering eye")
c.q(216, "match", "Which set contains the instruments shown for testing a watering eye?", "Nettleship punctum dilator, 26G bent needle cannula and Bowman's lacrimal probe",
    ["Schirmer strip, tonometer and gonioscopy lens", "Dacryoscope, 18G straight cannula and lacrimal hook", "Fluorescein strip, cryoprobe and keratometer"], "The page labels a Nettleship punctum dilator, 26-gauge bent needle cannula and Bowman's lacrimal probe.", [7], "Watering eye tests")
c.q(216, "scenario", "On syringing, fluid reaches the nose and throat. What does this show, and which test helps distinguish causes of watering despite patency?", "A patent drainage system; Jones dye test",
    ["Complete NLD obstruction; Schirmer test", "Canalicular block; TBUT", "Lacrimal sac fistula; phenol red thread test"], "Fluid reaching the nose and throat indicates patency; the Jones dye test helps assess hypersecretion, pump failure or partial obstruction when watering persists.", [8, 9], "Syringing")
c.q(216, "match", "During probing, a hard stop versus a soft stop indicates respectively:", "NLD blockage; lacrimal sac or canalicular block",
    ["Canalicular block; NLD blockage", "Lacrimal pump failure; hypersecretion", "Patent NLD; patent canaliculus"], "After regurgitation on syringing, probing is performed; hard stop indicates NLD blockage and soft stop lacrimal sac/canalicular block.", [10, 11, 12], "Probing")

c.unit("Jones dye tests and dacryocystitis", "Adnexa",
       "Jones I: 2% fluorescein in conjunctival sac; stained cotton at NLD opening means positive/hypersecretion; if negative, irrigate and perform Jones II. Jones II positivity means partial NLD obstruction; negative test suggests pump failure or partial canalicular obstruction. Dacryocystitis is lacrimal sac inflammation; congenital and acquired forms differ in cause and management.")
c.q(217, "recall", "Jones dye test I begins with instillation of ___ fluorescein into the conjunctival sac.", "2%",
    ["0.5%", "1%", "5%"], "Jones I uses 2% fluorescein in the conjunctival sac, with cotton at the NLD opening.", [1], "Jones dye tests")
c.q(217, "scenario", "In Jones I, the cotton bud at the NLD opening stains with fluorescein. This is a positive test indicating:", "Hypersecretion",
    ["Partial NLD obstruction", "Lacrimal pump failure", "Canalicular obstruction"], "A stained cotton bud makes Jones I positive and indicates hypersecretion.", [2], "Jones dye tests")
c.q(217, "match", "A negative Jones I is followed by irrigation and Jones II. Which Jones II result indicates partial NLD obstruction?", "Stained cotton bud after irrigation",
    ["No staining and no fluorescein in the conjunctival sac", "Regurgitation through the opposite punctum", "No wetting on Schirmer strip"], "If Jones I is negative, residual fluorescein is washed out; staining on Jones II indicates partial NLD obstruction.", [3, 4], "Jones dye tests")
c.q(217, "match", "A negative Jones II with no bud staining suggests which alternatives?", "Lacrimal pump failure or partial canalicular obstruction",
    ["Hypersecretion or complete NLD patency", "Orbital cellulitis or CST", "Aqueous deficiency or mucin deficiency"], "A negative Jones II with no stained bud suggests pump failure or partial canalicular obstruction; dacryocystography differentiates them.", [5], "Jones dye tests")
c.q(217, "fillup", "Dacryocystitis is inflammation of the lacrimal ___.", "Sac",
    ["Gland", "Punctum", "Conjunctiva"], "Dacryocystitis is inflammation of the lacrimal sac.", [6], "Dacryocystitis")
c.q(217, "match", "Congenital dacryocystitis typically presents with watering since birth due to non-canalization of the:", "Nasolacrimal duct",
    ["Upper canaliculus", "Lacrimal gland duct", "Inferior punctum"], "Congenital disease presents with watering since birth, caused by non-canalization of the NLD, commonly at Hasner's valve.", [7], "Congenital dacryocystitis")
c.q(217, "management", "Initial treatment listed for congenital dacryocystitis is lacrimal sac massage plus:", "Topical tobramycin or erythromycin",
    ["Systemic steroids", "Intralesional triamcinolone", "Topical atropine"], "Initial management includes lacrimal sac massage and topical antibiotics such as tobramycin or erythromycin.", [8], "Congenital dacryocystitis")
c.q(217, "match", "Match age with the listed congenital dacryocystitis intervention — 1) 9-12 months  2) >1 year  3) >4 years … A) Probing  B) DCR  C) Syringing",
    "1-C, 2-A, 3-B", ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"], "The page lists syringing at 9-12 months, probing after 1 year, and DCR after 4 years.", [9], "Congenital dacryocystitis")
c.q(217, "recall", "The acquired dacryocystitis organism listed is:", "Streptococcus hemolyticus",
    ["Staphylococcus epidermidis", "Pseudomonas aeruginosa", "Moraxella catarrhalis"], "Acquired dacryocystitis is attributed to Streptococcus hemolyticus; treatment is oral antibiotics and DCR if fistula is positive.", [10, 11], "Acquired dacryocystitis")
c.q(217, "management", "For acquired dacryocystitis, the listed treatment is oral antibiotics, with DCR if:", "Fistula is positive",
    ["Jones I is positive", "Schirmer wetting is below 10 mm", "A hard stop is present"], "Acquired disease is treated with oral antibiotics; DCR is listed if fistula is positive.", [11], "Acquired dacryocystitis")

c.unit("Lacrimal gland tumours and tear film", "Adnexa",
       "Pleomorphic adenoma is benign and adenoid cystic carcinoma malignant; lacrimal gland masses displace the globe down and medially. Tear film layers from cornea outward: mucin, aqueous, lipid; deficiency patterns have distinct associations.")
c.q(218, "match", "Which lacrimal gland tumour is benign and which is malignant?", "Pleomorphic adenoma; adenoid cystic carcinoma",
    ["Adenoid cystic carcinoma; pleomorphic adenoma", "Both are benign", "Both are malignant"], "Pleomorphic adenoma is benign; adenoid cystic carcinoma is malignant.", [1, 2], "Lacrimal gland tumours")
c.q(218, "scenario", "A lacrimal gland tumour displaces the globe in which direction?", "Downward and medially",
    ["Upward and laterally", "Straight anteriorly only", "Downward and laterally"], "Both listed lacrimal gland tumour types displace the eye downward and medially because of the gland's location.", [3], "Lacrimal gland tumours")
c.q(218, "match", "Order the tear film layers from the corneal surface outward.", "Mucin → aqueous → lipid",
    ["Lipid → mucin → aqueous", "Aqueous → lipid → mucin", "Mucin → lipid → aqueous"], "The innermost layer is mucin, middle is aqueous and outermost is lipid; the diagram also labels corneal epithelium with microvilli beneath the film.", [4, 5, 6, 7], "Tear film")
c.q(218, "recall", "The outer lipid layer of the tear film is produced by the meibomian glands and primarily:", "Prevents evaporation of the aqueous layer",
    ["Provides corneal sensation", "Drains tears into the nose", "Produces mucin from goblet cells"], "Meibomian lipid is the outermost layer and prevents evaporation of aqueous tears.", [6], "Tear film")
c.q(218, "match", "Which dry-eye deficiency and association are correctly paired?", "Aqueous deficiency: Sjögren syndrome; lipid deficiency: meibomian gland disease; mucin deficiency: vitamin A deficiency",
    ["Aqueous: vitamin A deficiency; lipid: Sjögren; mucin: contact lens wearer", "Aqueous: meibomian disease; lipid: vitamin A deficiency; mucin: Sjögren", "Aqueous: contact lens wearer; lipid: Sjögren; mucin: meibomian disease"], "Aqueous deficiency is KCS (e.g., Sjögren); lipid deficiency causes evaporative dry eye (e.g., MGD/contact lenses); mucin deficiency is associated with vitamin A deficiency.", [8, 9, 10], "Dry-eye disorders")
c.q(218, "recall", "Schirmer testing uses which filter paper and measures what?", "Whatman's No. 41 filter paper; tear production",
    ["Whatman's No. 1 filter paper; tear drainage", "Litmus paper; corneal sensitivity", "Phenol-red thread; tear evaporation"], "Schirmer is a quantitative test of tear production using Whatman's filter paper No. 41.", [11, 14], "Schirmer test")
c.q(218, "numeric", "In Schirmer testing, the strip is left for 5 minutes; wetting below ___ mm indicates dry eye.", "10",
    ["5", "15", "25"], "The strip is placed in the lower fornix for 5 minutes; >15 mm is normal and <10 mm indicates dry eye.", [12, 13], "Schirmer test")
c.q(218, "numeric", "A Schirmer wetting length greater than ___ mm is considered normal in the book.", "15",
    ["6", "10", "12"], "Schirmer >15 mm is normal; <10 mm indicates dry eye.", [13], "Schirmer test")

c.unit("Tear-film tests: TBUT and phenol red thread", "Adnexa",
       "TBUT uses 2% fluorescein and blue light; measure blink-to-first-dry-spot interval (<10 s suggests mucin deficiency). Phenol red thread changes yellow to red with tears; <6 mm suggests dry eye and >15 mm is normal.")
c.q(219, "recall", "TBUT is measured after instilling 2% fluorescein and illuminating the eye with:", "Blue light",
    ["Red-free green light", "Infrared light", "Ultraviolet light"], "For TBUT, 2% fluorescein is instilled and the tear film is observed with blue light.", [1], "TBUT")
c.q(219, "fillup", "TBUT is the interval between a blink and the appearance of the first ___ on the cornea.", "Dry spot",
    ["Fluorescein ring", "Vascular loop", "Conjunctival fold"], "TBUT measures the interval between blinking and the first dry spot on the cornea.", [2], "TBUT")
c.q(219, "numeric", "A TBUT of less than ___ seconds suggests mucin deficiency.", "10",
    ["3", "5", "15"], "The page associates TBUT <10 seconds with mucin deficiency.", [3], "TBUT")
c.q(219, "scenario", "A dry spot repeatedly appearing at a particular corneal location during TBUT suggests:", "Corneal disease",
    ["Aqueous deficiency alone", "Lacrimal pump failure", "NLD obstruction"], "A dry spot at a particular location is associated with corneal disease.", [4], "TBUT")
c.q(219, "recall", "In the phenol red thread test, the thread changes from yellow to ___ after contact with tears.", "Red",
    ["Blue", "Green", "Black"], "The thread is impregnated with phenol red dye, yellow in colour, and becomes red with tears.", [5], "Phenol red thread test")
c.q(219, "numeric", "Phenol red thread wetting below ___ mm indicates dry eye; above 15 mm is normal.", "6",
    ["3", "10", "12"], "Phenol red thread test: <6 mm indicates dry eye and >15 mm is normal; the thread is placed in the lower fornix.", [6, 7, 8], "Phenol red thread test")

covered = c.finish()
