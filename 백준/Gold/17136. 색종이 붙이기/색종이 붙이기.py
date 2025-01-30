# 백트래킹, 브루트포스

graph = [list(map(int, input().split())) for _ in range(10)]
paper = [0,0,0,0,0,0]
answer = 26

#종이 붙이기/때기 (0/1)
def fill(y, x, size, attached) :
    for i in range(y, y + size) :
        for j in range(x, x + size) :
            graph[i][j] = attached

# 해당 사이즈가 들어가는지 확인
def check(y, x, size) :
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] == 0:
                return False
    return True
            
#백트래핑 방법
def recur(y, x, cnt) :
    global answer
    if x >= 10:
        recur(y+1, 0, cnt)
        return

    if y >= 10:
        answer = min(answer ,cnt)
        return

    if graph[y][x] == 1:
        for size in range(1,6):
            if paper[size] == 5:
                continue
            if y+size > 10 or x+size > 10 :
                continue
                
            if check(y,x,size):
                fill(y,x,size,0)
                paper[size] += 1
                recur(y, x+size, cnt+1)
                # 더 좋은 수가 있나 확인하기 위해 스티커 때기
                paper[size] -= 1
                fill(y,x,size,1)
    else :
        recur(y, x+1, cnt)

recur(0,0,0)
if answer == 26:
    print(-1)
else :
    print(answer)