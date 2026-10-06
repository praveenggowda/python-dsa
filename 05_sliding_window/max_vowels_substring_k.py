def max_vowels(s: str, k: int) -> int:
    left = 0
    max_count = 0
    vowels_count = 0
    vowels = "aeiou"

    if k <= 0 or len(s) < k:
        return 0

    for right in range(len(s)):
        if s[right] in vowels:
            vowels_count += 1

        window_size = right - left + 1

        if window_size == k:
            max_count = max(max_count, vowels_count)

            if s[left] in vowels:
                vowels_count -= 1

            left += 1

    return max_count

if __name__ == "__main__":
    print(max_vowels("abciiidef", 3))  # 3
    print(max_vowels("aeiou", 2))      # 2
    print(max_vowels("leetcode", 3))   # 2
    print(max_vowels("rhythms", 4))    # 0
    print(max_vowels("a", 1))          # 1

# CLARIFICATIONS
# k <= 0 or len(s) < k: return 0 — no valid window exists
# Vowels are a, e, i, o, u — lowercase only
# Returns count of vowels in the best window, not a sum

# BRUTE FORCE
# For each starting index i, count vowels in s[i:i+k] with an inner loop
# Time: O(n * k)   Space: O(1)

# OPTIMISED — Fixed sliding window
# Count vowels as right expands into the window
# When window reaches size k: update max, then subtract left vowel before sliding
# Each character is visited once on entry and once on exit
# Time: O(n)   Space: O(1)
