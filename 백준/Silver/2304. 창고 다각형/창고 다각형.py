n = int(input())

g = [0]*1001
h_max = 0
index_max = 0

for i in range(n):
    w, h = map(int,input().split())
    g[w] = h
    #가장 큰 높이 저장
    if h_max < h:
        h_max = h
        index_max = w

answer = 0

#왼쪽 
current_height = 0
for left in range(1,index_max):
    if g[left] > current_height:
        current_height = g[left]
    answer += current_height

#오른쪽
current_height = 0
for right in range(1000,index_max,-1) :
    if g[right] > current_height:
        current_height = g[right]
    answer += current_height

print(answer+h_max)