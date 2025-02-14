# 1374 같은 문제 , 힙큐

import heapq

N = int(input())
item = []
for _ in range(N):
    start, end = map(int, input().split())
    item.append([start,end])

item.sort()
heap = []
heapq.heappush(heap, item[0][1])
for i in range(1,N) :
    if item[i][0] >= heap[0]:
        heapq.heappop(heap) # 끝 시간이 시작 시간 보다 빠르면 동시에 가능 
    heapq.heappush(heap, item[i][1])

# heap 에는 동시에 못하는 수업들만 남음
print(len(heap))
        
    
