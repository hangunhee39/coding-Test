# 완전 탐색

# 1. 전체 가능한 조합에서 안좋은 조합 빼기
from math import factorial

N, M = map(int, input().split())
total = factorial(N) // (factorial(N-3) * factorial(3))
bad = set()

for _ in range(M) :
    A, B = map(int, input().split())
    for i in range(1, N+1):
        if i == A or i == B:
            continue
        bad.add(tuple(sorted([A,B,i])))
print(total - len(bad))

# 2. table을 만들어 가능 조합 더하기 (제일 빠름)
from itertools import combinations

N, M = map(int, input().split())
bad = [[False for _ in range(N+1)] for _ in range(N+1)]
answer = 0

for _ in range(M) :
    A, B = map(int, input().split())
    bad[A][B] = True
    bad[B][A] = True

for i in range(1, N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            if not bad[i][j] and not bad[j][k] and not bad[k][i] :
                answer += 1
print(answer)

# 3. table을 만들어 가능 조합 더하기 (+combinations 사용하기)
from itertools import combinations

N, M = map(int, input().split())
bad = [[False for _ in range(N+1)] for _ in range(N+1)]
answer = 0

for _ in range(M) :
    A, B = map(int, input().split())
    bad[A][B] = True
    bad[B][A] = True

for comb in combinations(range(1, N+1), 3) :
    if bad[comb[0]][comb[1]] or bad[comb[1]][comb[2]] or bad[comb[2]][comb[0]]:
        continue
    answer += 1
    
print(answer)
