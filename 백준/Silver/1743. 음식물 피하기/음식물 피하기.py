from collections import deque

N, M, K = map(int, input().split())
visited = [[0]*M for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def bfs(y, x):
    global answer
    tmp = 1
    q = deque()
    q.append([y, x])
    visited[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 1:
                    q.append([ny, nx])
                    visited[ny][nx] = 0
                    tmp += 1

    answer = max(answer, tmp)

for _ in range(K):
    r, c = map(int, input().split())
    visited[r-1][c-1] = 1
    
for y in range(N):
    for x in range(M):
        if visited[y][x] == 1:
            bfs(y, x)

print(answer)
    