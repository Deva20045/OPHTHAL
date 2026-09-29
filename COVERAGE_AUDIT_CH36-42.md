# Coverage audit - Chapters 36-42 (Book pp. 164-194)

Every source line, heading, table row, figure caption and bracket read from the scanned pages is listed as a numbered point, in book order, with the question ID(s) that test it. `authoring/lib.py::finish()` refuses to write a chapter unless every point is covered, questions are in (page, first-point) order, each question has 4 distinct options and the answer is not length-predictable.

## Chapter 36 - Retinal Vascular Disorders : Part 2 (pp. 164-168): 64 questions, 6 units

### Book p164 - 14 source points, 9 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title: RETINAL VASCULAR DISORDERS : PART 2; heading 'Hypertensive retinopathy' | C36-001 |
| 2 | Phases: Vasoconstriction phase -> Sclerotic phase (Atherosclerosis) -> Exudative phase | C36-001 |
| 3 | Sub-heading 'Clinical features' / 'Keith-Wagner classification' (table: Grade / Characteristics) | C36-002 |
| 4 | Grade 1: Arteriolar attenuation; A:V (diameter) ratio = 1:3 (Normal 2:3) | C36-002 |
| 5 | Grade 2: Salus sign - deflection of blood vessel | C36-003 |
| 6 | Grade 3: Bonnet sign - banking of blood vessel | C36-003 |
| 7 | Grade 3: Gunn sign - tapering of blood vessel | C36-003 |
| 8 | Grade 3: Flame shaped hemorrhages with cotton wool spots | C36-004 |
| 9 | Bracket beside Grades 2 and 3: signs are 'At AV crossings in veins' | C36-005 |
| 10 | Grade 4: Copper wiring of arterioles | C36-006 |
| 11 | Grade 4: Silver wiring of arterioles | C36-006 |
| 12 | Grade 4: Papilledema | C36-006 |
| 13 | Figure 'Grade 4 HTN retinopathy' labels: 1 Cotton wool spots; 2 Swelling of optic disc; 3 Exudates: macular star appearance: malignant HTN | C36-007, C36-008 |
| 14 | Figure 'Grade 3 Hypertensive retinopathy' labels: cotton wool spots, AV change, hemorrhages (flame shaped) | C36-009 |

### Book p165 - 22 source points, 13 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading: Central Retinal Artery Occlusion (CRAO); CAUSES | C36-010 |
| 2 | Cause: Atherosclerosis: m/c | C36-010 |
| 3 | Cause: Emboli - Hollenhorst plaque: cholesterol emboli originating from bifurcation of CCA | C36-011 |
| 4 | Cause: Giant cell arteritis | C36-012 |
| 5 | Clinical feature: sudden, painless loss of vision | C36-013 |
| 6 | Clinical feature: optic atrophy (Consecutive) | C36-013 |
| 7 | Clinical feature: RAPD or Marcus Gunn pupil | C36-014 |
| 8 | Fundus: pale fundus d/t retinal edema | C36-015 |
| 9 | Fundus: cattle tracking fundus d/t segmentation of blood column | C36-015 |
| 10 | Fundus: cherry red spot at macula d/t collection of fluid in ganglion cell layers (GCL) of retina except at foveola | C36-015 |
| 11 | Figure caption: Cherry red spot (arrow at macula) | C36-016 |
| 12 | Figure caption: CRAO with macular cilioretinal artery sparing | C36-017 |
| 13 | Figure caption: Dye filling cilioretinal artery in FFA | C36-017 |
| 14 | Note 'Cherry red spots at macula' - mnemonic: Cherry trees never grow tall in sand, mud & grime | C36-018 |
| 15 | List item: CRAO | C36-019 |
| 16 | List item: Trauma-blunt | C36-019 |
| 17 | List item: Niemann Picks disease | C36-019 |
| 18 | List item: Gangliosidosis Type 1 | C36-020 |
| 19 | List item: Tay Sachs disease (bracket: Gangliosidosis Type 2) | C36-021 |
| 20 | List item: Sandhoffs disease (bracket: Gangliosidosis Type 2) | C36-021 |
| 21 | List item: metachromatic leukodystrophy | C36-022 |
| 22 | List item: Gaucher's disease: Type 2 | C36-022 |

### Book p166 - 20 source points, 19 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | TREATMENT: Ocular emergency: Rx within 4 hrs | C36-023 |
| 2 | 24-48 hrs: Complete occlusion | C36-024 |
| 3 | Ocular massage: dislodge emboli | C36-025 |
| 4 | Vasodilatation - sublingual isosorbide nitrate | C36-026 |
| 5 | Carbogen: 95% O2 + 5% CO2 -> hypercarbia -> raised PCO2 -> lowered pH -> vasodilatation (respiratory acidosis) | C36-027, C36-028 |
| 6 | Decrease IOP - IV mannitol | C36-029 |
| 7 | Decrease IOP - paracentesis: aspiration of aqueous | C36-029 |
| 8 | Rx of cause | C36-030 |
| 9 | Heading: Central retinal vein occlusion (CRVO); m/c cause: hypertension | C36-031 |
| 10 | 1. Non-ischemic stage: d/t stasis of blood -> hypoxia; and raised vascular permeability -> macular edema -> loss of vision | C36-032 |
| 11 | Rx: intravitreal triamcinolone | C36-033 |
| 12 | Rx: 0.7 mg dexamethasone intravitreal implants (Geneva study) | C36-033, C36-034 |
| 13 | Rx: anti VEGF drugs | C36-033 |
| 14 | 2. Ischemic stage: severe hypoxia -> capillary endothelium damage | C36-035 |
| 15 | Clinical feature: severe flame shaped hemorrhages | C36-036 |
| 16 | Figure caption: Tomato ketchup/splash appearance | C36-036 |
| 17 | Clinical feature: rubeosis iridis (neovascularisation of iris) d/t oxygen demand by posterior segment | C36-037 |
| 18 | Blood leak into anterior chamber -> blocks trabecular meshwork -> neovascular glaucoma AKA 100 day glaucoma: glaucoma progression of 3 months in CRVO | C36-038, C36-039 |
| 19 | Rx: panretinal photocoagulation | C36-040 |
| 20 | Note: m/c cause of neovascular glaucoma: diabetic retinopathy | C36-041 |

### Book p167 - 14 source points, 11 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | BRANCHED RETINAL VEIN OCCLUSION (BRVO): superior part of central retinal vein occluded | C36-042 |
| 2 | BRVO: m/c site: AV crossings | C36-043 |
| 3 | BRVO: m/c quadrant: superotemporal | C36-043 |
| 4 | Figure caption: BRVO | C36-044 |
| 5 | Heading: Retinopathy of prematurity (ROP) - occurs in: age at birth <= 32 weeks | C36-045 |
| 6 | ROP occurs in: birth weight <= 1750 grams | C36-046 |
| 7 | Age of screening table row 1: age at birth >= 28 wks, birth weight >= 1200 g -> 4 weeks after birth | C36-047 |
| 8 | Age of screening table row 2: age at birth < 28 wks, birth weight < 1200 g -> 2-3 weeks after birth | C36-048 |
| 9 | Stage 1: demarcating line between vascularized retina & peripheral avascular retina | C36-049 |
| 10 | Stage 2: ridge formation at demarcating line | C36-049 |
| 11 | Stage 3: extra retinal neovascularization on the ridge moving into vitreous | C36-050 |
| 12 | Stage 4: partial retinal detachment (RD) | C36-051 |
| 13 | Stage 5: total RD | C36-051 |
| 14 | Figure captions: Stage 2 ROP; Stage 3 ROP | C36-052 |

