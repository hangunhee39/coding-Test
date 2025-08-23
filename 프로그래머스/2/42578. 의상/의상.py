def solution(clothes):
    
    # 딕셔너리에 키에 리스트 저장
    # 종류 : list<아이템>
    dict = {}
    for v, k in clothes:
        if k in dict.keys():
            dict[k] += [v]
        else:
            dict[k] = [v]
    
    answer = 1
    for i in dict.values():
        answer *= (len(i) + 1)
    return answer - 1