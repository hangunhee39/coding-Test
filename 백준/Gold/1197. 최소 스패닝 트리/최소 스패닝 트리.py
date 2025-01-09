# MST 최소 스패닝 트리 (minimum spanning tree)
# 최소한(비용)으로 뻗어나가는 트리
 
# 프림 : 다익스트라 -> 트리(mst)
# 다익스트라를 이용해서, 방문한 곳인지 확인
# 1. 방문하면서 링크 정보를 저장 (한 리스)
# 2. 방문 한 곳은 다시 연결하지 않는다.

# 크루스칼 : 유니온파인드 -> 트리
# 1.일단 간 정보 전부 가져옴 (정렬해서)
# 2.find 한 후 같은 집합이 아니면 union


# 그래프를 트리(사이클x)로 바꾼다

# 프림 방식
import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [ 0 for _ in range(N+1)]

for _ in range(M) :
    A, B, C = map(int, input().split())

    graph[A].append([C,B])
    graph[B].append([C,A])

answer = 0

# 다익스트라 !

q = [[0,1]] # 가중치 0, 1에서 출발

while q :
    # 최소비요을 꺼냄 (리스트 앞에 있는 거 기준)
    weight,node = heapq.heappop(q)
    
    if visited[node] == 0:
        visited[node] = 1
        answer += weight

        for next in graph[node] :
            heapq.heappush(q, next)
        
print(answer)
#----------------------------------------------------------------------

#크루스칼

N, M = map(int, input().split())
link = [list(map(int, input().split())) for _ in range(M)]
link.sort(key = lambda x:x[2]) #가중치로 정렬

#유니온파인디
def _find(x) :
    while parent[x] != x: #루트가 나올때까지 반복
        x = parent[x]
    return x

def _union(a,b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a] :
        parent[b] = a
    else :
        parent[a] = b # 바꿔도 상관없음
        rank[b] += 1

parent = [i for i in range(1_000_001)]
rank = [0 for _ in range(1_000_001)]

answer = 0

for i in range(M) :
    a = link[i][0]
    b = link[i][1]
    weight = link[i][2]

    #같은 집합에 있는 지 확인
    a = _find(a) #부모
    b = _find(b) #부모
    if a == b:
        continue
    else :
        _union(a,b)
        answer += weight
        
print(answer)
        
    
