from lib import Chapter

POINTS = {
223: [
 "Chapter title Community Ophthalmology; NPCB started in 1976 and was amended to NPCBVI in 2017",
 "Clinical blindness: no perception of light",
 "NPCBVI (amended 2017) and WHO blindness: presenting VA <3/60 in better eye with best possible correction or visual field <10 degrees from fixation centre",
 "NPCBVI visual impairment table: blindness <3/60; severe VI <6/60 to 3/60; moderate VI <6/18 to 6/60; early VI <6/12 to 6/18, in better eye with available correction",
 "Functional low vision: VA <6/18 or field <10 degrees from fovea, with ability/potential to use vision for a task; BCVA/pinhole blindness <3/60 best corrected in better eye",
 "National blindness and visual impairment survey 2015-19 reported blindness prevalence 0.36% in 2019",
 "Program goal: reduce avoidable blindness prevalence (preventable + curable) to <0.25% by 2025",
],
224: [
 "Age >=50 blindness causes: cataract most common 66.2%; corneal opacity second 8.2%",
 "Age 0-49 blindness causes: corneal opacity most common 37.5%; amblyopia second 25%",
 "Age >=50 visual impairment: cataract most common 71.2%; refractive error second 13.4%",
 "Age 0-49 visual impairment: refractive error most common 29.6%; cataract second 25%",
 "Vision 2020 launched in 1999 in Geneva, Switzerland; adopted by India in 2001 at Goa",
 "Vision 2020 aims: reduce blind people to 25 million by 2020 and eliminate avoidable blindness",
 "Vision 2020 diseases in India: cataract, refractive errors, childhood blindness, endemic trachoma, glaucoma, diabetic retinopathy and corneal blindness",
 "Global Vision 2020 priorities: cataract, refractive errors, childhood blindness, endemic trachoma and onchocerciasis",
],
225: [
 "Vision 2020 apex (2; 1 per 500 million): RPCOS, AIIMS and Delhi",
 "Centre of excellence (20; 1 per 50 million): professional leadership, CME/research, standards/QA and strategy development",
 "Training centre (200; 1 per 5 million): ophthalmology department of medical college; tertiary retinal surgery, corneal transplantation, glaucoma surgery, training/CME",
 "Service centre (2000; 1 per 500,000): cataract and other common eye surgery, refraction, referral; ophthalmologist",
 "Vision centre (20,000; 1 per 50,000): refraction/glasses, primary eye care, school screening, screening/referral; paramedic ophthalmic assistant",
 "School screening target: classes V-VIII, age 10-14; one teacher per 150 students",
 "School screening uses vision screening cards and measurement tape, records VA; refer to nearest PHC if VA <6/9 in either eye",
],
226: [
 "Rashtriya Bal Swasthya Karyakram (RBSK) launched under National Health Mission; screening and early intervention from birth to 18 years",
 "RBSK 4 Ds: defects at birth, diseases, deficiencies and developmental delays",
 "Birth defects screened: neural tube defect, Down syndrome, cleft lip/palate, talipes, developmental dysplasia of hip, congenital cataract, congenital deafness, congenital heart disease, retinopathy of prematurity",
 "Deficiencies screened: severe anaemia, vitamin A deficiency/Bitot spot, vitamin D deficiency/rickets, severe acute malnutrition and goitre",
 "Childhood diseases screened: skin conditions (scabies/fungal infection/eczema), otitis media, rheumatic heart disease, reactive airway disease, dental caries and convulsive disorders",
 "Developmental delays screened: vision/hearing impairment, neuromotor, motor, cognitive and language delay, autism/behaviour disorder, learning disorder and ADHD",
 "Optional developmental-delay conditions: congenital hypothyroidism, sickle cell anaemia and beta thalassemia",
 "Tuberculosis and leprosy are included but are not specific to children",
],
227: [
 "RBSK newborns at public health facility/home: birth-6 weeks, estimated 2 crores, screened by mobile health team",
 "Preschool rural/urban-slum children: 6 weeks-6 years, estimated 8 crores, screened by Anganwadi and ANM workers",
 "School children in government/government-aided classes I-XII: 6-18 years, estimated 17 crores, school supported by district hospital, questionnaire screening",
 "RBSK intervention age 0-6 years: District Early Intervention Center (DEIC) and referral to appropriate tertiary centre",
 "RBSK intervention age 6-18 years: existing public health facility",
],
}

c = Chapter(48, "Community Ophthalmology", 223, 227, POINTS)

