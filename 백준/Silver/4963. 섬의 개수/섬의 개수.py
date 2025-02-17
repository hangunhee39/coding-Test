# BFS, 완전

from collections import deque

direct = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

while True:
    W, H = map(int, input().split())
    if H == 0 and W == 0:
        break
        
    graph = [list(map(int, input().split())) for _ in range(H)]
    q = deque()
    answer = 0

    # 완전 탐색 but 섬인 것에서만 bfs 탐색 시작
    for y in range(H):
        for x in range(W):
            if graph[y][x] == 1:
                q.append([y,x])
                graph[y][x] = 0
                while q:
                    cy ,cx = q.popleft()
                    for dy, dx in direct:
                        ny = dy + cy
                        nx = dx + cx
                        if 0<= nx < W and 0<= ny < H and graph[ny][nx] == 1:
                            q.append([ny,nx])
                            graph[ny][nx] = 0 # key : 방문한 섬은 지운다
                answer += 1 #완전 탐색 중 섬에서 시직하여 더 이상 이어진 섬이 없으면 +1 
    print(answer)
                    
    