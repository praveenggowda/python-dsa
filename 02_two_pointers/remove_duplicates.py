def remove_duplicates(nums: list[int]) -> int:
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left

if __name__ == "__main__":
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    print(nums1[:k1])  # [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = remove_duplicates(nums2)
    print(nums2[:k2])  # [0, 1, 2, 3, 4]

# CLARIFICATIONS
# Input array is sorted — duplicates are always adjacent
# Remove duplicates in-place, maintain relative order
# Return k — the count of unique elements
# Caller reads nums[0:k], the tail is ignored

# BRUTE FORCE
# Use a set to track seen values, rebuild array
# Time: O(n)   Space: O(n)

# OPTIMISED — Same direction two pointers (fast/slow)
# left starts at 1 — position for next unique value
# right scans from 1, compares to previous element (works because sorted)
# On new value: write to nums[left], advance left
# Return left as the unique element count
# Time: O(n)   Space: O(1)
