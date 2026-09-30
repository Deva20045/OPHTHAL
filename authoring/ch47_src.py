from lib import Chapter

# Read directly from the printed pages; page citations follow the scan headers.
POINTS = {
220: [
 "Chapter title Ocular Trauma; mechanical trauma is classified as blunt or penetrating",
 "Blunt trauma includes closed-globe injuries and contusions",
 "Blunt trauma examples: fist, tennis ball and champagne cork",
 "Black eye is a periocular hematoma; subconjunctival hemorrhage is common in trivial trauma",
 "Hyphema is blood in anterior chamber and the most common sign of blunt ocular trauma",
 "Hyphema bleeding source is circulus arteriosus major; topical steroids prevent rebleeding/inflammation; atropine is optional",
 "Paracentesis/washing of anterior chamber is considered if hyphema does not resorb within 4 days",
 "Iridodonesis is tremulous iris; iridodialysis is iris-root detachment from ciliary body and gives D-shaped pupil",
 "Rosette-shaped cataract is posterior subcapsular; ectopia lentis/subluxation is most commonly due to blunt trauma",
 "Vossius ring is imprint of miotic pupil on anterior lens; phacodonesis is tremulous lens",
],
221: [
 "Fundus trauma: cherry-red macular spot; Berlin edema is fluid collection due to blunt trauma",
 "Commotio retinae gives cloudy grey appearance; traumatic optic neuropathy is self-limiting",
 "Choroidal rupture has bucket-handle configuration",
 "Globe rupture can follow fall on knob-like object; common site superonasal limbus near Schlemm canal",
 "Penetrating trauma may cause sympathetic ophthalmia (panuveitis) and intraocular foreign body",
 "Iron/steel are commonest IOFB; investigation of choice CT scan; MRI is contraindicated",
 "Iron deposition causes siderosis bulbi: rust ring on anterior lens capsule, iris hyperpigmentation and secondary open-angle glaucoma",
 "Prussian blue reaction stains iron deposits",
 "Ophthalmia nodosa: caterpillar-hair contact causes uveitis",
 "Blow-out fracture is floor fracture and most common orbital fracture in trauma",
 "Blow-out fracture findings: infraorbital nerve anaesthesia and restrictive diplopia from inferior oblique/inferior rectus entrapment; diplopia on upgaze and downgaze",
],
222: [
 "Orbital fracture X-ray: tear-drop sign",
 "Roof-of-orbit fracture presents with raccoon/panda eyes",
 "Chemical injury: alkali causes tissue necrosis and deeper penetration; acid causes coagulation and does not penetrate",
 "Dua and Roper-Hall classifications are used to grade ocular surface burns",
 "Chemical injury first aid: copious irrigation with balanced salt solution or Ringer lactate and double eversion of eyelids",
 "Chemical injury medical management: topical antibiotics, atropine for ciliary spasm, lubricating drops",
 "Topical sodium citrate prevents proteolysis in chemical injury",
],
}

c = Chapter(47, "Ocular Trauma", 220, 222, POINTS)

c.unit("Blunt ocular trauma", "Miscellaneous",
       "Blunt trauma causes closed-globe injury and contusion. Recognize hyphema, iris/lens signs and their named features; manage hyphema to prevent rebleeding and intervene for persistent blood.")
c.q(220, "match", "Mechanical ocular trauma is divided into blunt trauma and:", "Penetrating trauma",
    ["Thermal trauma", "Chemical trauma", "Radiation trauma"], "The mechanical-trauma diagram divides injury into blunt (closed-globe injuries/contusions) and penetrating trauma.", [1, 2], "Ocular trauma classification")
c.q(220, "recall", "Which is an example of blunt ocular trauma listed on the page?", "Tennis ball injury",
    ["Chemical splash", "Caterpillar hair", "Laser exposure"], "Blunt-trauma examples include injury by fist, tennis ball and champagne cork.", [3], "Blunt trauma")
c.q(220, "match", "Match the sign with its description — 1) Black eye  2) Subconjunctival hemorrhage … A) Periocular hematoma  B) Common in trivial trauma",
    "1-A, 2-B", ["1-B, 2-A", "1-A, 2-A", "1-B, 2-B"], "Black eye is periocular hematoma; subconjunctival hemorrhage is common in trivial trauma.", [4], "Blunt trauma signs")
c.q(220, "scenario", "The most common sign of blunt ocular trauma is blood in the anterior chamber, called:", "Hyphema",
    ["Hyposphagma", "Vitreous hemorrhage", "Hypopyon"], "Hyphema is a collection of blood in the anterior chamber and is listed as the most common sign of blunt ocular trauma.", [5], "Hyphema")
