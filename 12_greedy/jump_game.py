# Problem: Jump Game
# Given an array of non-negative integers, each element represents the maximum
# number of steps you can jump forward from that position. Starting at index 0,
# determine if you can reach the last index.
#
# Example: [2, 3, 1, 1, 4] -> True
# Example: [3, 2, 1, 0, 4] -> False (always land on index 3 which is 0)
#
# Approach: greedy — track the furthest reachable index as you scan left to right.
# If current index exceeds the furthest reachable, return False.
# Time O(N), Space O(1)

def jump_game(nums: list[int]) -> bool:
    furthest = 0

    for (i, num) in enumerate(nums):
        if i > furthest:
            return False

        furthest = max(furthest, i + num)

    return True


if __name__ == "__main__":
    print(jump_game([2, 3, 1, 1, 4]))   # True
    print(jump_game([3, 2, 1, 0, 4]))   # False
    print(jump_game([0]))               # True (already at last index)
    print(jump_game([1, 0, 0]))         # False
