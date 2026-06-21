"""
Problem: Valid Anagram
LeetCode: 242
Category: Arrays & Hashing
Difficulty: Easy

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word formed by rearranging the letters of another word using all
original letters exactly once.

Examples:
Input: s = "anagram", t = "nagaram"  ->  Output: True
Input: s = "rat", t = "car"          ->  Output: False

Clarifications:
- Lowercase English letters only
- Different lengths -> False immediately

Brute Force:
Sort both strings and compare
Time: O(n log n)  Space: O(1)

Optimized Approach:
Character count array of size 26 (or dict)
Increment for s, decrement for t
If any count != 0 -> not an anagram

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Arrays & Hashing
"""

def is_anagram(s: str, t: str) -> bool:
    count = [0] * 26

    if len(s) != len(t):
        return False

    for c in s:
        count[ord(c) - ord('a')] += 1
    
    for c in t:
        count[ord(c) - ord('a')] -= 1 

    for c in count:
        if c != 0:
            return False

    return True

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("rat", ""))             # False
