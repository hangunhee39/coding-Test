N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

first = min(arr)
last = sum(arr)
answer = 0

while first <= last:
    mid = (first + last) // 2
    
    count = 1
    current = mid
    
    for day_cost in arr:
        if day_cost > current:
            count += 1
            current = mid
        current -= day_cost

    # 출금한 횟수가 작거나 하루 최고 지출보다 정답값이 작을 때는 정답값을 올린다.
    if count > M or mid < max(arr):
        first = mid + 1
    # 최소값을 구해야 한다.
    else : 
        last = mid - 1
        answer = mid

print(answer)   