T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    for c in coin:
        for i in range(c, M+1):
            dp[i] += dp[i-c]
    print(dp[M])