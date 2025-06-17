import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    x = int(input())

    # 힙은 원래 최소힙으로 정렬된다. 그래서 - 붙여서 최대 힙으로 정렬되게끔
    if x != 0:
        heapq.heappush(q, -x)
    else:
        if q:
            print(-heapq.heappop(q))
        else :
            print(0)
