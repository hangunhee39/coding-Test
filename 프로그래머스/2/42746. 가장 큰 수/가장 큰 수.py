def solution(numbers):
    arr = list(map(str, numbers))
    # 1000 미만 이여서 3번 곱하면 비교 가능 (문자 형태 일때)
    # 7 -> 777
    # 73 -> '737' 373
    # 730 -> '730' 730730
    arr.sort(key = lambda x: x*3, reverse = True)
    answer = str(int(''.join(arr)))
    
    return answer