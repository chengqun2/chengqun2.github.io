'''
290. Word Pattern (Easy)
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
'''

from itertools import zip_longest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        for item in zip_longest(pattern, s):
            print(item)
        return len(set(zip_longest(pattern, s))) == len(set(s)) == len(set(pattern))

solution = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))