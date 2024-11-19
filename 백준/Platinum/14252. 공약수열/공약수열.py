# 정수론, 완전 탐핵
# GCD 공약수
# GCD (A, B) -> GCD(B-A, A) -> GCD(A-(B-A), B-A) : 최대공약수 간격을 최소로 줄이자

# 두 수를 비교해서 최대공약수가 1이라면 ok 아니면 Nok

# 숫자를 1개 추가하거나
# 만약에 한개 추가해서 양 옆에 맞는 공약수를 추가할 수 없다면 2개 추가

# input
# 4
# 2200 42 2184 17

# output
# 3

# 42 부터 2184 까지 완전탐핵
import math

def _gcd(a,b) :
    while a%b != 0:
        tmp = a%b
        a =b
        b = tmp
    return b

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answerList= []
answer = 0

for i in range(0, n-1):
    if(math.gcd(arr[i], arr[i+1])==1) : # 두 수가 로 공약수인지 확인
        continue
    for j in range(arr[i], arr[i+1]):
        if math.gcd(arr[i], j) == 1:
            if math.gcd(arr[i+1], j) == 1:
                answer += 1
                answerList.append(j)
                break  # 공약수가 없음
        if j == arr[i+1]-1:
            answerList.append(j)
            answer += 2 # 공약수가 없으면 2개가 필요함

print(answer)
#print(answerList)