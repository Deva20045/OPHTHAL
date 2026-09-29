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

- **Verified offset table (OCR of every scanned page number, 2026-09).** The scans
  contain a few duplicate/unnumbered leaves, so K is NOT constant — always confirm
  the printed page number in the header before authoring:

| Part | PDF pages | K | Book pages | note |
|---|---|---|---|---|
| Part 1 | 1–3 | — | — | contents pages, no book number |
| Part 1 | 4–119 | −3 | 1–116 | verified at PDF 5→2, 8→5, 82→79, 84→81 |
| Part 2 | 1–20 | +116 | 117–136 | verified PDF 1→117, 20→136 |
| Part 2 | 21 | +115 | 136 | **duplicate scan of book p136** (second, annotated copy) |
| Part 2 | 22–68 | +115 | 137–183 | verified PDF 22→137, 27→142, 45→160 |
| Part 2 | 69–117 | +113 | 182–230 | verified PDF 69→182, 113→226, 116→229 |
| Part 2 | 117 | — | 230 | final leaf, unnumbered (last content page) |

  Practical rule for Chapters 31–35 (all rendered and read this session):
  Book p135 = PDF 19, p136 = PDF 20 (dup at 21), p137–183 = PDF + 115,
  p184+ = PDF + 113.

- First 3 PDF pages of Part 1 = the book's Contents pages (not content scope).
- Formula: **Book page = PDF page + K** (K per part above).
  Part 1: PDF p4 = Book p1 … PDF p119 = Book p116.
  Part 2: PDF p1 = Book p117 … PDF p117 = Book p233.
- Final content page = Book p233 (Miscellaneous — Physiology of Vision).

## Roadmap — all 50 chapters listed from day one (status: LIVE / SOON)
| # | Chapter | Book start | Status |
|---|---|---|---|
| 1 | Layers and Structure of Eyeball | p1 | **LIVE** |
| 2 | Anatomy of cornea, Anatomy of Sclera and its Pathologies | p3 | **LIVE** |
| 3 | Anatomy of Uvea, Accomodation with its Anomalies | p8 | **LIVE** |
| 4 | Anatomy of Retina | p13 | **LIVE** |
| 5 | Ocular Routes of Drug Administration, Blood Supply of Eye and Embryology of Eye | p14 | **LIVE** |
| 6 | Visual Pathway and Visual Field Defects | p21 | **LIVE** |
| 7 | Pupillary Reflexes, Light Reflex and its Lesions | p26 | **LIVE** |
| 8 | Optic Atrophy: Optic Neuritis, Optic Neuropathies and Papilledema | p32 | **LIVE** |
| 9 | Congenital Anomalies of Optic Disc and Colour Blindness | p40 | **LIVE** |
| 10 | Squint : Extraocular Muscles and Binocular Single Vision | p43 | **LIVE** |
| 11 | Squint : Classifications and Directions | p46 | **LIVE** |
| 12 | Squint : Investigations | p48 | **LIVE** |
| 13 | Paralytic Squint | p54 | **LIVE** |
| 14 | Gaze Defects | p59 | **LIVE** |
| 15 | Restrictive Squint and Comitant Squint | p63 | **LIVE** |
| 16 | Pseudo-strabismus and Ocular Myopathies | p66 | **LIVE** |
| 17 | Anatomy and Metabolism (Lens) | p68 | **LIVE** |
| 18 | Acquired Cataract : Types | p73 | **LIVE** |
| 19 | Acquired Cataract : Senile Cataract | p76 | **LIVE** |
| 20 | Cataract Surgery | p80 | **LIVE** |
| 21 | Complications of Cataract Surgery | p83 | **LIVE** |
| 22 | Congenital Cataract, Ectopia lentis and Miscellaneous | p87 | **LIVE** |
| 23 | Glaucoma : What and How? | p90 | **LIVE** |
| 24 | Investigations for Glaucoma | p94 | **LIVE** |
| 25 | Primary Open Angle Glaucoma | p102 | **LIVE** |
| 26 | Primary Angle Closure Glaucoma | p109 | **LIVE** |
| 27 | Secondary Glaucoma(s) and Congenital Glaucoma | p113 | **LIVE** |
| 28 | Tests for Vision and Normal Optics of Eyes | p117 | **LIVE** |
| 29 | Myopia and Hypermetropia | p122 | **LIVE** |
| 30 | Astigmatism, Reading of Spectacle Prescription and Binocular Errors | p130 | **LIVE** |
| 31 | Refraction : How to prescribe glasses and Aphakia | p135 | **LIVE** |
| 32 | Anatomy and Investigations of Retina | p142 | **LIVE** |
| 33 | Retinoblastoma and Macular Disorders | p148 | **LIVE** |
| 34 | Dystrophies of Fundus : Retinitis Pigmentosa and others | p156 | **LIVE** |
| 35 | Retinal Vascular Disorders : Part 1 | p160 | **LIVE** |
| 36 | Retinal Vascular Disorders : Part 2 | p164 | **LIVE** |
| 37 | Retinal Detachment | p169 | **LIVE** |
| 38 | Special Investigations for Cornea | p172 | **LIVE** |
| 39 | Corneal Ulcer and Keratitis | p175 | **LIVE** |
| 40 | Corneal Dystrophies, Keratoconus and Miscellaneous Disorders | p180 | **LIVE** |
| 41 | Anterior Uveitis | p185 | **LIVE** |
| 42 | Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders | p191 | **LIVE** |
| 43 | Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium | p195 | **LIVE** |
| 44 | Eyelids : Anatomy and Pathologies | p206 | **LIVE** |
| 45 | Anatomy of Orbit and Proptosis | p209 | **LIVE** |
| 46 | Lacrimal apparatus : Anatomy, Watering eye and Dry eye | p215 | **LIVE** |
| 47 | Ocular Trauma | p220 | SOON |
| 48 | Community Ophthalmology | p223 | SOON |
| 49 | Lasers In Ophthalmology | p228 | SOON |
| 50 | Physiology of Vision | p229 | SOON |

