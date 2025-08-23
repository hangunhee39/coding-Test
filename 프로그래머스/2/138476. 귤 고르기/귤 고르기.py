def solution(k, tangerine):
    dist = {}
    for i in tangerine :
        if i in dist :
            dist[i] += 1
        else :
            dist[i] = 1
    
    # 결과는 [(k, v),(k. v).. ] 형태로 리스트로 나옴
    sorted_dist = sorted(dist.items(), key = lambda x: x[1], reverse = True)
    
    answer = 0
    for _ , c in sorted_dist:
        k -= c
        answer += 1
        if k <= 0 :
            break
    
    return answer