c.unit("NPCBVI definitions and blindness indicators", "Miscellaneous",
       "NPCB became NPCBVI in 2017. Distinguish clinical blindness from program/WHO definitions and the visual-impairment bands; learn survey prevalence and the avoidable-blindness target.")
c.q(223, "numeric", "The original National Programme for Control of Blindness (NPCB) began in ___; it became NPCBVI in 2017.", "1976",
    ["1956", "1986", "1999"], "NPCB started in 1976 and was amended to NPCBVI in 2017.", [1], "NPCBVI")
c.q(223, "recall", "Clinical blindness is defined as:", "No perception of light",
    ["Visual acuity below 6/18", "A visual field below 40 degrees", "Inability to read N6"], "The clinical definition given is no perception of light.", [2], "Blindness definitions")
c.q(223, "match", "Under NPCBVI/WHO, blindness is presenting VA below 3/60 in the better eye with best correction OR visual field below ___ degrees from fixation.", "10",
    ["5", "20", "30"], "The definition is presenting VA <3/60 in the better eye with best possible correction or visual-field limitation to <10° from fixation.", [3], "Blindness definitions")
c.q(223, "match", "Which ordered visual-acuity bands correctly describe severe, moderate and early visual impairment?", "SVI: <6/60–3/60; MVI: <6/18–6/60; EVI: <6/12–6/18",
    ["SVI: <6/12–6/18; MVI: <6/60–3/60; EVI: <6/18–6/60", "SVI: <6/18–6/60; MVI: <6/12–6/18; EVI: <6/60–3/60", "SVI: <3/60 only; MVI: <6/9–6/18; EVI: <6/60–3/60"], "NPCBVI categories in the better eye with available correction: blindness <3/60, severe VI <6/60–3/60, moderate VI <6/18–6/60, early VI <6/12–6/18.", [4], "Visual impairment")
c.q(223, "scenario", "A person has VA <6/18 or field <10° from the fovea and can potentially use vision to plan or execute a task. This meets the listed description of:", "Functional low vision",
    ["Clinical blindness", "Early visual impairment only", "Transient visual obscuration"], "Functional low vision is VA <6/18 or field <10° from fovea with ability/potential to use vision for a task; the table also defines BCVA/pinhole blindness as best-corrected <3/60.", [5], "Functional low vision")
c.q(223, "numeric", "The 2015-19 National Blindness and Visual Impairment Survey reported blindness prevalence of ___ in 2019.", "0.36%",
    ["0.05%", "1.2%", "3.6%"], "The recent-facts note gives blindness prevalence as 0.36% in 2019.", [6], "Blindness indicators")
c.q(223, "numeric", "The program goal is to reduce avoidable blindness prevalence to below ___ by 2025.", "0.25%",
    ["0.05%", "1%", "2.5%"], "The listed goal is <0.25% avoidable blindness by 2025.", [7], "Blindness indicators")

c.unit("Causes of blindness and Vision 2020", "Miscellaneous",
       "Know age-stratified blindness and visual-impairment causes, Vision 2020 dates and aims, and the differing India/global priority-disease lists.")
c.q(224, "match", "For blindness, which cause ranking is shown for age >=50 versus age 0-49?", ">=50: cataract then corneal opacity; 0-49: corneal opacity then amblyopia",
    [">=50: amblyopia then refractive error; 0-49: cataract then glaucoma", ">=50: glaucoma then cataract; 0-49: refractive error then trauma", ">=50: corneal opacity then cataract; 0-49: amblyopia then cataract"], "At >=50, cataract is most common (66.2%) and corneal opacity second (8.2%); at 0-49, corneal opacity is most common (37.5%) and amblyopia second (25%).", [1, 2], "Blindness causes")
c.q(224, "match", "Which visual-impairment cause ranking is correct for older versus younger age groups?", ">=50: cataract then refractive errors; 0-49: refractive errors then cataract",
    [">=50: refractive errors then cataract; 0-49: cataract then glaucoma", ">=50: corneal opacity then glaucoma; 0-49: amblyopia then cataract", ">=50: cataract then corneal opacity; 0-49: glaucoma then refractive errors"], "For visual impairment, >=50: cataract 71.2% then refractive error 13.4%; age 0-49: refractive error 29.6% then cataract 25%.", [3, 4], "Visual impairment causes")
c.q(224, "numeric", "Vision 2020 launched in Geneva in 1999 and was adopted by India in ___ at Goa.", "2001",
    ["1997", "2005", "2010"], "Vision 2020 launched in 1999 in Geneva and India adopted it in 2001 at Goa.", [5], "Vision 2020")
