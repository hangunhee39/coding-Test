
def recur(idx, price) :
    global answer
    
    if (idx > n) :
        return
    elif (idx == n) :
        answer= max(answer, price)
        return
    
    # 한다
    recur(idx + listN[idx][0] , price + listN[idx][1])
    # 안한다
    recur(idx +1 , price)

answer = 0
n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)]
recur(0, 0)
print(answer)


# Top Down DP
def recur(idx):
    if idx == N: # 마지막 도착하면 끝
        return 0
    if idx > N: # 날짜 초과하면 무조건 못함
        return -99999999999
    if dp[idx] != -1 : #이미 저장상태이면 (Kick)
        return dp[idx]

    dp[idx] =max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx+1))
    return dp[idx] # 연결? -> max 에 비교할려면 필요함


N = int(input())
dp = [-1 for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(N)]

recur(0)
print(dp[0])


#DP bottomUp 점화식
N =  int(input())
interview = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

#뒤에서 부터 체우기
for idx in range(N)[::-1]:
    if idx + interview[idx][0] > N:
        dp[idx] = dp[idx+1] #범위보다 이상일때는, 퇴사일보다 더 일해야할때
    else :
        dp[idx] = max(dp[idx+interview[idx][0]]+interview[idx][1], dp[idx+1])
        
print(dp[0])
