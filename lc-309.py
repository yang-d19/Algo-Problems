class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0 for _ in range(n)]
        max_dp = [0 for _ in range(n)]

        for end in range(n):
            max_profit = 0
            for begin in range(end):
                last_sell_prof = prices[end] - prices[begin]
                if begin >= 3:
                    prev_sell_prof = max_dp[begin - 2]
                else:
                    prev_sell_prof = 0
                max_profit = max(max_profit, prev_sell_prof + last_sell_prof)
            dp[end] = max_profit
            if end > 0:
                max_dp[end] = max(max_dp[end - 1], dp[end])
            # print(f"dp[{end}] = {dp[end]}")
        
        max_all_prof = 0
        for end in range(n):
            max_all_prof = max(max_all_prof, dp[end])
        return max_all_prof

sol = Solution()

prices = [6,1,6,4,3,0,2]

result = sol.maxProfit(prices)

print(result)