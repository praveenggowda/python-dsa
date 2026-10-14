"""
Problem: Valid Palindrome
LeetCode: 125
Category: Two Pointers
Difficulty: Easy

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
Input: s = "A man, a plan, a canal: Panama"  ->  Output: True
Input: s = "race a car"                       ->  Output: False
Input: s = ""                                 ->  Output: True

Clarifications:
- Ignore non-alphanumeric characters (spaces, commas, colons)
- Case-insensitive comparison
- Empty string returns True (palindrome by definition)

Brute Force:
Clean the string first (filter non-alnum, lowercase), then compare to its reverse
Time: O(n)  Space: O(n)

Optimised:
Two pointers from opposite ends, skip non-alphanumeric with inner while loops,
compare lowercase characters, move inward on match
Time: O(n)  Space: O(1)

Pattern: Two Pointers
"""


def is_valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_valid_palindrome("race a car"))                       # False
    print(is_valid_palindrome(""))                                 # True
    print(is_valid_palindrome("L ,  UUL"))                        # True

