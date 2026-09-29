from lib import Chapter

POINTS = {
172: [
 "Chapter title SPECIAL INVESTIGATIONS FOR CORNEA; heading Keratometry; Principle: anterior surface of cornea acts as a convex mirror",
 "Size of image is proportional to 1/curvature",
 "Image seen as keratometric mires",
 "Photograph captions: Keratometer; Keratometric mires",
 "Correct positioning of mires: single, overlapped minus sign",
 "Correct positioning of mires: single, overlapped plus sign",
 "Uses 1: measure corneal curvature",
 "Uses 2: diagnose astigmatism - horizontally oval mires: with the rule astigmatism",
 "Uses 2: diagnose astigmatism - vertically oval mires: against the rule astigmatism",
 "Uses 3: to ascertain proper fitting of contact lens",
 "Uses 4: to diagnose keratoconus (pulsating mires seen)",
 "Figure captions: Good fit of lens; Steep fit of lens",
 "Heading: Pachymetry - measures corneal thickness",
 "Normal Corneal Thickness (CT): 0.5 to 0.6 mm (0.54 mm) or 540 micron",
 "CT is highest in the centre -> reduces towards periphery",
 "Pachymetry uses 1: eligibility for LASIK (continues on next page)",
],
173: [
 "LASIK: contraindicated (c/i) if CT < 450 micron",
 "Uses 2: IOP measurement: 1 mm Hg IOP = 10 micron of CT",
 "CT increased -> false high IOP; CT decreased -> false low IOP",
 "Figure caption: Pachymetry",
 "Heading: Corneal topography - examination of corneal surface; methods used",
 "Method 1: Placido disc (labels: viewing aperture with lens, reflection rings, handle)",
 "Figure caption: Reflection of placido disc: Normal",
 "Method 2: Orbscan - uses slit scan imaging principle",
 "Method 3: Pentacam measures: a. CT; b. corneal curvature; c. anterior segment imaging",
 "Pentacam measures: d. topographic elevation maps of anterior surface; e. topographic elevation maps of posterior surface",
 "Heading: Corneal vital staining - used to visualize and distinguish ulcer from surrounding healthy tissue",
 "Fluorescein dye: stains area of denuded epithelium (floor/base of ulcer)",
 "Fluorescein: visualized under cobalt blue light -> green fluorescence",
 "Ulcer diagram: stain in floor/base, margins",
],
174: [
 "Fluorescein other uses: Goldmann's applanation tonometry",
 "Fluorescein other uses: Jones' dye disappearance test (lacrimation assessment)",
 "Fluorescein other uses: Seidel's test (in penetrating trauma)",
 "Rose Bengal dye: stains devitalised/necrotic tissue (margins of ulcer)",
 "Rose Bengal disadvantage: can be toxic to healthy tissue",
 "Lissamine green dye: stains devitalised/damaged tissue",
 "Lissamine green advantage: non-toxic to healthy ocular tissue",
 "Lissamine green other uses: m/c used for diagnosis of dry eye by conjunctival staining",
 "Alcian blue dye: stains mucin deposits and filaments",
 "Photograph captions: Lissamine green dye; Rose bengal stain; Flourescein dye; Flourescein dye application",
 "Heading: Other corneal investigations - Confocal microscopy: non-invasive technique for in-vivo imaging of all layers of living cornea",
 "Corneal aesthesiometer: examines corneal sensations (figure caption: Corneal aesthesiometer)",
 "Instrument: pen-like instrument with filament (6 cm long)",
 "Length of filament eliciting corneal sensations proportional to corneal sensations proportional to 1/anaesthesia",
],
}

c = Chapter(38, "Special Investigations for Cornea", 172, 174, POINTS)

# ---------------------------------------------------------------- p172
c.unit("Keratometry", "Cornea",
       "Keratometry principle convex mirror image size 1/curvature mires; correct mire positioning; uses curvature astigmatism with/against the rule contact lens fitting keratoconus pulsating mires; good fit vs steep fit.")
c.q(172, "fillup", "The principle of keratometry is that the anterior surface of the cornea acts as a ___.",
    "Convex mirror",
    ["Concave mirror", "Plane mirror", "Converging lens"],
    "Keratometry principle: anterior surface of cornea acts as a convex mirror.",
    [1], "Keratometry")
c.q(172, "recall", "In keratometry, the size of the image is ___ the curvature, and the image is seen as ___.",
    "Inversely proportional to ; keratometric mires",
    ["Directly proportional to ; keratometric mires", "Inversely proportional to ; placido rings", "Directly proportional to ; placido rings"],
    "Size of image is proportional to 1/curvature; image seen as keratometric mires.",
    [2, 3], "Keratometry")
