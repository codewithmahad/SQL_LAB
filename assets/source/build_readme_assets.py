"""Build the README's SQL lab modelling studies with Python's standard library.

Run from the repository root:
    python assets/source/build_readme_assets.py

The three views share a small personal-lab domain. All SVGs have accessible
metadata, a transparent canvas, and light/dark plus desktop/mobile layouts.
Original product logo files are not read or modified by this generator.
"""

from __future__ import annotations

import html
from pathlib import Path
import xml.etree.ElementTree as ET


ASSETS = Path(__file__).resolve().parents[1]
FONT = "'Segoe UI', Arial, sans-serif"
THEMES = {
    "light": {"ink": "#24292F", "muted": "#57606A", "line": "#6E7781", "rule": "#D0D7DE"},
    "dark": {"ink": "#E6EDF3", "muted": "#A6AFBA", "line": "#919BA7", "rule": "#3D444D"},
}


def label(x, y, value, t, size=21, anchor="middle", weight="400", underline=False, muted=False):
    decoration = ' text-decoration="underline"' if underline else ""
    colour = t["muted"] if muted else t["ink"]
    return (f'<text x="{x}" y="{y}" fill="{colour}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"{decoration}>'
            f'{html.escape(value)}</text>')


def path(d, t, dashed=False, width=1.7):
    dash = ' stroke-dasharray="5 5"' if dashed else ""
    return f'<path d="{d}" fill="none" stroke="{t["line"]}" stroke-width="{width}" stroke-linejoin="round"{dash}/>'


def segment(x1, y1, x2, y2, t, dashed=False):
    return path(f"M{x1} {y1} L{x2} {y2}", t, dashed)


def box(cx, cy, width, height, value, t, size=23):
    return (f'<rect x="{cx-width/2}" y="{cy-height/2}" width="{width}" height="{height}" '
            f'fill="none" stroke="{t["line"]}" stroke-width="1.7"/>'
            + label(cx, cy+8, value, t, size, weight="500"))


def oval(cx, cy, rx, value, t, key=False, size=20, ry=29):
    key_width = {"topic_id": 74, "exercise_id": 98, "work_id": 72}.get(value, len(value)*size*0.48)
    underline = segment(cx-key_width/2, cy+11, cx+key_width/2, cy+11, t) if key else ""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
            f'fill="none" stroke="{t["line"]}" stroke-width="1.5"/>'
            + label(cx, cy+7, value, t, size) + underline)


def diamond(cx, cy, width, height, value, t, size=21):
    return (path(f"M{cx-width/2} {cy} L{cx} {cy-height/2} L{cx+width/2} {cy} L{cx} {cy+height/2} Z", t)
            + label(cx, cy+7, value, t, size))


def ring(cx, cy, radius, t):
    return f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{t["line"]}" stroke-width="1.7"/>'


def write(name, width, height, title, desc, parts):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
           f'<title id="title">{html.escape(title)}</title>\n'
           f'<desc id="desc">{html.escape(desc)}</desc>\n'
           + "\n".join(parts) + "\n</svg>\n")
    ET.fromstring(svg)
    (ASSETS / name).write_text(svg, encoding="utf-8")


def chen(theme, t):
    desc = ("Personal lab study in Chen notation. Topic and Exercise are rectangular entities, "
            "joined by a contains relationship diamond with one-to-many cardinality. "
            "Exercise has total participation, shown by a double line: each exercise belongs to a topic. "
            "Each entity has an oval title attribute and an underlined identifier attribute, "
            "topic_id or exercise_id. This is a modelling study, not an implemented database schema.")
    p = [
        segment(171, 153, 137, 99, t), segment(249, 153, 285, 99, t),
        segment(711, 153, 661, 99, t), segment(789, 153, 839, 99, t),
        segment(294, 185, 392, 185, t),
        segment(561.4, 181, 666, 181, t), segment(561.4, 189, 666, 189, t),
        box(210, 185, 168, 64, "Topic", t), box(750, 185, 168, 64, "Exercise", t),
        diamond(480, 185, 176, 106, "contains", t),
        oval(130, 70, 88, "topic_id", t, key=True), oval(292, 70, 63, "title", t),
        oval(654, 70, 94, "exercise_id", t, key=True), oval(846, 70, 63, "title", t),
        label(342, 170, "1", t, 20, muted=True), label(618, 170, "N", t, 20, muted=True),
    ]
    write(f"chen-{theme}.svg", 960, 270, "SQL lab / Chen study", desc, p)

    p = [
        segment(202, 140, 126, 82, t), segment(278, 140, 354, 82, t),
        segment(240, 204, 240, 268, t),
        segment(236, 357.8, 236, 424, t), segment(244, 357.8, 244, 424, t),
        segment(202, 488, 126, 546, t), segment(278, 488, 354, 546, t),
        box(240, 172, 170, 64, "Topic", t), box(240, 456, 170, 64, "Exercise", t),
        diamond(240, 314, 170, 92, "contains", t),
        oval(115, 54, 88, "topic_id", t, key=True), oval(365, 54, 67, "title", t),
        oval(115, 574, 94, "exercise_id", t, key=True), oval(365, 574, 67, "title", t),
        label(261, 244, "1", t, 20, muted=True), label(263, 399, "N", t, 20, muted=True),
    ]
    write(f"chen-mobile-{theme}.svg", 480, 630, "SQL lab / Chen study", desc, p)


