from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, graph) :
    q = deque()
    q.append([y,x])
    graph[y][x] = 0
    count = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < len(graph) and 0 <= nx < len(graph):
                if graph[ny][nx] == '1':
                    graph[ny][nx] = 0
                    q.append([ny, nx])
                    count += 1
    return count

N = int(input())
answer = []
graph = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            answer.append(bfs(i, j, graph))

answer.sort()
print(len(answer))
print(*answer, sep = '\n')
                    
                
        