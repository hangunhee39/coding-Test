def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [] # 인덱스를 넣어서 비교
               # 다음 큰 수 이므로 인덱스 비교해야함
    
    for index in range(n):
        current = numbers[index]
        # 스택에 마지막을 반복 비교해야함 (스택에 없으면 다음 큰 수가 이미 있는 상태임)
        while stack and numbers[stack[-1]] < current:
            answer[stack.pop()] = current
        stack.append(index)
    return answer