D ,P = map(int, input().split())
# 길이 별 DP 테이블을 만든다 (해당 길이에 최대 용량을 가진)
dp = [0]*(D+1) 
dp[0] = 1e9

for _ in range(P):
    length, capacity = map(int, input().split())
    # 뒤에서 부터 채운다 (1.현재 길이를 뺀 dp 테이블, 2.현재 용량 중 작은 값을)
    for i in range(D, length-1, -1):
        dp[i] = max(dp[i], min(capacity, dp[i-length]))


print(dp[D])