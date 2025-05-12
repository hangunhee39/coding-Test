N = int(input())
dp = [1e9] * (N+1)
dp[0] = 0 

for i in range(1, N+1):
    j = 1
    while (j**2) <= N:
        dp[i] = min(dp[i], dp[i - (j**2)] +1)
        j += 1

print(dp[N])