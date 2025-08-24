def solution(s):
    stack = []
    #stack = set() set이 안되는 이유 순서 보장을 안해서 

    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    
    for i in s :
        spy = i.split(',')
        for j in spy :
            if not int(j) in stack :
                stack.append(int(j))
    return stack