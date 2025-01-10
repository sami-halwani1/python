"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:

i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0
The solution set must not contain duplicate triplets.

Constraints
0 <= nums.length <= 3000
-10⁵ <= nums[i] <= 10⁵

Optimize for time complexity.
Use the two-pointer technique after sorting the array.

input: nums = [-1, 0, 1, 2, -1, -4]

"""
from typing import List
class Solution():
    def three_sum(self, nums: List[int] ) -> List[List[int]]:
        # ---- Incorrect Solution -- 
        # j, k = None, len(nums) -1
        # result = []

        # nums.sort() # [-4,-1,-1,0,1,2]
        # print(nums)
        # for i in range(len(nums)):
        #     k = len(nums) -1
        #     while k >=0 and i!=k: 
        #         if i != j and i!=k and j != k:
        #             num_j = nums[i] - nums[k]
        #             if (num_j in nums):
        #                 j = nums.index(num_j)
        #                 print(f'[{nums[i]}, {nums[j]}, {nums[k]}]')
        #                 if (nums[i] + nums[j] + nums[k]) == 0:
        #                     # print(f'[{nums[i]}, {nums[j]}, {nums[k]}]')
        #                     result.append([nums[i], nums[j], nums[k]])
        #         k-=1        

        #----Correct Solution
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
                
            j, k = i+1, len(nums)-1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                # print(current_sum)
                print(f'[{nums[i]},{nums[j]},{nums[k]}]')
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif current_sum<0:
                    j+=1
                else:
                    k-=1

        return result
    
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.three_sum(nums))