### Book p168 - 18 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Treatment: laser photocoagulation | C36-053 |
| 2 | Indication: pre-threshold ROP type 1 (ETROP study) | C36-053 |
| 3 | Zone 1 + any stage + plus disease (or) | C36-054 |
| 4 | Zone 1 + stage 3 (or) | C36-055 |
| 5 | Zone 2 + stage 2/3 + plus disease (or) | C36-055 |
| 6 | Plus disease: venous tortuosity & dilatation in >= 2 quadrants | C36-056 |
| 7 | Pars plana vitrectomy: if RD + | C36-057 |
| 8 | Figure 'Zones of retina': nasal, temporal, clock hours (12/3/6/9), zone I, II, III, macula, optic nerve, ora serrata | C36-058 |
| 9 | Heading: Miscellaneous | C36-059 |
| 10 | EALES' DISEASE triangle: Occlusion; Periphlebitis; Neovascularisation of retina -> recurrent vitreous hemorrhage | C36-059 |
| 11 | Eales' disease Rx: panretinal photocoagulation | C36-060 |
| 12 | COATS' DISEASE: idiopathic retinal telengiectasia | C36-061 |
| 13 | Coats': m > F | C36-062 |
| 14 | Coats': unilateral | C36-062 |
| 15 | Coats' clinical features: painless loss of vision | C36-063 |
| 16 | Coats' clinical features: strabismus | C36-063 |
| 17 | Coats' clinical features: leukocoria | C36-063 |
| 18 | Coats' clinical features: exudative retinal detachment | C36-064 |

## Chapter 37 - Retinal Detachment (pp. 169-171): 44 questions, 5 units

### Book p169 - 17 source points, 13 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading RETINAL DETACHMENT; definition: separation of neurosensory retina from retinal pigment epithelium and collection of subretinal fluid | C37-001 |
| 2 | Investigations: Indirect ophthalmoscopy: IOC | C37-002 |
| 3 | Investigations: Optical coherence tomography (OCT); B-scan ultrasonography | C37-003 |
| 4 | Figure Normal vs Retinal Detachment: NSR, subretinal space, RPE, fluid | C37-004 |
| 5 | Types: Retinal detachment (RD) -> Primary/Rhegmatogenous RD; Secondary RD -> Tractional, Exudative | C37-005 |
| 6 | Heading: Primary/Rhegmatogenous Retinal Detachment (RRD); Pathogenesis: Syneresis (liquefaction of vitreous) -> Posterior vitreous detachment (PVD) | C37-006 |
| 7 | Pathogenesis: dynamic vitreoretinal traction from attached parts of vitreous | C37-007 |
| 8 | Pathogenesis: retinal breaks develop -> fluid enters subretinal space | C37-007 |
| 9 | Figure: retina, detached parts of retina, attached parts of retina, vitreoretinal traction | C37-008 |
| 10 | Causes: pathological myopia (m/c) | C37-009 |
| 11 | Causes: blunt trauma | C37-010 |
| 12 | Causes: cataract surgery (aphakia) | C37-010 |
| 13 | Causes: lattice degeneration of retina | C37-010 |
| 14 | Symptoms: photophobia: flashes of light (stretching of nerve fibers -> ectopic neural impulses to brain) | C37-011 |
| 15 | Symptoms: floaters: small black flying dots (d/t vitreal opacities) | C37-012 |
| 16 | Symptoms: curtain falling in front of eye | C37-013 |
| 17 | Symptoms: loss of vision: sudden & painless | C37-013 |

### Book p170 - 23 source points, 19 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Signs 1: detached retina: gray/opaque, convex shaped | C37-014 |
| 2 | Signs 2: extent of RD till ora serrata | C37-015 |
| 3 | Signs 3: Shafer's sign - tobacco-dust appearance | C37-016 |
| 4 | Shafer's sign d/t deposition of brown pigmented cells at the anterior surface of vitreous | C37-017 |
| 5 | Eye diagram labels: RD, Shafer's sign | C37-018 |
| 6 | Photograph caption: RD | C37-019 |
| 7 | Photograph caption: U shaped retinal tear; m/c location: superotemporal quadrant | C37-019 |
| 8 | OCT caption 'Longstanding RRD' labels: RD, subretinal fluid, intraretinal cysts | C37-020 |
| 9 | Lincoff rules: rules to locate breaks in retina | C37-021 |
| 10 | Signs 4: RAPD (relative afferent pupillary defect) | C37-022 |
| 11 | Signs 5: in chronic RD - retinal atrophy | C37-023 |
| 12 | Chronic RD: subretinal demarcation lines k/a high water marks (> 3 months) | C37-023 |
| 13 | Chronic RD: intraretinal cysts (> 1 year) | C37-024 |
| 14 | Management - Prophylaxis: laser photocoagulation to seal breaks (usually superotemporal quadrant) | C37-025 |
| 15 | Treatment flowchart: mobile retina -> tamponade -> internal / external | C37-026 |
| 16 | Internal 1. Pneumatic retinopexy: uses SF6 or C3F8 (propane) | C37-027 |
| 17 | Pneumatic retinopexy: done in superior breaks | C37-028 |
| 18 | Internal 2. Silicone oil: injected into vitreous cavity | C37-029 |
| 19 | Silicone oil: removed after 8-12 weeks | C37-029 |
| 20 | Silicone oil complication: hyperoleon -> oil leaks into anterior chamber and collects superiorly (inverse hypopyon) | C37-030 |
| 21 | External tamponade: scleral buckling (scleral weight pushes RPE anteriorly) | C37-031 |
| 22 | Immobile retina: in proliferative vitreo-retinopathy (causes membrane formation & scarring) -> vitrectomy + subretinal fluid drainage | C37-032 |
| 23 | Note: Lincoff rules -> used to locate breaks in retina | C37-021 |

