N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = int(1e9)

# 팀을 나눈 모든 경우의 수에서 체크 가능 (백트레킹이 마지막까지 갔으므로)
def last():
    global answer
    team1, team2 = 0, 0

    # 브루트포스, 팀을 나눈 상태에서 차이 최소 값 계산
    for i in range(N):
        for j in range(N):
            if visited[i] == 0 and visited[j] == 0:
                team1 += graph[i][j]
            elif visited[i] != 0 and visited[j] != 0:
                team2 += graph[i][j]
                
    answer = min(answer, abs(team1 - team2))

# 백트레킹
def dfs(curent):
    if curent == N:
        last()
        return

    next = curent+1
    
    dfs(next)
    visited[curent] = 1
    dfs(next)
    visited[curent] = 0

dfs(0)
print(answer)