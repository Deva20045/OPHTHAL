from lib import Chapter

POINTS = {
191: [
 "Chapter title INTERMEDIATE, POSTERIOR, PAN-UVEITIS AND MISCELLANEOUS DISORDERS; heading Intermediate Uveitis: also known as pars planitis",
 "Causes: 1. Idiopathic (m/c)",
 "Causes: 2. Associated with: Lyme's disease",
 "Associated with: sarcoidosis",
 "Associated with: multiple sclerosis",
 "Associated with: tuberculosis",
 "Clinical features - symptoms: B/L floaters",
 "Symptoms: blurring of vision",
 "Signs: spillover anterior uveitis",
 "Signs: snowballs: aggregation of cells in vitreous",
 "Treatment: steroids: posterior subtenon injection; if fails -> steroids: systemic",
 "If fails -> immunomodulatory drugs: azathioprine",
 "If fails -> pars plana vitrectomy + photocoagulation of snowbank",
 "Snowbanking: fibrovascular plaque",
 "Cystoid macular edema: m/c cause of vision loss",
 "Heading Posterior Uveitis/Chorioretinitis: inflammation of choroid & retina",
 "Clinical features: 1. Floaters; 2. Painless loss of vision; 3. Scotoma",
 "Clinical features: 4. Metamorphopsia: distortion of image",
 "Clinical features: 5. Photopsia",
],
192: [
 "Causes table (Infectious | Non-infectious) - Infectious 1. Most common: toxoplasmosis",
 "Toxoplasmosis a. Active: headlight in fog appearance (d/t associated active vitritis) (figure A, B)",
 "Toxoplasmosis b. Chronic: punched out scar (figure)",
 "Cats are definitive hosts",
 "Toxoplasmosis causes focal chorioretinitis",
 "2. Toxocariasis: unilateral LOV",
 "Toxocariasis: leukocoria (white pupillary reflex)",
 "3. CMV retinitis: m/c cause of LOV in ocular HIV",
 "CMV retinitis a. Pizza pie appearance",
 "CMV retinitis b. Scrambled egg & ketchup appearance (figure)",
 "CMV retinitis c. Brushfire extension (figure)",
 "4. TB",
 "Non-infectious 1. Sarcoidosis: candle wax dripping appearance (d/t perivascular inflammation & sheathing) (figures)",
 "Sarcoidosis: Lander's sign: pre-retinal nodules",
 "2. Behcet's disease",
 "3. Birdshot chorioretinopathy: HLA A29 association",
 "4. Serpiginous choroiditis: HLA B7 association",
 "Focal chorioretinitis: Toxoplasma, Toxocariasis, CMV",
 "Multifocal chorioretinitis: HSV, TB, syphilis",
],
193: [
 "Treatment: 1. Infectious cases: treat the cause + systemic steroids",
 "Treatment: 2. Non-infectious cases: systemic steroids OR",
 "Adalimumab (visual studies I to II)",
 "Sirolimus (Sakura program)",
 "Voclosporin (Luminate trials)",
 "Heading Pan-uveitis; Causes: 1. Vogt-Koyanagi-Harada (VKH) syndrome: affects eye, ears, skin, meninges",
 "VKH eye: B/L granulomatous panuveitis",
 "VKH eye: sunset glow fundus: RPE atrophy",
 "VKH eye: Suiguira sign: perilimbal vitiligo",
 "VKH eye: exudative RD",
 "VKH ears: tinnitus; skin: vitiligo; meninges: meningoencephalitis",
 "2. Sympathetic ophthalmitis: clinical feature: granulomatous panuveitis",
 "Sympathetic ophthalmitis cause: accidental penetrating trauma affecting ciliary body",
 "Pathogenesis: trauma to one eye (exciting eye) -> >2 weeks -> sympathetic ophthalmitis in other eye (sympathizing eye)",
 "Prevention: enucleation of traumatic eye in 14 days",
 "Treatment: steroids",
],
194: [
 "Heading Miscellaneous; table Enucleation | Evisceration | Exenteration; Terminology - enucleation: removal of whole eyeball + optic nerve",
 "Terminology - evisceration: removal of all layers of eyeball except sclera",
 "Terminology - exenteration: removal of eye and orbital contents",
 "Indications - enucleation: retinoblastoma; trauma",
 "Indications - evisceration: endophthalmitis",
 "Indications - exenteration: orbital mucormycosis; tumors metastasised to orbit",
 "C/I - enucleation: panophthalmitis",
 "C/I - evisceration: retinoblastoma",
 "C/I - exenteration: dash (-)",
 "Appearance row: photographs of the three procedures",
 "Gyrate atrophy: type of choroid atrophy",
 "Gyrate atrophy: autosomal recessive",
 "Gyrate atrophy: mutation in ornithine aminotransferase gene: increased levels of ornithine",
 "Gyrate atrophy treatment: arginine restriction in diet (ornithine is synthesised from arginine)",
],
}

