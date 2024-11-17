# 정수론
# 펙토리얼 을 구해서 B - A = answer
# 약수 구하는 법 -> 2의 배수로 나누기 ex) 8
# 8
# 8 + 4:(1*4)
# 8 + 4:(2*2)
# 8 + 4:(4*1)

a, b = map(int, input().split())
a -= 1

tmp_a = 0
tmp_b = 0
tmp_a += a
tmp_b += b
for i in range(1, 99): #그냥 많은 수 반복
    tmp_a += (a//(2**i))*((2**i)-(2**(i-1)))
    tmp_b += (b//(2**i))*((2**i)-(2**(i-1)))
    
print(tmp_b-tmp_a)