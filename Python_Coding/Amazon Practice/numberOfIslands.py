from typing import List
"""
Given an m x n 2D binary grid "grid" which repsents a map of '1's (land) and '0's(water), return the number of islands

An island is surronder by water and is formed by connecting adacent lands horizontally or vertically.
 You may assume all four edges of the grid is surrounded by water

"""

class Solution():
    def numberOfIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        visited = set()

        def dfs(r,c):
            if (r,c) in visited:
                return 
            visited.add((r,c))
        
            directions = [[1,0],[-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1" and (r,c) not in visited:
                    dfs(r,c)
                    result += 1


        return result