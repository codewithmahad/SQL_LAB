-- LeetCode 595: Big Countries
-- Difficulty: Easy
-- Topics: SELECT, WHERE, OR
-- Link: https://leetcode.com/problems/big-countries/

-- Find countries meeting either the area or population threshold.

SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
