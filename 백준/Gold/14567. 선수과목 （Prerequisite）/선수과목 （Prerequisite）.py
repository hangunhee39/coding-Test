N, M = map(int, input().split())

indegree = [1] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1,N+1):
    for b in graph[i]:
        indegree[b] = max(indegree[b], indegree[i]+1)
print(*indegree[1:])
        
    