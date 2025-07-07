T = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1

def f(n):
    if n ==0:
        return 0
    
    if dp[n] == 0:
        dp[n] = f(n-3) + f(n-2)
        
    return dp[n]
    
for _ in range(T):
    x = int(input())
    print(f(x))
    
        
    
    