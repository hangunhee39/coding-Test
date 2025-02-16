# bfs 

from collections import deque

H, W = map(int, input().split())
graph = [[] for _ in range(H)]
q = deque() # 모래성이 없는 곳 (파도가 치는 곳)

for y in range(H):
    for item in list(input().strip()):
        # 모래성이 없는 곳을 큐에 담는다
        if item == '.':
            q.append([y,len(graph[y])])
            graph[y].append(0)
        else :
            graph[y].append(int(item))

direct = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
visited = [[0 for _ in range(W)] for _ in range(H)]

while q:
    y, x = q.popleft()
    for dy, dx in direct:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if graph[ny][nx] != 0:
                graph[ny][nx] -= 1 # 8 방향으로 파도를 쳐서
                if graph[ny][nx] == 0: # 모래성이 무너지면
                    q.append([ny,nx]) #새로운 파도가 치는 곳 생성
                    visited[ny][nx] = visited[y][x] +1 # 막타 친 곳에서 + 1
                                                       # 어짜피 건드린 곳 모두 같음

print(max(map(max, visited)))