# First Bad Version
# LeetCode 278 - Easy
#
# Problem:
#   You are given n versions of a product numbered from 1 to n.
#
#   There is a function:
#
#       isBadVersion(version)
#
#   which returns:
#
#       True  -> version is bad
#       False -> version is good
#
#   Once a version becomes bad,
#   every version after it is also bad.
#
#   Find and return the FIRST bad version.
#
# Clarifications:
#   - Versions are numbered from 1 to n
#   - There is always at least one bad version
#   - Minimize calls to isBadVersion()
#   - Must run in O(log n)
#
# Example 1:
#
# n = 5
# bad = 4
#
# Versions:
# 1  2  3  4  5
# G  G  G  B  B
#
# Output:
# 4
#
# Example 2:
#
# n = 1
# bad = 1
#
# Versions:
# 1
# B
#
# Output:
# 1
#
# Brute Force:
#   Check every version from 1 to n.
#   Return the first version where isBadVersion() == True.
#
# Time: O(n)
# Space: O(1)
#
# Optimised:
#   Use Binary Search.
#
#   Key insight:
#
#   Good Good Good Good Bad Bad Bad Bad
#                       ^
#               First Bad Version
#
#   We are searching for the boundary between:
#
#       Good Versions
#       Bad Versions
#
#   If mid is bad:
#       first bad could be mid
#       search left side
#
#   If mid is good:
#       first bad must be on the right
#       search right side
#
# Time: O(log n)
# Space: O(1)

def first_bad_version(n: int, bad: int) -> int:
    def isBadVersion(version: int) -> bool:
        return version >= bad

    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    print(first_bad_version(5, 4))   # expect 4
    print(first_bad_version(1, 1))   # expect 1
    print(first_bad_version(10, 3))  # expect 3
