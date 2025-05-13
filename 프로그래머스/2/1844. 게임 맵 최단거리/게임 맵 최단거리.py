from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x, maps, n, m):
    q = deque()
    q.append((y,x))
    
    while q :
        y, x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            elif maps[ny][nx] == 1 :
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))
                
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    bfs(0,0,maps,n,m)
    if maps[n-1][m-1] == 1 :
        return -1
    else :
        return maps[n-1][m-1]