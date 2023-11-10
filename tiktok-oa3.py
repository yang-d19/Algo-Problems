

def getMaxRequests(bandwidth, request, total_bandwidth):
    n = len(bandwidth)
    dp = [[0 for _ in range(total_bandwidth + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(1, total_bandwidth + 1):
            if w < bandwidth[i - 1]:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - bandwidth[i - 1]] + request[i - 1]
                            )
    
    return dp[n][total_bandwidth]


if __name__ == "__main__":
    # ans = getMaxRequests([200, 100, 350, 50, 100], [270, 142, 450, 124, 189], 500)
    ans = getMaxRequests([100, 500, 80, 25, 400], [100, 1000, 120, 110, 100], 200)
    print(ans)