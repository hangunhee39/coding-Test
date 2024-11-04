#완전탐색
#소인수분해가 안돼는 것을 찾는다
n = int(input())
for _ in range(n):
    num = int(input())

    for i in range(2,1_000_001):
        if num%i ==0 :
            print("NO")
            break
        if i == 1_000_000 :
            print("YES")