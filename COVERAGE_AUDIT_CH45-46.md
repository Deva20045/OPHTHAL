# Coverage audit - Chapters 45-46 (Book pp. 209-219)

Every source line, heading, table row, figure caption and bracket read from the scanned pages is listed as a numbered point, in book order, with the question ID(s) that test it. `authoring/lib.py::finish()` refuses to write a chapter unless every point is covered, questions are in (page, first-point) order, each question has 4 distinct options and the answer is not length-predictable.

## Chapter 45 - Anatomy of Orbit and Proptosis (pp. 209-214): 48 questions, 4 units

### Book p209 - 16 source points, 11 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title: Anatomy of Orbit and Proptosis; orbit is the bony cage surrounding the eye | C45-001 |
| 2 | Roof of orbit: frontal bone and lesser wing of sphenoid | C45-001 |
| 3 | Lateral wall: zygomatic bone and greater wing of sphenoid | C45-001 |
| 4 | Floor: maxilla, zygomatic bone, palatine bone; most common wall to fracture, causing blow-out fracture | C45-001, C45-002 |
| 5 | Medial wall: thinnest wall, lamina papyracea; mnemonic SMEL | C45-003, C45-004 |
| 6 | SMEL medial wall bones: sphenoid body; maxilla frontal process; ethmoid bone; lacrimal bone | C45-004 |
| 7 | Eyeball naturally protrudes slightly from lateral wall of orbit | C45-005 |
| 8 | Orbit schematic: medial walls parallel, separating the orbits from nasal cavities; distance between medial walls 2.5 cm | C45-006 |
| 9 | Orbit schematic: lateral walls are 90 degrees to each other and 45 degrees to medial walls | C45-007 |
| 10 | Apex of orbit: 90 degrees; annulus of Zinn contains origin of all extraocular muscles except inferior oblique | C45-008 |
| 11 | Bones forming orbit diagram labels frontal, sphenoid, zygomatic, maxilla, nasal, lacrimal, ethmoid and palatine bones | C45-001 |
| 12 | Bones diagram also labels supraorbital margin/foramen, superior orbital fissure, optic canal, infraorbital foramen and lacrimal fossa | C45-009 |
| 13 | Three openings into orbital apex: optic canal; superior orbital fissure; inferior orbital fissure | C45-009, C45-010, C45-011 |
| 14 | Superior orbital fissure lies between roof and lateral wall; inferior orbital fissure lies between floor and lateral wall | C45-009, C45-010 |
| 15 | Structures through annulus of Zinn: optic nerve (II), ophthalmic artery, superior and inferior divisions of oculomotor (III), nasociliary (V1), abducens (VI) | C45-011 |
| 16 | Orbital opening diagram labels lacrimal and frontal branches of V1, trochlear nerve (IV), levator palpebrae superioris, superior oblique, and superior/inferior ophthalmic veins | C45-011 |

### Book p210 - 12 source points, 8 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Proptosis/exophthalmos: protrusion of eyeball from lateral orbital rim; >21 mm or 2 mm difference between the eyes | C45-012 |
| 2 | Proptosis measurement uses an exophthalmometer; distance is measured from lateral orbital rim to anterior cornea | C45-013 |
| 3 | Hertel exophthalmometer measures both eyes together and is preferred overall | C45-014 |
| 4 | Luedde exophthalmometer measures one eye at a time and is preferred in children | C45-014 |
| 5 | Bilateral painless proptosis causes: Graves disease, cortico-cavernous fistula, leukemia/AML in children | C45-015 |
| 6 | Bilateral painful proptosis causes: cavernous sinus thrombosis (CST), Graves disease with painful restriction of ocular movement | C45-015 |
| 7 | Unilateral axial proptosis: along the visual axis, outward straight protrusion | C45-016 |
| 8 | Unilateral axial painful causes: orbital cellulitis and CST | C45-017 |
| 9 | Unilateral axial painless causes: optic nerve glioma and cavernous hemangioma | C45-017 |
| 10 | Unilateral abaxial proptosis: away from visual axis; direction depends on cause | C45-018 |
| 11 | Abaxial inferomedial displacement: superotemporal lesions, lacrimal gland tumours, dermoid cysts | C45-018 |
| 12 | Abaxial upward displacement: maxillary sinus tumour; lateral displacement: lacrimal sac lesion | C45-019 |

