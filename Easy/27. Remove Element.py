# LeetCode 27 - Remove Element
# Difficulty: Easy
# Topic: Two Pointers / Array
# Date: 11-12-2025

# Explanation:
# We are given an array nums and an integer val.
# The goal is to remove all occurrences of val in-place and return
# the number of elements that are not equal to val.

# Approach (Two Pointers):
# - Use a pointer k to track the position where the next valid
#   (non-val) element should be placed.
# - Loop through the array with i:
#       If nums[i] != val, copy nums[i] to nums[k] and move k forward.
# - After the loop, k represents the count of elements not equal to val.

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
