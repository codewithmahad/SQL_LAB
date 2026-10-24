-- LeetCode 1757: Recyclable and Low Fat Products
-- Difficulty: Easy
-- Topics: SELECT, WHERE, AND
-- Link: https://leetcode.com/problems/recyclable-and-low-fat-products/

-- Return product IDs where both low_fats and recyclable are 'Y'.

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';
