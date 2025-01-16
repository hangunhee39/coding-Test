from collections import deque
import sys
sys.setrecursionlimit(10**6)
imput = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

#정렬 작은 순
for i in range(1, N+1):
    graph[i].sort()

def bfs():
    q = deque()
    q.append(V)
    visited[V] = 1
    while q :
        node = q.popleft()
        print(node, end = " ")
        for k in graph[node]:
            if visited[k] == 0:
                visited[k] = 1
                q.append(k)


def dfs(node):
    print(node, end= " ")
    visited[node] = 1
    for k in graph[node]:
        if visited[k] == 0:
            dfs(k)
    return

dfs(V)
print()
visited = [0 for _ in range(N+1)]   
bfs()