c.q(220, "recall", "The bleeding source in traumatic hyphema is the:", "Circulus arteriosus major",
    ["Central retinal artery", "Circle of Zinn-Haller", "Long posterior ciliary artery"], "The source of bleeding is given as the circulus arteriosus major.", [6], "Hyphema")
c.q(220, "management", "Which is the listed reason for topical steroids in hyphema, with atropine as an optional adjunct?", "To prevent rebleeding and associated inflammation",
    ["To dissolve the clot immediately", "To prevent lens subluxation", "To lower the risk of siderosis"], "Topical steroids are used to prevent rebleeding and associated inflammation; atropine is optional.", [6], "Hyphema management")
c.q(220, "numeric", "If hyphema has not resorbed by ___ days, anterior-chamber paracentesis/washing is considered.", "4",
    ["1", "2", "7"], "Paracentesis/washing is listed if there is no resorption until 4 days.", [7], "Hyphema management")
c.q(220, "match", "Match the iris injury — 1) Iridodonesis  2) Iridodialysis … A) Detachment of iris root from ciliary body  B) Tremulous iris",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Iridodonesis is tremulous iris; iridodialysis is detachment of the iris root from ciliary body and produces a D-shaped pupil.", [8], "Iris trauma")
c.q(220, "scenario", "A D-shaped pupil after blunt trauma points to:", "Iridodialysis",
    ["Iridodonesis", "Hyphema", "Vossius ring"], "Iridodialysis detaches the iris root from the ciliary body and is associated with a D-shaped pupil.", [8], "Iris trauma")
c.q(220, "match", "Which traumatic lens-sign set is correctly matched?", "Rosette cataract: posterior subcapsular; Vossius ring: miotic-pupil imprint on anterior lens",
    ["Rosette cataract: nuclear; Vossius ring: posterior lens imprint", "Rosette cataract: cortical; Vossius ring: iris-root tear", "Rosette cataract: anterior subcapsular; Vossius ring: vitreous pigment"], "Rosette-shaped cataract is posterior subcapsular; Vossius ring is the imprint of a miotic pupil on the anterior lens surface.", [9, 10], "Lens trauma")
c.q(220, "recall", "The most common cause of ectopia lentis/subluxation listed here is:", "Blunt trauma",
    ["Penetrating injury", "Chemical injury", "Caterpillar-hair exposure"], "Ectopia lentis or subluxation of the lens is most commonly caused by blunt trauma.", [9], "Lens trauma")
c.q(220, "fillup", "Phacodonesis refers to a ___ lens.", "Tremulous",
    ["Vascularised", "Opacified", "Dislocated posteriorly"], "Phacodonesis is a tremulous lens.", [10], "Lens trauma")

c.unit("Posterior-segment, penetrating and orbital trauma", "Miscellaneous",
       "Blunt trauma may produce retinal, choroidal or globe injury. Penetrating trauma raises concern for sympathetic ophthalmia and IOFB; iron IOFB causes siderosis. Blow-out and roof fractures have distinctive findings.")
c.q(221, "match", "Match the posterior-segment sign — 1) Berlin edema  2) Commotio retinae … A) Cloudy grey appearance  B) Fluid collection after blunt trauma",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Berlin edema is fluid collection due to blunt trauma; commotio retinae has a cloudy grey appearance.", [1, 2], "Fundus trauma")
c.q(221, "recall", "Traumatic optic neuropathy is described on this page as:", "Self-limiting",
    ["Progressive in every case", "Always bilateral", "Caused by iron deposition"], "The page characterizes traumatic optic neuropathy as self-limiting.", [2], "Fundus trauma")
c.q(221, "fillup", "A choroidal rupture may have a ___-handle configuration.", "Bucket",
    ["Swan-neck", "Keyhole", "Crescent"], "The listed configuration of choroidal rupture is bucket-handle.", [3], "Fundus trauma")
c.q(221, "scenario", "After falling on a knob-like object, globe rupture is suspected. The common site listed is the superonasal limbus near:", "Schlemm canal",
    ["Fovea", "Lacrimal punctum", "Optic disc"], "Globe rupture may follow a fall on a knob-like object; the listed site is superonasal limbus near Schlemm canal.", [4], "Globe rupture")
c.q(221, "recall", "Penetrating trauma may lead to sympathetic ophthalmia, a:", "Panuveitis",
    ["Anterior scleritis", "Isolated keratitis", "Optic neuropathy"], "Sympathetic ophthalmia (panuveitis) and intraocular foreign body are listed complications of penetrating trauma.", [5], "Penetrating trauma")
c.q(221, "match", "For suspected metallic intraocular foreign body, match investigation and contraindicated imaging — IOC: ___; contraindicated: ___.", "CT scan; MRI",
    ["MRI; CT scan", "B-scan; plain X-ray", "OCT; fluorescein angiography"], "Iron and steel are common IOFBs; CT is the investigation of choice and MRI is contraindicated.", [6], "Intraocular foreign body")
c.q(221, "match", "Iron deposition in the eye produces which named condition and associated findings?", "Siderosis bulbi with lens-capsule rust ring, iris hyperpigmentation and secondary open-angle glaucoma",
    ["Chalcosis with sunflower cataract and hypotony", "Sympathetic ophthalmia with heterochromia", "Ophthalmia nodosa with corneal ulcer"], "Siderosis bulbi follows iron deposition and may cause a rust ring on anterior lens capsule, iris hyperpigmentation and secondary open-angle glaucoma.", [7], "Siderosis bulbi")
c.q(221, "recall", "Which reaction is used to stain iron deposits in siderosis bulbi?", "Prussian blue reaction",
    ["Schirmer reaction", "Seidel test", "Jones dye test"], "The diagnostic Prussian blue reaction stains iron deposits.", [8], "Siderosis bulbi")
c.q(221, "scenario", "Uveitis after contact with caterpillar hair is called:", "Ophthalmia nodosa",
    ["Sympathetic ophthalmia", "Siderosis bulbi", "Berlin edema"], "Ophthalmia nodosa is associated with caterpillar-hair contact and uveitis.", [9], "Penetrating trauma")
c.q(221, "recall", "The most common orbital fracture in trauma is a blow-out fracture of the orbital:", "Floor",
    ["Roof", "Medial wall", "Lateral wall"], "A blow-out fracture involves the orbital floor and is the most common orbital fracture in trauma.", [10], "Orbital trauma")
c.q(221, "match", "Blow-out fracture with inferior oblique/inferior rectus entrapment causes restrictive diplopia on:", "Upgaze and downgaze",
    ["Horizontal gaze only", "Convergence only", "Lateral gaze only"], "Clinical findings include infraorbital nerve anaesthesia and restrictive diplopia; entrapped inferior oblique/inferior rectus cause diplopia in upgaze and downgaze.", [11], "Orbital trauma")
c.q(222, "recall", "The X-ray sign associated with orbital fracture is the:", "Tear-drop sign",
    ["Sunburst sign", "Crescent sign", "Thumbprint sign"], "The orbital-trauma investigation note labels the X-ray tear-drop sign.", [1], "Orbital fractures")
c.q(222, "scenario", "Raccoon or panda eyes after trauma suggest fracture of the orbital:", "Roof",
    ["Floor", "Medial wall", "Lateral wall"], "Fracture of the roof of the orbit presents with raccoon/panda eyes.", [2], "Orbital fractures")

c.unit("Chemical ocular injuries", "Miscellaneous",
       "Alkali burns penetrate deeply after liquefactive necrosis; acids cause coagulation and less penetration. Grade ocular-surface burns with Dua or Roper-Hall and begin immediate copious irrigation, followed by supportive and anti-proteolytic treatment.")
c.q(222, "match", "Match the chemical with its tissue effect — 1) Alkali  2) Acid … A) Coagulation, limited penetration  B) Necrosis, deeper penetration",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Alkali causes tissue necrosis and deeper penetration; acid causes coagulation and does not penetrate as deeply.", [3], "Chemical injury")
c.q(222, "recall", "Which two classifications are listed for grading ocular-surface burns?", "Dua and Roper-Hall",
    ["FISTO and SAFE", "Spaeth and Shaffer", "Cotswold and WHO"], "Dua and Roper-Hall classifications are listed for grading ocular surface burns.", [4], "Chemical injury")
c.q(222, "management", "The immediate first-aid management of chemical eye injury is:", "Copious irrigation with BSS/Ringer lactate, with double eversion of the eyelids",
    ["Topical steroids before irrigation", "Pressure patching without irrigation", "Immediate paracentesis"], "Management begins with copious irrigation using balanced salt solution or Ringer lactate and double eversion of eyelids.", [5], "Chemical injury")
c.q(222, "match", "Match the adjunct in chemical injury — 1) Atropine  2) Topical sodium citrate … A) Prevents proteolysis  B) Relieves ciliary spasm",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Listed treatment includes topical antibiotics, atropine for ciliary spasm, lubricants and topical sodium citrate to prevent proteolysis.", [6, 7], "Chemical injury")

covered = c.finish()
