# PostgreSQL learning queries

Start with [01_environment.sql](01_fundamentals/01_environment.sql). It contains five read-only `SELECT` statements and needs no sample tables or data.

## Before running

- Have a running [PostgreSQL server](https://www.postgresql.org/download/) and an existing practice database you can connect to.
- Use DataGrip or the PostgreSQL `psql` command-line client.
- Know your connection's host, port, database name, and role. Keep passwords out of repository files.

The database name in the SQL file's header describes the original practice setup. The queries use whichever database you connect to; they do not create one.

## Run with DataGrip

1. Attach the `SQL_LAB` folder to your DataGrip project and open `learning/postgresql/01_fundamentals/01_environment.sql`.
2. Select the PostgreSQL data source for your existing practice database in the editor's data source selector.
3. Select one statement and press `Ctrl+Enter`. Confirm the selected statement if DataGrip shows a chooser. Repeat for the remaining statements.
4. Compare the results with the table below.

See [DataGrip's query execution guide](https://www.jetbrains.com/help/datagrip/run-a-query.html) for other keymaps and execution options.

## Run with psql (optional)

From the repository root, replace every `YOUR_...` placeholder with your connection details:

```sh
psql -X --set=ON_ERROR_STOP=on -h "YOUR_HOST" -p "YOUR_PORT" -U "YOUR_ROLE" -d "YOUR_DATABASE" -f "learning/postgresql/01_fundamentals/01_environment.sql"
```

`psql` must be on your `PATH`. Enter a password if prompted. `-X` skips psql startup files, `ON_ERROR_STOP` stops script processing on an error, and `-f` reads the SQL file. See the [psql reference](https://www.postgresql.org/docs/current/app-psql.html).

## What to check

| Result column | Expected result |
| :--- | :--- |
| `database_name` | The database you connected to. |
| `database_user` | The current role used by the session. |
| `schema_name` | The first existing schema in the search path, or `NULL` if none exists. |
| `result` | `30` |
| `total_price` | `5300` |

## LeetCode practice

The files under [practice/leetcode-sql-50](../../practice/leetcode-sql-50/) use problem-specific tables provided by LeetCode. Open the problem link in a solution's header and use LeetCode's PostgreSQL editor to run or submit it. Those tables are not set up by this environment exercise.

Saving or inspecting a solution here does not establish LeetCode acceptance.
