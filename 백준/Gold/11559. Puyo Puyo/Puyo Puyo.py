from collections import deque

graph = [list(input().strip()) for _ in range(12)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
answer = 0

# 역순으로 밑 부터 채우기 (중요 kick)
def down():
    for x in range(6):
        for y_top in range(10,-1,-1):
            for y_bot in range(11,y_top,-1):
                if graph[y_bot][x] == '.' and graph[y_top][x] != '.':
                    graph[y_bot][x] = graph[y_top][x]
                    graph[y_top][x] = '.'
                    
def delete(sames):
    for y, x in sames:
        graph[y][x] = '.'

# 시작 블록과 인접한 같은 블록만 return 
def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    sames = [[y,x]]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < 6 and 0<= ny < 12:
                if graph[ny][nx] == graph[y][x] and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    sames.append([ny, nx])
    return sames

while True:
    puyo = False
    visited = [[0]*6 for _ in range(12)]

    for y in range(12):
        for x in range(6):
            if visited[y][x] == 0 and graph[y][x] != '.':
                sames = bfs(y, x)

                if len(sames) >= 4:
                    puyo = True
                    delete(sames)
    if puyo:
        down()
        answer += 1
    else:
        print(answer)
        exit()
        
    