# DP - LIS (가장 긴 부분 수열)
# 나보다 작은 수가 있으면  +1

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [1]*N  # 1로 초기화 (제일 작아도 1)

for i in range(N):
    for j in range(i) : # 자기 보다 전에 있는 것 비교
        if arr[i] > arr[j]: 
            # 전에 있는 것보다 크면 전에 있던 수열보다 +1 해서 수열수 저장
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N-max(dp))