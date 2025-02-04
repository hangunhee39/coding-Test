# bfs
from collections import deque

N, K = map(int, input().split())
waters = list(map(int, input().split()))

# 범위가 너무 커서 set 으로 대체
# 2. visited를 dict 으로 해서 key-위치, value-불행수 로 가능
visited = set()

q = deque()
for i in waters :
    q.append([i,0])
    visited.add(i)
    K += 1

answer = 0
while q:
    x, bad = q.popleft()
    K -= 1
    answer += bad
    # 집을 전부 배치하면
    if K == 0:
        break
    for dx in [-1,1]:
        nx = x + dx
        if nx in visited:
            continue
        visited.add(nx)
        q.append([nx, bad+1])

print(answer)