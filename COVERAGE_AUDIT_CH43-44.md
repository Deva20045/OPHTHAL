# Coverage audit - Chapters 43-44 (Book pp. 195-208)

Every source line, heading, table row, figure caption and bracket read from the scanned pages is listed as a numbered point, in book order, with the question ID(s) that test it. `authoring/lib.py::finish()` refuses to write a chapter unless every point is covered, questions are in (page, first-point) order, each question has 4 distinct options and the answer is not length-predictable.

## Chapter 43 - Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium (pp. 195-205): 119 questions, 14 units

### Book p195 - 15 source points, 11 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title ANATOMY OF CONJUNCTIVA, TYPES OF CONJUNCTIVITIS AND PTERYGIUM; heading Anatomy (00:00:50) | C43-001 |
| 2 | Conjunctiva is transparent mucous membrane | C43-001 |
| 3 | It does not cover cornea | C43-001 |
| 4 | Parts of conjunctiva: Bulbar (covers sclera) | C43-002, C43-003 |
| 5 | Parts: Forniceal | C43-003 |
| 6 | Parts: Palpebral (lines inner surface of eyelids) | C43-002, C43-003 |
| 7 | Plica semilunaris: represents nictitating membrane | C43-004 |
| 8 | Caruncle: contains hair follicles | C43-004 |
| 9 | Plica semilunaris & caruncle: labelled together as rudimentary structures | C43-004, C43-005 |
| 10 | Histology: 1. Outermost layer: epithelium (non-keratinised stratified squamous) | C43-006 |
| 11 | Contains a. Goblet cells: secrete mucin (forms innermost layer of tear film) on parasympathetic stimulation | C43-007, C43-008 |
| 12 | Contains b. melanocytes | C43-009 |
| 13 | Contains c. Langerhans cells | C43-009 |
| 14 | 2. Adenoid/lymphatic layer: develops after 3 months of age | C43-010 |
| 15 | 3. Fibrous layer: contains nerve fibres & blood vessels | C43-011 |

### Book p196 - 17 source points, 9 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Lymphatic drainage: only site of lymphatic drainage from the eye | C43-012 |
| 2 | Drainage medially -> submandibular lymph nodes | C43-013 |
| 3 | Drainage laterally -> peri-auricular & superficial parotid lymph nodes | C43-013 |
| 4 | Drainage schematic of the eye/face (label: drainage medially and laterally) | C43-013 |
| 5 | Heading Conjunctivitis (00:08:40); aka eye flu | C43-014 |
| 6 | Symptoms: redness | C43-015 |
| 7 | Symptoms: discharge sticking to eyelids | C43-015 |
| 8 | Symptoms: foreign body sensation | C43-015 |
| 9 | Symptoms: lacrimation | C43-015 |
| 10 | Symptoms: itching (if allergic) | C43-016 |
| 11 | Symptoms: pain and loss of vision (LOV): corneal involvement | C43-016, C43-017 |
| 12 | Signs: 1. Conjunctival hyperemia (redness) | C43-018 |
| 13 | DD of circumcorneal redness: glaucoma | C43-019 |
| 14 | circumcorneal redness: uveitis | C43-019 |
| 15 | circumcorneal redness: corneal ulcer | C43-019 |
| 16 | Photograph caption: Conjunctival hyperemia | C43-020 |
| 17 | Photograph + note: Circumcorneal hyperemia - seen in glaucoma, uveitis, corneal ulcer | C43-020 |

### Book p197 - 11 source points, 8 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | 2. Subconjunctival hemorrhage: no treatment required (resolves spontaneously in ~2 weeks) | C43-021 |
| 2 | 3. Chemosis: swelling of bulbar conjunctiva | C43-022 |
| 3 | 4. Discharge: mucopurulent/watery | C43-023 |
| 4 | Discharge causes colored halos & stickiness which resolves on washing eye | C43-023 |
| 5 | 5. Inflammatory reactions of conjunctiva: Papillae: hypertrophied vessels | C43-024 |
| 6 | Follicles: lymphoid aggregates | C43-025 |
| 7 | Etiology table: mucopurulent discharge - papillary reaction: Bacterial; follicular reaction: Chlamydia | C43-026 |
| 8 | Etiology table: watery discharge - papillary reaction: Allergic; follicular reaction: viral | C43-026 |
| 9 | Heading Bacterial conjunctivitis (00:17:22) | C43-027 |
| 10 | Acute mucopurulent conjunctivitis: m/c cause Staphylococcus aureus | C43-027 |
| 11 | Treatment: topical antibiotics | C43-028 |

