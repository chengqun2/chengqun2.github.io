# 283. Move Zeroes (Easy)

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                '''
                The statement nums[left], nums[right] = nums[right], nums[left] 
                is a concise way to swap two values in a list at indices left and right. 
                It takes advantage of Python's tuple unpacking feature to perform the swap in a single line.
                '''
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        print(nums)
solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)