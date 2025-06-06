T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int ,input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in arr:
        for i in range(M+1):
            if i >= coin:
                dp[i] += dp[i - coin]
                
    print(dp[M])
    