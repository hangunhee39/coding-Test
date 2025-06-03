R, C, N = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

def bom(graph):
    tmp =  [["O" for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if graph[y][x] == 'O':
                for i in range(5):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if 0 <= ny < R and 0 <= nx < C:
                        tmp[ny][nx] = '.'
    return tmp

if N == 1 :
    for row in graph:
        print("".join(row))    
elif N % 2 == 0:
    for row in range(R):
        print('O'*C)
elif N % 4 == 3:
    answer = bom(graph)
    for row in answer:
        print("".join(row))
elif N % 4 == 1:
    answer = bom(bom(graph))
    for row in answer:
        print("".join(row))
        
    
