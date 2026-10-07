# Permutations — LeetCode 46 (Medium)
# Category: Backtracking
#
# Problem:
#   Given an array nums of distinct integers, return all possible permutations.
#   You can return the answer in any order.
#
# Clarifications:
#   - All integers are unique — no duplicate handling needed
#   - Numbers can be positive or negative
#   - Constraints guarantee at least one element — no empty array check needed
#   - 1 <= nums.length <= 6
#
# Backtracking template:
#   def backtrack(current, remaining):
#       if base case (current is complete):
#           add current.copy() to results
#           return
#       for choice in remaining:
#           current.append(choice)
#           backtrack(current, remaining without choice)
#           current.pop()
#
# Example:
#   nums = [1, 2, 3]
#   [] → pick 1 → [1] → pick 2 → [1,2] → pick 3 → [1,2,3] ✓
#                                        → backtrack → [1,2]
#                      → pick 3 → [1,3] → pick 2 → [1,3,2] ✓
#                                        → backtrack → [1,3]
#        → pick 2 → [2] → ...and so on
#
# Time:  O(n * n!)  — n! permutations, each takes O(n) to copy
# Space: O(n)       — recursion depth is n


def permutations(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(current, remaining):
        if len(current) == len(nums):
            result.append(current.copy())
            return

        for choice in remaining:
            current.append(choice)
            backtrack(current, [n for n in remaining if n != choice])
            current.pop()

    backtrack([], nums)
    return result

if __name__ == "__main__":
    print(permutations([1, 2, 3]))  # expected: 6 permutations
    print(permutations([0, 1]))     # expected: [[0,1],[1,0]]
    print(permutations([1]))        # expected: [[1]]
