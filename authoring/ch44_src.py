from lib import Chapter

# Read from the scanned book pages 206-208 (PDF 93-95 of Part 2).
POINTS = {
206: [
 "Chapter title EYELIDS : ANATOMY AND PATHOLOGIES; heading Anatomy (00:01:01)",
 "3 muscles: Levator palpebrae superioris - CN III - elevation of upper lid - presentation in palsy: ptosis",
 "Müller's muscle - sympathetic fibres - elevation of upper lid - presentation in palsy: ptosis",
 "Orbicularis oculi - CN VII - closure of eyelid - presentation in palsy: lagophthalmos",
 "3 glands: meibomian (tarsal) - modified sebaceous - opens posterior to anterior surface of eyelid margin",
 "Zeis - modified sebaceous - opens at base of lash follicles",
 "moll - modified sweat - opens at base of lash follicles",
 "EYELID schematic: grey line divides eyelid into anterior lamina and posterior lamina",
 "Anterior lamina: skin - thinnest skin in the body",
 "Anterior lamina: subcutaneous tissue",
 "Anterior lamina: muscles",
 "Posterior: tarsal plate has only fibrous tissue",
 "Posterior: palpebral conjunctiva",
 "Schematic labels: gray line, Zeis & moll glands, meibomian gland, eye lash",
 "Pathologies heading (00:09:16)",
 "CHALAZION & HORDEOLUM: chalazion - lipogranulomatous inflammation of meibomian gland",
 "external hordeolum/stye - suppurative inflammation of Zeis gland",
 "Infectivity: chalazion non-infective; external hordeolum infective - S. aureus",
],
207: [
 "Swelling: chalazion - painless, circumscribed swelling away from lid margin",
 "External hordeolum/stye - painful, diffuse swelling at the lid margin",
 "Rx chalazion: incision & curettage - horizontal incision on posterior part of eyelid (conjunctiva)",
 "Rx chalazion: intralesional triamcinolone",
 "Rx hordeolum: hot compresses",
 "Rx hordeolum: oral antibiotics if recurrent",
 "Complications - chalazion: recurrence -> sebaceous cell carcinoma",
 "Appearance row: photographs of chalazion and external hordeolum",
 "Hordeolum internum: suppurative inflammation of meibomian gland",
 "TRICHIASIS: inward misdirection of eyelashes",
 "Trichiasis causes corneal opacity",
 "Photograph caption: Trichiasis",
 "Treatment: epilation every 1-2 months",
 "Treatment: cryotherapy of lash base: definitive",
 "ENTROPION & ECTROPION table: entropion - inward turning of eyelid margin",
 "Ectropion - outward turning of eyelid margin; m/c cause: senility",
 "Rx entropion: spastic -> botulinum toxin injection",
 "Rx entropion: senile -> modified wheeler operation, weiss operation",
 "Rx entropion: cicatricial -> modified burrows operation, wedge resection",
 "Rx ectropion: medial conjunctivoplasty",
 "Rx ectropion: burvon smith operation",
 "Photographs: entropion and ectropion",
],
208: [
 "DISTICHIASIS: extra posterior row of eye lashes",
 "MADAROSIS: loss of lateral 1/3rd of eye lashes & eyebrow d/t chronic rubbing of the eye",
 "Photographs: distichiasis, madarosis",
 "TYLOSIS: thickening of eyelid margin",
 "ANKYLOBLEPHARON: fusion of eyelid margin of upper & lower lid",
 "Ankyloblepharon: post trauma",
 "CONGENITAL PTOSIS: d/t defective development of levator palpebrae superioris",
 "Clinical features: absent upper lid crease",
 "Clinical features: lid lag on downgaze - failure of eyelid to go down on downward gaze",
 "Photograph caption: Congenital Ptosis",
 "Treatment table: moderate ptosis + fair LPS function -> LPS resection",
 "Severe ptosis + poor LPS function -> frontalis sling SX",
 "Marcus Gunn jaw winking syndrome: d/t trigemino-oculomotor nerve synkinesis",
 "Closed jaw -> ptosis; open jaw -> lid moves up",
],
}

c = Chapter(44, "Eyelids : Anatomy and Pathologies", 206, 208, POINTS)

