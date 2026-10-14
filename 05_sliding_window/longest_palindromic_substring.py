"""
Problem: Longest Palindromic Substring
LeetCode: 5
Category: Sliding Window / Two Pointers
Difficulty: Medium

Problem Statement:
Given a string s, return the longest palindromic substring in s.

Examples:
Input: s = "babad"  ->  Output: "bab"  (or "aba")
Input: s = "cbbd"   ->  Output: "bb"

Clarifications:
- Input contains only letters and digits
- Empty string returns empty string
- Single character is a palindrome

Brute Force:
Fix left, slide right, check each substring with helper
Time: O(n³)  Space: O(1)

Optimised (expand around center):
For every index i, treat i as the center of a palindrome and expand outward.
Two cases per index: odd length (left=i, right=i) and even length (left=i, right=i+1).
Expand while characters match, track the longest found.
Time: O(n²)  Space: O(1)

Pattern: Expand Around Center
"""


def longest_palindrome(s: str) -> str:
    final_result: str = ""

    for left in range(len(s)):
        for right in range(left, len(s)):
            if is_palindrome(s, left, right):
                result = s[left:right + 1]

                if len(result) > len(final_result):
                    final_result = result

    return final_result


def longest_palindrome_optimised(s: str) -> str:
    final_result: str = ""

    for i in range(len(s)):
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result = s[left:right + 1]

            if len(result) > len(final_result):
                final_result = result

            left -= 1
            right += 1

        left, right = i, i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result = s[left:right + 1]

            if len(result) > len(final_result):
                final_result = result

            left -= 1
            right += 1

    return final_result


def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


print(longest_palindrome("babad"))  # bab or aba
print(longest_palindrome("cbbd"))  # bb
print(longest_palindrome("a"))  # a
print(longest_palindrome(""))  # ""

print(longest_palindrome_optimised("babad"))  # bab or aba
print(longest_palindrome_optimised("cbbd"))  # bb
print(longest_palindrome_optimised("a"))  # a
print(longest_palindrome_optimised(""))  # ""
