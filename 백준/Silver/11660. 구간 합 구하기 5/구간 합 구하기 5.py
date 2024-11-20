# 2차원 누적합

n,m = map(int,input().split())
graph =[list(map(int, input().split())) for _ in range(n)]

queries = [list(map(int, input().split())) for _ in range(m)]

prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for y in range(n):
    for x in range(n):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] -prefix[y][x]+ graph[y][x]


for y1, x1, y2, x2 in queries:
    answer = prefix[y2][x2] - prefix[y2][x1-1] - prefix[y1-1][x2] + prefix[y1-1][x1-1]
    print( answer)