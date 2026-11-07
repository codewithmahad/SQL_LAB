"""Build SQL_LAB's title and query illustrations using the standard library."""

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "readme"
FONT = "'Segoe UI', Arial, sans-serif"
MONO = "Consolas, 'Liberation Mono', monospace"
PALETTES = {
    "light": {"ink": "#1f2328", "muted": "#59636e", "line": "#b7c7d5", "blue": "#336791", "wash": "#edf4fa", "paper": "#ffffff"},
    "dark": {"ink": "#e6edf3", "muted": "#a3b3c2", "line": "#43586a", "blue": "#8bbce3", "wash": "#182d40", "paper": "#0d1117"},
}


def text(x, y, value, fill, size=18, weight=400, mono=False, anchor="start"):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'


def line(x1, y1, x2, y2, color, width=1):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"/>'


def write(name, width, height, title, desc, body):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" preserveAspectRatio="xMinYMid meet" role="img" aria-labelledby="title desc">\n<title id="title">{escape(title)}</title>\n<desc id="desc">{escape(desc)}</desc>\n' + "\n".join(body) + "\n</svg>\n"
    (OUT / name).write_text(svg, encoding="utf-8", newline="\n")


def title(theme, c):
    body = [f'<text x="0" y="49" font-family="{MONO}" font-size="52" font-weight="700" letter-spacing="-1"><tspan fill="{c["blue"]}">SQL</tspan><tspan fill="{c["ink"]}">_LAB</tspan></text>']
    write(f"sql-title-{theme}.svg", 230, 64, "SQL_LAB", "SQL in PostgreSQL blue, with LAB in neutral ink.", body)


def relations(theme, c):
    body = []
    for x, y, label, kind, value in [(6, 12, "Topic", "PK", "topic_id"), (102, 76, "Exercise", "FK", "topic_id")]:
        body += [f'<rect x="{x}" y="{y}" width="126" height="62" rx="5" fill="{c["paper"]}" stroke="{c["line"]}" stroke-width="1.5"/>',
                 text(x + 10, y + 21, label, c["ink"], 18, 600),
                 line(x, y + 29, x + 126, y + 29, c["line"]),
                 text(x + 10, y + 49, kind, c["blue"], 12, 700, mono=True),
                 text(x + 34, y + 49, value, c["muted"], 14, mono=True)]
    body += [f'<path d="M132 59H240V125H228M235 118L228 125L235 132" fill="none" stroke="{c["blue"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>']
    write(f"relations-{theme}.svg", 248, 146, "Primary key to foreign key", "Concept sketch: Topic.topic_id is a primary key referenced by Exercise.topic_id. The arrow indicates the matching key fields, not relationship cardinality.", body)


def label(body, x, y, number, name, c):
    body.extend([text(x, y, number, c["blue"], 14, 700, mono=True), text(x + 34, y, name, c["ink"], 21, 600)])


def query(body, x, y, c, size=19):
    for i, (keyword, rest) in enumerate([("SELECT", " product_id"), ("FROM", " Products"), ("WHERE", " low_fats = 'Y'"), ("  AND", " recyclable = 'Y';")]):
        body.append(f'<text x="{x}" y="{y + i * 30}" fill="{c["ink"]}" font-family="{MONO}" font-size="{size}" xml:space="preserve"><tspan fill="{c["blue"]}" font-weight="700">{escape(keyword)}</tspan><tspan>{escape(rest)}</tspan></text>')


def products(body, x, y, c, mobile=False):
    # Both required Y values are present only in illustrative rows 1 and 3.
    widths = [0, 112, 196, 302] if not mobile else [0, 120, 214, 330]
    centers = [(widths[i] + widths[i + 1]) / 2 for i in range(3)]
    for cx, name in zip(centers, ["product_id", "low_fats", "recyclable"]):
        body.append(text(x + cx, y, name, c["muted"], 14 if not mobile else 16, 600, mono=True, anchor="middle"))
    body.append(line(x, y + 13, x + widths[-1], y + 13, c["line"]))
    for i, row in enumerate([(0, "Y", "N"), (1, "Y", "Y"), (2, "N", "Y"), (3, "Y", "Y")]):
        baseline = y + 41 + i * 34
        if row[0] in (1, 3):
            body.append(f'<rect x="{x}" y="{baseline - 23}" width="{widths[-1]}" height="32" rx="4" fill="{c["wash"]}"/>')
        for cx, value in zip(centers, row):
            body.append(text(x + cx, baseline, str(value), c["blue"] if row[0] in (1, 3) else c["muted"], 19, 600 if row[0] in (1, 3) else 400, mono=True, anchor="middle"))


def result(body, x, y, c):
    body += [text(x, y, "product_id", c["muted"], 16, 600, mono=True), line(x, y + 13, x + 118, y + 13, c["line"])]
    for i, value in enumerate(["1", "3"]):
        body.append(text(x + 58, y + 43 + i * 34, value, c["blue"], 23, 700, mono=True, anchor="middle"))


def filtering(theme, c, mobile=False):
    body = []
    if mobile:
        label(body, 12, 28, "01", "Write the conditions", c)
        query(body, 12, 65, c, size=20)
        body += [line(12, 179, 342, 179, c["line"])]
        label(body, 12, 216, "02", "Check the input rows", c)
        products(body, 12, 254, c, mobile=True)
        body += [line(12, 419, 342, 419, c["line"])]
        label(body, 12, 456, "03", "Keep both matches", c)
        result(body, 12, 495, c)
        body += [text(158, 539, "low_fats = Y", c["muted"], 17, mono=True), text(158, 569, "recyclable = Y", c["muted"], 17, mono=True)]
        width, height = 354, 590
    else:
        label(body, 12, 28, "01", "Write the conditions", c)
        label(body, 383, 28, "02", "Check the input rows", c)
        label(body, 771, 28, "03", "Keep both matches", c)
        query(body, 12, 88, c)
        products(body, 383, 69, c)
        result(body, 771, 69, c)
        body += [line(352, 50, 352, 221, c["line"]), line(737, 50, 737, 221, c["line"]), text(771, 197, "AND: both are Y", c["muted"], 17)]
        width, height = 996, 230
    write(f'filter-{"mobile-" if mobile else ""}{theme}.svg', width, height, "AND filtering: query, input, result", "A worked illustration of LeetCode 1757. Products with IDs 0, 1, 2, and 3 have flag pairs Y/N, Y/Y, N/Y, and Y/Y. The saved query requires low_fats = 'Y' AND recyclable = 'Y' and returns IDs 1 and 3. Rows are illustrative; result order is unspecified.", body)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for theme, colors in PALETTES.items():
        title(theme, colors)
        relations(theme, colors)
        filtering(theme, colors)
        filtering(theme, colors, mobile=True)
    print("Built 8 title and query SVGs in assets/readme/.")
