import heapq

n, m = map(int, input().split())
dists = [int(1e9)] * (n+1)
graph = [[] for _ in range(n+1)]

def dijkstra(start, end):
    q = []
    heapq.heappush(q, [start, 0])
    dists[start] = 0
    while q:
        cur, dist = heapq.heappop(q)
        if dists[cur] < dist: # 기존 거리가 더 짧으면 패스
            continue

        for node, weigth in graph[cur]:
            cost = dist + weigth
            if cost < dists[node]:
                dists[node] = cost
                heapq.heappush(q, [node, cost])
    print(dists[end])

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())
dijkstra(start, end)
    