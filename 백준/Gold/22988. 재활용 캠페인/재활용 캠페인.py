#two pointer : 가능성을 지워주는 것 (가능성 없는 것 삭제)
# 정렬  -> two point

# ex) 13이면 
# 1. (한 개) 최대 용량보다 크거나 같으면 + 1
# 2. (두 개) 합쳐서 6.5 이상이면 + 1
# -> 6.5 에 가깝게 합치면 좋다
# 3. 만약에 조건에 맞지 않다면 짜투리로 넣어 줌 (+ 투포인터가 만나도 짜투리)
# 4. 짜투리는 0이 3개여도 무조건 +1 (3으로 나눴을 때 몫)
# ex) 0 + 0 + 6.5 = 6.5 , 6.5 + 0 = 13 

N, X =map(int, input().split())
items = sorted(list(map(int, input().split())))

s = 0
e = N-1

cnt = 0
remain = 0

#교차하면 멈춘다
while s <= e :  
    if items[e] == X :
        cnt += 1
        e -= 1
        continue
    
    if s == e :
        remain += 1
        break
    
    if items[e] + items[s] >= X/2 :
        cnt += 1
        s += 1
        e -= 1
    else :
        s += 1 # start 증가 -> 수가 커짐
        remain += 1
        
print(cnt + remain//3)