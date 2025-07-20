def solution(n, times):
    start = min(times)
    end = max(times)*n
    
    while start <= end:
        mid = (start + end)//2
        count = 0
        
        for t in times :
            count += mid//t
            
            if count > n:
                break
        
        if count >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer