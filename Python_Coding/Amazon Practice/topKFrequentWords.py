from typing import List
"""
Question: Given an array of strings words and an integer k, return the k most frequent words in the array.

The words should be returned in descending order of frequency.
If two words have the same frequency, sort them lexicographically (alphabetical order).

"""

class Solution():
    def topKFrequentWords(self, words: List[str], k: int) -> List[str]:
        myList = {}

        words.sort()

        for word in words:
            if word in myList:
                myList[word] += 1
            else: 
                myList[word] = 1

        sorted_words = sorted(myList.items(), key = lambda x: (-x[1], x[0]))

        results = []
        for word in sorted_words:
            sorted_word, frequency = word
            results.append(sorted_word)

        return results[:k]
    
words = ["i", "love", "leetcode", "i", "love", "coding" , "love"]
k = 2

sol = Solution()

result = sol.topKFrequentWords(words, k)
print(result)