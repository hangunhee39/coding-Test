n = int(input())
item = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(2)]

# 처음 값 세팅
for i in range(3):
    dp[0][i] = item[0][i]
    
for idx_n in range(1,n):
    for RGB in range(3) : # 처음 선택이
        if RGB == 0 : #red
            dp[1][0] = min(dp[0][1] + item[idx_n][RGB], dp[0][2] + item[idx_n][RGB])
        if RGB == 1: #green
            dp[1][1] = min(dp[0][0] + item[idx_n][RGB], dp[0][2] + item[idx_n][RGB])
        if RGB == 2: #blue
            dp[1][2] = min(dp[0][0] + item[idx_n][RGB], dp[0][1] + item[idx_n][RGB])
    
    for j in range(3) :
        dp[0][j] = dp[1][j]
        
print(min(dp[-1]))