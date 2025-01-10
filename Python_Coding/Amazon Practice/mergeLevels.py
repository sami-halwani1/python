from typing import List
"""
Given an array of intervals where each interval is represented as [start, end], 
merge all overlapping intervals and return an array of the non-overlapping intervals.

Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
"""

class Solution():
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <1:
            return []
        # x,y = intervals
        mergedList = []

        # for i in range(len(intervals)):
        #     for k in range(len(intervals)):
        #         if (x[i] <= x[k]) and (y[i] <= y[k]):

        intervals.sort(key= lambda x: x[0],)
        print(intervals)

        mergedList = [intervals[0]] #initialization of mergedList
        
        for currStart, currEnd in intervals[1:]:
            lastStart, lastEnd = mergedList[-1]

            if currStart <= lastEnd:
                mergedList[-1][1] = max(lastEnd, currEnd)
            else:
                mergedList.append([currStart, currEnd])

        return mergedList
    

sol = Solution()
intervals = [[1, 3], [2, 6], [15, 18] ,[8, 10] , [1,1]]
# intervals = []
result = sol.mergeIntervals(intervals)
print(result)