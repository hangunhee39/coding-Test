def solution(sequence, k):
    answer = []
    n = len(sequence)
    count = int(1e9)
    _sum = 0
    end = 0
    start = 0 
    
    
    while end < n:
        _sum += sequence[end]
        # _sum >= k 가 있는 이유 : 현재합이 k 보다 작아질때까지 빼야 하므로
        while _sum >= k and start <= end:
            if _sum == k :
                if end - start +1 < count:
                    count = end - start + 1
                    answer = [start, end]
            _sum -= sequence[start]
            start += 1
        end += 1
    
    return answer