# 유니온 파인드
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
par = [ i for i in range(N)]
h = [0] * N

def _union(A, B) :
    A = _find(A)
    B = _find(B)

    #먼저 조상이 겹치는지 확인
    if A == B:
        return True
        
    if h[A] < h[B]:
        par[A] = B
    elif h[B] < h[A] :
        par[B] = A
    else :
        par[A] = B
        h[B] += 1
    return False
    
def _find(A):
    if par[A] == A:
        return A
    else :
        par[A] = _find(par[A])
        return par[A]
        
for i in range(M):
    A, B = map(int, input().split())
    # 조상이 겹치면
    if _union(A,B) :
        print(i+1)
        exit()
    
print(0)
        
