# bfs, 완전 탐색
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
dict = [[0,1],[1,0],[0,-1],[-1,0]]
q = deque()

# 바꿔야 할 방 수 카운트
visted = [[-1]*n for _ in range(n)]

q.append([0,0])
visted[0][0] = 0
while q:
    y, x = q.popleft()
    for dy, dx in dict:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 0 and visted[ny][nx] == -1:
                q.append([ny,nx])
                visted[ny][nx] = visted[y][x] + 1
            # 흰색이면 앞(appendleft)에 추가해서 검정색일때 visited 조건에 걸리게 만든다
            elif graph[ny][nx] == 1 and visted[ny][nx] == -1:
                q.appendleft([ny,nx])
                visted[ny][nx] = visted[y][x] 
                
print(visted[n-1][n-1])
            