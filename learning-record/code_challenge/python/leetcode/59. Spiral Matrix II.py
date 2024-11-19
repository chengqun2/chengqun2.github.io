# 59. Spiral Matrix II (Medium)
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Clockwise order: from the top to the right, then down and then to the left, and back up to the top

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#[[1,2,3],
# [8,9,4],
# [7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        # Initialize boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1  # Start filling numbers from 1 to n^2
        while top <= bottom and left <= right:
            print(f"Move right along the top boundary::: top: {top}, bottom: {bottom}, left: {left}, right: {right}")
            # Move right along the top boundary
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
                print(f"Move-right: {matrix[top][col]}")
            top += 1

            print(f"Move down along the right boundary::: top: {top}, bottom: {bottom}, left: {left}, right: {right}")
            # # Move down along the right boundary
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
                print(f"Move-down: {matrix[row][right]}")
            right -= 1

            print(f"Move left along the bottom boundary::: top: {top}, bottom: {bottom}, left: {left}, right: {right}")
            # # Move left along the bottom boundary
            if top <= bottom:  # Ensure row exists
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                    print(f"Move-left: {matrix[bottom][col]}")
                bottom -= 1
            
            # Move up along the left boundary
            print(f"Move up along the left boundary::: bottom: {bottom}, top: {top}, left: {left}, right: {right}")
            if left <= right:  # Ensure column exists
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                    print(f"Move-up: {matrix[row][left]}")
                left += 1
        
        return matrix

solution = Solution()
print(solution.generateMatrix(3))
