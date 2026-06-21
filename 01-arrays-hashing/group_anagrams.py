"""
Problem: Group Anagrams
LeetCode: 49
Category: Arrays & Hashing
Difficulty: Medium

Problem Statement:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Examples:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Clarifications:
- All characters are lowercase English letters
- Order of groups does not matter
- Order within groups does not matter

Brute Force:
Sort each string, compare every pair
Time: O(n² * k log k)  Space: O(n)

Optimized Approach:
Sort each string -> use as dict key
All anagrams produce the same sorted key
Group words under the same key

Complexity:
Time Complexity: O(n * k log k) — n words, k = max word length
Space Complexity: O(n * k)

Pattern: Arrays & Hashing
"""

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
       
    for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word not in groups:
            groups[sorted_word] = []

        groups[sorted_word].append(word)      
    
    return list(groups.values())

def group_anagrams_using_defaultdict(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)      
    
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]
print(group_anagrams([""]))   # [[""]]
print(group_anagrams(["a"]))  # [["a"]]

print(group_anagrams_using_defaultdict(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]
print(group_anagrams_using_defaultdict([""]))   # [[""]]
print(group_anagrams_using_defaultdict(["a"]))  # [["a"]]