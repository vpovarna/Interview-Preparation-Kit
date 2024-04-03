from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       
        def dfs(r: int, c: int, i: int)-> bool:
            if len(word) == i:
                return True
            elif r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c]:
                return False
            else:
                tmp = board[r][c]
                board[r][c] = ' '
                
                res = dfs(r -1, c, i + 1) or \
                      dfs(r+1, c, i + 1) or \
                      dfs(r, c -1, i + 1) or \
                      dfs(r, c + 1, i + 1)
                board[r][c] = tmp
                return res
    
        row_nr = len(board)
        col_nr = len(board[0])
        
        for r in range(row_nr):
            for c in range(col_nr):
                if word[0] == board[r][c]:
                    if dfs(r,c,0):
                        return True
        
        return False