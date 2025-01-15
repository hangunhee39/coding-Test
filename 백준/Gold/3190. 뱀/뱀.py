from collections import deque

N = int(input())
K = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    Y, X = map(int, input().split())
    graph[Y][X] = 1
    
L = int(input())
directs = {}
for _ in range(L):
    time , direct = input().split()
    directs[int(time)] = direct

#시계방향 순 저장, 왜지
current_direct = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append([1,1])

x, y = 1, 1
time = 0

while 1: 
    nx = x + dx[current_direct]
    ny = y + dy[current_direct]
    time += 1
    
    #필드 내 확인
    if 1 <= nx <= N and 1 <= ny <= N:
         #뱀 몸에 만남
        if [ny,nx] in q:
            break
            
        #사과 먹기
        if graph[ny][nx] == 1 :
            graph[ny][nx] = 0
        else :
            q.popleft()
            
        q.append([ny,nx])
        x = nx
        y = ny

        #방향 전환
        if time in directs.keys():
            if directs[time] == 'L':
                if current_direct == 0 :
                    current_direct = 3
                else :
                    current_direct = current_direct -1
            else :
                current_direct = (current_direct + 1)%4
    else :
        break
        
print(time)