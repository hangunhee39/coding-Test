from collections import deque

def solution(x, y, n):
    visited = set()
    q = deque()
    q.append([x,0])
    
    while q:
        curr, count = q.popleft()
        if curr == y :
            return count
        
        for i in [curr+n, curr*2, curr*3]:
            if i <= y and i not in visited:
                q.append([i, count+1])
                visited.add(i)
            
    
    return -1