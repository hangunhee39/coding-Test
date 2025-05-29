#백트ㄹㅐ킹
dy = [[1,0],[0,1],[-1,0],[0,-1]] # ⌈ ⌉ ⌊ ⌋ 
dx = [[0,1],[-1,0],[0,1],[-1,0]]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def dfs(y, x, score):
    result = score

    if y == N:
        return result

    next_x = x + 1
    next_y = y
    if next_x == M:
        next_y = y + 1
        next_x = 0

    if visited[y][x] == 0:
        for i in range(4):
            ny1, ny2 = y + dy[i][0], y + dy[i][1]
            nx1, nx2 = x + dx[i][0], x + dx[i][1]
    
            if 0 <= ny1 < N and 0 <= ny2 < N and 0 <= nx1 < M and 0 <= nx2 < M:
                if visited[ny1][nx1] == 0 and visited[ny2][nx2] == 0:

                    # 방문
                    visited[ny1][nx1] = 1
                    visited[ny2][nx2] = 1
                    visited[y][x] = 1

                    result = max(result, dfs(next_y, next_x, score + graph[ny1][nx1] + 2* graph[y][x] + graph[ny2][nx2]))

                    # 방문 취소
                    visited[ny1][nx1] = 0
                    visited[ny2][nx2] = 0
                    visited[y][x] = 0
                    
    result = max(result, dfs(next_y, next_x, score))           
    return result
    
print(dfs(0,0,0))
            