### Book p211 - 10 source points, 6 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Most common adult cause of unilateral or bilateral proptosis: Graves disease; may be unilateral or bilateral | C45-020 |
| 2 | Children: unilateral proptosis commonly orbital cellulitis; bilateral proptosis leukemia/AML | C45-021 |
| 3 | Cavernous sinus thrombosis involves CN III, IV, VI, V1 and V2; orbital apex syndrome involves structures through superior orbital fissure and optic canal (CN II, III, IV, V1, VI) | C45-022 |
| 4 | CST causes sequential ophthalmoplegia: VI first, then III, then IV; orbital apex syndrome causes concurrent ophthalmoplegia with actions lost together | C45-022 |
| 5 | Ophthalmic nerve (V1) palsy/corneal anaesthesia is present in both CST and orbital apex syndrome | C45-023 |
| 6 | Visual loss: CST has no initial loss but may develop late from other causes; orbital apex syndrome has complete loss of vision | C45-024 |
| 7 | Mastoid-area edema due to CN V palsy: present in CST, absent in orbital apex syndrome | C45-025 |
| 8 | CST: bilateral, marked/severe chemosis and proptosis; orbital apex syndrome: unilateral, mild | C45-025 |
| 9 | Systemic signs such as fever are marked in CST and mild in orbital apex syndrome | C45-025 |
| 10 | Presentation: CST always bilateral, starting unilateral; orbital apex syndrome always unilateral | C45-025 |

### Book p212 - 12 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Orbital cellulitis causes: extension of paranasal sinusitis (most common), exogenous/trauma, hematogenous spread | C45-026 |
| 2 | Ethmoid sinusitis is the most common sinus source; Staphylococcus and Streptococci are common etiologic agents | C45-026, C45-027 |
| 3 | Orbital cellulitis is common in children with upper respiratory tract infection | C45-026 |
| 4 | Progression if untreated: preseptal cellulitis to orbital cellulitis to subperiosteal abscess | C45-028 |
| 5 | Preseptal cellulitis findings: eyelid edema, pain, inability to open eye; treatment topical/oral antibiotics | C45-029 |
| 6 | Orbital cellulitis findings: proptosis and limitation of eye movement; treat with IV antibiotics | C45-029 |
| 7 | Orbital cellulitis complication: optic nerve compression may cause blindness | C45-030 |
| 8 | Orbital septum formed by eyelid muscles, fascia, medial and lateral canthal ligaments; separates orbit from pre-orbital area into preseptal and postseptal compartments | C45-031 |
| 9 | Carotico-cavernous fistula (CCF) is an arteriovenous fistula between carotid artery and cavernous sinus | C45-032 |
| 10 | CCF is traumatic in 75% of cases or spontaneous | C45-033 |
| 11 | CCF proptosis is bilateral and pulsatile; bruit and thrill stop with pressure on ipsilateral carotid artery | C45-034 |
| 12 | CCF ophthalmoplegia first affects CN VI; investigation of choice is digital subtraction carotid angiography (DSCA) | C45-035 |

### Book p213 - 12 source points, 7 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Most common causes summary: adults Graves disease; children unilateral orbital cellulitis, bilateral leukemia/AML | C45-036 |
| 2 | Orbital varices are congenital enlargement of pre-existing venous channels | C45-036 |
| 3 | Orbital varix features: unilateral proptosis, bag-of-worms consistency, non-pulsatile, no bruit or thrill | C45-037 |
| 4 | Orbital varix complication: orbital hemorrhage/thrombosis | C45-038 |
| 5 | Intermittent proptosis on Valsalva or bending forward: orbital varices | C45-038 |
| 6 | Intermittent proptosis with upper respiratory infection: orbital lymphangioma | C45-038 |
| 7 | Intermittent proptosis on crying: capillary hemangioma in children; encephalocele in infants | C45-039 |
| 8 | Pulsatile proptosis causes: cortico-cavernous fistula; orbital roof fracture in NF-1 or trauma | C45-040 |
| 9 | Pseudo-proptosis means appearance of eyeball protrusion without true proptosis | C45-040 |
| 10 | Pseudo-proptosis causes: upper eyelid retraction (may be apraclonidine side effect); contralateral enophthalmos (trauma, Horner syndrome); axial length >26 mm; buphthalmos | C45-040 |
| 11 | Thyroid-associated ophthalmology: most common cause of unilateral and bilateral proptosis in adults; may occur in any state of thyroid activity | C45-041 |
| 12 | TAO pathogenesis: inflammation enlarges extraocular muscles; inflammation/infiltration of orbital fat pushes eyeball forward causing frank proptosis | C45-042 |

