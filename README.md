# PULSE Ophthalmology

A single-file MCQ study app for **Ophthalmology, Marrow Edition 8** (Book p1–233).
Questions follow the book **line-by-line, in strict page order**, in varied formats
(recall, fill-ups, match-the-following, true/false, clinical scenarios, odd-one-out,
numeric, management). Every explanation ends with the exact book-page citation, and
options are shuffled on every run — so after solving a chapter you should not need
the PDF.

> **Live:** https://deva20045.github.io/OPHTHAL/ (served from `main`; the working
> branch previews here). Open `pulse-ophthalmology.html` directly — no build step.

## Status
All 50 chapters are listed from day one; live chapters unlock automatically, the
rest show a **Soon** badge.

| Scope | Status |
|---|---|
| Ch 1 · Layers and Structure of Eyeball (p1–2) — 5 units, 40 questions | ✅ live |
| Ch 2 · Anatomy of cornea, Anatomy of Sclera and its Pathologies (p3–7) — 6 units, 40 questions | ✅ live on this branch |
| Ch 3 · Anatomy of Uvea, Accomodation with its Anomalies (p8–12) — 5 units, 37 questions | ✅ live on this branch |
| Ch 4 · Anatomy of Retina (p13) — 2 units, 14 questions | ✅ live on this branch |
| Ch 5 · Ocular Routes of Drug Administration, Blood Supply of Eye and Embryology of Eye (p14–20) — 6 units, 47 questions | ✅ live on this branch |
| Ch 6 · Visual Pathway and Visual Field Defects (p21–25) — 5 units, 42 questions | ✅ live on this branch |
| Ch 7 · Pupillary Reflexes, Light Reflex and its Lesions (p26–31) — 5 units, 40 questions | ✅ live |
| Ch 8 · Optic Atrophy: Optic Neuritis, Optic Neuropathies and Papilledema (p32–39) — 6 units, 48 questions | ✅ live |
| Ch 9 · Congenital Anomalies of Optic Disc and Colour Blindness (p40–42) — 3 units, 24 questions | ✅ live |
| Ch 10 · Squint : Extraocular Muscles and Binocular Single Vision (p43–45) — 3 units, 24 questions | ✅ live |
| Ch 11 · Squint : Classifications and Directions (p46–47) — 2 units, 20 questions | ✅ live |
| Ch 12 · Squint : Investigations (p48–53) — 5 units, 38 questions | ✅ live |
| Ch 13 · Paralytic Squint (p54–58) — 5 units, 40 questions | ✅ live |
| Ch 14 · Gaze Defects (p59–62) — 4 units, 33 questions | ✅ live |
| Ch 15 · Restrictive Squint and Comitant Squint (p63–65) — 3 units, 24 questions | ✅ live |
| Ch 16 · Pseudo-strabismus and Ocular Myopathies (p66–67) — 3 units, 29 questions | ✅ live on this branch |
| Ch 17–50 (Lens, Glaucoma, Optics, Retina, Cornea, Uvea, Conjunctiva, Adnexa, Miscellaneous) | 🚧 in progress |

See **`PROGRESS.md`** — the single source of truth: page-offset map, 50-chapter
roadmap, data schema, per-chapter pipeline, and NEXT step.

## Repository layout
| Path | What it is |
|---|---|
| `pulse-ophthalmology.html` | The app (all data embedded; standalone) |
| `index.html` | Redirect → `pulse-ophthalmology.html` |
| `data/chNN.json` | Authoring source of truth per live chapter |
| `build_content.py` | Roadmap + validator; embeds `data/chNN.json` into the app |
| `check_integrity.py` | Structural gate (counts, order, citations, option quality, JS syntax) |
| `check_app_smoke.js` | Runtime test (DOM shim): roadmap rows, paths, quiz start |
| `audit_variety.py` | Format-mix + predictability audit (output saved to `AUDIT.md`) |
| `uploads/` | The 2 source book PDFs (Book p1–233) |

## Run the checks (after any content change)
```bash
python build_content.py        # embeds data/ into pulse-ophthalmology.html
python check_integrity.py      # must PASS
node check_app_smoke.js        # must PASS
python audit_variety.py > AUDIT.md
```

## Quality bar (enforced, not aspirational)
- Every book line, table, diagram, flowchart, classification, value and exception
  covered in book order; every page cited.
- 4 distinct, plausible, medical options per question — never "None of the above",
  never length-givable (answer ≤ 3× longest distractor), options shuffled at runtime.
- Mixed formats in every unit; clinical scenarios, comparisons and exam
  distinctions, not page-quizzing.
