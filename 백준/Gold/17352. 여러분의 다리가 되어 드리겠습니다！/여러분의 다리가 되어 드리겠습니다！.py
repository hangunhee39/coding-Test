# 유니온 파인드 - 부모가 같은거 찾기
import sys
input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

def _union(a,b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return
        
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1

def _find(a):
    if parent[a] == a:
        return a
    else :
        parent[a] = _find(parent[a])
        return parent[a]

for i in range(N-2):
    a,b = map(int, input().split())
    _union(a,b)

for i in range(2, N + 1):
     if _find(1) != _find(i):
        print(1, i)
        exit()
    