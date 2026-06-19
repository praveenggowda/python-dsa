"""
Problem: Two Sum
LeetCode: 1
Category: Arrays & Hashing
Difficulty: Easy

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. You may assume exactly one solution exists
and you may not use the same element twice.

Examples:
Input: nums = [2,7,11,15], target = 9  ->  Output: [0,1]
Input: nums = [3,2,4], target = 6      ->  Output: [1,2]
Input: nums = [3,3], target = 6        ->  Output: [0,1]

Clarifications:
- Each input has exactly one solution
- Cannot use the same element twice
- Return answer in any order

Brute Force:
Two nested loops, check every pair
Time: O(n²)  Space: O(1)

Optimized Approach:
HashMap storing number -> index
For each number, check if complement (target - num) is already in the dict
If yes, return both indices. If no, store current number and index.

Why this approach?
Single pass. Looking up complement in dict is O(1).

Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Arrays & Hashing
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2,7,11,15], 9)) # [0,1]
print(two_sum([3,2,4], 6))     # [1,2]
print(two_sum([3,3], 6))       # [0,1]
