# -*- coding: utf-8 -*-
"""Extract English project blocks from eng_resume.legacy.html → _projects_en.txt"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "eng_resume.legacy.html").read_text(encoding="utf-8")
start = html.find("<!-- project experience -->")
end = html.find('<td class="plate1">Education</td>', start)
if start < 0 or end < 0:
    raise SystemExit("markers not found")
chunk = html[start:end]
blocks = re.split(r"<tr>\s*<td class=\"p15\">", chunk)
items: list[tuple[str, str, str]] = []

for b in blocks[1:]:
    tm = re.search(r"<strong>([\s\S]*?)</strong>", b)
    if not tm:
        continue
    title = re.sub(r"\s+", " ", tm.group(1)).strip()
    title = title.replace("&amp;", "&")
    tim = re.search(r'class="time">([^<]+)</td>', b)
    time = tim.group(1).strip() if tim else ""

    desc_parts: list[str] = []
    for km in re.finditer(
        r'class="keys">([\s\S]*?)</td>\s*<td[^>]*class="txt1"[^>]*>([\s\S]*?)</td>\s*</tr>',
        b,
    ):
        key = re.sub(r"\s+", " ", km.group(1)).strip()
        val = km.group(2)
        val = re.sub(r"<br\s*/?>", " ", val, flags=re.I)
        val = re.sub(r"<[^>]+>", "", val)
        val = re.sub(r"\s+", " ", val).strip()
        if not val:
            continue
        lk = key.lower()
        if any(
            x in lk
            for x in (
                "project description",
                "description",
                "related company",
                "所属公司",
            )
        ):
            if "related company" in lk or "所属公司" in key:
                desc_parts.append(f"[{key}] {val}")
            else:
                desc_parts.append(val)

    desc = " ".join(desc_parts).strip()[:2200]
    items.append((title, time, desc))

out = "\n---\n".join(f"{t}\n{time}\n{d}" for t, time, d in items)
(ROOT / "_projects_en.txt").write_text(out, encoding="utf-8")
print("wrote", len(items), "projects")
