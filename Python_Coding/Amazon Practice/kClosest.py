import string
from typing import List
import math

"""
Given an array of points where points[i] = [x_i, y_i] represents a 
point on the X-Y plane and an integer k, return the k closest points to the origin (0,0)

The distance between two points on X-Y plane is the euclidean distance (i.e., sqrt((x1-x2)**2 + (y1-y2)**2))

You may return the answer in any order. the answer is guaranteed to be unique (except for the order that it is in).
"""

class Solution:
    def kClosest(self, points: List[List[int]], k:int, origin: List[int]) -> List[List[int]]:
        result = []
        distances = []
        x0,y0 = origin

        for x,y in points:
            distance =  math.sqrt((x-x0)**2 + (y-y0)**2)
            distances.append([distance, x,y])

        distances.sort(key = lambda x:x[0], reverse=True)

        while k>0 and distances:
            distance, x,y  = distances.pop()
            result.append([x,y])
            k-=1

        return result
    

points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
origin = [0,0]
sol = Solution()
print(sol.kClosest(points, k, origin))