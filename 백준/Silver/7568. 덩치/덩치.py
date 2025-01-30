N = int(input())
arr = []
for _ in range(N) :
    X, Y = map(int, input().split())
    arr.append([X,Y])

for x,y in arr:
    answer = 1
    for p,q in arr:
        if p>x and q>y:
            answer += 1
    print(answer, end = " ")