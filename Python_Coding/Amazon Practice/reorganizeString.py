from collections import Counter
import heapq

class Solution():
    def reorganizeString(s: str) -> str:
        freq = Counter(s)
        max_heap = [(-count,char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        prev_count, prev_char = 0,''

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_count<0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char

        if len(result) != len(s):
            return ""
        
        return ''.join(result)


sol  = Solution()
s = input()
print(sol.reorganizeString(s))