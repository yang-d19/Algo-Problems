"""
Valid Sudoku
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        isValid = True

        # check 9 rows
        for row in range(9):
            hash_map = [0 for _ in range(10)]
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                val = int(val)
                if hash_map[val] == 0:
                    hash_map[val] = 1
                else:
                    isValid = False
                    break
            if not isValid:
                break
        
        # check 9 lines
        for col in range(9):
            hash_map = [0 for _ in range(10)]
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                val = int(val)
                if hash_map[val] == 0:
                    hash_map[val] = 1
                else:
                    isValid = False
                    break
            if not isValid:
                break
        
        # check 9 sub-boxes
        start_poses = [(0, 0), (0, 3), (0, 6),
                     (3, 0), (3, 3), (3, 6),
                     (6, 0), (6, 3), (6, 6)]
        
        for start_pos in start_poses:
            hash_map = [0 for _ in range(10)]
            for i in range(3):
                for j in range(3):
                    val = board[start_pos[0] + i][start_pos[1] + j]
                    if val == ".":
                        continue
                    val = int(val)
                    if hash_map[val] == 0:
                        hash_map[val] = 1
                    else:
                        isValid = False
                        break
                if not isValid:
                    break
            if not isValid:
                break
            
        return isValid


sol = Solution()

board = \
[["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

result = sol.isValidSudoku(board)

print(result)
