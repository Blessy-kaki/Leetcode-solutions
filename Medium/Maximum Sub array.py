# LeetCode 53 - Maximum Subarray
# Difficulty: Medium
# Topic: Kadane’s Algorithm / Dynamic Programming
# Date: 09-12-2025

# Explanation:
# We need to find a contiguous subarray with the largest sum.
# Kadane’s Algorithm idea:
# - curr_sum stores the best subarray sum ending at the current index.
# - At each element, decide:
#       → Start a new subarray from current number
#       → OR extend the previous subarray
# - max_sum keeps track of the best subarray sum.

# Time Complexity: O(n)
#   - We scan the array once.

# Space Complexity: O(1)
#   - Uses only two variables: curr_sum, max_sum.

class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = 0
        max_sum = nums[0]
        for i in nums:
            cur_sum = max(i, cur_sum + i)
            max_sum = max(max_sum, cur_sum)
        return max_sum  
