"""Authoring helper for Ch 36-42 (rebuilt line-by-line from the scanned book).

Each chapter source file declares, for every book page, the numbered list of source
POINTS (every line / heading / table row / label read from the scan, in reading order),
then writes questions that declare which points they cover (`cov`).  `finish()` refuses to
write anything unless: every point of every page is covered by >=1 question, questions are
in strict (page, first-point) order, options are 4 distinct strings, and the answer is not
length-predictable.  It also emits the page-by-page coverage audit rows.
"""
from __future__ import annotations
import json, random, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Chapter:
    def __init__(self, num, title, first, last, points, seed=None):
        self.num, self.title, self.first, self.last = num, title, first, last
        self.points = points            # {page: [str, ...]}
        self.qs, self.units = [], []
        self.rng = random.Random(seed if seed is not None else num * 7919)
        self._bag = []
        self._unit = None
        assert set(points) == set(range(first, last + 1)), f"points must exist for every page {first}-{last}"

    # ---- units -------------------------------------------------------
    def unit(self, title, sec, guide):
        self._unit = {"title": title, "sec": sec, "guide": guide, "qs": []}
        self.units.append(self._unit)

    # ---- questions ---------------------------------------------------
    def _slot(self):
        if not self._bag:
            self._bag = [0, 1, 2, 3]
            self.rng.shuffle(self._bag)
            if self.qs and self._bag[0] == self.qs[-1]["ans"]:
                self._bag.append(self._bag.pop(0))
        return self._bag.pop()

    def q(self, page, fmt, text, correct, wrong, exp, cov, sec=""):
        assert len(wrong) == 3, (page, text)
        assert self._unit is not None
        pos = self._slot()
        opts = list(wrong)
        opts.insert(pos, correct)
        n = len(self.qs) + 1
        qid = f"OPH-C{self.num}-{n:03d}"
        self.qs.append({
            "id": qid, "sec": sec or self._unit["title"], "page": page, "fmt": fmt,
            "q": text, "opts": opts, "ans": pos,
            "exp": exp.rstrip() + f" (Book p{page})",
            "_cov": sorted(set(cov)),
        })
        self._unit["qs"].append(qid)
        return qid

    # ---- verification + output --------------------------------------
    def finish(self):
        errs = []
        covered = {p: {} for p in self.points}
        last_key = (0, 0)
        for q in self.qs:
            key = (q["page"], q["_cov"][0] if q["_cov"] else 0)
            if key < last_key:
                errs.append(f'{q["id"]}: out of book order {key} < {last_key}')
            last_key = key
            for c in q["_cov"]:
                if not 1 <= c <= len(self.points[q["page"]]):
                    errs.append(f'{q["id"]}: bad point {c} on p{q["page"]}')
                else:
                    covered[q["page"]].setdefault(c, []).append(q["id"])
            if len({o.strip().casefold() for o in q["opts"]}) != 4:
                errs.append(f'{q["id"]}: options not distinct')
            lens = [len(o) for o in q["opts"]]
            if lens[q["ans"]] > 3 * max(l for i, l in enumerate(lens) if i != q["ans"]):
                errs.append(f'{q["id"]}: length giveaway')
        for p, pts in self.points.items():
            for i, t in enumerate(pts, 1):
                if i not in covered[p]:
                    errs.append(f"p{p} point {i} NOT COVERED: {t}")
        if errs:
            raise SystemExit("\n".join(errs))
        # write json
        units = []
        for i, u in enumerate(self.units, 1):
            pages = [next(q["page"] for q in self.qs if q["id"] == x) for x in u["qs"]]
            lo, hi = min(pages), max(pages)
            rng = f"p{lo}" if lo == hi else f"p{lo}-{hi}"
            units.append({"id": f"OPH-U{self.num}-{i}", "ch": self.num, "n": i, "title": u["title"],
                          "sec": f'{u["sec"]} · {rng}', "guide": u["guide"], "qs": u["qs"]})
        qs = [{k: v for k, v in q.items() if not k.startswith("_")} for q in self.qs]
        out = {"chapter": self.num, "title": self.title, "pageRange": f"{self.first}-{self.last}",
               "questions": qs, "units": units}
        (ROOT / "data" / f"ch{self.num:02d}.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return covered
