# README artwork

The README uses original product logos beside its section headings. The logos keep their original shapes and colours; GitHub's heading rules provide the visual overlap. The database sketches use transparent canvases and neutral linework, with light/dark and desktop/mobile versions.

## Original artwork

- `chen-{light,dark}.svg` — a lab-book concept in Chen notation: `Topic` contains `Exercise`, with oval attributes and underlined identifiers. The relationship is one-to-many, and each exercise belongs to a topic.
- `erd-{light,dark}.svg` — the relational view of that concept. `Exercise.topic_id` references `Topic.topic_id`; each exercise has its own primary key.
- `eer-{light,dark}.svg` — a separate conceptual study: `WorkItem` has overlapping, partial specializations into `SQLNote` and `DesignNote`.
- Each diagram has a `-mobile-` variant that arranges the same model vertically.

These are README concept sketches, not implemented database schemas or completed SQL exercises. Each SVG includes an accessible title and description, and the README supplies image alternatives.

Notation references: [Mermaid's crow's foot ER reference](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) and the specialization constraints in [King Abdulaziz University's EER teaching slides](https://www.kau.edu.sa/Files/0055554/Subjects/Chapt4-Enhanced%20Entity-Relationship%20and%20UML%20Modeling.pdf).

## Rebuild

The [source](source/build_readme_assets.py) uses **Python's standard library**. It needs no downloads or extra packages:

```sh
python assets/source/build_readme_assets.py
```

This regenerates 12 SVGs: light/dark and desktop/mobile variants of the three diagrams. Typography uses system font fallbacks. Product logos are separate files and are not modified by the generator.

## Logo credits

| Local file | Source |
| :--- | :--- |
| [postgresql.svg](logos/postgresql.svg) | PostgreSQL's Slonik elephant, via [Devicon's PostgreSQL artwork](https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg). [PostgreSQL press resources](https://www.postgresql.org/about/press/). |
| [datagrip.svg](logos/datagrip.svg) | JetBrains DataGrip, via [Devicon's DataGrip artwork](https://github.com/devicons/devicon/blob/master/icons/datagrip/datagrip-original.svg). [JetBrains brand resources](https://www.jetbrains.com/company/brand/). |
| [vscode.svg](logos/vscode.svg) | Microsoft Visual Studio Code. [Official icon archive](https://code.visualstudio.com/assets/branding/visual-studio-code-icons.zip), [brand guidelines](https://code.visualstudio.com/brand). This unmodified local file was reused from the existing [LINUX_LAB asset](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/logos/vscode.svg). |
| [git.svg](logos/git.svg) | Git logo by **Jason Long**, [official source](https://git-scm.com/downloads/logos), under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). This unmodified local file was reused from the existing [LINUX_LAB asset](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/logos/git.svg). |

Devicon's [MIT notice](licenses/devicon-LICENSE.txt) is retained for the two files sourced from that collection. Logos and product names belong to their respective owners and identify the software discussed here.
