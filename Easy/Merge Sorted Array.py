# LeetCode 88 - Merge Sorted Array
# Difficulty: Easy
# Topic: Two Pointers / Array
# Date: 11-12-2025

# Explanation:
# We are given two sorted arrays:
#   nums1 → size m + n (first m elements valid, last n empty)
#   nums2 → size n (all valid)

# Goal: Merge nums2 into nums1 as a single sorted array in-place.

# Approach (Two Pointers from End):
# - Use three pointers:
#       i = m - 1   → last valid element of nums1
#       j = n - 1   → last element of nums2
#       k = m + n - 1 → last position of nums1

# - Compare nums1[i] and nums2[j] from the end, and place the larger
#   value at nums1[k].
# - Move the pointer that placed the value.
# - Continue until all elements from nums2 are placed.

# Why from the end?
# - Because nums1 has extra space at the end. If we fill from the
#   beginning, we would overwrite the useful values in nums1.

# Time Complexity: O(m + n) / O(n)
#   - Each element is processed at most once.

# Space Complexity: O(1)
#   - No extra array is used; everything is done in-place.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        return nums1