*(Status column: Ch 1-46 = **LIVE**; every other chapter = **SOON** — rendered in the app
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
1. **Render** the chapter's book pages to PNG with `python render_pages.py --range F L`
   (it resolves Book page → PDF page by OCR of the printed header number, so it stays
   correct where the scan offsets drift) and read every line, table, diagram, flowchart
   and label; zoom into any unclear spot — never guess.
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
| `render_pages.py` | Renders book pages to PNG (`python render_pages.py 164 165` / `--range 164 168`); locates each page by OCR of the printed header number and falls back to the verified offset table |
| `AUDIT.md` | Latest output of `audit_variety.py` |
| `uploads/` | The 2 source book PDFs (Book p1–233) |

## Status
- [x] PDFs moved to `uploads/` and committed (renamed to descriptive part names)
- [x] App skeleton + index redirect (all 50 chapters listed, rest "Soon")
- [x] Tooling adapted from the PULSE Medicine template
- [x] **Ch 1 "Layers and Structure of Eyeball" (p1–2): 5 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 2 "Anatomy of cornea, Anatomy of Sclera and its Pathologies" (p3–7): 6 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 3 "Anatomy of Uvea, Accomodation with its Anomalies" (p8–12): 5 units, 37 questions — BUILT & VERIFIED**
- [x] **Ch 4 "Anatomy of Retina" (p13): 2 units, 14 questions — BUILT & VERIFIED**
- [x] **Ch 5 "Ocular Routes of Drug Administration, Blood Supply of Eye and Embryology of Eye" (p14–20): 6 units, 47 questions — BUILT & VERIFIED**
- [x] **Ch 6 "Visual Pathway and Visual Field Defects" (p21–25): 5 units, 42 questions — BUILT & VERIFIED**
- [x] **Ch 7 "Pupillary Reflexes, Light Reflex and its Lesions" (p26–31): 5 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 8 "Optic Atrophy: Optic Neuritis, Optic Neuropathies and Papilledema" (p32–39): 6 units, 48 questions — BUILT & VERIFIED**
- [x] **Ch 9 "Congenital Anomalies of Optic Disc and Colour Blindness" (p40–42): 3 units, 24 questions — BUILT & VERIFIED**
- [x] **Ch 10 "Squint : Extraocular Muscles and Binocular Single Vision" (p43–45): 3 units, 24 questions — BUILT & VERIFIED**
- [x] **Ch 11 "Squint : Classifications and Directions" (p46–47): 2 units, 20 questions — BUILT & VERIFIED**
- [x] **Ch 12 "Squint : Investigations" (p48–53): 5 units, 38 questions — BUILT & VERIFIED**
- [x] **Ch 13 "Paralytic Squint" (p54–58): 5 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 14 "Gaze Defects" (p59–62): 4 units, 33 questions — BUILT & VERIFIED**
- [x] **Ch 15 "Restrictive Squint and Comitant Squint" (p63–65): 3 units, 24 questions — BUILT & VERIFIED**
- [x] **Ch 16 "Pseudo-strabismus and Ocular Myopathies" (p66–67): 3 units, 20 questions — BUILT & VERIFIED**
- [x] **Ch 17 "Anatomy and Metabolism" (p68–72): 5 units, 40 questions — BUILT & VERIFIED**
- [x] **Ch 18 "Acquired Cataract : Types" (p73–75): 4 units, 28 questions — BUILT & VERIFIED**
- [x] **Ch 19 "Acquired Cataract : Senile Cataract" (p76–79): 4 units, 32 questions — BUILT & VERIFIED**
- [x] **Ch 20 "Cataract Surgery" (p80–82): 4 units, 28 questions — BUILT & VERIFIED**
- [x] **Ch 21 "Complications of Cataract Surgery" (p83–86): 4 units, 26 questions — BUILT & VERIFIED**
- [x] **Ch 22 "Congenital Cataract, Ectopia lentis and Miscellaneous" (p87–89): 3 units, 18 questions — BUILT & VERIFIED**
- [x] **Ch 23 "Glaucoma : What and How?" (p90–93): 4 units, 19 questions — BUILT & VERIFIED**
- [x] **Ch 24 "Investigations for Glaucoma" (p94–101): 6 units, 30 questions — BUILT & VERIFIED**
- [x] **Ch 25 "Primary Open Angle Glaucoma" (p102–108): 6 units, 30 questions — BUILT & VERIFIED**
- [x] **Ch 26 "Primary Angle Closure Glaucoma" (p109–112): 5 units, 35 questions — BUILT & VERIFIED**
- [x] **Ch 27 "Secondary Glaucoma(s) and Congenital Glaucoma" (p113–116): 6 units, 36 questions — BUILT & VERIFIED**
- [x] **Ch 28 "Tests for Vision and Normal Optics of Eyes" (p117–121): 5 units, 38 questions — BUILT & VERIFIED**
- [x] **Ch 29 "Myopia and Hypermetropia" (p122–129): 7 units, 47 questions — BUILT & VERIFIED**
- [x] **Ch 30 "Astigmatism, Reading of Spectacle Prescription and Binocular Errors" (p130–134): 5 units, 33 questions — BUILT & VERIFIED**
- [x] **Ch 31 "Refraction : How to prescribe glasses and Aphakia" (p135–141): 7 units, 43 questions — BUILT & VERIFIED**
- [x] **Ch 32 "Anatomy and Investigations of Retina" (p142–147): 7 units, 42 questions — BUILT & VERIFIED**
- [x] **Ch 33 "Retinoblastoma and Macular Disorders" (p148–155): 8 units, 53 questions — BUILT & VERIFIED**
- [x] **Ch 34 "Dystrophies of Fundus : Retinitis Pigmentosa and others" (p156–159): 5 units, 35 questions — BUILT & VERIFIED**
- [x] **Ch 35 "Retinal Vascular Disorders : Part 1" (p160–163): 5 units, 34 questions — BUILT & VERIFIED**
- [x] **Ch 36 "Retinal Vascular Disorders : Part 2" (p164–168): 6 units, 64 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 37 "Retinal Detachment" (p169–171): 5 units, 44 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 38 "Special Investigations for Cornea" (p172–174): 5 units, 39 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 39 "Corneal Ulcer and Keratitis" (p175–179): 8 units, 71 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 40 "Corneal Dystrophies, Keratoconus and Miscellaneous Disorders" (p180–184): 6 units, 67 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 41 "Anterior Uveitis" (p185–190): 9 units, 76 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 42 "Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders" (p191–194): 9 units, 48 questions — REBUILT FROM SCANS & VERIFIED** (line-by-line; coverage in `COVERAGE_AUDIT_CH36-42.md`)
- [x] **Ch 43 "Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium" (p195–205): 7 units, 72 questions — BUILT FROM SCANS & VERIFIED** (line-by-line; all 11 Book pages cited; no length-giveaway)
- [x] **Ch 44 "Eyelids : Anatomy and Pathologies" (p206–208): 4 units, 29 questions — BUILT FROM SCANS & VERIFIED** (line-by-line; all 3 Book pages cited)
- [x] **Ch 45 "Anatomy of Orbit and Proptosis" (p209–214): 5 units, 44 questions — BUILT FROM SCANS & VERIFIED** (line-by-line; all 6 Book pages cited)
- [x] **Ch 46 "Lacrimal apparatus : Anatomy, Watering eye and Dry eye" (p215–219): 4 units, 33 questions — BUILT FROM SCANS & VERIFIED** (line-by-line; all 5 Book pages cited)
- [ ] Ch 47–50 (per pipeline above)

## NEXT
**Ch 47 "Ocular Trauma" (p220–222)** —
render Part 2 PDF pages by printed page number (p220 onward = PDF 105 + … per offset p184+ = PDF +113), read line-by-line,
author it, run build + checks + audit, commit + push.

### Authoring pipeline used for Ch 36–42 (reuse it)
- `authoring/lib.py` — `Chapter(num, title, first, last, points)`; `points` = `{page: [every source
  line/heading/table row/caption in reading order]}`. `c.unit(...)` opens a unit,
  `c.q(page, fmt, stem, correct, [3 wrong], explanation, cov=[point numbers], sec)` adds a question.
  `c.finish()` refuses to write `data/chNN.json` unless every point is covered, questions are in
  (page, first-point) order, options are 4 distinct strings and the answer is not length-predictable;
  it shuffles answer positions and appends "(Book pN)" to explanations.
- `authoring/chNN_src.py` — one source file per chapter (points + questions).
- `python3 authoring/build_all.py [chNN_src ...]` — builds chapters; with no arguments it builds all of
  Ch 36–42 and regenerates `COVERAGE_AUDIT_CH36-42.md`.
- Scan quirks found while reading Ch 36–42: PDF 67/68 (p182/p183) are duplicated at PDF 69/70, so
  p184 = PDF 71 and K becomes +113 from there; Ch 42's p193/p194 print in order in the scan.
  Book spellings/handwriting are preserved (e.g. "Flourescein", "Cephalozin", "typer 1", "COAXa").

## Live
- Preview: https://deva20045.github.io/OPHTHAL/ (updates after merge to `main`)
- App file: `pulse-ophthalmology.html` (also at `/pulse-ophthalmology.html`)
