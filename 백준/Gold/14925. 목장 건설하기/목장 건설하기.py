# 누적합 , dp

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

# key point : 장애물에는 dp 도 0을 넣는다 (if 문에 걸림)
dp = [[0]*(N+1) for _ in range(M+1)]

for y in range(1,M+1):
    for x in range(1,N+1):
        if graph[y-1][x-1] == 0:
            # (가로,세로)중 작은 곳 + 1 하면 가장 큰 정사각형 구해짐
            dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1

print(max(map(max, dp)))
            