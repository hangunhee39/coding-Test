# 그리디 , 우선순위 큐
# 우선 순위 큐를 사용해야 시간,공간 복잡도에서 통과
import heapq

N = int(input())

item = []
for _ in range(N) :
    _, start, end = map(int, input().split())
    item.append([start,end])

item.sort()
heap = []
# 끝나는 시간 
heapq.heappush(heap, item[0][1])

for i in range(1, N):
    # 다음(정렬됨) 수업 시작 < 겹치는 수업 중 가장 일찍 종료된는 수업
    if item[i][0] < heap[0] : #heap 은 작은게 항상 index: 0 이다
        heapq.heappush(heap, item[i][1])
    else : # 한 강의실 이어 쓰기 가능
        heapq.heappop(heap) # 앞으로 겹칠일 없으니 빼준다 (정렬되었기 때문)
        heapq.heappush(heap, item[i][1])

print(len(heap))