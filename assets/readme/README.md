# README artwork

Compact artwork for SQL_LAB, with PostgreSQL blue (`#336791`) and neutral ink. Dark variants use a lighter blue for legibility. The title and small key sketch have light and dark versions; the filtering illustration also has a vertical layout for narrow screens.

| File | Purpose |
| :--- | :--- |
| `sql-title-{light,dark}.svg` | The lab title in Consolas with system monospace fallbacks. |
| `relations-{light,dark}.svg` | A conceptual link between `Topic.topic_id` and `Exercise.topic_id`, marked as primary and foreign keys. The arrow identifies the matching fields; it does not encode cardinality. |
| `filter-{light,dark}.svg` | A worked reading of the saved LeetCode 1757 query: its conditions, four illustrative input rows, and matching product IDs. |
| `filter-mobile-{light,dark}.svg` | The same query, input, and result arranged vertically. |

The filtering illustration uses the exact conditions from [1757_recyclable_and_low_fat_products.sql](../../practice/leetcode-sql-50/01_select/1757_recyclable_and_low_fat_products.sql). Its rows are illustrative, not a captured database run or a LeetCode submission. IDs 1 and 3 match both flags. Their displayed order is for explanation; SQL does not promise result order without [`ORDER BY`](https://www.postgresql.org/docs/current/queries-order.html).

Rebuild these eight assets from the repository root:

```sh
python assets/source/build_readme_identity.py
```

The [generator](../source/build_readme_identity.py) uses only Python's standard library. Generated SVGs have accessible titles and descriptions, system font fallbacks, and no scripts, font downloads, or external resources.

## Shared learning links

The closing section uses 20-pixel inline links to Java, DSA, and Linux. Its heading and compact footer match the other learning labs, while the paragraph describes SQL_LAB's role in query practice and relational design. The button artwork is reused unchanged from [DSA_LAB](https://github.com/codewithmahad/DSA_LAB). SQL problem-set links stay with the practice references; the personal coding-profile row belongs in DSA_LAB.

- **Java:** the coffee-cup geometry comes from [Devicon](https://github.com/devicons/devicon/blob/master/icons/java/java-original.svg), adapted to JAVA_LAB's blue and orange. Lettering follows [JAVA_LAB's title](https://github.com/codewithmahad/JAVA_LAB).
- **SQL:** the PostgreSQL elephant comes from [Devicon](https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg). The header uses the existing, unmodified [local logo](../logos/postgresql.svg).
- **DSA:** the original orange search tree and lettering come from [DSA_LAB](https://github.com/codewithmahad/DSA_LAB).
- **Linux:** the buttons embed **Tux, by Larry Ewing, created using The GIMP**. [Original artwork and reuse terms](http://isc.tamu.edu/~lewing/linux/) · [LINUX_LAB's source notes](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/README.md#tux).
- **LeetCode, HackerRank, and Codolio:** the profile buttons retain the platform graphics and outlined lettering from the [profile README artwork](https://github.com/codewithmahad/codewithmahad/tree/main/assets/profile/contact), as reused in DSA_LAB.

The existing [Devicon MIT notice](../licenses/devicon-LICENSE.txt) covers the Java and PostgreSQL source artwork. Product and platform names and marks belong to their respective owners.

[All artwork and logo credits](../README.md) · [Back to SQL_LAB](../../README.md)