# ---------------------------------------------------------------- p206
c.unit("Muscles of the eyelid", "Adnexa",
       "Levator palpebrae superioris (CN III) and Müller's muscle (sympathetic) elevate the upper lid - palsy gives ptosis; orbicularis oculi (CN VII) closes the eyelid - palsy gives lagophthalmos.")
c.q(206, "match", "Match the eyelid muscle with its nerve supply — 1) Levator palpebrae superioris  2) Müller's muscle  3) Orbicularis oculi  … A) Sympathetic fibres  B) CN III  C) CN VII",
    "1-B, 2-A, 3-C",
    ["1-A, 2-B, 3-C", "1-B, 2-C, 3-A", "1-C, 2-A, 3-B"],
    "3 muscles table: Levator palpebrae superioris - CN III; Müller's muscle - sympathetic fibres; Orbicularis oculi - CN VII.",
    [1, 2, 3, 4], "Eyelid muscles")
c.q(206, "fillup", "Elevation of the upper lid is produced by the levator palpebrae superioris and ___.",
    "Müller's muscle",
    ["Orbicularis oculi", "Frontalis", "Superior oblique"],
    "Levator palpebrae superioris and Müller's muscle both elevate the upper lid; orbicularis oculi closes the eyelid.",
    [2, 3], "Eyelid muscles")
c.q(206, "fillup", "Palsy of the orbicularis oculi (CN VII) presents as ___.",
    "Lagophthalmos",
    ["Ptosis", "Proptosis", "Entropion"],
    "Orbicularis oculi - CN VII - closure of eyelid; presentation in palsy: lagophthalmos. (Palsy of the lid elevators presents as ptosis.)",
    [4], "Eyelid muscles")

c.unit("Glands of the eyelid", "Adnexa",
       "Meibomian (tarsal) = modified sebaceous gland opening posterior to the anterior surface of the eyelid margin; Zeis = modified sebaceous and Moll = modified sweat gland, both opening at the base of the lash follicles.")
c.q(206, "match", "Match the eyelid gland with its type — 1) Meibomian (tarsal) gland  2) Moll gland  … A) Modified sweat gland  B) Modified sebaceous gland",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "3 glands: meibomian (tarsal) - modified sebaceous; Zeis - modified sebaceous; moll - modified sweat.",
    [5, 7], "Eyelid glands")
c.q(206, "fillup", "The meibomian (tarsal) gland opens ___ to the anterior surface of the eyelid margin.",
    "Posterior",
    ["Anterior", "Medial", "Lateral"],
    "Meibomian (tarsal) gland: modified sebaceous, opens posterior to anterior surface of eyelid margin.",
    [5], "Eyelid glands")
c.q(206, "scenario", "Which gland of the eyelid is a modified sebaceous gland that opens at the base of the lash follicles?",
    "Zeis gland",
    ["Meibomian (tarsal) gland", "Moll gland", "Accessory lacrimal gland of Wolfring"],
    "Zeis - modified sebaceous - opens at base of lash follicles. (Moll gland opens there too but is a modified sweat gland.)",
    [6], "Eyelid glands")

c.unit("Structure of the eyelid", "Adnexa",
       "Grey line divides the eyelid into anterior lamina (skin - thinnest in the body, subcutaneous tissue, muscles) and posterior lamina (tarsal plate of only fibrous tissue, palpebral conjunctiva); schematic labels: gray line, Zeis & moll glands, meibomian gland, eye lash.")
c.q(206, "fillup", "The grey line divides the eyelid into the anterior lamina and the ___.",
    "Posterior lamina",
    ["Marginal lamina", "Tarsal lamina", "Conjunctival lamina"],
    "EYELID: Grey line divides eyelid into anterior lamina and posterior lamina (schematic label: Gray line).",
    [8, 14], "Eyelid structure")
c.q(206, "oddoneout", "The anterior lamina of the eyelid consists of all of the following EXCEPT:",
    "Tarsal plate",
    ["Skin", "Subcutaneous tissue", "Muscles"],
    "Anterior lamina: skin, subcutaneous tissue, muscles. The tarsal plate and palpebral conjunctiva belong to the posterior lamina.",
    [9, 10, 11], "Eyelid structure")
c.q(206, "recall", "The skin of the eyelid is:",
    "The thinnest skin in the body",
    ["The thickest skin in the body", "Devoid of hair follicles", "Keratinised and rigid"],
    "Anterior lamina: skin - thinnest skin in the body.",
    [9], "Eyelid structure")