### Book p171 - 19 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading: Secondary Retinal Detachment; table columns Tractional RD / Exudative RD | C37-033 |
| 2 | Pathology - tractional: static vitreoretinal traction | C37-033 |
| 3 | Pathology - exudative: exudation into subretinal space | C37-033 |
| 4 | Etiology tractional: diabetic retinopathy (m/c) | C37-034 |
| 5 | Etiology tractional: retinopathy of prematurity | C37-035 |
| 6 | Etiology tractional: penetrating trauma | C37-035 |
| 7 | Etiology tractional: sickle cell retinopathy (Roth spots (+): hemorrhage with clear centre) - circled | C37-036 |
| 8 | Etiology exudative: choroidal melanoma (m/c) | C37-037 |
| 9 | Etiology exudative: toxemia of pregnancy | C37-038 |
| 10 | Etiology exudative: Coat's disease (idiopathic retinal telengiectasia) | C37-039 |
| 11 | Etiology exudative: VKH syndrome | C37-039 |
| 12 | Etiology exudative: central serous retinopathy | C37-039 |
| 13 | Clinical features tractional: loss of vision: gradual & painless | C37-040 |
| 14 | Tractional: shape of RD: concave | C37-040 |
| 15 | Tractional: photopsia, floaters, extension of RD till ora serrata - bracket (-) | C37-041 |
| 16 | Clinical features exudative: loss of vision: sudden, painless | C37-042 |
| 17 | Exudative: shape of RD: convex | C37-042 |
| 18 | Exudative: hallmark feature: shifting fluid (with shifting head position) | C37-043 |
| 19 | Treatment (both): treat the cause | C37-044 |

## Chapter 38 - Special Investigations for Cornea (pp. 172-174): 39 questions, 5 units

### Book p172 - 16 source points, 13 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title SPECIAL INVESTIGATIONS FOR CORNEA; heading Keratometry; Principle: anterior surface of cornea acts as a convex mirror | C38-001 |
| 2 | Size of image is proportional to 1/curvature | C38-002 |
| 3 | Image seen as keratometric mires | C38-002 |
| 4 | Photograph captions: Keratometer; Keratometric mires | C38-003 |
| 5 | Correct positioning of mires: single, overlapped minus sign | C38-004 |
| 6 | Correct positioning of mires: single, overlapped plus sign | C38-004 |
| 7 | Uses 1: measure corneal curvature | C38-005 |
| 8 | Uses 2: diagnose astigmatism - horizontally oval mires: with the rule astigmatism | C38-006 |
| 9 | Uses 2: diagnose astigmatism - vertically oval mires: against the rule astigmatism | C38-006 |
| 10 | Uses 3: to ascertain proper fitting of contact lens | C38-007 |
| 11 | Uses 4: to diagnose keratoconus (pulsating mires seen) | C38-008 |
| 12 | Figure captions: Good fit of lens; Steep fit of lens | C38-009 |
| 13 | Heading: Pachymetry - measures corneal thickness | C38-010 |
| 14 | Normal Corneal Thickness (CT): 0.5 to 0.6 mm (0.54 mm) or 540 micron | C38-011 |
| 15 | CT is highest in the centre -> reduces towards periphery | C38-012 |
| 16 | Pachymetry uses 1: eligibility for LASIK (continues on next page) | C38-013 |

### Book p173 - 14 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | LASIK: contraindicated (c/i) if CT < 450 micron | C38-014 |
| 2 | Uses 2: IOP measurement: 1 mm Hg IOP = 10 micron of CT | C38-015 |
| 3 | CT increased -> false high IOP; CT decreased -> false low IOP | C38-016 |
| 4 | Figure caption: Pachymetry | C38-017 |
| 5 | Heading: Corneal topography - examination of corneal surface; methods used | C38-018 |
| 6 | Method 1: Placido disc (labels: viewing aperture with lens, reflection rings, handle) | C38-019 |
| 7 | Figure caption: Reflection of placido disc: Normal | C38-020 |
| 8 | Method 2: Orbscan - uses slit scan imaging principle | C38-021 |
| 9 | Method 3: Pentacam measures: a. CT; b. corneal curvature; c. anterior segment imaging | C38-022 |
| 10 | Pentacam measures: d. topographic elevation maps of anterior surface; e. topographic elevation maps of posterior surface | C38-023 |
| 11 | Heading: Corneal vital staining - used to visualize and distinguish ulcer from surrounding healthy tissue | C38-024 |
| 12 | Fluorescein dye: stains area of denuded epithelium (floor/base of ulcer) | C38-025 |
| 13 | Fluorescein: visualized under cobalt blue light -> green fluorescence | C38-026 |
| 14 | Ulcer diagram: stain in floor/base, margins | C38-027 |

### Book p174 - 14 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Fluorescein other uses: Goldmann's applanation tonometry | C38-028 |
| 2 | Fluorescein other uses: Jones' dye disappearance test (lacrimation assessment) | C38-029 |
| 3 | Fluorescein other uses: Seidel's test (in penetrating trauma) | C38-029 |
| 4 | Rose Bengal dye: stains devitalised/necrotic tissue (margins of ulcer) | C38-030 |
| 5 | Rose Bengal disadvantage: can be toxic to healthy tissue | C38-031 |
| 6 | Lissamine green dye: stains devitalised/damaged tissue | C38-032 |
| 7 | Lissamine green advantage: non-toxic to healthy ocular tissue | C38-032 |
| 8 | Lissamine green other uses: m/c used for diagnosis of dry eye by conjunctival staining | C38-033 |
| 9 | Alcian blue dye: stains mucin deposits and filaments | C38-034 |
| 10 | Photograph captions: Lissamine green dye; Rose bengal stain; Flourescein dye; Flourescein dye application | C38-035 |
| 11 | Heading: Other corneal investigations - Confocal microscopy: non-invasive technique for in-vivo imaging of all layers of living cornea | C38-036 |
| 12 | Corneal aesthesiometer: examines corneal sensations (figure caption: Corneal aesthesiometer) | C38-037 |
| 13 | Instrument: pen-like instrument with filament (6 cm long) | C38-038 |
| 14 | Length of filament eliciting corneal sensations proportional to corneal sensations proportional to 1/anaesthesia | C38-039 |

## Chapter 39 - Corneal Ulcer and Keratitis (pp. 175-179): 71 questions, 8 units

### Book p175 - 21 source points, 15 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title CORNEAL ULCER AND KERATITIS; definition: discontinuity in corneal epithelium + cellular infiltration & necrosis of underlying layers | C39-001 |
| 2 | Heading Bacterial Corneal Ulcer; ETIOLOGY: Staphylococcus aureus: m/c worldwide | C39-002 |
| 3 | Pneumococcus: MC in India | C39-003 |
| 4 | Pneumococcus: ulcer serpens - centre -> periphery in zigzag pattern | C39-004 |
| 5 | Pneumococcus: hypopyon corneal ulcer | C39-004 |
| 6 | Pseudomonas: m/c in contact lens users | C39-005 |
| 7 | Pseudomonas: green discharge | C39-005 |
| 8 | Atypical mycobacteria: m/c in h/o LASIK | C39-006 |
| 9 | Nocardia: wreath shaped/pin head ulcer (figure caption: Wreath shaped ulcer) | C39-007 |
| 10 | Figure 'Pneumococcal ulcer' labels: corneal ulcer; hypopyon: collection of pus in anterior chamber | C39-008 |
| 11 | Bacteria invading intact epithelium: Neisseria - N. meningitidis, N. gonorrhoea | C39-009 |
| 12 | Bacteria invading intact epithelium: Corynebacterium diphtheria | C39-010 |
| 13 | Bacteria invading intact epithelium: Listeria | C39-010 |
| 14 | Bacteria invading intact epithelium: Shigella | C39-010 |
| 15 | Bacteria invading intact epithelium: Haemophilus aegyptius | C39-011 |
| 16 | PATHOGENESIS Stage 1 - initial stage: saucer shaped ulcer with overhanging margins | C39-012 |
| 17 | Stage 2 - progressive stage: infiltration by PMNs | C39-013 |
| 18 | Stage 2: hypopyon | C39-013 |
| 19 | Stage 2: keratouveitis - mobile: liquid like pus | C39-014 |
| 20 | Stage 2: keratouveitis - sterile | C39-014 |
| 21 | Stage diagram captions: Stage 1, Stage 2, Stage 3 | C39-015 |

