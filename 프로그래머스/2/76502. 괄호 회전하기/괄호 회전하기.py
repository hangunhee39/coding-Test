def solution(s):
    def _check():
        stack = [s[0]]
        for i in s[1:]:
            if not stack : stack.append(i)
            else :
                if i == ")" and stack[-1] == "(": stack.pop()
                elif i == "]" and stack[-1] == "[": stack.pop()
                elif i == "}" and stack[-1] == "{": stack.pop()
                else: stack.append(i)
        return len(stack) == 0
    
    answer = 0
    for i in range(len(s)):
        if _check() :
            answer += 1
        s = s[1:] + s[0]
    return answer