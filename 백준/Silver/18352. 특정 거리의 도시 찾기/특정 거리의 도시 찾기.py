from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
dists = [int(1e9)] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def dij(start):
    q = deque()
    q.append([start, 0])
    dists[start] = 0
    
    while q:
        current, dist = q.popleft()
        if dists[current] < dist:
            continue
            
        for node in graph[current]:
            if dists[node] >= dist + 1:
                dists[node] = dist + 1
                q.append([node, dist + 1])

dij(X)
isFound = False
for i in range(N+1):
    if dists[i] == K:
        print(i)
        isFound = True

if not isFound:
    print(-1)