### Book p176 - 20 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Stage 3 - regressive stage: smooth floor & edges of ulcer | C39-016 |
| 2 | Stage 3: vascularization + | C39-016 |
| 3 | Stage 3: decreased inflammatory response | C39-016 |
| 4 | Stage 4 - scar/cicatrization: permanent vision loss (figure caption: Stage 4) | C39-017 |
| 5 | COMPLICATION 1. Ectatic cicatrix: thinning of cornea | C39-018 |
| 6 | Ectatic cicatrix: bulging of cornea d/t raised IOP (temporary/permanent) | C39-018 |
| 7 | 2. Anterior staphyloma: bulging of cornea d/t thinning + incarceration of iris tissue | C39-019 |
| 8 | 3. Descemetocoele: herniation of Descemet's membrane through corneal ulcer | C39-020 |
| 9 | 4. Perforation of cornea: a. aqueous leak -> decreased IOP | C39-021 |
| 10 | Perforation: b. iris prolapse | C39-022 |
| 11 | Perforation: c. pseudo-cornea - corneal surface formed d/t plugging of perforation by iris tissue | C39-022 |
| 12 | 5. Endophthalmitis/Panophthalmitis | C39-023 |
| 13 | Photograph captions: Lobulated appearance of anterior staphyloma; Descemetocoele; Iris prolapse; Pseudo-cornea | C39-024 |
| 14 | MANAGEMENT Antibiotics: after gram staining & culture of ulcer base, scraping | C39-025 |
| 15 | Fortified antibiotics: fortified Cephalozin 5% + fortified Tobramycin 1.3% | C39-026 |
| 16 | Atropine eye drops: relieve ciliary spasms | C39-027 |
| 17 | Impending perforation: oral doxycycline | C39-028 |
| 18 | Impending perforation: soft bandage contact lens (BCL) | C39-028 |
| 19 | Impending perforation: cyanoacrylate glue | C39-028 |
| 20 | Contraindications: steroids d/t epithelial thinning | C39-029 |

### Book p177 - 20 source points, 16 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Fungal Corneal Ulcer; m/c cause: Aspergillus (filamentous fungi with septate hyphae) | C39-030 |
| 2 | H/O trauma with vegetative fungi | C39-031 |
| 3 | Signs: out of proportion to symptoms | C39-032 |
| 4 | Dry looking ulcer: 1. feathery ulcer margin; 2. satellite lesions | C39-033 |
| 5 | Dry looking ulcer: 3. Wessely immune ring: antigen-antibody complexes | C39-033, C39-034 |
| 6 | Hypopyon: thick, immobile | C39-035 |
| 7 | Hypopyon: 'Asterile' | C39-035 |
| 8 | Figure caption: Fungal Corneal Ulcer (arrows numbered 1, 2, 3) | C39-033 |
| 9 | Treatment: Antibiotics - Natamycin 5% eye drops: DOC for Aspergillus fusarium | C39-036 |
| 10 | Amphotericin B 0.15% eye drops | C39-037 |
| 11 | Atropine: supportive Rx | C39-038 |
| 12 | Steroids: C/I | C39-038 |
| 13 | Heading Acanthamoeba Keratitis; Risk factors: unhygienic practices in contact lens users | C39-039 |
| 14 | Contaminated solution, washing in tap water, swimming pools | C39-039 |
| 15 | Clinical features: symptoms out of proportion to signs | C39-040 |
| 16 | Signs: pseudodendritic keratitis | C39-041 |
| 17 | Signs: radial keratoneuritis - inflammation of nerves throughout cornea | C39-042 |
| 18 | Signs: ring shaped ulcer with abscess: pathognomonic (figure caption: Ring abscess) | C39-043 |
| 19 | Investigation 1. Gram staining (figure label: double walled Acanthamoeba cyst) | C39-044 |
| 20 | Investigation 2. Culture media: non-nutrient agar enriched with E. coli | C39-045 |

### Book p178 - 19 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Treatment: drugs inhibiting membrane synthesis - PHMB 0.02% (Polyhexamethylene biguanide): DOC | C39-046 |
| 2 | Drugs inhibiting membrane synthesis - Chlorhexidine 0.02% | C39-047 |
| 3 | Drugs inhibiting DNA synthesis: Propamidine: m/c | C39-048 |
| 4 | Heading Viral Keratitis; HERPES SIMPLEX VIRUS (HSV): 1° infection: conjunctivitis | C39-049 |
| 5 | HSV recurrent infection: keratitis | C39-049 |
| 6 | Clinical features a. Epithelial lesions: d/t active viral replication; fluorescence staining | C39-050 |
| 7 | Figures: superficial punctate (dot like) keratitis -> dendritic ulcer: branching with terminal buds -> geographic ulcer | C39-051 |
| 8 | Rx: 3% acyclovir eye ointment: 5 times/day x 10-14 days | C39-052 |
| 9 | Steroids: C/I | C39-052 |
| 10 | Note: other d/d's for dendritic ulcer: Acanthamoeba keratitis | C39-053 |
| 11 | Other d/d's for dendritic ulcer: HZV keratitis | C39-053 |
| 12 | Other d/d's for dendritic ulcer: Tyrosinemia | C39-053 |
| 13 | Other d/d's for dendritic ulcer: contact lens overuse | C39-053 |
| 14 | b. Stromal keratitis: i. Immune stromal keratitis: d/t type III hypersensitivity | C39-054 |
| 15 | Immune stromal keratitis: occurs following epithelial keratitis | C39-055 |
| 16 | Immune stromal keratitis Rx: 3% acyclovir ointment + topical steroids | C39-055 |
| 17 | ii. Necrotizing stromal keratitis: most severe form of stromal keratitis | C39-056 |
| 18 | Necrotizing stromal keratitis Rx: 3% acyclovir ointment + topical steroids | C39-056 |
| 19 | Figure caption: Immune Stromal Keratitis (label: central stromal haze) | C39-057 |

