# DFS -> 백트래킹 ( 반복문, 재귀함수 ) , *경우의 수 탐색
# BFS -> 그래프 탐색에 좋음,  *노드와 노드의 관계를 탐색

# ---- DFS ----------------
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node) :
    visited[node] = 1
    
    for next in graph[node]:
        if visited[next] == 1:
            continue
        recur(next)    

#1번 노드에 감염된거 검색
recur(1)

print(sum(visited)-1)

# ---- BFS ----------
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

#q 가 0이 되면 끝난다 ,
while len(q) > 0 : 
    node  = q.popleft()
    visited[node] = 1
    
    for next in graph[node] :
        if visited[next] == 1:
            continue
        q.append(next)
        
print(sum(visited) -1)
