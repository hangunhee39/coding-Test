N, Q = map(int, input().split())
arr = [int(input()) for _ in range(Q)]
visited = [0]*(N+1)

for current in arr:
    tmp = 0
    up = current
    
    while up >= 1:
        if visited[up] != 0:
            tmp = up
        up = up // 2

    if tmp == 0:
        visited[current] = 1
    print(tmp)