### Book p179 - 15 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | c. Endothelial lesion: i. Disciform keratitis: disc shaped areas of deep stromal/endothelial edema | C39-058 |
| 2 | Disciform keratitis: type IV hypersensitivity reaction | C39-059 |
| 3 | Hallmark of HSV keratitis: corneal anaesthesia -> metaherpetic keratitis/neurotrophic ulcer d/t 5th cranial nerve palsy | C39-060 |
| 4 | Heading HERPES ZOSTER OPHTHALMICUS/SHINGLES: affects dermatome supplied by ophthalmic branch of 5th cranial nerve | C39-061 |
| 5 | Hutchinson's sign: rash involving tip of the nose -> increased chance of Herpes Zoster Ophthalmicus | C39-062 |
| 6 | Clinical features 1. Pseudodendritic ulcer: branching pattern with no terminal buds | C39-063 |
| 7 | 2. Nummular keratitis | C39-064 |
| 8 | 3. Mucous plaque keratitis: in chronic cases | C39-065 |
| 9 | 4. Stromal keratitis | C39-065 |
| 10 | 5. Cranial nerve palsy: 3rd cranial nerve - m/c | C39-066 |
| 11 | 6. Sclerokeratitis: least common finding | C39-067 |
| 12 | 7. Post-herpetic neuralgia: persistence of pain after 1 month of resolution | C39-068 |
| 13 | Post-herpetic neuralgia: worse at night | C39-069 |
| 14 | Treatment: T. Acyclovir 800 mg x 5 times/day x 2 weeks | C39-070 |
| 15 | Figure captions: Shingles; Nummular keratitis (label: coin shaped sub-epithelial lesions) | C39-071 |

## Chapter 40 - Corneal Dystrophies, Keratoconus and Miscellaneous Disorders (pp. 180-184): 67 questions, 6 units

### Book p180 - 24 source points, 20 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title CORNEAL DYSTROPHIES, KERATOCONUS AND MISCELLANEOUS DISORDERS; heading Corneal Dystrophies; Features: primary corneal disease | C40-001 |
| 2 | Features: present in 1st and 2nd decades | C40-002 |
| 3 | Features: non-inflammatory, progressive, B/L | C40-003 |
| 4 | Features: autosomal dominant inheritance | C40-004 |
| 5 | Table header: Disease / Feature; row group 1. Epithelial | C40-005 |
| 6 | Cogan's epithelial basement membrane dystrophy / map dot: m/c corneal dystrophy | C40-005 |
| 7 | Meesmann epithelial dystrophy: non-progressive, d/t keratin gene mutation | C40-006 |
| 8 | Lisch epithelial dystrophy: AD/XLD | C40-007 |
| 9 | Row group 2. Bowman layer | C40-008 |
| 10 | Reis Buckler's dystrophy/CDB1/GCD III: fish net | C40-009, C40-010 |
| 11 | Schnyder central crystalline dystrophy: corneal lipid metabolism disorder | C40-009 |
| 12 | Thiel Behnke dystrophy / GCD III: honeycomb pattern of opacities | C40-009, C40-010 |
| 13 | Row group 3. Stromal | C40-011 |
| 14 | Lattice corneal dystrophy I / Biber Haab Dimmer; Lattice dystrophy II / Finnish: neuropathy seen 70-90 years | C40-011 |
| 15 | Lattice corneal dystrophy IIIA: AR, mulberry-like appearance | C40-012 |
| 16 | Lattice dystrophies (merged cell): amyloid deposit: stained by Congo red | C40-013 |
| 17 | Gelatinous drop like dystrophy/Japanese: hyaline deposit: stained by Masson Trichome stain | C40-014 |
| 18 | Granular corneal dystrophy I / Groenaw granular corneal dystrophy II: hyaline + amyloid deposit | C40-015 |
| 19 | Macular dystrophy/Groenow II: AR, L/C corneal dystrophy | C40-016 |
| 20 | Francois central cloudy dystrophy: inborn error of keratin sulphate metabolism | C40-017 |
| 21 | Row group 4. Endothelial | C40-018 |
| 22 | Fuch's endothelial dystrophy: corneal guttata: wart-like excrescences | C40-018 |
| 23 | Posterior polymorphous corneal dystrophy: feature cell shows a dash (-) | C40-019 |
| 24 | Congenital hereditary endothelial dystrophy I and II: both have AR inheritance and have perinatal onset | C40-020 |

### Book p181 - 14 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Meesmann epithelial dystrophy figure: microcysts in corneal epithelium | C40-021 |
| 2 | Macular dystrophy figure: acid mucopolysaccharidosis deposits; Alcian blue stain | C40-022 |
| 3 | Lattice corneal dystrophy - Type 1: PAS stain: amorphous deposit | C40-023 |
| 4 | Lattice type 1: Congo red stain: apple green birefringence | C40-023 |
| 5 | Granular dystrophy: masson trichome stain: hyaline deposits | C40-024 |
| 6 | Granular dystrophy: bread crumb like granules separated by well-demarcated clear space | C40-025 |
| 7 | Fuch's endothelial dystrophy: mutation of COAXa gene (as handwritten) | C40-026 |
| 8 | Fuch's: Descemet membrane + endothelium damaged | C40-027 |
| 9 | Fuch's: wart-like excrescences on cornea | C40-027 |
| 10 | Figure caption: Corneal guttae (Diagnostic) | C40-028 |
| 11 | RECURRENT CORNEAL EROSIONS - Causes: 1. Cogan dystrophy | C40-029 |
| 12 | Recurrent corneal erosions: 2. Thiel Behnke dystrophy | C40-029 |
| 13 | Recurrent corneal erosions: 3. Reis Buckler dystrophy | C40-029 |
| 14 | Recurrent corneal erosions: 4. Lattice type I | C40-030 |

### Book p182 - 19 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | METABOLIC CAUSES OF DYSTROPHY: 1. Meesmann epithelial dystrophy | C40-031 |
| 2 | Metabolic causes: 2. Macular dystrophy | C40-031 |
| 3 | Metabolic causes: 3. Schnyder central crystalline dystrophy | C40-031 |
| 4 | TREATMENT OF CORNEAL DYSTROPHIES: if visual loss +: keratoplasty/corneal transplantation | C40-032 |
| 5 | Heading Keratoconus: form of corneal ectasia | C40-033 |
| 6 | Keratoconus: non-inflammatory, progressive, usually B/L | C40-033 |
| 7 | Etiology: 1. congenital weakness | C40-034 |
| 8 | Etiology 2. Associated with: trauma | C40-035 |
| 9 | Associated with: vernal keratoconjunctivitis | C40-035 |
| 10 | Associated with: Down syndrome | C40-035 |
| 11 | Clinical features 1. myopic astigmatism | C40-036 |
| 12 | 2. Hallmark: stromal thinning (central/paracentral) -> inferior to the centre | C40-037 |
| 13 | 3. Munson's sign: bulging of lower eyelid on downgaze | C40-038 |
| 14 | 4. Rizzuti's sign: light from temporal side -> arrowhead pattern of light over nasal limbus | C40-038 |
| 15 | 5. On retinoscopy: scissoring reflex | C40-039 |
| 16 | 6. On ophthalmoscopy: oil droplet reflex | C40-039 |
| 17 | 7. Vogt's striae: stromal stress lines | C40-040 |
| 18 | Figure captions: Munson's sign; Rizzuti's sign; Oil droplet reflex | C40-041 |
| 19 | Diagnosis: IOC: corneal topography | C40-042 |

