import string
from typing import List

"""
You are given an array of logs. Each log is a space-delimeted string of words, where the first word is the indentifier.

There are two types of logs:
    - Letter-Logs: All Words(Except the Identifier) consist of lowercase english letters
    - Digit-logs: All Words(except the Identifier) consists of digits

Reorder these logs so that:
    1.) The Letter-logs come before all digit logs
    2.) The Letter-logs are sorted lixicogrpahically by their contents. If their contents
    are the same, then sort them lexicographically by their identifiers.
    3.) The digit logs maintain their relative orders

return the final order of logs 
"""

class Solution:
    def reorderDataLogs(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        result = letter_logs + digit_logs


        return result
    
sol = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", 'dig2 3 6', "let2 own kit dig", "let3 art zero"]
result= sol.reorderDataLogs(logs)
print(result)