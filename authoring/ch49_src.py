from lib import Chapter

POINTS = {
228: [
 "Chapter title Lasers in Ophthalmology; LASER expands to Light Amplification by Stimulated Emission of Radiation",
 "Laser tissue effects: photoablation burns/vaporizes tissue; photodisruption breaks tissue; photocoagulation coagulates tissue",
 "Photoablation mechanism: chemical effects break bonds and vaporize tissue; ultraviolet wavelength 150-300 nm",
 "Excimer argon-fluoride laser 193 nm; corneal refractive procedures include LASIK and PRK",
 "Photocoagulation mechanism: thermal effect denatures proteins; visible spectrum 400-580 nm",
 "Photocoagulation examples: argon green 514 nm, frequency-doubled Nd:YAG 532 nm, diode 810 nm (preferred in ROP), ruby red 694 nm",
 "Photocoagulation uses: panretinal photocoagulation for diabetic retinopathy and CRVO; trabeculoplasty for POAG",
 "Focal retinal photocoagulation uses: diabetic macular edema, CSR and ARMD",
 "Photodisruption mechanisms: electron stripping/ionization, plasma-like material breaks bonds, acoustic shock waves cause mechanical effect",
 "Photodisruption uses infrared invisible light; helium-neon red beam is used to view and aim",
 "Photodisruption examples: Nd:YAG 1064 nm and Nd:glass 1053 nm",
 "Nd:glass applications: FLACS for cataract surgery and SMILE for refractive-error correction",
 "Nd:YAG applications: posterior capsulotomy for PCO and peripheral iridotomy for angle closure glaucoma",
]
}

c = Chapter(49, "Lasers In Ophthalmology", 228, 228, POINTS)

c.unit("Laser principles and tissue effects", "Miscellaneous",
       "LASER means Light Amplification by Stimulated Emission of Radiation. Classify ocular laser effects as photoablation (burn/vaporize), photodisruption (break) or photocoagulation (coagulate), then connect mechanisms, wavelengths, devices and clinical uses.")
c.q(228, "fillup", "LASER stands for Light Amplification by Stimulated Emission of ___.", "Radiation",
    ["Reflection", "Refraction", "Resonance"], "The expansion given is Light Amplification by Stimulated Emission of Radiation.", [1], "Laser principles")
c.q(228, "match", "Match the laser effect with the tissue result — 1) Photoablation  2) Photodisruption  3) Photocoagulation … A) Coagulate  B) Break  C) Burn/vaporize",
    "1-C, 2-B, 3-A", ["1-A, 2-C, 3-B", "1-B, 2-A, 3-C", "1-C, 2-A, 3-B"], "The overview classifies photoablation as burning tissue, photodisruption as breaking tissue and photocoagulation as coagulating tissue.", [2], "Laser tissue effects")
c.q(228, "match", "Photoablation acts by breaking chemical bonds and vaporizing tissue; it uses which wavelength range?", "Ultraviolet, 150-300 nm",
    ["Visible, 400-580 nm", "Infrared, 800-1100 nm", "Radiofrequency, 1-10 cm"], "Photoablation produces chemical effects, breaks bonds and vaporizes tissue; the listed wavelength is ultraviolet 150-300 nm.", [3], "Photoablation")
c.q(228, "scenario", "Which laser and procedures are paired correctly for corneal refractive surgery?", "Argon-fluoride excimer, 193 nm; LASIK and PRK",
    ["Diode, 810 nm; posterior capsulotomy and iridotomy", "Nd:YAG, 1064 nm; LASIK and PRK", "Ruby, 694 nm; FLACS and SMILE"], "The excimer argon-fluoride laser is listed at 193 nm; photoablation applications include LASIK and PRK.", [4], "Photoablation")
c.q(228, "recall", "Photocoagulation produces a thermal effect that causes:", "Protein denaturation",
    ["Ionization by stripping electrons", "Vaporization by breaking chemical bonds", "Acoustic shock waves only"], "Photocoagulation's mechanism is thermal denaturation of proteins; its listed wavelength is visible spectrum 400-580 nm.", [5], "Photocoagulation")
c.q(228, "match", "Which list correctly matches photocoagulation laser with wavelength?", "Argon green 514 nm; frequency-doubled Nd:YAG 532 nm; diode 810 nm; ruby red 694 nm",
    ["Argon 193 nm; Nd:YAG 694 nm; diode 532 nm; ruby 810 nm", "Argon 1064 nm; Nd:YAG 810 nm; diode 694 nm; ruby 532 nm", "Argon 400 nm; Nd:YAG 580 nm; diode 193 nm; ruby 1053 nm"], "The photocoagulation examples are argon green 514 nm, frequency-doubled Nd:YAG 532 nm, diode 810 nm (preferred for ROP) and ruby red 694 nm.", [6], "Photocoagulation")
c.q(228, "match", "Panretinal photocoagulation is listed for diabetic retinopathy and CRVO; laser trabeculoplasty is used for:", "POAG",
    ["Angle-closure attack", "Retinoblastoma", "Corneal ulcer"], "Photocoagulation uses include PRP for diabetic retinopathy/CRVO and trabeculoplasty for POAG.", [7], "Photocoagulation uses")
c.q(228, "match", "Focal retinal photocoagulation is listed for diabetic macular edema, CSR and:", "ARMD",
    ["Retinitis pigmentosa", "Optic neuritis", "Keratoconus"], "Focal retinal laser uses listed are diabetic macular edema, CSR and ARMD.", [8], "Photocoagulation uses")
c.q(228, "match", "Which mechanisms occur in photodisruption?", "Ionization, plasma-mediated bond breakage and acoustic shock waves",
    ["Protein denaturation only", "Ultraviolet bond breaking followed by vaporization", "Selective photoreceptor bleaching only"], "Photodisruption combines electron stripping/ionization, plasma-like material that breaks bonds and acoustic shock waves producing mechanical effect.", [9], "Photodisruption")
c.q(228, "recall", "The invisible photodisruption beam is aimed using a visible ___ beam.", "Helium-neon red",
    ["Argon green", "Excimer ultraviolet", "Ruby infrared"], "Infrared photodisruption is invisible; a helium-neon red beam is used to view and aim.", [10], "Photodisruption")
c.q(228, "match", "Which photodisruption laser wavelengths are listed?", "Nd:YAG 1064 nm and Nd:glass 1053 nm",
    ["Excimer 193 nm and argon 514 nm", "Diode 810 nm and ruby 694 nm", "Nd:YAG 532 nm and Nd:glass 193 nm"], "The photodisruption table lists Nd:YAG 1064 nm and Nd:glass 1053 nm.", [11], "Photodisruption")
c.q(228, "match", "Nd:glass is listed for FLACS and:", "SMILE refractive-error correction",
    ["Posterior capsulotomy for PCO", "Peripheral iridotomy for angle closure", "Laser trabeculoplasty for POAG"], "Nd:glass uses include FLACS for cataract surgery and SMILE for refractive-error correction.", [12], "Photodisruption uses")
c.q(228, "management", "Nd:YAG photodisruption is used for posterior capsulotomy for PCO and peripheral iridotomy for:", "Angle-closure glaucoma",
    ["POAG", "CRVO", "Diabetic macular edema"], "Nd:YAG is listed for posterior capsulotomy in PCO and peripheral iridotomy in angle-closure glaucoma.", [13], "Photodisruption uses")

covered = c.finish()
