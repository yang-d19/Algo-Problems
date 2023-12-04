class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        longest_path_mat = [[-1 for j in range(cols)] for i in range(rows)]

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def find_longest_path(i, j):
            if longest_path_mat[i][j] == -1:
                longest_path = 1
                for direct in directions:
                    new_i = i + direct[0]
                    new_j = j + direct[1]
                    if new_i < 0 or new_i >= rows \
                        or new_j < 0 or new_j > cols:
                        continue
                    
                    if longest_path_mat[new_i][new_j] < matrix[i][j]:
                        if longest_path_mat[new_i][new_j] == -1:
                            find_longest_path(new_i, new_j)
                        longest_path = max(longest_path, 1 + longest_path_mat[new_i][new_j])

        max_path = 1

        for row in range(rows):
            for col in range(cols):
                find_longest_path(row, col)
                max_path = max(max_path, longest_path_mat[row][col])
        
        return max_path


sol = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
result = sol.longestIncreasingPath(matrix)
print(result)