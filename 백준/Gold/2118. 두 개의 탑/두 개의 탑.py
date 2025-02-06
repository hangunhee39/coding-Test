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