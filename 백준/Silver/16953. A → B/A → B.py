from collections import deque

A, B = map(int, input().split())
q = deque()
q.append([A, 1])

while q:
    num, count = q.popleft()

    if num > B:
        continue
    
    if num == B:
        print(count)
        exit()

    q.append([num*2, count+1])
    q.append([num*10+1, count+1])

print(-1)
        
    