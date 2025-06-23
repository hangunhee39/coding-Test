N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: x[0])
dp = [1]*(N)

# LIS - 가장 긴 부분 수열 찾기
for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))