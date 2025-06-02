import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
graph = [[[0,0,0] for _ in range(N+1)] for _ in range(M+1)]
graph_sum = [[[0,0,0] for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
    arr = input().strip()
    for j in range(1,N+1):
        if arr[j-1] == 'J':
            graph[i][j][0] = 1
        elif arr[j-1] == 'I':
            graph[i][j][1] = 1
        else :
            graph[i][j][2] = 1

for i in range(1,M+1):
    for j in range(1,N+1):
        graph_sum[i][j][0] = graph_sum[i][j-1][0] + graph_sum[i-1][j][0] + graph[i][j][0] - graph_sum[i-1][j-1][0] 
        graph_sum[i][j][1] = graph_sum[i][j-1][1] + graph_sum[i-1][j][1] + graph[i][j][1] - graph_sum[i-1][j-1][1] 
        graph_sum[i][j][2] = graph_sum[i][j-1][2] + graph_sum[i-1][j][2] + graph[i][j][2] - graph_sum[i-1][j-1][2] 

for _ in range(K):
    a, b, c, d = map(int, input().split())
    j = graph_sum[c][d][0] - graph_sum[a-1][d][0] - graph_sum[c][b-1][0] + graph_sum[a-1][b-1][0]
    i = graph_sum[c][d][1] - graph_sum[a-1][d][1] - graph_sum[c][b-1][1] + graph_sum[a-1][b-1][1]
    o = graph_sum[c][d][2] - graph_sum[a-1][d][2] - graph_sum[c][b-1][2] + graph_sum[a-1][b-1][2]
    print(j, o, i)
        
    