c.q(206, "fillup", "The tarsal plate of the posterior lamina contains only ___ tissue.",
    "Fibrous",
    ["Elastic", "Muscular", "Adipose"],
    "Posterior: tarsal plate has only fibrous tissue.",
    [12], "Eyelid structure")
c.q(206, "recall", "The posterior lamina of the eyelid consists of the tarsal plate and:",
    "Palpebral conjunctiva",
    ["Skin and subcutaneous tissue", "Orbicularis oculi", "Levator palpebrae superioris"],
    "Posterior lamina: tarsal plate (only fibrous tissue) and palpebral conjunctiva.",
    [13], "Eyelid structure")
c.q(206, "recall", "In the schematic of the eyelid, the Zeis & moll glands are shown opening at the base of the ___, while the meibomian gland opens behind the grey line.",
    "Eye lash",
    ["Tarsal plate", "Plica semilunaris", "Lacrimal punctum"],
    "Schematic labels: Gray line, Zeis & moll glands, meibomian gland, eye lash.",
    [14], "Eyelid structure")

c.unit("Chalazion and hordeolum", "Adnexa",
       "Chalazion = non-infective lipogranulomatous inflammation of meibomian gland, painless swelling away from the lid margin, incision & curettage (horizontal, posterior) or intralesional triamcinolone, recurrence may lead to sebaceous cell carcinoma; external hordeolum/stye = infective suppurative inflammation of Zeis gland (S. aureus), painful diffuse swelling at the lid margin, hot compresses + oral antibiotics if recurrent; hordeolum internum = meibomian gland.")
c.q(206, "match", "Match the condition with its pathology — 1) Chalazion  2) External hordeolum/stye  … A) Suppurative inflammation of Zeis gland  B) Lipogranulomatous inflammation of meibomian gland",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "CHALAZION & HORDEOLUM: chalazion - lipogranulomatous inflammation of meibomian gland (non-infective); external hordeolum/stye - suppurative inflammation of Zeis gland (infective).",
    [15, 16, 17], "Chalazion and hordeolum")
c.q(206, "fillup", "External hordeolum/stye is infective, most commonly due to ___.",
    "S. aureus",
    ["Streptococcus pyogenes", "Moraxella lacunata", "HSV-II"],
    "Infectivity: chalazion non-infective; external hordeolum infective - S. aureus.",
    [18], "Chalazion and hordeolum")
c.q(207, "scenario", "A patient has a painless, circumscribed swelling away from the lid margin (photograph of the appearance row). The diagnosis is:",
    "Chalazion",
    ["External hordeolum/stye", "Hordeolum internum", "Tylosis"],
    "Swelling: chalazion - painless, circumscribed swelling away from lid margin (appearance row photographs).",
    [1, 8], "Chalazion and hordeolum")
c.q(207, "scenario", "A patient has a painful, diffuse swelling at the lid margin. The diagnosis is:",
    "External hordeolum/stye",
    ["Chalazion", "Madarosis", "Tylosis"],
    "External hordeolum/stye: painful, diffuse swelling at the lid margin.",
    [2], "Chalazion and hordeolum")
c.q(207, "match", "Match the treatment of chalazion with its detail — 1) Incision & curettage  2) Intralesional injection  … A) Triamcinolone  B) Horizontal incision on the posterior part of the eyelid (conjunctiva)",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Rx of chalazion: incision & curettage - horizontal incision on posterior part of eyelid (conjunctiva); intralesional triamcinolone.",
    [3, 4], "Chalazion treatment")
c.q(207, "management", "Treatment of external hordeolum/stye is:",
    "Hot compresses, with oral antibiotics if recurrent",
    ["Incision and curettage with intralesional triamcinolone", "Cryotherapy of the lash base", "Topical mitomycin C"],
    "Rx hordeolum: hot compresses; oral antibiotics if recurrent.",
    [5, 6], "Hordeolum treatment")
c.q(207, "scenario", "A chalazion recurs repeatedly. Which complication does the table warn about?",
    "Sebaceous cell carcinoma",
    ["Squamous cell carcinoma", "Basal cell carcinoma", "Malignant melanoma"],
    "Complications - chalazion: recurrence -> sebaceous cell carcinoma. (Hordeolum: no complication listed, appearance row gives its photograph.)",
    [7, 8], "Chalazion complications")
