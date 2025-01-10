from typing import List
"""
You are given an m x n grid of characters board and a string word. Return True if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

input: board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "ABCCED"

output = True

"""
class Solution():
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, tempStr):
            if (row,col) in visited:
                return False
            visited.add((row, col))
            tempStr += board[row][col]

            if not word.startswith(tempStr):
                visited.remove((row, col))
                return False
            if tempStr == word:
                return True

            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                if nr in range(rows) and nc in range(cols) :
                    if dfs(nr,nc, tempStr):
                        return True
            visited.remove((row,col))
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, ""):
                    return True
                    
        
        return False
    
sol = Solution()
board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
# word = "ABCCED"
word = "ABCB"
# word = "SEE"
print(sol.exist(board, word))