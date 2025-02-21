from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])

        res = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    # check up, check left
                    # if BOTH up and left do not have 'x', add 1 to res
                    # if up is not a valid location, just check left
                    # if left is not valid, just check up
                    # if both left and up are out of bounds, just add 1 to res
                    left_empty = False
                    top_empty = False
                    if j > 0:
                        if board[i][j-1] == '.':
                            left_empty = True
                    else:
                        left_empty = True
                    
                    if i > 0:
                        if board[i-1][j] == '.':
                            top_empty = True
                    else:
                        top_empty = True

                    if left_empty and top_empty:
                        res += 1
        return res