### Book p183 - 18 source points, 13 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Keratoconus treatment: rigid contact lens (may lead to opacity) | C40-043 |
| 2 | Treatment: keratoplasty | C40-044 |
| 3 | Treatment: C3R (corneal collagen cross linking using riboflavin and UVA radiation) | C40-044, C40-045 |
| 4 | Heading Miscellaneous; Band shaped keratopathy: d/t deposits of calcium in Bowman's layer | C40-046 |
| 5 | Band shaped keratopathy treatment: chelation with EDTA (figure caption: Band shaped keratopathy) | C40-047 |
| 6 | Arcus senilis: occurs in old age | C40-048 |
| 7 | Arcus senilis: d/t lipid deposition on Descemet's membrane near periphery | C40-048 |
| 8 | Lucid interval of Vogt: clear zone of cornea b/w arcus and limbus (figure caption: Arcus senilis) | C40-049 |
| 9 | Interstitial keratitis: inflammation only of corneal stroma | C40-050 |
| 10 | Causes: congenital syphilis | C40-051 |
| 11 | Causes: Cogan syndrome (interstitial keratitis + deafness) | C40-052 |
| 12 | Causes: tuberculosis | C40-051 |
| 13 | Causes: Herpes Simplex Virus (HSV) | C40-051 |
| 14 | Heading Keratoplasty: AKA corneal transplantation | C40-053 |
| 15 | TYPES 1. Penetrating keratoplasty (full thickness) | C40-054 |
| 16 | 2. Lamellar keratoplasty (partial thickness) | C40-054 |
| 17 | Lamellar: DSEK (Descemet's stripping endothelial keratoplasty) | C40-055 |
| 18 | Lamellar: DALK (Deep anterior lamellar keratoplasty) | C40-055 |

### Book p184 - 14 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Table 'Removal of' - Penetrating keratoplasty: epithelium to endothelium (i.e. all 5 layers) | C40-056 |
| 2 | Removal of - DSEK: only endothelium & Descemet's membrane (i.e. posterior 2 layers) | C40-057 |
| 3 | Removal of - DALK: corneal tissue from epithelium upto stroma (i.e. anterior 3 layers) | C40-058 |
| 4 | Indication - Penetrating keratoplasty: pseudophakic bullous keratopathy | C40-059 |
| 5 | Indication - DSEK: dash (-) | C40-059 |
| 6 | Indication - DALK: acute hydrops in severe keratoconus | C40-059 |
| 7 | Table last row: cross-section diagrams for the three procedures | C40-060 |
| 8 | Procedure: host cornea cut using a trephine (diameter 7.5 mm) -> implant the graft cornea (diameter 0.25 mm larger than host opening) | C40-061, C40-062 |
| 9 | Figure captions: Trephine; Post-keratoplasty | C40-063 |
| 10 | Graft rejection: endothelial rejection (m/c) | C40-064 |
| 11 | Endothelial rejection forms Khodadoust line (diagnostic) | C40-064 |
| 12 | Storage media table - Short term: < 48 hrs; 4°C, moist chamber/McCarey Kaufman medium | C40-065 |
| 13 | Storage media - Intermediate term: < 2 weeks; feature dash (-) | C40-066 |
| 14 | Storage media - Long term: up to 35 days; cryopreservation (-70°C) | C40-067 |

## Chapter 41 - Anterior Uveitis (pp. 185-190): 76 questions, 9 units

### Book p185 - 18 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title ANTERIOR UVEITIS; heading Classification of Uveitis; Anatomical classification table: columns Anterior uveitis (AU) / Intermediate uveitis / Posterior uveitis / Pan uveitis | C41-001 |
| 2 | AKA row - Anterior uveitis: iridocyclitis | C41-001 |
| 3 | AKA row - Intermediate uveitis: pars planitis / posterior cyclitis | C41-001 |
| 4 | AKA row - Posterior uveitis: chorioretinitis / retinochoroiditis | C41-001 |
| 5 | AKA row - Pan uveitis: dash (-) | C41-002 |
| 6 | Involvement of - AU: iris: iritis; pars plicata: cyclitis | C41-003 |
| 7 | Involvement of - Intermediate uveitis: peripheral retina: basal retinochoroiditis; vitreous: vitritis/hyalitis | C41-004 |
| 8 | Involvement of - Posterior uveitis: choroid & retina | C41-005 |
| 9 | Involvement of - Pan uveitis: all layers of uvea | C41-005 |
| 10 | Clinical classification: Acute: duration < 3 months | C41-006 |
| 11 | Clinical classification: Chronic: duration > 3 months + relapse in < 3 months | C41-007 |
| 12 | Clinical classification: Recurrent: >= 3 months b/w 2 episodes | C41-008 |
| 13 | Etiological classification: granulomatous; non-granulomatous | C41-009 |
| 14 | Heading Clinical features of Anterior Uveitis; SYMPTOMS: pain: referred along branches of 5th nerve | C41-010 |
| 15 | Symptoms: redness | C41-011 |
| 16 | Symptoms: blurring of vision d/t corneal haze and aqueous turbidity | C41-011 |
| 17 | Symptoms: photophobia: severe | C41-012 |
| 18 | Symptoms: lacrimation | C41-012 |

### Book p186 - 21 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | SIGNS 1. Conjunctiva: circumcorneal congestion | C41-013 |
| 2 | 2. Cornea: corneal haze d/t raised intraocular pressure (IOP)/toxins | C41-014 |
| 3 | Keratic precipitates (KPs): cellular deposits on corneal endothelium | C41-015 |
| 4 | KPs location: Arlt's triangle (m/c) (figure: Keratic precipitates, label Arlt's triangle) | C41-015 |
| 5 | KP table - mutton fat: seen in granulomatous uveitis; contain macrophages | C41-016 |
| 6 | KP table - fine granules: seen in non-granulomatous uveitis; contain lymphocytes | C41-016 |
| 7 | KP table - pigmented: seen in chronic non-granulomatous uveitis; other features dash (-) | C41-017 |
| 8 | KP table - stellate: seen in herpetic uveitis, toxoplasmosis, Fuchs heterochromic iridocyclitis (FHI); star-shaped, diffuse distribution | C41-018 |
| 9 | Anterior chamber: 1. Aqueous cells: markers of disease activity | C41-019 |
| 10 | 2. Aqueous flare: turbidity of aqueous d/t leakage of proteins | C41-020 |
| 11 | Aqueous flare: visible d/t Tyndall effect/Brownian movement | C41-020 |
| 12 | Figure caption: Aqueous cells (labels: aqueous, cornea) | C41-021 |
| 13 | 3. Hypopyon: hypopyon + anterior uveitis: Behcet's disease | C41-022 |
| 14 | 4. Hyphema: hyphema + anterior uveitis: herpetic uveitis | C41-023 |
| 15 | Hyphema + AU: toxoplasmosis | C41-023 |
| 16 | Hyphema + AU: syphilis | C41-023 |
| 17 | Iris: 1. Pseudo-rubiosis: d/t dilated iris vessels | C41-024 |
| 18 | 2. Muddy iris: seen in acute cases | C41-025 |
| 19 | Muddy iris: AKA water logged iris | C41-025 |
| 20 | 3. Iris atrophy: seen in chronic cases | C41-026 |
| 21 | Iris atrophy types: sectoral: herpetic uveitis; diffuse: FHI (figure caption: Sectoral iris atrophy) | C41-026 |