### Book p214 - 11 source points, 6 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Goldzeieher's sign is the earliest TAO sign: congestion/hyperemia | C45-043 |
| 2 | Dalrymple sign (most common): upper eyelid retraction causing pseudo-proptosis due to constriction of Müller's muscle; seen in 92% | C45-043, C45-044 |
| 3 | Proptosis is second most common TAO feature, axial unilateral or bilateral, seen in 60% | C45-043 |
| 4 | Von Graefe sign: lid lag on downgaze, upper eyelid does not move down | C45-045 |
| 5 | Kocher's sign: staring/startled appearance | C45-045 |
| 6 | Stellwag sign: reduced eyelid blinking due to upper eyelid retraction | C45-045 |
| 7 | Restrictive squint from extraocular muscle fibrosis causes loss of movement; inferior rectus affected first, so elevation is first affected | C45-046 |
| 8 | Clinical photos label Dalrymple sign, proptosis and von Graefe sign (eyeball down with eyelid lagging) | C45-047 |
| 9 | TAO complication: exposure keratitis due to inability to close eye | C45-047 |
| 10 | TAO management: ensure euthyroid state; lubricants for exposure keratitis | C45-047, C45-048 |
| 11 | Supportive TAO treatment: Botox injection into Müller's muscle for upper lid retraction; systemic steroids for inflammation | C45-048 |

## Chapter 46 - Lacrimal apparatus : Anatomy, Watering eye and Dry eye (pp. 215-219): 38 questions, 5 units

### Book p215 - 12 source points, 6 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title: Lacrimal apparatus: anatomy, watering eye and dry eye; tears have secretion and drainage pathways | C46-001 |
| 2 | Main lacrimal gland is divided by levator palpebrae superioris | C46-001 |
| 3 | Orbital part of lacrimal gland is superior; palpebral part is inferior | C46-001 |
| 4 | Main lacrimal gland has main excretory ducts; function is reflex tear secretion | C46-002 |
| 5 | Accessory lacrimal glands of Krause and Wolfring lie in fornix between sclera and palpebral conjunctiva | C46-002, C46-003 |
| 6 | Krause and Wolfring accessory glands provide basal tear secretion | C46-002 |
| 7 | Parasympathetic lacrimal secretomotor centre: superior salivatory nucleus in pons | C46-004 |
| 8 | Preganglionic parasympathetic pathway: greater superficial petrosal nerve, branch of facial nerve | C46-004 |
| 9 | Parasympathetic pathway synapses in pterygopalatine ganglion | C46-004 |
| 10 | Postganglionic pathway: zygomatic nerve, branch of maxillary division of trigeminal, stimulates lacrimal gland secretion | C46-004 |
| 11 | Sympathetic innervation of lacrimal gland has inhibitory function | C46-005 |
| 12 | Lacrimal apparatus figure labels main gland, orbital part, palpebral part, excretory ducts and drainage structures | C46-006 |

### Book p216 - 12 source points, 8 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Drainage: upper and lower puncta lead to upper and lower canaliculi, then lacrimal sac | C46-007 |
| 2 | Lacrimal sac is surrounded by orbicularis oculi; blinking assists drainage | C46-008 |
| 3 | Nasolacrimal duct opens into inferior meatus of nose | C46-007, C46-009 |
| 4 | Opening of nasolacrimal duct is guarded by valve of Hasner; commonest congenital dacryocystitis block | C46-009, C46-010 |
| 5 | Watering eye from hyperlacrimation: increased tear secretion due to emotional stress or inflammation | C46-011 |
| 6 | Epiphora is watering due to blockage of tear drainage | C46-011 |
| 7 | Testing watering eye instruments: Nettleship punctum dilator, 26-gauge bent needle cannula and Bowman's lacrimal probe | C46-012 |
| 8 | Syringing: after punctal dilation, blunt 26-gauge needle enters punctum and canaliculus; saline is injected | C46-013 |
| 9 | Fluid reaching nose and throat indicates patent drainage; consider hypersecretion, lacrimal pump failure or partial obstruction (Jones dye test) | C46-013 |
| 10 | Regurgitation of fluid during syringing indicates obstruction/blockage; proceed to probing | C46-014 |
| 11 | On probing, hard stop indicates nasolacrimal duct blockage | C46-014 |
| 12 | On probing, soft stop indicates lacrimal sac or canalicular block | C46-014 |

