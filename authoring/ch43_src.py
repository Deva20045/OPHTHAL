from lib import Chapter

# Read from the scanned book. NOTE (scan quirk): PDF pages 88 and 89 carry the
# leaves printed "202" and "201" respectively, i.e. the two leaves are out of
# order in the scan file.  The printed numbers are the citation anchor, so this
# chapter is authored in printed-page order 195 ... 205, where the content flows
# correctly (p201 = FISTO + ophthalmia neonatorum; p202 = prophylaxis of
# ophthalmia neonatorum + allergic conjunctivitis).
POINTS = {
195: [
 "Chapter title ANATOMY OF CONJUNCTIVA, TYPES OF CONJUNCTIVITIS AND PTERYGIUM; heading Anatomy (00:00:50)",
 "Conjunctiva is transparent mucous membrane",
 "It does not cover cornea",
 "Parts of conjunctiva: Bulbar (covers sclera)",
 "Parts: Forniceal",
 "Parts: Palpebral (lines inner surface of eyelids)",
 "Plica semilunaris: represents nictitating membrane",
 "Caruncle: contains hair follicles",
 "Plica semilunaris & caruncle: labelled together as rudimentary structures",
 "Histology: 1. Outermost layer: epithelium (non-keratinised stratified squamous)",
 "Contains a. Goblet cells: secrete mucin (forms innermost layer of tear film) on parasympathetic stimulation",
 "Contains b. melanocytes",
 "Contains c. Langerhans cells",
 "2. Adenoid/lymphatic layer: develops after 3 months of age",
 "3. Fibrous layer: contains nerve fibres & blood vessels",
],
196: [
 "Lymphatic drainage: only site of lymphatic drainage from the eye",
 "Drainage medially -> submandibular lymph nodes",
 "Drainage laterally -> peri-auricular & superficial parotid lymph nodes",
 "Drainage schematic of the eye/face (label: drainage medially and laterally)",
 "Heading Conjunctivitis (00:08:40); aka eye flu",
 "Symptoms: redness",
 "Symptoms: discharge sticking to eyelids",
 "Symptoms: foreign body sensation",
 "Symptoms: lacrimation",
 "Symptoms: itching (if allergic)",
 "Symptoms: pain and loss of vision (LOV): corneal involvement",
 "Signs: 1. Conjunctival hyperemia (redness)",
 "DD of circumcorneal redness: glaucoma",
 "circumcorneal redness: uveitis",
 "circumcorneal redness: corneal ulcer",
 "Photograph caption: Conjunctival hyperemia",
 "Photograph + note: Circumcorneal hyperemia - seen in glaucoma, uveitis, corneal ulcer",
],
197: [
 "2. Subconjunctival hemorrhage: no treatment required (resolves spontaneously in ~2 weeks)",
 "3. Chemosis: swelling of bulbar conjunctiva",
 "4. Discharge: mucopurulent/watery",
 "Discharge causes colored halos & stickiness which resolves on washing eye",
 "5. Inflammatory reactions of conjunctiva: Papillae: hypertrophied vessels",
 "Follicles: lymphoid aggregates",
 "Etiology table: mucopurulent discharge - papillary reaction: Bacterial; follicular reaction: Chlamydia",
 "Etiology table: watery discharge - papillary reaction: Allergic; follicular reaction: viral",
 "Heading Bacterial conjunctivitis (00:17:22)",
 "Acute mucopurulent conjunctivitis: m/c cause Staphylococcus aureus",
 "Treatment: topical antibiotics",
],
198: [
 "Heading Acute purulent/hyperacute conjunctivitis/Blenorrhoea",
 "m/c cause: Neisseria gonorrhoeae",
 "Route of transmission: Oculogenital",
 "Clinical features: 1. Copious purulent discharge",
 "2. Swelling of eyelids -> Overhanging",
 "3. Intense pain",
 "4. Pre-auricular lymphadenopathy",
 "Treatment: IM Ceftriaxone 1g single dose",
 "followed by Oral erythromycin x 2 weeks",
 "Photograph caption: Blennorrhoea",
 "Heading Acute membranous conjunctivitis: m/c cause overall/in adults: Pneumococcus",
 "m/c cause in unimmunised children: Corynebacterium diphtheriae",
 "Clinical features: membrane formed -> fused with epithelium -> bleeds on removal",
 "Heading Acute pseudomembranous conjunctivitis: membrane does not fuse with epithelium",
 "No bleeding on removal",
 "Photograph caption: Pseudomembrane peeling",
 "Heading Angular/diplobacillary conjunctivitis: m/c cause moraxella lacunata/axenfeld",
 "Clinical features: excoriation at canthi (Lateral > medial)",
 "Clinical features: redness at intermarginal strip",
 "Clinical features: blepharitis (inflammation of eyelid margin)",
 "Treatment: tetracycline 1% eye ointment for >= 2 wks",
 "Treatment: zinc boric eye drops (zinc blocks proteolytic activity)",
],
199: [
 "Heading Viral Conjunctivitis (00:27:00); adenoviral conjunctivitis",
 "Non-specific follicular conjunctivitis: serovars 1 to 11 & 19",
 "Epidemic keratoconjunctivitis (EKC): serovars 8, 19, 37",
 "Pharyngoconjunctival fever (PCF): serovars 3, 4, 7",
 "Pharyngoconjunctival fever: associated with preauricular lymphadenopathy",
 "Apollo conjunctivitis/Acute hemorrhagic conjunctivitis: hemorrhage of palpebral & bulbar conjunctiva",
 "Photograph: acute hemorrhagic (Apollo) conjunctivitis of both eyes",
 "Causes: 1. Picornavirus: Enterovirus type 70, Coxsackie A24 (m/c)",
 "Causes: 2. Adenovirus type 11",
 "molluscum contagiosum clinical features: unilateral, painless nodule with umbilicated appearance",
 "Nodule contains viral particles",
 "Periodic shedding of virus -> conjunctivitis",
 "Treatment: surgical excision [if cosmetic indication (+)]",
 "Photograph caption: umbilicated nodule",
 "Heading Chlamydial Conjunctivitis (00:33:14): Adult inclusion conjunctivitis: D to K serovars",
 "Trachoma: A, B, Ba, C serovars",
 "Ophthalmia neonatorum: D to K serovars; other causes",
 "TRACHOMA aka Egyptian ophthalmia",
 "Route of transmission: mnemonic: 3F",
 "1. Fingers",
 "2. Flies",
 "3. Fomites",
],
200: [
 "Pathology: Type IV hypersensitivity reaction: active inflammation + cicatrization",
 "Age group: < 10 yrs",
 "Clinical signs: 1. Sago grain follicles: necrosis & Leber",
 "m/c site: upper palpebral conjunctiva",
 "Necrosis & Leber cells seen",
 "Photograph caption: Sago grain follicles",
 "2. Cicatricial sign: a. Arlt's line: line of cicatrization",
 "Photograph labels: Arlt's line - lower 2/3rd, upper 1/3rd",
 "b. Herbert's pits: pathognomonic",
 "d/t healing of limbal follicles",
 "Photograph label: Herbert's pits",
 "c. Pannus: vascularisation of cornea superiorly",
 "Complications: trichiasis (inturned eyelash) -> corneal ulcer -> scar formation -> loss of vision",
 "Treatment: SAFE strategy (WHO, 1996)",
 "Surgery for inturned eyelids",
 "Antibiotics: Azithromycin 1g",
 "Facial cleanliness",
 "Environmental change",
 "Indications for treatment: prevalence in 1-9 yr old children > 10% -> mass prophylaxis",
 "Prevalence 5-10% -> treatment to affected children & family",
 "Prevalence < 5% -> facial cleanliness & environmental change advised",
],
201: [
 "FISTO classification (WHO): TF: Trachomatous inflammation follicular: > 5 follicles +; active stage, treatment: antibiotics",
 "TI: Trachomatous inflammation intense: thickening of upper palpebral conjunctiva; active stage (antibiotics)",
 "TS: Trachomatous scarring: Arlt's line; inactive stage: no treatment",
 "TT: Trachomatous trichiasis: eyelash growing inwards; requires surgery",
 "CO: Corneal opacity: visual impairment; management -",
 "Photograph captions: trachomatous inflammation follicular (TF), follicular and intense (TF), trachomatous scarring (TS), trachomatous trichiasis (TT), corneal opacity (CO)",
 "Heading OPHTHALMIA NEONATORUM: conjunctivitis in neonates (< 28 days of onset)",
 "Onset within first 6h: chemical conjunctivitis (silver nitrate)",
 "Onset 24 to 48h: Neisseria gonorrhoeae (most severe)",
 "Onset 2 to 5 d: other bacteria",
 "Onset 5 to 7 d: HSV-II",
 "Onset > 1 wk: Chlamydia trachomatis (D to K): m/c",
 "Photograph caption: Ophthalmia neonatorum",
],
202: [
 "Prevention: 1. Crede's method: topical 1% silver nitrate (not recommended d/t chemical conjunctivitis)",
 "Prevention: 2. 0.5% erythromycin; 3. 1% tetracycline",
 "Both: single application",
 "Both: within 1 hr of birth",
 "Heading Allergic conjunctivitis (00:50:24); presents with papillae reaction + watery discharge + itching",
 "VERNAL KERATOCONJUNCTIVITIS/SPRING CATARRH: Type I hypersensitivity reaction (eg: pollen)",
 "Incidence: age 5-15 yrs",
 "Incidence: males > females (young boys)",
 "Incidence: m/c in spring & summer",
 "Incidence: H/O atopy present",
 "Clinical signs: 1. Papillary hypertrophy: cobble stone papillae",
 "Giant papillae: > 1mm size",
 "2. Horner Trantas sign: collection of eosinophils + epithelial debris",
 "Horner Trantas sign site: on limbus",
 "Photograph labels: Horner trantas sign; Pseudogerontoxon",
 "3. Pseudogerontoxon: paralimbal grey-white band (d/t lipid deposition) in children",
 "Pseudogerontoxon appearance similar to arcus senilis",
 "4. Shield ulcer (in cornea)",
 "5. Dennie morgan line: extra lower-lid crease",
 "6. Maxwell Lyon sign: ropy discharge",
 "Note: excessive itching -> increased incidence of keratoconus",
],
203: [
 "Treatment (VKC): 1. Cold compress",
 "2. Topical anti-histamine",
 "3. Topical mast cell stabilisers",
 "4. DOC: Olopatadine or Alcaftadine",
 "5. Topical steroids in acute exacerbation (for symptomatic treatment)",
 "ATOPIC KERATOCONJUNCTIVITIS: seen in 2nd to 5th decade",
 "Clinical features: eyelids: Hertoghe sign (lateral eyebrow lost)",
 "Clinical features: itching",
 "Clinical features: papillae",
 "Clinical features: watery discharge",
 "Treatment: 1. topical anti-histamine",
 "2. topical mast cell stabilisers",
 "GIANT PAPILLARY KERATOCONJUNCTIVITIS: papillae > 1mm",
 "Type IV hypersensitivity reaction",
 "Etiology: mechanically induced by contact lens",
 "ocular prostheses",
 "protruding sutures",
 "Treatment: anti-histamine + surgery to remove irritant (if required)",
 "PHYLCTENULAR KERATOCONJUNCTIVITIS: Type IV hypersensitivity reaction in response to endogenous allergen",
 "Etiology: m/c in India: TB",
 "Etiology: m/c in western countries: Staphylococcus aureus",
 "Clinical features: phlycten: nodule near limbus",
 "Grows towards cornea -> ulcerates",
 "Gives rise to: sacrofulous ulcer",
 "fascicular ulcer",
 "miliary ulcer",
 "Treatment: topical steroids",
 "Photograph caption: Phlycten",
],
204: [
 "Heading Pterygium (01:07:20): triangular, fibrovascular growth of degenerative sub-conjunctival tissue over cornea",
 "Destroys Bowman's layer & superficial stroma",
 "Associated with UV ray exposure",
 "Associated with dust",
 "Associated with humidity",
 "Cause: limbal stem cell deficiency -> activation of matrix metalloproteinase",
 "Site: Nasal > Lateral",
 "Clinical features: 1. triangular growth with apex towards cornea",
 "2. Stocker's line: deposition of iron in front of apex",
 "3. Loss of vision",
 "Causes of LOV: a. corneal astigmatism",
 "b. encroaching into visual axis",
 "Photograph label: covers pupillary area",
 "Treatment: surgical excision: increased rate of recurrence",
 "To reduce recurrence: 1. topical mitomycin C",
 "2. Autograft: harvested from same eye",
 "Autograft site: usually superior",
 "Autograft fixed with sutures/fibrin glue/autologous serum",
 "Photographs: pterygium with apex towards cornea; pterygium covering the pupillary area",
],
205: [
 "Heading Pinguecula & concretions (01:14:28)",
 "PINGUECULA: elastic degeneration of collagen fibres in stroma of conjunctiva",
 "m/c site: nasal part of conjunctiva",
 "Photograph caption: yellowish fat-like nodules",
 "CONCRETIONS: collection of epithelial debris & mucus",
 "Cause: irritation d/t friction of eyelid against bulbar conjunctiva & cornea while blinking",
 "Treatment: removal with 26g needle",
 "Spontaneously resolves with good lubrication",
 "Note: concretions do not contain calcium deposits",
 "Photograph caption: minute yellowish-white elevations",
],
}

