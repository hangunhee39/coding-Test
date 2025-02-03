# BFS 
from collections import deque 

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

monkey = [[-1,0],[0,1],[1,0],[0,-1]]
horse = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs():
    # 횟수 저장 -> [Y좌표][X좌표][K개수]
    count = [[[-1]*(K+1) for _ in range(W)]for _ in range(H)]
    q = deque()
    q.append([0,0,K])
    while q :
        y, x, k = q.popleft()
        if y == H-1 and x == W-1:
            return count[y][x][k]+1
        if k > 0:
            for dy, dx in horse:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and graph[ny][nx] == 0 and count[ny][nx][k] == -1:
                    q.append([ny, nx , k-1])
                    count[ny][nx][k-1] = count[y][x][k] + 1

        for dy, dx in monkey:
            ny = y + dy 
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and graph[ny][nx] == 0 and count[ny][nx][k] == -1:
                q.append([ny, nx, k])
                count[ny][nx][k] = count[y][x][k] + 1         
    return -1
print(bfs())
