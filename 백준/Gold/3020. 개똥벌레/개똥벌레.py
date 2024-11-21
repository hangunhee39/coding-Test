import sys
input = sys.stdin.readline

w, h = map(int, input().split())

g = [0]*h

# 벽 시작을 +1 벽 끝나고 한칸 뒤를 -1 로 준다 (종류석은 뒤가 없음)
for i in range(1, w+1) :
    wall = int(input())
    # 종류석
    if i%2 == 0:
        g[h-wall] += 1
    # 석순
    else :
        g[0] += 1
        g[wall] -=1
        
low = 500001
count = 0
prefix = [0]*(h+1)

for j in range(1,h+1) :
    #누적합
    prefix[j] = prefix[j-1] + g[j-1]

    #최소값 갱신
    if low > prefix[j]:
        low = prefix[j]
        count = 1
    # 벽에 막히는 수가 같으면 카운트 +
    elif low == prefix[j] :
        count += 1
        
print(low, count)