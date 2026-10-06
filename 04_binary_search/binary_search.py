# Binary Search
# LeetCode 704 - Easy
#
# Problem:
#   Given a sorted array of integers nums and an integer target,
#   return the index of target if it exists.
#   Otherwise, return -1.
#
# Clarifications:
#   - nums is sorted in ascending order
#   - Values are distinct
#   - Return the index, not the value
#   - Return -1 if target is not found
#   - Array can be empty
#
# Examples:
#
# nums = [-1,0,3,5,9,12], target = 9
# Output: 4
#
# nums = [-1,0,3,5,9,12], target = 2
# Output: -1
#
# Brute Force:
#   Loop through every element until target is found.
#
#   Time: O(n)
#   Space: O(1)
#
# Optimised:
#   Since the array is sorted,
#   compare target with the middle element.
#
#   If target < nums[mid]
#       search left half
#
#   If target > nums[mid]
#       search right half
#
#   If target == nums[mid]
#       return mid
#
#   Eliminate half the search space every iteration.
#
#   Time: O(log n)
#   Space: O(1)

def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == "__main__":
    print(binary_search([], 0))                      # expect -1
    print(binary_search([1, 2, 3, 4], 5))            # expect -1
    print(binary_search([1, 3, 5, 7, 9], 3))         # expect 1
    print(binary_search([1, 3, 5, 7, 9, 11, 13], 9)) # expect 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))    # expect 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))    # expect -1
