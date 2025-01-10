from typing import List
"""
You are given a 2D grid consisting of '1's (land) and '0's (water). An island is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

Write a function to count the number of islands in the grid.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3

"""
class Solution():
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()


        def dfs(row, col):
            if (row,col) in visited:
                return
            visited.add((row,col))

            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            for dir_row, dir_col in directions:
                new_row = dir_row + row
                new_col = dir_col + col
                if (new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col]  == "1"):
                    dfs(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row,col)
                    numOfIslands +=1


        return numOfIslands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
result = sol.numIslands(grid)
print(result)





"""
Given an m x n 2D binary grid "grid" which repsents a map of '1's (land) and '0's(water), return the number of islands

An island is surronder by water and is formed by connecting adacent lands horizontally or vertically.
 You may assume all four edges of the grid is surrounded by water

"""

# class Solution():
#     def numberOfIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         result = 0
#         visited = set()

#         def dfs(r,c):
#             if (r,c) in visited:
#                 return 
#             visited.add((r,c))
        
#             directions = [[1,0],[-1,0], [0,1], [0,-1]]

#             for dr, dc in directions:
#                 nr = dr + r
#                 nc = dc + c
#                 if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
#                     dfs(nr, nc)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] =="1" and (r,c) not in visited:
#                     dfs(r,c)
#                     result += 1


#         return result