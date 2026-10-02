from collections import defaultdict

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

def two_sum_all_pairs(nums: list[int], target: int) -> list[list[int]]:
    seen: defaultdict[int, list[int]] = defaultdict(list)
    collect = []

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            for index in seen[complement]:
                collect.append([index, i])

        seen[num].append(i)

    return collect

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]

        if total < target:
            left += 1
        else:
            right -= 1

    return []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))            # [0, 1]
    print(two_sum([3, 2, 4], 6))                 # [1, 2]
    print(two_sum([3, 3], 6))                    # [0, 1]
    print(two_sum([2, 7, 11, 15], 10))           # []
    print(two_sum([], 6))                        # []

    print()

    print(two_sum_all_pairs([1, 3, 2, 3, 4, 1], 4))  # [[0,1],[0,3],[1,5],[3,5]]
    print(two_sum_all_pairs([3, 3], 6))               # [[0,1]]
    print(two_sum_all_pairs([1, 2, 3], 10))           # []

    print()

    print(two_sum_sorted([2, 7, 11, 15], 9))     # [0, 1]
    print(two_sum_sorted([2, 3, 4], 6))          # [0, 2]
    print(two_sum_sorted([3, 3], 6))             # [0, 1]
    print(two_sum_sorted([2, 7, 11, 15], 10))    # []
    print(two_sum_sorted([], 6))                 # []

# CLARIFICATIONS
# Negative numbers allowed
# Empty array → return empty array
# Return indices of the two numbers, not the values
# Duplicates possible

# BRUTE FORCE
# Two nested loops — check every pair
# Time: O(n^2)   Space: O(1)

# OPTIMISED — HashMap (two_sum)
# For each number compute complement = target - num
# If complement already in seen → return [seen[complement], i]
# Otherwise store num → i
# Time: O(n)   Space: O(n)

# VARIANT — All pairs (two_sum_all_pairs)
# Store list of indices per value using defaultdict(list)
# Inner loop over all stored indices of the complement
# Time: O(n^2) worst case (all duplicates)   Space: O(n)

# VARIANT — Sorted input only (two_sum_sorted)
# Opposite ends two pointer — only valid when array is already sorted
# Sorting an unsorted array to use this would scramble original indices
# Time: O(n)   Space: O(1)
