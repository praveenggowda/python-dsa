# House Robber — LeetCode 102 (Medium)
# Category: 1D Dynamic Programming
#
# Problem:
#   Given an array of non-negative integers representing money in each house,
#   return the maximum amount you can rob without robbing two adjacent houses.
#
# Clarifications:
#   - Cannot rob two directly adjacent houses
#   - CAN skip multiple consecutive houses — you are not forced to alternate
#   - All values are non-negative (0 to 400)
#   - Array length: 1 to 100
#   - Single house: rob it, return nums[0]
#   - Two houses: return max(nums[0], nums[1])
#
# Key insight:
#   At every house, two choices:
#     Rob it:  best[i-2] + nums[i]
#     Skip it: best[i-1]
#   Take the max of the two.
#
# Example:
#   nums = [2, 7, 9, 3, 1]
#   i=0: best = 2
#   i=1: max(0+7=7, 2) = 7
#   i=2: max(2+9=11, 7) = 11
#   i=3: max(7+3=10, 11) = 11
#   i=4: max(11+1=12, 11) = 12
#   Output: 12
#
# Time:  O(n)
# Space: O(1) — only two variables needed, not a full array
from unittest import skip

def house_robber(nums: list[int]) -> int:
    prev2 = 0
    prev1 = 0

    for num in nums:
        current = max(prev2 + num, prev1)
        prev2 = prev1
        prev1 = current

    return prev1

if __name__ == "__main__":
    print(house_robber([1, 2, 3, 1]))       # expected: 4
    print(house_robber([2, 7, 9, 3, 1]))    # expected: 12
    print(house_robber([1, 4, 1]))          # expected: 4
    print(house_robber([2, 1, 1, 2]))       # expected: 4
    print(house_robber([5]))                # expected: 5
    print(house_robber([2, 7]))             # expected: 7