c = Chapter(43, "Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium", 195, 205, POINTS)

# ---------------------------------------------------------------- p195
c.unit("Anatomy of conjunctiva: parts", "Conjunctiva",
       "Conjunctiva = transparent mucous membrane that does not cover the cornea; bulbar, forniceal and palpebral parts; plica semilunaris (nictitating membrane) and caruncle (hair follicles) as rudimentary structures.")
c.q(195, "recall", "Which statement about the conjunctiva is correct?",
    "It is a transparent mucous membrane that does not cover the cornea",
    ["It is an opaque fibrous coat that covers the cornea", "It is a transparent membrane that continues over the cornea", "It is a mucous membrane that covers the cornea but not the sclera"],
    "Conjunctiva is a transparent mucous membrane. It does not cover cornea.",
    [1, 2, 3], "Anatomy of conjunctiva")
c.q(195, "fillup", "The bulbar conjunctiva covers the ___, while the palpebral conjunctiva lines the inner surface of the ___.",
    "Sclera; eyelids",
    ["Cornea; eyelids", "Sclera; orbit", "Tarsal plate; fornix"],
    "Parts of conjunctiva: Bulbar (covers sclera); Forniceal; Palpebral (lines inner surface of eyelids).",
    [4, 6], "Parts of conjunctiva")
c.q(195, "recall", "Which of the following is a part of the conjunctiva that forms the fold between the bulbar and palpebral parts?",
    "Forniceal conjunctiva",
    ["Marginal conjunctiva", "Tarsal conjunctiva", "Limbic conjunctiva"],
    "Parts of conjunctiva: Bulbar (covers sclera), Forniceal, Palpebral (lines inner surface of eyelids).",
    [4, 5, 6], "Parts of conjunctiva")
c.q(195, "match", "Match the rudimentary structure of the conjunctiva with its description — 1) Plica semilunaris  2) Caruncle  … A) Contains hair follicles  B) Represents nictitating membrane",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Plica semilunaris: represents nictitating membrane. Caruncle: contains hair follicles. Together they are labelled rudimentary structures.",
    [7, 8, 9], "Rudimentary structures")
c.q(195, "truefalse", "True or false — 'The caruncle and the plica semilunaris are labelled as rudimentary structures of the conjunctiva.'",
    "True - the plica semilunaris represents the nictitating membrane and the caruncle contains hair follicles",
    ["False - only the plica semilunaris is a rudimentary structure", "False - both are fully developed lacrimal structures", "True - but the caruncle is a modified meibomian gland"],
    "Plica semilunaris (nicitiating membrane) and caruncle (hair follicles) are bracketed together as rudimentary structures.",
    [9], "Rudimentary structures")

c.unit("Histology of the conjunctiva", "Conjunctiva",
       "Outermost epithelium = non-keratinised stratified squamous with goblet cells (mucin, innermost tear-film layer, parasympathetic), melanocytes and Langerhans cells; adenoid/lymphatic layer develops after 3 months; fibrous layer carries nerves and vessels.")
c.q(195, "fillup", "The outermost layer of the conjunctiva is a ___ epithelium.",
    "Non-keratinised stratified squamous",
    ["Keratinised stratified squamous", "Non-keratinised columnar", "Transitional"],
    "1. Outermost layer: epithelium (non-keratinised stratified squamous).",
    [10], "Histology")
