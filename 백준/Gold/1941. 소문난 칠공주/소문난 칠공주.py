from collections import deque
import sys
input = sys.stdin.readline
    
graph = [list(input().strip()) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 7명 선택하기 DFS (백트래킹)
def dfs(start, count, Y_count):
    global answer
    if Y_count >= 4:
        return

    if count == 7:
        y = (start-1) // 5
        x = (start-1) % 5
        if bfs(y, x):
            answer += 1
        return

    # 1차원 배열로 한 이유 - 안 겹치게 하기 위해서
    for i in range(start, 25):
        y = i // 5
        x = i % 5

        visited[y][x] = 1
        if graph[y][x] == 'Y':
            dfs(i+1, count+1, Y_count+1)
        else:
            dfs(i+1, count+1, Y_count)
        visited[y][x] = 0

# 7명이 인접한지 확인 BFS
def bfs(y, x):
    checked = [[0]*5 for _ in range(5)]
    q = deque()
    q.append([y,x])
    checked[y][x] = 1
    count = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 5 and 0 <= nx < 5:
                if visited[ny][nx] == 1 and checked[ny][nx] == 0:
                    checked[ny][nx] = 1
                    count += 1
                    q.append([ny,nx])
    if count == 7:
        return True
    else:
        return False
        
dfs(0,0,0)
print(answer)
                
            
        