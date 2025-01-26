
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M)]

dx = [0, -1, -1, 0 , 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
crossX = [-1, 1, -1, 1]
crossY = [-1, -1, 1, 1]

cloud = [[N-1, 0],[N-1, 1],[N-2, 0],[N-2, 1]]

for d, s in cmd :
    #구름 이동
    moved_cloud = []
    prev_cloud = [[False for _ in range(N)] for _ in range(N)]
    for y, x in cloud :
        ny = (y + dy[d] * s)% N # 끝이 연결 
        nx = (x + dx[d] * s)% N 
        moved_cloud.append([ny, nx])
        prev_cloud[ny][nx] = True
        graph[ny][nx] += 1 # 구름 위치에 1증가 
    
    #대각선 확인 후 물 증가
    for y, x in moved_cloud :
        cross_count = 0
        for i in range(4) :
             ny = y + crossY[i]
             nx = x + crossX[i]
             if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] > 0 :
                       cross_count += 1
        graph[y][x] += cross_count
    
    # 새로운 구룸 찾기 (물이 2 이상)
    new_cloud = []
    for y in range(N) :
        for x in range(N) :
            if graph[y][x] >= 2 and not prev_cloud[y][x]:
                new_cloud.append([y, x])
                graph[y][x] -= 2
    cloud = new_cloud

print(sum(map(sum, graph)))