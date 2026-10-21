from collections import defaultdict

def check_inclusion(s1: str, s2: str) -> bool:
    target = defaultdict(int)
    window_count = defaultdict(int)

    for char in s1:
        target[char] += 1

    left = 0

    for right in range(len(s2)):
        window_count[s2[right]] += 1

        if right - left + 1 > len(s1):
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            left += 1

        if target == window_count:
            return True

    return False

if __name__ == "__main__":
    print(check_inclusion("ab", "eidbaooo"))  # True
    print(check_inclusion("ab", "eidboaoo"))  # False
    print(check_inclusion("adc", "dcda"))     # True
    print(check_inclusion("abc", "a"))        # False
    print(check_inclusion("a", "a"))          # True

# CLARIFICATIONS
# Return True if any permutation of s1 is a substring of s2
# Permutations have the same length and same character frequencies
# Only lowercase English letters

# BRUTE FORCE
# Generate all permutations of s1, check if any is a substring of s2
# Time: O(n! * m)   Space: O(n)

# OPTIMISED — Fixed sliding window with frequency map comparison
# Window size is fixed at len(s1) — permutations always have the same length
# Build target frequency map from s1
# Slide window over s2: add right character, remove left when window exceeds len(s1)
# Delete keys when count hits zero so dict equality check stays accurate
# Compare target == window_count at each step — O(alphabet) per step, O(n) overall
# Trade-off: a matches counter would reduce comparison to O(1) per step
# Time: O(n)   Space: O(1) — maps hold at most 26 keys
