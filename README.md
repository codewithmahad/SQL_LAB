<a id="sql_lab"></a>

<div align="center">

<h1>SQL_LAB</h1>

**My SQL lab book.**

Queries, database models, practice attempts, and notes for the next time I need them.

[Lab record](#lab-record) &nbsp; / &nbsp; [Progress](#progress) &nbsp; / &nbsp; [Schema sketchbook](#schema-sketchbook) &nbsp; / &nbsp; [Revision index](#revision-index)

</div>

<br>

I'm **Shaikh Mahad**, a BS Software Engineering student at **UBIT, University of Karachi**, building towards backend development. This repository holds the database side of that work.

I use it to keep my SQL practice organised, track what I've covered, and find my own notes when I need to revise. Over time, I want the files and their history to show how my work improves: the queries I write, the models I design, and the decisions I can explain.

<br>

<a href="https://www.postgresql.org/"><img align="right" src="assets/logos/postgresql.svg" alt="PostgreSQL" width="150"></a>

## Lab record

**Current focus · PostgreSQL fundamentals**

My latest entry covers the database environment and basic expressions. This index points to the work already in the repository; I'll add entries as I study and practise more topics.

<br clear="right">

| Entry | Work recorded | File |
| :--- | :--- | :--- |
| **01 · Environment** | Database, role, schema, and arithmetic expressions. Five read-only statements. | [01_environment.sql](learning/postgresql/01_fundamentals/01_environment.sql) |

## Progress

**Recorded** means there's work in the repo to revisit. **Planned** is still ahead of me.

| Area | Status | Coverage / next work |
| :--- | :--- | :--- |
| PostgreSQL environment | **Recorded** | Connection context and basic `SELECT` expressions. |
| Query fundamentals | Planned | Data types, filtering, sorting, `NULL`, and aggregates. |
| Relationships & modelling | Planned | Keys, joins, subqueries, Chen ER, relational ERD, and EER models. |
| Data integrity | Planned | Constraints, schema decisions, data changes, and transactions. |
| Advanced queries | Planned | CTEs, window functions, views, and PostgreSQL functions. |
| Performance | Planned | Indexes, `EXPLAIN`, execution plans, and query comparisons. |

**Practice queue:** LeetCode SQL 50 and HackerRank SQL. Solutions will join the lab record as I work through them.

## Schema sketchbook

Database design belongs in this lab alongside the SQL. This is where I want to keep models, revisions, and the reasoning behind a schema.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/chen-mobile-dark.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/chen-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/chen-mobile-light.svg">
  <img src="assets/chen-light.svg" alt="Chen ER sketch of the lab book: Topic has a one-to-many contains relationship with Exercise. Attributes appear as ovals and identifiers are underlined." width="100%" loading="lazy">
</picture>

<sub>Lab-book concept sketch · Chen ER · topics and their exercises.</sub>

<details>
<summary><strong>Other modelling views · relational ERD & EER</strong></summary>

<br>

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/erd-mobile-dark.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/erd-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/erd-mobile-light.svg">
  <img src="assets/erd-light.svg" alt="Relational sketch of Topic and Exercise, linked by the topic_id foreign key." width="100%" loading="lazy">
</picture>

<sub>Relational view · Topic and Exercise.</sub>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/eer-mobile-dark.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/eer-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/eer-mobile-light.svg">
  <img src="assets/eer-light.svg" alt="EER sketch of WorkItem with SQLNote and DesignNote subtypes, using overlapping partial specialization." width="100%" loading="lazy">
</picture>

<sub>Conceptual EER view · work items and study notes.</sub>

</details>

<br>

<a href="https://www.jetbrains.com/datagrip/"><img align="right" src="assets/logos/datagrip.svg" alt="JetBrains DataGrip" width="140"></a>

## Working setup

**PostgreSQL** is my main database, with **DataGrip** for SQL work and **VS Code** for repository files and notes. **Git** keeps the history as I add, revisit, and improve entries.

Learning files live under `learning/postgresql/`, with the saved roadmap under `resources/`.

<br clear="right">

<details>
<summary><strong>Repository layout</strong></summary>

```text
SQL_LAB/
├── learning/
│   └── postgresql/
│       └── 01_fundamentals/
│           └── 01_environment.sql
├── resources/
│   └── sql-roadmap.pdf
├── assets/                         # README diagrams and logos
└── README.md                       # Lab index and progress
```

</details>

<br>

<a href="https://code.visualstudio.com/"><img align="right" src="assets/logos/vscode.svg" alt="Visual Studio Code" width="145"></a>

## Revision index

The shortcuts I want when I come back to a topic. As the lab grows, this will link to my worked examples, corrections, and notes from earlier attempts.

**Next revision:** revisit the environment exercise and check that I can explain each result without the comments.

<br clear="right">

| Looking for | Reference |
| :--- | :--- |
| My environment & expression work | [Environment entry](learning/postgresql/01_fundamentals/01_environment.sql) |
| My study roadmap | [SQL roadmap PDF](resources/sql-roadmap.pdf) |
| PostgreSQL syntax & behaviour | [SQL reference](https://www.postgresql.org/docs/current/sql.html) |
| Database, role & schema functions | [Session information functions](https://www.postgresql.org/docs/current/functions-info.html) |
| Planned problem sets | [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) · [HackerRank SQL](https://www.hackerrank.com/domains/sql) |

<br>

<a href="https://git-scm.com/"><img align="right" src="assets/logos/git.svg" alt="Git" width="110"></a>

## Beyond the lab

If something here is useful for your own revision, use it as a reference. Corrections are welcome through an [issue](https://github.com/codewithmahad/SQL_LAB/issues) or pull request.

[**More of my work →**](https://github.com/codewithmahad?tab=repositories)

<br clear="right">

<details>
<summary><code>-- a note to future me</code></summary>

```text
brain cache expired.
restoring from SQL_LAB...
```

</details>

<sub>Shaikh Mahad · BSSE, UBIT &nbsp; / &nbsp; <a href="assets/README.md">Artwork credits</a> &nbsp; / &nbsp; <a href="#sql_lab">Back to top ↑</a></sub>
