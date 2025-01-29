# DP 
# dp 태이블에서 3, 5 전에 설탕 봉지가 만들어지면 작은 값에서 + 1

N = int(input())
dp = [-1]*(N+1)

for i in range(3, N+1) :
    if i == 3 or i == 5:
        dp[i] = 1
        continue
    # 5를 먼저 해서 5위주로 생성
    if i % 5 == 0:
        dp[i] = dp[i-5] + 1
        continue
    if i % 3 == 0:
        dp[i] = dp[i-3] + 1
        continue
    if dp[i-3] != -1 and dp[i-5] != -1 :
        dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N])