### Book p198 - 22 source points, 15 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Acute purulent/hyperacute conjunctivitis/Blenorrhoea | C43-029 |
| 2 | m/c cause: Neisseria gonorrhoeae | C43-030 |
| 3 | Route of transmission: Oculogenital | C43-031 |
| 4 | Clinical features: 1. Copious purulent discharge | C43-032 |
| 5 | 2. Swelling of eyelids -> Overhanging | C43-032 |
| 6 | 3. Intense pain | C43-032 |
| 7 | 4. Pre-auricular lymphadenopathy | C43-032 |
| 8 | Treatment: IM Ceftriaxone 1g single dose | C43-033 |
| 9 | followed by Oral erythromycin x 2 weeks | C43-033 |
| 10 | Photograph caption: Blennorrhoea | C43-034 |
| 11 | Heading Acute membranous conjunctivitis: m/c cause overall/in adults: Pneumococcus | C43-035 |
| 12 | m/c cause in unimmunised children: Corynebacterium diphtheriae | C43-036 |
| 13 | Clinical features: membrane formed -> fused with epithelium -> bleeds on removal | C43-037 |
| 14 | Heading Acute pseudomembranous conjunctivitis: membrane does not fuse with epithelium | C43-037 |
| 15 | No bleeding on removal | C43-037 |
| 16 | Photograph caption: Pseudomembrane peeling | C43-038 |
| 17 | Heading Angular/diplobacillary conjunctivitis: m/c cause moraxella lacunata/axenfeld | C43-039 |
| 18 | Clinical features: excoriation at canthi (Lateral > medial) | C43-040 |
| 19 | Clinical features: redness at intermarginal strip | C43-041 |
| 20 | Clinical features: blepharitis (inflammation of eyelid margin) | C43-042 |
| 21 | Treatment: tetracycline 1% eye ointment for >= 2 wks | C43-043 |
| 22 | Treatment: zinc boric eye drops (zinc blocks proteolytic activity) | C43-043 |

### Book p199 - 22 source points, 9 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Viral Conjunctivitis (00:27:00); adenoviral conjunctivitis | C43-044 |
| 2 | Non-specific follicular conjunctivitis: serovars 1 to 11 & 19 | C43-044 |
| 3 | Epidemic keratoconjunctivitis (EKC): serovars 8, 19, 37 | C43-044 |
| 4 | Pharyngoconjunctival fever (PCF): serovars 3, 4, 7 | C43-044 |
| 5 | Pharyngoconjunctival fever: associated with preauricular lymphadenopathy | C43-045 |
| 6 | Apollo conjunctivitis/Acute hemorrhagic conjunctivitis: hemorrhage of palpebral & bulbar conjunctiva | C43-046 |
| 7 | Photograph: acute hemorrhagic (Apollo) conjunctivitis of both eyes | C43-046 |
| 8 | Causes: 1. Picornavirus: Enterovirus type 70, Coxsackie A24 (m/c) | C43-047 |
| 9 | Causes: 2. Adenovirus type 11 | C43-047 |
| 10 | molluscum contagiosum clinical features: unilateral, painless nodule with umbilicated appearance | C43-048 |
| 11 | Nodule contains viral particles | C43-048 |
| 12 | Periodic shedding of virus -> conjunctivitis | C43-048 |
| 13 | Treatment: surgical excision [if cosmetic indication (+)] | C43-048 |
| 14 | Photograph caption: umbilicated nodule | C43-049 |
| 15 | Heading Chlamydial Conjunctivitis (00:33:14): Adult inclusion conjunctivitis: D to K serovars | C43-050 |
| 16 | Trachoma: A, B, Ba, C serovars | C43-050 |
| 17 | Ophthalmia neonatorum: D to K serovars; other causes | C43-050 |
| 18 | TRACHOMA aka Egyptian ophthalmia | C43-051 |
| 19 | Route of transmission: mnemonic: 3F | C43-052 |
| 20 | 1. Fingers | C43-052 |
| 21 | 2. Flies | C43-052 |
| 22 | 3. Fomites | C43-052 |

