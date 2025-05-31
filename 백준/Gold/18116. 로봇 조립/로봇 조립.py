import sys

N = int(input())
input = sys.stdin.readline

parent = [i for i in range(10**6 + 1)]
rank = [1 for _ in range(10**6 + 1)]

def _union(a,b):
    a = _find(a)
    b = _find(b)
    if a == b:
        return

    if rank[a] < rank[b]:
        parent[a] = b
        rank[b] += rank[a]
    else :
        parent[b] = a
        rank[a] += rank[b]

def _find(a):
    if a == parent[a]:
        return a
    else :
        parent[a] = _find(parent[a])
        return parent[a]

for _ in range(N):
    arr = input().split()
    if arr[0] == 'I':
        _union(int(arr[1]), int(arr[2]))
    else :
        print(rank[_find(int(arr[1]))])
        
    
    