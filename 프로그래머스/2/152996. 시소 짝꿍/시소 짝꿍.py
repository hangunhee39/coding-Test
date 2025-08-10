from collections import Counter

def solution(weights):
    answer = 0
    
    weight_count = Counter(weights)
    for k, v in weight_count.items():
        if v > 1:
            answer += v*(v-1)//2
    weights = set(weights)
    
    for weight in weights:
        for i in [2, 3/2, 4/3]:
            if weight * i in weights:
                answer += weight_count[weight] * weight_count[weight*i]
    
    return answer