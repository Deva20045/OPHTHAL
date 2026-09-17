# PULSE Ophthalmology — Build Progress (single source of truth)

## Goal
A learner should **not need to read the PDF separately** after solving the questions.
Every line, table, diagram, flowchart, classification, value and exception of the book
scope (Book p1–233) is converted into questions in strict book order.

## Book & page map
- Book: **Ophthalmology, Marrow Edition 8** (scan footer: "Ophthalmology · v1.0 ·
  Marrow 8.0 · 2024") — scans cover **Book pages 1–233** (236 PDF pages in 2 files).
- The scans have **no text layer**; content is read from rendered page images
  (zoom into any unclear spot; never guess), with the book's printed page number
  in the header used as the citation anchor.
- Offsets (book page = PDF page + K):

| Part file (in `uploads/`) | PDF pages | K | Book pages |
|---|---|---|---|
| `Ophthalmology_Part1_pages_1-116.pdf` | 1–119 | −3 | 1–116 |
| `Ophthalmology_Part2_pages_117-233.pdf` | 1–117 | +116 | 117–233 |

- First 3 PDF pages of Part 1 = the book's Contents pages (not content scope).
- Formula: **Book page = PDF page + K** (K per part above).
  Part 1: PDF p4 = Book p1 … PDF p119 = Book p116.
  Part 2: PDF p1 = Book p117 … PDF p117 = Book p233.
- Final content page = Book p233 (Miscellaneous — Physiology of Vision).

## Roadmap — all 50 chapters listed from day one (status: LIVE / SOON)
| # | Chapter | Book start | Status |
|---|---|---|---|
| 1 | Layers and Structure of Eyeball | p1 | **LIVE** |
| 2 | Anatomy of cornea, Anatomy of Sclera and its Pathologies | p3 | SOON |
| 3 | Anatomy of Uvea, Accomodation with its Anomalies | p8 | SOON |
| 4 | Anatomy of Retina | p13 | SOON |
| 5 | Ocular Routes of Drug Administration, Blood Supply of Eye and Embryology of Eye | p14 | SOON |
| 6 | Visual Pathway and Visual Field Defects | p21 | SOON |
| 7 | Pupillary Reflexes, Light Reflex and its Lesions | p26 | SOON |
| 8 | Optic Atrophy: Optic Neuritis, Optic Neuropathies and Papilledema | p32 | SOON |
| 9 | Congenital Anomalies of Optic Disc and Colour Blindness | p40 | SOON |
| 10 | Squint : Extraocular Muscles and Binocular Single Vision | p43 | SOON |
| 11 | Squint : Classifications and Directions | p46 | SOON |
| 12 | Squint : Investigations | p48 | SOON |
| 13 | Paralytic Squint | p54 | SOON |
| 14 | Gaze Defects | p59 | SOON |
| 15 | Restrictive Squint and Comitant Squint | p63 | SOON |
| 16 | Pseudo-strabismus and Ocular Myopathies | p66 | SOON |
| 17 | Anatomy and Metabolism (Lens) | p68 | SOON |
| 18 | Acquired Cataract : Types | p73 | SOON |
| 19 | Acquired Cataract : Senile Cataract | p76 | SOON |
| 20 | Cataract Surgery | p80 | SOON |
| 21 | Complications of Cataract Surgery | p83 | SOON |
| 22 | Congenital Cataract, Ectopia lentis and Miscellaneous | p87 | SOON |
| 23 | Glaucoma : What and How? | p90 | SOON |
| 24 | Investigations for Glaucoma | p94 | SOON |
| 25 | Primary open angle glaucoma | p102 | SOON |
| 26 | Primary Angle Closure Glaucoma | p109 | SOON |
| 27 | Secondary Glaucoma(s) and Congenital Glaucoma | p113 | SOON |
| 28 | Tests for Vision and Normal Optics of Eyes | p117 | SOON |
| 29 | Myopia and Hypermetropia | p122 | SOON |
| 30 | Astigmatism, Reading of Spectacle Prescription and Binocular Errors | p130 | SOON |
| 31 | Refraction : How to prescribe glasses and Aphakia | p135 | SOON |
| 32 | Anatomy and Investigations of Retina | p142 | SOON |
| 33 | Retinoblastoma and Macular Disorders | p148 | SOON |
| 34 | Dystrophies of Fundus : Retinitis Pigmentosa and others | p156 | SOON |
| 35 | Retinal Vascular Disorders : Part 1 | p160 | SOON |
| 36 | Retinal Vascular Disorders : Part 2 | p164 | SOON |
| 37 | Retinal Detachment | p169 | SOON |
| 38 | Special Investigations for Cornea | p172 | SOON |
| 39 | Corneal Ulcer and Keratitis | p175 | SOON |
| 40 | Corneal Dystrophies, Keratoconus and Miscellaneous Disorders | p180 | SOON |
| 41 | Anterior Uveitis | p185 | SOON |
| 42 | Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders | p191 | SOON |
| 43 | Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium | p195 | SOON |
| 44 | Eyelids : Anatomy and Pathologies | p206 | SOON |
| 45 | Anatomy of Orbit and Proptosis | p209 | SOON |
| 46 | Lacrimal apparatus : Anatomy, Watering eye and Dry eye | p215 | SOON |
| 47 | Ocular Trauma | p220 | SOON |
| 48 | Community Ophthalmology | p223 | SOON |
| 49 | Lasers In Ophthalmology | p228 | SOON |
| 50 | Physiology of Vision | p229 | SOON |

*(Status column: Ch 1 = **LIVE**; every other chapter = **SOON** — rendered in the app
as a locked "Soon" row. Update this table as chapters go live.)*

### Section spans
- **Basic Anatomy of Eye** — Ch 1–5 (p1→p14)
- **Neuro-Ophthalmology** — Ch 6–9 (p21→p40)
- **Squint** — Ch 10–16 (p43→p66)
- **Lens** — Ch 17–22 (p68→p87)
- **Glaucoma** — Ch 23–27 (p90→p113)
- **Optics** — Ch 28–31 (p117→p135)
- **Retina** — Ch 32–37 (p142→p169)
- **Cornea** — Ch 38–40 (p172→p180)
- **Uvea** — Ch 41–42 (p185→p191)
- **Conjunctiva** — Ch 43 (p195)
- **Adnexa** — Ch 44–46 (p206→p215)
- **Miscellaneous** — Ch 47–50 (p220→p229)

## Data schema (prefix `OPH-`)
- **Question**: `{"id":"OPH-C<N>-<seq:03d>", "sec":"<Unit section>", "page":<int>,
  "q":"...", "opts":[4 strings], "ans":0-3, "exp":"...(Book pX)",
  "fmt":"fillup|match|truefalse|scenario|oddoneout|recall|numeric|management"}`
- **Unit**: `{"id":"OPH-U<N>-<n>", "ch":N, "n":n, "title":"...", "sec":"<Section> · pX-Y",
  "guide":"...", "qs":[ids in book order]}`
- **Chapter (roadmap)**: `{"n":1..50, "t":"Title", "p":<start page>, "live":bool}`
- Source of truth = `data/chNN.json`; `build_content.py` embeds it into
  `pulse-ophthalmology.html` and refuses to build if metadata or page ranges disagree.

## Per-chapter pipeline (repeat for every chapter)
1. **Render** the chapter's book pages to PNG (Book p = PDF p + K per the map above)
   and read every line, table, diagram, flowchart and label; zoom into any unclear
   spot — never guess.
2. **Author** `data/chNN.json`: questions in strict book order; units grouped by
   section; ≥1 varied-format item per unit (fill-up / match / true-false / scenario /
   odd-one-out / numeric / management); every explanation ends `(Book pX)`; every
   book page cited by ≥1 question; 4 plausible medical options with educational
   distractors (no "None of the above", no length giveaways, answers spread A–D).
3. **Build**: `python build_content.py` (embeds JSON → `pulse-ophthalmology.html`,
   marks the chapter live, validates title + page range vs the roadmap).
4. **Verify**: `python check_integrity.py` (structure, counts, order, citations,
   no-length-giveaway answers) + `node check_app_smoke.js` (runtime roadmap + quiz)
   + `python audit_variety.py` (format mix, predictability signals) → regenerate
   `AUDIT.md`.
5. **Commit + push** `arena/01a0b0b1-ophthal`, update this file (status, NEXT).
6. **User quality-checks**, then merges to `main` → chapter goes live at
   https://deva20045.github.io/OPHTHAL/

## Tooling
| File | Purpose |
|---|---|
| `pulse-ophthalmology.html` | The app (single HTML, no build step; open directly or via GitHub Pages) |
| `index.html` | Redirect → `pulse-ophthalmology.html` |
| `build_content.py` | 50-ch roadmap + JSON validator/embedder |
| `check_integrity.py` | Structural checks: counts, IDs, options, citations, order, source↔app equality, JS syntax |
| `check_app_smoke.js` | Runtime DOM-shim test: full 50-row roadmap, live-ch paths, quiz start |
| `audit_variety.py` | Format mix + predictability signals (length bias, hedging, fillers, template runs, option reuse) |
| `AUDIT.md` | Latest output of `audit_variety.py` |
| `uploads/` | The 2 source book PDFs (Book p1–233) |

## Status
- [x] PDFs moved to `uploads/` and committed (renamed to descriptive part names)
- [x] App skeleton + index redirect (all 50 chapters listed, rest "Soon")
- [x] Tooling adapted from the PULSE Medicine template
- [x] **Ch 1 "Layers and Structure of Eyeball" (p1–2): 5 units, 40 questions — BUILT & VERIFIED**
- [ ] Ch 2–50 (per pipeline above)

## NEXT
**Ch 2 "Anatomy of cornea, Anatomy of Sclera and its Pathologies" (p3–7)** —
render Part 1 PDF pages 6–10, read line-by-line, author `data/ch02.json`,
run build + checks + audit, commit + push.

## Live
- Preview: https://deva20045.github.io/OPHTHAL/ (updates after merge to `main`)
- App file: `pulse-ophthalmology.html` (also at `/pulse-ophthalmology.html`)