c = Chapter(42, "Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders", 191, 194, POINTS)

# ---------------------------------------------------------------- p191
c.unit("Intermediate uveitis: causes and features", "Uvea",
       "Intermediate uveitis (pars planitis); idiopathic m/c; Lyme's, sarcoidosis, MS, TB; B/L floaters, blurring; spillover anterior uveitis; snowballs.")
c.q(191, "fillup", "Intermediate uveitis is also known as ___.",
    "Pars planitis",
    ["Retinochoroiditis", "Iridocyclitis", "Vitelliform uveitis"],
    "Intermediate Uveitis: Also known as pars planitis.",
    [1], "Intermediate uveitis")
c.q(191, "recall", "What is the most common cause of intermediate uveitis?",
    "Idiopathic",
    ["Lyme's disease", "Sarcoidosis", "Tuberculosis"],
    "Causes: 1. Idiopathic (m/c); 2. Associated with Lyme's disease, sarcoidosis, multiple sclerosis, tuberculosis.",
    [2], "Intermediate uveitis")
c.q(191, "oddoneout", "Intermediate uveitis is associated with all of the following EXCEPT:",
    "Vogt-Koyanagi-Harada syndrome",
    ["Lyme's disease", "Multiple sclerosis", "Tuberculosis"],
    "Associated with: Lyme's disease, sarcoidosis, multiple sclerosis, tuberculosis. (VKH syndrome is listed under pan-uveitis.)",
    [3, 4, 5, 6], "Intermediate uveitis")
c.q(191, "scenario", "A patient reports bilateral floaters and blurring of vision. Which uveitis does the book describe with these symptoms?",
    "Intermediate uveitis",
    ["Anterior uveitis", "Sympathetic ophthalmitis", "Vogt-Koyanagi-Harada syndrome"],
    "Intermediate uveitis symptoms: B/L floaters; blurring of vision.",
    [7, 8], "Intermediate uveitis")
c.q(191, "fillup", "In intermediate uveitis, the anterior segment shows ___ anterior uveitis.",
    "Spillover",
    ["Granulomatous", "Recurrent", "Hypopyon"],
    "Signs: Spillover anterior uveitis.",
    [9], "Intermediate uveitis")
c.q(191, "recall", "In intermediate uveitis, 'snowballs' are:",
    "Aggregations of cells in the vitreous",
    ["A fibrovascular plaque", "Pre-retinal nodules", "Perilimbal vitiligo"],
    "Snowballs: Aggregation of cells in vitreous.",
    [10], "Intermediate uveitis")

c.unit("Intermediate uveitis: treatment and complications", "Uvea",
       "Stepwise treatment: posterior subtenon steroid, systemic steroid, azathioprine, pars plana vitrectomy + photocoagulation of snowbank; snowbanking; CME.")
c.q(191, "management", "In intermediate uveitis, what is the first step of steroid treatment, and what is the next step if it fails?",
    "Posterior subtenon steroid injection; then systemic steroids",
    ["Systemic steroids; then posterior subtenon injection", "Posterior subtenon injection; then azathioprine", "Systemic steroids; then pars plana vitrectomy"],
    "Treatment: Steroids: posterior subtenon injection; if fails -> steroids: systemic.",
    [11], "Intermediate uveitis treatment")
c.q(191, "management", "Intermediate uveitis has failed posterior subtenon and systemic steroids. Which immunomodulatory drug is next?",
    "Azathioprine",
    ["Adalimumab", "Voclosporin", "Sirolimus"],
    "If fails -> immunomodulatory drugs: azathioprine.",
    [12], "Intermediate uveitis treatment")