c.q(224, "recall", "One stated Vision 2020 aim was to reduce the number of blind people to ___ million by 2020.", "25",
    ["5", "10", "50"], "The stated aims were to reduce blind people to 25 million by 2020 and eliminate avoidable blindness.", [6], "Vision 2020")
c.q(224, "match", "Which condition appears among India's Vision 2020 priorities but not the listed global five?", "Glaucoma",
    ["Cataract", "Refractive errors", "Endemic trachoma"], "India's list includes cataract, refractive errors, childhood blindness, endemic trachoma, glaucoma, diabetic retinopathy and corneal blindness; global list includes the first four and onchocerciasis.", [7, 8], "Vision 2020")

c.unit("Vision 2020 service pyramid and school screening", "Miscellaneous",
       "The Vision 2020 pyramid scales apex, excellence, training, service and vision centres by population served, workforce and services. School screening targets class V-VIII and refers reduced acuity to PHC.")
c.q(225, "match", "Match Vision 2020 centre tier with approximate number — 1) Apex  2) Centre of excellence  3) Training centre  4) Service centre  5) Vision centre … A) 200  B) 20,000  C) 2  D) 2,000  E) 20",
    "1-C, 2-E, 3-A, 4-D, 5-B", ["1-E, 2-C, 3-D, 4-A, 5-B", "1-C, 2-A, 3-E, 4-B, 5-D", "1-B, 2-D, 3-A, 4-E, 5-C"], "The pyramid lists 2 apexes, one per 500 million population.", [1], "Vision 2020 service pyramid")
c.q(225, "match", "Professional leadership, CME/research, quality assurance and strategy development are functions of the:", "Centre of excellence",
    ["Vision centre", "Service centre", "Apex centre only"], "The centre of excellence is assigned leadership, CME/research, standards/QA and strategy development.", [2], "Vision 2020 service pyramid")
c.q(225, "match", "Which tier and service are paired correctly?", "Training centre: tertiary eye care and surgical training at a medical-college ophthalmology department",
    ["Vision centre: retinal surgery and corneal transplantation", "Service centre: school screening by a paramedic", "Apex: routine refraction and spectacles"], "Training centres are ophthalmology departments of medical colleges, providing tertiary eye care (retinal, corneal and glaucoma surgery) and training/CME.", [3], "Vision 2020 service pyramid")
c.q(225, "match", "A service centre is staffed by an ophthalmologist and provides common eye surgery, refraction and:", "Referral services",
    ["Only school screening", "National strategy development", "Retinal gene therapy"], "Service centres provide cataract/other common surgery, refraction and referral services; ratio 1 per 500,000.", [4], "Vision 2020 service pyramid")
c.q(225, "recall", "Vision centres provide primary eye care and school screening; the listed provider is a:", "Paramedic ophthalmic assistant",
    ["Retinal surgeon", "District ophthalmologist only", "Classroom teacher only"], "Vision centres provide refraction/glasses, primary eye care and screening/referral, performed by a paramedic ophthalmic assistant.", [5], "Vision 2020 service pyramid")
c.q(225, "match", "The school eye-screening programme targets children in classes ___, usually aged 10-14 years.", "V-VIII",
    ["I-II", "III-IV", "IX-XII"], "The target is classes V-VIII (10-14 years); one teacher screens about 150 students.", [6], "School screening")
c.q(225, "management", "A school-screening child has VA <6/9 in either eye. The listed next step is referral to the nearest:", "Primary health centre (PHC)",
    ["Apex centre directly", "Optical shop only", "District medical college without assessment"], "Vision screening cards and a measurement tape are used, VA is recorded and a child with VA <6/9 in either eye is referred to the nearest PHC.", [6, 7], "School screening")

c.unit("RBSK: aims, 4 Ds and screened conditions", "Miscellaneous",
       "RBSK under NHM provides screening/early intervention from birth to 18 years. Its 4 Ds organize birth defects, diseases, deficiencies and developmental delays; know the eye-relevant birth-defect and vision-impairment entries among the broader list.")
c.q(226, "recall", "Rashtriya Bal Swasthya Karyakram (RBSK) operates under the:", "National Health Mission",
    ["National AIDS Control Programme", "National Rural Livelihood Mission", "National Tobacco Control Programme"], "RBSK is launched under the National Health Mission and covers screening/early intervention from birth to 18 years.", [1], "RBSK")
c.q(226, "match", "The RBSK 4 Ds are defects at birth, diseases, deficiencies and:", "Developmental delays",
    ["Disability certificates", "Dental care", "Drug reactions"], "RBSK screens the 4 Ds: defects at birth, diseases, deficiencies and developmental delays.", [2], "RBSK")
