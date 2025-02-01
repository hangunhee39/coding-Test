N, K = map(int, input().split())
visited = [False]*(N+1)
anser = 0

for i in range(2,N+1) :
    for j in range(i, N+1, i):
        if not visited[j]:
            answer = j
            visited[j] = True
            K -= 1
        # 조건에 맞을때 멈추기
        if K == 0:
            print(answer)
            exit()
            
            