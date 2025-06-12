N = int(input())

# [1칸 뛰었을때, 2칸 뛰었을때]
data = [[]] + [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
# [ 3칸 뛰기 사용 x , 3칸 뛰기 사용 o ] - 각 칸에 오는 최소의 값을 저장
# 1번이 초기 값이므로 0,0 을 넣은다
dp = [[0,0],[0,0]] + [[int(1e9), int(1e9)] for _ in range(N)]

for i in range(2, N+1):

    # 한칸 뛰기
    dp[i][0] = min(dp[i][0], dp[i-1][0] + data[i-1][0])
    dp[i][1] = min(dp[i][1], dp[i-1][1] + data[i-1][0])

    # 두칸 뛰기
    if i-2 >= 1:
        dp[i][0] = min(dp[i][0], dp[i-2][0] + data[i-2][1])
        dp[i][1] = min(dp[i][1], dp[i-2][1] + data[i-2][1])

    # 세칸 뛰기
    if i-3 >= 1:
        # dp[i-3][0] 에서 3칸 뛴 값만 비교하므로 세칸 뛴 횟수는 1 or 0 고정
        dp[i][1] = min(dp[i][1], dp[i-3][0] + K)

print(min(dp[N]))