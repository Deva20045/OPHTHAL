"""Build data/ch36..ch50.json from authoring sources and write the coverage audits.

Usage: python3 authoring/build_all.py            -> all of Ch 36-50 + the coverage audit files
       python3 authoring/build_all.py ch50_src   -> just one source module (no audit file)
"""
import importlib, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent
ALL = [f"ch{n}_src" for n in range(36, 51)]
# audit file name -> (chapter numbers included, book page span)
AUDITS = {
    "COVERAGE_AUDIT_CH36-42.md": (range(36, 43), (164, 194)),
    "COVERAGE_AUDIT_CH43-44.md": (range(43, 45), (195, 208)),
    "COVERAGE_AUDIT_CH45-46.md": (range(45, 47), (209, 219)),
    "COVERAGE_AUDIT_CH47-50.md": (range(47, 51), (220, 230)),
}
mods = sys.argv[1:] or ALL
res = {}
for m in mods:
    mod = importlib.import_module(m)
    c = mod.c
    print(c.num, len(c.qs), "questions", len(c.units), "units")
    res[c.num] = (c, mod.covered)
if len(mods) == len(ALL):
    for name, (numbers, span) in AUDITS.items():
        L = [f"# Coverage audit - Chapters {numbers.start}-{numbers.stop - 1} (Book pp. {span[0]}-{span[1]})", "",
             "Every source line, heading, table row, figure caption and bracket read from the scanned pages "
             "is listed as a numbered point, in book order, with the question ID(s) that test it. "
             "`authoring/lib.py::finish()` refuses to write a chapter unless every point is covered, questions are in "
             "(page, first-point) order, each question has 4 distinct options and the answer is not length-predictable.", ""]
        tp = tq = 0
        for n in numbers:
            c, cov = res[n]
            L += [f"## Chapter {c.num} - {c.title} (pp. {c.first}-{c.last}): {len(c.qs)} questions, {len(c.units)} units", ""]
            for p in range(c.first, c.last + 1):
                pts = c.points[p]
                qn = len({q for v in cov[p].values() for q in v})
                L += [f"### Book p{p} - {len(pts)} source points, {qn} questions", "",
                      "| # | Source line / point (as read from scan) | Question ID(s) |", "|---|---|---|"]
                for i, t in enumerate(pts, 1):
                    ids = ", ".join(x.replace("OPH-", "") for x in cov[p][i])
                    L.append(f"| {i} | {t.replace('|', '/')} | {ids} |")
                L.append("")
                tp += len(pts)
            tq += len(c.qs)
        L += ["## Totals", "", f"- Source points: {tp}, all covered (0 uncovered)", f"- Questions: {tq}", ""]
        (ROOT / name).write_text("\n".join(L), encoding="utf-8")
        print("audit written:", name, tp, "points,", tq, "questions")
