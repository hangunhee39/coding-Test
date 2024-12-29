N = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(N)]

for i in range(N) : 
    for j in range(i) : #i-1 까지만 비교
        if arr[i] > arr[j] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))