c.q(191, "management", "If azathioprine also fails in intermediate uveitis, the book advises:",
    "Pars plana vitrectomy plus photocoagulation of the snowbank",
    ["Enucleation of the eye", "Repeat posterior subtenon steroid injection", "Arginine restriction in the diet"],
    "If fails -> Pars plana vitrectomy + Photocoagulation of snowbank.",
    [13], "Intermediate uveitis treatment")
c.q(191, "recall", "Snowbanking in intermediate uveitis is a:",
    "Fibrovascular plaque",
    ["Aggregation of cells in the vitreous", "Punched out scar", "Perivascular sheathing"],
    "Snowbanking: Fibrovascular plaque.",
    [14], "Intermediate uveitis complications")
c.q(191, "recall", "Which condition is the most common cause of vision loss in intermediate uveitis?",
    "Cystoid macular edema",
    ["Exudative retinal detachment", "Sunset glow fundus", "Leukocoria"],
    "Cystoid macular edema: m/c cause of vision loss.",
    [15], "Intermediate uveitis complications")

c.unit("Posterior uveitis: clinical features", "Uvea",
       "Posterior uveitis/chorioretinitis inflammation of choroid & retina; floaters, painless loss of vision, scotoma, metamorphopsia distortion of image, photopsia.")
c.q(191, "fillup", "Posterior uveitis (chorioretinitis) is inflammation of the choroid and ___.",
    "Retina",
    ["Iris", "Pars plicata", "Vitreous"],
    "Posterior Uveitis/Chorioretinitis: Inflammation of choroid & retina.",
    [16], "Posterior uveitis")
c.q(191, "oddoneout", "Which of the following is NOT among the listed clinical features of posterior uveitis?",
    "Severe pain with circumcorneal congestion",
    ["Floaters", "Painless loss of vision", "Scotoma"],
    "Clinical features: 1. Floaters 2. Painless loss of vision 3. Scotoma 4. Metamorphopsia 5. Photopsia.",
    [17], "Posterior uveitis")
c.q(191, "recall", "Metamorphopsia is distortion of image. Which feature is listed fifth after it?",
    "Photopsia",
    ["Scotoma", "Floaters", "Painless loss of vision"],
    "4. Metamorphopsia: Distortion of image. 5. Photopsia.",
    [18, 19], "Posterior uveitis")

# ---------------------------------------------------------------- p192
c.unit("Posterior uveitis: infectious causes", "Uvea",
       "Toxoplasmosis m/c headlight in fog punched out scar cats focal chorioretinitis; toxocariasis unilateral LOV leukocoria; CMV retinitis m/c in HIV pizza pie scrambled egg ketchup brushfire; TB.")
c.q(192, "recall", "What is the most common infectious cause of posterior uveitis in the table?",
    "Toxoplasmosis",
    ["Toxocariasis", "CMV retinitis", "Tuberculosis"],
    "Infectious: 1. Most common: Toxoplasmosis.",
    [1], "Infectious causes")
c.q(192, "match", "Match the stage of toxoplasmosis with its fundus appearance — 1) Active  2) Chronic  … A) Punched out scar  B) Headlight in fog appearance  C) Candle wax dripping appearance",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-C"],
    "Active: headlight in fog appearance (d/t associated active vitritis). Chronic: punched out scar.",
    [2, 3], "Infectious causes")
c.q(192, "scenario", "Cats are the definitive hosts for the organism that causes focal chorioretinitis. Which infection?",
    "Toxoplasmosis",
    ["Toxocariasis", "CMV retinitis", "Tuberculosis"],
    "Cats are definitive hosts. Toxoplasmosis causes focal chorioretinitis.",
    [4, 5], "Infectious causes")
c.q(192, "scenario", "A child has unilateral loss of vision with leukocoria (white pupillary reflex). Which infectious cause does the table list?",
    "Toxocariasis",
    ["Toxoplasmosis", "CMV retinitis", "Tuberculosis"],
    "2. Toxocariasis: Unilateral LOV; Leukocoria (white pupillary reflex).",
    [6, 7], "Infectious causes")
c.q(192, "recall", "Which infection is the most common cause of loss of vision in ocular HIV?",
    "CMV retinitis",
    ["Toxoplasmosis", "Toxocariasis", "Syphilis"],
    "3. CMV retinitis: m/c cause of LOV in ocular HIV.",
    [8], "Infectious causes")
