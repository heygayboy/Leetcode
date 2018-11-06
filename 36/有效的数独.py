# -*- coding: utf-8 -*-


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowHash = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        lineHash = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        boxHash = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                else:
                    if num not in rowHash[i] and num not in lineHash[j] and num not in boxHash[3 * (i / 3) + (j / 3)]:
                        rowHash[i][num] = 1
                        lineHash[j][num] = 1
                        boxHash[3 * (i / 3) + (j / 3)][num] = 1
                    else:
                        return False
        return True


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
a = Solution().isValidSudoku(board)
