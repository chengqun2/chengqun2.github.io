# 59. Spiral Matrix II (Medium)
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Clockwise order: from the top to the right, then down and then to the left, and back up to the top

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        
        return mat

solution = Solution()
print(solution.generateMatrix(3))