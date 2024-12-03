
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