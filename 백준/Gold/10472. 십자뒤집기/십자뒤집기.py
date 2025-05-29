P = int(input())
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1] 

def bfs(y, x, graph):
    result = int(1e9)

    # 다 돌았을때 검정색이 있으면 무한대 리턴
    if y == 3:
        for i in range(3):
            for j in range(3):
                if graph[i][j] == '*':
                    return int(1e9)
        return 0

    #brute force 로 전 구간 탐색
    nx = x+1
    ny = y
    if nx == 3:
        nx = 0
        ny = y+1
        
    paint(y, x, graph) # 칠하고
    result = min(result, bfs(ny, nx, graph)+1) 
    paint(y, x, graph) # 되돌리기
    result = min(result, bfs(ny, nx, graph))

    return result

def paint(y, x, graph):
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < 3 and 0 <= nx < 3:
            if graph[ny][nx] == '*':
                graph[ny][nx] = '.'
            else :
                graph[ny][nx] = '*'

for _ in range(P):
    graph = [list(input().strip()) for _ in range(3)]
    answer = bfs(0, 0, graph)
    print(answer)
    