c.q(207, "recall", "Hordeolum internum is suppurative inflammation of the ___ gland.",
    "Meibomian",
    ["Zeis", "Moll", "Accessory lacrimal"],
    "Hordeolum internum: suppurative inflammation of meibomian gland.",
    [9], "Chalazion and hordeolum")

c.unit("Trichiasis", "Adnexa",
       "Inward misdirection of eyelashes causing corneal opacity; epilation every 1-2 months, with cryotherapy of the lash base as the definitive treatment.")
c.q(207, "fillup", "Trichiasis is ___ of the eyelashes.",
    "Inward misdirection",
    ["Outward misdirection", "Loss of the lateral third", "An extra posterior row"],
    "TRICHIASIS: inward misdirection of eyelashes.",
    [10], "Trichiasis")
c.q(207, "scenario", "Trichiasis causes ___ of the cornea.",
    "Opacity",
    ["Vascularisation", "Ectasia", "Oedema"],
    "Trichiasis causes corneal opacity.",
    [11], "Trichiasis")
c.q(207, "recall", "The clinical photograph of lashes touching the globe on this page is captioned:",
    "Trichiasis",
    ["Distichiasis", "Madarosis", "Entropion"],
    "Photograph caption: Trichiasis - inward misdirection of eyelashes.",
    [12], "Trichiasis")
c.q(207, "management", "Which is the definitive treatment of trichiasis?",
    "Cryotherapy of the lash base",
    ["Epilation every 1-2 months", "Botulinum toxin injection", "Modified Wheeler operation"],
    "Treatment: epilation every 1-2 months; cryotherapy of lash base - definitive.",
    [13, 14], "Trichiasis treatment")

c.unit("Entropion and ectropion", "Adnexa",
       "Entropion = inward turning of the eyelid margin (spastic - botulinum toxin; senile - modified Wheeler/Weiss operation; cicatricial - modified Burrows operation, wedge resection); ectropion = outward turning of the eyelid margin, most commonly due to senility, treated by medial conjunctivoplasty or burvon smith operation.")
c.q(207, "fillup", "Entropion is inward turning of the ___.",
    "Eyelid margin",
    ["Punctum", "Lateral canthus", "Tarsal plate"],
    "ENTROPION & ECTROPION table: entropion - inward turning of eyelid margin (photograph of entropion).",
    [15, 22], "Entropion and ectropion")
c.q(207, "scenario", "Outward turning of the eyelid margin, most commonly caused by senility, is called:",
    "Ectropion",
    ["Entropion", "Distichiasis", "Ankyloblepharon"],
    "Ectropion - outward turning of eyelid margin; m/c cause: senility.",
    [16], "Entropion and ectropion")
c.q(207, "match", "Match the type of entropion with its operation — 1) Spastic  2) Senile  3) Cicatricial  … A) Modified Burrows operation, wedge resection  B) Botulinum toxin injection  C) Modified Wheeler operation, Weiss operation",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Rx of entropion: spastic -> botulinum toxin injection; senile -> modified wheeler operation, weiss operation; cicatricial -> modified burrows operation, wedge resection.",
    [17, 18, 19], "Entropion treatment")
c.q(207, "recall", "Which operation is listed for ectropion?",
    "Medial conjunctivoplasty",
    ["Modified Wheeler operation", "Weiss operation", "Modified Burrows operation"],
    "Rx of ectropion: medial conjunctivoplasty; burvon smith operation. (The other options are operations for entropion.)",
    [20], "Ectropion treatment")
c.q(207, "recall", "Besides medial conjunctivoplasty, the other operation listed for ectropion (as written in the book) is:",
    "Burvon smith operation",
    ["Wedge resection", "Botulinum toxin injection", "Modified Burrows operation"],
    "Rx of ectropion: medial conjunctivoplasty; burvon smith operation (the operation is written this way in the book).",
    [21, 22], "Ectropion treatment")

c.unit("Distichiasis, madarosis, tylosis and ankyloblepharon", "Adnexa",
       "Distichiasis = extra posterior row of lashes; madarosis = loss of lateral 1/3rd of lashes and eyebrow due to chronic rubbing; tylosis = thickening of the eyelid margin; ankyloblepharon = post-traumatic fusion of the upper and lower eyelid margins.")
