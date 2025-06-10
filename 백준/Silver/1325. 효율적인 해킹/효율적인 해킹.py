from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
counts = [0] *(N+1)

def bfs(a):
    q = deque()
    visited = [0] * (N+1)
    count = 0
    
    q.append(a)
    visited[a] = 1

    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
                count += 1
    return count

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

# 해당 경로로 몇 개를 감염시켰는지 저장
for i in range(1, N+1):
    counts[i] = bfs(i)

for i in range(1, N+1):
    if counts[i] == max(counts):
        print(i, end = " ")