# Problem: Kth Largest Element in an Array
# Given an unsorted array and an integer k, return the kth largest element.
# The kth largest element is the kth largest in sorted order, not kth distinct.
#
# Example: nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
# Example: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 -> 4
#
# Constraints:
# - May contain duplicates
# - May contain negative numbers
# - Return -1 if array is empty
#
# Brute force: sort descending, return index k-1. Time O(N log N), Space O(1)
#
# Optimised: min heap of size k. Push every element, pop when size exceeds k.
# At the end, heap[0] is the kth largest. Time O(N log K), Space O(K)

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    if not nums:
        return -1

    heap: list[int] = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5
    print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(kth_largest([], 1))                    # -1
    print(kth_largest([1], 1))                   # 1
    print(kth_largest([-1, -2, -3], 2))          # -2
