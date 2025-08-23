from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    def bfs(start) :
        visited = [0] * (n+1)
        q = deque()
        q.append(start)
        visited[start] = 1
        count = 1
        while q:
            cur = q.popleft()
            visited[cur] = 1
            count += 1
            for i in graph[cur]:
                if not visited[i]:
                    q.append(i)
        return count
    
    # 그래프 만들기
    for a, b in wires :
        graph[a].append(b)
        graph[b].append(a)
        
    # 선 끊고 최소 개수 세고 다시 연결
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer