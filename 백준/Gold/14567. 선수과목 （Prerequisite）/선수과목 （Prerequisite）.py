import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

answer = [1] * (N+1)
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
q = deque()

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬
for i in range(1,N+1):

    # 더 이상 위에 있는게 없으면 큐에 삽입 -> 순서대로 삽입됨
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1 
        # 더 이상 밑에가 없으면 삽입
        if indegree[i] == 0:                
            answer[i] = answer[now] + 1
            q.append(i)
 
print(*answer[1:])
        