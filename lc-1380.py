class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        m = len(matrix)
        n = len(matrix[0])
        tag = [[0 for i in range(n)] for j in range(m)]

        # find the min element in each row
        for row in range(m):
            min_val = 100001
            min_col = -1
            for col in range(n):
                if matrix[row][col] < min_val:
                    min_val = matrix[row][col]
                    min_col = col
            tag[row][min_col] = 1
        
        # find the max element in each column
        for col in range(n):
            max_val = 0
            max_row = -1
            for row in range(m):
                if matrix[row][col] > max_val:
                    max_val = matrix[row][col]
                    max_row = row
            if tag[max_row][col] == 1:
                ans.append(matrix[max_row][col])

        return ans


ss = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

sol = Solution()
ret = sol.luckyNumbers(ss)

print(ret)
