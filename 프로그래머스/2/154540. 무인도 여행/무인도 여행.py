from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def solution(maps):
    maps = [list(row) for row in maps]
    
    answer = []
    len_y = len(maps)
    len_x = len(maps[0])
    
    def bfs(y, x):
        q = deque([[y, x]])
        tmp = int(maps[y][x])
        maps[y][x] = 'X'
        
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0 <= ny < len_y and 0 <= nx < len_x and maps[ny][nx] != 'X':
                    tmp += int(maps[ny][nx])
                    maps[ny][nx] = 'X'
                    q.append([ny, nx])
        answer.append(tmp)
    
    for y in range(len_y):
        for x in range(len_x):
            if maps[y][x] != 'X':
                bfs(y, x)

    if len(answer) == 0 :
        return [-1]
    else :
        return sorted(answer)