c.q(195, "recall", "The goblet cells of the conjunctival epithelium secrete mucin on which stimulation?",
    "Parasympathetic stimulation",
    ["Sympathetic stimulation", "No stimulation - continuous basal secretion", "Trigeminal (corneal reflex) stimulation"],
    "Goblet cells: secrete mucin (forms innermost layer of tear film) on parasympathetic stimulation.",
    [11], "Histology")
c.q(195, "scenario", "A patient's tear film is deficient in its innermost layer. Which conjunctival cells are responsible for this layer?",
    "Goblet cells",
    ["Langerhans cells", "Melanocytes", "Fibrous layer cells"],
    "Goblet cells secrete mucin, which forms the innermost layer of the tear film.",
    [11], "Histology")
c.q(195, "oddoneout", "Besides goblet cells, the conjunctival epithelium contains melanocytes and which other cell?",
    "Langerhans cells",
    ["Merkel cells", "Paneth cells", "Schwann cells"],
    "The epithelium contains: a. Goblet cells b. Melanocytes c. Langerhans cells.",
    [12, 13], "Histology")
c.q(195, "numeric", "The adenoid/lymphatic layer of the conjunctiva develops after how long?",
    "3 months of age",
    ["3 weeks of age", "3 years of age", "Birth - it is fully developed at birth"],
    "2. Adenoid/lymphatic layer: develops after 3 months of age.",
    [14], "Histology")
c.q(195, "fillup", "The fibrous layer of the conjunctiva contains nerve fibres and ___.",
    "Blood vessels",
    ["Lymphoid aggregates", "Goblet cells", "Smooth muscle fibres"],
    "3. Fibrous layer: contains nerve fibres & blood vessels.",
    [15], "Histology")

# ---------------------------------------------------------------- p196
c.unit("Lymphatic drainage of the conjunctiva", "Conjunctiva",
       "Conjunctiva is the only site of lymphatic drainage from the eye: medially to submandibular nodes, laterally to peri-auricular and superficial parotid nodes.")
c.q(196, "fillup", "The conjunctiva is the only site of ___ from the eye.",
    "Lymphatic drainage",
    ["Aqueous outflow", "Venous drainage", "Arterial supply"],
    "Lymphatic drainage: only site of lymphatic drainage from the eye.",
    [1], "Lymphatic drainage")
c.q(196, "match", "Match the direction of conjunctival lymphatic drainage with its lymph nodes — 1) Medially  2) Laterally  … A) Peri-auricular & superficial parotid lymph nodes  B) Submandibular lymph nodes",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Drainage: medially -> submandibular lymph nodes; laterally -> peri-auricular & superficial parotid lymph nodes.",
    [2, 3, 4], "Lymphatic drainage")

c.unit("Conjunctivitis: symptoms and signs", "Conjunctiva",
       "Aka eye flu: redness, discharge sticking to eyelids, foreign body sensation, lacrimation, itching (if allergic), pain and LOV (corneal involvement); conjunctival vs circumcorneal hyperemia and its differential diagnosis.")
c.q(196, "recall", "Conjunctivitis is also known as:",
    "Eye flu",
    ["Spring catarrh", "Egyptian ophthalmia", "Madras eye"],
    "Conjunctivitis: Aka eye flu. (Spring catarrh is vernal keratoconjunctivitis and Egyptian ophthalmia is trachoma.)",
    [5], "Conjunctivitis")
c.q(196, "oddoneout", "Which of the following is NOT listed among the symptoms of conjunctivitis?",
    "Painless proptosis",
    ["Redness", "Foreign body sensation", "Lacrimation"],
    "Symptoms: redness, discharge sticking to eyelids, foreign body sensation, lacrimation; itching (if allergic); pain and loss of vision (corneal involvement).",
    [6, 7, 8, 9], "Symptoms")
c.q(196, "scenario", "A young patient with conjunctivitis complains of itching. The book attributes the itching to:",
    "Allergy",
    ["Corneal involvement", "Bacterial superinfection", "Raised intraocular pressure"],
    "Symptoms include itching (if allergic); pain and loss of vision are seen with corneal involvement.",
    [10, 11], "Symptoms")
c.q(196, "scenario", "A patient with conjunctivitis develops pain and loss of vision. According to the book this indicates:",
    "Corneal involvement",
    ["Scleral involvement", "Orbital cellulitis", "Chronic dacryocystitis"],
    "Pain and loss of vision (LOV): corneal involvement.",
    [11], "Symptoms")
c.q(196, "recall", "Which vascular sign is listed first under the signs of conjunctivitis?",
    "Conjunctival hyperemia",
    ["Circumcorneal hyperemia", "Subconjunctival hemorrhage", "Chemosis"],
    "Signs: 1. Conjunctival hyperemia (redness).",
    [12], "Signs")
c.q(196, "oddoneout", "Circumcorneal redness is the differential diagnosis of conjunctival redness and is seen in all of the following EXCEPT:",
    "Subconjunctival hemorrhage",
    ["Glaucoma", "Uveitis", "Corneal ulcer"],
    "Differential diagnosis of circumcorneal redness: glaucoma, uveitis, corneal ulcer.",
    [13, 14, 15], "Signs")
c.q(196, "fillup", "The two clinical photographs on this page are captioned conjunctival hyperemia and ___ hyperemia.",
    "Circumcorneal",
    ["Subconjunctival", "Episcleral", "Limbic"],
    "Photographs: conjunctival hyperemia and circumcorneal hyperemia. Note: circumcorneal hyperemia is seen in glaucoma, uveitis and corneal ulcer.",
    [16, 17], "Signs")

# ---------------------------------------------------------------- p197
c.unit("Other conjunctival signs and inflammatory reactions", "Conjunctiva",
       "Subconjunctival hemorrhage needs no treatment; chemosis = swelling of bulbar conjunctiva; discharge causes colored halos and stickiness; papillae = hypertrophied vessels, follicles = lymphoid aggregates; discharge-to-reaction etiology table.")
c.q(197, "management", "A patient has a bright red patch on the conjunctiva that resolves on its own. What treatment does the book advise for subconjunctival hemorrhage?",
    "No treatment is required",
    ["Topical antibiotics for two weeks", "Topical steroids", "Immediate surgical drainage"],
    "2. Subconjunctival hemorrhage: No treatment required (resolves spontaneously in ~2 weeks).",
    [1], "Subconjunctival hemorrhage")
c.q(197, "fillup", "Chemosis is swelling of the ___ conjunctiva.",
    "Bulbar",
    ["Palpebral", "Forniceal", "Tarsal"],
    "3. Chemosis: swelling of bulbar conjunctiva.",
    [2], "Chemosis")
c.q(197, "scenario", "A patient reports colored halos that disappear on washing the eye, along with stickiness of the lids. The discharge responsible is described as:",
    "Mucopurulent or watery",
    ["Blood-stained", "Fibrinous", "Gritty and sand-like"],
    "4. Discharge: mucopurulent/watery; causes colored halos & stickiness which resolves on washing eye.",
    [3, 4], "Discharge")
c.q(197, "recall", "In the inflammatory reaction of the conjunctiva, papillae represent:",
    "Hypertrophied vessels",
    ["Lymphoid aggregates", "Fibrovascular plaques", "Granulomatous nodules"],
    "5. Inflammatory reactions of conjunctiva: Papillae - hypertrophied vessels; Follicles - lymphoid aggregates.",
    [5], "Inflammatory reactions")
c.q(197, "fillup", "In contrast to papillae, conjunctival follicles are ___.",
    "Lymphoid aggregates",
    ["Hypertrophied vessels", "Collections of eosinophils and epithelial debris", "Deposits of lipid"],
    "Follicles: lymphoid aggregates. (Papillae are hypertrophied vessels.)",
    [6], "Inflammatory reactions")
c.q(197, "match", "Match the discharge with the conjunctival reaction it indicates — 1) Mucopurulent discharge  2) Watery discharge  … A) Papillary reaction - bacterial; follicular reaction - Chlamydia  B) Papillary reaction - allergic; follicular reaction - viral",
    "1-A, 2-B",
    ["1-B, 2-A", "1-A, 2-A", "1-B, 2-B"],
    "Etiology table: mucopurulent discharge - papillary: bacterial, follicular: Chlamydia. Watery discharge - papillary: allergic, follicular: viral.",
    [7, 8], "Etiology table")
