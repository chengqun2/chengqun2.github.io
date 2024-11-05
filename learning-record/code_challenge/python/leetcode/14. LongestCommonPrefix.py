# 14. Longest Common Prefix (Easy)
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""

# Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longest_Common_Prefix(self, strs: List[str]) -> str:
        ans  = ''
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                return ans
        return ans 
solution = Solution()
strs = ["flower","flow","flight"]
print(solution.longest_Common_Prefix(strs))