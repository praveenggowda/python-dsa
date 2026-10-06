from collections import defaultdict

def find_anagrams(s: str, p: str) -> list[int]:
    target = defaultdict(int)
    window = defaultdict(int)
    left = 0
    output: list[int] = []

    for char in p:
        target[char] += 1

    for right in range(len(s)):
        window[s[right]] += 1
        window_size = right - left + 1

        if window_size > len(p):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        if window == target:
            output.append(left)

    return output

if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
    print(find_anagrams("abab", "ab"))         # [0, 1, 2]
    print(find_anagrams("aa", "bb"))           # []
    print(find_anagrams("a", "a"))             # [0]

# CLARIFICATIONS
# Return all starting indices in s where an anagram of p begins
# An anagram is a permutation — same characters, same frequencies, any order
# Only lowercase English letters

# BRUTE FORCE
# For every starting index i, check if s[i:i+len(p)] is an anagram of p using a frequency map
# Time: O(n * len(p))   Space: O(1)

# OPTIMISED — Fixed sliding window with frequency map comparison
# Identical pattern to Permutation in String — collect all matches instead of returning on first
# Window size fixed at len(p), slide over s
# Delete keys at zero to keep dict equality accurate
# Append left (window start) to output whenever window == target
# Trade-off: matches counter would reduce per-step comparison from O(alphabet) to O(1)
# Time: O(n)   Space: O(1) — maps hold at most 26 keys