### Book p187 - 12 source points, 9 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | 4. Iris nodules table - Location: Koeppe nodules: pupillary margin; Busacca nodules: iris stroma | C41-027 |
| 2 | Iris nodules table - Found in: Koeppe: granulomatous uveitis and non granulomatous uveitis; Busacca: granulomatous uveitis | C41-028 |
| 3 | Figure captions: Koeppe nodules; Busacca nodules | C41-029 |
| 4 | Pupil: 1. Miosis: acute cases | C41-030 |
| 5 | 2. Festooned pupil: chronic cases | C41-031 |
| 6 | Festooned pupil mechanism: exudation -> formation of incomplete posterior synechiae (adhesion b/w pupillary margin and lens) -> dilates the pupil -> irregular dilation (figure caption: Festooned pupil) | C41-031 |
| 7 | 3. Fixed pupil: recurrent cases | C41-032 |
| 8 | Fixed pupil: annular/ring/complete posterior synechiae (360° adhesion) -> no aqueous flow from posterior chamber to anterior chamber -> secondary angle closure glaucoma | C41-032 |
| 9 | 4. Total posterior synechiae (TPS): exudation in posterior chamber -> adhesion b/w posterior surface of iris and lens | C41-033 |
| 10 | 5. Cyclitic membrane: TPS + exudates leak behind lens | C41-034 |
| 11 | Cyclitic membrane: covers ciliary processes, equator & posterior surface of lens -> no aqueous secretion -> decreased IOP | C41-034 |
| 12 | 6. Occlusio pupillae: exudates organised across anterior surface of pupil (figure caption: Occlusio pupillae) | C41-035 |

### Book p188 - 20 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | IOP - Acute AU: raised IOP d/t trabecular meshwork blockage by cells and proteins + associated trabeculitis | C41-036 |
| 2 | IOP - Chronic AU: decreased IOP d/t cyclitic membrane + shut down of ciliary body | C41-037 |
| 3 | Heading Complications and Treatment of AU; Complications 1. Complicated cataract: m/c | C41-038 |
| 4 | Complicated cataract: bread crumb appearance + polychromatic lustre | C41-038 |
| 5 | Note: causes of complicated cataract, mnemonic UMAR: Uveitis | C41-039 |
| 6 | UMAR: Myopia | C41-039 |
| 7 | UMAR: Angle closure glaucoma | C41-040 |
| 8 | UMAR: Retinitis pigmentosa | C41-039 |
| 9 | 2. Secondary angle closure glaucoma: m/c in recurrent cases | C41-041 |
| 10 | 3. Band shaped keratopathy: calcium deposits in Bowman's layer of cornea | C41-042 |
| 11 | 4. Cystoid macular edema: m/c cause of visual loss d/t posterior involvement in anterior uveitis (AU) | C41-043 |
| 12 | Treatment: topical steroids: prednisolone | C41-044 |
| 13 | Topical steroids: difluprednate | C41-044 |
| 14 | Antimetabolites: azathioprine | C41-044 |
| 15 | Azathioprine: given if inflammation + recurrent episodes requiring long term steroids | C41-045 |
| 16 | Cycloplegics: atropine; action: relax ciliary muscle -> pain relief | C41-046 |
| 17 | Atropine action: break posterior synechiae | C41-046 |
| 18 | Atropine action: prevent formation of posterior synechiae | C41-046 |
| 19 | Note: side effects of steroids: topical administration: glaucoma | C41-047 |
| 20 | Side effects of steroids: systemic administration: cataract | C41-047 |

### Book p189 - 18 source points, 16 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Causes of Anterior Uveitis; GRANULOMATOUS a. Tuberculosis | C41-048 |
| 2 | b. Leprosy: m/c: lepromatous leprosy | C41-049 |
| 3 | Leprosy: iris pearls: pathognomonic feature | C41-049 |
| 4 | c. Sarcoidosis: m/c ocular manifestation of sarcoidosis: granulomatous anterior uveitis | C41-050 |
| 5 | Sarcoidosis: Lofgren syndrome: erythema nodosum + B/L lymphadenopathy + anterior uveitis | C41-051 |
| 6 | Sarcoidosis: Heerfordt syndrome/uveoparotid fever | C41-052 |
| 7 | d. Syphilis: m/c in late congenital syphilis | C41-053 |
| 8 | Syphilis presentation: iris roseolas | C41-053 |
| 9 | e. Herpes: AU + raised IOP + hyphema + stellate KPs + sectoral iris atrophy | C41-054 |
| 10 | 2. NON GRANULOMATOUS - Acute: 1. Idiopathic: m/c | C41-055 |
| 11 | 2. HLA B27 associated disease: ankylosing spondylitis: lower back pain + stiffness + recurrent U/L AU | C41-056 |
| 12 | Reiter's disease: triad (conjunctivitis, urethritis, arthritis) | C41-057 |
| 13 | Reiter's: + U/L AU + keratoderma blenorrhagicum + circinate balanitis + history of travel | C41-058 |
| 14 | Psoriatic arthritis: sausage digits + B/L AU | C41-059 |
| 15 | 3. Behcet's disease: A/w HLA B5, B51 | C41-060 |
| 16 | Behcet's: B/L recurrent AU + cold mobile hypopyon + aphthous mouth ulcers | C41-061 |
| 17 | 4. Inflammatory bowel disease: ulcerative colitis (12%) > Crohn's disease (2.4%) | C41-062 |
| 18 | 5. Drug induced uveitis (list continues on next page) | C41-063 |

### Book p190 - 18 source points, 13 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Mnemonic: CML Please Relapse Slowly - Cidofovir, metipranolol, Latanoprost | C41-064 |
| 2 | Mnemonic drug: pilocarpine | C41-065 |
| 3 | Mnemonic drug: rifabutin | C41-065 |
| 4 | Mnemonic drug: sulfonamides | C41-065 |
| 5 | Chronic: Juvenile Idiopathic Arthritis (JIA): m/c cause of AU in paediatric age group | C41-066 |
| 6 | JIA types: pauciarticular: <= 4 joints involved | C41-067 |
| 7 | JIA types: polyarticular: > 4 joints involved | C41-067 |
| 8 | JIA types: Stills disease | C41-068 |
| 9 | Pauciarticular type 1: m/c in females; m/c a/w AU | C41-069 |
| 10 | Pauciarticular type 1: RF -ve (seronegative); ANA +ve | C41-070 |
| 11 | Pauciarticular type 2: m/c in males | C41-071 |
| 12 | 2. Fuch's Heterochromic Iridocyclitis (FHC): clinical features mnemonic NO FUCHS: No posterior synechiae | C41-072 |
| 13 | NO FUCHS: Floaters | C41-073 |
| 14 | NO FUCHS: Unilateral | C41-073 |
| 15 | NO FUCHS: Cataract | C41-073 |
| 16 | NO FUCHS: Heterochromia iridis: hypochromia in the affected eye d/t loss of iris crypts | C41-074 |
| 17 | NO FUCHS: Stellate keratic precipitates | C41-075 |
| 18 | Amsler's sign: bleeding on paracentesis | C41-076 |