c.q(197, "recall", "What is the most common cause of acute mucopurulent conjunctivitis?",
    "Staphylococcus aureus",
    ["Neisseria gonorrhoeae", "Streptococcus pneumoniae", "Haemophilus influenzae"],
    "Acute mucopurulent conjunctivitis: m/c cause Staphylococcus aureus.",
    [9, 10], "Bacterial conjunctivitis")
c.q(197, "management", "Treatment of acute mucopurulent conjunctivitis is:",
    "Topical antibiotics",
    ["Oral antibiotics for 2 weeks", "Topical steroids", "Silver nitrate 1% application"],
    "Acute mucopurulent conjunctivitis: treatment - topical antibiotics.",
    [11], "Bacterial conjunctivitis")

# ---------------------------------------------------------------- p198
c.unit("Bacterial conjunctivitis: purulent, membranous and angular", "Conjunctiva",
       "Blenorrhoea (N. gonorrhoeae, oculogenital, ceftriaxone + erythromycin); membranous (Pneumococcus/diphtheria, membrane fuses and bleeds) vs pseudomembranous (no fusion, no bleeding); angular conjunctivitis (Moraxella, excoriation at canthi, tetracycline + zinc boric).")
c.q(198, "fillup", "Acute purulent/hyperacute conjunctivitis is also known as ___.",
    "Blenorrhoea",
    ["Trachoma", "Spring catarrh", "Egyptian ophthalmia"],
    "Heading: Acute purulent/hyperacute conjunctivitis/Blenorrhoea.",
    [1], "Hyperacute conjunctivitis")
c.q(198, "recall", "The most common cause of acute purulent/hyperacute conjunctivitis is:",
    "Neisseria gonorrhoeae",
    ["Staphylococcus aureus", "Pneumococcus", "Moraxella lacunata"],
    "m/c cause: Neisseria gonorrhoeae.",
    [2], "Hyperacute conjunctivitis")
c.q(198, "fillup", "The route of transmission of hyperacute purulent conjunctivitis is ___.",
    "Oculogenital",
    ["Orofecal", "Respiratory droplet", "Vector-borne"],
    "Route of transmission: Oculogenital.",
    [3], "Hyperacute conjunctivitis")
c.q(198, "scenario", "Which set of clinical features does the book list for blennorrhoea?",
    "Copious purulent discharge, overhanging swollen eyelids, intense pain and pre-auricular lymphadenopathy",
    ["Watery discharge, itching and cobble stone papillae", "Mucopurulent discharge with redness at the intermarginal strip", "Membrane that fuses with the epithelium and bleeds on removal"],
    "Clinical features: 1. Copious purulent discharge. 2. Swelling of eyelids -> overhanging. 3. Intense pain. 4. Pre-auricular lymphadenopathy.",
    [4, 5, 6, 7], "Hyperacute conjunctivitis")
c.q(198, "management", "Treatment of acute purulent conjunctivitis as given in the book is:",
    "IM ceftriaxone 1 g single dose, followed by oral erythromycin for 2 weeks",
    ["Topical antibiotics alone for 2 weeks", "IM ceftriaxone 1 g single dose alone", "Topical tetracycline ointment with zinc boric drops"],
    "Treatment: IM Ceftriaxone 1g single dose followed by oral erythromycin x 2 weeks.",
    [8, 9], "Hyperacute conjunctivitis")
c.q(198, "scenario", "A photograph on this page shows a patient with marked lid swelling and purulent discharge. Its caption is:",
    "Blennorrhoea",
    ["Pseudomembrane peeling", "Trachomatous trichiasis", "Sago grain follicles"],
    "Photograph caption: Blennorrhoea.",
    [10], "Hyperacute conjunctivitis")
c.q(198, "recall", "What is the most common cause of acute membranous conjunctivitis overall/in adults?",
    "Pneumococcus",
    ["Corynebacterium diphtheriae", "Staphylococcus aureus", "Neisseria gonorrhoeae"],
    "Acute membranous conjunctivitis - m/c cause: overall/in adults: Pneumococcus.",
    [11], "Membranous conjunctivitis")
c.q(198, "scenario", "In unimmunised children, acute membranous conjunctivitis is most commonly caused by:",
    "Corynebacterium diphtheriae",
    ["Pneumococcus", "Moraxella lacunata", "Adenovirus type 11"],
    "m/c cause in unimmunised children: Corynebacterium diphtheriae.",
    [12], "Membranous conjunctivitis")
c.q(198, "truefalse", "True or false — 'In membranous conjunctivitis the membrane does not fuse with the epithelium, so there is no bleeding on removal.'",
    "False - that describes acute pseudomembranous conjunctivitis; in membranous conjunctivitis the membrane fuses with the epithelium and bleeds on removal",
    ["True - this distinguishes it from pseudomembranous conjunctivitis", "False - in membranous conjunctivitis the membrane fuses but still does not bleed", "True - and the membrane is fixed with fibrin glue"],
    "Acute membranous conjunctivitis: membrane formed -> fused with epithelium -> bleeds on removal. Acute pseudomembranous conjunctivitis: membrane does not fuse with epithelium -> no bleeding on removal.",
    [13, 14, 15], "Membranous conjunctivitis")
c.q(198, "fillup", "The photograph on this page showing a red eye with a peeling membrane is captioned:",
    "Pseudomembrane peeling",
    ["Blennorrhoea peeling", "Sloughing pterygium", "Sago grain follicles"],
    "Photograph caption: Pseudomembrane peeling.",
    [16], "Membranous conjunctivitis")
c.q(198, "recall", "Angular/diplobacillary conjunctivitis is most commonly caused by:",
    "Moraxella lacunata/axenfeld",
    ["Staphylococcus aureus", "Pneumococcus", "Chlamydia trachomatis"],
    "Angular/diplobacillary conjunctivitis: m/c cause moraxella lacunata/axenfeld.",
    [17], "Angular conjunctivitis")
c.q(198, "fillup", "Excoriation in angular conjunctivitis is seen at the canthi, with ___ involvement greater than ___.",
    "Lateral; medial",
    ["Medial; lateral", "Superior; inferior", "Lateral; inferior"],
    "Clinical features: excoriation at canthi (Lateral > medial).",
    [18], "Angular conjunctivitis")
c.q(198, "recall", "In angular conjunctivitis, redness is seen at the:",
    "Intermarginal strip",
    ["Limbus", "Plica semilunaris", "Bulbar conjunctiva over the rectus insertions"],
    "Clinical features: redness at intermarginal strip.",
    [19], "Angular conjunctivitis")
c.q(198, "scenario", "A patient with angular conjunctivitis has blepharitis. In the book this refers to inflammation of the:",
    "Eyelid margin",
    ["Lacrimal sac", "Tarsal plate", "Meibomian gland only"],
    "Clinical features: blepharitis (inflammation of eyelid margin).",
    [20], "Angular conjunctivitis")
c.q(198, "management", "Treatment of angular conjunctivitis includes tetracycline 1% eye ointment for at least 2 weeks along with:",
    "Zinc boric eye drops, because zinc blocks proteolytic activity",
    ["Topical steroids, because zinc blocks proteolytic activity", "Oral erythromycin for 2 weeks", "Silver nitrate 1%, which blocks proteolytic activity"],
    "Treatment: tetracycline 1% eye ointment for >= 2 wks; zinc boric eye drops (zinc blocks proteolytic activity).",
    [21, 22], "Angular conjunctivitis")

# ---------------------------------------------------------------- p199
c.unit("Viral conjunctivitis", "Conjunctiva",
       "Adenoviral: non-specific follicular (1-11, 19), EKC (8, 19, 37), PCF (3, 4, 7 with preauricular lymphadenopathy); Apollo/acute hemorrhagic conjunctivitis (Coxsackie A24 m/c, enterovirus 70, adenovirus 11); molluscum contagiosum nodule.")
