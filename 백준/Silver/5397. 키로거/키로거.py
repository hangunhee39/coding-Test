# 스택, 큐

from collections import deque 
N = int(input())

for _ in range(N):
    # 큐
    buf = deque()
    # 스택
    answer = []
    s = deque(list(input()))
    for i in range(len(s)):
        c = s.popleft()
        if c == '>':
            if buf:
                obj = buf.popleft()
                answer.append(obj)
        elif c == '<' :
            if answer:
                obj = answer.pop()
                buf.appendleft(obj)
        elif c == '-' :
            if answer:
                answer.pop()
        else :
            answer.append(c)
    print(''.join(answer) + ''.join(buf))