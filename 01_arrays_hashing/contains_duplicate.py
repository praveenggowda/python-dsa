"""
Problem: Contains Duplicate
LeetCode: 217
Category: Arrays & Hashing
Difficulty: Easy

Problem Statement:
Given an integer array nums, return true if any value appears at least twice
in the array, and false if every element is distinct.

Examples:
Input: nums = [1,2,3,1]             ->  Output: True
Input: nums = [1,2,3,4]             ->  Output: False
Input: nums = [1,1,1,3,3,4,3,2,4,2] ->  Output: True

Clarifications:
- Negative numbers allowed
- Empty array -> False

Brute Force:
Two nested loops, compare every pair
Time: O(n²)  Space: O(1)

Optimized Approach:
HashSet — add each number, if already exists return True

Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Arrays & Hashing
"""

def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num) 
    
    return False    

print(contains_duplicate([1, 2, 3, 1]))                     # True
print(contains_duplicate([1, 2, 3, 4]))                     # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))   # True
print(contains_duplicate([]))                               # False
