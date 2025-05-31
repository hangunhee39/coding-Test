N = int(input())
arr = [[0,0]]
dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]

answer_grade = 1e9
answer_count = 0

for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(2):
        dp[i][j][0] = arr[i][j]
        if arr[i][j] in arr[i-1]:
            if arr[i][j] == arr[i-1][0]:
                dp[i][j][1] = dp[i-1][0][1]
            else :
                dp[i][j][1] = dp[i-1][1][1]
        dp[i][j][1] += 1 

        if answer_count < dp[i][j][1]:
            answer_count = dp[i][j][1]
            answer_grade = dp[i][j][0]
        elif answer_count == dp[i][j][1]:
            answer_grade = min(answer_grade, dp[i][j][0])

print(answer_count,answer_grade)
            