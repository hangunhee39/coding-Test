def solution(sizes):
    h = []
    w = []
    
    # 큰 걸 w 로 저장
    for card in sizes:
        h.append(min(card))
        w.append(max(card))
    
    answer = max(h) * max(w) 
    return answer