### Book p200 - 21 source points, 9 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Pathology: Type IV hypersensitivity reaction: active inflammation + cicatrization | C43-053 |
| 2 | Age group: < 10 yrs | C43-054 |
| 3 | Clinical signs: 1. Sago grain follicles: necrosis & Leber | C43-055 |
| 4 | m/c site: upper palpebral conjunctiva | C43-055 |
| 5 | Necrosis & Leber cells seen | C43-055 |
| 6 | Photograph caption: Sago grain follicles | C43-055 |
| 7 | 2. Cicatricial sign: a. Arlt's line: line of cicatrization | C43-056 |
| 8 | Photograph labels: Arlt's line - lower 2/3rd, upper 1/3rd | C43-056 |
| 9 | b. Herbert's pits: pathognomonic | C43-057 |
| 10 | d/t healing of limbal follicles | C43-057 |
| 11 | Photograph label: Herbert's pits | C43-057 |
| 12 | c. Pannus: vascularisation of cornea superiorly | C43-058 |
| 13 | Complications: trichiasis (inturned eyelash) -> corneal ulcer -> scar formation -> loss of vision | C43-059 |
| 14 | Treatment: SAFE strategy (WHO, 1996) | C43-060 |
| 15 | Surgery for inturned eyelids | C43-060 |
| 16 | Antibiotics: Azithromycin 1g | C43-060 |
| 17 | Facial cleanliness | C43-060 |
| 18 | Environmental change | C43-060 |
| 19 | Indications for treatment: prevalence in 1-9 yr old children > 10% -> mass prophylaxis | C43-061 |
| 20 | Prevalence 5-10% -> treatment to affected children & family | C43-061 |
| 21 | Prevalence < 5% -> facial cleanliness & environmental change advised | C43-061 |

### Book p201 - 13 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | FISTO classification (WHO): TF: Trachomatous inflammation follicular: > 5 follicles +; active stage, treatment: antibiotics | C43-062, C43-063 |
| 2 | TI: Trachomatous inflammation intense: thickening of upper palpebral conjunctiva; active stage (antibiotics) | C43-062, C43-063, C43-064 |
| 3 | TS: Trachomatous scarring: Arlt's line; inactive stage: no treatment | C43-062, C43-063, C43-064 |
| 4 | TT: Trachomatous trichiasis: eyelash growing inwards; requires surgery | C43-063, C43-064 |
| 5 | CO: Corneal opacity: visual impairment; management - | C43-062 |
| 6 | Photograph captions: trachomatous inflammation follicular (TF), follicular and intense (TF), trachomatous scarring (TS), trachomatous trichiasis (TT), corneal opacity (CO) | C43-065 |
| 7 | Heading OPHTHALMIA NEONATORUM: conjunctivitis in neonates (< 28 days of onset) | C43-066 |
| 8 | Onset within first 6h: chemical conjunctivitis (silver nitrate) | C43-067 |
| 9 | Onset 24 to 48h: Neisseria gonorrhoeae (most severe) | C43-067, C43-068 |
| 10 | Onset 2 to 5 d: other bacteria | C43-069 |
| 11 | Onset 5 to 7 d: HSV-II | C43-067 |
| 12 | Onset > 1 wk: Chlamydia trachomatis (D to K): m/c | C43-070 |
| 13 | Photograph caption: Ophthalmia neonatorum | C43-071 |

