#정수론
# 약수는 루트 씌운거에 밑에서만 찾으면 된다.

n = int(input())
arr = [int(x) for x in input().split()]
answer = 0

for i in arr:
    buf = set()
    for j in range(1,int(i**0.5)+1) :
        if i%j ==0:
            buf.add(j)
            buf.add(j//i)
            
    if len(buf) == 2:
        answer +=1
        
print(answer)