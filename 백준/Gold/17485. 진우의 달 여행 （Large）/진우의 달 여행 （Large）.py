#DP 

N, M = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(N)]
dp = [[[1e9]*3 for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        for i in range(3):
            #처음 세팅
            if y==0:
                dp[y][x][i] = map[y][x]
                continue

            # 그리프 밖에 부분 예외
            if (x == 0 and i == 0) or (x == M-1 and i == 2):
                continue
                
            if i == 0:
                dp[y][x][0] = min(dp[y-1][x-1][1],dp[y-1][x-1][2]) + map[y][x]
            elif i == 1:
                dp[y][x][1] = min(dp[y-1][x][0],dp[y-1][x][2]) + map[y][x]
            elif i == 2:
                dp[y][x][2] = min(dp[y-1][x+1][0],dp[y-1][x+1][1]) + map[y][x]

answer = 1e9
for x in range(M):
    for i in range(3):
        answer = min(answer, dp[N-1][x][i])
print(answer)
    
            