### Book p202 - 21 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Prevention: 1. Crede's method: topical 1% silver nitrate (not recommended d/t chemical conjunctivitis) | C43-072 |
| 2 | Prevention: 2. 0.5% erythromycin; 3. 1% tetracycline | C43-073 |
| 3 | Both: single application | C43-073 |
| 4 | Both: within 1 hr of birth | C43-073 |
| 5 | Heading Allergic conjunctivitis (00:50:24); presents with papillae reaction + watery discharge + itching | C43-074 |
| 6 | VERNAL KERATOCONJUNCTIVITIS/SPRING CATARRH: Type I hypersensitivity reaction (eg: pollen) | C43-075 |
| 7 | Incidence: age 5-15 yrs | C43-076 |
| 8 | Incidence: males > females (young boys) | C43-076 |
| 9 | Incidence: m/c in spring & summer | C43-076 |
| 10 | Incidence: H/O atopy present | C43-077 |
| 11 | Clinical signs: 1. Papillary hypertrophy: cobble stone papillae | C43-078 |
| 12 | Giant papillae: > 1mm size | C43-079 |
| 13 | 2. Horner Trantas sign: collection of eosinophils + epithelial debris | C43-080 |
| 14 | Horner Trantas sign site: on limbus | C43-080 |
| 15 | Photograph labels: Horner trantas sign; Pseudogerontoxon | C43-081 |
| 16 | 3. Pseudogerontoxon: paralimbal grey-white band (d/t lipid deposition) in children | C43-081 |
| 17 | Pseudogerontoxon appearance similar to arcus senilis | C43-081 |
| 18 | 4. Shield ulcer (in cornea) | C43-082 |
| 19 | 5. Dennie morgan line: extra lower-lid crease | C43-083 |
| 20 | 6. Maxwell Lyon sign: ropy discharge | C43-084 |
| 21 | Note: excessive itching -> increased incidence of keratoconus | C43-085 |

### Book p203 - 28 source points, 15 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Treatment (VKC): 1. Cold compress | C43-086 |
| 2 | 2. Topical anti-histamine | C43-086 |
| 3 | 3. Topical mast cell stabilisers | C43-086 |
| 4 | 4. DOC: Olopatadine or Alcaftadine | C43-087 |
| 5 | 5. Topical steroids in acute exacerbation (for symptomatic treatment) | C43-088 |
| 6 | ATOPIC KERATOCONJUNCTIVITIS: seen in 2nd to 5th decade | C43-089 |
| 7 | Clinical features: eyelids: Hertoghe sign (lateral eyebrow lost) | C43-090 |
| 8 | Clinical features: itching | C43-091 |
| 9 | Clinical features: papillae | C43-091 |
| 10 | Clinical features: watery discharge | C43-091 |
| 11 | Treatment: 1. topical anti-histamine | C43-092 |
| 12 | 2. topical mast cell stabilisers | C43-092 |
| 13 | GIANT PAPILLARY KERATOCONJUNCTIVITIS: papillae > 1mm | C43-093 |
| 14 | Type IV hypersensitivity reaction | C43-093 |
| 15 | Etiology: mechanically induced by contact lens | C43-094 |
| 16 | ocular prostheses | C43-094 |
| 17 | protruding sutures | C43-094 |
| 18 | Treatment: anti-histamine + surgery to remove irritant (if required) | C43-095 |
| 19 | PHYLCTENULAR KERATOCONJUNCTIVITIS: Type IV hypersensitivity reaction in response to endogenous allergen | C43-096 |
| 20 | Etiology: m/c in India: TB | C43-097 |
| 21 | Etiology: m/c in western countries: Staphylococcus aureus | C43-097 |
| 22 | Clinical features: phlycten: nodule near limbus | C43-098 |
| 23 | Grows towards cornea -> ulcerates | C43-099 |
| 24 | Gives rise to: sacrofulous ulcer | C43-099 |
| 25 | fascicular ulcer | C43-099 |
| 26 | miliary ulcer | C43-099 |
| 27 | Treatment: topical steroids | C43-100 |
| 28 | Photograph caption: Phlycten | C43-098 |