c.q(172, "recall", "The two photographs at the top right of the keratometry page are captioned:",
    "Keratometer and Keratometric mires",
    ["Keratometer and Reflection of placido disc", "Pachymetry and Keratometric mires", "Keratometric mires and Good fit of lens"],
    "Photograph captions: Keratometer; Keratometric mires.",
    [4], "Keratometry")
c.q(172, "recall", "In the diagram of correct positioning of mires, the mires must show which appearance?",
    "A single, overlapped plus sign and a single, overlapped minus sign",
    ["Two separate plus signs and a single minus sign", "A single plus sign with two separate minus signs", "Two separate plus signs and two separate minus signs"],
    "Correct positioning of mires: single, overlapped minus sign and single, overlapped plus sign.",
    [5, 6], "Keratometry")
c.q(172, "management", "Which corneal parameter is measured by keratometry, as the first use listed?",
    "Corneal curvature",
    ["Corneal thickness", "Corneal sensation", "Topographic elevation of the posterior surface"],
    "Uses of keratometry: 1. Measure corneal curvature.",
    [7], "Keratometry - uses")
c.q(172, "match", "Match the keratometric mire shape with the astigmatism it diagnoses — 1) Horizontally oval mires  2) Vertically oval mires  … A) Against the rule astigmatism  B) With the rule astigmatism",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "Horizontally oval mires: with the rule astigmatism. Vertically oval mires: against the rule astigmatism.",
    [8, 9], "Keratometry - uses")
c.q(172, "management", "For which purpose, other than measuring curvature and diagnosing astigmatism, is a keratometer used per the book?",
    "To ascertain proper fitting of contact lens",
    ["To measure corneal thickness", "To examine corneal sensations", "To visualise an ulcer against healthy tissue"],
    "Uses 3: To ascertain proper fitting of contact lens.",
    [10], "Keratometry - uses")
c.q(172, "scenario", "On keratometry the mires appear pulsating. Which corneal disorder does the book say this diagnoses?",
    "Keratoconus",
    ["With the rule astigmatism", "Against the rule astigmatism", "Steep fit of a contact lens"],
    "Uses 4: To diagnose keratoconus (pulsating mires seen).",
    [11], "Keratometry - uses")
c.q(172, "recall", "In the pair of mire pictures, the one with a distorted, wavy mire circle is captioned:",
    "Steep fit of lens",
    ["Good fit of lens", "Keratometric mires", "Reflection of placido disc: Normal"],
    "The two mire pictures are captioned Good fit of lens (regular circle) and Steep fit of lens (wavy circle).",
    [12], "Keratometry - uses")

c.unit("Pachymetry", "Cornea",
       "Pachymetry measures corneal thickness normal 0.5-0.6 mm 0.54 mm 540 micron highest centre; LASIK eligibility c/i CT <450 micron; IOP measurement 1 mmHg = 10 micron; false high/low IOP.")
c.q(172, "fillup", "Pachymetry measures corneal ___.",
    "Thickness",
    ["Curvature", "Sensation", "Surface elevation"],
    "Pachymetry: measures corneal thickness.",
    [13], "Pachymetry")
c.q(172, "numeric", "The normal corneal thickness (CT) in the book is:",
    "0.5 to 0.6 mm (0.54 mm or 540 micron)",
    ["0.4 to 0.45 mm (0.42 mm or 420 micron)", "0.7 to 0.8 mm (0.75 mm or 750 micron)", "0.3 to 0.4 mm (0.35 mm or 350 micron)"],
    "Normal Corneal Thickness (CT): 0.5 to 0.6 mm (0.54 mm) or 540 micron.",
    [14], "Pachymetry")
c.q(172, "truefalse", "True or false — 'Corneal thickness is highest at the periphery and reduces towards the centre.' Choose the correct verdict:",
    "False - CT is highest in the centre and reduces towards the periphery",
    ["True - CT is highest at the periphery", "False - CT is uniform across the cornea", "True - CT is lowest in the centre and highest at the limbus"],
    "CT is highest in the centre -> reduces towards periphery.",
    [15], "Pachymetry")
c.q(172, "scenario", "A patient is being assessed for eligibility for LASIK, and the surgeon needs to know the corneal thickness. Which investigation does the book list for this use?",
    "Pachymetry",
    ["Keratometry", "Pentacam elevation map alone", "Corneal aesthesiometer"],
    "Pachymetry uses: 1. Eligibility for LASIK.",
    [16], "Pachymetry")
c.q(173, "numeric", "LASIK is contraindicated if the corneal thickness is less than:",
    "450 micron",
    ["540 micron", "350 micron", "600 micron"],
    "Eligibility for LASIK: c/i if CT < 450 micron.",
    [1], "Pachymetry")
c.q(173, "numeric", "For IOP measurement, 1 mm Hg of IOP corresponds to how much corneal thickness?",
    "10 micron",
    ["1 micron", "100 micron", "50 micron"],
    "IOP measurement: 1 mm Hg IOP = 10 micron of CT.",
    [2], "Pachymetry")
