class Solution(object):
    def gen(self, left, right, curr_pair):
        if left == 0 and right == 0:
            self.result.append(curr_pair)
        if left > 0:
            self.gen(left - 1, right, curr_pair + '(')
        if right > left:
            self.gen(left, right - 1, curr_pair + ')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.gen(n, n, "")
        return self.result
    

sol = Solution()   

res = sol.generateParenthesis(2)

print(res)