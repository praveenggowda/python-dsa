"""
Problem: Top K Frequent Elements
LeetCode: 347
Category: Heap / Priority Queue
Difficulty: Medium

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2  ->  Output: [1,2]
Input: nums = [1], k = 1             ->  Output: [1]

Clarifications:
- The answer is guaranteed to be unique
- k is always valid (1 <= k <= number of unique elements)
- Return in any order

Brute Force:
Count frequencies, sort by frequency descending, return first k
Time: O(n log n)  Space: O(n)

Optimized Approach:
Count frequencies with Counter
Use min heap of size k — lowest frequency at top gets kicked out
What remains is the k most frequent elements

Complexity:
Time Complexity: O(n log k)
Space Complexity: O(n + k)

Pattern: HashMap + Min Heap
"""

import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequencies: dict[int, int] = {}
    heap = []
    result = []

    for num in nums:
        if num not in frequencies:
            frequencies[num] = 0
        
        frequencies[num] += 1
    
    for num, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, num))

        if len(heap) > k:
            heapq.heappop(heap)

    for frequency, num in heap:
        result.append(num)
    
    return result

def top_k_frequent_using_counter(nums: list[int], k: int) -> list[int]:
    frequencies: dict[int, int] = {}
    heap = []
    result = []

    for num, frequency in Counter(nums).items():
        heapq.heappush(heap, (frequency, num))

        if len(heap) > k:
            heapq.heappop(heap)

    for frequency, num in heap:
        result.append(num)
    return result

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_k_frequent([1], 1))                   # [1]
print(top_k_frequent([3, 3, 3, 2, 2, 1], 2))  # [3, 2]

print(top_k_frequent_using_counter([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_k_frequent_using_counter([1], 1))                   # [1]
print(top_k_frequent_using_counter([3, 3, 3, 2, 2, 1], 2))  # [3, 2]
