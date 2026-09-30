from lib import Chapter

# The uploaded Part 2 scan ends at the leaf printed p230; page numbers are verified from headers.
POINTS = {
229: [
 "Chapter title Physiology of Vision; rhodopsin is the visual pigment",
 "Rhodopsin components: opsin/scotopsin, a GPCR enabling signalling, and 11-cis retinal, light-sensitive chromophore",
 "Light absorption converts 11-cis retinal to the more stable 11-trans retinal isomer",
 "Visual cycle occurs in rod photoreceptors; RBP is retinol-binding protein carrying retinol in blood; IRBP is intraretinal binding protein",
 "Retinol/RBP supplies vitamin-A-derived 11-cis retinol/11-cis retinal; all-trans retinal is recycled through all-trans retinol and retinyl esters",
 "Visual-pigment regeneration depends on RPE-65 gene; 11-cis retinal recombines with opsin to form rhodopsin",
 "Light-activated rhodopsin forms metarhodopsin II, an unstable phototransduction enzyme acting in milliseconds",
],
230: [
 "Phototransduction: metarhodopsin II activates transducin by GDP-to-GTP exchange",
 "Transducin activates phosphodiesterase (PDE), which hydrolyses cGMP to 5-prime GMP",
 "Falling cGMP closes Na+ channels, stops Na+ influx and stops glutamate efflux",
 "Photoreceptor hyperpolarisation is a graded local potential, not an action potential, and travels by electronic conduction",
 "Signal reaches bipolar cells then ganglion cells; ganglion cells are the site of action potentials",
 "Visual pathway reaches lateral geniculate body (LGB), which has six layers",
 "LGB layers 1 and 2: magnocellular pathway for motion and black-and-white vision",
 "LGB layers 3 to 6: parvocellular pathway for fine details and colour vision",
 "In light, photoreceptors hyperpolarise; in darkness, they remain depolarised",
 "RPE-65 gene mutation prevents 11-cis retinal chromophore regeneration and causes retinitis pigmentosa and Leber congenital amaurosis",
]
}

c = Chapter(50, "Physiology of Vision", 229, 230, POINTS)

c.unit("Rhodopsin and visual cycle", "Miscellaneous",
       "Rhodopsin consists of opsin (a GPCR) and 11-cis retinal chromophore. Light isomerizes retinal; the rod visual cycle recycles vitamin-A-derived retinoids across photoreceptor and RPE, with RPE-65 required for regeneration.")
c.q(229, "recall", "The visual pigment in rods is:", "Rhodopsin",
    ["Photopsin", "Melanopsin", "Iodopsin"], "The page identifies rhodopsin as the visual pigment.", [1], "Visual pigment")
c.q(229, "match", "Match rhodopsin's components with their roles — 1) Opsin/scotopsin  2) 11-cis retinal … A) Light-sensitive chromophore  B) GPCR that enables signalling",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "Opsin/scotopsin is a GPCR enabling signalling; 11-cis retinal is the light-sensitive chromophore.", [2], "Visual pigment")
c.q(229, "fillup", "After absorbing light, 11-cis retinal isomerizes to the more stable ___ retinal.", "11-trans",
    ["9-cis", "13-cis", "all-trans retinol"], "Light absorption converts 11-cis retinal to the more stable 11-trans retinal isomer.", [3], "Visual pigment")
c.q(229, "recall", "The visual cycle shown occurs in rod photoreceptors; RBP transports retinol in blood and IRBP means:", "Intraretinal binding protein",
    ["Inter-receptor bipolar protein", "Intra-retinal bicarbonate pump", "Iridocorneal binding protein"], "The site is rod photoreceptors; RBP is retinol-binding protein and IRBP is intraretinal binding protein.", [4], "Visual cycle")
c.q(229, "match", "Which sequence best describes retinoid recycling in the visual cycle?", "11-cis retinoid forms rhodopsin; light produces all-trans retinal, which is recycled via retinol/retinyl esters to 11-cis retinal",
    ["All-trans retinal forms rhodopsin directly; light converts it to vitamin D", "11-cis retinal is irreversibly degraded and replaced by melanin", "Opsin converts retinyl esters directly into cGMP"], "Vitamin-A-derived retinoids are carried by RBP/IRBP; all-trans retinal is recycled through retinol and retinyl esters, with RPE-linked regeneration of 11-cis retinoid.", [4, 5, 6], "Visual cycle")
c.q(229, "scenario", "A mutation in the RPE-65 gene disrupts visual-pigment regeneration. The chromophore that cannot be regenerated is:", "11-cis retinal",
    ["All-trans retinyl ester", "5-prime GMP", "Metarhodopsin II"], "RPE-65-dependent regeneration produces 11-cis retinal, which recombines with opsin to form rhodopsin.", [6], "Visual cycle")
