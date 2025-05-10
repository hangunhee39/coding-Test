#dp, 맨 뒤가 정답인 경우

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = arr[0]

if n == 1:
    print(dp[0])
    exit()

dp[1] = arr[0] + arr[1]

if n == 2:
    print(dp[1])
    exit()

dp[2] = max(arr[0], arr[1]) + arr[2]

if n == 3:
    print(dp[2])
    exit()
    
for i in range(3, n):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[-1])