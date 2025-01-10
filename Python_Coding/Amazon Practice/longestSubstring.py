"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
The string consists of English letters, digits, symbols, and spaces.
The solution should be efficient.

Input: s = "abcabcbb"
"""

class Solution():
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left +1)


        return max_length

#O(n**2) runtime
# class Solution():
#     def length_of_longest_substring(self, s: str) -> int:
#         count = 0
#         tempStr =""
#         for letter in s:
#             if letter not in tempStr:
#                 tempStr += letter
#             else:
#                 if len(tempStr) > count:
#                     count = len(tempStr)
#                 tempStr = letter
            
            
#         return count
    
sol  = Solution()
# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
print(f'longest Substring is {sol.length_of_longest_substring(s)}')







"""
Given a string s, find the length of the longest substring without repeating characters.

constraints:
0 <= s.length <= 5 * 10⁴
s consists of English letters, digits, symbols, and spaces.
"""

#Old Version
# class Solution():
#     def longestSubstring(self, s: str) -> int:
#         counter = 0
#         strList = []
#         tempStr = ""
#         for i in s:
#             if i not in tempStr:
#                 tempStr += i
#             else:
#                 strList.append(tempStr)
#                 if len(tempStr) > counter:
#                     counter = len(tempStr)

#         return
# sol  = Solution()
# s = "abcabcbb"
# print(f'longest Substring is {sol.longestSubstring(s)}')