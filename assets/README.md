# README artwork

The README uses original product logos beside its section headings and in two database/stack compositions. The logos keep their original shapes and colours; GitHub's heading rules provide the visual overlap beside sections. All generated artwork has light/dark and desktop/mobile versions.

## Original artwork

- `databases-{light,dark}.svg` — MySQL, SQLite, PostgreSQL, Microsoft SQL Server, and Oracle Database, with PostgreSQL highlighted as the working database. This is context for the database choice, not a claim of proficiency in all five.
- `backend-stack-{light,dark}.svg` — Java + Spring Boot + PostgreSQL, shown inside the database-choice dropdown as a future backend direction.
- `chen-{light,dark}.svg` — a lab-book concept in Chen notation: `Topic` contains `Exercise`, with oval attributes and underlined identifiers. The relationship is one-to-many, and each exercise belongs to a topic.
- `erd-{light,dark}.svg` — the relational view of that concept. `Exercise.topic_id` references `Topic.topic_id`; each exercise has its own primary key.
- `eer-{light,dark}.svg` — a separate conceptual study: `WorkItem` has overlapping, partial specializations into `SQLNote` and `DesignNote`.
- Each asset has a `-mobile-` variant with a layout suited to narrow screens.

These are README concept sketches, not implemented database schemas or completed SQL exercises. Each SVG includes an accessible title and description, and the README supplies image alternatives.

Notation references: [Mermaid's crow's foot ER reference](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) and the specialization constraints in [King Abdulaziz University's EER teaching slides](https://www.kau.edu.sa/Files/0055554/Subjects/Chapt4-Enhanced%20Entity-Relationship%20and%20UML%20Modeling.pdf).

## Rebuild

Both generators use **Python's standard library**. The [diagram generator](source/build_readme_assets.py) draws the models; the [banner generator](source/build_readme_banners.py) also reads the credited local logos. They need no downloads or extra packages:

```sh
python assets/source/build_readme_assets.py
python assets/source/build_readme_banners.py
```

This regenerates 20 SVGs: 12 diagram variants and 8 database-lineup/stack variants. Typography uses system font fallbacks. Logo originals stay unchanged. Embedded copies have isolated SVG IDs and CSS classes to avoid collisions, and Oracle's transparent outer padding is cropped without changing the wordmark. The generated SVGs are self-contained and load no remote resources.

## Logo credits

| Local file | Source |
| :--- | :--- |
| [postgresql.svg](logos/postgresql.svg) | PostgreSQL's Slonik elephant, via [Devicon's PostgreSQL artwork](https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg). [PostgreSQL press resources](https://www.postgresql.org/about/press/). |
| [datagrip.svg](logos/datagrip.svg) | JetBrains DataGrip, via [Devicon's DataGrip artwork](https://github.com/devicons/devicon/blob/master/icons/datagrip/datagrip-original.svg). [JetBrains brand resources](https://www.jetbrains.com/company/brand/). |
| [vscode.svg](logos/vscode.svg) | Microsoft Visual Studio Code. [Official icon archive](https://code.visualstudio.com/assets/branding/visual-studio-code-icons.zip), [brand guidelines](https://code.visualstudio.com/brand). This unmodified local file was reused from the existing [LINUX_LAB asset](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/logos/vscode.svg). |
| [git.svg](logos/git.svg) | Git logo by **Jason Long**, [official source](https://git-scm.com/downloads/logos), under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). This unmodified local file was reused from the existing [LINUX_LAB asset](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/logos/git.svg). |
| [mysql.svg](logos/mysql.svg) | MySQL dolphin, via [Devicon's original artwork](https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original.svg). |
| [sqlite.svg](logos/sqlite.svg) | SQLite, via [Devicon's original artwork](https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg). |
| [sqlserver.svg](logos/sqlserver.svg) | Microsoft SQL Server, via [Devicon's original artwork](https://github.com/devicons/devicon/blob/master/icons/microsoftsqlserver/microsoftsqlserver-original.svg). |
| [oracle.svg](logos/oracle.svg) | Oracle wordmark, via [Devicon's original artwork](https://github.com/devicons/devicon/blob/master/icons/oracle/oracle-original.svg). |
| [java.svg](logos/java.svg) | Java, via [Devicon's original artwork](https://github.com/devicons/devicon/blob/master/icons/java/java-original.svg). |
| [springboot.svg](logos/springboot.svg) | Spring Boot's official [project icon](https://spring.io/img/projects/spring-boot.svg). [Spring trademark guidelines](https://spring.io/trademarks/). Spring is a trademark of Broadcom Inc. and/or its subsidiaries. |

Devicon's [MIT notice](licenses/devicon-LICENSE.txt) is retained for the seven files sourced from that collection. Logos and product names belong to their respective owners and identify the software discussed here.
