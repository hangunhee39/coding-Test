N, M = map(int, input().split())
rank = [0] * (N+1)
parent = [ i for i in range(N+1)]
answer = 0
graph = [ list(map(int, input().split())) for _ in range(M)]
graph.sort(key = lambda x:x[2])
max_sum = sum(row[2] for row in graph)
count = 0

def _find(a):
    if a == parent[a]:
        return a
    else :
        parent[a] = _find(parent[a])
        return parent[a]

def _union(a, b):
    a = _find(a)
    b = _find(b)
    
    if a == b:
        return False

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1 
    return True

for i in range(M) :
    a = graph[i][0]
    b = graph[i][1]
    weight = graph[i][2]

    #같은 집합에 있는 지 확인
    a = _find(a) 
    b = _find(b)
    if a == b:
        continue
    else :
        if _union(a,b):
            count += 1
        answer += weight

if count == N-1:
    print(max_sum - answer)
else :
    print(-1)