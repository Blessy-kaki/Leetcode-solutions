# LeetCode 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Kadane’s Algorithm / single pass
# Date: 08-12-2025

# Explanation:
# We want to maximize the profit = selling price - buying price.
# The main idea:
# - Track the minimum price seen so far (best day to buy).
# - For each price, calculate possible profit if sold today.
# - Keep updating the maximum profit.

# Time Complexity: O(n)
#   - We traverse the array once.

# Space Complexity: O(1)
#   - Only a few variables are used.

class Solution(object):
    def maxProfit(self, prices):
        max_pro = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            cur_pro = prices[i] - buy_price
            max_pro = max(max_pro, cur_pro)
            buy_price = min(buy_price, prices[i])
        if max_pro <= 0:
            return 0    
        return max_pro 