c.q(226, "match", "Which set contains only listed congenital/birth defects screened under RBSK?", "Congenital cataract, retinopathy of prematurity, neural-tube defect and congenital heart disease",
    ["Age-related cataract, diabetic retinopathy, glaucoma and trachoma", "Dry eye, pterygium, keratoconus and uveitis", "Myopia, optic neuritis, AMD and retinal detachment"], "Birth defects include neural-tube defect, Down syndrome, cleft lip/palate, talipes, developmental dysplasia of hip, congenital cataract/deafness/heart disease and ROP.", [3], "RBSK screened conditions")
c.q(226, "match", "Which list is made up of RBSK deficiency conditions?", "Severe anaemia, vitamin A deficiency, vitamin D deficiency, severe acute malnutrition and goitre",
    ["Otitis media, dental caries, scabies and convulsions", "Autism, ADHD, language delay and hearing impairment", "Cleft palate, talipes, ROP and congenital cataract"], "Deficiencies include severe anaemia, vitamin A deficiency (Bitot spot), vitamin D deficiency (rickets), severe acute malnutrition and goitre.", [4], "RBSK screened conditions")
c.q(226, "match", "Which collection belongs to the childhood-disease group in RBSK?", "Skin conditions, otitis media, rheumatic heart disease, reactive airway disease, dental caries and convulsive disorders",
    ["Cleft lip, Down syndrome, talipes and ROP", "Anaemia, goitre, rickets and Bitot spots", "Autism, ADHD, hearing loss and motor delay"], "The childhood-disease list includes skin conditions (scabies/fungal infection/eczema), otitis media, rheumatic heart disease, reactive airway disease, dental caries and convulsive disorders.", [5], "RBSK screened conditions")
c.q(226, "match", "Which is listed under developmental delays, with congenital hypothyroidism/sickle cell/beta thalassemia marked optional?", "Vision impairment",
    ["Cleft palate", "Otitis media", "Severe acute malnutrition"], "Developmental delays include vision/hearing impairment, neuromotor/motor/cognitive/language delay, autism, learning disorder and ADHD; congenital hypothyroidism, sickle cell anaemia and beta thalassemia are optional.", [6, 7], "RBSK screened conditions")
c.q(226, "truefalse", "Tuberculosis and leprosy appear in the RBSK list but are noted as not specific to children.", "True",
    ["False", "Only tuberculosis is listed", "Only leprosy is listed"], "The page brackets tuberculosis and leprosy as conditions not specific to children.", [8], "RBSK screened conditions")

c.unit("RBSK screening pathways and intervention", "Miscellaneous",
       "RBSK groups screening by age and setting: newborns, preschool children and school children. Know coverage estimates, responsible screeners and the intervention destination for ages 0-6 versus 6-18.")
c.q(227, "match", "Match the RBSK screening category with age, approximate coverage and provider — newborns; preschool; school children.", "Birth-6 weeks / 2 crore / mobile team; 6 weeks-6 years / 8 crore / Anganwadi + ANM; 6-18 years / 17 crore / school-district hospital questionnaires",
    ["Birth-6 weeks / 17 crore / teacher; 6 weeks-6 years / 2 crore / mobile team; 6-18 / 8 crore / ANM", "Birth-6 years / 2 crore / district hospital; 6-18 / 8 crore / mobile team; preschool / 17 crore / teacher", "Birth-6 weeks / 8 crore / ANM; preschool / 17 crore / district hospital; school / 2 crore / mobile team"], "Newborns (birth-6 weeks): 2 crores, mobile health team; preschool (6 weeks-6 years): 8 crores, Anganwadi/ANM; school (6-18): 17 crores, district-hospital-supported school questionnaires.", [1, 2, 3], "RBSK screening")
c.q(227, "match", "For a child aged 0-6 years needing RBSK intervention, referral is through the:", "District Early Intervention Center (DEIC) to an appropriate tertiary centre",
    ["Vision centre only", "Existing public health facility only", "School questionnaire team"], "For ages 0-6, intervention is via DEIC with referral to an appropriate tertiary centre; for 6-18 years, use an existing public health facility.", [4, 5], "RBSK intervention")
c.q(227, "match", "RBSK intervention for ages 6-18 years is provided through an:", "Existing public health facility",
    ["DEIC exclusively", "Mobile team only", "Private tertiary hospital only"], "The listed route is DEIC/tertiary referral for ages 0-6 and existing public health facility for ages 6-18.", [5], "RBSK intervention")

covered = c.finish()