### Book p204 - 19 source points, 11 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Pterygium (01:07:20): triangular, fibrovascular growth of degenerative sub-conjunctival tissue over cornea | C43-101 |
| 2 | Destroys Bowman's layer & superficial stroma | C43-102 |
| 3 | Associated with UV ray exposure | C43-103 |
| 4 | Associated with dust | C43-103 |
| 5 | Associated with humidity | C43-103 |
| 6 | Cause: limbal stem cell deficiency -> activation of matrix metalloproteinase | C43-104 |
| 7 | Site: Nasal > Lateral | C43-105 |
| 8 | Clinical features: 1. triangular growth with apex towards cornea | C43-106 |
| 9 | 2. Stocker's line: deposition of iron in front of apex | C43-107 |
| 10 | 3. Loss of vision | C43-108 |
| 11 | Causes of LOV: a. corneal astigmatism | C43-108 |
| 12 | b. encroaching into visual axis | C43-108 |
| 13 | Photograph label: covers pupillary area | C43-108 |
| 14 | Treatment: surgical excision: increased rate of recurrence | C43-109 |
| 15 | To reduce recurrence: 1. topical mitomycin C | C43-110 |
| 16 | 2. Autograft: harvested from same eye | C43-111 |
| 17 | Autograft site: usually superior | C43-111 |
| 18 | Autograft fixed with sutures/fibrin glue/autologous serum | C43-111 |
| 19 | Photographs: pterygium with apex towards cornea; pterygium covering the pupillary area | C43-101 |

### Book p205 - 10 source points, 8 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Heading Pinguecula & concretions (01:14:28) | C43-112 |
| 2 | PINGUECULA: elastic degeneration of collagen fibres in stroma of conjunctiva | C43-112 |
| 3 | m/c site: nasal part of conjunctiva | C43-113 |
| 4 | Photograph caption: yellowish fat-like nodules | C43-114 |
| 5 | CONCRETIONS: collection of epithelial debris & mucus | C43-115 |
| 6 | Cause: irritation d/t friction of eyelid against bulbar conjunctiva & cornea while blinking | C43-116 |
| 7 | Treatment: removal with 26g needle | C43-117 |
| 8 | Spontaneously resolves with good lubrication | C43-117 |
| 9 | Note: concretions do not contain calcium deposits | C43-118 |
| 10 | Photograph caption: minute yellowish-white elevations | C43-119 |

## Chapter 44 - Eyelids : Anatomy and Pathologies (pp. 206-208): 39 questions, 8 units

### Book p206 - 18 source points, 14 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Chapter title EYELIDS : ANATOMY AND PATHOLOGIES; heading Anatomy (00:01:01) | C44-001 |
| 2 | 3 muscles: Levator palpebrae superioris - CN III - elevation of upper lid - presentation in palsy: ptosis | C44-001, C44-002 |
| 3 | Müller's muscle - sympathetic fibres - elevation of upper lid - presentation in palsy: ptosis | C44-001, C44-002 |
| 4 | Orbicularis oculi - CN VII - closure of eyelid - presentation in palsy: lagophthalmos | C44-001, C44-003 |
| 5 | 3 glands: meibomian (tarsal) - modified sebaceous - opens posterior to anterior surface of eyelid margin | C44-004, C44-005 |
| 6 | Zeis - modified sebaceous - opens at base of lash follicles | C44-006 |
| 7 | moll - modified sweat - opens at base of lash follicles | C44-004 |
| 8 | EYELID schematic: grey line divides eyelid into anterior lamina and posterior lamina | C44-007 |
| 9 | Anterior lamina: skin - thinnest skin in the body | C44-008, C44-009 |
| 10 | Anterior lamina: subcutaneous tissue | C44-008 |
| 11 | Anterior lamina: muscles | C44-008 |
| 12 | Posterior: tarsal plate has only fibrous tissue | C44-010 |
| 13 | Posterior: palpebral conjunctiva | C44-011 |
| 14 | Schematic labels: gray line, Zeis & moll glands, meibomian gland, eye lash | C44-007, C44-012 |
| 15 | Pathologies heading (00:09:16) | C44-013 |
| 16 | CHALAZION & HORDEOLUM: chalazion - lipogranulomatous inflammation of meibomian gland | C44-013 |
| 17 | external hordeolum/stye - suppurative inflammation of Zeis gland | C44-013 |
| 18 | Infectivity: chalazion non-infective; external hordeolum infective - S. aureus | C44-014 |

