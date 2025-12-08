# LeetCode 75 - Sort Colors
# Difficulty: Medium
# Topic: Dutch National Flag Algorithm
# Date: 08-12-2025

#Explanation:
# We use three pointers:
#   low  -> boundary for 0s
#   mid  -> current element
#   high -> boundary for 2s

# Logic:
# - If nums[mid] == 0: swap with low, move both low and mid
# - If nums[mid] == 1: just move mid
# - If nums[mid] == 2: swap with high, move high only

# Time Complexity: O(n)  
#   - Each element is processed at most once.

# Space Complexity: O(1)  
#   - Sorting is done in-place using only pointers.

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0,0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid] 
                high -= 1
        return nums               

