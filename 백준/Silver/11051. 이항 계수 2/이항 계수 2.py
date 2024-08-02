n, k = map(int, input().split())
if k == 0:
    print(1)
else:
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(2, n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
    
    print(dp[n][k])