c.q(173, "match", "Match the corneal thickness change with its effect on the measured IOP — 1) CT increased  2) CT decreased  … A) False low IOP  B) False high IOP",
    "1-B, 2-A",
    ["1-A, 2-B", "1-B, 2-B", "1-A, 2-A"],
    "CT up -> false high IOP; CT down -> false low IOP.",
    [3], "Pachymetry")
c.q(173, "recall", "The colour-coded corneal thickness map and section at the top right of p173 is captioned:",
    "Pachymetry",
    ["Corneal topography", "Keratometric mires", "Reflection of placido disc: Normal"],
    "Figure caption: Pachymetry.",
    [4], "Pachymetry")

# ---------------------------------------------------------------- p173 topography
c.unit("Corneal topography", "Cornea",
       "Corneal topography examination of corneal surface; placido disc labels normal reflection; Orbscan slit scan; Pentacam measures CT curvature anterior segment imaging elevation maps of anterior and posterior surfaces.")
c.q(173, "fillup", "Corneal topography is the examination of the corneal ___.",
    "Surface",
    ["Thickness", "Sensations", "Endothelial layer"],
    "Corneal topography: Examination of corneal surface.",
    [5], "Corneal topography")
c.q(173, "recall", "The placido disc figure is labelled with which structures?",
    "Viewing aperture with lens, reflection rings and handle",
    ["Viewing aperture with lens, keratometric mires and handle", "Slit beam, reflection rings and handle", "Viewing aperture with lens, reflection rings and filament"],
    "Placido disc labels: viewing apperture with lens, reflection rings, handle.",
    [6], "Corneal topography")
c.q(173, "recall", "In the figure 'Reflection of placido disc: Normal', the reflection on the cornea appears as:",
    "Regular concentric rings",
    ["Horizontally oval rings", "Vertically oval rings", "Pulsating rings"],
    "The normal reflection of the placido disc shows regular concentric rings.",
    [7], "Corneal topography")
c.q(173, "fillup", "Orbscan uses the ___ imaging principle.",
    "Slit scan",
    ["Placido reflection", "Confocal", "Fluorescein staining"],
    "Method 2: Orbscan: Uses slit scan imaging principle.",
    [8], "Corneal topography")
c.q(173, "oddoneout", "Pentacam measures all of the following EXCEPT:",
    "Corneal sensations",
    ["Corneal thickness (CT)", "Corneal curvature", "Anterior segment imaging"],
    "Pentacam measures CT, corneal curvature, anterior segment imaging and topographic elevation maps of both surfaces. Corneal sensations are examined by the corneal aesthesiometer (p174).",
    [9], "Corneal topography")
c.q(173, "recall", "Pentacam produces topographic elevation maps of which corneal surfaces?",
    "Both the anterior and the posterior surface",
    ["Anterior surface only", "Posterior surface only", "Anterior surface and limbal vessels"],
    "Pentacam: d. topographic elevation maps of anterior surface; e. topographic elevation maps of posterior surface.",
    [10], "Corneal topography")

# ---------------------------------------------------------------- vital staining
c.unit("Corneal vital staining", "Cornea",
       "Vital staining to distinguish ulcer from healthy tissue; fluorescein denuded epithelium floor/base cobalt blue green; uses Goldmann applanation Jones' dye Seidel's test; rose bengal; lissamine green dry eye; alcian blue mucin filaments.")
c.q(173, "recall", "What is corneal vital staining used for?",
    "To visualize and distinguish the ulcer from surrounding healthy tissue",
    ["To measure the depth of the anterior chamber", "To map the elevation of the posterior corneal surface", "To measure corneal sensations"],
    "Corneal vital staining: used to visualize and distinguish ulcer from surrounding healthy tissue.",
    [11], "Vital staining")
c.q(173, "scenario", "A corneal ulcer's floor/base shows staining because the epithelium is denuded. Which dye stains this area?",
    "Fluorescein dye",
    ["Rose Bengal dye", "Alcian blue dye", "Lissamine green dye"],
    "Fluorescein dye: stains area of denuded epithelium (floor/base of ulcer).",
    [12], "Vital staining - fluorescein")
c.q(173, "fillup", "Fluorescein is visualized under ___ light, which gives ___ fluorescence.",
    "Cobalt blue ; green",
    ["Cobalt blue ; red", "Red-free ; green", "White ; yellow"],
    "Visualized under cobalt blue light -> Green fluorescence.",
    [13], "Vital staining - fluorescein")
c.q(173, "recall", "The ulcer diagram beside fluorescein dye shows the stain in which sites?",
    "Floor/base and margins",
    ["Floor/base only", "Margins only", "Epithelium and endothelium"],
    "Diagram: Stain in -> Floor/base, Margins.",
    [14], "Vital staining - fluorescein")
