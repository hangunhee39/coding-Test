N, M = map(int, input().split())
item = [list(map(int, input().split()[1:])) for _ in range(N)]
count = [0]*(M+1)

for arr in item :
    for c in arr:
        count[c] += 1

for arr in item :
    isAll2 = True
    for c in arr :
        if count[c] == 1:
            isAll2 = False
            break
    if isAll2:
        print(1)
        exit()
print(0)