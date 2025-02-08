# 투 포인터, 슬라이싱 윈도
from collections import deque
import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
item = []
for i in range(N) :
    item.append(int(input()))

q = deque()
q.extend(item[:k])
answer = 0
for i in range(N):
     # 회전 초밥이기 때문에
    q.popleft()
    q.append(item[(i+k)%N])
    if c in q :
        answer = max(answer , len(set(q)))
    else :
        answer = max(answer , len(set(q)) + 1)

print(answer)