# 다익스트라 - 최단거리 구하기
# BFS DFS랑 차이점 간선의 길이 (가중치)

# 3가지 방법
# 1. BFS    2. min (a, b)   3. 노드 이동할때 마다 전체 최단거리 갱신
# 오류를 막기 위해, 어떤 노드로 가도 최소거리 방문!!

from collections import deque

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]

visited = [0 for _ in range(N+1)]
dist = [ 1e9 for _ in range(N+1)]

for _ in range(M) :
    A,B,C = map(int, input().split())
    graph[A].append((B,C))
    
#bfs !
q = deque()
q.append(start)
visited[start] = 1
dist[start] = 0

def shortest_finder():
    mini = 1e9
    idx = 0
    for i in range(1,N+1) :
        if dist[i] <= mini:
            idx = i
            mini = dist[i]
    return idx

# q가 아무것도 없으면 false
while q:
    node = q.popleft()
    for next, weight in graph[node] :
        #1. 각각의 노드에 값을 업데읕
        #2. 만약에 여러 경로가 있다면 min 비교
        dist[next] = min(dist[node] + weight, dist[next])
        q.append(next)
        visited[next] = 1
        
        #3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탑색! (오염 !)
        idx = shortest_finder()
        if idx in q :
            # 짧은 거리 우선순위 높이기 
            q.remove(idx)
            q.appendleft(idx)
            
print(dist)
#------------------------------------------
import heapq

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]

dist = [ 1e9  for _ in range(N+1)]

for _ in range(M) :
    A,B,C = map(int, input().split())
    graph[A].append((B,C))
    
#bfs !
q = []
heapq.heappush(q, [0,start]) #힙 상테(우선 순위 정렬) 유지 한 상태로 넣기
dist[start] = 0

# q가 아무것도 없으면 false
while q:
    
    #우선 순위 큐를 이용하여, 거리를 보고 정렬
    #heapq.heapify(q) #문제점 : 힙 상태 깨짐
    _w, node = heapq.heappop(q) # 힙 상태 유지
    
    for next, weight in graph[node] :
        #1. 각각의 노드에 값을 업데읕
        #2. 만약에 여러 경로가 있다면 min 비교
        #3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탑색! (오염 !)
        
        # visted 필요 없이 더 작을 때만 업데이트
        if dist[node] + weight < dist[next] :
            dist[next] = dist[node] + weight
            heapq.heappush(q, [dist[next], next])
        
            
for i in range(1, N+1):
    if dist[i] == 1e9:
        print("INF")  
    else:
        print(dist[i]) 
