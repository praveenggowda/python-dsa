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


# CLARIFICATIONS
# Ignore non-alphanumeric characters (spaces, commas, colons)
# Case-insensitive comparison
# Empty string → True (palindrome by definition)

# BRUTE FORCE
# Clean the string first (filter non-alnum, lowercase), then compare to its reverse
# Time: O(n)   Space: O(n)  (new string allocated)

# OPTIMISED — Two Pointers (opposite ends)
# Left pointer at 0, right pointer at len-1
# Skip non-alphanumeric from both sides using inner while loops
# Compare lowercase characters, move both pointers inward
# Time: O(n)   Space: O(1)  (no extra string, just two pointers)
