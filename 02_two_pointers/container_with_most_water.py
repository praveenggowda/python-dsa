"""
Problem: Container With Most Water
LeetCode: 11
Category: Two Pointers
Difficulty: Medium

Problem Statement:
Given an integer array heights where heights[i] represents the height of a vertical line,
find two lines that together with the x-axis form a container that holds the most water.

Examples:
Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: heights = []
Output: -1

Clarifications:
- No negative numbers
- Return -1 for empty input
- Area = min(height[left], height[right]) * (right - left)

Optimised Approach:
Two pointers starting at both ends. Move the pointer on the shorter side inward —
moving the taller side can only decrease width without any guarantee of taller height.

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Two Pointers
"""


def most_water_container(heights: list[int]) -> int:
    if not heights:
        return -1

    right = len(heights) - 1
    left = 0
    max_area = 0

    while left < right:
        height = min(heights[left], heights[right])
        distance = right - left
        area = height * distance

        if area > max_area:
            max_area = area

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(most_water_container([]))
print(most_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))