c.q(229, "recall", "The unstable light-activated intermediate that acts as an enzyme in phototransduction for milliseconds is:", "Metarhodopsin II",
    ["Scotopsin", "11-cis retinol", "Transducin GDP"], "Metarhodopsin II is an unstable intermediate, acts within milliseconds and functions as an enzyme for phototransduction.", [7], "Visual cycle")

c.unit("Phototransduction cascade", "Miscellaneous",
       "Metarhodopsin II activates transducin and PDE, reducing cGMP. Na+ channels close, glutamate release stops and the photoreceptor hyperpolarises; graded signals reach bipolar cells and then ganglion-cell action potentials.")
c.q(230, "match", "Order the early phototransduction cascade.", "Metarhodopsin II → transducin (GDP-GTP exchange) → PDE activation",
    ["PDE → rhodopsin → transducin hydrolysis", "Transducin → cGMP synthesis → metarhodopsin II", "Opsin → Na+ influx → PDE inhibition"], "Metarhodopsin II activates transducin by GDP-to-GTP exchange; transducin activates phosphodiesterase.", [1, 2], "Phototransduction")
c.q(230, "fillup", "PDE hydrolyses cGMP to 5-prime ___.", "GMP",
    ["ATP", "AMP", "GDP"], "Activated PDE hydrolyses cGMP to 5-prime GMP.", [2], "Phototransduction")
c.q(230, "match", "When cGMP concentration falls, which photoreceptor changes occur?", "Na+ channels close, Na+ influx stops and glutamate efflux stops",
    ["Na+ channels open, Na+ influx rises and glutamate release rises", "Ca2+ channels open and action potentials begin in rods", "Chloride channels close while glutamate efflux increases"], "Reduced cGMP closes Na+ channels, stopping Na+ influx and glutamate efflux.", [3], "Phototransduction")
c.q(230, "truefalse", "The light response in a photoreceptor is a graded hyperpolarising local potential, not an action potential.", "True",
    ["False", "It is an all-or-none rod action potential", "It is a graded depolarising potential"], "Photoreceptor hyperpolarisation is graded, is not an action potential and is transmitted by electronic conduction.", [4, 9], "Photoreceptor response")
c.q(230, "recall", "The phototransduction signal passes first to bipolar cells and then to ganglion cells, where:", "Action potentials are generated",
    ["Rhodopsin is regenerated", "cGMP is synthesised", "The tear film is secreted"], "The signal reaches bipolar cells, then ganglion cells; ganglion cells are the site of action potentials.", [5], "Retinal signal transmission")

c.unit("Lateral geniculate pathways and light/dark response", "Miscellaneous",
       "The ganglion-cell visual signal reaches the six-layer LGB. Layers 1-2 are magnocellular (motion, black-and-white); layers 3-6 are parvocellular (fine detail, colour). Light hyperpolarises photoreceptors; darkness depolarises them.")
c.q(230, "recall", "The visual pathway reaches the lateral geniculate body, which has ___ layers.", "Six",
    ["Two", "Four", "Eight"], "The LGB is shown with six layers.", [6], "Lateral geniculate body")
c.q(230, "match", "Match LGB layers and pathway — 1) Layers 1-2  2) Layers 3-6 … A) Parvocellular: fine details and colour  B) Magnocellular: motion and black-and-white",
    "1-B, 2-A", ["1-A, 2-B", "1-A, 2-A", "1-B, 2-B"], "LGB layers 1-2 are magnocellular for motion/black-and-white; layers 3-6 are parvocellular for fine detail/colour.", [7, 8], "Lateral geniculate pathways")
c.q(230, "scenario", "A photoreceptor exposed to light becomes hyperpolarised; in darkness it is:", "Depolarised",
    ["Also hyperpolarised", "At resting potential with an action potential", "Unable to release neurotransmitter under either condition"], "The page contrasts hyperpolarisation under light with a depolarising state under dark.", [9], "Photoreceptor response")
c.q(230, "match", "RPE-65 mutation prevents regeneration of 11-cis retinal and is linked to:", "Retinitis pigmentosa and Leber congenital amaurosis",
    ["Retinoblastoma and Coats disease", "Cataract and keratoconus", "Glaucoma and optic neuritis"], "The diagram links RPE-65 gene mutation and lack of 11-cis retinal regeneration with retinitis pigmentosa and Leber congenital amaurosis.", [10], "Visual-cycle disorders")

covered = c.finish()
