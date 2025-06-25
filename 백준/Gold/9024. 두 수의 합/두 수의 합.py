t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    diff = int(1e9)
    
    start = 0
    end = n-1

    while start < end:
        cur = arr[start] + arr[end]
        cur_diff = abs(cur - k)

        if cur < k:
            start += 1
            
            if cur_diff == diff:
                answer += 1
            elif cur_diff < diff :
                answer = 1
                diff = cur_diff
            
        elif cur > k:
            end -= 1

            if cur_diff == diff:
                answer += 1
            elif cur_diff < diff :
                answer = 1
                diff = cur_diff
        else :
            if diff != cur_diff:
                answer = 0
            diff = cur_diff
            start += 1
            answer += 1
            
    print(answer)
        