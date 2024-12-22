#Top Down DP

#더 필요하면 3,4 차원으로 만들기~
def recur(idx, weigth) :
    
    if weigth > B :
        return -9999999
    if idx == N :
        return 0 
    if dp[idx][weigth] != -1  :
        return dp[idx][weigth]
    
    dp[idx][weigth] = max(recur(idx+1, weigth + items[idx][0]) + items[idx][1], recur(idx+1 ,weigth))
    return dp[idx][weigth]

N, B =map(int, input().split())

items = [list(map(int,input().split())) for _ in range(N)]
#2차원 배열 y 는 무게
dp = [[-1 for _ in range(100_001)] for _ in range(N+1)]
    
recur(0,0)
print(dp[0][0])

#=======================================#
#점화식 bottomUp
N, B =map(int, input().split())

items = [list(map(int,input().split())) for _ in range(N)]
#2차원 배열 y 는 무게
dp = [[0]*(B+1) for _ in range(N+1)]
    
for idx in range(1, N+1) :
    for weight in range(1,B+1) :
        if weight < items[idx-1][0]: #최대 무게 보다 작으면 그래로 가져온다
            dp[idx][weight] = dp[idx-1][weight]
        else : 
            dp[idx][weight] = max(dp[idx-1][weight - items[idx-1][0]] + items[idx-1][1], dp[idx-1][weight])
print(dp[N][B])
