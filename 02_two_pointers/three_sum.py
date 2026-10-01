def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    output: list[list[int]] = []

    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                output.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return output


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(three_sum([0, 1, 1]))              # []
    print(three_sum([0, 0, 0]))              # [[0,0,0]]

# CLARIFICATIONS
# Return all unique triplets that sum to zero
# No duplicate triplets in output
# Order of elements within a triplet does not matter
# Array may contain duplicates

# BRUTE FORCE
# Three nested loops — check every combination of three elements
# Time: O(n^3)   Space: O(1)

# OPTIMISED — Sort + Two Pointers
# Sort the array so duplicates are adjacent and two-pointer works correctly
# For each anchor i, run opposite-ends two pointer on the rest
# Skip duplicate anchors: if nums[i] == nums[i-1], continue
# After a match: move both pointers, then skip inner duplicates
# Time: O(n^2)   Space: O(1)