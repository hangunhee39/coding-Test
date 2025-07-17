def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*(i)))
    
    for i in range(2,9): #1은 이미 있으니 2부터
        for j in range(1,i):
            
            # j번 변경한거와  j-i번 변경한것을 사칙연산하면 i 번 변경한게 된다.
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a-b)
                    dp[i].add(a+b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)
                        
        if number in dp[i]:
            return i
    
    return -1