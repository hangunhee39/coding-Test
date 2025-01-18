# BFS 
# 깊이 별로 카운트 하는 문제
# ex ) 
# 0
# 1 1 1 1 
# 2 2
# 3 3 3 3 3
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [0 for _ in range(N+1)]
count = [0 for _ in range(N+1)] #깊이 별 카운트

answer = [5_001 for _ in range(N+1)]

def bfs(start) :
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                #깊이 별로 카운트 증가
                count[next] = count[now] + 1
                visited[next] = 1
                q.append(next)

    answer[start] = sum(count)
    return 

for i in range(1,N+1):
    bfs(i)
    visited = [0 for _ in range(N+1)]
    count = [0 for _ in range(N+1)]

#원래 작은 인덱스 반환
print(answer.index(min(answer)))