c.q(199, "match", "Match the adenoviral conjunctivitis with its serovars — 1) Non-specific follicular conjunctivitis  2) Epidemic keratoconjunctivitis (EKC)  3) Pharyngoconjunctival fever (PCF)  … A) Serovars 8, 19, 37  B) Serovars 3, 4, 7  C) Serovars 1 to 11 & 19",
    "1-C, 2-A, 3-B",
    ["1-C, 2-B, 3-A", "1-A, 2-C, 3-B", "1-B, 2-A, 3-C"],
    "Non-specific follicular conjunctivitis: serovars 1 to 11 & 19. EKC: serovars 8, 19, 37. PCF: serovars 3, 4, 7.",
    [1, 2, 3, 4], "Adenoviral conjunctivitis")
c.q(199, "scenario", "A patient with pharyngoconjunctival fever has enlarged lymph nodes. The book records this as:",
    "Preauricular lymphadenopathy",
    ["Submandibular lymphadenopathy", "Submental lymphadenopathy", "Generalised lymphadenopathy"],
    "Pharyngoconjunctival fever (PCF): associated with preauricular lymphadenopathy.",
    [5], "Adenoviral conjunctivitis")
c.q(199, "fillup", "Apollo conjunctivitis is also known as acute ___ conjunctivitis, and causes hemorrhage of the palpebral and bulbar conjunctiva.",
    "Hemorrhagic",
    ["Membranous", "Follicular", "Angular"],
    "Apollo conjunctivitis/Acute hemorrhagic conjunctivitis: hemorrhage of palpebral & bulbar conjunctiva (photograph of both red eyes).",
    [6, 7], "Apollo conjunctivitis")
c.q(199, "recall", "The most common cause of Apollo (acute hemorrhagic) conjunctivitis is:",
    "Coxsackie A24",
    ["Enterovirus type 70", "Adenovirus type 11", "Adenovirus type 8"],
    "Causes: 1. Picornavirus: Enterovirus type 70, Coxsackie A24 (m/c). 2. Adenovirus type 11.",
    [8, 9], "Apollo conjunctivitis")
c.q(199, "scenario", "A patient has a unilateral, painless, umbilicated nodule which periodically sheds virus and produces conjunctivitis. What is the treatment advised in the book?",
    "Surgical excision, if the cosmetic indication is positive",
    ["Topical antivirals with cold compress", "Cryotherapy of the lash base", "Observation, since it never sheds virus"],
    "Molluscum contagiosum: nodule contains viral particles -> periodic shedding of virus -> conjunctivitis. Treatment: surgical excision [if cosmetic indication (+)].",
    [10, 11, 12, 13], "Molluscum contagiosum")
c.q(199, "fillup", "The photograph on this page showing a lid nodule with a central depression is captioned:",
    "Umbilicated nodule",
    ["Sago grain nodule", "Phlycten", "Chalazion"],
    "Photograph caption: umbilicated nodule (molluscum contagiosum).",
    [14], "Molluscum contagiosum")

# ---------------------------------------------------------------- p199-200
c.unit("Chlamydial conjunctivitis and trachoma", "Conjunctiva",
       "Chlamydia serovars (adult inclusion D-K; trachoma A, B, Ba, C; ophthalmia neonatorum D-K); trachoma = Egyptian ophthalmia, 3F transmission; Type IV hypersensitivity; sago grain follicles with Leber cells; Arlt's line, Herbert's pits, pannus; SAFE strategy and the prevalence-based treatment table.")
c.q(199, "match", "Match the chlamydial condition with its serovars — 1) Trachoma  2) Adult inclusion conjunctivitis  3) Ophthalmia neonatorum  … A) D to K serovars  B) A, B, Ba, C serovars  C) D to K serovars and other causes",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-B, 3-A"],
    "Adult inclusion conjunctivitis: D to K serovars. Trachoma: A, B, Ba, C serovars. Ophthalmia neonatorum: D to K serovars; other causes.",
    [15, 16, 17], "Chlamydial conjunctivitis")
c.q(199, "recall", "Trachoma is also known as:",
    "Egyptian ophthalmia",
    ["Apollo conjunctivitis", "Eye flu", "Spring catarrh"],
    "TRACHOMA aka Egyptian ophthalmia.",
    [18], "Trachoma")
c.q(199, "fillup", "The route of transmission of trachoma is remembered by the mnemonic ___.",
    "3F",
    ["3D", "4F", "SAFE"],
    "Route of transmission: mnemonic 3F - fingers, flies, fomites.",
    [19, 20, 21, 22], "Trachoma")
c.q(200, "fillup", "The pathology of trachoma is a Type ___ hypersensitivity reaction with active inflammation and cicatrization.",
    "IV",
    ["I", "II", "III"],
    "Pathology: Type IV hypersensitivity reaction: active inflammation + cicatrization.",
    [1], "Trachoma")
c.q(200, "numeric", "Trachoma is described in which age group?",
    "Less than 10 years",
    ["10 to 20 years", "20 to 40 years", "Above 40 years"],
    "Age group: < 10 yrs.",
    [2], "Trachoma")
c.q(200, "recall", "Sago grain follicles in trachoma show which histological feature?",
    "Necrosis and Leber cells",
    ["Eosinophils and epithelial debris", "Caseating granulomas", "Deposits of iron"],
    "Clinical signs: 1. Sago grain follicles: necrosis & Leber; m/c site: upper palpebral conjunctiva; necrosis & Leber cells seen (photograph: sago grain follicles).",
    [3, 4, 5, 6], "Trachoma clinical signs")
c.q(200, "fillup", "Arlt's line in trachoma is a line of ___.",
    "Cicatrization",
    ["Iron deposition", "Lipid deposition", "Vascularisation"],
    "2. Cicatricial sign: a. Arlt's line: line of cicatrization (photograph labelled lower 2/3rd and upper 1/3rd).",
    [7, 8], "Trachoma clinical signs")
c.q(200, "scenario", "Herbert's pits are pathognomonic of trachoma and result from healing of:",
    "Limbal follicles",
    ["Sago grain follicles of the upper tarsus", "Shield ulcers", "Pannus vessels"],
    "b. Herbert's pits: pathognomonic; d/t healing of limbal follicles (photograph label: Herbert's pits).",
    [9, 10, 11], "Trachoma clinical signs")
c.q(200, "recall", "Pannus in trachoma is:",
    "Vascularisation of the cornea superiorly",
    ["Deposition of iron in the cornea", "An opaque corneal scar", "A paralimbal grey-white band"],
    "c. Pannus: vascularisation of cornea superiorly.",
    [12], "Trachoma clinical signs")
c.q(200, "scenario", "Which sequence of trachoma complications does the book give?",
    "Trichiasis -> corneal ulcer -> scar formation -> loss of vision",
    ["Pannus -> trichiasis -> corneal opacity -> loss of vision", "Corneal ulcer -> trichiasis -> pannus -> loss of vision", "Herbert's pits -> trichiasis -> corneal ulcer -> loss of vision"],
    "Complications: trichiasis (inturned eyelash) -> corneal ulcer -> scar formation -> loss of vision.",
    [13], "Trachoma complications")
c.q(200, "match", "Match the letter of the SAFE strategy (WHO, 1996) with its component — 1) S  2) A  3) F  4) E  … A) Azithromycin 1g  B) Surgery for inturned eyelids  C) Facial cleanliness  D) Environmental change",
    "1-B, 2-A, 3-C, 4-D",
    ["1-B, 2-A, 3-D, 4-C", "1-A, 2-B, 3-C, 4-D", "1-B, 2-C, 3-A, 4-D"],
    "SAFE strategy (WHO, 1996): Surgery for inturned eyelids; Antibiotics: Azithromycin 1g; Facial cleanliness; Environmental change.",
    [14, 15, 16, 17, 18], "Trachoma treatment")
c.q(200, "management", "According to the prevalence-based table, what is advised when trachoma prevalence in 1-9 year old children is more than 10%?",
    "Mass prophylaxis",
    ["Treatment to affected children and family", "Facial cleanliness and environmental change alone", "Surgery for all inturned eyelids"],
    "Indications for treatment: > 10% -> mass prophylaxis; 5-10% -> treatment to affected children & family; < 5% -> facial cleanliness & environmental change advised.",
    [19, 20, 21], "Trachoma treatment")

# ---------------------------------------------------------------- p201
c.unit("FISTO classification (WHO)", "Conjunctiva",
       "TF (>5 follicles, active, antibiotics), TI (thickening of upper palpebral conjunctiva, active), TS (Arlt's line, inactive, no treatment), TT (eyelash growing inwards, surgery), CO (corneal opacity, visual impairment).")
