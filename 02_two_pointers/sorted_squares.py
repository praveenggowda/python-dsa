def sorted_squares(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    pos = len(nums) - 1
    result = [0] * len(nums)

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq < right_sq:
            result[pos] = right_sq
            right -= 1
        else:
            result[pos] = left_sq
            left += 1

        pos -= 1

    return result


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))    # [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))    # [4, 9, 9, 49, 121]
    print(sorted_squares([0]))                   # [0]
    print(sorted_squares([1]))                   # [1]
    print(sorted_squares([-1]))                  # [1]
    print(sorted_squares([-5, -4, -3, -2, -1])) # [1, 4, 9, 16, 25]
    print(sorted_squares([1, 2, 3, 4, 5]))      # [1, 4, 9, 16, 25]
    print(sorted_squares([-2, -1, 0, 1, 2]))    # [0, 1, 1, 4, 4]
    print(sorted_squares([-3, -3, -2, 1]))      # [1, 4, 9, 9]
    print(sorted_squares([-10_000, 10_000]))    # [100000000, 100000000]


# CLARIFICATIONS
# Input is sorted in non-decreasing order (may contain negatives)
# Return new array of squares in sorted order
# Negatives when squared can be larger than positives

# BRUTE FORCE
# Square each element, then sort
# Time: O(n log n)   Space: O(n)

# OPTIMISED — Opposite ends two pointers, fill from back
# Largest squares are always at the two ends of a sorted array
# Compare left_sq and right_sq, place the larger at pos (back of result)
# Move the pointer with the larger square inward, decrement pos
# Time: O(n)   Space: O(n)
