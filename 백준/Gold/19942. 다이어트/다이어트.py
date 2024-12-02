
def recur(idx, A, B ,C, D, PRICE) :
    global answer, answer_idx
    
    if idx == n :
        if A >= a and B >=b and C>=c and D >= d :
            if answer > PRICE :
                answer = PRICE
                # 해당하는 값 인덱스 추출하기 
                answer_idx = [i + 1 for i in range(n) if selected[i]]    
            #예외 상황 처리
            elif answer == PRICE :
                current_idx = [i+1 for i in range(n) if selected[i]]
                # 사전 순 비교 예외조건 처리
                if current_idx < answer_idx :
                    answer_idx = current_idx

        return


    #사용한 경우
    selected[idx] = True
    recur(idx+1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], PRICE+ingre[idx][4])
    #안사용한 경우
    selected[idx] = False
    recur(idx+1, A, B, C, D, PRICE)
    

answer = 1000000001
answer_idx = []

n = int(input())
# 불변 객체여서 글로벌로 안해도 됨
selected = [False]*n

a, b, c, d = map(int,input().split())
ingre = [list(map(int, input().split())) for _ in range(n)]

recur(0,0,0,0,0,0)
if answer == 1000000001 : 
    print(-1)
else :
    print(answer)
    print(*answer_idx)