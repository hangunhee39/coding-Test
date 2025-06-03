from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
answer = -1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            q.append([y,x])

bfs()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(-1)
            exit()
        else:
            answer = max(answer, graph[y][x])

print(answer-1)