-- LeetCode 1683: Invalid Tweets
-- Difficulty: Easy
-- Topics: SELECT, WHERE, LENGTH
-- Link: https://leetcode.com/problems/invalid-tweets/

-- Identify tweets containing more than 15 characters.

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
