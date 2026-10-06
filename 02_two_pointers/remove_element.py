def remove_element(nums: list[int], val: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] != val:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[right] == val:
            right -= 1

    return left

if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    k1 = remove_element(nums1, 3)
    print(nums1[:k1])  # [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = remove_element(nums2, 2)
    print(nums2[:k2])  # [0, 1, 4, 0, 3]

    nums3 = [3, 3]
    k3 = remove_element(nums3, 3)
    print(nums3[:k3])  # []

# CLARIFICATIONS
# Remove all occurrences of val in-place
# Return k — the count of elements not equal to val
# Caller reads nums[0:k], the tail is ignored
# Array is not necessarily sorted

# BRUTE FORCE
# Collect non-val elements into a new array, copy back
# Time: O(n)   Space: O(n)

# OPTIMISED — Opposite ends two pointers
# left scans from start, right scans from end
# On non-val at left: advance left
# On val at left: swap with right (moves val to the back), do not advance left yet
# Shrink right whenever nums[right] is val
# Use left <= right to ensure the element at the meeting point is also processed
# Return left as count of non-val elements
# Time: O(n)   Space: O(1)
