
#use : 아무 재료를 사용안했을때 예외처리
def recur(idx, suger, salt, use) :
    global answer
    
    if idx == n :
        if use == 0 :
            return
        result = abs(suger - salt)
        answer = min(answer, result)
        return
    
    #경우 담기
    recur(idx+1, suger*ingre[idx][0], salt+ingre[idx][1], use + 1)
    #경우 안담기
    recur(idx+1, suger, salt, use)

n = int(input())

answer = 1000000001
ingre = [list(map(int, input().split())) for _ in range(n)]
recur(0,1,0,0)

print(answer)