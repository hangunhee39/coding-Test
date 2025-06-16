from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
answer = int(1e9)

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            home.append([y,x])
        elif graph[y][x] == 2:
            chicken.append([y,x])

# M개 지점 선택 combinations
for chickens in combinations(chicken, M):
    tmp = 0
    for h_y, h_x in home:
        h_to_c = int(1e9) # 한 집에서 최소 거리 치킨집 
        for c_y, c_x in chickens:
            # 선택된 치킨집과 집까지 최소 거리 구하기
            h_to_c = min(h_to_c, abs(c_y - h_y) + abs(c_x - h_x))
        tmp += h_to_c
    answer = min(answer, tmp)

print(answer)
    