c.q(174, "fillup", "Besides staining ulcers, fluorescein is used in ___ applanation tonometry.",
    "Goldmann's",
    ["Schiotz", "Perkins", "Non-contact"],
    "Other uses (of fluorescein): Goldmann's applanation tonometry.",
    [1], "Vital staining - fluorescein")
c.q(174, "match", "Match the fluorescein test with its use — 1) Jones' dye disappearance test  2) Seidel's test  … A) Penetrating trauma  B) Lacrimation assessment  C) Dry eye by conjunctival staining",
    "1-B, 2-A",
    ["1-A, 2-B", "1-C, 2-A", "1-B, 2-C"],
    "Jones' dye disappearance test: lacrimation assessment. Seidel's test (in penetrating trauma).",
    [2, 3], "Vital staining - fluorescein")
c.q(174, "scenario", "Which dye stains devitalised/necrotic tissue at the margins of an ulcer?",
    "Rose Bengal dye",
    ["Fluorescein dye", "Alcian blue dye", "Trypan blue dye"],
    "Rose Bengal dye: stains devitalised/necrotic tissue (margins of ulcer).",
    [4], "Vital staining - rose bengal")
c.q(174, "fillup", "The disadvantage of Rose Bengal dye is that it can be ___ to healthy tissue.",
    "Toxic",
    ["Non-toxic", "Fluorescent", "Sterilising"],
    "Disadvantage: can be toxic to healthy tissue.",
    [5], "Vital staining - rose bengal")
c.q(174, "recall", "Lissamine green stains devitalised/damaged tissue and, unlike Rose Bengal, is ___ to healthy ocular tissue.",
    "Non-toxic",
    ["Toxic", "Fluorescent under cobalt blue light", "Restricted to ulcer margins only"],
    "Lissamine green dye: stains devitalised/damaged tissue. Advantage: non-toxic to healthy ocular tissue.",
    [6, 7], "Vital staining - lissamine green")
c.q(174, "management", "Which dye is most commonly used for the diagnosis of dry eye by conjunctival staining?",
    "Lissamine green dye",
    ["Fluorescein dye", "Rose Bengal dye", "Alcian blue dye"],
    "Lissamine green - other uses: m/c used for diagnosis of dry eye by conjunctival staining.",
    [8], "Vital staining - lissamine green")
c.q(174, "recall", "Alcian blue dye stains:",
    "Mucin deposits and filaments",
    ["Denuded epithelium of the ulcer floor", "Devitalised tissue at ulcer margins", "Aqueous leakage in penetrating trauma"],
    "Alcian blue dye: stains mucin deposits and filaments.",
    [9], "Vital staining - alcian blue")
c.q(174, "recall", "The three eye photographs on p174 (left to right) are captioned:",
    "Lissamine green dye, Rose bengal stain and Flourescein dye",
    ["Rose bengal stain, Lissamine green dye and Flourescein dye", "Flourescein dye, Rose bengal stain and Lissamine green dye", "Lissamine green dye, Flourescein dye and Rose bengal stain"],
    "Captions: Lissamine green dye, Rose bengal stain, Flourescein dye (plus 'Flourescein dye application' beside the fluorescein section).",
    [10], "Vital staining - figures")

c.unit("Other corneal investigations", "Cornea",
       "Confocal microscopy non-invasive in-vivo imaging all layers; corneal aesthesiometer pen-like 6 cm filament; filament length corneal sensations 1/anaesthesia.")
c.q(174, "recall", "Which technique is a non-invasive method for in-vivo imaging of all layers of the living cornea?",
    "Confocal microscopy",
    ["Orbscan", "Pachymetry", "Keratometry"],
    "Confocal microscopy: non-invasive technique for in-vivo imaging of all layers of living cornea.",
    [11], "Other investigations")
c.q(174, "scenario", "A clinician wants to examine corneal sensations using the pen-like instrument beside the nose diagram. What is it called?",
    "Corneal aesthesiometer",
    ["Keratometer", "Pachymeter", "Placido disc"],
    "Corneal aesthesiometer: examines corneal sensations.",
    [12], "Other investigations")
c.q(174, "numeric", "The corneal aesthesiometer is a pen-like instrument with a filament of what length?",
    "6 cm",
    ["6 mm", "16 cm", "60 cm"],
    "Instrument: pen-like instrument with filament (6 cm long).",
    [13], "Other investigations")
c.q(174, "recall", "As written in the book, the length of filament eliciting corneal sensations is proportional to corneal sensations, which are ___ anaesthesia.",
    "Inversely proportional to",
    ["Directly proportional to", "Independent of", "Equal to"],
    "Length of filament eliciting corneal sensations is proportional to corneal sensations, which are proportional to 1/anaesthesia.",
    [14], "Other investigations")

covered = c.finish()
