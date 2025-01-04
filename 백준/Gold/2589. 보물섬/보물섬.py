# DFS -> 백트래킹 ( 반복문, 재귀함수 ) , *경우의 수 탐색
# BFS -> 그래프 탐색에 좋음,  *노드와 노드의 관계를 탐색

#완전 탐색적 사고 -> 계속 돌면서 제일 먼 곳 업데이트

from collections import deque

Y, X = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(Y)]

maxAns = 0

#완전 탐색 안에서 각각 BFS 탐색
for y in range(Y) :
    for x in range(X):
        
        #땅일때 만 
        if graph[y][x] == 'L' :
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            dist = [[0 for _ in range(X)] for _ in range(Y)]
            
            #BFS
            q = deque()
            q.append([y,x])
            visited[y][x] = 1
            
            while q :
                ey, ex = q.popleft()
                
                for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ny = ey + dy
                    nx = ex + dx
                    
                    if 0 <= ny < Y and 0 <= nx < X and graph[ny][nx] == 'L' and visited[ny][nx] == 0:
                                visited[ny][nx] = 1
                                dist[ny][nx] = dist[ey][ex] + 1
                                maxAns = max(maxAns, dist[ny][nx])
                                q.append([ny,nx])

print(maxAns)
