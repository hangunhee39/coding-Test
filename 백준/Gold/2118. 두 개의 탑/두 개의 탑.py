# 누적합, 투포인트
from itertools import accumulate

N = int(input())
item = [ int(input()) for _ in range(N)]
prefix = [0] + list(accumulate(item))

total = prefix[-1]
start = 0 
end = 0
answer = 0

while start < N and end < N :
    #시계 방향 , 반시계 방향 비교해서 작은 길이
    length = min(prefix[end] - prefix[start], total + prefix[start] - prefix[end] )
    #현재 정답보다 길면 바꾸기
    answer = max(answer, length)
    
    # 반 시계 부분이 더 작아지면 start 를 +1 시킨다, 왜냐하면 조건문은 무조건 커짐
    # 길이는 최소값 중 최대값을 구하는 것 이므로 (min에서 작아짐)
    if prefix[end] - prefix[start] >= total + prefix[start] - prefix[end]:
        start += 1
    else :
        end += 1

print(answer)

# 누적합, 투포인터, 이진탐색

N = int(input())
item = [0] * N 
prefix = [0] * (N+1)   
for i in range(N):
    item[i] = int(input())
    prefix[i+1] = prefix[i] + item[i]
 
total = prefix[-1]   
 
answer = 0

# item 을 하나씩 돌가면서 완전 탐색
for i in range(1, N+1):
    start, end = i, N
    
    # 이진탐색
    while start <= end:
        mid = (start+end) // 2
        
        # i 부터 mid 까지 길이(시계 반향)가 더 크면 mid 를 줄인다 (start 옮겨서) 
        # 시계 방향 길이 + 반 시계 방향 길이 = total 
        length1 = prefix[mid] - prefix[i-1]
        length2 = total - length1
        if length1 < length2:
            start = mid + 1
        else:
            end = mid - 1
        answer = max(answer, min(length1, length2))
print(answer)
