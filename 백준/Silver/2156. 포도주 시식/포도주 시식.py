N = int(input())
arr = list(int(input()) for _ in range(N))
dp = [0] * N
dp[0] = arr[0]

if N > 1:
    dp[1] = arr[0] + arr[1]
    
if N > 2:
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])

for i in range(3,N):
    dp[i] = max(dp[i-2] + arr[i], dp[i-1], dp[i-3] + arr[i-1] + arr[i])

print(max(dp))
    