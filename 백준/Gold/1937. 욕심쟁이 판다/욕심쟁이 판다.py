#2차원 DP
# 모든 점을 방문 -> 재귀로 구현
# -> 재귀를 DP로 바꾼다
# def recur(y, x) :
    
#     point = 0
#     for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]] :
#         ey = y + dy
#         ex = x + dx
    
#         if 0 <= ey < n and 0 <= ex < n:
#             if graph[y][x] < graph[ey][ex]:
#                 # 갈 곳이 있으면 +1
#                 return recur(ey,ex) + 1   
#         #주변보다 다 커서 돌아갈 때
#         return 0
    
#     return max(recur(y-1,x), recur(y+1,x), recur(y,x-1),recur(y,x+1))
import sys
sys.setrecursionlimit(10**6)

def recur(y, x) :
    
    #DP 재사용!!!!
    if dp[y][x] != 0:
        return dp[y][x]
    
    #point = 0 
    #dp가 곧 포인트
    for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]] :
        ey = y + dy
        ex = x + dx
    
        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                # 포인트에 저장
                #return max(recur(y-1,x), recur(y+1,x), recur(y,x-1),recur(y,x+1))
                #를 point로 임시 저장한 다음 가장 큰 값 리턴 느낌
                dp[y][x] = max(dp[y][x], recur(ey,ex) + 1)
    return dp[y][x]


n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]


for y in range(n):
    for x in range(n) :
        recur(y,x)

#2차원 배열에서 최대 뽑기
print(max(map(max,dp)) +1)