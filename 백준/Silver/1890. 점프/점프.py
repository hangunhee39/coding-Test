import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        if graph[y][x] == 0:
            break
            
        jump = graph[y][x]
        if dp[y][x] == 0 :
            continue
            
        if y + jump < N:
            dp[y+jump][x] += dp[y][x]
        if x + jump < N:
            dp[y][x+jump] += dp[y][x]

print(dp[N-1][N-1])