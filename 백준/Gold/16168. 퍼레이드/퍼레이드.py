# 유니온 파인드, bfs
# 오일러 알고리즘 (한붓 긋기)
import sys
sys.setrecursionlimit(10**6)

def _union(A,B):
    A = _find(A)
    B = _find(B)

    if A == B:
        return
    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A] :
        par[B] = A
    else :
        par[A] = B
        rank[B] += 1

def _find(A) :
    if par[A] == A:
        return A
    else :
        par[A] = _find(par[A])
        return _find(par[A])
        
    

V, E = map(int, input().split())
par = [ i for i in range(V+1)] # 부모 확인
rank = [ 0 for _ in range(V+1)] # 높이 - 유니온 시간 단축용
edge = [ 0 for _ in range(V+1)] # 간선 

for _ in range(E):
    A,B = map(int, input().split())
    _union(A,B)
    edge[A] += 1
    edge[B] += 1

# 오일러 조건 
# 1.간선의 개수가 전부 짝수이거나
# 2. 딱 2개만 홀수이다
count = 0

# 모든 지점이 연결된 그래프이다
if all(par[1] == par[i] for i in range(1,V+1)):
    for e in edge:
        if e%2 == 1:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else :
        print("NO")
else :
    print("NO")
# 97퍼 실패 -> 이유를 모르겠음
