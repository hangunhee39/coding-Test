# DP, 에라토스테네스의 체

import math

def is_prime(num) :
    for i in range(2, int(math.sqrt(num))+1) :
        if num % i == 0:
            return False
    return True

N = int(input())
prime_list = []
dp = [0 for _ in range(N+1)]

# dp 0은 소수로 뺏을때 딱 값가 맞았을 때!
dp[0] = 1

for i in range(2,N+1):
    if is_prime(i):
        prime_list.append(i)

# 소수 값들이 해당 값 이전 까지 개수를 적는다 
# (3,dp = 1) -> (4, dp[4](1) + dp[1] = 1) -> (5, dp[5](0) + 1) -> (8, dp[8]- dp[5](1))
# (5,dp = 1) -> (6, dp[6] + dp[1] = 0) -> (7, dp = 1) -> (8, dp = 3)
# (7,dp = 1) -> (8, dp[8](3) + dp[1](0) = 3)
for prime in prime_list:
    for i in range(prime, N+1):
        # 계속 쌓인다. 결과가
        dp[i] = (dp[i] + dp[i-prime]) % 123456789

print(dp[N])
    