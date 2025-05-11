N, M = map(int, input().split())
K = int(input())

dp =[[0] * (N+1) for _ in range(M + 1)]
dp[0][0] = 1
wall = []

for _ in range(K):
    a, b, c, d = map(int, input().split())
    wall.append((a, b, c, d))
    wall.append((c, d, a, b))

for m in range(M+1):
    for n in range(N+1):
        if n > 0 and (n - 1, m, n, m) not in wall:
            dp[m][n] += dp[m][n-1]
        if m > 0 and (n, m - 1, n, m) not in wall:
            dp[m][n] += dp[m-1][n]

print(dp[M][N])
        
        