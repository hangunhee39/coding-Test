R ,C = map(int, input().split())
graph = [[] for _ in range(R)]
for i in range(R):
    graph[i] = list(map(int, input().split()))
T = int(input())   

filter_img = []
j = []

for y in range(R-2):
    for x in range(C-2):
        for dy in range(3):
            for dx in range(3):
                ny = dy + y 
                nx = dx + x
                j.append(graph[ny][nx])
        filter_img.append(sorted(j)[4])
        j = []
        
print(sum(1 for i in filter_img if i >= T))