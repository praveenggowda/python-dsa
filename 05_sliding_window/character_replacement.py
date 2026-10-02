from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    left = 0
    max_length = 0
    count = defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1

        window_size = right - left + 1
        max_freq = max(count.values())
        replacement_needed = window_size - max_freq

        while replacement_needed > k:
            count[s[left]] -= 1
            left += 1
            window_size = right - left + 1
            max_freq = max(count.values())
            replacement_needed = window_size - max_freq

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))    # 4
    print(character_replacement("AABABBA", 1)) # 4
    print(character_replacement("AAAA", 2))    # 4
    print(character_replacement("A", 0))       # 1


# CLARIFICATIONS
# You can replace at most k characters in the string
# Find the length of the longest substring where all characters are the same after replacements
# Only uppercase English letters

# BRUTE FORCE
# For every pair (i, j), count the most frequent character — replacements needed = length - max_freq
# If replacements <= k the window is valid, track the max length
# Time: O(n^2)   Space: O(1)

# OPTIMISED — Dynamic sliding window with frequency map
# Key insight: replacements needed = window_size - max_freq (characters that are not the dominant one)
# Expand right, add to count, recalculate max_freq and replacements needed
# If replacements_needed > k: shrink from left until window is valid again
# max(count.values()) recalculates max_freq each shrink step — O(alphabet) per step, O(n) overall
# Time: O(n)   Space: O(1) — at most 26 keys in count