c.q(201, "match", "Match the FISTO grade with its feature — 1) TF  2) TI  3) TS  4) CO  … A) Thickening of upper palpebral conjunctiva  B) > 5 follicles +  C) Arlt's line  D) Visual impairment",
    "1-B, 2-A, 3-C, 4-D",
    ["1-A, 2-B, 3-C, 4-D", "1-B, 2-A, 3-D, 4-C", "1-C, 2-A, 3-B, 4-D"],
    "FISTO: TF - trachomatous inflammation follicular: > 5 follicles +. TI - trachomatous inflammation intense: thickening of upper palpebral conjunctiva. TS - trachomatous scarring: Arlt's line. CO - corneal opacity: visual impairment.",
    [1, 2, 3, 5], "FISTO classification")
c.q(201, "truefalse", "True or false — 'The FISTO table treats the inactive stage of trachoma (TS) with antibiotics.'",
    "False - TS (trachomatous scarring) is the inactive stage and needs no treatment; TF and TI are the active stage treated with antibiotics",
    ["True - all grades receive antibiotics", "False - TS requires surgery, not antibiotics", "True - but the antibiotics are given topically only"],
    "TS: trachomatous scarring - Arlt's line; inactive stage: no treatment. TF and TI are active stage: treatment - antibiotics. TT requires surgery.",
    [1, 2, 3, 4], "FISTO classification")
c.q(201, "management", "In the FISTO table, which grade requires surgery?",
    "TT - trachomatous trichiasis, with eyelash growing inwards",
    ["TF - trachomatous inflammation follicular", "TI - trachomatous inflammation intense", "TS - trachomatous scarring"],
    "TT: Trachomatous trichiasis - eyelash growing inwards; requires surgery. TF and TI are the active stage (antibiotics); TS is the inactive stage (no treatment).",
    [2, 3, 4], "FISTO classification")
c.q(201, "recall", "The five photographs of the FISTO classification are captioned trachomatous inflammation follicular, trachomatous inflammation follicular and intense, trachomatous scarring, trachomatous trichiasis and:",
    "Corneal opacity (CO)",
    ["Herbert's pits", "Pannus", "Sago grain follicles"],
    "Photograph captions: trachomatous inflammation follicular (TF), trachomatous inflammation follicular and intense (TF), trachomatous scarring (TS), trachomatous trichiasis (TT), corneal opacity (CO).",
    [6], "FISTO classification")

c.unit("Ophthalmia neonatorum: causes and prophylaxis", "Conjunctiva",
       "Conjunctivitis in neonates (<28 days of onset); causes by onset - chemical/silver nitrate (6 h), gonococcus (24-48 h, most severe), other bacteria (2-5 d), HSV-II (5-7 d), Chlamydia D-K (>1 wk, m/c); prophylaxis - Crede's silver nitrate (not recommended), erythromycin 0.5%/tetracycline 1% single application within 1 hour of birth.")
c.q(201, "fillup", "Ophthalmia neonatorum is conjunctivitis in neonates with onset within ___ days.",
    "28",
    ["7", "14", "21"],
    "Ophthalmia neonatorum: conjunctivitis in neonates (< 28 days of onset).",
    [7], "Ophthalmia neonatorum")
c.q(201, "match", "Match the onset after birth with the cause of ophthalmia neonatorum — 1) Within first 6 h  2) 24 to 48 h  3) 5 to 7 d  … A) HSV-II  B) Chemical conjunctivitis (silver nitrate)  C) Neisseria gonorrhoeae",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Causes table: within first 6h - chemical conjunctivitis (silver nitrate); 24 to 48h - Neisseria gonorrhoeae (most severe); 5 to 7 d - HSV-II.",
    [8, 9, 11], "Ophthalmia neonatorum")
c.q(201, "recall", "Which cause of ophthalmia neonatorum does the table mark as the most severe?",
    "Neisseria gonorrhoeae",
    ["Chemical conjunctivitis", "HSV-II", "Chlamydia trachomatis"],
    "24 to 48h: Neisseria gonorrhoeae (most severe).",
    [9], "Ophthalmia neonatorum")
c.q(201, "recall", "Ophthalmia neonatorum developing 2 to 5 days after birth is caused by:",
    "Other bacteria",
    ["Neisseria gonorrhoeae", "HSV-II", "Chlamydia trachomatis"],
    "Causes table: 2 to 5 d - other bacteria.",
    [10], "Ophthalmia neonatorum")
c.q(201, "scenario", "A neonate develops conjunctivitis more than 1 week after birth. What is the most common organism?",
    "Chlamydia trachomatis (D to K)",
    ["Neisseria gonorrhoeae", "HSV-II", "Staphylococcus aureus"],
    "Causes table: > 1 wk - Chlamydia trachomatis (D to K): m/c.",
    [12], "Ophthalmia neonatorum")
c.q(201, "scenario", "The book's clinical photograph of a neonate with bilateral purulent conjunctivitis illustrates:",
    "Ophthalmia neonatorum",
    ["Trachoma", "Blenorrhoea", "Vernal keratoconjunctivitis"],
    "Photograph caption: Ophthalmia neonatorum - conjunctivitis in neonates with onset < 28 days.",
    [13], "Ophthalmia neonatorum")
c.q(202, "truefalse", "True or false — \"Crede's method of prophylaxis (topical 1% silver nitrate) is recommended for the prevention of ophthalmia neonatorum.\"",
    "False - it is not recommended because it causes chemical conjunctivitis",
    ["True - it is the first choice for prophylaxis", "False - it fell out of use because silver nitrate is inactive against gonococci", "True - but it is applied only after 1 hour of birth"],
    "Prevention: 1. Crede's method: topical 1% silver nitrate (not recommended d/t chemical conjunctivitis).",
    [1], "Ophthalmia neonatorum prophylaxis")
c.q(202, "management", "For prophylaxis of ophthalmia neonatorum the book advises 0.5% erythromycin or 1% tetracycline as:",
    "A single application within 1 hour of birth",
    ["A once-daily application for 1 week", "A single application within 6 hours of birth", "Three applications on the first day of life"],
    "Prevention: 2. 0.5% erythromycin; 3. 1% tetracycline - single application, within 1 hr of birth.",
    [2, 3, 4], "Ophthalmia neonatorum prophylaxis")

# ---------------------------------------------------------------- p202-203
c.unit("Allergic conjunctivitis: vernal keratoconjunctivitis", "Conjunctiva",
       "Allergic conjunctivitis = papillary reaction + watery discharge + itching; VKC/spring catarrh, Type I hypersensitivity (pollen), 5-15 yrs, boys, spring and summer, atopy; cobble stone/giant papillae, Horner Trantas sign, pseudogerontoxon, shield ulcer, Dennie Morgan line, Maxwell Lyon sign, keratoconus risk; treatment ladder.")
c.q(202, "fillup", "Allergic conjunctivitis presents with ___ reaction, watery discharge and itching.",
    "Papillae (papillary)",
    ["Follicular", "Membranous", "Granulomatous"],
    "Allergic conjunctivitis: presents with papillae reaction + watery discharge + itching.",
    [5], "Allergic conjunctivitis")
c.q(202, "recall", "Vernal keratoconjunctivitis is also known as spring catarrh and is which type of hypersensitivity reaction?",
    "Type I hypersensitivity reaction, eg. pollen",
    ["Type II hypersensitivity reaction", "Type III hypersensitivity reaction", "Type IV hypersensitivity reaction"],
    "VERNAL KERATOCONJUNCTIVITIS/SPRING CATARRH: Type I hypersensitivity reaction (eg: pollen).",
    [6], "Vernal keratoconjunctivitis")
c.q(202, "match", "Match the incidence feature of vernal keratoconjunctivitis — 1) Age  2) Sex  3) Season  … A) Males > females (young boys)  B) 5-15 yrs  C) m/c in spring & summer",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "Incidence: age 5-15 yrs; males > females (young boys); m/c in spring & summer; H/O atopy present.",
    [7, 8, 9], "Vernal keratoconjunctivitis")
c.q(202, "recall", "Besides age, sex and season, which incidence factor is listed for vernal keratoconjunctivitis?",
    "History of atopy",
    ["History of contact lens use", "History of ocular trauma", "History of cataract surgery"],
    "Incidence: H/O atopy present.",
    [10], "Vernal keratoconjunctivitis")
