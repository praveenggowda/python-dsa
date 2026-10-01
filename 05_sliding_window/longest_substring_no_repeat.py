def longest_substring_no_repeat_set(s: str) -> int:
    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def longest_substring_no_repeat_map(s: str) -> int:
    left = 0
    seen = {}
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    for fn in [longest_substring_no_repeat_set, longest_substring_no_repeat_map]:
        print(fn("abcabcbb"))  # 3
        print(fn("bbbbb"))     # 1
        print(fn("pwwkew"))    # 3
        print(fn(""))          # 0
        print(fn(" "))         # 1
        print(fn("abba"))      # 2
        print("---")


# CLARIFICATIONS
# Return the length of the longest substring with no repeated characters
# Empty string returns 0
# Spaces and special characters count as valid characters

# BRUTE FORCE
# For every pair (i, j), check if s[i:j] has all unique characters using a set
# Time: O(n^2)   Space: O(n)

# OPTIMISED v1 — Dynamic sliding window with set
# Expand right, if duplicate found shrink left one step at a time until clear
# Each character is added and removed at most once — O(n) amortized
# Time: O(n)   Space: O(min(n, alphabet))

# OPTIMISED v2 — Dynamic sliding window with hashmap (no inner loop)
# Store last seen index of each character
# On duplicate: jump left directly to seen[char] + 1, skipping intermediate steps
# Guard seen[char] >= left prevents jumping backward outside the current window
# Time: O(n)   Space: O(min(n, alphabet))
