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

The closing section has a paragraph specific to the host repository, a row of links to the other three labs, a short practice-profile line, and the LeetCode, HackerRank, and Codolio buttons. The lab and profile buttons are 40 pixels high.

The lab buttons use one solid pale fill each: Java white, DSA amber, PostgreSQL blue, and Linux silver. Their Segoe UI Semibold labels are converted to paths and vertically centered by their actual glyph bounds. Icon and label groups are centered together. The paired light/dark filenames use the same solid palette so the links stay consistent in both themes.

- **Java:** the Devicon coffee-cup geometry, adapted to Java.com blue and orange.
- **DSA:** an original orange search-tree symbol.
- **SQL:** the original Devicon PostgreSQL elephant.
- **Linux:** unchanged **Tux, by Larry Ewing, created using The GIMP**. [Original artwork and reuse terms](http://isc.tamu.edu/~lewing/linux/) · [LINUX_LAB source notes](https://github.com/codewithmahad/LINUX_LAB/blob/main/assets/README.md#tux).

The existing [Devicon MIT notice](../licenses/devicon-LICENSE.txt) covers the Java and PostgreSQL source artwork. The coding-profile buttons retain the original platform graphics from [my profile artwork](https://github.com/codewithmahad/codewithmahad/tree/main/assets/profile/contact).

[All artwork and logo credits](../README.md) · [Back to SQL_LAB](../../README.md)


The connected-labs title is a normal section heading. Lab buttons use black text on light fills; Java has a white background and a larger coffee-cup mark, SQL uses a stronger blue, and DSA has black branches and secondary-node outlines around orange centers. The social-button content is enlarged by 15% inside the same 40-pixel height, with wider backgrounds to preserve its proportions.
