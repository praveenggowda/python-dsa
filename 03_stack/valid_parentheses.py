"""
Problem: Valid Parentheses
LeetCode: 20
Category: Stack
Difficulty: Easy

Problem Statement:
Given a string s containing only '(', ')', '{', '}', '[', ']',
return True if the string is valid.

A string is valid if:
1. Every opening bracket has a corresponding closing bracket
2. Brackets close in the correct order
3. Every closing bracket has a corresponding opening bracket of the same type

Examples:
Input: s = "()"       ->  Output: True
Input: s = "()[]{}"   ->  Output: True
Input: s = "(]"       ->  Output: False
Input: s = "([)]"     ->  Output: False
Input: s = "{[]}"     ->  Output: True

Clarifications:
- Empty string is valid (vacuously valid — mention assumption to interviewer)
- Only contains (){}[]
- No alphanumerics in input

Brute Force:
No obvious brute force — stack is the natural solution.

Optimized Approach:
Use a stack (deque). For each character:
- Opening bracket -> push to stack
- Closing bracket -> check if top of stack is the matching opener
- If mismatch or stack empty -> return False
At the end, stack must be empty.

Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

Pattern: Stack
"""

from collections import deque

def is_valid(s: str) -> bool:
    stack = deque()

    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else: 
            
            if len(stack) == 0:
                return False

            if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':            
                stack.pop()
            else:
                return False

    return len(stack) == 0

print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
