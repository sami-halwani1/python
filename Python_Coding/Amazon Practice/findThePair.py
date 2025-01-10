from typing import List

"""
You are given an array of integers nums and an integer target. Return the indices of the two numbers such that they add up to the target.

Constraints:
Each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

input: nums = [2, 7, 11, 15]  
target = 9

"""
class Solution():
    def two_sum(self, nums: List[int] , sum: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(len(nums)):
                if(k > i):
                    if (nums[i] + nums[k]) == sum:
                        return [i, k]
        
        return []


sol = Solution()
nums = [2, 7, 11, 15]  
target = 9
print(sol.two_sum(nums, target))

# Optimized Version:

# class Solution:
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         # Dictionary to store the complement and its index
#         num_to_index = {}
        
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_to_index:
#                 return [num_to_index[complement], i]
#             num_to_index[num] = i  # Store the index of the current number
        
#         return []