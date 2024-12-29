#2차원 DP
# 모든 점을 방문 -> 재귀로 구현
# -> 재귀를 DP로 바꾼다

import sys
sys.setrecursionlimit(10**6)

def recur(y,x) :
    # 끝에 도달 시
    if y == Y-1 and x == X-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
        ey = y + dy
        ex = x + dx
        
        if 0 <= ey < Y and 0 <= ex < X:
            if graph[y][x] > graph[ey][ex] :
                route += recur(ey, ex)
                
    dp[y][x]= route
    return dp[y][x]                   

Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]
recur(0,0)
print(dp[0][0])