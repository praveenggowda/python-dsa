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


# CLARIFICATIONS
# Can delete at most one character
# After deletion, check if the remaining string is a palindrome
# Case-sensitive, no non-alphanumeric filtering (unlike Valid Palindrome I)

# BRUTE FORCE
# Try deleting each character one by one, check if palindrome each time
# Time: O(n^2)   Space: O(n)

# OPTIMISED — Two pointers + helper
# Scan from both ends while characters match
# On first mismatch: try skipping left OR skipping right
# If either remaining window is a palindrome → True
# Helper is_palindrome checks a substring by index range, no new string allocated
# Time: O(n)   Space: O(1)
