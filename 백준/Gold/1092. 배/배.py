# 그리드

N = int(input())
limit = sorted(list(map(int, input().split())), reverse=True) 
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)  
answer = 0

# 크레인으로 가장 무거운 박스를 옮길 수 없는 경우
if limit[0] < box[0]:
    print(-1)
    exit()
    
while box:
    answer += 1  
    # limit값이 한바퀴 돌면 1 초 증가
    for l in limit:  
        # 옮길 수 있는 박스가 있으면 큐에서 뺀다 (정렬된 상태에서)
        for b in box :
            if l >= b: 
                box.remove(b)
                break

print(answer)