# 3. Longest Substring Without Repeating Characters  (Medium)
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def longest_substring(self, str: str) -> int:
        if not str:
            return 0
            
        char_map = {}
        max_length = 0
        start = 0
        
        for right, char in enumerate(str):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            else:
                max_length = max(max_length, right - start + 1)
            char_map[char] = right
            
        return max_length 

solution = Solution()
print(solution.longest_substring('pwwkew'))