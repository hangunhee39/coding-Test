# 정수론
# GCD 공약수
# GCD (A, B) -> GCD(B-A, A) -> GCD(A-(B-A), B-A) : 최대공약수 간격을 최소로 줄이자

#최대 공약수는 두 수를 나눳을때 나머지가 생기지 않는다

#갭을 줄인다 : 
#121 7
# 121 - 7- 7-7 -7-7  == 121 %7

# 라이브러리 사용
#import math
#a, b = 10, 15
#math.gcd(a, b) 

def _gcd(a,b) :
    while a % b != 0:
        tmp = a%b
        a =b
        b = tmp
    return b

def _lcm(a,b) :
     return a*b//_gcd(a,b)
 
def _ab(gcd, lcm):
    AxB = lcm * gcd  # A * B = LCM * GCD
    sum = float('inf')  # 최소 합 초기값
    result = (0, 0)  # 결과값 초기화

    # 약수 찾기
    for A in range(1, int(AxB**0.5) + 1):
        if AxB % A == 0:  # A가 AxB의 약수일 경우
            B = AxB // A  # B 계산

            if _gcd(A, B) == gcd:  # GCD 조건 확인
                if A + B < sum:  
                    sum = A + B
                    result = (A, B)

    return result

gcd, lcm = map(int, input().split()) 

print(*_ab(gcd, lcm))