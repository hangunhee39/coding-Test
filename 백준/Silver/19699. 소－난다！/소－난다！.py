# 에라토스테네스의 체
from itertools import combinations

N, M = map(int, input().split())
H = list(map(int, input().split()))
anser = set()

prime = [True] * 10000
for i in range(2, 10000):
    if prime[i]:
        for j in range(i*2, 10000, i):
            prime[j] = False

for bundle in combinations(range(N), M):
    t = 0
    for b in bundle:
        t += H[b]
    if prime[t]:
        anser.add(t)

if anser:
    print(*sorted(anser))
else :
    print(-1)
        