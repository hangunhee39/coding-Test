# 그리디

N, L = map(int, input().split())
item = sorted(list(map(int, input().split())))

for i in item :
    if L >= i:
        L += 1
    else :
        break
print(L)
    
