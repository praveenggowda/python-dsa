def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
    print(longest_ones([0, 0, 1, 1, 1, 0, 0], 0))               # 3
    print(longest_ones([1, 1, 1, 1], 2))                         # 4
    print(longest_ones([0, 0, 0, 0], 2))                         # 2
    print(longest_ones([1, 0, 1, 0, 1, 0, 1], 1))               # 3
    print(longest_ones([], 2))                                   # 0

# CLARIFICATIONS
# Binary array of 0s and 1s
# Can flip at most k zeros to ones
# Return the length of the longest subarray of 1s after at most k flips

# BRUTE FORCE
# For every pair (i, j), count zeros in nums[i:j+1] — if zero_count <= k the window is valid
# Time: O(n^2)   Space: O(1)

# OPTIMISED — Dynamic sliding window with zero counter
# Track zero_count as right expands
# When zero_count > k: shrink from left, decrement zero_count only when left passes a zero
# No frequency map needed — zeros are binary so a single counter is enough
# Time: O(n)   Space: O(1)
