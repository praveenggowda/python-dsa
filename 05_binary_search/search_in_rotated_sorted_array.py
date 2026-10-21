# Search in Rotated Sorted Array
# LeetCode 33 - Medium
#
# Problem:
#   A sorted array of distinct integers is rotated at an unknown pivot index k.
#   Given the rotated array and a target, return the index of target or -1 if not found.
#   Must run in O(log n) time.
#
# Clarifications:
#   - Values can be negative (-10^4 <= nums[i] <= 10^4)
#   - All values are distinct
#   - Array is always sorted in ascending order before rotation
#   - Return -1 if array is empty or target is not found
#   - Return the index, not the value
#
# Brute Force:
#   Loop through every element and return the index when nums[i] == target.
#   Time: O(n) | Space: O(1)
#
# Optimised (Binary Search):
#   Key insight: when you split a rotated sorted array at mid, one half is ALWAYS sorted.
#   A rotation takes a sorted array and moves the back portion to the front.
#   So at any mid-point, either the left or right side has no wrap-around and stays sorted.
#   Use that guaranteed-sorted half to decide which side the target must be on.
#
#   If left half is sorted (nums[left] <= nums[mid]):
#     - If target is within [nums[left], nums[mid]) -> go left
#     - Else -> go right
#   If right half is sorted:
#     - If target is within (nums[mid], nums[right]] -> go right
#     - Else -> go left
#
#   Time: O(log n) | Space: O(1)

def search_in_rotated_sorted_array(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    print(search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0))  # expect 4
    print(search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3))  # expect -1
    print(search_in_rotated_sorted_array([1], 0))                     # expect -1
    print(search_in_rotated_sorted_array([5, 1, 3], 5))               # expect 0
    print(search_in_rotated_sorted_array([3, 1], 1))                  # expect 1
