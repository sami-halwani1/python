"""
Given a string s, find the length of the longest substring without repeating characters.

constraints:
0 <= s.length <= 5 * 10⁴
s consists of English letters, digits, symbols, and spaces.
"""

class Solution():
    def longestSubstring(self, s: str) -> int:
        counter = 0
        strList = []
        tempStr = ""
        for i in s:
            if i not in tempStr:
                tempStr += i
            else:
                strList.append(tempStr)
                if len(tempStr) > counter:
                    counter = len(tempStr)



        return
    
sol  = Solution()
s = "abcabcbb"
print(f'longest Substring is {sol.longestSubstring(s)}')