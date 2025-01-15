#DFS 방식
import sys
from collections import deque
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(y,x):
    if graph[y][x] == 0:
        return
    graph[y][x] = 0
    
    for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
        ey = y + dy
        ex = x + dx
        
        if 0<= ey < Y and 0 <= ex < X:
            dfs(ey, ex)
    return

#BFS 방식
def bfs(y,x) :
    q = deque()
    q.append([y,x])
    graph[y][x] = 0

    while q:
        ey ,ex = q.popleft()
        graph[ey][ex] = 0
        
        for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny = ey + dy
            nx = ex + dx

            if 0<= ny < Y and 0 <= nx < X and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([ny,nx])
            
    return

for _ in range(T) :
    answer = 0
    X, Y ,N = map(int, input().split())
    graph = [[0 for _ in range(X)] for _ in range(Y)]
    
    for _ in range(N):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(Y) :
        for x in range(X):
            if graph[y][x] == 1:
                answer += 1
                #dfs(y,x)
                bfs(y,x)

    print(answer)
            
    
        
