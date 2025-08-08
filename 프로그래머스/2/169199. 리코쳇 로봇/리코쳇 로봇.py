from collections import deque
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def solution(board):
    H = len(board)
    W = len(board[0])
    
    def bfs(start_y, start_x) :
        q = deque()
        q.append([start_y, start_x, 0])
        visited = [[0 for _ in range(W)] for _ in range(H)]
        visited[start_y][start_x] = 1 #방문했던 곳을 알아야 무한루프 안걸림
        
        while q:
            y, x, c = q.popleft()
            if board[y][x] == 'G':
                return c
            
            for i in range(4):
                ny = y
                nx = x
                # D가 나올때까지 쭉 미끌어지기
                while 0 <= ny + dy[i] < H and 0 <= nx + dx[i] < W and board[ny + dy[i]][nx + dx[i]] != 'D' :
                    ny += dy[i]
                    nx += dx[i]
                
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny,nx,c+1]) # 카운터도 넣는게 kick
        return -1
    
    for y in range(H):
        for x in range(W):
            if board[y][x] == 'R' :
                return bfs(y,x)
    