#!/usr/bin/env python3
"""Render book pages of the Ophthalmology scans (Book p1-233) to PNG.

The scans in `uploads/` have no text layer and their printed page numbers do NOT
follow one constant offset: a few leaves are duplicated or unnumbered, so
Book page != PDF page + K everywhere.  See the "Verified offset table" in
PROGRESS.md.  This helper therefore locates each page by OCR of the printed
number in the page header (when an OCR engine is available) and falls back to
the offset table otherwise.

Usage
-----
    python render_pages.py 164 165 166          # render those book pages
    python render_pages.py --range 164 168      # render a range
    python render_pages.py --range 164 168 --dpi 300 --out pages/

Requirements
------------
    pip install pymupdf              # rendering (required)
    pip install rapidocr-onnxruntime # header OCR (optional but recommended)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UPLOADS = ROOT / "uploads"
PARTS = [
    ("Ophthalmology_Part1_pages_1-116.pdf", 1, 116),
    ("Ophthalmology_Part2_pages_117-233.pdf", 117, 233),
]

# Verified offset table (see PROGRESS.md): (last PDF page, offset K) with
# Book page = PDF page + K.  Used when OCR is unavailable or a header is blank.
OFFSETS: dict[str, list[tuple[int, int]]] = {
    "Ophthalmology_Part1_pages_1-116.pdf": [(3, -3), (119, -3)],
    "Ophthalmology_Part2_pages_117-233.pdf": [(20, 116), (21, 115), (68, 115), (117, 113)],
}


def guess_pdf_page(part: str, book_page: int) -> int:
    for last_pdf, offset in OFFSETS[part]:
        if book_page - offset <= last_pdf:
            return book_page - offset
    return book_page - OFFSETS[part][-1][1]


def header_number(doc, pdf_index: int, ocr) -> int | None:
    """Return the printed book page number in the header of a PDF page."""
    if ocr is None:
        return None
    try:
        from PIL import Image
    except ImportError:  # pragma: no cover - Pillow ships with the OCR stack
        return None
    page = doc[pdf_index]
    clip = page.rect
    clip = type(clip)(0, 0, clip.width, 110)
    pix = page.get_pixmap(dpi=250, clip=clip)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    result, _ = ocr(img)
    for _box, text, _score in result or []:
        if re.fullmatch(r"\d{1,3}", text.strip()):
            return int(text.strip())
    return None


def find_pdf_index(doc, part: str, book_page: int, ocr) -> int:
    """Locate a book page, confirming the printed number when OCR is available."""
    guess = guess_pdf_page(part, book_page)
    first = max(0, (guess - 1) - 4)
    last = min(doc.page_count - 1, (guess - 1) + 4)
    for index in range(first, last + 1):
        if header_number(doc, index, ocr) == book_page:
            return index
    if ocr is None:
        print(
            f"  warning: rendering PDF page {guess} for Book p{book_page} without "
            "header OCR - install rapidocr-onnxruntime to verify page numbers",
            file=sys.stderr,
        )
    return guess - 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pages", nargs="*", type=int, help="book pages to render")
    parser.add_argument("--range", nargs=2, type=int, metavar=("FIRST", "LAST"))
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--out", default=".", help="output directory")
    parser.add_argument("--no-ocr", action="store_true", help="skip header OCR verification")
    args = parser.parse_args()

    wanted = list(args.pages)
    if args.range:
        wanted += list(range(args.range[0], args.range[1] + 1))
    if not wanted:
        parser.error("give at least one book page or --range FIRST LAST")

    ocr = None
    if not args.no_ocr:
        try:
            from rapidocr_onnxruntime import RapidOCR

            ocr = RapidOCR()
        except Exception:  # pragma: no cover - optional dependency
            print("  note: rapidocr-onnxruntime unavailable; using the offset table only", file=sys.stderr)

    import pymupdf

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    docs = {}
    for book_page in wanted:
        for part, low, high in PARTS:
            if low <= book_page <= high:
                break
        else:
            print(f"Book p{book_page} is outside the scan range (1-233)", file=sys.stderr)
            continue
        if part not in docs:
            docs[part] = pymupdf.open(str(UPLOADS / part))
        doc = docs[part]
        index = find_pdf_index(doc, part, book_page, ocr)
        out = outdir / f"book-p{book_page}.png"
        doc[index].get_pixmap(dpi=args.dpi).save(out)
        print(f"Book p{book_page} -> {part} PDF p{index + 1} -> {out}")


if __name__ == "__main__":
    main()
