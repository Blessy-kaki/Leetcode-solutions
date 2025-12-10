# LeetCode 118 - Pascal's Triangle
# Difficulty: Easy
# Topic: Dynamic Programming / Math
# Date: 10-12-2025

# Explanation:
# Pascal's Triangle is built row by row.
# Each row starts and ends with 1.
# For inner elements:
#    curr[i] = prev[i] + prev[i - 1]
#
# Steps:
# 1. Create each row filled with 1s.
# 2. From row 2 onward, fill middle values using the previous row.
# 3. Add each completed row to the triangle list.

# Time Complexity: O(numRows^2)
#   - Because each row has increasing number of elements (1 + 2 + ... + n).

# Space Complexity: O(numRows^2)
#   - The entire triangle is stored in memory.

class Solution(object):
    def generate(self, numRows):
        triangle = []
        for row in range(numRows):
            curr = [1] * (row + 1)

            if row >= 2:
                prev = triangle[row - 1]

                for i in range(1, row):
                    curr[i] = prev[i] + prev[i - 1]
            triangle.append(curr) 
        return triangle  
