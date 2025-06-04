N = int(input())
graph = [list(input().strip()) for _ in range(N)]
graph_count = [[1e9]*N for _ in range(N)]
answer = 0

def floid() :
    for i in range(N): # 중간에 거쳐 가는 경우
        for y in range(N):
            for x in range(N):
                if i == y or y == x or x == i:
                    continue
                else:
                    graph_count[y][x] = min(graph_count[y][x], graph_count[y][i] + graph_count[i][x])

                    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'Y':
            graph_count[i][j] = 1

floid()

for i in range(N):
    tmp = 0
    for j in range(N):
        if graph_count[i][j] <= 2:
            tmp += 1
    answer = max(answer, tmp)
    
print(answer)