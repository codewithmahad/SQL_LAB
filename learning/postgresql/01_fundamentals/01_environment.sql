
-- Topic: PostgreSQL environment and basic SELECT
-- Database: backend_sql_lab
-- Purpose: Safe, read-only practice queries

-- Identify the connected database.
SELECT current_database() AS database_name;

-- Identify the database role used by this session.
SELECT current_user AS database_user;

-- Identify the first existing schema in the search path.
SELECT current_schema() AS schema_name;

-- Evaluate a simple arithmetic expression.
SELECT 10 + 20 AS result;

-- Calculate the combined price of two items.
SELECT 3500 + 1800 AS total_price;
    