c.q(192, "oddoneout", "Which appearance is NOT described for CMV retinitis?",
    "Candle wax dripping appearance",
    ["Pizza pie appearance", "Scrambled egg & ketchup appearance", "Brushfire extension"],
    "CMV retinitis: a. Pizza pie appearance; b. Scrambled egg & ketchup appearance; c. Brushfire extension. (Candle wax dripping is sarcoidosis.)",
    [9, 10, 11], "Infectious causes")
c.q(192, "recall", "Besides toxoplasmosis, toxocariasis and CMV retinitis, which is listed as an infectious cause?",
    "TB",
    ["Sarcoidosis", "Behcet's disease", "Birdshot chorioretinopathy"],
    "Infectious: 1. Toxoplasmosis 2. Toxocariasis 3. CMV retinitis 4. TB. Sarcoidosis, Behcet's and birdshot are non-infectious.",
    [12], "Infectious causes")

c.unit("Posterior uveitis: non-infectious causes and pattern", "Uvea",
       "Sarcoidosis candle wax dripping Lander's sign; Behcet's; birdshot HLA A29; serpiginous HLA B7; focal vs multifocal chorioretinitis.")
c.q(192, "scenario", "A fundus shows a candle wax dripping appearance. What is the cause of this appearance in sarcoidosis?",
    "Perivascular inflammation and sheathing",
    ["Active associated vitritis", "Loss of iris crypts", "Distortion of the image"],
    "Sarcoidosis: candle wax dripping appearance (d/t perivascular inflammation & sheathing).",
    [13], "Non-infectious causes")
c.q(192, "fillup", "In sarcoidosis, Lander's sign refers to ___.",
    "Pre-retinal nodules",
    ["Perilimbal vitiligo", "Bleeding on paracentesis", "Sunset glow fundus"],
    "Lander's sign: Pre-retinal nodules.",
    [14], "Non-infectious causes")
c.q(192, "recall", "Which of the following is listed under NON-infectious causes of posterior uveitis?",
    "Behcet's disease",
    ["Toxoplasmosis", "CMV retinitis", "Toxocariasis"],
    "Non-infectious: 1. Sarcoidosis 2. Behcet's disease 3. Birdshot chorioretinopathy 4. Serpiginous choroiditis.",
    [15], "Non-infectious causes")
c.q(192, "match", "Match the condition with its HLA association — 1) Birdshot chorioretinopathy  2) Serpiginous choroiditis  … A) HLA B7  B) HLA A29  C) HLA B27",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-C"],
    "Birdshot chorioretinopathy: HLA A29 association. Serpiginous choroiditis: HLA B7 association.",
    [16, 17], "Non-infectious causes")
c.q(192, "match", "Match the pattern with its causes — 1) Focal chorioretinitis  2) Multifocal chorioretinitis  … A) Toxoplasma, Toxocariasis, CMV  B) HSV, TB, syphilis  C) Toxoplasma, TB, syphilis",
    "1-A, 2-B",
    ["1-B, 2-A", "1-C, 2-B", "1-A, 2-C"],
    "Focal chorioretinitis: Toxoplasma, Toxocariasis, CMV. Multifocal chorioretinitis: HSV, TB, syphilis.",
    [18, 19], "Focal vs multifocal")

# ---------------------------------------------------------------- p193
c.unit("Posterior uveitis treatment and Vogt-Koyanagi-Harada syndrome", "Uvea",
       "Infectious: treat the cause + systemic steroids; non-infectious: systemic steroids or adalimumab (Visual), sirolimus (Sakura), voclosporin (Luminate); VKH eye ears skin meninges.")
c.q(193, "management", "Treatment of infectious posterior uveitis is:",
    "Treat the cause plus systemic steroids",
    ["Systemic steroids alone", "Adalimumab alone", "Posterior subtenon steroid alone"],
    "Treatment: 1. Infectious cases: Treat the cause + systemic steroids.",
    [1], "Posterior uveitis treatment")
c.q(193, "match", "For non-infectious posterior uveitis (alternative to systemic steroids), match the drug with its study — 1) Adalimumab  2) Sirolimus  3) Voclosporin  … A) Luminate trials  B) Visual studies I to II  C) Sakura program",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Non-infectious cases: systemic steroids OR adalimumab (visual studies I to II); sirolimus (Sakura program); voclosporin (Luminate trials).",
    [2, 3, 4, 5], "Posterior uveitis treatment")
