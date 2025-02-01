# DP top down (메모리 초과)
# 배낭 문제 -2차원 배열 마이그래아션 방식 (실패)
import sys
sys.setrecursionlimit(10**6) 

D, P = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(P)]
# dp는 용량을 채운다
dp = [[-1 for _ in range(100_001)] for _ in range(P+1)]

def recur(idx, length) :
    if length >= D:
        # 길이가 맞을 때 아이템 값을 return
        if length == D:
            return item[idx-1][1] 
        return - 9999999
    if idx == P :
        return 0
    if dp[idx][length] != -1:
        return dp[idx][length]
        
    # 파이프를 쓰거나/안쓰거나 할 때 -> (전체 중) 최대값 !
    # 파이프를 쓰면 사용하는 파이프 중 최소값 !
    dp[idx][length] = max(min(recur(idx+1,length + item[idx][0]),item[idx][1]), recur(idx+1, length))
    
    return dp[idx][length]

recur(0,0)
print(dp[0][0])

#---------------------정답 ------------------------

D ,P = map(int, input().split())
# 길이 별 DP 테이블을 만든다 (해당 길이에 최대 용량을 가진)
dp = [0]*(D+1) 
dp[0] = 1e9

for _ in range(P):
    length, capacity = map(int, input().split())
    # 뒤에서 부터 채운다 (1.현재 길이를 뺀 dp 테이블, 2.현재 용량 중 작은 값을)
    # 뒤에서 부터 하는 이유 : 앞에서 부터 하면 이미 작업한 구분을 또 건둘 수도 있다 -> 앞에서 부터 하려면 copy 를 만들어서 해야함
    for i in range(D, length-1, -1):
        dp[i] = max(dp[i], min(capacity, dp[i-length]))


print(dp[D])
