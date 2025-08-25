def solution(order):
    answer = 0
    n = len(order)
    tmp = []
    idx = 0
    
    for i in range(1, n+1):
        tmp.append(i)
        while tmp :
            if tmp[-1] == order[idx]:
                answer += 1
                idx += 1
                tmp.pop()
            else :
                break
    
    return answer