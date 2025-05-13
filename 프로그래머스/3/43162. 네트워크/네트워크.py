from collections import deque 

def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    
    def bfs(c) :
        visited[c] = True
        q = deque()
        q.append(c)
        
        while q :
            current = q.popleft()
            for i in range(n) :
                if computers[current][i] == 1 and not visited[i] :
                    q.append(i)
                    visited[i] = True
    
    for j in range(n) :
        if not visited[j] :
            bfs(j)
            answer += 1
            
    return answer