c.q(202, "recall", "Cobble stone papillae of vernal keratoconjunctivitis are due to:",
    "Papillary hypertrophy",
    ["Lymphoid follicle formation", "Corneal vascularisation", "Deposition of lipid"],
    "Clinical signs: 1. Papillary hypertrophy: cobble stone papillae.",
    [11], "VKC clinical signs")
c.q(202, "numeric", "Giant papillae in vernal keratoconjunctivitis are larger than:",
    "1 mm",
    ["0.5 mm", "2 mm", "3 mm"],
    "Giant papillae: > 1mm size.",
    [12], "VKC clinical signs")
c.q(202, "fillup", "Horner Trantas sign is a collection of ___ and epithelial debris, situated on the ___.",
    "Eosinophils; limbus",
    ["Neutrophils; limbus", "Leber cells; upper tarsus", "Eosinophils; lower fornix"],
    "2. Horner Trantas sign: collection of eosinophils + epithelial debris; site: on limbus.",
    [13, 14], "VKC clinical signs")
c.q(202, "scenario", "A child with spring catarrh has a paralimbal grey-white band that resembles arcus senilis. This sign is due to:",
    "Pseudogerontoxon from lipid deposition",
    ["Horner Trantas sign from eosinophil collection", "Stocker's line from iron deposition", "Pannus from vascularisation"],
    "3. Pseudogerontoxon: paralimbal grey-white band (d/t lipid deposition) in children; appearance similar to arcus senilis (photograph labels: Horner trantas sign; Pseudogerontoxon).",
    [15, 16, 17], "VKC clinical signs")
c.q(202, "recall", "Which corneal sign is listed in vernal keratoconjunctivitis?",
    "Shield ulcer",
    ["Phlycten", "Dendritic ulcer", "Pannus"],
    "Clinical signs: 4. Shield ulcer (in cornea).",
    [18], "VKC clinical signs")
c.q(202, "fillup", "Dennie Morgan line in vernal keratoconjunctivitis is an extra ___ crease.",
    "Lower-lid",
    ["Upper-lid", "Medial canthal", "Lateral canthal"],
    "5. Dennie morgan line: extra lower-lid crease.",
    [19], "VKC clinical signs")
c.q(202, "recall", "Maxwell Lyon sign in vernal keratoconjunctivitis is:",
    "Ropy discharge",
    ["Mucopurulent discharge", "Watery discharge", "Blood-stained discharge"],
    "6. Maxwell Lyon sign: ropy discharge.",
    [20], "VKC clinical signs")
c.q(202, "scenario", "The book warns that excessive itching in vernal keratoconjunctivitis leads to:",
    "Increased incidence of keratoconus",
    ["Increased incidence of shield ulcer", "Progression to pterygium", "Development of Herbert's pits"],
    "Note: excessive itching -> increased incidence of keratoconus.",
    [21], "VKC complications")
c.q(203, "management", "What is the first step in the treatment of vernal keratoconjunctivitis?",
    "Cold compress",
    ["Topical steroids", "Topical mast cell stabilisers", "Surgery"],
    "Treatment: 1. Cold compress; 2. Topical anti-histamine; 3. Topical mast cell stabilisers; 4. DOC: Olopatadine or Alcaftadine; 5. Topical steroids in acute exacerbation.",
    [1, 2, 3], "VKC treatment")
c.q(203, "recall", "The drugs of choice (DOC) in vernal keratoconjunctivitis are:",
    "Olopatadine or alcaftadine",
    ["Azithromycin or tetracycline", "Mitomycin C or erythromycin", "Pilocarpine or tropicamide"],
    "4. DOC: Olopatadine or Alcaftadine.",
    [4], "VKC treatment")
c.q(203, "management", "When are topical steroids used in vernal keratoconjunctivitis?",
    "In acute exacerbation, for symptomatic treatment",
    ["As long-term maintenance therapy", "Prophylactically before every spring season", "Only after surgical excision"],
    "5. Topical steroids in acute exacerbation (for symptomatic treatment).",
    [5], "VKC treatment")

c.unit("Atopic, giant papillary and phlyctenular keratoconjunctivitis", "Conjunctiva",
       "AKC (2nd-5th decade, Hertoghe sign, anti-histamine + mast cell stabilisers); GPC (papillae >1 mm, Type IV, contact lens/prostheses/sutures, anti-histamine + removal of irritant); phlyctenular KC (Type IV to endogenous allergen, TB in India, S. aureus in the west, phlycten near limbus ulcerating into sacrofulous/fascicular/miliary ulcers, topical steroids).")
c.q(203, "numeric", "Atopic keratoconjunctivitis is seen in which decades of life?",
    "2nd to 5th decade",
    ["1st to 2nd decade", "5th to 6th decade", "1st decade only"],
    "ATOPIC KERATOCONJUNCTIVITIS: seen in 2nd to 5th decade.",
    [6], "Atopic keratoconjunctivitis")
c.q(203, "scenario", "An adult with atopic keratoconjunctivitis has lost the lateral part of his eyebrow. This sign is called:",
    "Hertoghe sign",
    ["Horner Trantas sign", "Dennie Morgan line", "Maxwell Lyon sign"],
    "Clinical features: eyelids - Hertoghe sign (lateral eyebrow lost).",
    [7], "Atopic keratoconjunctivitis")
c.q(203, "oddoneout", "Which of the following is NOT listed among the clinical features of atopic keratoconjunctivitis?",
    "Ropy discharge",
    ["Itching", "Papillae", "Watery discharge"],
    "AKC clinical features: eyelids - Hertoghe sign (lateral eyebrow lost); itching; papillae; watery discharge. (Ropy discharge is the Maxwell Lyon sign of VKC.)",
    [8, 9, 10], "Atopic keratoconjunctivitis")
c.q(203, "management", "Treatment of atopic keratoconjunctivitis is topical anti-histamine and:",
    "Topical mast cell stabilisers",
    ["Topical steroids", "Oral erythromycin", "Surgical excision of the lid lesion"],
    "AKC treatment: 1. Topical anti-histamine; 2. Topical mast cell stabilisers.",
    [11, 12], "Atopic keratoconjunctivitis")
c.q(203, "recall", "Giant papillary keratoconjunctivitis has papillae > 1 mm and which type of hypersensitivity reaction?",
    "Type IV hypersensitivity reaction",
    ["Type I hypersensitivity reaction", "Type II hypersensitivity reaction", "Type III hypersensitivity reaction"],
    "GIANT PAPILLARY KERATOCONJUNCTIVITIS: papillae > 1mm; Type IV hypersensitivity reaction.",
    [13, 14], "Giant papillary keratoconjunctivitis")
c.q(203, "oddoneout", "Giant papillary keratoconjunctivitis is mechanically induced by all of the following EXCEPT:",
    "Pollen",
    ["Contact lens", "Ocular prostheses", "Protruding sutures"],
    "Etiology of GPC: mechanically induced by contact lens, ocular prostheses, protruding sutures.",
    [15, 16, 17], "Giant papillary keratoconjunctivitis")
c.q(203, "management", "Treatment of giant papillary keratoconjunctivitis is:",
    "Anti-histamine plus surgery to remove the irritant (if required)",
    ["Topical steroids plus cold compress", "Topical mitomycin C", "Observation only, as it always resolves spontaneously"],
    "Treatment: anti-histamine + surgery to remove irritant (if required).",
    [18], "Giant papillary keratoconjunctivitis")
c.q(203, "scenario", "Phlyctenular keratoconjunctivitis is a Type IV hypersensitivity reaction in response to:",
    "An endogenous allergen",
    ["Pollen (exogenous allergen)", "Contact lens material", "Silver nitrate"],
    "PHYLCTENULAR KERATOCONJUNCTIVITIS: Type IV hypersensitivity reaction in response to endogenous allergen.",
    [19], "Phlyctenular keratoconjunctivitis")
c.q(203, "match", "Match the region with the most common cause of phlyctenular keratoconjunctivitis — 1) India  2) Western countries  … A) Staphylococcus aureus  B) TB",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Etiology: m/c in India - TB; m/c in western countries - Staphylococcus aureus.",
    [20, 21], "Phlyctenular keratoconjunctivitis")
