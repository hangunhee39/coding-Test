W, H = map(int, input().split())
# dp[y값][x값]
# [0 - 계속 y축, 1 x축으로 오다가 이번에 y축, 2-계속 x축, 3 - x축으로 턴]
# 0,2 번은 계속 왔기 때문에 전에 꺽었는지 계속 왔는지를 더한다
# 1,3 번은 전에 꺽었지 때문에 계속 직진할 수 밖에 없다
dp = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]

# 1,3 번에 안 넣는 이유 어쩌피 전에껄 이어 받기 때문에
for y in range(1,H):
    dp[y][0][0] = 1
for x in range(1,W):
    dp[0][x][2] = 1
    
for y in range(1, H):
    for x in range(1, W):
        dp[y][x][0] = (dp[y-1][x][0] + dp[y-1][x][1]) % 100000 # 계속 위 (계속 위 + 저번에 턴)
        dp[y][x][1] = (dp[y-1][x][2])  # 이번에 위로 턴 (쭉 오른쪽으로 오던거랑 같음)
        dp[y][x][2] = (dp[y][x-1][2] + dp[y][x-1][3]) % 100000 # 계속 오른쪽 (계속 오른쪽 + 저번에 턴 )
        dp[y][x][3] = (dp[y][x-1][0])  # 이번에 오른쪽으로 턴 (쭉 위로 오던가랑 같음)
        
print(sum(dp[H-1][W-1]) % 100000)
    