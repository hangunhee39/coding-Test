#  X, Y 따로 해서 더하기 
# 모든 곳에 생각 -> 
# 한명의 집에서 모이는게 무조건 짧다 ->
# 4명의 거리를 구한 뒤에 가까운 순서대로 더해주기

n = int(input())
arr = []
arr_y = []
arr_x = []
answer = [-1]*n

for _ in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
    arr_x.append(a)
    arr_y.append(b)

# 15 14 3 1
# 15 16 3 4
# 14 15 1 3
# 16 15 4 3
for y in arr_y: 
    for x in arr_x:
        dist = []

        for ex,ey in arr:
            d = abs(ex-x) + abs(ey-y) # 무조건 자기가 있는 점이 있음
            dist.append(d)


        dist.sort()

        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1 :
                answer[i] = tmp
            else :
                answer[i] = min(tmp, answer[i])

print(*answer)