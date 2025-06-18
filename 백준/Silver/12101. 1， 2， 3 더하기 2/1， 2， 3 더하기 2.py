from collections import deque

n, k = map(int, input().split())

q = deque()
answer = []

for i in range(1,4):
    q.append([i])
    while q:
        arr = q.popleft()
        total = sum(arr)

        if total > n:
            continue

        if total == n:
            answer.append(arr)
            continue

        for i in [1, 2, 3]:
            q.append(arr + [i])

answer.sort()
if k <= len(answer):
    print('+'.join(map(str, answer[k - 1])))
else:
    print(-1)