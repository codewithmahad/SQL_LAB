-- LeetCode 584: Find Customer Referee
-- Difficulty: Easy
-- Topics: WHERE, OR, NULL
-- Link: https://leetcode.com/problems/find-customer-referee/

-- Exclude customers referred by ID 2 while retaining customers
-- whose referee_id is NULL.

SELECT name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;
