# 빽트레킹, bfs
from collections import deque
import copy
import sys
input = sys.stdin.readline

Y, X = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
virus = []
for y in range(Y):
    for x in range(X):
        if graph[y][x] == 2:
            virus.append([y,x])
        
answer = 0

def wall(count):
    if count == 3:
        bfs()
        return

    for y in range(Y):
        for x in range(X):
            if graph[y][x] == 0:
                graph[y][x] = 1
                wall(count + 1)
                graph[y][x] = 0
            
def bfs():
    q = deque()
    q.extend(virus) #각각의 요소를 따로 추가, append 는 한 요소로 추가함
    
    #graph_copy = copy.deepcopy(graph) #원본 유지
    copy_graph = [row[:] for row in graph]
    
    while q:
        y,x = q.popleft()
        for ey, ex in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny = y + ey
            nx = x + ex
            
            if 0 <= ny <Y and 0 <= nx <X and copy_graph[ny][nx] == 0:
                copy_graph[ny][nx] = 2
                q.append([ny,nx])

    global answer
    count = sum(y.count(0) for y in copy_graph)
    answer = max(answer, count)
    return

wall(0)
print(answer)