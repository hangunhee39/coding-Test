
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
        
    