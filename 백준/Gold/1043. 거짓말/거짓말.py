N, M = map(int, input().split())

parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

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
        return

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else :
        parent[b] = a
        rank[a] += 1
        
true_mans = list(map(int, input().split()))
partys = [list(map(int, input().split()))for _ in range(M)]
answer = 0

for i in range(2, len(true_mans)):
    _union(true_mans[1], true_mans[i])

for party in partys:
    for i in range(2, len(party)):
        _union(party[1], party[i])

if len(true_mans) == 1:
    print(len(partys))
    exit()
else :
    true_set = _find(true_mans[1])
    
for party in partys:
    if _find(party[1]) != true_set:
        answer += 1

print(answer)
        
    