def maximum_sum(nums: list[int], k: int) -> int:
    left = 0
    max_sum = float('-inf')
    window_sum = 0

    if k <= 0 or len(nums) < k:
        return 0

    for right in range(len(nums)):
        window_size = right - left + 1
        window_sum += nums[right]

        if window_size == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1

    return max_sum

if __name__ == "__main__":
    print(maximum_sum([2, 1, 5, 1, 3, 2], 3))  # 9
    print(maximum_sum([2, 3, 4, 1, 5], 2))     # 7
    print(maximum_sum([-3, -1, -2], 2))        # -1
    print(maximum_sum([2, 3], 3))              # 0
    print(maximum_sum([], 0))                  # 0


# CLARIFICATIONS
# k <= 0 or len(nums) < k: return 0 — no valid window exists
# Array can contain negative numbers — max_sum starts at -inf not 0
# Returns the maximum sum across all windows of exactly size k

# BRUTE FORCE
# For each starting index i, compute sum of nums[i:i+k] — nested loop
# Time: O(n * k)   Space: O(1)

# OPTIMISED — Fixed sliding window
# Window of exactly k elements slides from left to right
# Add nums[right] when entering, subtract nums[left] when leaving
# Each element is added once and removed once
# Time: O(n)   Space: O(1)
