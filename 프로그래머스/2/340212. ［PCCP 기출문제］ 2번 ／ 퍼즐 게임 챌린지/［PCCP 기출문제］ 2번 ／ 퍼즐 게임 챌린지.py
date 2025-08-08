def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    
    answer = end
    
    while start <= end :
        mid = (start + end)//2
        tmp = times[0]
        
        for i in range(1, len(times)):
            if mid >= diffs[i]:
                tmp += times[i]
            else :
                tmp += (times[i] + times[i-1])*(diffs[i]-mid) + times[i]

        if limit >= tmp:
            answer = mid
            end = mid - 1
        else :
            start = mid + 1
    
    return answer