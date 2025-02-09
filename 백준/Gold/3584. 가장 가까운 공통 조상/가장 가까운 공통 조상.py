# 그래프 탐색

import sys
sys.setrecursionlimit(10**6)
T = int(input())

def _find(A, par, ancestor) :
    if par[A] == A :
        return
    else :
        ancestor.append(par[A])
        _find(par[A], par, ancestor)
        

for _ in range(T):
    N =  int(input())
    par = [ 0 for i in range(N+1)]
    parA = []
    parB = []
    for i in range(N):
        A, B = map(int, input().split())

        # 부모 리스트 뽑기 (A,B)
        if i == N-1:
            parA.append(A)
            parB.append(B)
            _find(A, par, parA)
            _find(B, par, parB)
            for p in parA:
                if p in parB:
                    print(p)
                    break
        else :
            # 부모 리스트에 넣기
            par[B] = A
                    