c.q(193, "recall", "Vogt-Koyanagi-Harada (VKH) syndrome affects which four structures?",
    "Eye, ears, skin and meninges",
    ["Eye, ears, skin and joints", "Eye, ears, heart and meninges", "Eye, skin, meninges and parotid gland"],
    "VKH syndrome affects: Eye, Ears, Skin, Meninges.",
    [6], "Vogt-Koyanagi-Harada syndrome")
c.q(193, "fillup", "The ocular involvement in VKH is bilateral ___ panuveitis.",
    "Granulomatous",
    ["Non-granulomatous", "Hemorrhagic", "Suppurative"],
    "Eye: B/L granulomatous panuveitis.",
    [7], "Vogt-Koyanagi-Harada syndrome")
c.q(193, "recall", "'Sunset glow fundus' in VKH results from:",
    "RPE atrophy",
    ["Perivascular sheathing", "Loss of iris crypts", "Vitreous snowballs"],
    "Sunset glow fundus: RPE atrophy.",
    [8], "Vogt-Koyanagi-Harada syndrome")
c.q(193, "scenario", "A VKH patient shows perilimbal vitiligo. What is this sign called?",
    "Suiguira sign",
    ["Lander's sign", "Amsler's sign", "Arlt's sign"],
    "Suiguira sign: Perilimbal vitiligo.",
    [9], "Vogt-Koyanagi-Harada syndrome")
c.q(193, "scenario", "Which type of retinal detachment is listed in the eye findings of VKH?",
    "Exudative RD",
    ["Rhegmatogenous RD", "Tractional RD", "Total RD from a giant tear"],
    "VKH eye: Exudative RD.",
    [10], "Vogt-Koyanagi-Harada syndrome")
c.q(193, "match", "Match the VKH structure with its finding — 1) Ears  2) Skin  3) Meninges  … A) Vitiligo  B) Meningoencephalitis  C) Tinnitus",
    "1-C, 2-A, 3-B",
    ["1-A, 2-C, 3-B", "1-C, 2-B, 3-A", "1-B, 2-A, 3-C"],
    "Ears: tinnitus; skin: vitiligo; meninges: meningoencephalitis.",
    [11], "Vogt-Koyanagi-Harada syndrome")

c.unit("Sympathetic ophthalmitis", "Uvea",
       "Granulomatous panuveitis; accidental penetrating trauma to ciliary body; exciting eye, >2 weeks, sympathizing eye; enucleation within 14 days; steroids.")
c.q(193, "scenario", "A patient develops granulomatous panuveitis after accidental penetrating trauma affecting the ciliary body. Which condition?",
    "Sympathetic ophthalmitis",
    ["Vogt-Koyanagi-Harada syndrome", "Birdshot chorioretinopathy", "Intermediate uveitis"],
    "Sympathetic ophthalmitis: clinical feature granulomatous panuveitis; cause: accidental penetrating trauma affecting ciliary body.",
    [12, 13], "Sympathetic ophthalmitis")
c.q(193, "numeric", "After trauma to one eye (exciting eye), sympathetic ophthalmitis appears in the other (sympathizing) eye after more than:",
    "2 weeks",
    ["2 days", "14 weeks", "2 months"],
    "Pathogenesis: trauma to one eye (exciting eye) -> >2 weeks -> sympathetic ophthalmitis in other eye (sympathizing eye).",
    [14], "Sympathetic ophthalmitis")
c.q(193, "management", "To prevent sympathetic ophthalmitis, the traumatic eye should undergo enucleation within:",
    "14 days",
    ["2 days", "6 weeks", "3 months"],
    "Prevention: Enucleation of traumatic eye in 14 days.",
    [15], "Sympathetic ophthalmitis")
c.q(193, "management", "Once sympathetic ophthalmitis has developed, the treatment given in the book is:",
    "Steroids",
    ["Arginine restriction", "Pars plana vitrectomy", "Evisceration"],
    "Treatment: Steroids.",
    [16], "Sympathetic ophthalmitis")

# ---------------------------------------------------------------- p194
c.unit("Miscellaneous: enucleation, evisceration, exenteration", "Uvea",
       "Terminology, indications and contraindications of enucleation, evisceration and exenteration.")
