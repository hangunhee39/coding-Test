# DP, 

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k+1)]
dp[0] = 1 # 금액에 딱 맞을 때

for _ in range(n):
    coins.append(int(input()))

# 가능한 경우를 계속 쌓는 느낌
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])