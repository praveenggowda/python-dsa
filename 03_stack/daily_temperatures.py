"""
Problem: Daily Temperatures
LeetCode: 739
Category: Stack
Difficulty: Medium

Problem Statement:
Given an array of integers temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get
a warmer temperature. If there is no future warmer day, answer[i] == 0.

Examples:
Input: temperatures = [73,74,75,71,69,72,76,73]  ->  Output: [1,1,4,2,1,1,0,0]
Input: temperatures = [30,40,50,60]               ->  Output: [1,1,1,0]
Input: temperatures = [30,60,90]                  ->  Output: [1,1,0]

Clarifications:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
- Answer is 0 if no warmer day exists

Brute Force:
For each day, scan forward until a warmer day is found.
Time Complexity: O(n^2)
Space Complexity: O(1)

Optimized Approach:
Use a monotonic decreasing stack of indices.
Stack holds indices of days still waiting for a warmer day.
When a warmer temperature arrives, pop all cooler days and record the gap.

Complexity:
Time Complexity: O(n) — each index pushed and popped at most once
Space Complexity: O(n)

Pattern: Monotonic Stack
"""

from collections import deque

def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = deque()
    answer = [0] * len(temperatures)

    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    return answer

if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30, 40, 50, 60]))                   # [1,1,1,0]
    print(daily_temperatures([30, 60, 90]))                       # [1,1,0]