c.q(194, "match", "Match the procedure with its terminology — 1) Enucleation  2) Evisceration  3) Exenteration  … A) Removal of eye and orbital contents  B) Removal of whole eyeball + optic nerve  C) Removal of all layers of eyeball except sclera",
    "1-B, 2-C, 3-A",
    ["1-C, 2-B, 3-A", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B"],
    "Enucleation: removal of whole eyeball + optic nerve. Evisceration: removal of all layers of eyeball except sclera. Exenteration: removal of eye and orbital contents.",
    [1, 2, 3], "Miscellaneous procedures")
c.q(194, "scenario", "Which indications does the table list for enucleation?",
    "Retinoblastoma and trauma",
    ["Endophthalmitis and trauma", "Orbital mucormycosis and retinoblastoma", "Panophthalmitis and endophthalmitis"],
    "Indications - enucleation: retinoblastoma; trauma.",
    [4], "Miscellaneous procedures")
c.q(194, "scenario", "Evisceration is indicated in:",
    "Endophthalmitis",
    ["Retinoblastoma", "Panophthalmitis", "Orbital mucormycosis"],
    "Indications - evisceration: endophthalmitis.",
    [5], "Miscellaneous procedures")
c.q(194, "management", "Exenteration is indicated in orbital mucormycosis and in:",
    "Tumors metastasised to the orbit",
    ["Trauma to the globe", "Endophthalmitis", "Retinoblastoma confined to the globe"],
    "Indications - exenteration: orbital mucormycosis; tumors metastasised to orbit.",
    [6], "Miscellaneous procedures")
c.q(194, "truefalse", "True or false — 'The table lists retinoblastoma as a contraindication for enucleation.' Choose the correct verdict:",
    "False - enucleation is contraindicated in panophthalmitis; retinoblastoma is the contraindication for evisceration",
    ["True - enucleation and evisceration are both contraindicated in retinoblastoma", "False - retinoblastoma is a contraindication for exenteration", "True - enucleation is contraindicated in retinoblastoma and panophthalmitis"],
    "C/I - enucleation: panophthalmitis; evisceration: retinoblastoma; exenteration: dash (-).",
    [7, 8, 9], "Miscellaneous procedures")
c.q(194, "recall", "The Appearance row of the table shows photographs of:",
    "Enucleation, evisceration and exenteration",
    ["Only enucleation and exenteration", "Gyrate atrophy fundus and evisceration", "Enucleation, evisceration and exenteration together with orbital mucormycosis"],
    "Appearance row: photographs under Enucleation, Evisceration and Exenteration.",
    [10], "Miscellaneous procedures")

c.unit("Gyrate atrophy", "Uvea",
       "Gyrate atrophy: choroid atrophy, autosomal recessive, ornithine aminotransferase gene, raised ornithine, arginine restriction.")
c.q(194, "fillup", "Gyrate atrophy is a type of ___ atrophy.",
    "Choroid",
    ["Optic nerve", "Iris", "Retinal pigment epithelium"],
    "Gyrate atrophy: Type of choroid atrophy.",
    [11], "Gyrate atrophy")
c.q(194, "recall", "What is the inheritance pattern of gyrate atrophy?",
    "Autosomal recessive",
    ["Autosomal dominant", "X-linked recessive", "Mitochondrial"],
    "Gyrate atrophy: Autosomal recessive.",
    [12], "Gyrate atrophy")
c.q(194, "scenario", "Gyrate atrophy results from mutation in which gene, and what happens to ornithine?",
    "Ornithine aminotransferase gene; ornithine levels rise",
    ["Ornithine aminotransferase gene; ornithine levels fall", "Arginase gene; ornithine levels rise", "Arginine synthetase gene; ornithine levels fall"],
    "Mutation in ornithine aminotransferase gene: increased levels of ornithine.",
    [13], "Gyrate atrophy")
c.q(194, "management", "Treatment of gyrate atrophy is restriction of which dietary component, since ornithine is synthesised from it?",
    "Arginine",
    ["Ornithine", "Lysine", "Glutamate"],
    "Treatment: Arginine restriction in diet (ornithine is synthesised from arginine).",
    [14], "Gyrate atrophy")

covered = c.finish()
