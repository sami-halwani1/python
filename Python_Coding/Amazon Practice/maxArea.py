"""
You are given an array height of non-negative integers where each element represents the height of a vertical line on a coordinate plane. 
The distance between two lines is the difference in their indices.

Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water it can contain.

input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49


"""
# ------Correct but not Optimized
# from typing import List
# class Solution():
#     def max_area(self, height: List[int]) -> int:

#         max_area = 0

#         for i in range(len(height)):
#             for j in range(len(height) -1,-1,-1):
#                 if j == i:
#                     continue

#                 area = min(height[i], height[j]) * (i-j)
#                 if area >= 0 and area > max_area:
#                     max_area = area 

#         return max_area

from typing import List
class Solution():
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        i  = 0
        j = len(height)-1

        while i < j:
            area = min(height[i], height[j]) * (j-i)
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7,9]
# height = [1, 1]
print(sol.max_area(height))