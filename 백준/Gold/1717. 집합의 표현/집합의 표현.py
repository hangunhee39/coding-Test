# 유니온 파인드
# 두 노드, 두 숫자, 두 무엇가가 같은 집합안에 있나요? 를 찾는 문제

# 자기를 스스로 부모로 지정 -> 부모인것은 dp 에 담기
# 가장 위에 있는 조상을 파악 -> 이 친구들이 같은 조상인가?

#find 최적화 = 경로단축 
#union 최적화 = Union By Rank (랭크를 두고 합치기)

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

def _union(a,b) :
    a = _find(a)
    b = _find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] == b
    elif rank[a] > rank[a]:
        parent[b] == a
    else : 
        parent[b] = a # 반대로도 상관 없음
        rank[b] +=1
    

def _find(a) :
    if parent[a] == a:
        return a
    else :
        parent[a] = _find(parent[a]) #경로 단축
        return parent[a]



for _ in range(M) :
    X, A, B = map(int, input().split())

    if X == 0:
        _union(A, B)
    else :
        if _find(A) == _find(B):
            print("YES")
        else :
            print("NO")
        
        
    