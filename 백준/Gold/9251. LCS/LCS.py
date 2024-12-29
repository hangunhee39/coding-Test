#LCS (well-know)
# 맨 뒤 문자를 계속~ 비교하기 
# 같다면 둘 다 빼고 +1
# 틀리면 둘 중 하나 없애고 계속 비교

# 뒤에만 비교하면 앞에는 어떤 수여도 상관없음 -> 코드에서는 앞에서 부터 가능
# -> 코드에서는 앞에서 부터 시작하긴 함 -> 완전탐색 사용 -> dp

M = list(str(input()))
N = list(str(input()))

dp = [[0 for _ in range(len(N)+1)]for _ in range(len(M)+1)]

for y in range(1, len(M)+1):
    for x in range(1, len(N) +1):
        if M[y-1] == N[x-1] :
            dp[y][x] =dp[y-1][x-1]+1
        else : # 둘 중 하나 지웠을 때 큰 값
            dp[y][x] =max(dp[y-1][x], dp[y][x-1])

print(dp[len(M)][len(N)])

            