## Chapter 42 - Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders (pp. 191-194): 48 questions, 9 units

### Book p191 - 19 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title INTERMEDIATE, POSTERIOR, PAN-UVEITIS AND MISCELLANEOUS DISORDERS; heading Intermediate Uveitis: also known as pars planitis | C42-001 |
| 2 | Causes: 1. Idiopathic (m/c) | C42-002 |
| 3 | Causes: 2. Associated with: Lyme's disease | C42-003 |
| 4 | Associated with: sarcoidosis | C42-003 |
| 5 | Associated with: multiple sclerosis | C42-003 |
| 6 | Associated with: tuberculosis | C42-003 |
| 7 | Clinical features - symptoms: B/L floaters | C42-004 |
| 8 | Symptoms: blurring of vision | C42-004 |
| 9 | Signs: spillover anterior uveitis | C42-005 |
| 10 | Signs: snowballs: aggregation of cells in vitreous | C42-006 |
| 11 | Treatment: steroids: posterior subtenon injection; if fails -> steroids: systemic | C42-007 |
| 12 | If fails -> immunomodulatory drugs: azathioprine | C42-008 |
| 13 | If fails -> pars plana vitrectomy + photocoagulation of snowbank | C42-009 |
| 14 | Snowbanking: fibrovascular plaque | C42-010 |
| 15 | Cystoid macular edema: m/c cause of vision loss | C42-011 |
| 16 | Heading Posterior Uveitis/Chorioretinitis: inflammation of choroid & retina | C42-012 |
| 17 | Clinical features: 1. Floaters; 2. Painless loss of vision; 3. Scotoma | C42-013 |
| 18 | Clinical features: 4. Metamorphopsia: distortion of image | C42-014 |
| 19 | Clinical features: 5. Photopsia | C42-014 |

### Book p192 - 19 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Causes table (Infectious / Non-infectious) - Infectious 1. Most common: toxoplasmosis | C42-015 |
| 2 | Toxoplasmosis a. Active: headlight in fog appearance (d/t associated active vitritis) (figure A, B) | C42-016 |
| 3 | Toxoplasmosis b. Chronic: punched out scar (figure) | C42-016 |
| 4 | Cats are definitive hosts | C42-017 |
| 5 | Toxoplasmosis causes focal chorioretinitis | C42-017 |
| 6 | 2. Toxocariasis: unilateral LOV | C42-018 |
| 7 | Toxocariasis: leukocoria (white pupillary reflex) | C42-018 |
| 8 | 3. CMV retinitis: m/c cause of LOV in ocular HIV | C42-019 |
| 9 | CMV retinitis a. Pizza pie appearance | C42-020 |
| 10 | CMV retinitis b. Scrambled egg & ketchup appearance (figure) | C42-020 |
| 11 | CMV retinitis c. Brushfire extension (figure) | C42-020 |
| 12 | 4. TB | C42-021 |
| 13 | Non-infectious 1. Sarcoidosis: candle wax dripping appearance (d/t perivascular inflammation & sheathing) (figures) | C42-022 |
| 14 | Sarcoidosis: Lander's sign: pre-retinal nodules | C42-023 |
| 15 | 2. Behcet's disease | C42-024 |
| 16 | 3. Birdshot chorioretinopathy: HLA A29 association | C42-025 |
| 17 | 4. Serpiginous choroiditis: HLA B7 association | C42-025 |
| 18 | Focal chorioretinitis: Toxoplasma, Toxocariasis, CMV | C42-026 |
| 19 | Multifocal chorioretinitis: HSV, TB, syphilis | C42-026 |

### Book p193 - 16 source points, 12 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Treatment: 1. Infectious cases: treat the cause + systemic steroids | C42-027 |
| 2 | Treatment: 2. Non-infectious cases: systemic steroids OR | C42-028 |
| 3 | Adalimumab (visual studies I to II) | C42-028 |
| 4 | Sirolimus (Sakura program) | C42-028 |
| 5 | Voclosporin (Luminate trials) | C42-028 |
| 6 | Heading Pan-uveitis; Causes: 1. Vogt-Koyanagi-Harada (VKH) syndrome: affects eye, ears, skin, meninges | C42-029 |
| 7 | VKH eye: B/L granulomatous panuveitis | C42-030 |
| 8 | VKH eye: sunset glow fundus: RPE atrophy | C42-031 |
| 9 | VKH eye: Suiguira sign: perilimbal vitiligo | C42-032 |
| 10 | VKH eye: exudative RD | C42-033 |
| 11 | VKH ears: tinnitus; skin: vitiligo; meninges: meningoencephalitis | C42-034 |
| 12 | 2. Sympathetic ophthalmitis: clinical feature: granulomatous panuveitis | C42-035 |
| 13 | Sympathetic ophthalmitis cause: accidental penetrating trauma affecting ciliary body | C42-035 |
| 14 | Pathogenesis: trauma to one eye (exciting eye) -> >2 weeks -> sympathetic ophthalmitis in other eye (sympathizing eye) | C42-036 |
| 15 | Prevention: enucleation of traumatic eye in 14 days | C42-037 |
| 16 | Treatment: steroids | C42-038 |

### Book p194 - 14 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Miscellaneous; table Enucleation / Evisceration / Exenteration; Terminology - enucleation: removal of whole eyeball + optic nerve | C42-039 |
| 2 | Terminology - evisceration: removal of all layers of eyeball except sclera | C42-039 |
| 3 | Terminology - exenteration: removal of eye and orbital contents | C42-039 |
| 4 | Indications - enucleation: retinoblastoma; trauma | C42-040 |
| 5 | Indications - evisceration: endophthalmitis | C42-041 |
| 6 | Indications - exenteration: orbital mucormycosis; tumors metastasised to orbit | C42-042 |
| 7 | C/I - enucleation: panophthalmitis | C42-043 |
| 8 | C/I - evisceration: retinoblastoma | C42-043 |
| 9 | C/I - exenteration: dash (-) | C42-043 |
| 10 | Appearance row: photographs of the three procedures | C42-044 |
| 11 | Gyrate atrophy: type of choroid atrophy | C42-045 |
| 12 | Gyrate atrophy: autosomal recessive | C42-046 |
| 13 | Gyrate atrophy: mutation in ornithine aminotransferase gene: increased levels of ornithine | C42-047 |
| 14 | Gyrate atrophy treatment: arginine restriction in diet (ornithine is synthesised from arginine) | C42-048 |

## Totals

- Source points: 550, all covered (0 uncovered)
- Questions: 409
