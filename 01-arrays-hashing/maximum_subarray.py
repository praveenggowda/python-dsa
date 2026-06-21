"""
Problem: Maximum Subarray
LeetCode: 53
Category: Arrays & Hashing
Difficulty: Medium

Problem Statement:
Given an integer array nums, find the subarray with the largest sum and return the sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  ->  Output: 6
Input: nums = [1]                      ->  Output: 1
Input: nums = [5,4,-1,7,8]             ->  Output: 23

Clarifications:
- Array contains at least one element
- Can contain negative numbers
- Must return the sum, not the subarray itself

Brute Force:
Check every subarray and track maximum sum
Time: O(n²)  Space: O(1)

Optimized Approach:
Kadane's algorithm — at each element decide whether to extend current subarray or start fresh
current_sum = max(num, current_sum + num)
Track max_sum throughout

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Kadane's Algorithm
"""

def max_sub_array(nums: list[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_sub_array([1]))                              # 1
print(max_sub_array([5, 4, -1, 7, 8]))                 # 23
print(max_sub_array([-3, -1, -2]))                     # -1
