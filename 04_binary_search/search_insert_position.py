# Search Insert Position
# LeetCode 35 - Easy
#
# Problem:
#   Given a sorted array of distinct integers nums and a target value,
#   return the index if the target is found.
#
#   If the target is not found, return the index where it would be
#   inserted in order while maintaining the sorted order.
#
# Clarifications:
#   - nums is sorted in ascending order
#   - Values are distinct
#   - Return the index, not the value
#   - Array can be empty
#   - Must run in O(log n) time
#
# Examples:
#
# nums = [1,3,5,6], target = 5
# Output: 2
#
# nums = [1,3,5,6], target = 2
# Output: 1
#
# nums = [1,3,5,6], target = 7
# Output: 4
#
# nums = [1,3,5,6], target = 0
# Output: 0
#
# Brute Force:
#   Scan from left to right.
#   Return the first index where nums[i] >= target.
#
#   Time: O(n)
#   Space: O(1)
#
# Optimised (Binary Search):
#   Use binary search to locate the target.
#
#   If target is found:
#       return its index
#
#   If target is not found:
#       return the position where it should be inserted.
#
#   Hint:
#       After the binary search finishes,
#       left will point to the insertion position.
#
#   Time: O(log n)
#   Space: O(1)

def search_insert(nums: list[int], target: int) -> int:
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

    return left

if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 5))  # expect 2
    print(search_insert([1, 3, 5, 6], 2))  # expect 1
    print(search_insert([1, 3, 5, 6], 7))  # expect 4
    print(search_insert([1, 3, 5, 6], 0))  # expect 0
