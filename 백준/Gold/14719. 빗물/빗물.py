h, w = map(int, input().split())

g = list(map(int,input().split()))

#가장 높은 값 정보
h_max = max(g)
index_max = g.index(h_max)

answer = 0

current_max = 0
for i in range(0,index_max):
    if g[i] > current_max:
        current_max = g[i]
    answer += current_max-g[i]
    
current_max = 0
for j in range(w-1,index_max,-1):
    if g[j] > current_max:
        current_max = g[j]
    answer += current_max-g[j]

print(answer)