c.q(203, "recall", "A phlycten is a nodule located near the:",
    "Limbus",
    ["Punctum", "Fornix", "Lacrimal gland"],
    "Clinical features: phlycten - nodule near limbus (photograph caption: Phlycten).",
    [22, 28], "Phlyctenular keratoconjunctivitis")
c.q(203, "scenario", "A phlycten grows towards the cornea and ulcerates. Which ulcers does the flow chart say it gives rise to?",
    "Sacrofulous, fascicular and miliary ulcers",
    ["Mooren's, rodent and neurotrophic ulcers", "Dendritic, geographic and amoebic ulcers", "Marginal, shield and perforating ulcers"],
    "Phlycten -> grows towards cornea -> ulcerates -> gives rise to sacrofulous ulcer, fascicular ulcer, miliary ulcer.",
    [23, 24, 25, 26], "Phlyctenular keratoconjunctivitis")
c.q(203, "management", "Treatment of phlyctenular keratoconjunctivitis is:",
    "Topical steroids",
    ["Topical antibiotics", "Topical mitomycin C", "Surgical excision of the phlycten"],
    "Treatment: topical steroids.",
    [27], "Phlyctenular keratoconjunctivitis")

# ---------------------------------------------------------------- p204
c.unit("Pterygium", "Conjunctiva",
       "Triangular fibrovascular growth over the cornea destroying Bowman's layer and superficial stroma; UV, dust, humidity; limbal stem cell deficiency with matrix metalloproteinase activation; nasal > lateral; Stocker's line; loss of vision; excision with mitomycin C and autograft.")
c.q(204, "fillup", "Pterygium is a triangular, ___ growth of degenerative sub-conjunctival tissue over the cornea.",
    "Fibrovascular",
    ["Lipid", "Granulomatous", "Cystic"],
    "Pterygium: triangular, fibrovascular growth of degenerative sub-conjunctival tissue over cornea (photographs of pterygium).",
    [1, 19], "Pterygium")
c.q(204, "recall", "Pterygium destroys which layers of the cornea?",
    "Bowman's layer and superficial stroma",
    ["Descemet's membrane and endothelium", "Epithelium only", "Full-thickness stroma up to the endothelium"],
    "Pterygium destroys Bowman's layer & superficial stroma.",
    [2], "Pterygium")
c.q(204, "oddoneout", "Pterygium is associated with all of the following EXCEPT:",
    "Cold climate",
    ["UV ray exposure", "Dust", "Humidity"],
    "Pterygium is associated with UV ray exposure, dust, humidity.",
    [3, 4, 5], "Pterygium")
c.q(204, "scenario", "The cause of pterygium is limbal stem cell deficiency leading to:",
    "Activation of matrix metalloproteinase",
    ["Deposition of iron in the cornea", "Deposition of lipid in the paralimbal area", "Elastic degeneration of collagen fibres"],
    "Cause: limbal stem cell deficiency -> activation of matrix metalloproteinase.",
    [6], "Pterygium")
c.q(204, "numeric", "Pterygium is more common on which side?",
    "Nasal more than lateral",
    ["Lateral more than nasal", "Equally on both sides", "Inferior more than superior"],
    "Site: Nasal > Lateral.",
    [7], "Pterygium")
c.q(204, "fillup", "In pterygium the triangular growth has its apex towards the ___.",
    "Cornea",
    ["Canthus", "Fornix", "Lacrimal gland"],
    "Clinical features: 1. Triangular growth with apex towards cornea.",
    [8], "Pterygium")
c.q(204, "scenario", "Stocker's line in pterygium is:",
    "Deposition of iron in front of the apex",
    ["A line of cicatrization", "Deposition of lipid in the paralimbal area", "An extra crease of the lower lid"],
    "2. Stocker's line: deposition of iron in front of apex.",
    [9], "Pterygium")
c.q(204, "scenario", "A pterygium is reducing a patient's vision. According to the book this is due to corneal astigmatism or:",
    "Encroaching into the visual axis (covering the pupillary area)",
    ["Recurrent inflammation of the pterygium", "Deposition of iron in front of the apex", "Associated cataract"],
    "Loss of vision in pterygium: a. corneal astigmatism; b. encroaching into visual axis (the photograph is labelled 'covers pupillary area').",
    [10, 11, 12, 13], "Pterygium")
c.q(204, "management", "What is the drawback of surgical excision of pterygium?",
    "It increases the rate of recurrence",
    ["It causes corneal perforation", "It causes ptosis", "It causes loss of the eyelid margin"],
    "Treatment: surgical excision - increased rate of recurrence.",
    [14], "Pterygium treatment")
c.q(204, "management", "Which topical agent is used to reduce recurrence after pterygium excision?",
    "Mitomycin C",
    ["Silver nitrate", "Tetracycline", "Olopatadine"],
    "To reduce recurrence: 1. Topical mitomycin C; 2. Autograft.",
    [15], "Pterygium treatment")
c.q(204, "recall", "The autograft used to reduce recurrence after pterygium excision is harvested from:",
    "The same eye, usually from the superior site, and fixed with sutures, fibrin glue or autologous serum",
    ["The other eye, usually from the superior site", "The buccal mucosa, fixed with sutures", "The same eye, usually from the inferior fornix"],
    "Autograft: harvested from same eye; site: usually superior; fixed with sutures/fibrin glue/autologous serum.",
    [16, 17, 18], "Pterygium treatment")

# ---------------------------------------------------------------- p205
c.unit("Pinguecula and concretions", "Conjunctiva",
       "Pinguecula = elastic degeneration of collagen fibres in the conjunctival stroma, commonest nasally, yellowish fat-like nodules; concretions = epithelial debris and mucus from friction while blinking, removed with a 26g needle, resolve with lubrication, contain no calcium.")
c.q(205, "fillup", "Pinguecula is ___ degeneration of collagen fibres in the stroma of the conjunctiva.",
    "Elastic",
    ["Mucoid", "Fibrinoid", "Calcific"],
    "Heading: Pinguecula & concretions. PINGUECULA: elastic degeneration of collagen fibres in stroma of conjunctiva.",
    [1, 2], "Pinguecula")
c.q(205, "recall", "What is the most common site of pinguecula?",
    "Nasal part of the conjunctiva",
    ["Temporal part of the conjunctiva", "Superior fornix", "Lower palpebral conjunctiva"],
    "m/c site: nasal part of conjunctiva.",
    [3], "Pinguecula")
c.q(205, "scenario", "A yellowish fat-like nodule is seen on the conjunctiva away from the cornea. The photograph on this page labels it as:",
    "Yellowish fat-like nodules - pinguecula",
    ["Minute yellowish-white elevations - concretions", "Phlycten near the limbus", "Sago grain follicles"],
    "Photograph caption (pinguecula): yellowish fat-like nodules.",
    [4], "Pinguecula")
c.q(205, "fillup", "Concretions are a collection of ___ and mucus.",
    "Epithelial debris",
    ["Calcium deposits", "Lymphoid aggregates", "Lipid droplets"],
    "CONCRETIONS: collection of epithelial debris & mucus.",
    [5], "Concretions")
c.q(205, "scenario", "Concretions are caused by irritation due to friction of the eyelid against the bulbar conjunctiva and cornea while:",
    "Blinking",
    ["Reading for long hours", "Sleeping", "Rubbing the eye with the knuckles"],
    "Cause: irritation d/t friction of eyelid against bulbar conjunctiva & cornea while blinking.",
    [6], "Concretions")
c.q(205, "management", "How are concretions removed?",
    "With a 26g needle",
    ["By cryotherapy of the conjunctiva", "By surgical excision under local anaesthesia", "By topical mitomycin C"],
    "Treatment: Removel with 26g needle. (Also: spontaneously resolves with good lubrication.)",
    [7, 8], "Concretions")
c.q(205, "truefalse", "True or false — 'Concretions contain calcium deposits.'",
    "False - the note states that concretions do not contain calcium deposits",
    ["True - they are calcific deposits in the conjunctiva", "False - they contain lipid deposits instead of calcium", "True - they contain calcium and mucus"],
    "Note: Concretions do not contain calcium deposits.",
    [9], "Concretions")
c.q(205, "fillup", "The photograph of concretions on this page shows minute ___ elevations.",
    "Yellowish-white",
    ["Reddish-blue", "Black", "Grey-brown"],
    "Photograph caption (concretions): minute yellowish-white elevations.",
    [10], "Concretions")

covered = c.finish()
