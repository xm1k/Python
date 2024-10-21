"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/valid-sudoku/description/
"""

class Solution(object):
    def isValidSudoku(self, board):
        hashSet = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] + "in row: " + str(r) in hashSet or board[r][c] + "in column: " + str(
                            c) in hashSet or board[r][c] + "in box: " + str(r // 3) + "-" + str(c // 3) in hashSet:
                        return False

                    hashSet.add(board[r][c] + "in row: " + str(r))
                    hashSet.add(board[r][c] + "in column: " + str(c))
                    hashSet.add(board[r][c] + "in box: " + str(r // 3) + "-" + str(c // 3))

        return True