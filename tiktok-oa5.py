def maximum_product_sum(memory):
    MOD = 10**9+7
    n = len(memory)
    for i in range(n//2):
        x, y = memory[i], memory[n-i-1]
        memory[i], memory[n-i-1] = min(x,y), max(x,y)
    return sum([memory[i]*(i+1) for i in range(n)]) % MOD

if __name__ == "__main__":
    # ans = maximum_product_sum([2, 4, 1, 3])
    ans = maximum_product_sum([5, 1, 4, 2, 4, 1, 2, 3])
    print(ans)