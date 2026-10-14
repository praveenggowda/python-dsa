"""
Problem: Valid Palindrome II
LeetCode: 680
Category: Two Pointers
Difficulty: Easy

Problem Statement:
Given a string s, return true if the s can be palindrome after deleting at most one character.

Examples:
Input: s = "aba"   ->  Output: True
Input: s = "abca"  ->  Output: True  (remove 'c' or 'b')
Input: s = "abc"   ->  Output: False

Clarifications:
- Can delete at most one character
- Case-sensitive, no non-alphanumeric filtering (unlike Valid Palindrome I)
- Empty string and single character are palindromes

Brute Force:
Try deleting each character one by one, check if palindrome each time
Time: O(n²)  Space: O(n)

Optimised:
Two pointers from opposite ends, on first mismatch try skipping left OR skipping right.
If either remaining window is a palindrome return True.
Time: O(n)  Space: O(1)

Pattern: Two Pointers
"""


def valid_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)

    return True

def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True

if __name__ == "__main__":
    print(valid_palindrome("aba"))    # True
    print(valid_palindrome("abca"))   # True
    print(valid_palindrome("abc"))    # False
    print(valid_palindrome("deeee"))  # True
    print(valid_palindrome("cbbcc"))  # True

