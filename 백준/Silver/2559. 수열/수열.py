# 누적함
# (컴퓨터에게 기억하는 방법 알려주기) -> 같은 연산 반복 안하게
# prefix  간격더하기


a, b = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(a+1)]

for i in range(a):
    prefix[i+1] = prefix[i] + arr[i]

answer = []

for j in range(b, a+1) :
    answer.append(prefix[j] - prefix[j-b])

print(max(answer))