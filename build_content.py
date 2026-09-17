#!/usr/bin/env python3
"""Embed the chapter JSON artifacts into the standalone PULSE Ophthalmology app.

The browser app is intentionally a single offline HTML file.  Structured chapter
artifacts in data/chNN.json are the editable source of truth; run this script
whenever a chapter artifact changes.  Chapters without an artifact remain on
the roadmap as "Soon" (live: false).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-ophthalmology.html"
DATA_PATH = ROOT / "data"

# Full roadmap (Book p1-233) from the book's Contents pages,
# cross-verified against the scanned chapter title pages.  Number, title,
# starting Book page.  The "p" shown on the roadmap is the starting page.
CHAPTERS = [
    (1, "Layers and Structure of Eyeball", 1),
    (2, "Anatomy of cornea, Anatomy of Sclera and its Pathologies", 3),
    (3, "Anatomy of Uvea, Accomodation with its Anomalies", 8),
    (4, "Anatomy of Retina", 13),
    (5, "Ocular Routes of Drug Administration, Blood Supply of Eye and Embryology of Eye", 14),
    (6, "Visual Pathway and Visual Field Defects", 21),
    (7, "Pupillary Reflexes, Light Reflex and its Lesions", 26),
    (8, "Optic Atrophy: Optic Neuritis, Optic Neuropathies and Papilledema", 32),
    (9, "Congenital Anomalies of Optic Disc and Colour Blindness", 40),
    (10, "Squint : Extraocular Muscles and Binocular Single Vision", 43),
    (11, "Squint : Classifications and Directions", 46),
    (12, "Squint : Investigations", 48),
    (13, "Paralytic Squint", 54),
    (14, "Gaze Defects", 59),
    (15, "Restrictive Squint and Comitant Squint", 63),
    (16, "Pseudo-strabismus and Ocular Myopathies", 66),
    (17, "Anatomy and Metabolism", 68),
    (18, "Acquired Cataract : Types", 73),
    (19, "Acquired Cataract : Senile Cataract", 76),
    (20, "Cataract Surgery", 80),
    (21, "Complications of Cataract Surgery", 83),
    (22, "Congenital Cataract, Ectopia lentis and Miscellaneous", 87),
    (23, "Glaucoma : What and How?", 90),
    (24, "Investigations for Glaucoma", 94),
    (25, "Primary open angle glaucoma", 102),
    (26, "Primary Angle Closure Glaucoma", 109),
    (27, "Secondary Glaucoma(s) and Congenital Glaucoma", 113),
    (28, "Tests for Vision and Normal Optics of Eyes", 117),
    (29, "Myopia and Hypermetropia", 122),
    (30, "Astigmatism, Reading of Spectacle Prescription and Binocular Errors", 130),
    (31, "Refraction : How to prescribe glasses and Aphakia", 135),
    (32, "Anatomy and Investigations of Retina", 142),
    (33, "Retinoblastoma and Macular Disorders", 148),
    (34, "Dystrophies of Fundus : Retinitis Pigmentosa and others", 156),
    (35, "Retinal Vascular Disorders : Part 1", 160),
    (36, "Retinal Vascular Disorders : Part 2", 164),
    (37, "Retinal Detachment", 169),
    (38, "Special Investigations for Cornea", 172),
    (39, "Corneal Ulcer and Keratitis", 175),
    (40, "Corneal Dystrophies, Keratoconus and Miscellaneous Disorders", 180),
    (41, "Anterior Uveitis", 185),
    (42, "Intermediate, Posterior, Pan-uveitis and Miscellaneous Disorders", 191),
    (43, "Anatomy of Conjunctiva, Types of Conjunctivitis and Pterygium", 195),
    (44, "Eyelids : Anatomy and Pathologies", 206),
    (45, "Anatomy of Orbit and Proptosis", 209),
    (46, "Lacrimal apparatus : Anatomy, Watering eye and Dry eye", 215),
    (47, "Ocular Trauma", 220),
    (48, "Community Ophthalmology", 223),
    (49, "Lasers In Ophthalmology", 228),
    (50, "Physiology of Vision", 229),
]


def compact(value: object) -> str:
    """Use compact, UTF-8 JSON so the standalone app remains easy to ship."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def between(text: str, start: str, end: str) -> tuple[int, int]:
    first = text.index(start)
    second = text.index(end, first)
    return first, second


def main() -> None:
    expected = {number: (title, page) for number, title, page in CHAPTERS}
    questions: list[dict] = []
    units: list[dict] = []
    live: dict[int, dict] = {}

    for number, title, start_page in CHAPTERS:
        path = DATA_PATH / f"ch{number:02d}.json"
        if not path.exists():
            continue
        chapter = json.loads(path.read_text(encoding="utf-8"))
        if chapter["chapter"] != number:
            raise ValueError(f"{path.name}: chapter number does not match filename")
        if chapter["title"] != title:
            raise ValueError(
                f"{path.name}: expected title {title!r}, got {chapter['title']!r}"
            )
        first = int(chapter["pageRange"].split("-", 1)[0])
        if first != start_page:
            raise ValueError(
                f"{path.name}: pageRange starts at {first}, expected {start_page}"
            )
        for q in chapter["questions"]:
            if not re.fullmatch(rf"OPH-C{number}-\d{{3}}", q["id"]):
                raise ValueError(
                    f"{path.name}: question id {q['id']!r} does not match OPH-C{number}-NNN"
                )
        for u in chapter["units"]:
            if not re.fullmatch(rf"OPH-U{number}-\d+", u["id"]):
                raise ValueError(
                    f"{path.name}: unit id {u['id']!r} does not match OPH-U{number}-N"
                )
        questions.extend(chapter["questions"])
        units.extend(chapter["units"])
        live[number] = chapter

    html = APP_PATH.read_text(encoding="utf-8")
    q_start, _ = between(html, "const QUESTIONS = ", "\nconst UNITS = ")
    u_start, _ = between(html, "const UNITS = ", "\nconst CHAPTERS = ")
    c_start, c_end = between(html, "const CHAPTERS = ", "\nconst QBYID = ")

    roadmap = []
    for number, title, start_page in CHAPTERS:
        if number in live:
            first = int(live[number]["pageRange"].split("-", 1)[0])
            roadmap.append({"n": number, "t": title, "p": first, "live": True})
        else:
            roadmap.append({"n": number, "t": title, "p": start_page, "live": False})

    html = (
        html[:q_start]
        + "const QUESTIONS = "
        + compact(questions)
        + ";\nconst UNITS = "
        + compact(units)
        + ";\nconst CHAPTERS = "
        + json.dumps(roadmap, ensure_ascii=False, indent=2)
        + ";"
        + html[c_end:]
    )
    APP_PATH.write_text(html, encoding="utf-8")
    live_count = len(live)
    print(
        f"Embedded {len(questions)} questions and {len(units)} units across "
        f"{live_count} live chapter(s) of {len(CHAPTERS)} roadmap chapters "
        f"in {APP_PATH.name}."
    )


if __name__ == "__main__":
    main()
