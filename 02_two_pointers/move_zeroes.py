def move_zeroes(nums: list[int]) -> list[int]:
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    print(move_zeroes([0]))               # [0]
    print(move_zeroes([1, 2, 3]))         # [1, 2, 3]

# CLARIFICATIONS
# Move all zeroes to the end, maintain relative order of non-zero elements
# In-place — do not allocate a new array
# Return the modified array

# BRUTE FORCE
# Collect non-zero elements into a new array, fill remainder with zeroes
# Time: O(n)   Space: O(n)

# OPTIMISED — Same direction two pointers (fast/slow)
# left tracks the next position for a non-zero value
# right scans the full array
# On non-zero: swap nums[left] and nums[right], advance left
# Zeroes naturally accumulate at the back
# Time: O(n)   Space: O(1)
