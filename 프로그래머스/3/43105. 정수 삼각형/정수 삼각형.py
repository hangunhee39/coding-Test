def solution(triangle):
    l = len(triangle) - 1
    
    # 아래 -> 위, 로 해야 밑이 더 많아서 비교 편하다
    while l > 0:
        for i in range(l):
            triangle[l-1][i] += max(triangle[l][i], triangle[l][i+1])
        l -= 1
    print(triangle[0][0])
    return triangle[0][0]