c.q(208, "fillup", "Distichiasis is an extra ___ row of eye lashes.",
    "Posterior",
    ["Anterior", "Medial", "Inferior"],
    "DISTICHIASIS: extra posterior row of eye lashes (photograph: distichiasis).",
    [1], "Distichiasis")
c.q(208, "scenario", "A patient has lost the lateral one-third of his eye lashes and eyebrow due to chronic rubbing of the eye. This is called:",
    "Madarosis",
    ["Distichiasis", "Tylosis", "Trichiasis"],
    "MADAROSIS: loss of lateral 1/3rd of eye lashes & eyebrow d/t chronic rubbing of the eye (photograph: madarosis).",
    [2, 3], "Madarosis")
c.q(208, "fillup", "Tylosis is thickening of the ___.",
    "Eyelid margin",
    ["Tarsal plate", "Cornea", "Conjunctiva"],
    "TYLOSIS: thickening of eyelid margin.",
    [4], "Tylosis")
c.q(208, "scenario", "Fusion of the eyelid margins of the upper and lower lid, occurring after trauma, is:",
    "Ankyloblepharon",
    ["Symblepharon", "Distichiasis", "Entropion"],
    "ANKYLOBLEPHARON: fusion of eyelid margin of upper & lower lid; post trauma.",
    [5, 6], "Ankyloblepharon")

c.unit("Congenital ptosis and Marcus Gunn jaw winking syndrome", "Adnexa",
       "Congenital ptosis from defective development of levator palpebrae superioris; absent upper lid crease and lid lag on downgaze; moderate ptosis with fair LPS function - LPS resection, severe ptosis with poor LPS function - frontalis sling Sx; Marcus Gunn jaw winking = trigemino-oculomotor synkinesis (closed jaw - ptosis, open jaw - lid moves up).")
c.q(208, "fillup", "Congenital ptosis is due to defective development of the ___.",
    "Levator palpebrae superioris",
    ["Müller's muscle", "Orbicularis oculi", "Frontalis"],
    "CONGENITAL PTOSIS: d/t defective development of levator palpebrae superioris (photograph: congenital ptosis).",
    [7, 10], "Congenital ptosis")
c.q(208, "recall", "The two clinical features of congenital ptosis given in the book are absent upper lid crease and:",
    "Lid lag on downgaze",
    ["Proptosis on upgaze", "Lid retraction on upgaze", "Lagophthalmos during sleep"],
    "Clinical features: absent upper lid crease; lid lag on downgaze - failure of eyelid to go down on downward gaze.",
    [8, 9], "Congenital ptosis")
c.q(208, "scenario", "Lid lag on downgaze in congenital ptosis means:",
    "Failure of the eyelid to go down on downward gaze",
    ["Failure of the eyelid to move up on upward gaze", "Failure of the eyelid to close on blinking", "Downward displacement of the lid on upgaze"],
    "Lid lag on downgaze: failure of eyelid to go down on downward gaze.",
    [9], "Congenital ptosis")
c.q(208, "match", "Match the ptosis with its treatment — 1) Moderate ptosis, fair LPS function  2) Severe ptosis, poor LPS function  … A) Frontalis sling SX  B) LPS resection",
    "1-B, 2-A",
    ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"],
    "Treatment table: moderate ptosis with fair LPS function -> LPS resection; severe ptosis with poor LPS function -> frontalis sling SX.",
    [11, 12], "Congenital ptosis treatment")
c.q(208, "fillup", "Marcus Gunn jaw winking syndrome is due to ___ nerve synkinesis.",
    "Trigemino-oculomotor",
    ["Trigemino-facial", "Oculomotor-sympathetic", "Trigemino-abducens"],
    "Marcus Gunn jaw winking syndrome: d/t trigemino-oculomotor nerve synkinesis.",
    [13], "Marcus Gunn syndrome")
c.q(208, "scenario", "In Marcus Gunn jaw winking syndrome, what happens on opening the jaw?",
    "The lid moves up, while a closed jaw shows ptosis",
    ["The lid droops further, while a closed jaw shows retraction", "The lid closes completely", "The globe proptoses"],
    "Closed jaw -> ptosis; open jaw -> lid moves up.",
    [14], "Marcus Gunn syndrome")

covered = c.finish()