### Book p217 - 11 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Jones dye test I: 2% fluorescein is instilled into conjunctival sac; cotton is placed at opening of NLD | C46-015 |
| 2 | Jones I: stained cotton bud is positive and indicates hypersecretion | C46-016 |
| 3 | Jones I: no staining is negative; irrigate residual fluorescein and perform Jones dye test II | C46-017 |
| 4 | Jones II: stained bud after irrigation is positive and indicates partial NLD obstruction | C46-017 |
| 5 | Jones II negative with no staining: lacrimal pump failure or partial canalicular obstruction | C46-018 |
| 6 | Dacryocystitis is inflammation of lacrimal sac | C46-019 |
| 7 | Congenital dacryocystitis: watering since birth due to non-canalization of NLD; commonest obstruction at valve of Hasner | C46-020 |
| 8 | Congenital dacryocystitis treatment: lacrimal sac massage and topical tobramycin/erythromycin | C46-021 |
| 9 | Age-based congenital treatment: 9-12 months syringing; >1 year probing; >4 years dacryocystorhinostomy (DCR) | C46-022 |
| 10 | Acquired dacryocystitis cause listed: Streptococcus hemolyticus | C46-023 |
| 11 | Acquired dacryocystitis treatment: oral antibiotics; DCR if fistula is positive | C46-023, C46-024 |

### Book p218 - 14 source points, 8 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Lacrimal gland tumours: pleomorphic adenoma is benign | C46-025 |
| 2 | Adenoid cystic carcinoma of lacrimal gland is malignant | C46-025 |
| 3 | Both lacrimal gland tumour types displace the eye downward and medially due to gland location | C46-026 |
| 4 | Tear film innermost layer: mucin from goblet cells | C46-027 |
| 5 | Tear film middle layer: aqueous from lacrimal glands | C46-027 |
| 6 | Tear film outermost layer: lipid from meibomian gland, prevents evaporation of aqueous | C46-027, C46-028 |
| 7 | Corneal epithelium with microvilli is labelled under the tear film layers | C46-027 |
| 8 | Aqueous deficiency: keratoconjunctivitis sicca; example Sjögren syndrome | C46-029 |
| 9 | Lipid deficiency: evaporative dry eye; examples meibomian gland disease and contact lens wearer | C46-029 |
| 10 | Mucin deficiency example: vitamin A deficiency | C46-029 |
| 11 | Schirmer test is quantitative measurement of tear production using Whatman's filter paper No. 41 | C46-030 |
| 12 | Schirmer procedure: filter strip inserted in lower fornix for 5 minutes; measure wet length | C46-031 |
| 13 | Schirmer wetting >15 mm is normal; <10 mm indicates dry eye | C46-031, C46-032 |
| 14 | Schirmer test illustrations label Whatman's filter paper and test procedure | C46-030 |

### Book p219 - 8 source points, 6 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | TBUT: instill 2% fluorescein in conjunctival sac and illuminate with blue light | C46-033 |
| 2 | TBUT is interval between a blink and appearance of first dry spot on cornea | C46-034 |
| 3 | TBUT <10 seconds suggests mucin deficiency | C46-035 |
| 4 | A dry spot at a particular location suggests corneal disease | C46-036 |
| 5 | Phenol red thread test: thread impregnated with phenol red dye is yellow before tears and red after contact with tears | C46-037 |
| 6 | Phenol red thread is placed in lower fornix | C46-038 |
| 7 | Phenol red thread test <6 mm indicates dry eye; >15 mm is normal | C46-038 |
| 8 | Phenol red thread test diagram labels thread placement in lower fornix | C46-038 |

## Totals

- Source points: 130, all covered (0 uncovered)
- Questions: 86
