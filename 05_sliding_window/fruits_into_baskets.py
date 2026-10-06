from collections import defaultdict

def total_fruit(fruits: list[int]) -> int:
    left = 0
    max_length = 0
    count = defaultdict(int)

    for right in range(len(fruits)):
        count[fruits[right]] += 1

        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    print(total_fruit([1, 2, 1]))       # 3
    print(total_fruit([0, 1, 2, 2]))    # 3
    print(total_fruit([1, 2, 3, 2, 2])) # 4
    print(total_fruit([]))              # 0
    print(total_fruit([1]))             # 1

# CLARIFICATIONS
# You have two baskets, each can hold only one type of fruit
# Pick fruits from a contiguous section of trees, maximise the number picked
# Equivalent to: longest subarray with at most 2 distinct values

# BRUTE FORCE
# For every pair (i, j), count distinct values in fruits[i:j+1] — nested loop
# Time: O(n^2)   Space: O(1)

# OPTIMISED — Dynamic sliding window with frequency map
# Expand right, add fruit to count map
# When more than 2 distinct types: shrink left, decrement count, delete key when zero
# Window is always the longest valid subarray with at most 2 distinct types
# Time: O(n)   Space: O(1) — count map holds at most 3 keys at any moment