### Book p207 - 22 source points, 15 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | Swelling: chalazion - painless, circumscribed swelling away from lid margin | C44-015 |
| 2 | External hordeolum/stye - painful, diffuse swelling at the lid margin | C44-016 |
| 3 | Rx chalazion: incision & curettage - horizontal incision on posterior part of eyelid (conjunctiva) | C44-017 |
| 4 | Rx chalazion: intralesional triamcinolone | C44-017 |
| 5 | Rx hordeolum: hot compresses | C44-018 |
| 6 | Rx hordeolum: oral antibiotics if recurrent | C44-018 |
| 7 | Complications - chalazion: recurrence -> sebaceous cell carcinoma | C44-019 |
| 8 | Appearance row: photographs of chalazion and external hordeolum | C44-015, C44-019 |
| 9 | Hordeolum internum: suppurative inflammation of meibomian gland | C44-020 |
| 10 | TRICHIASIS: inward misdirection of eyelashes | C44-021 |
| 11 | Trichiasis causes corneal opacity | C44-022 |
| 12 | Photograph caption: Trichiasis | C44-023 |
| 13 | Treatment: epilation every 1-2 months | C44-024 |
| 14 | Treatment: cryotherapy of lash base: definitive | C44-024 |
| 15 | ENTROPION & ECTROPION table: entropion - inward turning of eyelid margin | C44-025 |
| 16 | Ectropion - outward turning of eyelid margin; m/c cause: senility | C44-026 |
| 17 | Rx entropion: spastic -> botulinum toxin injection | C44-027 |
| 18 | Rx entropion: senile -> modified wheeler operation, weiss operation | C44-027 |
| 19 | Rx entropion: cicatricial -> modified burrows operation, wedge resection | C44-027 |
| 20 | Rx ectropion: medial conjunctivoplasty | C44-028 |
| 21 | Rx ectropion: burvon smith operation | C44-029 |
| 22 | Photographs: entropion and ectropion | C44-025, C44-029 |

### Book p208 - 14 source points, 10 questions

| # | Source line / point (as read from scan) | Question ID(s) |
|---|---|---|
| 1 | DISTICHIASIS: extra posterior row of eye lashes | C44-030 |
| 2 | MADAROSIS: loss of lateral 1/3rd of eye lashes & eyebrow d/t chronic rubbing of the eye | C44-031 |
| 3 | Photographs: distichiasis, madarosis | C44-031 |
| 4 | TYLOSIS: thickening of eyelid margin | C44-032 |
| 5 | ANKYLOBLEPHARON: fusion of eyelid margin of upper & lower lid | C44-033 |
| 6 | Ankyloblepharon: post trauma | C44-033 |
| 7 | CONGENITAL PTOSIS: d/t defective development of levator palpebrae superioris | C44-034 |
| 8 | Clinical features: absent upper lid crease | C44-035 |
| 9 | Clinical features: lid lag on downgaze - failure of eyelid to go down on downward gaze | C44-035, C44-036 |
| 10 | Photograph caption: Congenital Ptosis | C44-034 |
| 11 | Treatment table: moderate ptosis + fair LPS function -> LPS resection | C44-037 |
| 12 | Severe ptosis + poor LPS function -> frontalis sling SX | C44-037 |
| 13 | Marcus Gunn jaw winking syndrome: d/t trigemino-oculomotor nerve synkinesis | C44-038 |
| 14 | Closed jaw -> ptosis; open jaw -> lid moves up | C44-039 |

## Totals

- Source points: 253, all covered (0 uncovered)
- Questions: 158
