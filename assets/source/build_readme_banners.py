"""Build the README's database lineup and Java stack compositions.

Uses only Python's standard library and the credited local SVG logo originals.
Logos retain their geometry and colours; only placement and scale change.
"""

from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1]
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
FONT = "'Segoe UI', Arial, sans-serif"
THEMES = {
    "light": dict(ink="#1F2328", muted="#59636E", rule="#D1D9E0", panel="#F6F8FA", selected="#EDF3F7"),
    "dark": dict(ink="#F0F3F6", muted="#A7B0BA", rule="#343D47", panel="#151B23", selected="#1C2B37"),
}


def text(x, y, value, t, size=18, weight=400, anchor="start", muted=False, tracking=0):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{tracking}" '
            f'fill="{t["muted"] if muted else t["ink"]}">{html.escape(value)}</text>')


def rect(x, y, w, h, t, fill="none", radius=0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{fill}" stroke="{t["rule"]}" stroke-width="1"/>')


def line(x1, y1, x2, y2, t):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{t["rule"]}"/>' if y1 == y2 else (
        f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{t["rule"]}"/>')


def logo(name, cx, cy, size):
    """Embed vector originals with independent IDs and CSS class names."""
    node = ET.parse(ASSETS / "logos" / f"{name}.svg").getroot()
    prefix = name + "-"
    ids = {n.attrib["id"] for n in node.iter() if "id" in n.attrib}
    classes = {c for n in node.iter() for c in n.attrib.get("class", "").split()}
    for n in node.iter():
        for attr, value in list(n.attrib.items()):
            if attr == "id":
                n.set(attr, prefix + value)
            elif attr == "class":
                n.set(attr, " ".join(prefix + c for c in value.split()))
            else:
                for ident in ids:
                    value = value.replace(f"url(#{ident})", f"url(#{prefix}{ident})")
                    if value == f"#{ident}":
                        value = "#" + prefix + ident
                n.set(attr, value)
        if n.tag == f"{{{SVG}}}style" and n.text:
            for cls in classes:
                n.text = re.sub(r"\." + re.escape(cls) + r"(?=[\s{,:.])", "." + prefix + cls, n.text)
    width = height = size
    if name == "oracle":
        # Remove only transparent source padding, preserving the full wordmark.
        node.set("viewBox", "0 52 128 24")
        width, height = size * 1.7, size * 1.7 * 24 / 128
    node.set("x", str(cx - width / 2))
    node.set("y", str(cy - height / 2))
    node.set("width", str(width))
    node.set("height", str(height))
    node.set("preserveAspectRatio", "xMidYMid meet")
    return ET.tostring(node, encoding="unicode")


def write(name, w, h, title, desc, parts):
    result = (f'<svg xmlns="{SVG}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
              f'role="img" aria-labelledby="title desc">\n'
              f'<title id="title">{html.escape(title)}</title>\n'
              f'<desc id="desc">{html.escape(desc)}</desc>\n'
              + "\n".join(parts) + "\n</svg>\n")
    ET.fromstring(result)
    (ASSETS / name).write_text(result, encoding="utf-8")


def databases(theme, t, mobile):
    w, h = (480, 365) if mobile else (960, 222)
    p = [text(24, 28, "RELATIONAL DATABASES", t, 12, 500, muted=True, tracking=1.5),
         line(24, 46, w-24, 46, t)]
    names = [("mysql", "MySQL"), ("sqlite", "SQLite"), ("postgresql", "PostgreSQL"),
             ("sqlserver", "SQL Server"), ("oracle", "Oracle Database")]
    positions = [(80, 104), (240, 104), (400, 104), (160, 263), (320, 263)] if mobile else [
        (104, 117), (292, 117), (480, 117), (668, 117), (856, 117)]
    for (name, label), (x, y) in zip(names, positions):
        if name == "postgresql":
            p.append(rect(x-72, y-44, 144, 132, t, t["selected"], 12))
        p += [logo(name, x, y, 60 if mobile else 66),
              text(x, y+57, label, t, 17 if mobile else 18, 500, anchor="middle")]
        if name == "postgresql":
            p.append(text(x, y+77, "MY LAB", t, 10, 600, anchor="middle", muted=True, tracking=1.6))
    suffix = f"mobile-{theme}" if mobile else theme
    write(f"databases-{suffix}.svg", w, h, "Relational databases — PostgreSQL is my working database",
          "MySQL, SQLite, PostgreSQL, Microsoft SQL Server, and Oracle Database. PostgreSQL is highlighted as the database used in this lab; this lineup is not a proficiency claim.", p)


def stack(theme, t, mobile):
    w, h = (480, 210) if mobile else (960, 225)
    p = [rect(0.5, 0.5, w-1, h-1, t, t["panel"], 14),
         text(26 if mobile else 34, 33, "THE STACK I'M BUILDING TOWARDS", t, 12, 500, muted=True, tracking=1.2)]
    positions = [86, 240, 394] if mobile else [200, 480, 760]
    y = 106 if mobile else 115
    for x, name, label in zip(positions, ["java", "springboot", "postgresql"], ["Java", "Spring Boot", "PostgreSQL"]):
        p += [logo(name, x, y, 62 if mobile else 78),
              text(x, y+64, label, t, 18 if mobile else 20, 500, anchor="middle")]
    for x1, x2 in zip(positions, positions[1:]):
        p.append(text((x1+x2)/2, y+8, "+", t, 28, 300, anchor="middle", muted=True))
    suffix = f"mobile-{theme}" if mobile else theme
    write(f"backend-stack-{suffix}.svg", w, h, "Java + Spring Boot + PostgreSQL",
          "The backend stack I am building towards: Java, Spring Boot, and PostgreSQL. This describes my chosen direction, not a completed application in this repository.", p)


if __name__ == "__main__":
    for theme, colours in THEMES.items():
        for mobile in [False, True]:
            databases(theme, colours, mobile)
            stack(theme, colours, mobile)
    print("Built 8 database-lineup and backend-stack SVG variants.")
