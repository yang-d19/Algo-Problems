class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # greedy?
        ans = 0
        for i in range(1, len(prices)):
            prof = prices[i] - prices[i - 1]
            if prof > 0:
                ans += prof
        return ans
    

sol = Solution()   

res = sol.maxProfit([7, 6, 4, 3, 1])

print(res)