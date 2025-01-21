#시뮬레이션

def roll(cmd): 
    if cmd == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] 
    elif cmd == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] 
    elif cmd == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] 
    elif cmd == 4: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] 

N, M, y, x, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
#동서북남 방향
dy = [0, 0, 0, -1, 1] 
dx = [0, 1, -1, 0, 0]

for i in cmd:
    if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
        y = y + dy[i]
        x = x + dx[i]
        roll(i)
        if graph[y][x] == 0: 
            graph[y][x] = dice[-1]
        else : 
            dice[-1] = graph[y][x]
            graph[y][x] = 0
        print(dice[0])
