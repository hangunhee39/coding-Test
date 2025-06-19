N, M, H = map(int, input().split())
dp = [[0]*(H+1) for _ in range(N+1)] 

for i in range(1,N+1):
    arr = list(map(int, input().split()))

    for j in range(H+1):
        dp[i][j] = dp[i-1][j]
    
    for item in arr:
        dp[i][item] += 1
        for k in range(item+1, H+1):
            dp[i][k] += dp[i-1][k-item]

print(dp[N][H]%10007)