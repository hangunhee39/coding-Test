import heapq

def solution(book_time):
    answer = 0
    heap = []
    
    book_time = sorted(book_time)
    #book_time.sort(key = lambda x: x[0])
    
    def time_to_int (time):
        h, m = map(int, time.split(':'))
        return h*60 + m

    for s, e in book_time:
        start = time_to_int(s)
        end = time_to_int(e) + 10
        
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        
        heapq.heappush(heap, end)

        
    return answer