def table(x, y, width, title, rows, t):
    header, row_height = 56, 42
    height = header + len(rows)*row_height + 12
    p = [f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="5" fill="none" '
         f'stroke="{t["line"]}" stroke-width="1.7"/>',
         segment(x, y+header, x+width, y+header, t),
         label(x+22, y+36, title, t, 23, anchor="start", weight="600")]
    for i, (field, key) in enumerate(rows):
        p.append(label(x+22, y+header+30+i*row_height, field, t, 20, anchor="start"))
        if key:
            p.append(label(x+width-20, y+header+29+i*row_height, key, t, 15, anchor="end", muted=True))
    return p


def erd(theme, t):
    desc = ("Logical view of the same lab model. Topic has primary key topic_id and title. "
            "Exercise has primary key exercise_id, foreign key topic_id, and title. "
            "Each Exercise belongs to exactly one Topic; a Topic can have zero or many Exercises. "
            "The dashed non-identifying relationship leaves exercise_id as an independent primary key. "
            "This is a modelling study, not an implemented database schema.")
    p = table(45, 54, 300, "Topic", [("topic_id", "PK"), ("title", "")], t)
    p += table(615, 54, 300, "Exercise", [("exercise_id", "PK"), ("topic_id", "FK"), ("title", "")], t)
    p += [segment(345, 152, 570, 152, t, dashed=True),
          segment(361, 140, 361, 164, t), segment(371, 140, 371, 164, t),
          ring(577, 152, 7, t), segment(584, 152, 615, 152, t),
          path("M615 139 L596 152 L615 165", t),
          label(480, 130, "contains", t, 19, muted=True)]
    write(f"erd-{theme}.svg", 960, 278, "SQL lab / logical model", desc, p)

    p = table(55, 25, 370, "Topic", [("topic_id", "PK"), ("title", "")], t)
    p += table(55, 335, 370, "Exercise", [("exercise_id", "PK"), ("topic_id", "FK"), ("title", "")], t)
    p += [segment(240, 177, 240, 290, t, dashed=True),
          segment(228, 195, 252, 195, t), segment(228, 205, 252, 205, t),
          ring(240, 297, 7, t), segment(240, 304, 240, 335, t),
          path("M227 335 L240 316 L253 335", t),
          label(264, 258, "contains", t, 18, anchor="start", muted=True)]
    write(f"erd-mobile-{theme}.svg", 480, 555, "SQL lab / logical model", desc, p)


def eer(theme, t):
    desc = ("Enhanced conceptual model of lab work. WorkItem has an underlined work_id identifier "
            "and a title attribute. It specializes into SQLNote and DesignNote. The circle marked o "
            "denotes overlapping membership: one item may be both types. The single line from "
            "WorkItem denotes partial specialization: an item may be neither. Both subtypes inherit "
            "WorkItem attributes. This is a modelling study, not an implemented database schema.")
    p = [
        segment(310, 70, 385, 70, t), segment(575, 70, 650, 70, t),
        segment(480, 102, 480, 168, t),
        segment(460, 207, 270, 288, t), segment(500, 207, 690, 288, t),
        oval(220, 70, 90, "work_id", t, key=True), oval(725, 70, 75, "title", t),
        box(480, 70, 190, 64, "WorkItem", t),
        ring(480, 192, 24, t), label(480, 200, "o", t, 26),
        box(270, 320, 190, 64, "SQLNote", t), box(690, 320, 190, 64, "DesignNote", t),
    ]
    write(f"eer-{theme}.svg", 960, 390, "SQL lab / EER study", desc, p)

    p = [
        segment(201, 142, 130, 82, t), segment(279, 142, 350, 82, t),
        segment(240, 206, 240, 272, t),
        segment(222, 315, 124, 412, t), segment(258, 315, 356, 412, t),
        oval(115, 54, 86, "work_id", t, key=True), oval(365, 54, 67, "title", t),
        box(240, 174, 190, 64, "WorkItem", t),
        ring(240, 296, 24, t), label(240, 304, "o", t, 26),
        box(124, 444, 196, 64, "SQLNote", t, 22), box(356, 444, 196, 64, "DesignNote", t, 22),
    ]
    write(f"eer-mobile-{theme}.svg", 480, 510, "SQL lab / EER study", desc, p)


if __name__ == "__main__":
    for theme, colours in THEMES.items():
        chen(theme, colours)
        erd(theme, colours)
        eer(theme, colours)
    print("Built 12 SVGs: Chen, logical ER, and enhanced ER studies in light/dark and desktop/mobile layouts.")
