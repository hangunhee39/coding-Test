# 2. table을 만들어 가능 조합 더하기
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