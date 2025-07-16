def solution(number, k):
    stack = []
    
    for i in number:
        # 새로 들어오는 것 보다 작은게 바로 밑에 있으면 빼준다 (순서 중요)
        while stack and i > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    
    while k > 0:
        stack.pop()
        k -= 1
                
    answer = "".join(stack)
    return answer