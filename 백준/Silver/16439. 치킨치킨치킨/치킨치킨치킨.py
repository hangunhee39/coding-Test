from itertools import combinations
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for a, b, c in combinations(range(M), 3):
    sum = 0
    for i in range(N):
        sum += max(arr[i][a], arr[i][b], arr[i][c])
    answer = max(answer, sum)
print(answer)