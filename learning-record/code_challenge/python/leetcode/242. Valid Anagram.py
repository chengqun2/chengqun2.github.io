# 242. Valid Anagram (Easy)

# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
# Test cases
def test_isAnagram():
    solution = Solution()
    
    # Test case 1: Valid anagram
    assert solution.isAnagram("anagram", "nagaram") == True
    
    # Test case 2: Not an anagram
    assert solution.isAnagram("rat", "car") == False
    
    # Test case 3: Different lengths
    assert solution.isAnagram("ab", "abc") == False
    
    # Test case 4: Empty strings
    assert solution.isAnagram("", "") == True
    
    # Test case 5: Same characters, different counts
    assert solution.isAnagram("aaab", "aaba") == True
    
    print("All test cases passed!")

# Run tests
if __name__ == "__main__":
    test_isAnagram()
